#ifndef NXOpen_UISTYLER_LABELITEM_HXX_INCLUDED
#define NXOpen_UISTYLER_LABELITEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_LabelItem.ja
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
        class LabelItem;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
        /** Represents a Label for UI Styler. */
        class NXOPENUICPPEXPORT LabelItem : public UIStyler::StylerItem
        {
            public: explicit LabelItem(void *ptr);
            /** Specifies a filename that contains a bitmap definition. 
                The filename must contain a UBM, XPM, or BMP extension. 
                When you use this field, the system displays a bitmap for this dialog item 
                instead of a text label. When a bitmap is present, the system uses 
                the text label as tooltip text when a user places the mouse cursor over the bitmap. 
                We recommend that you use a 16x16 bitmap for this dialog item.  <br> License requirements : None */
            public: void SetBitmap
            (
                const NXString & bitmap_file /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use. <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & str_label /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the seisitivity of the dialog item <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /** type */ 
            );
            /**Returns  the seisitivity of the dialog item <br> License requirements : None */
            public: bool Sensitivity
            (
            );
            /**Sets  the visibility of the dialog item <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** type */ 
            );
            /**Returns  the visibility of the dialog item <br> License requirements : None */
            public: bool Visibility
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif