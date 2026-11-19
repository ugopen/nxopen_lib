//----------------------------------------------------------------------------
//                  Copyright (c) 2007 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// MenuBarCSharpApp.cs
//
// Description:
//   This is a an example of adding a C Sharp application to NX.
//
//   Note: You must include a reference to Microsoft.VisualBasic to 
//   compile this program.
//
//   In addition to using this source file there are two menu files 
//   (MenuBarDotNetAppButton.men and MenuBarCSharpApp.men) which are also required.
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/.NET/MenuBarDotNetApp.
//
//   Please see the "Adding Custom Applications to NX" chapter of the
//   NX Open Programmer's Guide or search the documentation for
//   "MenuBarDotNetApp" for a detailed description of this example.
//
//   These files are intended to provide a template that can be modified
//   by renaming the files, and renaming the variables and routines
//   to allow you create your own application.
//
//   Additional information on MenuScript can be found in:
//     - the MenuScript User's Guide
//     - the NXOpen Programmer's Guide
//     - the NX Open for .NET Reference Guide (see MenuBar)
//     - any other place in the NX documentation that comes up when
//       you search for "MenuScript" or "MenuBar"
//
//   *** PLEASE NOTE ***
//   The shared library created from this program must be placed in the
//   "application" directory under a directory listed in the file pointed to by the
//   environment variable in UGII_CUSTOM_DIRECTORY_FILE (i.e. the shared library must
//   not be in the "startup" directory).
//
//----------------------------------------------------------------------------


using System;
using Microsoft.VisualBasic;
using NXOpen;
using NXOpen.UF;

public class Program
{
    // class members
    static Session theSession = null;
    static ListingWindow lw = null;
    static UI theUI = NXOpen.UI.GetUI();
    public static bool isDisposeCalled;

