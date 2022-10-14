//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom Menu creation
//=============================================================================
//

//==============================================================================
//  Purpose:  This file contains C++ source to guide you in adding the 
//   Custom menu to Tc navigator popupMenus  . 
//
//  The information in this file provides you with the following:
//
//  1.  How to Register the Custom popup menu callbacks
//  2.  How to access data from the popupMenu call backs
//  3.  How to add data the popuMenus.
//==============================================================================


#include "CustomMenuCreator.hpp"
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/PDM_PdmNavigatorNode.hxx>
#include <string.h>
using namespace NXOpen;
// using namespace NXOpen::CustomPopupMenu;


/* Include files */
#include <sstream>
#include <iostream>
using std::ostringstream;
using std::endl;    
using std::ends;
using std::cerr;

#include <uf.h>
#include <uf_ui.h>
#include <uf_exit.h>
#include <uf_ugmgr.h>

#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))




//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(CustomMenuCreator::m_Session) = 0;
UI *(CustomMenuCreator::m_UI) = 0;

CustomMenuCreator* CustomMenuCreator::m_Instance = 0;


static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133];
        // use string method to replace deprecated sprintf function.
        std::string formattedMessage;
        std::ostringstream temp;
        temp << "*** ERROR code " << irc << " at line " << line << " in " << file << ":\n+++ ";
        formattedMessage = temp.str();

        UF_get_fail_message(irc, err);
        UF_print_syslog(const_cast<char *>(formattedMessage.c_str()), FALSE);
        UF_print_syslog(err, FALSE);
        UF_print_syslog("\n", FALSE);
        UF_print_syslog(call, FALSE);
        UF_print_syslog(";\n", FALSE);
        
        if (!UF_UI_open_listing_window())
        {
            UF_UI_write_listing_window(formattedMessage.c_str());
            UF_UI_write_listing_window(err);
            UF_UI_write_listing_window("\n");
            UF_UI_write_listing_window(call);
            UF_UI_write_listing_window(";\n");
        }
    }
    
    return(irc);
}


//--------------------------------------------------------------------------------
CustomMenuCreator::CustomMenuCreator()
: m_MenuHandler(0)
{
}

//------------------------------------------------------------------------------
CustomMenuCreator::~CustomMenuCreator()
{
    //
    // Menu handler must be deleted when the DLL gets unloaded
    // this will ensure that callbacks get unregistered.
    //
    if (m_MenuHandler != 0)
    {
        delete m_MenuHandler;
        m_MenuHandler = 0;
    }
}



//--------------------------------------------------------------------------------
CustomMenuCreator* CustomMenuCreator::GetInstance()
{
    if (m_Instance == 0)
    {
        m_Instance = new CustomMenuCreator();
    }
    return m_Instance;
}

//--------------------------------------------------------------------------------
void CustomMenuCreator::RemoveInstance()
{
    if (m_Instance != 0)
    {
        delete m_Instance;
        m_Instance=0;
    }
}

//--------------------------------------------------------------------------------
void CustomMenuCreator::RegisterCallbacks()
{
    if (m_MenuHandler != 0)
    {
        //
        // Menu handler has already been created and callbacks registered
        //
        return;
    }
    try
    {
        // Initialize the NX Open C++ API environment
        m_Session = NXOpen::Session::GetSession();
        
        //
        // Get The NX open UI object
        //
        CustomMenuCreator::m_UI = UI::GetUI();
        
        //
        //Create Popup Menu Handler 
        //
        m_MenuHandler = CustomMenuCreator::m_UI->CreateCustomPopupMenuHandler();
        
        // Registration of callback functions
        
        // registers the AddPopupMenu Call back
        m_MenuHandler->RegisterAddCustomPopupMenuCallback (make_callback(this, &CustomMenuCreator::addPopupMenuCallBack));
        //theMenuHandler->RegisterAddCustomPopupMenuCallback (make_callback(&CustomMenuCreator::addPopupMenuCallBack));
        // registers the popupMeny Invoked call back 
        m_MenuHandler->RegisterCustomPopupMenuInvokedCallback(make_callback(this,&CustomMenuCreator::popupMenuInvokedCallBack));
        // theMenuHandler->RegisterCustomPopupMenuInvokedCallback(make_callback(&CustomMenuCreator::popupMenuInvokedCallBack));
        
    }
    catch (const NXOpen::NXException& ex)
    {
        if (m_MenuHandler != 0)
        {
            delete m_MenuHandler;
            m_MenuHandler = 0;
        }
        const char* str = ex.Message();
        std::cerr << "Caught exception" << ex.Message() << std::endl;
        throw;
    }
}


//-------------------------------------------------------------------------------
extern DllExport void ufsta( char *param, int *returnCode, int rlen )
{
    
    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) ) 
    {
        /* Failed to initialize */
        return;
    }
    
    try
    {
        CustomMenuCreator *pMenuCreator = CustomMenuCreator::GetInstance();
        pMenuCreator->RegisterCallbacks();
    }
    catch(exception& ex)
    {
        
    }
}

//-------------------------------------------------------------------------------
extern DllExport void ufusr( char *param, int *returnCode, int rlen )
{
    /* Initialize the API environment */
    if( UF_CALL(UF_initialize()) ) 
    {
        /* Failed to initialize */
        return;
    }
    
    try
    {
        CustomMenuCreator *pMenuCreator = CustomMenuCreator::GetInstance();
        pMenuCreator->RegisterCallbacks();
    }
    catch(exception& ex)
    {
    }
}

/*****************************************************************************
 **  Utilities
 *****************************************************************************/

/* Unload Handler
 **     This function specifies when to unload your application from NX.
 **     If your application registers a callback (from a MenuScript item or a
 **     User Defined Object for example), this function MUST return
 **     "UF_UNLOAD_UG_TERMINATE". */

extern int ufusr_ask_unload( void )
{
    // Terminates client application at the request of the user
    return UF_UNLOAD_SEL_DIALOG;
    
    // Terminates client application when NX terminates
    // return( UF_UNLOAD_UG_TERMINATE );
}


//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    try
    {
        // Delte the custom application object which will delete menu handler
        // object ( which ensures all the callbacks are unregistered)
        CustomMenuCreator::RemoveInstance();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
    }
}


//------------------------------------------------------------------------------

int CustomMenuCreator::popupMenuInvokedCallBack()
{   
    //
    // The invoked menu item can be queried. Menu Item can be again queried for
    // ID and name.
    //
    NXOpen::CustomPopupMenuItem* pMenuItem = m_MenuHandler->GetInvokedCommand();
    
    //
    // The List of nodes selected in the Tree  can be queried. This information can be
    // used by the client application to determine the type of menus that needs to be
    // added.
    //
    std::vector<NXOpen::TreeListNode*> selectedNodes;
    m_MenuHandler->GetSelectedNodes(selectedNodes);
    
    std::vector<NXOpen::NXString> uids;
    std::vector<NXOpen::NXString> nodeTypes;
    for (int i=0; i < selectedNodes.size(); i++)
    {
        //
        // For each Object returned in the List the UID and Node Type can be queried. Need
        // to cast the object to NXOpen::PDM::PdmNavigatorNode before quering the UID and Type.
        //
        
        NXOpen::PDM::PdmNavigatorNode *selnode = dynamic_cast<NXOpen::PDM::PdmNavigatorNode *> (selectedNodes[i]);
        NXOpen::NXString uid = selnode->GetUid();
        NXOpen::NXString nodeType = selnode->GetNodeType();
        
        uids.push_back (uid);
        nodeTypes.push_back (nodeType);
    }
    
    ListingWindow* lw = m_Session->ListingWindow();
    if (lw != 0)
    {
        lw->Open();
        lw->WriteLine(" ");
        lw->WriteLine("Inside popupMenuInvokedCallBack Callback ");
        lw->WriteLine("COMMAND NAME: ");
        lw->WriteLine(pMenuItem->GetName());
        lw->WriteLine("SELECTED NODE UIDS: ");
        for (int i=0; i < uids.size(); i++)
        {
            lw->WriteLine(uids[i]);
        }
        
        lw->WriteLine("SELECTED NODE TYPES: ");
        for (int i=0; i < nodeTypes.size(); i++)
        {
            lw->WriteLine(nodeTypes[i]);
        }
        
        
        //
        // Follwing is a sample code to demonstrate how to make Tc user exists call using the above information.
        // In order to use this code need to customize Teamcenter user exists. For details please look at
        // Teamcenter documentation.
        //
        
        if (strcmp (pMenuItem->GetName().getText(), "Revise") == 0)
        {
            lw->WriteLine("NEW REVISION ID: ");
            lw->WriteLine ("Implement Teamcenter user exits function to show output");
            //
            // Uncomment code below after implementing the user exits method
            //
            
            // int errorCode =0;
            // char* name =0;
            // UF_UGMGR_invoke_pdm_server( 2,const_cast <char*>(uids[0].getUTF8Text()), &errorCode, &name);
            // lw->WriteLine(name);
            // UF_free(name);
        }
        else
        {
            lw->WriteLine("SELECTED OBJECT NAMES: ");
            lw->WriteLine ("Implement Teamcenter user exits function to show output");
            //
            // Uncomment code below after implementing the user exits method
            //
            
            // for (int i=0; i < uids.size(); i++)
            // {
            //    int errorCode =0;
            //    char* name =0;
            //    UF_UGMGR_invoke_pdm_server( 1,const_cast <char*>(uids[i].getUTF8Text()), &errorCode, &name);
            //    lw->WriteLine(name);
            //    UF_free(name);
            // }
        }
    }
    
    delete pMenuItem;
    return 0;
}

//-------------------------------------------------------------------------------------
int CustomMenuCreator::addPopupMenuCallBack()
{
    NXOpen::CustomPopupMenuItem *pItemMM1=0;
    NXOpen::CustomPopupMenu *pMenuMM2=0;
    NXOpen::CustomPopupMenuItem *pItemMM3=0;
    NXOpen::CustomPopupMenuItem *pItemMM4=0;
    NXOpen::CustomPopupMenuItem *pSubMenuSM21=0;
    NXOpen::CustomPopupMenu *pSubMenuSM22=0;
    NXOpen::CustomPopupMenuItem *pSubMenuSM221=0;
    
    try
    {
        //
        // The List of object selected in the Tree  can be queried.
        //
        std::vector<NXOpen::TreeListNode*> selectedObjs;
        m_MenuHandler->GetSelectedNodes(selectedObjs);
        //
        // The selected object(s) can be queried. Following is an example of using 
        // a single selected object. For multiple selection object see the popupMenuInvokedCallBack()
        // example code.
        //
        NXOpen::PDM::PdmNavigatorNode *selobj = dynamic_cast<NXOpen::PDM::PdmNavigatorNode *> (selectedObjs[0]);
        NXOpen::NXString uid = selobj->GetUid();
        NXOpen::NXString objectType = selobj->GetNodeType();
        
        //
        // Add the Top Level Menus/Separators. Top level menus/menu items/seperators
        // must be added by calling menu handler. Subsequent sublevel menus/menu items/seperators
        // can be added by calling add methods on the corresponding parent menu/submenu.
        //
        m_MenuHandler->AddMenuSeparator();
        pItemMM1 = m_MenuHandler->AddMenuItem(1,"Main Menu 1");
        
        pMenuMM2 = m_MenuHandler->AddMenu (2,"Main Menu 2");
        
        //
        // Add the First Level Menus/Separators to "Main Menu 2"
        //
        pSubMenuSM21 = pMenuMM2->AddMenuItem(3, "Sub Menu 2-1");
        pMenuMM2->AddMenuSeparator();
        pSubMenuSM22 = pMenuMM2->AddMenu (4, "Sub Menu 2-2");
        
        // 
        // Add Second Level Menu to "Sub Menu 2-2"
        //
        pSubMenuSM221 = pSubMenuSM22->AddMenuItem (5,"Sub Menu 2-2-1");
        
        pItemMM3 = m_MenuHandler->AddMenuItem (6,"Revise");
        if ((selectedObjs.size() == 1) && (strcmp (objectType.getText(), "ItemRevision") == 0))
        {
            //
            // Create an new menu only when there is 1 selection and the selection is ItemRevision
            //
            pItemMM4 = m_MenuHandler->AddMenuItem(7,"Main Menu 3");
        }
        else
        {
            // Code below will show the number of selection objects and the object type of the
            // first selection
            
            // ListingWindow* lw = m_Session->ListingWindow();
            // if (lw != 0)
            // {
            //     lw->Open();
            //     lw->WriteLine(" ");
            //     char buffer[33];
            //     itoa(selectedObjs.size(), buffer, 10);
            //     lw->WriteLine(buffer);
            //     lw->WriteLine(objectType.getText());        
            // }
            
            // Disable the menu when multiple selection and for any selection object which is
            // not item revision
            pItemMM3->SetDisabled();
        }
        
        // All the menus/submenus created must be deleted
        delete pItemMM1;
        delete pMenuMM2;
        if (pItemMM3)
            delete pItemMM3;
        if (pItemMM4)
            delete pItemMM4;
        delete pSubMenuSM21;
        delete pSubMenuSM22;
        delete pSubMenuSM221;
    }
    catch (const NXOpen::NXException& ex)
    {
        const char* str = ex.Message();
        std::cerr << "Caught exception" << ex.Message() << std::endl;
        
        // All the menus/submenus created must be deleted
        if (pItemMM1)
            delete pItemMM1;
        if (pMenuMM2)
            delete pMenuMM2;
        if (pItemMM3)
            delete pItemMM3;
        if (pItemMM4)
            delete pItemMM4;
        if (pSubMenuSM21)
            delete pSubMenuSM21;
        if (pSubMenuSM22)
            delete pSubMenuSM22;
        if (pSubMenuSM221)
            delete pSubMenuSM221;
        throw;
    }
    
    return 0;
}


