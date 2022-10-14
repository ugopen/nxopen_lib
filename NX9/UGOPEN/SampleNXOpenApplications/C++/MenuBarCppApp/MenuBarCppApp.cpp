//----------------------------------------------------------------------------
//                  Copyright (c) 2007 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// MenuBarCppApp.cpp
//
// Description:
//   This is a an example of adding a C++ application to NX.
//   In addition to using this source file and the associated header file
//   (MenuBarCppApp.h) and there are two menu files (MenuBarCppAppButton.men
//   and MenuBarCppApp.men) which are also required.
//   All of the files for this sample reside in the ugopen kit under:
//   SampleNXOpenApplications/C++/MenuBarCppApp.
//
//   Please see the "Adding Custom Applications to NX" chapter of the
//   NX Open Programmer's Guide or search the documentation for
//   "MenuBarCppApp" for a detailed description of this example.
//
//   These files are intended to provide a template that can be modified
//   by renaming the files, and renaming the variables and routines
//   to allow you create your own application.
// 
//   Additional information on MenuScript can be found in:
//     - the MenuScript User's Guide
//     - the NXOpen Programmer's Guide
//     - the NX Open C++ Reference Guide (see MenuBar)
//     - the Open C Programmer's Guide
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

#include <NXOpen/UI.hxx>
#include <NXOpen/Selection.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/ListingWindow.hxx>
#include "MenuBarCppApp.h"
#include <stdio.h>
#include <iostream>
#include <sstream>
#undef CreateDialog

//------------------------------------------------------------------------------
// Prototypes
//------------------------------------------------------------------------------
extern "C" DllExport void ufsta(char *param, int *retcod, int param_len);
extern "C" DllExport int ufusr_ask_unload();
extern "C" DllExport void ufusr_cleanup(void);


//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(CppMenuBarApplication::theSession) = NULL;
UI *(CppMenuBarApplication::theUI) = NULL;
int CppMenuBarApplication::registered = 0;
ListingWindow* CppMenuBarApplication::lw = NULL;
CppMenuBarApplication *theCppMenuBarApplication = NULL;


