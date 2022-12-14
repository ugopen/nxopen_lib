#ifndef NXOpen_VALIDATIONDRAWINGREGIONVALIDATOR_HXX_INCLUDED
#define NXOpen_VALIDATIONDRAWINGREGIONVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ValidationDrawingRegionValidator.ja
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
    class ValidationDrawingRegionValidator;
    class ValidationBaseValidator;
    class _ValidationDrawingRegionValidatorBuilder;
    class ValidationDrawingRegionValidatorImpl;

    /// \cond NX_NO_DOC 
    /** validator for Drawing Region  <br> This is a test class.  <br> 
     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ValidationDrawingRegionValidator : public NXOpen::ValidationBaseValidator
    {
        private: ValidationDrawingRegionValidatorImpl * m_validationdrawingregionvalidator_impl;
        private: friend class  _ValidationDrawingRegionValidatorBuilder;
        protected: ValidationDrawingRegionValidator();
        public: ~ValidationDrawingRegionValidator();
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
