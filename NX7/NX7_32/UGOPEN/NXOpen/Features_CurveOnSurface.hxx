#ifndef NXOpen_FEATURES_CURVEONSURFACE_HXX_INCLUDED
#define NXOpen_FEATURES_CURVEONSURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CurveOnSurface.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class CurveOnSurface;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _CurveOnSurfaceBuilder;
        /** Represents a curve on surface feature */
        class NXOPENCPPEXPORT CurveOnSurface : public Features::Feature
        {
            private: friend class  _CurveOnSurfaceBuilder;
            protected: CurveOnSurface();
        };
    }
}
#undef EXPORTLIBRARY
#endif
