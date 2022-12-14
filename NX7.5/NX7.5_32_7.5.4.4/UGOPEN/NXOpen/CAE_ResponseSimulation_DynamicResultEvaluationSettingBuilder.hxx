#ifndef NXOpen_CAE_RESPONSESIMULATION_DYNAMICRESULTEVALUATIONSETTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_DYNAMICRESULTEVALUATIONSETTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_DynamicResultEvaluationSettingBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class DynamicResultEvaluationSettingBuilder;
        }
    }
    class Builder;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _DynamicResultEvaluationSettingBuilderBuilder;
            class DynamicResultEvaluationSettingBuilderImpl;
            /** Represents the abstract builder class of evaluation setting for all dynamic results evaluations.
                 <br> This is an abstract class, and cannot be created. <br> */
            class NXOPENCPPEXPORT  DynamicResultEvaluationSettingBuilder : public Builder
            {
                private: DynamicResultEvaluationSettingBuilderImpl * m_dynamicresultevaluationsettingbuilder_impl;
                private: friend class  _DynamicResultEvaluationSettingBuilderBuilder;
                protected: DynamicResultEvaluationSettingBuilder();
                public: ~DynamicResultEvaluationSettingBuilder();
                /** Returns the description.  @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: std::vector<NXString> GetDescriptionString
                (
                );
                /** Sets the description  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDescriptionString
                (
                    const std::vector<NXString> & description /** description */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
