#ifndef NXOpen_MECHATRONICS_PHYSICSJOINTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_PHYSICSJOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PhysicsJointBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Mechatronics_PhysicsJointBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class PhysicsJointBuilder;
    }
    class Builder;
    class SelectNXObject;
    namespace Mechatronics
    {
        class _PhysicsJointBuilderBuilder;
        class PhysicsJointBuilderImpl;
        /** Represents a base builder for Physics Joints.  <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT  PhysicsJointBuilder : public Builder
        {
            private: PhysicsJointBuilderImpl * m_physicsjointbuilder_impl;
            private: friend class  _PhysicsJointBuilderBuilder;
            protected: PhysicsJointBuilder();
            public: ~PhysicsJointBuilder();
            /**Returns  the attachment of joint. This can be a @link RigidBody RigidBody@endlink  
                    or objects which can create a rigid body by.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::SelectNXObject * Attachment
            (
            );
            /**Returns  the base of joint. This can be a @link RigidBody RigidBody@endlink  
                    or objects which can create a rigid body by.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::SelectNXObject * Base
            (
            );
            /**Returns  the name.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXString Name
            (
            );
            /**Sets  the name.  <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif