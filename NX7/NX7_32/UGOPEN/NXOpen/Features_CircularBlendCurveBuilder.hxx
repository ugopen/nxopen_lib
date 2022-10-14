#ifndef NXOpen_FEATURES_CIRCULARBLENDCURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_CIRCULARBLENDCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CircularBlendCurveBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_CircularBlendCurveBuilder.hxx>
#include <NXOpen/GeometricUtilities_CurveFitOptions.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class CircularBlendCurveBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CurveFitOptions;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class Section;
    namespace Features
    {
        class _CircularBlendCurveBuilderBuilder;
        /**
            Represents a @link Features::CircularBlendCurve Features::CircularBlendCurve@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateCircularBlendCurveBuilder Features::FeatureCollection::CreateCircularBlendCurveBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        CurveFitMethod.FitOption </td> <td> 
         
        Cubic </td> </tr> 

        <tr><td> 
         
        CurveFitMethod.MaximumDegree </td> <td> 
         
        7 </td> </tr> 

        <tr><td> 
         
        CurveFitMethod.MaximumSegments </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CylinderRadius.Value </td> <td> 
         
        0.0 (millimeters part), 0.0 (inches part) </td> </tr> 

        <tr><td> 
         
        DirectionOption </td> <td> 
         
        BestFit </td> </tr> 

        <tr><td> 
         
        PointArclength.Expression.Value </td> <td> 
         
        0.0 (millimeters part), 0.0 (inches part) </td> </tr> 

        <tr><td> 
         
        RadiusOption </td> <td> 
         
        PointOnFirstCurve </td> </tr> 

        <tr><td> 
         
        ShapeControlFirstCurve </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        ShapeControlSecondCurve </td> <td> 
         
        2.0 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT CircularBlendCurveBuilder : public Features::FeatureBuilder
        {
            /** Represents the cylinder direction options */
            public: enum CylinderDirectionOption
            {
                CylinderDirectionOptionBestFit/** Best fit method*/,
                CylinderDirectionOptionVariable/** Variable method*/,
                CylinderDirectionOptionVector/** Specify vector method*/,
                CylinderDirectionOptionCurrentView/** Current view method*/
            };

            /** Represents the cylinder radius options */
            public: enum CylinderRadiusOption
            {
                CylinderRadiusOptionPointOnFirstCurve/** Radius by point on first curve*/,
                CylinderRadiusOptionPointOnSecondCurve/** Radius by point on second curve*/,
                CylinderRadiusOptionValue/** Radius by value*/
            };

            private: friend class  _CircularBlendCurveBuilderBuilder;
            protected: CircularBlendCurveBuilder();
            /**Returns  the first curve chain  <br> License requirements : None */
            public: NXOpen::Section * FirstCurve
            (
            );
            /**Returns  the second curve chain <br> License requirements : None */
            public: NXOpen::Section * SecondCurve
            (
            );
            /**Returns  the cylinder direction option as @link Features::CircularBlendCurveBuilder::CylinderDirectionOption Features::CircularBlendCurveBuilder::CylinderDirectionOption@endlink  <br> License requirements : None */
            public: NXOpen::Features::CircularBlendCurveBuilder::CylinderDirectionOption DirectionOption
            (
            );
            /**Sets  the cylinder direction option as @link Features::CircularBlendCurveBuilder::CylinderDirectionOption Features::CircularBlendCurveBuilder::CylinderDirectionOption@endlink  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirectionOption
            (
                NXOpen::Features::CircularBlendCurveBuilder::CylinderDirectionOption directionOption /** directionoption */ 
            );
            /**Returns  the vector for cylinder direction, if @link Features::CircularBlendCurveBuilder::CylinderDirectionOption Features::CircularBlendCurveBuilder::CylinderDirectionOption@endlink  is @link Features::CircularBlendCurveBuilder::CylinderDirectionOptionVector Features::CircularBlendCurveBuilder::CylinderDirectionOptionVector@endlink   <br> License requirements : None */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector for cylinder direction, if @link Features::CircularBlendCurveBuilder::CylinderDirectionOption Features::CircularBlendCurveBuilder::CylinderDirectionOption@endlink  is @link Features::CircularBlendCurveBuilder::CylinderDirectionOptionVector Features::CircularBlendCurveBuilder::CylinderDirectionOptionVector@endlink   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetVector
            (
                NXOpen::Direction * vector /** vector */ 
            );
            /**Returns  the cylinder radius option as @link Features::CircularBlendCurveBuilder::CylinderRadiusOption Features::CircularBlendCurveBuilder::CylinderRadiusOption@endlink  <br> License requirements : None */
            public: NXOpen::Features::CircularBlendCurveBuilder::CylinderRadiusOption RadiusOption
            (
            );
            /**Sets  the cylinder radius option as @link Features::CircularBlendCurveBuilder::CylinderRadiusOption Features::CircularBlendCurveBuilder::CylinderRadiusOption@endlink  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetRadiusOption
            (
                NXOpen::Features::CircularBlendCurveBuilder::CylinderRadiusOption radiusOption /** radiusoption */ 
            );
            /**Returns  the cylinder radius as @link Expression Expression@endlink , if  @link Features::CircularBlendCurveBuilder::CylinderRadiusOption Features::CircularBlendCurveBuilder::CylinderRadiusOption@endlink  is @link Features::CircularBlendCurveBuilder::CylinderRadiusOptionValue Features::CircularBlendCurveBuilder::CylinderRadiusOptionValue@endlink  <br> License requirements : None */
            public: NXOpen::Expression * CylinderRadius
            (
            );
            /**Returns  the location of the point on curve as arclength or %arclength, if  @link Features::CircularBlendCurveBuilder::CylinderRadiusOption Features::CircularBlendCurveBuilder::CylinderRadiusOption@endlink  is @link Features::CircularBlendCurveBuilder::CylinderRadiusOptionPointOnFirstCurve Features::CircularBlendCurveBuilder::CylinderRadiusOptionPointOnFirstCurve@endlink  or @link Features::CircularBlendCurveBuilder::CylinderRadiusOptionPointOnSecondCurve Features::CircularBlendCurveBuilder::CylinderRadiusOptionPointOnSecondCurve@endlink  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * PointArclength
            (
            );
            /**Returns  the shape control for  first curve, specifies how quickly the circular blend curve deviates from the first curve. The lower the number, the quicker the deviation.  <br> License requirements : None */
            public: double ShapeControlFirstCurve
            (
            );
            /**Sets  the shape control for  first curve, specifies how quickly the circular blend curve deviates from the first curve. The lower the number, the quicker the deviation.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShapeControlFirstCurve
            (
                double shapeControlCurve1 /** shapecontrolcurve1 */ 
            );
            /**Returns  the shape control for  second curve, specifies how quickly the circular blend curve deviates from the second curve. The lower the number, the quicker the deviation.  <br> License requirements : None */
            public: double ShapeControlSecondCurve
            (
            );
            /**Sets  the shape control for  second curve, specifies how quickly the circular blend curve deviates from the second curve. The lower the number, the quicker the deviation.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShapeControlSecondCurve
            (
                double shapeControlCurve2 /** shapecontrolcurve2 */ 
            );
            /**Returns  whether to create the associative output or non associative output <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  whether to create the associative output or non associative output <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /** Complements the circular blend curve  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void ComplementArc
            (
            );
            /**Returns  the curve fit method as @link GeometricUtilities::CurveFitOptions GeometricUtilities::CurveFitOptions@endlink   <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveFitOptions * CurveFitMethod
            (
            );
            /**Returns  the distance tolerance  <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /** Evaluates the circular blend curve <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void Evaluate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif