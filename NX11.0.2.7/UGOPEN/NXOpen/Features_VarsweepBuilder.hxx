#ifndef NXOpen_FEATURES_VARSWEEPBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VARSWEEPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VarsweepBuilder.ja
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
#include <NXOpen/Features_VarsweepBuilder.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/GeometricUtilities_PlayButtonsBuilder.hxx>
#include <NXOpen/GeometricUtilities_SecondarySectionData.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class VarsweepBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BooleanOperation;
    }
    namespace GeometricUtilities
    {
        class FeatureOptions;
    }
    namespace GeometricUtilities
    {
        class Limits;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    namespace GeometricUtilities
    {
        class PlayButtonsBuilder;
    }
    namespace GeometricUtilities
    {
        class SecondarySectionData;
    }
    class ObjectList;
    class Section;
    namespace Features
    {
        class _VarsweepBuilderBuilder;
        class VarsweepBuilderImpl;
        /** Represents a Variational Sweep feature builder. It creates or edits VarSweep feature. <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateVarsweepBuilder  NXOpen::Features::FeatureCollection::CreateVarsweepBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ConstantFittingSectionCount </td> <td> 
         
        -1 </td> </tr> 

        <tr><td> 
         
        PlayButtons.CurrentStep </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PlayButtons.PlayModes </td> <td> 
         
        PlayOnce </td> </tr> 

        <tr><td> 
         
        PlayButtons.ScaleSpeed </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        PlayButtons.ScaleStep </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PlayButtons.Speed </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ReviewSection </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  VarsweepBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: VarsweepBuilderImpl * m_varsweepbuilder_impl;
            private: friend class  _VarsweepBuilderBuilder;
            protected: VarsweepBuilder();
            public: ~VarsweepBuilder();
            /**Sets  the master section. Variational sweep accepts
                    sections created ONLY on in the context of a Sketch on Path.
                    Make sure this section is coming from sketch curves created using
                    the sketch on path feature.
                    Return code : 0 : no error,
                    VARSWEEP_SKETCH_NOT_ON_PATH : on an error condition
                  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSection
            (
                NXOpen::Section * section /** master section */
            );
            /**Sets  the distance tolerance
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distance tolerance */ 
            );
            /**Sets  the angle tolerance [degrees]
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngularTolerance
            (
                double angleTolerance /** angle tolerance */ 
            );
            /**Sets  the merge faces option
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMergeFacesOption
            (
                bool mergeFacesOption /** merge faces option */ 
            );
            /**Sets  the re-project curves option
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReProjectCurvesOption
            (
                bool reProjectCurvesOption /** re project curves option */ 
            );
            /**Sets  the constant fitting section count
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetConstantFittingSectionCount
            (
                int constantFittingSectionCount /** constant fitting section count */ 
            );
            /**Returns  the variational sweep limits
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricUtilities::Limits * Limits
            (
            );
            /**Returns  the distance tolerance
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Returns  the angle tolerance [degrees]
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: double AngularTolerance
            (
            );
            /**Returns  the merge faces option
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool MergeFacesOption
            (
            );
            /**Returns  the re-project curves option
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReProjectCurvesOption
            (
            );
            /**Returns  the constant fitting section count
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: int ConstantFittingSectionCount
            (
            );
            /**Returns  the master section. Variational sweep accepts
                    sections created ONLY on in the context of a Sketch on Path.
                    Make sure this section is coming from sketch curves created using
                    the sketch on path feature.
                    Return code : 0 : no error,
                    VARSWEEP_SKETCH_NOT_ON_PATH : on an error condition
                  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Returns  the boolean option 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanOperation * BooleanOperation
            (
            );
            /**Returns  the solid versus sheet body type option 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FeatureOptions * FeatureOptions
            (
            );
            /**Returns  the sketch on path
                    
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::Feature * SketchOnPathFeature
            (
            );
            /**Returns  the secondary section list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ObjectList * List
            (
            );
            /**Sets  the secondary section list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetList
            (
                NXOpen::ObjectList * list /** list */ 
            );
            /** Create new list item
                       @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SecondarySectionData * NewListItem
            (
            );
            /**Returns  the review section 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReviewSection
            (
            );
            /**Sets  the review section 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReviewSection
            (
                bool reviewSection /** reviewsection */ 
            );
            /**Returns  the path increment 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * PathIncrement
            (
            );
            /**Returns  the play buttons builder
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PlayButtonsBuilder * PlayButtons
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
