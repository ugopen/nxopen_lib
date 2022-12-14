#ifndef NXOpen_BODYVALIDATOR_HXX_INCLUDED
#define NXOpen_BODYVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BodyValidator.ja
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
    class BodyValidator;
    class IValidator;
    class _BodyValidatorBuilder;
    class BodyValidatorImpl;
    /** validator for a Body in a part.  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  BodyValidator : public TaggedObject, public virtual IValidator
    {
        private: BodyValidatorImpl * m_bodyvalidator_impl;
        private: friend class  _BodyValidatorBuilder;
        protected: BodyValidator();
        public: ~BodyValidator();
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
