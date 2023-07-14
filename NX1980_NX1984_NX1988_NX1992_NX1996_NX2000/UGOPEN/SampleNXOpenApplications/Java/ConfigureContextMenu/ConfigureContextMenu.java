//----------------------------------------------------------------------------
//   Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//
// ConfigureContextMenu.Java
//
// Description:
//   This is a an example of customizing context menus in NX.
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/Java/ConfigureContextMenu/.
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
    
import nxopen.*;
import nxopen.menubar.*;
import nxopen.uf.*;

//------------------------------------------------------------
// Class ConfigureContextMenu
//
//     Used to demo registration and use of the context
//     menu customization callback.
//------------------------------------------------------------
public class ConfigureContextMenu implements nxopen.menubar.MenuBarManager.ConfigureContextMenu
{
    // class members
    public static Session theSession = null;
    public static ListingWindow lw = null;
    public static UI theUI = null;
    public static UFSession theUFsession = null;
    
    // constructor
    public ConfigureContextMenu()
    {
    }

    //------------------------------------------------------------------------------
    // Callback Name: configureContextMenu
    //    Executed when a customizable context menu is about to be displayed.  
    //------------------------------------------------------------------------------
    public int configureContextMenu(nxopen.menubar.ContextMenu menu, nxopen.menubar.ContextMenuProperties props)
    {
        try
        {
            // When in the Modeling application, hide the Delete button in the Graphics Window Context menu.
            int module_id = theUFsession.UF().askApplicationModule();
            if (module_id == UFConstants.UF_APP_MODELING && props.location().equals("GraphicsWindow"))
            {
                if (menu.hasEntryWithName("UG_EDIT_DELETE"))
                {
                    nxopen.menubar.ContextMenuEntry deleteMenuEntry = menu.getEntryWithName("UG_EDIT_DELETE");
                    menu.hideEntry(deleteMenuEntry);
                }
            }
            
            // Find the last visible push-button entry on the menu
            nxopen.menubar.ContextMenuEntry entry = null;

            int numMenuEntries = menu.numberOfEntries();
            for (int i = 0; i < numMenuEntries; i++)
            {
                nxopen.menubar.ContextMenuEntry entry2 = menu.getEntry(i);

                // Identify the last menu entry which is something that can be
                // activated and which is visible and sensitive.
                if (entry2.entryType() == nxopen.menubar.ContextMenuEntry.Type.PUSH_BUTTON &&
                    !entry2.isHidden() && entry2.isSensitive())
                {
                    entry = entry2;
                }
            }

            // Set identified entry as the default and move to the top of the menu.
            if (entry != null)
            {
                menu.setDefaultEntry(entry);
                menu.moveEntry(entry, 0);
            }
            
            // Add an additional menu button for a specific context.
            if ( props.context().equals("Features.Cylinder") )
            {
                // Retrieve an NX menu button
                nxopen.menubar.MenuButton newButton = theUI.menuBarManager().getButtonFromName("UG_PREFERENCES_VISUALIZATION");

                nxopen.menubar.ContextMenu subMenu = menu.addSubmenu("Custom", -1);
                subMenu.addMenuButton(newButton, -1);
            }
            
            // Add a label to identify the context menu for Features Cylinder.
            if ( props.context().equals("Features.Cylinder") )
            {
                menu.addMenuLabel("Features Cylinder", 0);
            }

            // Open the Print the Information window and print the menu.
            lw.open();
            lw.writeLine("Customize menu for " + props.context() + " in " + props.location());
            printMenu(menu, props, "   ");
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }

        return 0;
    }

    //------------------------------------------------------------------------------
    // Method: printMenu
    //    Prints a note and a description of the menu to the listing window.
    //------------------------------------------------------------------------------
    public static void printMenu(nxopen.menubar.ContextMenu menu, 
                                 nxopen.menubar.ContextMenuProperties props,
                                 String prefix)
    {
        try
        {
            int numMenuEntries = menu.numberOfEntries();
            for(int i = 0; i < numMenuEntries; i++)
            {
                nxopen.menubar.ContextMenuEntry entry = menu.getEntry(i);
                if (entry.entryType() == nxopen.menubar.ContextMenuEntry.Type.SEPARATOR)
                    lw.writeLine(prefix + Integer.toString(i) + " = ---------------");
                else
                    lw.writeLine(prefix + Integer.toString(i) + " = " + entry.label());
                    
                // If this entry is a submenu, write out its submenu as well.        
                if (entry.entryType() == nxopen.menubar.ContextMenuEntry.Type.SUBMENU)
                {
                    printMenu(menu.getSubmenu(i), props, prefix + "  ");
                }
            }
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }
    }

    //------------------------------------------------------------------------------
    //  NX Startup
    //      This entry point activates the application at NX startup
    //
    //  Will work when complete path of the dll is provided to Environment Variable 
    //  USER_STARTUP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static void startup (String [] args)
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUFsession = (UFSession)SessionFactory.get("UFSession");
            lw = theSession.listingWindow();
            theUI = (UI)SessionFactory.get("UI");
            
            theUI.menuBarManager().registerConfigureContextMenuCallback( 
                                "ConfigureContextMenu.java", 
                                "An example of context menu customization demonstrating various functions.",
                                new ConfigureContextMenu() );
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
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
    //----------------------------------------------------
    public static int getUnloadOption()
    {
        //Unloads the image when the NX session terminates
        return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    }
}

