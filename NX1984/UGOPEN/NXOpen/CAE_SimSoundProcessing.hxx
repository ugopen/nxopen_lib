#ifndef NXOpen_CAE_SIMSOUNDPROCESSING_HXX_INCLUDED
#define NXOpen_CAE_SIMSOUNDPROCESSING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimSoundProcessing.ja
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
        class SimSoundProcessing;
    }
    namespace CAE
    {
        class SimSoundProcessingImpulseResponsesCollection;
    }
    namespace CAE
    {
        class SimSoundProcessingSourcesCollection;
    }
    namespace CAE
    {
        class SimSoundProcessingTracksCollection;
    }
    namespace CAE
    {
        class SimSoundProcessingTreatmentsCollection;
    }
    class NXObject;
    namespace CAE
    {
        class _SimSoundProcessingBuilder;
        class SimSoundProcessingImpl;
        /**  @brief  This is the class handling the Sound Processing.  

          <br> To create a new instance of this class, use @link NXOpen::CAE::SimSoundProcessingCollection::Create  NXOpen::CAE::SimSoundProcessingCollection::Create @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimSoundProcessing : public NXOpen::NXObject
        {
            private: SimSoundProcessingImpl * m_simsoundprocessing_impl;
            private: friend class  _SimSoundProcessingBuilder;
            protected: SimSoundProcessing();
            public: ~SimSoundProcessing();
            /**Returns  the name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Process and play. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Play
            (
                bool loop /** loop */ 
            );
            /** Stop playing. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Stop
            (
            );
            /** Process and plot. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Plot
            (
                int deviceIndex /** deviceindex */ ,
                int viewportIndex /** viewportindex */ 
            );
            /** Process and save. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Save
            (
                const NXString & fileName /** filename */ 
            );
            /** Process and save. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void Save
            (
                const char * fileName /** filename */ 
            );


            /** Returns the @link NXOpen::CAE::SimSoundProcessingSourcesCollection NXOpen::CAE::SimSoundProcessingSourcesCollection@endlink  
             <br>  Created in NX1980.0.0.  <br>  
            */
            public: NXOpen::CAE::SimSoundProcessingSourcesCollection *Sources();
            /** Returns the @link NXOpen::CAE::SimSoundProcessingTreatmentsCollection NXOpen::CAE::SimSoundProcessingTreatmentsCollection@endlink  
             <br>  Created in NX1980.0.0.  <br>  
            */
            public: NXOpen::CAE::SimSoundProcessingTreatmentsCollection *Treatments();
            /** Returns the @link NXOpen::CAE::SimSoundProcessingImpulseResponsesCollection NXOpen::CAE::SimSoundProcessingImpulseResponsesCollection@endlink  
             <br>  Created in NX1980.0.0.  <br>  
            */
            public: NXOpen::CAE::SimSoundProcessingImpulseResponsesCollection *ImpulseResponses();
            /** Returns the @link NXOpen::CAE::SimSoundProcessingTracksCollection NXOpen::CAE::SimSoundProcessingTracksCollection@endlink  
             <br>  Created in NX1980.0.0.  <br>  
            */
            public: NXOpen::CAE::SimSoundProcessingTracksCollection *Tracks();
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