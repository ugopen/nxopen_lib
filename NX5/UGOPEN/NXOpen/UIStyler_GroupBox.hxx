#ifndef NXOpen_UISTYLER_GROUPBOX_HXX_INCLUDED
#define NXOpen_UISTYLER_GROUPBOX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_GroupBox.ja
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
        class GroupBox;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
        /** Represents a GroupBox for UI Styler. */
        class NXOPENUICPPEXPORT GroupBox : public UIStyler::StylerItem
        {
            public: explicit GroupBox(void *ptr);
            /**  <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & str_label /** Text label to display in the top line of the group box frame   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the sensitivity  <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /** TRUE if sensitive, FALSE if insensitive */
            );
            /**Returns  the sensitivity  <br> License requirements : None */
            public: bool Sensitivity
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
        };
    }
}
#undef EXPORTLIBRARY
#endif