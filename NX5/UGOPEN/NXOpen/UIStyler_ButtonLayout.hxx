#ifndef NXOpen_UISTYLER_BUTTONLAYOUT_HXX_INCLUDED
#define NXOpen_UISTYLER_BUTTONLAYOUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_ButtonLayout.ja
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
        class ButtonLayout;
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
        /** Represents a Button Layout for UI Styler. */
        class NXOPENUICPPEXPORT ButtonLayout : public UIStyler::StylerItem
        {
            public: typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> Activate;
            public: explicit ButtonLayout(void *ptr);
            /**Registers activate callback. This method should be called before calling @link  Dialog::Show   Dialog::Show @endlink  or @link  Dialog::RegisterWithUiMenu   Dialog::RegisterWithUiMenu @endlink   <br> License requirements : None */
            public: void AddActivateHandler
            (
                const NXOpen::UIStyler::ButtonLayout::Activate&  activateevent /** Callback for activate event */,
                bool is_dialog_launching_event /** TRUE if dialog is going to launch, FALSE if not */
            );
            /** Sets the sensitivity  <br> License requirements : None */
            public: void SetSensitivity
            (
                int subitem_index /** If the entire dialog item should change to the new sensitivity state, 
                        set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity 
                        state, set this field to its zero-based index. */,
                bool type /** TRUE if sensitive, FALSE if insensitive */
            );
            /** Gets the sensitivity  @return   <br> License requirements : None */
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
            /** Gets selected index  @return   <br> License requirements : None */
            public: int GetSelectedIndexValue
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