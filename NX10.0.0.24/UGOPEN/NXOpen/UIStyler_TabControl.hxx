#ifndef NXOpen_UISTYLER_TABCONTROL_HXX_INCLUDED
#define NXOpen_UISTYLER_TABCONTROL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_TabControl.ja
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
#include <NXOpen/UIStyler_StylerItem.hxx>
#include <NXOpen/UIStyler_PageSwitchData.hxx>
#include <NXOpen/UIStyler_StylerItem.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace UIStyler
    {
        class TabControl;
    }
    namespace UIStyler
    {
        class PageSwitchData;
    }
    namespace UIStyler
    {
        class StylerEvent;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
        class TabControlImpl;
        /** Represents a Tab Control for UI Styler. 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  TabControl : public NXOpen::UIStyler::StylerItem
        {
            public: /**Called when a user switches tabs. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> SwitchHandler;
            private: TabControlImpl * m_tabcontrol_impl;
            /// \cond NX_NO_DOC 
            public: explicit TabControl(void *ptr);
            /// \endcond 
            /**Registers switch callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void AddSwitchHandler
            (
                const NXOpen::UIStyler::TabControl::SwitchHandler&  switchevent /** switchevent */ ,
                bool isDialogLaunchingEvent /** is dialog launching event */ 
            );
            /**Sets  the sensitivity of the dialog item 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /** TRUE if sensitive, FALSE if insensitive */
            );
            /**Returns  the sensitivity of the dialog item 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Sensitivity
            (
            );
            /**Sets  the visibility of the dialog item
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** TRUE if visible, FALSE if invisible */
            );
            /**Returns  the visibility of the dialog item
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Visibility
            (
            );
            /**Returns  the page switch data
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::UIStyler::PageSwitchData * PageSwitchData
            (
            );
            /** Sets focus 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFocus
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
