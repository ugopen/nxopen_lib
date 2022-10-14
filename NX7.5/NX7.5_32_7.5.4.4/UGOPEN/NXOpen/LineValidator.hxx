#ifndef NXOpen_LINEVALIDATOR_HXX_INCLUDED
#define NXOpen_LINEVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineValidator.ja
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
#include <NXOpen/CurveValidator.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    class LineValidator;
    class CurveValidator;
    class _LineValidatorBuilder;
    class LineValidatorImpl;
    /** validator for curve in a part.  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  LineValidator : public CurveValidator
    {
        private: LineValidatorImpl * m_linevalidator_impl;
        private: friend class  _LineValidatorBuilder;
        protected: LineValidator();
        public: ~LineValidator();
    };
}
#undef EXPORTLIBRARY
#endif