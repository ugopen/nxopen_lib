#ifndef NXOpen_CAM_WEDMBASEDGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMBASEDGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmBasedGeomBuilder.ja
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
#include <NXOpen/CAM_ParamBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class WedmBasedGeomBuilder;
    }
    namespace CAM
    {
        class LayoutCiBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _WedmBasedGeomBuilderBuilder;
        /** Represents a WedmBasedGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateWedmBasedGeomBuilder CAM::NCGroupCollection::CreateWedmBasedGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WedmBasedGeomBuilder : public CAM::ParamBuilder
        {
            private: friend class  _WedmBasedGeomBuilderBuilder;
            protected: WedmBasedGeomBuilder();
            /**Returns  the Rough and Backburn Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: int BackburnFlag
            (
            );
            /**Sets  the Rough and Backburn Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBackburnFlag
            (
                int backburnFlag /** the Backburn Flag  */
            );
            /**Returns  the Backburn Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: int BackburnPasses
            (
            );
            /**Sets  the Backburn Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBackburnPasses
            (
                int backburnPasses /** the Backburn Passes  */
            );
            /**Returns  the Rough Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: int RoughPasses
            (
            );
            /**Sets  the Rough Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRoughPasses
            (
                int roughPasses /** the Rough Passes  */
            );
            /**Returns  the Finish Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: int FinishPasses
            (
            );
            /**Sets  the Finish Passes  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFinishPasses
            (
                int finishPasses /** the Finish Passes  */
            );
            /**Returns  the Backburn Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double BackburnDistance
            (
            );
            /**Sets  the Backburn Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBackburnDistance
            (
                double backburnDistance /** the Backburn Distance  */
            );
            /**Returns  the Wire Diameter  <br> License requirements : cam_base ("CAM BASE") */
            public: double WireDiameter
            (
            );
            /**Sets  the Wire Diameter  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetWireDiameter
            (
                double wireDiameter /** the Wire Diameter  */
            );
            /**Returns  the Upper Plane  <br> License requirements : cam_base ("CAM BASE") */
            public: double UpperPlane
            (
            );
            /**Sets  the Upper Plane  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetUpperPlane
            (
                double upperPlane /** the Upper Plane  */
            );
            /**Returns  the Lower Plane  <br> License requirements : cam_base ("CAM BASE") */
            public: double LowerPlane
            (
            );
            /**Sets  the Lower Plane  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLowerPlane
            (
                double lowerPlane /** the Lower Plane  */
            );
            /**Returns  the Cut Direction  <br> License requirements : cam_base ("CAM BASE") */
            public: int CutDirection
            (
            );
            /**Sets  the Cut Direction  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutDirection
            (
                int cutDirection /** the Cut Direction  */
            );
            /**Returns  the Stop Point Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: int StopPointFlag
            (
            );
            /**Sets  the Stop Point Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStopPointFlag
            (
                int stopPointFlag /** the Stop Point Flag  */
            );
            /**Returns  the Stop Point Type  <br> License requirements : cam_base ("CAM BASE") */
            public: int StopPointType
            (
            );
            /**Sets  the Stop Point Type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStopPointType
            (
                int stopPointType /** the Stop Point Type  */
            );
            /**Returns  the Stop Point Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double StopPointDistance
            (
            );
            /**Sets  the Stop Point Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStopPointDistance
            (
                double stopPointDistance /** the Stop Point Distance  */
            );
            /**Returns  the Nocore Stock  <br> License requirements : cam_base ("CAM BASE") */
            public: double NocoreStock
            (
            );
            /**Sets  the Nocore Stock  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNocoreStock
            (
                double nocoreStock /** the Nocore Stock  */
            );
            /**Returns  the Stepover Type  <br> License requirements : cam_base ("CAM BASE") */
            public: int StepoverType
            (
            );
            /**Sets  the Stepover Type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverType
            (
                int stepoverType /** the Stepover Type */
            );
            /**Returns  the Stepover Percent  <br> License requirements : cam_base ("CAM BASE") */
            public: double StepoverPercent
            (
            );
            /**Sets  the Stepover Percent  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverPercent
            (
                double stepoverPercent /** the Stepover Percent */
            );
            /**Returns  the Stepover Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double StepoverDistance
            (
            );
            /**Sets  the Stepover Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepoverDistance
            (
                double stepoverDistance /** the Stepover Distance */
            );
            /**Returns  the Smooth Leadin Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: int SmoothLeadinFlag
            (
            );
            /**Sets  the Smooth Leadin Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSmoothLeadinFlag
            (
                int leadInFlag /** the Smooth Leadin Flag  */
            );
            /**Returns  the Smooth Leadin Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double SmoothLeadinDistance
            (
            );
            /**Sets  the Smooth Leadin Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSmoothLeadinDistance
            (
                double leadInDistance /** the Smooth Leadin Distance  */
            );
            /**Returns  the Smooth Leadout Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: int SmoothLeadoutFlag
            (
            );
            /**Sets  the Smooth Leadout Flag  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSmoothLeadoutFlag
            (
                int leadOutFlag /** the Smooth Leadout Flag  */
            );
            /**Returns  the Smooth Leadout Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double SmoothLeadoutDistance
            (
            );
            /**Sets  the Smooth Leadout Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSmoothLeadoutDistance
            (
                double leadOutDistance /** the Smooth Leadout Distance  */
            );
            /**Returns  the From Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: int FromPointStatus
            (
            );
            /**Sets  the From Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFromPointStatus
            (
                int status /** the From Point Status  */
            );
            /**Returns  the From Point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * FromPoint
            (
            );
            /**Sets  the From Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFromPoint
            (
                NXOpen::NXObject * point /** the From Point */
            );
            /**Returns  the From Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * FromPointToolAxis
            (
            );
            /**Sets  the From Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFromPointToolAxis
            (
                NXOpen::NXObject * tool_axis /** the From Point Tool Axis */
            );
            /**Returns  the Thread Hole Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: int ThreadHolePointStatus
            (
            );
            /**Sets  the Thread Hole Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetThreadHolePointStatus
            (
                int status /** the Thread Hole Point Status  */
            );
            /**Returns  the Thread Hole Point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * ThreadHolePoint
            (
            );
            /**Sets  the Thread Hole Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetThreadHolePoint
            (
                NXOpen::NXObject * point /** the Thread Hole Point */
            );
            /**Returns  the Thread Hole Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * ThreadHolePointToolAxis
            (
            );
            /**Sets  the Thread Hole Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetThreadHolePointToolAxis
            (
                NXOpen::NXObject * tool_axis /** the Thread Hole Point Tool Axis */
            );
            /**Returns  the Retract Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: int RetractPointStatus
            (
            );
            /**Sets  the Retract Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractPointStatus
            (
                int status /** the Retract Point Status  */
            );
            /**Returns  the Retract Point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * RetractPoint
            (
            );
            /**Sets  the Retract Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractPoint
            (
                NXOpen::NXObject * point /** the Retract Point */
            );
            /**Returns  the Retract Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * RetractPointToolAxis
            (
            );
            /**Sets  the Retract Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractPointToolAxis
            (
                NXOpen::NXObject * tool_axis /** the Retract Point Tool Axis */
            );
            /**Returns  the Go Home Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: int GoHomePointStatus
            (
            );
            /**Sets  the Go Home Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGoHomePointStatus
            (
                int status /** the Go Home Point Status  */
            );
            /**Returns  the Go Home Point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * GoHomePoint
            (
            );
            /**Sets  the Go Home Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGoHomePoint
            (
                NXOpen::NXObject * point /** the Go Home Point */
            );
            /**Returns  the Go Home Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * GoHomePointToolAxis
            (
            );
            /**Sets  the Go Home Point Tool Axis  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetGoHomePointToolAxis
            (
                NXOpen::NXObject * tool_axis /** the Go Home Point Tool Axis */
            );
            /**Returns  the Lead In Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: int LeadInPointStatus
            (
            );
            /**Sets  the Lead In Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLeadInPointStatus
            (
                int status /** the Lead In Point Status  */
            );
            /**Returns  the Lead In Point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * LeadInPoint
            (
            );
            /**Sets  the Lead In Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLeadInPoint
            (
                NXOpen::NXObject * point /** the Lead In Point */
            );
            /**Returns  the Lead Out Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: int LeadOutPointStatus
            (
            );
            /**Sets  the Lead Out Point Status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLeadOutPointStatus
            (
                int status /** the Lead Out Point Status  */
            );
            /**Returns  the Lead Out Point  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::NXObject * LeadOutPoint
            (
            );
            /**Sets  the Lead Out Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLeadOutPoint
            (
                NXOpen::NXObject * point /** the Lead Out Point */
            );
            /**Returns  the Tab Points  <br> License requirements : cam_base ("CAM BASE") */
            public: int NumTabs
            (
            );
            /**Sets  the Tab Points  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNumTabs
            (
                int num_tabs /** the Num Tabs  */
            );
            /**Returns  the Tab Points Region Method  <br> License requirements : cam_base ("CAM BASE") */
            public: int RegionMethod
            (
            );
            /**Sets  the Tab Points Region Method  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRegionMethod
            (
                int region_method /** the Tab Points Region Method  */
            );
            /**Returns  the Save Layer/Layout builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::LayoutCiBuilder * LayoutCiBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
