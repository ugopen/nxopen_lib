#ifndef NXOpen_CAM_BOUNDARYTURNMEMBERCORNER_HXX_INCLUDED
#define NXOpen_CAM_BOUNDARYTURNMEMBERCORNER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BoundaryTurnMemberCorner.ja
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
#include <NXOpen/CAM_BoundaryTurnMemberCorner.hxx>
#include <NXOpen/CAM_BoundaryTurnSet.hxx>
#include <NXOpen/Builder.hxx>
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
        class BoundaryTurnMemberCorner;
    }
    class Builder;
    namespace CAM
    {
        class _BoundaryTurnMemberCornerBuilder;
        class BoundaryTurnMemberCornerImpl;
        /**
            Represents a @link NXOpen::CAM::BoundaryTurnMemberCorner NXOpen::CAM::BoundaryTurnMemberCorner@endlink 
             <br> This builder cannot be instantiated separately.  <br> 
         <br>  Created in NX9.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  BoundaryTurnMemberCorner : public NXOpen::Builder
        {
            /** the corner types available */
            public: enum CornerType
            {
                CornerTypeGeneral/** general */ ,
                CornerTypeConstantRadiusChamfer/** constant radius chamfer */ ,
                CornerTypeKeepTangentPoint/** keep tangent point */ 
            };

            /** the corner shape types available */
            public: enum ShapeType
            {
                ShapeTypeNone/** none */ ,
                ShapeTypeRoundbeforestock/** roundbeforestock */ ,
                ShapeTypeBreakbeforestock/** breakbeforestock */ ,
                ShapeTypeRoundafterstock/** roundafterstock */ ,
                ShapeTypeBreakafterstock/** breakafterstock */ 
            };

            /** the corner angle types available */
            public: enum AngleValueType
            {
                AngleValueTypeNone/** none */ ,
                AngleValueTypeCurrentsegment/** currentsegment */ ,
                AngleValueTypePrevioussegment/** previoussegment */ 
            };

            /** the corner feed rate types available */
            public: enum FeedType
            {
                FeedTypeNone/** none */ ,
                FeedTypeSpecify/** specify */ 
            };

            private: BoundaryTurnMemberCornerImpl * m_boundaryturnmembercorner_impl;
            private: friend class  _BoundaryTurnMemberCornerBuilder;
            protected: BoundaryTurnMemberCorner();
            public: ~BoundaryTurnMemberCorner();
            /**Returns  the corner type 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberCorner::CornerType Type
            (
            );
            /**Sets  the corner type 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::CAM::BoundaryTurnMemberCorner::CornerType cornerType /** cornertype */ 
            );
            /**Returns  the corner shape 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberCorner::ShapeType Shape
            (
            );
            /**Sets  the corner shape 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetShape
            (
                NXOpen::CAM::BoundaryTurnMemberCorner::ShapeType cornerShape /** cornershape */ 
            );
            /**Returns  the corner radius 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: double Radius
            (
            );
            /**Sets  the corner radius 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRadius
            (
                double cornerRadius /** cornerradius */ 
            );
            /**Returns  the corner distance 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: double Distance
            (
            );
            /**Sets  the corner distance 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDistance
            (
                double cornerDistance /** cornerdistance */ 
            );
            /**Returns  the corner angle type 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberCorner::AngleValueType AngleType
            (
            );
            /**Sets  the corner angle type 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAngleType
            (
                NXOpen::CAM::BoundaryTurnMemberCorner::AngleValueType cornerAngle /** cornerangle */ 
            );
            /**Returns  the corner angle value 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the corner angle value 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAngle
            (
                double angleValue /** anglevalue */ 
            );
            /**Returns  the corner feed rate type 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberCorner::FeedType CornerFeedType
            (
            );
            /**Sets  the corner feed rate type 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCornerFeedType
            (
                NXOpen::CAM::BoundaryTurnMemberCorner::FeedType newValue /** newvalue */ 
            );
            /**Returns  the feed rate value 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: double FeedValue
            (
            );
            /**Sets  the feed rate value 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeedValue
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the feed rate unit 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnSet::FeedUnitTypes FeedUnit
            (
            );
            /**Sets  the feed rate unit 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeedUnit
            (
                NXOpen::CAM::BoundaryTurnSet::FeedUnitTypes newUnit /** newunit */ 
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