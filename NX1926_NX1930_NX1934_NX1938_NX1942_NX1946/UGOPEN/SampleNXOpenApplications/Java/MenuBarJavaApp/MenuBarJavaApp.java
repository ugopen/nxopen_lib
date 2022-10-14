//----------------------------------------------------------------------------
//                  Copyright (c) 2007 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// SampleCppApp.cpp
//
// Description:
//   This is a an example of adding a JAVA application to NX.
//   In addition to using this source file there are two menu files
//   (MenuBarJavaAppButton.men and MenuBarJavaApp.men) which are also required.
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/Java/MenuBarJavaApp.
//
//   Please see the "Adding Custom Applications to NX" chapter of the
//   NX Open Programmer's Guide or search the documentation for
//   "MenuBarJavaApp" for a detailed description of this example.
//
//   These files are intended to provide a template that can be modified
//   by renaming the files, and renaming the variables and routines
//   to allow you create your own application.
//
//   Additional information on MenuScript can be found in:
//     - the MenuScript User's Guide
//     - the NXOpen Programmer's Guide
//     - the NX Open for Java Reference Guide (see MenuBar)
//     - any other place in the NX documentation that comes up when
//       you search for "MenuScript" or "MenuBar"
//
//   *** PLEASE NOTE ***
//   The class created from this program must be placed in the
//   "application" directory under a directory listed in the file pointed to by the
//   environment variable in UGII_CUSTOM_DIRECTORY_FILE (i.e. the shared library must
//   not be in the "startup" directory).
//
//----------------------------------------------------------------------------

import nxopen.*;
import nxopen.menubar.*;
import java.io.*;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.EventQueue;

// MenuBarJavaApp class used to demo a custom application with callbacks in the java language
public class MenuBarJavaApp implements nxopen.menubar.MenuBarManager.InitializeMenuApplication, nxopen.menubar.MenuBarManager.EnterMenuApplication, nxopen.menubar.MenuBarManager.ExitMenuApplication, nxopen.menubar.MenuBarManager.ActionCallback
{
    // class members
    public static Session theSession = null;
    public static ListingWindow lw = null;
    public static UI theUI = null;
    public static int testStatus = 0;

    static MenuBarJavaApp theMenuBarJavaApp;

    // Used to tell us if we've already registered our callbacks
    public static int registered = 0;
    static int isDisposeCalled;

