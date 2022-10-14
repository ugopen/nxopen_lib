#ifndef NXOpen_FEATURES_WINDSHIELDDATUM_HXX_INCLUDED
#define NXOpen_FEATURES_WINDSHIELDDATUM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WindshieldDatum.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class WindshieldDatum;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _WindshieldDatumBuilder;
        class WindshieldDatumImpl;
        /** Represents a windshield datum feature */
        class NXOPENCPPEXPORT  WindshieldDatum : public Features::Feature
        {
            private: WindshieldDatumImpl * m_windshielddatum_impl;
            private: friend class  _WindshieldDatumBuilder;
            protected: WindshieldDatum();
            public: ~WindshieldDatum();
        };
    }
}
#undef EXPORTLIBRARY
#endif