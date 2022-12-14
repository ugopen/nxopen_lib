#ifndef NXOpen_VALIDATIONSYMBOLVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONSYMBOLVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationSymbolValidator.ja
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
    class ValidationSymbolValidator;
    class ValidationAnnotationValidator;
    class _ValidationSymbolValidatorBuilder;
    class ValidationSymbolValidatorImpl;
    /** validator for a drafting symbol  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationSymbolValidator : public ValidationAnnotationValidator
    {
        private: ValidationSymbolValidatorImpl * m_validationsymbolvalidator_impl;
        private: friend class  _ValidationSymbolValidatorBuilder;
        protected: ValidationSymbolValidator();
        public: ~ValidationSymbolValidator();
    };
}
#undef EXPORTLIBRARY
#endif
