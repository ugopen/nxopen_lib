#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_VIEWCONTOURBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_VIEWCONTOURBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_ViewContourBuilder.ja
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
#include <NXOpen/Features_TopologyOptimization_Study.hxx>
#include <NXOpen/Builder.hxx>
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
        namespace TopologyOptimization
        {
            class ViewContourBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class Study;
        }
    }
    class SelectTaggedObjectList;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _ViewContourBuilderBuilder;
            class ViewContourBuilderImpl;
            /**
                    Represents a builder to specify contour display settings and plot contours according to the settings
                     <br> To create a new instance of this class, use @link NXOpen::Features::TopologyOptimization::PostManager::CreateViewContourBuilder  NXOpen::Features::TopologyOptimization::PostManager::CreateViewContourBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ViewContourBuilder : public NXOpen::Builder
            {
                /** Display type option */
                public: enum DisplayOption
                {
                    DisplayOptionSingle/** single */ ,
                    DisplayOptionComparison/** comparison */ 
                };

                /** Result type and component type option */
                public: enum ResultComponentOption
                {
                    ResultComponentOptionDisplacementMagnitude/** displacement magnitude */ ,
                    ResultComponentOptionDisplacementWorstInXYZ/** displacement worst in xyz */ ,
                    ResultComponentOptionDisplacementX/** displacement x */ ,
                    ResultComponentOptionDisplacementY/** displacement y */ ,
                    ResultComponentOptionDisplacementZ/** displacement z */ ,
                    ResultComponentOptionDisplacementAll/** Displacement All includes Worst in XYZ, X, Y and Z*/,
                    ResultComponentOptionStressVonMises/** stress von mises */ ,
                    ResultComponentOptionStressWorstPrincipal/** stress worst principal */ 
                };

                /** Contour display style option */
                public: enum ContourDisplayStyleOption
                {
                    ContourDisplayStyleOptionSmooth/** smooth */ ,
                    ContourDisplayStyleOptionBanded/** banded */ 
                };

                /** Color scale range option */
                public: enum ColorScaleRangeOption
                {
                    ColorScaleRangeOptionPerView/** per view */ ,
                    ColorScaleRangeOptionCommonAcrossViews/** common across views */ 
                };

                private: ViewContourBuilderImpl * m_viewcontourbuilder_impl;
                private: friend class  _ViewContourBuilderBuilder;
                protected: ViewContourBuilder();
                public: ~ViewContourBuilder();
                /**Returns  the display type choice 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::ViewContourBuilder::DisplayOption DisplayType
                (
                );
                /**Sets  the display type choice 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetDisplayType
                (
                    NXOpen::Features::TopologyOptimization::ViewContourBuilder::DisplayOption displayType /** displaytype */ 
                );
                /**Returns  the first study choice 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::Study * FirstStudy
                (
                );
                /**Sets  the first study choice 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetFirstStudy
                (
                    NXOpen::Features::TopologyOptimization::Study * study /** study */ 
                );
                /**Returns  the subcase index for first study choice 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: int SubcaseIndexForFirstStudy
                (
                );
                /**Sets  the subcase index for first study choice 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetSubcaseIndexForFirstStudy
                (
                    int subcaseIndexForFirstStudy /** subcaseindexforfirststudy */ 
                );
                /**Returns  the second study choice, this choice is available for study comparison case 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::Study * SecondStudy
                (
                );
                /**Sets  the second study choice, this choice is available for study comparison case 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetSecondStudy
                (
                    NXOpen::Features::TopologyOptimization::Study * study /** study */ 
                );
                /**Returns  the subcase index for second study choice, this choice is available for study comparison case 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: int SubcaseIndexForSecondStudy
                (
                );
                /**Sets  the subcase index for second study choice, this choice is available for study comparison case 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetSubcaseIndexForSecondStudy
                (
                    int subcaseIndexForSecondStudy /** subcaseindexforsecondstudy */ 
                );
                /**Returns  the selected solid bodies for scenery bodies or design spaces 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectTaggedObjectList * Bodies
                (
                );
                /**Returns  the result component type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::ViewContourBuilder::ResultComponentOption ResultComponentType
                (
                );
                /**Sets  the result component type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetResultComponentType
                (
                    NXOpen::Features::TopologyOptimization::ViewContourBuilder::ResultComponentOption resultComponentType /** resultcomponenttype */ 
                );
                /**Returns  the contour display style 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::ViewContourBuilder::ContourDisplayStyleOption ContourDisplayStyle
                (
                );
                /**Sets  the contour display style 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetContourDisplayStyle
                (
                    NXOpen::Features::TopologyOptimization::ViewContourBuilder::ContourDisplayStyleOption contourDisplayStyle /** contourdisplaystyle */ 
                );
                /**Returns  the color scale range type. This option is only available for multiple contours display like comparison report, single report with specified
                            @link  Features::TopologyOptimization::ViewContourBuilder::ResultComponentOption::DisplacementAll   Features::TopologyOptimization::ViewContourBuilder::ResultComponentOption::DisplacementAll @endlink  
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::ViewContourBuilder::ColorScaleRangeOption ColorScaleRangeType
                (
                );
                /**Sets  the color scale range type. This option is only available for multiple contours display like comparison report, single report with specified
                            @link  Features::TopologyOptimization::ViewContourBuilder::ResultComponentOption::DisplacementAll   Features::TopologyOptimization::ViewContourBuilder::ResultComponentOption::DisplacementAll @endlink  
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetColorScaleRangeType
                (
                    NXOpen::Features::TopologyOptimization::ViewContourBuilder::ColorScaleRangeOption colorScaleRangeOption /** colorscalerangeoption */ 
                );
            };
        }
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
