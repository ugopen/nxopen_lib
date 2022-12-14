#ifndef NXOpen_CAM_LASERPROFILEMOVE_HXX_INCLUDED
#define NXOpen_CAM_LASERPROFILEMOVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_LaserProfileMove.ja
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
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Section.hxx>
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
        class LaserProfileMove;
    }
    namespace CAM
    {
        class LaserControlPoint;
    }
    namespace CAM
    {
        class LaserControlPointList;
    }
    namespace CAM
    {
        class LaserCutDirection;
    }
    namespace CAM
    {
        class LaserHeadOrientation;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    class CartesianCoordinateSystem;
    class NXObject;
    class Point;
    class Section;
    namespace CAM
    {
        class _LaserProfileMoveBuilder;
        class LaserProfileMoveImpl;
        /** Represents a LaserProfileMove  <br> To create a new instance of this class, use @link CAM::MoveCollection::CreateLaserProfileMove  CAM::MoveCollection::CreateLaserProfileMove @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  LaserProfileMove : public CAM::MoveBuilder
        {
            /** the Shape Type enum 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum ShapeTypes
            {
                ShapeTypesExternalTrim/** External Trim */,
                ShapeTypesInternalTrim/** Internal Trim */,
                ShapeTypesOpenProfile/** Open Profile */
            };

            /** the Tool Side enum 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum ToolSides
            {
                ToolSidesOn/** On */,
                ToolSidesLeft/** Left */,
                ToolSidesRight/** Right */
            };

            /** the Collision Check enum 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum CollisionChecks
            {
                CollisionChecksNone/** None */,
                CollisionChecksNozzleOnly/** Nozzle Only */,
                CollisionChecksNozzleAndHolder/** Nozzle and Holder */,
                CollisionChecksSolidLaserHead/** Solid Laser Head */
            };

            /** the Interpolation Method enum 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum InterpMethods
            {
                InterpMethodsLinear/** Linear */,
                InterpMethodsCubicSpline/** Cubic Spline */,
                InterpMethodsSmooth/** Smooth */
            };

            private: LaserProfileMoveImpl * m_laserprofilemove_impl;
            private: friend class  _LaserProfileMoveBuilder;
            protected: LaserProfileMove();
            public: ~LaserProfileMove();
            /**Returns  the Cut Direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserCutDirection * CutDirection
            (
            );
            /**Returns  the Head Orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserHeadOrientation * HeadOrientation
            (
            );
            /**Returns  the Profile Section 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * ProfileSection
            (
            );
            /**Sets  the Profile Section 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetProfileSection
            (
                NXOpen::Section * profileSection /** the Profile Section */
            );
            /**Returns  the Max Gap Distance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double MaxGapDist
            (
            );
            /**Sets  the Max Gap Distance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMaxGapDist
            (
                double newValue /** the Max Gap Distance */
            );
            /**Returns  the Shape Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserProfileMove::ShapeTypes ShapeType
            (
            );
            /**Sets  the Shape Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetShapeType
            (
                NXOpen::CAM::LaserProfileMove::ShapeTypes type /** the shape type */
            );
            /**Returns  the Tool Side 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserProfileMove::ToolSides ToolSide
            (
            );
            /**Sets  the Tool Side 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolSide
            (
                NXOpen::CAM::LaserProfileMove::ToolSides type /** the tool side */
            );
            /**Returns  the Collision Check 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserProfileMove::CollisionChecks CollisionCheck
            (
            );
            /**Sets  the Collision Check 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCollisionCheck
            (
                NXOpen::CAM::LaserProfileMove::CollisionChecks type /** the collision check */
            );
            /**Returns  the Max Tilt Angle 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double MaxTiltAngle
            (
            );
            /**Sets  the Max Tilt Angle 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMaxTiltAngle
            (
                double newValue /** the Max Tilt Angle */
            );
            /**Returns  the Interpolation Method 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserProfileMove::InterpMethods InterpMethod
            (
            );
            /**Sets  the Interpolation Method 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInterpMethod
            (
                NXOpen::CAM::LaserProfileMove::InterpMethods type /** the interpolation method */
            );
            /**Returns  the List 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::LaserControlPointList * List
            (
            );
            /** Create a new Laser Control Point   @return  the control points 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::LaserControlPoint * CreateControlPoint
            (
                int headOrientType /** head orient type */,
                NXOpen::Point * pointTag /** the point */,
                NXOpen::CartesianCoordinateSystem * csysTag /** the csys */,
                int processType /** point process type */,
                bool toggle /** events toggle */,
                NXOpen::NXObject * udePathTag /** the ude path */,
                int pointType /** point type */
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
