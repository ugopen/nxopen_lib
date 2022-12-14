#ifndef NXOpen_AME_EXTRACTATTRIBUTEBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXTRACTATTRIBUTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExtractAttributeBuilder.ja
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
#include <NXOpen/AME_ExtractAttributeAbsoluteBuilder.hxx>
#include <NXOpen/AME_ExtractAttributeCurrentObjectBuilder.hxx>
#include <NXOpen/AME_ExtractAttributePortBuilder.hxx>
#include <NXOpen/AME_ExtractAttributeRelativeBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class ExtractAttributeBuilder;
    }
    namespace AME
    {
        class ExtractAttributeAbsoluteBuilder;
    }
    namespace AME
    {
        class ExtractAttributeCurrentObjectBuilder;
    }
    namespace AME
    {
        class ExtractAttributePortBuilder;
    }
    namespace AME
    {
        class ExtractAttributeRelativeBuilder;
    }
    class Builder;
    namespace AME
    {
        class _ExtractAttributeBuilderBuilder;
        class ExtractAttributeBuilderImpl;
        /** Create a extract attribute   <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateExtractAttributeBuilder  NXOpen::AME::AMEManager::CreateExtractAttributeBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExtractAttributeBuilder : public NXOpen::Builder
        {
            /** extract type Type */
            public: enum Type
            {
                TypeCurrentObject/** current object */ ,
                TypeSelectObject/** select object */ ,
                TypeDetermineByExpression/** determine by expression */ ,
                TypePort/** port */ 
            };

            private: ExtractAttributeBuilderImpl * m_extractattributebuilder_impl;
            private: friend class  _ExtractAttributeBuilderBuilder;
            protected: ExtractAttributeBuilder();
            public: ~ExtractAttributeBuilder();
            /**Returns  the object type extraction
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ExtractAttributeBuilder::Type ExtractType
            (
            );
            /**Sets  the object type extraction
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetExtractType
            (
                NXOpen::AME::ExtractAttributeBuilder::Type type /** type */ 
            );
            /**Returns  the relative attribute builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ExtractAttributeRelativeBuilder * RelativeAttributeBuilder
            (
            );
            /**Returns  the absolute attribute builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ExtractAttributeAbsoluteBuilder * AbsoluteAttributeBuilder
            (
            );
            /**Returns  the current object attribute builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ExtractAttributeCurrentObjectBuilder * CurrentObjectAttributeBuilder
            (
            );
            /**Returns  the port attribute builder 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ExtractAttributePortBuilder * PortAttributeBuilder
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
