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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
        /** Represents a studio surface feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StudioSurfaceBuilder  NXOpen::Features::StudioSurfaceBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  StudioSurface : public NXOpen::Features::BodyFeature
        {
            private: StudioSurfaceImpl * m_studiosurface_impl;
            private: friend class  _StudioSurfaceBuilder;
            protected: StudioSurface();
            public: ~StudioSurface();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
