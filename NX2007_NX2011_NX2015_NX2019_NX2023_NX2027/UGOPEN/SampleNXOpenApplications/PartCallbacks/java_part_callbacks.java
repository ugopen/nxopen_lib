//----------------------------------------------------------------------------
//                  Copyright (c) 2007 UGS Corp.
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// java_part_callbacks.java
//
// Description:
//     This simple demo registers part callbacks for every available reason
//     via the Java language.
//
//     After compiling and linking this demo program, the output class or jar needs
//     to be placed in a folder called startup (for example c:\\user_dir\\startup).
//     Also the UGII_USER_DIR enviornment variable needs to point to the startup
//     directory's parent folder (for example: UGII_USER_DIR=c:\\user_dir).
//     Once you have the startup directory and user dir environment variable
//     set up, start NX.  The part callbacks will be registered at startup.
//     Now anytime you create new, open, save, save as, close, modify, rename,
//     or change the workpart your callbacks will be executed.
//
//     To demo all of the available part callbacks at runtime - compile and link
//     execute_all_part_callbacks.c.
//     Then start NX and go to File->Execute->NX Open and select your compiled
//     execute_all_callbacks program.
//
//---------------------------------------------------------------------------/

import nxopen.*;
import nxopen.uf.*;
import java.io.*;

// java_part_callbacks class used to demo all of the available part related callback functions in the java language
public class java_part_callbacks implements nxopen.PartCollection.PartCreatedHandler, nxopen.PartCollection.PartOpenedHandler, nxopen.PartCollection.PartSavedHandler, nxopen.PartCollection.PartSavedAsHandler, nxopen.PartCollection.PartClosedHandler, nxopen.PartCollection.PartModifiedHandler, nxopen.PartCollection.PartRenamedHandler, nxopen.PartCollection.WorkPartChangedHandler
{
    // class members
    public static Session theSession = null;
    public static ListingWindow lw = null;

    public static UFSession theUFSession = null;
    static java_part_callbacks the_java_part_callbacks;

    // Used to tell us if we've already registered our callbacks
    public static int registered = 0;

    // The ids of the registered callbacks are used if
    // you ever want to unregister a callback.
    // If you plan to register the callback once for
    // the enitre session, and don't intend to remove them ,
    // (recommended) tracking the id may not be necessary.
    public static int idPartCreated1 = 0;
    public static int idPartOpened1 = 0;
    public static int idPartSaved1 = 0;
    public static int idPartSavedAs1 = 0;
    public static int idPartClosed1 = 0;
    public static int idPartModified1 = 0;
    public static int idPartRenamed1 = 0;
    public static int idWorkPartChanged1 = 0;

    static int isDisposeCalled;

    // constructor
    public java_part_callbacks()
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");
            lw = theSession.listingWindow();
            initializeCallbacks();
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
    }

    // Initialize Callbacks - registers the part callbacks with NX
    private void initializeCallbacks()
    {
        try
        {
               if( registered == 0 )
               {
                   idPartCreated1 = theSession.parts().addPartCreatedHandler(this);
                   idPartOpened1 = theSession.parts().addPartOpenedHandler(this);
                   idPartSaved1 = theSession.parts().addPartSavedHandler(this);
                   idPartSavedAs1 = theSession.parts().addPartSavedAsHandler(this);
                   idPartClosed1 = theSession.parts().addPartClosedHandler(this);
                   idPartModified1 = theSession.parts().addPartModifiedHandler(this);
                   idPartRenamed1 = theSession.parts().addPartRenamedHandler(this);
                   idWorkPartChanged1 = theSession.parts().addWorkPartChangedHandler(this);
                   registered = 1;
            }
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
    }


    // Called manually from File->Execute->NX Open
    public static void main(String[] args)
    {
        try
        {
            if( the_java_part_callbacks == null )
            {
                the_java_part_callbacks = new java_part_callbacks();
            }
        }
        catch (Exception e)
        {
        }
    }

    // Called when NX starts up
    public static void startup (String [] args)throws NXException, java.rmi.RemoteException
    {
        try
        {
            the_java_part_callbacks = new java_part_callbacks();
        }

        catch(Exception ex)
        {
        }

    } // startup ends


    //  getUnloadOption()
    //
    //    Used to tell NX when to unload this library
    //
    //    Available options include:
    //       BaseSession.LibraryUnloadOption.IMMEDIATELY
    //       BaseSession.LibraryUnloadOption.EXPLICITLY
    //       BaseSession.LibraryUnloadOption.AT_TERMINATION
    //
    //    Any programs that register callbacks must use
    //    AtTermination as the unload option.
    //
    public static int getUnloadOption()
    {
        return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    }

    // Called when a new part is created
    // Prints the name of the created part to the listing window
    public void partCreatedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA created: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when a part is opened
    // Prints the name of the opened part to the listing window
    public void partOpenedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA opened: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when a part is saved
    // Prints the name of the saved part to the listing window
    public void partSavedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA saved: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when a part is saved as
    // Prints the name of the saved as part to the listing window
    public void partSavedAsHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA saved as: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when a part is closed
    // Prints the name of the closed part to the listing window
    public void partClosedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA closed: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when a part is modified for the first time
    // Prints the name of the modified part to the listing window
    public void partModifiedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA modified: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when a part is renamed
    // Prints the name of the renamed part to the listing window
    public void partRenamedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA renamed: " + p.fullPath());
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }

    // Called when the workpart changes
    // Prints the name of old workpart and new workpart to the listing window
    public void workPartChangedHandler(BasePart p)
    {
        try
        {
            lw.open();
            lw.writeLine("    JAVA work part changed:");
            if (p == null)
            {
                lw.writeLine("        Old Work Part: NULL");
            }
            else
            {
                lw.writeLine("        Old Work Part: " + p.fullPath());
            }
            if (theSession.parts().work() == null)
            {
                lw.writeLine("        New Work Part: NULL");
            }
            else
            {
                lw.writeLine("        New Work Part: " + theSession.parts().work().fullPath());
            }

        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return;
    }
}

