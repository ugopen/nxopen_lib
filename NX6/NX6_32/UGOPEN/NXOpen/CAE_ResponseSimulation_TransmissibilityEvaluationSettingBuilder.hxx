#ifndef NXOpen_CAE_RESPONSESIMULATION_TRANSMISSIBILITYEVALUATIONSETTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_TRANSMISSIBILITYEVALUATIONSETTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_TransmissibilityEvaluationSettingBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_ModalResultsEvaluationSettingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class TransmissibilityEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ModalResultsEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _TransmissibilityEvaluationSettingBuilderBuilder;
            /** This is a manager to the @link CAE::ResponseSimulation::TransmissibilityEvaluationSetting CAE::ResponseSimulation::TransmissibilityEvaluationSetting@endlink  class. 
                Object of type @link CAE::ResponseSimulation::TransmissibilityEvaluationSetting CAE::ResponseSimulation::TransmissibilityEvaluationSetting@endlink  can be 
                created and edited only through this class
                  <br> To create a new instance of this class, use @link CAE::ResponseSimulation::EvaluationSettingManager::CreateTransmissibilityEvaluationSettingBuilder CAE::ResponseSimulation::EvaluationSettingManager::CreateTransmissibilityEvaluationSettingBuilder@endlink  <br> */
            class NXOPENCPPEXPORT TransmissibilityEvaluationSettingBuilder : public CAE::ResponseSimulation::ModalResultsEvaluationSettingBuilder
            {
                /** This enum defines input motion type */
                public: enum MotionType
                {
                    MotionTypeDisplacement/** displacement */ ,
                    MotionTypeVelocity/** velocity */ ,
                    MotionTypeAcceleration/** acceleration */ 
                };

                private: friend class  _TransmissibilityEvaluationSettingBuilderBuilder;
                protected: TransmissibilityEvaluationSettingBuilder();
                /**Returns  the input motion type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSettingBuilder::MotionType InputMotionType
                (
                );
                /**Sets  the input motion type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetInputMotionType
                (
                    NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSettingBuilder::MotionType motionType /** motion type */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif