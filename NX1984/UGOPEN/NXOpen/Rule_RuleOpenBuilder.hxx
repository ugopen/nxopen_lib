#ifndef NXOpen_RULE_RULEOPENBUILDER_HXX_INCLUDED
#define NXOpen_RULE_RULEOPENBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_RuleOpenBuilder.ja
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
#include <NXOpen/libruleopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Rule
    {
        class RuleOpenBuilder;
    }
    class Builder;
    namespace Rule
    {
        class _RuleOpenBuilderBuilder;
        class RuleOpenBuilderImpl;
        /** Represents a Builder for RuleOpen functionality <br> To create a new instance of this class, use @link NXOpen::Rule::RuleManager::CreateRuleOpenBuilder  NXOpen::Rule::RuleManager::CreateRuleOpenBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  RuleOpenBuilder : public NXOpen::Builder
        {
            private: RuleOpenBuilderImpl * m_ruleopenbuilder_impl;
            private: friend class  _RuleOpenBuilderBuilder;
            protected: RuleOpenBuilder();
            public: ~RuleOpenBuilder();
            /** The rule path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPath
            (
                const NXString & path /** Rule file path */
            );
            /** The rule path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetPath
            (
                const char * path /** Rule file path */
            );
            /**Returns  the rule name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the rule name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetName
            (
                const NXString & ruleName /** the rule name */
            );
            /**Sets  the rule name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetName
            (
                const char * ruleName /** the rule name */
            );
            /** The rule description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDescription
            (
            );
            /** Sets rule description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDescription
            (
                const std::vector<NXString> & text /** text */ 
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