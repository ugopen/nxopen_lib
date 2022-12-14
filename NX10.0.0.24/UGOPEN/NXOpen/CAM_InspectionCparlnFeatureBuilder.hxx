#ifndef NXOpen_CAM_INSPECTIONCPARLNFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONCPARLNFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionCparlnFeatureBuilder.ja
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
#include <NXOpen/CAM_InspectionCparlnFeatureBuilder.hxx>
#include <NXOpen/CAM_InspectionOperationEnums.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
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
        class InspectionCparlnFeatureBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class Direction;
    class SelectFace;
    class SelectNXObjectList;
    namespace CAM
    {
        class _InspectionCparlnFeatureBuilderBuilder;
        class InspectionCparlnFeatureBuilderImpl;
        /** Represents a CMM Inspection Cparln Feature Builder.
                A Cparln is a bounded slot defined by closed ended parallel lines.  <br> To create a new instance of this class, use @link NXOpen::CAM::InspectionOperationCollection::CreateInspectionCparlnFeatureBuilder  NXOpen::CAM::InspectionOperationCollection::CreateInspectionCparlnFeatureBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionCparlnFeatureBuilder : public NXOpen::CAM::OperationBuilder
        {
            /** The shape of the end of the bounded slot/tab (round or square) */
            public: enum EndTypes
            {
                EndTypesRound/** Bounded slot/tab has round end */,
                EndTypesSquare/** Bounded slot/tab has square end */
            };

            private: InspectionCparlnFeatureBuilderImpl * m_inspectioncparlnfeaturebuilder_impl;
            private: friend class  _InspectionCparlnFeatureBuilderBuilder;
            protected: InspectionCparlnFeatureBuilder();
            public: ~InspectionCparlnFeatureBuilder();
            /**Returns  the selected geometry, consisting of two parallel lines 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectedGeometry
            (
            );
            /**Returns  the selector for projection faces 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * SelectProjectionFaces
            (
            );
            /**Returns  the reverse direction button used to reverse the normal direction vector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction button used to reverse the normal direction vector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the length direction vector selector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * LengthDirVector
            (
            );
            /**Sets  the length direction vector selector 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLengthDirVector
            (
                NXOpen::Direction * lengthDirVector /** lengthdirvector */ 
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
            /**Returns  the inspection feature inner outer type (slot/tab) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CamInspectionOperationInneroutertypes InnerOuterType
            (
            );
            /**Sets  the inspection feature inner outer type (slot/tab) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetInnerOuterType
            (
                NXOpen::CAM::CamInspectionOperationInneroutertypes innerOuterType /** inneroutertype */ 
            );
            /**Returns  the length of the bounded slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double Length
            (
            );
            /**Sets  the length of the bounded slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLength
            (
                double length /** length */ 
            );
            /**Returns  the width of the bounded slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double Width
            (
            );
            /**Sets  the width of the bounded slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetWidth
            (
                double width /** width */ 
            );
            /**Returns  the end type of the bounded slot or tab (round or square) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionCparlnFeatureBuilder::EndTypes EndType
            (
            );
            /**Sets  the end type of the bounded slot or tab (round or square) 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEndType
            (
                NXOpen::CAM::InspectionCparlnFeatureBuilder::EndTypes endType /** endtype */ 
            );
            /**Returns  the location point X coordinate at the center of the face of the slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double LocationPointX
            (
            );
            /**Sets  the location point X coordinate at the center of the face of the slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLocationPointX
            (
                double locationPointX /** locationpointx */ 
            );
            /**Returns  the location point Y coordinate at the center of the face of the slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double LocationPointY
            (
            );
            /**Sets  the location point Y coordinate at the center of the face of the slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLocationPointY
            (
                double locationPointY /** locationpointy */ 
            );
            /**Returns  the location point Z coordinate at the center of the face of the slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double LocationPointZ
            (
            );
            /**Sets  the location point Z coordinate at the center of the face of the slot or tab 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLocationPointZ
            (
                double locationPointZ /** locationpointz */ 
            );
            /**Returns  the slot or tab normal direction I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalDirectionI
            (
            );
            /**Sets  the slot or tab normal direction I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNormalDirectionI
            (
                double normalDirectionI /** normaldirectioni */ 
            );
            /**Returns  the slot or tab normal direction J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalDirectionJ
            (
            );
            /**Sets  the slot or tab normal direction J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNormalDirectionJ
            (
                double normalDirectionJ /** normaldirectionj */ 
            );
            /**Returns  the slot or tab normal direction K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalDirectionK
            (
            );
            /**Sets  the slot or tab normal direction K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNormalDirectionK
            (
                double normalDirectionK /** normaldirectionk */ 
            );
            /**Returns  the slot or tab length direction I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double LengthDirectionI
            (
            );
            /**Sets  the slot or tab length direction I component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLengthDirectionI
            (
                double lengthDirectionI /** lengthdirectioni */ 
            );
            /**Returns  the slot or tab length direction J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double LengthDirectionJ
            (
            );
            /**Sets  the slot or tab length direction J component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLengthDirectionJ
            (
                double lengthDirectionJ /** lengthdirectionj */ 
            );
            /**Returns  the slot or tab length direction K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double LengthDirectionK
            (
            );
            /**Sets  the slot or tab length direction K component 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLengthDirectionK
            (
                double lengthDirectionK /** lengthdirectionk */ 
            );
            /**Returns  the slot or tab feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the slot or tab feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the slot or tab feature name 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Updates cparln inspection feature characteristic parameters based on selected geometry 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateParams
            (
            );
            /** Flips the cparln inspection feature normal vector 
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
            /** Updates the cparln inspection feature offset distance and associated values 
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
            /** Updates cparln inspection feature characteristic parameters based on selected end type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateEndType
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
