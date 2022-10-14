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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_ThroughCurvesBuilder.hxx>
#include <NXOpen/GeometricUtilities_AlignmentMethodBuilder.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_FlowDirection.hxx>
#include <NXOpen/GeometricUtilities_Rebuild.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class ThroughCurvesBuilderImpl;
        /**
            Represents a @link NXOpen::Features::ThroughCurves NXOpen::Features::ThroughCurves@endlink  builder.
             <br> This builder lets you create or edit a body through a collection of curve outlines in one direction.
            The curve outlines are referred to as section strings. 
             <br> 
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateThroughCurvesBuilder  NXOpen::Features::FeatureCollection::CreateThroughCurvesBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Alignment.AlignType </td> <td> 
         
        Parameter </td> </tr> 

        <tr><td> 
         
        ClosedInV </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        Construction </td> <td> 
         
        Normal </td> </tr> 

        <tr><td> 
         
        FirstSectionContinuity.ContinuityType </td> <td> 
         
        G0 </td> </tr> 

        <tr><td> 
         
        FlowDirection.FlowDirectionType </td> <td> 
         
        NotSpecified </td> </tr> 

        <tr><td> 
         
        LastSectionContinuity.ContinuityType </td> <td> 
         
        G0 </td> </tr> 

        <tr><td> 
         
        LoftingSurfaceRebuildData.Degree </td> <td> 
         
        3 </td> </tr> 

        <tr><td> 
         
        LoftingSurfaceRebuildData.RebuildType </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        NormalToEndSections </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        PatchType </td> <td> 
         
        Multiple </td> </tr> 

        <tr><td> 
         
        PreserveShape </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        SectionSurfaceRebuildData.RebuildType </td> <td> 
         
        None </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ThroughCurvesBuilder : public NXOpen::Features::FeatureBuilder
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

            /** This enum represents the body type option. If sections are all
                        closed, if possible then a solid body can be created. */
            public: enum BodyPreferenceTypes
            {
                BodyPreferenceTypesSolid/** Solid */,
                BodyPreferenceTypesSheet/** Sheet */
            };

            private: ThroughCurvesBuilderImpl * m_throughcurvesbuilder_impl;
            private: friend class  _ThroughCurvesBuilderBuilder;
            protected: ThroughCurvesBuilder();
            public: ~ThroughCurvesBuilder();
            /**Returns  the sections list which is required. See @link NXOpen::ObjectList NXOpen::ObjectList@endlink  for details.
                    The section strings define the rows of the body. A section string can consist of a single object or
                    multiple objects, and each object can be one of the following: a curve or a solid edge.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::SectionList * SectionsList
            (
            );
            /**Returns  the first section continuity. See @link NXOpen::GeometricUtilities::Continuity NXOpen::GeometricUtilities::Continuity@endlink  for details.
                    Define continuity constraint at the first section side.
                    It contains the continuity type and the constraint face.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Continuity * FirstSectionContinuity
            (
            );
            /**Returns  the last section continuity. See @link NXOpen::GeometricUtilities::Continuity NXOpen::GeometricUtilities::Continuity@endlink  for details.
                    Define continuity constraint at the last section side.
                    It contains the continuity type and the constraint face.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Continuity * LastSectionContinuity
            (
            );
            /**Returns  the flow direction. See @link NXOpen::GeometricUtilities::FlowDirection NXOpen::GeometricUtilities::FlowDirection@endlink  for details.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::FlowDirection * FlowDirection
            (
            );
            /**Returns  the alignment. See @link NXOpen::GeometricUtilities::AlignmentMethodBuilder NXOpen::GeometricUtilities::AlignmentMethodBuilder@endlink  for details.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::AlignmentMethodBuilder * Alignment
            (
            );
            /**Returns  the patch type. Lets you create a body containing a single patch or multiple patches.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::Features::ThroughCurvesBuilder::PatchTypes PatchType
            (
            );
            /**Sets  the patch type. Lets you create a body containing a single patch or multiple patches.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetPatchType
            (
                NXOpen::Features::ThroughCurvesBuilder::PatchTypes patchType /** patch type */ 
            );
            /**Returns  the closed in V. When this option is ON, the sheet is closed along columns (that is, the V direction).
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: bool ClosedInV
            (
            );
            /**Sets  the closed in V. When this option is ON, the sheet is closed along columns (that is, the V direction).
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetClosedInV
            (
                bool closedInV /** closed in v */ 
            );
            /**Returns  the option of normal to end sections for Through Curves surface, which makes the output surface 
                    normal to the two end sections.If an end section is planar, the surface will be parallel to the plane 
                    normal at the end.If an end section is a 3D curve, an average normal vector will be computed, and the 
                    surface will be parallel to the average normal at the end. If an end section is a line, the normal 
                    vector will be computed so that it points from the end section to the section next to the end section. 
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: bool NormalToEndSections
            (
            );
            /**Sets  the option of normal to end sections for Through Curves surface, which makes the output surface 
                    normal to the two end sections.If an end section is planar, the surface will be parallel to the plane 
                    normal at the end.If an end section is a 3D curve, an average normal vector will be computed, and the 
                    surface will be parallel to the average normal at the end. If an end section is a line, the normal 
                    vector will be computed so that it points from the end section to the section next to the end section. 
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetNormalToEndSections
            (
                bool normalToEndSections /** normal to end sections */ 
            );
            /**Returns  the construction options.
                    Use one of three construction options when you create a Through Curves feature: Normal, Use Spline Points and Simple.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::Features::ThroughCurvesBuilder::ConstructionMethod Construction
            (
            );
            /**Sets  the construction options.
                    Use one of three construction options when you create a Through Curves feature: Normal, Use Spline Points and Simple.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetConstruction
            (
                NXOpen::Features::ThroughCurvesBuilder::ConstructionMethod construction /** construction */ 
            );
            /**Returns  the section template curve.
                    Control the building of the simple surface in section curve direction.
                    It is only available when the construction method is simple.
                    If you leave it empty, the system will automatically choose the most complicated one for fitting.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::Section * SectionTemplateString
            (
            );
            /**Sets  the section template curve.
                    Control the building of the simple surface in section curve direction.
                    It is only available when the construction method is simple.
                    If you leave it empty, the system will automatically choose the most complicated one for fitting.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetSectionTemplateString
            (
                NXOpen::Section * sectionTemplate /** sectiontemplate */ 
            );
            /**Returns  the preserve shape. Allow you to keep sharp edges, overriding the default of approximating the output
                    surface. Setting the Tolerance to 0.0 will achieve the same result. 
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: bool PreserveShape
            (
            );
            /**Sets  the preserve shape. Allow you to keep sharp edges, overriding the default of approximating the output
                    surface. Setting the Tolerance to 0.0 will achieve the same result. 
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetPreserveShape
            (
                bool preserveShape /** preserve shape */ 
            );
            /**Returns  the section surface rebuild data. See @link NXOpen::GeometricUtilities::Rebuild NXOpen::GeometricUtilities::Rebuild@endlink  for details.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Rebuild * SectionSurfaceRebuildData
            (
            );
            /**Returns  the lofting surface rebuild data. See @link NXOpen::GeometricUtilities::Rebuild NXOpen::GeometricUtilities::Rebuild@endlink  for details.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Rebuild * LoftingSurfaceRebuildData
            (
            );
            /**Returns  the position tolerance.
                    Control the distance accuracy of the rebuild surface in relation to the input curves.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: double PositionTolerance
            (
            );
            /**Sets  the position tolerance.
                    Control the distance accuracy of the rebuild surface in relation to the input curves.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetPositionTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the tangent tolerance.
                    Control the angular accuracy of the rebuild surface in relation to the input curves.It is expressed in degree.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: double TangentTolerance
            (
            );
            /**Sets  the tangent tolerance.
                    Control the angular accuracy of the rebuild surface in relation to the input curves.It is expressed in degree.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetTangentTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the curvature tolerance.
                    Control the curvature tolerance of the rebuild surface in relation to the input curves.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: double CurvatureTolerance
            (
            );
            /**Sets  the curvature tolerance.
                    Control the curvature tolerance of the rebuild surface in relation to the input curves.
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetCurvatureTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the body type options 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::ThroughCurvesBuilder::BodyPreferenceTypes BodyPreference
            (
            );
            /**Sets  the body type options 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR nx_freeform_1 ("basic freeform modeling") */
            public: void SetBodyPreference
            (
                NXOpen::Features::ThroughCurvesBuilder::BodyPreferenceTypes bodyPreference /** bodypreference */ 
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