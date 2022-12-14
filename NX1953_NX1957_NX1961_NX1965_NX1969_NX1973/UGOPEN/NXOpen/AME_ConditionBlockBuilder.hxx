#ifndef NXOpen_AME_CONDITIONBLOCKBUILDER_HXX_INCLUDED
#define NXOpen_AME_CONDITIONBLOCKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ConditionBlockBuilder.ja
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
#include <NXOpen/AME_BaseEvaluatorBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class ConditionBlockBuilder;
    }
    namespace AME
    {
        class _ConditionBlockBuilderBuilder;
        class ConditionBlockBuilderImpl;
        /** Represents an object that is used to specify conditions based on the property name, value and comparison operator <br> This object does not need a creator.  <br> 
         <br>  Created in NX12.0.1.  <br>  
        */
        class AMEOPENCPPEXPORT  ConditionBlockBuilder : public NXOpen::TaggedObject
        {
            private: ConditionBlockBuilderImpl * m_conditionblockbuilder_impl;
            private: friend class  _ConditionBlockBuilderBuilder;
            protected: ConditionBlockBuilder();
            public: ~ConditionBlockBuilder();
            /**Returns  the property name 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString PropertyName
            (
            );
            /**Sets  the property name 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPropertyName
            (
                const NXString & propertyName /** propertyname */ 
            );
            /**Sets  the property name 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPropertyName
            (
                const char * propertyName /** propertyname */ 
            );
            /**Returns  the condition type 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::BaseEvaluatorBuilder::ConditionType ComparatorType
            (
            );
            /**Sets  the condition type 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetComparatorType
            (
                NXOpen::AME::BaseEvaluatorBuilder::ConditionType comparatorType /** comparatortype */ 
            );
            /**Returns  the comparison string value 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString ComparativeValueString
            (
            );
            /**Sets  the comparison string value 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetComparativeValueString
            (
                const NXString & comparativeValueString /** comparativevaluestring */ 
            );
            /**Sets  the comparison string value 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetComparativeValueString
            (
                const char * comparativeValueString /** comparativevaluestring */ 
            );
            /**Returns  the comparison numeric value
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: double ComparativeValueNumeric
            (
            );
            /**Sets  the comparison numeric value
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetComparativeValueNumeric
            (
                double comparativeValueNumeric /** comparativevaluenumeric */ 
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
