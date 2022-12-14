#ifndef NXOpen_CAM_INSPECTIONDELTAMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONDELTAMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionDeltaMoveBuilder.ja
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
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/CAM_InspectionDeltaMoveBuilder.hxx>
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
        class InspectionDeltaMoveBuilder;
    }
    namespace CAM
    {
        class InspectionMoveBuilder;
    }
    namespace CAM
    {
        class _InspectionDeltaMoveBuilderBuilder;
        class InspectionDeltaMoveBuilderImpl;
        /** Represents the builder for the CMM Inspection sub-operation Delta Move.  <br> To create a new instance of this class, use @link CAM::InspectionMoveCollection::CreateInspectionDeltaMoveBuilder  CAM::InspectionMoveCollection::CreateInspectionDeltaMoveBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionDeltaMoveBuilder : public CAM::InspectionMoveBuilder
        {
            /** Move Intent */
            public: enum IntentType
            {
                IntentTypeWcs/** WCS */,
                IntentTypeMcs/** MCS */
            };

            private: InspectionDeltaMoveBuilderImpl * m_inspectiondeltamovebuilder_impl;
            private: friend class  _InspectionDeltaMoveBuilderBuilder;
            protected: InspectionDeltaMoveBuilder();
            public: ~InspectionDeltaMoveBuilder();
            /**Returns  the delta X coordinate 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DeltaX
            (
            );
            /**Sets  the delta X coordinate 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDeltaX
            (
                double deltaX /** deltax */ 
            );
            /**Returns  the delta Y coordinate 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DeltaY
            (
            );
            /**Sets  the delta Y coordinate 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDeltaY
            (
                double deltaY /** deltay */ 
            );
            /**Returns  the delta Z coordinate 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double DeltaZ
            (
            );
            /**Sets  the delta Z coordinate 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDeltaZ
            (
                double deltaZ /** deltaz */ 
            );
            /**Returns  the intent 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionDeltaMoveBuilder::IntentType Intent
            (
            );
            /**Sets  the intent 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: void SetIntent
            (
                NXOpen::CAM::InspectionDeltaMoveBuilder::IntentType intent /** intent */ 
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
