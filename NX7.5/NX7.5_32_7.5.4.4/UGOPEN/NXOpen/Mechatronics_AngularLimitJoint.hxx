#ifndef NXOpen_MECHATRONICS_ANGULARLIMITJOINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_ANGULARLIMITJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_AngularLimitJoint.ja
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
        class AngularLimitJoint;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _AngularLimitJointBuilder;
        class AngularLimitJointImpl;
        /** Represents the Angular Limit Joint. Angular limit joint causes objects to stop 
            moving when their relative position moves beyond a certain degree or get too close together. */
        class NXOPENCPPEXPORT  AngularLimitJoint : public Mechatronics::PhysicsJoint
        {
            private: AngularLimitJointImpl * m_angularlimitjoint_impl;
            private: friend class  _AngularLimitJointBuilder;
            protected: AngularLimitJoint();
            public: ~AngularLimitJoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif
