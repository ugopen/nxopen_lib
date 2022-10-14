#ifndef NXOpen_CAE_CORRELMODEPAIRINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELMODEPAIRINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelModePairingBuilder.ja
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
        class CorrelModePairingBuilder;
    }
    namespace CAE
    {
        class CorrelBaseBuilder;
    }
    namespace CAE
    {
        class _CorrelModePairingBuilderBuilder;
        class CorrelModePairingBuilderImpl;
        /** This builder is used to control the mode pairing behavior of a @link NXOpen::CAE::CorrelSolution NXOpen::CAE::CorrelSolution@endlink   <br> To create a new instance of this class, use @link NXOpen::CAE::CorrelSolution::CreateModePairingBuilder  NXOpen::CAE::CorrelSolution::CreateModePairingBuilder @endlink  <br> 
         <br>  Created in NX6.0.1.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelModePairingBuilder : public NXOpen::CAE::CorrelBaseBuilder
        {
            /** The automatic pairing rule type */
            public: enum Auto
            {
                AutoNone/** not automatic */,
                AutoSequential/** by mode numbers */,
                AutoFrequency/** by frequency */,
                AutoMac/** by mac metric */,
                AutoFreqMac/** by frequency AND mac */
            };

            private: CorrelModePairingBuilderImpl * m_correlmodepairingbuilder_impl;
            private: friend class  _CorrelModePairingBuilderBuilder;
            protected: CorrelModePairingBuilder();
            public: ~CorrelModePairingBuilder();
            /**Returns  the automatic pairing rule 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CorrelModePairingBuilder::Auto AutomaticRule
            (
            );
            /**Sets  the automatic pairing rule 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetAutomaticRule
            (
                NXOpen::CAE::CorrelModePairingBuilder::Auto rule /** rule */ 
            );
            /**Returns  the frequency-pairing tolerance 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: double FrequencyTolerance
            (
            );
            /**Sets  the frequency-pairing tolerance 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetFrequencyTolerance
            (
                double frequencyTol /** frequency tol */ 
            );
            /**Returns  the minimum MAC allowable for pairing by MAC 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: double MacLowerBound
            (
            );
            /**Sets  the minimum MAC allowable for pairing by MAC 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetMacLowerBound
            (
                double macLowerBound /** mac lower bound */ 
            );
            /** Add a manually paired mode pair 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void AddManualPair
            (
                int refModeId /** Reference mode ID */,
                int workModeId /** Work mode ID */
            );
            /** Remove a manually paired mode pair 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void RemoveManualPair
            (
                int refModeId /** Reference mode ID */,
                int workModeId /** Work mode ID */
            );
            /** Clear all manually paired mode pairs 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ClearAllManualPairs
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