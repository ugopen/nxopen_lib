#ifndef NXOpen_FEATURES_DIVIDECURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DIVIDECURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DivideCurveBuilder.ja
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
#include <NXOpen/Features_DivideCurveBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class DivideCurveBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BoundingObjectBuilderList;
    }
    class SelectCurve;
    class SelectPointList;
    namespace Features
    {
        class _DivideCurveBuilderBuilder;
        class DivideCurveBuilderImpl;
        /**
            Represents a builder for non-associative divide curve operation.
             <br> To create a new instance of this class, use @link Features::BaseFeatureCollection::CreateDivideCurveBuilder  Features::BaseFeatureCollection::CreateDivideCurveBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ArcLength </td> <td> 
         
        1.0 </td> </tr> 

        <tr><td> 
         
        CornerNumber </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        EqualArcLengthSegments </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        EqualParameterSegments </td> <td> 
         
        2 </td> </tr> 

        <tr><td> 
         
        KnotPointNumber </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DivideCurveBuilder : public Features::FeatureBuilder
        {
            /** Represents the Divide Curve equal segment method types */
            public: enum EqualSegmentOption
            {
                EqualSegmentOptionEqualParameter/** Equal Parameter */,
                EqualSegmentOptionEqualArcLength/** Equal Arc length */
            };

            /** Represents the Divide Curve Input Arc length direction flag */
            public: enum InputArcLengthDirectionFlag
            {
                InputArcLengthDirectionFlagStart/** Input Arc length from start */,
                InputArcLengthDirectionFlagEnd/** Input Arc length from end */
            };

            /** Represents the Divide Curve at Knot option types */
            public: enum KnotPointOption
            {
                KnotPointOptionByNumber/** By Number */,
                KnotPointOptionSelectPoint/** Screen Position */,
                KnotPointOptionAllKnotpoints/** All Knotpoints */
            };

            /** Represents the Divide Curve at Corner option types */
            public: enum CornerOption
            {
                CornerOptionByNumber/** By Number */,
                CornerOptionSelectPoint/** Screen Position */,
                CornerOptionAllCornerpoints/** All Cornerpoints */
            };

            /** Represents the Divide Curve types */
            public: enum Types
            {
                TypesEqualSegments/** Equal Segments */,
                TypesByBoundingObjects/** By Bounding Objects */,
                TypesInputArcLengthSegments/** Input Arc Length Segments */,
                TypesAtKnotpoints/** At Knotpoints */,
                TypesAtCorners/** At Corners */
            };

            private: DivideCurveBuilderImpl * m_dividecurvebuilder_impl;
            private: friend class  _DivideCurveBuilderBuilder;
            protected: DivideCurveBuilder();
            public: ~DivideCurveBuilder();
            /**Returns  the divide type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::Types Type
            (
            );
            /**Sets  the divide type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetType
            (
                NXOpen::Features::DivideCurveBuilder::Types type /** type */ 
            );
            /**Returns  the select dividing curve 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCurve * DividingCurve
            (
            );
            /**Returns  the equal segment method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::EqualSegmentOption EqualSegmentMethod
            (
            );
            /**Sets  the equal segment method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEqualSegmentMethod
            (
                NXOpen::Features::DivideCurveBuilder::EqualSegmentOption equalSegmentMethod /** equalsegmentmethod */ 
            );
            /**Returns  the equal parameter segments 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int EqualParameterSegments
            (
            );
            /**Sets  the equal parameter segments 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEqualParameterSegments
            (
                int equalParameterSegments /** equalparametersegments */ 
            );
            /**Returns  the equal arc length segments 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int EqualArcLengthSegments
            (
            );
            /**Sets  the equal arc length segments 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEqualArcLengthSegments
            (
                int equalArcLengthSegments /** equalarclengthsegments */ 
            );
            /**Returns  the arc length 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ArcLength
            (
            );
            /**Sets  the arc length 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetArcLength
            (
                double arcLength /** arclength */ 
            );
            /**Returns  the input arc length direction flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::InputArcLengthDirectionFlag DirectionFlag
            (
            );
            /**Sets  the input arc length direction flag 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetDirectionFlag
            (
                NXOpen::Features::DivideCurveBuilder::InputArcLengthDirectionFlag directionFlag /** directionflag */ 
            );
            /**Returns  the knot point method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::KnotPointOption KnotPointMethod
            (
            );
            /**Sets  the knot point method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetKnotPointMethod
            (
                NXOpen::Features::DivideCurveBuilder::KnotPointOption knotPointMethod /** knotpointmethod */ 
            );
            /**Returns  the knot point number 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int KnotPointNumber
            (
            );
            /**Sets  the knot point number 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetKnotPointNumber
            (
                int knotPointNumber /** knotpointnumber */ 
            );
            /**Returns  the knot point 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * KnotPoint
            (
            );
            /**Returns  the corner method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::CornerOption CornerMethod
            (
            );
            /**Sets  the corner method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetCornerMethod
            (
                NXOpen::Features::DivideCurveBuilder::CornerOption cornerMethod /** cornermethod */ 
            );
            /**Returns  the corner number 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int CornerNumber
            (
            );
            /**Sets  the corner number 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetCornerNumber
            (
                int cornerNumber /** cornernumber */ 
            );
            /**Returns  the corner point 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * CornerPoint
            (
            );
            /**Returns  the Bounding Objects list 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BoundingObjectBuilderList * BoundingObjects
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