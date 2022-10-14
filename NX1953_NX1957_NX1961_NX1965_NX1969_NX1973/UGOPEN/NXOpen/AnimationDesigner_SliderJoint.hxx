#ifndef NXOpen_ANIMATIONDESIGNER_SLIDERJOINT_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_SLIDERJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_SliderJoint.ja
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
        class SliderJoint;
    }
    namespace AnimationDesigner
    {
        class PhysicsJoint;
    }
    namespace AnimationDesigner
    {
        class _SliderJointBuilder;
        class SliderJointImpl;
        /** Represents a Slider Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::SliderJointBuilder  NXOpen::AnimationDesigner::SliderJointBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  SliderJoint : public NXOpen::AnimationDesigner::PhysicsJoint
        {
            private: SliderJointImpl * m_sliderjoint_impl;
            private: friend class  _SliderJointBuilder;
            protected: SliderJoint();
            public: ~SliderJoint();
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