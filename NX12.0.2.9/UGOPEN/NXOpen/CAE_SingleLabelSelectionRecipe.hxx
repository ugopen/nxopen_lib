#ifndef NXOpen_CAE_SINGLELABELSELECTIONRECIPE_HXX_INCLUDED
#define NXOpen_CAE_SINGLELABELSELECTIONRECIPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SingleLabelSelectionRecipe.ja
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
#include <NXOpen/CAE_AttributeSelectionRecipe.hxx>
#include <NXOpen/CAE_SelectionRecipe.hxx>
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
        class SingleLabelSelectionRecipe;
    }
    namespace CAE
    {
        class SelectionRecipe;
    }
    namespace CAE
    {
        class _SingleLabelSelectionRecipeBuilder;
        class SingleLabelSelectionRecipeImpl;
        /**  @brief  Represents a Selection Recipe based on a single Node Label  

          <br> To obtain an instance of this object use one of the creators in @link NXOpen::CAE::SelectionRecipeCollection NXOpen::CAE::SelectionRecipeCollection@endlink .  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SingleLabelSelectionRecipe : public NXOpen::CAE::SelectionRecipe
        {
            private: SingleLabelSelectionRecipeImpl * m_singlelabelselectionrecipe_impl;
            private: friend class  _SingleLabelSelectionRecipeBuilder;
            protected: SingleLabelSelectionRecipe();
            public: ~SingleLabelSelectionRecipe();
            /**Returns  the Node Label. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int Label
            (
            );
            /** Set the Node Label. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetLabel
            (
                int label /** label */ 
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
