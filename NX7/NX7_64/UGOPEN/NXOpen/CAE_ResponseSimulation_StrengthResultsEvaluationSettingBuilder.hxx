#ifndef NXOpen_CAE_RESPONSESIMULATION_STRENGTHRESULTSEVALUATIONSETTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_STRENGTHRESULTSEVALUATIONSETTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_StrengthResultsEvaluationSettingBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation.hxx>
#include <NXOpen/CAE_ResponseSimulation_DynamicResultEvaluationSettingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrengthResultsEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        class FEElement;
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class CombinationEvaluationOptions;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class DataLocation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class DynamicResultEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _StrengthResultsEvaluationSettingBuilderBuilder;
            /** This is a manager to the @link CAE::ResponseSimulation::StrengthResultsEvaluationSetting CAE::ResponseSimulation::StrengthResultsEvaluationSetting@endlink  class. 
                Object of type @link CAE::ResponseSimulation::StrengthResultsEvaluationSetting CAE::ResponseSimulation::StrengthResultsEvaluationSetting@endlink  can be 
                created and edited only through this class
                  <br> To create a new instance of this class, use @link CAE::ResponseSimulation::EvaluationSettingManager::CreateStrengthResultsEvaluationSettingBuilder CAE::ResponseSimulation::EvaluationSettingManager::CreateStrengthResultsEvaluationSettingBuilder@endlink  <br> */
            class NXOPENCPPEXPORT StrengthResultsEvaluationSettingBuilder : public CAE::ResponseSimulation::DynamicResultEvaluationSettingBuilder
            {
                private: friend class  _StrengthResultsEvaluationSettingBuilderBuilder;
                protected: StrengthResultsEvaluationSettingBuilder();
                /** Returns the destination elements  @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: std::vector<NXOpen::CAE::FEElement *> GetDestinationElements
                (
                );
                /** Sets the destination elements  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDestinationElements
                (
                    const std::vector<NXOpen::CAE::FEElement *> & destinationElement /** destination element */ 
                );
                /**Returns  the stress criteria type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrengthStressCriteria StressCriteriaType
                (
                );
                /**Sets  the stress criteria type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetStressCriteriaType
                (
                    NXOpen::CAE::ResponseSimulation::StrengthStressCriteria stressCriteria /** stress criteria */ 
                );
                /**Returns  the stress option type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrengthStressOption StressOptionType
                (
                );
                /**Sets  the stress option type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetStressOptionType
                (
                    NXOpen::CAE::ResponseSimulation::StrengthStressOption stressOption /** stress option */ 
                );
                /**Returns  the definition method of material  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::StrengthStressMaterialDefinitionMethod MaterialDefinitionType
                (
                );
                /**Sets  the definition method of material  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetMaterialDefinitionType
                (
                    NXOpen::CAE::ResponseSimulation::StrengthStressMaterialDefinitionMethod materialProperty /** material property */ 
                );
                /**Returns  the choice of override material property or not. If false, the material safty factor will be read 
                             from destination element selected, else a customized value will be used  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: bool MaterialOverrideOption
                (
                );
                /**Sets  the choice of override material property or not. If false, the material safty factor will be read 
                             from destination element selected, else a customized value will be used  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetMaterialOverrideOption
                (
                    bool overrideMaterialProperty /** override material property */ 
                );
                /**Returns  the customized material safety factor  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double MaterialSafetyFactor
                (
                );
                /**Sets  the customized material safety factor  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetMaterialSafetyFactor
                (
                    double safetyFactor /** safety factor */ 
                );
                /**Returns  the customized standard deviation for random event  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double StandardDeviation
                (
                );
                /**Sets  the customized standard deviation for random event  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetStandardDeviation
                (
                    double standardDeviation /** standard deviation */ 
                );
                /**Returns  the setting of combination evaluation  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::CombinationEvaluationOptions * CombinationOptionsBuilder
                (
                );
                /**Returns  the setting of combination evaluation  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DataLocation * DataLocation
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif