#ifndef NXOpen_VALIDATIONPARTLISTVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONPARTLISTVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationPartListValidator.ja
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
#include <NXOpen/ValidationTabnotValidator.hxx>
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
    class ValidationPartListValidator;
    class ValidationTabnotValidator;
    class _ValidationPartListValidatorBuilder;
    class ValidationPartListValidatorImpl;
    /** validator for a parts list  <br> This is a test class.  <br> 
     <br>  Created in NX7.5.1.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationPartListValidator : public ValidationTabnotValidator
    {
        private: ValidationPartListValidatorImpl * m_validationpartlistvalidator_impl;
        private: friend class  _ValidationPartListValidatorBuilder;
        protected: ValidationPartListValidator();
        public: ~ValidationPartListValidator();
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
