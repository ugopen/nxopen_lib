#ifndef NXOpen_CAM_INSPECTIONSCANARCBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSCANARCBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionScanArcBuilder.ja
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
#include <NXOpen/CAM_InspectionScanArcBuilder.hxx>
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionScanArcBuilder;
    }
    namespace CAM
    {
        class InspectionMoveBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _InspectionScanArcBuilderBuilder;
        class InspectionScanArcBuilderImpl;
        /** Represents the builder for the CMM Inspection sub-operation Scan Arc.  <br> To create a new instance of this class, use @link CAM::InspectionMoveCollection::CreateInspectionScanArcBuilder CAM::InspectionMoveCollection::CreateInspectionScanArcBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  InspectionScanArcBuilder : public CAM::InspectionMoveBuilder
        {
            private: InspectionScanArcBuilderImpl * m_inspectionscanarcbuilder_impl;
            private: friend class  _InspectionScanArcBuilderBuilder;
            protected: InspectionScanArcBuilder();
            public: ~InspectionScanArcBuilder();
            /**Returns  the Arc  <br> License requirements : None */
            public: NXOpen::NXObject * Arc
            (
            );
            /**Sets  the Arc  <br> License requirements : None */
            public: void SetArc
            (
                NXOpen::NXObject * arc /** arc */ 
            );
            /**Returns  the Reverse Direction flag on the Arc  <br> License requirements : None */
            public: bool Reversedirection
            (
            );
            /**Sets  the Reverse Direction flag on the Arc  <br> License requirements : None */
            public: void SetReversedirection
            (
                bool reversedir /** reversedir */ 
            );
            /**Returns  the Start Distance of the Scan Arc  <br> License requirements : None */
            public: double StartDistance
            (
            );
            /**Sets  the Start Distance of the Scan Arc  <br> License requirements : None */
            public: void SetStartDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the End Distance of the Scan Arc  <br> License requirements : None */
            public: double EndDistance
            (
            );
            /**Sets  the End Distance of the Scan Arc  <br> License requirements : None */
            public: void SetEndDistance
            (
                double distance /** distance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif