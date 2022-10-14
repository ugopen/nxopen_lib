#ifndef NXOpen_FEATURES_ADMOFFSETREGION_HXX_INCLUDED
#define NXOpen_FEATURES_ADMOFFSETREGION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AdmOffsetRegion.ja
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
        class AdmOffsetRegion;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _AdmOffsetRegionBuilder;
        class AdmOffsetRegionImpl;
        /** Represents a linear dimension feature */
        class NXOPENCPPEXPORT  AdmOffsetRegion : public Features::BodyFeature
        {
            private: AdmOffsetRegionImpl * m_admoffsetregion_impl;
            private: friend class  _AdmOffsetRegionBuilder;
            protected: AdmOffsetRegion();
            public: ~AdmOffsetRegion();
        };
    }
}
#undef EXPORTLIBRARY
#endif