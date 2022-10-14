#ifndef NXOpen_CAE_CACHERESULTRECIPEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CACHERESULTRECIPEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CacheResultRecipeBuilder.ja
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
#include <NXOpen/CAE_BaseIteration.hxx>
#include <NXOpen/Builder.hxx>
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
        class CacheResultRecipeBuilder;
    }
    class Builder;
    namespace CAE
    {
        class BaseIteration;
    }
    namespace CAE
    {
        class BaseResultType;
    }
    namespace CAE
    {
        class _CacheResultRecipeBuilderBuilder;
        class CacheResultRecipeBuilderImpl;
        /** Represents a @link NXOpen::CAE::CacheResultRecipeBuilder NXOpen::CAE::CacheResultRecipeBuilder@endlink  
                Cached result types will used during the post processing workflows.
                Once result type are cached those will used instead of loading the 
                result type again  <br> To obtain an instance of this class use @link NXOpen::Session::ResultManager NXOpen::Session::ResultManager@endlink .  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CacheResultRecipeBuilder : public NXOpen::Builder
        {
            private: CacheResultRecipeBuilderImpl * m_cacheresultrecipebuilder_impl;
            private: friend class  _CacheResultRecipeBuilderBuilder;
            protected: CacheResultRecipeBuilder();
            public: ~CacheResultRecipeBuilder();
            /** Set result type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetEquivalentResultType
            (
                NXOpen::CAE::BaseResultType * restype /** restype */ 
            );
            /**Returns  the enum to filter iteration 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::BaseIteration::IterationValueType IterationValueTypeFilter
            (
            );
            /**Sets  the enum to filter iteration 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetIterationValueTypeFilter
            (
                NXOpen::CAE::BaseIteration::IterationValueType filterIteration /** filteriteration */ 
            );
            /** Set start iteration 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetStartIteration
            (
                NXOpen::CAE::BaseIteration * iteration /** iteration */ 
            );
            /** Set end iteration 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetEndIteration
            (
                NXOpen::CAE::BaseIteration * iteration /** iteration */ 
            );
            /**Returns  the step spacing to be used between the start and end iteration. 
                        This option can be used to reduce the amount of data cached. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int IterationStepSpacing
            (
            );
            /**Sets  the step spacing to be used between the start and end iteration. 
                        This option can be used to reduce the amount of data cached. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetIterationStepSpacing
            (
                int iterationStepSpacing /** iterationstepspacing */ 
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