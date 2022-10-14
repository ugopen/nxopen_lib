#ifndef NXOpen_CAE_RESPONSESIMULATION_ROTATIONALDDAMEXCITATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_ROTATIONALDDAMEXCITATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_RotationalDDAMExcitationBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_DDAMExcitationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class RotationalDDAMExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class DDAMExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _RotationalDDAMExcitationBuilderBuilder;
            /** Represents the manager to @link CAE::ResponseSimulation::DDAMExcitation CAE::ResponseSimulation::DDAMExcitation@endlink .
                 The object of type @link CAE::ResponseSimulation::DDAMExcitation CAE::ResponseSimulation::DDAMExcitation@endlink  can only
                be created or edited through this class.  <br> To create a new instance of this class, use @link CAE::ResponseSimulation::ExcitationCollection::CreateRotationalDdamExcitationBuilder CAE::ResponseSimulation::ExcitationCollection::CreateRotationalDdamExcitationBuilder@endlink  <br> */
            class NXOPENCPPEXPORT RotationalDDAMExcitationBuilder : public CAE::ResponseSimulation::DDAMExcitationBuilder
            {
                private: friend class  _RotationalDDAMExcitationBuilderBuilder;
                protected: RotationalDDAMExcitationBuilder();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif