#ifndef NXOpen_CAM_BOUNDARYTURNMEMBERSET_HXX_INCLUDED
#define NXOpen_CAM_BOUNDARYTURNMEMBERSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BoundaryTurnMemberSet.ja
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
#include <NXOpen/CAM_BoundaryTurnMemberEvents.hxx>
#include <NXOpen/CAM_BoundaryTurnMemberFeed.hxx>
#include <NXOpen/CAM_BoundaryTurnMemberFineFinishCorner.hxx>
#include <NXOpen/CAM_BoundaryTurnMemberFineFinishOffset.hxx>
#include <NXOpen/CAM_BoundaryTurnMemberOffset.hxx>
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
        class BoundaryTurnMemberSet;
    }
    namespace CAM
    {
        class BoundaryMemberSet;
    }
    namespace CAM
    {
        class BoundaryTurnMemberCorner;
    }
    namespace CAM
    {
        class BoundaryTurnMemberEvents;
    }
    namespace CAM
    {
        class BoundaryTurnMemberFeed;
    }
    namespace CAM
    {
        class BoundaryTurnMemberFineFinishCorner;
    }
    namespace CAM
    {
        class BoundaryTurnMemberFineFinishOffset;
    }
    namespace CAM
    {
        class BoundaryTurnMemberOffset;
    }
    namespace CAM
    {
        class _BoundaryTurnMemberSetBuilder;
        class BoundaryTurnMemberSetImpl;
        /** Represents a boundary turning member set . <br> This is an abstract class and cannot be instantiated.  <br> 
         <br>  Created in NX9.0.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  BoundaryTurnMemberSet : public NXOpen::CAM::BoundaryMemberSet
        {
            /** the types available for the concave corners */
            public: enum ConcaveCornersTypeValue
            {
                ConcaveCornersTypeValueExtend/** extend */ ,
                ConcaveCornersTypeValueConnectLinear/** connect linear */ 
            };

            private: BoundaryTurnMemberSetImpl * m_boundaryturnmemberset_impl;
            private: friend class  _BoundaryTurnMemberSetBuilder;
            protected: BoundaryTurnMemberSet();
            public: ~BoundaryTurnMemberSet();
            /**Returns  the ignore member toggle 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: bool IgnoreMember
            (
            );
            /**Sets  the ignore member toggle 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIgnoreMember
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the concave corners 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberSet::ConcaveCornersTypeValue ConcaveCorners
            (
            );
            /**Sets  the concave corners 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetConcaveCorners
            (
                NXOpen::CAM::BoundaryTurnMemberSet::ConcaveCornersTypeValue newValue /** newvalue */ 
            );
            /**Returns  the main corner 1 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberCorner * Corner1
            (
            );
            /**Returns  the main corner 2 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberCorner * Corner2
            (
            );
            /**Returns  the main offset 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberOffset * OffsetBuilder
            (
            );
            /**Returns  the fine finish corner 1 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberFineFinishCorner * FineFinishCorner1
            (
            );
            /**Returns  the fine finish corner 2 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberFineFinishCorner * FineFinishCorner2
            (
            );
            /**Returns  the fine finish offset 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberFineFinishOffset * FineFinishOffset
            (
            );
            /**Returns  the custom feed rate 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberFeed * CustomFeed
            (
            );
            /**Returns  the post events 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::BoundaryTurnMemberEvents * Events
            (
            );
            /**Returns  the ignore fine finish offset 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: bool IgnoreFineFinishOffset
            (
            );
            /**Sets  the ignore fine finish offset 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIgnoreFineFinishOffset
            (
                bool newValue /** newvalue */ 
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
