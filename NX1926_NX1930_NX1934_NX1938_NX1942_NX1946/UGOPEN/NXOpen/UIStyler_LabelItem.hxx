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
        class LabelItem;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
        class LabelItemImpl;
        /** Represents a Label for UI Styler. 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  LabelItem : public NXOpen::UIStyler::StylerItem
        {
            private: LabelItemImpl * m_labelitem_impl;
            /// \cond NX_NO_DOC 
            public: explicit LabelItem(void *ptr);
            /// \endcond 
            /** Specifies a filename that contains a bitmap definition. 
                The filename must contain a UBM, XPM, or BMP extension. 
                When you use this field, the system displays a bitmap for this dialog item 
                instead of a text label. When a bitmap is present, the system uses 
                the text label as tooltip text when a user places the mouse cursor over the bitmap. 
                We recommend that you use a 16x16 bitmap for this dialog item. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBitmap
            (
                const NXString & bitmapFile /** bitmap file */ 
            );
            /** Specifies a filename that contains a bitmap definition. 
                The filename must contain a UBM, XPM, or BMP extension. 
                When you use this field, the system displays a bitmap for this dialog item 
                instead of a text label. When a bitmap is present, the system uses 
                the text label as tooltip text when a user places the mouse cursor over the bitmap. 
                We recommend that you use a 16x16 bitmap for this dialog item. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetBitmap
            (
                const char * bitmapFile /** bitmap file */ 
            );
            /** Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** str label */ 
            );
            /** Specifies descriptive text to display for the dialog item. It should describe the dialog item's intended use.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetLabel
            (
                const char * strLabel /** str label */ 
            );
            /**Sets  the seisitivity of the dialog item
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSensitivity
            (
                bool type /** type */ 
            );
            /**Returns  the seisitivity of the dialog item
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
                bool type /** type */ 
            );
            /**Returns  the visibility of the dialog item
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Visibility
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
