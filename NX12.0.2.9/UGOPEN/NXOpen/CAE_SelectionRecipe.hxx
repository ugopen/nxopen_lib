#ifndef NXOpen_CAE_SELECTIONRECIPE_HXX_INCLUDED
#define NXOpen_CAE_SELECTIONRECIPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SelectionRecipe.ja
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
#include <NXOpen/CAE_SetObject.hxx>
#include <NXOpen/DisplayableObject.hxx>
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
        class SelectionRecipe;
    }
    namespace CAE
    {
        class SelectionRecipeDisplay;
    }
    class DisplayableObject;
    class TaggedObject;
    namespace CAE
    {
        class _SelectionRecipeBuilder;
        class SelectionRecipeImpl;
        /**
             Represents a class @link NXOpen::CAE::SelectionRecipe NXOpen::CAE::SelectionRecipe@endlink . 
             <br> This is an abstract class  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SelectionRecipe : public NXOpen::DisplayableObject
        {
            private: SelectionRecipeImpl * m_selectionrecipe_impl;
            private: friend class  _SelectionRecipeBuilder;
            protected: SelectionRecipe();
            public: ~SelectionRecipe();
            /** Gets the name of the Selection Recipe  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetName
            (
            );
            /** Sets the name of the Selection Recipe 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /** Sets the name of the Selection Recipe 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Returns Entity Types supported by the Selection Recipe. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void GetEntityTypes
            (
                std::vector<NXOpen::CAE::CaeSetGroupFilterType> & entityTypes /** Entity types to which this recipe resolves to.*/
            );
            /** Gets entities in the Selection Recipe.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetEntities
            (
            );
            /** Shows the contents of the Selection Recipe only. 
                        Note that @link CAE::FEElemEdge CAE::FEElemEdge@endlink , @link CAE::FEElemFace CAE::FEElemFace@endlink  and @link CAE::CAEEdge CAE::CAEEdge@endlink  
                        do not participate in this command. They are non-displayable entities and are never drawn individually in NX. Use 
                        @link NXOpen::CAE::SelectionRecipe::HasNonDisplayableEntities NXOpen::CAE::SelectionRecipe::HasNonDisplayableEntities@endlink  to determine if the Selection Recipe contains these entities.
                    
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void ShowContentsOnly
            (
            );
            /** Show the contents of the Selection Recipe.
                        Note that @link CAE::FEElemEdge CAE::FEElemEdge@endlink , @link CAE::FEElemFace CAE::FEElemFace@endlink  and @link CAE::CAEEdge CAE::CAEEdge@endlink  
                        do not participate in this command. They are non-displayable entities and are never drawn individually in NX. Use 
                        @link NXOpen::CAE::SelectionRecipe::HasNonDisplayableEntities NXOpen::CAE::SelectionRecipe::HasNonDisplayableEntities@endlink  to determine if the Selection Recipe contains these entities.
                    
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void ShowContents
            (
            );
            /** Hide the contents of the Selection Recipe.
                        Note that @link CAE::FEElemEdge CAE::FEElemEdge@endlink , @link CAE::FEElemFace CAE::FEElemFace@endlink  and @link CAE::CAEEdge CAE::CAEEdge@endlink  
                        do not participate in this command. They are non-displayable entities and are never drawn individually in NX. Use 
                        @link NXOpen::CAE::SelectionRecipe::HasNonDisplayableEntities NXOpen::CAE::SelectionRecipe::HasNonDisplayableEntities@endlink  to determine if the Selection Recipe contains these entities.
                    
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void HideContents
            (
            );
            /** Display information of this Selection Recipe 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: void Information
            (
            );
            /** Returns whether the Selection Recipe has non-displayable entities  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool HasNonDisplayableEntities
            (
            );


            /** Returns the display attributes belonging to the Selection Recipe 
             <br>  Created in NX12.0.0.  <br>  
            */
            public: NXOpen::CAE::SelectionRecipeDisplay *Display();
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
