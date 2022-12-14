#ifndef NXOpen_MECHATRONICS_FIXEDJOINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_FIXEDJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_FixedJoint.ja
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
        class FixedJoint;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _FixedJointBuilder;
        class FixedJointImpl;
        /** Represents the Fixed Joint. Fixed joint is that objects are glued to one
            another completely. */
        class NXOPENCPPEXPORT  FixedJoint : public Mechatronics::PhysicsJoint
        {
            private: FixedJointImpl * m_fixedjoint_impl;
            private: friend class  _FixedJointBuilder;
            protected: FixedJoint();
            public: ~FixedJoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif
