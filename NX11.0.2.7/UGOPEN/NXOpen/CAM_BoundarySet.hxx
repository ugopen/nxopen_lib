#ifndef NXOpen_CAM_BOUNDARYSET_HXX_INCLUDED
#define NXOpen_CAM_BOUNDARYSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BoundarySet.ja
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
#include <NXOpen/CAM_BoundaryMemberSet.hxx>
#include <NXOpen/CAM_BoundarySet.hxx>
#include <NXOpen/CAM_Typedefs.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class BoundarySet;
    }
    namespace CAM
    {
        class BoundaryMemberSet;
    }
    namespace CAM
    {
        class BoundaryMemberSetList;
    }
    class NXObject;
    class Plane;
    class SelectTaggedObject;
    class SelectTaggedObjectList;
    namespace CAM
    {
        class _BoundarySetBuilder;
        class BoundarySetImpl;
        /** Represents a boundary set.   <br> To create a new instance of this class, use @link NXOpen::CAM::Boundary::CreateBoundarySet  NXOpen::CAM::Boundary::CreateBoundarySet @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  BoundarySet : public NXOpen::TaggedObject
        {
            /** the boundary types 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum BoundaryTypes
            {
                BoundaryTypesClosed/** close boundary */,
                BoundaryTypesOpen/** open boundary */
            };

            /** the tool side types 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum ToolSideTypes
            {
                ToolSideTypesInsideOrLeft/** inside for closed boundary, or left side for open boundary */,
                ToolSideTypesOutsideOrRight/** outside for closed boundary, or right side for open boundary */
            };

            /** the boundary plane types 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum PlaneTypes
            {
                PlaneTypesAutomatic/** automatically get a boundary plane from selected entities */,
                PlaneTypesUserDefined/** user defined plane */
            };

            /** the tool position 
             <br>  Created in NX9.0.1.  <br>  
            */
            public: enum ToolPositionTypes
            {
                ToolPositionTypesOn/** tool tip positioned on boundary */,
                ToolPositionTypesContact/** tool tip positioned contacting boundary */
            };

            private: BoundarySetImpl * m_boundaryset_impl;
            private: friend class  _BoundarySetBuilder;
            protected: BoundarySet();
            public: ~BoundarySet();
            /**Returns  the points list 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * PointList
            (
            );
            /** Add curves to the boundary 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void AppendCurves
            (
                const std::vector<NXOpen::NXObject *> & curves /** the curves */,
                const NXOpen::Point3d & pickPoint /** the pick point (start point on first member) */,
                const NXOpen::Matrix3x3 & matrix /** the view matrix */
            );
            /** Remove curves from the boundary 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void RemoveCurves
            (
                const std::vector<NXOpen::NXObject *> & curves /** the curves */
            );
            /**Returns  the boundary member list 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryMemberSetList * BoundaryMemberList
            (
            );
            /** Create an empty boundary member set @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::BoundaryMemberSet * CreateBoundaryMemberSet
            (
            );
            /**Returns  the flag whether this boundary has custom offset activated 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool CustomOffset
            (
            );
            /**Sets  the flag whether this boundary has custom offset activated 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomOffset
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the offset value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double Offset
            (
            );
            /**Sets  the offset value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOffset
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the offset intent 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ParamValueIntent OffsetIntent
            (
            );
            /**Sets  the offset intent 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOffsetIntent
            (
                NXOpen::CAM::ParamValueIntent newValue /** newvalue */ 
            );
            /**Returns  the boundary type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundarySet::BoundaryTypes BoundaryType
            (
            );
            /**Sets  the boundary type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBoundaryType
            (
                NXOpen::CAM::BoundarySet::BoundaryTypes newValue /** newvalue */ 
            );
            /**Returns  the tool side 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundarySet::ToolSideTypes ToolSide
            (
            );
            /**Sets  the tool side 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolSide
            (
                NXOpen::CAM::BoundarySet::ToolSideTypes newValue /** newvalue */ 
            );
            /**Returns  the tool position 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundarySet::ToolPositionTypes ToolPosition
            (
            );
            /**Sets  the tool position 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolPosition
            (
                NXOpen::CAM::BoundarySet::ToolPositionTypes newValue /** newvalue */ 
            );
            /**Returns  the boundary plane type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundarySet::PlaneTypes PlaneType
            (
            );
            /**Sets  the boundary plane type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPlaneType
            (
                NXOpen::CAM::BoundarySet::PlaneTypes newValue /** newvalue */ 
            );
            /**Returns  the boundary plane 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the boundary plane 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPlane
            (
                NXOpen::Plane * newValue /** newvalue */ 
            );
            /**Returns  the select object 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObject * SelectObject
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
