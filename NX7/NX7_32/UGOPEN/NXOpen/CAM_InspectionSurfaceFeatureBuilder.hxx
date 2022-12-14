#ifndef NXOpen_CAM_INSPECTIONSURFACEFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSURFACEFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionSurfaceFeatureBuilder.ja
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
#include <NXOpen/CAM_InspectionSurfaceFeatureBuilder.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionSurfaceFeatureBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class SelectFace;
    namespace CAM
    {
        class _InspectionSurfaceFeatureBuilderBuilder;
        /** Represents a CMM Inspection Curve Feature builder  <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionSurfaceFeatureBuilder CAM::InspectionOperationCollection::CreateInspectionSurfaceFeatureBuilder@endlink  <br> */
        class NXOPENCPPEXPORT InspectionSurfaceFeatureBuilder : public CAM::OperationBuilder
        {
            private: friend class  _InspectionSurfaceFeatureBuilderBuilder;
            protected: InspectionSurfaceFeatureBuilder();
            /**Returns  the selected face  <br> License requirements : None */
            public: NXOpen::SelectFace * SelectedFace
            (
            );
            /**Returns  the reverse direction  <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
