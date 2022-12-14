#ifndef NXOpen_CAE_CORRELMODECLUSTERINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELMODECLUSTERINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelModeClusteringBuilder.ja
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
#include <NXOpen/CAE_CorrelBaseBuilder.hxx>
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
        class CorrelModeClusteringBuilder;
    }
    namespace CAE
    {
        class CorrelBaseBuilder;
    }
    namespace CAE
    {
        class _CorrelModeClusteringBuilderBuilder;
        class CorrelModeClusteringBuilderImpl;
        /** This builder is used to control the mode clustering behavior of a @link NXOpen::CAE::CorrelSolution NXOpen::CAE::CorrelSolution@endlink   <br> To create a new instance of this class, use @link NXOpen::CAE::CorrelSolution::CreateModeClusteringBuilder  NXOpen::CAE::CorrelSolution::CreateModeClusteringBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelModeClusteringBuilder : public NXOpen::CAE::CorrelBaseBuilder
        {
            private: CorrelModeClusteringBuilderImpl * m_correlmodeclusteringbuilder_impl;
            private: friend class  _CorrelModeClusteringBuilderBuilder;
            protected: CorrelModeClusteringBuilder();
            public: ~CorrelModeClusteringBuilder();
            /** Add a mode cluster 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void AddCluster
            (
                const std::vector<int> & refModes /** refmodes */ ,
                const std::vector<int> & workModes /** workmodes */ 
            );
            /** Modify a mode cluster 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ModifyCluster
            (
                int clusterIndex /** clusterindex */ ,
                const std::vector<int> & refModes /** refmodes */ ,
                const std::vector<int> & workModes /** workmodes */ 
            );
            /** Remove a mode cluster 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void RemoveCluster
            (
                int clusterIndex /** clusterindex */ 
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
