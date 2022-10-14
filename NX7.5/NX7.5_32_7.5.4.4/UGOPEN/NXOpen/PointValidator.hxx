#ifndef NXOpen_POINTVALIDATOR_HXX_INCLUDED
#define NXOpen_POINTVALIDATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PointValidator.ja
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
    class PointValidator;
    class CurveValidator;
    class _PointValidatorBuilder;
    class PointValidatorImpl;
    /** validator for curve in a part.  <br> This is a test class. <br> */
    class NXOPENDEBUGSESSIONCPPEXPORT  PointValidator : public CurveValidator
    {
        private: PointValidatorImpl * m_pointvalidator_impl;
        private: friend class  _PointValidatorBuilder;
        protected: PointValidator();
        public: ~PointValidator();
    };
}
#undef EXPORTLIBRARY
#endif