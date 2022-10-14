#ifndef NXOpen_CAM_CIRCULARABOUTAXISMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CIRCULARABOUTAXISMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CircularAboutAxisMoveBuilder.ja
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
#include <NXOpen/CAM_ExpressionDouble.hxx>
#include <NXOpen/CAM_ReferencePoint.hxx>
#include <NXOpen/CAM_ReferenceVector.hxx>
#include <NXOpen/CAM_MoveBuilder.hxx>
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
        class CircularAboutAxisMoveBuilder;
    }
    namespace CAM
    {
        class ExpressionDouble;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class ReferencePoint;
    }
    namespace CAM
    {
        class ReferenceVector;
    }
    class Direction;
    class Point;
    namespace CAM
    {
        class _CircularAboutAxisMoveBuilderBuilder;
        class CircularAboutAxisMoveBuilderImpl;
        /** Represents the Circular Move To Point Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateCircularAboutAxisMoveBuilder  NXOpen::CAM::MoveCollection::CreateCircularAboutAxisMoveBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CircularAboutAxisMoveBuilder : public NXOpen::CAM::MoveBuilder
        {
            /** the axis type */
            public: enum AxisType
            {
                AxisTypeTool/** Tool Axis */,
                AxisTypeVector/** Vector */
            };

            /** the motion end type */
            public: enum EndType
            {
                EndTypeAngle/** Angle */,
                EndTypePoint/** Point */
            };

            /** the extension type */
            public: enum ExtensionType
            {
                ExtensionTypeAngle/** Angle */,
                ExtensionTypeDistance/** Distance */
            };

            private: CircularAboutAxisMoveBuilderImpl * m_circularaboutaxismovebuilder_impl;
            private: friend class  _CircularAboutAxisMoveBuilderBuilder;
            protected: CircularAboutAxisMoveBuilder();
            public: ~CircularAboutAxisMoveBuilder();
            /**Returns  the center 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferencePoint NXOpen::CAM::ReferencePoint@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferencePoint instead.") NXOpen::Point * CenterPoint
            (
            );
            /**Sets  the center 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferencePoint NXOpen::CAM::ReferencePoint@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferencePoint instead.") void SetCenterPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the axis type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder::AxisType ArcAxisType
            (
            );
            /**Sets  the axis type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetArcAxisType
            (
                NXOpen::CAM::CircularAboutAxisMoveBuilder::AxisType axisType /** axistype */ 
            );
            /**Returns  the arc axis 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferenceVector NXOpen::CAM::ReferenceVector@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferenceVector instead.") NXOpen::Direction * ArcAxis
            (
            );
            /**Sets  the arc axis 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferenceVector NXOpen::CAM::ReferenceVector@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferenceVector instead.") void SetArcAxis
            (
                NXOpen::Direction * vec /** vec */ 
            );
            /**Returns  the arc end type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder::EndType MotionEndType
            (
            );
            /**Sets  the arc end type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMotionEndType
            (
                NXOpen::CAM::CircularAboutAxisMoveBuilder::EndType arcEndType /** arcendtype */ 
            );
            /**Returns  the sweep angle 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") double SweepAngle
            (
            );
            /**Sets  the sweep angle 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") void SetSweepAngle
            (
                double sweepAngle /** sweepangle */ 
            );
            /**Returns  the arc end point 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferencePoint NXOpen::CAM::ReferencePoint@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferencePoint instead.") NXOpen::Point * EndPoint
            (
            );
            /**Sets  the arc end point 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferencePoint NXOpen::CAM::ReferencePoint@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferencePoint instead.") void SetEndPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the arc extension type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CircularAboutAxisMoveBuilder::ExtensionType ArcExtendMethod
            (
            );
            /**Sets  the arc extension type  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetArcExtendMethod
            (
                NXOpen::CAM::CircularAboutAxisMoveBuilder::ExtensionType arcExtendMethod /** arcextendmethod */ 
            );
            /**Returns  the extend angle 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") double ExtendAngle
            (
            );
            /**Sets  the extend angle 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") void SetExtendAngle
            (
                double extendAngle /** extendangle */ 
            );
            /**Returns  the extend distance 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") double ExtendDistance
            (
            );
            /**Sets  the extend distance 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") void SetExtendDistance
            (
                double extendDistance /** extenddistance */ 
            );
            /**Returns  the center point builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ReferencePoint * CenterPointBuilder
            (
            );
            /**Returns  the end point builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ReferencePoint * EndPointBuilder
            (
            );
            /**Returns  the arc axis vector builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ReferenceVector * ArcAxisVectorBuilder
            (
            );
            /**Returns  the sweep angle builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ExpressionDouble * SweepAngleBuilder
            (
            );
            /**Returns  the extend angle builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ExpressionDouble * ExtendAngleBuilder
            (
            );
            /**Returns  the extend distance builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ExpressionDouble * ExtendDistanceBuilder
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