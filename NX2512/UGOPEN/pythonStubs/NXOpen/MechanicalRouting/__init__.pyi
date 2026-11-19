from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
class BuilderFactory(NXOpen.Object): 
    """ Represents an NXOpen.MechanicalRouting.BuilderFactory object.  Use this object 
        to create specific routing mechanical builders.
    """
    def CreateBulkReplacementBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, segmentsOrStocks: List[NXOpen.NXObject]) -> BulkReplacementBuilder:
        """
          Creates a NXOpen.MechanicalRouting.BulkReplacementBuilder object. 
         Returns builder ( BulkReplacementBuilder NXOpen.Mech): .
        """
        pass
    def CreateCablewayAttributeBuilder(part: NXOpen.Part) -> CablewayAttributeBuilder:
        """
          Create a NXOpen.MechanicalRouting.CablewayAttributeBuilder object. 
         Returns builder ( CablewayAttributeBuilder NXOpen.Mech): .
        """
        pass
    def CreateCablewayExportBuilder(part: NXOpen.Part) -> CablewayExportBuilder:
        """
          Create a NXOpen.MechanicalRouting.CablewayExportBuilder object. 
         Returns builder ( CablewayExportBuilder NXOpen.Mech): .
        """
        pass
    def CreateCablewayMoveCableTrayBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> CablewayMoveCableTrayBuilder:
        """
          Create a NXOpen.MechanicalRouting.CablewayMoveCableTrayBuilder object. 
         Returns builder ( CablewayMoveCableTrayBuilder NXOpen.Mech): .
        """
        pass
    def CreateCablewayNearNodeBuilder(part: NXOpen.Part) -> CablewayNearNodeBuilder:
        """
          Create a NXOpen.MechanicalRouting.CablewayNearNodeBuilder object. 
         Returns builder ( CablewayNearNodeBuilder NXOpen.Mech): .
        """
        pass
    def CreateCablewayNodeIdentifierBuilder(part: NXOpen.Part) -> CablewayNodeIdentifierBuilder:
        """
          Create a NXOpen.MechanicalRouting.CablewayNodeIdentifierBuilder object. 
         Returns builder ( CablewayNodeIdentifierBuilder NXOpen.Mech): .
        """
        pass
    def CreateDeflectorBuilder(part: NXOpen.Part, deflector: Deflector) -> DeflectorBuilder:
        """
          Creates a NXOpen.MechanicalRouting.DeflectorBuilder object. 
         Returns builder ( DeflectorBuilder NXOpen.Mech): .
        """
        pass
    def CreateDuctReinforcementContainerBuilder(part: NXOpen.Part, drc: DuctReinforcementContainer) -> DuctReinforcementContainerBuilder:
        """
          Creates a NXOpen.MechanicalRouting.DuctReinforcementContainerBuilder object. 
         Returns builder ( DuctReinforcementContainerBuilder NXOpen.Mech): .
        """
        pass
    def CreateEditCutElbowBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> EditCutElbowBuilder:
        """
          Creates a NXOpen.MechanicalRouting.EditCutElbowBuilder object. 
         Returns builder ( EditCutElbowBuilder NXOpen.Mech): .
        """
        pass
    def CreateEndformBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> EndformBuilder:
        """
          Creates a NXOpen.MechanicalRouting.EndformBuilder object. 
         Returns builder ( EndformBuilder NXOpen.Mech): .
        """
        pass
    def CreateFillRuleAndSegregationBuilder(part: NXOpen.Part) -> FillRuleAndSegregationBuilder:
        """
          Creates a NXOpen.MechanicalRouting.FillRuleAndSegregationBuilder object. 
         Returns builder ( FillRuleAndSegregationBuilder NXOpen.Mech): .
        """
        pass
    def CreateFlowAnalysisBuilder(part: NXOpen.Part) -> FlowAnalysisBuilder:
        """
          Create a NXOpen.MechanicalRouting.FlowAnalysisBuilder object. 
         Returns builder ( FlowAnalysisBuilder NXOpen.Mech): .
        """
        pass
    def CreateGenerateSpoolsBuilder(part: NXOpen.Part, contextComponent: NXOpen.Assemblies.Component) -> GenerateSpoolsBuilder:
        """
          Creates a NXOpen.MechanicalRouting.GenerateSpoolsBuilder object. 
         Returns builder ( GenerateSpoolsBuilder NXOpen.Mech): .
        """
        pass
    def CreateHVACSupportBuilder(part: NXOpen.Part) -> HVACSupportBuilder:
        """
          Creates a NXOpen.MechanicalRouting.HVACSupportBuilder object. 
         Returns builder ( HVACSupportBuilder NXOpen.Mech): .
        """
        pass
    def CreateHVACSupportExtensionBuilder(part: NXOpen.Part) -> HVACSupportExtensionBuilder:
        """
          Creates a NXOpen.MechanicalRouting.HVACSupportExtensionBuilder object. 
         Returns builder ( HVACSupportExtensionBuilder NXOpen.Mech): .
        """
        pass
    def CreateJumpPathBuilder(part: NXOpen.Part) -> JumpPathBuilder:
        """
          Creates a NXOpen.MechanicalRouting.JumpPathBuilder object. 
         Returns builder ( JumpPathBuilder NXOpen.Mech): .
        """
        pass
    def CreatePipeBendAnalysisBuilder(part: NXOpen.Part) -> PipeBendAnalysisBuilder:
        """
          Create a NXOpen.MechanicalRouting.PipeBendAnalysisBuilder object. 
         Returns builder ( PipeBendAnalysisBuilder NXOpen.Mech): .
        """
        pass
    def CreatePipingComponentFileBuilder(part: NXOpen.Part) -> PipingComponentFileBuilder:
        """
          Creates a NXOpen.MechanicalRouting.PipingComponentFileBuilder object. 
         Returns builder ( PipingComponentFileBuilder NXOpen.Mech): .
        """
        pass
    def CreatePlaceElbowsBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> PlaceElbowsBuilder:
        """
          Creates a NXOpen.MechanicalRouting.PlaceElbowsBuilder object. 
         Returns builder ( PlaceElbowsBuilder NXOpen.Mech): .
        """
        pass
    def CreatePublishSpoolAssembliesBuilder(part: NXOpen.Part) -> PublishSpoolAssembliesBuilder:
        """
         Creates a NXOpen.MechanicalRouting.PublishSpoolAssembliesBuilder object. 
         Returns builder ( PublishSpoolAssembliesBuilder NXOpen.Mech): .
        """
        pass
    def CreateSlopePathBuilder(part: NXOpen.Part) -> SlopePathBuilder:
        """
          Create a NXOpen.MechanicalRouting.SlopePathBuilder object. 
         Returns builder ( SlopePathBuilder NXOpen.Mech): .
        """
        pass
    def CreateSpaceReservationReplacementBuilder(part: NXOpen.Part) -> SpaceReservationReplacementBuilder:
        """
          Creates a NXOpen.MechanicalRouting.SpaceReservationReplacementBuilder object. 
         Returns builder ( SpaceReservationReplacementBuilder NXOpen.Mech): .
        """
        pass
    def CreateSpoolBuilder(part: NXOpen.Part, spoolToEdit: Spool) -> SpoolBuilder:
        """
          Creates a NXOpen.MechanicalRouting.SpoolBuilder object. 
         Returns builder ( SpoolBuilder NXOpen.Mech): .
        """
        pass
    def CreateSpoolDelimiterBuilder(part: NXOpen.Part) -> SpoolDelimiterBuilder:
        """
         Creates a NXOpen.MechanicalRouting.SpoolDelimiterBuilder object. 
         Returns builder ( SpoolDelimiterBuilder NXOpen.Mech): .
        """
        pass
    def CreateUpdateRunBuilder(part: NXOpen.Part) -> UpdateRunBuilder:
        """
         Creates a NXOpen.MechanicalRouting.UpdateRunBuilder object. 
         Returns builder ( UpdateRunBuilder NXOpen.Mech): .
        """
        pass
import NXOpen.Routing
class BulkReplacementBuilder(NXOpen.Routing.BulkReplacementBuilder): 
    """ Builder class for Bulk Replacement which manages replacement operations on design elements """
    pass
import NXOpen
class CablewayAttributeBuilder(NXOpen.Builder): 
    """
        CablewayAttributeBuilder is to assign predefined attributevalue to selected routing objects
    """
    class AttributeCatalogType(Enum):
        """
        Members Include: 
         |EditPointAttributes| 
         |EditCurveAttributes| 
         |EditHangerAttributes| 

        """
        EditPointAttributes: int
        EditCurveAttributes: int
        EditHangerAttributes: int
        @staticmethod
        def ValueOf(value: int) -> CablewayAttributeBuilder.AttributeCatalogType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttributeCatalog(self) -> CablewayAttributeBuilder.AttributeCatalogType:
        """
        Getter for property: ( CablewayAttributeBuilder.AttributeCatalogType NXOpen.Mech) AttributeCatalog
         Returns the attribute catalog   
            
         
        """
        pass
    @AttributeCatalog.setter
    def AttributeCatalog(self, attributeCatalog: CablewayAttributeBuilder.AttributeCatalogType):
        """
        Setter for property: ( CablewayAttributeBuilder.AttributeCatalogType NXOpen.Mech) AttributeCatalog
         Returns the attribute catalog   
            
         
        """
        pass
    @property
    def SelectedObjectList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedObjectList
         Returns the route object collector   
            
         
        """
        pass
    def BuildEquivalentPointsMap(self, objects: List[NXOpen.TaggedObject]) -> None:
        """
         Build equivalent points map. The equivalent points are controlpoints or Cablewaynetworks point that are overlapped in connected parts.
                They should have the same cableway attributes. The reason is to build the map is when assign attributes to point, only assign to one of them, 
                then copy the attributes assigned to all its equivalent points. 
        """
        pass
    def CopyTemplateAttributesToEquivalentPoints(self, objects: List[NXOpen.TaggedObject]) -> None:
        """
         Copy template attributes from point to its equivalent points. The equivalent points are controlpoints or Cablewaynetworks point that are overlapped in connected parts.
                Before copying the attributes, build the equivalent points map first.
        """
        pass
import NXOpen
import NXOpen.Routing
class CablewayElectricalTopologyPathBuilder(NXOpen.Builder): 
    """ Builder for marking paths as Electrical Topology Paths. """
    @property
    def ElectricalTopologyPath(self) -> bool:
        """
        Getter for property: (bool) ElectricalTopologyPath
         Returns whether to mark or unmark the selected stock components as cableway Electrical Topology Path.  
             
         
        """
        pass
    @ElectricalTopologyPath.setter
    def ElectricalTopologyPath(self, isElectricalTopologyPath: bool):
        """
        Setter for property: (bool) ElectricalTopologyPath
         Returns whether to mark or unmark the selected stock components as cableway Electrical Topology Path.  
             
         
        """
        pass
    @property
    def StockComponents(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) StockComponents
         Returns the selected stock components.  
           These can have bare paths.
                    If any stock components have regular stock, then they will always be deleted from 
                    the stock component part before marking the stock components as cableway Electrical Topology Path.   
         
        """
        pass
import NXOpen
class CablewayExportBuilder(NXOpen.Builder): 
    """ Builder class for Cableway Export command. """
    class ExportMode(Enum):
        """
        Members Include: 
         |Native|  Export to a native XML file. 
         |Teamcenter|  Reserved for future use. 

        """
        Native: int
        Teamcenter: int
        @staticmethod
        def ValueOf(value: int) -> CablewayExportBuilder.ExportMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExportType(self) -> CablewayExportBuilder.ExportMode:
        """
        Getter for property: ( CablewayExportBuilder.ExportMode NXOpen.Mech) ExportType
         Returns the type of export, either to a Teamcenter data set or to a native file.  
             
         
        """
        pass
    @ExportType.setter
    def ExportType(self, exportMode: CablewayExportBuilder.ExportMode):
        """
        Setter for property: ( CablewayExportBuilder.ExportMode NXOpen.Mech) ExportType
         Returns the type of export, either to a Teamcenter data set or to a native file.  
             
         
        """
        pass
    def ExportToFile(self, xmlFileName: str, dataTypeToExport: RoutingManager.DataType, maxSearchLevels: int) -> None:
        """
         Exports the Cableway data to the given operating system file. 
        """
        pass
import NXOpen
import NXOpen.Routing
class CablewayInterfaceNodeBuilder(NXOpen.Builder): 
    """ Builder class for Cableway Interface Node command. """
    @property
    def NodeSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) NodeSelection
         Returns the object used for selection of  Routing::ControlPoint  or  Routing::Port 
                    (a.  
          k.a. "nodes").   
         
        """
        pass
    @property
    def RemoveInterfaceNode(self) -> bool:
        """
        Getter for property: (bool) RemoveInterfaceNode
         Returns the toggle to remove the interface node   
            
         
        """
        pass
    @RemoveInterfaceNode.setter
    def RemoveInterfaceNode(self, removeInterfaceNode: bool):
        """
        Setter for property: (bool) RemoveInterfaceNode
         Returns the toggle to remove the interface node   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Routing
class CablewayMoveCableTrayBuilder(NXOpen.Builder): 
    """ Builder class for Cableway MoveCableTray command. """
    class DetachTypes(Enum):
        """
        Members Include: 
         |AlwaysMaintainConnections| 
         |DetachSelectedObjects| 

        """
        AlwaysMaintainConnections: int
        DetachSelectedObjects: int
        @staticmethod
        def ValueOf(value: int) -> CablewayMoveCableTrayBuilder.DetachTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ComponentSelection
         Returns the objects that needs to be transformed.  
           The objects can be etp or Cableway Network components (Tray) that have properties that 
                    make them suitable to be moved by the routing application.   
         
        """
        pass
    @property
    def CreateExtensions(self) -> bool:
        """
        Getter for property: (bool) CreateExtensions
         Returns the status of create extensions flag   
            
         
        """
        pass
    @CreateExtensions.setter
    def CreateExtensions(self, needToCreateExtensionSegments: bool):
        """
        Setter for property: (bool) CreateExtensions
         Returns the status of create extensions flag   
            
         
        """
        pass
    @property
    def DetachType(self) -> CablewayMoveCableTrayBuilder.DetachTypes:
        """
        Getter for property: ( CablewayMoveCableTrayBuilder.DetachTypes NXOpen.Mech) DetachType
         Returns the detach type setting.  
           
                    Allows the user to specify acceptable detach types for objects that prevent the transformation of the 
                    selected objects.
                  
         
        """
        pass
    @DetachType.setter
    def DetachType(self, detachType: CablewayMoveCableTrayBuilder.DetachTypes):
        """
        Setter for property: ( CablewayMoveCableTrayBuilder.DetachTypes NXOpen.Mech) DetachType
         Returns the detach type setting.  
           
                    Allows the user to specify acceptable detach types for objects that prevent the transformation of the 
                    selected objects.
                  
         
        """
        pass
    @property
    def Motion(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ModlMotion) Motion
         Returns the transformation to apply to the selected routing objects.  
             
         
        """
        pass
    @property
    def PathOffset(self) -> float:
        """
        Getter for property: (float) PathOffset
         Returns the path offset required for creating extension segments   
            
         
        """
        pass
    @PathOffset.setter
    def PathOffset(self, pathOffset: float):
        """
        Setter for property: (float) PathOffset
         Returns the path offset required for creating extension segments   
            
         
        """
        pass
    @property
    def Preview(self) -> bool:
        """
        Getter for property: (bool) Preview
         Returns the preview setting   
            
         
        """
        pass
    @Preview.setter
    def Preview(self, preview: bool):
        """
        Setter for property: (bool) Preview
         Returns the preview setting   
            
         
        """
        pass
    def DragObjects(self) -> None:
        """
         Perform a drag operation.  
        """
        pass
    def PrepareMoveCableTrayData(self) -> None:
        """
         Prepare Move Cable Tray Data before moving tray 
        """
        pass
    def ResetDrag(self) -> None:
        """
         Reset a drag operation 
        """
        pass
    def StartDrag(self) -> None:
        """
         Begin a drag operation.  
        """
        pass
    def StopDrag(self) -> None:
        """
         End a drag operation 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class CablewayNearNodeBuilder(NXOpen.Builder): 
    """ Builder class for Cableway Near Node dialog. """
    @property
    def DeviceComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) DeviceComponent
         Returns the device's  Assemblies::Component .  
             
         
        """
        pass
    @DeviceComponent.setter
    def DeviceComponent(self, device: NXOpen.Assemblies.Component):
        """
        Setter for property: ( NXOpen.Assemblies.Component) DeviceComponent
         Returns the device's  Assemblies::Component .  
             
         
        """
        pass
    @property
    def DeviceSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) DeviceSelection
         Returns the object used for selection of a  Assemblies::Component  or  Routing::MultiPort  representing a device.  
             
         
        """
        pass
    @property
    def Multiport(self) -> NXOpen.Routing.MultiPort:
        """
        Getter for property: ( NXOpen.Routing.MultiPort) Multiport
         Returns the device's  Routing::MultiPort .  
             
         
        """
        pass
    @Multiport.setter
    def Multiport(self, multiPort: NXOpen.Routing.MultiPort):
        """
        Setter for property: ( NXOpen.Routing.MultiPort) Multiport
         Returns the device's  Routing::MultiPort .  
             
         
        """
        pass
    @property
    def NodeSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) NodeSelection
         Returns the object used for selection of  Routing::ControlPoint  or  Point 
                    (a.  
          k.a. "nodes").   
         
        """
        pass
    def GetDistances(self) -> List[float]:
        """
         Gets the distances between the Routing.ControlPoint or Point
                    and the device. 
         Returns distances (List[float]): .
        """
        pass
    def GetNodes(self) -> List[NXOpen.SmartObject]:
        """
         Gets the Routing.ControlPoints or Points
                    selected as near node for the device. 
         Returns nodes ( NXOpen.SmartObject Li): .
        """
        pass
    def RemoveDeviceComponent(self) -> None:
        """
         Removes the Assemblies.Component. 
        """
        pass
    def RemoveMultiport(self) -> None:
        """
         Removes the Routing.MultiPort. 
        """
        pass
    def SetDistances(self, distances: List[float]) -> None:
        """
         Gets the distances between the Routing.ControlPoints and Points
                    and the device. 
        """
        pass
    def SetNodes(self, nodes: List[NXOpen.SmartObject]) -> None:
        """
         Sets the Routing.ControlPoints or Points
                    selected as near node for the device. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class CablewayNearNodeCollection(NXOpen.TaggedObjectCollection): 
    """  Represents a collection of NXOpen.MechanicalRouting.CablewayNearNode objects. 
        Iterating this collection only returns live uncondemned objects contained in the owning part
    """
    def CreateCablewayNearNodeForDevice(self, device: NXOpen.Assemblies.Component, nodes: List[NXOpen.SmartObject], distances: List[float]) -> CablewayNearNode:
        """
         Creates a NXOpen.MechanicalRouting.CablewayNearNode object. 
         Returns cablewayNearNode ( CablewayNearNode NXOpen.Mech):  .
        """
        pass
    def CreateCablewayNearNodeForMultiPort(self, multiPort: NXOpen.Routing.MultiPort, nodes: List[NXOpen.SmartObject], distances: List[float]) -> CablewayNearNode:
        """
         Creates a NXOpen.MechanicalRouting.CablewayNearNode object. 
         Returns cablewayNearNode ( CablewayNearNode NXOpen.Mech):  .
        """
        pass
    def FindCablewayNearNodeFromDevice(self, device: NXOpen.Assemblies.Component) -> CablewayNearNode:
        """
         Find a NXOpen.MechanicalRouting.CablewayNearNode object related
                    to the given device component, if any. 
         Returns cablewayNearNode ( CablewayNearNode NXOpen.Mech):  .
        """
        pass
    def FindCablewayNearNodeFromMultiPort(self, multiPort: NXOpen.Routing.MultiPort) -> CablewayNearNode:
        """
         Find a NXOpen.MechanicalRouting.CablewayNearNode object related
                    to the given MultiPort, if any. 
         Returns cablewayNearNode ( CablewayNearNode NXOpen.Mech):  .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class CablewayNearNode(NXOpen.NXObject): 
    """ The Cableway Near Node class maintains the relationship between a device and the
        Routing.ControlPoints that are near to the device.
        Use the NXOpen.MechanicalRouting.CablewayNearNodeCollection
        to create a new Cableway Near Node object.
        You can use either a Assemblies.Component to represent the device or a
        Routing.MultiPort, but not both.
        """
    @property
    def Device(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) Device
         Returns the device's  Assemblies::Component .  
             
         
        """
        pass
    @Device.setter
    def Device(self, device: NXOpen.Assemblies.Component):
        """
        Setter for property: ( NXOpen.Assemblies.Component) Device
         Returns the device's  Assemblies::Component .  
             
         
        """
        pass
    @property
    def Multiport(self) -> NXOpen.Routing.MultiPort:
        """
        Getter for property: ( NXOpen.Routing.MultiPort) Multiport
         Returns the device's  Routing::MultiPort .  
             
         
        """
        pass
    @Multiport.setter
    def Multiport(self, multiport: NXOpen.Routing.MultiPort):
        """
        Setter for property: ( NXOpen.Routing.MultiPort) Multiport
         Returns the device's  Routing::MultiPort .  
             
         
        """
        pass
    def GetDistances(self) -> List[float]:
        """
         Gets the distances between the Routing.ControlPoint or Point
                    and the device. 
         Returns distances (List[float]): .
        """
        pass
    def GetNodes(self) -> List[NXOpen.SmartObject]:
        """
         Gets the Routing.ControlPoint or Point
                    selected as near node for the device. 
         Returns nodes ( NXOpen.SmartObject Li): .
        """
        pass
    def SetDistances(self, distances: List[float]) -> None:
        """
         Gets the distances between the Routing.ControlPoint or Point
                    and the device. 
        """
        pass
    def SetNodes(self, nodes: List[NXOpen.SmartObject]) -> None:
        """
         Sets the Routing.ControlPoint or Point
                    selected as near node for the device. 
        """
        pass
import NXOpen
import NXOpen.Routing
class CablewayNodeIdentifierBuilder(NXOpen.Builder): 
    """ Builder class for Cableway Node Identifier command. """
    @property
    def NodeSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) NodeSelection
         Returns the object used for selection of  Routing::ControlPoint  or  Point 
                    (a.  
          k.a. "nodes").   
         
        """
        pass
    def GetNodes(self) -> List[NXOpen.SmartObject]:
        """
         Gets the Routing.ControlPoints or Points 
         Returns nodes ( NXOpen.SmartObject Li): .
        """
        pass
    def SetIdentifiers(self, identifiers: List[str]) -> None:
        """
         Sets the identifiers to be placed on the nodes by the Commit method.
                
        """
        pass
    def SetNodes(self, nodes: List[NXOpen.SmartObject]) -> None:
        """
         Sets the Routing.ControlPoints or Points. 
        """
        pass
import NXOpen
import NXOpen.Routing
import NXOpen.RoutingCommon
class CablewayPatternBuilder(NXOpen.Builder): 
    """ Builder class for Cableway Interface Node command. """
    class CablewayPatternMethod(Enum):
        """
        Members Include: 
         |NotSet|  No Pattern. 
         |SpecifiedPattern|  Pattern selected from Specify Item dialog 
         |SpecifiedStock|  Stock selected from Specify Item dialog 
         |SpecifiedSpaceReservation|  Space Reservation selected from Specify Item dialog 

        """
        NotSet: int
        SpecifiedPattern: int
        SpecifiedStock: int
        SpecifiedSpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> CablewayPatternBuilder.CablewayPatternMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EditingType(Enum):
        """
        Members Include: 
         |Pattern|  Edit Pattern. 
         |SpaceReservation|  Edit Space Reservation 

        """
        Pattern: int
        SpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> CablewayPatternBuilder.EditingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CablewayPatternMethodType(self) -> CablewayPatternBuilder.CablewayPatternMethod:
        """
        Getter for property: ( CablewayPatternBuilder.CablewayPatternMethod NXOpen.Mech) CablewayPatternMethodType
         Returns the method to determine which pattern to assign.  
             
         
        """
        pass
    @CablewayPatternMethodType.setter
    def CablewayPatternMethodType(self, method: CablewayPatternBuilder.CablewayPatternMethod):
        """
        Setter for property: ( CablewayPatternBuilder.CablewayPatternMethod NXOpen.Mech) CablewayPatternMethodType
         Returns the method to determine which pattern to assign.  
             
         
        """
        pass
    @property
    def CablewayPatternPartNumber(self) -> str:
        """
        Getter for property: (str) CablewayPatternPartNumber
         Returns   
            
         
        """
        pass
    @property
    def CablewayPatternSettings(self) -> NXOpen.RoutingCommon.CablewayPatternBlockBuilder:
        """
        Getter for property: ( NXOpen.RoutingCommon.CablewayPatternBlockBuilder) CablewayPatternSettings
         Returns the cableway pattern block    
            
         
        """
        pass
    @property
    def EditType(self) -> CablewayPatternBuilder.EditingType:
        """
        Getter for property: ( CablewayPatternBuilder.EditingType NXOpen.Mech) EditType
         Returns the value of toggle for enabling space reservation editing   
            
         
        """
        pass
    @EditType.setter
    def EditType(self, editType: CablewayPatternBuilder.EditingType):
        """
        Setter for property: ( CablewayPatternBuilder.EditingType NXOpen.Mech) EditType
         Returns the value of toggle for enabling space reservation editing   
            
         
        """
        pass
    @property
    def PathSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PathSelection
         Returns the object used for selection of path segments   
            
         
        """
        pass
    def Flip(self) -> None:
        """
         The button to handle the flip state 
        """
        pass
    def GetAttributeHolder(self) -> NXOpen.Routing.AttributeHolder:
        """
         Gets the attribute holder for library defined attributes on cableway pattern to be applied 
         Returns libraryDefinedAttributeHolder ( NXOpen.Routing.AttributeHolder): .
        """
        pass
    def ResetAttributeHolder(self) -> None:
        """
         Resets the attribute holder for library defined attributes for cableway pattern attribute holder
                    This API is recommended to be used before assigning attributes onto builder so as to ensure cableway pattern apply operation to function correctly 
        """
        pass
    def SetFlip(self, flip: bool) -> None:
        """
         
        """
        pass
import NXOpen
class CollectionsManager(NXOpen.Object): 
    """ Represents an NXOpen.MechanicalRouting.CollectionsManager object,
        which manages various collections of Routing objects.
     """
    @property
    def CablewayNearNodes() -> CablewayNearNodeCollection:
        """
         The collection of Cableway Near Nodes objects. 
        """
        pass
    @property
    def Spools() -> SpoolCollection:
        """
         The collection of Spool objects. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class ConnectivityService(NXOpen.Object): 
    """ Represents a NXOpen.MechanicalRouting.ConnectivityService object.
        Use the MechanicalRouting.RoutingManager.ConnectivityService to obtain
        an instance of this class.
     """
    class ComponentType(Enum):
        """
        Members Include: 
         |Fitting| 
         |Stock| 
         |Any| 

        """
        Fitting: int
        Stock: int
        Any: int
        @staticmethod
        def ValueOf(value: int) -> ConnectivityService.ComponentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AskAppViewSizeCharx() -> List[str]:
        """
          Returns the size characteristics from current App View. 
         Returns sizeCharx (List[str]): .
        """
        pass
    def GetConnectedHeaderAndOutletComponents(stockTag: NXOpen.Routing.Stock) -> Tuple[List[NXOpen.Routing.ControlPoint], List[NXOpen.Assemblies.Component], List[NXOpen.Assemblies.Component], NXOpen.ErrorList]:
        """
          Returns the header outlet component connected to given stock 
         Returns A tuple consisting of (outletRcps, connectedHeaders, connectedOutlets, errorList). 
         - outletRcps is:  NXOpen.Routing.ControlPoint Li. Outlet control points.
         - connectedHeaders is:  NXOpen.Assemblies.Component Li. Headers connected to input Stock.
         - connectedOutlets is:  NXOpen.Assemblies.Component Li. Outlets connected to input Stock.
         - errorList is:  NXOpen.ErrorList. Any errors that occurred during the operation  .

        """
        pass
    def GetConnectedPorts(part: NXOpen.Part) -> Tuple[List[NXOpen.Routing.Port], List[NXOpen.Routing.Port]]:
        """
          Returns the pairs of connected ports in the part. 
         Returns A tuple consisting of (connectedPorts1, connectedPorts2). 
         - connectedPorts1 is:  NXOpen.Routing.Port Li.  .
         - connectedPorts2 is:  NXOpen.Routing.Port Li.  .

        """
        pass
    def GetConnectedPortsFromComponent(part: NXOpen.Assemblies.Component) -> Tuple[List[NXOpen.Routing.Port], List[NXOpen.Routing.Port]]:
        """
          Returns the pairs of ports connected to the given component. 
         Returns A tuple consisting of (connectedPorts1, connectedPorts2). 
         - connectedPorts1 is:  NXOpen.Routing.Port Li.  .
         - connectedPorts2 is:  NXOpen.Routing.Port Li.  .

        """
        pass
    def GetHeaderAndOutletComponentsFromPart(part: NXOpen.Part) -> Tuple[List[NXOpen.Routing.ControlPoint], List[NXOpen.Assemblies.Component], List[NXOpen.Assemblies.Component]]:
        """
          Returns the header outlet component present in given the part 
         Returns A tuple consisting of (outletRcps, headers, outlets). 
         - outletRcps is:  NXOpen.Routing.ControlPoint Li. Outlet control points in given work part .
         - headers is:  NXOpen.Assemblies.Component Li. Headers present in given the part .
         - outlets is:  NXOpen.Assemblies.Component Li. Outlets present in given the part .

        """
        pass
import NXOpen
class CustomManager(NXOpen.Object): 
    """ The Mechancanical Routing Custom Manager allows you to customize the Routed System Designer (RSD)
        Mechanical application by adding plugins. """
    def RemoveAllPlugins(self) -> None:
        """
         Removes all the registered plugins. 
        """
        pass
    def RemoveRunFulfillmentEvaluationPlugin(self) -> None:
        """
         Removes any registered plugin to evaluate the logical run object. 
        """
        pass
    def RemoveRunMappingStatusMessageEvaluationPlugin(self) -> None:
        """
         Removes any registered plugin that is called when a mapping status needs to be returned
                    for an individual mapping status message when evaluating logical runs objects. 
        """
        pass
    def RemoveRunMappingStatusMessageStringPlugin(self) -> None:
        """
         Removes any registered plugin that is called when a user facing string needs to be returned
                    for an individual mapping status message when evaluating logical runs objects. 
        """
        pass
    RunFulfillmentEvaluationPlugin = Callable[[NXOpen.Schematic.Model.BaseObject, RunMappingStatusMessageList], None]
    RunMappingStatusMessageEvaluationPlugin = Callable[[RunsAssignmentManager.MappingStatusMessage], None]
    RunMappingStatusMessageStringPlugin = Callable[[RunsAssignmentManager.MappingStatusMessage], None]
    def SetRunFulfillmentEvaluationPlugin(self, runFulfillmentEvaluationPlugin: CustomManager.RunFulfillmentEvaluationPlugin) -> None:
        """
         Sets the plugin called when a logical run object is evaluated. Will
                    throw an error if already registered. 
        """
        pass
    def SetRunMappingStatusMessageEvaluationPlugin(self, messageEvaluationPlugin: CustomManager.RunMappingStatusMessageEvaluationPlugin) -> None:
        """
         Sets the plugin called when a mapping status needs to be returned for an individual
                    mapping status message when evaluating logical runs objects. Will throw an error if
                    already registered. 
        """
        pass
    def SetRunMappingStatusMessageStringPlugin(self, messageStringPlugin: CustomManager.RunMappingStatusMessageStringPlugin) -> None:
        """
         Sets the plugin called when a user facing string needs to be returned for an individual
                    mapping status message when evaluating logical runs objects. Will throw an error if
                    already registered. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Tooling
class DeflectorBuilder(NXOpen.Builder): 
    """ Builder for creatingediting deflectors.
    """
    @property
    def OutletCollector(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) OutletCollector
         Returns the outlet components on which to create deflector   
            
         
        """
        pass
    @property
    def ReuseItemSelection(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseItemSelection
         Returns the reuse item builder which is used to specify PTS template    
            
         
        """
        pass
    @property
    def ReverseFlowDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseFlowDirection
         Returns the flag to specify whether the deflectors are created on the reverse side along flow direction   
            
         
        """
        pass
    @ReverseFlowDirection.setter
    def ReverseFlowDirection(self, reverseFlowDirection: bool):
        """
        Setter for property: (bool) ReverseFlowDirection
         Returns the flag to specify whether the deflectors are created on the reverse side along flow direction   
            
         
        """
        pass
    def LoadPart(self, fileSpec: str) -> NXOpen.BasePart:
        """
         The part tag loaded from the specified path 
         Returns partTag ( NXOpen.BasePart): .
        """
        pass
    def UpdateEditPartSize(self, fileSpec: str, usePersistentObjectDimensions: bool) -> None:
        """
         Update edit part size 
        """
        pass
import NXOpen
class Deflector(NXOpen.NXObject): 
    """ The Deflector class maintains a set of deflectors.
        Use the NXOpen.MechanicalRouting.DeflectorBuilder
        to create a new deflector object.
    """
    pass
import NXOpen
import NXOpen.Tooling
class DuctReinforcementContainerBuilder(NXOpen.Builder): 
    """ Builder for creatingediting Duct Reinforcement Containers.
    """
    @property
    def FacesToReinforce(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FacesToReinforce
         Returns the inner rectangular duct faces to reinforce   
            
         
        """
        pass
    @property
    def HeightCount(self) -> int:
        """
        Getter for property: (int) HeightCount
         Returns the number of reinforcements placed on the height faces   
            
         
        """
        pass
    @HeightCount.setter
    def HeightCount(self, heightCount: int):
        """
        Setter for property: (int) HeightCount
         Returns the number of reinforcements placed on the height faces   
            
         
        """
        pass
    @property
    def HeightEndGap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeightEndGap
         Returns the distance between the outer reinforcements and the sides of the duct for the height faces   
            
         
        """
        pass
    @property
    def SelectReuseItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectReuseItem
         Returns the reuse library selection builder, which is used to select the reinforcement part file   
            
         
        """
        pass
    @property
    def WidthCount(self) -> int:
        """
        Getter for property: (int) WidthCount
         Returns the number of reinforcements placed on the width faces   
            
         
        """
        pass
    @WidthCount.setter
    def WidthCount(self, widthCount: int):
        """
        Setter for property: (int) WidthCount
         Returns the number of reinforcements placed on the width faces   
            
         
        """
        pass
    @property
    def WidthEndGap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WidthEndGap
         Returns the distance between the outer reinforcements and the sides of the duct for the width faces   
            
         
        """
        pass
import NXOpen
class DuctReinforcementContainer(NXOpen.NXObject): 
    """ The Duct Reinforcement Container class maintains a set of reinforcment occurrences on ducts.
        Use the NXOpen.MechanicalRouting.DuctReinforcementContainerBuilder
        to create a new Duct Reinforcement Container object.
    """
    def OffsetAndSnip(self, reinforcementFaceOccs: List[NXOpen.NXObject], lengthOffset: float, snipAngle: float, snipOffset: float) -> None:
        """
         Do an offset and snip. Pass in the end faces of the reinforcement part occurrence 
        """
        pass
import NXOpen
import NXOpen.Routing
class EditCutElbowBuilder(NXOpen.Builder): 
    """ Builder for lockingunlocking cut elbows.
    """
    class Type(Enum):
        """
        Members Include: 
         |Lock|  Lock cut elbow 
         |Unlock|  unlock cut elbow 

        """
        Lock: int
        Unlock: int
        @staticmethod
        def ValueOf(value: int) -> EditCutElbowBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LockCutAngle(self) -> bool:
        """
        Getter for property: (bool) LockCutAngle
         Returns the lock setting for the cut elbow   
            
         
        """
        pass
    @LockCutAngle.setter
    def LockCutAngle(self, lockCutElbow: bool):
        """
        Setter for property: (bool) LockCutAngle
         Returns the lock setting for the cut elbow   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the routing object collector that collects elbow components for modifications.  
            
         
        """
        pass
import NXOpen
import NXOpen.Routing
class EndformBuilder(NXOpen.Builder): 
    """ Builder for creatingediting endforms.
    """
    @property
    def RouteControlPointList(self) -> NXOpen.Routing.RouteObjectCollectorList:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollectorList) RouteControlPointList
         Returns the RouteControlPoint list   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the routing object collector that collects stocks to apply endform.  
             
         
        """
        pass
    def CreateRouteControlPointListItem(self) -> NXOpen.Routing.RouteObjectCollector:
        """
         Create a RouteControlPoint list item. 
         Returns listitem ( NXOpen.Routing.RouteObjectCollector): .
        """
        pass
    def EditEndform(self) -> None:
        """
         Edit EndForm 
        """
        pass
    def PlaceEndform(self) -> None:
        """
         Place EndForm 
        """
        pass
    def RemoveEndform(self) -> None:
        """
         Remove EndForm 
        """
        pass
    def SetClassificationIdentifier(self, classificationId: str) -> None:
        """
         Sets the classificaiton identifier of the endform part 
        """
        pass
    def SetFileName(self, filename: str) -> None:
        """
         Sets the file name of the endform part 
        """
        pass
    def SetPartNumberIdentifier(self, partNumber: str) -> None:
        """
         Sets the part number identifier of the endform part 
        """
        pass
import NXOpen
import NXOpen.Routing
class FillRuleAndSegregationBuilder(NXOpen.Builder): 
    """Builder class for Fill Rule and Segregation command."""
    @property
    def CablewayObjects(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) CablewayObjects
         Returns the cableway objects   
            
         
        """
        pass
    def ApplyLowerFillPercentage(self, cablewayObject: NXOpen.TaggedObject, tierNumber: int, lowerFillPercentage: float) -> None:
        """
         Assigns lower fill percentages for electrical topology path or its owning component.
        """
        pass
    def ApplyOverriddenFillRule(self, cablewayObject: NXOpen.TaggedObject, tierNumber: int, overriddenFillRuleValue: str) -> None:
        """
        Assigns overridden fill rule value to cableway object. 
                Cableway object can be electrical topology path, its owning component or a component with cableway network curves.
                If user does not want to override the fill rule, it is expected that user provides "None".
        """
        pass
    def ApplyOverriddenSegregationCodes(self, cablewayObject: NXOpen.TaggedObject, tierNumber: int, overriddenSegregationCode: str) -> None:
        """
        Assigns overridden segregation codes value to cableway object. 
                Cableway object can be electrical topology path, its owning component or a component with cableway network curves.
                If user does not want to override the segregation code, it is expected that user provides "None".
        """
        pass
    def ApplyUpperFillPercentage(self, cablewayObject: NXOpen.TaggedObject, tierNumber: int, upperFillPercentage: float) -> None:
        """
         Assigns upper fill percentages for electrical topology path or its owning components.
        """
        pass
import NXOpen
import NXOpen.Routing
class FlowAnalysisBuilder(NXOpen.Builder): 
    """ Builder class for Flow Analysis command. """
    @property
    def ReturnAbsoluteHumidity(self) -> float:
        """
        Getter for property: (float) ReturnAbsoluteHumidity
         Returns the double return absolute humidity   
            
         
        """
        pass
    @ReturnAbsoluteHumidity.setter
    def ReturnAbsoluteHumidity(self, returnAbsoluteHumidity: float):
        """
        Setter for property: (float) ReturnAbsoluteHumidity
         Returns the double return absolute humidity   
            
         
        """
        pass
    @property
    def ReturnAtmosphericPressure(self) -> float:
        """
        Getter for property: (float) ReturnAtmosphericPressure
         Returns the double return atmospe   
            
         
        """
        pass
    @ReturnAtmosphericPressure.setter
    def ReturnAtmosphericPressure(self, returnAtmosphericPressure: float):
        """
        Setter for property: (float) ReturnAtmosphericPressure
         Returns the double return atmospe   
            
         
        """
        pass
    @property
    def ReturnDensity(self) -> float:
        """
        Getter for property: (float) ReturnDensity
         Returns the double return density   
            
         
        """
        pass
    @ReturnDensity.setter
    def ReturnDensity(self, returnDensity: float):
        """
        Setter for property: (float) ReturnDensity
         Returns the double return density   
            
         
        """
        pass
    @property
    def ReturnRelativeHumidity(self) -> float:
        """
        Getter for property: (float) ReturnRelativeHumidity
         Returns the double return relative humidity   
            
         
        """
        pass
    @ReturnRelativeHumidity.setter
    def ReturnRelativeHumidity(self, returnRelativeHumidity: float):
        """
        Setter for property: (float) ReturnRelativeHumidity
         Returns the double return relative humidity   
            
         
        """
        pass
    @property
    def ReturnTemperature(self) -> float:
        """
        Getter for property: (float) ReturnTemperature
         Returns the double return temperature   
            
         
        """
        pass
    @ReturnTemperature.setter
    def ReturnTemperature(self, returnTemperature: float):
        """
        Setter for property: (float) ReturnTemperature
         Returns the double return temperature   
            
         
        """
        pass
    @property
    def ReturnViscosity(self) -> float:
        """
        Getter for property: (float) ReturnViscosity
         Returns the double return viscosity   
            
         
        """
        pass
    @ReturnViscosity.setter
    def ReturnViscosity(self, returnViscosity: float):
        """
        Setter for property: (float) ReturnViscosity
         Returns the double return viscosity   
            
         
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
    def SupplyAbsoluteHumidity(self) -> float:
        """
        Getter for property: (float) SupplyAbsoluteHumidity
         Returns the double supply absolute humidity   
            
         
        """
        pass
    @SupplyAbsoluteHumidity.setter
    def SupplyAbsoluteHumidity(self, supplyAbsoluteHumidity: float):
        """
        Setter for property: (float) SupplyAbsoluteHumidity
         Returns the double supply absolute humidity   
            
         
        """
        pass
    @property
    def SupplyAtmosphericPressure(self) -> float:
        """
        Getter for property: (float) SupplyAtmosphericPressure
         Returns the double supply atmospheric pressure   
            
         
        """
        pass
    @SupplyAtmosphericPressure.setter
    def SupplyAtmosphericPressure(self, supplyAtmosphericPressure: float):
        """
        Setter for property: (float) SupplyAtmosphericPressure
         Returns the double supply atmospheric pressure   
            
         
        """
        pass
    @property
    def SupplyDensity(self) -> float:
        """
        Getter for property: (float) SupplyDensity
         Returns the double supply density   
            
         
        """
        pass
    @SupplyDensity.setter
    def SupplyDensity(self, supplyDensity: float):
        """
        Setter for property: (float) SupplyDensity
         Returns the double supply density   
            
         
        """
        pass
    @property
    def SupplyRelativeHumidity(self) -> float:
        """
        Getter for property: (float) SupplyRelativeHumidity
         Returns the double supply relative humidity   
            
         
        """
        pass
    @SupplyRelativeHumidity.setter
    def SupplyRelativeHumidity(self, supplyRelativeHumidity: float):
        """
        Setter for property: (float) SupplyRelativeHumidity
         Returns the double supply relative humidity   
            
         
        """
        pass
    @property
    def SupplyTemperature(self) -> float:
        """
        Getter for property: (float) SupplyTemperature
         Returns the double supply temperature   
            
         
        """
        pass
    @SupplyTemperature.setter
    def SupplyTemperature(self, supplyTemperature: float):
        """
        Setter for property: (float) SupplyTemperature
         Returns the double supply temperature   
            
         
        """
        pass
    @property
    def SupplyViscosity(self) -> float:
        """
        Getter for property: (float) SupplyViscosity
         Returns the double supply viscosity   
            
         
        """
        pass
    @SupplyViscosity.setter
    def SupplyViscosity(self, supplyViscosity: float):
        """
        Setter for property: (float) SupplyViscosity
         Returns the double supply viscosity   
            
         
        """
        pass
    def CalculateFlowrate(self) -> None:
        """
         Calculate the flowrate 
        """
        pass
    def GetInletFlowrate(self) -> float:
        """
         Returns the flowrate from the INLET port in the FAN 
         Returns flowrateValue (float): .
        """
        pass
    def GetNumberOfElementsInHvacSystem(self) -> int:
        """
         Returns the number of elements in the HVAC system 
         Returns numberOfElements (int): .
        """
        pass
    def GetOutletFlowrate(self) -> float:
        """
         Returns the flowrate from the OUTLET port in the FAN 
         Returns flowrateValue (float): .
        """
        pass
    def IsValidHvacSystem(self, selectedObj: NXOpen.NXObject) -> int:
        """
         Returns true if the HVAC system has is defined correctly 
         Returns errorHvacSystem (int): .
        """
        pass
    def SetFlowrate(self, selectedObj: NXOpen.NXObject, flowrateValue: float) -> None:
        """
         Set the flowrate to the node 
        """
        pass
import NXOpen
import NXOpen.Routing
class GenerateSpoolsBuilder(NXOpen.Builder): 
    """ Builder for generating spools from delimited Routing assemblies.
    """
    class SpoolSorting(Enum):
        """
        Members Include: 
         |ByInputComponentOrder|  Generated spools are sorted by the order of their components in the input components. 
         |ByInputComponentOrderAndConnectivity|  Generated spools are sorted by the order of their components in the input components and the connectivity between spool components. 

        """
        ByInputComponentOrder: int
        ByInputComponentOrderAndConnectivity: int
        @staticmethod
        def ValueOf(value: int) -> GenerateSpoolsBuilder.SpoolSorting:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def GeneratedSpoolSorting(self) -> GenerateSpoolsBuilder.SpoolSorting:
        """
        Getter for property: ( GenerateSpoolsBuilder.SpoolSorting NXOpen.Mech) GeneratedSpoolSorting
         Returns the sorting method to use for generated spools   
            
         
        """
        pass
    @GeneratedSpoolSorting.setter
    def GeneratedSpoolSorting(self, sorting: GenerateSpoolsBuilder.SpoolSorting):
        """
        Setter for property: ( GenerateSpoolsBuilder.SpoolSorting NXOpen.Mech) GeneratedSpoolSorting
         Returns the sorting method to use for generated spools   
            
         
        """
        pass
    @property
    def IncludeEquipmentComponents(self) -> bool:
        """
        Getter for property: (bool) IncludeEquipmentComponents
         Returns a boolean value that indicates whether components that are placed as equipment should be included in generated spools.  
             
         
        """
        pass
    @IncludeEquipmentComponents.setter
    def IncludeEquipmentComponents(self, includeEquipmentComponents: bool):
        """
        Setter for property: (bool) IncludeEquipmentComponents
         Returns a boolean value that indicates whether components that are placed as equipment should be included in generated spools.  
             
         
        """
        pass
    @property
    def Members(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) Members
         Returns the  NXOpen::Routing::RouteObjectCollector  used to collect the components for spool generation   
            
         
        """
        pass
    def AddComponentsForRun(self, run: NXOpen.NXObject) -> None:
        """
         Adds the components assigned to the run to the components used for spool generation 
        """
        pass
    def AddComponentsForRunBranch(self, runBranch: NXOpen.NXObject) -> None:
        """
         Adds the components assigned to the run branch to the components used for spool generation 
        """
        pass
    def AddComponentsForSimplifiedViewRun(self, run: NXOpen.NXObject) -> None:
        """
         Adds the members of a run shown in the Simplified View of the Run Navigator to the components used for spool generation.  
        """
        pass
import NXOpen
import NXOpen.Placement
import NXOpen.Routing
class HVACSupportBuilder(NXOpen.Builder): 
    """ Represents a HVAC Support builder. You can use it to place HVAC support parts. """
    class DrivenDimensionOption(Enum):
        """
        Members Include: 
         |Start|  driven dimension measured from duct start side 
         |End|  driven dimension measured from duct end side 

        """
        Start: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> HVACSupportBuilder.DrivenDimensionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetLibraryDefinedAttributeHolder(self) -> NXOpen.Routing.AttributeHolder:
        """
         Gets the attribute holder for library defined attributes on placed part instance 
         Returns libraryDefinedAttributeHolder ( NXOpen.Routing.AttributeHolder): .
        """
        pass
    def InitializePlacementEngineBuilder(self) -> NXOpen.Placement.PlacementEngineBuilder:
        """
         Initializes the placement engine builder with inputs already present in the HVAC support builder and computes solutions.  
         Returns placementEngineBuilder ( NXOpen.Placement.PlacementEngineBuilder): .
        """
        pass
    def ResetAttributesOnLibraryDefinedAttributeHolder(self) -> None:
        """
         Resets the attribute holder for library defined attributes for part to be placed
                This API is recommended to be used before assigning attributes onto builder so as to ensure part placement to function correctly 
        """
        pass
    def SetDrivenDimensionOption(self, option: HVACSupportBuilder.DrivenDimensionOption) -> None:
        """
         Sets the option of driven dimension for HVAC support placement.  
        """
        pass
    def SetDrivenDimensionValue(self, dimValue: float) -> None:
        """
         Sets the value of driven dimension for HVAC support placement.  
        """
        pass
    def SetFileNameOfPartToPlace(self, filename: str) -> None:
        """
         Sets the full file path of the HVAC support part to place. 
        """
        pass
    def SetPickPoint(self, pickPoint: NXOpen.Point3d) -> None:
        """
         Sets the pick point for HVAC support placement. After calling MechanicalRouting.HVACSupportBuilder.SetReferenceObjectForPlacement, you can call this method to change location for HVAC support part placement. 
        """
        pass
    def SetReferenceObjectForPlacement(self, referenceObject: NXOpen.TaggedObject, pickPoint: NXOpen.Point3d) -> None:
        """
         Sets the reference object and reference location for HVAC support placement. The reference object can be a routing line or a duct body. 
        """
        pass
import NXOpen
class HVACSupportExtensionBuilder(NXOpen.Builder): 
    """ Represents a HVAC Support extension builder. You can use it to extend multiple HVAC support to specified target objects. """
    @property
    def ReferenceFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) ReferenceFace
         Returns the reference face to extend the supports to.  
           You can use either reference face or reference plane as extension target object.  If reference face is set, the  ReferencePlane and  SetReferencePlane  is ignored.   
         
        """
        pass
    @property
    def ReferencePlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) ReferencePlane
         Returns the reference plane to extend the supports to.  
           You can use either reference face or reference plane as extension target object. If  ReferenceFace and  SetReferenceFace  is set, this reference plane is ignored.   
         
        """
        pass
    @ReferencePlane.setter
    def ReferencePlane(self, referencePlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) ReferencePlane
         Returns the reference plane to extend the supports to.  
           You can use either reference face or reference plane as extension target object. If  ReferenceFace and  SetReferenceFace  is set, this reference plane is ignored.   
         
        """
        pass
    @property
    def SupportCollector(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) SupportCollector
         Returns the support collector to be extended.  
             
         
        """
        pass
import NXOpen
import NXOpen.Routing
class JumpPathBuilder(NXOpen.Builder): 
    """ Builder for marking paths as cableway jumps. """
    @property
    def JumpPath(self) -> bool:
        """
        Getter for property: (bool) JumpPath
         Returns whether to mark or unmark the selected stock components as cableway jump.  
             
         
        """
        pass
    @JumpPath.setter
    def JumpPath(self, isJumpPath: bool):
        """
        Setter for property: (bool) JumpPath
         Returns whether to mark or unmark the selected stock components as cableway jump.  
             
         
        """
        pass
    @property
    def SelectedRoutingObjects(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SelectedRoutingObjects
         Returns the selected routing objects.  
           These can be any path, stock or space reservations.
                    Reference stock are not eligible to be jumps, they will be skipped.
                    If any stock components have regular stock, then they will always be deleted from 
                    the stock component part before marking the stock components as cableway jump.   
         
        """
        pass
    @property
    def SpaceReservationSettings(self) -> NXOpen.Routing.StockBlockBuilder:
        """
        Getter for property: ( NXOpen.Routing.StockBlockBuilder) SpaceReservationSettings
         Returns the builder for assigning space reservation to the path.  
             
         
        """
        pass
    @property
    def StockComponents(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) StockComponents
         Returns the selected stock components.  
           These can have bare paths or space reservations.
                    Reference stock are not eligible to be jumps, they will be skipped.
                    If any stock components have regular stock, then they will always be deleted from 
                    the stock component part before marking the stock components as cableway jump.   
         
        """
        pass
import NXOpen
import NXOpen.Routing
class PipeBendAnalysisBuilder(NXOpen.Builder): 
    """ Builder class for Bending Analysis command. """
    @property
    def SegmentCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SegmentCollector
         Returns the routing selector   
            
         
        """
        pass
    def FillBendMachine(self, elbowSelected: NXOpen.NXObject, index: int) -> None:
        """
         Fill the bend machine for the index in the table 
        """
        pass
    def SetClassificationId(self, classificationId: str) -> None:
        """
         Sets the identifier of the classification object associated with the stock part to create 
        """
        pass
    def SetNewSelection(self, newSelection: NXOpen.NXObject) -> None:
        """
         Set the selection from scene to fill the data in the report 
        """
        pass
    def SetPartNumberIdentifier(self, partNumberId: str) -> None:
        """
         Sets the identifier of the attributeHolder object associated with the stock part to create 
        """
        pass
    def SetRtsSelected(self, rtsSelected: NXOpen.NXObject) -> None:
        """
         Set the Rts selected to analize 
        """
        pass
    def SetStockData(self, selectedStock: NXOpen.NXObject) -> None:
        """
         Set the stock data from scene to make the analysis 
        """
        pass
    def SetStockDataFromLibrary(self, selectedStockHolder: NXOpen.NXObject) -> None:
        """
         Set the stock data from the library to make the analysis 
        """
        pass
import NXOpen
import NXOpen.Routing
class PipeClampBuilder(NXOpen.Builder): 
    """This creates a Pipe Clamp Builder that adds clamps to fasten the pipes with support"""
    @property
    def PipeSupportPlacementData(self) -> PipeSupportPlacementBuilder:
        """
        Getter for property: ( PipeSupportPlacementBuilder NXOpen.Mech) PipeSupportPlacementData
         Returns the Pipe Support Placement Data   
            
         
        """
        pass
    @property
    def ReferenceComponent(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ReferenceComponent
         Returns the select pipes   
            
         
        """
        pass
import NXOpen
class PipeClamp(NXOpen.NXObject): 
    """ The Pipe Clamp class represents a u-bolt, clamp and strap.
        Use the NXOpen.MechanicalRouting.PipeClampBuilder
        to create a new Pipe Clamp object.
    """
    pass
import NXOpen
import NXOpen.Features.ShipDesign
import NXOpen.Routing
class PipeSupportBuilder(NXOpen.Builder): 
    """This creates a Pipe Support Builder that adds support to the selected pipes"""
    class SupportBocks(Enum):
        """
        Members Include: 
         |UserDefined| 

        """
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> PipeSupportBuilder.SupportBocks:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def PipeSupportPlacementData(self) -> PipeSupportPlacementBuilder:
        """
        Getter for property: ( PipeSupportPlacementBuilder NXOpen.Mech) PipeSupportPlacementData
         Returns the PipeSupportPlacement Data   
            
         
        """
        pass
    @property
    def ReuseLibPath(self) -> str:
        """
        Getter for property: (str) ReuseLibPath
         Returns the reuse lib path   
            
         
        """
        pass
    @ReuseLibPath.setter
    def ReuseLibPath(self, reuseLibPath: str):
        """
        Setter for property: (str) ReuseLibPath
         Returns the reuse lib path   
            
         
        """
        pass
    @property
    def SelectedPipes(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SelectedPipes
         Returns the select pipes   
            
         
        """
        pass
    @property
    def SpreadsheetStockData(self) -> NXOpen.Features.ShipDesign.SteelFeatureSpreadsheetBuilder:
        """
        Getter for property: ( NXOpen.Features.ShipDesign.SteelFeatureSpreadsheetBuilder) SpreadsheetStockData
         Returns the spreadsheet Stock Data   
            
         
        """
        pass
    @property
    def SupportBlockName(self) -> str:
        """
        Getter for property: (str) SupportBlockName
         Returns the support name   
            
         
        """
        pass
    @SupportBlockName.setter
    def SupportBlockName(self, supportBlockName: str):
        """
        Setter for property: (str) SupportBlockName
         Returns the support name   
            
         
        """
        pass
    @property
    def SupportBlockOptions(self) -> PipeSupportBuilder.SupportBocks:
        """
        Getter for property: ( PipeSupportBuilder.SupportBocks NXOpen.Mech) SupportBlockOptions
         Returns the support block options   
            
         
        """
        pass
    @SupportBlockOptions.setter
    def SupportBlockOptions(self, supportBlockOptions: PipeSupportBuilder.SupportBocks):
        """
        Setter for property: ( PipeSupportBuilder.SupportBocks NXOpen.Mech) SupportBlockOptions
         Returns the support block options   
            
         
        """
        pass
    def CloneAndLoadTemplatePart(self) -> NXOpen.Part:
        """
         Clone and load template part 
         Returns part ( NXOpen.Part): .
        """
        pass
    def GetModelFileName(self) -> Tuple[str, str]:
        """
         Model file name from spreadsheet 
         Returns A tuple consisting of (currentReuseItemPath, partDisplayName). 
         - currentReuseItemPath is: str.
         - partDisplayName is: str.

        """
        pass
    def GetPipeSupportPlacementEvent(self) -> int:
        """
         Get the event from pipe support placement builder 
         Returns placementEvent (int): .
        """
        pass
    def SetIsApplyOverhangRule(self, isApplyOverhangRule: bool) -> None:
        """
         Update IsApplyOverHangRule for pipe support 
        """
        pass
    def UnloadPipeSupportOnTypeChange(self) -> bool:
        """
         Unload pipe support on type change 
         Returns isPipeSupportTypeChanged (bool): .
        """
        pass
    def UpdateMemberSize(self) -> None:
        """
         Update member size 
        """
        pass
    def UpdateOverhangOfPipeSupport(self) -> None:
        """
         Update overhang for pipe support 
        """
        pass
    def UpdateSpreadSheetBuilderFromPipeSupportMember(self) -> None:
        """
         Update spreadsheet data from existing member in pipe support assembly 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Routing
class PipeSupportPlacementBuilder(NXOpen.Builder): 
    """This creates a Pipe Support Placement Builder that defines placement and orientation"""
    class AlignOptionTypes(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 
         |Port| 
         |Starboard| 
         |Forward| 
         |Aft| 

        """
        Up: int
        Down: int
        Port: int
        Starboard: int
        Forward: int
        Aft: int
        @staticmethod
        def ValueOf(value: int) -> PipeSupportPlacementBuilder.AlignOptionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignOptions(self) -> PipeSupportPlacementBuilder.AlignOptionTypes:
        """
        Getter for property: ( PipeSupportPlacementBuilder.AlignOptionTypes NXOpen.Mech) AlignOptions
         Returns the align options   
            
         
        """
        pass
    @AlignOptions.setter
    def AlignOptions(self, alignOptions: PipeSupportPlacementBuilder.AlignOptionTypes):
        """
        Setter for property: ( PipeSupportPlacementBuilder.AlignOptionTypes NXOpen.Mech) AlignOptions
         Returns the align options   
            
         
        """
        pass
    @property
    def EventType(self) -> int:
        """
        Getter for property: (int) EventType
         Returns the placement event types   
            
         
        """
        pass
    @EventType.setter
    def EventType(self, eventType: int):
        """
        Setter for property: (int) EventType
         Returns the placement event types   
            
         
        """
        pass
    @property
    def FlowDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) FlowDirection
         Returns the flag to place the support in the direction opposite to that of the pipe flow   
            
         
        """
        pass
    @property
    def IsSupportFlipped(self) -> bool:
        """
        Getter for property: (bool) IsSupportFlipped
         Returns the flag to specify whether the pipesupportplacement are created on the reverse side along flow direction   
            
         
        """
        pass
    @IsSupportFlipped.setter
    def IsSupportFlipped(self, isSupportFlipped: bool):
        """
        Setter for property: (bool) IsSupportFlipped
         Returns the flag to specify whether the pipesupportplacement are created on the reverse side along flow direction   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def ReverseFlowDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseFlowDirection
         Returns the flag to specify whether the pipesupportplacement are created on the reverse side along flow direction   
            
         
        """
        pass
    @ReverseFlowDirection.setter
    def ReverseFlowDirection(self, reverseFlowDirection: bool):
        """
        Setter for property: (bool) ReverseFlowDirection
         Returns the flag to specify whether the pipesupportplacement are created on the reverse side along flow direction   
            
         
        """
        pass
    @property
    def RouteSegment(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteSegment
         Returns the select pipes   
            
         
        """
        pass
    @property
    def SubdivideAtPoint(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) SubdivideAtPoint
         Returns the subdivide point   
            
         
        """
        pass
import NXOpen
class PipeSupportPlacement(NXOpen.NXObject): 
    """ The Pipe Support Placement class maintains a set of support profiles and pipe support placements.
        Use the NXOpen.MechanicalRouting.PipeSupportPlacementBuilder
        to create a new Pipe Support Placement object.
    """
    pass
import NXOpen
class PipeSupport(NXOpen.NXObject): 
    """ The PipeSupport class maintains a set of support profiles and fasteneres.
        Use the NXOpen.MechanicalRouting.PipeSupportBuilder
        to create a new Pipe Support object.
    """
    pass
import NXOpen
import NXOpen.Routing
class PipingComponentFileBuilder(NXOpen.Builder): 
    """ the Builder for PipingComponentFile data"""
    @property
    def ComponentsCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ComponentsCollector
         Returns the selected components    
            
         
        """
        pass
    @property
    def PcfFileName(self) -> str:
        """
        Getter for property: (str) PcfFileName
         Returns the pcf file name.  
             
         
        """
        pass
    @PcfFileName.setter
    def PcfFileName(self, fileName: str):
        """
        Setter for property: (str) PcfFileName
         Returns the pcf file name.  
             
         
        """
        pass
import NXOpen
import NXOpen.Routing
class PlaceCableTraysBuilder(NXOpen.Builder): 
    """ Builder class for Place Cable Trays command.
        Places cable tray parts onto a Electrical Topology Path (ETP).
    """
    class PartIDType(Enum):
        """
        Members Include: 
         |Unknown|  Unknown type of part identifier.          
         |FilePath|  The full path to a part file on disk.     
         |PartNumber|  The PART_NUMBER from the reuse library.   
         |ClassificationObject|  The node identifier from classifications. 

        """
        Unknown: int
        FilePath: int
        PartNumber: int
        ClassificationObject: int
        @staticmethod
        def ValueOf(value: int) -> PlaceCableTraysBuilder.PartIDType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FirstAirGap(self) -> float:
        """
        Getter for property: (float) FirstAirGap
         Returns the air gap used from the start of the Mechanical Topology Path (ETP) to the first cable tray.  
             
         
        """
        pass
    @FirstAirGap.setter
    def FirstAirGap(self, airGap: float):
        """
        Setter for property: (float) FirstAirGap
         Returns the air gap used from the start of the Mechanical Topology Path (ETP) to the first cable tray.  
             
         
        """
        pass
    @property
    def HorizontalElbowPartIdentifier(self) -> str:
        """
        Getter for property: (str) HorizontalElbowPartIdentifier
         Returns the horizontal elbow's part identifier.  
             
         
        """
        pass
    @HorizontalElbowPartIdentifier.setter
    def HorizontalElbowPartIdentifier(self, elbowPartIdentifier: str):
        """
        Setter for property: (str) HorizontalElbowPartIdentifier
         Returns the horizontal elbow's part identifier.  
             
         
        """
        pass
    @property
    def HorizontalElbowPartIdentifierType(self) -> PlaceCableTraysBuilder.PartIDType:
        """
        Getter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) HorizontalElbowPartIdentifierType
         Returns the type of identifier used to find the horizontal elbow part.  
             
         
        """
        pass
    @HorizontalElbowPartIdentifierType.setter
    def HorizontalElbowPartIdentifierType(self, elbowPartIDType: PlaceCableTraysBuilder.PartIDType):
        """
        Setter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) HorizontalElbowPartIdentifierType
         Returns the type of identifier used to find the horizontal elbow part.  
             
         
        """
        pass
    @property
    def InsideVerticalElbowPartIdentifier(self) -> str:
        """
        Getter for property: (str) InsideVerticalElbowPartIdentifier
         Returns the inside vertical elbow's part identifier.  
             
         
        """
        pass
    @InsideVerticalElbowPartIdentifier.setter
    def InsideVerticalElbowPartIdentifier(self, elbowPartIdentifier: str):
        """
        Setter for property: (str) InsideVerticalElbowPartIdentifier
         Returns the inside vertical elbow's part identifier.  
             
         
        """
        pass
    @property
    def InsideVerticalElbowPartIdentifierType(self) -> PlaceCableTraysBuilder.PartIDType:
        """
        Getter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) InsideVerticalElbowPartIdentifierType
         Returns the type of identifier used to find the inside vertical elbow part.  
             
         
        """
        pass
    @InsideVerticalElbowPartIdentifierType.setter
    def InsideVerticalElbowPartIdentifierType(self, elbowPartIDType: PlaceCableTraysBuilder.PartIDType):
        """
        Setter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) InsideVerticalElbowPartIdentifierType
         Returns the type of identifier used to find the inside vertical elbow part.  
             
         
        """
        pass
    @property
    def MiddleAirGap(self) -> float:
        """
        Getter for property: (float) MiddleAirGap
         Returns the air gap used between each cable tray.  
             
         
        """
        pass
    @MiddleAirGap.setter
    def MiddleAirGap(self, airGap: float):
        """
        Setter for property: (float) MiddleAirGap
         Returns the air gap used between each cable tray.  
             
         
        """
        pass
    @property
    def OutsideVerticalElbowPartIdentifier(self) -> str:
        """
        Getter for property: (str) OutsideVerticalElbowPartIdentifier
         Returns the outside vertical elbow's part identifier.  
             
         
        """
        pass
    @OutsideVerticalElbowPartIdentifier.setter
    def OutsideVerticalElbowPartIdentifier(self, elbowPartIdentifier: str):
        """
        Setter for property: (str) OutsideVerticalElbowPartIdentifier
         Returns the outside vertical elbow's part identifier.  
             
         
        """
        pass
    @property
    def OutsideVerticalElbowPartIdentifierType(self) -> PlaceCableTraysBuilder.PartIDType:
        """
        Getter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) OutsideVerticalElbowPartIdentifierType
         Returns the type of identifier used to find the outside vertical elbow part.  
             
         
        """
        pass
    @OutsideVerticalElbowPartIdentifierType.setter
    def OutsideVerticalElbowPartIdentifierType(self, elbowPartIDType: PlaceCableTraysBuilder.PartIDType):
        """
        Setter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) OutsideVerticalElbowPartIdentifierType
         Returns the type of identifier used to find the outside vertical elbow part.  
             
         
        """
        pass
    @property
    def PathSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PathSelection
         Returns the object used for selection of an Electrical Topology Path (ETP).  
             
         
        """
        pass
    @property
    def ReverseStartDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseStartDirection
         Returns whether the path has been reversed from its natural direction.  
             
         
        """
        pass
    @ReverseStartDirection.setter
    def ReverseStartDirection(self, isReversed: bool):
        """
        Setter for property: (bool) ReverseStartDirection
         Returns whether the path has been reversed from its natural direction.  
             
         
        """
        pass
    @property
    def TrayPartIdentifier(self) -> str:
        """
        Getter for property: (str) TrayPartIdentifier
         Returns the tray's part identifier.  
             
         
        """
        pass
    @TrayPartIdentifier.setter
    def TrayPartIdentifier(self, trayPartIdentifier: str):
        """
        Setter for property: (str) TrayPartIdentifier
         Returns the tray's part identifier.  
             
         
        """
        pass
    @property
    def TrayPartIdentifierType(self) -> PlaceCableTraysBuilder.PartIDType:
        """
        Getter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) TrayPartIdentifierType
         Returns the type of identifier used to find the tray part.  
             
         
        """
        pass
    @TrayPartIdentifierType.setter
    def TrayPartIdentifierType(self, trayPartIDType: PlaceCableTraysBuilder.PartIDType):
        """
        Setter for property: ( PlaceCableTraysBuilder.PartIDType NXOpen.Mech) TrayPartIdentifierType
         Returns the type of identifier used to find the tray part.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Display
import NXOpen.Routing
class PlaceElbowsBuilder(NXOpen.Builder): 
    """ Builder for placing multiple elbows."""
    class ReferenceSetType(Enum):
        """
        Members Include: 
         |Model|  Use model 
         |EntirePart|  Entire part 
         |Empty|  Empty reference set 

        """
        Model: int
        EntirePart: int
        Empty: int
        @staticmethod
        def ValueOf(value: int) -> PlaceElbowsBuilder.ReferenceSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowCutElbows(self) -> bool:
        """
        Getter for property: (bool) AllowCutElbows
         Returns a flag that determines whether an elbow should be cut to fit between the segments.  
             
         
        """
        pass
    @AllowCutElbows.setter
    def AllowCutElbows(self, allowCutElbows: bool):
        """
        Setter for property: (bool) AllowCutElbows
         Returns a flag that determines whether an elbow should be cut to fit between the segments.  
             
         
        """
        pass
    @property
    def LayerSettings(self) -> NXOpen.Display.LayerSettingsBuilder:
        """
        Getter for property: ( NXOpen.Display.LayerSettingsBuilder) LayerSettings
         Returns the layer setting for elbows to be placed   
            
         
        """
        pass
    @property
    def PlacementLocationCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PlacementLocationCollector
         Returns the routing control points or port collector   
            
         
        """
        pass
    @property
    def ReferenceSet(self) -> PlaceElbowsBuilder.ReferenceSetType:
        """
        Getter for property: ( PlaceElbowsBuilder.ReferenceSetType NXOpen.Mech) ReferenceSet
         Returns the reference set for elbows to be placed   
            
         
        """
        pass
    @ReferenceSet.setter
    def ReferenceSet(self, referenceSet: PlaceElbowsBuilder.ReferenceSetType):
        """
        Setter for property: ( PlaceElbowsBuilder.ReferenceSetType NXOpen.Mech) ReferenceSet
         Returns the reference set for elbows to be placed   
            
         
        """
        pass
    def GetPlacedElbowComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the elbow components of placed elbows. 
         Returns elbowComponents ( NXOpen.Assemblies.Component Li):  The components of placed elbows. .
        """
        pass
    def SelectComponentToBePlaced(self, placementLocation: NXOpen.NXObject, selectedMemberIdentifier: str) -> None:
        """
         Selects the member identifier of the elbow from reuse library to be placed at given placement location. 
        """
        pass
    def SetElbowSourceNodeIdentifier(self, elbowSourceNodeIdentifier: str) -> None:
        """
         The unique identifier of the elbow node 
        """
        pass
