#ifndef NXOpen_VALIDATIONPMIPOSITIONINGCOLLECTIONVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONPMIPOSITIONINGCOLLECTIONVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationPMIPositioningCollectionValidator.ja
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
#include <NXOpen/ValidationObjectCollectionValidator.hxx>
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
    class ValidationPMIPositioningCollectionValidator;
    class ValidationObjectCollectionValidator;
    class _ValidationPMIPositioningCollectionValidatorBuilder;
    class ValidationPMIPositioningCollectionValidatorImpl;

    /// \cond NX_NO_DOC 
    /** validator for all PMI Positioning in a part  <br> This is a test class.  <br> 
     <br>  Created in NX1926.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationPMIPositioningCollectionValidator : public NXOpen::ValidationObjectCollectionValidator
    {
        private: ValidationPMIPositioningCollectionValidatorImpl * m_validationpmipositioningcollectionvalidator_impl;
        private: friend class  _ValidationPMIPositioningCollectionValidatorBuilder;
        protected: ValidationPMIPositioningCollectionValidator();
        public: ~ValidationPMIPositioningCollectionValidator();
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
