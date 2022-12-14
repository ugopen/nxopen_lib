#ifndef NXOpen_FEATURES_STUDIOSPLINEBUILDEREX_HXX_INCLUDED
#define NXOpen_FEATURES_STUDIOSPLINEBUILDEREX_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_StudioSplineBuilderEx.ja
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
#include <NXOpen/Features_GeometricConstraintDataManager.hxx>
#include <NXOpen/Features_StudioSplineBuilderEx.hxx>
#include <NXOpen/GeometricUtilities_OrientXpressBuilder.hxx>
#include <NXOpen/GeometricUtilities_SplineExtensionBuilder.hxx>
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
        class StudioSplineBuilderEx;
    }
    class CoordinateSystem;
    class Direction;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class GeometricConstraintDataManager;
    }
    namespace GeometricUtilities
    {
        class OrientXpressBuilder;
    }
    namespace GeometricUtilities
    {
        class SplineExtensionBuilder;
    }
    class NXObject;
    class Plane;
    class Spline;
    namespace Features
    {
        class _StudioSplineBuilderExBuilder;
        class StudioSplineBuilderExImpl;
        /** Studio Spline builder class.  <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateStudioSplineBuilderEx  Features::FeatureCollection::CreateStudioSplineBuilderEx @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DrawingPlaneOption </td> <td> 
         
        View </td> </tr> 

        <tr><td> 
         
        Extender.EndExtensionOption </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        Extender.EndValue.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Extender.StartExtensionOption </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        Extender.StartValue.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        InputCurveOption </td> <td> 
         
        Hide </td> </tr> 

        <tr><td> 
         
        MatchKnotsType </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        MovementMethod </td> <td> 
         
        View </td> </tr> 

        <tr><td> 
         
        Type </td> <td> 
         
        ThroughPoints </td> </tr> 

        <tr><td> 
         
        WCSOption </td> <td> 
         
        X </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  StudioSplineBuilderEx : public Features::FeatureBuilder
        {
            /** Spline methods. */
            public: enum Types
            {
                TypesThroughPoints/** Spline through points */,
                TypesByPoles/** Spline by poles */
            };

            /** Options for creating knots at the defining points in case of through point spline */
            public: enum MatchKnotsTypes
            {
                MatchKnotsTypesNone/** No knot matching */,
                MatchKnotsTypesCubic/** Match knots for cubic non-periodic spline */,
                MatchKnotsTypesGeneral/** Match knots for general spline */
            };

            /** Drawing plane options */
            public: enum DrawingPlaneOptions
            {
                DrawingPlaneOptionsView/** View plane */,
                DrawingPlaneOptionsXY/** XY plane */,
                DrawingPlaneOptionsYZ/** YZ plane */,
                DrawingPlaneOptionsXZ/** XZ plane */,
                DrawingPlaneOptionsGeneral/** General plane */
            };

            /** Options of the actions to be taken on an input non-parametric spline
                        after its editing is done. These options are used only while trying
                        to make non-parametric spline a feature. */
            public: enum InputCurveOptions
            {
                InputCurveOptionsKeep/** Keep original curve */,
                InputCurveOptionsHide/** Hide original curve */,
                InputCurveOptionsDelete/** Delete original curve */
            };

            /** Points movement types */
            public: enum MovementMethodType
            {
                MovementMethodTypeWCS/** Movement along WCS principal axis or plane */,
                MovementMethodTypeView/** Movement in view plane */,
                MovementMethodTypeVector/** Movement along arbitrary direction */,
                MovementMethodTypePlane/** Movement in arbitrary plane */,
                MovementMethodTypeNormal/** Movement along a face normal */,
                MovementMethodTypePolygon/** Movement along a relevant control polygon segment */
            };

            /** WCS principal axis or plane types */
            public: enum WCSOptionType
            {
                WCSOptionTypeX/** Along X axis */,
                WCSOptionTypeY/** Along Y axis */,
                WCSOptionTypeZ/** Along Z axis */,
                WCSOptionTypeYZ/** In YZ plane */,
                WCSOptionTypeXZ/** In XZ plane */,
                WCSOptionTypeXY/** In XY plane */
            };

            private: StudioSplineBuilderExImpl * m_studiosplinebuilderex_impl;
            private: friend class  _StudioSplineBuilderExBuilder;
            protected: StudioSplineBuilderEx();
            public: ~StudioSplineBuilderEx();
            /**Returns  the spline method 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::StudioSplineBuilderEx::Types Type
            (
            );
            /**Sets  the spline method 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::Features::StudioSplineBuilderEx::Types type /** type */ 
            );
            /**Returns  the degree 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: int Degree
            (
            );
            /**Sets  the degree 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetDegree
            (
                int degree /** degree */ 
            );
            /**Returns  a constraint to match knots at the defining points for a through point spline 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::StudioSplineBuilderEx::MatchKnotsTypes MatchKnotsType
            (
            );
            /**Sets  a constraint to match knots at the defining points for a through point spline 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetMatchKnotsType
            (
                NXOpen::Features::StudioSplineBuilderEx::MatchKnotsTypes matchKnotsType /** matchknotstype */ 
            );
            /**Returns  a flag indicating if single segment by pole spline is to be created 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsSingleSegment
            (
            );
            /**Sets  a flag indicating if single segment by pole spline is to be created 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetSingleSegment
            (
                bool isSingleSegment /** issinglesegment */ 
            );
            /**Returns  the periodicity 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsPeriodic
            (
            );
            /**Sets  the periodicity 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetPeriodic
            (
                bool periodicity /** periodicity */ 
            );
            /**Returns  a drawing plane option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::StudioSplineBuilderEx::DrawingPlaneOptions DrawingPlaneOption
            (
            );
            /**Sets  a drawing plane option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetDrawingPlaneOption
            (
                NXOpen::Features::StudioSplineBuilderEx::DrawingPlaneOptions planeOption /** planeoption */ 
            );
            /**Returns  the drawing plane 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * DrawingPlane
            (
            );
            /**Sets  the drawing plane 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetDrawingPlane
            (
                NXOpen::Plane * drawingPlane /** drawingplane */ 
            );
            /**Returns  the movement method 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::StudioSplineBuilderEx::MovementMethodType MovementMethod
            (
            );
            /**Sets  the movement method 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetMovementMethod
            (
                NXOpen::Features::StudioSplineBuilderEx::MovementMethodType movementMethod /** movementmethod */ 
            );
            /**Returns  the WCS option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::StudioSplineBuilderEx::WCSOptionType WCSOption
            (
            );
            /**Sets  the WCS option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetWCSOption
            (
                NXOpen::Features::StudioSplineBuilderEx::WCSOptionType wcsOption /** wcsoption */ 
            );
            /**Returns  the orient express object 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OrientXpressBuilder * OrientExpress
            (
            );
            /**Returns  the movement vector 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * MovementVector
            (
            );
            /**Sets  the movement vector 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetMovementVector
            (
                NXOpen::Direction * movementVector /** movementvector */ 
            );
            /**Returns  the movement plane 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * MovementPlane
            (
            );
            /**Sets  the movement plane 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetMovementPlane
            (
                NXOpen::Plane * movementPlane /** movementplane */ 
            );
            /**Returns  the constraint manager 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GeometricConstraintDataManager * ConstraintManager
            (
            );
            /**Returns  the extension option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SplineExtensionBuilder * Extender
            (
            );
            /**Returns  the flag indicating if free or non attached defining points or poles should be 
                        moved proportionally during update of the spline feature 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool HasProportionalUpdate
            (
            );
            /**Sets  the flag indicating if free or non attached defining points or poles should be 
                        moved proportionally during update of the spline feature 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetHasProportionalUpdate
            (
                bool hasProportionalUpdate /** hasproportionalupdate */ 
            );
            /**Returns  the flag indicating if a feature should be created 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsAssociative
            (
            );
            /**Sets  the flag indicating if a feature should be created 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the input curve option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::StudioSplineBuilderEx::InputCurveOptions InputCurveOption
            (
            );
            /**Sets  the input curve option 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetInputCurveOption
            (
                NXOpen::Features::StudioSplineBuilderEx::InputCurveOptions option /** option */ 
            );
            /** Queries the knot sequence for by pole spline  @return  The knot sequence 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetKnots
            (
            );
            /** Sets the optional knot sequence for by pole spline 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetKnots
            (
                const std::vector<double> & knots /** The knot sequence */
            );
            /** Queries the parameters at defining points for a through point spline  @return  The parameters 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetParameters
            (
            );
            /** Sets the optional parameters at defining points for a through point spline 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetParameters
            (
                const std::vector<double> & parameters /** The parameters */
            );
            /**Returns  the spline curve 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Spline * Curve
            (
            );
            /** Sets a non-parametric spline for editing 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void EditSpline
            (
                NXOpen::NXObject * spline /** spline */ 
            );
            /** Inserts knot at a closest point on the spline 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void InsertKnot
            (
                const NXOpen::Point3d & point /** Point at which knot to be inserted */
            );
            /** Inserts a pole in the middle of a control polygon segment 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void InsertPole
            (
                int afterIndex /** Index of a pole after which to insert new pole */
            );
            /** Evaluates the spline 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void Evaluate
            (
            );
            /**Returns  the flag indicating if spline has plane constraint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool HasPlaneConstraint
            (
            );
            /**Sets  the flag indicating if spline has plane constraint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetHasPlaneConstraint
            (
                bool hasConstraint /** hasconstraint */ 
            );
            /**Returns  the coordinate system defining plane constraint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * ConstraintPlane
            (
            );
            /**Sets  the coordinate system defining plane constraint 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetConstraintPlane
            (
                NXOpen::CoordinateSystem * coordinateSystem /** coordinatesystem */ 
            );
            /** Updates spline based on constraint plane 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void UpdateOnConstraintPlane
            (
            );
            /**Returns  the flag indicating if WCS like tool should be deployed when a point or pole handle is selected 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanUseOrientationTool
            (
            );
            /**Sets  the flag indicating if WCS like tool should be deployed when a point or pole handle is selected 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING") OR cam_base ("CAM BASE") */
            public: void SetCanUseOrientationTool
            (
                bool useOrientationTool /** useorientationtool */ 
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
