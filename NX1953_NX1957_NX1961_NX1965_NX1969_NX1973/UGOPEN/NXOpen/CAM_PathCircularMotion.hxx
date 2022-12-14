#ifndef NXOpen_CAM_PATHCIRCULARMOTION_HXX_INCLUDED
#define NXOpen_CAM_PATHCIRCULARMOTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PathCircularMotion.ja
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
#include <NXOpen/CAM_PathData.hxx>
#include <NXOpen/CAM_PathLinearMotion.hxx>
#include <NXOpen/ugmath.hxx>
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
        class PathCircularMotion;
    }
    namespace CAM
    {
        class PathLinearMotion;
    }
    namespace CAM
    {
        class PathCircularMotionImpl;
        /** This class represents the data of a Linear Motion
         <br>  Created in NX10.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  PathCircularMotion : public NXOpen::CAM::PathLinearMotion
        {
            private: PathCircularMotionImpl * m_pathcircularmotion_impl;
            /// \cond NX_NO_DOC 
            public: explicit PathCircularMotion(void *ptr);
            /// \endcond 
            /**Returns  the center of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d ArcCenter
            (
            );
            /**Sets  the center of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetArcCenter
            (
                const NXOpen::Point3d & arcCenter /** arccenter */ 
            );
            /**Returns  the axis of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vector3d ArcAxis
            (
            );
            /**Sets  the axis of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetArcAxis
            (
                const NXOpen::Vector3d & arcAxis /** arcaxis */ 
            );
            /**Returns  the radius of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: double ArcRadius
            (
            );
            /**Sets  the radius of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetArcRadius
            (
                double arcRadius /** arcradius */ 
            );
            /**Returns  the direction of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamPathDir Direction
            (
            );
            /**Sets  the direction of the arc motion 
             <br>  Created in NX10.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDirection
            (
                NXOpen::CAM::CamPathDir arcDirection /** arcdirection */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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
