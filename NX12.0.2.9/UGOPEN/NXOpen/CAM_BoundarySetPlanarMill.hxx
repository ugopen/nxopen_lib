#ifndef NXOpen_CAM_BOUNDARYSETPLANARMILL_HXX_INCLUDED
#define NXOpen_CAM_BOUNDARYSETPLANARMILL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BoundarySetPlanarMill.ja
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
#include <NXOpen/CAM_BoundaryMemberSetPlanarMill.hxx>
#include <NXOpen/CAM_BoundarySet.hxx>
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
        class BoundarySetPlanarMill;
    }
    namespace CAM
    {
        class BoundaryMemberSetPlanarMill;
    }
    namespace CAM
    {
        class BoundarySet;
    }
    namespace CAM
    {
        class _BoundarySetPlanarMillBuilder;
        class BoundarySetPlanarMillImpl;
        /** Represents a boundary set for the planar mill/surface contour operation  <br> To create a new instance of this class, use @link NXOpen::CAM::Boundary::CreateBoundarySetPlanarMill  NXOpen::CAM::Boundary::CreateBoundarySetPlanarMill @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  BoundarySetPlanarMill : public NXOpen::CAM::BoundarySet
        {
            /** the types available for the feed rate unit */
            public: enum FeedUnitTypes
            {
                FeedUnitTypesNone/** no feed rate unit*/,
                FeedUnitTypesPerMinute/** use per minute as the feed rate unit*/,
                FeedUnitTypesPerRevolution/** use per revolution as the feed rate unit*/
            };

            /** the boundary position where to trim or to extend */
            public: enum TrimExtendPosition
            {
                TrimExtendPositionAtStart/** trim or extend at start */,
                TrimExtendPositionAtEnd/** trim or extend at end */,
                TrimExtendPositionAtStartAndEnd/** trim or extend at start and at end */,
                TrimExtendPositionUnknown/** unknown */
            };

            private: BoundarySetPlanarMillImpl * m_boundarysetplanarmill_impl;
            private: friend class  _BoundarySetPlanarMillBuilder;
            protected: BoundarySetPlanarMill();
            public: ~BoundarySetPlanarMill();
            /** Create an empty custom member data set for a planar mill/surface contour boundary @return  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::BoundaryMemberSetPlanarMill * CreateBoundaryMemberSetPlanarMill
            (
            );
            /**Returns  the tolerance toggle 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CustomTolerance
            (
            );
            /**Sets  the tolerance toggle 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomTolerance
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the in tolerance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double InTolerance
            (
            );
            /**Sets  the in tolerance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInTolerance
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the out tolerance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double OutTolerance
            (
            );
            /**Sets  the out tolerance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOutTolerance
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the blank distance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CustomBlankDistance
            (
            );
            /**Sets  the blank distance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomBlankDistance
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the blank_distance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double BlankDistance
            (
            );
            /**Sets  the blank_distance 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBlankDistance
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the flag whether this boundary has custom stock activated 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CustomStock
            (
            );
            /**Sets  the flag whether this boundary has custom stock activated 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomStock
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the stock value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double Stock
            (
            );
            /**Sets  the stock value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStock
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the feed rate toggle 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CustomFeed
            (
            );
            /**Sets  the feed rate toggle 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomFeed
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the feed rate value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double FeedValue
            (
            );
            /**Sets  the feed rate value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeedValue
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the feed rate unit 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundarySetPlanarMill::FeedUnitTypes FeedUnit
            (
            );
            /**Sets  the feed rate unit 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeedUnit
            (
                NXOpen::CAM::BoundarySetPlanarMill::FeedUnitTypes newUnit /** newunit */ 
            );
            /** Trim or extend the start point of an open boundary 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void ExtendOrTrimStartPoint
            (
                double distance /** distance */ 
            );
            /** Trim or extend the end point of a closed boundary 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void ExtendOrTrimEndPoint
            (
                double distance /** distance */ 
            );
            /** Move the start point of a closed boundary 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveStartPoint
            (
                NXOpen::CAM::BoundaryMemberSetPlanarMill * bndSet /** bndset */ ,
                double distance /** distance */ 
            );
            /** Create curve boundary from permanent one
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void CreateCurveBoundaryFromPermanent
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