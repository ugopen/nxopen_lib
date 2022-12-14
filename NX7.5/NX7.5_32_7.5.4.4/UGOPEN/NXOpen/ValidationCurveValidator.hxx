#ifndef NXOpen_VALIDATIONCURVEVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONCURVEVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationCurveValidator.ja
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
#include <NXOpen/ValidationBaseValidator.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class ValidationCurveValidator;
    class ValidationBaseValidator;
    class _ValidationCurveValidatorBuilder;
    class ValidationCurveValidatorImpl;
    /** validator for a drafting curve  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationCurveValidator : public ValidationBaseValidator
    {
        private: ValidationCurveValidatorImpl * m_validationcurvevalidator_impl;
        private: friend class  _ValidationCurveValidatorBuilder;
        protected: ValidationCurveValidator();
        public: ~ValidationCurveValidator();
    };
}
#undef EXPORTLIBRARY
#endif
