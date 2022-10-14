#ifndef NXOpen_CAE_SIMAUTOBCRECIPE_HXX_INCLUDED
#define NXOpen_CAE_SIMAUTOBCRECIPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimAutoBcRecipe.ja
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
#include <NXOpen/CAE_SimRecipe.hxx>
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
        class SimAutoBcRecipe;
    }
    namespace CAE
    {
        class SimBC;
    }
    namespace CAE
    {
        class SimRecipe;
    }
    namespace CAE
    {
        class _SimAutoBcRecipeBuilder;
        class SimAutoBcRecipeImpl;
        /** 
               @brief  Represents a simulation recipe containing the parameters needed 
              for the generation of a set of face pairs from the faces/bodies in the model  

         
              <br> To create a new instance of this class, use @link CAE::SimRecipeCollection::CreateAutoBcRecipe  CAE::SimRecipeCollection::CreateAutoBcRecipe @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimAutoBcRecipe : public CAE::SimRecipe
        {
            private: SimAutoBcRecipeImpl * m_simautobcrecipe_impl;
            private: friend class  _SimAutoBcRecipeBuilder;
            protected: SimAutoBcRecipe();
            public: ~SimAutoBcRecipe();
            /** Get the list of @link CAE::SimBC CAE::SimBC@endlink     
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetBcList
            (
                std::vector<NXOpen::CAE::SimBC *> & bcList /** BCs generated from recipe */
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