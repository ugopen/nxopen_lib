#ifndef NXOpen_FEATURES_COMPENSATEROUGHDATA_HXX_INCLUDED
#define NXOpen_FEATURES_COMPENSATEROUGHDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CompensateRoughData.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class CompensateRoughData;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _CompensateRoughDataBuilder;
        class CompensateRoughDataImpl;
        /** Represents a compensate rough curve or compensate rough sheet feature */
        class NXOPENCPPEXPORT  CompensateRoughData : public Features::BodyFeature
        {
            private: CompensateRoughDataImpl * m_compensateroughdata_impl;
            private: friend class  _CompensateRoughDataBuilder;
            protected: CompensateRoughData();
            public: ~CompensateRoughData();
        };
    }
}
#undef EXPORTLIBRARY
#endif