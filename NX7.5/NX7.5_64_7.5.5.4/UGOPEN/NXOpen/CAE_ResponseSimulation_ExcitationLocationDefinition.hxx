#ifndef NXOpen_CAE_RESPONSESIMULATION_EXCITATIONLOCATIONDEFINITION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_EXCITATIONLOCATIONDEFINITION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_ExcitationLocationDefinition.ja
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
#include <NXOpen/CAE_ResponseSimulation_ExcitationBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ExcitationLocationDefinition;
        }
    }
    class SelectObject;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _ExcitationLocationDefinitionBuilder;
            class ExcitationLocationDefinitionImpl;
            /** Represents the manager to @link CAE::ResponseSimulation::DistributedLoadExcitation CAE::ResponseSimulation::DistributedLoadExcitation@endlink .
                 The object of type @link CAE::ResponseSimulation::DistributedLoadExcitation CAE::ResponseSimulation::DistributedLoadExcitation@endlink 
                  can only be created or edited through this class.
                 */
            class NXOPENCPPEXPORT  ExcitationLocationDefinition : public TaggedObject
            {
                private: ExcitationLocationDefinitionImpl * m_excitationlocationdefinition_impl;
                private: friend class  _ExcitationLocationDefinitionBuilder;
                protected: ExcitationLocationDefinition();
                public: ~ExcitationLocationDefinition();
                /**Returns  the excitation location on which the excitation will be applied. The excitation location
                        type could be force location, enforced motion location or dynamic load defined in response 
                        dynamic solution  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::SelectObject * ExcitationLocation
                (
                );
                /**Returns  the ID of excitation location on which the excitation will be applied. The excitation location ID
                        could be node label or load set label  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: int ExcitationLocationId
                (
                );
                /**Sets  the ID of excitation location on which the excitation will be applied. The excitation location ID
                        could be node label or load set label  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetExcitationLocationId
                (
                    int excitaitonLocationId /** excitaitonlocationid */ 
                );
                /**Returns  the type of excitaion location  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::ExcitationBuilder::ExcitationLocationType ExcitationLocationType
                (
                );
                /**Sets  the type of excitaion location  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetExcitationLocationType
                (
                    NXOpen::CAE::ResponseSimulation::ExcitationBuilder::ExcitationLocationType excitationLocationType /** excitationlocationtype */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
