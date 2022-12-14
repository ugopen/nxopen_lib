#ifndef NXOpen_FEATURES_HOLEPACKAGE_HXX_INCLUDED
#define NXOpen_FEATURES_HOLEPACKAGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_HolePackage.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class HolePackage;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _HolePackageBuilder;
        /** Represents a hole package and hole series feature */
        class NXOPENCPPEXPORT HolePackage : public Features::BodyFeature
        {
            private: friend class  _HolePackageBuilder;
            protected: HolePackage();
            /** Returns the number of holes and corresponding origins of the hole package  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void GetOrigins
            (
                std::vector<NXOpen::Point3d> & origins /** Array of origins. */
            );
            /** Returns the number of holes and corresponding directions of the hole package  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void GetDirections
            (
                std::vector<NXOpen::Vector3d> & directions /** Array of origins. */
            );
            /** Returns the start hole feature in hole series feature  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::Feature * GetHoleSeriesStartHoleFeature
            (
            );
            /** Returns the middle hole features in hole series feature  @return  Array of Middle Hole Features.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Features::Feature *> GetHoleSeriesMiddleHoleFeatures
            (
            );
            /** Returns the end hole feature in hole series feature  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::Feature * GetHoleSeriesEndHoleFeature
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
