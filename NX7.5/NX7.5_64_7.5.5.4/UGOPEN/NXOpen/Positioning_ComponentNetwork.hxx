#ifndef NXOpen_POSITIONING_COMPONENTNETWORK_HXX_INCLUDED
#define NXOpen_POSITIONING_COMPONENTNETWORK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Positioning_ComponentNetwork.ja
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
#include <NXOpen/Positioning_Network.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Positioning
    {
        class ComponentNetwork;
    }
    namespace Positioning
    {
        class Network;
    }
    namespace Positioning
    {
        class _ComponentNetworkBuilder;
        class ComponentNetworkImpl;
        /**
                Network for use in positioning components in NX.
                A component network extends the @link Positioning::Network Positioning::Network@endlink  by
                adding support for @link Assemblies::Arrangement Assemblies::Arrangement@endlink s.
             <br> Use @link Positioning::Positioner::EstablishNetwork Positioning::Positioner::EstablishNetwork@endlink  to create an instance of this class. <br> */
        class NXOPENCPPEXPORT  ComponentNetwork : public Positioning::Network
        {
            /** 
                        Specifies how changes in the network are applied to arrangements.
                    */
            public: enum ArrangementsMode
            {
                ArrangementsModeExisting/** Apply transforms in arrangements according to existing component properties.
                                                                                                Constraints are created non-arrangement specific. */,
                ArrangementsModeInUsed/** Apply transforms in the used arrangement only. 
                                                                                                Constraints are created arrangement specific in the used arrangement 
                                                                                                and suppressed in all other arrangements*/
            };

            private: ComponentNetworkImpl * m_componentnetwork_impl;
            private: friend class  _ComponentNetworkBuilder;
            protected: ComponentNetwork();
            public: ~ComponentNetwork();
            /**Returns 
                        the arrangements mode for this network.
                     <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: NXOpen::Positioning::ComponentNetwork::ArrangementsMode NetworkArrangementsMode
            (
            );
            /**Sets 
                        the arrangements mode for this network.
                     <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void SetNetworkArrangementsMode
            (
                NXOpen::Positioning::ComponentNetwork::ArrangementsMode mode /** The @link Positioning::ComponentNetwork::ArrangementsMode Positioning::ComponentNetwork::ArrangementsMode@endlink .*/
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
