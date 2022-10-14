#ifndef NXOpen_FEATURES_SECTIONSURFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SECTIONSURFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SectionSurfaceBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SectionSurfaceBuilder.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_DepthSkewBuilder.hxx>
#include <NXOpen/GeometricUtilities_LawBuilder.hxx>
#include <NXOpen/GeometricUtilities_Rebuild.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class SectionSurfaceBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class Continuity;
    }
    namespace GeometricUtilities
    {
        class DepthSkewBuilder;
    }
    namespace GeometricUtilities
    {
        class LawBuilder;
    }
    namespace GeometricUtilities
    {
        class Rebuild;
    }
    class ScCollector;
    class Section;
    namespace Features
    {
        class _SectionSurfaceBuilderBuilder;
        class SectionSurfaceBuilderImpl;
        /**
            Represents a @link Features::SectionSurface Features::SectionSurface@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateSectionSurfaceBuilder  Features::FeatureCollection::CreateSectionSurfaceBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AngleLaw.EndValue.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        AngleLaw.Function </td> <td> 
         
        ft </td> </tr> 

        <tr><td> 
         
        AngleLaw.LawType </td> <td> 
         
        Constant </td> </tr> 

        <tr><td> 
         
        AngleLaw.Parameter </td> <td> 
         
        t </td> </tr> 

        <tr><td> 
         
        AngleLaw.StartValue.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        AngleLaw.Value.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        EndContinuity.ContinuityType </td> <td> 
         
        G1 </td> </tr> 

        <tr><td> 
         
        RadiusLaw.EndValue.Value </td> <td> 
         
        1.0 (millimeters part), 0.05 (inches part) </td> </tr> 

        <tr><td> 
         
        RadiusLaw.StartValue.Value </td> <td> 
         
        1.0 (millimeters part), 0.05 (inches part) </td> </tr> 

        <tr><td> 
         
        RadiusLaw.Value.Value </td> <td> 
         
        1.0 (millimeters part), 0.05 (inches part) </td> </tr> 

        <tr><td> 
         
        RhoLaw.EndValue.Value </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        RhoLaw.StartValue.Value </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        RhoLaw.Value.Value </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        SectionMethodCircularTangent </td> <td> 
         
        FilletArc </td> </tr> 

        <tr><td> 
         
        SectionMethodFilletBridge </td> <td> 
         
        Continuity </td> </tr> 

        <tr><td> 
         
        SectionMethodRho </td> <td> 
         
        Rho </td> </tr> 

        <tr><td> 
         
        StartContinuity.ContinuityType </td> <td> 
         
        G1 </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  SectionSurfaceBuilder : public Features::FeatureBuilder
        {
            /** This enum represents the current types of section surface methods*/
            public: enum Types
            {
                TypesEndsApexShoulder/** ends apex shoulder*/,
                TypesEndsSlopeShoulder/** ends slope shoulder */,
                TypesFilletShoulder/** fillet shoulder */,
                TypesEndsApexRho/** ends apex rho */,
                TypesEndsSlopeRho/** ends slope rho */,
                TypesFilletRho/** fillet rho */,
                TypesEndsApexHilite/** ends apex hilite */,
                TypesEndsSlopeHilite/** ends slope hilite */,
                TypesFilletHilite/** fillet hilite */,
                TypesFourPointSlope/** four point slope */,
                TypesFivePoint/** five point */,
                TypesThreePointArc/** three point arc */,
                TypesTwoPointRadius/** two point radius */,
                TypesEndSlopeArc/** point radius angle arc */,
                TypesPointRadiusAngleArc/** point radius angle arc */,
                TypesCircle/** circle */,
                TypesCircleTangent/** circle tangent */,
                TypesEndsSlopeCubic/** ends slope cubic */,
                TypesFilletBridge/** fillet bridge */,
                TypesLinearTangent/** linear tangent */
            };

            /** This enum represents the type of the region where depth and skew can be applied*/
            public: enum ControlRegionEnum
            {
                ControlRegionEnumEntire/** depth and skew applied to the entire section surface */,
                ControlRegionEnumStart/** depth and skew applied to the start section of the section surface */,
                ControlRegionEnumEnd/** depth and skew applied to the end section of the section surface */
            };

            /** This enum represents the type of flow direction for the start/end of the section surface*/
            public: enum FlowDirectionEnum
            {
                FlowDirectionEnumNotSpecified/** flow direction not specified */,
                FlowDirectionEnumPerpendicular/** flow direction perpendicular to the guide */,
                FlowDirectionEnumIsoLineU/** flow direction follows iso u of the start surface */,
                FlowDirectionEnumIsoLineV/** flow direction follows iso v of the start surface */
            };

            /** This enum represents the current types of section surface in u direction*/
            public: enum UDegreeEnum
            {
                UDegreeEnumConic/** conic in u */,
                UDegreeEnumCubic/** cubic in u */,
                UDegreeEnumQuintic/** quintic in u */
            };

            /** This enum represents the current types of section method for section methods with rho law*/
            public: enum SectionMethodRhoEnum
            {
                SectionMethodRhoEnumRho/** rho law method */,
                SectionMethodRhoEnumLeastTension/** least tension method */
            };

            /** This enum represents the current types of section method for circular tangent method*/
            public: enum SectionMethodCircularTangentEnum
            {
                SectionMethodCircularTangentEnumFilletArc/** fillet arc */,
                SectionMethodCircularTangentEnumCoverArc/** cover arc */
            };

            /** This enum represents the current types of section method for fillet bridge method*/
            public: enum SectionMethodFilletBridgeEnum
            {
                SectionMethodFilletBridgeEnumContinuity/** continuity options */,
                SectionMethodFilletBridgeEnumInheritShape/** inherit shape option */
            };

            private: SectionSurfaceBuilderImpl * m_sectionsurfacebuilder_impl;
            private: friend class  _SectionSurfaceBuilderBuilder;
            protected: SectionSurfaceBuilder();
            public: ~SectionSurfaceBuilder();
            /**Returns  the type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::Types Type
            (
            );
            /**Sets  the type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetType
            (
                NXOpen::Features::SectionSurfaceBuilder::Types type /** type */ 
            );
            /**Returns  the start guide 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * StartGuide
            (
            );
            /**Returns  the end guide
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * EndGuide
            (
            );
            /**Returns  the interior guide1.         
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesFourPointSlope Features::SectionSurfaceBuilder::TypesFourPointSlope@endlink , 
                        @link Features::SectionSurfaceBuilder::TypesFivePoint Features::SectionSurfaceBuilder::TypesFivePoint@endlink , and 
                        @link Features::SectionSurfaceBuilder::TypesThreePointArc Features::SectionSurfaceBuilder::TypesThreePointArc@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * InteriorGuide1
            (
            );
            /**Returns  the interior guide2 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesFourPointSlope Features::SectionSurfaceBuilder::TypesFourPointSlope@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFivePoint Features::SectionSurfaceBuilder::TypesFivePoint@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * InteriorGuide2
            (
            );
            /**Returns  the interior guide3 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesFourPointSlope Features::SectionSurfaceBuilder::TypesFourPointSlope@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFivePoint Features::SectionSurfaceBuilder::TypesFivePoint@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * InteriorGuide3
            (
            );
            /**Returns  the orientation guide.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesCircle Features::SectionSurfaceBuilder::TypesCircle@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * OrientationGuide
            (
            );
            /**Returns  the apex curve. 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesEndsApexShoulder Features::SectionSurfaceBuilder::TypesEndsApexShoulder@endlink , 
                        @link Features::SectionSurfaceBuilder::TypesEndsApexRho Features::SectionSurfaceBuilder::TypesEndsApexRho@endlink , and 
                        @link Features::SectionSurfaceBuilder::TypesEndsApexHilite Features::SectionSurfaceBuilder::TypesEndsApexHilite@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * ApexCurve
            (
            );
            /**Returns  the start slope.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeShoulder Features::SectionSurfaceBuilder::TypesEndsSlopeShoulder@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeRho Features::SectionSurfaceBuilder::TypesEndsSlopeRho@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeHilite Features::SectionSurfaceBuilder::TypesEndsSlopeHilite@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeCubic Features::SectionSurfaceBuilder::TypesEndsSlopeCubic@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFourPointSlope Features::SectionSurfaceBuilder::TypesFourPointSlope@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * StartSlope
            (
            );
            /**Returns  the end slope.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeShoulder Features::SectionSurfaceBuilder::TypesEndsSlopeShoulder@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeRho Features::SectionSurfaceBuilder::TypesEndsSlopeRho@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeHilite Features::SectionSurfaceBuilder::TypesEndsSlopeHilite@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeCubic Features::SectionSurfaceBuilder::TypesEndsSlopeCubic@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFourPointSlope Features::SectionSurfaceBuilder::TypesFourPointSlope@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * EndSlope
            (
            );
            /**Returns  the start surface.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesFilletShoulder Features::SectionSurfaceBuilder::TypesFilletShoulder@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesFilletRho Features::SectionSurfaceBuilder::TypesFilletRho@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesFilletHilite Features::SectionSurfaceBuilder::TypesFilletHilite@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletBridge Features::SectionSurfaceBuilder::TypesFilletBridge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * StartSurface
            (
            );
            /**Returns  the reverse start direction.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletBridge Features::SectionSurfaceBuilder::TypesFilletBridge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseStartDirection
            (
            );
            /**Sets  the reverse start direction.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletBridge Features::SectionSurfaceBuilder::TypesFilletBridge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetReverseStartDirection
            (
                bool reverseStartDirection /** reversestartdirection */ 
            );
            /**Returns  the end surface 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesFilletShoulder Features::SectionSurfaceBuilder::TypesFilletShoulder@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesFilletRho Features::SectionSurfaceBuilder::TypesFilletRho@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesFilletHilite Features::SectionSurfaceBuilder::TypesFilletHilite@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletBridge Features::SectionSurfaceBuilder::TypesFilletBridge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * EndSurface
            (
            );
            /**Returns  the reverse end surface 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletBridge Features::SectionSurfaceBuilder::TypesFilletBridge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseEndSurface
            (
            );
            /**Sets  the reverse end surface 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc Features::SectionSurfaceBuilder::TypesPointRadiusAngleArc@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletBridge Features::SectionSurfaceBuilder::TypesFilletBridge@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetReverseEndSurface
            (
                bool reverseEndSurface /** reverseendsurface */ 
            );
            /**Returns  the section method for rho law
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::SectionMethodRhoEnum SectionMethodRho
            (
            );
            /**Sets  the section method for rho law
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetSectionMethodRho
            (
                NXOpen::Features::SectionSurfaceBuilder::SectionMethodRhoEnum sectionMethodRho /** sectionmethodrho */ 
            );
            /**Returns  the section method for circular tangent
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::SectionMethodCircularTangentEnum SectionMethodCircularTangent
            (
            );
            /**Sets  the section method for circular tangent
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetSectionMethodCircularTangent
            (
                NXOpen::Features::SectionSurfaceBuilder::SectionMethodCircularTangentEnum sectionMethodCircularTangent /** sectionmethodcirculartangent */ 
            );
            /**Returns  the section method for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::SectionMethodFilletBridgeEnum SectionMethodFilletBridge
            (
            );
            /**Sets  the section method for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetSectionMethodFilletBridge
            (
                NXOpen::Features::SectionSurfaceBuilder::SectionMethodFilletBridgeEnum sectionMethodFilletBridge /** sectionmethodfilletbridge */ 
            );
            /**Returns  the start continuity for fillet bridge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * StartContinuity
            (
            );
            /**Returns  the end continuity for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * EndContinuity
            (
            );
            /**Returns  the start shape curve for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * StartShapeCurve
            (
            );
            /**Returns  the end shape curve for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * EndShapeCurve
            (
            );
            /**Returns  the control region for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::ControlRegionEnum ControlRegion
            (
            );
            /**Sets  the control region for fillet bridge
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetControlRegion
            (
                NXOpen::Features::SectionSurfaceBuilder::ControlRegionEnum controlRegion /** controlregion */ 
            );
            /**Returns  the start flow direction for fillet bridge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::FlowDirectionEnum StartFlowDirection
            (
            );
            /**Sets  the start flow direction for fillet bridge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetStartFlowDirection
            (
                NXOpen::Features::SectionSurfaceBuilder::FlowDirectionEnum startFlowDirection /** startflowdirection */ 
            );
            /**Returns  the end flow direction for fillet bridge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::FlowDirectionEnum EndFlowDirection
            (
            );
            /**Sets  the end flow direction for fillet bridge 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetEndFlowDirection
            (
                NXOpen::Features::SectionSurfaceBuilder::FlowDirectionEnum endFlowDirection /** endflowdirection */ 
            );
            /**Returns  the shoulder.
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesEndsApexShoulder Features::SectionSurfaceBuilder::TypesEndsApexShoulder@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeShoulder Features::SectionSurfaceBuilder::TypesEndsSlopeShoulder@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletShoulder Features::SectionSurfaceBuilder::TypesFilletShoulder@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Shoulder
            (
            );
            /**Returns  the start highlight section. 
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesEndsApexHilite Features::SectionSurfaceBuilder::TypesEndsApexHilite@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeHilite Features::SectionSurfaceBuilder::TypesEndsSlopeHilite@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletHilite Features::SectionSurfaceBuilder::TypesFilletHilite@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * StartHighlightSection
            (
            );
            /**Returns  the end highlight section .
                        Only applies to the follow section surface types:
                        @link Features::SectionSurfaceBuilder::TypesEndsApexHilite Features::SectionSurfaceBuilder::TypesEndsApexHilite@endlink ,
                        @link Features::SectionSurfaceBuilder::TypesEndsSlopeHilite Features::SectionSurfaceBuilder::TypesEndsSlopeHilite@endlink  and
                        @link Features::SectionSurfaceBuilder::TypesFilletHilite Features::SectionSurfaceBuilder::TypesFilletHilite@endlink  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * EndHighlightSection
            (
            );
            /**Returns  the rho Law 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * RhoLaw
            (
            );
            /**Returns  the radius Law 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * RadiusLaw
            (
            );
            /**Returns  the angle Law 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * AngleLaw
            (
            );
            /**Returns  the spine curve 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * SpineCurve
            (
            );
            /**Returns  the u degree 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionSurfaceBuilder::UDegreeEnum UDegree
            (
            );
            /**Sets  the u degree 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetUDegree
            (
                NXOpen::Features::SectionSurfaceBuilder::UDegreeEnum uDegree /** udegree */ 
            );
            /**Returns  the v degree 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Rebuild * VDegree
            (
            );
            /**Returns  the position tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: double PositionTolerance
            (
            );
            /**Sets  the position tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetPositionTolerance
            (
                double positionTolerance /** positiontolerance */ 
            );
            /**Returns  the tangent tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: double TangentTolerance
            (
            );
            /**Sets  the tangent tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetTangentTolerance
            (
                double tangentTolerance /** tangenttolerance */ 
            );
            /**Returns  the curvature tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: double CurvatureTolerance
            (
            );
            /**Sets  the curvature tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetCurvatureTolerance
            (
                double curvatureTolerance /** curvaturetolerance */ 
            );
            /**Returns  the alternate method.
                        This api only applies to the follow section surface methods,
                        circle_tangent and linear-tangent 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int AlternateMethod
            (
            );
            /**Sets  the alternate method.
                        This api only applies to the follow section surface methods,
                        circle_tangent and linear-tangent 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_2 ("advanced freeform modeling") */
            public: void SetAlternateMethod
            (
                int alternateMethod /** alternatemethod */ 
            );
            /**Returns  the entire region depth and skew 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DepthSkewBuilder * EntireRegionDepthSkew
            (
            );
            /**Returns  the start depth and skew 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DepthSkewBuilder * StartDepthSkew
            (
            );
            /**Returns  the end depth and skew 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DepthSkewBuilder * EndDepthSkew
            (
            );
            /**Returns  whether an apex curve should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateApexCurve
            (
            );
            /**Sets  whether an apex curve should be created 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling"), solid_modeling ("SOLIDS MODELING") */
            public: void SetCreateApexCurve
            (
                bool createApexCurve /** createapexcurve */ 
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