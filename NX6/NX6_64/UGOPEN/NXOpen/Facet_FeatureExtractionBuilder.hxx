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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Facet_FeatureExtractionBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /**
            Represents a @link Facet::FeatureExtractionBuilder Facet::FeatureExtractionBuilder@endlink 
            It extracts feature lines or separates regions of different curvature
            from a facet body based on the curvature map.
            For facet body curvature, please see @link Facet::CurvatureBuilder Facet::CurvatureBuilder@endlink .
             <br> To create a new instance of this class, use @link Facet::FacetedBodyCollection::CreateFacetFeatureExtractionBuilder Facet::FacetedBodyCollection::CreateFacetFeatureExtractionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT FeatureExtractionBuilder : public Builder
        {
            /** Specifies how to handle the input facet bodies. */
            public: enum InputActions
            {
                InputActionsBlank/** Blank the input facet bodies */,
                InputActionsRetain/** Retain the input facet bodies */,
                InputActionsDelete/** Delete the input facet bodies */
            };

            private: friend class  _FeatureExtractionBuilderBuilder;
            protected: FeatureExtractionBuilder();
            /**Returns  the input facet body selection list  <br> License requirements : None */
            public: NXOpen::Facet::SelectFacetedBodyList * FacetBodies
            (
            );
            /**Returns   the extracting regions option  <br> License requirements : None */
            public: bool AreRegionsEnabled
            (
            );
            /**Sets   the extracting regions option  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetAreRegionsEnabled
            (
                bool regionsEnabled /** regionsenabled */ 
            );
            /**Returns  the extracting borders option  <br> License requirements : None */
            public: bool AreBordersEnabled
            (
            );
            /**Sets  the extracting borders option  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetAreBordersEnabled
            (
                bool bordersEnabled /** bordersenabled */ 
            );
            /**Returns  the smoothing option  <br> License requirements : None */
            public: bool IsSmoothingEnabled
            (
            );
            /**Sets  the smoothing option  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSmoothingEnabled
            (
                bool smoothingEanbled /** smoothingeanbled */ 
            );
            /**Returns  the smoothing factor  <br> License requirements : None */
            public: double SmoothingFactor
            (
            );
            /**Sets  the smoothing factor  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSmoothingFactor
            (
                double smoothingFactor /** smoothingfactor */ 
            );
            /**Returns  the input facet body action  <br> License requirements : None */
            public: NXOpen::Facet::FeatureExtractionBuilder::InputActions InputAction
            (
            );
            /**Sets  the input facet body action  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetInputAction
            (
                NXOpen::Facet::FeatureExtractionBuilder::InputActions inputAction /** inputaction */ 
            );
            /**Returns  the minimum border length  <br> License requirements : None */
            public: double MinimumBorderLength
            (
            );
            /**Sets  the minimum border length  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinimumBorderLength
            (
                double minimumBorderLength /** minimumborderlength */ 
            );
            /** Gets the extracted facet bodies. Call @link Builder::Commit Builder::Commit@endlink  before calling this method.  @return  The extracted facet bodies  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: std::vector<NXOpen::Facet::FacetedBody *> GetExtractedRegions
            (
            );
            /** Gets the extracted curves. Call @link Builder::Commit Builder::Commit@endlink  before calling this method.  @return  The extracted curves <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: std::vector<NXOpen::Spline *> GetExtractedBorders
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif