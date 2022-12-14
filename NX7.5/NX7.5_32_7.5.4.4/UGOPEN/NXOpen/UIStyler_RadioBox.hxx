#ifndef NXOpen_UISTYLER_RADIOBOX_HXX_INCLUDED
#define NXOpen_UISTYLER_RADIOBOX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_RadioBox.ja
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
namespace NXOpen
{
    namespace UIStyler
    {
        class RadioBox;
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
        class RadioBoxImpl;
        /** Represents a RadioBox for UI Styler */
        class NXOPENUICPPEXPORT  RadioBox : public UIStyler::StylerItem
        {
            public: /**Called when a dialog user click on a button in the radio box.
                Do not terminate the dialog with a value-changed callback. 
                The dialog should always return UF_UI_CB_CONTINUE_DIALOG.   <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> ValueChanged;
            private: RadioBoxImpl * m_radiobox_impl;
            public: explicit RadioBox(void *ptr);
            /**Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink   <br> License requirements : None */
            public: void AddValueChangedHandler
            (
                const NXOpen::UIStyler::RadioBox::ValueChanged&  valuechangedevent /** Callback for value changed event */,
                bool isDialogLaunchingEvent /** TRUE if dialog is going to launch, FALSE if not */
            );
            /** Sets label  <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** Text to be set for the descriptive label   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the item value  <br> License requirements : None */
            public: void SetItemValue
            (
                int itemVal /** Zero-based index indicating the choice to be selected. 
                    It must be in the range of existing choices.*/
            );
            /**Returns  the item value  <br> License requirements : None */
            public: int ItemValue
            (
            );
            /** Sets the sensitivity  <br> License requirements : None */
            public: void SetSensitivity
            (
                int subitemIndex /** subitem index */ ,
                bool type /** TRUE if visible, FALSE if invisible */
            );
            /** Gets the sensitivity  @return   <br> License requirements : None */
            public: bool GetSensitivity
            (
            );
            /**Sets  the visibility  <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** TRUE if sensitive, FALSE if insensitive */
            );
            /**Returns  the visibility  <br> License requirements : None */
            public: bool Visibility
            (
            );
            /** Set default action  <br> License requirements : None */
            public: void SetDefaultAction
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
