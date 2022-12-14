#ifndef NXOpen_CAE_RESPONSESIMULATION_TRANSLATIONALNODALFUNCTIONEXCITATION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_TRANSLATIONALNODALFUNCTIONEXCITATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_TranslationalNodalFunctionExcitation.ja
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
#include <NXOpen/CAE_ResponseSimulation_NodalFunctionExcitation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class TranslationalNodalFunctionExcitation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class NodalFunctionExcitation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _TranslationalNodalFunctionExcitationBuilder;
            /** Represents a translational nodal function excitation */
            class NXOPENCPPEXPORT TranslationalNodalFunctionExcitation : public CAE::ResponseSimulation::NodalFunctionExcitation
            {
                private: friend class  _TranslationalNodalFunctionExcitationBuilder;
                protected: TranslationalNodalFunctionExcitation();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
