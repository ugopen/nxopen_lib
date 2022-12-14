#ifndef NXOpen_CAM_INSPECTIONCYLINDERFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONCYLINDERFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionCylinderFeatureBuilder.ja
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
#include <NXOpen/CAM_InspectionCylinderFeatureBuilder.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionCylinderFeatureBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class Direction;
    class SelectNXObject;
    namespace CAM
    {
        class _InspectionCylinderFeatureBuilderBuilder;
        /** Represents a CMM Inspection Cylinder Feature builder  <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionCylinderFeatureBuilder CAM::InspectionOperationCollection::CreateInspectionCylinderFeatureBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ExtentType </td> <td> 
         
        Bounded </td> </tr> 

        <tr><td> 
         
        InnerOuterType </td> <td> 
         
        Inner </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT InspectionCylinderFeatureBuilder : public CAM::OperationBuilder
        {
            /** Coordinate system that the inspection feature data is relative to */
            public: enum CsysReferenceTypeEnum
            {
                CsysReferenceTypeEnumRelativetoPCS/** Relative to Part Coordinate System */,
                CsysReferenceTypeEnumAbsolute/** Relative to Absolute Coordinate System */
            };

            /** Directionality of feature surface */
            public: enum InnerOuterTypeEnum
            {
                InnerOuterTypeEnumInner/** Feature with surface normal pointing inward (hole)*/,
                InnerOuterTypeEnumOuter/** Feature with surface normal pointing outward (pin)*/
            };

            /** Specifies whether the feature extent is bounded or unbounded */
            public: enum ExtentTypeEnum
            {
                ExtentTypeEnumBounded/** Feature extent has bounds */,
                ExtentTypeEnumUnbounded/** Feature extent is infinite */
            };

            private: friend class  _InspectionCylinderFeatureBuilderBuilder;
            protected: InspectionCylinderFeatureBuilder();
            /**Returns  the selected cylinder  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectedCylinder
            (
            );
            /**Returns  the cylinders axis vector  <br> License requirements : None */
            public: NXOpen::Direction * AxisVector
            (
            );
            /**Sets  the cylinders axis vector  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisVector
            (
                NXOpen::Direction * axisVector /** axisvector */ 
            );
            /**Returns  the coordinate system reference type  <br> License requirements : None */
            public: NXOpen::CAM::InspectionCylinderFeatureBuilder::CsysReferenceTypeEnum CsysReferenceType
            (
            );
            /**Sets  the coordinate system reference type  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetCsysReferenceType
            (
                NXOpen::CAM::InspectionCylinderFeatureBuilder::CsysReferenceTypeEnum csysReferenceType /** csysreferencetype */ 
            );
            /**Returns  the inspection feature inner/outer type (hole/pin)  <br> License requirements : None */
            public: NXOpen::CAM::InspectionCylinderFeatureBuilder::InnerOuterTypeEnum InnerOuterType
            (
            );
            /**Sets  the inspection feature inner/outer type (hole/pin)  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetInnerOuterType
            (
                NXOpen::CAM::InspectionCylinderFeatureBuilder::InnerOuterTypeEnum innerOuterType /** inneroutertype */ 
            );
            /**Returns  the cylinder radius  <br> License requirements : None */
            public: double Radius
            (
            );
            /**Sets  the cylinder radius  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetRadius
            (
                double radius /** radius */ 
            );
            /**Returns  the extent type  <br> License requirements : None */
            public: NXOpen::CAM::InspectionCylinderFeatureBuilder::ExtentTypeEnum ExtentType
            (
            );
            /**Sets  the extent type  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetExtentType
            (
                NXOpen::CAM::InspectionCylinderFeatureBuilder::ExtentTypeEnum extentType /** extenttype */ 
            );
            /**Returns  the length of the cylinder  <br> License requirements : None */
            public: double Length
            (
            );
            /**Sets  the length of the cylinder  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetLength
            (
                double length /** length */ 
            );
            /**Returns  the base point X coordinate  <br> License requirements : None */
            public: double BasePointX
            (
            );
            /**Sets  the base point X coordinate  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetBasePointX
            (
                double basePointX /** basepointx */ 
            );
            /**Returns  the base point Y coordinate  <br> License requirements : None */
            public: double BasePointY
            (
            );
            /**Sets  the base point Y coordinate  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetBasePointY
            (
                double basePointY /** basepointy */ 
            );
            /**Returns  the base point Z coordinate  <br> License requirements : None */
            public: double BasePointZ
            (
            );
            /**Sets  the base point Z coordinate  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetBasePointZ
            (
                double basePointZ /** basepointz */ 
            );
            /**Returns  the axis direction vector I component  <br> License requirements : None */
            public: double AxisDirectionI
            (
            );
            /**Sets  the axis direction vector I component  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisDirectionI
            (
                double axisDirectionI /** axisdirectioni */ 
            );
            /**Returns  the axis direction vector J component  <br> License requirements : None */
            public: double AxisDirectionJ
            (
            );
            /**Sets  the axis direction vector J component  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisDirectionJ
            (
                double axisDirectionJ /** axisdirectionj */ 
            );
            /**Returns  the axis direction vector K component  <br> License requirements : None */
            public: double AxisDirectionK
            (
            );
            /**Sets  the axis direction vector K component  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void SetAxisDirectionK
            (
                double axisDirectionK /** axisdirectionk */ 
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
            /** Updates cylinder inspection feature characteristic parameters based on selected geometry  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateParams
            (
            );
            /** Flips the cylinder inspection feature axis direction vector  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void FlipAxisDirection
            (
            );
            /** Updates cylinder inspection feature axis direction vector based on selected vector  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateAxisDirection
            (
                const NXOpen::Vector3d & vector /** vector */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
