#ifndef NXOpen_CAE_RESPONSESIMULATION_MODALRESULTSEVALUATIONSETTING_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_MODALRESULTSEVALUATIONSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_ModalResultsEvaluationSetting.ja
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
#include <NXOpen/CAE_ResponseSimulation_FunctionEvaluationSetting.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ModalResultsEvaluationSetting;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class FunctionEvaluationSetting;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _ModalResultsEvaluationSettingBuilder;
            /** Represents the abstract class of evaluation setting for FRF and transmissibility  <br> This is an abstract class, and cannot be created. <br> */
            class NXOPENCPPEXPORT ModalResultsEvaluationSetting : public CAE::ResponseSimulation::FunctionEvaluationSetting
            {
                private: friend class  _ModalResultsEvaluationSettingBuilder;
                protected: ModalResultsEvaluationSetting();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
