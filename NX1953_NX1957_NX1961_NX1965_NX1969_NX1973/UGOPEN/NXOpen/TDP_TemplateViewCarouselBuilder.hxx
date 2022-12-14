#ifndef NXOpen_TDP_TEMPLATEVIEWCAROUSELBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEVIEWCAROUSELBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplateViewCarouselBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
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
        class TemplateViewCarouselBuilder;
    }
    class LineColorFontWidthBuilder;
    class SelectDisplayableObject;
    namespace TDP
    {
        class TemplateBaseRectangleBuilder;
    }
    namespace TDP
    {
        class _TemplateViewCarouselBuilderBuilder;
        class TemplateViewCarouselBuilderImpl;
        /** Represents a Template View Carousel Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateViewCarouselBuilder  NXOpen::TDP::Manager::CreateTemplateViewCarouselBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplateViewCarouselBuilder : public NXOpen::TDP::TemplateBaseRectangleBuilder
        {
            private: TemplateViewCarouselBuilderImpl * m_templateviewcarouselbuilder_impl;
            private: friend class  _TemplateViewCarouselBuilderBuilder;
            protected: TemplateViewCarouselBuilder();
            public: ~TemplateViewCarouselBuilder();
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
            /**Returns  the selected viewport 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * SelectViewport
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
