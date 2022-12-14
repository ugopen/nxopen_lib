#ifndef NXOpen_CAE_RESPONSESIMULATION_NODALFUNCTIONEXCITATION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_NODALFUNCTIONEXCITATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_NodalFunctionExcitation.ja
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
#include <NXOpen/CAE_ResponseSimulation_Excitation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
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
            class Excitation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _NodalFunctionExcitationBuilder;
            /** Represents the abstract class of nodal function excitation  <br> This is an abstract class, and cannot be created. <br> */
            class NXOPENCPPEXPORT NodalFunctionExcitation : public CAE::ResponseSimulation::Excitation
            {
                /** the subtype of nodal function excitation */
                public: enum Type
                {
                    TypeNodalForce/** nodal force */ ,
                    TypeEnforcedMotion/** enforced motion */ 
                };

                private: friend class  _NodalFunctionExcitationBuilder;
                protected: NodalFunctionExcitation();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
