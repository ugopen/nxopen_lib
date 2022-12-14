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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_AestheticFaceBlendBuilder.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_DegreesAndSegmentsOrPatchesBuilder.hxx>
#include <NXOpen/GeometricUtilities_LawBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
    class ScCollector;
    class Section;
    namespace Features
    {
        class _AestheticFaceBlendBuilderBuilder;
        class AestheticFaceBlendBuilderImpl;
        /** This class will provide ability to create aesthetically pleasing blend surfaces on sheet and solid bodies. <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateAestheticFaceBlendBuilder Features::FeatureCollection::CreateAestheticFaceBlendBuilder@endlink  <br> 
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
         
        CenterRadiusLaw.LawType </td> <td> 
         
        MultiTransition </td> </tr> 

        <tr><td> 
         
        ChordLength.Value </td> <td> 
         
        10 (millimeters part), 0.4 (inches part) </td> </tr> 

        <tr><td> 
         
        Continuity.ContinuityType </td> <td> 
         
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
         
        IsMinimumRadius </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsRationalOutput </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsSameTransition </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        IsTrimInputFaces </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MinimumRadius.Value </td> <td> 
         
        2.5 (millimeters part), 0.098 (inches part) </td> </tr> 

        <tr><td> 
         
        ShapeOption </td> <td> 
         
        Accelerated </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  AestheticFaceBlendBuilder : public Features::FeatureBuilder
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

            /** Trimming options */
            public: enum BlendFacesType
            {
                BlendFacesTypeTrimtoAllInputFaces/** Trims all input faces. */,
                BlendFacesTypeTrimtoShortInputFaces/** Trims short input faces. */,
                BlendFacesTypeTrimtoLongInputFaces/** Trims long input faces. */,
                BlendFacesTypeDoNotTrimBlendFaces/** This option controls to trim blend faces or not */
            };

            private: AestheticFaceBlendBuilderImpl * m_aestheticfaceblendbuilder_impl;
            private: friend class  _AestheticFaceBlendBuilderBuilder;
            protected: AestheticFaceBlendBuilder();
            public: ~AestheticFaceBlendBuilder();
            /**Returns  the face chain1  <br> License requirements : None */
            public: NXOpen::ScCollector * FaceChain1
            (
            );
            /**Returns  the reverse normal1  <br> License requirements : None */
            public: bool ReverseNormal1
            (
            );
            /**Sets  the reverse normal1  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetReverseNormal1
            (
                bool reverseNormal1 /** reversenormal1 */ 
            );
            /**Returns  the face chain2  <br> License requirements : None */
            public: NXOpen::ScCollector * FaceChain2
            (
            );
            /**Returns  the reverse normal2  <br> License requirements : None */
            public: bool ReverseNormal2
            (
            );
            /**Sets  the reverse normal2  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetReverseNormal2
            (
                bool reverseNormal2 /** reversenormal2 */ 
            );
            /**Returns  the alignment option  <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::AlignmentType AlignmentOption
            (
            );
            /**Sets  the alignment option  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetAlignmentOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::AlignmentType alignmentOption /** alignmentoption */ 
            );
            /**Returns  the parameter spine  <br> License requirements : None */
            public: NXOpen::Section * ParameterSpine
            (
            );
            /**Returns  the section alignment vector  <br> License requirements : None */
            public: NXOpen::Direction * SectionAlignmentVector
            (
            );
            /**Sets  the section alignment vector  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSectionAlignmentVector
            (
                NXOpen::Direction * sectionAlignmentVector /** sectionalignmentvector */ 
            );
            /**Returns  the method option  <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::BlendType BlendOption
            (
            );
            /**Sets  the method option  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetBlendOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::BlendType blendOption /** blendoption */ 
            );
            /**Returns  the law variable  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * BaseRadiusLaw
            (
            );
            /**Returns  the chord length  <br> License requirements : None */
            public: NXOpen::Expression * ChordLength
            (
            );
            /**Returns  the shape option  <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::ShapeType ShapeOption
            (
            );
            /**Sets  the shape option  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetShapeOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::ShapeType shapeOption /** shapeoption */ 
            );
            /**Returns  the blend cross section is using the same transition as blend tangent or not  <br> License requirements : None */
            public: bool IsSameTransition
            (
            );
            /**Sets  the blend cross section is using the same transition as blend tangent or not  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetSameTransition
            (
                bool isSameTransition /** issametransition */ 
            );
            /**Returns  the center radius law  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::LawBuilder * CenterRadiusLaw
            (
            );
            /**Returns  the continuity  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * Continuity
            (
            );
            /**Returns  the is min radius  <br> License requirements : None */
            public: bool IsMinimumRadius
            (
            );
            /**Sets  the is min radius  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumRadius
            (
                bool isMinimumRadius /** isminimumradius */ 
            );
            /**Returns  the min radius  <br> License requirements : None */
            public: NXOpen::Expression * MinimumRadius
            (
            );
            /**Returns  the blend faces option  <br> License requirements : None */
            public: NXOpen::Features::AestheticFaceBlendBuilder::BlendFacesType BlendFacesOption
            (
            );
            /**Sets  the blend faces option  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetBlendFacesOption
            (
                NXOpen::Features::AestheticFaceBlendBuilder::BlendFacesType blendFacesOption /** blendfacesoption */ 
            );
            /**Returns  the is trim faces  <br> License requirements : None */
            public: bool IsTrimInputFaces
            (
            );
            /**Sets  the is trim faces  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetTrimInputFaces
            (
                bool isTrimFaces /** istrimfaces */ 
            );
            /**Returns  the is rational output  <br> License requirements : None */
            public: bool IsRationalOutput
            (
            );
            /**Sets  the is rational output  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetRationalOutput
            (
                bool isRationalOutput /** isrationaloutput */ 
            );
            /**Returns  the degrees  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DegreesAndSegmentsOrPatchesBuilder * Degrees
            (
            );
            /**Returns  the position tolerance  <br> License requirements : None */
            public: double PositionTolerance
            (
            );
            /**Sets  the position tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetPositionTolerance
            (
                double positionTolerance /** positiontolerance */ 
            );
            /**Returns  the tangent tolerance  <br> License requirements : None */
            public: double TangentTolerance
            (
            );
            /**Sets  the tangent tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetTangentTolerance
            (
                double tangentTolerance /** tangenttolerance */ 
            );
            /**Returns  the curvature tolerance  <br> License requirements : None */
            public: double CurvatureTolerance
            (
            );
            /**Sets  the curvature tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetCurvatureTolerance
            (
                double curvatureTolerance /** curvaturetolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
