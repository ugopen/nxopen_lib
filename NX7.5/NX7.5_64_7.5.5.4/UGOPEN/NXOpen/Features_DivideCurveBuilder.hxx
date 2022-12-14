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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class DivideCurveBuilder;
    }
    class Direction;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BoundingObjectBuilderList;
    }
    class Plane;
    class Point;
    class SelectCurve;
    class SelectObject;
    class SelectPointList;
    namespace Features
    {
        class _DivideCurveBuilderBuilder;
        class DivideCurveBuilderImpl;
        /**
            Represents a builder for non-associative divide curve operation.
             <br> To create a new instance of this class, use @link Features::BaseFeatureCollection::CreateDivideCurveBuilder Features::BaseFeatureCollection::CreateDivideCurveBuilder@endlink  <br> 
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
        */
        class NXOPENCPPEXPORT  DivideCurveBuilder : public Features::FeatureBuilder
        {
            /** Represents the Divide Curve equal segment method types */
            public: enum EqualSegmentOption
            {
                EqualSegmentOptionEqualParameter/** Equal Parameter */,
                EqualSegmentOptionEqualArcLength/** Equal Arc length */
            };

            /** Represents the Divide Curve Bounding Objects option types */
            public: enum BoundingObjectOption
            {
                BoundingObjectOptionExistingCurve/** Existing Curve */,
                BoundingObjectOptionProjectPoint/** Project Point */,
                BoundingObjectOptionTwoPoints/** Two Points */,
                BoundingObjectOptionPointAndVector/** Point and Vector */,
                BoundingObjectOptionByPlane/** By Plane */
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
            /**Returns  the divide type  <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::Types Type
            (
            );
            /**Sets  the divide type  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetType
            (
                NXOpen::Features::DivideCurveBuilder::Types type /** type */ 
            );
            /**Returns  the select dividing curve  <br> License requirements : None */
            public: NXOpen::SelectCurve * DividingCurve
            (
            );
            /**Returns  the equal segment method  <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::EqualSegmentOption EqualSegmentMethod
            (
            );
            /**Sets  the equal segment method  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEqualSegmentMethod
            (
                NXOpen::Features::DivideCurveBuilder::EqualSegmentOption equalSegmentMethod /** equalsegmentmethod */ 
            );
            /**Returns  the equal parameter segments  <br> License requirements : None */
            public: int EqualParameterSegments
            (
            );
            /**Sets  the equal parameter segments  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEqualParameterSegments
            (
                int equalParameterSegments /** equalparametersegments */ 
            );
            /**Returns  the equal arc length segments  <br> License requirements : None */
            public: int EqualArcLengthSegments
            (
            );
            /**Sets  the equal arc length segments  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetEqualArcLengthSegments
            (
                int equalArcLengthSegments /** equalarclengthsegments */ 
            );
            /**Returns  the bounding object method 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Features::DivideCurveBuilder::BoundingObjectOption BoundingObjectMethod
            (
            );
            /**Sets  the bounding object method 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingObjectMethod
            (
                NXOpen::Features::DivideCurveBuilder::BoundingObjectOption boundingObjectMethod /** boundingobjectmethod */ 
            );
            /**Returns  the existing bounding curve 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::SelectObject * BoundingCurve
            (
            );
            /**Returns  the bounding project point 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Point * BoundingProjectPoint
            (
            );
            /**Sets  the bounding project point 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingProjectPoint
            (
                NXOpen::Point * projectPoint /** projectpoint */ 
            );
            /**Returns  the bounding point1 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Point * BoundingPoint1
            (
            );
            /**Sets  the bounding point1 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingPoint1
            (
                NXOpen::Point * point1 /** point1 */ 
            );
            /**Returns  the bounding point2 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Point * BoundingPoint2
            (
            );
            /**Sets  the bounding point2 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingPoint2
            (
                NXOpen::Point * point2 /** point2 */ 
            );
            /**Returns  the bounding point 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Point * BoundingPoint
            (
            );
            /**Sets  the bounding point 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the bounding vector 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Direction * BoundingVector
            (
            );
            /**Sets  the bounding vector 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingVector
            (
                NXOpen::Direction * vector /** vector */ 
            );
            /**Returns  the bounding plane 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Plane * BoundingPlane
            (
            );
            /**Sets  the bounding plane 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetBoundingPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the intersection reference 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::Point * IntersectionReference
            (
            );
            /**Sets  the intersection reference 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") void SetIntersectionReference
            (
                NXOpen::Point * intersectionReference /** intersectionreference */ 
            );
            /**Returns  the arc length  <br> License requirements : None */
            public: double ArcLength
            (
            );
            /**Sets  the arc length  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetArcLength
            (
                double arcLength /** arclength */ 
            );
            /**Returns  the input arc length direction flag  <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::InputArcLengthDirectionFlag DirectionFlag
            (
            );
            /**Sets  the input arc length direction flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetDirectionFlag
            (
                NXOpen::Features::DivideCurveBuilder::InputArcLengthDirectionFlag directionFlag /** directionflag */ 
            );
            /**Returns  the knot point method  <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::KnotPointOption KnotPointMethod
            (
            );
            /**Sets  the knot point method  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetKnotPointMethod
            (
                NXOpen::Features::DivideCurveBuilder::KnotPointOption knotPointMethod /** knotpointmethod */ 
            );
            /**Returns  the knot point number  <br> License requirements : None */
            public: int KnotPointNumber
            (
            );
            /**Sets  the knot point number  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetKnotPointNumber
            (
                int knotPointNumber /** knotpointnumber */ 
            );
            /**Returns  the knot point  <br> License requirements : None */
            public: NXOpen::SelectPointList * KnotPoint
            (
            );
            /**Returns  the corner method  <br> License requirements : None */
            public: NXOpen::Features::DivideCurveBuilder::CornerOption CornerMethod
            (
            );
            /**Sets  the corner method  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetCornerMethod
            (
                NXOpen::Features::DivideCurveBuilder::CornerOption cornerMethod /** cornermethod */ 
            );
            /**Returns  the corner number  <br> License requirements : None */
            public: int CornerNumber
            (
            );
            /**Sets  the corner number  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
            public: void SetCornerNumber
            (
                int cornerNumber /** cornernumber */ 
            );
            /**Returns  the corner point  <br> License requirements : None */
            public: NXOpen::SelectPointList * CornerPoint
            (
            );
            /**Returns  the Bounding Objects list  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BoundingObjectBuilderList * BoundingObjects
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
