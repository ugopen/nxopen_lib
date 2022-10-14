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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
    class Section;
    namespace Features
    {
        class _VarsweepBuilderBuilder;
        /** Represents a Variational Sweep feature builder. It creates or edits VarSweep feature. <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateVarsweepBuilder Features::FeatureCollection::CreateVarsweepBuilder@endlink  <br> */
        class NXOPENCPPEXPORT VarsweepBuilder : public Features::FeatureBuilder
        {
            private: friend class  _VarsweepBuilderBuilder;
            protected: VarsweepBuilder();
            /**Sets  the master section. Variational sweep accepts 
                    sections created ONLY on in the context of a Sketch on Path. 
                    Make sure this section is coming from sketch curves created using
                    the sketch on path feature.
                    Return code : 0 : no error,
                    VARSWEEP_SKETCH_NOT_ON_PATH : on an error condition
                   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSection
            (
                NXOpen::Section * section /** master section */
            );
            /**Sets  the distance tolerance <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distance_tolerance /** */
            );
            /**Sets  the angle tolerance [degrees] <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngularTolerance
            (
                double angle_tolerance /** */
            );
            /**Sets  the merge faces option <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMergeFacesOption
            (
                bool merge_faces_option /** */
            );
            /**Sets  the child feature option 
                   Precondition : Variational Sweep is the next feature
                                  after the sketch i.e there is no feature between
                                  sketch and the Varsweep getting created
                   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSketchChildFeatureOption
            (
                bool child_feature_option /** */
            );
            /**Returns  the distance tolerance <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Returns  the angle tolerance [degrees] <br> License requirements : None */
            public: double AngularTolerance
            (
            );
            /**Returns  the merge faces option <br> License requirements : None */
            public: bool MergeFacesOption
            (
            );
            /**Returns  the master section. Variational sweep accepts 
                    sections created ONLY on in the context of a Sketch on Path. 
                    Make sure this section is coming from sketch curves created using
                    the sketch on path feature.
                    Return code : 0 : no error,
                    VARSWEEP_SKETCH_NOT_ON_PATH : on an error condition
                   <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Returns  the boolean option  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanOperation * BooleanOperation
            (
            );
            /**Returns  the solid versus sheet body type option  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FeatureOptions * FeatureOptions
            (
            );
            /**Returns  the sketch on path
                     <br> License requirements : None */
            public: NXOpen::Features::Feature * SketchOnPathFeature
            (
            );
            /**Returns  the child feature option 
                   Precondition : Variational Sweep is the next feature
                                  after the sketch i.e there is no feature between
                                  sketch and the Varsweep getting created
                   <br> License requirements : None */
            public: bool SketchChildFeatureOption
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif