#ifndef NXOpen_CAM_INSPECTIONSPHEREFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSPHEREFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionSphereFeatureBuilder.ja
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
#include <NXOpen/CAM_InspectionSphereFeatureBuilder.hxx>
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
        class InspectionSphereFeatureBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class SelectNXObject;
    namespace CAM
    {
        class _InspectionSphereFeatureBuilderBuilder;
        class InspectionSphereFeatureBuilderImpl;
        /** Represents a CMM inspection sphere feature builder  <br> To create a new instance of this class, use @link NXOpen::CAM::InspectionOperationCollection::CreateInspectionSphereFeatureBuilder  NXOpen::CAM::InspectionOperationCollection::CreateInspectionSphereFeatureBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionSphereFeatureBuilder : public NXOpen::CAM::OperationBuilder
        {
            private: InspectionSphereFeatureBuilderImpl * m_inspectionspherefeaturebuilder_impl;
            private: friend class  _InspectionSphereFeatureBuilderBuilder;
            protected: InspectionSphereFeatureBuilder();
            public: ~InspectionSphereFeatureBuilder();
            /**Returns  the selected sphere 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectSphere
            (
            );
            /**Returns  the csys ref type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationCsysreferencetypes CsysRefType
            (
            );
            /**Sets  the csys ref type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCsysRefType
            (
                NXOpen::CAM::CamInspectionOperationCsysreferencetypes csysRefType /** csysreftype */ 
            );
            /**Returns  the inner outer type (spherical hole or spherical boss) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationInneroutertypes InnerOuterType
            (
            );
            /**Sets  the inner outer type (spherical hole or spherical boss) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetInnerOuterType
            (
                NXOpen::CAM::CamInspectionOperationInneroutertypes innerOuterType /** inneroutertype */ 
            );
            /**Returns  the sphere diameter 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double Diameter
            (
            );
            /**Sets  the sphere diameter 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDiameter
            (
                double diameter /** diameter */ 
            );
            /**Returns  the sphere center point X coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double CenterPointX
            (
            );
            /**Sets  the sphere center point X coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCenterPointX
            (
                double centerPointX /** centerpointx */ 
            );
            /**Returns  the sphere center point Y coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double CenterPointY
            (
            );
            /**Sets  the sphere center point Y coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCenterPointY
            (
                double centerPointY /** centerpointy */ 
            );
            /**Returns  the sphere center point Z coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double CenterPointZ
            (
            );
            /**Sets  the sphere center point Z coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCenterPointZ
            (
                double centerPointZ /** centerpointz */ 
            );
            /**Returns  the sphere inspection feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the sphere inspection feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the sphere inspection feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Updates sphere inspection feature characteristic parameters based on selected geometry 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateParams
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
