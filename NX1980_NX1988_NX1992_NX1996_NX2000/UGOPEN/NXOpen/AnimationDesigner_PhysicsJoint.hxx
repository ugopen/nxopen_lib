#ifndef NXOpen_ANIMATIONDESIGNER_PHYSICSJOINT_HXX_INCLUDED
#define NXOpen_ANIMATIONDESIGNER_PHYSICSJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AnimationDesigner_PhysicsJoint.ja
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
#include <NXOpen/DisplayableObject.hxx>
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
        class PhysicsJoint;
    }
    class DisplayableObject;
    namespace AnimationDesigner
    {
        class _PhysicsJointBuilder;
        class PhysicsJointImpl;
        /** Represents the Animation Designer joint class. <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX12.0.2.  <br>  
        */
        class ANIMATIONDESIGNEROPENCPPEXPORT  PhysicsJoint : public NXOpen::DisplayableObject
        {
            private: PhysicsJointImpl * m_physicsjoint_impl;
            private: friend class  _PhysicsJointBuilder;
            protected: PhysicsJoint();
            public: ~PhysicsJoint();
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