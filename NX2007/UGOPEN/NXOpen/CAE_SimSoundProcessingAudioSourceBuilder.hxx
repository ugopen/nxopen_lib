#ifndef NXOpen_CAE_SIMSOUNDPROCESSINGAUDIOSOURCEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SIMSOUNDPROCESSINGAUDIOSOURCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimSoundProcessingAudioSourceBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/CAE_SimSoundProcessingSourceBuilder.hxx>
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
        class SimSoundProcessingAudioSourceBuilder;
    }
    namespace CAE
    {
        class SimSoundProcessingSourceBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _SimSoundProcessingAudioSourceBuilderBuilder;
        class SimSoundProcessingAudioSourceBuilderImpl;
        /** The builder class for @link NXOpen::CAE::SimSoundProcessingAudioSource NXOpen::CAE::SimSoundProcessingAudioSource@endlink .  <br> There is no kf creator for this.  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimSoundProcessingAudioSourceBuilder : public NXOpen::CAE::SimSoundProcessingSourceBuilder
        {
            private: SimSoundProcessingAudioSourceBuilderImpl * m_simsoundprocessingaudiosourcebuilder_impl;
            private: friend class  _SimSoundProcessingAudioSourceBuilderBuilder;
            protected: SimSoundProcessingAudioSourceBuilder();
            public: ~SimSoundProcessingAudioSourceBuilder();
            /**Returns  the file path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FileName
            (
            );
            /**Sets  the file path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFileName
            (
                const NXString & fileName /** filename */ 
            );
            /**Sets  the file path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetFileName
            (
                const char * fileName /** filename */ 
            );
            /**Returns  the option to enable setting the upper time limit 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool EnableWavUpperTimeLimit
            (
            );
            /**Sets  the option to enable setting the upper time limit 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEnableWavUpperTimeLimit
            (
                bool enableWavUpperTimeLimit /** enablewavuppertimelimit */ 
            );
            /**Returns  the upper limit, in time units (seconds) 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WavUpperTimeLimit
            (
            );
            /** Play the selected file. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Play
            (
                bool playInLoop /** playinloop */ 
            );
            /** Stop playing. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Stop
            (
            );
            /** Plot the content of the selected audio file. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Plot
            (
                int deviceIndex /** deviceindex */ ,
                int viewportIndex /** viewportindex */ 
            );
            /**Returns  the flag to enable normalization of the audio signals 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool EnableNormalization
            (
            );
            /**Sets  the flag to enable normalization of the audio signals 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEnableNormalization
            (
                bool enableNormalization /** enablenormalization */ 
            );
            /**Returns  the flag specifying the normalization type, rms or peak 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool RmsNormalization
            (
            );
            /**Sets  the flag specifying the normalization type, rms or peak 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetRmsNormalization
            (
                bool rmsNormalization /** rmsnormalization */ 
            );
            /**Returns  the normalization value in dB 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: int NormalizationValue
            (
            );
            /**Sets  the normalization value in dB 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNormalizationValue
            (
                int normalizationValue /** normalizationvalue */ 
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