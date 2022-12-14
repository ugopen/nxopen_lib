#ifndef NXOpen_GEOMETRICUTILITIES_CURVESHAPINGBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_CURVESHAPINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_CurveShapingBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_Continuity.hxx>
#include <NXOpen/GeometricUtilities_CurveShapingBuilder.hxx>
#include <NXOpen/GeometricUtilities_OrientXpressBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class CurveShapingBuilder;
    }
    class Curve;
    class Direction;
    namespace Features
    {
        class GeometricConstraintDataManager;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OrientXpressBuilder;
    }
    class Plane;
    class Point;
    class SelectPointList;
    class SelectSplineList;
    class Spline;
    namespace GeometricUtilities
    {
        class _CurveShapingBuilderBuilder;
        class CurveShapingBuilderImpl;
        /** Represents a @link GeometricUtilities::CurveShapingBuilder GeometricUtilities::CurveShapingBuilder@endlink .
                This class allows shaping of curves by identifying key points on them and modifying the
                location of those points. It also allows constraining curve ends.  */
        class NXOPENCPPEXPORT  CurveShapingBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Point insertion option */
            public: enum InsertionMethodOptions
            {
                InsertionMethodOptionsUniform/** Insert points uniformly */,
                InsertionMethodOptionsThroughPoints/** Insert points through points */,
                InsertionMethodOptionsBetweenPoints/** Insert points between points */
            };

            /** Curve parameter points movement types */
            public: enum MovementMethodType
            {
                MovementMethodTypeWCS/** Movement along WCS principal axis or plane */,
                MovementMethodTypeView/** Movement in view plane */,
                MovementMethodTypeVector/** Movement along arbitrary direction */,
                MovementMethodTypePlane/** Movement in arbitrary plane */,
                MovementMethodTypeNormal/** Movement along a face normal */
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

            private: CurveShapingBuilderImpl * m_curveshapingbuilder_impl;
            private: friend class  _CurveShapingBuilderBuilder;
            protected: CurveShapingBuilder();
            public: ~CurveShapingBuilder();
            /**Returns  the point insertion method  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveShapingBuilder::InsertionMethodOptions InsertionMethod
            (
            );
            /**Sets  the point insertion method  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetInsertionMethod
            (
                NXOpen::GeometricUtilities::CurveShapingBuilder::InsertionMethodOptions insertionMethod /** insertionmethod */ 
            );
            /**Returns  the specified points to define insertion point locations  <br> License requirements : None */
            public: NXOpen::SelectPointList * SpecifyPoints
            (
            );
            /**Returns  the number of points to be inserted  <br> License requirements : None */
            public: int Number
            (
            );
            /**Sets  the number of points to be inserted  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetNumber
            (
                int number /** number */ 
            );
            /**Returns  the curve selection for point insertion  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: NXOpen::SelectSplineList * SelectCurves
            (
            );
            /**Returns  the constraint manager. Allows definition of key points to be used to shape the curve.  <br> License requirements : None */
            public: NXOpen::Features::GeometricConstraintDataManager * ConstraintManager
            (
            );
            /**Returns  the value indicating if transition type is linear  <br> License requirements : None */
            public: bool HasLinearTransition
            (
            );
            /**Sets  the value indicating if transition type is linear  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetHasLinearTransition
            (
                bool hasLinear /** haslinear */ 
            );
            /**Returns  the value indicating if point should be moved along curve. A key point is moved along the curve
                        in order to change its parametric location without affecting curve shape.   <br> License requirements : None */
            public: bool CanMoveAlongCurve
            (
            );
            /**Sets  the value indicating if point should be moved along curve. A key point is moved along the curve
                        in order to change its parametric location without affecting curve shape.   <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetCanMoveAlongCurve
            (
                bool canMoveAlongCurve /** canmovealongcurve */ 
            );
            /**Returns  the movement method  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveShapingBuilder::MovementMethodType MovementMethod
            (
            );
            /**Sets  the movement method  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMovementMethod
            (
                NXOpen::GeometricUtilities::CurveShapingBuilder::MovementMethodType movementMethod /** movementmethod */ 
            );
            /**Returns  the WCS option  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveShapingBuilder::WCSOptionType WCSOption
            (
            );
            /**Sets  the WCS option  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetWCSOption
            (
                NXOpen::GeometricUtilities::CurveShapingBuilder::WCSOptionType wcsOption /** wcsoption */ 
            );
            /**Returns  the orient express object  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OrientXpressBuilder * OrientExpress
            (
            );
            /**Returns  the movement vector  <br> License requirements : None */
            public: NXOpen::Direction * MovementVector
            (
            );
            /**Sets  the movement vector  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMovementVector
            (
                NXOpen::Direction * movementVector /** movementvector */ 
            );
            /**Returns  the movement plane  <br> License requirements : None */
            public: NXOpen::Plane * MovementPlane
            (
            );
            /**Sets  the movement plane  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetMovementPlane
            (
                NXOpen::Plane * movementPlane /** movementplane */ 
            );
            /**Returns  the continuity at start of the curve  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity::ContinuityTypes StartContinuity
            (
            );
            /**Sets  the continuity at start of the curve  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetStartContinuity
            (
                NXOpen::GeometricUtilities::Continuity::ContinuityTypes startContinuity /** startcontinuity */ 
            );
            /**Returns  the continuity at end of the curve  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Continuity::ContinuityTypes EndContinuity
            (
            );
            /**Sets  the continuity at end of the curve  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetEndContinuity
            (
                NXOpen::GeometricUtilities::Continuity::ContinuityTypes endContinuity /** endcontinuity */ 
            );
            /** Adds a curve for shaping  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void AddCurve
            (
                NXOpen::Curve * curve /** Curve to be deformed */
            );
            /** Removes a curve  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void RemoveCurve
            (
                NXOpen::Curve * curve /** Curve to be deleted */
            );
            /** Sets key points that are selected or will be moved  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetActivePoints
            (
                const std::vector<NXOpen::Point *> & points /** Key points */,
                NXOpen::Point * masterPoint /** Point which user actually moves to move a group of selected points */
            );
            /** Deforms curves based on active points  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void Deform
            (
            );
            /** Applies parameter value from a key point to a group of key points without affecting curve shape  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void ApplyParameterValue
            (
                NXOpen::Point * sourcePoint /** Point whose parameter value to be applied */,
                const std::vector<NXOpen::Point *> & destinationPoints /** Points to be edited */
            );
            /** Deletes all points on a curve. If no curve is specified, deletes all points on all curves.  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void DeleteAllPoints
            (
                NXOpen::Spline * curve /** Curve */
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
