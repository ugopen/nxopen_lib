//
//         Copyright 2010 Siemens Product Lifecycle Management Software Inc.
//                          All Rights Reserved.
//
//====================================================================================================
//
//====================================================================================================
//
package nxopen.examples.assemblies;
import java.io.PrintStream;
import java.rmi.RemoteException;
import java.util.Collection;
import java.util.Iterator;

import utils.AssemblyListingWindowOutputStream;

import nxopen.NXException;
import nxopen.Part;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.assemblies.Component;
import nxopen.assemblies.ComponentAssembly;

/*
 * Created on Feb 24, 2005
 * 
 * Copyright (c) 2005 UGS Corp. 
 *   All Rights Reserved.
 * 
 */

/**
 * @author pesumner
 * Walks through the components of an assembly and performs an operation on each component.
 * You can customize this program to change the operation that it performs on each
 * component by changing the IComponentFunctor passed into the walk method.
 *
 */
public class AssemblyListing {
    
    private static PrintStream out;

    public static void main(String[] args) {
        try {
            Session theSession = (Session)SessionFactory.get("Session");
            out = new PrintStream(new AssemblyListingWindowOutputStream(theSession.listingWindow()));
            
            if((args.length == 1 && args[0].equals("")))
            {
                //No arguments were passed. So skip checking for arguments.
            }
            else
            {
                if ( args.length > 0 ) {
                    if ( args[0].equals("-p") ) {
                        theSession.parts().openDisplay(args[1]);
                    }
                    else {
                        out.println("Unrecognized flag " + args[0]);
                        return;
                    }
                }
            }
            out.println("Listing child components");
            
            Part part1 = theSession.parts().work();
            if (part1 != null) {
                out.println("Work part: " + part1.fullPath());
    
                ComponentWriter writer = new ComponentWriter(out);
    
                ComponentAssembly c = part1.componentAssembly();
                if ( c.rootComponent() == null ) {
                    out.println("Work part does not contain an assembly");
                    return;
                }
                AssemblyListing.walk(c.rootComponent(), 0, writer);
    
                BOMCalculator calc = new BOMCalculator();
                AssemblyListing.walk(c.rootComponent(), 0, calc);
                Collection bomTable = calc.getBOMTable();
                out.println(" ");

                out.println("BOM Table");

                for (Iterator i = bomTable.iterator(); i.hasNext();) {
                    BOMPair bomEntry = (BOMPair) i.next();
                    out.println(((Part)bomEntry.getComponent().prototype()).leaf() + "    " + bomEntry.getComponent().name() + ": " + bomEntry.getCount());
                    }
   
                }
            else {
                out.println("No parts are open");
            }
        } catch (Exception ex) {
            out.println("Exception encountered: " + ex.getMessage());
            ex.printStackTrace(out);
        }
    }
    
    /** Executes functor.execute on Component c and all its descendents */
    public static void walk(Component c, int level, IComponentFunctor functor) throws NXException, RemoteException {
        Component[] children = c.getChildren();
        functor.execute(c);
        for (int ii = 0; ii < children.length; ii++) {
            AssemblyListing.walk(children[ii], level + 1, functor);
        }
    }
    
    public static int getUnloadOption() {
        return nxopen.BaseSession.LibraryUnloadOption.IMMEDIATELY;
    }
}
