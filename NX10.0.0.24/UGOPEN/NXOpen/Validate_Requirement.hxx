#ifndef NXOpen_VALIDATE_REQUIREMENT_HXX_INCLUDED
#define NXOpen_VALIDATE_REQUIREMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_Requirement.ja
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
        class Requirement;
    }
    class NXObject;
    namespace Validate
    {
        class RequirementCheck;
    }
    namespace Validate
    {
        class _RequirementBuilder;
        class RequirementImpl;
        /**
             Represents a @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  object.
             <br> To create or edit an instance of this class, use @link NXOpen::Validate::RequirementBuilder  NXOpen::Validate::RequirementBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  Requirement : public NXOpen::NXObject
        {
            private: RequirementImpl * m_requirement_impl;
            private: friend class  _RequirementBuilder;
            protected: Requirement();
            public: ~Requirement();
            /** Creates a @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  for a requirement @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::RequirementCheck * NewCheck
            (
                const NXString & name /** name of requirement check */,
                const NXString & formula /** expression or formula of the requirement check */
            );
            /** Creates a @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  for a requirement @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            NXOpen::Validate::RequirementCheck * NewCheck
            (
                const char * name /** name of requirement check */,
                const char * formula /** expression or formula of the requirement check */
            );
            /** Deletes a user requirement and child @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  or removes a external requirement. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
            );
            /** Refreshs a requirement from external source.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void RefreshFromExternalSource
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
