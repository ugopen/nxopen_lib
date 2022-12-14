#ifndef NXOpen_VALIDATIONHATCHVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONHATCHVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationHatchValidator.ja
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
    class ValidationHatchValidator;
    class ValidationAnnotationValidator;
    class _ValidationHatchValidatorBuilder;
    class ValidationHatchValidatorImpl;

    /// \cond NX_NO_DOC 
    /** validator for crosshatching  <br> This is a test class.  <br> 
     <br>  Created in NX7.5.1.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationHatchValidator : public NXOpen::ValidationAnnotationValidator
    {
        private: ValidationHatchValidatorImpl * m_validationhatchvalidator_impl;
        private: friend class  _ValidationHatchValidatorBuilder;
        protected: ValidationHatchValidator();
        public: ~ValidationHatchValidator();
    };

    /// \endcond 
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
