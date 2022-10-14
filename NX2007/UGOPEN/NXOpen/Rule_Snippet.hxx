#ifndef NXOpen_RULE_SNIPPET_HXX_INCLUDED
#define NXOpen_RULE_SNIPPET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Rule_Snippet.ja
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
#include <NXOpen/NXObject.hxx>
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
        class Snippet;
    }
    class NXObject;
    namespace Rule
    {
        class RuleInstance;
    }
    namespace Rule
    {
        class _SnippetBuilder;
        class SnippetImpl;
        /** Represents a @link NXOpen::Rule::Snippet NXOpen::Rule::Snippet@endlink   <br> This is a rule snippet object class.  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class RULEOPENCPPEXPORT  Snippet : public NXOpen::NXObject
        {
            private: SnippetImpl * m_snippet_impl;
            private: friend class  _SnippetBuilder;
            protected: Snippet();
            public: ~Snippet();
            /** Returns the rule instance of snippet 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Rule::RuleInstance * GetRuleInstance
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