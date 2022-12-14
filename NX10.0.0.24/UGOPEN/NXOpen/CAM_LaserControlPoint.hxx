#ifndef NXOpen_CAM_LASERCONTROLPOINT_HXX_INCLUDED
#define NXOpen_CAM_LASERCONTROLPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_LaserControlPoint.ja
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
        class LaserControlPoint;
    }
    namespace CAM
    {
        class UdeSet;
    }
    class CartesianCoordinateSystem;
    class Point;
    namespace CAM
    {
        class _LaserControlPointBuilder;
        class LaserControlPointImpl;
        /** Represents a Laser Control Point builder  <br> To create a new instance of this class, use @link NXOpen::CAM::LaserProfileMove::CreateControlPoint  NXOpen::CAM::LaserProfileMove::CreateControlPoint @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  LaserControlPoint : public NXOpen::TaggedObject
        {
            /** the Local Head Orientation Enum 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum HeadOrientTypes
            {
                HeadOrientTypesNone/** None */,
                HeadOrientTypesSpecify/** Specify */,
                HeadOrientTypesDynamic/** Dynamic */
            };

            /** the Control Point type 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum ControlPointTypes
            {
                ControlPointTypesSys/** sys */,
                ControlPointTypesAdj/** adj */,
                ControlPointTypesColl/** coll */,
                ControlPointTypesMod/** mod */,
                ControlPointTypesUser/** user */
            };

            /** the Point Process Enumeration 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum ProcessTypes
            {
                ProcessTypesProjectToToolPath/** Project to Tool Path */,
                ProcessTypesDriveToPoint/** Drive to Point */
            };

            private: LaserControlPointImpl * m_lasercontrolpoint_impl;
            private: friend class  _LaserControlPointBuilder;
            protected: LaserControlPoint();
            public: ~LaserControlPoint();
            /**Returns  the Local Head Orientation Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserControlPoint::HeadOrientTypes LocalHeadOrientType
            (
            );
            /**Sets  the Local Head Orientation Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLocalHeadOrientType
            (
                NXOpen::CAM::LaserControlPoint::HeadOrientTypes type /** type */ 
            );
            /**Returns  the Control Point 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the Control Point 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoint
            (
                NXOpen::Point * newValue /** the point*/
            );
            /**Returns  the Local Head Orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CartesianCoordinateSystem * Csys
            (
            );
            /**Sets  the Local Head Orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCsys
            (
                NXOpen::CartesianCoordinateSystem * mcs /** the local head orientation */
            );
            /**Returns  the flag whether the control event is available 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool EventFlag
            (
            );
            /**Sets  the flag whether the control event is available 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEventFlag
            (
                bool newValue /** the logical value */
            );
            /**Returns  the Machine Control Events 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::UdeSet * UdeSet
            (
            );
            /**Returns  the Point Process Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserControlPoint::ProcessTypes ProcessType
            (
            );
            /**Sets  the Point Process Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetProcessType
            (
                NXOpen::CAM::LaserControlPoint::ProcessTypes type /** type */ 
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
