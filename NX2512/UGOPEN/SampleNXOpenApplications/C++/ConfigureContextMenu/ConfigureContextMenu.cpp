//----------------------------------------------------------------------------
//   Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//
// ConfigureContextMenu.cpp
//
// Description:
//   This is a an example of customizing context menus in NX.
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/Cpp/ConfigureContextMenu/.
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

#include <NXOpen/ListingWindow.hxx>
#include "ConfigureContextMenu.h"
#include <uf_exit.h>
#include <uf_ugopenint.h>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <string>

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session* ConfigureContextMenu::theSession = NULL;
UI* ConfigureContextMenu::theUI = NULL;
ListingWindow* ConfigureContextMenu::lw = NULL;
static ConfigureContextMenu* theConfigureContextMenu = NULL;


//------------------------------------------------------------------------------
// Constructor for CppMenuBarApplication class
//------------------------------------------------------------------------------
ConfigureContextMenu::ConfigureContextMenu()
{
    try
    {
        // Initialize the NX Open C++ API environment
        ConfigureContextMenu::theSession = Session::GetSession();
        ConfigureContextMenu::theUI = UI::GetUI();

        // Initialize the listing window
        if( ConfigureContextMenu::lw == NULL )
        {
            ConfigureContextMenu::lw = ConfigureContextMenu::theSession->ListingWindow();
        }

        // Initialize the Context Menu Callback
        ConfigureContextMenu::theUI->MenuBarManager()->RegisterConfigureContextMenuCallback(
                                "ConfigureContextMenu.cpp", 
                                "An example of context menu customization demonstrating various functions.",
                                make_callback(this, &ConfigureContextMenu::CustomizeMenu));
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
}


//---------------------------------------------
// Called when NX starts up
// Registers the callback with NX
//---------------------------------------------
extern void ufsta(char *param, int *retcod, int param_len)
{
    theConfigureContextMenu = new ConfigureContextMenu();
}

//----------------------------------------------------
// Unload Handler
//     This function specifies when to unload your application from Unigraphics.
//     If your application registers a callback (from a MenuScript item or a
//     User Defined Object for example), this function MUST return
//     "AtTermination".
//
//  Available Options:
//  Immediately : unload the library as soon as the automation program has completed
//  Explicitly  : unload the library from the "Unload Shared Image" dialog
//  AtTermination : unload the library when the NX session terminates
//----------------------------------------------------
extern int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Method: ufusr_cleanup()
// You have the option of coding the cleanup routine to perform any housekeeping
// chores that may need to be performed. If you code the cleanup routine, it is
// automatically called by NX.
//------------------------------------------------------------------------------
extern void ufusr_cleanup(void)
{
    // Add your cleanup code here
}


//------------------------------------------------------------------------------
// PrintMenu
//    Prints a note and a description of the menu to the listing window.
//------------------------------------------------------------------------------
void ConfigureContextMenu::PrintMenu(MenuBar::ContextMenu* menu, 
                                     MenuBar::ContextMenuProperties* props, 
                                     NXString prefix)
{
    int numMenuEntries = menu->NumberOfEntries();

    for (int i = 0; i < numMenuEntries; i++)
    { 
        std::stringstream num;
        num << i;
        const std::string& str = num.str();

        MenuBar::ContextMenuEntry* entry = menu->GetEntry(i);
        if (entry->EntryType() == MenuBar::ContextMenuEntry::TypeSeparator)
            ConfigureContextMenu::lw->WriteLine(prefix + str.c_str() + " = --------------------");
        else
            ConfigureContextMenu::lw->WriteLine(prefix + str.c_str() + " = " + entry->Label());

        // If this entry is a submenu, write out its submenu as well.        
        if (entry->EntryType() == MenuBar::ContextMenuEntry::TypeSubmenu)
        {
            PrintMenu(menu->GetSubmenu(i), props, prefix + "  ");
        }
    }
}


//------------------------------------------------------------------------------
//------------------------- Callback Functions ---------------------------------
//------------------------------------------------------------------------------


int ConfigureContextMenu::
    CustomizeMenu(MenuBar::ContextMenu* menu, MenuBar::ContextMenuProperties* props)
{
    try
    {
        // When in the Modeling application, hide the Delete button in the Graphics Window context menu.
        int module_id;
        UF_ask_application_module(&module_id);
        if (module_id == UF_APP_MODELING && strcmp(props->Location().GetText(), "GraphicsWindow") == 0)
        {
            if (menu->HasEntryWithName("UG_EDIT_DELETE"))
            {
                MenuBar::ContextMenuEntry* deleteMenuEntry = menu->GetEntryWithName("UG_EDIT_DELETE");
                menu->HideEntry(deleteMenuEntry);
            }
        }

        // Find the last visible push-button entry on the menu
        MenuBar::ContextMenuEntry* entry = NULL;
        int numMenuEntries = menu->NumberOfEntries();
        for (int i = 0; i < numMenuEntries; i++)
        {
            MenuBar::ContextMenuEntry* entry2 = menu->GetEntry(i);

            // Identify the last menu entry which is something that can be
            // activated and which is visible and sensitive.
            if (entry2->EntryType() == MenuBar::ContextMenuEntry::TypePushButton &&
                !entry2->IsHidden() && entry2->IsSensitive())
            {
                entry = entry2;
            }
        }

        // Set identified entry as the default and move to the top of the menu.
        if (entry != NULL)
        {
            menu->SetDefaultEntry(entry);
            menu->MoveEntry(entry, 0);
        }
            
        // Add an additional menu button for a specific context.
        if ( strcmp(props->Context().GetText(), "Features.Cylinder") == 0 )
        {
            // Retrieve an NX menu button
            MenuBar::MenuButton* newButton = 
                theUI->MenuBarManager()->GetButtonFromName("UG_PREFERENCES_VISUALIZATION");

            MenuBar::ContextMenu* subMenu = menu->AddSubmenu("Custom", -1);
            subMenu->AddMenuButton(newButton, -1);
        }
            
        // Add a label to identify the context menu for Features Cylinder.
        if ( strcmp(props->Context().GetText(), "Features.Cylinder") == 0 )
        {
            // Create Label
            menu->AddMenuLabel("Features Cylinder", 0);
        }

        // Open the Print the Information window and print the menu.
        ConfigureContextMenu::lw->Open();
        ConfigureContextMenu::lw->WriteLine("Customize menu for " + props->Context() + " in " + props->Location());
        PrintMenu(menu, props, "   ");
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }

    return 0;
}
