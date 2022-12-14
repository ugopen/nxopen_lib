#ifndef NXOpen_MECHATRONICS_ANGULARSPRINGJOINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_ANGULARSPRINGJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_AngularSpringJoint.ja
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
#include <NXOpen/Mechatronics_PhysicsJoint.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class AngularSpringJoint;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _AngularSpringJointBuilder;
        class AngularSpringJointImpl;
        /** Represents the Angular Spring Joint. Angular spring joint causes objects to behave as though 
            there is a spring-like force between them that grows as the object become farther apart or closer together. */
        class NXOPENCPPEXPORT  AngularSpringJoint : public Mechatronics::PhysicsJoint
        {
            private: AngularSpringJointImpl * m_angularspringjoint_impl;
            private: friend class  _AngularSpringJointBuilder;
            protected: AngularSpringJoint();
            public: ~AngularSpringJoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif
