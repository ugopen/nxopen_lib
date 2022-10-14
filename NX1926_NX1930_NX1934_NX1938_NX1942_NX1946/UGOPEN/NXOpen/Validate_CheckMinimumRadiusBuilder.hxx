#ifndef NXOpen_VALIDATE_CHECKMINIMUMRADIUSBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_CHECKMINIMUMRADIUSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_CheckMinimumRadiusBuilder.ja
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
#include <NXOpen/GeometricUtilities_DisplayResolutionBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Validate_SelectionAndPlacementBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class CheckMinimumRadiusBuilder;
    }
    class Builder;
    class Face;
    namespace GeometricUtilities
    {
        class DisplayResolutionBuilder;
    }
    class NXColor;
    namespace Validate
    {
        class SelectionAndPlacementBuilder;
    }
    namespace Validate
    {
        class _CheckMinimumRadiusBuilderBuilder;
        class CheckMinimumRadiusBuilderImpl;
        /** Represents a Check Minimum Radius builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckMinimumRadiusBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckMinimumRadiusBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AutomaticUpdate </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.AngleTolerance </term> <description> 
         
        15.0 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.EdgeTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.FaceTolerance </term> <description> 
         
        0.005 </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.Resolution </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        DisplayResolutionBuilder.WidthTolerance </term> <description> 
         
        0.3 </description> </item> 

        <item><term> 
         
        ExcludeConvex </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        LessThanMinimumRadiusColor </term> <description> 
         
        186 </description> </item> 

        <item><term> 
         
        MinimumRadius </term> <description> 
         
        0.5 (millimeters part), 0.02 (inches part) </description> </item> 

        <item><term> 
         
        MoreThanMinimumRadiusColor </term> <description> 
         
        36 </description> </item> 

        <item><term> 
         
        PreviewState </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ShowOnlyFailArea </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  CheckMinimumRadiusBuilder : public NXOpen::Builder
        {
            /** Represents the curvature type */
            public: enum CurvatureTypes
            {
                CurvatureTypesRadius/** 3D Minimum */,
                CurvatureTypesSectional/** sectional */ 
            };

            private: CheckMinimumRadiusBuilderImpl * m_checkminimumradiusbuilder_impl;
            private: friend class  _CheckMinimumRadiusBuilderBuilder;
            protected: CheckMinimumRadiusBuilder();
            public: ~CheckMinimumRadiusBuilder();
            /**Returns  the selection and placement builder
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::SelectionAndPlacementBuilder * SelectionAndPlacement
            (
            );
            /**Returns  the curvature type to compute and display.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validate::CheckMinimumRadiusBuilder::CurvatureTypes CurvatureType
            (
            );
            /**Sets  the curvature type to compute and display.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCurvatureType
            (
                NXOpen::Validate::CheckMinimumRadiusBuilder::CurvatureTypes curvatureType /** curvaturetype */ 
            );
            /**Returns  the Minimum Radius 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumRadius
            (
            );
            /**Sets  the Minimum Radius 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumRadius
            (
                double minimumRadius /** minimumradius */ 
            );
            /**Returns  the Exclude Convex  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ExcludeConvex
            (
            );
            /**Sets  the Exclude Convex  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExcludeConvex
            (
                bool excludeConvex /** excludeconvex */ 
            );
            /**Returns  the show only less than minimum radius toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowOnlyFailArea
            (
            );
            /**Sets  the show only less than minimum radius toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowOnlyFailArea
            (
                bool showOnlyFailArea /** showonlyfailarea */ 
            );
            /**Returns  the More Than Minimum Radius Color
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * MoreThanMinimumRadiusColor
            (
            );
            /**Sets  the More Than Minimum Radius Color
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMoreThanMinimumRadiusColor
            (
                NXOpen::NXColor * moreThanMinimumRadiusColor /** morethanminimumradiuscolor */ 
            );
            /**Returns  the Less Than Minimum Radius Color
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * LessThanMinimumRadiusColor
            (
            );
            /**Sets  the Less Than Minimum Radius Color
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLessThanMinimumRadiusColor
            (
                NXOpen::NXColor * lessThanMinimumRadiusColor /** lessthanminimumradiuscolor */ 
            );
            /** Returns the dynamic result  @return  The minimum radius evaluated 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double GetDynamicResult
            (
                NXOpen::Face * selectedFace /** The specified face */,
                const NXOpen::Point3d & dynamicPnt /** The specified point */
            );
            /**Returns  the automatic update toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutomaticUpdate
            (
            );
            /**Sets  the automatic update toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAutomaticUpdate
            (
                bool automaticUpdate /** automaticupdate */ 
            );
            /**Returns  the preview toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreviewState
            (
            );
            /**Sets  the preview toggle 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPreviewState
            (
                bool previewState /** previewstate */ 
            );
            /**Returns  the area where radius is less than the minimum radius 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: double FailureArea
            (
            );
            /**Returns  the display resolution 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::DisplayResolutionBuilder * DisplayResolutionBuilder
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