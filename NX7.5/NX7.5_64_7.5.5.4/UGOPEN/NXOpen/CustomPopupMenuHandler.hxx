#ifndef NXOpen_CUSTOMPOPUPMENUHANDLER_HXX_INCLUDED
#define NXOpen_CUSTOMPOPUPMENUHANDLER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CustomPopupMenuHandler.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CustomPopupMenu.hxx>
#include <NXOpen/CustomPopupMenuHandler.hxx>
#include <NXOpen/CustomPopupMenuItem.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/TreeListNode.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    class CustomPopupMenuHandler;
    class CustomPopupMenu;
    class CustomPopupMenuItem;
    class TreeListNode;
    class CustomPopupMenuHandlerImpl;
    /** Represents Custom Popup Menu Handler class */
    class NXOPENUICPPEXPORT  CustomPopupMenuHandler : public TransientObject
    {
        public: /**This callback will be invoked by NX application when a RMB click is performed on 
               NX Tc Navigator application. Customer can query the selected object(s) and set 
               the cascading custom popup menu to be appended to the existing COTS (Commercial, off-the-shelf)
               RMB popup menu. <br> License requirements : None */
        typedef NXOpen::Callback0<int> AddCustomPopupMenuCallback;
        public: /**This callback will be invoked by NX when user clicks on a custom menu item. The picked menu
               and object(s) selected can be queried from within this callback.The custom implementation can 
               perform appropriate action associated with this menu pick.  <br> License requirements : None */
        typedef NXOpen::Callback0<int> CustomPopupMenuInvokedCallback;
        private: CustomPopupMenuHandlerImpl * m_custompopupmenuhandler_impl;
        public: explicit CustomPopupMenuHandler(void *ptr);
        /**Registers the add_custom_popup_menu_callback callback method with the popup menu
               handler object. <br> License requirements : None */
        public: void RegisterAddCustomPopupMenuCallback
        (
            const NXOpen::CustomPopupMenuHandler::AddCustomPopupMenuCallback&  popupCb /** popup cb */ 
        );
        /**Registers the add_custom_popup_menu_callback callback method with the popup menu
               handler object. <br> License requirements : None */
        public: void RegisterCustomPopupMenuInvokedCallback
        (
            const NXOpen::CustomPopupMenuHandler::CustomPopupMenuInvokedCallback&  popupCb /** popup cb */ 
        );
        /** Returns a list of node(s) selected during a RMB click. Customer can call this query API
                 inside the implementation of @link AddCustomPopupMenuCallback AddCustomPopupMenuCallback@endlink  or 
                 @link CustomPopupMenuInvokedCallback CustomPopupMenuInvokedCallback@endlink  to obtain additional information  <br> License requirements : None */
        public: void GetSelectedNodes
        (
            std::vector<NXOpen::TreeListNode *> & selectedNodes /** Selected Nodes */
        );
        /**Returns the menu item for the command invoked  @return  menu item  <br> License requirements : None */
        public: NXOpen::CustomPopupMenuItem * GetInvokedCommand
        (
        );
        /** Frees the object from memory.  After this method is called,
                 it is illegal to use the object.  In .NET, this method is automatically
                 called when the object is deleted by the garbage collector. 
              <br> License requirements : None */
        public: virtual ~CustomPopupMenuHandler();
        /** Adds and returns a menu to the COTS (Commercial, off-the-shelf) RMB menu @return  menu  <br> License requirements : None */
        public: NXOpen::CustomPopupMenu * AddMenu
        (
            int menuId /** Id of the menu */,
            const NXString & menuName /** name of the menu   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Adds and returns a menu item to the COTS (Commercial, off-the-shelf) RMB menu @return  menu item  <br> License requirements : None */
        public: NXOpen::CustomPopupMenuItem * AddMenuItem
        (
            int menuItemId /** Id of the menu item */,
            const NXString & menuItemName /** name of the menu item   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Adds a separator to the COTS (Commercial, off-the-shelf) RMB menu <br> License requirements : None */
        public: void AddMenuSeparator
        (
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
