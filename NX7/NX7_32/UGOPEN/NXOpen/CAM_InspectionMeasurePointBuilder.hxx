#ifndef NXOpen_CAM_INSPECTIONMEASUREPOINTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONMEASUREPOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionMeasurePointBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_InspectionMeasurePointBuilder.hxx>
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionMeasurePointBuilder;
    }
    namespace CAM
    {
        class InspectionMoveBuilder;
    }
    class Point;
    namespace CAM
    {
        class _InspectionMeasurePointBuilderBuilder;
        /** Represents the builder for the CMM Inspection sub-operation Linear Move To Point.  <br> To create a new instance of this class, use @link CAM::InspectionMoveCollection::CreateInspectionMeasurePointBuilder CAM::InspectionMoveCollection::CreateInspectionMeasurePointBuilder@endlink  <br> */
        class NXOPENCPPEXPORT InspectionMeasurePointBuilder : public CAM::InspectionMoveBuilder
        {
            private: friend class  _InspectionMeasurePointBuilderBuilder;
            protected: InspectionMeasurePointBuilder();
            /**Returns  the point  <br> License requirements : None */
            public: NXOpen::Point * TargetPoint
            (
            );
            /**Sets  the point  <br> License requirements : None */
            public: void SetTargetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the I direction at measured point  <br> License requirements : None */
            public: double I
            (
            );
            /**Sets  the I direction at measured point  <br> License requirements : None */
            public: void SetI
            (
                double direction /** direction */ 
            );
            /**Returns  the J direction at measured point  <br> License requirements : None */
            public: double J
            (
            );
            /**Sets  the J direction at measured point  <br> License requirements : None */
            public: void SetJ
            (
                double direction /** direction */ 
            );
            /**Returns  the K direction at measured point  <br> License requirements : None */
            public: double K
            (
            );
            /**Sets  the K direction at measured point  <br> License requirements : None */
            public: void SetK
            (
                double direction /** direction */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
