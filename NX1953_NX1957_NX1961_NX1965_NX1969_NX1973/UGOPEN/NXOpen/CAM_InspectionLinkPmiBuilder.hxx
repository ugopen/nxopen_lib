#ifndef NXOpen_CAM_INSPECTIONLINKPMIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONLINKPMIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionLinkPmiBuilder.ja
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
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class InspectionLinkPmiBuilder;
    }
    class Builder;
    class SelectNXObjectList;
    namespace CAM
    {
        class _InspectionLinkPmiBuilderBuilder;
        class InspectionLinkPmiBuilderImpl;
        /** Create Link PMI Dialog Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::InspectionOperationCollection::CreateInspectionLinkPmiBuilder  NXOpen::CAM::InspectionOperationCollection::CreateInspectionLinkPmiBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionLinkPmiBuilder : public NXOpen::Builder
        {
            /** Specifies the scope of the link PMI command */
            public: enum PmiScopeTypes
            {
                PmiScopeTypesWorkpieceOnly/** Link PMI will be performed for the workpiece only */,
                PmiScopeTypesWorkpieceandComponents/** Link PMI will be performed for the workpiece and components */
            };

            /** Specifies whether paths will be created by Link PMI */
            public: enum CreatePathsOptions
            {
                CreatePathsOptionsYes/** Paths will be created by Link PMI */,
                CreatePathsOptionsNo/** Paths will not be created by Link PMI */
            };

            /** Specifies the Point Order Optimization Type */
            public: enum PointOrderTypes
            {
                PointOrderTypesOff/** No point order optimization will be done */,
                PointOrderTypesNearestNeighbor/** Point order optimization will use the nearest neighbor method */,
                PointOrderTypesShortestPath/** Point order optimization will use the shortest path method */
            };

            /** Specifies the Path Order Optimization Type */
            public: enum PathOrderTypes
            {
                PathOrderTypesOff/** No path order optimization will be done */,
                PathOrderTypesBySensor/** Path order optimization will use the by sensor method */,
                PathOrderTypesNearestNeighbor/** Path order optimization will use the nearest neighbor method */,
                PathOrderTypesShortestPath/** Path order optimization will use the shortest path method */
            };

            /** Specifies whether collision avoidance will be done */
            public: enum CollisionAvoidanceEnumType
            {
                CollisionAvoidanceEnumTypeOff/** Collision avoidance will not be done */,
                CollisionAvoidanceEnumTypeOn/** Collision avoidance will be done */
            };

            private: InspectionLinkPmiBuilderImpl * m_inspectionlinkpmibuilder_impl;
            private: friend class  _InspectionLinkPmiBuilderBuilder;
            protected: InspectionLinkPmiBuilder();
            public: ~InspectionLinkPmiBuilder();
            /**Returns  the name of the workpiece to be processed by Link PMI 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString WorkpieceString
            (
            );
            /**Sets  the name of the workpiece to be processed by Link PMI 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetWorkpieceString
            (
                const NXString & workpieceString /** workpiecestring */ 
            );
            /**Sets  the name of the workpiece to be processed by Link PMI 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetWorkpieceString
            (
                const char * workpieceString /** workpiecestring */ 
            );
            /**Returns  the scope of the Link PMI function 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionLinkPmiBuilder::PmiScopeTypes ScopeEnum
            (
            );
            /**Sets  the scope of the Link PMI function 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetScopeEnum
            (
                NXOpen::CAM::InspectionLinkPmiBuilder::PmiScopeTypes scopeEnum /** scopeenum */ 
            );
            /**Returns  the PMI View selection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ViewString
            (
            );
            /**Sets  the PMI View selection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetViewString
            (
                const NXString & viewString /** viewstring */ 
            );
            /**Sets  the PMI View selection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetViewString
            (
                const char * viewString /** viewstring */ 
            );
            /**Returns  the create paths enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionLinkPmiBuilder::CreatePathsOptions CreatePathsEnum
            (
            );
            /**Sets  the create paths enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCreatePathsEnum
            (
                NXOpen::CAM::InspectionLinkPmiBuilder::CreatePathsOptions createPathsEnum /** createpathsenum */ 
            );
            /**Returns  the tool to use for inspection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ToolString
            (
            );
            /**Sets  the tool to use for inspection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetToolString
            (
                const NXString & toolString /** toolstring */ 
            );
            /**Sets  the tool to use for inspection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetToolString
            (
                const char * toolString /** toolstring */ 
            );
            /**Returns  the tip to use for inspection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString TipString
            (
            );
            /**Sets  the tip to use for inspection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTipString
            (
                const NXString & tipString /** tipstring */ 
            );
            /**Sets  the tip to use for inspection string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetTipString
            (
                const char * tipString /** tipstring */ 
            );
            /**Returns  the angle specification string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AngleString
            (
            );
            /**Sets  the angle specification string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleString
            (
                const NXString & angleString /** anglestring */ 
            );
            /**Sets  the angle specification string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetAngleString
            (
                const char * angleString /** anglestring */ 
            );
            /**Returns  the A angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleA
            (
            );
            /**Sets  the A angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleA
            (
                double angleA /** anglea */ 
            );
            /**Returns  the B angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleB
            (
            );
            /**Sets  the B angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleB
            (
                double angleB /** angleb */ 
            );
            /** Button to select safe plane 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SafePlaneSelectAction
            (
            );
            /** Button to display selected safe plane 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SafePlaneDisplayAction
            (
            );
            /**Returns  the point order optimization type enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionLinkPmiBuilder::PointOrderTypes PointOrderEnum
            (
            );
            /**Sets  the point order optimization type enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetPointOrderEnum
            (
                NXOpen::CAM::InspectionLinkPmiBuilder::PointOrderTypes pointOrderEnum /** pointorderenum */ 
            );
            /**Returns  the path order optimization type enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionLinkPmiBuilder::PathOrderTypes PathOrderEnum
            (
            );
            /**Sets  the path order optimization type enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetPathOrderEnum
            (
                NXOpen::CAM::InspectionLinkPmiBuilder::PathOrderTypes pathOrderEnum /** pathorderenum */ 
            );
            /**Returns  the collision avoidance enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionLinkPmiBuilder::CollisionAvoidanceEnumType CollisionAvoidanceEnum
            (
            );
            /**Sets  the collision avoidance enum 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCollisionAvoidanceEnum
            (
                NXOpen::CAM::InspectionLinkPmiBuilder::CollisionAvoidanceEnumType collisionAvoidanceEnum /** collisionavoidanceenum */ 
            );
            /**Returns  the program location string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ProgramLocationString
            (
            );
            /**Sets  the program location string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgramLocationString
            (
                const NXString & programLocationString /** programlocationstring */ 
            );
            /**Sets  the program location string 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetProgramLocationString
            (
                const char * programLocationString /** programlocationstring */ 
            );
            /** Links PMI and GDT to Inspection features and tolerances. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void LinkToPmi
            (
            );
            /** Get results from Link PMI.  @return  Results strings 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: std::vector<NXString> GetResults
            (
            );
            /** Output results report from Link PMI. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void OutputResults
            (
                NXOpen::ListingWindow::DeviceType deviceType /** The type of device (file, Information window, or both) */,
                const NXString & fileName /** Name of the file.  Used only if the device type is file or both. */
            );
            /** Output results report from Link PMI. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void OutputResults
            (
                NXOpen::ListingWindow::DeviceType deviceType /** The type of device (file, Information window, or both) */,
                const char * fileName /** Name of the file.  Used only if the device type is file or both. */
            );
            /**Returns  the preferred probe tip type 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionMoveBuilder::ProbeTipTypes ProbeTipType
            (
            );
            /**Sets  the preferred probe tip type 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProbeTipType
            (
                NXOpen::CAM::InspectionMoveBuilder::ProbeTipTypes tipType /** tiptype */ 
            );
            /**Returns  the component selector 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * ComponentSelection
            (
            );
            /**Returns  the include sub-components option 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: bool IncludeSubComponents
            (
            );
            /**Sets  the include sub-components option 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIncludeSubComponents
            (
                bool includeSubComponents /** includesubcomponents */ 
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
