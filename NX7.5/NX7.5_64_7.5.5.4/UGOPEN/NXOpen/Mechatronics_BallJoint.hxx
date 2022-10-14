#ifndef NXOpen_MECHATRONICS_BALLJOINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_BALLJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_BallJoint.ja
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
        class BallJoint;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _BallJointBuilder;
        class BallJointImpl;
        /** Represents the Ball Joint. Objects are connected at a shared point and
            can move all ways rotationally. */
        class NXOPENCPPEXPORT  BallJoint : public Mechatronics::PhysicsJoint
        {
            private: BallJointImpl * m_balljoint_impl;
            private: friend class  _BallJointBuilder;
            protected: BallJoint();
            public: ~BallJoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif