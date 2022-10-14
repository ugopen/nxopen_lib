#ifndef NXOpen_DRAFTING_SPECIFYRULEBUILDER_HXX_INCLUDED
#define NXOpen_DRAFTING_SPECIFYRULEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drafting_SpecifyRuleBuilder.ja
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
#include <NXOpen/Drafting_SpecifyRuleBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_drafting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drafting
    {
        class SpecifyRuleBuilder;
    }
    namespace Annotations
    {
        class Note;
    }
    class Builder;
    namespace Drafting
    {
        class _SpecifyRuleBuilderBuilder;
        class SpecifyRuleBuilderImpl;
        /** This class is used to specify knowledge fusion rule for a note object in a drawing template. 
                The rule is stored on the note and is executed when the template is instantiated.  <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateSpecifyRuleBuilder  NXOpen::Drafting::AutomationManager::CreateSpecifyRuleBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_DRAFTINGEXPORT  SpecifyRuleBuilder : public NXOpen::Builder
        {
            private: SpecifyRuleBuilderImpl * m_specifyrulebuilder_impl;
            private: friend class  _SpecifyRuleBuilderBuilder;
            protected: SpecifyRuleBuilder();
            public: ~SpecifyRuleBuilder();
            /**Returns  the rule 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Rule
            (
            );
            /**Sets  the rule 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drawing_auto ("NX Drawing Automation") */
            public: void SetRule
            (
                const NXString & rule /** rule */ 
            );
            /**Sets  the rule 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drawing_auto ("NX Drawing Automation") */
            void SetRule
            (
                const char * rule /** rule */ 
            );
            /**Returns  the note to add rule to
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::Note * Note
            (
            );
            /**Sets  the note to add rule to
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drawing_auto ("NX Drawing Automation") */
            public: void SetNote
            (
                NXOpen::Annotations::Note * note /** Note object */
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