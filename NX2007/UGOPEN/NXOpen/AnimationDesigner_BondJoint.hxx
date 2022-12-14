#ifndef NXOpen_ANIMATIONDESIGNER_BONDJOINT_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_BONDJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_BondJoint.ja
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
        class BondJoint;
    }
    namespace AnimationDesigner
    {
        class PhysicsJoint;
    }
    namespace AnimationDesigner
    {
        class _BondJointBuilder;
        class BondJointImpl;
        /** Represents a Bond Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::BondJointBuilder  NXOpen::AnimationDesigner::BondJointBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  BondJoint : public NXOpen::AnimationDesigner::PhysicsJoint
        {
            private: BondJointImpl * m_bondjoint_impl;
            private: friend class  _BondJointBuilder;
            protected: BondJoint();
            public: ~BondJoint();
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
