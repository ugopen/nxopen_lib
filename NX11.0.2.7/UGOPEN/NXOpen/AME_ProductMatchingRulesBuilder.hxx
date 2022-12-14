#ifndef NXOpen_AME_PRODUCTMATCHINGRULESBUILDER_HXX_INCLUDED
#define NXOpen_AME_PRODUCTMATCHINGRULESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ProductMatchingRulesBuilder.ja
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
#include <NXOpen/AME_ProductMatchingRulesBuilder.hxx>
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
        class ProductMatchingRulesBuilder;
    }
    class Builder;
    namespace AME
    {
        class _ProductMatchingRulesBuilderBuilder;
        class ProductMatchingRulesBuilderImpl;
        /** Represents Product Matching Rules class builder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateProductMatchingRulesBuilder  NXOpen::AME::AMEManager::CreateProductMatchingRulesBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ProductMatchingRulesBuilder : public NXOpen::Builder
        {
            /** Represents matching rule condition */
            public: enum Condition
            {
                ConditionValueIsEqual/** used if conditon is "Value is equal" */,
                ConditionMatch/** used if conditon is "Match" */
            };

            private: ProductMatchingRulesBuilderImpl * m_productmatchingrulesbuilder_impl;
            private: friend class  _ProductMatchingRulesBuilderBuilder;
            protected: ProductMatchingRulesBuilder();
            public: ~ProductMatchingRulesBuilder();
            /** Add new product matching rule 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddNewRule
            (
                int index /** index */ ,
                const NXString & propertyName /** propertyname */ ,
                NXOpen::AME::ProductMatchingRulesBuilder::Condition condition /** condition */ ,
                const NXString & deviceValue /** devicevalue */ ,
                const NXString & productValue /** productvalue */ 
            );
            /** Add new product matching rule 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void AddNewRule
            (
                int index /** index */ ,
                const char * propertyName /** propertyname */ ,
                NXOpen::AME::ProductMatchingRulesBuilder::Condition condition /** condition */ ,
                const char * deviceValue /** devicevalue */ ,
                const char * productValue /** productvalue */ 
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
