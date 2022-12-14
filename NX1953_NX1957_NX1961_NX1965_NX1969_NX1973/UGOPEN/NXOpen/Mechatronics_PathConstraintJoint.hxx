#ifndef NXOpen_MECHATRONICS_PATHCONSTRAINTJOINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_PATHCONSTRAINTJOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PathConstraintJoint.ja
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
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class PathConstraintJoint;
    }
    namespace Mechatronics
    {
        class PhysicsJoint;
    }
    namespace Mechatronics
    {
        class _PathConstraintJointBuilder;
        class PathConstraintJointImpl;
        /** Represents the Path Constraint Joint class. It defines a object that limits a rigid body on path, which is defined
                a sequence of orientation CSYS.  <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::PathConstraintJointBuilder  NXOpen::Mechatronics::PathConstraintJointBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  PathConstraintJoint : public NXOpen::Mechatronics::PhysicsJoint
        {
            private: PathConstraintJointImpl * m_pathconstraintjoint_impl;
            private: friend class  _PathConstraintJointBuilder;
            protected: PathConstraintJoint();
            public: ~PathConstraintJoint();
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
