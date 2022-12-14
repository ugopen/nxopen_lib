#ifndef NXOpen_VALIDATIONPMIPLANARCPSVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONPMIPLANARCPSVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationPMIPlanarCPSValidator.ja
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
    class ValidationPMIPlanarCPSValidator;
    class ValidationAnnotationValidator;
    class _ValidationPMIPlanarCPSValidatorBuilder;
    class ValidationPMIPlanarCPSValidatorImpl;
    /** validator for a PMI Cutting Plate  <br> This is a test class.  <br> 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationPMIPlanarCPSValidator : public ValidationAnnotationValidator
    {
        private: ValidationPMIPlanarCPSValidatorImpl * m_validationpmiplanarcpsvalidator_impl;
        private: friend class  _ValidationPMIPlanarCPSValidatorBuilder;
        protected: ValidationPMIPlanarCPSValidator();
        public: ~ValidationPMIPlanarCPSValidator();
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
