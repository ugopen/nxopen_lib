#ifndef NXOpen_ROUTING_ELECTRICAL_CONNECTORDEVICE_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_CONNECTORDEVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_ConnectorDevice.ja
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
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_SingleDevice.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class ConnectorDevice;
        }
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class CableDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class Connection;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalPartDefinitionShadow;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalStockDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class HarnessDevice;
        }
    }
    namespace Routing
    {
        class LogicalTerminal;
    }
    namespace Routing
    {
        class Port;
    }
    namespace Routing
    {
        class SingleDevice;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class _ConnectorDeviceBuilder;
            /**
                        The Electrical ConnectorDevice corresponds to a connector instance of
                        @link Routing::SingleDevice Routing::SingleDevice@endlink .
                     <br> To create a new instance of this class, use @link Routing::Electrical::ConnectorDeviceCollection::CreateConnectorDevice Routing::Electrical::ConnectorDeviceCollection::CreateConnectorDevice@endlink  <br> */
            class NXOPENCPPEXPORT ConnectorDevice : public Routing::SingleDevice
            {
                /** Component type */
                public: enum ComponentType
                {
                    ComponentTypeNone/** none */ ,
                    ComponentTypeConnector/** connector */ ,
                    ComponentTypeSplice/** splice */ ,
                    ComponentTypeDevice/** device */ ,
                    ComponentTypeOther/** other */ 
                };

                /** Assignment method */
                public: enum Assign
                {
                    AssignNone/** none */ ,
                    AssignAuto/** auto */ ,
                    AssignManual/** manual */ 
                };

                private: friend class  _ConnectorDeviceBuilder;
                protected: ConnectorDevice();
                /** Get part definition.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ElectricalPartDefinitionShadow * GetPartDefinition
                (
                );
                /** Sets part definition.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetPartDefinition
                (
                    NXOpen::Routing::Electrical::ElectricalPartDefinitionShadow * elecPartDefinitionShadow /** elec part definition shadow */ 
                );
                /** Get terminals.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: std::vector<NXOpen::Routing::LogicalTerminal *> GetTerminals
                (
                );
                /** Remove a terminal.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool RemoveTerminal
                (
                    NXOpen::Routing::LogicalTerminal * routeTerminalToRemove /** route terminal to remove */ 
                );
                /**Returns  the connector type.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ConnectorDevice::ComponentType ConnectorType
                (
                );
                /**Sets  the connector type.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetConnectorType
                (
                    NXOpen::Routing::Electrical::ConnectorDevice::ComponentType elecRlistComponent /** elec rlist component */ 
                );
                /** Get assign method.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::ConnectorDevice::Assign GetAssignMethod
                (
                );
                /** Get the nearest @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink  encountered up the parent-child hierarchy.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::HarnessDevice * FindNearestHarnessDevice
                (
                );
                /** Get the nearest @link Routing::Electrical::CableDevice Routing::Electrical::CableDevice@endlink  encountered up the parent-child hierarchy.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Electrical::CableDevice * FindNearestCableDevice
                (
                );
                /** Is the device a NX device?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool IsNxDevice
                (
                    NXOpen::Routing::Electrical::HarnessDevice * elecHarnessDevice /** elec harness device */ 
                );
                /** Is the device a connector?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool IsNxConnector
                (
                    NXOpen::Routing::Electrical::HarnessDevice * elecHarnessDevice /** elec harness device */ 
                );
                /** Is the device used in a routed connection?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool IsUsedInRoutedConnection
                (
                    NXOpen::Routing::Electrical::HarnessDevice * elecHarnessDevice /** elec harness device */ 
                );
                /** Unassign connector.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void UnassignConnector
                (
                );
                /** Assign a connector manually.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void ManuallyAssignConnector
                (
                    NXOpen::Assemblies::Component * elecConnectorPartOccurrence /** Component to assign. */
                );
                /** Find routed stock devices.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> FindRoutedStockDevices
                (
                );
                /** Get status of a connector device (assigned or not).  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: bool IsAssigned
                (
                );
                /** Find stock devices.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> FindStockDevices
                (
                );
                /** Find connections.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: std::vector<NXOpen::Routing::Electrical::Connection *> FindConnections
                (
                );
                /**Returns  the component name.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXString ComponentName
                (
                );
                /**Sets  the component name.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: void SetComponentName
                (
                    const NXString & componentName /** component name */ 
                );
                /** Get @link Routing::LogicalTerminal Routing::LogicalTerminal@endlink  given the name of the terminal.
                                If a terminal does not exists creates a terminal @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::LogicalTerminal * GetTerminal
                (
                    const NXString & terminalName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    bool createTerminal /** TRUE - creates a new terminal if one does not exist with given name*/
                );
                /** Find parts matching the connector device. Searches for "PART_NAME" 
                                property on connector device to search for matches in the part tables
                                Returns  all matching rows from the part tables.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: std::vector<NXOpen::Routing::CharacteristicList *> FindMatchingParts
                (
                );
                /** Searches for a placement port for the connector device. The placement
                                port is defined in the component list by attribute "DEVICE_PIN" or
                                "EQUIPMENT_PIN". If the attribute is not defined, searches for the 
                                first available port on the relating device.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Routing::Port * FindPlacer
                (
                    double* placerPos /** placer pos */ 
                );
                /** Loads the parts based on the @link Routing::CharacteristicList Routing::CharacteristicList@endlink 
                                adds the instance of the part to the current work part and places the 
                                instance on the placer.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") */
                public: NXOpen::Assemblies::Component * PlaceConnectorOnPort
                (
                    NXOpen::Routing::CharacteristicList * match /** match */ ,
                    NXOpen::Routing::Port * placer /** placer */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
