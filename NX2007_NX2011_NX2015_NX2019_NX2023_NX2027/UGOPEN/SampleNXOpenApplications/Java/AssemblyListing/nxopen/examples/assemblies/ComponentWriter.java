/*
 * Created on Feb 24, 2005
 * 
 * Copyright 2005 UGS Corp. All Rights Reserved.
 * 
 */
package nxopen.examples.assemblies;
import java.rmi.RemoteException;

import nxopen.NXException;
import nxopen.INXObject;
import nxopen.NXObject;
import nxopen.Part;
import nxopen.assemblies.Component;

/**
 * @author pesumner
 * An implementation of IComponentFunctor.  Writes the name and path of
 * the component.
 */
public class ComponentWriter implements IComponentFunctor {

    private java.io.PrintStream out;
    
    public ComponentWriter(java.io.PrintStream out) {
        this.out = out;
    }
    /* (non-Javadoc)
     * @see nxopen.examples.IComponentFunctor#execute(NXOpen.Assemblies.Component)
     */
    public void execute(Component c) {
        try {
            INXObject prototype = c.prototype();
            if (prototype instanceof Part) {
                out.println("Walking: " + ((Part)c.prototype()).fullPath() + " " + c.name());
            } else {
                out.println("Walking: " + c.name());
            }
        } catch (NXException nxEx) {
            nxEx.printStackTrace(out);
        } catch (RemoteException ex) {
            ex.printStackTrace(out);
        }
    }
}
