#ifndef NXOpen_AME_EXTRACTATTRIBUTERELATIVEBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXTRACTATTRIBUTERELATIVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExtractAttributeRelativeBuilder.ja
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
#include <NXOpen/AME_SelectionEngineeringObjectDefinitionBuilder.hxx>
#include <NXOpen/AME_ExtractAttributeBaseBuilder.hxx>
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
        class ExtractAttributeRelativeBuilder;
    }
    namespace AME
    {
        class ExtractAttributeBaseBuilder;
    }
    namespace AME
    {
        class SelectionEngineeringObjectDefinitionBuilder;
    }
    class Expression;
    class NXObject;
    namespace AME
    {
        class _ExtractAttributeRelativeBuilderBuilder;
        class ExtractAttributeRelativeBuilderImpl;
        /** Create a extract attribute   <br> This object does not need a creator.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExtractAttributeRelativeBuilder : public NXOpen::AME::ExtractAttributeBaseBuilder
        {
            private: ExtractAttributeRelativeBuilderImpl * m_extractattributerelativebuilder_impl;
            private: friend class  _ExtractAttributeRelativeBuilderBuilder;
            protected: ExtractAttributeRelativeBuilder();
            public: ~ExtractAttributeRelativeBuilder();
            /**Returns  the object to hold the type id
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::NXObject * TypeProperty
            (
            );
            /**Returns  the expression for the relative formula
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::Expression * Expression
            (
            );
            /**Returns  the object to hold the attribute list to select the attribute name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectionEngineeringObjectDefinitionBuilder * SelectType
            (
            );
            /**Returns  the object found by the relative formula
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::NXObject * ObjectFromExp
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