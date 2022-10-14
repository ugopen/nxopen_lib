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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAE_CorrelModePairingBuilder.hxx>
#include <NXOpen/CAE_CorrelBaseBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** This builder is used to control the mode pairing behavior of a @link CAE::CorrelSolution CAE::CorrelSolution@endlink   <br> To create a new instance of this class, use @link CAE::CorrelSolution::CreateModePairingBuilder CAE::CorrelSolution::CreateModePairingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CorrelModePairingBuilder : public CAE::CorrelBaseBuilder
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

            private: friend class  _CorrelModePairingBuilderBuilder;
            protected: CorrelModePairingBuilder();
            /**Returns  the automatic pairing rule  <br> License requirements : None */
            public: NXOpen::CAE::CorrelModePairingBuilder::Auto AutomaticRule
            (
            );
            /**Sets  the automatic pairing rule  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetAutomaticRule
            (
                NXOpen::CAE::CorrelModePairingBuilder::Auto rule /** rule */ 
            );
            /**Returns  the frequency-pairing tolerance  <br> License requirements : None */
            public: double FrequencyTolerance
            (
            );
            /**Sets  the frequency-pairing tolerance  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetFrequencyTolerance
            (
                double frequencyTol /** frequency tol */ 
            );
            /**Returns  the minimum MAC allowable for pairing by MAC  <br> License requirements : None */
            public: double MacLowerBound
            (
            );
            /**Sets  the minimum MAC allowable for pairing by MAC  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetMacLowerBound
            (
                double macLowerBound /** mac lower bound */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif