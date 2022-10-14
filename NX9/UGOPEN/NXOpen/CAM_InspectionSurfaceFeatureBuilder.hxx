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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/CAM_InspectionSurfaceFeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class InspectionSurfaceFeatureBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class SelectFace;
    class SelectPointList;
    namespace CAM
    {
        class _InspectionSurfaceFeatureBuilderBuilder;
        class InspectionSurfaceFeatureBuilderImpl;
        /** Represents a CMM Inspection Curve Feature builder  <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionSurfaceFeatureBuilder  CAM::InspectionOperationCollection::CreateInspectionSurfaceFeatureBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionSurfaceFeatureBuilder : public CAM::OperationBuilder
        {
            /** The method used to define point data */
            public: enum PointDataDefinitionType
            {
                PointDataDefinitionTypeNone/** No point data is defined */,
                PointDataDefinitionTypePointSet/** A set of points are defined using parameters */,
                PointDataDefinitionTypeIndividualPoints/** Individual points are defined */
            };

            /** the method used to define the start and end points */
            public: enum StartEndModeType
            {
                StartEndModeTypePercentage/** Percent */,
                StartEndModeTypeDistance/** Distance */
            };

            private: InspectionSurfaceFeatureBuilderImpl * m_inspectionsurfacefeaturebuilder_impl;
            private: friend class  _InspectionSurfaceFeatureBuilderBuilder;
            protected: InspectionSurfaceFeatureBuilder();
            public: ~InspectionSurfaceFeatureBuilder();
            /**Returns  the selected face 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * SelectedFace
            (
            );
            /**Returns  the reverse direction 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the point data definition type 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionSurfaceFeatureBuilder::PointDataDefinitionType PointDataDefinition
            (
            );
            /**Sets  the point data definition type 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetPointDataDefinition
            (
                NXOpen::CAM::InspectionSurfaceFeatureBuilder::PointDataDefinitionType pointDataDefinition /** pointdatadefinition */ 
            );
            /**Returns  the number of U points 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: int NumberOfUPoints
            (
            );
            /**Sets  the number of U points 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNumberOfUPoints
            (
                int numberOfUPoints /** numberofupoints */ 
            );
            /**Returns  the number of V points 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: int NumberOfVPoints
            (
            );
            /**Sets  the number of V points 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNumberOfVPoints
            (
                int numberOfVPoints /** numberofvpoints */ 
            );
            /**Returns  the U start end mode 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionSurfaceFeatureBuilder::StartEndModeType UStartEndMode
            (
            );
            /**Sets  the U start end mode 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetUStartEndMode
            (
                NXOpen::CAM::InspectionSurfaceFeatureBuilder::StartEndModeType uStartEndMode /** ustartendmode */ 
            );
            /**Returns  the start percent in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double StartUPercent
            (
            );
            /**Sets  the start percent in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartUPercent
            (
                double startUPercent /** startupercent */ 
            );
            /**Returns  the end percent in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double EndUPercent
            (
            );
            /**Sets  the end percent in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEndUPercent
            (
                double endUPercent /** endupercent */ 
            );
            /**Returns  the start distance in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double StartUDistance
            (
            );
            /**Sets  the start distance in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartUDistance
            (
                double startUDistance /** startudistance */ 
            );
            /**Returns  the end distance in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double EndUDistance
            (
            );
            /**Sets  the end distance in the U direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEndUDistance
            (
                double endUDistance /** endudistance */ 
            );
            /**Returns  the V start end mode 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionSurfaceFeatureBuilder::StartEndModeType VStartEndMode
            (
            );
            /**Sets  the V start end mode 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVStartEndMode
            (
                NXOpen::CAM::InspectionSurfaceFeatureBuilder::StartEndModeType vStartEndMode /** vstartendmode */ 
            );
            /**Returns  the start percent n the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double StartVPercent
            (
            );
            /**Sets  the start percent n the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartVPercent
            (
                double startVPercent /** startvpercent */ 
            );
            /**Returns  the end percent in the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double EndVPercent
            (
            );
            /**Sets  the end percent in the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEndVPercent
            (
                double endVPercent /** endvpercent */ 
            );
            /**Returns  the start distance n the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double StartVDistance
            (
            );
            /**Sets  the start distance n the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartVDistance
            (
                double startVDistance /** startvdistance */ 
            );
            /**Returns  the end distance in the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: double EndVDistance
            (
            );
            /**Sets  the end distance in the V direction 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEndVDistance
            (
                double endVDistance /** endvdistance */ 
            );
            /**Returns  the user specified point selector 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * PointSelector
            (
            );
            /**Returns  the name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Creates preview of point definition data 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void PreviewPointData
            (
                bool showExisting /** showexisting */ 
            );
            /**Returns  the point data definition changed flag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsPointDefinitionChanged
            (
            );
            /**Sets  the point data definition changed flag 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetPointDefinitionChanged
            (
                bool isChanged /** ischanged */ 
            );
            /** Erases display of point definition data 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void ErasePointDefinitionDisplay
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