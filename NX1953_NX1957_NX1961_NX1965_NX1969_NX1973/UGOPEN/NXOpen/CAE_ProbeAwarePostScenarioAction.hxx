#ifndef NXOpen_CAE_PROBEAWAREPOSTSCENARIOACTION_HXX_INCLUDED
#define NXOpen_CAE_PROBEAWAREPOSTSCENARIOACTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ProbeAwarePostScenarioAction.ja
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
#include <NXOpen/CAE_PostScenarioAction.hxx>
#include <NXOpen/CAE_PostScenarioAction.hxx>
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
        class ProbeAwarePostScenarioAction;
    }
    namespace CAE
    {
        class PostScenarioAction;
    }
    class Unit;
    namespace CAE
    {
        class ProbeAwarePostScenarioActionImpl;

        /// \cond NX_NO_DOC 
        /**  @brief A post scenario action that can be launched from a post scenario which creates 2D graphs and its result depends on the position of probing cursors.  

         
              *
              * See also @link CAE::PostScenario::GetAvailableActions CAE::PostScenario::GetAvailableActions@endlink .
               <br> No support for KF.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ProbeAwarePostScenarioAction : public NXOpen::CAE::PostScenarioAction
        {
            private: ProbeAwarePostScenarioActionImpl * m_probeawarepostscenarioaction_impl;
            /// \cond NX_NO_DOC 
            public: explicit ProbeAwarePostScenarioAction(void *ptr);
            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Specify the probe location for primary abscissa axes (usually known as X). 

             
                      *
                      * The values array are values and not indices. The values and units lists must have the same length. There shall be one value per axis.
                      
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddXProbeInfo
            (
                int graphIndex /** the index of the graph this applies to */,
                const std::vector<double> & values /** values */ ,
                const std::vector<NXOpen::Unit *> & units /** units */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Specify the probe location for secondary abscissa axes (usually rendered vertically). 

             
                      *
                      * The values array are values and not indices. The values and units lists must have the same length. There shall be one value per axis.
                      
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddZProbeInfo
            (
                int graphIndex /** the index of the graph this applies to */,
                const std::vector<double> & values /** values */ ,
                const std::vector<NXOpen::Unit *> & units /** units */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Specify the probe location for an order probe. 

             
                      *
                      * Order probes can be found in Color Map displays, and represent the directly proportional relation between RPM speeds and harmonic frequency
                      
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddOrderProbeInfo
            (
                int graphIndex /** the index of the graph this applies to */,
                double value /** value */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Specify the probe location for an angle probe. 

             
                      
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddAngleProbeInfo
            (
                int graphIndex /** the index of the graph this applies to */,
                double value /** value */ ,
                NXOpen::Unit * unit /** unit */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Retrieve available primary abscissa axes measures. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetAvailableXAxisMeasures
            (
                int graphIndex /** graph index */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Retrieve available secondary abscissa axes measures. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetAvailableZAxisMeasures
            (
                int graphIndex /** graph index */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Check if this plot supports an order probe.
                      *
                      * See @link CAE::ProbeAwarePostScenarioAction::AddOrderProbeInfo CAE::ProbeAwarePostScenarioAction::AddOrderProbeInfo@endlink 
                      
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsOrderProbeSupported
            (
                int graphIndex /** graph index */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Check if this plot supports an angle probe.
                      
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsAngleProbeSupported
            (
                int graphIndex /** graph index */ 
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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
