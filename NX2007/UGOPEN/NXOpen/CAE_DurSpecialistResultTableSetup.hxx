#ifndef NXOpen_CAE_DURSPECIALISTRESULTTABLESETUP_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTRESULTTABLESETUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistResultTableSetup.ja
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
#include <NXOpen/TransientObject.hxx>
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
        class DurSpecialistResultTableSetup;
    }
    namespace CAE
    {
        class DurSpecialistResultTableSetupImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistResultTableSetup NXOpen::CAE::DurSpecialistResultTableSetup@endlink .  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistSolutionCollection::CreateResultSetup  NXOpen::CAE::DurSpecialistSolutionCollection::CreateResultSetup @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistResultTableSetup : public NXOpen::TransientObject
        {
            /** The result types that can be requested in a result table */
            public: enum ResultType
            {
                ResultTypeCyclicFatigueDamage/** Cyclic fatigue damage */,
                ResultTypeFatigueLife/** Fatigue Life */,
                ResultTypeFatigueLifetime/** Fatigue Lifetime */,
                ResultTypeMileage/** Mileage */,
                ResultTypeMaxStressAmplitude/** Max. stress amplitude */,
                ResultTypeMaxStress/** Max. stress */,
                ResultTypeMinStress/** Min. stress */,
                ResultTypeMeanStress/** Mean stress */,
                ResultTypeStaticSafetyFactor/** Static safety factor */,
                ResultTypeDesignLifeFactor/** Design life factor */,
                ResultTypeDesignLoadFactor/** Design load factor */,
                ResultTypeDurabilityFailureType/** Durability failure type */,
                ResultTypeMinEnergyReleaseRate/** Min. energy release rate */,
                ResultTypeMaxEnergyReleaseRate/** Max. energy release rate */,
                ResultTypeMeanEnergyReleaseRate/** Mean energy release rate */,
                ResultTypeMaxEnergyReleaseRateAmplitude/** Max. energy release rate amplitude */,
                ResultTypeEquivalentEnergyReleaseRate/** Equivalent energy release rate */,
                ResultTypeDegradationFactor/** Degradation factor */,
                ResultTypeEquivalentLife/** Equivalent Life */,
                ResultTypeStressReductionFactor/** Stress reduction factor */,
                ResultTypeStiffnessReduction2D/** Stiffness reduction 2D */,
                ResultTypeStiffnessReduction3D/** Stiffness reduction 3D */,
                ResultTypeAccumulatedDamage/** Accumulated damage */,
                ResultTypeDurabilitySafetyFactor/** Durability safety factor */,
                ResultTypeCombinedSafetyFactor/** Combined safety factor */,
                ResultTypeCombinedSafetyFactorCalculated/** Combined safety factor calculated */,
                ResultTypeMaxTemperature/** Max. temperature */,
                ResultTypeMinTemperature/** Min. temperature */
            };

            private: DurSpecialistResultTableSetupImpl * m_durspecialistresulttablesetup_impl;
            /// \cond NX_NO_DOC 
            public: explicit DurSpecialistResultTableSetup(void *ptr);
            /// \endcond 
            /** The result types requested in order.  The first result type is the critical result. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void ApplyResultTypes
            (
                const std::vector<NXOpen::CAE::DurSpecialistResultTableSetup::ResultType> & resultTypes /** resulttypes */ 
            );
            /**Returns  the toggle that determines whether or not to show a summary of critical results for all local definitions 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleLocalDefinition
            (
            );
            /**Sets  the toggle that determines whether or not to show a summary of critical results for all local definitions 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToggleLocalDefinition
            (
                bool toggleLocalDefinition /** togglelocaldefinition */ 
            );
            /**Returns  the toggle that determines whether or not to show a summary of critical results for all events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleEvent
            (
            );
            /**Sets  the toggle that determines whether or not to show a summary of critical results for all events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToggleEvent
            (
                bool toggleEvent /** toggleevent */ 
            );
            /**Returns  the toggle that determines whether or not to show a summary of critical results for all time steps 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleResultStep
            (
            );
            /**Sets  the toggle that determines whether or not to show a summary of critical results for all time steps 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToggleResultStep
            (
                bool toggleResultStep /** toggleresultstep */ 
            );
            /**Returns  the toggle that determines whether or not to show a summary of critical results for single events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleSingleEventResults
            (
            );
            /**Sets  the toggle that determines whether or not to show a summary of critical results for single events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToggleSingleEventResults
            (
                bool toggleSingleEventResults /** togglesingleeventresults */ 
            );
            /**Returns  the toggle that determines whether or not to show a summary of critical results for repeated events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleRepeatedEventResults
            (
            );
            /**Sets  the toggle that determines whether or not to show a summary of critical results for repeated events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToggleRepeatedEventResults
            (
                bool toggleRepeatedEventResults /** togglerepeatedeventresults */ 
            );
            /**Returns  the toggle that determines whether or not to show a summary of critical results for accumulated events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleAccumulatedEventResults
            (
            );
            /**Sets  the toggle that determines whether or not to show a summary of critical results for accumulated events 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToggleAccumulatedEventResults
            (
                bool toggleAccumulatedEventResults /** toggleaccumulatedeventresults */ 
            );
            /** Frees the object from memory.  After this method is called,
                        it is illegal to use the object. In .NET, this method is automatically
                        called when the object is deleted by the garbage collector. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~DurSpecialistResultTableSetup();
            /** Deletes the result table toggles entity. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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
