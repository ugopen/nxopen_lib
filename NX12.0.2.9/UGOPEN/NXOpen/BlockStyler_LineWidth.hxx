#ifndef NXOpen_BLOCKSTYLER_LINEWIDTH_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_LINEWIDTH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_LineWidth.ja
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
#include <NXOpen/BlockStyler_UIBlock.hxx>
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
    namespace BlockStyler
    {
        class LineWidth;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _LineWidthBuilder;
        class LineWidthImpl;
        /** Represents a Line Width block
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  LineWidth : public NXOpen::BlockStyler::UIBlock
        {
            private: LineWidthImpl * m_linewidth_impl;
            private: friend class  _LineWidthBuilder;
            protected: LineWidth();
            public: ~LineWidth();
            /**Returns  the AllowDefaultWidth
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool AllowDefaultWidth
            (
            );
            /**Returns  the AllowNoChangeWidth. If true, no change in width is allowed.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool AllowNoChangeWidth
            (
            );
            /**Returns  the LabelVisibility
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool LabelVisibility
            (
            );
            /**Sets  the LabelVisibility
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLabelVisibility
            (
                bool visible /** visible */ 
            );
            /**Returns  the LineWidthValue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int LineWidthValue
            (
            );
            /**Sets  the LineWidthValue
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLineWidthValue
            (
                int widthValue /** width value */ 
            );
            /**Returns  the ShowDefaultAsOriginal. If true, default entry is shown as original.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ShowDefaultAsOriginal
            (
            );
        };
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
