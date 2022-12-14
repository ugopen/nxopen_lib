#ifndef NXOpen_FEATURES_THROUGHCURVESBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_THROUGHCURVESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ThroughCurvesBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ThroughCurvesBuilder.hxx>
#include <NXOpen/GeometricUtilities_AlignmentMethodBuilder.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_FlowDirection.hxx>
#include <NXOpen/GeometricUtilities_Rebuild.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ThroughCurvesBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class AlignmentMethodBuilder;
    }
    namespace GeometricUtilities
    {
        class Continuity;
    }
    namespace GeometricUtilities
    {
        class FlowDirection;
    }
    namespace GeometricUtilities
    {
        class Rebuild;
    }
    class Section;
    class SectionList;
    namespace Features
    {
        class _ThroughCurvesBuilderBuilder;
        /**
            Represents a @link Features::ThroughCurves Features::ThroughCurves@endlink  builder.
             <br> This builder lets you create or edit a body through a collection of curve outlines in one direction.
            The curve outlines are referred to as section strings. 
             <br> 
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateThroughCurvesBuilder Features::FeatureCollection::CreateThroughCurvesBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ThroughCurvesBuilder : public Features::FeatureBuilder
        {
            /** 
                    This enum represents the Patch options. 
                    */
            public: enum PatchTypes
            {
                PatchTypesSingle/** single patch.*/,
                PatchTypesMultiple/** multiple patches.*/,
                PatchTypesMatchString/** patch match string.*/
            };

            /** 
                    This enum represents the Construction options.
                    */
            public: enum ConstructionMethod
            {
                ConstructionMethodNormal/** Use the standard procedures.*/,
                ConstructionMethodSplinePoints/** Use the points and tangent values at the points for reparameterizing curves.*/,
                ConstructionMethodSimple/** Build the simplest mesh surface possible.*/
            };

            private: friend class  _ThroughCurvesBuilderBuilder;
            protected: ThroughCurvesBuilder();
            /**Returns  the sections list which is required. See @link ObjectList ObjectList@endlink  for details.
                    The section strings define the rows of the body. A section string can consist of a single object or
                    multiple objects, and each object can be one of the following: a curve or a solid edge. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::SectionList * SectionsList
            (
            );
            /**Returns  the first section continuity. See @link GeometricUtilities::Continuity GeometricUtilities::Continuity@endlink  for details.
                    Define continuity constraint at the first section side.
                    It contains the continuity type and the constraint face.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Continuity * FirstSectionContinuity
            (
            );
            /**Returns  the last section continuity. See @link GeometricUtilities::Continuity GeometricUtilities::Continuity@endlink  for details.
                    Define continuity constraint at the last section side.
                    It contains the continuity type and the constraint face.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Continuity * LastSectionContinuity
            (
            );
            /**Returns  the flow direction. See @link GeometricUtilities::FlowDirection GeometricUtilities::FlowDirection@endlink  for details.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::FlowDirection * FlowDirection
            (
            );
            /**Returns  the alignment. See @link GeometricUtilities::AlignmentMethodBuilder GeometricUtilities::AlignmentMethodBuilder@endlink  for details.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::AlignmentMethodBuilder * Alignment
            (
            );
            /**Returns  the patch type. Lets you create a body containing a single patch or multiple patches.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::Features::ThroughCurvesBuilder::PatchTypes PatchType
            (
            );
            /**Sets  the patch type. Lets you create a body containing a single patch or multiple patches.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetPatchType
            (
                NXOpen::Features::ThroughCurvesBuilder::PatchTypes patch_type /** patch type */ 
            );
            /**Returns  the closed in V. When this option is ON, the sheet is closed along columns (that is, the V direction).
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: bool ClosedInV
            (
            );
            /**Sets  the closed in V. When this option is ON, the sheet is closed along columns (that is, the V direction).
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetClosedInV
            (
                bool closed_in_v /** closed in v */ 
            );
            /**Returns  the option of normal to end sections for Through Curves surface, which makes the output surface 
                    normal to the two end sections.If an end section is planar, the surface will be parallel to the plane 
                    normal at the end.If an end section is a 3D curve, an average normal vector will be computed, and the 
                    surface will be parallel to the average normal at the end. If an end section is a line, the normal 
                    vector will be computed so that it points from the end section to the section next to the end section. 
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: bool NormalToEndSections
            (
            );
            /**Sets  the option of normal to end sections for Through Curves surface, which makes the output surface 
                    normal to the two end sections.If an end section is planar, the surface will be parallel to the plane 
                    normal at the end.If an end section is a 3D curve, an average normal vector will be computed, and the 
                    surface will be parallel to the average normal at the end. If an end section is a line, the normal 
                    vector will be computed so that it points from the end section to the section next to the end section. 
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetNormalToEndSections
            (
                bool normal_to_end_sections /** normal to end sections */ 
            );
            /**Returns  the construction options.
                    Use one of three construction options when you create a Through Curves feature: Normal, Use Spline Points and Simple.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::Features::ThroughCurvesBuilder::ConstructionMethod Construction
            (
            );
            /**Sets  the construction options.
                    Use one of three construction options when you create a Through Curves feature: Normal, Use Spline Points and Simple.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetConstruction
            (
                NXOpen::Features::ThroughCurvesBuilder::ConstructionMethod construction /** construction */ 
            );
            /**Returns  the section template curve.
                    Control the building of the simple surface in section curve direction.
                    It is only available when the construction method is simple.
                    If you leave it empty, the system will automatically choose the most complicated one for fitting.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::Section * SectionTemplateString
            (
            );
            /**Sets  the section template curve.
                    Control the building of the simple surface in section curve direction.
                    It is only available when the construction method is simple.
                    If you leave it empty, the system will automatically choose the most complicated one for fitting.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetSectionTemplateString
            (
                NXOpen::Section * sectionTemplate /** sectiontemplate */ 
            );
            /**Returns  the preserve shape. Allow you to keep sharp edges, overriding the default of approximating the output
                    surface. Setting the Tolerance to 0.0 will achieve the same result. 
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: bool PreserveShape
            (
            );
            /**Sets  the preserve shape. Allow you to keep sharp edges, overriding the default of approximating the output
                    surface. Setting the Tolerance to 0.0 will achieve the same result. 
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetPreserveShape
            (
                bool preserve_shape /** preserve shape */ 
            );
            /**Returns  the section surface rebuild data. See @link GeometricUtilities::Rebuild GeometricUtilities::Rebuild@endlink  for details.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Rebuild * SectionSurfaceRebuildData
            (
            );
            /**Returns  the lofting surface rebuild data. See @link GeometricUtilities::Rebuild GeometricUtilities::Rebuild@endlink  for details.
                     <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Rebuild * LoftingSurfaceRebuildData
            (
            );
            /**Returns  the position tolerance.
                    Control the distance accuracy of the rebuild surface in relation to the input curves. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: double PositionTolerance
            (
            );
            /**Sets  the position tolerance.
                    Control the distance accuracy of the rebuild surface in relation to the input curves. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetPositionTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the tangent tolerance.
                    Control the angular accuracy of the rebuild surface in relation to the input curves.It is expressed in degree. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: double TangentTolerance
            (
            );
            /**Sets  the tangent tolerance.
                    Control the angular accuracy of the rebuild surface in relation to the input curves.It is expressed in degree. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetTangentTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the curvature tolerance.
                    Control the curvature tolerance of the rebuild surface in relation to the input curves. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: double CurvatureTolerance
            (
            );
            /**Sets  the curvature tolerance.
                    Control the curvature tolerance of the rebuild surface in relation to the input curves. <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetCurvatureTolerance
            (
                double tolerance /** tolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
