#ifndef NXOpen_TDP_TEMPLATEPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplatePropertiesBuilder.ja
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
        class TemplatePropertiesBuilder;
    }
    class Builder;
    namespace TDP
    {
        class _TemplatePropertiesBuilderBuilder;
        class TemplatePropertiesBuilderImpl;
        /** Represents a Template Properties Builder  <br> No KF support.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplatePropertiesBuilder : public NXOpen::Builder
        {
            /** represents the template format */
            public: enum TemplateFormatEnum
            {
                TemplateFormatEnumFormat3DPDF/** 3D PDF format */,
                TemplateFormatEnumFormatJTplusPDF/** JT plus PDF format */
            };

            private: TemplatePropertiesBuilderImpl * m_templatepropertiesbuilder_impl;
            private: friend class  _TemplatePropertiesBuilderBuilder;
            protected: TemplatePropertiesBuilder();
            public: ~TemplatePropertiesBuilder();
            /**Returns  the template format 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplatePropertiesBuilder::TemplateFormatEnum TemplateFormat
            (
            );
            /**Sets  the template format 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTemplateFormat
            (
                NXOpen::TDP::TemplatePropertiesBuilder::TemplateFormatEnum templateFormat /** templateformat */ 
            );
            /**Returns  the presentation name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PresentationName
            (
            );
            /**Sets  the presentation name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPresentationName
            (
                const NXString & presentationName /** presentationname */ 
            );
            /**Sets  the presentation name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            void SetPresentationName
            (
                const char * presentationName /** presentationname */ 
            );
            /** Returns the description 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDescription
            (
            );
            /** Sets the description 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDescription
            (
                const std::vector<NXString> & description /** description */ 
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
