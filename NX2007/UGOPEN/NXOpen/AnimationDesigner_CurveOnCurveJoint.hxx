#ifndef NXOpen_ANIMATIONDESIGNER_CURVEONCURVEJOINT_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_CURVEONCURVEJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_CurveOnCurveJoint.ja
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
#include <NXOpen/AnimationDesigner_PhysicsJoint.hxx>
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
        class CurveOnCurveJoint;
    }
    namespace AnimationDesigner
    {
        class PhysicsJoint;
    }
    namespace AnimationDesigner
    {
        class _CurveOnCurveJointBuilder;
        class CurveOnCurveJointImpl;
        /** Represents a Curve On Curve Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::CurveOnCurveJointBuilder  NXOpen::AnimationDesigner::CurveOnCurveJointBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  CurveOnCurveJoint : public NXOpen::AnimationDesigner::PhysicsJoint
        {
            private: CurveOnCurveJointImpl * m_curveoncurvejoint_impl;
            private: friend class  _CurveOnCurveJointBuilder;
            protected: CurveOnCurveJoint();
            public: ~CurveOnCurveJoint();
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