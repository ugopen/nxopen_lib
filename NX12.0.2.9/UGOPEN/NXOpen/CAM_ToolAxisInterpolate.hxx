#ifndef NXOpen_CAM_TOOLAXISINTERPOLATE_HXX_INCLUDED
#define NXOpen_CAM_TOOLAXISINTERPOLATE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolAxisInterpolate.ja
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
        class ToolAxisInterpolate;
    }
    class Point;
    namespace CAM
    {
        class _ToolAxisInterpolateBuilder;
        class ToolAxisInterpolateImpl;
        /** Represents a Tool Axis Interpolate Builder 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ToolAxisInterpolate : public NXOpen::TaggedObject
        {
            /** the available types for Interpolate Types*/
            public: enum InterpolateTypes
            {
                InterpolateTypesVector/** Interpolate Types: Vector */,
                InterpolateTypesAngleToPart/** Interpolate Types: Angle to Part */,
                InterpolateTypesAngleToDrive/** Interpolate Types: Angle to Drive */
            };

            /** the available types for interpolate method*/
            public: enum InterpolationMethodTypes
            {
                InterpolationMethodTypesLinear/** Linear */,
                InterpolationMethodTypesCubicSpline/** Cubic Spline */,
                InterpolationMethodTypesSmooth/** Smooth */
            };

            /** the available types for the control direction*/
            public: enum ControlDirectionTypes
            {
                ControlDirectionTypesUandv/** U and V */,
                ControlDirectionTypesU/** U only */,
                ControlDirectionTypesV/** V only */
            };

            /** the available types for turn interpolation method */
            public: enum TurnInterpolationMethodTypes
            {
                TurnInterpolationMethodTypesAbsolute/** Absolute */,
                TurnInterpolationMethodTypesRelative/** Relative */
            };

            /** the available types for turn input mode */
            public: enum TurnInputModeTypes
            {
                TurnInputModeTypesHolderAngleFromPart/** holder angle from part */,
                TurnInputModeTypesClearanceAngle/** clearance angle */,
                TurnInputModeTypesCuttingAngle/** cutting angle */
            };

            private: ToolAxisInterpolateImpl * m_toolaxisinterpolate_impl;
            private: friend class  _ToolAxisInterpolateBuilder;
            protected: ToolAxisInterpolate();
            public: ~ToolAxisInterpolate();
            /**Returns  the interpolation method type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisInterpolate::InterpolationMethodTypes InterpolationMethod
            (
            );
            /**Sets  the interpolation method type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInterpolationMethod
            (
                NXOpen::CAM::ToolAxisInterpolate::InterpolationMethodTypes newValue /** the interpolation method type */
            );
            /** The action of Reset to Default 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void ResetToDefault
            (
            );
            /** Get the point  @return  the point 
             <br>  Created in NX7.5.5.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * GetPoint
            (
                int index /** the index of item */
            );
            /** Get the total number of interpolate data points  @return  the total number 
             <br>  Created in NX7.5.5.  <br>  
             <br> License requirements : None */
            public: int GetTotalNumberOfPoints
            (
            );
            /**Returns  the turn interpolation method type
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisInterpolate::TurnInterpolationMethodTypes TurnInterpolationMethod
            (
            );
            /**Sets  the turn interpolation method type
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTurnInterpolationMethod
            (
                NXOpen::CAM::ToolAxisInterpolate::TurnInterpolationMethodTypes newValue /** the turn interpolation method type */
            );
            /**Returns  the control direction type 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisInterpolate::ControlDirectionTypes ControlDirection
            (
            );
            /**Sets  the control direction type 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetControlDirection
            (
                NXOpen::CAM::ToolAxisInterpolate::ControlDirectionTypes newValue /** the control direction type */
            );
            /**Returns  the turn input mode type 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisInterpolate::TurnInputModeTypes TurnInputMode
            (
            );
            /**Sets  the turn input mode type 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTurnInputMode
            (
                NXOpen::CAM::ToolAxisInterpolate::TurnInputModeTypes newValue /** the turn input mode type */
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