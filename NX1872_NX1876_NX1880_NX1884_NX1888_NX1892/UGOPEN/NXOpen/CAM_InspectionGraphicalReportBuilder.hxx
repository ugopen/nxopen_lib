#ifndef NXOpen_CAM_INSPECTIONGRAPHICALREPORTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONGRAPHICALREPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionGraphicalReportBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
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
        class InspectionGraphicalReportBuilder;
    }
    namespace CAM
    {
        class InspectionGraphicalVariableBuilderList;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class SelectNXObjectList;
    namespace CAM
    {
        class _InspectionGraphicalReportBuilderBuilder;
        class InspectionGraphicalReportBuilderImpl;
        /** Represents the builder for the CMM Inspection Graphical Report Operation  <br> To create a new instance of this class, use @link NXOpen::CAM::InspectionOperationCollection::CreateGraphicalReportBuilder  NXOpen::CAM::InspectionOperationCollection::CreateGraphicalReportBuilder @endlink  <br> 
         <br>  Created in NX10.0.3.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionGraphicalReportBuilder : public NXOpen::CAM::OperationBuilder
        {
            /** Types of graphical reports */
            public: enum GraphicalReportFilterType
            {
                GraphicalReportFilterTypeTolerances/** Tolerance based */,
                GraphicalReportFilterTypePoints/** Point based */,
                GraphicalReportFilterTypeTitlePage/** Title page */,
                GraphicalReportFilterTypeSummary/** Summary */,
                GraphicalReportFilterTypeMinMaxDiameter/** Minimum maximum diameter */
            };

            /** Filters for specifying report objects */
            public: enum GraphicalReportFilter
            {
                GraphicalReportFilterNone/** No filter */
            };

            private: InspectionGraphicalReportBuilderImpl * m_inspectiongraphicalreportbuilder_impl;
            private: friend class  _InspectionGraphicalReportBuilderBuilder;
            protected: InspectionGraphicalReportBuilder();
            public: ~InspectionGraphicalReportBuilder();
            /**Returns  the camera to use 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXString Camera
            (
            );
            /**Sets  the camera to use 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCamera
            (
                const NXString & camera /** camera */ 
            );
            /**Sets  the camera to use 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetCamera
            (
                const char * camera /** camera */ 
            );
            /** Cache the current view settings. 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SaveViewCacheSettings
            (
            );
            /** Capture the current view. 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void CaptureCurrentView
            (
            );
            /** Activate the specified view. 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void ActivateView
            (
            );
            /** Restore the original view. 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void RestoreOriginalView
            (
            );
            /**Returns  the report filter type 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGraphicalReportBuilder::GraphicalReportFilterType ReportFilterType
            (
            );
            /**Sets  the report filter type 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReportFilterType
            (
                NXOpen::CAM::InspectionGraphicalReportBuilder::GraphicalReportFilterType reportFilterType /** reportfiltertype */ 
            );
            /**Returns  the report filter object 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXString ReportFilterObject
            (
            );
            /**Sets  the report filter object 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReportFilterObject
            (
                const NXString & reportFilterObject /** reportfilterobject */ 
            );
            /**Sets  the report filter object 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetReportFilterObject
            (
                const char * reportFilterObject /** reportfilterobject */ 
            );
            /**Returns  the available objects screen selection button 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * AvailableSelection
            (
            );
            /**Returns  the option to report minimum cross section 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool MinCrossSection
            (
            );
            /**Sets  the option to report minimum cross section 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMinCrossSection
            (
                bool minCrossSection /** mincrosssection */ 
            );
            /**Returns  the option to report maximum cross section 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool MaxCrossSection
            (
            );
            /**Sets  the option to report maximum cross section 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMaxCrossSection
            (
                bool maxCrossSection /** maxcrosssection */ 
            );
            /**Returns  the option to report minimum out of round 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool MinOutOfRound
            (
            );
            /**Sets  the option to report minimum out of round 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMinOutOfRound
            (
                bool minOutOfRound /** minoutofround */ 
            );
            /**Returns  the option to report maximum out of round 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: bool MaxOutOfRound
            (
            );
            /**Sets  the option to report maximum out of round 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetMaxOutOfRound
            (
                bool maxOutOfRound /** maxoutofround */ 
            );
            /**Returns  the filter enum 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGraphicalReportBuilder::GraphicalReportFilter FilterEnum
            (
            );
            /**Sets  the filter enum 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFilterEnum
            (
                NXOpen::CAM::InspectionGraphicalReportBuilder::GraphicalReportFilter filterEnum /** filterenum */ 
            );
            /**Returns  the report operation name 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXString ReportName
            (
            );
            /**Sets  the report operation name 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReportName
            (
                const NXString & reportName /** reportname */ 
            );
            /**Sets  the report operation name 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetReportName
            (
                const char * reportName /** reportname */ 
            );
            /**Returns  the report title 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : None */
            public: NXString ReportTitle
            (
            );
            /**Sets  the report title 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReportTitle
            (
                const NXString & reportTitle /** reporttitle */ 
            );
            /**Sets  the report title 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetReportTitle
            (
                const char * reportTitle /** reporttitle */ 
            );
            /**Returns  the list of graphical variable builders 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGraphicalVariableBuilderList * VariablesList
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