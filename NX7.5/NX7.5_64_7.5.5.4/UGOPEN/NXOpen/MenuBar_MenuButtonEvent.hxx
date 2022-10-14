#ifndef NXOpen_MENUBAR_MENUBUTTONEVENT_HXX_INCLUDED
#define NXOpen_MENUBAR_MENUBUTTONEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MenuBar_MenuButtonEvent.ja
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
#include <NXOpen/MenuBar_MenuButton.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>
namespace NXOpen
{
    namespace MenuBar
    {
        class MenuButtonEvent;
    }
    namespace MenuBar
    {
        class MenuButton;
    }
    namespace MenuBar
    {
    }
    namespace MenuBar
    {
        class MenuButtonEventImpl;
        /** Implements the Event Object for Menu Buttons */
        class NXOPENUICPPEXPORT  MenuButtonEvent : public TransientObject
        {
            private: MenuButtonEventImpl * m_menubuttonevent_impl;
            public: explicit MenuButtonEvent(void *ptr);
            /** Frees the object from memory.  After this method is
                        called, it is illegal to use the object.  In .NET and Java,
                        his method is automatically called when the object is
                        deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~MenuButtonEvent();
            /**Returns  the activated MenuButton.  <br> License requirements : None */
            public: NXOpen::MenuBar::MenuButton * ActiveButton
            (
            );
            /**Returns  the name of the menu bar.  <br> License requirements : None */
            public: NXString MenuBarName
            (
            );
            /** Get the ancestors of the active button.  @return  The ancestors that caused the event to fire  <br> License requirements : None */
            public: std::vector<NXString> GetMenuAncestors
            (
            );
            /**Returns  the activated MenuButton's owning application identifier.  <br> License requirements : None */
            public: int ApplicationId
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif