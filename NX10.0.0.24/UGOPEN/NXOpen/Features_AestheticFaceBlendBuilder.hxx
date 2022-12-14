#ifndef NXOpen_FEATURES_AESTHETICFACEBLENDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_AESTHETICFACEBLENDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AestheticFaceBlendBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_AestheticFaceBlendBuilder.hxx>
#include <NXOpen/GeometricUtilities_BlendLimitsData.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_DegreesAndSegmentsOrPatchesBuilder.hxx>
#include <NXOpen/GeometricUtilities_LawBuilder.hxx>
#include <NXOpen/GeometricUtilities_TangentMagnitudeBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class AestheticFaceBlendBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BlendLimitsData;
    }
    namespace GeometricUtilities
    {
        class Continuity;
    }
    namespace GeometricUtilities
    {
        class DegreesAndSegmentsOrPatchesBuilder;
    }
    namespace GeometricUtilities
    {
        class LawBuilder;
    }
    namespace GeometricUtilities
    {
        class TangentMagnitudeBuilder;
    }
    class Point;
    class ScCollector;
    class Section;
    namespace Features
    {
        class _AestheticFaceBlendBuilderBuilder;
        class AestheticFaceBlendBuilderImpl;
        /** This class will provide ability to create aesthetically pleasing blend surfaces on sheet and solid bodies. <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateAestheticFaceBlendBuilder  NXOpen::Features::FeatureCollection::CreateAestheticFaceBlendBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AlignmentOption </td> <td> 
         
        RollingBall </td> </tr> 

        <tr><td> 
         
        BaseRadiusLaw.Function </td> <td> 
         
        ft </td> </tr> 

        <tr><td> 
         
        BaseRadiusLaw.LawType </td> <td> 
         
        MultiTransition </td> </tr> 

        <tr><td> 
         
        BaseRadiusLaw.Parameter </td> <td> 
         
        t </td> </tr> 

        <tr><td> 
         
        BlendFacesOption </td> <td> 
         
        TrimtoAllInputFaces </td> </tr> 

        <tr><td> 
         
        BlendOption </td> <td> 
         
        Radius </td> </tr> 

        <tr><td> 
         
        CenterChordLaw.LawType </td> <td> 
         
        Constant </td> </tr> 

        <tr><td> 
         
        CenterOption </td> <td> 
         
        CenterRadius </td> </tr> 

        <tr><td> 
         
        CenterRadiusLaw.LawType </td> <td> 
         
        MultiTransition </td> </tr> 

        <tr><td> 
         
        Chain1Continuity.ContinuityType </td> <td> 
         
        G1 </td> </tr> 

        <tr><td> 
         
        Chain2Continuity.ContinuityType </td> <td> 
         
        G1 </td> </tr> 

        <tr><td> 
         
        ChordLength.Value (deprecated) </td> <td> 
         
        10 (millimeters part), 0.4 (inches part) </td> </tr> 

        <tr><td> 
         
        ChordLengthLaw.LawType </td> <td> 
         
        Constant </td> </tr> 

        <tr><td> 
         
        Continuity.ContinuityType (deprecated) </td> <td> 
         
        G1 </td> </tr> 

        <tr><td> 
         
        CurvatureTolerance </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        Degrees.Degree </td> <td> 
         
        3 </td> </tr> 

        <tr><td> 
         
        Degrees.SegmentsOrPatches </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        Degrees.UDegree </td> <td> 
         
        5 </td> </tr> 

        <tr><td> 
         
        Degrees.UPatches </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        Degrees.VDegree </td> <td> 
         
        5 </td> </tr> 

        <tr><td> 
         
        Degrees.VPatches </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        IsAccelerated </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        IsBezier </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsCenterlineCurve </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsMinimumRadius </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsMinimumSubtendedAngle </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsRationalOutput </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsSameTransition </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        IsSewAllFaces </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsTrimInputFaces </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsWashout1 </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsWashout2 </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MinimumEdgeLength </td> <td> 
         
        10 </td> </tr> 

        <tr><td> 
         
        MinimumRadius.Value </td> <td> 
         
        2.5 (millimeters part), 0.098 (inches part) </td> </tr> 

        <tr><td> 
         
        MinimumSubtendedAngle </td> <td> 
         
        5.0 </td> </tr> 

        <tr><td> 
         
        RhoOption </td> <td> 
         
        Relative </td> </tr> 

        <tr><td> 
         
        RhoValue </td> <td> 
         
        0.6 </td> </tr> 

        <tr><td> 
         
        SectionScaling1.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        SectionScaling2.Value </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        SegmentationOption </td> <td> 
         
        AtAllTransitions </td> </tr> 

        <tr><td> 
         
        ShapeOption (deprecated) </td> <td> 
         
        Accelerated </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  AestheticFaceBlendBuilder : public NXOpen::Features::FeatureBuilder
        {
            /**Alignment method provides the ability to align the cross sections of the blend in the user specified direction*/
            public: enum AlignmentType
            {
                AlignmentTypeRollingBall/**Rolling Ball option will align the sections at contact point.*/,
                AlignmentTypeSpineCurve/**Spine Curve option will align the sections based on a string of curves.*/,
                AlignmentTypeVector/**Vector option will align the sections based on the vector */
            };

            /**Tangent method will create tangent lines based on the method employed.*/
            public: enum BlendType
            {
                BlendTypeRadius/** Radius of the rolling ball is used to create the tangent lines.*/,
                BlendTypeChordLength/** Chord Length will keep the appearance of a constant width blend through areas which have changing angles between the input walls.*/
            };

            /** Shape methods will define the high level shape of the blend cross section. */
            public: enum ShapeType
            {
                ShapeTypeAccelerated/** Accelerated option will generate more shapes depending on the size of the center radius and continuity specified. */,
                ShapeTypeCircular/** Circular option will always generate a constant radius arc shape. */
            };

            /** Center methods will define peak of the blend */
            public: enum CenterType
            {
                CenterTypeCenterRadius/** Center radius option. */,
                CenterTypeRho/** Rho is the ratio of the center radius and the base radius. */
            };

            /** Trimming options */
            public: enum BlendFacesType
            {
                BlendFacesTypeTrimtoAllInputFaces/** Trims all input faces. */,
                BlendFacesTypeTrimtoShortInputFaces/** Trims short input faces. */,
                BlendFacesTypeTrimtoLongInputFaces/** Trims long input faces. */,
                BlendFacesTypeDoNotTrimBlendFaces/** This option controls to trim blend faces or not */
            };

            /** Start object overriding trim options */
            public: enum StartTrimObjectType
            {
                StartTrimObjectTypeNone/** Does not override start trim object. */,
                StartTrimObjectTypePlane/** Overrides start trim object with plane. */,
                StartTrimObjectTypeFace/** Override start trim object with face. */
            };

            /** End object overriding trim options */
            public: enum EndTrimObjectType
            {
                EndTrimObjectTypeNone/** Does not override end trim object. */,
                EndTrimObjectTypePlane/** Overrides end trim object with plane. */,
                EndTrimObjectTypeFace/** Override end trim object with face. */
            };

            /** Segmentations options */
            public: enum SegmentationType
            {
                SegmentationTypeAtAllTransitions/** Segmentation at all transitions */,
                SegmentationTypeAtTransitionsonFaceChain1/** Segmentation at Face Chain1 transition */,
                SegmentationTypeAtTransitionsonFaceChain2/** Segementation at Face Chain2 transition */,
                SegmentationTypeAtAllTransitionsandMergeSmallBlendFaces/** Secgmentation at all transitions and merge small blend faces */
            };

            /** Rho options */
            public: enum RhoType
            {
                RhoTypeRelative/** Relative Rho: it's the ratio of BaseRadius/(BaseRadius + CenterRadius) */,
                RhoTypeAbsolute/** Absolute Rho: does not take into account the subtended angle */
            };

            private: AestheticFaceBlendBuilderImpl * m_aestheticfaceblendbuilder_impl;
            private: friend class  _AestheticFaceBlendBuilderBuilder;
            protected: AestheticFaceBlendBuilder();
            public: ~AestheticFaceBlendBuilder();
            /**Returns  the face chain1 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FaceChain1
            (
            );
            /**Returns  the reverse normal1 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseNormal1
            (
            );
            /**Sets  the reverse normal1 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetReverseNormal1
            (
                bool reverseNormal1 /** reversenormal1 */ 
            );
            /**Returns  the face chain2 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FaceChain2
            (
            );
            /**Returns  the reverse normal2 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseNormal2
            (
            );
            /**Sets  the reverse normal2 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetReverseNormal2
            (
                bool reverseNormal2 /** reversenormal2 */ 
            );
            /**Returns  the alignment option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::AlignmentType AlignmentOption
            (
            );
            /**Sets  the alignment option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetAlignmentOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::AlignmentType alignmentOption /** alignmentoption */ 
            );
            /**Returns  the parameter spine 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * ParameterSpine
            (
            );
            /**Returns  the section alignment vector 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * SectionAlignmentVector
            (
            );
            /**Sets  the section alignment vector 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSectionAlignmentVector
            (
                NXOpen::Direction * sectionAlignmentVector /** sectionalignmentvector */ 
            );
            /**Returns  the method option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::BlendType BlendOption
            (
            );
            /**Sets  the method option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetBlendOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::BlendType blendOption /** blendoption */ 
            );
            /**Returns  the base radius law variable 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * BaseRadiusLaw
            (
            );
            /**Returns  the chord length law variable 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * ChordLengthLaw
            (
            );
            /**Returns  the chord length 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link Features::AestheticFaceBlendBuilder::ChordLengthLaw Features::AestheticFaceBlendBuilder::ChordLengthLaw@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use Features::AestheticFaceBlendBuilder::ChordLengthLaw instead.") NXOpen::Expression * ChordLength
            (
            );
            /**Returns  the shape option 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link Features::AestheticFaceBlendBuilder::IsAccelerated Features::AestheticFaceBlendBuilder::IsAccelerated@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use Features::AestheticFaceBlendBuilder::IsAccelerated instead.") NXOpen::Features::AestheticFaceBlendBuilder::ShapeType ShapeOption
            (
            );
            /**Sets  the shape option 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link Features::AestheticFaceBlendBuilder::SetAccelerated Features::AestheticFaceBlendBuilder::SetAccelerated@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use Features::AestheticFaceBlendBuilder::SetAccelerated instead.") void SetShapeOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::ShapeType shapeOption /** shapeoption */ 
            );
            /**Returns  the method to control the shape 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsAccelerated
            (
            );
            /**Sets  the method to control the shape 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetAccelerated
            (
                bool isAccelerated /** isaccelerated */ 
            );
            /**Returns  the blend cross section is using the same transition as blend tangent or not 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsSameTransition
            (
            );
            /**Sets  the blend cross section is using the same transition as blend tangent or not 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSameTransition
            (
                bool isSameTransition /** issametransition */ 
            );
            /**Returns  the center option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::CenterType CenterOption
            (
            );
            /**Sets  the center option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetCenterOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::CenterType centerOption /** centeroption */ 
            );
            /**Returns  the rho option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::RhoType RhoOption
            (
            );
            /**Sets  the rho option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRhoOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::RhoType rhoType /** rhotype */ 
            );
            /**Returns  the rho value 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RhoValue
            (
            );
            /**Sets  the rho value 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRhoValue
            (
                double rhoValue /** rhovalue */ 
            );
            /**Returns  the center radius law 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * CenterRadiusLaw
            (
            );
            /**Returns  the center chord law 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * CenterChordLaw
            (
            );
            /**Returns  the tangent magnitude 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::TangentMagnitudeBuilder * TangentMagnitude
            (
            );
            /**Returns  the continuity 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link Features::AestheticFaceBlendBuilder::Chain1Continuity Features::AestheticFaceBlendBuilder::Chain1Continuity@endlink  and @link Features::AestheticFaceBlendBuilder::Chain2Continuity Features::AestheticFaceBlendBuilder::Chain2Continuity@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use Features::AestheticFaceBlendBuilder::Chain1Continuity and Features::AestheticFaceBlendBuilder::Chain2Continuity instead.") NXOpen::GeometricUtilities::Continuity * Continuity
            (
            );
            /**Returns  the chain 1 continuity 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * Chain1Continuity
            (
            );
            /**Returns  the chain 2 continuity 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * Chain2Continuity
            (
            );
            /**Returns  the is min radius 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsMinimumRadius
            (
            );
            /**Sets  the is min radius 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumRadius
            (
                bool isMinimumRadius /** isminimumradius */ 
            );
            /**Returns  the min radius 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MinimumRadius
            (
            );
            /**Returns  the blend faces option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::BlendFacesType BlendFacesOption
            (
            );
            /**Sets  the blend faces option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetBlendFacesOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::BlendFacesType blendFacesOption /** blendfacesoption */ 
            );
            /**Returns  the is trim faces 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsTrimInputFaces
            (
            );
            /**Sets  the is trim faces 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetTrimInputFaces
            (
                bool isTrimFaces /** istrimfaces */ 
            );
            /**Returns  the is sew faces 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsSewAllFaces
            (
            );
            /**Sets  the is sew faces 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSewAllFaces
            (
                bool isSewFaces /** issewfaces */ 
            );
            /**Returns  the trim object collector list 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BlendLimitsData * LimitsList
            (
            );
            /**Returns  the washout1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsWashout1
            (
            );
            /**Sets  the washout1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetWashout1
            (
                bool isWashout1 /** iswashout1 */ 
            );
            /**Returns  the start point1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ConstrainedStartPoint1
            (
            );
            /**Sets  the start point1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetConstrainedStartPoint1
            (
                NXOpen::Point * startPoint1 /** startpoint1 */ 
            );
            /**Returns  the end point1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ConstrainedEndPoint1
            (
            );
            /**Sets  the end point1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetConstrainedEndPoint1
            (
                NXOpen::Point * endPoint1 /** endpoint1 */ 
            );
            /**Returns  the section scaling 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SectionScaling1
            (
            );
            /**Returns  the toggle washout2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsWashout2
            (
            );
            /**Sets  the toggle washout2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetWashout2
            (
                bool isWashout2 /** iswashout2 */ 
            );
            /**Returns  the start point2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ConstrainedStartPoint2
            (
            );
            /**Sets  the start point2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetConstrainedStartPoint2
            (
                NXOpen::Point * startPoint2 /** startpoint2 */ 
            );
            /**Returns  the end point2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ConstrainedEndPoint2
            (
            );
            /**Sets  the end point2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetConstrainedEndPoint2
            (
                NXOpen::Point * endPoint2 /** endpoint2 */ 
            );
            /**Returns  the section scaling2 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SectionScaling2
            (
            );
            /**Returns  the rational output 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsRationalOutput
            (
            );
            /**Sets  the rational output 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRationalOutput
            (
                bool isRationalOutput /** isrationaloutput */ 
            );
            /**Returns  the degrees 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DegreesAndSegmentsOrPatchesBuilder * Degrees
            (
            );
            /**Returns  the bezier 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsBezier
            (
            );
            /**Sets  the bezier 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetBezier
            (
                bool isBezier /** isbezier */ 
            );
            /**Returns  the centerline curve 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsCenterlineCurve
            (
            );
            /**Sets  the centerline curve 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetCenterlineCurve
            (
                bool isCenterlineCurve /** iscenterlinecurve */ 
            );
            /**Returns  the segmentation option
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::SegmentationType SegmentationOption
            (
            );
            /**Sets  the segmentation option
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSegmentationOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::SegmentationType segmentationOption /** segmentationoption */ 
            );
            /**Returns  the max edge length 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumEdgeLength
            (
            );
            /**Sets  the max edge length 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumEdgeLength
            (
                double minEdgeLength /** minedgelength */ 
            );
            /**Returns  the position tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double PositionTolerance
            (
            );
            /**Sets  the position tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetPositionTolerance
            (
                double positionTolerance /** positiontolerance */ 
            );
            /**Returns  the tangent tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double TangentTolerance
            (
            );
            /**Sets  the tangent tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetTangentTolerance
            (
                double tangentTolerance /** tangenttolerance */ 
            );
            /**Returns  the curvature tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double CurvatureTolerance
            (
            );
            /**Sets  the curvature tolerance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetCurvatureTolerance
            (
                double curvatureTolerance /** curvaturetolerance */ 
            );
            /**Returns  the relative start point on the washout curve of start blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RelativeStartBlendStartPoint
            (
            );
            /**Sets  the relative start point on the washout curve of start blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRelativeStartBlendStartPoint
            (
                double startPoint /** startpoint */ 
            );
            /**Returns  the relative end point on the washout curve of start blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RelativeStartBlendEndPoint
            (
            );
            /**Sets  the relative end point on the washout curve of start blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRelativeStartBlendEndPoint
            (
                double endPoint /** endpoint */ 
            );
            /**Returns  the relative start point on the washout curve of end blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RelativeEndBlendStartPoint
            (
            );
            /**Sets  the relative start point on the washout curve of end blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRelativeEndBlendStartPoint
            (
                double startPoint /** startpoint */ 
            );
            /**Returns  the relative end point on the washout curve of end blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double RelativeEndBlendEndPoint
            (
            );
            /**Sets  the relative end point on the washout curve of end blend.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRelativeEndBlendEndPoint
            (
                double endPoint /** endpoint */ 
            );
            /**Returns  the minimum subtended angle flag 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsMinimumSubtendedAngle
            (
            );
            /**Sets  the minimum subtended angle flag 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumSubtendedAngle
            (
                bool isMinimumSubtendedAngle /** isminimumsubtendedangle */ 
            );
            /**Returns  the minimum subtended angle 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumSubtendedAngle
            (
            );
            /**Sets  the minimum subtended angle 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumSubtendedAngle
            (
                double minimumSubtendedAngle /** minimumsubtendedangle */ 
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
