#ifndef NXOpen_CAE_RESPONSESIMULATION_SENSOREVALUATIONSETTING_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_SENSOREVALUATIONSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_SensorEvaluationSetting.ja
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
#include <NXOpen/CAE_ResponseSimulation_DynamicResultEvaluationSetting.hxx>
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
            class SensorEvaluationSetting;
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
            class _SensorEvaluationSettingBuilder;
            class SensorEvaluationSettingImpl;
            /** Represents the parameters setting for sensor evaluation.  For more information, see the 
                Response Simulation section of the Gateway Help  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ResponseSimulation::SensorEvaluationSettingBuilder  NXOpen::CAE::ResponseSimulation::SensorEvaluationSettingBuilder @endlink  <br> 
             <br>  Created in NX6.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  SensorEvaluationSetting : public NXOpen::CAE::ResponseSimulation::DynamicResultEvaluationSetting
            {
                private: SensorEvaluationSettingImpl * m_sensorevaluationsetting_impl;
                private: friend class  _SensorEvaluationSettingBuilder;
                protected: SensorEvaluationSetting();
                public: ~SensorEvaluationSetting();
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
