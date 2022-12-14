#ifndef NXOpen_FEATURES_DATUMPLANEFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_DATUMPLANEFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DatumPlaneFeature.ja
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
#include <NXOpen/Features_DatumFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class DatumPlaneFeature;
    }
    class DatumPlane;
    namespace Features
    {
        class DatumFeature;
    }
    namespace Features
    {
        class _DatumPlaneFeatureBuilder;
        /** Represents a datum plane feature */
        class NXOPENCPPEXPORT DatumPlaneFeature : public Features::DatumFeature
        {
            private: friend class  _DatumPlaneFeatureBuilder;
            protected: DatumPlaneFeature();
            /**Returns  the geometric object associated to the datum plane feature <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::DatumPlane * DatumPlane
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
