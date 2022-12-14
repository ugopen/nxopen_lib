#ifndef NXOpen_TDP_TEMPLATEVIEWPORTBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEVIEWPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplateViewportBuilder.ja
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
#include <NXOpen/LineColorFontWidthBuilder.hxx>
#include <NXOpen/TDP_TemplateBaseRectangleBuilder.hxx>
#include <NXOpen/libtdpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace TDP
    {
        class TemplateViewportBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace TDP
    {
        class TemplateBaseRectangleBuilder;
    }
    namespace TDP
    {
        class _TemplateViewportBuilderBuilder;
        class TemplateViewportBuilderImpl;
        /** Represents a Template Viewport Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateViewportBuilder  NXOpen::TDP::Manager::CreateTemplateViewportBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplateViewportBuilder : public NXOpen::TDP::TemplateBaseRectangleBuilder
        {
            private: TemplateViewportBuilderImpl * m_templateviewportbuilder_impl;
            private: friend class  _TemplateViewportBuilderBuilder;
            protected: TemplateViewportBuilder();
            public: ~TemplateViewportBuilder();
            /**Returns  the show border toggle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowBorder
            (
            );
            /**Sets  the show border toggle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowBorder
            (
                bool showBorder /** showborder */ 
            );
            /**Returns  the color and width 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * ColorWidth
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
