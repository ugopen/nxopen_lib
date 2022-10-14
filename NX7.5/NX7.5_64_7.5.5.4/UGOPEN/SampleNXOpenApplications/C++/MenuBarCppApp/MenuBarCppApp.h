//----------------------------------------------------------------------------
//                  Copyright (c) 2007 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// MenuBarCppApp.h
//
// Description:
//     This demo registers an application and buttons using the C++ language.
//     See MenuBarCppApp.cpp for more detailed instructions.
//
//----------------------------------------------------------------------------

#include <iostream>
#include <uf_defs.h>
#include <uf.h>
#include <uf_ui.h>


#include <NXOpen/Session.hxx>
#include <NXOpen/MenuBar_MenuBarManager.hxx>
#include <NXOpen/MenuBar_MenuButton.hxx>
#include <NXOpen/MenuBar_MenuButtonEvent.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>


using namespace std;
using namespace NXOpen;
class CppMenuBarApplication;
extern CppMenuBarApplication *theCppMenuBarApplication;


class CppMenuBarApplication
{
    // class members
    public:
        static Session* theSession;
        static UI* theUI;
        static ListingWindow* lw;
        static int registered;

        CppMenuBarApplication();
        ~CppMenuBarApplication();

        //-----------------------
        // Callback Prototypes
        //-----------------------
        int CppMenuBarApplicationInit(void);
        int CppMenuBarApplicationEnter(void);
        int CppMenuBarApplicationExit(void);

        MenuBar::MenuBarManager::CallbackStatus PrintButtonIdCB( MenuBar::MenuButtonEvent* buttonEvent );
        MenuBar::MenuBarManager::CallbackStatus TestCallbackReturnsCB( MenuBar::MenuButtonEvent* buttonEvent );
        MenuBar::MenuBarManager::CallbackStatus PrintApplicationIdCB( MenuBar::MenuButtonEvent* buttonEvent );
        MenuBar::MenuBarManager::CallbackStatus PrintButtonDataCB( MenuBar::MenuButtonEvent* buttonEvent );
        MenuBar::MenuBarManager::CallbackStatus PrintToggleStatusCB( MenuBar::MenuButtonEvent* buttonEvent );


    private:

        //-----------------------------
        // Registers the callback in NX
        //-----------------------------
        void InitializeCallbacks();
};
