#ifndef NXOpen_VALIDATIONLAYOUT2DLINKSVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONLAYOUT2DLINKSVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationLayout2dLinksValidator.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ValidationLayout2dLinksValidator;
    class ValidationBaseValidator;
    class _ValidationLayout2dLinksValidatorBuilder;
    class ValidationLayout2dLinksValidatorImpl;

    /// \cond NX_NO_DOC 
    /** validator for Layout2d links <br> This is a test class.  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationLayout2dLinksValidator : public NXOpen::ValidationBaseValidator
    {
        private: ValidationLayout2dLinksValidatorImpl * m_validationlayout2dlinksvalidator_impl;
        private: friend class  _ValidationLayout2dLinksValidatorBuilder;
        protected: ValidationLayout2dLinksValidator();
        public: ~ValidationLayout2dLinksValidator();
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
