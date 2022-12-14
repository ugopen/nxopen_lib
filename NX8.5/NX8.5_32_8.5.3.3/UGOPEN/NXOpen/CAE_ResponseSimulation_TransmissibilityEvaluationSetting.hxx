#ifndef NXOpen_CAE_RESPONSESIMULATION_TRANSMISSIBILITYEVALUATIONSETTING_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_TRANSMISSIBILITYEVALUATIONSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_TransmissibilityEvaluationSetting.ja
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
#include <NXOpen/CAE_ResponseSimulation_ModalResultsEvaluationSetting.hxx>
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
        namespace ResponseSimulation
        {
            class TransmissibilityEvaluationSetting;
        }
    }
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
            class _TransmissibilityEvaluationSettingBuilder;
            class TransmissibilityEvaluationSettingImpl;
            /** Represents parameters setting for transmissibility evaluation  <br> To create or edit an instance of this class, use @link CAE::ResponseSimulation::TransmissibilityEvaluationSettingBuilder  CAE::ResponseSimulation::TransmissibilityEvaluationSettingBuilder @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TransmissibilityEvaluationSetting : public CAE::ResponseSimulation::ModalResultsEvaluationSetting
            {
                private: TransmissibilityEvaluationSettingImpl * m_transmissibilityevaluationsetting_impl;
                private: friend class  _TransmissibilityEvaluationSettingBuilder;
                protected: TransmissibilityEvaluationSetting();
                public: ~TransmissibilityEvaluationSetting();
            };
        }
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
