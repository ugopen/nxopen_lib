#ifndef NXOpen_POSITIONING_COMPONENTCONSTRAINT_HXX_INCLUDED
#define NXOpen_POSITIONING_COMPONENTCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Positioning_ComponentConstraint.ja
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
#include <NXOpen/Positioning_Constraint.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Positioning
    {
        class ComponentConstraint;
    }
    namespace Assemblies
    {
        class Arrangement;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Positioning
    {
        class Constraint;
    }
    namespace Positioning
    {
        class _ComponentConstraintBuilder;
        class ComponentConstraintImpl;
        /**
            Constraint for use in positioning assembly objects in NX.
            
        */
        class NXOPENCPPEXPORT  ComponentConstraint : public Positioning::Constraint
        {
            private: ComponentConstraintImpl * m_componentconstraint_impl;
            private: friend class  _ComponentConstraintBuilder;
            protected: ComponentConstraint();
            public: ~ComponentConstraint();
            /**
                    Remembers the constraint in the prototype part of a referenced component
                    for reuse in other occurrences of the part. Fix and Bond constraints are
                    never remembered.  If the constraint does not reference geometry in the
                    component, it is not remembered.
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void RememberOnComponent
            (
                NXOpen::Assemblies::Component * component /** The @link Assemblies::Component Assemblies::Component@endlink  on which the constraint is remembered */
            );
            /**Returns 
                    the arrangement specific state of this @link Positioning::ComponentConstraint Positioning::ComponentConstraint@endlink  in the 
                    @link Positioning::ComponentPositioner::PrimaryArrangement Positioning::ComponentPositioner::PrimaryArrangement @endlink and @link Positioning::ComponentPositioner::SetPrimaryArrangement Positioning::ComponentPositioner::SetPrimaryArrangement @endlink .  Constraints can
                    never be arrangement specific in piece parts.
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool ArrangementSpecific
            (
            );
            /**Sets 
                    the arrangement specific state of this @link Positioning::ComponentConstraint Positioning::ComponentConstraint@endlink  in the 
                    @link Positioning::ComponentPositioner::PrimaryArrangement Positioning::ComponentPositioner::PrimaryArrangement @endlink and @link Positioning::ComponentPositioner::SetPrimaryArrangement Positioning::ComponentPositioner::SetPrimaryArrangement @endlink .  Constraints can
                    never be arrangement specific in piece parts.
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetArrangementSpecific
            (
                bool arrangementSpecific /**  The arrangement specific state */
            );
            /**
                    Get the arrangement specific state of this @link Positioning::ComponentConstraint Positioning::ComponentConstraint@endlink  in the 
                    specified @link Assemblies::Arrangement Assemblies::Arrangement@endlink .
                 @return   The arrangement specific state.  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool GetSpecificInArrangement
            (
                NXOpen::Assemblies::Arrangement * arrangement /**  The @link Assemblies::Arrangement Assemblies::Arrangement@endlink  in which the arrangement specific state is being enquired. */
            );
            /**
                    Set the arrangement specific state of this @link Positioning::ComponentConstraint Positioning::ComponentConstraint@endlink  in the 
                    specified @link Assemblies::Arrangement Assemblies::Arrangement@endlink .
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetSpecificInArrangement
            (
                NXOpen::Assemblies::Arrangement * arrangement /**  The @link Assemblies::Arrangement Assemblies::Arrangement@endlink  in which the arrangement specific state is being set. */,
                bool arrangementSpecific /**  The arrangement specific state. */
            );
            /**
                    Get the suppression state of this @link Positioning::ComponentConstraint Positioning::ComponentConstraint@endlink  in the 
                    specified @link Assemblies::Arrangement Assemblies::Arrangement@endlink .  If the constraint is not arrangement
                    specific in this arrangement then the shared suppression state, used across all 
                    arrangements where the constraint is not arrangement specific, is used.
                 @return   The suppression state.  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: bool GetSuppressedInArrangement
            (
                NXOpen::Assemblies::Arrangement * arrangement /**  The @link Assemblies::Arrangement Assemblies::Arrangement@endlink  in which the suppression state is being enquired. */
            );
            /**
                    Set the suppression state of this @link Positioning::ComponentConstraint Positioning::ComponentConstraint@endlink  in the 
                    specified @link Assemblies::Arrangement Assemblies::Arrangement@endlink .  If the constraint is not arrangement
                    specific in this arrangement then the shared suppression state, used across all 
                    arrangements where the constraint is not arrangement specific, is set.
                 <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetSuppressedInArrangement
            (
                NXOpen::Assemblies::Arrangement * arrangement /**  The @link Assemblies::Arrangement Assemblies::Arrangement@endlink  in which the suppression state is being set. */,
                bool suppressed /**  The suppression state. */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif