#ifndef NXOpen_CAE_RESPONSESIMULATION_EVALUATIONSETTING_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_EVALUATIONSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_EvaluationSetting.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class EvaluationSetting;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _EvaluationSettingBuilder;
            /** Represents the abstract class of all evaluation setting classes.  <br> This is an abstract class, and cannot be created. <br> */
            class NXOPENCPPEXPORT EvaluationSetting : public NXObject
            {
                private: friend class  _EvaluationSettingBuilder;
                protected: EvaluationSetting();
                /** Destroies the evaluation setting object after evaluation.  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void Destroy
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif