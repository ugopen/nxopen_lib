#ifndef NXOpen_CAM_TURNAVOIDANCECLEARANCEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNAVOIDANCECLEARANCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnAvoidanceClearanceBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class TurnAvoidanceClearanceBuilder;
    }
    class Point;
    namespace CAM
    {
        class _TurnAvoidanceClearanceBuilderBuilder;
        class TurnAvoidanceClearanceBuilderImpl;
        /** Represents an avoidance start of engage Builder 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnAvoidanceClearanceBuilder : public NXOpen::TaggedObject
        {
            /** The radial plane mode options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum RadialPlaneModes
            {
                RadialPlaneModesNone/** Plane is inactive. */,
                RadialPlaneModesPoint/** Plane is defined by point. */,
                RadialPlaneModesDistance/** Plane is defined by distance value. */
            };

            /** The axial plane mode options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum AxialPlaneModes
            {
                AxialPlaneModesNone/** Plane is inactive. */,
                AxialPlaneModesPoint/** Plane is defined by point. */,
                AxialPlaneModesDistance/** Plane is defined by distance value. */
            };

            private: TurnAvoidanceClearanceBuilderImpl * m_turnavoidanceclearancebuilder_impl;
            private: friend class  _TurnAvoidanceClearanceBuilderBuilder;
            protected: TurnAvoidanceClearanceBuilder();
            public: ~TurnAvoidanceClearanceBuilder();
            /**Returns  the radial plane mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceClearanceBuilder::RadialPlaneModes RadialPlaneMode
            (
            );
            /**Sets  the radial plane mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRadialPlaneMode
            (
                NXOpen::CAM::TurnAvoidanceClearanceBuilder::RadialPlaneModes radialPlaneMode /** the radial plane mode value */
            );
            /**Returns  the radial plane point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * RadialPlanePoint
            (
            );
            /**Sets  the radial plane point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRadialPlanePoint
            (
                NXOpen::Point * radialPlanePoint /** the radial plane point value */
            );
            /**Returns  the radial plane value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double RadialPlaneValue
            (
            );
            /**Sets  the radial plane value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRadialPlaneValue
            (
                double radialPlaneValue /** the radial plane value value */
            );
            /**Returns  the axial plane mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceClearanceBuilder::AxialPlaneModes AxialPlaneMode
            (
            );
            /**Sets  the axial plane mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAxialPlaneMode
            (
                NXOpen::CAM::TurnAvoidanceClearanceBuilder::AxialPlaneModes axialPlaneMode /** the axial plane mode value */
            );
            /**Returns  the axial plane point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * AxialPlanePoint
            (
            );
            /**Sets  the axial plane point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAxialPlanePoint
            (
                NXOpen::Point * axialPlanePoint /** the axial plane point value */
            );
            /**Returns  the axial plane value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double AxialPlaneValue
            (
            );
            /**Sets  the axial plane value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAxialPlaneValue
            (
                double axialPlaneValue /** the axial plane value value */
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
