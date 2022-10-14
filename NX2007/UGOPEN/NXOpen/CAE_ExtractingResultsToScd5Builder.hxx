#ifndef NXOpen_CAE_EXTRACTINGRESULTSTOSCD5BUILDER_HXX_INCLUDED
#define NXOpen_CAE_EXTRACTINGRESULTSTOSCD5BUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ExtractingResultsToScd5Builder.ja
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
#include <NXOpen/CAE_ExtractingResultsToScd5OutputSettings.hxx>
#include <NXOpen/CAE_ResultsManipulationInputSettings.hxx>
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
        class ExtractingResultsToScd5Builder;
    }
    class Builder;
    namespace CAE
    {
        class ExtractingResultsToScd5OutputSettings;
    }
    namespace CAE
    {
        class ResultsManipulationInputSettings;
    }
    namespace CAE
    {
        class _ExtractingResultsToScd5BuilderBuilder;
        class ExtractingResultsToScd5BuilderImpl;
        /**  @brief 
                Represents a @link NXOpen::CAE::ExtractingResultsToScd5Builder NXOpen::CAE::ExtractingResultsToScd5Builder@endlink  to
                extract the specified results on selected entities into SCD5 file.
                 

         
                
                <ol>
                <li>
                The outputs are based on nodes or elements according to the results, if input entities are groups
                or selection recipes, nodes and elements will be retrieved from these entities.
                </li>
                <li>
                You can specify the option for incompatible result.
                </li>
                <li>
                You can specify the output units system.
                </li>
                </ol>
                
             <br> To create a new instance of this class, use @link NXOpen::CAE::ResultManager::CreateExtractingResultsToScd5Builder  NXOpen::CAE::ResultManager::CreateExtractingResultsToScd5Builder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ExtractingResultsToScd5Builder : public NXOpen::Builder
        {
            private: ExtractingResultsToScd5BuilderImpl * m_extractingresultstoscd5builder_impl;
            private: friend class  _ExtractingResultsToScd5BuilderBuilder;
            protected: ExtractingResultsToScd5Builder();
            public: ~ExtractingResultsToScd5Builder();
            /**Returns  the input settings 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::ResultsManipulationInputSettings * InputSettings
            (
            );
            /**Returns  the output settings 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::ExtractingResultsToScd5OutputSettings * OutputSettings
            (
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