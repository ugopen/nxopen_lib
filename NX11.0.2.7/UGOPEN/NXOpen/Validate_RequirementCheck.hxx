#ifndef NXOpen_VALIDATE_REQUIREMENTCHECK_HXX_INCLUDED
#define NXOpen_VALIDATE_REQUIREMENTCHECK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_RequirementCheck.ja
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
#include <NXOpen/Validation.hxx>
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class RequirementCheck;
    }
    namespace Validate
    {
        class Requirement;
    }
    class Validation;
    namespace Validate
    {
        class _RequirementCheckBuilder;
        class RequirementCheckImpl;
        /**
             Represents an NX @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  object.
             <br> To create a new instance of this class, use @link NXOpen::Validate::RequirementCheckCollection::CreateRequirementCheck  NXOpen::Validate::RequirementCheckCollection::CreateRequirementCheck @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  RequirementCheck : public NXOpen::Validation
        {
            /** This enum represents the Save Results to Teamcenter option */
            public: enum SaveResultsToTeamcenterOptions
            {
                SaveResultsToTeamcenterOptionsDoNotSave/** Do not perform save. */,
                SaveResultsToTeamcenterOptionsSaveIfPassed/** Perform save only if the result is passed. */,
                SaveResultsToTeamcenterOptionsAlwaysSave/** Always perform save */
            };

            private: RequirementCheckImpl * m_requirementcheck_impl;
            private: friend class  _RequirementCheckBuilder;
            protected: RequirementCheck();
            public: ~RequirementCheck();
            /**Returns  the name of requirement check shown in Requirements Validation dialog 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString CheckName
            (
            );
            /**Sets  the name of requirement check shown in Requirements Validation dialog 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCheckName
            (
                const NXString & checkName /** checkname */ 
            );
            /**Sets  the name of requirement check shown in Requirements Validation dialog 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetCheckName
            (
                const char * checkName /** checkname */ 
            );
            /**Returns  the Save Results to Teamcenter option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementCheck::SaveResultsToTeamcenterOptions SaveResultsToTeamcenterOption
            (
            );
            /**Sets  the Save Results to Teamcenter option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSaveResultsToTeamcenterOption
            (
                NXOpen::Validate::RequirementCheck::SaveResultsToTeamcenterOptions option /** option */ 
            );
            /**Returns  the formula of requirement check 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Formula
            (
            );
            /** Sets the formula of requirement check. The requirement check will be re-evaluated. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetFormula
            (
                const NXString & formula /** formula */ 
            );
            /** Sets the formula of requirement check. The requirement check will be re-evaluated. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetFormula
            (
                const char * formula /** formula */ 
            );
            /**Returns  the parent @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::Requirement * ParentRequirement
            (
            );
            /**Sets  the parent @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetParentRequirement
            (
                NXOpen::Validate::Requirement * parentRequirement /** parentrequirement */ 
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
