#ifndef NXOpen_CAE_ENERGYDISTRIBUTIONTABLEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ENERGYDISTRIBUTIONTABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_EnergyDistributionTableBuilder.ja
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
#include <NXOpen/CAE_EnergyDistributionTableResultGroupData.hxx>
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
        class EnergyDistributionTableBuilder;
    }
    class Builder;
    namespace CAE
    {
        class BaseIteration;
    }
    namespace CAE
    {
        class BaseLoadcase;
    }
    namespace CAE
    {
        class BaseResultType;
    }
    namespace CAE
    {
        class CaeGroup;
    }
    namespace CAE
    {
        class EnergyDistributionTableResultGroupData;
    }
    namespace CAE
    {
        class Result;
    }
    namespace CAE
    {
        class _EnergyDistributionTableBuilderBuilder;
        class EnergyDistributionTableBuilderImpl;
        /** This builder is meant energy distribution per Caegroup. Build is used to export energy distribution
                per Group in set groups in xls file. It also exports energy distribution per Physical Property in group. <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateEnergyDistributionTableBuilder  NXOpen::CAE::SimSimulation::CreateEnergyDistributionTableBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  EnergyDistributionTableBuilder : public NXOpen::Builder
        {
            private: EnergyDistributionTableBuilderImpl * m_energydistributiontablebuilder_impl;
            private: friend class  _EnergyDistributionTableBuilderBuilder;
            protected: EnergyDistributionTableBuilder();
            public: ~EnergyDistributionTableBuilder();
            /**Returns  the result 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Result * Result
            (
            );
            /**Sets  the result 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: void SetResult
            (
                NXOpen::CAE::Result * result /** result */ 
            );
            /**Returns  the load case 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::BaseLoadcase * LoadCase
            (
            );
            /**Sets  the load case 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: void SetLoadCase
            (
                NXOpen::CAE::BaseLoadcase * iLoadCase /** iloadcase */ 
            );
            /**Returns  the iteration 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::BaseIteration * Iteration
            (
            );
            /**Sets  the iteration 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: void SetIteration
            (
                NXOpen::CAE::BaseIteration * iIteration /** iiteration */ 
            );
            /**Returns  the result type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::BaseResultType * ResultType
            (
            );
            /**Sets  the result type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: void SetResultType
            (
                NXOpen::CAE::BaseResultType * resulttype /** resulttype */ 
            );
            /** Get cae groups from simulation file  @return  simulation groups 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::CaeGroup *> GetGroups
            (
            );
            /** Set cae groups from simulation file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: void SetGroups
            (
                const std::vector<NXOpen::CAE::CaeGroup *> & objects /** objects */ 
            );
            /** Export result file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: void Export
            (
                const NXString & iAbsoluteFilePath /** iabsolutefilepath */ 
            );
            /** Export result file 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            void Export
            (
                const char * iAbsoluteFilePath /** iabsolutefilepath */ 
            );
            /** Retreive computed result data  @return  computed result data 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_nv_modeling ("Simcenter Noise and Vibration modeling") */
            public: std::vector<NXOpen::CAE::EnergyDistributionTableResultGroupData *> GetResults
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