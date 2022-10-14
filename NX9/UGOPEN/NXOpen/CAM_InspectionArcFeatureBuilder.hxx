#ifndef NXOpen_CAM_INSPECTIONARCFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONARCFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionArcFeatureBuilder.ja
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
#include <NXOpen/CAM_InspectionArcFeatureBuilder.hxx>
#include <NXOpen/CAM_InspectionOperationEnums.hxx>
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
        class InspectionArcFeatureBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InspectionCylinderCircleFitModeBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class SelectNXObjectList;
    namespace CAM
    {
        class _InspectionArcFeatureBuilderBuilder;
        class InspectionArcFeatureBuilderImpl;
        /** Represents a CMM Inspection Arc Feature builder  <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionArcFeatureBuilder  CAM::InspectionOperationCollection::CreateInspectionArcFeatureBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionArcFeatureBuilder : public CAM::OperationBuilder
        {
            private: InspectionArcFeatureBuilderImpl * m_inspectionarcfeaturebuilder_impl;
            private: friend class  _InspectionArcFeatureBuilderBuilder;
            protected: InspectionArcFeatureBuilder();
            public: ~InspectionArcFeatureBuilder();
            /**Returns  the selected Arc 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectArc
            (
            );
            /**Returns  the reverse normal vector direction button 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse normal vector direction button 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the coordinate system reference type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationCsysreferencetypes CsysRefType
            (
            );
            /**Sets  the coordinate system reference type 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCsysRefType
            (
                NXOpen::CAM::CamInspectionOperationCsysreferencetypes csysRefType /** csysreftype */ 
            );
            /**Returns  the inspection feature inner/outer type (hole/pin) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationInneroutertypes InOutType
            (
            );
            /**Sets  the inspection feature inner/outer type (hole/pin) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetInOutType
            (
                NXOpen::CAM::CamInspectionOperationInneroutertypes inOutType /** inouttype */ 
            );
            /**Returns  the inspection feature radius 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double Radius
            (
            );
            /**Sets  the inspection feature radius 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetRadius
            (
                double radius /** radius */ 
            );
            /**Returns  the start vector I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double StartVectorI
            (
            );
            /**Sets  the start vector I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartVectorI
            (
                double startVectorI /** startvectori */ 
            );
            /**Returns  the start vector J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double StartVectorJ
            (
            );
            /**Sets  the start vector J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartVectorJ
            (
                double jStartVec /** jstartvec */ 
            );
            /**Returns  the start vector K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double StartVectorK
            (
            );
            /**Sets  the start vector K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartVectorK
            (
                double kStartVec /** kstartvec */ 
            );
            /**Returns  the Arc start angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double StartAngle
            (
            );
            /**Sets  the Arc start angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartAngle
            (
                double startAngle /** startangle */ 
            );
            /**Returns  the Arc end angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double EndAngle
            (
            );
            /**Sets  the Arc end angle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEndAngle
            (
                double endAngle /** endangle */ 
            );
            /**Returns  the center point X coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double CenterPointX
            (
            );
            /**Sets  the center point X coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCenterPointX
            (
                double x /** x */ 
            );
            /**Returns  the center point Y coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double CenterPointY
            (
            );
            /**Sets  the center point Y coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCenterPointY
            (
                double y /** y */ 
            );
            /**Returns  the center point Z coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double CenterPointZ
            (
            );
            /**Sets  the center point Z coordinate 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCenterPointZ
            (
                double z /** z */ 
            );
            /**Returns  the normal vector I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalVectorI
            (
            );
            /**Sets  the normal vector I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNormalVectorI
            (
                double i /** i */ 
            );
            /**Returns  the normal vector J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalVectorJ
            (
            );
            /**Sets  the normal vector J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNormalVectorJ
            (
                double j /** j */ 
            );
            /**Returns  the normal vector K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalVectorK
            (
            );
            /**Sets  the normal vector K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNormalVectorK
            (
                double k /** k */ 
            );
            /**Returns  the Inspection Arc Feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the Inspection Arc Feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the Inspection Arc Feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Updates arc inspection feature characteristic parameters based on selected geometry 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateParams
            (
            );
            /** Flips the arc inspection feature normal vector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void FlipNormal
            (
            );
            /**Returns  the offset distance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * OffsetDistance
            (
            );
            /** Updates the arc inspection feature offset distance and associated values 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateOffset
            (
            );
            /** Reverses the offset direction 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void ReverseOffsetDirection
            (
            );
            /**Returns  the Cylinder Circle Fitting Mode Builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCylinderCircleFitModeBuilder * CylinderCircleFitModeBuilder
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