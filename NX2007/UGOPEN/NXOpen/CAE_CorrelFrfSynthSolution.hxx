#ifndef NXOpen_CAE_CORRELFRFSYNTHSOLUTION_HXX_INCLUDED
#define NXOpen_CAE_CORRELFRFSYNTHSOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelFrfSynthSolution.ja
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
#include <NXOpen/CAE_CorrelFrfSolution.hxx>
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
        class CorrelFrfSynthSolution;
    }
    namespace CAE
    {
        class CorrelFrfSolution;
    }
    namespace CAE
    {
        class _CorrelFrfSynthSolutionBuilder;
        class CorrelFrfSynthSolutionImpl;
        /** Represents a @link NXOpen::CAE::CorrelFrfSynthSolution NXOpen::CAE::CorrelFrfSynthSolution@endlink ,
                which is a meta-solution used to compare results from two structural dynamics solutions  <br> To create or edit an instance of this class, use @link NXOpen::CAE::CorrelSolutionBuilder  NXOpen::CAE::CorrelSolutionBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelFrfSynthSolution : public NXOpen::CAE::CorrelFrfSolution
        {
            private: CorrelFrfSynthSolutionImpl * m_correlfrfsynthsolution_impl;
            private: friend class  _CorrelFrfSynthSolutionBuilder;
            protected: CorrelFrfSynthSolution();
            public: ~CorrelFrfSynthSolution();
            /** Show Mode information. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ShowModeInformation
            (
            );
            /** Set Active Mode flag. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveWorkMode
            (
                int index /** index */ ,
                bool isActive /** isactive */ 
            );
            /** Set multiple Active Mode flags. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveWorkModes
            (
                const std::vector<int> & indices /** indices */ ,
                const std::vector<bool> & isActive /** isactive */ 
            );
            /** Set Damping value. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDampingValue
            (
                int index /** index */ ,
                double value /** value */ 
            );
            /** Set multiple Damping values. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDampingValues
            (
                const std::vector<int> & indices /** indices */ ,
                const std::vector<double> & values /** values */ 
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