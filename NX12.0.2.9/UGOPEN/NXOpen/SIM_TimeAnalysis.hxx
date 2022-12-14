#ifndef NXOpen_SIM_TIMEANALYSIS_HXX_INCLUDED
#define NXOpen_SIM_TIMEANALYSIS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_TimeAnalysis.ja
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
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class TimeAnalysis;
    }
    namespace SIM
    {
        class _TimeAnalysisBuilder;
        class TimeAnalysisImpl;
        /**  @brief  Represents the TimeAnalysis class object  

            <br> These objects are created by the simulation for each channel.  <br> 
         <br>  Created in NX11.0.2.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  TimeAnalysis : public NXOpen::TaggedObject
        {
            private: TimeAnalysisImpl * m_timeanalysis_impl;
            private: friend class  _TimeAnalysisBuilder;
            protected: TimeAnalysis();
            public: ~TimeAnalysis();
            /** Start the Time Analysis
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Start
            (
            );
            /** Stop the Time Analysis
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Stop
            (
            );
            /** Reset the Time Analysis
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void Reset
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
