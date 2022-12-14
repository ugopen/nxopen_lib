#ifndef NXOpen_CAM_INSPECTIONCREATEPATHSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONCREATEPATHSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionCreatePathsBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAM_InspectionCreatePathsBuilder.hxx>
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
        class InspectionCreatePathsBuilder;
    }
    class Builder;
    namespace CAM
    {
        class InspectionGroup;
    }
    namespace CAM
    {
        class InspectionSetup;
    }
    class SelectNXObjectList;
    namespace CAM
    {
        class _InspectionCreatePathsBuilderBuilder;
        class InspectionCreatePathsBuilderImpl;
        /** Create Paths Dialog builder  <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionCreatePathsBuilder  CAM::InspectionOperationCollection::CreateInspectionCreatePathsBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionCreatePathsBuilder : public Builder
        {
            private: InspectionCreatePathsBuilderImpl * m_inspectioncreatepathsbuilder_impl;
            private: friend class  _InspectionCreatePathsBuilderBuilder;
            protected: InspectionCreatePathsBuilder();
            public: ~InspectionCreatePathsBuilder();
            /**Returns  the select features button 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectFeatures
            (
            );
            /**Returns  the tool to use for inspection 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ToolString
            (
            );
            /**Sets  the tool to use for inspection 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetToolString
            (
                const NXString & toolString /** toolstring */ 
            );
            /**Sets  the tool to use for inspection 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetToolString
            (
                const char * toolString /** toolstring */ 
            );
            /**Returns  the tip to use for inspection 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString TipString
            (
            );
            /**Sets  the tip to use for inspection 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTipString
            (
                const NXString & tipString /** tipstring */ 
            );
            /**Sets  the tip to use for inspection 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetTipString
            (
                const char * tipString /** tipstring */ 
            );
            /**Returns  the angle specification 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString AngleString
            (
            );
            /**Sets  the angle specification 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleString
            (
                const NXString & angleString /** anglestring */ 
            );
            /**Sets  the angle specification 
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
            /**Returns  the program location 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ProgramLocationString
            (
            );
            /**Sets  the program location 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgramLocationString
            (
                const NXString & programLocationString /** programlocationstring */ 
            );
            /**Sets  the program location 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetProgramLocationString
            (
                const char * programLocationString /** programlocationstring */ 
            );
            /** Returns the selected features.  @return  Selected features 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetSelectedFeatures
            (
            );
            /** Sets the selected features. 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSelectedFeatures
            (
                std::vector<NXString> & selectedFeatures /** Selected features   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates paths for the selected features. 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void CreatePaths
            (
            );
            /**Returns  the setup 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionSetup * Setup
            (
            );
            /**Sets  the setup 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSetup
            (
                NXOpen::CAM::InspectionSetup * setup /** setup */ 
            );
            /**Returns  the program group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGroup * ProgramGroup
            (
            );
            /**Sets  the program group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetProgramGroup
            (
                NXOpen::CAM::InspectionGroup * progGroup /** proggroup */ 
            );
            /**Returns  the tool group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGroup * ToolGroup
            (
            );
            /**Sets  the tool group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetToolGroup
            (
                NXOpen::CAM::InspectionGroup * toolGroup /** toolgroup */ 
            );
            /**Returns  the geometry group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGroup * GeometryGroup
            (
            );
            /**Sets  the geometry group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetGeometryGroup
            (
                NXOpen::CAM::InspectionGroup * geomGroup /** geomgroup */ 
            );
            /**Returns  the sensor group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionGroup * SensorGroup
            (
            );
            /**Sets  the sensor group 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSensorGroup
            (
                NXOpen::CAM::InspectionGroup * sensorGroup /** sensorgroup */ 
            );
            /**Returns  the method type name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString TypeName
            (
            );
            /**Sets  the method type name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTypeName
            (
                const NXString & typeName /** typename */ 
            );
            /**Sets  the method type name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetTypeName
            (
                const char * typeName /** typename */ 
            );
            /** Returns the selected features method  @return  Selected feature method tags 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAM::InspectionGroup *> GetFeatureMethods
            (
            );
            /** Sets the selected features method 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFeatureMethods
            (
                const std::vector<NXOpen::CAM::InspectionGroup *> & featureMethods /** Selected feature method tags */
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
