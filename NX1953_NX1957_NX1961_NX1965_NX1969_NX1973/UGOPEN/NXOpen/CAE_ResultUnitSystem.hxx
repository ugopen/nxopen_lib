#ifndef NXOpen_CAE_RESULTUNITSYSTEM_HXX_INCLUDED
#define NXOpen_CAE_RESULTUNITSYSTEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultUnitSystem.ja
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
        class ResultUnitSystem;
    }
    class Unit;
    namespace CAE
    {
        class _ResultUnitSystemBuilder;
        class ResultUnitSystemImpl;
        /**
            Represents a @link NXOpen::CAE::ResultUnitSystem NXOpen::CAE::ResultUnitSystem@endlink 
             <br> To obtain an instance of this class use @link NXOpen::Session::ResultManager NXOpen::Session::ResultManager@endlink .  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultUnitSystem : public NXOpen::TaggedObject
        {
            private: ResultUnitSystemImpl * m_resultunitsystem_impl;
            private: friend class  _ResultUnitSystemBuilder;
            protected: ResultUnitSystem();
            public: ~ResultUnitSystem();
            /**Returns  the unit of mass 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * MassUnit
            (
            );
            /**Sets  the unit of mass 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetMassUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of length 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * LengthUnit
            (
            );
            /**Sets  the unit of length 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLengthUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of time 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * TimeUnit
            (
            );
            /**Sets  the unit of time 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetTimeUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of temperature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * TemperatureUnit
            (
            );
            /**Sets  the unit of temperature 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetTemperatureUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of electric charge 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * ElectricChargeUnit
            (
            );
            /**Sets  the unit of electric charge 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetElectricChargeUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of temperature difference 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * DeltaTemperatureUnit
            (
            );
            /**Sets  the unit of temperature difference 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDeltaTemperatureUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of angle 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * AngleUnit
            (
            );
            /**Sets  the unit of angle 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetAngleUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of Lumious Intensity  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * LumiousIntensityUnit
            (
            );
            /**Sets  the unit of Lumious Intensity  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetLumiousIntensityUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /**Returns  the unit of Amount Of Substance   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::Unit * AmountOfSubstanceUnit
            (
            );
            /**Sets  the unit of Amount Of Substance   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetAmountOfSubstanceUnit
            (
                NXOpen::Unit * unit /** unit */ 
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