#ifndef NXOpen_MOTION_CURVECONTACTRECURDYN_HXX_INCLUDED
#define NXOpen_MOTION_CURVECONTACTRECURDYN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CurveContactRecurdyn.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class CurveContactRecurdyn;
    }
    class Expression;
    class NXObject;
    namespace Motion
    {
        class _CurveContactRecurdynBuilder;
        class CurveContactRecurdynImpl;
        /** Represents a @link NXOpen::Motion::CurveContactRecurdyn NXOpen::Motion::CurveContactRecurdyn@endlink  
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  CurveContactRecurdyn : public NXOpen::NXObject
        {
            private: CurveContactRecurdynImpl * m_curvecontactrecurdyn_impl;
            private: friend class  _CurveContactRecurdynBuilder;
            protected: CurveContactRecurdyn();
            public: ~CurveContactRecurdyn();
            /**Returns  the stiffness expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StiffnessExpression
            (
            );
            /**Returns  the force exponent expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ForceExponentExpression
            (
            );
            /**Returns  the material damping expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaterialDampingExpression
            (
            );
            /**Returns  the penetration depth expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PenetrationDepthExpression
            (
            );
            /**Returns  the Buffer Radius Factor expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BufferRadiusFactorExpression
            (
            );
            /**Returns  the Maximun Step Size Factor expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * MaximumStepSizeFactorExpression
            (
            );
            /**Returns  the Curve Tolerance Factor expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * CurveToleranceFactorExpression
            (
            );
            /**Returns  the first curve maximum penetration expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FirstCurveMaximumPenetrationExpression
            (
            );
            /**Returns  the second curve maximum penetration expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SecondCurveMaximumPenetrationExpression
            (
            );
            /**Returns  the static coefficient expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StaticCoefficientExpression
            (
            );
            /**Returns  the slip velocity expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SlipVelocityExpression
            (
            );
            /**Returns  the dynamic coefficient expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DynamicCoefficientExpression
            (
            );
            /**Returns  the transition velocity expression
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TransitionVelocityExpression
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