//------------------------------------------------------------------------------
// Constructor for CppMenuBarApplication class
//------------------------------------------------------------------------------
CppMenuBarApplication::CppMenuBarApplication()
{
    try
    {
        // Initialize the NX Open C++ API environment
        theSession = Session::GetSession();
        theUI = UI::GetUI();

        // Initialize the Open C API environment
        int errorCode = UF_initialize();
        if(0 != errorCode)
            throw NXOpen::NXException::Create(errorCode);

        // Initialize the listing window
        if( lw == NULL )
        {
            lw = theSession->ListingWindow();
        }

        // Initialize the Button Callbacks
        InitializeCallbacks();
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
    return;
}

//------------------------------------------------------------------------------
// Registers a callback for the button
//------------------------------------------------------------------------------
void CppMenuBarApplication::InitializeCallbacks()
{
    try
    {
        if( registered == 0 )
        {
            theUI->MenuBarManager()->RegisterApplication("SAMPLE_CPP_APP",
                    make_callback(this, &CppMenuBarApplication::CppMenuBarApplicationInit),
                    make_callback(this, &CppMenuBarApplication::CppMenuBarApplicationEnter),
                    make_callback(this, &CppMenuBarApplication::CppMenuBarApplicationExit),
                    true, true, true );

            theUI->MenuBarManager()->AddMenuAction("SAMPLE_CPP_APP__action1", make_callback(this, &CppMenuBarApplication::PrintButtonIdCB) );
            theUI->MenuBarManager()->AddMenuAction("SAMPLE_CPP_APP__action2", make_callback(this, &CppMenuBarApplication::TestCallbackReturnsCB) );
            theUI->MenuBarManager()->AddMenuAction("SAMPLE_CPP_APP__action3", make_callback(this, &CppMenuBarApplication::PrintApplicationIdCB) );
            theUI->MenuBarManager()->AddMenuAction("SAMPLE_CPP_APP__action4", make_callback(this, &CppMenuBarApplication::PrintButtonDataCB) );
            theUI->MenuBarManager()->AddMenuAction("SAMPLE_CPP_APP__action5", make_callback(this, &CppMenuBarApplication::PrintToggleStatusCB) );
            registered = 1;
        }
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
    return;
}


//---------------------------------------------
// Called when NX starts up
// Registers the callback with NX
//---------------------------------------------
extern "C" DllExport void ufsta(char *param, int *retcod, int param_len)
{
    theCppMenuBarApplication = new CppMenuBarApplication();
    return;
} // ufsta ends


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
extern "C" DllExport int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Method: ufusr_cleanup()
// You have the option of coding the cleanup routine to perform any housekeeping
// chores that may need to be performed. If you code the cleanup routine, it is
// automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    // Add your cleanup code here
    return;
}




//------------------------------------------------------------------------------
//------------------------- Callback Functions ---------------------------------
//------------------------------------------------------------------------------

//----------------------------------------------------
//  CppMenuBarApplicationInit()
//    Init callback is executed when the application
//    is entered.  It's used to initialize the
//    application's data.
//
//    Prints a note to the listing window.
//----------------------------------------------------
int CppMenuBarApplication::CppMenuBarApplicationInit()
{
    lw->Open();
    lw->WriteLine(" ");
    lw->WriteLine("Inside My CPP Init Callback");
    lw->WriteLine(" ");

    return 0;
}


//----------------------------------------------------
//  CppMenuBarApplicationEnter()
//    Enter callback is executed when the application
//    is selected (activated) from the pulldown menu.
//    If this is the first time entering the application,
//    the Init Proc callback will get called first to
//    initialize any data required by this callback.
//
//    Prints a note to the listing window.
//----------------------------------------------------
int CppMenuBarApplication::CppMenuBarApplicationEnter()
{
    lw->Open();
    lw->WriteLine(" ");
    lw->WriteLine("Inside My CPP Enter Callback");
    lw->WriteLine(" ");

    return 0;
}

//----------------------------------------------------
//  CppMenuBarApplicationExit()
//    Exit callback is executed when the application
//    is exited.  It's used to free (clean up) the
//    application's data.
//
//    Prints a note to the listing window.
//----------------------------------------------------
int CppMenuBarApplication::CppMenuBarApplicationExit()
{
    lw->Open();
    lw->WriteLine(" ");
    lw->WriteLine("Inside My CPP Exit Callback");
    lw->WriteLine(" ");

    return 0;
}



//------------------------------------------------------------------------------
// Callback Name: PrintButtonIdCB
//   This is a callback method associated with SAMPLE_CPP_APP__action1 action button.
//   This will get executed whenever 'Print Button ID' is selected from the
//   'Sample CPP' menu.
//   Given a button name (such as SAMPLE_CPP_APP_BUTTON1) from the user, the
//   input button's id gets printed to the listing window.
//------------------------------------------------------------------------------
MenuBar::MenuBarManager::CallbackStatus CppMenuBarApplication::PrintButtonIdCB( NXOpen::MenuBar::MenuButtonEvent* buttonEvent )
{
    if( !UF_initialize() )
    {
        int  response = 0;
        int  len = 0;
        char msg[256];

        lw->Open();
        lw->WriteLine(" ");
        lw->WriteLine("Inside PrintButtonIdCB Callback:");

        // set the default button name, to the name of the button which activated this event
        std::string name = buttonEvent->ActiveButton()->ButtonName().GetLocaleText(); 
        UF_UI_lock_ug_access( UF_UI_FROM_CUSTOM );
        response = uc1600( "Enter name of button you wish to query", const_cast<char *>(name.c_str()), &len );
        UF_UI_unlock_ug_access( UF_UI_FROM_CUSTOM );

		std::ostringstream buffer; 
        if ( response == 3 || response == 5 )
        {
            // get the button with this name
            MenuBar::MenuButton* myButton = theUI->MenuBarManager()->GetButtonFromName(const_cast<char *>(name.c_str()));
			
            if( myButton != NULL )
            {
                buffer << myButton->ButtonId(); 
                std::string msg = buffer.str(); 
                lw->WriteLine( msg );
            }
            else
            {
				buffer << name; 
                std::string msg = "    button not found " + buffer.str();
                lw->WriteLine( msg );
            }
        }
        else
        {
                buffer << response;
			    std::string msg = "    response: " + buffer.str();
                lw->WriteLine( msg );
        }
        lw->WriteLine(" ");
    }
    UF_terminate();
    return MenuBar::MenuBarManager::CallbackStatusContinue;
}


//------------------------------------------------------------------------------
// Callback Name: TestCallbackReturnsCB
//   This is a callback method associated with SAMPLE_CPP_APP__action2 action button.
//   This will get executed whenever 'Test Callback Returns' is selected from the
//   'Sample CPP' menu.
//   It will let you select the status you wish to return from this callback.
//------------------------------------------------------------------------------
MenuBar::MenuBarManager::CallbackStatus CppMenuBarApplication::TestCallbackReturnsCB( NXOpen::MenuBar::MenuButtonEvent* buttonEvent )
{
    MenuBar::MenuBarManager::CallbackStatus cb_status = MenuBar::MenuBarManager::CallbackStatusContinue;
    if( !UF_initialize() )
    {
        int  response = 0;
        int  len = 0;
		char items[5][38] = {"Continue","Cancel","Override Standard","Warning","Error"};

        lw->Open();
        lw->WriteLine(" ");
        lw->WriteLine("Inside TestCallbackReturnsCB Callback:");

        // set the default button name, to the name of the button which activated this event
		std::string name = buttonEvent->ActiveButton()->ButtonTypeName().GetLocaleText();
        UF_UI_lock_ug_access( UF_UI_FROM_CUSTOM );
        response = uc1603( "Select a return status", 0, items, 5 );
        UF_UI_unlock_ug_access( UF_UI_FROM_CUSTOM );


        if ( response == 1 || response == 5 )
        {
            // Back or Continue
            cb_status = MenuBar::MenuBarManager::CallbackStatusContinue;
            lw->WriteLine( "    Returning CallbackStatusContinue" );
        }
        else if( response == 2 || response == 6 )
        {
            // cancel
            cb_status = MenuBar::MenuBarManager::CallbackStatusCancel;
            lw->WriteLine( "    Returning CallbackStatusCancel" );
        }
        else if( response == 7 )
        {
            cb_status = MenuBar::MenuBarManager::CallbackStatusOverrideStandard;
            lw->WriteLine( "    Returning CallbackStatusOverrideStandard" );
        }
        else if( response == 8 )
        {
            cb_status = MenuBar::MenuBarManager::CallbackStatusWarning;
            lw->WriteLine( "    Returning CallbackStatusWarning" );
        }
        else if( response == 9 )
        {
            cb_status = MenuBar::MenuBarManager::CallbackStatusError;
            lw->WriteLine( "    Returning CallbackStatusError" );
        }
        lw->WriteLine(" ");
    }
    UF_terminate();
    return cb_status;
}

//------------------------------------------------------------------------------
// Callback Name: PrintApplicationIdCB
//   This is a callback method associated with SAMPLE_CPP_APP__action3 action button.
//   This will get executed whenever 'Print Application ID' is selected from the
//   'Sample CPP' menu.
//   Prints the application id of the active button.
//------------------------------------------------------------------------------
MenuBar::MenuBarManager::CallbackStatus CppMenuBarApplication::PrintApplicationIdCB( NXOpen::MenuBar::MenuButtonEvent* buttonEvent )
{
    lw->Open();
    lw->WriteLine(" ");
    lw->WriteLine("Inside PrintApplicationIdCB Callback:");
	std::ostringstream msgbuffer; 
	msgbuffer << buttonEvent->ApplicationId();
	std::string msg = "    Application Id: "+ msgbuffer.str();
    lw->WriteLine( msg );
    lw->WriteLine(" ");
    return MenuBar::MenuBarManager::CallbackStatusContinue;
}
//------------------------------------------------------------------------------
// Callback Name: PrintButtonDataCB
//   This is a callback method associated with SAMPLE_CPP_APP__action4 action button.
//   This will get executed whenever 'Print This Button Data' is selected from the
//   'Sample CPP' menu.
//   It will print lots of info about the button to the listing window.
//------------------------------------------------------------------------------
MenuBar::MenuBarManager::CallbackStatus CppMenuBarApplication::PrintButtonDataCB( NXOpen::MenuBar::MenuButtonEvent* buttonEvent )
{
    lw->Open();
    lw->WriteLine(" ");
    lw->WriteLine("Inside PrintButtonDataCB Callback:");

    std::ostringstream ButtonIdBuffer; 
	ButtonIdBuffer << buttonEvent->ActiveButton()->ButtonId();
	std::string ButtonId = "    Button Id: " + ButtonIdBuffer.str();
	lw->WriteLine( ButtonId );

	std::string ButtonName = "    Name: ";
	ButtonName += buttonEvent->ActiveButton()->ButtonName().GetLocaleText();
    lw->WriteLine( ButtonName );
    
	std::string ButtonTypeName = "    Button type name: ";
	ButtonTypeName += buttonEvent->ActiveButton()->ButtonTypeName().GetLocaleText();
	lw->WriteLine( ButtonTypeName );
    
	std::string MenubarName = "    Menubar Name: ";
	MenubarName += buttonEvent->MenuBarName().GetLocaleText();
	lw->WriteLine( MenubarName );
    
	std::ostringstream ApplicationIdBuffer;
	ApplicationIdBuffer << buttonEvent->ApplicationId();
	std::string ApplicationId = "    Application Id: ";
	ApplicationId += ApplicationIdBuffer.str();
	lw->WriteLine( ApplicationId );
    

    std::vector<NXOpen::NXString> ancestors = buttonEvent->GetMenuAncestors();
    for( int i = 0; i < ancestors.capacity(); i++ )
    {
		std::ostringstream IteratorBuffer;
		IteratorBuffer << i;
		std::string msg = "    Ancestor: ";
		msg += IteratorBuffer.str();
		msg += " ";
		msg += ancestors[i].GetLocaleText();
        lw->WriteLine(msg);
    }
    lw->WriteLine(" ");
    return MenuBar::MenuBarManager::CallbackStatusContinue;
}
//------------------------------------------------------------------------------
// Callback Name: PrintToggleStatusCB
//   This is a callback method associated with SAMPLE_CPP_APP__action5 action button.
//   This will get executed whenever 'Print This Button Data' is selected from the
//   'Sample CPP' menu.
//   It will print the current status of the toggle
//------------------------------------------------------------------------------
MenuBar::MenuBarManager::CallbackStatus CppMenuBarApplication::PrintToggleStatusCB( NXOpen::MenuBar::MenuButtonEvent* buttonEvent )
{
    lw->Open();
    lw->WriteLine(" ");
    lw->WriteLine("Inside PrintToggleStatusCB Callback:");
    if( buttonEvent->ActiveButton()->ToggleStatus() == MenuBar::MenuButton::ToggleOn )
    {
        lw->WriteLine("   The toggle is now ON");
    }
    else
    {
        lw->WriteLine("   The toggle is now OFF");
    }

    lw->WriteLine(" ");
    return MenuBar::MenuBarManager::CallbackStatusContinue;
}
