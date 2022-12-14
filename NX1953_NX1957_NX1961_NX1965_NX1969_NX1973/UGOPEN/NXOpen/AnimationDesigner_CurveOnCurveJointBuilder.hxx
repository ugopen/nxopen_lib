#ifndef NXOpen_ANIMATIONDESIGNER_CURVEONCURVEJOINTBUILDER_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_CURVEONCURVEJOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_CurveOnCurveJointBuilder.ja
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
#include <NXOpen/AnimationDesigner_PhysicsJointBuilder.hxx>
#include <NXOpen/libanimationdesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AnimationDesigner
    {
        class CurveOnCurveJointBuilder;
    }
    namespace AnimationDesigner
    {
        class PhysicsJointBuilder;
    }
    class Direction;
    class Expression;
    class NXObject;
    class Point;
    namespace AnimationDesigner
    {
        class _CurveOnCurveJointBuilderBuilder;
        class CurveOnCurveJointBuilderImpl;
        /** Represents a @link NXOpen::AnimationDesigner::CurveOnCurveJointBuilder NXOpen::AnimationDesigner::CurveOnCurveJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::CurveOnCurveJointCollection::CreateCurveOnCurveJointBuilder  NXOpen::AnimationDesigner::CurveOnCurveJointCollection::CreateCurveOnCurveJointBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  CurveOnCurveJointBuilder : public NXOpen::AnimationDesigner::PhysicsJointBuilder
        {
            private: CurveOnCurveJointBuilderImpl * m_curveoncurvejointbuilder_impl;
            private: friend class  _CurveOnCurveJointBuilderBuilder;
            protected: CurveOnCurveJointBuilder();
            public: ~CurveOnCurveJointBuilder();
            /** Gets the section curve which belong to the attachment.  @return  curve or edge 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: std::vector<NXOpen::NXObject *> GetSectionCurve
            (
            );
            /** Sets the section curve which belong to the attachment. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetSectionCurve
            (
                const std::vector<NXOpen::NXObject *> & curves /** curve or edge */
            );
            /** Gets the connected curve which the attachment will move along.  @return  curve or edge 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: std::vector<NXOpen::NXObject *> GetConnectedCurve
            (
            );
            /** Sets the connected curve which the attachment will move along. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetConnectedCurve
            (
                const std::vector<NXOpen::NXObject *> & curves /** curve or edge */
            );
            /**Returns  the selected point on curve. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::Point * PointOnCurve
            (
            );
            /**Sets  the selected point on curve. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetPointOnCurve
            (
                NXOpen::Point * pointOnCurve /** pointoncurve */ 
            );
            /**Returns  the axis vector which is tangent to the connected curve at the selected point. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::Direction * AxisVector
            (
            );
            /**Sets  the axis vector which is tangent to the connected curve at the selected point. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetAxisVector
            (
                NXOpen::Direction * axisVector /** axisvector */ 
            );
            /**Returns  the offset specifies the "Zero Point" on the curve whose distance to the point along the curve is the offset value.
                        Zero Point is on the opposite direction of the axis with respect to the point on the curve. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: NXOpen::Expression * Offset
            (
            );
            /**Returns  the sliding flag. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: bool Sliding
            (
            );
            /**Sets  the sliding flag. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void SetSliding
            (
                bool sliding /** sliding */ 
            );
            /** Evaluates the path. If there is no path, create it, otherwise evaluate it. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_animationdesigner (" NX Animation Designer") */
            public: void EvaluatePath
            (
                const std::vector<NXOpen::NXObject *> & curves /** curve or edge */
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
