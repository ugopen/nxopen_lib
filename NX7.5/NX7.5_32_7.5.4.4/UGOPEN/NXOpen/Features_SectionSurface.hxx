#ifndef NXOpen_FEATURES_SECTIONSURFACE_HXX_INCLUDED
#define NXOpen_FEATURES_SECTIONSURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SectionSurface.ja
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
        class SectionSurface;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SectionSurfaceBuilder;
        class SectionSurfaceImpl;
        /** Represents a section surface feature */
        class NXOPENCPPEXPORT  SectionSurface : public Features::BodyFeature
        {
            private: SectionSurfaceImpl * m_sectionsurface_impl;
            private: friend class  _SectionSurfaceBuilder;
            protected: SectionSurface();
            public: ~SectionSurface();
        };
    }
}
#undef EXPORTLIBRARY
#endif
