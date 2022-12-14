#ifndef NXOpen_CAE_LAMINATESINEEVENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LAMINATESINEEVENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateSineEventBuilder.ja
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
#include <NXOpen/CAE_LaminateDynamicEventBuilder.hxx>
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
        class LaminateSineEventBuilder;
    }
    namespace CAE
    {
        class LaminateDynamicEventBuilder;
    }
    namespace CAE
    {
        class LaminateModeProperty;
    }
    namespace CAE
    {
        class _LaminateSineEventBuilderBuilder;
        class LaminateSineEventBuilderImpl;
        /** Represents a @link NXOpen::CAE::LaminateSineEvent NXOpen::CAE::LaminateSineEvent@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::LaminateDynamicEventCollection::CreateSineEventBuilder  NXOpen::CAE::LaminateDynamicEventCollection::CreateSineEventBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminateSineEventBuilder : public NXOpen::CAE::LaminateDynamicEventBuilder
        {
            /** The reference enum. */
            public: enum NaturalFrequeciesEnum
            {
                NaturalFrequeciesEnumAll/** Select all natural frequencies */,
                NaturalFrequeciesEnumSelect/** Manually select natural frequencies */
            };

            /** The intermediate frequencies options */
            public: enum IntermediateFrequeciesEnum
            {
                IntermediateFrequeciesEnumIncrementLinear/** Linear Increments */,
                IntermediateFrequeciesEnumIncrementLogarithmic/** Logarithmic Increments */,
                IntermediateFrequeciesEnumBetweenFrequencies/** Between Frequencies */
            };

            /** The intermediate in between frequencies increment option */
            public: enum IntermediateFrequeciesBetweenEnum
            {
                IntermediateFrequeciesBetweenEnumLinear/** Linear increments */,
                IntermediateFrequeciesBetweenEnumLogarithmic/** Logarithmic increments */
            };

            /** The additional frequencies units */
            public: enum AdditionalFrequeciesUnitsEnum
            {
                AdditionalFrequeciesUnitsEnumHz/** hz */ ,
                AdditionalFrequeciesUnitsEnumKHz/** khz */ ,
                AdditionalFrequeciesUnitsEnumMHz/** mhz */ ,
                AdditionalFrequeciesUnitsEnumGHz/** ghz */ 
            };

            private: LaminateSineEventBuilderImpl * m_laminatesineeventbuilder_impl;
            private: friend class  _LaminateSineEventBuilderBuilder;
            protected: LaminateSineEventBuilder();
            public: ~LaminateSineEventBuilder();
            /**Returns  the natural frequencies option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool NaturalFrequenciesEnable
            (
            );
            /**Sets  the natural frequencies option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetNaturalFrequenciesEnable
            (
                bool naturalFrequenciesEnable /** naturalfrequenciesenable */ 
            );
            /**Returns  the natural frequencies selection option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::LaminateSineEventBuilder::NaturalFrequeciesEnum NaturalFrequenciesChoice
            (
            );
            /**Sets  the natural frequencies selection option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetNaturalFrequenciesChoice
            (
                NXOpen::CAE::LaminateSineEventBuilder::NaturalFrequeciesEnum naturalFrequenciesChoice /** naturalfrequencieschoice */ 
            );
            /** Sets the a mode property selection 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SelectModes
            (
                const std::vector<NXOpen::CAE::LaminateModeProperty *> & selectedModes /** selected modes */ 
            );
            /**Returns  the intermediate frequencies control 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool IntermediateFrequenciesEnable
            (
            );
            /**Sets  the intermediate frequencies control 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetIntermediateFrequenciesEnable
            (
                bool intermediateFrequenciesEnable /** intermediatefrequenciesenable */ 
            );
            /**Returns  the intermediate frequencies option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::LaminateSineEventBuilder::IntermediateFrequeciesEnum IntermediateFrequenciesOption
            (
            );
            /**Sets  the intermediate frequencies option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetIntermediateFrequenciesOption
            (
                NXOpen::CAE::LaminateSineEventBuilder::IntermediateFrequeciesEnum intermediateFrequenciesOption /** intermediatefrequenciesoption */ 
            );
            /**Returns  the intermediate frequencies number of increments for linear and logarithmic options 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int IntermediateFrequenciesNumIncrements
            (
            );
            /**Sets  the intermediate frequencies number of increments for linear and logarithmic options 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetIntermediateFrequenciesNumIncrements
            (
                int intermediateFrequenciesNumIncrements /** intermediatefrequenciesnumincrements */ 
            );
            /**Returns  the option to include the natural frequencis in the intermediate frequencies with the linear and logarithmic options 
             <br>  @deprecated Deprecated in NX11.0.0.  This function has no replacement. The IntermediateFrequenciesIncludeNatFreq property is simply not supported by the Sine Event solver and has never been. This parameter is useless. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  This function has no replacement. The IntermediateFrequenciesIncludeNatFreq property is simply not supported by the Sine Event solver and has never been. This parameter is useless.") bool IntermediateFrequenciesIncludeNatFreq
            (
            );
            /**Sets  the option to include the natural frequencis in the intermediate frequencies with the linear and logarithmic options 
             <br>  @deprecated Deprecated in NX11.0.0.  This function has no replacement. The IntermediateFrequenciesIncludeNatFreq property is simply not supported by the Sine Event solver and has never been. This parameter is useless. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  This function has no replacement. The IntermediateFrequenciesIncludeNatFreq property is simply not supported by the Sine Event solver and has never been. This parameter is useless.") void SetIntermediateFrequenciesIncludeNatFreq
            (
                bool intermediateFrequenciesIncludeNatFreq /** intermediatefrequenciesincludenatfreq */ 
            );
            /**Returns  the intermediate in between frequencies option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::LaminateSineEventBuilder::IntermediateFrequeciesBetweenEnum IntermediateFrequenciesBetweenOption
            (
            );
            /**Sets  the intermediate in between frequencies option 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetIntermediateFrequenciesBetweenOption
            (
                NXOpen::CAE::LaminateSineEventBuilder::IntermediateFrequeciesBetweenEnum intermediateFrequenciesBetweenOption /** intermediatefrequenciesbetweenoption */ 
            );
            /**Returns  the intermediate in between frequencies number of excitations 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int IntermediateFrequenciesNumExcitations
            (
            );
            /**Sets  the intermediate in between frequencies number of excitations 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetIntermediateFrequenciesNumExcitations
            (
                int intermediateFrequenciesNumExcitations /** intermediatefrequenciesnumexcitations */ 
            );
            /**Returns  the intermediate in between frequencies number of excitations 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double IntermediateFrequenciesCluster
            (
            );
            /**Sets  the intermediate in between frequencies number of excitations 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetIntermediateFrequenciesCluster
            (
                double intermediateFrequenciesCluster /** intermediatefrequenciescluster */ 
            );
            /**Returns  the option to consider break points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool AdditionalFrequenciesBreakPoints
            (
            );
            /**Sets  the option to consider break points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetAdditionalFrequenciesBreakPoints
            (
                bool additionalFrequenciesBreakPoints /** additionalfrequenciesbreakpoints */ 
            );
            /**Returns  the option to consider break points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::LaminateSineEventBuilder::AdditionalFrequeciesUnitsEnum AdditionalFrequenciesUnits
            (
            );
            /**Sets  the option to consider break points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetAdditionalFrequenciesUnits
            (
                NXOpen::CAE::LaminateSineEventBuilder::AdditionalFrequeciesUnitsEnum additionalFrequenciesUnits /** additionalfrequenciesunits */ 
            );
            /** Sets the additional frequencies values 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetAdditionalFrequencies
            (
                const std::vector<double> & additionalFrequencies /** additionalfrequencies */ 
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
