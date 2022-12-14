#ifndef NXOpen_RULE_RULESAVEASBUILDER_HXX_INCLUDED
#define NXOpen_RULE_RULESAVEASBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_RuleSaveAsBuilder.ja
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
#include <NXOpen/Rule_RuleBaseSaveBuilder.hxx>
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
        class RuleSaveAsBuilder;
    }
    namespace Rule
    {
        class RuleBaseSaveBuilder;
    }
    namespace Rule
    {
        class _RuleSaveAsBuilderBuilder;
        class RuleSaveAsBuilderImpl;
        /** Represents a Builder for RuleSaveAs functionality <br> To create a new instance of this class, use @link NXOpen::Rule::RuleManager::CreateRuleSaveAsBuilder  NXOpen::Rule::RuleManager::CreateRuleSaveAsBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  RuleSaveAsBuilder : public NXOpen::Rule::RuleBaseSaveBuilder
        {
            private: RuleSaveAsBuilderImpl * m_rulesaveasbuilder_impl;
            private: friend class  _RuleSaveAsBuilderBuilder;
            protected: RuleSaveAsBuilder();
            public: ~RuleSaveAsBuilder();
            /**Sets the container 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void PreCommit
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
