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
#include <NXOpen/CAM_InspectionDeltaMoveBuilder.hxx>
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents the builder for the CMM Inspection sub-operation Delta Move.  <br> To create a new instance of this class, use @link CAM::InspectionMoveCollection::CreateInspectionDeltaMoveBuilder CAM::InspectionMoveCollection::CreateInspectionDeltaMoveBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  InspectionDeltaMoveBuilder : public CAM::InspectionMoveBuilder
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
            /**Returns  the delta X coordinate  <br> License requirements : None */
            public: double DeltaX
            (
            );
            /**Sets  the delta X coordinate  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDeltaX
            (
                double deltaX /** deltax */ 
            );
            /**Returns  the delta Y coordinate  <br> License requirements : None */
            public: double DeltaY
            (
            );
            /**Sets  the delta Y coordinate  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDeltaY
            (
                double deltaY /** deltay */ 
            );
            /**Returns  the delta Z coordinate  <br> License requirements : None */
            public: double DeltaZ
            (
            );
            /**Sets  the delta Z coordinate  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDeltaZ
            (
                double deltaZ /** deltaz */ 
            );
            /**Returns  the intent  <br> License requirements : None */
            public: NXOpen::CAM::InspectionDeltaMoveBuilder::IntentType Intent
            (
            );
            /**Sets  the intent  <br> License requirements : None */
            public: void SetIntent
            (
                NXOpen::CAM::InspectionDeltaMoveBuilder::IntentType intent /** intent */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif