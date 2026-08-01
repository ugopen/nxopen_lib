from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AssignProxyBuilder(NXOpen.Builder): 
    """     
    Represents a NXOpen.Routing.Electrical.AssignProxyBuilder. This is used 
    to create a proxy port and assign it to a connector.
    """
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the position of the proxy port to be created.  
          
                  
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the position of the proxy port to be created.  
          
                  
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the direction of the proxy port to be created.  
          
                  
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the direction of the proxy port to be created.  
          
                  
         
        """
        pass
import NXOpen
class CableConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Electrical.CableConnection objects.
            
            See the NX Routing help for detailed information on the Connection data model.
            
        """
    def CreateCableConnection(self) -> CableConnection:
        """
         Creates a NXOpen.Routing.Electrical.CableConnection object. 
         Returns cable_connection ( CableConnection NXOpen.Routi):  .
        """
        pass
    def CreateShieldConnection(self) -> CableConnection:
        """
         Creates a NXOpen.Routing.Electrical.CableConnection object
                        implemented by a NXOpen.Routing.Electrical.ShieldDevice. 
         Returns cable_connection ( CableConnection NXOpen.Routi):  .
        """
        pass
class CableConnection(Connection): 
    """ Connection used by a NXOpen.Routing.Electrical.CableDevice.
            
            Use is similar to a NXOpen.Routing.Electrical.PathConnection, 
            except that a cable connection may have many paths due to many wire andor cable children.
            
            See the NX Routing help for detailed information on the Connection data model.
        """
    def IsCableRouted(self) -> bool:
        """
         Is this cable routed? 
         Returns is_routed (bool):  
                                        true The cable is routed.
                                        false The cable not routed.
                                    
                                .
        """
        pass
import NXOpen.Routing
class CableDefinition(NXOpen.Routing.AssemblyDefinition): 
    """ Holds the collection of wires in a NXOpen.Routing.Electrical.CableDevice.
            
            A cable consists of both a NXOpen.Routing.Electrical.CableDevice
            and a NXOpen.Routing.Electrical.CableDefinition.
            A NXOpen.Routing.Electrical.CableDevice object uses a 
            NXOpen.Routing.Electrical.CableDefinition to hold
            a collection of NXOpen.Routing.Electrical.WireDevice objects andor
            NXOpen.Routing.Electrical.CableDevice objects contained
            by the cable. This definition corresponds to AP212 Assembly_definition.
            
            See the NX Routing help for detailed information on the Connection data model.
        """
    pass
class CableDevice(ElectricalStockDevice): 
    """ Corresponds to a cable instance of an NXOpen.Routing.Electrical.ElectricalStockDevice.
            
            A cable consists of both a NXOpen.Routing.Electrical.CableDevice
            and a NXOpen.Routing.Electrical.CableDefinition.
            A NXOpen.Routing.Electrical.CableDevice object uses a 
            NXOpen.Routing.Electrical.CableDefinition to hold
            a collection of NXOpen.Routing.Electrical.WireDevice objects andor
            NXOpen.Routing.Electrical.CableDevice objects contained
            by the cable.
            
            See the NX Routing help for detailed information on the Connection data model.
        """
    def GetAssemblyDefinition(self) -> CableDefinition:
        """
         Returns the associated NXOpen.Routing.Electrical.CableDefinition. 
         Returns elec_cable_definition ( CableDefinition NXOpen.Routi):  .
        """
        pass
    def GetConduitPartNumber(self) -> str:
        """
         Returns the part number of the conduit applied over this NXOpen.Routing.Electrical.CableDevice
                        object. 
         Returns conduitPartNumber (str):  .
        """
        pass
    def ImportCablePart(self, part_name: str) -> None:
        """
         Loads the given cable part and imports the connections from given part and adds them as
                        children to the NXOpen.Routing.Electrical.CableDevice. 
        """
        pass
    def SetConduitPartNumber(self, conduitPartNumber: str) -> None:
        """
         Sets the part number of the conduit to be applied over this NXOpen.Routing.Electrical.CableDevice
                        object. 
        """
        pass
class CableStockDefinition(ElectricalStockDefinition): 
    """ Describes a cable's stock.
            
            Contains characteristics of the material that makes up the cable.
            
            See the NX Routing help for detailed information on the Connection data model.
        """
    @property
    def CableLocation(self) -> int:
        """
        Getter for property: (int) CableLocation
         Returnsthe cable stock's location   
            
         
        """
        pass
    @CableLocation.setter
    def CableLocation(self, locationValue: int):
        """
        Setter for property: (int) CableLocation
         Returnsthe cable stock's location   
            
         
        """
        pass
    @property
    def CoverThickness(self) -> float:
        """
        Getter for property: (float) CoverThickness
         Returnsthe thickness of the cable's covering.  
             
         
        """
        pass
    @CoverThickness.setter
    def CoverThickness(self, thicknessValue: float):
        """
        Setter for property: (float) CoverThickness
         Returnsthe thickness of the cable's covering.  
             
         
        """
        pass
    @property
    def WireSpacing(self) -> float:
        """
        Getter for property: (float) WireSpacing
         Returnsthe separation between wires in a cable.  
             
         
        """
        pass
    @WireSpacing.setter
    def WireSpacing(self, spacingValue: float):
        """
        Setter for property: (float) WireSpacing
         Returnsthe separation between wires in a cable.  
             
         
        """
        pass
import NXOpen
import NXOpen.Routing
class CablewaysBuilder(NXOpen.Builder): 
    """ Represents NXOpen.Routing.Electrical.CablewaysBuilder. """
    @property
    def AllowNewCables(self) -> bool:
        """
        Getter for property: (bool) AllowNewCables
         Returns the allow new cables toggle   
            
         
        """
        pass
    @AllowNewCables.setter
    def AllowNewCables(self, allowNewCables: bool):
        """
        Setter for property: (bool) AllowNewCables
         Returns the allow new cables toggle   
            
         
        """
        pass
    @property
    def AllowOverFill(self) -> bool:
        """
        Getter for property: (bool) AllowOverFill
         Returns the Allow Overfill toggle   
            
         
        """
        pass
    @AllowOverFill.setter
    def AllowOverFill(self, allowOverfill: bool):
        """
        Setter for property: (bool) AllowOverFill
         Returns the Allow Overfill toggle   
            
         
        """
        pass
    @property
    def CableTrayArea(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CableTrayArea
         Returns the cabletray area expression   
            
         
        """
        pass
    @property
    def CableTrayMaximumHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CableTrayMaximumHeight
         Returns the cabletray maximum height expression   
            
         
        """
        pass
    @property
    def CabletrayHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CabletrayHeight
         Returns the cabletray height expression   
            
         
        """
        pass
    @property
    def CabletrayWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CabletrayWidth
         Returns the cabletray width expression   
            
         
        """
        pass
    @property
    def FillPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FillPercentage
         Returns the fill percentage expression   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the route object collector   
            
         
        """
        pass
    @property
    def SpecifiedFillPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpecifiedFillPercentage
         Returns the specified fill percentage expression   
            
         
        """
        pass
import NXOpen
class CablewaysLayoutBuilder(NXOpen.Builder): 
    """ Represents NXOpen.Routing.Electrical.CablewaysLayoutBuilder. """
    pass
import NXOpen
class CablewaysLayoutViewCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Electrical.CablewaysLayoutView objects. """
    def CreateLayoutView(self, segment: NXOpen.Curve) -> CablewaysLayoutView:
        """
         Creates NXOpen.Routing.Electrical.CablewaysLayoutView object. 
                    Only one NXOpen.Routing.Electrical.CablewaysLayoutView object
                    can exist per segment, so if the object already exists, it returns the same.
                
         Returns view ( CablewaysLayoutView NXOpen.Routi): .
        """
        pass
import NXOpen
class CablewaysLayoutView(NXOpen.NXObject): 
    """ Represents the CablewaysLayoutView class. """
    def CondemnLayoutViewEntities(self) -> None:
        """
         Condemns the layout view entities. 
        """
        pass
    def FlipView(self) -> None:
        """
         Flips the layout view along view direction. 
        """
        pass
    def GetViewDirection(self) -> bool:
        """
         Returns the view direction. 
         Returns viewDirection (bool):  .
        """
        pass
    def GetViewMatrixAndOrigin(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Point3d]:
        """
         Returns the orientation matrix and origin associated with the layout view. 
         Returns A tuple consisting of (orientation, origin). 
         - orientation is:  NXOpen.Matrix3x3. .
         - origin is:  NXOpen.Point3d. .

        """
        pass
    def HighlightView(self) -> None:
        """
         Highlights the layout view. 
        """
        pass
    @overload
    def PositionLayoutView(self, orientation: NXOpen.Matrix3x3, origin: NXOpen.Point3d) -> None:
        """
          Positions the layout view in the 3D space as per input orientation matrix and origin. 
        """
        pass
    @overload
    def PositionLayoutView(self, toOrientation: NXOpen.Xform) -> None:
        """
          Positions the layout view in the 3D space as per the NXOpen.Xform. 
        """
        pass
    def UncondemnLayoutViewEntities(self) -> None:
        """
          Uncondemns the layout view entities. 
        """
        pass
    def UnhighlightView(self) -> None:
        """
         Unhighlights the layout view. 
        """
        pass
import NXOpen
class ConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Electrical.Connection objects.  """
    def GetConnections(self) -> List[Connection]:
        """
         Get Connections 
         Returns connections ( Connection List[NXOpen.Rou):  .
        """
        pass
import NXOpen.Routing
class Connection(NXOpen.Routing.LogicalConnection): 
    """ 
            The electrical usage of a NXOpen.Routing.LogicalConnection, restricted to
            one From and one To terminal.
            
            
            See NX Open Routing help for detailed information on the Connection data model.
            
        """
    class RouteLevel(Enum):
        """
        Members Include: 
         |NotRouted| 
         |Pin|  Route to the pin on the connector component. 
         |Component|  Route to the connector component directly without regard for the pins. 
         |Mixed|  Route to the pin, if possible, otherwise route to the component. 

        """
        NotRouted: int
        Pin: int
        Component: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> Connection.RouteLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FromTerminal(self) -> NXOpen.Routing.LogicalTerminal:
        """
        Getter for property: ( NXOpen.Routing.LogicalTerminal) FromTerminal
         Returns the From terminal.  
           The From terminal is one end of an electrical connection.  From does not imply an ordering.  
         
        """
        pass
    @FromTerminal.setter
    def FromTerminal(self, from_terminal: NXOpen.Routing.LogicalTerminal):
        """
        Setter for property: ( NXOpen.Routing.LogicalTerminal) FromTerminal
         Returns the From terminal.  
           The From terminal is one end of an electrical connection.  From does not imply an ordering.  
         
        """
        pass
    @property
    def MaximumPathLength(self) -> float:
        """
        Getter for property: (float) MaximumPathLength
         Returns the maximum path length for this connection.  
            Maximum path length is the longest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    @MaximumPathLength.setter
    def MaximumPathLength(self, path_length: float):
        """
        Setter for property: (float) MaximumPathLength
         Returns the maximum path length for this connection.  
            Maximum path length is the longest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    @property
    def MinimumPathLength(self) -> float:
        """
        Getter for property: (float) MinimumPathLength
         Returns the minimum path length for this connection.  
            Minimum path length is the shortest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    @MinimumPathLength.setter
    def MinimumPathLength(self, path_length: float):
        """
        Setter for property: (float) MinimumPathLength
         Returns the minimum path length for this connection.  
            Minimum path length is the shortest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    @property
    def PathLengthMultiplier(self) -> str:
        """
        Getter for property: (str) PathLengthMultiplier
         Returns the path length multiplier.  
            Used to calculate cut length.
                        Cut length = length  multiplier + offset   
         
        """
        pass
    @PathLengthMultiplier.setter
    def PathLengthMultiplier(self, path_length_multiplier: str):
        """
        Setter for property: (str) PathLengthMultiplier
         Returns the path length multiplier.  
            Used to calculate cut length.
                        Cut length = length  multiplier + offset   
         
        """
        pass
    @property
    def PathLengthOffset(self) -> str:
        """
        Getter for property: (str) PathLengthOffset
         Returns the path length offset.  
            Used to calculate cut length.
                        Cut length = length  multiplier + offset   
         
        """
        pass
    @PathLengthOffset.setter
    def PathLengthOffset(self, path_length_offset: str):
        """
        Setter for property: (str) PathLengthOffset
         Returns the path length offset.  
            Used to calculate cut length.
                        Cut length = length  multiplier + offset   
         
        """
        pass
    @property
    def ToTerminal(self) -> NXOpen.Routing.LogicalTerminal:
        """
        Getter for property: ( NXOpen.Routing.LogicalTerminal) ToTerminal
         Returns the To terminal.  
           The To terminal is one end of an electrical connection.  To does not imply an ordering  
         
        """
        pass
    @ToTerminal.setter
    def ToTerminal(self, to_terminal: NXOpen.Routing.LogicalTerminal):
        """
        Setter for property: ( NXOpen.Routing.LogicalTerminal) ToTerminal
         Returns the To terminal.  
           The To terminal is one end of an electrical connection.  To does not imply an ordering  
         
        """
        pass
    def AddIntermediateTerminal(self, intermediate_terminal: NXOpen.Routing.LogicalTerminal) -> bool:
        """
         Add an intermediate terminal to this connection
         Returns result (bool):  Was the NXOpen.Routing.LogicalTerminal added successfully?  .
        """
        pass
    def AssignPath(self, routeLevel: Connection.RouteLevel, path: NXOpen.Routing.Path) -> None:
        """
         Assigns the given path to this connection and routes the connection on the path using the given routing level.
                        Use NXOpen.Routing.Electrical.Connection.FindPaths to find all available paths for this connection.
                    
        """
        pass
    def AutomaticallyRoute(self, routeLevel: Connection.RouteLevel) -> None:
        """
         Automatically routes this connection on the shortest path using the given routing level. 
        """
        pass
    def FindFromConnector(self) -> ConnectorDevice:
        """
         Get the From Connector for this connection.  From does not imply an ordering. 
         Returns connector_device ( ConnectorDevice NXOpen.Routi):  May be   .
        """
        pass
    def FindNearestCableDevice(self) -> CableDevice:
        """
         Query this connection to find the nearest harness.
                        Only finds a cable that is a parent to this connection at some level up the connection heirarchy.
         Returns cable_device ( CableDevice NXOpen.Routi):  Will be  if connection is not in a cable .
        """
        pass
    def FindNearestHarnessDevice(self) -> HarnessDevice:
        """
         Query this connection to find the nearest harness.
                        Only finds a harness that is a parent to this connection at some level up the connection heirarchy. 
         Returns harness_device ( HarnessDevice NXOpen.Routi):  May be  if connection is not in a harness .
        """
        pass
    def FindNearestParentDevice(self) -> NXOpen.Routing.SingleDevice:
        """
         Queries this connection for the nearest parent device.  The nearest parent device is either
                        a cable, shield, or harness  
         Returns single_device ( NXOpen.Routing.SingleDevice):  Will be  if connection is not in a harness, cable, or shield. .
        """
        pass
    def FindPaths(self, routeLevel: Connection.RouteLevel) -> List[NXOpen.Routing.Path]:
        """
         Returns all the possible paths this connection can use. 
         Returns paths ( NXOpen.Routing.Path Li):  Possible paths this connection can use. .
        """
        pass
    def FindToConnector(self) -> ConnectorDevice:
        """
         Get the To Connector for this connection.  To does not imply an ordering 
         Returns connector_device ( ConnectorDevice NXOpen.Routi):  May be  .
        """
        pass
    def GetIntermediateTerminals(self) -> List[NXOpen.Routing.LogicalTerminal]:
        """
         Get the intermediate terminals associated with this connection. Intermediate Terminals are
                        optional and need not exist for a NXOpen.Routing.Electrical.Connection to be valid in NX.
         Returns intermediate_terminals ( NXOpen.Routing.LogicalTerminal Li):  Collection of intermediate NXOpen.Routing.LogicalTerminal - May be .
        """
        pass
    def GetRoutedLevel(self) -> str:
        """
         Gets the level used to route this connection. 
         Returns routed_level (str):  
                                                                           "C" Connection routed at component level
                                                                           "P" Connection routed at pin level
                                                                           "M" Connection routed at mixed level
                                                                            .
        """
        pass
    def GetRoutedLevelEnum(self) -> Connection.RouteLevel:
        """
         Similar to NXOpen.Routing.Electrical.Connection.GetRoutedLevel,
                        but returns the NXOpen.Routing.Electrical.Connection.RouteLevel enumeration instead of a string. 
         Returns route_level ( Connection.RouteLevel NXOpen.Routi):  Route level. .
        """
        pass
    def GetRoutingMethod(self) -> str:
        """
         Gets the method used to route this connection. 
         Returns routing_method (str):  
                                                                            "A" Connection is auto routed
                                                                            "M" Connection is manual routed
                                                                            "N" Connection is not routed
                                                                             .
        """
        pass
    def IsExternallyRouted(self) -> bool:
        """
                     Returns true if connection is routed externally, else returns false.
                    
         Returns is_externally_routed (bool): .
        """
        pass
    def IsRouted(self) -> bool:
        """
         Is this connection routed? 
         Returns is_routed (bool):  Is this connection routed? .
        """
        pass
    def RemoveIntermediateTerminal(self, intermediate_terminal: NXOpen.Routing.LogicalTerminal) -> bool:
        """
         Remove an intermediate terminal from this connection
         Returns result (bool):  Was the NXOpen.Routing.LogicalTerminal removed successfully?  .
        """
        pass
    def ReplaceIntermediateTerminals(self, intermediate_terminals: List[NXOpen.Routing.LogicalTerminal]) -> None:
        """
         Replaces the intermediate terminals associated with this connection. 
        """
        pass
    def Unroute(self) -> None:
        """
         Unroutes this connection. 
        """
        pass
import NXOpen
class ConnectorDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Electrical.ConnectorDevice (CD) objects.  """
    def AutoAssignConnectors(self, connectors: List[ConnectorDevice]) -> None:
        """
         Auto assignment is done using one
                    of the three matching methods, Part Name, Component Name or Attribute. 
        """
        pass
    @overload
    def CreateConnectorDevice(self, connector_type: ConnectorDevice.ComponentType, component_name: str) -> ConnectorDevice:
        """
         Creates a NXOpen.Routing.Electrical.ConnectorDevice. 
         Returns connector_device ( ConnectorDevice NXOpen.Routi):  .
        """
        pass
    @overload
    def CreateConnectorDevice(self, harness_device: HarnessDevice, equipment_name: str, connector_name: str, connector_type: ConnectorDevice.ComponentType) -> ConnectorDevice:
        """
         Finds or Creates a NXOpen.Routing.Electrical.ConnectorDevice for given equipmentName and or 
                        connectorName. Builds NXOpen.Routing.Electrical.ElectricalDeviceRelationship between 
                        equipment and connector, if equipmentName and connectorName are not .
                        Adds connector to harnessDevice, if connectorName and harnessDevice are not . 
         Returns connector_device ( ConnectorDevice NXOpen.Routi):  .
        """
        pass
    def GetConnectorSingleDevices(self) -> List[ConnectorDevice]:
        """
         Get connectors from the work part. 
         Returns connectors ( ConnectorDevice List[NXOpen.Rou):  .
        """
        pass
    def GetEquipmentSingleDevices(self) -> List[ConnectorDevice]:
        """
         Get equipment from the work part. 
         Returns equipment ( ConnectorDevice List[NXOpen.Rou):  .
        """
        pass
    def GetSpliceConnectorDevice(self, spliceName: str) -> ConnectorDevice:
        """
         Returns Splice NXOpen.Routing.Electrical.ConnectorDevice, based on the name provided. 
         Returns spliceSingleDevice ( ConnectorDevice NXOpen.Routi):  .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class ConnectorDevice(NXOpen.Routing.SingleDevice): 
    """
            The Electrical ConnectorDevice corresponds to a connector instance of
            NXOpen.Routing.SingleDevice.
        """
    class Assign(Enum):
        """
        Members Include: 
         |NotSet|  
         |Auto|  
         |Manual|  

        """
        NotSet: int
        Auto: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> ConnectorDevice.Assign:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentType(Enum):
        """
        Members Include: 
         |NotSet|  
         |Connector|  
         |Splice|  
         |Device|  
         |Other|  

        """
        NotSet: int
        Connector: int
        Splice: int
        Device: int
        Other: int
        @staticmethod
        def ValueOf(value: int) -> ConnectorDevice.ComponentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the component name.  
             
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, component_name: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name.  
             
         
        """
        pass
    @property
    def ConnectorType(self) -> ConnectorDevice.ComponentType:
        """
        Getter for property: ( ConnectorDevice.ComponentType NXOpen.Routi) ConnectorType
         Returns the connector type.  
             
         
        """
        pass
    @ConnectorType.setter
    def ConnectorType(self, elec_rlist_component: ConnectorDevice.ComponentType):
        """
        Setter for property: ( ConnectorDevice.ComponentType NXOpen.Routi) ConnectorType
         Returns the connector type.  
             
         
        """
        pass
    def AutomaticallyAssignConnector(self, elec_connector_part_occurrence: NXOpen.Assemblies.Component) -> None:
        """
         Assigns a connector to the given compoent and sets the assignment method to "automatically assigned". 
        """
        pass
    def FindConnections(self) -> List[Connection]:
        """
         Find connections. 
         Returns connections ( Connection List[NXOpen.Rou):  .
        """
        pass
    def FindMatchingParts(self) -> List[NXOpen.Routing.CharacteristicList]:
        """
         Find parts matching the connector device. Searches for "PART_NAME" 
                        property on connector device to search for matches in the part tables
                        Returns  all matching rows from the part tables. 
         Returns matches ( NXOpen.Routing.CharacteristicList Li):  .
        """
        pass
    def FindNearestCableDevice(self) -> CableDevice:
        """
         Get the nearest NXOpen.Routing.Electrical.CableDevice encountered up the parent-child hierarchy. 
         Returns elec_nearest_cable_device ( CableDevice NXOpen.Routi):  .
        """
        pass
    def FindNearestHarnessDevice(self) -> HarnessDevice:
        """
         Get the nearest NXOpen.Routing.Electrical.HarnessDevice encountered up the parent-child hierarchy. 
         Returns elec_nearest_harness_device ( HarnessDevice NXOpen.Routi):  .
        """
        pass
    def FindPlacementPort(self) -> Tuple[NXOpen.Routing.Port, NXOpen.Point3d]:
        """
         Searches for a placement port for the connector device. The placement
                        port is defined in the component list by attribute "DEVICE_PIN", 
                        "EQUIPMENT_PIN", or "MODULAR_PARENT_POSITION". If the attribute is not defined,
                        searches for the first available port on the relating device.
                    
         Returns A tuple consisting of (port, portPosition). 
         - port is:  NXOpen.Routing.Port.
         - portPosition is:  NXOpen.Point3d. The position of the port in the context of the work part. .

        """
        pass
    def FindRoutedStockDevices(self) -> List[ElectricalStockDevice]:
        """
         Find routed stock devices. 
         Returns routed_stock_devices ( ElectricalStockDevice List[NXOpen.Rou):  .
        """
        pass
    def FindStockDevices(self) -> List[ElectricalStockDevice]:
        """
         Find stock devices. 
         Returns stock_devices ( ElectricalStockDevice List[NXOpen.Rou):  .
        """
        pass
    def GetAssignMethod(self) -> ConnectorDevice.Assign:
        """
         Get assign method. 
         Returns elec_connector_device_assign_method ( ConnectorDevice.Assign NXOpen.Routi):  .
        """
        pass
    def GetPartDefinition(self) -> ElectricalPartDefinitionShadow:
        """
         Get part definition. 
         Returns elec_part_definition_shadow ( ElectricalPartDefinitionShadow NXOpen.Routi):  .
        """
        pass
    def GetTerminal(self, terminal_name: str, create_terminal: bool) -> NXOpen.Routing.LogicalTerminal:
        """
         Get NXOpen.Routing.LogicalTerminal given the name of the terminal.
                        If a terminal does not exists creates a terminal
         Returns terminal ( NXOpen.Routing.LogicalTerminal):  .
        """
        pass
    def GetTerminals(self) -> List[NXOpen.Routing.LogicalTerminal]:
        """
         Get terminals. 
         Returns route_terminals ( NXOpen.Routing.LogicalTerminal Li):  .
        """
        pass
    def IsAssigned(self) -> bool:
        """
         Get status of a connector device (assigned or not). 
         Returns result (bool):  .
        """
        pass
    def IsNxConnector(self, elec_harness_device: HarnessDevice) -> bool:
        """
         Is the device a connector? 
         Returns result (bool):  .
        """
        pass
    def IsNxDevice(self, elec_harness_device: HarnessDevice) -> bool:
        """
         Is the device a NX device? 
         Returns result (bool):  .
        """
        pass
    def IsUsedInRoutedConnection(self, elec_harness_device: HarnessDevice) -> bool:
        """
         Is the device used in a routed connection? 
         Returns result (bool):  .
        """
        pass
    def ManuallyAssignConnector(self, elec_connector_part_occurrence: NXOpen.Assemblies.Component) -> None:
        """
         Assign a connector manually. 
        """
        pass
    def ManuallyAssignConnectorGroup(self, elec_connector_group: NXOpen.Group) -> None:
        """
         Assign a connector manually for object NXOpen.Group. 
        """
        pass
    def PlaceConnectorOnPort(self, match: NXOpen.Routing.CharacteristicList, placer: NXOpen.Routing.Port) -> NXOpen.Assemblies.Component:
        """
         Loads the parts based on the NXOpen.Routing.CharacteristicList
                        adds the instance of the part to the current work part and places the 
                        instance on the placer. 
         Returns nxComp ( NXOpen.Assemblies.Component):  .
        """
        pass
    def ProxyAssignConnector(self, proxy: NXOpen.Routing.Port) -> None:
        """
         Assign a connector to a proxy port. 
        """
        pass
    def RemoveTerminal(self, route_terminal_to_remove: NXOpen.Routing.LogicalTerminal) -> bool:
        """
         Remove a terminal. 
         Returns result (bool):  .
        """
        pass
    def SetPartDefinition(self, elec_part_definition_shadow: ElectricalPartDefinitionShadow) -> None:
        """
         Sets part definition. 
        """
        pass
    def UnassignConnector(self) -> None:
        """
         Unassign connector. 
        """
        pass
class DerivativeDefinition(HarnessDefinition): 
    """ Represents a NXOpen.Routing.Electrical.DerivativeDefinition """
    pass
import NXOpen
class DerivativeDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Routing.Electrical.DerivativeDevice objects.  """
    def CreateDerivativeDevice(self) -> DerivativeDevice:
        """
         Creates Routing.Electrical.DerivativeDevice with given name. 
         Returns derivative_device ( DerivativeDevice NXOpen.Routi):  .
        """
        pass
    def GetDerivativeSingleDevices(self) -> List[DerivativeDevice]:
        """
         Get derivatives 
         Returns derivatives ( DerivativeDevice List[NXOpen.Rou):  .
        """
        pass
class DerivativeDevice(HarnessDevice): 
    """
            The Electrical DerivativeDevice corresponds to a derivative instance of the 
            Routing.Electrical.HarnessDevice.
        """
    def GetDerivativeDefinition(self) -> DerivativeDefinition:
        """
         Get derivative definition. 
         Returns elec_derivative_definition ( DerivativeDefinition NXOpen.Routi):  .
        """
        pass
import NXOpen
class ElectricalDeviceRelationshipCollection(NXOpen.TaggedObjectCollection): 
    """
             Represents a collection of NXOpen.Routing.Electrical.ElectricalDeviceRelationship objects.
           
        """
    def CreateElectricalDeviceRelationship(self) -> ElectricalDeviceRelationship:
        """
         Creates a NXOpen.Routing.Electrical.ElectricalDeviceRelationship object. 
         Returns electrical_device_relationship ( ElectricalDeviceRelationship NXOpen.Routi):  .
        """
        pass
import NXOpen.Routing
class ElectricalDeviceRelationship(NXOpen.Routing.DeviceRelationship): 
    """
             Represents a relationship between Routing Electrical devices.
           
           
             Use this class to associate electrical connectors to electrical equipment outside of a harness.
            
           
            (example)
                Use an ElectricalDeviceRelationship to represent connectors C1 and C2 mounted on a piece of equipment, D1.
                The Relating object is D1 and the Related objects are C1 and C2.
           
        """
    pass
import NXOpen
class ElectricalFormatCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a Routing NXOpen.Routing.Electrical.ElectricalFormatCollection object.
         """
    def CreateFormat(self, name: str, type: ElectricalFormat.Type) -> ElectricalFormat:
        """
         Creates a NXOpen.Routing.Electrical.ElectricalFormat object. 
         Returns format ( ElectricalFormat NXOpen.Routi):  .
        """
        pass
    def GetDisplayFormat(self, type: ElectricalFormat.Type) -> ElectricalFormat:
        """
         Get the displayed NXOpen.Routing.Electrical.ElectricalFormat object for the
                        given navigator type. 
         Returns format ( ElectricalFormat NXOpen.Routi):  .
        """
        pass
    def SetDisplayFormat(self, type: ElectricalFormat.Type, format: ElectricalFormat) -> None:
        """
         Set the NXOpen.Routing.Electrical.ElectricalFormat object as displayed
                        format for the given navigator type. 
        """
        pass
import NXOpen
class ElectricalFormat(NXOpen.TaggedObject): 
    """ Represents a Routing Electrical ElectricalFormat.
         """
    class Type(Enum):
        """
        Members Include: 
         |Connections|  
         |Components|  

        """
        Connections: int
        Components: int
        @staticmethod
        def ValueOf(value: int) -> ElectricalFormat.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FormatType(self) -> ElectricalFormat.Type:
        """
        Getter for property: ( ElectricalFormat.Type NXOpen.Routi) FormatType
         Returns the type of  NXOpen::Routing::Electrical::ElectricalFormat    
            
         
        """
        pass
    @FormatType.setter
    def FormatType(self, type: ElectricalFormat.Type):
        """
        Setter for property: ( ElectricalFormat.Type NXOpen.Routi) FormatType
         Returns the type of  NXOpen::Routing::Electrical::ElectricalFormat    
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of  NXOpen::Routing::Electrical::ElectricalFormat    
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of  NXOpen::Routing::Electrical::ElectricalFormat    
            
         
        """
        pass
import NXOpen
class ElectricalNavigatorFilterCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a Routing NXOpen.Routing.Electrical.ElectricalNavigatorFilterCollection object.
         """
    def CreateFilter(self, name: str, clause: str) -> ElectricalNavigatorFilter:
        """
         Creates a NXOpen.Routing.Electrical.ElectricalNavigatorFilter object. 
         Returns filter ( ElectricalNavigatorFilter NXOpen.Routi):  .
        """
        pass
    def GetDisplayFilter(self, type: ElectricalFormat.Type) -> ElectricalNavigatorFilter:
        """
         Get the displayed NXOpen.Routing.Electrical.ElectricalNavigatorFilter object
                        for the given navigator type 
         Returns filter ( ElectricalNavigatorFilter NXOpen.Routi):  .
        """
        pass
    def SetDisplayFilter(self, type: ElectricalFormat.Type, filter: ElectricalNavigatorFilter) -> None:
        """
         Set the NXOpen.Routing.Electrical.ElectricalNavigatorFilter object as 
                        displayed filter for given navigator type. 
        """
        pass
import NXOpen
class ElectricalNavigatorFilter(NXOpen.NavigatorFilter): 
    """ Represents a Routing Electrical Navigator Filter object.
         """
    pass
import NXOpen.Routing
class ElectricalPartDefinitionShadow(NXOpen.Routing.PartDefinitionShadow): 
    """ Represents NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow object """
    pass
import NXOpen.Routing
class ElectricalStockDefinition(NXOpen.Routing.StockDefinition): 
    """ Represents NXOpen.Routing.Electrical.ElectricalStockDefinition object """
    class SectionType(Enum):
        """
        Members Include: 
         |Circular|  
         |Rectangular|  

        """
        Circular: int
        Rectangular: int
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDefinition.SectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CrossSectionType(self) -> ElectricalStockDefinition.SectionType:
        """
        Getter for property: ( ElectricalStockDefinition.SectionType NXOpen.Routi) CrossSectionType
         Returns  the cross section type of stock   
            
         
        """
        pass
    @CrossSectionType.setter
    def CrossSectionType(self, sectionType: ElectricalStockDefinition.SectionType):
        """
        Setter for property: ( ElectricalStockDefinition.SectionType NXOpen.Routi) CrossSectionType
         Returns  the cross section type of stock   
            
         
        """
        pass
    @property
    def Gauge(self) -> float:
        """
        Getter for property: (float) Gauge
         Returns  the gauge of stock   
            
         
        """
        pass
    @Gauge.setter
    def Gauge(self, gaugeValue: float):
        """
        Setter for property: (float) Gauge
         Returns  the gauge of stock   
            
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns  the height of stock   
            
         
        """
        pass
    @Height.setter
    def Height(self, heightValue: float):
        """
        Setter for property: (float) Height
         Returns  the height of stock   
            
         
        """
        pass
    @property
    def LinearDensity(self) -> float:
        """
        Getter for property: (float) LinearDensity
         Returns  the linear density of stock    
            
         
        """
        pass
    @LinearDensity.setter
    def LinearDensity(self, densityValue: float):
        """
        Setter for property: (float) LinearDensity
         Returns  the linear density of stock    
            
         
        """
        pass
    @property
    def MinBendRadius(self) -> float:
        """
        Getter for property: (float) MinBendRadius
         Returns  the min bend radius of stock   
            
         
        """
        pass
    @MinBendRadius.setter
    def MinBendRadius(self, radiusValue: float):
        """
        Setter for property: (float) MinBendRadius
         Returns  the min bend radius of stock   
            
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of stock   
            
         
        """
        pass
    @Width.setter
    def Width(self, widthValue: float):
        """
        Setter for property: (float) Width
         Returns the width of stock   
            
         
        """
        pass
    @property
    def WireType(self) -> str:
        """
        Getter for property: (str) WireType
         Returns  the wire type of stock   
            
         
        """
        pass
    @WireType.setter
    def WireType(self, wireType: str):
        """
        Setter for property: (str) WireType
         Returns  the wire type of stock   
            
         
        """
        pass
import NXOpen
class ElectricalStockDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Electrical.ElectricalStockDevice (ESD) objects.  """
    def AssignStock(self, stock_devices: List[ElectricalStockDevice], route_type: ElectricalStockDevice.RouteTypes) -> None:
        """
         Assign NXOpen.Routing.Stock to input stock devices.
                        The assigned NXOpen.Routing.Stock is a bundle stock,
                        and the routine will perform the bundling calculations. This routine
                        should also be called after performing NXOpen.Routing.Electrical.ElectricalStockDevice.ManuallyRoute. 
        """
        pass
    def AutoRouteAll(self, route_level: ElectricalStockDevice.RouteLevel, route_sel: ElectricalStockDevice.AutoRouteSel) -> Tuple[int, NXOpen.ErrorList]:
        """
         Automatically routes all of the stock devices in the work part. Routing can be done
                        on pin, component or mixed level and it is based on shortest length
                        (See NXOpen.Routing.Electrical.ElectricalStockDevice for more details). 
         Returns A tuple consisting of (no_of_routed_stock_devices, error_list). 
         - no_of_routed_stock_devices is: int. .
         - error_list is:  NXOpen.ErrorList. Any errors that occurred during Automatic Routing. .

        """
        pass
    def AutoRouteConnections(self, route_level: ElectricalStockDevice.RouteLevel, route_sel: ElectricalStockDevice.AutoRouteSel, stock_devices: List[ElectricalStockDevice]) -> Tuple[int, NXOpen.ErrorList]:
        """
         Automatically routes the selected stock devices. Routing can be done
                        on pin, component or mixed level and it is based on shortest length
                        (See NXOpen.Routing.Electrical.ElectricalStockDevice for more details). 
         Returns A tuple consisting of (no_of_routed_stock_devices, error_list). 
         - no_of_routed_stock_devices is: int. .
         - error_list is:  NXOpen.ErrorList. Any errors that occurred during Automatic Routing. .

        """
        pass
    def GetElectricalStockDevicesInPart(self) -> List[ElectricalStockDevice]:
        """
         Returns the electrical stock devices in part. 
         Returns stockDevices ( ElectricalStockDevice List[NXOpen.Rou): .
        """
        pass
    def RemoveStock(self, stock_devices: List[ElectricalStockDevice]) -> List[ElectricalStockDevice]:
        """
         Removes NXOpen.Routing.Stock from input stock devices.
                        Removes all segments from input wires and updates harnesses associated 
                        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                        the NXOpen.Routing.Wire. 
         Returns removed_stock_devices ( ElectricalStockDevice List[NXOpen.Rou):  .
        """
        pass
    def Unroute(self, stock_devices: List[ElectricalStockDevice]) -> List[ElectricalStockDevice]:
        """
         Removes all bundle NXOpen.Routing.Stock from input stock devices.
                        Removes all segments from input wires and updates harnesses associated 
                        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                        the NXOpen.Routing.Wire. Use this when no rebundling is 
                        necessary 
         Returns removed_stock_devices ( ElectricalStockDevice List[NXOpen.Rou):  .
        """
        pass
    def UnrouteAll(self) -> List[ElectricalStockDevice]:
        """
         Removes all bundle NXOpen.Routing.Stock from all stock devices.
                        Removes all segments from input wires and updates harnesses associated 
                        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                        the NXOpen.Routing.Wire. Use this when no rebundling is 
                        necessary 
         Returns removed_stock_devices ( ElectricalStockDevice List[NXOpen.Rou):  .
        """
        pass
import NXOpen
import NXOpen.Routing
class ElectricalStockDevice(NXOpen.Routing.StockDevice): 
    """
           The Electrical Stock Device is a non instantiable superclass to classify
           all electrical stock-based single devices.
        """
    class AutoRouteSel(Enum):
        """
        Members Include: 
         |BundleDiameter|  
         |LeastBundles|  
         |DesignRules|  
         |LeastSegments|  
         |ShortestLength|  

        """
        BundleDiameter: int
        LeastBundles: int
        DesignRules: int
        LeastSegments: int
        ShortestLength: int
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDevice.AutoRouteSel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RouteLevel(Enum):
        """
        Members Include: 
         |Pin|  
         |Comp|  
         |Mixed|  
         |Partial|  

        """
        Pin: int
        Comp: int
        Mixed: int
        Partial: int
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDevice.RouteLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RouteTypes(Enum):
        """
        Members Include: 
         |DefaultRoute|  
         |AutoRoute|  
         |ManualRoute|  

        """
        DefaultRoute: int
        AutoRoute: int
        ManualRoute: int
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDevice.RouteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorName(self) -> str:
        """
        Getter for property: (str) ColorName
         Returns the color name.  
             
         
        """
        pass
    @ColorName.setter
    def ColorName(self, color_name: str):
        """
        Setter for property: (str) ColorName
         Returns the color name.  
             
         
        """
        pass
    @property
    def CutLength(self) -> float:
        """
        Getter for property: (float) CutLength
         Returns the cut length.  
             
         
        """
        pass
    @CutLength.setter
    def CutLength(self, cut_length: float):
        """
        Setter for property: (float) CutLength
         Returns the cut length.  
             
         
        """
        pass
    @property
    def NxColorValue(self) -> int:
        """
        Getter for property: (int) NxColorValue
         Returns the NX color value.  
             
         
        """
        pass
    @NxColorValue.setter
    def NxColorValue(self, nx_color_value: int):
        """
        Setter for property: (int) NxColorValue
         Returns the NX color value.  
             
         
        """
        pass
    def CalculateCutLength(self) -> float:
        """
         Calculates and sets cut length on object. 
         Returns cut_length (float):  Calculated cut length .
        """
        pass
    def ChangeHarness(self, harness_device: HarnessDevice) -> None:
        """
         Adds this stockdevice as child of given HarnessDevice. 
        """
        pass
    def FindFromConnector(self) -> ConnectorDevice:
        """
         Find the from connector for this stock device. If there is no
                    from connector,  is returned. 
         Returns from_connector ( ConnectorDevice NXOpen.Routi):  .
        """
        pass
    def FindImplementedConnection(self) -> Connection:
        """
         Find the NXOpen.Routing.Electrical.Connection implemented by this device. 
         Returns implemented_connection ( Connection NXOpen.Routi):  .
        """
        pass
    def FindNearestHarnessDefinition(self) -> HarnessDefinition:
        """
         Get nearest NXOpen.Routing.Electrical.HarnessDefinition encountered up the parent-child hierarchy. 
         Returns elec_harness_definition ( HarnessDefinition NXOpen.Routi):  .
        """
        pass
    def FindNearestHarnessDevice(self) -> HarnessDevice:
        """
         Find the nearest NXOpen.Routing.Electrical.HarnessDevice encountered up the parent-child hierarchy. 
         Returns elec_harness_device ( HarnessDevice NXOpen.Routi):  .
        """
        pass
    def FindToConnector(self) -> ConnectorDevice:
        """
         Find the to connector for this stock device. If there is no
                    to connector,  is returned. 
         Returns to_connector ( ConnectorDevice NXOpen.Routi):  .
        """
        pass
    def FindTopmostCableDefinition(self) -> CableDefinition:
        """
         Get topmost NXOpen.Routing.Electrical.CableDefinition encountered up the parent-child hierarchy. 
         Returns elec_cable_definition ( CableDefinition NXOpen.Routi):  .
        """
        pass
    def GetCapitalBundleSolids(self) -> List[NXOpen.Body]:
        """
         Gets the solid bodies representing the bundles created when importing data from Capital. 
         Returns bodies ( NXOpen.Body Li): .
        """
        pass
    def GetIntermediateComponents(self) -> List[ConnectorDevice]:
        """
         Get intermediate components 
         Returns intermediate_components ( ConnectorDevice List[NXOpen.Rou):  .
        """
        pass
    def GetIntermediateTerminals(self) -> List[NXOpen.Routing.LogicalTerminal]:
        """
         Get the intermediate terminals associated to this stock device. 
         Returns intermediate_terminals ( NXOpen.Routing.LogicalTerminal Li):  .
        """
        pass
    def HasIntermediateComponents(self) -> bool:
        """
         Does this stock device have intermediate components? 
         Returns result (bool):  .
        """
        pass
    def ManuallyRoute(self, route_level: ElectricalStockDevice.RouteLevel, segments: List[NXOpen.Routing.ISegment]) -> None:
        """
         Manually routes a NXOpen.Routing.Electrical.ElectricalStockDevice. 
                        on given NXOpen.Routing.ISegment. The input segments should form a continuous 
                        path between two NXOpen.Routing.Electrical.ConnectorDevice objects. 
        """
        pass
import NXOpen.Routing
class HarnessDefinition(NXOpen.Routing.AssemblyDefinition): 
    """ Represents a NXOpen.Routing.Electrical.HarnessDefinition """
    def GetChildConnections(self) -> List[Connection]:
        """
         Returns all of the Connection objects that are implemented by single devices
                        that are children of this harness
                      
         Returns connections ( Connection List[NXOpen.Rou): .
        """
        pass
import NXOpen
class HarnessDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Routing.Electrical.HarnessDevice objects.  """
    @overload
    def CreateHarnessDevice(self) -> HarnessDevice:
        """
         Creates Routing.Electrical.HarnessDevice. 
         Returns harness_device ( HarnessDevice NXOpen.Routi):  .
        """
        pass
    @overload
    def CreateHarnessDevice(self, harness_name: str) -> HarnessDevice:
        """
         Creates Routing.Electrical.HarnessDevice with given name. 
         Returns harness_device ( HarnessDevice NXOpen.Routi):  .
        """
        pass
    def GetHarnessSingleDevices(self) -> List[HarnessDevice]:
        """
         Get harnesses 
         Returns harnesses ( HarnessDevice List[NXOpen.Rou):  .
        """
        pass
import NXOpen.Routing
class HarnessDevice(NXOpen.Routing.SingleDevice): 
    """
            The Electrical HarnessDevice corresponds to a harness instance of the 
            Routing.SingleDevice.
        """
    def GetHarnessDefinition(self) -> HarnessDefinition:
        """
         Get harness definition. 
         Returns elec_harness_definition ( HarnessDefinition NXOpen.Routi):  .
        """
        pass
import NXOpen
class JumperConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ A collection of NXOpen.Routing.Electrical.JumperConnection objects. """
    def CreateJumperConnection(self) -> JumperConnection:
        """
         Creates a NXOpen.Routing.Electrical.JumperConnection object. 
         Returns jumper_connection ( JumperConnection NXOpen.Routi):  A NXOpen.Routing.Electrical.JumperConnection .
        """
        pass
class JumperConnection(PathConnection): 
    """ 
           A jumper connection connects ports on the same connector.
                      
           
           A path may or may not be associated with this type of connection.  
           Specifies that terminals on the same part instance are connected somehow.
           See NX Open Routing help for detailed information on the Connection data model.
           
           
        """
    pass
import NXOpen
class NonPathConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ 
            A collection of NXOpen.Routing.Electrical.NonPathConnection objects.
            
            
            See NX Open Routing help for detailed information on the Connection data model.
            
         """
    def CreateNonPathConnection(self) -> NonPathConnection:
        """
         Creates a NXOpen.Routing.Electrical.NonPathConnection object. 
         Returns non_path_connection ( NonPathConnection NXOpen.Routi):  A NXOpen.Routing.Electrical.NonPathConnection  .
        """
        pass
class NonPathConnection(Connection): 
    """ 
            Describes a connection that does not have a path
            
            
            A pathless connection represents the abilitiy for objects to be 
            connected even though there is not an explicit path between them.
            See NX Open Routing help for detailed information on the Connection data model.
            
        """
    pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class PathArrangementBuilder(NXOpen.Builder): 
    """ Builder class to manage Path Arrangements.
    """
    @property
    def HarnessPartOccurrence(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) HarnessPartOccurrence
         Returns the harness component in the context of the part that was used to create the extracted port.  
             
         
        """
        pass
    @HarnessPartOccurrence.setter
    def HarnessPartOccurrence(self, partOcc: NXOpen.Assemblies.Component):
        """
        Setter for property: ( NXOpen.Assemblies.Component) HarnessPartOccurrence
         Returns the harness component in the context of the part that was used to create the extracted port.  
             
         
        """
        pass
    @property
    def PrototypePort(self) -> NXOpen.Routing.Port:
        """
        Getter for property: ( NXOpen.Routing.Port) PrototypePort
         Returns the prototype of the extract port that is used as the reference port.  
             
         
        """
        pass
    @PrototypePort.setter
    def PrototypePort(self, port: NXOpen.Routing.Port):
        """
        Setter for property: ( NXOpen.Routing.Port) PrototypePort
         Returns the prototype of the extract port that is used as the reference port.  
             
         
        """
        pass
    @property
    def PrototypePortPartOccurrence(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) PrototypePortPartOccurrence
         Returns the component part that contains the prototype of the extract port that is used as the reference
                    port.  
             
         
        """
        pass
    @PrototypePortPartOccurrence.setter
    def PrototypePortPartOccurrence(self, partOcc: NXOpen.Assemblies.Component):
        """
        Setter for property: ( NXOpen.Assemblies.Component) PrototypePortPartOccurrence
         Returns the component part that contains the prototype of the extract port that is used as the reference
                    port.  
             
         
        """
        pass
    @property
    def ReferencePort(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ReferencePort
         Returns the port on which the offset is based when defining the path arrangement.  
           The port property
                    can be either a port or a port occurrence.   
         
        """
        pass
    @ReferencePort.setter
    def ReferencePort(self, port: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ReferencePort
         Returns the port on which the offset is based when defining the path arrangement.  
           The port property
                    can be either a port or a port occurrence.   
         
        """
        pass
    def ClearHarnessData(self) -> None:
        """
         Clears the builder data associated with stored harness, namely the ReferencePort and
                  the HarnessOccurrence, along with internal data. Note that the PrototypePortPartOccurrence
                  and the PrototypePort are not cleared with this call.  
        """
        pass
    def DeletePathArrangement(self) -> None:
        """
         Deletes path arrangement through builder 
        """
        pass
    def EstablishPathArrangement(self) -> None:
        """
         Retrieves the Path Arrangement object based on the data stored in the builder. If one does not
                    yet exist, a new one will be created. The retrieved object is stored internally in the biuilder.
                    This method is called after setting HarnessPartOccurrence and ReferencePort 
        """
        pass
    def InitializeBuilderFromArrangedPort(self, port: NXOpen.Routing.Port) -> None:
        """
         Initializes builder from arranged port 
        """
        pass
    def SetPathArrangementOrigin(self, point: NXOpen.Point3d) -> None:
        """
         Sets a new origin for the point on the harness path. This point should be in the
                    context of the current root part. 
        """
        pass
import NXOpen
class PathConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ 
            A collection of NXOpen.Routing.Electrical.PathConnection objects.
            
            
            See NX Open Routing help for detailed information on the Connection data model.
            
         """
    def CreatePathConnection(self) -> PathConnection:
        """
         Create a NXOpen.Routing.Electrical.PathConnection object. 
         Returns path_connection ( PathConnection NXOpen.Routi):  A NXOpen.Routing.Electrical.PathConnection .
        """
        pass
class PathConnection(Connection): 
    """ 
            Describes a connection that has a path
            
            
            From and To terminals are not coincident and need a path definition to be routable.            
            See NX Open Routing help for detailed information on the Connection data model.
            
        """
    pass
class ShieldDefinition(CableDefinition): 
    """ Represents Routing Electrical ShieldDefinition object """
    pass
class ShieldDevice(CableDevice): 
    """
            The Electrical ShieldDevice corresponds to a shield instance of
            Routing.Electrical.ElectricalStockDevice. 
            An electrical shield device is both an assembly definition and a electrical stock device.
        """
    pass
class ShieldStockDefinition(CableStockDefinition): 
    """ Represents Routing Electrical ShieldStockDefinition object """
    pass
import NXOpen
class SortConnectionsPluginData(NXOpen.TaggedObject): 
    """ Data object created by Routing just before routing connections.
            Routing sends this object to any registered Sort Connections plugin with the
            "Stock Devices to sort" filled in.

            It is the Sort Connections plugin responsibility to sort the Stock Devices and
            to put the sorted Stock Devices into "Sorted Stock Devices".

            For more information, see Routing.CustomManager and the
            Routing.CustomManager.SetSortConnectionsPlugin
        """
    def GetStockDevicesToSort(self) -> List[ElectricalStockDevice]:
        """
         Gets the stock devices such as Routing.Electrical.WireDevices
                        that implement connections Routing is about to route along their paths. 
         Returns stockDevices ( ElectricalStockDevice List[NXOpen.Rou):  The Routing.Electrical.ElectricalStockDevices to sort in the order in which
                            you want to route them. .
        """
        pass
    def SetSortedStockDevices(self, stockDevices: List[ElectricalStockDevice]) -> None:
        """
         Sets the stock devices sorted in the order in which you want their connections to route. 
        """
        pass
import NXOpen
class SplicePointCollection(NXOpen.TaggedObjectCollection): 
    """ The collection of all NXOpen.Routing.Electrical.SplicePoints.
            Use the NXOpen.Routing.Electrical.SplicePositionBuilder to create
            a NXOpen.Routing.Electrical.SplicePoint.
        """
    pass
import NXOpen
import NXOpen.Features
class SplicePoint(NXOpen.Point): 
    """ Represents a NXOpen.Routing.Electrical.SplicePoint. """
    @property
    def AdditionalLength(self) -> float:
        """
        Getter for property: (float) AdditionalLength
         Returns the additional length required for a wire using this splice point.  
             
         
        """
        pass
    @property
    def ConnectorDevice(self) -> ConnectorDevice:
        """
        Getter for property: ( ConnectorDevice NXOpen.Routi) ConnectorDevice
         Returns the  Routing::Electrical::ConnectorDevice  to which this splice is assigned.  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of this splice point.  
             
         
        """
        pass
    @property
    def SphereFeature(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) SphereFeature
         Returns the sphere feature that represents this splice point.  
             
         
        """
        pass
import NXOpen
import NXOpen.Routing
class SplicePositionBuilder(NXOpen.Builder): 
    """ Represents NXOpen.Routing.Electrical.SplicePositionBuilder. """
    @property
    def AdditionalLength(self) -> float:
        """
        Getter for property: (float) AdditionalLength
         Returns the additional length required for the wire for the fabrication of splice.  
             
         
        """
        pass
    @AdditionalLength.setter
    def AdditionalLength(self, additionalLength: float):
        """
        Setter for property: (float) AdditionalLength
         Returns the additional length required for the wire for the fabrication of splice.  
             
         
        """
        pass
    @property
    def DistanceForSplicePoint(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceForSplicePoint
         Returns the distance for splice point from the inferred anchor node on route section.  
             
         
        """
        pass
    @property
    def PointOnPath(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnPath
         Returns the point on pathcurve selected by user to position a splice   
            
         
        """
        pass
    @PointOnPath.setter
    def PointOnPath(self, pointOnPath: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnPath
         Returns the point on pathcurve selected by user to position a splice   
            
         
        """
        pass
    @property
    def SpliceName(self) -> str:
        """
        Getter for property: (str) SpliceName
         Returns the splice name given by NX user or received from capital.  
             
         
        """
        pass
    @SpliceName.setter
    def SpliceName(self, spliceName: str):
        """
        Setter for property: (str) SpliceName
         Returns the splice name given by NX user or received from capital.  
             
         
        """
        pass
    @property
    def SwitchRouteNode(self) -> bool:
        """
        Getter for property: (bool) SwitchRouteNode
         Returns the switch route node can be used by user to highlight and store the route node opposite to the inferred anchor node.  
             
         
        """
        pass
    @SwitchRouteNode.setter
    def SwitchRouteNode(self, switchRouteNode: bool):
        """
        Setter for property: (bool) SwitchRouteNode
         Returns the switch route node can be used by user to highlight and store the route node opposite to the inferred anchor node.  
             
         
        """
        pass
    def SetDistanceFromAnchorNode(self, distanceForSplicePoint: float) -> None:
        """
         The automation user has to set distance to place a splice on route section. The distance would be considered from the start node
                        of the route section. 
        """
        pass
    def SetEndRouteNodesOfRouteSection(self, startRouteNode: NXOpen.Routing.ControlPoint, endRouteNode: NXOpen.Routing.ControlPoint) -> None:
        """
         The automation user has to set the end route nodes of the route section in order to place splice on route section. 
        """
        pass
    def SetTotalCurveLengthOfRouteSection(self, totalLengthOfRouteSection: float) -> None:
        """
         The automation user has to set the total length of route section. This will be used for internal validations and to place splice correctly. 
        """
        pass
class SystemDefinition(HarnessDefinition): 
    """ Represents a NXOpen.Routing.Electrical.SystemDefinition """
    pass
import NXOpen
class SystemDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Electrical.SystemDevice objects.  """
    @overload
    def CreateSystemDevice(self) -> SystemDevice:
        """
         Creates NXOpen.Routing.Electrical.SystemDevice. 
         Returns system_device ( SystemDevice NXOpen.Routi):  The new System Device. .
        """
        pass
    @overload
    def CreateSystemDevice(self, system_name: str) -> SystemDevice:
        """
         Creates NXOpen.Routing.Electrical.SystemDevice with given name. 
         Returns system_device ( SystemDevice NXOpen.Routi):  The new System Device. .
        """
        pass
    def GetSystemSingleDevices(self) -> List[SystemDevice]:
        """
         Get System Devices. 
         Returns systems ( SystemDevice List[NXOpen.Rou):  The array of System Devices in the given part. .
        """
        pass
class SystemDevice(HarnessDevice): 
    """
            The Electrical SystemDevice corresponds to a system instance of the 
            NXOpen.Routing.SingleDevice.
        """
    def GetSystemDefinition(self) -> SystemDefinition:
        """
         Returns the NXOpen.Routing.Electrical.SystemDefinition
                        used by this NXOpen.Routing.Electrical.SystemDevice. 
         Returns system_definition ( SystemDefinition NXOpen.Routi):  The NXOpen.Routing.Electrical.SystemDefinition used by this NXOpen.Routing.Electrical.SystemDevice. .
        """
        pass
class WireDevice(ElectricalStockDevice): 
    """
            The Electrical WireDevice corresponds to a wire instance of
            NXOpen.Routing.Electrical.ElectricalStockDevice.
        """
    pass
