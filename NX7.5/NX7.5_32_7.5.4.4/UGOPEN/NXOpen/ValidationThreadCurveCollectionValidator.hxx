#ifndef NXOpen_VALIDATIONTHREADCURVECOLLECTIONVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONTHREADCURVECOLLECTIONVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationThreadCurveCollectionValidator.ja
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
#include <NXOpen/ValidationCurveCollectionValidator.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class ValidationThreadCurveCollectionValidator;
    class ValidationCurveCollectionValidator;
    class _ValidationThreadCurveCollectionValidatorBuilder;
    class ValidationThreadCurveCollectionValidatorImpl;
    /** validator for all thread curves in a part  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationThreadCurveCollectionValidator : public ValidationCurveCollectionValidator
    {
        private: ValidationThreadCurveCollectionValidatorImpl * m_validationthreadcurvecollectionvalidator_impl;
        private: friend class  _ValidationThreadCurveCollectionValidatorBuilder;
        protected: ValidationThreadCurveCollectionValidator();
        public: ~ValidationThreadCurveCollectionValidator();
    };
}
#undef EXPORTLIBRARY
#endif