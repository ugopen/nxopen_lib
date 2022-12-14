#ifndef NXOpen_CAE_FLUIDDOMAINRECIPE_HXX_INCLUDED
#define NXOpen_CAE_FLUIDDOMAINRECIPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FluidDomainRecipe.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class FluidDomainRecipe;
    }
    namespace CAE
    {
        class CfdContactPreventionConstraint;
    }
    namespace CAE
    {
        class CfdLocalResolutionConstraint;
    }
    namespace CAE
    {
        class _FluidDomainRecipeBuilder;
        class FluidDomainRecipeImpl;
        /**  @brief  Represents a FluidDomainRecipe  

           <br> To create or edit an instance of this class, use @link CAE::FluidDomainBuilder  CAE::FluidDomainBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  FluidDomainRecipe : public TaggedObject
        {
            private: FluidDomainRecipeImpl * m_fluiddomainrecipe_impl;
            private: friend class  _FluidDomainRecipeBuilder;
            protected: FluidDomainRecipe();
            public: ~FluidDomainRecipe();
            /** Sets the name of the fluid domain recipe
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            public: void SetName
            (
                const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the name of the fluid domain recipe
                    
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            void SetName
            (
                const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the name of the fluid domain recipe  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            public: NXString GetName
            (
            );
            /** Adds a @link CAE::CfdLocalResolutionConstraint CAE::CfdLocalResolutionConstraint@endlink  constraint
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            public: void AddLocalResolutionConstraint
            (
                NXOpen::CAE::CfdLocalResolutionConstraint * localResolutionConstraint /** localresolutionconstraint */ 
            );
            /** Removes a @link CAE::CfdLocalResolutionConstraint CAE::CfdLocalResolutionConstraint@endlink  constraint
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            public: void RemoveLocalResolutionConstraint
            (
                NXOpen::CAE::CfdLocalResolutionConstraint * localResolutionConstraint /** localresolutionconstraint */ 
            );
            /** Adds a @link CAE::CfdContactPreventionConstraint CAE::CfdContactPreventionConstraint@endlink  constraint
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            public: void AddContactPreventionConstraint
            (
                NXOpen::CAE::CfdContactPreventionConstraint * contactPreventionConstraint /** contactpreventionconstraint */ 
            );
            /** Removes a @link CAE::CfdContactPreventionConstraint CAE::CfdContactPreventionConstraint@endlink  constraint
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_adv_fluid_mod ("NX Advanced Fluid Modeling") */
            public: void RemoveContactPreventionConstraint
            (
                NXOpen::CAE::CfdContactPreventionConstraint * contactPreventionConstraint /** contactpreventionconstraint */ 
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
