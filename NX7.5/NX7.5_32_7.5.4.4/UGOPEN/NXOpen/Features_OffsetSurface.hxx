#ifndef NXOpen_FEATURES_OFFSETSURFACE_HXX_INCLUDED
#define NXOpen_FEATURES_OFFSETSURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_OffsetSurface.ja
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
        class OffsetSurface;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _OffsetSurfaceBuilder;
        class OffsetSurfaceImpl;
        /** Represents a offset surface feature. */
        class NXOPENCPPEXPORT  OffsetSurface : public Features::BodyFeature
        {
            private: OffsetSurfaceImpl * m_offsetsurface_impl;
            private: friend class  _OffsetSurfaceBuilder;
            protected: OffsetSurface();
            public: ~OffsetSurface();
        };
    }
}
#undef EXPORTLIBRARY
#endif