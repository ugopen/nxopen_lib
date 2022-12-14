#ifndef NXOpen_GEOMETRICANALYSIS_DEVIATIONGAUGEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_DEVIATIONGAUGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_DeviationGaugeBuilder.ja
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
#include <NXOpen/Features_GeometricConstraintDataManager.hxx>
#include <NXOpen/GeometricUtilities_CurveRangeBuilder.hxx>
#include <NXOpen/GeometricUtilities_SurfaceRangeBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class DeviationGaugeBuilder;
    }
    class Builder;
    class Direction;
    namespace Features
    {
        class GeometricConstraintDataManager;
    }
    namespace GeometricUtilities
    {
        class CurveRangeBuilder;
    }
    namespace GeometricUtilities
    {
        class SurfaceRangeBuilder;
    }
    class NXObject;
    class Plane;
    class SelectNXObjectList;
    namespace GeometricAnalysis
    {
        class _DeviationGaugeBuilderBuilder;
        class DeviationGaugeBuilderImpl;
        /** DeviationGaugeBuilder class   <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateDeviationGaugeBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateDeviationGaugeBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ColorPlotType </term> <description> 
         
        Blend </description> </item> 

        <item><term> 
         
        CurveRangeControl.AnchorPosition </term> <description> 
         
        Start </description> </item> 

        <item><term> 
         
        DeviationIntervals </term> <description> 
         
        5 </description> </item> 

        <item><term> 
         
        HasAbsoluteColorPlot </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        HasAdditionalValuesLabel </term> <description> 
         
        None </description> </item> 

        <item><term> 
         
        HasMaximumValueLabel </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        HasMinimumValueLabel </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        InnerTolerance </term> <description> 
         
        0.1 </description> </item> 

        <item><term> 
         
        IsLabelDisplayed </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        IsMarkerDisplayed </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        IsNeedlePlotDisplayed </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        MaxCheckingAngle </term> <description> 
         
        5 </description> </item> 

        <item><term> 
         
        MaxCheckingDistance </term> <description> 
         
        1 (millimeters part), 0.5 (inches part) </description> </item> 

        <item><term> 
         
        MeasurementMethod </term> <description> 
         
        ThreeDim </description> </item> 

        <item><term> 
         
        MeasurementSamples </term> <description> 
         
        20 </description> </item> 

        <item><term> 
         
        MinMaxOption </term> <description> 
         
        Minmax </description> </item> 

        <item><term> 
         
        NeedleScale </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        NegativeInnerTolerance </term> <description> 
         
        -0.001 </description> </item> 

        <item><term> 
         
        NegativeOuterTolerance </term> <description> 
         
        -0.001 </description> </item> 

        <item><term> 
         
        OuterTolerance </term> <description> 
         
        0.1 </description> </item> 

        <item><term> 
         
        PositiveInnerTolerance </term> <description> 
         
        0.001 </description> </item> 

        <item><term> 
         
        PositiveOuterTolerance </term> <description> 
         
        0.001 </description> </item> 

        <item><term> 
         
        ReportingPerType </term> <description> 
         
        AnalysisObject </description> </item> 

        <item><term> 
         
        SpatialResolution </term> <description> 
         
        0.1 </description> </item> 

        <item><term> 
         
        SurfaceRangeControl.AnchorPosition </term> <description> 
         
        Vertex1 </description> </item> 

        <item><term> 
         
        XyzDirection </term> <description> 
         
        X </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  DeviationGaugeBuilder : public NXOpen::Builder
        {
            /** This enum represents the Deviation Gauge  Analysis Object evaluation types */
            public: enum MeasurementMethodType
            {
                MeasurementMethodTypeThreeDim/** 3D  */,
                MeasurementMethodTypeXyzDirection/** XYZ direction  */,
                MeasurementMethodTypeWorkView/** Work view     */,
                MeasurementMethodTypeVectorComponent/** Vector component    */,
                MeasurementMethodTypePlane/** Plane   */,
                MeasurementMethodTypeAlongVector/** Along vector   */
            };

            /** This enum represents the Deviation Gauge Analysis Object X, Y, Z direction options */
            public: enum XyzDirectionType
            {
                XyzDirectionTypeX/** X direction */,
                XyzDirectionTypeY/** Y direction */,
                XyzDirectionTypeZ/** Z direction */
            };

            /** This enum represents the Deviation Gauge  Analysis Object additional values label type */
            public: enum AdditionalValuesLabelType
            {
                AdditionalValuesLabelTypeUserDefined/**  User Defined  */,
                AdditionalValuesLabelTypeIntermediate/** Intermediate  */,
                AdditionalValuesLabelTypeAll/** All  */,
                AdditionalValuesLabelTypeNone/** None  */
            };

            /** This enum represents the Deviation Gauge  Analysis Object min max type */
            public: enum MinMaxType
            {
                MinMaxTypeMinmax/** Minimum/Maximum      */,
                MinMaxTypeMinimum/** Minimum  */,
                MinMaxTypeMaximum/** Maximum  */,
                MinMaxTypeNone/** None  */
            };

            /** This enum represents the Deviation Gauge  Analysis Object color plot types */
            public: enum ColorPlotTypes
            {
                ColorPlotTypesBlend/**  Blend */,
                ColorPlotTypesStepped/**  Stepped */,
                ColorPlotTypesNone/**  None  */
            };

            /** This enum represents the Deviation Gauge  Analysis Object reporting per setting */
            public: enum ReportingPerTypes
            {
                ReportingPerTypesAnalysisObject/**  Per Analysis Object */,
                ReportingPerTypesTarget/**  Per Target Object  */,
                ReportingPerTypesReference/**  Per Reference Object */
            };

            private: DeviationGaugeBuilderImpl * m_deviationgaugebuilder_impl;
            private: friend class  _DeviationGaugeBuilderBuilder;
            protected: DeviationGaugeBuilder();
            public: ~DeviationGaugeBuilder();
            /** Adds dynamic points to the Deviation Gauge. 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void AddDynamicPoints
            (
            );
            /**Returns  the target object 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::SelectNXObjectList * TargetObjects
            (
            );
            /**Returns  the reference object 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::SelectNXObjectList * ReferenceObjects
            (
            );
            /**Returns  the measurement method 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder::MeasurementMethodType MeasurementMethod
            (
            );
            /**Sets  the measurement method 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMeasurementMethod
            (
                NXOpen::GeometricAnalysis::DeviationGaugeBuilder::MeasurementMethodType measurementMethod /** measurementmethod */ 
            );
            /**Returns  the xyz direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder::XyzDirectionType XyzDirection
            (
            );
            /**Sets  the xyz direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetXyzDirection
            (
                NXOpen::GeometricAnalysis::DeviationGaugeBuilder::XyzDirectionType xyzDirection /** xyzdirection */ 
            );
            /**Returns  the direction vector. Not used if the measurement method is ThreeDim or Plane 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Direction * VectorComponentDirection
            (
            );
            /**Sets  the direction vector. Not used if the measurement method is ThreeDim or Plane 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetVectorComponentDirection
            (
                NXOpen::Direction * vectorComponentDirection /** vectorcomponentdirection */ 
            );
            /**Returns  the plane for measurement direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the plane for measurement direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the maximum checking distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double MaxCheckingDistance
            (
            );
            /**Sets  the maximum checking distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMaxCheckingDistance
            (
                double maxCheckingDistance /** maxcheckingdistance */ 
            );
            /**Returns  the maximum checking angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double MaxCheckingAngle
            (
            );
            /**Sets  the maximum checking angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMaxCheckingAngle
            (
                double maxCheckingAngle /** maxcheckingangle */ 
            );
            /**Returns  the number of measurement samples 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int MeasurementSamples
            (
            );
            /**Sets  the number of measurement samples 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMeasurementSamples
            (
                int measurementSamples /** measurementsamples */ 
            );
            /**Returns  the maximum checking angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double SpatialResolution
            (
            );
            /**Sets  the maximum checking angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSpatialResolution
            (
                double spatialResolution /** spatialresolution */ 
            );
            /**Returns   a value indicating whether to display label   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool IsLabelDisplayed
            (
            );
            /**Sets   a value indicating whether to display label   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetLabelDisplayed
            (
                bool labelDisplayed /** labeldisplayed */ 
            );
            /**Returns  a value indicating whether to display needle plot  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool IsNeedlePlotDisplayed
            (
            );
            /**Sets  a value indicating whether to display needle plot  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetNeedlePlotDisplayed
            (
                bool isNeedlePlotDisplayed /** isneedleplotdisplayed */ 
            );
            /**Returns  a value indicating whether to display marker  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool IsMarkerDisplayed
            (
            );
            /**Sets  a value indicating whether to display marker  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMarkerDisplayed
            (
                bool isMarkerDisplayed /** ismarkerdisplayed */ 
            );
            /**Returns  a value indicating whether to display color map  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool IsColorMapDisplayed
            (
            );
            /**Sets  a value indicating whether to display color map  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetColorMapDisplayed
            (
                bool isColorMapDisplayed /** iscolormapdisplayed */ 
            );
            /**Returns  a value indicating whether to display minimum value label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool HasMinimumValueLabel
            (
            );
            /**Sets  a value indicating whether to display minimum value label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasMinimumValueLabel
            (
                bool minimumValueLabel /** minimumvaluelabel */ 
            );
            /**Returns  a value indicating whether to display maximum value label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool HasMaximumValueLabel
            (
            );
            /**Sets  a value indicating whether to display maximum value label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasMaximumValueLabel
            (
                bool maximumValueLabel /** maximumvaluelabel */ 
            );
            /**Returns  a value indicating whether to display inner tolerance label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool HasInnerToleranceLabel
            (
            );
            /**Sets  a value indicating whether to display inner tolerance label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasInnerToleranceLabel
            (
                bool innerToleranceLabel /** innertolerancelabel */ 
            );
            /**Returns  a value indicating whether to display cross_curve deviation label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool HasCrossCurveDeviationLabel
            (
            );
            /**Sets  a value indicating whether to display cross_curve deviation label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasCrossCurveDeviationLabel
            (
                bool crossCurveDeviationLabel /** crosscurvedeviationlabel */ 
            );
            /**Returns  a value indicating whether to add additional values label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder::AdditionalValuesLabelType HasAdditionalValuesLabel
            (
            );
            /**Sets  a value indicating whether to add additional values label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasAdditionalValuesLabel
            (
                NXOpen::GeometricAnalysis::DeviationGaugeBuilder::AdditionalValuesLabelType additionalValuesLabel /** additionalvalueslabel */ 
            );
            /**Returns  the number of deviation intervals 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: int DeviationIntervals
            (
            );
            /**Sets  the number of deviation intervals 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetDeviationIntervals
            (
                int deviationIntervals /** deviationintervals */ 
            );
            /**Returns  a value indicating whether to use automatic scale factor 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool SuggestScaleFactor
            (
            );
            /**Sets  a value indicating whether to use automatic scale factor 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSuggestScaleFactor
            (
                bool suggestScaleFactor /** suggestscalefactor */ 
            );
            /**Returns  the needle scale 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double NeedleScale
            (
            );
            /**Sets  the needle scale 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetNeedleScale
            (
                double needleScale /** needlescale */ 
            );
            /**Returns  the min_max type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder::MinMaxType MinMaxOption
            (
            );
            /**Sets  the min_max type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMinMaxOption
            (
                NXOpen::GeometricAnalysis::DeviationGaugeBuilder::MinMaxType minMax /** minmax */ 
            );
            /**Returns  a value indicating whether to reverse the direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool IsDirectionReversed
            (
            );
            /**Sets  a value indicating whether to reverse the direction 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetDirectionReversed
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  a value indicating whether to plot using absolute value   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool HasAbsoluteColorPlot
            (
            );
            /**Sets  a value indicating whether to plot using absolute value   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasAbsoluteColorPlot
            (
                bool absoluteColorPlot /** absolutecolorplot */ 
            );
            /**Returns  the color plot type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder::ColorPlotTypes ColorPlotType
            (
            );
            /**Sets  the color plot type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetColorPlotType
            (
                NXOpen::GeometricAnalysis::DeviationGaugeBuilder::ColorPlotTypes colorPlotType /** colorplottype */ 
            );
            /**Returns  the outer tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double OuterTolerance
            (
            );
            /**Sets  the outer tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetOuterTolerance
            (
                double outerTolerance /** outertolerance */ 
            );
            /**Returns  the inner tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double InnerTolerance
            (
            );
            /**Sets  the inner tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetInnerTolerance
            (
                double innerTolerance /** innertolerance */ 
            );
            /**Returns  the positive outer tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double PositiveOuterTolerance
            (
            );
            /**Sets  the positive outer tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPositiveOuterTolerance
            (
                double positiveOuterTolerance /** positiveoutertolerance */ 
            );
            /**Returns  the positive inner tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double PositiveInnerTolerance
            (
            );
            /**Sets  the positive inner tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetPositiveInnerTolerance
            (
                double positiveInnerTolerance /** positiveinnertolerance */ 
            );
            /**Returns  the negative inner tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double NegativeInnerTolerance
            (
            );
            /**Sets  the negative inner tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetNegativeInnerTolerance
            (
                double negativennerTolerance /** negativennertolerance */ 
            );
            /**Returns  the negative outer tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: double NegativeOuterTolerance
            (
            );
            /**Sets  the negative outer tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetNegativeOuterTolerance
            (
                double negativeOuterTolerance /** negativeoutertolerance */ 
            );
            /**Returns  the surface range   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::SurfaceRangeBuilder * SurfaceRangeControl
            (
            );
            /**Returns  the curve range   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricUtilities::CurveRangeBuilder * CurveRangeControl
            (
            );
            /**Returns  a value indicating whether to enable floating info label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool HasInfoLabel
            (
            );
            /**Sets  a value indicating whether to enable floating info label 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasInfoLabel
            (
                bool infoLabel /** infolabel */ 
            );
            /**Returns   a value indicating whether to use defining points. Available only if target is curve with defining points   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: bool UseDefiningPoints
            (
            );
            /**Sets   a value indicating whether to use defining points. Available only if target is curve with defining points   
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetUseDefiningPoints
            (
                bool useDefiningPoints /** usedefiningpoints */ 
            );
            /**Returns  the constraint manager 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::Features::GeometricConstraintDataManager * ConstraintManager
            (
            );
            /**Returns  the reporting per option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::GeometricAnalysis::DeviationGaugeBuilder::ReportingPerTypes ReportingPerType
            (
            );
            /**Sets  the reporting per option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetReportingPerType
            (
                NXOpen::GeometricAnalysis::DeviationGaugeBuilder::ReportingPerTypes reportingPerType /** reportingpertype */ 
            );
            /** Add a PMI label in specified position to represent the deviation value. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void AddPMILabel
            (
                NXOpen::NXObject * snappedObject /** The face or curve which the PMI label pointed to. */
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
