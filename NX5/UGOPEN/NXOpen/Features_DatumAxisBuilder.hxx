#ifndef NXOpen_FEATURES_DATUMAXISBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DATUMAXISBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DatumAxisBuilder.ja
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
#include <NXOpen/Features_DatumBuilder.hxx>
#include <NXOpen/Features_DatumAxisBuilder.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/type.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class DatumAxisBuilder;
    }
    class Direction;
    class DisplayableObject;
    namespace Features
    {
        class DatumBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class ICurve;
    class NXObject;
    class Point;
    class SelectCurve;
    class SelectNXObject;
    class SelectNXObjectList;
    namespace Features
    {
        class _DatumAxisBuilderBuilder;
        /** Represents a datum axis feature builder. Provides methods to create datum axis thru two points, 
        point and direction and point on curve. Also provides generic method for creation of datum axis feature
         <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateDatumAxisBuilder Features::FeatureCollection::CreateDatumAxisBuilder@endlink  <br> */
        class NXOPENCPPEXPORT DatumAxisBuilder : public Features::DatumBuilder
        {
            /** Specifies the fixed type datum axis going thru only one specific axis or thru all axes. */
            public: enum FixedType
            {
                FixedTypeAll/** all */ ,
                FixedTypeX/** x */ ,
                FixedTypeY/** y */ ,
                FixedTypeZ/** z */ 
            };

            /** Specifies the distance on the curve as absolute distance or relative distance as percentage */
            public: enum CurveOption
            {
                CurveOptionDistance/** Absolute distance */,
                CurveOptionPercent/** Relative distance as percentage */
            };

            /** Specifies the alternate solution for datum axis using point on curve method only*/
            public: enum AlternateSolution
            {
                AlternateSolutionUndefined/** undefined */ ,
                AlternateSolutionTangent/** tangent */ ,
                AlternateSolutionNormal/** normal */ ,
                AlternateSolutionBinormal/** binormal */ ,
                AlternateSolutionOppositeTangent/** opposite tangent */ ,
                AlternateSolutionOppositeNormal/** opposite normal */ ,
                AlternateSolutionOppositeBinormal/** opposite binormal */ ,
                AlternateSolutionProject/** This direction is calculated by projecting a point selected along a curve
                																	    to a line, a datum axis, an edge of a solid, a planar face or a datum plane 
                																	*/
            };

            /** Specifies different constraint types for selected geometries */
            public: enum ConstraintType
            {
                ConstraintTypeUndefined/** undefined */ ,
                ConstraintTypeCoincident/** coincident */ ,
                ConstraintTypeParallel/** parallel */ ,
                ConstraintTypePerpendicular/** perpendicular */ ,
                ConstraintTypeCenter/** center */ ,
                ConstraintTypeTangent/** tangent */ ,
                ConstraintTypeDistance/** distance */ ,
                ConstraintTypeAngle/** angle */ ,
                ConstraintTypeFrenet/** frenet */ 
            };

            /** Specifies points for which arclength is to be used. Percentage of arclength is used for points for which 
            	arclength option is not selected. Specified for creation of datum axis using thru two points method. */
            public: enum UseArcLength
            {
                UseArcLengthNoPoint/** All points use percentage of arclength */,
                UseArcLengthFirstPoint/** Only first point uses arclength */,
                UseArcLengthSecondPoint/** Only second point uses arclength */,
                UseArcLengthAllPoints/** Both points use arclength */
            };

            /** Two available direction orientations that the user can choose when the Datum Axis type is Point and Direction */
            public: enum DirectionOrientations
            {
                DirectionOrientationsParallelToVector/** parallel to vector */ ,
                DirectionOrientationsPerpendicularToVector/** perpendicular to vector */ 
            };

            /** Available orientations that the user can choose when the Datum Axis type is On Curve Vector */
            public: enum CurveOrientations
            {
                CurveOrientationsTangent/** tangent */ ,
                CurveOrientationsNormal/** normal */ ,
                CurveOrientationsBinormal/** binormal */ ,
                CurveOrientationsPerpendicularToObject/** perpendicular to object */ ,
                CurveOrientationsParallelToObject/** parallel to object */ 
            };

            /** New Datum Axis types in NX5 */
            public: enum Types
            {
                TypesInferred/** inferred */ ,
                TypesIntersection/** intersection */ ,
                TypesCurveOrFaceAxis/** curve or face axis */ ,
                TypesOnCurveVector/** on curve vector */ ,
                TypesXcAxis/** xc axis */ ,
                TypesYcAxis/** yc axis */ ,
                TypesZcAxis/** zc axis */ ,
                TypesPointAndDir/** point and dir */ ,
                TypesTwoPoints/** two points */ ,
                TypesFixed/** fixed */ 
            };

            private: friend class  _DatumAxisBuilderBuilder;
            protected: DatumAxisBuilder();
            /**Returns   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool ReverseDirection
            (
            );
            /**Sets   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseDirection
            (
                bool reverse_direction /** reverse direction */ 
            );
            /**  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointAndDirection
            (
                NXOpen::Point * point /** point */ ,
                NXOpen::Direction * direction /** direction */ 
            );
            /** Sets two points  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTwoPoints
            (
                NXOpen::Point * point1 /** point1 */ ,
                NXOpen::Point * point2 /** point2 */ ,
                NXOpen::Features::DatumAxisBuilder::UseArcLength use_arc_length /** Specify points which use arclength instead of percentage of arclength */
            );
            /** Sets curve or edge and arc length  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arc_length /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumAxisBuilder::AlternateSolution alternate_solution /** Alternate solution */,
                NXOpen::Features::DatumAxisBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** Curve or Edge object */
            );
            /** Sets Curve or Edge object and arc length with an extra geometry in picture 
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arc_length /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumAxisBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** Curve or Edge object */,
                NXOpen::NXObject * second_geometry /** Second geometric object */
            );
            /** Sets Curve or Edge object and arc length with an extra geometry in picture 
             @deprecated Deprecated in NX4 <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arc_length /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumAxisBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::NXObject * second_geometry /** Second Geometric object */,
                NXOpen::ICurve * curve /** Curve or Edge object */
            );
            /** Sets Curve or Edge object and arc length with an extra geometry in picture  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arc_length /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumAxisBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** Curve or Edge object */,
                NXOpen::DisplayableObject * second_geometry /** Second geometric object */
            );
            /** Sets Curve or Edge object and arc length with an extra geometry in picture  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arc_length /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumAxisBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::DisplayableObject * second_geometry /** Second Geometric object */,
                NXOpen::ICurve * curve /** Curve or Edge object */
            );
            /** Sets two different geometric objects. Possible combinations are:
                <ul>
                    <li> If first constrain is Through Point, then the second contraint can be:
                        <ul>
                            <li>Solid Body Vertex (endpoint) </li>        
                            <li>Edge Midpoint </li>
                        </ul>
                    </li>
                    <li>If first constrain is Intersection of Plane, then the second contraint can be:
                        <ul>  
                            <li>Through the straight edge formed by the intersection of two planes </li>
                        </ul>
                    </li>
                    <li>If first constrain is Through Curve, then the second contraint can be:
                        <ul>       
                            <li>Used with Through Point constraint and along a curve </li>
                        </ul>
                    </li>
                    <li>If first constrain is Perpendicular to object, then the second contraint can be:
                        <ul> 
                            <li>Through Curve and Through Point perpendicular to lines, linear edge, 
                                         datum planes, datum axis, or planar faces </li>
                        </ul>
                    </li>        
                </ul>                              
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetGeometryAndConstraints
            (
                NXOpen::DisplayableObject * geometry_1 /** First geometric object */,
                NXOpen::Features::DatumAxisBuilder::ConstraintType geometry_constraint_type_1 /** Constraint type of first geometry */,
                int constraint_attribute_1 /** Constraint attribute value of first geometry VRH alternate_solution_only - only for point on curve*/,
                double constraint_value_1 /** Constraint value parameter of first geometry */,
                const NXString & constraint_1 /** Constraint attached with first geometric object. 
                                                                                              Set to "0.0" in case value is not specified    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::DisplayableObject * geometry_2 /** Second geometric object */,
                NXOpen::Features::DatumAxisBuilder::ConstraintType geometry_constraint_type_2 /** Constraint type of second geometry */,
                int constraint_attribute_2 /** Constraint attribute value of second geometry */,
                double constraint_value_2 /** Constraint value parameter of second geometry */,
                const NXString & constraint_2 /** Constraint attached with second geometric object. 
                                                                                              Set to "0.0" in case value is not specified    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Sense direction /** Flag to specify datum axis direction */
            );
            /** Sets type of fixed datum axis  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFixedDatumAxis
            (
                NXOpen::Features::DatumAxisBuilder::FixedType type /** Indicates fixed datum axis type */
            );
            /**Returns  the Datum Axis type  <br> License requirements : None */
            public: NXOpen::Features::DatumAxisBuilder::Types Type
            (
            );
            /**Sets  the Datum Axis type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::DatumAxisBuilder::Types type /** type */ 
            );
            /**Returns  the objects to define Datum Axis. This is used only if the Datum Axis type is 
                        @link TypesInferred TypesInferred@endlink 
                     <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * Objects
            (
            );
            /**Returns  the curve. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink  
                     <br> License requirements : None */
            public: NXOpen::SelectCurve * Curve
            (
            );
            /**Returns  the point. This is used only if the Datum Axis type is 
                        @link TypesPointAndDir TypesPointAndDir@endlink 
                     <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the point. This is used only if the Datum Axis type is 
                        @link TypesPointAndDir TypesPointAndDir@endlink 
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPoint
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the first point. This is used only if the Datum Axis type is 
                        @link TypesTwoPoints TypesTwoPoints@endlink  
                     <br> License requirements : None */
            public: NXOpen::Point * Point1
            (
            );
            /**Sets  the first point. This is used only if the Datum Axis type is 
                        @link TypesTwoPoints TypesTwoPoints@endlink  
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPoint1
            (
                NXOpen::Point * point1 /** point1 */ 
            );
            /**Returns  the second point. This is used only if the Datum Axis type is 
                        @link TypesTwoPoints TypesTwoPoints@endlink   
                     <br> License requirements : None */
            public: NXOpen::Point * Point2
            (
            );
            /**Sets  the second point. This is used only if the Datum Axis type is 
                        @link TypesTwoPoints TypesTwoPoints@endlink   
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPoint2
            (
                NXOpen::Point * point2 /** point2 */ 
            );
            /**Returns  the first object (i.e. a planar face or datum plane). This is used only if the Datum Axis type is 
                        @link TypesIntersection TypesIntersection@endlink 
                     <br> License requirements : None */
            public: NXOpen::SelectNXObject * Object1
            (
            );
            /**Returns  the second object (i.e. a planar face or datum plane). This is used only if the Datum Axis type is 
                        @link TypesIntersection TypesIntersection@endlink   
                     <br> License requirements : None */
            public: NXOpen::SelectNXObject * Object2
            (
            );
            /**Returns  the curve or face . This is used only if the Datum Axis type is 
                        @link TypesCurveOrFaceAxis TypesCurveOrFaceAxis@endlink  
                     <br> License requirements : None */
            public: NXOpen::SelectNXObject * CurveOrFace
            (
            );
            /**Returns  the direction orientation. This is used only if the Datum Axis type is 
                        @link TypesPointAndDir TypesPointAndDir@endlink   
                     <br> License requirements : None */
            public: NXOpen::Features::DatumAxisBuilder::DirectionOrientations DirectionOrientation
            (
            );
            /**Sets  the direction orientation. This is used only if the Datum Axis type is 
                        @link TypesPointAndDir TypesPointAndDir@endlink   
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirectionOrientation
            (
                NXOpen::Features::DatumAxisBuilder::DirectionOrientations directionOrientation /** directionorientation */ 
            );
            /**Returns  the vector. This is used only if the Datum Axis type is 
                        @link TypesPointAndDir TypesPointAndDir@endlink  
                     <br> License requirements : None */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector. This is used only if the Datum Axis type is 
                        @link TypesPointAndDir TypesPointAndDir@endlink  
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetVector
            (
                NXOpen::Direction * vector /** vector */ 
            );
            /**Returns  the arc length. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink   
                     <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * ArcLength
            (
            );
            /**Returns  the orientation of vector on a curve. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink   
                     <br> License requirements : None */
            public: NXOpen::Features::DatumAxisBuilder::CurveOrientations CurveOrientation
            (
            );
            /**Sets  the orientation of vector on a curve. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink   
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCurveOrientation
            (
                NXOpen::Features::DatumAxisBuilder::CurveOrientations curveOrientation /** curveorientation */ 
            );
            /**Returns  the alternate solution type. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink   
                     <br> License requirements : None */
            public: NXOpen::Features::DatumAxisBuilder::AlternateSolution AlternateSolutionType
            (
            );
            /**Sets  the alternate solution type. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink   
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAlternateSolutionType
            (
                NXOpen::Features::DatumAxisBuilder::AlternateSolution alternate_solution_type /** alternate solution type */ 
            );
            /**Returns  the orientation object. This is used only if the Datum Axis type is 
                        @link TypesOnCurveVector TypesOnCurveVector@endlink  
                     <br> License requirements : None */
            public: NXOpen::SelectNXObject * OrientationObject
            (
            );
            /**Returns  the datum axis direction. If true, the Datum Axis direction is reversed  <br> License requirements : None */
            public: bool IsAxisReversed
            (
            );
            /**Sets  the datum axis direction. If true, the Datum Axis direction is reversed  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAxisReversed
            (
                bool isAxisReversed /** isaxisreversed */ 
            );
            /**Returns  the associativity. If true, the Datum Axis is associative  <br> License requirements : None */
            public: bool IsAssociative
            (
            );
            /**Sets  the associativity. If true, the Datum Axis is associative  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool isAssociative /** isassociative */ 
            );
            /**Returns  the resized distance for the end point. If the value is 0.0, then this datum axis is not resized at end point  <br> License requirements : None */
            public: double ResizedEndDistance
            (
            );
            /**Sets  the resized distance for the end point. If the value is 0.0, then this datum axis is not resized at end point  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetResizedEndDistance
            (
                double resizedEndDistance /** resizedenddistance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif