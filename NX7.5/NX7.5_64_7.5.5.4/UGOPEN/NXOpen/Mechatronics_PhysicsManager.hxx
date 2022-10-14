#ifndef NXOpen_MECHATRONICS_PHYSICSMANAGER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_PHYSICSMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PhysicsManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class PhysicsManager;
    }
    class Part;
    namespace Mechatronics
    {
        class AngularLimitJointCollection;
    }
    namespace Mechatronics
    {
        class AngularSpringJointCollection;
    }
    namespace Mechatronics
    {
        class BallJointCollection;
    }
    namespace Mechatronics
    {
        class BreakingConstraintCollection;
    }
    namespace Mechatronics
    {
        class CamCollection;
    }
    namespace Mechatronics
    {
        class ChangeMaterialCollection;
    }
    namespace Mechatronics
    {
        class CollisionBodyCollection;
    }
    namespace Mechatronics
    {
        class CollisionMaterialCollection;
    }
    namespace Mechatronics
    {
        class CollisionSensorCollection;
    }
    namespace Mechatronics
    {
        class CylindricalJointCollection;
    }
    namespace Mechatronics
    {
        class FixedJointCollection;
    }
    namespace Mechatronics
    {
        class GearCollection;
    }
    namespace Mechatronics
    {
        class HingeJointCollection;
    }
    namespace Mechatronics
    {
        class LinearLimitJointCollection;
    }
    namespace Mechatronics
    {
        class LinearSpringJointCollection;
    }
    namespace Mechatronics
    {
        class MotionProfileCollection;
    }
    namespace Mechatronics
    {
        class ObjectSinkCollection;
    }
    namespace Mechatronics
    {
        class ObjectSourceCollection;
    }
    namespace Mechatronics
    {
        class PositionControlCollection;
    }
    namespace Mechatronics
    {
        class PreferencesBuilder;
    }
    namespace Mechatronics
    {
        class PreventCollisionCollection;
    }
    namespace Mechatronics
    {
        class RigidBodyCollection;
    }
    namespace Mechatronics
    {
        class RuntimeBehaviorCollection;
    }
    namespace Mechatronics
    {
        class SlidingJointCollection;
    }
    namespace Mechatronics
    {
        class SpeedControlCollection;
    }
    namespace Mechatronics
    {
        class TransportSurfaceCollection;
    }
    namespace Mechatronics
    {
        class PhysicsManagerImpl;
        /** A manager to deal with all physics objects.  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
        class NXOPENCPPEXPORT  PhysicsManager
        {
            private: PhysicsManagerImpl * m_physicsmanager_impl;
            private: NXOpen::Part* m_owner;
            /** Constructor */
            public: explicit PhysicsManager(NXOpen::Part *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PhysicsManager();
            /** Creates a @link Mechatronics::PreferencesBuilder Mechatronics::PreferencesBuilder@endlink  object.  @return  Mechatronics Preferences builder <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::PreferencesBuilder * CreatePreferenceBuilder
            (
            );


            /** Returns the @link Mechatronics::RigidBodyCollection  Mechatronics::RigidBodyCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::RigidBodyCollection *RigidBodies();
            /** Returns the @link Mechatronics::CollisionBodyCollection  Mechatronics::CollisionBodyCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::CollisionBodyCollection *CollisionBodies();
            /** Returns the @link Mechatronics::MotionProfileCollection  Mechatronics::MotionProfileCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::MotionProfileCollection *MotionProfiles();
            /** Returns the @link Mechatronics::RuntimeBehaviorCollection  Mechatronics::RuntimeBehaviorCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::RuntimeBehaviorCollection *RuntimeBehaviors();
            /** Returns the @link Mechatronics::CollisionMaterialCollection  Mechatronics::CollisionMaterialCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::CollisionMaterialCollection *CollisionMaterials();
            /** Returns the @link Mechatronics::TransportSurfaceCollection  Mechatronics::TransportSurfaceCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::TransportSurfaceCollection *TransportSurfaces();
            /** Returns the @link Mechatronics::HingeJointCollection  Mechatronics::HingeJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::HingeJointCollection *HingeJoints();
            /** Returns the @link Mechatronics::SpeedControlCollection  Mechatronics::SpeedControlCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::SpeedControlCollection *SpeedControls();
            /** Returns the @link Mechatronics::PositionControlCollection  Mechatronics::PositionControlCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::PositionControlCollection *PositionControls();
            /** Returns the @link Mechatronics::SlidingJointCollection  Mechatronics::SlidingJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::SlidingJointCollection *SlidingJoints();
            /** Returns the @link Mechatronics::CollisionSensorCollection  Mechatronics::CollisionSensorCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::CollisionSensorCollection *CollisionSensors();
            /** Returns the @link Mechatronics::CylindricalJointCollection  Mechatronics::CylindricalJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::CylindricalJointCollection *CylindricalJoints();
            /** Returns the @link Mechatronics::FixedJointCollection  Mechatronics::FixedJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::FixedJointCollection *FixedJoints();
            /** Returns the @link Mechatronics::BallJointCollection  Mechatronics::BallJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::BallJointCollection *BallJoints();
            /** Returns the @link Mechatronics::AngularSpringJointCollection  Mechatronics::AngularSpringJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::AngularSpringJointCollection *AngularSpringJoints();
            /** Returns the @link Mechatronics::LinearSpringJointCollection  Mechatronics::LinearSpringJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::LinearSpringJointCollection *LinearSpringJoints();
            /** Returns the @link Mechatronics::GearCollection  Mechatronics::GearCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::GearCollection *Gears();
            /** Returns the @link Mechatronics::CamCollection  Mechatronics::CamCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::CamCollection *Cams();
            /** Returns the @link Mechatronics::AngularLimitJointCollection  Mechatronics::AngularLimitJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::AngularLimitJointCollection *AngularLimitJoints();
            /** Returns the @link Mechatronics::LinearLimitJointCollection  Mechatronics::LinearLimitJointCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::LinearLimitJointCollection *LinearLimitJoints();
            /** Returns the @link Mechatronics::BreakingConstraintCollection  Mechatronics::BreakingConstraintCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::BreakingConstraintCollection *BreakingConstraints();
            /** Returns the @link Mechatronics::PreventCollisionCollection  Mechatronics::PreventCollisionCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::PreventCollisionCollection *PreventCollisions();
            /** Returns the @link Mechatronics::ChangeMaterialCollection  Mechatronics::ChangeMaterialCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::ChangeMaterialCollection *ChangeMaterials();
            /** Returns the @link Mechatronics::ObjectSourceCollection  Mechatronics::ObjectSourceCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::ObjectSourceCollection *ObjectSources();
            /** Returns the @link Mechatronics::ObjectSinkCollection  Mechatronics::ObjectSinkCollection @endlink  belonging to this part */
            public: NXOpen::Mechatronics::ObjectSinkCollection *ObjectSinks();
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif