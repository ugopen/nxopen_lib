#ifndef NXOpen_CAE_RESPONSESIMULATION_DATALOCATION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_DATALOCATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_DataLocation.ja
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
#include <NXOpen/TaggedObject.hxx>
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
            class DataLocation;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _DataLocationBuilder;
            class DataLocationImpl;
            /** Represents the data location to perform evaluation 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  DataLocation : public NXOpen::TaggedObject
            {
                /** Specifies the location for beam */
                public: enum Beam
                {
                    BeamC/** c */ ,
                    BeamD/** d */ ,
                    BeamE/** e */ ,
                    BeamF/** f */ 
                };

                /** Specifies the location for shell */
                public: enum Shell
                {
                    ShellTop/** top */ ,
                    ShellBottom/** bottom */ ,
                    ShellMiddle/** middle */ 
                };

                /** Specifies the element location for element */
                public: enum Element
                {
                    ElementBoth/** both */ ,
                    ElementCentroid/** centroid */ ,
                    ElementCorners/** corners */ 
                };

                private: DataLocationImpl * m_datalocation_impl;
                private: friend class  _DataLocationBuilder;
                protected: DataLocation();
                public: ~DataLocation();
                /**Returns  the method to define frequency
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DataLocation::Beam BeamLocation
                (
                );
                /**Sets  the method to define frequency
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetBeamLocation
                (
                    NXOpen::CAE::ResponseSimulation::DataLocation::Beam beamLocation /** beam location */ 
                );
                /**Returns  the start value of frequency range. Only available when the frequency is defined
                        by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DataLocation::Shell ShellLocation
                (
                );
                /**Sets  the start value of frequency range. Only available when the frequency is defined
                        by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetShellLocation
                (
                    NXOpen::CAE::ResponseSimulation::DataLocation::Shell shellLocation /** shell location */ 
                );
                /**Returns  the element location. Only available when stress and strain is defined
                        by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DataLocation::Element ElementLocation
                (
                );
                /**Sets  the element location. Only available when stress and strain is defined
                        by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetElementLocation
                (
                    NXOpen::CAE::ResponseSimulation::DataLocation::Element elementLocation /** element location */ 
                );
                /**Returns  the end value of frequency range. Only available when the frequency is defined 
                        by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: int LayerSelection
                (
                );
                /**Sets  the end value of frequency range. Only available when the frequency is defined 
                        by @link CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange CAE::ResponseSimulation::FrequencyDefinition::DefinitionRange@endlink  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetLayerSelection
                (
                    int layerNumber /** layer number */ 
                );
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
