#ifndef NXOpen_MECHANICALROUTING_CONNECTIVITYSERVICE_HXX_INCLUDED
#define NXOpen_MECHANICALROUTING_CONNECTIVITYSERVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MechanicalRouting_ConnectivityService.ja
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
#include <NXOpen/ErrorList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_mechanicalrouting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MechanicalRouting
    {
        class ConnectivityService;
    }
    namespace MechanicalRouting
    {
        class RoutingManager;
    }
    namespace Assemblies
    {
        class Component;
    }
    class ErrorList;
    class Part;
    namespace Routing
    {
        class Port;
    }
    namespace MechanicalRouting
    {
        class ConnectivityServiceImpl;
        /** Represents a @link NXOpen::MechanicalRouting::ConnectivityService NXOpen::MechanicalRouting::ConnectivityService@endlink  object.
                Use the @link MechanicalRouting::RoutingManager::ConnectivityService MechanicalRouting::RoutingManager::ConnectivityService@endlink  to obtain
                an instance of this class.
              <br> To obtain an instance of this class, refer to @link NXOpen::MechanicalRouting::RoutingManager  NXOpen::MechanicalRouting::RoutingManager @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHANICALROUTINGEXPORT  ConnectivityService
        {
            /** Represents the method to use to get the connected components of the selected component.
                        1. Fitting : Fitting components connected to selected component.
                        2. Stock : Stock components connected to selected component.
                        3. Any: Any components either stock or fittings connected to selected component.
                    */

            /// \cond NX_NO_DOC 
            public: enum ComponentType
            {
                ComponentTypeFitting/** fitting */ ,
                ComponentTypeStock/** stock */ ,
                ComponentTypeAny/** any */ 
            };


            /// \endcond 
            private: ConnectivityServiceImpl * m_connectivityservice_impl;
            private: NXOpen::MechanicalRouting::RoutingManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ConnectivityService(NXOpen::MechanicalRouting::RoutingManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ConnectivityService();
            /**  Returns the pairs of connected ports in the part. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void GetConnectedPorts
            (
                NXOpen::Part * part /** The part. */,
                std::vector<NXOpen::Routing::Port *> & connectedPorts1 /** connectedports1 */ ,
                std::vector<NXOpen::Routing::Port *> & connectedPorts2 /** connectedports2 */ 
            );

            /// \cond NX_NO_DOC 
            /**  Returns the pairs of ports connected to the given Design Element. 
             <br>  @deprecated Deprecated in NX1899.0.0.  JA_MECHANICALROUTING_CONNECTIVITY_SERVICE_get_connected_ports_from_component <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  JA_MECHANICALROUTING_CONNECTIVITY_SERVICE_get_connected_ports_from_component") void GetPortsConnectedToDesignElement
            (
                NXOpen::Assemblies::Component * part /** The component of the Design Element. */,
                std::vector<NXOpen::Routing::Port *> & connectedPorts1 /** connectedports1 */ ,
                std::vector<NXOpen::Routing::Port *> & connectedPorts2 /** connectedports2 */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  Discovers, loads and returns the components connected to the given Design Element. 
             <br>  @deprecated Deprecated in NX1926.0.0.  JA_MECHANICALROUTING_CONNECTIVITY_SERVICE_get_components_connected_to_component <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX1926.0.0.  JA_MECHANICALROUTING_CONNECTIVITY_SERVICE_get_components_connected_to_component") void GetComponentsConnectedToDesignElement
            (
                NXOpen::Assemblies::Component * containerTag /** The assembly of the component. */,
                NXOpen::Assemblies::Component * componentTag /** The component to get connected components for. */,
                std::vector<NXOpen::Assemblies::Component *> & connectedComponents /** connectedcomponents */ ,
                NXOpen::ErrorList ** errorList /** Any errors that occurred during the operation  */
            );

            /// \endcond 
            /**  Returns the pairs of ports connected to the given component. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void GetConnectedPortsFromComponent
            (
                NXOpen::Assemblies::Component * part /** The Component */,
                std::vector<NXOpen::Routing::Port *> & connectedPorts1 /** connectedports1 */ ,
                std::vector<NXOpen::Routing::Port *> & connectedPorts2 /** connectedports2 */ 
            );

            /// \cond NX_NO_DOC 
            /**  Discovers, loads and returns the components connected to the given component. 
             <br>  @deprecated Deprecated in NX1953.0.0.  No alternative provided for this method. <br>  

             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX1953.0.0.  No alternative provided for this method.") void GetComponentsConnectedToComponent
            (
                NXOpen::Assemblies::Component * containerTag /** The assembly of the component. */,
                NXOpen::Assemblies::Component * componentTag /** The component to get connected components for. */,
                NXOpen::MechanicalRouting::ConnectivityService::ComponentType componentType /** The connected components to get from selected component. */,
                std::vector<NXOpen::Assemblies::Component *> & connectedComponents /** connectedcomponents */ ,
                NXOpen::ErrorList ** errorList /** Any errors that occurred during the operation  */
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  

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
