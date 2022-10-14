#ifndef NXOpen_CAM_NORMALTOTOOLAXISMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NORMALTOTOOLAXISMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NormalToToolAxisMoveBuilder.ja
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
#include <NXOpen/CAM_RoundPointBuilder.hxx>
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
        class NormalToToolAxisMoveBuilder;
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
    namespace CAM
    {
        class RoundPointBuilder;
    }
    class Direction;
    class Point;
    namespace CAM
    {
        class _NormalToToolAxisMoveBuilderBuilder;
        class NormalToToolAxisMoveBuilderImpl;
        /** Represents the Move To Point Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateNormalToToolAxisMoveBuilder  NXOpen::CAM::MoveCollection::CreateNormalToToolAxisMoveBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NormalToToolAxisMoveBuilder : public NXOpen::CAM::MoveBuilder
        {
            /** the normal orientation */
            public: enum Orientation
            {
                OrientationAlongVector/** Along Vector */,
                OrientationTowardsPoint/** Towards Point */
            };

            private: NormalToToolAxisMoveBuilderImpl * m_normaltotoolaxismovebuilder_impl;
            private: friend class  _NormalToToolAxisMoveBuilderBuilder;
            protected: NormalToToolAxisMoveBuilder();
            public: ~NormalToToolAxisMoveBuilder();
            /**Returns  the normal type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NormalToToolAxisMoveBuilder::Orientation MoveType
            (
            );
            /**Sets  the normal type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMoveType
            (
                NXOpen::CAM::NormalToToolAxisMoveBuilder::Orientation normaltype /** normaltype */ 
            );
            /**Returns  the point in normal direction
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferencePoint NXOpen::CAM::ReferencePoint@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferencePoint instead.") NXOpen::Point * Point
            (
            );
            /**Sets  the point in normal direction
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferencePoint NXOpen::CAM::ReferencePoint@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferencePoint instead.") void SetPoint
            (
                NXOpen::Point * location /** location */ 
            );
            /**Returns  the vector 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferenceVector NXOpen::CAM::ReferenceVector@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferenceVector instead.") NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ReferenceVector NXOpen::CAM::ReferenceVector@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ReferenceVector instead.") void SetVector
            (
                NXOpen::Direction * vec /** vec */ 
            );
            /**Returns  the distance 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") double Distance
            (
            );
            /**Sets  the distance 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") void SetDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the angle 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") double Angle
            (
            );
            /**Sets  the angle 
             <br>  @deprecated Deprecated in NX12.0.1.  Use @link NXOpen::CAM::ExpressionDouble NXOpen::CAM::ExpressionDouble@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX12.0.1.  Use NXOpen::CAM::ExpressionDouble instead.") void SetAngle
            (
                double distance /** distance */ 
            );
            /**Returns  the round point builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::RoundPointBuilder * RoundPoint
            (
            );
            /**Returns  the end point builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ReferencePoint * EndPointBuilder
            (
            );
            /**Returns  the vector builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ReferenceVector * VectorBuilder
            (
            );
            /**Returns  the angle builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ExpressionDouble * AngleBuilder
            (
            );
            /**Returns  the distance builder
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ExpressionDouble * DistanceBuilder
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