#ifndef NXOpen_UISTYLER_OPTIONTOGGLE_HXX_INCLUDED
#define NXOpen_UISTYLER_OPTIONTOGGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_OptionToggle.ja
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
        class OptionToggle;
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
        class OptionToggleImpl;
        /** Represents a OptionToggle for UI Styler */
        class NXOPENUICPPEXPORT  OptionToggle : public UIStyler::StylerItem
        {
            public: /** Called when a dialog user selects an option from the menu   <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> Activate;
            public: /**Called when a dialog user clicks on the button or presses the spacebar when the button has keyboard focus. 
                Do not terminate the dialog with a value-changed callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG.  <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> ValueChanged;
            private: OptionToggleImpl * m_optiontoggle_impl;
            public: explicit OptionToggle(void *ptr);
            /**Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink   <br> License requirements : None */
            public: void AddActivateHandler
            (
                const NXOpen::UIStyler::OptionToggle::Activate&  activateevent /** Callback for activate event */,
                bool isDialogLaunchingEvent /** TRUE if dialog is going to launch, FALSE if not */
            );
            /**Registers value change callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink   <br> License requirements : None */
            public: void AddValueChangedHandler
            (
                const NXOpen::UIStyler::OptionToggle::ValueChanged&  valuechangedevent /** Callback for value changed event */,
                bool isDialogLaunchingEvent /** TRUE if dialog is going to launch, FALSE if not */
            );
            /** Set bitmaps  <br> License requirements : None */
            public: void SetBitmaps
            (
                std::vector<NXString> & bitmaps /** An array of one or more bitmap filenames. 
                        If all bitmaps for the option menu reside in the same file, specify an array of just one entry, 
                        which contains the bitmap filename for this attribute. All existing choices for the option menu 
                        remain intact when this attribute is set. Only the bitmaps are changed. Note that the number of 
                        bitmaps must match the number of existing choices.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets label  <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** Text to be set for the tool tip.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets items in the array  <br> License requirements : None */
            public: void SetItems
            (
                std::vector<NXString> & strListArray /** An array of new choices to be used for the dialog item. 
                        Note that this removes all existing choices (both text and bitmaps).   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns the items  @return  An array of items  <br> License requirements : None */
            public: std::vector<NXString> GetItems
            (
            );
            /** Sets item value  <br> License requirements : None */
            public: void SetItemValue
            (
                int subitemIndex /** Zero-based index indicating the choice to be selected. 
                        It must be in the range of existing choices.*/,
                bool setCheck /** TRUE if set, FALSE if unset. */
            );
            /** Returns item value  @return  Item value  <br> License requirements : None */
            public: int GetItemValue
            (
                bool* setCheck /** set check */ 
            );
            /** Set the sesitivity  <br> License requirements : None */
            public: void SetSensitivity
            (
                int subitemIndex /** If the entire dialog item should change to the new Sensitivity state, 
                        set this field to UF_STYLER_NO_SUB_INDEX. If only one sub-item should change to the new sensitivity 
                        state, set this field to its zero-based index. */,
                bool type /** TRUE if sensitive, FALSE if insensitive */
            );
            /** Returns the sesitivity  @return   <br> License requirements : None */
            public: bool GetSensitivity
            (
            );
            /**Sets  the visibility  <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** TRUE if visible, FALSE if invisible */
            );
            /**Returns  the visibility  <br> License requirements : None */
            public: bool Visibility
            (
            );
            /** Sets default action  <br> License requirements : None */
            public: void SetDefaultAction
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
