#ifndef NXOpen_MECHATRONICS_PHYSICSCONSTRAINT_HXX_INCLUDED
#define NXOpen_MECHATRONICS_PHYSICSCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PhysicsConstraint.ja
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
        class PhysicsConstraint;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _PhysicsConstraintBuilder;
        class PhysicsConstraintImpl;
        /** Represents the mechatronics constraint class. <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  PhysicsConstraint : public NXOpen::DisplayableObject
        {
            private: PhysicsConstraintImpl * m_physicsconstraint_impl;
            private: friend class  _PhysicsConstraintBuilder;
            protected: PhysicsConstraint();
            public: ~PhysicsConstraint();
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
