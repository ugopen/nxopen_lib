#ifndef NXOpen_FEATURES_FACEBLENDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_FACEBLENDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FaceBlendBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class FaceBlendBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CircularCrossSection;
    }
    namespace GeometricUtilities
    {
        class ConicCrossSection;
    }
    class ISurface;
    class Plane;
    class Point;
    class ScCollector;
    class Section;
    namespace Features
    {
        class _FaceBlendBuilderBuilder;
        class FaceBlendBuilderImpl;
        /** Represents a face blend builder. 
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateFaceBlendBuilder Features::FeatureCollection::CreateFaceBlendBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CircularCrossSection.LawControl.Function </td> <td> 
         
        ft </td> </tr> 

        <tr><td> 
         
        CircularCrossSection.LawControl.LawType </td> <td> 
         
        Constant </td> </tr> 

        <tr><td> 
         
        CircularCrossSection.LawControl.Parameter </td> <td> 
         
        t </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  FaceBlendBuilder : public Features::FeatureBuilder
        {
            /** This enum represents the Face Blend types */
            public: enum Type
            {
                TypeRollingBall/** rolling ball */ ,
                TypeSwept/** swept */ 
            };

            /** This enum represents the Cross section types */
            public: enum CrossSectionOption
            {
                CrossSectionOptionCircular/** circular */ ,
                CrossSectionOptionConic/** conic */ 
            };

            /** This enum represents the Trimming options for Face Blend */
            public: enum TrimmingMethod
            {
                TrimmingMethodToAllFaces/** Trim to all faces */,
                TrimmingMethodShort/** Trim short */,
                TrimmingMethodLong/** Trim long */,
                TrimmingMethodNone/** No trim */
            };

            /** This enum represents the overflow options */
            public: enum OverflowMethod
            {
                OverflowMethodNone/** No overflow option */,
                OverflowMethodNotch/** Notch or Maintain Blend And Move Sharp Edges option */
            };

            /** This enum represents the rho types */
            public: enum RhoMethod
            {
                RhoMethodAbsolute/** Absolute (NX) rho type */,
                RhoMethodRelative/** Relative (I-deas) rho type */
            };

            /** This enum represents the Face Blend defining type, it is added in NX75 for new three face blend */
            public: enum DefiningType
            {
                DefiningTypeBlendTwoFace/** this is for normal two face blend */,
                DefiningTypeBlendThreeFace/** this is form new three face blend */
            };

            private: FaceBlendBuilderImpl * m_faceblendbuilder_impl;
            private: friend class  _FaceBlendBuilderBuilder;
            protected: FaceBlendBuilder();
            public: ~FaceBlendBuilder();
            /**Sets  the first face collector
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFirstFaceCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the first face collector
                 <br> License requirements : None */
            public: NXOpen::ScCollector * FirstFaceCollector
            (
            );
            /**Sets  the first face set normal reversal flag
                 <br> License requirements : None */
            public: void SetReverseFirstFaceNormal
            (
                bool flipFlag /** flip flag */ 
            );
            /**Returns  the first face set normal reversal flag
                 <br> License requirements : None */
            public: bool ReverseFirstFaceNormal
            (
            );
            /**Sets  the second face collector
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSecondFaceCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the second face collector
                 <br> License requirements : None */
            public: NXOpen::ScCollector * SecondFaceCollector
            (
            );
            /**Sets  the second face set normal reversal flag
                 <br> License requirements : None */
            public: void SetReverseSecondFaceNormal
            (
                bool flipFlag /** flip flag */ 
            );
            /**Returns  the second face set normal reversal flag
                 <br> License requirements : None */
            public: bool ReverseSecondFaceNormal
            (
            );
            /**Returns  the face blend circular section
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CircularCrossSection * CircularCrossSection
            (
            );
            /**Returns  the face blend conic section
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ConicCrossSection * ConicCrossSection
            (
            );
            /**Returns  the spine for face blend
                 <br> License requirements : None */
            public: NXOpen::Section * Spine
            (
            );
            /**Sets  the spine for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSpine
            (
                NXOpen::Section * spine /** spine */ 
            );
            /**Returns  the cliff edge collector for face blend
                 <br> License requirements : None */
            public: NXOpen::ScCollector * CoincidentEdgeCollector
            (
            );
            /**Sets  the cliff edge collector for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCoincidentEdgeCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the tangency collector of edges or/and curves for face blend
                 <br> License requirements : None */
            public: NXOpen::ScCollector * TangencyCollector
            (
            );
            /**Sets  the tangency collector of edges or/and curves for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTangencyCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the tangency object for face blend.
                 <br> License requirements : None */
            public: NXOpen::ISurface * TangentSurface
            (
            );
            /**Sets  the tangency object for face blend.
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTangentSurface
            (
                NXOpen::ISurface * object /** object */ 
            );
            /**Sets  the third face set normal reversal flag
                 <br> License requirements : None */
            public: void SetReverseThirdFaceNormal
            (
                bool flipFlag /** flip flag */ 
            );
            /**Returns  the third face set normal reversal flag
                 <br> License requirements : None */
            public: bool ReverseThirdFaceNormal
            (
            );
            /**Returns  the face blend help point
                 <br> License requirements : None */
            public: NXOpen::Point * HelpPoint
            (
            );
            /**Sets  the face blend help point
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetHelpPoint
            (
                NXOpen::Point * helpPoint /** help point */ 
            );
            /** This function is to get limit planes for a face blend feature.
                 <br> License requirements : None */
            public: void GetLimitPlanes
            (
                NXOpen::Plane ** startLimitPlane /** Start limit plane */,
                NXOpen::Plane ** endLimitPlane /** End limit plane */
            );
            /** This function is to set limit planes for a face blend feature.
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetLimitPlanes
            (
                NXOpen::Plane * startLimitPlane /** Start limit plane */,
                NXOpen::Plane * endLimitPlane /** End limit plane */
            );
            /**Returns  the start limit faceset collector
                 <br> License requirements : None */
            public: NXOpen::ScCollector * StartLimitFacesetCollector
            (
            );
            /**Sets  the start limit faceset collector
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartLimitFacesetCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the end limit faceset collector
                 <br> License requirements : None */
            public: NXOpen::ScCollector * EndLimitFacesetCollector
            (
            );
            /**Sets  the end limit faceset collector
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndLimitFacesetCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the start limiting face normal flag  <br> License requirements : None */
            public: bool StartLimitFaceNormalFlag
            (
            );
            /**Sets  the start limiting face normal flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartLimitFaceNormalFlag
            (
                bool flipFlag /** flip flag */ 
            );
            /**Returns  the end limiting face normal flag  <br> License requirements : None */
            public: bool EndLimitFaceNormalFlag
            (
            );
            /**Sets  the end limiting face normal flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndLimitFaceNormalFlag
            (
                bool flipFlag /** flip flag */ 
            );
            /**Returns  the trimming option for face blend
                 <br> License requirements : None */
            public: NXOpen::Features::FaceBlendBuilder::TrimmingMethod TrimmingOption
            (
            );
            /**Sets  the trimming option for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTrimmingOption
            (
                NXOpen::Features::FaceBlendBuilder::TrimmingMethod trimmingOption /** trimming option */ 
            );
            /**Returns  the option for Trim Input Faces to Blend Faces
                 <br> License requirements : None */
            public: bool TrimInputFacesToBlendFaces
            (
            );
            /**Sets  the option for Trim Input Faces to Blend Faces
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTrimInputFacesToBlendFaces
            (
                bool trimInputFacesToBlendFaces /** trim input faces to blend faces */ 
            );
            /**Returns  the sew option for face blend
                 <br> License requirements : None */
            public: bool SewAllFaces
            (
            );
            /**Sets  the sew option for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSewAllFaces
            (
                bool sewOption /** sew option */ 
            );
            /**Returns  the type for face blend
                 <br> License requirements : None */
            public: NXOpen::Features::FaceBlendBuilder::Type BlendType
            (
            );
            /**Sets  the type for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetBlendType
            (
                NXOpen::Features::FaceBlendBuilder::Type type /** type */ 
            );
            /**Returns  the cross section for face blend
                 <br> License requirements : None */
            public: NXOpen::Features::FaceBlendBuilder::CrossSectionOption CrossSectionType
            (
            );
            /**Sets  the cross section for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCrossSectionType
            (
                NXOpen::Features::FaceBlendBuilder::CrossSectionOption type /** type */ 
            );
            /**Returns  the option for Add Tangent Faces As Encountered
                 <br> License requirements : None */
            public: bool AddTangentFaces
            (
            );
            /**Sets  the option for Add Tangent Faces As Encountered
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAddTangentFaces
            (
                bool option /** option */ 
            );
            /**Returns  the option for Orient Cross Section By Isoparameter Lines for Swept section type only
                 <br> License requirements : None */
            public: bool IsIsoparameterLineOriented
            (
            );
            /**Sets  the option for Orient Cross Section By Isoparameter Lines for Swept section type only
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetIsoparameterLineOriented
            (
                bool option /** option */ 
            );
            /**Returns  the self-intersections option for face blend
                 <br> License requirements : None */
            public: bool RemoveSelfIntersections
            (
            );
            /**Sets  the self-intersections option for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRemoveSelfIntersections
            (
                bool option /** option */ 
            );
            /**Returns  the propagate past the sharp edges option for face blend
                 <br> License requirements : None */
            public: bool PropagatePastSharpEdges
            (
            );
            /**Sets  the propagate past the sharp edges option for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPropagatePastSharpEdges
            (
                bool option /** option */ 
            );
            /**Returns  the propagation angle for face blend
                 <br> License requirements : None */
            public: double PropagationAngle
            (
            );
            /**Sets  the propagation angle for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPropagationAngle
            (
                double propagationAngle /** propagation angle */ 
            );
            /**Returns  the projection option for face blend
                 <br> License requirements : None */
            public: bool ProjectToSecondWall
            (
            );
            /**Sets  the projection option for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetProjectToSecondWall
            (
                bool projectToSecondWall /** project to second wall */ 
            );
            /**Returns  the overflow option for face blend
                 <br> License requirements : None */
            public: NXOpen::Features::FaceBlendBuilder::OverflowMethod OverflowOption
            (
            );
            /**Sets  the overflow option for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOverflowOption
            (
                NXOpen::Features::FaceBlendBuilder::OverflowMethod option /** option */ 
            );
            /**Returns  the rho type for face blend
                 <br> License requirements : None */
            public: NXOpen::Features::FaceBlendBuilder::RhoMethod RhoType
            (
            );
            /**Sets  the rho type for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRhoType
            (
                NXOpen::Features::FaceBlendBuilder::RhoMethod rhoMethod /** rho method */ 
            );
            /**Returns  the tolerance for face blend
                 <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance for face blend
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the start parameter or 'from' range for the third face with a three-face blend
                    <br> License requirements : None */
            public: double ThirdFaceStartParameter
            (
            );
            /**Sets  the start parameter or 'from' range for the third face with a three-face blend
                    <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetThirdFaceStartParameter
            (
                double range /** range */ 
            );
            /**Returns  the end paramater or 'to' range for the third face with a three-face blend
                    <br> License requirements : None */
            public: double ThirdFaceEndParameter
            (
            );
            /**Sets  the end paramater or 'to' range for the third face with a three-face blend
                    <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetThirdFaceEndParameter
            (
                double range /** range */ 
            );
            /**Returns  the start limit plane capping option  <br> License requirements : None */
            public: bool StartCapLimitPlaneOption
            (
            );
            /**Sets  the start limit plane capping option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartCapLimitPlaneOption
            (
                bool option /** option */ 
            );
            /**Returns  the end limit plane capping option  <br> License requirements : None */
            public: bool EndCapLimitPlaneOption
            (
            );
            /**Sets  the end limit plane capping option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndCapLimitPlaneOption
            (
                bool option /** option */ 
            );
            /**Returns  the start limit point  <br> License requirements : None */
            public: NXOpen::Point * StartLimitPoint
            (
            );
            /**Sets  the start limit point  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartLimitPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the end limit point  <br> License requirements : None */
            public: NXOpen::Point * EndLimitPoint
            (
            );
            /**Sets  the end limit point  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndLimitPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /** Updates all the constant law parms in the builder using builder section. This call must be
                  made every time the section is updated. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UpdateConstantLawProfiles
            (
            );
            /**Returns  the face blend defining type get
                   <br> License requirements : None */
            public: NXOpen::Features::FaceBlendBuilder::DefiningType FaceBlendDefineType
            (
            );
            /**Sets  the face blend defining type get
                   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFaceBlendDefineType
            (
                NXOpen::Features::FaceBlendBuilder::DefiningType type /** type */ 
            );
            /**Sets  the middle face collector get
                    <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMiddleFaceCollector
            (
                NXOpen::ScCollector * collector /** collector */ 
            );
            /**Returns  the middle face collector get
                    <br> License requirements : None */
            public: NXOpen::ScCollector * MiddleFaceCollector
            (
            );
            /**Sets  the middle face set normal reversal flag
                    <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMiddleFaceNormFlag
            (
                bool flipFlag /** flip flag */ 
            );
            /**Returns  the middle face set normal reversal flag
                    <br> License requirements : None */
            public: bool MiddleFaceNormFlag
            (
            );
            /**Returns  the cliff projection option for face blend
                   <br> License requirements : None */
            public: bool CliffProjectOntoSecondWall
            (
            );
            /**Sets  the cliff projection option for face blend
                   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCliffProjectOntoSecondWall
            (
                bool projectOntoSecondWall /** project onto second wall */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif