#ifndef NXOpen_VALIDATIONLABELONPARENTVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONLABELONPARENTVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationLabelOnParentValidator.ja
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
    class ValidationLabelOnParentValidator;
    class ValidationAnnotationValidator;
    class _ValidationLabelOnParentValidatorBuilder;
    class ValidationLabelOnParentValidatorImpl;
    /** validator for a label on parent  <br> This is a test class.  <br> 
     <br>  Created in NX7.5.1.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationLabelOnParentValidator : public NXOpen::ValidationAnnotationValidator
    {
        private: ValidationLabelOnParentValidatorImpl * m_validationlabelonparentvalidator_impl;
        private: friend class  _ValidationLabelOnParentValidatorBuilder;
        protected: ValidationLabelOnParentValidator();
        public: ~ValidationLabelOnParentValidator();
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
