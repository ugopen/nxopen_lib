#ifndef NXOpen_CAM_TURNAVOIDANCEGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNAVOIDANCEGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnAvoidanceGeomBuilder.ja
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
#include <NXOpen/CAM_FeatureGeomBuilder.hxx>
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
        class TurnAvoidanceGeomBuilder;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceApproachBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceClearanceBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceDepartureBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceFromBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceGohomeBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceReturnBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceStartBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceStartOfEngageBuilder;
    }
    namespace CAM
    {
        class _TurnAvoidanceGeomBuilderBuilder;
        class TurnAvoidanceGeomBuilderImpl;
        /** Represents a TurnAvoidanceGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateTurnAvoidanceGeomBuilder  CAM::NCGroupCollection::CreateTurnAvoidanceGeomBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnAvoidanceGeomBuilder : public CAM::FeatureGeomBuilder
        {
            private: TurnAvoidanceGeomBuilderImpl * m_turnavoidancegeombuilder_impl;
            private: friend class  _TurnAvoidanceGeomBuilderBuilder;
            protected: TurnAvoidanceGeomBuilder();
            public: ~TurnAvoidanceGeomBuilder();
            /**Returns  the avoidance from builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceFromBuilder * AvoidanceFromBuilder
            (
            );
            /**Returns  the start point builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceStartBuilder * AvoidanceStartBuilder
            (
            );
            /**Returns  the approach path builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceApproachBuilder * AvoidanceApproachBuilder
            (
            );
            /**Returns  the start of engage builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceStartOfEngageBuilder * AvoidanceStartOfEngageBuilder
            (
            );
            /**Returns  the departure path builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceDepartureBuilder * AvoidanceDepartureBuilder
            (
            );
            /**Returns  the return path builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceReturnBuilder * AvoidanceReturnBuilder
            (
            );
            /**Returns  the gohome point builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceGohomeBuilder * AvoidanceGohomeBuilder
            (
            );
            /**Returns  the clearance builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::TurnAvoidanceClearanceBuilder * AvoidanceClearanceBuilder
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