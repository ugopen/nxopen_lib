#ifndef NXOpen_CUSTOMPOPUPMENU_HXX_INCLUDED
#define NXOpen_CUSTOMPOPUPMENU_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CustomPopupMenu.ja
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
#include <NXOpen/CustomPopupMenuItem.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    class CustomPopupMenu;
    class CustomPopupMenuItem;
    class CustomPopupMenuImpl;
    /** Represents Custom Popup Menu Item class */
    class NXOPENUICPPEXPORT  CustomPopupMenu : public CustomPopupMenuItem
    {
        private: CustomPopupMenuImpl * m_custompopupmenu_impl;
        public: explicit CustomPopupMenu(void *ptr);
        /** Adds and returns a menu item to this menu  @return  menu item  <br> License requirements : None */
        public: NXOpen::CustomPopupMenuItem * AddMenuItem
        (
            int menuItemId /** Id of the menu item */,
            const NXString & menuItemName /** name of the menu item   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Adds and returns a menu to this menu  @return  menu  <br> License requirements : None */
        public: NXOpen::CustomPopupMenu * AddMenu
        (
            int menuId /** Id of the menu */,
            const NXString & menuName /** name of the menu   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Adds a separator in the submenu  <br> License requirements : None */
        public: void AddMenuSeparator
        (
        );
        /** Frees the object from memory.  After this method is called,
                 it is illegal to use the object.  In .NET, this method is automatically
                 called when the object is deleted by the garbage collector. 
              <br> License requirements : None */
        public: virtual ~CustomPopupMenu();
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
