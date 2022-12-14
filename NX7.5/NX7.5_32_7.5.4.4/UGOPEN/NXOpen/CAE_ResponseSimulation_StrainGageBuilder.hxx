#ifndef NXOpen_CAE_RESPONSESIMULATION_STRAINGAGEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_STRAINGAGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_StrainGageBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_BaseBuilder.hxx>
#include <NXOpen/CAE_ResponseSimulation.hxx>
#include <NXOpen/CAE_ResponseSimulation_StrainGageBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrainGageBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class BaseBuilder;
        }
    }
    namespace CAE
    {
        class SelectFEElemFaceList;
    }
    namespace CAE
    {
        class SelectFEElementList;
    }
    namespace CAE
    {
        class SelectFENodeList;
    }
    class Expression;
    class SmartObject;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _StrainGageBuilderBuilder;
            class StrainGageBuilderImpl;
            /**
                Represents a StrainGageBuilder
                 <br> To create a new instance of this class, use @link CAE::ResponseSimulation::StrainGageCollection::CreateStrainGageBuilder CAE::ResponseSimulation::StrainGageCollection::CreateStrainGageBuilder@endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            GageType </td> <td> 
             
            UniAxial </td> </tr> 

            <tr><td> 
             
            Placement </td> <td> 
             
            Node </td> </tr> 

            <tr><td> 
             
            Plane </td> <td> 
             
            FacePlane </td> </tr> 

            <tr><td> 
             
            ResultType </td> <td> 
             
            Strain </td> </tr> 

            <tr><td> 
             
            RotationAngle.Value </td> <td> 
             
            0.0 (millimeters part), 0.0 (inches part) </td> </tr> 

            <tr><td> 
             
            ShellElementFace </td> <td> 
             
            Top </td> </tr> 

            </table>  
            */
            class NXOPENCPPEXPORT  StrainGageBuilder : public CAE::ResponseSimulation::BaseBuilder
            {
                private: StrainGageBuilderImpl * m_straingagebuilder_impl;
                private: friend class  _StrainGageBuilderBuilder;
                protected: StrainGageBuilder();
                public: ~StrainGageBuilder();
                /**Returns  the type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGageType GageType
                (
                );
                /**Sets  the type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetGageType
                (
                    NXOpen::CAE::ResponseSimulation::StrainGageType gageType /** gage type */ 
                );
                /**Returns  the result type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGageResult ResultType
                (
                );
                /**Sets  the result type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResultType
                (
                    NXOpen::CAE::ResponseSimulation::StrainGageResult resultType /** result type */ 
                );
                /**Returns  the placement type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGagePlacementType Placement
                (
                );
                /**Sets  the placement type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetPlacement
                (
                    NXOpen::CAE::ResponseSimulation::StrainGagePlacementType gagePlacement /** gage placement */ 
                );
                /**Returns  the shell element face location type of strain gage  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGageShellElementFaceType ShellElementFace
                (
                );
                /**Sets  the shell element face location type of strain gage  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetShellElementFace
                (
                    NXOpen::CAE::ResponseSimulation::StrainGageShellElementFaceType shellElementFace /** shell element face */ 
                );
                /**Returns  the destination nodes, Only available when the strain gage's placement type is
                            @link CAE::ResponseSimulation::StrainGagePlacementTypeNode CAE::ResponseSimulation::StrainGagePlacementTypeNode@endlink    <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::SelectFENodeList * SelectedNode
                (
                );
                /**Returns   Use @link CAE::ResponseSimulation::StrainGageBuilder::SelectedElementFaces CAE::ResponseSimulation::StrainGageBuilder::SelectedElementFaces@endlink  instead.  
                 @deprecated Deprecated in NX7.5.2 <br> 
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public:  NX_DEPRECATED("Deprecated in NX7.5.2") NXOpen::CAE::SelectFEElementList * SelectedElement
                (
                );
                /**Returns   the selected element face.
                            Only available when the strain gage's placement type is
                            @link CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter@endlink    <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::SelectFEElemFaceList * SelectedElementFaces
                (
                );
                /** Use @link CAE::ResponseSimulation::StrainGageBuilder::SelectedElementFaces CAE::ResponseSimulation::StrainGageBuilder::SelectedElementFaces@endlink  instead.  @return  
                 @deprecated Deprecated in NX7.5.2 <br> 
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public:  NX_DEPRECATED("Deprecated in NX7.5.2") std::vector<int> GetSelectedElementFaceId
                (
                );
                /** Sets the selected element face, must set the element to define the element face.
                            Only available when the strain gage's placement type is
                            @link CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter CAE::ResponseSimulation::StrainGagePlacementTypeElementFaceCenter@endlink 
                 @deprecated Deprecated in NX7.5.2 <br> 
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public:  NX_DEPRECATED("Deprecated in NX7.5.2") void SetSelectedElementFaceId
                (
                    const std::vector<int> & destinationElementId /** destination element id */ 
                );
                /**Returns  the orientation plane type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrainGageOrientationPlane Plane
                (
                );
                /**Sets  the orientation plane type of strain gage <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetPlane
                (
                    NXOpen::CAE::ResponseSimulation::StrainGageOrientationPlane plane /** plane */ 
                );
                /**Returns  the orientation direction, Only available when the strain gage's orientation plane type is
                            @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::SmartObject * Csys
                (
                );
                /**Sets  the orientation direction, Only available when the strain gage's orientation plane type is
                            @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetCsys
                (
                    NXOpen::SmartObject * orientationCoordSystem /** orientation coord system */ 
                );
                /**Returns  the rotation angle, Only available when the strain gage's orientation plane type is
                            @link CAE::ResponseSimulation::StrainGageOrientationPlaneCsys CAE::ResponseSimulation::StrainGageOrientationPlaneCsys@endlink   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::Expression * RotationAngle
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
