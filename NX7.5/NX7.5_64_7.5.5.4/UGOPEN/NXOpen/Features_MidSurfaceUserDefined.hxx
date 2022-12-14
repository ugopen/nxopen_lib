#ifndef NXOpen_FEATURES_MIDSURFACEUSERDEFINED_HXX_INCLUDED
#define NXOpen_FEATURES_MIDSURFACEUSERDEFINED_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MidSurfaceUserDefined.ja
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
        class MidSurfaceUserDefined;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _MidSurfaceUserDefinedBuilder;
        class MidSurfaceUserDefinedImpl;
        /** Represents a midsurface user defined feature */
        class NXOPENCPPEXPORT  MidSurfaceUserDefined : public Features::BodyFeature
        {
            private: MidSurfaceUserDefinedImpl * m_midsurfaceuserdefined_impl;
            private: friend class  _MidSurfaceUserDefinedBuilder;
            protected: MidSurfaceUserDefined();
            public: ~MidSurfaceUserDefined();
        };
    }
}
#undef EXPORTLIBRARY
#endif
