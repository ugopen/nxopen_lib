#ifndef NXOpen_VALIDATIONDRAFTINGEDGEVDCURVECOLLECTIONVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONDRAFTINGEDGEVDCURVECOLLECTIONVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationDraftingEdgeVDCurveCollectionValidator.ja
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

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ValidationDraftingEdgeVDCurveCollectionValidator;
    class ValidationCurveCollectionValidator;
    class _ValidationDraftingEdgeVDCurveCollectionValidatorBuilder;
    class ValidationDraftingEdgeVDCurveCollectionValidatorImpl;
    /** validator for all drafting edge vdcurves in a part  <br> This is a test class.  <br> 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationDraftingEdgeVDCurveCollectionValidator : public NXOpen::ValidationCurveCollectionValidator
    {
        private: ValidationDraftingEdgeVDCurveCollectionValidatorImpl * m_validationdraftingedgevdcurvecollectionvalidator_impl;
        private: friend class  _ValidationDraftingEdgeVDCurveCollectionValidatorBuilder;
        protected: ValidationDraftingEdgeVDCurveCollectionValidator();
        public: ~ValidationDraftingEdgeVDCurveCollectionValidator();
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
