#ifndef NXOpen_UISTYLER_WIDESTRING_HXX_INCLUDED
#define NXOpen_UISTYLER_WIDESTRING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_WideString.ja
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
        class WideString;
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
        class WideStringImpl;
        /** Represents a WideString for UI Styler 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  WideString : public NXOpen::UIStyler::StylerItem
        {
            public: /** Called when a dialog user enters a character string and presses Return.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> Activate;
            private: WideStringImpl * m_widestring_impl;
            /// \cond NX_NO_DOC 
            public: explicit WideString(void *ptr);
            /// \endcond 
            /**Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void AddActivateHandler
            (
                const NXOpen::UIStyler::WideString::Activate&  activateevent /** activateevent */ ,
                bool isDialogLaunchingEvent /** is dialog launching event */ 
            );
            /**Sets  the string value for this dialog item.
                 It can be the initial value that is programmatically defined, or interactively entered by the user. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetItemValue
            (
                const NXString & itemValue /** item value */ 
            );
            /**Sets  the string value for this dialog item.
                 It can be the initial value that is programmatically defined, or interactively entered by the user. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetItemValue
            (
                const char * itemValue /** item value */ 
            );
            /**Returns  the string value for this dialog item.
                 It can be the initial value that is programmatically defined, or interactively entered by the user. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ItemValue
            (
            );
            /** Specifies descriptive text to display for the dialog item. 
                It should describe the dialog item's intended use
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** Label string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Specifies descriptive text to display for the dialog item. 
                It should describe the dialog item's intended use
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetLabel
            (
                const char * strLabel /** Label string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the sensitivity of the wide string
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /** type */ 
            );
            /**Returns  the sensitivity of the wide string
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Sensitivity
            (
            );
            /**Sets  the visibility of the wide string
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** type */ 
            );
            /**Returns  the visibility of the wide string
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Visibility
            (
            );
            /** Indicates that this dialog item is receiving keyboard focus.
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
