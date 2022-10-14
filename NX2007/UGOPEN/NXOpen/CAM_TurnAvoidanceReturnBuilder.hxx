#ifndef NXOpen_CAM_TURNAVOIDANCERETURNBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNAVOIDANCERETURNBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnAvoidanceReturnBuilder.ja
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
        class TurnAvoidanceReturnBuilder;
    }
    class NXObject;
    class Point;
    namespace CAM
    {
        class _TurnAvoidanceReturnBuilderBuilder;
        class TurnAvoidanceReturnBuilderImpl;
        /** Represents an avoidance return Builder 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnAvoidanceReturnBuilder : public NXOpen::TaggedObject
        {
            /** the return point motion type options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum ReturnPointMotionTypes
            {
                ReturnPointMotionTypesNone/** Point is inactive. */,
                ReturnPointMotionTypesAutomatic/** Motion type: Automatic to point. */,
                ReturnPointMotionTypesDirect/** Motion type: Direct to point. */,
                ReturnPointMotionTypesRadialThenAxial/** Motion type: Radial then axial to point. */,
                ReturnPointMotionTypesAxialThenRadial/** Motion type: Axial then axial to point. */,
                ReturnPointMotionTypesClearRadialThenDirect/** Motion type: Radial to clearance plane then direct to point. */,
                ReturnPointMotionTypesClearAxialThenDirect/** Motion type: Axial to clearance plane then direct to point. */,
                ReturnPointMotionTypesClearRadialOnly/** Motion type: Radial to clearance plane only (no motion to point). */,
                ReturnPointMotionTypesClearAxialOnly/** Motion type: Axial to clearance plane only (no motion to point). */
            };

            /** The return point mode options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum ReturnPointModes
            {
                ReturnPointModesPoint/** Point is defined by point. */,
                ReturnPointModesDeltaAngleDistance/** Point is defined by angle and distance. */,
                ReturnPointModesDeltaVectorDistance/** Point is defined by vector and distance. */,
                ReturnPointModesDeltaMove/** Point is defined by delta move (X and Y coordinate). */,
                ReturnPointModesSameAsStart/** Point is locked start point. */
            };

            private: TurnAvoidanceReturnBuilderImpl * m_turnavoidancereturnbuilder_impl;
            private: friend class  _TurnAvoidanceReturnBuilderBuilder;
            protected: TurnAvoidanceReturnBuilder();
            public: ~TurnAvoidanceReturnBuilder();
            /**Returns  the return point motion type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceReturnBuilder::ReturnPointMotionTypes ReturnPointMotionType
            (
            );
            /**Sets  the return point motion type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnPointMotionType
            (
                NXOpen::CAM::TurnAvoidanceReturnBuilder::ReturnPointMotionTypes returnPointMotionType /** the return point motion type value */
            );
            /**Returns  the return point mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceReturnBuilder::ReturnPointModes ReturnPointMode
            (
            );
            /**Sets  the return point mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnPointMode
            (
                NXOpen::CAM::TurnAvoidanceReturnBuilder::ReturnPointModes returnPointMode /** the return point mode value */
            );
            /**Returns  the return point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ReturnPoint
            (
            );
            /**Sets  the return point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnPoint
            (
                NXOpen::Point * returnPoint /** the return point value */
            );
            /**Returns  the return delta angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double ReturnDeltaAngle
            (
            );
            /**Sets  the return delta angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnDeltaAngle
            (
                double returnDeltaAngle /** the return delta angle value */
            );
            /**Returns  the return delta distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double ReturnDeltaDistance
            (
            );
            /**Sets  the return delta distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnDeltaDistance
            (
                double returnDeltaDistance /** the return delta distance value */
            );
            /**Returns  the return delta vector 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * ReturnDeltaVector
            (
            );
            /**Sets  the return delta vector 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnDeltaVector
            (
                NXOpen::NXObject * returnDeltaVector /** the return delta vector value */
            );
            /**Returns  the return delta X 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double ReturnDeltaX
            (
            );
            /**Sets  the return delta X 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnDeltaX
            (
                double returnDeltaX /** the return delta x value */
            );
            /**Returns  the return delta Y 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double ReturnDeltaY
            (
            );
            /**Sets  the return delta Y 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReturnDeltaY
            (
                double returnDeltaY /** the return delta x value */
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