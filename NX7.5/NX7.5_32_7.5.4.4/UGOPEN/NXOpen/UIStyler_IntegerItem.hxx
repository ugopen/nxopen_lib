#ifndef NXOpen_UISTYLER_INTEGERITEM_HXX_INCLUDED
#define NXOpen_UISTYLER_INTEGERITEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_IntegerItem.ja
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
        class IntegerItem;
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
        class IntegerItemImpl;
        /** Represents a Integer for UI Styler. */
        class NXOPENUICPPEXPORT  IntegerItem : public UIStyler::StylerItem
        {
            public: /**Called when a dialog user enters a valid integer value and presses Return  <br> License requirements : None */
            typedef NXOpen::Callback1<NXOpen::UIStyler::DialogState, NXOpen::UIStyler::StylerEvent *> Activate;
            private: IntegerItemImpl * m_integeritem_impl;
            public: explicit IntegerItem(void *ptr);
            /**Registers activate callback. This method should be called before calling @link  UIStyler::Dialog::Show   UIStyler::Dialog::Show @endlink  or @link  UIStyler::Dialog::RegisterWithUiMenu   UIStyler::Dialog::RegisterWithUiMenu @endlink   <br> License requirements : None */
            public: void AddActivateHandler
            (
                const NXOpen::UIStyler::IntegerItem::Activate&  activateevent /** activateevent */ ,
                bool isDialogLaunchingEvent /** is dialog launching event */ 
            );
            /**Sets the value obtained from the text field. <br> License requirements : None */
            public: void SetItemValue
            (
                int itemVal /** item val */ 
            );
            /**Returns the value obtained from the text field. <br> License requirements : None */
            public: int ItemValue
            (
            );
            /**Specifies a filename that contains a bitmap definition. The filename must contain a UBM, XPM, or BMP 
                extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
                label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
                mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item. 
                 <br> License requirements : None */
            public: void SetBitmap
            (
                const NXString & bitmap /**Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Specifies descriptive text to display for the dialog item. It should describe the dialog 
                item's intended use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.  <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** String to display on the left side of the text field.  <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Sets  the sensitivity of Integer item  <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /**TRUE if sensitive, FALSE if insensitive*/
            );
            /**Returns  the sensitivity of Integer item  <br> License requirements : None */
            public: bool Sensitivity
            (
            );
            /**Sets  the visibility of the dialog item. <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /**TRUE if the dialog item is sensitive; FALSE if insensitive*/
            );
            /**Returns  the visibility of the dialog item. <br> License requirements : None */
            public: bool Visibility
            (
            );
            /** Sets focus  <br> License requirements : None */
            public: void SetFocus
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
