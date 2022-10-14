#ifndef NXOpen_VALIDATIONBASEARROWVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONBASEARROWVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationBaseArrowValidator.ja
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
#include <NXOpen/ValidationAnnotationValidator.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ValidationBaseArrowValidator;
    class ValidationAnnotationValidator;
    class _ValidationBaseArrowValidatorBuilder;
    class ValidationBaseArrowValidatorImpl;
    /** validator for a Base Arrow <br> This is a test class.  <br> 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationBaseArrowValidator : public NXOpen::ValidationAnnotationValidator
    {
        private: ValidationBaseArrowValidatorImpl * m_validationbasearrowvalidator_impl;
        private: friend class  _ValidationBaseArrowValidatorBuilder;
        protected: ValidationBaseArrowValidator();
        public: ~ValidationBaseArrowValidator();
    };
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