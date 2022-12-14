#ifndef NXOpen_UISTYLER_PUSHBUTTON_HXX_INCLUDED
#define NXOpen_UISTYLER_PUSHBUTTON_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_PushButton.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
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
        class PushButton;
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
        /** Represents a PushButton for UI Styler */
        class NXOPENUICPPEXPORT PushButton : public UIStyler::StylerItem
        {
            public: typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> Activate;
            public: explicit PushButton(void *ptr);
            /**Registers activate callback. This method should be called before calling @link  Dialog::Show   Dialog::Show @endlink  or @link  Dialog::RegisterWithUiMenu   Dialog::RegisterWithUiMenu @endlink   <br> License requirements : None */
            public: void AddActivateHandler
            (
                const NXOpen::UIStyler::PushButton::Activate&  activateevent /** activateevent */ ,
                bool is_dialog_launching_event /** is dialog launching event */ 
            );
            /**Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
                extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
                label. When a bitmap is present, the system uses the text label as a popup hint when a user places the 
                mouse cursor over the bitmap.   <br> License requirements : None */
            public: void SetBitmap
            (
                const NXString & bitmap /**the bitmap extension   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended 
                use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.   <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & str_label /**the label string   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the senstivity of dialog. <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /** to set senstivity of dialog */
            );
            /**Returns  the senstivity of dialog. <br> License requirements : None */
            public: bool Sensitivity
            (
            );
            /**Sets  the visibility of dialog.   <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /**to set visibility of dialog */
            );
            /**Returns  the visibility of dialog.   <br> License requirements : None */
            public: bool Visibility
            (
            );
            /**Indicates that this dialog item is receiving keyboard focus.  <br> License requirements : None */
            public: void SetFocus
            (
            );
            /** Sets default action  <br> License requirements : None */
            public: void SetDefaultAction
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