    //------------------------------------------------------------------------------
    // Callback Name: ApplicationInit
    //    Executed when the application is entered.  
    //    It's used to initialize the application's data.
    //
    //    Prints a note to the listing window.
    //------------------------------------------------------------------------------
    public static int ApplicationInit()
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside My CSharp Init Callback");
        lw.WriteLine(" ");
        return 0;
    }

    //------------------------------------------------------------------------------
    // Callback Name: ApplicationEnter
    //    Executed when the application is selected 
    //    (activated) from the pulldown menu.  
    //    If this is the first time entering the application,
    //    the ApplicationInit callback will get called first to
    //    initialize any data required by this callback.
    //
    //    Prints a note to the listing window.
    //------------------------------------------------------------------------------
    public static int ApplicationEnter()
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside My CSharp Enter Callback");
        lw.WriteLine(" ");
        return 0;
    }

    //------------------------------------------------------------------------------
    // Callback Name: ApplicationExit
    //    Executed when the application is exited.  
    //    It's used to free (clean up) the application's data.
    //
    //    Prints a note to the listing window.
    //------------------------------------------------------------------------------
    public static int ApplicationExit()
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside My CSharp Exit Callback");
        lw.WriteLine(" ");
        return 0;
    }
    
    //------------------------------------------------------------------------------
    // Callback Name: PrintButtonIdCB
    //   This is a callback method associated with SAMPLE_CSHARP_APP__action1 action button.
    //   This will get executed whenever 'Print Button ID' is selected from the
    //   'Sample C Sharp' menu.
    //   Given a button name (such as SAMPLE_CSHARP_APP_BUTTON1) from the user, the
    //   input button's id gets printed to the listing window.
    //------------------------------------------------------------------------------
    public static NXOpen.MenuBar.MenuBarManager.CallbackStatus PrintButtonIdCB(NXOpen.MenuBar.MenuButtonEvent buttonEvent)
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside PrintButtonIdCB Callback:");
        String buttonName = buttonEvent.ActiveButton.ButtonName;
        buttonName = Interaction.InputBox( "Enter name of button you wish to query", "Print Button Id", buttonName, 100, 100 );
        
        NXOpen.MenuBar.MenuButton myButton = theUI.MenuBarManager.GetButtonFromName(buttonName);
        if( myButton == null )
        {
            lw.WriteLine("    " + buttonName + " button not found");
        }
        else
        {
            lw.WriteLine("    Button Id for " + buttonName + ": " + myButton.ButtonId);
        }
        lw.WriteLine(" ");
        return NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue;
    }

    //------------------------------------------------------------------------------
    // Callback Name: TestCallbackReturnsCB
    //   This is a callback method associated with SAMPLE_CSHARP_APP__action2 action button.
    //   This will get executed whenever 'Test Callback Returns' is selected from the
    //   'Sample C Sharp' menu.
    //   Prompts the user for a number between 0-4.
    //   Tests the return value specified by the user, and prints a note to the
    //   listing window stating which return value was used.    
    //------------------------------------------------------------------------------
    public static NXOpen.MenuBar.MenuBarManager.CallbackStatus TestCallbackReturnsCB(NXOpen.MenuBar.MenuButtonEvent buttonEvent)
    {
        // ---- Enter your callback code here -----
        NXOpen.MenuBar.MenuBarManager.CallbackStatus status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue;
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside TestCallbackReturnsCB Callback:");
        
        String returnString = Interaction.InputBox("Enter a number between 0 and 4", "Test Callback Returns", "0", 100, 100);
        if( returnString == "0" )
        {
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue;
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue");
        }
        else if (returnString == "1")
        {
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Cancel;
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Cancel");
        }
        else if (returnString == "2")
        {
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.OverrideStandard;
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.OverrideStandard");
        }
        else if (returnString == "3")
        {
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Warning;
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Warning");
        }
        else if (returnString == "4")
        {
            status = NXOpen.MenuBar.MenuBarManager.CallbackStatus.Error;
            lw.WriteLine("    Returning: NXOpen.MenuBar.MenuBarManager.CallbackStatus.Error");
        }
        else
        {
            lw.WriteLine("    Invalid Input: must be an integer between 0 and 4");
        }
        lw.WriteLine(" ");

        return status;
    }

    //------------------------------------------------------------------------------
    // Callback Name: PrintApplicationIdCB
    //   This is a callback method associated with SAMPLE_CSHARP_APP__action3 action button.
    //   This will get executed whenever 'Print Application ID' is selected from the
    //   'Sample C Sharp' menu.
    //   Prints the application id of the active button.
    //------------------------------------------------------------------------------
    public static NXOpen.MenuBar.MenuBarManager.CallbackStatus PrintApplicationIdCB(NXOpen.MenuBar.MenuButtonEvent buttonEvent)
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside PrintApplicationIdCB Callback:");
        lw.WriteLine("    Application Id: " + buttonEvent.ApplicationId );
        lw.WriteLine(" ");

        return NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue;
    }

    //------------------------------------------------------------------------------
    // Callback Name: PrintButtonDataCB
    //   This is a callback method associated with SAMPLE_CSHARP_APP__action4 action button.
    //   This will get executed whenever 'Print This Button Data' is selected from the
    //   'Sample C Sharp' menu.
    //   It will print lots of info about the button to the listing window.
    //------------------------------------------------------------------------------
    public static NXOpen.MenuBar.MenuBarManager.CallbackStatus PrintButtonDataCB(NXOpen.MenuBar.MenuButtonEvent buttonEvent)
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside My CS Callback:");
        lw.WriteLine("    Button Id: " + buttonEvent.ActiveButton.ButtonId);
        lw.WriteLine("    Name: " + buttonEvent.ActiveButton.ButtonName);
        lw.WriteLine("    Button type name: " + buttonEvent.ActiveButton.ButtonTypeName);
        lw.WriteLine("    Menubar Name: " + buttonEvent.MenuBarName);
        lw.WriteLine("    Application Id: " + buttonEvent.ApplicationId);
        string[] ancestors = buttonEvent.GetMenuAncestors();
        for( int i = 0; i < ancestors.Length; i++ )
        {
            lw.WriteLine("    Ancestor[" + i + "]: " + ancestors.GetValue(i));
        }
        lw.WriteLine(" ");
        return NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue;
    }

    //------------------------------------------------------------------------------
    // Callback Name: PrintToggleStatusCB
    //   This is a callback method associated with SAMPLE_CSHARP_APP__action5 action button.
    //   This will get executed whenever 'Print This Button Data' is selected from the
    //   'Sample C Sharp' menu.
    //   It will print the current status of the toggle
    //------------------------------------------------------------------------------
    public static NXOpen.MenuBar.MenuBarManager.CallbackStatus PrintToggleStatusCB(NXOpen.MenuBar.MenuButtonEvent buttonEvent)
    {
        // ---- Enter your callback code here -----
        lw.Open();
        lw.WriteLine(" ");
        lw.WriteLine("Inside PrintToggleStatusCB Callback:");
        if( buttonEvent.ActiveButton.ToggleStatus == NXOpen.MenuBar.MenuButton.Toggle.On )
        {
            lw.WriteLine("   The toggle is now ON");
        }
        else
        {
            lw.WriteLine("   The toggle is now OFF");
        }
        lw.WriteLine(" ");
        return NXOpen.MenuBar.MenuBarManager.CallbackStatus.Continue;
    }


    //------------------------------------------------------------------------------
    //  NX Startup
    //      This entry point registers the application at NX startup
    //------------------------------------------------------------------------------
    public static int Startup()
    {
        int retValue = 0;
        try
        {
            if (theSession == null)
            {
                theSession = Session.GetSession();
            }
            if (lw == null)
            {
                lw = theSession.ListingWindow;
            }
            theUI.MenuBarManager.RegisterApplication("SAMPLE_CSHARP_APP", 
            new NXOpen.MenuBar.MenuBarManager.InitializeMenuApplication(Program.ApplicationInit),
            new NXOpen.MenuBar.MenuBarManager.EnterMenuApplication(Program.ApplicationEnter),
            new NXOpen.MenuBar.MenuBarManager.ExitMenuApplication(Program.ApplicationExit), true, true, true );
            theUI.MenuBarManager.AddMenuAction("SAMPLE_CSHARP_APP__action1", new NXOpen.MenuBar.MenuBarManager.ActionCallback(Program.PrintButtonIdCB));
            theUI.MenuBarManager.AddMenuAction("SAMPLE_CSHARP_APP__action2", new NXOpen.MenuBar.MenuBarManager.ActionCallback(Program.TestCallbackReturnsCB));
            theUI.MenuBarManager.AddMenuAction("SAMPLE_CSHARP_APP__action3", new NXOpen.MenuBar.MenuBarManager.ActionCallback(Program.PrintApplicationIdCB));
            theUI.MenuBarManager.AddMenuAction("SAMPLE_CSHARP_APP__action4", new NXOpen.MenuBar.MenuBarManager.ActionCallback(Program.PrintButtonDataCB));
            theUI.MenuBarManager.AddMenuAction("SAMPLE_CSHARP_APP__action5", new NXOpen.MenuBar.MenuBarManager.ActionCallback(Program.PrintToggleStatusCB));
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
        }
        return retValue;
    }

    //------------------------------------------------------------------------------
    // Following method disposes all the class members
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        try
        {
            if (isDisposeCalled == false)
            {
                //TODO: Add your application code here 
            }
            isDisposeCalled = true;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----

        }
    }

    //------------------------------------------------------------
    //
    //  GetUnloadOption()
    //
    //     Used to tell NX when to unload this library
    //
    //     Available options include:
    //       Session.LibraryUnloadOption.Immediately
    //       Session.LibraryUnloadOption.Explicitly
    //       Session.LibraryUnloadOption.AtTermination
    //
    //     Any programs that register callbacks must use 
    //     AtTermination as the unload option.
    //------------------------------------------------------------
    public static int GetUnloadOption(string arg)
    {
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);

        //Unloads the image immediately after execution within NX
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
        return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }

}

