#ifndef NXOpen_AME_NAMINGRULEBUILDER_HXX_INCLUDED
#define NXOpen_AME_NAMINGRULEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_NamingRuleBuilder.ja
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
#include <NXOpen/AME_SelectClassificationBuilder.hxx>
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
        class NamingRuleBuilder;
    }
    namespace AME
    {
        class SelectClassificationBuilder;
    }
    class Builder;
    namespace AME
    {
        class _NamingRuleBuilderBuilder;
        class NamingRuleBuilderImpl;
        /** Naming Rule Builder  <br> To create a new instance of this class, use @link NXOpen::AME::NamingRuleListBuilder::CreateRule  NXOpen::AME::NamingRuleListBuilder::CreateRule @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  NamingRuleBuilder : public NXOpen::Builder
        {
            private: NamingRuleBuilderImpl * m_namingrulebuilder_impl;
            private: friend class  _NamingRuleBuilderBuilder;
            protected: NamingRuleBuilder();
            public: ~NamingRuleBuilder();
            /**Returns  the classification item 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectClassificationBuilder * ClassificationItem
            (
            );
            /**Returns  the engineering object name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString EoName
            (
            );
            /**Sets  the engineering object name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetEoName
            (
                const NXString & eoName /** eoname */ 
            );
            /**Sets  the engineering object name
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetEoName
            (
                const char * eoName /** eoname */ 
            );
            /**Returns  the name in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString NameInFunction
            (
            );
            /**Sets  the name in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetNameInFunction
            (
                const NXString & nameInFunction /** nameinfunction */ 
            );
            /**Sets  the name in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetNameInFunction
            (
                const char * nameInFunction /** nameinfunction */ 
            );
            /**Returns  the name in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString NameInLocation
            (
            );
            /**Sets  the name in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetNameInLocation
            (
                const NXString & nameInLocation /** nameinlocation */ 
            );
            /**Sets  the name in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetNameInLocation
            (
                const char * nameInLocation /** nameinlocation */ 
            );
            /**Returns  the name in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString NameInProduct
            (
            );
            /**Sets  the name in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetNameInProduct
            (
                const NXString & nameInProduct /** nameinproduct */ 
            );
            /**Sets  the name in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetNameInProduct
            (
                const char * nameInProduct /** nameinproduct */ 
            );
            /**Returns  the start index in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StartIndexInFunction
            (
            );
            /**Sets  the start index in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStartIndexInFunction
            (
                int startIndex /** startindex */ 
            );
            /**Returns  the index increment in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int IndexIncrementInFunction
            (
            );
            /**Sets  the index increment in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndexIncrementInFunction
            (
                int indexIncrement /** indexincrement */ 
            );
            /**Returns  the index display digits in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int IndexDigitsInFunction
            (
            );
            /**Sets  the index display digits in function aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndexDigitsInFunction
            (
                int indexIncrement /** indexincrement */ 
            );
            /**Returns  the start index in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StartIndexInLocation
            (
            );
            /**Sets  the start index in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStartIndexInLocation
            (
                int startIndex /** startindex */ 
            );
            /**Returns  the index increment in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int IndexIncrementInLocation
            (
            );
            /**Sets  the index increment in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndexIncrementInLocation
            (
                int indexIncrement /** indexincrement */ 
            );
            /**Returns  the index display digits in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int IndexDigitsInLocation
            (
            );
            /**Sets  the index display digits in location aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndexDigitsInLocation
            (
                int indexIncrement /** indexincrement */ 
            );
            /**Returns  the start index in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StartIndexInProduct
            (
            );
            /**Sets  the start index in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStartIndexInProduct
            (
                int startIndex /** startindex */ 
            );
            /**Returns  the index increment in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int IndexIncrementInProduct
            (
            );
            /**Sets  the index increment in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndexIncrementInProduct
            (
                int indexIncrement /** indexincrement */ 
            );
            /**Returns  the index display digits in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int IndexDigitsInProduct
            (
            );
            /**Sets  the index display digits in product aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetIndexDigitsInProduct
            (
                int indexIncrement /** indexincrement */ 
            );
            /**Returns  the Classification ID 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString SelectedClassification
            (
            );
            /**Sets  the Classification ID 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectedClassification
            (
                const NXString & classification /** classification */ 
            );
            /**Sets  the Classification ID 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetSelectedClassification
            (
                const char * classification /** classification */ 
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
