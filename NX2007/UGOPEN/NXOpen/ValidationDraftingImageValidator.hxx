#ifndef NXOpen_VALIDATIONDRAFTINGIMAGEVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONDRAFTINGIMAGEVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationDraftingImageValidator.ja
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
    class ValidationDraftingImageValidator;
    class ValidationBaseValidator;
    class _ValidationDraftingImageValidatorBuilder;
    class ValidationDraftingImageValidatorImpl;

    /// \cond NX_NO_DOC 
    /** validator for a drafting image  <br> This is a test class.  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationDraftingImageValidator : public NXOpen::ValidationBaseValidator
    {
        private: ValidationDraftingImageValidatorImpl * m_validationdraftingimagevalidator_impl;
        private: friend class  _ValidationDraftingImageValidatorBuilder;
        protected: ValidationDraftingImageValidator();
        public: ~ValidationDraftingImageValidator();
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
