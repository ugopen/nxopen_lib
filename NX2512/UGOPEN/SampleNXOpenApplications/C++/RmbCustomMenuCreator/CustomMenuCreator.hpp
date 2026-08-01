//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom Menu creation
//=============================================================================
//

#ifndef CUSTOMMENU_H_INCLUDED
#define CUSTOMMENU_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <iostream>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/CustomPopupMenuHandler.hxx>
#include <NXOpen/View.hxx>


using namespace std;
using namespace NXOpen;

/**
*   Class CustomMenuCreator
*   
*   Client class to load RMB custom menu 
*   
*   @author Subhasish Mukherjee, Panchu Palaniappan
*   
*   @version 1.0
*
*/
class CustomMenuCreator
{
    
public:
	/**
    *   Returns a single instance of the singleton class
    *
    *   @return CustomMenuCreator*
    */
    static CustomMenuCreator* GetInstance();

    /**
    *   Deletes the single instance of the singleton class
    *
    *   @return CustomMenuCreator*
    */
    static void RemoveInstance();
    
    /**
    *   Destructor
    *
    */
    ~CustomMenuCreator();    
    
    /**
    *   Registers the callback methods with the menu handler
    *
    */
    void RegisterCallbacks();

    /**
    *   Callback method to add custom menus/submenus
    *
    */
    int popupMenuInvokedCallBack();

    /**
    *   Callback method that gets invoked when a custom menu
    *   is selected.
    *
    */
    int addPopupMenuCallBack();
    
private:

    /**
    *   Constructor
    *
    */
    CustomMenuCreator();

    // Singleton instance of the class
    static CustomMenuCreator* m_Instance;

    // Session
    static Session *m_Session;

    // UI
    static UI *m_UI;

    // Menu Handler
    NXOpen::CustomPopupMenuHandler* m_MenuHandler;
};
#endif //CUSTOMMENU_H_INCLUDED

