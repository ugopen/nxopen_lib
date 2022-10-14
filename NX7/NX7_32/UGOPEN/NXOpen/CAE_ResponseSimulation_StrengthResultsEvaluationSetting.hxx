#ifndef NXOpen_CAE_RESPONSESIMULATION_STRENGTHRESULTSEVALUATIONSETTING_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_STRENGTHRESULTSEVALUATIONSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_StrengthResultsEvaluationSetting.ja
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
#include <NXOpen/CAE_ResponseSimulation_DynamicResultEvaluationSetting.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrengthResultsEvaluationSetting;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class DynamicResultEvaluationSetting;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _StrengthResultsEvaluationSettingBuilder;
            /** Represents parameters setting for strength results evaluation. Available to all kinds of 
                event type */
            class NXOPENCPPEXPORT StrengthResultsEvaluationSetting : public CAE::ResponseSimulation::DynamicResultEvaluationSetting
            {
                private: friend class  _StrengthResultsEvaluationSettingBuilder;
                protected: StrengthResultsEvaluationSetting();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif