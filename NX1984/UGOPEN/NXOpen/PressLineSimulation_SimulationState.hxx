#ifndef NXOpen_PRESSLINESIMULATION_SIMULATIONSTATE_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_SIMULATIONSTATE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_SimulationState.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libpresslinesimulopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PressLineSimulation
    {
        class SimulationState;
    }
    class NXObject;
    namespace PressLineSimulation
    {
        class _SimulationStateBuilder;
        class SimulationStateImpl;
        /** This class represents a simulation state of the simulation.
            The simulation state stores the current angle of the simulation. <br> Use the @link NXOpen::PressLineSimulation::SimulationSetup NXOpen::PressLineSimulation::SimulationSetup@endlink  class to obtain an instances of this class.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  SimulationState : public NXOpen::NXObject
        {
            private: SimulationStateImpl * m_simulationstate_impl;
            private: friend class  _SimulationStateBuilder;
            protected: SimulationState();
            public: ~SimulationState();
            /**Sets  the current angle of the simulation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetSimulationAngle
            (
                double theCurrentAngle /** thecurrentangle */ 
            );
            /**Returns  the current angle of the simulation 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: double SimulationAngle
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