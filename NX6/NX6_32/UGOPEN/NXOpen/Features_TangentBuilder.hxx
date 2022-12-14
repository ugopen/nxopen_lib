#ifndef NXOpen_FEATURES_TANGENTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TANGENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TangentBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/Features_TangentBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class TangentBuilder;
    }
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class SelectFace;
    class SelectISurface;
    namespace Features
    {
        class _TangentBuilderBuilder;
        /**
            Represents a @link Features::Tangent Features::Tangent@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateTangentBuilder Features::FeatureCollection::CreateTangentBuilder@endlink  <br> 
        Default values:
        MoveAlongFace.CoaxialEnabled: 0
        MoveAlongFace.CoplanarAxesEnabled: 0
        MoveAlongFace.CoplanarEnabled: 0
        MoveAlongFace.EqualDiameterEnabled: 0
        MoveAlongFace.ParallelEnabled: 0
        MoveAlongFace.PerpendicularEnabled: 0
        MoveAlongFace.SymmetricEnabled: 0
        MoveAlongFace.TangentEnabled: 0
        MoveAlongFace.UseFaceBrowse: 1
        */
        class NXOPENCPPEXPORT TangentBuilder : public Features::FeatureBuilder
        {
            private: friend class  _TangentBuilderBuilder;
            protected: TangentBuilder();
            /**Returns  the motion face  <br> License requirements : None */
            public: NXOpen::SelectFace * MotionFace
            (
            );
            /**Returns  the through point  <br> License requirements : None */
            public: NXOpen::Point * ThroughPoint
            (
            );
            /**Sets  the through point  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetThroughPoint
            (
                NXOpen::Point * throughPoint /** throughpoint */ 
            );
            /**Returns  the stationary face  <br> License requirements : None */
            public: NXOpen::SelectISurface * StationaryFace
            (
            );
            /**Returns  the move along faces  <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * MoveAlongFace
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
