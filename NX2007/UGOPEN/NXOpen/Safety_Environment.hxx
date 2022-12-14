#ifndef NXOpen_SAFETY_ENVIRONMENT_HXX_INCLUDED
#define NXOpen_SAFETY_ENVIRONMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Safety_Environment.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/Safety_EnvSettingsBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libsafetyopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Safety
    {
        class Environment;
    }
    class Session;
    class Part;
    namespace Safety
    {
        class ArrangementManager;
    }
    namespace Safety
    {
        class BodyCollection;
    }
    namespace Safety
    {
        class BodyManager;
    }
    namespace Safety
    {
        class CharacteristicCollection;
    }
    namespace Safety
    {
        class CharacteristicManager;
    }
    namespace Safety
    {
        class ContactCollection;
    }
    namespace Safety
    {
        class ContactManager;
    }
    namespace Safety
    {
        class EnvSettingsBuilder;
    }
    namespace Safety
    {
        class FeModelCollection;
    }
    namespace Safety
    {
        class FeModelManager;
    }
    namespace Safety
    {
        class JointCollection;
    }
    namespace Safety
    {
        class JointManager;
    }
    namespace Safety
    {
        class ModelComponentCollection;
    }
    namespace Safety
    {
        class ModelComponentManager;
    }
    namespace Safety
    {
        class ModelSystemCollection;
    }
    namespace Safety
    {
        class ModelSystemManager;
    }
    namespace Safety
    {
        class RestraintCollection;
    }
    namespace Safety
    {
        class RestraintManager;
    }
    namespace Safety
    {
        class SolutionCollection;
    }
    namespace Safety
    {
        class SolutionManager;
    }
    namespace Safety
    {
        class SurfaceCollection;
    }
    namespace Safety
    {
        class SurfaceManager;
    }
    namespace Safety
    {
        class EnvironmentImpl;
        /** A manager for Safety application objects  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class SAFETYOPENCPPEXPORT  Environment
        {
            private: EnvironmentImpl * m_environment_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit Environment(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static Environment* theEnvironment;
            /** Returns the Environment object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static Environment* GetEnvironment(NXOpen::Session *owner);
            public: ~Environment();
            /** Ensures an environment for Safety appliction is created and initialized 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void InitializeEnvironment
            (
                NXOpen::Part * part /** part */ 
            );
            /** Returns the builder for environment settings 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Safety::EnvSettingsBuilder * GetEnvironmentSettingsBuilder
            (
                NXOpen::Part * part /** part */ 
            );


            /** Returns the model system manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::ModelSystemManager *ModelSystemManager();
            /** Returns the model component manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::ModelComponentManager *ModelComponentManager();
            /** Returns the arrangement manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::ArrangementManager *ArrangementManager();
            /** Returns the body manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::BodyManager *BodyManager();
            /** Returns the characteristic manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::CharacteristicManager *CharacteristicManager();
            /** Returns the contact manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::ContactManager *ContactManager();
            /** Returns the femodel manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::FeModelManager *FeModelManager();
            /** Returns the joint manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::JointManager *JointManager();
            /** Returns the restraint manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::RestraintManager *RestraintManager();
            /** Returns the solution manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::SolutionManager *SolutionManager();
            /** Returns the surface manager of this environment 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::SurfaceManager *SurfaceManager();
            /** Returns the @link NXOpen::Safety::ModelSystemCollection  NXOpen::Safety::ModelSystemCollection @endlink  belonging to this part 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::ModelSystemCollection *ModelSystems();
            /** Returns the @link NXOpen::Safety::ModelComponentCollection  NXOpen::Safety::ModelComponentCollection @endlink  belonging to this part 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::ModelComponentCollection *ModelCompnents();
            /** Returns the @link NXOpen::Safety::BodyCollection  NXOpen::Safety::BodyCollection @endlink  belonging to this part 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Safety::BodyCollection *Bodies();
            /** Returns the @link NXOpen::Safety::CharacteristicCollection  NXOpen::Safety::CharacteristicCollection @endlink  belonging to this part 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::CharacteristicCollection *Characteristics();
            /** Returns the @link NXOpen::Safety::ContactCollection  NXOpen::Safety::ContactCollection @endlink  belonging to this part 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Safety::ContactCollection *Contacts();
            /** Returns the @link NXOpen::Safety::FeModelCollection  NXOpen::Safety::FeModelCollection @endlink  belonging to this part 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Safety::FeModelCollection *FeModels();
            /** Returns the @link NXOpen::Safety::JointCollection  NXOpen::Safety::JointCollection @endlink  belonging to this part 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Safety::JointCollection *Joints();
            /** Returns the @link NXOpen::Safety::RestraintCollection  NXOpen::Safety::RestraintCollection @endlink  belonging to this part 
             <br>  Created in NX2007.0.0.  <br>  
            */
            public: NXOpen::Safety::RestraintCollection *Restraints();
            /** Returns the @link NXOpen::Safety::SurfaceCollection  NXOpen::Safety::SurfaceCollection @endlink  belonging to this part 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::Safety::SurfaceCollection *Surfaces();
            /** Returns the @link NXOpen::Safety::SolutionCollection  NXOpen::Safety::SolutionCollection @endlink  belonging to this part 
             <br>  Created in NX1980.0.0.  <br>  
            */
            public: NXOpen::Safety::SolutionCollection *Solution();
        }; //lint !e1712 default constructor not defined for class  

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
