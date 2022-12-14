#ifndef NXOpen_VALIDATIONSURFACEFINISHVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONSURFACEFINISHVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationSurfaceFinishValidator.ja
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
#include <NXOpen/ValidationSymbolValidator.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class ValidationSurfaceFinishValidator;
    class ValidationSymbolValidator;
    class _ValidationSurfaceFinishValidatorBuilder;
    class ValidationSurfaceFinishValidatorImpl;
    /** validator for a surface finish symbol  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationSurfaceFinishValidator : public ValidationSymbolValidator
    {
        private: ValidationSurfaceFinishValidatorImpl * m_validationsurfacefinishvalidator_impl;
        private: friend class  _ValidationSurfaceFinishValidatorBuilder;
        protected: ValidationSurfaceFinishValidator();
        public: ~ValidationSurfaceFinishValidator();
    };
}
#undef EXPORTLIBRARY
#endif
