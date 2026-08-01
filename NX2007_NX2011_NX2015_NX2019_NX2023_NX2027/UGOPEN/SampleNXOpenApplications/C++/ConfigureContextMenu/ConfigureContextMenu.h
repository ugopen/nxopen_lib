//----------------------------------------------------------------------------
//   Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc.
//                         All rights reserved
//----------------------------------------------------------------------------
// 
//
// ConfigureContextMenu.h
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

#include <iostream>
#include <uf.h>
#include <uf_ui.h>

#include <NXOpen/Session.hxx>
#include <NXOpen/MenuBar_ContextMenu.hxx>
#include <NXOpen/MenuBar_ContextMenuEntry.hxx>
#include <NXOpen/MenuBar_ContextMenuProperties.hxx>
#include <NXOpen/MenuBar_MenuBarManager.hxx>
#include <NXOpen/MenuBar_MenuButton.hxx>
#include <NXOpen/MenuBar_MenuButtonEvent.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>


using namespace std;
using namespace NXOpen;
class ConfigureContextMenu;

class ConfigureContextMenu
{
    // class members
    public:
        static Session* theSession;
        static UI* theUI;
        static ListingWindow* lw;

        ConfigureContextMenu();
        ~ConfigureContextMenu();

        //-----------------------
        // Callback Prototypes
        //-----------------------

        int CustomizeMenu(
            MenuBar::ContextMenu* menu, MenuBar::ContextMenuProperties* props);


    private:

        //-----------------------------
        // Prints a note and a description of the menu to the listing window.
        //-----------------------------
        void PrintMenu(MenuBar::ContextMenu* menu, 
            MenuBar::ContextMenuProperties* props, NXString prefix = "   ");
};
