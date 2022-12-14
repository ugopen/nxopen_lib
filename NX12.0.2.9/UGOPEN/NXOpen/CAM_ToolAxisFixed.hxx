#ifndef NXOpen_CAM_TOOLAXISFIXED_HXX_INCLUDED
#define NXOpen_CAM_TOOLAXISFIXED_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolAxisFixed.ja
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
#include <NXOpen/CAM_ToolAxisBase.hxx>
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
        class ToolAxisFixed;
    }
    namespace CAM
    {
        class ToolAxisBase;
    }
    namespace CAM
    {
        class _ToolAxisFixedBuilder;
        class ToolAxisFixedImpl;
        /** Represents a Tool Axis Fixed Builder 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ToolAxisFixed : public NXOpen::CAM::ToolAxisBase
        {
            /** Available types for Tool Axis Fixed */
            public: enum Types
            {
                TypesNone/** None or +ZM*/,
                TypesFixed/** Fixed */,
                TypesNormalToPart/** Normal To Floor Face */,
                TypesNormalToFirstFace/** Normal To First Face */,
                TypesDynamic/** Dynamic */,
                TypesTangentToCurve/** tangent to curve */,
                TypesTangentToCurveAtAngle/** tangent to curve at angle */
            };

            private: ToolAxisFixedImpl * m_toolaxisfixed_impl;
            private: friend class  _ToolAxisFixedBuilder;
            protected: ToolAxisFixed();
            public: ~ToolAxisFixed();
            /**Returns  the tool axis types 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisFixed::Types ToolAxisType
            (
            );
            /**Sets  the tool axis types 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolAxisType
            (
                NXOpen::CAM::ToolAxisFixed::Types toolAxis /** the tool axis type */
            );
            /**Returns  the indicator if the preferred angles are defined 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsPreferredAnglesDefined
            (
            );
            /**Returns  the preferred fouth angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double PreferredFourthAngle
            (
            );
            /**Returns  the preferred fifth angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double PreferredFifthAngle
            (
            );
            /**Returns  the tangent to curve angle 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: double TangentToCurveAngle
            (
            );
            /**Sets  the tangent to curve angle 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: void SetTangentToCurveAngle
            (
                double tangentToCurveAngle /** the tangent curve angle */
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
