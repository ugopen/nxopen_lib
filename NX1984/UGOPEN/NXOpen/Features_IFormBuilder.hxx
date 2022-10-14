#ifndef NXOpen_FEATURES_IFORMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_IFORMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_IFormBuilder.ja
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
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_CurveShapingBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class IFormBuilder;
    }
    class Curve;
    class Face;
    namespace Features
    {
        class FaceRecognitionBuilder;
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
        class CurveShapingBuilder;
    }
    class SelectPointList;
    namespace Features
    {
        class _IFormBuilderBuilder;
        class IFormBuilderImpl;
        /**
                Represents a @link NXOpen::Features::IForm NXOpen::Features::IForm@endlink  builder.
                This class allows definition of iso-parameter curves on a face. These curves then
                can be shaped using @link NXOpen::GeometricUtilities::CurveShapingBuilder NXOpen::GeometricUtilities::CurveShapingBuilder@endlink  to 
                finally shape the face.
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateIformBuilder  NXOpen::Features::FeatureCollection::CreateIformBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BSurfaceExtractionOption </term> <description> 
         
        Original </description> </item> 

        <item><term> 
         
        CanApplyToAll </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        CanKeepParameterization </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        CurveShaper.HasLinearTransition </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        CurveShaper.InsertionMethod </term> <description> 
         
        Uniform </description> </item> 

        <item><term> 
         
        CurveShaper.MovementMethod </term> <description> 
         
        Normal </description> </item> 

        <item><term> 
         
        CurveShaper.Number </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        CurveShaper.WCSOption </term> <description> 
         
        XY </description> </item> 

        <item><term> 
         
        FaceToDeform.CloneEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.CoaxialEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.CoplanarAxesEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.CoplanarEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.EqualDiameterEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.OffsetEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.ParallelEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.PatternEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.PerpendicularEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.SameEntryEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.SameEntrySurfaceEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.SameOrbitEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.SymmetricEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.TangentEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.ThicknessChainEnabled </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        FaceToDeform.UseFaceBrowse </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        InsertionMethod </term> <description> 
         
        Uniform </description> </item> 

        <item><term> 
         
        Number </term> <description> 
         
        3 </description> </item> 

        <item><term> 
         
        ParameterDirection </term> <description> 
         
        IsoU </description> </item> 

        <item><term> 
         
        TransitionType </term> <description> 
         
        Global </description> </item> 

        <item><term> 
         
        UMaxContinuity.ContinuityType </term> <description> 
         
        G0 </description> </item> 

        <item><term> 
         
        UMinContinuity.ContinuityType </term> <description> 
         
        G0 </description> </item> 

        <item><term> 
         
        VMaxContinuity.ContinuityType </term> <description> 
         
        G0 </description> </item> 

        <item><term> 
         
        VMinContinuity.ContinuityType </term> <description> 
         
        G0 </description> </item> 

        </list> 

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  IFormBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Iso-parameter direction options */
            public: enum ParameterDirectionOptions
            {
                ParameterDirectionOptionsIsoU/** Iso-U direction */,
                ParameterDirectionOptionsIsoV/** Iso-V direction */
            };

            /** Iso-parameter curve insertion option */
            public: enum InsertionMethodOptions
            {
                InsertionMethodOptionsUniform/** Insert curves uniformly */,
                InsertionMethodOptionsThroughPoints/** Insert curves through points */,
                InsertionMethodOptionsBetweenPoints/** Insert curves between points */
            };

            /** Transition options of the surface */
            public: enum TransitionTypes
            {
                TransitionTypesLocal/** Local transition */,
                TransitionTypesGlobal/** Global transition */
            };

            /** Global transition options of the surface */
            public: enum GlobalTransitionTypes
            {
                GlobalTransitionTypesBlend/** Blend type global transition */,
                GlobalTransitionTypesBell/** Bell type global transition */
            };

            /** B-surface extraction options */
            public: enum BSurfaceExtractionOptions
            {
                BSurfaceExtractionOptionsOriginal/** Extract original surface */,
                BSurfaceExtractionOptionsMinimumBounded/** Extract minimum bounded surface */,
                BSurfaceExtractionOptionsFittedToBoundary/** Extract surface fitted to boundary of face */
            };

            private: IFormBuilderImpl * m_iformbuilder_impl;
            private: friend class  _IFormBuilderBuilder;
            protected: IFormBuilder();
            public: ~IFormBuilder();
            /**Returns  the face to deform. Please refer @link NXOpen::Features::FaceRecognitionBuilder NXOpen::Features::FaceRecognitionBuilder@endlink  for details. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FaceToDeform
            (
            );
            /**Returns  the iso-parameter direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::IFormBuilder::ParameterDirectionOptions ParameterDirection
            (
            );
            /**Sets  the iso-parameter direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetParameterDirection
            (
                NXOpen::Features::IFormBuilder::ParameterDirectionOptions parameterDirection /** parameterdirection */ 
            );
            /**Returns  the iso-parameter curve insertion method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::IFormBuilder::InsertionMethodOptions InsertionMethod
            (
            );
            /**Sets  the iso-parameter curve insertion method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetInsertionMethod
            (
                NXOpen::Features::IFormBuilder::InsertionMethodOptions insertionMethod /** insertionmethod */ 
            );
            /**Returns  the specified points to define iso-parameter curve 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * SpecifyPoints
            (
            );
            /**Returns  the number of iso-parameter curves to be inserted 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int Number
            (
            );
            /**Sets  the number of iso-parameter curves to be inserted 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetNumber
            (
                int number /** number */ 
            );
            /**Returns  the iso-parameter curve shaper 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveShapingBuilder * CurveShaper
            (
            );
            /**Returns  the transition options for local surface deformation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::IFormBuilder::TransitionTypes TransitionType
            (
            );
            /**Sets  the transition options for local surface deformation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetTransitionType
            (
                NXOpen::Features::IFormBuilder::TransitionTypes transitionType /** transitiontype */ 
            );
            /**Returns  the value indicating if continuity is to be applied to all sides of the surface 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool CanApplyToAll
            (
            );
            /**Sets  the value indicating if continuity is to be applied to all sides of the surface 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetCanApplyToAll
            (
                bool applyToAll /** applytoall */ 
            );
            /**Returns  the continuity at minimum U direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * UMinContinuity
            (
            );
            /**Returns  the continuity at maximum U direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * UMaxContinuity
            (
            );
            /**Returns  the continuity at minimum V direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * VMinContinuity
            (
            );
            /**Returns  the continuity at maximum U direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity * VMaxContinuity
            (
            );
            /**Returns  the value indicating if input surface parameterization should be preserved during deformation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool CanKeepParameterization
            (
            );
            /**Sets  the value indicating if input surface parameterization should be preserved during deformation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetCanKeepParameterization
            (
                bool canKeepParameterization /** cankeepparameterization */ 
            );
            /**Returns  the b-surface extraction option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::IFormBuilder::BSurfaceExtractionOptions BSurfaceExtractionOption
            (
            );
            /**Sets  the b-surface extraction option 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetBSurfaceExtractionOption
            (
                NXOpen::Features::IFormBuilder::BSurfaceExtractionOptions option /** option */ 
            );
            /**Returns  the tolerance used for b-surface extraction from a face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double ExtractTolerance
            (
            );
            /**Sets  the tolerance used for b-surface extraction from a face 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetExtractTolerance
            (
                double extractTolerance /** extracttolerance */ 
            );
            /** Deletes a iso-parameter curve 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void DeleteCurve
            (
                NXOpen::Curve * curve /** Curve to be deleted */
            );
            /** Removes parameters of a owning feature of a face to be deformed 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void RemoveFeatureParameters
            (
                NXOpen::Face * face /** Face to be used for feature parameter removal */
            );
            /**Returns  whether the operation is applied to a copy of the face there by creating new body 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool CanCreateNewBody
            (
            );
            /**Sets  whether the operation is applied to a copy of the face there by creating new body 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetCanCreateNewBody
            (
                bool newBody /** newbody */ 
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