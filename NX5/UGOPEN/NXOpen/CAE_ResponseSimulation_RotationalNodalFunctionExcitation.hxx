#ifndef NXOpen_CAE_RESPONSESIMULATION_ROTATIONALNODALFUNCTIONEXCITATION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_ROTATIONALNODALFUNCTIONEXCITATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_RotationalNodalFunctionExcitation.ja
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
            class RotationalNodalFunctionExcitation;
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
            class _RotationalNodalFunctionExcitationBuilder;
            /** Represents a rotational nodal function excitation */
            class NXOPENCPPEXPORT RotationalNodalFunctionExcitation : public CAE::ResponseSimulation::NodalFunctionExcitation
            {
                private: friend class  _RotationalNodalFunctionExcitationBuilder;
                protected: RotationalNodalFunctionExcitation();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
