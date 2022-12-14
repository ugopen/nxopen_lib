#ifndef NXOpen_CAE_RESPONSESIMULATION_RMSRESULTSEVALUATIONSETTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_RMSRESULTSEVALUATIONSETTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_RmsResultsEvaluationSettingBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_PrlResultsEvaluationSettingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class RmsResultsEvaluationSettingBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class PrlResultsEvaluationSettingBuilder;
        }
    }
    class Direction;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _RmsResultsEvaluationSettingBuilderBuilder;
            /** This is a manager to the @link CAE::ResponseSimulation::RmsResultsEvaluationSetting CAE::ResponseSimulation::RmsResultsEvaluationSetting@endlink  class. 
                Object of type @link CAE::ResponseSimulation::RmsResultsEvaluationSetting CAE::ResponseSimulation::RmsResultsEvaluationSetting@endlink  can be 
                created and edited only through this class
                  <br> To create a new instance of this class, use @link CAE::ResponseSimulation::EvaluationSettingManager::CreateRmsResultsEvaluationSettingBuilder CAE::ResponseSimulation::EvaluationSettingManager::CreateRmsResultsEvaluationSettingBuilder@endlink  <br> */
            class NXOPENCPPEXPORT RmsResultsEvaluationSettingBuilder : public CAE::ResponseSimulation::PrlResultsEvaluationSettingBuilder
            {
                private: friend class  _RmsResultsEvaluationSettingBuilderBuilder;
                protected: RmsResultsEvaluationSettingBuilder();
                /**Returns  the option of using user defined direction  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: bool UsingUserDefinedDirection
                (
                );
                /**Sets  the option of using user defined direction  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetUsingUserDefinedDirection
                (
                    bool using_user_defined_direction /** using user defined direction */ 
                );
                /**Returns   the user defined direction  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::Direction * UserDefinedDirection
                (
                );
                /**Sets   the user defined direction  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetUserDefinedDirection
                (
                    NXOpen::Direction * user_defined_direction /** user defined direction */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
