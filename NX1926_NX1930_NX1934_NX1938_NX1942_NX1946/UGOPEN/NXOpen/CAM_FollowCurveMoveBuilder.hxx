#ifndef NXOpen_CAM_FOLLOWCURVEMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_FOLLOWCURVEMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FollowCurveMoveBuilder.ja
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
#include <NXOpen/CAM_FollowGeometryMoveBuilder.hxx>
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
        class FollowCurveMoveBuilder;
    }
    namespace CAM
    {
        class FollowGeometryMoveBuilder;
    }
    class Direction;
    class Point;
    class Section;
    namespace CAM
    {
        class _FollowCurveMoveBuilderBuilder;
        class FollowCurveMoveBuilderImpl;
        /** Represents the Follow Curve Move Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateFollowCurveMoveBuilder  NXOpen::CAM::MoveCollection::CreateFollowCurveMoveBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FeedRate </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        FeedType </term> <description> 
         
        Motion </description> </item> 

        <item><term> 
         
        FeedUnit </term> <description> 
         
        None </description> </item> 

        <item><term> 
         
        MotionType </term> <description> 
         
        Cut </description> </item> 

        <item><term> 
         
        ProtectedMove </term> <description> 
         
        true </description> </item> 

        </list> 

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  FollowCurveMoveBuilder : public NXOpen::CAM::FollowGeometryMoveBuilder
        {
            private: FollowCurveMoveBuilderImpl * m_followcurvemovebuilder_impl;
            private: friend class  _FollowCurveMoveBuilderBuilder;
            protected: FollowCurveMoveBuilder();
            public: ~FollowCurveMoveBuilder();
            /**Returns  the geometry selection 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Geometry
            (
            );
            /**Sets  the geometry selection 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGeometry
            (
                NXOpen::Section * geometryCollector /** geometrycollector */ 
            );
            /**Returns  the end location 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * EndPoint
            (
            );
            /**Sets  the end location 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEndPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the end tool axis 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * EndToolAxis
            (
            );
            /**Sets  the end tool axis 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEndToolAxis
            (
                NXOpen::Direction * vec /** vec */ 
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
