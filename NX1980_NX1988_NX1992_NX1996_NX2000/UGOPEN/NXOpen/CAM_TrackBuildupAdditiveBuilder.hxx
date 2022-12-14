#ifndef NXOpen_CAM_TRACKBUILDUPADDITIVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TRACKBUILDUPADDITIVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TrackBuildupAdditiveBuilder.ja
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
#include <NXOpen/CAM_Geometry.hxx>
#include <NXOpen/CAM_MillOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class TrackBuildupAdditiveBuilder;
    }
    namespace CAM
    {
        class Geometry;
    }
    namespace CAM
    {
        class MillOperationBuilder;
    }
    namespace CAM
    {
        class _TrackBuildupAdditiveBuilderBuilder;
        class TrackBuildupAdditiveBuilderImpl;
        /** Represents a track buildup additive builder  <br> To create a new instance of this class, use @link NXOpen::CAM::OperationCollection::CreateTrackBuildupAdditiveBuilder  NXOpen::CAM::OperationCollection::CreateTrackBuildupAdditiveBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TrackBuildupAdditiveBuilder : public NXOpen::CAM::MillOperationBuilder
        {
            private: TrackBuildupAdditiveBuilderImpl * m_trackbuildupadditivebuilder_impl;
            private: friend class  _TrackBuildupAdditiveBuilderBuilder;
            protected: TrackBuildupAdditiveBuilder();
            public: ~TrackBuildupAdditiveBuilder();
            /**Returns  the check geometry builder
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * CheckGeometry
            (
            );
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