    // constructor
    public MenuBarJavaApp()
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            lw = theSession.listingWindow();
            theUI = (UI)SessionFactory.get("UI");
            initializeCallbacks();
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
    }

    // InitializeCallbacks - registers the callbacks with NX
    private void initializeCallbacks()
    {
        try
        {
            if( registered == 0 )
            {
                int my_app = theUI.menuBarManager().registerApplication("SAMPLE_JAVA_APP", this, this, this, true, true, true );
                theUI.menuBarManager().addMenuAction( "SAMPLE_JAVA_APP__action1", this );
                theUI.menuBarManager().addMenuAction( "SAMPLE_JAVA_APP__action2", this );
                theUI.menuBarManager().addMenuAction( "SAMPLE_JAVA_APP__action3", this );
                theUI.menuBarManager().addMenuAction( "SAMPLE_JAVA_APP__action4", this );
                theUI.menuBarManager().addMenuAction( "SAMPLE_JAVA_APP__action5", this );
                registered = 1;
            }
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
    }

    //----------------------------------------------------
    //  This entry point executes at the startup of NX.
    //  Used to register the application and callbacks.
    //----------------------------------------------------
    public static void startup (String [] args)throws NXException, java.rmi.RemoteException
    {

        try
        {
            theMenuBarJavaApp = new MenuBarJavaApp();
        }

        catch(Exception ex)
        {
        }

    }

    //----------------------------------------------------
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
    //----------------------------------------------------
    public static int getUnloadOption()
    {
        return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    }




    //----------------------------------------------------
    //  initializeMenuApplication()
    //    Init Proc callback is executed when the application
    //    is entered.  It's used to initialize the
    //    application's data.
    //
    //    Prints a note to the listing window.
    //----------------------------------------------------
    public int initializeMenuApplication()
    {
        try
        {

            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside My JAVA Init Proc");
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return 0;
    }

    //----------------------------------------------------
    //  exitMenuApplication()
    //    Exit Proc callback is executed when the application
    //    is exited.  It's used to free (clean up) the
    //    application's data.
    //
    //    Prints a note to the listing window.
    //----------------------------------------------------
    public int exitMenuApplication()
    {
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside My JAVA Exit Proc");
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return 0;
    }

    //----------------------------------------------------
    //  enterMenuApplication()
    //    Enter Proc callback is executed when the application
    //    is selected (activated) from the pulldown menu.
    //    If this is the first time entering the application,
    //    the Init Proc callback will get called first to
    //    initialize any data required by this callback.
    //
    //    Prints a note to the listing window.
    //----------------------------------------------------
    public int enterMenuApplication()
    {
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside My JAVA Enter Proc");
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }
        return 0;
    }

    //------------------------------------------------------------------------------
    // printButtonIdCB
    //   This is a callback method associated with SAMPLE_JAVA_APP__action1 action button.
    //   This will get executed whenever 'Print Button ID' is selected from the
    //   'Sample Java' menu.
    //   Prints the button id of the active button to the listing window.
    //------------------------------------------------------------------------------
    public nxopen.menubar.MenuBarManager.CallbackStatus printButtonIdCB( nxopen.menubar.MenuButtonEvent buttonEvent )
    {
        nxopen.menubar.MenuBarManager.CallbackStatus status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside printButtonIdCB Callback:");
            lw.writeLine("    Button Id: " + buttonEvent.activeButton().buttonId());
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }

        return status;
    }

    //------------------------------------------------------------------------------
    // testCallbackReturnsCB
    //   This is a callback method associated with SAMPLE_JAVA_APP__action2 action button.
    //   This will get executed whenever 'Test Callback Returns' is selected from the
    //   'Sample Java' menu.
    //
    //   The first time it is called it will return 0 (CONTINUE)
    //   The next time it is called it will return 1 (CANCEL)
    //   Each time it is invoke if returns the next possible status value
    //   After the sixth time it's called it starts the cycle over by returnng 0 (CONTINUE)
    //
    //   Prints a note to the listing window stating which return value was used.
    //------------------------------------------------------------------------------
    public nxopen.menubar.MenuBarManager.CallbackStatus testCallbackReturnsCB( nxopen.menubar.MenuButtonEvent buttonEvent )
    {
        nxopen.menubar.MenuBarManager.CallbackStatus status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside testCallbackReturnsCB Callback:");

            if( testStatus == 0 )
            {
                status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
                lw.writeLine("    Returning: nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE");
            }
            else if( testStatus == 1 )
            {
                status = nxopen.menubar.MenuBarManager.CallbackStatus.CANCEL;
                lw.writeLine("    Returning: nxopen.menubar.MenuBarManager.CallbackStatus.CANCEL");
            }
            else if( testStatus == 2 )
            {
                status = nxopen.menubar.MenuBarManager.CallbackStatus.OVERRIDE_STANDARD;
                lw.writeLine("    Returning: nxopen.menubar.MenuBarManager.CallbackStatus.OVERRIDE_STANDARD");
            }
            else if( testStatus == 3 )
            {
                status = nxopen.menubar.MenuBarManager.CallbackStatus.WARNING;
                lw.writeLine("    Returning: nxopen.menubar.MenuBarManager.CallbackStatus.WARNING");
            }
            else if( testStatus == 4 )
            {
                status = nxopen.menubar.MenuBarManager.CallbackStatus.ERROR;
                lw.writeLine("    Returning: nxopen.menubar.MenuBarManager.CallbackStatus.ERROR");
            }
            lw.writeLine(" ");
            testStatus++;
            if( testStatus > 4 )
            {
                testStatus = 0;
            }

        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }

        return status;
    }

    //------------------------------------------------------------------------------
    // printApplicationIdCB
    //   This is a callback method associated with SAMPLE_JAVA_APP__action3 action button.
    //   This will get executed whenever 'Print Application ID' is selected from the
    //   'Sample Java' menu.
    //   Prints the application id of the active button to the listing window.
    //------------------------------------------------------------------------------
    public nxopen.menubar.MenuBarManager.CallbackStatus printApplicationIdCB( nxopen.menubar.MenuButtonEvent buttonEvent )
    {
        nxopen.menubar.MenuBarManager.CallbackStatus status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside printApplicationIdCB Callback:");
            lw.writeLine("    Application Id: " + buttonEvent.applicationId());
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }

        return status;
    }


    //------------------------------------------------------------------------------
    // printButtonDataCB
    //   This is a callback method associated with SAMPLE_JAVA_APP__action4 action button.
    //   This will get executed whenever 'Print This Button Data' is selected from the
    //   'Sample Java' menu.
    //   It will print lots of info about the button to the listing window.
    //------------------------------------------------------------------------------
    public nxopen.menubar.MenuBarManager.CallbackStatus printButtonDataCB( nxopen.menubar.MenuButtonEvent buttonEvent )
    {
        nxopen.menubar.MenuBarManager.CallbackStatus status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside printButtonDataCB Callback:");

            lw.writeLine("    Button Id: " + buttonEvent.activeButton().buttonId());
            lw.writeLine("    Name: " + buttonEvent.activeButton().buttonName());
            lw.writeLine("    Button type name: " + buttonEvent.activeButton().buttonTypeName());
            lw.writeLine("    Menubar Name: " + buttonEvent.menuBarName());
            lw.writeLine("    Application Id: " + buttonEvent.applicationId());
            String[] ancestors = buttonEvent.getMenuAncestors();
            for( int i = 0; i < ancestors.length; i++ )
            {
                lw.writeLine("    Ancestor[" + i + "]: " + ancestors[i]);
            }
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }

        return status;
    }


    //------------------------------------------------------------------------------
    // printToggleStatusCB
    //   This is a callback method associated with SAMPLE_JAVA_APP__action5 action button.
    //   This will get executed whenever 'Print This Button Data' is selected from the
    //   'Sample Java' menu.
    //   It will print the current status of the toggle
    //------------------------------------------------------------------------------
    public nxopen.menubar.MenuBarManager.CallbackStatus printToggleStatusCB( nxopen.menubar.MenuButtonEvent buttonEvent )
    {
        nxopen.menubar.MenuBarManager.CallbackStatus status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
        try
        {
            lw.open();
            lw.writeLine(" ");
            lw.writeLine("Inside printToggleStatusCB Callback:");

            if( buttonEvent.activeButton().toggleStatus() == nxopen.menubar.MenuButton.Toggle.ON)
            {
                lw.writeLine("    The toggle is now ON" );
            }
            else
            {
                lw.writeLine("    The toggle is now OFF" );
            }
            lw.writeLine(" ");
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }

        return status;
    }


    //------------------------------------------------------------------------------
    // Callback Name: actionCallback
    //   This is a callback method associated with all of the 'Sample Java' menu
    //   action buttons.
    //   Whenever a button is activated, we enter this function, and determine which
    //   button triggered the callback, then call the specific function for the
    //   given button.
    //------------------------------------------------------------------------------
    public nxopen.menubar.MenuBarManager.CallbackStatus actionCallback( nxopen.menubar.MenuButtonEvent buttonEvent )
    {
        nxopen.menubar.MenuBarManager.CallbackStatus status = nxopen.menubar.MenuBarManager.CallbackStatus.CONTINUE;
        try
        {
            // First we need to determine which button's action we need to perform
            if( buttonEvent.activeButton().buttonName().equals("SAMPLE_JAVA_APP_BUTTON1") )
            {
                status = printButtonIdCB( buttonEvent );
            }
            else if( buttonEvent.activeButton().buttonName().equals("SAMPLE_JAVA_APP_BUTTON2") )
            {
                status = testCallbackReturnsCB( buttonEvent );
            }
            else if( buttonEvent.activeButton().buttonName().equals( "SAMPLE_JAVA_APP_BUTTON3") )
            {
                status = printApplicationIdCB( buttonEvent );
            }
            else if( buttonEvent.activeButton().buttonName().equals( "SAMPLE_JAVA_APP_BUTTON4") )
            {
                status = printButtonDataCB( buttonEvent );
            }
            else if( buttonEvent.activeButton().buttonName().equals( "SAMPLE_JAVA_APP_BUTTON5") )
            {
                status = printToggleStatusCB( buttonEvent );
            }
            else
            {
                lw.open();
                lw.writeLine(" ");
                lw.writeLine("Inside Unknown JAVA actionCallback");
                lw.writeLine("'"+buttonEvent.activeButton().buttonName()+"'");
                lw.writeLine(" ");
            }
        }
        catch(Exception ex)
        {
            System.out.println("Error Message");
            System.out.println(ex.getMessage());
        }

        return status;
    }


}

