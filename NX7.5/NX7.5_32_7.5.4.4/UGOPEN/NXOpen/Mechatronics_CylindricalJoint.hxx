#ifndef NXOpen_MECHATRONICS_CYLINDRICALJOINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_CYLINDRICALJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_CylindricalJoint.ja
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
        class CylindricalJoint;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _CylindricalJointBuilder;
        class CylindricalJointImpl;
        /** Represents the Cylindrical Joint. A Cylindrical Joint is a connection that 
            can move both linearly and rotationally. */
        class NXOPENCPPEXPORT  CylindricalJoint : public Mechatronics::PhysicsJoint
        {
            private: CylindricalJointImpl * m_cylindricaljoint_impl;
            private: friend class  _CylindricalJointBuilder;
            protected: CylindricalJoint();
            public: ~CylindricalJoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif