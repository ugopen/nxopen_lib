#ifndef NXOpen_TDP_TEMPLATEPAGEBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEPAGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplatePageBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class TemplatePageBuilder;
    }
    class Builder;
    namespace TDP
    {
        class _TemplatePageBuilderBuilder;
        class TemplatePageBuilderImpl;
        /** Represents a @link TDP::TemplatePage TDP::TemplatePage@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplatePageBuilder  NXOpen::TDP::Manager::CreateTemplatePageBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplatePageBuilder : public NXOpen::Builder
        {
            /** template orientation */
            public: enum OrientationType
            {
                OrientationTypeLandscape/** landscape */ ,
                OrientationTypePortrait/** portrait */ 
            };

            /** metric template standard size */
            public: enum MetricSizeType
            {
                MetricSizeTypeA0/** a0 */ ,
                MetricSizeTypeA1/** a1 */ ,
                MetricSizeTypeA2/** a2 */ ,
                MetricSizeTypeA3/** a3 */ ,
                MetricSizeTypeA4/** a4 */ ,
                MetricSizeTypeCustom/** custom */ 
            };

            /** english template standard size */
            public: enum EnglishSizeType
            {
                EnglishSizeTypeA/** a */ ,
                EnglishSizeTypeB/** b */ ,
                EnglishSizeTypeC/** c */ ,
                EnglishSizeTypeD/** d */ ,
                EnglishSizeTypeE/** e */ ,
                EnglishSizeTypeF/** f */ ,
                EnglishSizeTypeH/** h */ ,
                EnglishSizeTypeJ/** j */ ,
                EnglishSizeTypeCustom/** custom */ 
            };

            private: TemplatePageBuilderImpl * m_templatepagebuilder_impl;
            private: friend class  _TemplatePageBuilderBuilder;
            protected: TemplatePageBuilder();
            public: ~TemplatePageBuilder();
            /**Returns  the orientation 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplatePageBuilder::OrientationType Orientation
            (
            );
            /**Sets  the orientation 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOrientation
            (
                NXOpen::TDP::TemplatePageBuilder::OrientationType orientation /** the orientation for the page */
            );
            /**Returns  the standard metric size to be used for the page to be created or edited. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplatePageBuilder::MetricSizeType StandardMetricSize
            (
            );
            /**Sets  the standard metric size to be used for the page to be created or edited. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStandardMetricSize
            (
                NXOpen::TDP::TemplatePageBuilder::MetricSizeType metricSize /** the standard metric size for the page */
            );
            /**Returns  the standard english size to be used for the page to be created or edited. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplatePageBuilder::EnglishSizeType StandardEnglishSize
            (
            );
            /**Sets  the standard english size to be used for the page to be created or edited. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStandardEnglishSize
            (
                NXOpen::TDP::TemplatePageBuilder::EnglishSizeType englishSize /** the standard english size for the page */
            );
            /**Returns  the custom or standard height for the page 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: double Height
            (
            );
            /**Sets  the custom or standard height for the page 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHeight
            (
                double customHeight /** the custom height for the page */
            );
            /**Returns  the custom or standard length to be used for the page to be created or edited. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: double Length
            (
            );
            /**Sets  the custom or standard length to be used for the page to be created or edited. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLength
            (
                double customLength /** the custom length for the page */
            );
            /**Returns  the show Page number 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowPageNumber
            (
            );
            /**Sets  the show Page number 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowPageNumber
            (
                bool showPageNumber /** show page number for the page */
            );
            /**Returns  the Page Name text 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PageName
            (
            );
            /**Sets  the Page Name text 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPageName
            (
                const NXString & pageName /** name for the page */
            );
            /**Sets  the Page Name text 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            void SetPageName
            (
                const char * pageName /** name for the page */
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