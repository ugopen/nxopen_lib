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
        class PhysicsJointBuilder;
    }
    class Builder;
    class NXObject;
    class SelectNXObject;
    namespace Mechatronics
    {
        class _PhysicsJointBuilderBuilder;
        class PhysicsJointBuilderImpl;
        /** Represents a base builder for Physics Joints.  <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  PhysicsJointBuilder : public Builder
        {
            private: PhysicsJointBuilderImpl * m_physicsjointbuilder_impl;
            private: friend class  _PhysicsJointBuilderBuilder;
            protected: PhysicsJointBuilder();
            public: ~PhysicsJointBuilder();
            /**Returns  the attachment of joint. This can be a @link RigidBody RigidBody@endlink  
                    or objects which can create a rigid body by. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::SelectNXObject * Attachment
            (
            );
            /** Sets the attachment. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetAttachment
            (
                NXOpen::NXObject * attachment /** attachment */ 
            );
            /**Returns  the base of joint. This can be a @link RigidBody RigidBody@endlink  
                    or objects which can create a rigid body by. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::SelectNXObject * Base
            (
            );
            /** Sets the base. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetBase
            (
                NXOpen::NXObject * base /** base */ 
            );
            /**Returns  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void SetName
            (
                const char * name /** name */ 
            );
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