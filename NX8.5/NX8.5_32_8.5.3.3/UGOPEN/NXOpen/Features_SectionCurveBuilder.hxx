#ifndef NXOpen_FEATURES_SECTIONCURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SECTIONCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SectionCurveBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SectionCurveBuilder.hxx>
#include <NXOpen/GeometricUtilities_CurveFitData.hxx>
#include <NXOpen/GeometricUtilities_CurveFitJoin.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class SectionCurveBuilder;
    }
    class Direction;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CurveFitData;
    }
    namespace GeometricUtilities
    {
        class CurveFitJoin;
    }
    class Group;
    class ISurface;
    class Plane;
    class Point;
    class SelectObject;
    class SelectObjectList;
    namespace Features
    {
        class _SectionCurveBuilderBuilder;
        class SectionCurveBuilderImpl;
        /**
            Represents a @link Features::SectionCurve Features::SectionCurve@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateSectionCurveBuilder  Features::FeatureCollection::CreateSectionCurveBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        CurveFitData.CurveJoinMethod </td> <td> 
         
        No </td> </tr> 

        <tr><td> 
         
        CurveFitData.Degree </td> <td> 
         
        7 </td> </tr> 

        <tr><td> 
         
        CurveFitData.FitMethod </td> <td> 
         
        DegreeAndSegments </td> </tr> 

        <tr><td> 
         
        CurveFitData.IsAdvancedFit </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFitData.IsAlignShape </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CurveFitData.MaximumDegree </td> <td> 
         
        7 </td> </tr> 

        <tr><td> 
         
        CurveFitData.MaximumSegments </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CurveFitData.MinimumDegree </td> <td> 
         
        5 </td> </tr> 

        <tr><td> 
         
        CurveFitData.Segments </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CurveFitJoinOptions.CurveFitOptions.FitOption </td> <td> 
         
        Cubic </td> </tr> 

        <tr><td> 
         
        CurveFitJoinOptions.CurveFitOptions.MaximumDegree </td> <td> 
         
        7 </td> </tr> 

        <tr><td> 
         
        CurveFitJoinOptions.CurveFitOptions.MaximumSegments </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        EndAngle </td> <td> 
         
        20.0 </td> </tr> 

        <tr><td> 
         
        EndDistance </td> <td> 
         
        10.0 (millimeters part), 0.5 (inches part) </td> </tr> 

        <tr><td> 
         
        EndPercentage </td> <td> 
         
        100.0 </td> </tr> 

        <tr><td> 
         
        GroupObjects </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        Increment </td> <td> 
         
        5.0 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        NumberOfCopies </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        OutputPoints </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        Ratio </td> <td> 
         
        1.0 </td> </tr> 

        <tr><td> 
         
        SampleDistance </td> <td> 
         
        1.0 (millimeters part), 0.04 (inches part) </td> </tr> 

        <tr><td> 
         
        SpacingAlongCurveType </td> <td> 
         
        EqualArcLength </td> </tr> 

        <tr><td> 
         
        StartAngle </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        StartDistance </td> <td> 
         
        0.0 (millimeters part), 0.0 (inches part) </td> </tr> 

        <tr><td> 
         
        StartPercentage </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        StepAngle </td> <td> 
         
        10.0 </td> </tr> 

        <tr><td> 
         
        StepDistance </td> <td> 
         
        5.0 (millimeters part), 0.25 (inches part) </td> </tr> 

        <tr><td> 
         
        Type </td> <td> 
         
        Selected </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  SectionCurveBuilder : public Features::FeatureBuilder
        {
            /** Represents section plane type. */
            public: enum PlaneType
            {
                PlaneTypeSelected/** Planes are selected (not specified by
                                                                                    one of the following methods)  */,
                PlaneTypeParallel/** Set of planes parallel to a base plane  */,
                PlaneTypeRadial/** Set of planes radiating from a base plane  */,
                PlaneTypePerpendicularToCurve/** Set of planes perpendicular to a curve */
            };

            /** Represents spacing type. */
            public: enum SpacingType
            {
                SpacingTypeEqualArcLength/**  Equal arclength spacing  */,
                SpacingTypeEqualParameterSpacing/**  Equal parameter spacing  */,
                SpacingTypeGeometricProgressionSpacing/**  Geometric progression spacing  */,
                SpacingTypeChordalToleranceSpacing/**  Chordal tolerance spacing  */,
                SpacingTypeIncrementalArclengthSpacing/**  Incremental arclength spacing  */
            };

            private: SectionCurveBuilderImpl * m_sectioncurvebuilder_impl;
            private: friend class  _SectionCurveBuilderBuilder;
            protected: SectionCurveBuilder();
            public: ~SectionCurveBuilder();
            /**Returns  the type of the section curve builder
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionCurveBuilder::PlaneType Type
            (
            );
            /**Sets  the type of the section curve builder
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::SectionCurveBuilder::PlaneType type /** type */ 
            );
            /**Returns  the type of spacing
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SectionCurveBuilder::SpacingType SpacingAlongCurveType
            (
            );
            /**Sets  the type of spacing
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSpacingAlongCurveType
            (
                NXOpen::Features::SectionCurveBuilder::SpacingType spacingAlongCurve /** spacing along curve */ 
            );
            /**Returns  the selected objects 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObjectList * ObjectsToSection
            (
            );
            /**Returns  the selected planes 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObjectList * SectionPlanes
            (
            );
            /**Returns  the plane 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * SectionPlane
            (
            );
            /**Sets  the plane 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSectionPlane
            (
                NXOpen::Plane * sectionPlane /** section plane */ 
            );
            /**Returns  the base plane 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ISurface * BasePlane
            (
            );
            /**Sets  the base plane 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetBasePlane
            (
                NXOpen::ISurface * basePlane /** base plane */ 
            );
            /**Returns  the vector for radial plane type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * RadialPlaneVector
            (
            );
            /**Sets  the vector for radial plane type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRadialPlaneVector
            (
                NXOpen::Direction * radialPlaneVector /** radial plane vector */ 
            );
            /**Returns  the point for radial plane type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * RadialPlanePoint
            (
            );
            /**Sets  the point for radial plane type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRadialPlanePoint
            (
                NXOpen::Point * radialPlanePoint /** radial plane point */ 
            );
            /**Returns  the curve for perpendicular to curve type
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObject * CurveForPerpendicularPlane
            (
            );
            /**Returns  the the start distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double StartDistance
            (
            );
            /**Sets  the the start distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartDistance
            (
                double startDistance /** start distance */ 
            );
            /**Returns  the the end distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double EndDistance
            (
            );
            /**Sets  the the end distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndDistance
            (
                double endDistance /** end distance */ 
            );
            /**Returns  the step distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double StepDistance
            (
            );
            /**Sets  the step distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStepDistance
            (
                double stepDistance /** step distance */ 
            );
            /**Returns  the start angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double StartAngle
            (
            );
            /**Sets  the start angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartAngle
            (
                double startAngle /** start angle */ 
            );
            /**Returns  the end angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double EndAngle
            (
            );
            /**Sets  the end angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndAngle
            (
                double endAngle /** end angle */ 
            );
            /**Returns  the step angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double StepAngle
            (
            );
            /**Sets  the step angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStepAngle
            (
                double stepAngle /** step angle */ 
            );
            /**Returns  the sample distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double SampleDistance
            (
            );
            /**Sets  the sample distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSampleDistance
            (
                double sampleDistance /** sample distance */ 
            );
            /**Returns  the start percentage. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double StartPercentage
            (
            );
            /**Sets  the start percentage. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetStartPercentage
            (
                double startPercentage /** start percentage */ 
            );
            /**Returns  the end percentage. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double EndPercentage
            (
            );
            /**Sets  the end percentage. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetEndPercentage
            (
                double endPercentage /** end percentage */ 
            );
            /**Returns  the number of copies 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int NumberOfCopies
            (
            );
            /**Sets  the number of copies 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetNumberOfCopies
            (
                int numberOfCopies /** numberofcopies */ 
            );
            /**Returns  the ratio 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Ratio
            (
            );
            /**Sets  the ratio 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRatio
            (
                double ratio /** ratio */ 
            );
            /**Returns  the increment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Increment
            (
            );
            /**Sets  the increment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetIncrement
            (
                double increment /** increment */ 
            );
            /**Returns  the tolerance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the chordal tolerance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ChordalTolerance
            (
            );
            /**Sets  the chordal tolerance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetChordalTolerance
            (
                double chordalTolerance /** chordal tolerance */ 
            );
            /**Returns  the associativity 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associativity 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the grouping 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool GroupObjects
            (
            );
            /**Sets  the grouping 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetGroupObjects
            (
                bool groupObjects /** group objects */ 
            );
            /**Returns  the output points 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputPoints
            (
            );
            /**Sets  the output points 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOutputPoints
            (
                bool outputPoints /** output points */ 
            );
            /**Returns   the curve fit join option
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveFitJoin * CurveFitJoinOptions
            (
            );
            /** Gets the output groups for non-associated output curve @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Group *> GetOutputGroups
            (
            );
            /**Returns  the curve fit settings 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveFitData * CurveFitData
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
