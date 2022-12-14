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
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents a Tool Axis Interpolate Builder */
        class NXOPENCPPEXPORT  ToolAxisInterpolate : public TaggedObject
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

            private: ToolAxisInterpolateImpl * m_toolaxisinterpolate_impl;
            private: friend class  _ToolAxisInterpolateBuilder;
            protected: ToolAxisInterpolate();
            public: ~ToolAxisInterpolate();
            /**Returns  the interpolation method type  <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisInterpolate::InterpolationMethodTypes InterpolationMethod
            (
            );
            /**Sets  the interpolation method type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInterpolationMethod
            (
                NXOpen::CAM::ToolAxisInterpolate::InterpolationMethodTypes newValue /** the interpolation method type */
            );
            /** The action of Reset to Default  <br> License requirements : cam_base ("CAM BASE") */
            public: void ResetToDefault
            (
            );
            /** Get the point  @return  the point  <br> License requirements : None */
            public: NXOpen::Point * GetPoint
            (
                int index /** the index of item */
            );
            /** Get the total number of interpolate data points  @return  the total number  <br> License requirements : None */
            public: int GetTotalNumberOfPoints
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
