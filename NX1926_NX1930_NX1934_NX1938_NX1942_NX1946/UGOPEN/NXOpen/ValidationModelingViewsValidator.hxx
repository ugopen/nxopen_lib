#ifndef NXOpen_VALIDATIONMODELINGVIEWSVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONMODELINGVIEWSVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationModelingViewsValidator.ja
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
#include <NXOpen/ValidationModelingViewValidator.hxx>
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
    class ValidationModelingViewsValidator;
    class ValidationModelingViewValidator;
    class _ValidationModelingViewsValidatorBuilder;
    class ValidationModelingViewsValidatorImpl;
    /** validator for all modeling views  <br> This is a test class.  <br> 
     <br>  Created in NX10.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationModelingViewsValidator : public NXOpen::ValidationModelingViewValidator
    {
        private: ValidationModelingViewsValidatorImpl * m_validationmodelingviewsvalidator_impl;
        private: friend class  _ValidationModelingViewsValidatorBuilder;
        protected: ValidationModelingViewsValidator();
        public: ~ValidationModelingViewsValidator();
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