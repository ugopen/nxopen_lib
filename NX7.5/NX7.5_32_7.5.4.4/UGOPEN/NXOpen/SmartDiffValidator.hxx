#ifndef NXOpen_SMARTDIFFVALIDATOR_HXX_INCLUDED
#define NXOpen_SMARTDIFFVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SmartDiffValidator.ja
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
#include <NXOpen/IValidator.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class SmartDiffValidator;
    class IValidator;
    class _SmartDiffValidatorBuilder;
    class SmartDiffValidatorImpl;
    /** Implementation for Smart File Differencing 
          */
    class NXOPENDEBUGSESSIONCPPEXPORT  SmartDiffValidator : public TaggedObject, public virtual IValidator
    {
        private: SmartDiffValidatorImpl * m_smartdiffvalidator_impl;
        private: friend class  _SmartDiffValidatorBuilder;
        protected: SmartDiffValidator();
        public: ~SmartDiffValidator();
        /**Returns  the algorithm to use for validation.  <br> License requirements : None */
        public: virtual NXOpen::ValidatorVersion ValidatorVersion
        (
        );
        /**Sets  the algorithm to use for validation.  <br> License requirements : None */
        public: virtual void SetValidatorVersion
        (
            NXOpen::ValidatorVersion version /** version */ 
        );
        /**Returns  the print level for validation.  <br> License requirements : None */
        public: virtual NXOpen::ValidatorPrintLevel ValidatorPrintLevel
        (
        );
        /**Sets  the print level for validation.  <br> License requirements : None */
        public: virtual void SetValidatorPrintLevel
        (
            NXOpen::ValidatorPrintLevel level /** level */ 
        );
        /** Deletes the validator.  <br> License requirements : None */
        public: virtual void Destroy
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif