#ifndef NXOpen_FEATURES_DATUMPLANEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DATUMPLANEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DatumPlaneBuilder.ja
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
#include <NXOpen/Features_DatumBuilder.hxx>
#include <NXOpen/ugmath.hxx>
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
        class DatumPlaneBuilder;
    }
    class DatumPlane;
    class Direction;
    class DisplayableObject;
    class Face;
    namespace Features
    {
        class DatumBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    class ICurve;
    class Plane;
    class Point;
    namespace Features
    {
        class _DatumPlaneBuilderBuilder;
        class DatumPlaneBuilderImpl;
        /** Represents a datum plane feature builder. Provides methods to create datum planes 
        thru three points, point and direction and point on curve  <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateDatumPlaneBuilder  Features::FeatureCollection::CreateDatumPlaneBuilder @endlink  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DatumPlaneBuilder : public Features::DatumBuilder
        {
            /** Specifies the fixed type datum plane going thru only one specific plane or thru all planes */
            public: enum FixedType
            {
                FixedTypeAll/** Fixed datum plane thru all planes */,
                FixedTypeXy/** Fixed datum plane thru XY plane */,
                FixedTypeYz/** Fixed datum plane thru YZ plane */,
                FixedTypeZx/** Fixed datum plane thru ZX plane */
            };

            /** Specifies points for which arclength is to be used. Percentage of arclength is used for points for which 
            arclength option is not selected. Specified for creation of datum plane using thru three points method. */
            public: enum UseArcLength
            {
                UseArcLengthNoPoint/** All points use percentage of arclength */,
                UseArcLengthFirstPoint/** Only first point uses arclength */,
                UseArcLengthSecondPoint/** Only second point uses arclength */,
                UseArcLengthThirdPoint/** Only third point uses arclength */,
                UseArcLengthFirstAndSecondPoint/** Only first and second point use arclength */,
                UseArcLengthFirstAndThirdPoint/** Only first and third point use arclength */,
                UseArcLengthSecondAndThirdPoint/** Only second and third point use arclength */,
                UseArcLengthAllPoints/** All points use arclength */
            };

            /** Specifies the distance on the curve as absolute distance or relative distance as percentage */
            public: enum CurveOption
            {
                CurveOptionDistance/** Absolute distance. */,
                CurveOptionPercent/** Relative distance as percentage. */
            };

            /** Specifies the alternate solution for a datum plane using point on curve method */
            public: enum AlternateSolution
            {
                AlternateSolutionTangent/** Indicates the datum plane as tangent to curve */,
                AlternateSolutionNormal/** Datum plane at normal to curve */,
                AlternateSolutionBinormal/** Datum plane at binormal to curve */,
                AlternateSolutionOppositeTangent/** Datum plane at opposite to tangent to curve */,
                AlternateSolutionOppositeNormal/** Datum plane at opposite to normal to curve */,
                AlternateSolutionOppositeBinormal/** Datum plane at opposite to binormal to curve  */,
                AlternateSolutionProject/** This direction is calculated by projecting a point selected along a curve
                                                                                 to a line, a datum axis, an edge of a solid, a planar face or a datum plane 
                                                                                 */,
                AlternateSolutionProjectView/** Datum plane direction is calculated during creation based on the view plane.
                                                                                 The datum plane normal is projected onto the view plane during creation time.
                                                                                 The datum plane normal is maintained constant thereafter
                                                                                 */
            };

            /** Specifies different constraint types of selected geometries */
            public: enum ConstraintType
            {
                ConstraintTypeUndefined/** Not defined */,
                ConstraintTypeCoincident/** Coincident constraint*/,
                ConstraintTypeParallel/** Parallel constraint */,
                ConstraintTypePerpendicular/** Perpendicular constraint */,
                ConstraintTypeCenter/** Center constraint */,
                ConstraintTypeTangent/** Tangent constraint  */,
                ConstraintTypeDistance/** Distance constraint */,
                ConstraintTypeAngle/** Angle constraint  */,
                ConstraintTypeFrenet/** Frenet constraint */
            };

            private: DatumPlaneBuilderImpl * m_datumplanebuilder_impl;
            private: friend class  _DatumPlaneBuilderBuilder;
            protected: DatumPlaneBuilder();
            public: ~DatumPlaneBuilder();
            /** Sets point and direction 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointAndDirection
            (
                NXOpen::Point * point /** Point */,
                NXOpen::Direction * direction /** Direction */
            );
            /** Sets curve or edge and arc length 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arcLength /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumPlaneBuilder::AlternateSolution alternateSolution /** Alternate solution */,
                NXOpen::Features::DatumPlaneBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** curve or edge */
            );
            /** Sets curve or edge and arc length 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetPointOnCurve
            (
                double arcLength /** Arc length */,
                const char * constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumPlaneBuilder::AlternateSolution alternateSolution /** Alternate solution */,
                NXOpen::Features::DatumPlaneBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** curve or edge */
            );
            /** Sets curve or edge and arc length 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arcLength /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumPlaneBuilder::AlternateSolution alternateSolution /** Alternate solution */,
                NXOpen::Features::DatumPlaneBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** Curve or edge */,
                NXOpen::Direction * direction /** Direction */
            );
            /** Sets curve or edge and arc length 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetPointOnCurve
            (
                double arcLength /** Arc length */,
                const char * constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumPlaneBuilder::AlternateSolution alternateSolution /** Alternate solution */,
                NXOpen::Features::DatumPlaneBuilder::CurveOption option /** Absolute distance or relative distance */,
                NXOpen::ICurve * curve /** Curve or edge */,
                NXOpen::Direction * direction /** Direction */
            );
            /** Sets curve or edge object and arc length with other geometry selected. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPointOnCurve
            (
                double arcLength /** Arc length */,
                const NXString & constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumPlaneBuilder::CurveOption option /** Whether the absolute distance has been selected or relative */,
                NXOpen::ICurve * curve /** Curve or Edge object already created */,
                NXOpen::DisplayableObject * secondGeometry /** Second geometric object */
            );
            /** Sets curve or edge object and arc length with other geometry selected. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetPointOnCurve
            (
                double arcLength /** Arc length */,
                const char * constraint /** Constraint expression. Usually same as arc_length   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::Features::DatumPlaneBuilder::CurveOption option /** Whether the absolute distance has been selected or relative */,
                NXOpen::ICurve * curve /** Curve or Edge object already created */,
                NXOpen::DisplayableObject * secondGeometry /** Second geometric object */
            );
            /** Sets three different points. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetThreePoints
            (
                NXOpen::Point * point1 /** First point */,
                NXOpen::Point * point2 /** Second point */,
                NXOpen::Point * point3 /** Third point */,
                NXOpen::Features::DatumPlaneBuilder::UseArcLength useArcLength /** Specify points which use arclength instead of percentage of arclength */
            );
            /** Sets one face object and offset 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFaceAndOffset
            (
                NXOpen::Face * face /** Face object */,
                double offsetValue /** Offset double parameter */,
                const NXString & expression /** Offset string parameter   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets one face object and offset 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetFaceAndOffset
            (
                NXOpen::Face * face /** Face object */,
                double offsetValue /** Offset double parameter */,
                const char * expression /** Offset string parameter   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets corner points to builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCornerPoints
            (
                const NXOpen::Point3d & corner1 /** corner1 */ ,
                const NXOpen::Point3d & corner2 /** corner2 */ ,
                const NXOpen::Point3d & corner3 /** corner3 */ ,
                const NXOpen::Point3d & corner4 /** corner4 */ 
            );
            /** Sets two different geometric objects. Possible combinations are: 
                 <ul>
                 <li> If first constrain is Through Datum Axis, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis Through Point Angle to Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Solid Edge and Linear Geometry, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis Through Point Angle to Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Face Axis, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis Through Point Angle to Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Point, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Parallel to Plane Perpendicular to Curve 
                                 Parallel to Surface's Tangent Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Angle to Plane, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis</li>
                    </ul>
                 </li>
                 <li> If first constrain is Tangent to Face, then the second contraint can be:
                    <ul>
                        <li>Through Point Angle to Plane</li>
                        <li>0 Deg Angle to Plane</li>
                        <li>90 Deg Tangent to Face</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Curve, then the second contraint can be:
                    <ul>
                        <li>Through Point Perpendicular to View Plane</li>
                    </ul>
                 </li>     

                 </ul>
                
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetGeometryAndConstraints
            (
                NXOpen::DisplayableObject * geometry1 /** First geometric object  */,
                NXOpen::Features::DatumPlaneBuilder::ConstraintType geometryConstraintType1 /** Constraint type of first geometry */,
                int constraintAttribute1 /** Constraint attribute value of first geometry */,
                double constraintValue1 /** Constraint value parameter of first geometry */,
                const NXString & constraint1 /** Constraint attached with first geometric object. 
                                                                                           Set to "0.0" in case value is not specified    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::DisplayableObject * geometry2 /** Second geometric object */,
                NXOpen::Features::DatumPlaneBuilder::ConstraintType geometryConstraintType2 /** Constraint type of first geometry */,
                int constraintAttribute2 /** Constraint attribute value of second geometry */,
                double constraintValue2 /** Constraint value parameter of second geometry */,
                const NXString & constraint2 /** Constraint attached with second geometric object. 
                                                                                           Set to "0.0" in case value is not specified   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets two different geometric objects. Possible combinations are: 
                 <ul>
                 <li> If first constrain is Through Datum Axis, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis Through Point Angle to Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Solid Edge and Linear Geometry, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis Through Point Angle to Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Face Axis, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis Through Point Angle to Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Point, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Parallel to Plane Perpendicular to Curve 
                                 Parallel to Surface's Tangent Plane</li>
                    </ul>
                 </li>
                 <li> If first constrain is Angle to Plane, then the second contraint can be:
                    <ul>
                        <li>Through Axis Through Edge</li>
                        <li>Linear Geometry Through Face Axis</li>
                    </ul>
                 </li>
                 <li> If first constrain is Tangent to Face, then the second contraint can be:
                    <ul>
                        <li>Through Point Angle to Plane</li>
                        <li>0 Deg Angle to Plane</li>
                        <li>90 Deg Tangent to Face</li>
                    </ul>
                 </li>
                 <li> If first constrain is Through Curve, then the second contraint can be:
                    <ul>
                        <li>Through Point Perpendicular to View Plane</li>
                    </ul>
                 </li>     

                 </ul>
                
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetGeometryAndConstraints
            (
                NXOpen::DisplayableObject * geometry1 /** First geometric object  */,
                NXOpen::Features::DatumPlaneBuilder::ConstraintType geometryConstraintType1 /** Constraint type of first geometry */,
                int constraintAttribute1 /** Constraint attribute value of first geometry */,
                double constraintValue1 /** Constraint value parameter of first geometry */,
                const char * constraint1 /** Constraint attached with first geometric object. 
                                                                                           Set to "0.0" in case value is not specified    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::DisplayableObject * geometry2 /** Second geometric object */,
                NXOpen::Features::DatumPlaneBuilder::ConstraintType geometryConstraintType2 /** Constraint type of first geometry */,
                int constraintAttribute2 /** Constraint attribute value of second geometry */,
                double constraintValue2 /** Constraint value parameter of second geometry */,
                const char * constraint2 /** Constraint attached with second geometric object. 
                                                                                           Set to "0.0" in case value is not specified   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets type of fixed datum plane. 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFixedDatumPlane
            (
                NXOpen::Features::DatumPlaneBuilder::FixedType type /** Indicates fixed datum plane type */
            );
            /** The plane is use to create the feature  @return   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Plane * GetPlane
            (
            );
            /** Update the feature if the feature does not exist then create it @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::Feature * UpdateFeature
            (
            );
            /** The datum display object this is the feature output  @return   
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::DatumPlane * GetDatum
            (
            );
            /**Returns  the resize during update 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool ResizeDuringUpdate
            (
            );
            /**Sets  the resize during update 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetResizeDuringUpdate
            (
                bool resize /** resize during update */
            );
            /**Returns  the offset instance plane flag  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool OffsetInstance
            (
            );
            /**Sets  the offset instance plane flag  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOffsetInstance
            (
                bool offsetInstance /** offset instance */
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