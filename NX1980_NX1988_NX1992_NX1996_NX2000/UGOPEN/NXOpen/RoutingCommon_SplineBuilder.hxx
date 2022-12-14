#ifndef NXOpen_ROUTINGCOMMON_SPLINEBUILDER_HXX_INCLUDED
#define NXOpen_ROUTINGCOMMON_SPLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RoutingCommon_SplineBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/RoutingCommon_SplinePointBuilder.hxx>
#include <NXOpen/Routing_StockBlockBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_routingcommon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace RoutingCommon
    {
        class SplineBuilder;
    }
    class Builder;
    class Curve;
    class Direction;
    class Expression;
    class Part;
    namespace Routing
    {
        class ControlPoint;
    }
    namespace Routing
    {
        class StockBlockBuilder;
    }
    namespace RoutingCommon
    {
        class SplinePointBuilder;
    }
    namespace RoutingCommon
    {
        class SplinePointBuilderList;
    }
    namespace RoutingCommon
    {
        class _SplineBuilderBuilder;
        class SplineBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::RoutingCommon::SplineBuilder NXOpen::RoutingCommon::SplineBuilder@endlink  object.
                The builder allows for creating and editing of splines, adding extensions,
                adding stock offset points, adding stock, locking length, adding slack, and locking to other
                objects.
             <br> To create a new instance of this class, use @link NXOpen::RoutingCommon::BuilderFactory::CreateSplineBuilder  NXOpen::RoutingCommon::BuilderFactory::CreateSplineBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGCOMMONEXPORT  SplineBuilder : public NXOpen::Builder
        {
            /** Describes user attribute methods options.
                        These value are used to set minimum checking method.
                        If checking method is ratio to diameter than allowable radius will be computed by
                        ratioToDiameter x Stock Diameter.
                    */

            /// \cond NX_NO_DOC 
            public: enum SplineAttributeOptions
            {
                SplineAttributeOptionsRadius/** A radius method option for spline user attribute  */,
                SplineAttributeOptionsRatioToDiameter/** A ratio to diameter method option for spline user attribute. */
            };


            /// \endcond 
            /** Describes the type of slack to be applied to the spline. */

            /// \cond NX_NO_DOC 
            public: enum LengthType
            {
                LengthTypeLockLength/** The length of the spline is slacking to a specified and locked length. */,
                LengthTypeTotalPercentage/** Slack value is ratio of extra length. Non-end defining points relaxed down */,
                LengthTypeTotalAdditional/** Slack value is extra length. Non-end defining points relaxed down */,
                LengthTypeUndefined/** Slack length is undefined. */
            };


            /// \endcond 
            private: SplineBuilderImpl * m_splinebuilder_impl;
            private: friend class  _SplineBuilderBuilder;
            protected: SplineBuilder();
            public: ~SplineBuilder();

            /// \cond NX_NO_DOC 
            /** Removes the defining point from the spline.
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveDefiningPoint
            (
                int index /** index */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the list of defining points 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::RoutingCommon::SplinePointBuilderList * PointList
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Gets the locked length expression.  @return  The length used for locked length splines. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * GetLockedLengthExpression
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the stock settings for creating stock. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::StockBlockBuilder * StockSettings
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get work part of which spline will be created on  @return  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Part * GetWorkPart
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Locks the length of the current spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void LockSplineLengthNoShaping
            (
                NXOpen::Expression * length /** The length to lock the spline. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Removes all shaping applied to the spline (Lock length, slacking). 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveAllShaping
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void AddSlackToSpline
            (
                NXOpen::RoutingCommon::SplineBuilder::LengthType lengthType /** The type of slack to add. */,
                NXOpen::Expression * lengthValue /** The amount of slack to add. */,
                NXOpen::Direction * slackDirection /** The direction to apply slack.*/
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets extension on a point of this spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void AssignExtensionAtPointIndex
            (
                int pointIndex /** Point to assign extension. */,
                const NXOpen::Point3d & location /** Location of the extension direction. */,
                const NXOpen::Vector3d & direction /** Direction of the extension on the target spline. */,
                double forward /** Distance to apply if no extension exists. */,
                double backward /** Distance to apply if no extension exists. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets extension on one end of the target spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void AssignExtension
            (
                NXOpen::Routing::ControlPoint * controlPoint /** Control point on which to assign extension. */,
                NXOpen::Curve * targetCurve /** Target spline of said point. */,
                const NXOpen::Point3d & location /** Location of the extension direction. */,
                const NXOpen::Vector3d & direction /** Direction of the extension on the target spline. */,
                double distance /** Distance to apply end on which the control point exists. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets tangency between two splines. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void AssignTangency
            (
                NXOpen::Routing::ControlPoint * thisControlPoint /** ControlPoint on the first spline that must be used to share tangency. */,
                NXOpen::Curve * thisCurve /** First spline being made tangent. */,
                NXOpen::Routing::ControlPoint * targetControlPoint /** ControlPoint on the second spline that must be used to share tangency. */,
                NXOpen::Curve * targetCurve /** Target spline being made tangent. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Locks the length of the current spline and fixes the interior points of the spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void LockSplineLengthWithShapingFixedPoints
            (
                NXOpen::Expression * length /** The length to lock the spline. */,
                NXOpen::Direction * slackDirection /** The direction to apply slack.  */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Locks the length of the current spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void LockSplineLengthWithShaping
            (
                NXOpen::Expression * length /** The length to lock the spline. */,
                NXOpen::Direction * slackDirection /** The direction to apply slack.*/
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Adds slack to the spline without locking the length.
                        This will move the interior defining points of the spline in the slack direction
                        until the given length is reached.
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void ShapeByAdditionalLengthMovingPoints
            (
                NXOpen::Expression * length /** The length of the spline. */,
                NXOpen::RoutingCommon::SplineBuilder::LengthType lengthType /** The type of slack. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  whether the spline minimum radius value should be checked or not on this spline.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool UseMinimumCheckingValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  whether the spline minimum radius value should be checked or not on this spline.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetUseMinimumCheckingValue
            (
                bool useMinRadius /** useminradius */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the minimum checking method for this spline.
                    See @link NXOpen::RoutingCommon::SplineBuilder::SplineAttributeOptions NXOpen::RoutingCommon::SplineBuilder::SplineAttributeOptions@endlink  for valid
                    options 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::RoutingCommon::SplineBuilder::SplineAttributeOptions MinimumCheckingMethod
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the minimum checking method for this spline.
                    See @link NXOpen::RoutingCommon::SplineBuilder::SplineAttributeOptions NXOpen::RoutingCommon::SplineBuilder::SplineAttributeOptions@endlink  for valid
                    options 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetMinimumCheckingMethod
            (
                NXOpen::RoutingCommon::SplineBuilder::SplineAttributeOptions routeCheckingMethod /** routecheckingmethod */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the minimum radius allowed for this spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * MinimumCheckingAllowableValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the minimum ratio allowed for this spline
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * MinimumCheckingAllowableRatio
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  whether the spline minimum radius value should be displayed or not. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool ShowSplineMinimumRadius
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  whether the spline minimum radius value should be displayed or not. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetShowSplineMinimumRadius
            (
                bool allowDisplay /** allowdisplay */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Remove any tangency connectivity information between spline at the given point. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveTangency
            (
                NXOpen::RoutingCommon::SplinePointBuilder * point /** point */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Can tangency connectivity information be applied on this spline at the given point. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool CanAssignTangency
            (
                NXOpen::RoutingCommon::SplinePointBuilder * point /** point */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Is the curvature controlled for this spline 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool IsCurvatureControlled
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Enable curvature control for this spline 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void EnableCurvatureControl
            (
                NXOpen::Expression * minRadiusExp /** The minimum radius used for curvature controlled splines. */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Disable curvature control for this spline 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void DisableCurvatureControl
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Gets the expression for the minimum radius allowed for this spline. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * GetBoundedCurvatureRadius
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Has the curvature control for the spline failed?
                     
                        Note that the routine returns false if no curvature has been applied.
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool HasCurvatureControlFailed
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  a setting to control extension values when detaching a point in the spline 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool RemoveExtensionUponDetach
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  a setting to control extension values when detaching a point in the spline 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetRemoveExtensionUponDetach
            (
                bool removeExt /** removeext */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the current spline being created or edited.
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Curve * SplineCurve
            (
            );

            /// \endcond 
        };

        /// \endcond 
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
