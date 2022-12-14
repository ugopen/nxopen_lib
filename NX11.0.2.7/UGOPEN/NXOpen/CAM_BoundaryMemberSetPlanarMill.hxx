#ifndef NXOpen_CAM_BOUNDARYMEMBERSETPLANARMILL_HXX_INCLUDED
#define NXOpen_CAM_BOUNDARYMEMBERSETPLANARMILL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BoundaryMemberSetPlanarMill.ja
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
#include <NXOpen/CAM_BoundaryMemberSet.hxx>
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
        class BoundaryMemberSetPlanarMill;
    }
    namespace CAM
    {
        class BoundaryMemberSet;
    }
    namespace CAM
    {
        class _BoundaryMemberSetPlanarMillBuilder;
        class BoundaryMemberSetPlanarMillImpl;
        /** Represents a boundary member set . <br> To create a new instance of this class, use @link NXOpen::CAM::BoundarySetPlanarMill::CreateBoundaryMemberSetPlanarMill  NXOpen::CAM::BoundarySetPlanarMill::CreateBoundaryMemberSetPlanarMill @endlink  <br> 
         <br>  Created in NX11.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  BoundaryMemberSetPlanarMill : public NXOpen::CAM::BoundaryMemberSet
        {
            /** the types available for the feed rate unit */
            public: enum FeedUnitTypes
            {
                FeedUnitTypesNone/** no feed rate unit*/,
                FeedUnitTypesPerMinute/** use per minute as the feed rate unit*/,
                FeedUnitTypesPerRevolution/** use per revolution as the feed rate unit*/
            };

            private: BoundaryMemberSetPlanarMillImpl * m_boundarymembersetplanarmill_impl;
            private: friend class  _BoundaryMemberSetPlanarMillBuilder;
            protected: BoundaryMemberSetPlanarMill();
            public: ~BoundaryMemberSetPlanarMill();
            /**Returns  the tool position 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: int ToolPosition
            (
            );
            /**Sets  the tool position 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolPosition
            (
                int newValue /** newvalue */ 
            );
            /**Returns  the tolerance status 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CustomTolerance
            (
            );
            /**Sets  the tolerance status 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomTolerance
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the intol value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double InTolerance
            (
            );
            /**Sets  the intol value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInTolerance
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the outtol value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: double OutTolerance
            (
            );
            /**Sets  the outtol value 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOutTolerance
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
            /**Returns  the feed rate status 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool CustomFeed
            (
            );
            /**Sets  the feed rate status 
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
            public: NXOpen::CAM::BoundaryMemberSetPlanarMill::FeedUnitTypes FeedUnit
            (
            );
            /**Sets  the feed rate unit 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeedUnit
            (
                NXOpen::CAM::BoundaryMemberSetPlanarMill::FeedUnitTypes newUnit /** newunit */ 
            );
            /** Start on this member 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void StartOnThisMember
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
