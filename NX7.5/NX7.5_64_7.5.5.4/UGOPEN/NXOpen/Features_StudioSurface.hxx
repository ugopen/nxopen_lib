#ifndef NXOpen_FEATURES_STUDIOSURFACE_HXX_INCLUDED
#define NXOpen_FEATURES_STUDIOSURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_StudioSurface.ja
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
        class StudioSurface;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _StudioSurfaceBuilder;
        class StudioSurfaceImpl;
        /** Represents a studio surface feature */
        class NXOPENCPPEXPORT  StudioSurface : public Features::BodyFeature
        {
            private: StudioSurfaceImpl * m_studiosurface_impl;
            private: friend class  _StudioSurfaceBuilder;
            protected: StudioSurface();
            public: ~StudioSurface();
        };
    }
}
#undef EXPORTLIBRARY
#endif