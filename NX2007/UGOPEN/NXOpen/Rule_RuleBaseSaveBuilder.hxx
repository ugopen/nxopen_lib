#ifndef NXOpen_RULE_RULEBASESAVEBUILDER_HXX_INCLUDED
#define NXOpen_RULE_RULEBASESAVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_RuleBaseSaveBuilder.ja
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
#include <NXOpen/PDM_PartOperationBuilder.hxx>
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
        class RuleBaseSaveBuilder;
    }
    class Builder;
    namespace PDM
    {
        class PartOperationBuilder;
    }
    namespace Rule
    {
        class _RuleBaseSaveBuilderBuilder;
        class RuleBaseSaveBuilderImpl;
        /** Represents a Builder for RuleSave functionality <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  RuleBaseSaveBuilder : public NXOpen::Builder
        {
            private: RuleBaseSaveBuilderImpl * m_rulebasesavebuilder_impl;
            private: friend class  _RuleBaseSaveBuilderBuilder;
            protected: RuleBaseSaveBuilder();
            public: ~RuleBaseSaveBuilder();
            /** The rule folder path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFolderPath
            (
                const NXString & folderPath /** Rule folder path */
            );
            /** The rule folder path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetFolderPath
            (
                const char * folderPath /** Rule folder path */
            );
            /** The rule file name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRuleFileName
            (
                const NXString & ruleFileName /** Rule file name */
            );
            /** The rule file name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            void SetRuleFileName
            (
                const char * ruleFileName /** Rule file name */
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
            /** The property description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDescription
            (
            );
            /** Sets the description 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDescription
            (
                const std::vector<NXString> & text /** text */ 
            );
            /** Gets @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartOperationBuilder * GetPartOperationBuilder
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