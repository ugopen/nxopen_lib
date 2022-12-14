#ifndef NXOpen_VALIDATIONDATUMVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONDATUMVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationDatumValidator.ja
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
namespace NXOpen
{
    class ValidationDatumValidator;
    class ValidationAnnotationValidator;
    class _ValidationDatumValidatorBuilder;
    class ValidationDatumValidatorImpl;
    /** validator for a datum annotation  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationDatumValidator : public ValidationAnnotationValidator
    {
        private: ValidationDatumValidatorImpl * m_validationdatumvalidator_impl;
        private: friend class  _ValidationDatumValidatorBuilder;
        protected: ValidationDatumValidator();
        public: ~ValidationDatumValidator();
    };
}
#undef EXPORTLIBRARY
#endif
