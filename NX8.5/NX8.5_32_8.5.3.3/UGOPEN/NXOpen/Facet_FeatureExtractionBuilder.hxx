#ifndef NXOpen_FACET_FEATUREEXTRACTIONBUILDER_HXX_INCLUDED
#define NXOpen_FACET_FEATUREEXTRACTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_FeatureExtractionBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Facet_FeatureExtractionBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_facet_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Facet
    {
        class FeatureExtractionBuilder;
    }
    class Builder;
    namespace Facet
    {
        class FacetedBody;
    }
    namespace Facet
    {
        class SelectFacetedBodyList;
    }
    class Spline;
    namespace Facet
    {
        class _FeatureExtractionBuilderBuilder;
        class FeatureExtractionBuilderImpl;
        /**
            Represents a @link Facet::FeatureExtractionBuilder Facet::FeatureExtractionBuilder@endlink 
            It extracts feature lines or separates regions of different curvature
            from a facet body based on the curvature map.
            For facet body curvature, please see @link Facet::CurvatureBuilder Facet::CurvatureBuilder@endlink .
             <br> To create a new instance of this class, use @link Facet::FacetedBodyCollection::CreateFacetFeatureExtractionBuilder  Facet::FacetedBodyCollection::CreateFacetFeatureExtractionBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  FeatureExtractionBuilder : public Builder
        {
            /** Specifies how to handle the input facet bodies. */
            public: enum InputActions
            {
                InputActionsBlank/** Blank the input facet bodies */,
                InputActionsRetain/** Retain the input facet bodies */,
                InputActionsDelete/** Delete the input facet bodies */
            };

            private: FeatureExtractionBuilderImpl * m_featureextractionbuilder_impl;
            private: friend class  _FeatureExtractionBuilderBuilder;
            protected: FeatureExtractionBuilder();
            public: ~FeatureExtractionBuilder();
            /**Returns  the input facet body selection list 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SelectFacetedBodyList * FacetBodies
            (
            );
            /**Returns   the extracting regions option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool AreRegionsEnabled
            (
            );
            /**Sets   the extracting regions option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetAreRegionsEnabled
            (
                bool regionsEnabled /** regionsenabled */ 
            );
            /**Returns  the extracting borders option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool AreBordersEnabled
            (
            );
            /**Sets  the extracting borders option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetAreBordersEnabled
            (
                bool bordersEnabled /** bordersenabled */ 
            );
            /**Returns  the smoothing option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsSmoothingEnabled
            (
            );
            /**Sets  the smoothing option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSmoothingEnabled
            (
                bool smoothingEanbled /** smoothingeanbled */ 
            );
            /**Returns  the smoothing factor 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double SmoothingFactor
            (
            );
            /**Sets  the smoothing factor 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSmoothingFactor
            (
                double smoothingFactor /** smoothingfactor */ 
            );
            /**Returns  the input facet body action 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::FeatureExtractionBuilder::InputActions InputAction
            (
            );
            /**Sets  the input facet body action 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetInputAction
            (
                NXOpen::Facet::FeatureExtractionBuilder::InputActions inputAction /** inputaction */ 
            );
            /**Returns  the minimum border length 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumBorderLength
            (
            );
            /**Sets  the minimum border length 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumBorderLength
            (
                double minimumBorderLength /** minimumborderlength */ 
            );
            /** Gets the extracted facet bodies. Call @link Builder::Commit Builder::Commit@endlink  before calling this method.  @return  The extracted facet bodies 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: std::vector<NXOpen::Facet::FacetedBody *> GetExtractedRegions
            (
            );
            /** Gets the extracted curves. Call @link Builder::Commit Builder::Commit@endlink  before calling this method.  @return  The extracted curves
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: std::vector<NXOpen::Spline *> GetExtractedBorders
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
