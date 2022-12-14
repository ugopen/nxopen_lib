#ifndef NXOpen_AME_CREATERULESETBUILDER_HXX_INCLUDED
#define NXOpen_AME_CREATERULESETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_CreateRuleSetBuilder.ja
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
        class CreateRuleSetBuilder;
    }
    class Builder;
    namespace AME
    {
        class _CreateRuleSetBuilderBuilder;
        class CreateRuleSetBuilderImpl;
        /**
                JA class for crete rule set
             <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateCreateRuleSetBuilder  NXOpen::AME::AMEManager::CreateCreateRuleSetBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  CreateRuleSetBuilder : public NXOpen::Builder
        {
            /**
                        Definition of the rule set types
                    */
            public: enum RulesType
            {
                RulesTypeNamingScheme/** naming scheme */ ,
                RulesTypePlcAddressingRule/** plc addressing rule */ 
            };

            private: CreateRuleSetBuilderImpl * m_createrulesetbuilder_impl;
            private: friend class  _CreateRuleSetBuilderBuilder;
            protected: CreateRuleSetBuilder();
            public: ~CreateRuleSetBuilder();
            /**Returns  the enum to rule set type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::CreateRuleSetBuilder::RulesType RuleType
            (
            );
            /**Sets  the enum to rule set type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetRuleType
            (
                NXOpen::AME::CreateRuleSetBuilder::RulesType ruleType /** ruletype */ 
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
