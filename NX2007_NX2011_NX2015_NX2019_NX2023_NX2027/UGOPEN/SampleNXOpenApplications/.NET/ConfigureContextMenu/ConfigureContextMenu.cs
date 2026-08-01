//----------------------------------------------------------------------------
//   Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//
// ConfigureContextMenu.cs
//
// Description:
//   This is a an example of customizing context menus in NX.
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/DotNET/ConfigureContextMenu/.
//
//   These files are intended to provide a template that can be modified
//   by renaming the files, and renaming the variables and routines
//   to allow you create your own customization.
//
//   *** PLEASE NOTE ***
//   The shared library created from this program must be placed in the
//   "startup" directory under a directory listed in the file pointed to by the
//   environment variable in UGII_CUSTOM_DIRECTORY_FILE.
//
//----------------------------------------------------------------------------
using System;
using NXOpen;
using NXOpenUI;
using NXOpen.UF;
  
//------------------------------------------------------------
// Class ConfigureContextMenu
//
//     Used to demo registration and use of the context
//     menu customization callback.
//------------------------------------------------------------  
public class ConfigureContextMenu
{
    // class members
    private static Session theSession;
    private static UI theUI;
    private static ListingWindow lw;
    private static NXOpen.UF.UFSession theUFSession;

    //------------------------------------------------------------------------------
    // Callback Name: CustomizeMenu
    //    Executed when a customizable context menu is about to be displayed.  
    //------------------------------------------------------------------------------
    public static int CustomizeMenu(NXOpen.MenuBar.ContextMenu menu, 
                                    NXOpen.MenuBar.ContextMenuProperties props)
    {
        // When in the Modeling application, hide the Delete button in the Graphics Window context menu.
        int moduleId;
        theUFSession.UF.AskApplicationModule(out moduleId);
        if (moduleId == UFConstants.UF_APP_MODELING && string.Equals(props.Location, "GraphicsWindow"))
        {
            if (menu.HasEntryWithName("UG_EDIT_DELETE"))
            {
                NXOpen.MenuBar.ContextMenuEntry deleteMenuEntry = menu.GetEntryWithName("UG_EDIT_DELETE");
                menu.HideEntry(deleteMenuEntry);
            }
        }

        // Find the last visible push-button entry on the menu
        NXOpen.MenuBar.ContextMenuEntry entry = null;
        int numMenuEntries = menu.NumberOfEntries;
        for (int i = 0; i < numMenuEntries; i++)
        {
            NXOpen.MenuBar.ContextMenuEntry entry2 = menu.GetEntry(i);

            // Identify the last menu entry which is something that can be
            // activated and which is visible and sensitive.
            if (entry2.EntryType == NXOpen.MenuBar.ContextMenuEntry.Type.PushButton &&
                !entry2.IsHidden && entry2.IsSensitive)
            {
                entry = entry2;
            }
        }

        // Set identified entry as the default and move to the top of the menu.
        if (entry != null)
        {
            menu.SetDefaultEntry(entry);
            menu.MoveEntry(entry, 0);
        }
        
        // Add an additional menu button for a specific context.
        if ( string.Equals(props.Context, "Features.Cylinder") )
        {
            // Retrieve an NX menu button
            NXOpen.MenuBar.MenuButton newButton = theUI.MenuBarManager.GetButtonFromName("UG_PREFERENCES_VISUALIZATION");

            NXOpen.MenuBar.ContextMenu subMenu = menu.AddSubmenu("Custom", -1);
            subMenu.AddMenuButton(newButton, -1);
        }

        // Add a label to identify the context menu for Features Cylinder.
        if (string.Equals(props.Context, "Features.Cylinder"))
        {
            menu.AddMenuLabel("Features Cylinder", 0);
        }

        // Open the Print the Information window and print the menu.
        lw.Open();
        lw.WriteLine("Customize menu for " + props.Context + " in " + props.Location);
        PrintMenu(menu, props);

        return 0;
    }

    //------------------------------------------------------------------------------
    // Callback Name: PrintMenu
    //    Prints a note and a description of the menu to the listing window.
    //------------------------------------------------------------------------------
    public static void PrintMenu(NXOpen.MenuBar.ContextMenu menu, 
                                 NXOpen.MenuBar.ContextMenuProperties props, 
                                 string prefix = "   ")
    {
        int numMenuEntries = menu.NumberOfEntries;
        for (int i = 0; i < numMenuEntries; i++)
        {
            NXOpen.MenuBar.ContextMenuEntry entry = menu.GetEntry(i);
            if (entry.EntryType == NXOpen.MenuBar.ContextMenuEntry.Type.Separator)
                lw.WriteLine(prefix + i + " = --------------------");
            else
                lw.WriteLine(prefix + i + " = " + entry.Label);

            // If this entry is a submenu, write out its submenu as well.        
            if (entry.EntryType == NXOpen.MenuBar.ContextMenuEntry.Type.Submenu)
            {
                PrintMenu(menu.GetSubmenu(i), props, prefix + "  ");
            }
        }
    }

    //------------------------------------------------------------------------------
    //  NX Startup
    //      This entry point activates the application at NX startup
    //
    //  Will work when complete path of the dll is provided to Environment Variable 
    //  USER_STARTUP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int Startup()
    {
        theSession = Session.GetSession();
        theUFSession = UFSession.GetUFSession();
        theUI = UI.GetUI();
        lw = theSession.ListingWindow;

        theUI.MenuBarManager.RegisterConfigureContextMenuCallback(
                                "ConfigureContextMenu.cs", 
                                "An example of context menu customization demonstrating various functions.",
                                new NXOpen.MenuBar.MenuBarManager.ConfigureContextMenu(CustomizeMenu));

        return 0;
    }

    //------------------------------------------------------------
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
        //Unloads the image when the NX session terminates
        return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
    }
}