import NXOpen
class PublishSpoolAssembliesBuilder(NXOpen.Builder): 
    """ Builder for publishing spool assemblies for spools.
    """
    class CloseAfterSaveBehavior(Enum):
        """
        Members Include: 
         |DontClose|  Don't close the spool assembly after save. 
         |Close|  If the spool assembly is not already open, closes the spool assembly after save. 

        """
        DontClose: int
        Close: int
        @staticmethod
        def ValueOf(value: int) -> PublishSpoolAssembliesBuilder.CloseAfterSaveBehavior:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CloseBehavior(self) -> PublishSpoolAssembliesBuilder.CloseAfterSaveBehavior:
        """
        Getter for property: ( PublishSpoolAssembliesBuilder.CloseAfterSaveBehavior NXOpen.Mech) CloseBehavior
         Returns the behavior for closing spool assemblies after save   
            
         
        """
        pass
    @CloseBehavior.setter
    def CloseBehavior(self, behavior: PublishSpoolAssembliesBuilder.CloseAfterSaveBehavior):
        """
        Setter for property: ( PublishSpoolAssembliesBuilder.CloseAfterSaveBehavior NXOpen.Mech) CloseBehavior
         Returns the behavior for closing spool assemblies after save   
            
         
        """
        pass
    def GetFailedSpools(self) -> List[Spool]:
        """
         Gets the spools that failed to publish spool assemblies. 
         Returns failedSpools ( Spool List[NXOpen.Me): .
        """
        pass
    def GetSpools(self) -> List[Spool]:
        """
         Gets the spools to createupdate spool assemblies for 
         Returns spools ( Spool List[NXOpen.Me): .
        """
        pass
    def GetUpToDateSpools(self) -> List[Spool]:
        """
         Gets the spools that didn't update because they were already up-to-date. 
         Returns upToDateSpools ( Spool List[NXOpen.Me): .
        """
        pass
    def GetUpdatedSpools(self) -> List[Spool]:
        """
         Gets the spools that have successfully published spool assemblies. 
         Returns updatedSpools ( Spool List[NXOpen.Me): .
        """
        pass
    def OutputReport(self) -> None:
        """
         Outputs the report to detail the result of publishing spool assemblies. 
        """
        pass
    def SetSpools(self, spools: List[Spool]) -> None:
        """
         Sets the spools to createupdate spool assemblies for 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class RoutingManager(NXOpen.Object): 
    """ Represents an NXOpen.MechanicalRouting.RoutingManager object.
     """
    class DataType(Enum):
        """
        Members Include: 
         |All|  Export everything (segments, nodes, and devices).                
         |Network|  Export the segments and nodes that make up the cableway network. 
         |Devices|  Export the devices that connect to the cableway network.         

        """
        All: int
        Network: int
        Devices: int
        @staticmethod
        def ValueOf(value: int) -> RoutingManager.DataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuilderFactory() -> BuilderFactory:
        """
          Returns a  NXOpen::MechanicalRouting::BuilderFactory  object.  Use this object
                     to create specific routing mechanical builders.
                
        """
        pass
    @property
    def ConnectivityService() -> ConnectivityService:
        """
          Returns a  NXOpen::MechanicalRouting::ConnectivityService  object.  Use this object
                     for specific Routing Mechanical Connectivity Service.
                
        """
        pass
    @property
    def RunsManager() -> RunsManager:
        """
          Returns a  NXOpen::MechanicalRouting::RunsManager  object. Use this object
                     for specific Routing Mechanical Runs Manager.
                
        """
        pass
    @property
    def RunsAssignmentManager() -> RunsAssignmentManager:
        """
          Returns a  NXOpen::MechanicalRouting::RunsAssignmentManager  object. Use this object
                     for specific Routing Mechanical Runs Assignment Manager.
                
        """
        pass
    @property
    def SpoolManager() -> SpoolManager:
        """
          Returns a  NXOpen::MechanicalRouting::SpoolManager  object. Use this object
                     for managing spools and their associated objects
                
        """
        pass
    def AddGuidToObjectAttribute(guidObject: NXOpen.NXObject, attributeName: str) -> None:
        """
         Generates a Globally Unique Identifier (GUID) and adds it as the value of the
                    given attribute on the given object.
                
        """
        pass
    def ExportCablewayToFile(part: NXOpen.BasePart, xmlFileName: str, action: str, dataTypeToExport: RoutingManager.DataType, maxSearchLevels: int) -> None:
        """
         Exports all of the NX Routing cableway information from the given part
                    to the given XML file in a format the Capital Cable Router can read.
                    Returns an error if
                    
                        Unable to write to the file
                        There is no Routing data in the part
                    
                
        """
        pass
    def GetCoincidentNodes(nodeOccurrence: NXOpen.TaggedObject) -> List[NXOpen.TaggedObject]:
        """
         Get all coincident nodes at specified node. Node can be either controlpoint or cablewaynetwork point and is occurrence based.
         Returns coincidentNodes ( NXOpen.TaggedObject Li): .
        """
        pass
    def GetDuctReinforcementContainers(part: NXOpen.BasePart) -> List[DuctReinforcementContainer]:
        """
         Returns all NXOpen.MechanicalRouting.DuctReinforcementContainer objects in
                    the specified NXOpen.BasePart.
                
         Returns drcs ( DuctReinforcementContainer List[NXOpen.Me): .
        """
        pass
    def GetFillRuleAndSegregationForEtpComponentAtGivenTier(etpComponent: NXOpen.Assemblies.Component, tierIndex: int) -> Tuple[str, str, str]:
        """
          Returns the library-defined fill rule, overridden fill rule, and overridden segregation codes for a given electrical topology path component at the specified tier index.
                     Note: The tier index should start from 1 (e.g., Tier 1, Tier 2, ...). 
         Returns A tuple consisting of (libraryDefinedFillRule, overriddenFillRule, overriddenSegregationCodes). 
         - libraryDefinedFillRule is: str. library defined fill rule for an etp component at given tier index.
         - overriddenFillRule is: str. overridden fill rule for an etp component at given tier index.
         - overriddenSegregationCodes is: str. overridden segregation codes for an etp component at given tier index.

        """
        pass
    def GetPatternComponentsForEtpComponent(etpComponent: NXOpen.Assemblies.Component) -> List[NXOpen.Assemblies.Component]:
        """
          Returns all pattern components associated with the specified electrical topology path component. 
         Returns patternComponents ( NXOpen.Assemblies.Component Li):  associated pattern components .
        """
        pass
    def GetPatternComponentsForEtpComponentAtGivenTier(etpComponent: NXOpen.Assemblies.Component, tierIndex: int) -> List[NXOpen.Assemblies.Component]:
        """
          Returns all pattern components associated with the specified electrical topology path component at the specified tier index.
                     Note: The tier index should start from 1 (e.g., Tier 1, Tier 2, ...). 
         Returns patternComponents ( NXOpen.Assemblies.Component Li):  associated pattern components .
        """
        pass
    def GetPortsFromFitting(fittingComponent: NXOpen.Assemblies.Component) -> List[NXOpen.Routing.Port]:
        """
          Gets port occurrences from given fitting component.
                     One of the ports returned may not be from the part of that component and may be a prototype port if the
                     component is a cut elbow.
                
         Returns ports ( NXOpen.Routing.Port Li):   .
        """
        pass
    def GetReferencingEtpComponentForPatternComponent(patternComponent: NXOpen.Assemblies.Component) -> NXOpen.Assemblies.Component:
        """
          Returns the electrical topology path component that is referenced by the specified pattern component. 
         Returns etpComponent ( NXOpen.Assemblies.Component):  referenced etp component .
        """
        pass
import NXOpen
class RunMappingStatusMessageList(NXOpen.TransientObject): 
    """
         Contains a list of run mapping status messages.
    """
    def AddMessage(self, message: RunsAssignmentManager.MappingStatusMessage) -> None:
        """
         Adds a mapping status message to this list. 
        """
        pass
    def Clear(self) -> None:
        """
         Clears all messages from this list. 
        """
        pass
    def ContainsMessage(self, message: RunsAssignmentManager.MappingStatusMessage) -> bool:
        """
         Checks if the passed in mapping status message is already in the list. 
         Returns containsMessage (bool): .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object. 
        """
        pass
    def GetNthMessage(self, nthIndex: int) -> RunsAssignmentManager.MappingStatusMessage:
        """
         Gets the nth mapping status message in the list. 
         Returns message ( RunsAssignmentManager.MappingStatusMessage NXOpen.Mech):  The integer value of the characteristic. .
        """
        pass
    def GetNumberOfMessages(self) -> int:
        """
         Gets the number of mapping status messages in the list. 
         Returns numberOfMessages (int):  The integer value of the characteristic. .
        """
        pass
    def RemoveMessage(self, message: RunsAssignmentManager.MappingStatusMessage) -> None:
        """
         Removes the passed in mapping status message from the list. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
import NXOpen.Schematic.Mechanical
class RunsAssignmentManager(NXOpen.Object): 
    """ Represents the Runs Assignment Manager used to assign or unassign objects in the Routing Assembly
        to their corresponding objects in the P and ID run
    """
    class MappingStatus(Enum):
        """
        Members Include: 
         |Unknown| 
         |Pass| 
         |Warning| 
         |Error| 
         |CannotBeEvaluated| 

        """
        Unknown: int
        Pass: int
        Warning: int
        Error: int
        CannotBeEvaluated: int
        @staticmethod
        def ValueOf(value: int) -> RunsAssignmentManager.MappingStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MappingStatusMessage(Enum):
        """
        Members Include: 
         |Unknown| 
         |Assigned| 
         |NotAssigned| 
         |OneOrMoreConnectedPortsNotAssigned| 
         |Unloaded| 
         |DeviationOfDiscipline| 
         |DeviationOfSpecification| 
         |DeviationOfDisciplineAndSpecification| 
         |BreakAtFromPort| 
         |BreakAtToPort| 
         |BreakInContinuityOfObjectsInConnection| 
         |OneOrMoreBareSegmentsInConnection| 
         |AssignedStockDoesNotMatchLogicalStock| 
         |PortIdentifierDoesNotMatchLogicalPortIdentifier| 
         |ParentRunLoadedInMultipleOpenParts| 
         |PartAssociatedToRunNotLoaded| 
         |OneOrMoreBranchMembersHasAWarning| 
         |OneOrMoreBranchMembersHasAnError| 
         |OneOrMoreBranchMembersCannotBeEvaluated| 
         |OneOrMoreRunMembersHasAWarning| 
         |OneOrMoreRunMembersHasAnError| 
         |OneOrMoreRunMembersCannotBeEvaluated| 
         |ToPortEquipmentPartNotLoaded| 
         |FromPortEquipmentPartNotLoaded| 
         |AnUnkownErrorHasOccurred| 
         |OpenEndedConnectionAtFromPort| 
         |OpenEndedConnectionAtToPort| 
         |AssignedEquipmentDoesNotMatchLogicalEquipment| 
         |Suppressed| 
         |ToPortEquipmentSuppressed| 
         |FromPortEquipmentSuppressed| 
         |TerminatingPortDisconnectedFromAllTerminatingPorts| 
         |TerminatingPortNotConnectedToAllTerminatingPorts| 
         |BranchesWithinRunAreNotContiguous| 
         |PortAssignedMultipleTimes| 
         |EquipmentPortsAssignedInMultipleParts| 
         |ConnectionFromPortAssignedMultipleTimes| 
         |ConnectionToPortAssignedMultipleTimes| 
         |ComparisonAttributeValuesDoNotMatch| 
         |ConnectionAssignedInClosedAssembly| 
         |ConnectionFromPortAssignedInClosedAssembly| 
         |ConnectionToPortAssignedInClosedAssembly| 
         |ComparisonAttributeOfMatchingTypeAndNameCouldNotBeFound| 
         |MultipleAssociatedAssemblyRevisionsLoaded| 
         |BreakInContinuityOfDirectlyConnectedPorts| 
         |BreakInContinuityOfOutletJunction| 
         |UserDefined1| 
         |UserDefined2| 
         |UserDefined3| 
         |UserDefined4| 
         |UserDefined5| 
         |UserDefined6| 
         |UserDefined7| 
         |UserDefined8| 
         |UserDefined9| 
         |UserDefined10| 
         |DeviationOfDisciplineOfDirectConnection| 
         |DeviationOfSpecificationOfDirectConnection| 
         |DeviationOfDisciplineAndSpecificationOfDirectConnection| 
         |DeviationOfInsulationSpecification| 
         |DeviationOfInsulationType| 
         |InsulationNotAssignedToRun| 
         |SpecifiedInsulationMissing| 
         |OneOrMoreInsulationsIsNotLoaded| 
         |OneOrMoreInsulationsIsSuppressed| 
         |DirectlyConnectedPortAssignedInClosedAssembly| 
         |PortFlowDirectionDoesNotMatchLogicalPortFlowDirection| 
         |SystemPartExistsButNotAssigned| 
         |SystemPartTagsMismatch| 

        """
        Unknown: int
        Assigned: int
        NotAssigned: int
        OneOrMoreConnectedPortsNotAssigned: int
        Unloaded: int
        DeviationOfDiscipline: int
        DeviationOfSpecification: int
        DeviationOfDisciplineAndSpecification: int
        BreakAtFromPort: int
        BreakAtToPort: int
        BreakInContinuityOfObjectsInConnection: int
        OneOrMoreBareSegmentsInConnection: int
        AssignedStockDoesNotMatchLogicalStock: int
        PortIdentifierDoesNotMatchLogicalPortIdentifier: int
        ParentRunLoadedInMultipleOpenParts: int
        PartAssociatedToRunNotLoaded: int
        OneOrMoreBranchMembersHasAWarning: int
        OneOrMoreBranchMembersHasAnError: int
        OneOrMoreBranchMembersCannotBeEvaluated: int
        OneOrMoreRunMembersHasAWarning: int
        OneOrMoreRunMembersHasAnError: int
        OneOrMoreRunMembersCannotBeEvaluated: int
        ToPortEquipmentPartNotLoaded: int
        FromPortEquipmentPartNotLoaded: int
        AnUnkownErrorHasOccurred: int
        OpenEndedConnectionAtFromPort: int
        OpenEndedConnectionAtToPort: int
        AssignedEquipmentDoesNotMatchLogicalEquipment: int
        Suppressed: int
        ToPortEquipmentSuppressed: int
        FromPortEquipmentSuppressed: int
        TerminatingPortDisconnectedFromAllTerminatingPorts: int
        TerminatingPortNotConnectedToAllTerminatingPorts: int
        BranchesWithinRunAreNotContiguous: int
        PortAssignedMultipleTimes: int
        EquipmentPortsAssignedInMultipleParts: int
        ConnectionFromPortAssignedMultipleTimes: int
        ConnectionToPortAssignedMultipleTimes: int
        ComparisonAttributeValuesDoNotMatch: int
        ConnectionAssignedInClosedAssembly: int
        ConnectionFromPortAssignedInClosedAssembly: int
        ConnectionToPortAssignedInClosedAssembly: int
        ComparisonAttributeOfMatchingTypeAndNameCouldNotBeFound: int
        MultipleAssociatedAssemblyRevisionsLoaded: int
        BreakInContinuityOfDirectlyConnectedPorts: int
        BreakInContinuityOfOutletJunction: int
        UserDefined1: int
        UserDefined2: int
        UserDefined3: int
        UserDefined4: int
        UserDefined5: int
        UserDefined6: int
        UserDefined7: int
        UserDefined8: int
        UserDefined9: int
        UserDefined10: int
        DeviationOfDisciplineOfDirectConnection: int
        DeviationOfSpecificationOfDirectConnection: int
        DeviationOfDisciplineAndSpecificationOfDirectConnection: int
        DeviationOfInsulationSpecification: int
        DeviationOfInsulationType: int
        InsulationNotAssignedToRun: int
        SpecifiedInsulationMissing: int
        OneOrMoreInsulationsIsNotLoaded: int
        OneOrMoreInsulationsIsSuppressed: int
        DirectlyConnectedPortAssignedInClosedAssembly: int
        PortFlowDirectionDoesNotMatchLogicalPortFlowDirection: int
        SystemPartExistsButNotAssigned: int
        SystemPartTagsMismatch: int
        @staticmethod
        def ValueOf(value: int) -> RunsAssignmentManager.MappingStatusMessage:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AssignComponentPort(component: NXOpen.Assemblies.Component, physicalPort: NXOpen.Routing.Port, logicalPort: NXOpen.NXObject) -> None:
        """
         Assigns the 3D port object to the logical object it corresponds to 
        """
        pass
    def AssignComponentToLogicalEquipment(component: NXOpen.Assemblies.Component, logicalEquipment: NXOpen.NXObject) -> None:
        """
         Assigns a component Assemblies.Component to a logical equipment object. 
        """
        pass
    def AssignComponentsToLogicalConnection(components: List[NXOpen.Assemblies.Component], logicalConnection: NXOpen.NXObject) -> None:
        """
         Assigns a list of components mapping to a logical connection object. 
        """
        pass
    def AssignPort(physicalPort: NXOpen.Routing.Port, logicalPort: NXOpen.NXObject) -> None:
        """
         Assigns the 3D WAVE linked port object to the logical object it corresponds to 
        """
        pass
    def AssignPosition(position: NXOpen.Routing.IRoutePosition, positionComponent: NXOpen.Assemblies.Component, logicalPort: NXOpen.NXObject) -> None:
        """
         Assigns a NXOpen.Routing.IRoutePosition to a logical port 
        """
        pass
    def AssignSingleComponentToLogicalConnection(component: NXOpen.Assemblies.Component, logicalConnection: NXOpen.NXObject) -> None:
        """
         Assigns a single component to a logical connection object. 
        """
        pass
    def AssignSystemParts(workPart: NXOpen.Part, workPartComponent: NXOpen.Assemblies.Component, logicalEquipment: List[NXOpen.TaggedObject]) -> bool:
        """
         Automatically assigns 3D ports or WAVE linked ports to the logical equipment
                    it corresponds to based on the System Part Tag on the logical equipment.
                    The work part component can be  when the work part and the display part are the same.
                    Does nothing if the logical port has no System Part Tag or the system part is not loaded.
                
         Returns success (bool):  Were any system parts assigned? .
        """
        pass
    def GetAssignedLogicalConnection(component: NXOpen.Assemblies.Component) -> NXOpen.NXObject:
        """
         Gets the assigned logical connection for the passed in NXOpen.Assemblies.Component 
         Returns logicalConnection ( NXOpen.NXObject):  The logical connection object.
        """
        pass
    def GetAssignedLogicalEquipment(component: NXOpen.Assemblies.Component) -> NXOpen.NXObject:
        """
         Gets the assigned logical equipment for the passed in NXOpen.Assemblies.Component 
         Returns logicalEquipment ( NXOpen.NXObject):  The logical equipment object.
        """
        pass
    def GetAssignedLogicalJunctions(component: NXOpen.Assemblies.Component) -> List[NXOpen.NXObject]:
        """
         Gets the assigned logical junctions for the passed in NXOpen.Assemblies.Component 
         Returns logicalJunctions ( NXOpen.NXObject Li):  The logical junctions if the Assemblies.Component is assigned.
        """
        pass
    def GetAssignedLogicalPort(component: NXOpen.Assemblies.Component, position: NXOpen.Routing.IRoutePosition) -> NXOpen.NXObject:
        """
         Gets the assigned logical port for the passed in NXOpen.Routing.IRoutePosition. 
         Returns logicalPort ( NXOpen.NXObject):  The logical port.
        """
        pass
    def GetAssignedRuns(component: NXOpen.Assemblies.Component) -> List[NXOpen.Schematic.Mechanical.Run]:
        """
         Gets the runs to which the given component is assigned. 
         Returns runs ( NXOpen.Schematic.Mechanical.Run Li):  The runs the Assemblies.Component is assigned in.
        """
        pass
    def GetComponentLogicalEquipmentAssignedTo(part: NXOpen.Part, logicalEquipment: NXOpen.NXObject) -> NXOpen.Assemblies.Component:
        """
         Gets the part occurrence the logical equipment is assigned to in the part 
         Returns component ( NXOpen.Assemblies.Component):  The component the logical equipment is assigned to.
        """
        pass
    def GetComponentsLogicalConnectionAssignedTo(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the part occurrences the logical connection is assigned to in the part 
         Returns components ( NXOpen.Assemblies.Component Li):  The output component array.
        """
        pass
    def GetComponentsLogicalConnectionAssignedToInSession(connection: NXOpen.NXObject) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the components assigned to the logical connection in the whole session. 
         Returns components ( NXOpen.Assemblies.Component Li): .
        """
        pass
    def GetComponentsLogicalEquipmentAssignedToInSession(equipment: NXOpen.NXObject) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the components assigned to the logical equipment in the whole session. 
         Returns components ( NXOpen.Assemblies.Component Li): .
        """
        pass
    def GetLogicalConnectionFromPortAssignedTo(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> Tuple[NXOpen.Assemblies.Component, NXOpen.NXObject]:
        """
         Gets the port of the from port the logical connection is assigned to and its corresponding component in the part
         Returns A tuple consisting of (component, port). 
         - component is:  NXOpen.Assemblies.Component. The component the 3D port represents.
         - port is:  NXOpen.NXObject. The Routing Port object.

        """
        pass
    def GetLogicalConnectionFromPositionAssignedTo(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> Tuple[NXOpen.Assemblies.Component, NXOpen.Routing.IRoutePosition]:
        """
         Gets the NXOpen.Routing.IRoutePosition of a NXOpen.Assemblies.Component assigned to a
                    logical connection that is connected to the NXOpen.Routing.IRoutePosition assigned to the from port of the connection. 
         Returns A tuple consisting of (positionComponent, position). 
         - positionComponent is:  NXOpen.Assemblies.Component. The NXOpen.Assemblies.Component of the NXOpen.Routing.IRoutePosition.
         - position is:  NXOpen.Routing.IRoutePosition. The NXOpen.Routing.IRoutePosition.

        """
        pass
    def GetLogicalConnectionToPortAssignedTo(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> Tuple[NXOpen.Assemblies.Component, NXOpen.NXObject]:
        """
         Gets the port of the to port the logical connection is assigned to and its corresponding component in the part 
         Returns A tuple consisting of (component, port). 
         - component is:  NXOpen.Assemblies.Component. The component the 3D port represents.
         - port is:  NXOpen.NXObject. The Routing Port object.

        """
        pass
    def GetLogicalConnectionToPositionAssignedTo(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> Tuple[NXOpen.Assemblies.Component, NXOpen.Routing.IRoutePosition]:
        """
         Gets the NXOpen.Routing.IRoutePosition of a NXOpen.Assemblies.Component assigned to a
                    logical connection that is connected to the NXOpen.Routing.IRoutePosition assigned to the to port of the connection. 
         Returns A tuple consisting of (positionComponent, position). 
         - positionComponent is:  NXOpen.Assemblies.Component. The NXOpen.Assemblies.Component of the NXOpen.Routing.IRoutePosition.
         - position is:  NXOpen.Routing.IRoutePosition. The NXOpen.Routing.IRoutePosition.

        """
        pass
    def GetLogicalObjectMappingStatus(logicalDesignObject: NXOpen.NXObject) -> Tuple[RunsAssignmentManager.MappingStatus, RunsAssignmentManager.MappingStatusMessage]:
        """
         Gets the mapping status for a logical design object.
                Mapping statuses for direct connection fulfillment can be retrieved by passing in the start or end port of a direct connection. 
         Returns A tuple consisting of (mappingStatus, message). 
         - mappingStatus is:  RunsAssignmentManager.MappingStatus NXOpen.Mech. The mapping status.
         - message is:  RunsAssignmentManager.MappingStatusMessage NXOpen.Mech. The mapping status message.

        """
        pass
    def GetMappingStatusMessageUserString(message: RunsAssignmentManager.MappingStatusMessage) -> str:
        """
         Gets the user string for the passed in mapping status message. 
         Returns messageString (str):  The mapping status message string.
        """
        pass
    def GetPortLogicalPortAssignedTo(part: NXOpen.Part, logicalPort: NXOpen.NXObject) -> Tuple[NXOpen.Assemblies.Component, NXOpen.NXObject]:
        """
         Gets the 3D port object and the component the logical port is assigned to in the part 
         Returns A tuple consisting of (component, port). 
         - component is:  NXOpen.Assemblies.Component. The component the 3D port represents.
         - port is:  NXOpen.NXObject. The Routing Port object.

        """
        pass
    def GetPositionLogicalPortAssignedTo(part: NXOpen.Part, logicalPort: NXOpen.NXObject) -> Tuple[NXOpen.Assemblies.Component, NXOpen.Routing.IRoutePosition]:
        """
         Gets the NXOpen.Routing.IRoutePosition that the logical port is assigned to in the part 
         Returns A tuple consisting of (positionComponent, position). 
         - positionComponent is:  NXOpen.Assemblies.Component. The NXOpen.Assemblies.Component that the NXOpen.Routing.IRoutePosition belongs to. .
         - position is:  NXOpen.Routing.IRoutePosition. The assigned NXOpen.Routing.IRoutePosition object.

        """
        pass
    def GetPositionsLogicalPortAssignedToInSession(port: NXOpen.NXObject) -> Tuple[List[NXOpen.Routing.IRoutePosition], List[NXOpen.Assemblies.Component]]:
        """
         Gets the positions assigned to the logical port in the whole session. 
         Returns A tuple consisting of (positions, components). 
         - positions is:  NXOpen.Routing.IRoutePosition Li.
         - components is:  NXOpen.Assemblies.Component Li.

        """
        pass
    def GetSimplifiedViewLogicalObjectMappingStatus(logicalDesignObject: NXOpen.NXObject) -> Tuple[RunsAssignmentManager.MappingStatus, RunsAssignmentManager.MappingStatusMessage]:
        """
         Gets the simplified view mapping status from the logical design object. 
         Returns A tuple consisting of (mappingStatus, message). 
         - mappingStatus is:  RunsAssignmentManager.MappingStatus NXOpen.Mech. The mapping status.
         - message is:  RunsAssignmentManager.MappingStatusMessage NXOpen.Mech. The mapping status message.

        """
        pass
    def IsComponentAssignedToConnection(component: NXOpen.Assemblies.Component) -> bool:
        """
         Is the given part occ assigned to connection? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsComponentAssignedToEquipment(component: NXOpen.Assemblies.Component) -> bool:
        """
         Is the given part occ assigned to equipment? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsComponentAssignedToJunction(component: NXOpen.Assemblies.Component) -> bool:
        """
         Is the given Assemblies.Component assigned to a logical junction? 
         Returns isAssigned (bool):  Is the Assemblies.Component assigned?.
        """
        pass
    def IsLogicalConnectionAssigned(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> bool:
        """
         Is the given logical connection assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsLogicalConnectionFromPortAssigned(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> bool:
        """
         Is the given logical connection's From Port assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsLogicalConnectionFromPositionAssigned(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> bool:
        """
         Determines whether there is a NXOpen.Routing.IRoutePosition of a NXOpen.Assemblies.Component assigned to a
                    logical connection that is connected to the NXOpen.Routing.IRoutePosition assigned to the from port of the connection. 
         Returns isAssigned (bool):  Does the NXOpen.Routing.IRoutePosition exist? .
        """
        pass
    def IsLogicalConnectionToPortAssigned(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> bool:
        """
         Is the given logical connection's To Port assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsLogicalConnectionToPositionAssigned(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> bool:
        """
         Determines whether there is a NXOpen.Routing.IRoutePosition of a NXOpen.Assemblies.Component assigned to a
                    logical connection that is connected to the NXOpen.Routing.IRoutePosition assigned to the to port of the connection. 
         Returns isAssigned (bool):  Does the NXOpen.Routing.IRoutePosition exist? .
        """
        pass
    def IsLogicalDesignObjectAssigned(part: NXOpen.Part, logicalDesignObject: NXOpen.NXObject) -> bool:
        """
         Is the given logical design object assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsLogicalDesignedObjectAssignedInSession(logicalDesignObj: NXOpen.NXObject) -> bool:
        """
         Determines if the logical design object is assigned in the session. 
         Returns isAssigned (bool): .
        """
        pass
    def IsLogicalEquipmentAssigned(part: NXOpen.Part, logicalEquipment: NXOpen.NXObject) -> bool:
        """
         Is the given logical equipment assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsLogicalJunctionAssigned(part: NXOpen.Part, logicalJunction: NXOpen.NXObject) -> bool:
        """
         Is the given logical junction assigned? 
         Returns isAssigned (bool):  The result of whether the junction is assigned.
        """
        pass
    def IsLogicalPortAssigned(part: NXOpen.Part, logicalPort: NXOpen.NXObject) -> bool:
        """
         Is the given logical port assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsPortAssigned(component: NXOpen.Assemblies.Component, port: NXOpen.NXObject) -> bool:
        """
         Is the 3D port object assigned? 
         Returns isAssigned (bool):  The result of whether the object is assigned.
        """
        pass
    def IsPositionAssigned(positionComponent: NXOpen.Assemblies.Component, position: NXOpen.Routing.IRoutePosition) -> bool:
        """
         Determines whether the NXOpen.Routing.IRoutePosition is assigned to a logical port 
         Returns isAssigned (bool):  The result of whether the NXOpen.Routing.IRoutePosition is assigned .
        """
        pass
    def MakeComponentBranchTerminating(component: NXOpen.Assemblies.Component) -> None:
        """
         Converts a non-terminating component into a terminating component. Will only have an effect on components that are not inherently terminating. 
        """
        pass
    def MakeComponentNotBranchTerminating(component: NXOpen.Assemblies.Component) -> None:
        """
         Converts a terminating component into a non-terminating component. Will only have an effect on components that are not inherently terminating. 
        """
        pass
    def MapComponentToPart(part: NXOpen.Part, component: NXOpen.Assemblies.Component) -> NXOpen.Assemblies.Component:
        """
         Maps a component to a given part 
         Returns mappedComponent ( NXOpen.Assemblies.Component):  The mapped component.
        """
        pass
    def PrepareForUpdatingToSpecification(run: NXOpen.Schematic.Mechanical.Run) -> BulkReplacementBuilder:
        """
          Returns a NXOpen.MechanicalRouting.BulkReplacementBuilder object which can be committed or can be used to launch UI  
         Returns bulkReplacementBuilder ( BulkReplacementBuilder NXOpen.Mech): .
        """
        pass
    def RefreshFulfillmentInformation(runs: List[NXOpen.NXObject]) -> None:
        """
         Refreshes the fulfillment information of the selected runs from Teamcenter. 
        """
        pass
    def RefreshMappingStatusAndUpdateView(part: NXOpen.Part, runObject: NXOpen.NXObject) -> None:
        """
         Refreshes mapping status and update run navigator view. 
        """
        pass
    def Unassign(part: NXOpen.Part, logicalPort: NXOpen.NXObject) -> None:
        """
         Removes assignment of any 3D port objects to the passed in logical object 
        """
        pass
    def UnassignComponent(component: NXOpen.Assemblies.Component) -> None:
        """
         Removes assignment of the 3D part occurrence from any connection or junction it might be assigned to 
        """
        pass
    def UnassignComponentFromLogicalEquipment(part: NXOpen.Part, logicalEquipment: NXOpen.NXObject) -> None:
        """
         Unassigns all the components that are currently assigned to the given logical equipment object. 
        """
        pass
    def UnassignComponents(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Unassigns the given components from the logical connections and ports that they are assigned to. 
        """
        pass
    def UnassignComponentsFromLogicalConnection(part: NXOpen.Part, logicalConnection: NXOpen.NXObject) -> None:
        """
         Unassigns all the components currently assigned to this logical connection object. 
        """
        pass
    def UnassignLogicalConnectionInSession(logicalConnection: NXOpen.NXObject) -> None:
        """
         Unassigns all the components currently assigned to this logical connection object in the session. 
        """
        pass
    def UnassignLogicalEquipmentInSession(logicalEquipment: NXOpen.NXObject) -> None:
        """
         Unassigns all the components that are currently assigned to the given logical equipment object in the session. 
        """
        pass
    def UnassignLogicalObjectsInSession(logicalObjects: List[NXOpen.NXObject]) -> None:
        """
         Removes all 3D object assignments from the given logical objects in the session. 
        """
        pass
    def UnassignLogicalPortInSession(logicalPort: NXOpen.NXObject) -> None:
        """
         Removes all 3D object assignments from the logical port in the session. 
        """
        pass
    def UnassignPositions(positions: List[NXOpen.Routing.IRoutePosition], positionComponents: List[NXOpen.Assemblies.Component]) -> None:
        """
         Unassigns the given positions from the logical ports that they are assigned to. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class RunsManager(NXOpen.Object): 
    """ Represents the Runs Manager used to manage runs in Mechanical Routing application,
        including loading and unloading runs, associatingdetaching runs tofrom the part, settingclearing
        the active run, and addingremoving components tofrom the runs
    """
    def AddComponentsToRun(componentsToAdd: List[NXOpen.Assemblies.Component], run: NXOpen.NXObject) -> None:
        """
         Makes the passed in components members of the passed in run 
        """
        pass
    def AddToRun(component: NXOpen.Assemblies.Component, run: NXOpen.NXObject) -> None:
        """
         Makes the passed in component a member of the passed in run 
        """
        pass
    def AlignComponentsInBranchToFlowDirection(part: NXOpen.Part, branch: NXOpen.NXObject) -> bool:
        """
         Validates and flips the parts in branch to align with flow direction 
         Returns isAnyPartFlipped (bool):  Is any part is flipped .
        """
        pass
    def AlignComponentsInRunToFlowDirection(part: NXOpen.Part, run: NXOpen.NXObject) -> bool:
        """
         Validates and flips the parts in run to align with flow direction 
         Returns isAnyPartFlipped (bool):  Is any part is flipped .
        """
        pass
    def AssociateRun(part: NXOpen.Part, run: NXOpen.NXObject) -> None:
        """
         Associates the run to the part
                
        """
        pass
    def Delete3dRunObject(part: NXOpen.Part, runObject: NXOpen.NXObject) -> None:
        """
         Deletes a RSD 3D authored run or branch object 
        """
        pass
    def Delete3dRunObjects(runObjects: List[NXOpen.NXObject]) -> None:
        """
         Deletes one or more 3D authored runs or branches from the part file 
        """
        pass
    def DissociateRun(part: NXOpen.Part, run: NXOpen.NXObject) -> None:
        """
         Detaches the run from the part
                
        """
        pass
    def GetLoadedRuns() -> List[NXOpen.NXObject]:
        """
         Gets the loaded runs in the NX session
                
         Returns runs ( NXOpen.NXObject Li):  The run objects that are loaded in the NX session .
        """
        pass
    def LoadAssociatedAssemblies(runObjects: List[NXOpen.NXObject]) -> None:
        """
         Loads the assemblies associated to the given run objects. 
        """
        pass
    def LoadRuns(collaborativeDesign: NXOpen.CollaborativeDesign, runIdsToLoad: List[str]) -> None:
        """
         Loads the runs in to the NX session
                
        """
        pass
    def MakeRunInactive(part: NXOpen.Part) -> None:
        """
         Makes any active runs inactive for the specified part
                
        """
        pass
    def MoveComponentsToRun(componentsToMove: List[NXOpen.Assemblies.Component], run: NXOpen.NXObject) -> None:
        """
         Moves membership of the passed in components from whatever runs they belong to the passed in run 
        """
        pass
    def MoveToRun(component: NXOpen.Assemblies.Component, run: NXOpen.NXObject) -> None:
        """
         Moves membership of the passed in component from whatever run it belongs to the passed in run 
        """
        pass
    def RemoveComponentFromRun(component: NXOpen.Assemblies.Component, run: NXOpen.NXObject) -> None:
        """
         Removes the passed in component from membership of the passed in run 
        """
        pass
    def RemoveComponentsFromRun(componentsToRemove: List[NXOpen.Assemblies.Component], run: NXOpen.NXObject) -> None:
        """
         Removes the passed in components from membership of the passed in run 
        """
        pass
    def ReverseFlowDirectionForRunBranch(run: NXOpen.NXObject) -> None:
        """
         Reverses the flow direction of the specified branch of the run 
        """
        pass
    def SetActiveRun(part: NXOpen.Part, run: NXOpen.NXObject) -> None:
        """
         Sets the active run to the passed in run for the specified part
                
        """
        pass
    def ShowFlowDirectionForRun(part: NXOpen.Part, run: NXOpen.NXObject) -> None:
        """
         Shows the flow direction of all the branches for the run 
        """
        pass
    def ShowFlowDirectionForRunBranch(part: NXOpen.Part, run: NXOpen.NXObject) -> None:
        """
         Shows the flow direction of the specified branch of the run 
        """
        pass
    def UnloadRun(run: NXOpen.NXObject) -> None:
        """
         Closes and unloads the passed in run
                
        """
        pass
import NXOpen
import NXOpen.Routing
class SlopePathBuilder(NXOpen.Builder): 
    """ Builder class for Slope Path command. """
    class ModeENUM(Enum):
        """
        Members Include: 
         |Forward| 
         |Backward| 

        """
        Forward: int
        Backward: int
        @staticmethod
        def ValueOf(value: int) -> SlopePathBuilder.ModeENUM:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationENUM(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 

        """
        Up: int
        Down: int
        @staticmethod
        def ValueOf(value: int) -> SlopePathBuilder.OrientationENUM:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SlopFallENUM(Enum):
        """
        Members Include: 
         |Angle| 
         |Ratio1in| 
         |Percentage| 

        """
        Angle: int
        Ratio1in: int
        Percentage: int
        @staticmethod
        def ValueOf(value: int) -> SlopePathBuilder.SlopFallENUM:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def ApplicationMode(self) -> SlopePathBuilder.ModeENUM:
        """
        Getter for property: ( SlopePathBuilder.ModeENUM NXOpen.Mech) ApplicationMode
         Returns the application mode   
            
         
        """
        pass
    @ApplicationMode.setter
    def ApplicationMode(self, applicationMode: SlopePathBuilder.ModeENUM):
        """
        Setter for property: ( SlopePathBuilder.ModeENUM NXOpen.Mech) ApplicationMode
         Returns the application mode   
            
         
        """
        pass
    @property
    def ApplySlopeToPath(self) -> bool:
        """
        Getter for property: (bool) ApplySlopeToPath
         Returns the apply slope to path   
            
         
        """
        pass
    @ApplySlopeToPath.setter
    def ApplySlopeToPath(self, applySlopeToPath: bool):
        """
        Setter for property: (bool) ApplySlopeToPath
         Returns the apply slope to path   
            
         
        """
        pass
    @property
    def FallDistance(self) -> float:
        """
        Getter for property: (float) FallDistance
         Returns the fall distance   
            
         
        """
        pass
    @FallDistance.setter
    def FallDistance(self, fallDistance: float):
        """
        Setter for property: (float) FallDistance
         Returns the fall distance   
            
         
        """
        pass
    @property
    def LockFirst(self) -> bool:
        """
        Getter for property: (bool) LockFirst
         Returns the lock first   
            
         
        """
        pass
    @LockFirst.setter
    def LockFirst(self, lockFirst: bool):
        """
        Setter for property: (bool) LockFirst
         Returns the lock first   
            
         
        """
        pass
    @property
    def LockLast(self) -> bool:
        """
        Getter for property: (bool) LockLast
         Returns the lock last   
            
         
        """
        pass
    @LockLast.setter
    def LockLast(self, lockLast: bool):
        """
        Setter for property: (bool) LockLast
         Returns the lock last   
            
         
        """
        pass
    @property
    def Orientation(self) -> SlopePathBuilder.OrientationENUM:
        """
        Getter for property: ( SlopePathBuilder.OrientationENUM NXOpen.Mech) Orientation
         Returns the orientation   
            
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: SlopePathBuilder.OrientationENUM):
        """
        Setter for property: ( SlopePathBuilder.OrientationENUM NXOpen.Mech) Orientation
         Returns the orientation   
            
         
        """
        pass
    @property
    def Percentage(self) -> float:
        """
        Getter for property: (float) Percentage
         Returns the percentage   
            
         
        """
        pass
    @Percentage.setter
    def Percentage(self, percentage: float):
        """
        Setter for property: (float) Percentage
         Returns the percentage   
            
         
        """
        pass
    @property
    def Ratio(self) -> float:
        """
        Getter for property: (float) Ratio
         Returns the ratio   
            
         
        """
        pass
    @Ratio.setter
    def Ratio(self, ratio: float):
        """
        Setter for property: (float) Ratio
         Returns the ratio   
            
         
        """
        pass
    @property
    def SlopeCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SlopeCollector
         Returns the slope collector   
            
         
        """
        pass
    @property
    def SlopeFallMethod(self) -> SlopePathBuilder.SlopFallENUM:
        """
        Getter for property: ( SlopePathBuilder.SlopFallENUM NXOpen.Mech) SlopeFallMethod
         Returns the slope fall method   
            
         
        """
        pass
    @SlopeFallMethod.setter
    def SlopeFallMethod(self, slopeFallMethod: SlopePathBuilder.SlopFallENUM):
        """
        Setter for property: ( SlopePathBuilder.SlopFallENUM NXOpen.Mech) SlopeFallMethod
         Returns the slope fall method   
            
         
        """
        pass
    def ComputeLegFall(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def ComputeLegSequence(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def IsLegFullyLocked(self, selectId: int) -> bool:
        """
         Method to return if a leg is fully locked 
         Returns isFullyLocked (bool): .
        """
        pass
    def IsLegFullyLockedBySystem(self, selectId: int) -> bool:
        """
         Method to return if a leg is fully locked by system
         Returns isFullyLockedBySystem (bool): .
        """
        pass
    def IsLegLocked(self, selectId: int, firstLock: bool) -> bool:
        """
         Method to return if a leg is locked, if firstLock is true check the first lock else check the last 
         Returns isLocked (bool): .
        """
        pass
    def IsLegLockedBySystem(self, selectId: int, firstLock: bool) -> bool:
        """
         Method to return if a leg is locked by system, if firstLock is true check the first lock else check the last 
         Returns isLockedBySystem (bool): .
        """
        pass
    def PathSequenceData(self, selectId: int) -> Tuple[bool, int, int, float, float, float]:
        """
         Method to return leg path sequence data
         Returns A tuple consisting of (validSelectId, pathSlant, pathOrient, pathSlope, pathFall, pathProjectedLength). 
         - validSelectId is: bool.
         - pathSlant is: int.
         - pathOrient is: int.
         - pathSlope is: float.
         - pathFall is: float.
         - pathProjectedLength is: float.

        """
        pass
    def PathSequenceEntityTags(self, selectId: int) -> Tuple[bool, List[NXOpen.TaggedObject]]:
        """
         Method to return path sequence entity tags
         Returns A tuple consisting of (validSelectId, pathEntityTags). 
         - validSelectId is: bool.
         - pathEntityTags is:  NXOpen.TaggedObject Li.

        """
        pass
    def ReverseStartDirection(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def SetLegPathFirstLock(self, legIndex: int, lock: bool) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def SetLegPathLastLock(self, legIndex: int, lock: bool) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def ValidatePathSelection(self) -> int:
        """
         Method to validate the path selection 
         Returns errorSelection (int): .
        """
        pass
import NXOpen
import NXOpen.Routing
class SpaceReservationReplacementBuilder(NXOpen.Builder): 
    """Builder class for Space Reservation Replacement command."""
    @property
    def ElectricalTopologyPathSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ElectricalTopologyPathSelection
         Returns the object used for selection of an Electrical Topology Path (ETP).  
             
         
        """
        pass
    def RecommendSpaceReservationWidths(self, objects: List[NXOpen.NXObject], lowerFillPercentages: List[float], upperFillPercentages: List[float], listOfWidth: List[float], maxWidthSuggestion: int, tierID: str) -> List[float]:
        """
         Recommends optimal space reservation width from given list of widths. If the recommendation is not possible then 
                existing width will be returned. User is expected to send segment occurrences. Its recommended to provide segments
                having same space reservation type applied.
         Returns recommendedWidths (List[float]): .
        """
        pass
import NXOpen
import NXOpen.Routing
class SpoolBuilder(NXOpen.Builder): 
    """ Builder for creatingediting spool objects.
    """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of the spool   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description of the spool   
            
         
        """
        pass
    @property
    def Members(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) Members
         Returns the  NXOpen::Routing::RouteObjectCollector  used to collect the members of the spool  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the spool   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the spool   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SpoolCollection(NXOpen.TaggedObjectCollection): 
    """  Represents a collection of NXOpen.MechanicalRouting.Spool objects. 
        Iterating this collection only returns live uncondemned objects contained in the owning part
    """
    def GetSpoolFromComponent(self, component: NXOpen.Assemblies.Component) -> Spool:
        """
         Returns the NXOpen.MechanicalRouting.Spool to which this component
                    belongs, if any. Returns  if the component does not belong to a spool. 
         Returns spool ( Spool NXOpen.Mech):  .
        """
        pass
import NXOpen
import NXOpen.Routing
class SpoolDelimiterBuilder(NXOpen.Builder): 
    """ Builder for specifying delimiters for spools from Routing assemblies.
    """
    @property
    def FittingComponents(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) FittingComponents
         Returns the  NXOpen::Routing::RouteObjectCollector  used to collect the components for delimiting spools   
            
         
        """
        pass
    @property
    def PortsToSetAsDelimiters(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PortsToSetAsDelimiters
         Returns the  NXOpen::Routing::RouteObjectCollector  used to collect ports to set as spool delimiters   
            
         
        """
        pass
    @property
    def PortsToUnsetAsDelimiters(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PortsToUnsetAsDelimiters
         Returns the  NXOpen::Routing::RouteObjectCollector  used to collect ports to unset as spool delimiters   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SpoolManager(NXOpen.Object): 
    """ Represents the Spool Manager used to manage spools and their associated objects
    """
    def FindParentAssembly(spoolAssemblyPart: NXOpen.Part) -> NXOpen.Part:
        """
         When given a spool assembly part, returns the parent assembly part, if it's loaded.
                    Returns  if the parent assembly is not loaded. 
         Returns parentAssemblyPart ( NXOpen.Part): .
        """
        pass
    def FindParentAssemblyComponent(spoolAssemblyComponent: NXOpen.Assemblies.Component, sourceSpool: Spool) -> NXOpen.Assemblies.Component:
        """
         When given a spool assembly component, returns the parent assembly component, if it's loaded.
                    Returns  if the parent assembly is not loaded. 
         Returns parentAssemblyComponent ( NXOpen.Assemblies.Component):  The parent assembly component. .
        """
        pass
    def FindSourceSpool(spoolAssemblyPart: NXOpen.Part) -> Spool:
        """
         Finds the spool used to create the spool assembly.
                    Returns  if the parent assembly is not loaded. 
         Returns sourceSpool ( Spool NXOpen.Mech): .
        """
        pass
    def IsSpoolAssembly(part: NXOpen.Part) -> bool:
        """
         Is the part a spool assembly? 
         Returns isSpoolAssembly (bool): .
        """
        pass
    def MoveMembersToSpool(members: List[NXOpen.Assemblies.Component], desinationSpool: Spool) -> None:
        """
         Moves the members to the destination spool, removing them from their original spools 
        """
        pass
    def QueryParentAssembly(spoolAssembly: NXOpen.Part) -> str:
        """
         Queries the filename of the assembly that contains the spool that the spool assembly was published from. 
         Returns parentFileName (str):  The parent assembly of the spool assembly .
        """
        pass
    def QuerySpoolAssemblies(spools: List[Spool]) -> List[str]:
        """
         Queries the filenames of the associated spool assemblies of the given spools.
                    If a spool does not have an associated spool assembly, this returns an empty value in the array. 
         Returns spoolAssemblyFileNames (List[str]):  The spool assemblies for the spools. .
        """
        pass
    def RefreshSpoolAssemblyInformation(spools: List[Spool]) -> None:
        """
         Refreshes spool assembly information for the given spools from Teamcenter. 
        """
        pass
    def RefreshSpools(part: NXOpen.Part) -> None:
        """
         Refreshes the associated view set and component group of the spools 
        """
        pass
    def RemoveMembersFromTheirSpools(members: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes members from the spools they are members of 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class Spool(NXOpen.NXObject): 
    """ The Spool class maintains a list of components used in a single manufactuable unit.
        Use the NXOpen.MechanicalRouting.SpoolBuilder
        to create a new Spool object.
        """
    class SpoolAssemblyPublishStatus(Enum):
        """
        Members Include: 
         |Unknown|  The spool assembly status is unknown, most likely due to unconfigured spool assembly revision 
         |UpToDate|  The spool assembly is up to date with design changes. 
         |OutOfDate|  The spool assembly is out of date with design changes. 

        """
        Unknown: int
        UpToDate: int
        OutOfDate: int
        @staticmethod
        def ValueOf(value: int) -> Spool.SpoolAssemblyPublishStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentGroup(self) -> NXOpen.Assemblies.ComponentGroup:
        """
        Getter for property: ( NXOpen.Assemblies.ComponentGroup) ComponentGroup
         Returns the component group of the spool   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of the spool   
            
         
        """
        pass
    @property
    def HasSpoolAssembly(self) -> bool:
        """
        Getter for property: (bool) HasSpoolAssembly
         Returns the existence of a spool assembly published for the spool   
            
         
        """
        pass
    @property
    def LastPublishDate(self) -> str:
        """
        Getter for property: (str) LastPublishDate
         Returns the last publish date of the spool assembly   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the spool   
            
         
        """
        pass
    @property
    def SpoolAssemblyFileName(self) -> str:
        """
        Getter for property: (str) SpoolAssemblyFileName
         Returns the file name of the published spool assembly   
            
         
        """
        pass
    @property
    def SpoolAssemblyStatus(self) -> Spool.SpoolAssemblyPublishStatus:
        """
        Getter for property: ( Spool.SpoolAssemblyPublishStatus NXOpen.Mech) SpoolAssemblyStatus
         Returns the status of the spool assembly   
            
         
        """
        pass
    @property
    def ViewSet(self) -> NXOpen.ViewSet:
        """
        Getter for property: ( NXOpen.ViewSet) ViewSet
         Returns the view set of the spool   
            
         
        """
        pass
    def GetMembers(self) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the members of the spool 
         Returns members ( NXOpen.Assemblies.Component Li): .
        """
        pass
    def HasMember(self, objectValue: NXOpen.Assemblies.Component) -> bool:
        """
         Does the spool have the passed in object as a member? 
         Returns hasMember (bool): .
        """
        pass
import NXOpen
import NXOpen.Schematic.Mechanical
class UpdateRunBuilder(NXOpen.Builder): 
    """ Builder for updating runs referenced by Routed System Designer assemblies to specific revisionsversions of the runs
    """
    class Status(Enum):
        """
        Members Include: 
         |RetainedExistingRevision| 
         |Dissociated| 
         |UpdatedToSelectedRevision| 
         |UpdatedToLatestRevision| 

        """
        RetainedExistingRevision: int
        Dissociated: int
        UpdatedToSelectedRevision: int
        UpdatedToLatestRevision: int
        @staticmethod
        def ValueOf(value: int) -> UpdateRunBuilder.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddAllRuns(self) -> None:
        """
         Adds all the runs in the NX session to be updated to a different revisionversion 
        """
        pass
    def AddRuns(self, runs: List[NXOpen.Schematic.Mechanical.Run]) -> None:
        """
         Adds the specified the runs to be updated to a different revisionversion 
        """
        pass
    def GetRunStatus(self, runIdentifier: str) -> UpdateRunBuilder.Status:
        """
         Gets the status of updating the specified run 
         Returns status ( UpdateRunBuilder.Status NXOpen.Mech):  The status of the specified run .
        """
        pass
    def GetSelectedRunRevision(self, run: NXOpen.Schematic.Mechanical.Run) -> str:
        """
         Gets which revision of the run is specified to update the run to 
         Returns revision (str):  The selected revision for this run object .
        """
        pass
    def SetRunToDissociate(self, run: NXOpen.Schematic.Mechanical.Run) -> None:
        """
         Sets the specified run to be dissociated from the Routed System Designer assemblies 
        """
        pass
    def SetSelectedRunRevision(self, run: NXOpen.Schematic.Mechanical.Run, revision: str) -> None:
        """
         Sets the specific revision to update the run to 
        """
        pass
