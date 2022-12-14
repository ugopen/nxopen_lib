#ifndef NXOpen_CAM_INSPECTIONCONEFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONCONEFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionConeFeatureBuilder.ja
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
#include <NXOpen/CAM_InspectionOperationEnums.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class InspectionConeFeatureBuilder;
    }
    namespace CAM
    {
        class InspectionAxisExtrapolationModeBuilder;
    }
    namespace CAM
    {
        class InspectionCylinderCircleFitModeBuilder;
    }
    namespace CAM
    {
        class InspectionFeatureDataFilterBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class Direction;
    class SelectNXObject;
    namespace CAM
    {
        class _InspectionConeFeatureBuilderBuilder;
        class InspectionConeFeatureBuilderImpl;
        /** Represents a CMM Inspection Cone Feature builder  <br> To create a new instance of this class, use @link NXOpen::CAM::InspectionOperationCollection::CreateInspectionConeFeatureBuilder  NXOpen::CAM::InspectionOperationCollection::CreateInspectionConeFeatureBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionConeFeatureBuilder : public NXOpen::CAM::OperationBuilder
        {
            private: InspectionConeFeatureBuilderImpl * m_inspectionconefeaturebuilder_impl;
            private: friend class  _InspectionConeFeatureBuilderBuilder;
            protected: InspectionConeFeatureBuilder();
            public: ~InspectionConeFeatureBuilder();
            /**Returns  the selected cone 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectedCone
            (
            );
            /**Returns  the cones axis vector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * AxisVector
            (
            );
            /**Sets  the cones axis vector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisVector
            (
                NXOpen::Direction * axisVector /** axisvector */ 
            );
            /**Returns  the coordinate system reference type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationCsysreferencetypes CsysReferenceType
            (
            );
            /**Sets  the coordinate system reference type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCsysReferenceType
            (
                NXOpen::CAM::CamInspectionOperationCsysreferencetypes csysReferenceType /** csysreferencetype */ 
            );
            /**Returns  the inspection feature inner/outer type (hole/pin) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationInneroutertypes InnerOuterType
            (
            );
            /**Sets  the inspection feature inner/outer type (hole/pin) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetInnerOuterType
            (
                NXOpen::CAM::CamInspectionOperationInneroutertypes innerOuterType /** inneroutertype */ 
            );
            /**Returns  the included angle of the cone 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double IncludedAngle
            (
            );
            /**Sets  the included angle of the cone 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIncludedAngle
            (
                double includedAngle /** includedangle */ 
            );
            /**Returns  the extent type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationExtenttypes ExtentType
            (
            );
            /**Sets  the extent type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetExtentType
            (
                NXOpen::CAM::CamInspectionOperationExtenttypes extentType /** extenttype */ 
            );
            /**Returns  the vertex point X coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double VertexPointX
            (
            );
            /**Sets  the vertex point X coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVertexPointX
            (
                double vertexPointX /** vertexpointx */ 
            );
            /**Returns  the vertex point Y coordinate
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double VertexPointY
            (
            );
            /**Sets  the vertex point Y coordinate
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVertexPointY
            (
                double vertexPointY /** vertexpointy */ 
            );
            /**Returns  the vertex point Z coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double VertexPointZ
            (
            );
            /**Sets  the vertex point Z coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVertexPointZ
            (
                double vertexPointZ /** vertexpointz */ 
            );
            /**Returns  the axis direction vector I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double AxisDirectionI
            (
            );
            /**Sets  the axis direction vector I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisDirectionI
            (
                double axisDirectionI /** axisdirectioni */ 
            );
            /**Returns  the axis direction vector J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double AxisDirectionJ
            (
            );
            /**Sets  the axis direction vector J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisDirectionJ
            (
                double axisDirectionJ /** axisdirectionj */ 
            );
            /**Returns  the axis direction vector K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double AxisDirectionK
            (
            );
            /**Sets  the axis direction vector K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisDirectionK
            (
                double axisDirectionK /** axisdirectionk */ 
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
            /** Updates cone inspection feature characteristic parameters based on selected geometry 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateParams
            (
            );
            /**Returns  the Cylinder Circle Fitting Mode Builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCylinderCircleFitModeBuilder * CylinderCircleFitModeBuilder
            (
            );
            /**Returns  the Axis Extrapolation Mode Builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionAxisExtrapolationModeBuilder * AxisExtrapolationModeBuilder
            (
            );
            /**Returns  the Data Filter Builder 
             <br>  Created in NX1880.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionFeatureDataFilterBuilder * DataFilterBuilder
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
