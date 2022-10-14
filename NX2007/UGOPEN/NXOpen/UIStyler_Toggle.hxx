#ifndef NXOpen_UISTYLER_TOGGLE_HXX_INCLUDED
#define NXOpen_UISTYLER_TOGGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_Toggle.ja
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
        class Toggle;
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
        class ToggleImpl;
        /** Represents a Toggle for UI Styler. 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  Toggle : public NXOpen::UIStyler::StylerItem
        {
            public: /** Called when a dialog user clicks on the button or presses the spacebar when the button has keyboard focus. 
                    Do not terminate the dialog with a value-changed callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> ValueChanged;
            private: ToggleImpl * m_toggle_impl;
            /// \cond NX_NO_DOC 
            public: explicit Toggle(void *ptr);
            /// \endcond 
            /**Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void AddValueChangedHandler
            (
                const NXOpen::UIStyler::Toggle::ValueChanged&  valuechangedevent /** Value changed event */,
                bool isDialogLaunchingEvent /** True if launch any dialog else False */
            );
            /** Sets the label to display on the right side of the toggle button. 
                If the toggle button displays a bitmap, then this text label is used as a popup hint instead
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** str label */ 
            );
            /** Sets the label to display on the right side of the toggle button. 
                If the toggle button displays a bitmap, then this text label is used as a popup hint instead
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetLabel
            (
                const char * strLabel /** str label */ 
            );
            /**Sets  an item value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetItemValue
            (
                bool itemVal /** item val */ 
            );
            /**Returns  an item value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool ItemValue
            (
            );
            /** Sets the sensitivity of the toggle button 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSensitivity
            (
                int subitemIndex /** subitem index */ ,
                bool type /** type */ 
            );
            /** Gets the sensitivity  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetSensitivity
            (
            );
            /**Sets  the visibility of the toggle
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** type */ 
            );
            /**Returns  the visibility of the toggle
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
            /** Indicates that this dialog item should override the accelerator 
                on the second mouse button, which normally accelerates to the OK button. 
                When you set this attribute, a click on the second mouse button triggers 
                this dialog item's ON/OFF state and calls the Value Changed callback 
                instead of the action of the OK button.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDefaultAction
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