from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AutomaticRoutingBuilder(NXOpen.Builder): 
    """ Builder Class for Automatic Routing UI """
    def GetEndNode(self, cable: Cable) -> Node:
        """
         Gets the end NXOpen.CableRouter.Managed.Node for this automatic routing operation.
         Returns endNode ( Node NXOpen.Cable): .
        """
        pass
    def GetMandatoryNode(self, cable: Cable) -> List[Node]:
        """
         Gets the mandatory NXOpen.CableRouter.Managed.Node objects that the path must pass through.
         Returns mandatoryNodes ( Node List[NXOpen.Cab): .
        """
        pass
    def GetProhibitedSegment(self, cable: Cable) -> List[LineSegment]:
        """
         Gets the prohibited NXOpen.CableRouter.Managed.LineSegment objects that the path must not pass through.
         Returns prohibitedSegments ( LineSegment List[NXOpen.Cab): .
        """
        pass
    def GetStartNode(self, cable: Cable) -> Node:
        """
         Gets the start NXOpen.CableRouter.Managed.Node for this automatic routing operation.
         Returns startNode ( Node NXOpen.Cable): .
        """
        pass
    def SetEndNode(self, cable: Cable, endNode: Node) -> None:
        """
         Sets the end NXOpen.CableRouter.Managed.Node for this automatic routing operation.
        """
        pass
    def SetMandatoryNode(self, cable: Cable, mandatoryNode: List[Node]) -> None:
        """
         Sets the mandatory NXOpen.CableRouter.Managed.Node objects that the path must pass through.
        """
        pass
    def SetProhibitedSegment(self, cable: Cable, prohibitedSegments: List[LineSegment]) -> None:
        """
         Sets the prohibited NXOpen.CableRouter.Managed.LineSegment objects that the path must not pass through.
        """
        pass
    def SetStartNode(self, cable: Cable, startNode: Node) -> None:
        """
         Sets the start NXOpen.CableRouter.Managed.Node for this automatic routing operation.
        """
        pass
    def StartAutomaticRouting(self) -> None:
        """
         Activates this operation to start automatically routing the stored NXOpen.CableRouter.Managed.Cable
        """
        pass
    def StopAutomaticRouting(self) -> None:
        """
         Clears all operations remaining for automatic routing. 
        """
        pass
    def ValidateBuilderUpToDate(self) -> bool:
        """
         Verifies the stored objects are up to date with Teamcenter 
         Returns isUpdated (bool): .
        """
        pass
import NXOpen
class BaseData(NXOpen.DisplayableObject): 
    """ Represents the classes that are created in the Cable Router application. """
    def GetCustomAttribute(self, id: str) -> str:
        """
         Retrieves the custom attribute requested from this object 
         Returns value (str): .
        """
        pass
import NXOpen
class CableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.Cable objects. """
    def FindObject(self, journalIdentifier: str) -> Cable:
        """
         Finds the NXOpen.CableRouter.Managed.Cable with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns node ( Cable NXOpen.Cable):  NXOpen.CableRouter.Managed.Cable with this name. .
        """
        pass
class CableRouterManagedCableproperties(Enum):
    """
    Members Include: 
     |CableNull| 
     |CableLogicalName| 
     |CableLogicalRevision| 
     |CablePhysicalName| 
     |CablePhysicalRevision| 
     |CableFromDevice| 
     |CableToDevice| 
     |CableRouteStatus| 
     |CableLengthCorrection| 
     |CableFromExtraLength| 
     |CableToExtraLength| 
     |CableFromNodeId| 
     |CableToNodeId| 
     |CableLength| 
     |CableWeigth| 
     |CableSystem| 
     |CableSegregation| 
     |CableMinLength| 
     |CableMaxLength| 
     |CableStock| 
     |CableLinearWeight| 
     |CableOuterDiameter| 
     |CableMinimumBendRadius| 
     |CableEstimatedLength| 
     |CableCustom| 

    """
    CableNull: int
    CableLogicalName: int
    CableLogicalRevision: int
    CablePhysicalName: int
    CablePhysicalRevision: int
    CableFromDevice: int
    CableToDevice: int
    CableRouteStatus: int
    CableLengthCorrection: int
    CableFromExtraLength: int
    CableToExtraLength: int
    CableFromNodeId: int
    CableToNodeId: int
    CableLength: int
    CableWeigth: int
    CableSystem: int
    CableSegregation: int
    CableMinLength: int
    CableMaxLength: int
    CableStock: int
    CableLinearWeight: int
    CableOuterDiameter: int
    CableMinimumBendRadius: int
    CableEstimatedLength: int
    CableCustom: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedCableproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedCableRoutestatus(Enum):
    """
    Members Include: 
     |Unset| 
     |NotRouted| 
     |PartiallyRouted| 
     |FullyRouted| 
     |OffRouted| 
     |Approved| 

    """
    Unset: int
    NotRouted: int
    PartiallyRouted: int
    FullyRouted: int
    OffRouted: int
    Approved: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedCableRoutestatus:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedContainerCalculatedproperties:
    """
     Enum Type for the calculated properties of Containers
    """
    @property
    def ValidProperties(self) -> bool:
        """
        Getter for property ValidProperties
        """
        pass
    @ValidProperties.setter
    def ValidProperties(self, value: bool):
        """
        Getter for property ValidPropertiesSetter for property ValidProperties
        """
        pass
    @property
    def RoutableEntitiesFilling(self) -> float:
        """
        Getter for property RoutableEntitiesFilling
        """
        pass
    @RoutableEntitiesFilling.setter
    def RoutableEntitiesFilling(self, value: float):
        """
        Getter for property RoutableEntitiesFillingSetter for property RoutableEntitiesFilling
        """
        pass
    @property
    def RoutableEntitiesFillingPercentage(self) -> float:
        """
        Getter for property RoutableEntitiesFillingPercentage
        """
        pass
    @RoutableEntitiesFillingPercentage.setter
    def RoutableEntitiesFillingPercentage(self, value: float):
        """
        Getter for property RoutableEntitiesFillingPercentageSetter for property RoutableEntitiesFillingPercentage
        """
        pass
    @property
    def OverallFilling(self) -> float:
        """
        Getter for property OverallFilling
        """
        pass
    @OverallFilling.setter
    def OverallFilling(self, value: float):
        """
        Getter for property OverallFillingSetter for property OverallFilling
        """
        pass
    @property
    def OverallFillingPercentage(self) -> float:
        """
        Getter for property OverallFillingPercentage
        """
        pass
    @OverallFillingPercentage.setter
    def OverallFillingPercentage(self, value: float):
        """
        Getter for property OverallFillingPercentageSetter for property OverallFillingPercentage
        """
        pass
    @property
    def Weight(self) -> float:
        """
        Getter for property Weight
        """
        pass
    @Weight.setter
    def Weight(self, value: float):
        """
        Getter for property WeightSetter for property Weight
        """
        pass
    @property
    def WeightPercentage(self) -> float:
        """
        Getter for property WeightPercentage
        """
        pass
    @WeightPercentage.setter
    def WeightPercentage(self, value: float):
        """
        Getter for property WeightPercentageSetter for property WeightPercentage
        """
        pass
    @property
    def AvailableFilling(self) -> float:
        """
        Getter for property AvailableFilling
        """
        pass
    @AvailableFilling.setter
    def AvailableFilling(self, value: float):
        """
        Getter for property AvailableFillingSetter for property AvailableFilling
        """
        pass
    @property
    def AvailableFillingPercentage(self) -> float:
        """
        Getter for property AvailableFillingPercentage
        """
        pass
    @AvailableFillingPercentage.setter
    def AvailableFillingPercentage(self, value: float):
        """
        Getter for property AvailableFillingPercentageSetter for property AvailableFillingPercentage
        """
        pass
class CableRouterManagedContainerproperties(Enum):
    """
    Members Include: 
     |ContainerNull| 
     |ContainerId| 
     |ContainerHeight| 
     |ContainerWidth| 
     |ContainerBendRadius| 
     |ContainerWeight| 
     |ContainerPermissibleWeight| 
     |ContainerCablewayType| 
     |ContainerFillRule| 
     |ContainerDiameter| 
     |ContainerRoutableEntitiesFilling| 
     |ContainerRoutableEntitiesFillingPercentage| 
     |ContainerOverallFilling| 
     |ContainerOverallFillingPercentage| 
     |ContainerOverallWeight| 
     |ContainerOverallWeightPercentage| 
     |ContainerAvailableFilling| 
     |ContainerAvailableFillingPercentage| 
     |ContainerCustom| 

    """
    ContainerNull: int
    ContainerId: int
    ContainerHeight: int
    ContainerWidth: int
    ContainerBendRadius: int
    ContainerWeight: int
    ContainerPermissibleWeight: int
    ContainerCablewayType: int
    ContainerFillRule: int
    ContainerDiameter: int
    ContainerRoutableEntitiesFilling: int
    ContainerRoutableEntitiesFillingPercentage: int
    ContainerOverallFilling: int
    ContainerOverallFillingPercentage: int
    ContainerOverallWeight: int
    ContainerOverallWeightPercentage: int
    ContainerAvailableFilling: int
    ContainerAvailableFillingPercentage: int
    ContainerCustom: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedContainerproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedDeviceproperties(Enum):
    """
    Members Include: 
     |DeviceNull| 
     |DeviceLogicalName| 
     |DeviceLogicalRevision| 
     |DevicePhysicalName| 
     |DevicePhysicalRevision| 
     |DeviceX| 
     |DeviceY| 
     |DeviceZ| 
     |DeviceCustom| 

    """
    DeviceNull: int
    DeviceLogicalName: int
    DeviceLogicalRevision: int
    DevicePhysicalName: int
    DevicePhysicalRevision: int
    DeviceX: int
    DeviceY: int
    DeviceZ: int
    DeviceCustom: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedDeviceproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedLinesegmentproperties(Enum):
    """
    Members Include: 
     |LineNull| 
     |LineId| 
     |LineTcid| 
     |LineRacewayId| 
     |LineLength| 
     |LineIsPenetration| 
     |LineCustom| 

    """
    LineNull: int
    LineId: int
    LineTcid: int
    LineRacewayId: int
    LineLength: int
    LineIsPenetration: int
    LineCustom: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedLinesegmentproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedNodeproperties(Enum):
    """
    Members Include: 
     |NodeNull| 
     |NodeId| 
     |NodeX| 
     |NodeY| 
     |NodeZ| 
     |NodeIsInterface| 
     |NodeCustom| 

    """
    NodeNull: int
    NodeId: int
    NodeX: int
    NodeY: int
    NodeZ: int
    NodeIsInterface: int
    NodeCustom: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedNodeproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedObjecttypes(Enum):
    """
    Members Include: 
     |NoObject| 
     |Node| 
     |Device| 
     |LineSegment| 
     |Container| 

    """
    NoObject: int
    Node: int
    Device: int
    LineSegment: int
    Container: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedObjecttypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedRouteLengthupdatestate(Enum):
    """
    Members Include: 
     |NotSet| 
     |AlreadyUpToDate| 
     |Success| 
     |Error| 

    """
    NotSet: int
    AlreadyUpToDate: int
    Success: int
    Error: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedRouteLengthupdatestate:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedRouteValidationresult(Enum):
    """
    Members Include: 
     |NotSet| 
     |Valid| 
     |Warn| 
     |Error| 

    """
    NotSet: int
    Valid: int
    Warn: int
    Error: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedRouteValidationresult:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedSettingsBuilderRulevisibility(Enum):
    """
    Members Include: 
     |NotApplied| 
     |Visible| 
     |Invisible| 

    """
    NotApplied: int
    Visible: int
    Invisible: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedSettingsBuilderRulevisibility:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedSettingsNumericcomparison(Enum):
    """
    Members Include: 
     |NoComparison| 
     |LessThan| 
     |LessEqualThan| 
     |Equals| 
     |NotEquals| 
     |GreaterEqualThan| 
     |GreaterThan| 

    """
    NoComparison: int
    LessThan: int
    LessEqualThan: int
    Equals: int
    NotEquals: int
    GreaterEqualThan: int
    GreaterThan: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedSettingsNumericcomparison:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedSettingsStringcomparison(Enum):
    """
    Members Include: 
     |NotSet| 
     |Same| 
     |NotSame| 
     |Contains| 
     |DoesNotContain| 
     |ColorCode| 

    """
    NotSet: int
    Same: int
    NotSame: int
    Contains: int
    DoesNotContain: int
    ColorCode: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedSettingsStringcomparison:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedStructuralItemSelectionstate(Enum):
    """
    Members Include: 
     |NotSelected| 
     |PartiallySelected| 
     |Selected| 

    """
    NotSelected: int
    PartiallySelected: int
    Selected: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedStructuralItemSelectionstate:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterManagedVisibilityFrameSelectionstate(Enum):
    """
    Members Include: 
     |NotSelected| 
     |PartiallySelected| 
     |Selected| 

    """
    NotSelected: int
    PartiallySelected: int
    Selected: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterManagedVisibilityFrameSelectionstate:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CablewayAssemblyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.CablewayAssembly objects. """
    def FindObject(self, journalIdentifier: str) -> CablewayAssembly:
        """
         Finds the NXOpen.CableRouter.Managed.CablewayAssembly with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns cablewayAssembly ( CablewayAssembly NXOpen.Cable):  NXOpen.CableRouter.Managed.CablewayAssembly with this name. .
        """
        pass
import NXOpen
class CablewayAssembly(NXOpen.NXObject): 
    """ Represents the Cableway Assembly class. """
    pass
class Cable(BaseData): 
    """ Represents the physical and logical cables in the NX Cable Router application. """
    @property
    def EndDevice(self) -> Device:
        """
        Getter for property: ( Device NXOpen.Cable) EndDevice
         Returns the ending  NXOpen::CableRouter::Managed::Device  for this object  
            
         
        """
        pass
    @property
    def FromExtraLength(self) -> float:
        """
        Getter for property: (float) FromExtraLength
         Returns the from extra length  
            
         
        """
        pass
    @property
    def FromNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.Cable) FromNode
         Returns the from  NXOpen::CableRouter::Managed::Node  for this object  
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of the path  
            
         
        """
        pass
    @property
    def LengthCorrection(self) -> float:
        """
        Getter for property: (float) LengthCorrection
         Returns the length correction   
            
         
        """
        pass
    @property
    def LogicalID(self) -> str:
        """
        Getter for property: (str) LogicalID
         Returns the logical  NXOpen::CableRouter::Managed::Cable  identifier   
            
         
        """
        pass
    @property
    def MaximumLength(self) -> float:
        """
        Getter for property: (float) MaximumLength
         Returns the maximum length of the path  
            
         
        """
        pass
    @property
    def MinimumLength(self) -> float:
        """
        Getter for property: (float) MinimumLength
         Returns the minimum length of the path  
            
         
        """
        pass
    @property
    def RouteStatus(self) -> CableRouterManagedCableRoutestatus:
        """
        Getter for property: ( CableRouterManagedCableRoutestatus NXOpen.Cable) RouteStatus
         Returns the to route status for this object  
            
         
        """
        pass
    @property
    def StartDevice(self) -> Device:
        """
        Getter for property: ( Device NXOpen.Cable) StartDevice
         Returns the starting  NXOpen::CableRouter::Managed::Device  for this object   
            
         
        """
        pass
    @property
    def ToExtraLength(self) -> float:
        """
        Getter for property: (float) ToExtraLength
         Returns the to extra length  
            
         
        """
        pass
    @property
    def ToNode(self) -> Node:
        """
        Getter for property: ( Node NXOpen.Cable) ToNode
         Returns the to  NXOpen::CableRouter::Managed::Node  for this object  
            
         
        """
        pass
    def GetSegmentPaths(self) -> List[SegmentPath]:
        """
         This method returns NXOpen.CableRouter.Managed.SegmentPath set saved for this cable 
         Returns segmentPaths ( SegmentPath List[NXOpen.Cab): .
        """
        pass
import NXOpen
class ContainerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.Container objects. """
    def FindObject(self, journalIdentifier: str) -> Container:
        """
         Finds the NXOpen.CableRouter.Managed.Container with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns node ( Container NXOpen.Cable):  NXOpen.CableRouter.Managed.Container with this name. .
        """
        pass
class ContainerReference(BaseData): 
    """ Represents a reference to the NXOpen.CableRouter.Managed.Container class which may or may not be loaded. """
    @property
    def CablewayAssembly(self) -> CablewayAssembly:
        """
        Getter for property: ( CablewayAssembly NXOpen.Cable) CablewayAssembly
         Returns a reference for the  NXOpen::CableRouter::Managed::CablewayAssembly   of this reference    
            
         
        """
        pass
    @property
    def LineSegmentID(self) -> str:
        """
        Getter for property: (str) LineSegmentID
         Returns a string for the  NXOpen::CableRouter::Managed::LineSegment  id of this reference    
            
         
        """
        pass
    @property
    def LoadedContainer(self) -> Container:
        """
        Getter for property: ( Container NXOpen.Cable) LoadedContainer
         Returns the  NXOpen::CableRouter::Managed::Container  loaded in the current session.  
            This value may be null   
         
        """
        pass
    @property
    def TierID(self) -> str:
        """
        Getter for property: (str) TierID
         Returns a string for the  NXOpen::CableRouter::Managed::Container  tier id of this reference   
            
         
        """
        pass
import NXOpen
class Container(BaseData): 
    """ Represents the Container class. """
    @property
    def BendRadius(self) -> float:
        """
        Getter for property: (float) BendRadius
         Returns the bend radius in part units   
            
         
        """
        pass
    @property
    def CablewayType(self) -> str:
        """
        Getter for property: (str) CablewayType
         Returns the type name of the tray   
            
         
        """
        pass
    @property
    def FillRule(self) -> str:
        """
        Getter for property: (str) FillRule
         Returns the fill rule id of the tray  
            
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the tray in part units   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns a string for the ID   
            
         
        """
        pass
    @property
    def OwningLineSegment(self) -> LineSegment:
        """
        Getter for property: ( LineSegment NXOpen.Cable) OwningLineSegment
         Returns a reference for the owning  NXOpen::CableRouter::Managed::LineSegment     
            
         
        """
        pass
    @property
    def PermissibleWeight(self) -> float:
        """
        Getter for property: (float) PermissibleWeight
         Returns the permissible weight of the tray in part units   
            
         
        """
        pass
    @property
    def Weight(self) -> float:
        """
        Getter for property: (float) Weight
         Returns the weight of tray contents in part units   
            
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of the tray in part units   
            
         
        """
        pass
    def RetrieveCablePositions(self) -> Tuple[List[Cable], List[NXOpen.Point2d]]:
        """
         Retrieves the cross sectional NXOpen.CableRouter.Managed.Cable positions
         Returns A tuple consisting of (cables, position). 
         - cables is:  Cable List[NXOpen.Cab.
         - position is:  NXOpen.Point2d Li.

        """
        pass
    def RetrieveCrossSection(self) -> str:
        """
         Retrieves the cross sectional view as a SVG string
         Returns crossSectionViewSVG (str): .
        """
        pass
import NXOpen
class CopyRouteBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Copy Route operations. """
    @property
    def SelectDestinationCable(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectDestinationCable
         Returns the select destination  NXOpen::CableRouter::Managed::Cable  for the copy operation   
            
         
        """
        pass
    @property
    def SelectSourceCable(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectSourceCable
         Returns the select source  NXOpen::CableRouter::Managed::Cable  for the copy operation   
            
         
        """
        pass
import NXOpen
import NXOpen.PDM
class CreatePhysicalCableBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Create Physical Cable operations.
            """
    def SetObjectCreateBuilder(self, objectCreateBuilder: NXOpen.PDM.ObjectCreateBuilder) -> None:
        """
         Sets NXOpen.PDM.ObjectCreateBuilder 
        """
        pass
import NXOpen
class DesignContextBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Cable Router Design Context operations.
            """
    def GetDesignContextManaged(self) -> Tuple[str, str]:
        """
         Gets the managed mode design item context for the Design and Physical Roots.
         Returns A tuple consisting of (physicalContext, designContext). 
         - physicalContext is: str.
         - designContext is: str.

        """
        pass
    def SetDesignContextManaged(self, physicalContext: str, designContext: str) -> None:
        """
         Sets the managed mode design item context for the Design and Physical Roots.
        """
        pass
import NXOpen
class DeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.Device objects. """
    def FindObject(self, journalIdentifier: str) -> Device:
        """
         Finds the NXOpen.CableRouter.Managed.Device with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns node ( Device NXOpen.Cable):  NXOpen.CableRouter.Managed.Device with this name. .
        """
        pass
class Device(DisplayedBaseData): 
    """ Represents the electrical devices class. """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns a string for the ID   
            
         
        """
        pass
    def GetLocation(self) -> List[float]:
        """
         Retrieves the point for the location of this object 
         Returns location (List[float]): .
        """
        pass
    def GetShownPorts(self) -> List[Port]:
        """
         
                    Returns the shown ports 
                    
                    
                    
                    This method will return an empty array if the device ports are not instantiated.
                    Caller can instantiate device ports by method NXOpen.CableRouter.Managed.RoutingOperations.DisplayDevicePorts.
                     
         Returns shownPorts ( Port List[NXOpen.Cab): .
        """
        pass
class DisplayedBaseData(BaseData): 
    """ Represents the cable router objects drawn to screen. """
    @property
    def UserDefinedColor(self) -> int:
        """
        Getter for property: (int) UserDefinedColor
         Returns the color set by users  
            
         
        """
        pass
    @UserDefinedColor.setter
    def UserDefinedColor(self, userDefinedColor: int):
        """
        Setter for property: (int) UserDefinedColor
         Returns the color set by users  
            
         
        """
        pass
import NXOpen
class EditAutomaticRoutingBuilder(NXOpen.Builder): 
    """ Builder Class for Automatic Routing UI """
    class RoutingParameter(Enum):
        """
        Members Include: 
         |All| 
         |StartNode| 
         |EndNode| 
         |AllowOverfilling| 
         |MandatoryNodes| 
         |ProhibitedSegments| 

        """
        All: int
        StartNode: int
        EndNode: int
        AllowOverfilling: int
        MandatoryNodes: int
        ProhibitedSegments: int
        @staticmethod
        def ValueOf(value: int) -> EditAutomaticRoutingBuilder.RoutingParameter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowOverfilling(self) -> bool:
        """
        Getter for property: (bool) AllowOverfilling
         Returns the allow_overfilling toggle state.  
            
         
        """
        pass
    @AllowOverfilling.setter
    def AllowOverfilling(self, isAllowed: bool):
        """
        Setter for property: (bool) AllowOverfilling
         Returns the allow_overfilling toggle state.  
            
         
        """
        pass
    @property
    def EndNode(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) EndNode
         Returns the end  NXOpen::CableRouter::Managed::Node .  
            
         
        """
        pass
    @property
    def MandatoryNodes(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) MandatoryNodes
         Returns the mandatory  NXOpen::CableRouter::Managed::Node  objects that the path must pass through.  
            
         
        """
        pass
    @property
    def ProhibitedSegments(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) ProhibitedSegments
         Returns the prohibited  NXOpen::CableRouter::Managed::LineSegment  objects that the path must not pass through.  
            
         
        """
        pass
    @property
    def StartNode(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) StartNode
         Returns the start  NXOpen::CableRouter::Managed::Node .  
            
         
        """
        pass
    def ValidateBuilderUpToDate(self) -> bool:
        """
         Verifies the stored objects are up to date with Teamcenter 
         Returns isUpdated (bool): .
        """
        pass
import NXOpen
class EditCablePropertiesBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Edit Cable Properties operations.
            """
    @property
    def FromEndExtraLength(self) -> float:
        """
        Getter for property: (float) FromEndExtraLength
         Returns the from end extra length   
            
         
        """
        pass
    @FromEndExtraLength.setter
    def FromEndExtraLength(self, fromEndExtraLength: float):
        """
        Setter for property: (float) FromEndExtraLength
         Returns the from end extra length   
            
         
        """
        pass
    @property
    def LengthCorrectionFactor(self) -> float:
        """
        Getter for property: (float) LengthCorrectionFactor
         Returns the length correction factor   
            
         
        """
        pass
    @LengthCorrectionFactor.setter
    def LengthCorrectionFactor(self, lengthCorrectionFactor: float):
        """
        Setter for property: (float) LengthCorrectionFactor
         Returns the length correction factor   
            
         
        """
        pass
    @property
    def SelectFromNode(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectFromNode
         Returns the select from  NXOpen::CableRouter::Managed::Node    
            
         
        """
        pass
    @property
    def SelectToNode(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectToNode
         Returns the select to  NXOpen::CableRouter::Managed::Node    
            
         
        """
        pass
    @property
    def ToEndExtraLength(self) -> float:
        """
        Getter for property: (float) ToEndExtraLength
         Returns the to end extra length   
            
         
        """
        pass
    @ToEndExtraLength.setter
    def ToEndExtraLength(self, toEndExtraLength: float):
        """
        Setter for property: (float) ToEndExtraLength
         Returns the to end extra length   
            
         
        """
        pass
    def RestoreFromPortFromLogical(self) -> None:
        """
         Restore the from NXOpen.CableRouter.Managed.Port from the logical definition 
        """
        pass
    def RestoreToPortFromLogical(self) -> None:
        """
         Restore the to NXOpen.CableRouter.Managed.Port from the logical definition 
        """
        pass
import NXOpen
class EditEquipmentNodesBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Edit Equipment Nodes operations.
            """
    @property
    def SelectDevice(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectDevice
         Returns the select device   
            
         
        """
        pass
    @property
    def SelectEquipmentNodes(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectEquipmentNodes
         Returns the select equipment nodes   
            
         
        """
        pass
    @property
    def SelectPort(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectPort
         Returns the select port   
            
         
        """
        pass
import NXOpen
class Folder(NXOpen.NXObject): 
    """ Represents the Folder class. """
    def GetChildrenCables(self) -> List[Cable]:
        """
         Returns the children cables 
         Returns cables ( Cable List[NXOpen.Cab): .
        """
        pass
    def GetChildrenDevices(self) -> List[Device]:
        """
         Returns the children devices 
         Returns devices ( Device List[NXOpen.Cab): .
        """
        pass
import NXOpen
class LineSegmentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.LineSegment. """
    def FindObject(self, journalIdentifier: str) -> LineSegment:
        """
         Finds the NXOpen.CableRouter.Managed.LineSegment with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns node ( LineSegment NXOpen.Cable):  NXOpen.CableRouter.Managed.LineSegment with this name. .
        """
        pass
class LineSegment(DisplayedBaseData): 
    """ Represents the line segments connecting NXOpen.CableRouter.Managed.Node objects. """
    @property
    def EndObject(self) -> DisplayedBaseData:
        """
        Getter for property: ( DisplayedBaseData NXOpen.Cable) EndObject
         Returns the ending position of this object   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns a string for the ID   
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of this object   
            
         
        """
        pass
    @property
    def PenetrationFlag(self) -> str:
        """
        Getter for property: (str) PenetrationFlag
         Returns the flag for whether this object is a penetration   
            
         
        """
        pass
    @property
    def RacewayID(self) -> str:
        """
        Getter for property: (str) RacewayID
         Returns a string for the Raceway ID   
            
         
        """
        pass
    @property
    def StartObject(self) -> DisplayedBaseData:
        """
        Getter for property: ( DisplayedBaseData NXOpen.Cable) StartObject
         Returns the starting position of this object   
            
         
        """
        pass
    @property
    def TeamcenterID(self) -> str:
        """
        Getter for property: (str) TeamcenterID
         Returns a string for the Teamcenter ID   
            
         
        """
        pass
    def GetContainers(self) -> List[Container]:
        """
         Retrieves the set of NXOpen.CableRouter.Managed.Container objects that represent the trays of this segment 
         Returns containers ( Container List[NXOpen.Cab): .
        """
        pass
import NXOpen
class ManualRoutingBuilder(NXOpen.Builder): 
    """ Builder Class for Manual Routing operations to add and remove from a NXOpen.CableRouter.Managed.Cable path """
    def AddContainerToRoute(self, containerToAdd: Container) -> bool:
        """
          Adds the NXOpen.CableRouter.Managed.Container as the next part of the route. 
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def AddLineSegmentToRoute(self, lineToAdd: LineSegment) -> bool:
        """
         Adds the NXOpen.CableRouter.Managed.LineSegment as the next part of the route.
                     This will allow the system to chose the desired tier from the list of tiers within the NXOpen.CableRouter.Managed.LineSegment 
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def GetAvailableContainers(self) -> List[Container]:
        """
          Returns a set of NXOpen.CableRouter.Managed.Container that are available to add to the current NXOpen.CableRouter.Managed.Cable 
         Returns containers ( Container List[NXOpen.Cab): .
        """
        pass
    def GetRoutingFocus(self) -> Node:
        """
         Gets the NXOpen.CableRouter.Managed.Node as the point to continue routing from.
         Returns nodeToFocus ( Node NXOpen.Cable): .
        """
        pass
    def GetWorkInProgressContainers(self) -> List[Container]:
        """
          Returns a set of NXOpen.CableRouter.Managed.Container that are in the work in progress route of the current NXOpen.CableRouter.Managed.Cable 
         Returns containers ( Container List[NXOpen.Cab): .
        """
        pass
    def RemoveObjectsFromRoute(self, linesToRemove: List[LineSegment], containersToRemove: List[Container]) -> bool:
        """
          Removes the given NXOpen.CableRouter.Managed.LineSegment and NXOpen.CableRouter.Managed.Container from the route.
                    For the NXOpen.CableRouter.Managed.LineSegment, the NXOpen.CableRouter.Managed.LineSegment removed will be all 
                    NXOpen.CableRouter.Managed.Container that are part of the route
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def SetRoutingFocus(self, nodeToFocus: Node) -> bool:
        """
         Sets the NXOpen.CableRouter.Managed.Node as the point to continue routing from.
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def StartManualRouting(self) -> bool:
        """
         Call to activate this operation to start manually routing the stored NXOpen.CableRouter.Managed.Cable, only one cable can be routing at a time 
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def StopManualRouting(self) -> bool:
        """
         Call to activate this operation to stop manually routing the stored NXOpen.CableRouter.Managed.Cable 
         Returns wasUpdateTriggered (bool): .
        """
        pass
import NXOpen
class NodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.Node objects. """
    def FindObject(self, journalIdentifier: str) -> Node:
        """
         Finds the NXOpen.CableRouter.Managed.Node with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns node ( Node NXOpen.Cable):  NXOpen.CableRouter.Managed.Node with this name. .
        """
        pass
class Node(DisplayedBaseData): 
    """ Represents the points which exist in the NXOpen.CableRouter.Managed.CablewayAssembly class. """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns a string for the ID   
            
         
        """
        pass
    @property
    def InterfaceFlag(self) -> str:
        """
        Getter for property: (str) InterfaceFlag
         Returns a string for the ID   
            
         
        """
        pass
    def GetLocation(self) -> List[float]:
        """
         Retrieves the point for the location of this object 
         Returns location (List[float]): .
        """
        pass
class Port(DisplayedBaseData): 
    """ Represents the Port class. """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the string for the ID   
            
         
        """
        pass
    def GetEquipmentNodes(self) -> List[Node]:
        """
         Returns the equipment nodes 
         Returns equipmentNodes ( Node List[NXOpen.Cab): .
        """
        pass
    def GetLocation(self) -> List[float]:
        """
         Returns the location 
         Returns location (List[float]): .
        """
        pass
import NXOpen
class RoutingOperations(NXOpen.Object): 
    """ A collection of methods to trigger on routing operations """
    @property
    def PhysicalCableSaveLocation(self) -> StructuralItem:
        """
        Getter for property: ( StructuralItem NXOpen.Cable) PhysicalCableSaveLocation
         Returns  the locations for saving the  NXOpen::CableRouter::Managed::Cable  physical item  
            
         
        """
        pass
    @PhysicalCableSaveLocation.setter
    def PhysicalCableSaveLocation(self, saveLocation: StructuralItem):
        """
        Setter for property: ( StructuralItem NXOpen.Cable) PhysicalCableSaveLocation
         Returns  the locations for saving the  NXOpen::CableRouter::Managed::Cable  physical item  
            
         
        """
        pass
    def AcceptRoute(self, cableToAccept: Cable) -> None:
        """
          Accepts the work in progress route of the given NXOpen.CableRouter.Managed.Cable
        """
        pass
    def AddContainerToActiveRoute(self, containerToAdd: Container) -> bool:
        """
          Adds the NXOpen.CableRouter.Managed.Container to the current NXOpen.CableRouter.Managed.Cable.
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def AddLineToActiveRoute(self, lineToAdd: LineSegment) -> bool:
        """
          Adds the NXOpen.CableRouter.Managed.Container chosen by the system from the given NXOpen.CableRouter.Managed.LineSegment to the current NXOpen.CableRouter.Managed.Cable.
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def ChangeTier(self, cableToModify: Cable, currentSetContainer: Container, newTierID: str, isAllowedOverfilling: bool) -> None:
        """
         Modifies the path of the given NXOpen.CableRouter.Managed.Cable to change
                    the NXOpen.CableRouter.Managed.Container to the specified tier if part of its
                    parent NXOpen.CableRouter.Managed.LineSegment.
        """
        pass
    def CleanUpRoutes(self) -> None:
        """
          Clears any existing work in progress routes for any pending NXOpen.CableRouter.Managed.Cable
        """
        pass
    def ClearCableRoute(self, cables: List[Cable]) -> bool:
        """
          Clears the given set of NXOpen.CableRouter.Managed.Cable paths
         Returns updateTriggered (bool): .
        """
        pass
    def DisplayCableRoute(self, currentlyRoutingCable: Cable) -> None:
        """
          Displays the current NXOpen.CableRouter.Managed.Cable route stored.  Note, the active route will have priority over displaying cables.
        """
        pass
    def DisplayDevicePorts(self, currentlyEditingDevice: Device) -> None:
        """
          Displays the current NXOpen.CableRouter.Managed.Device ports stored.
        """
        pass
    def FitCable(self, cableToFitScreen: Cable) -> None:
        """
          Fits the view to the current NXOpen.CableRouter.Managed.Cable.
        """
        pass
    def GetActiveCableRouting(self) -> Cable:
        """
          Returns the current NXOpen.CableRouter.Managed.Cable that is being routed.  There may be nothing routing
         Returns currentlyRoutingCable ( Cable NXOpen.Cable): .
        """
        pass
    def GetActiveRouteAvailableContainers(self) -> List[Container]:
        """
          Returns a set of NXOpen.CableRouter.Managed.Container that are available to add to the current NXOpen.CableRouter.Managed.Cable 
         Returns containers ( Container List[NXOpen.Cab): .
        """
        pass
    def GetActiveRouteWorkInProgressContainers(self) -> List[Container]:
        """
          Returns a set of NXOpen.CableRouter.Managed.Container that are in the work in progress route of the current NXOpen.CableRouter.Managed.Cable 
         Returns containers ( Container List[NXOpen.Cab): .
        """
        pass
    def GetCablesNeedingApproval(self) -> List[Cable]:
        """
          Returns a set of NXOpen.CableRouter.Managed.Cable that are pending review of confirming its route
         Returns cablesPending ( Cable List[NXOpen.Cab): .
        """
        pass
    def GetLoadedObjectsCount(self) -> Tuple[int, int, int]:
        """
          Retrieves the count of objects currently loaded in the session
         Returns A tuple consisting of (nodeCount, lineSegmentCount, deviceCount). 
         - nodeCount is: int.
         - lineSegmentCount is: int.
         - deviceCount is: int.

        """
        pass
    def GetRootDesignStructuralItem(self) -> StructuralItem:
        """
          Retrieves the root NXOpen.CableRouter.Managed.StructuralItem for the design structure
         Returns rootDesignItem ( StructuralItem NXOpen.Cable): .
        """
        pass
    def GetRootPhysicalStructuralItem(self) -> StructuralItem:
        """
          Retrieves the root NXOpen.CableRouter.Managed.StructuralItem for the physical structure
         Returns rootPhysicalItem ( StructuralItem NXOpen.Cable): .
        """
        pass
    def GetRouteWorkInProgressContainers(self, cableToAsk: Cable) -> List[Container]:
        """
          Returns a set of NXOpen.CableRouter.Managed.Container that are in the work in progress route of the current NXOpen.CableRouter.Managed.Cable 
         Returns containers ( Container List[NXOpen.Cab): .
        """
        pass
    def HighlightLineSegments(self, selectedLineSegments: List[LineSegment]) -> None:
        """
          Highlights the current NXOpen.CableRouter.Managed.LineSegment line segments which are selected.
        """
        pass
    def InitializeWorkInProgress(self, cableToInitialize: Cable) -> bool:
        """
          Initializes the work in progress route of the given NXOpen.CableRouter.Managed.Cable
         Returns isUpdated (bool): .
        """
        pass
    def LoadVessel(self) -> None:
        """
          Loads the vessel with the currently selected breakdown
        """
        pass
    def QueryCables(self, objectToQuery: BaseData) -> List[Cable]:
        """
          Retrieves the set of NXOpen.CableRouter.Managed.Cable referencing the given set of NXOpen.CableRouter.Managed.BaseData
         Returns cables ( Cable List[NXOpen.Cab): .
        """
        pass
    def RefreshDisplay(self) -> None:
        """
          Refreshes the display of displayed datas which have user defined colors
        """
        pass
    def RejectRoute(self, cableToReject: Cable) -> bool:
        """
          Rejects the work in progress route of the given NXOpen.CableRouter.Managed.Cable
         Returns isUpdated (bool): .
        """
        pass
    def RemoveLinesFromActiveRoute(self, linesToRemove: List[LineSegment]) -> bool:
        """
          Removes all of the NXOpen.CableRouter.Managed.Container in the given NXOpen.CableRouter.Managed.LineSegment from the current NXOpen.CableRouter.Managed.Cable.
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def RemoveObjectsFromActiveRoute(self, linesToRemove: List[LineSegment], containersToRemove: List[Container]) -> bool:
        """
          Removes all of the NXOpen.CableRouter.Managed.Container and NXOpen.CableRouter.Managed.LineSegment from the current NXOpen.CableRouter.Managed.Cable.
         Returns wasUpdateTriggered (bool): .
        """
        pass
    def RenderWorkInProgressRoute(self, cableToRender: Cable) -> None:
        """
          Renders the work in progress route of the given NXOpen.CableRouter.Managed.Cable
        """
        pass
    def ResetDevice(self, cableToReset: Cable) -> None:
        """
         Reset devices of the given NXOpen.CableRouter.Managed.Cable. 
        """
        pass
    def RetrieveCrossSection(self, containerToQuery: Container) -> str:
        """
         Retrieves the cross sectional view of this container
         Returns crossSectionViewSVG (str): .
        """
        pass
    def RetrieveFillInformation(self, containersToQuery: List[Container]) -> List[CableRouterManagedContainerCalculatedproperties]:
        """
          Retrieve the set of fill informations of the given objects
         Returns fillPropertiesFound ( CableRouterManagedContainerCalculatedproperties List[NXOpen.Cab): .
        """
        pass
    def StartAutomaticRouting(self, cable: Cable) -> None:
        """
         Start Automatically Routing the stored NXOpen.CableRouter.Managed.Cable
        """
        pass
    def UnloadVessel(self) -> None:
        """
          Clear the currently loaded vessel
        """
        pass
    def UpdateLength(self, cableToUpdate: Cable) -> CableRouterManagedRouteLengthupdatestate:
        """
          Update the length of the given NXOpen.CableRouter.Managed.Cable. 
         Returns lengthUpdateState ( CableRouterManagedRouteLengthupdatestate NXOpen.Cable): .
        """
        pass
    def ValidateBaseDatasUpToDate(self, objectsToValidate: List[BaseData]) -> bool:
        """
          Validates that the given NXOpen.CableRouter.Managed.BaseData and its dependent objects are up to date
         Returns updateTriggered (bool): .
        """
        pass
    def ValidateCableRoute(self, cables: List[Cable]) -> Tuple[List[CableRouterManagedRouteValidationresult], List[str]]:
        """
          Validates the given set of NXOpen.CableRouter.Managed.Cable paths
         Returns A tuple consisting of (validationResults, errors). 
         - validationResults is:  CableRouterManagedRouteValidationresult List[NXOpen.Cab.
         - errors is: List[str].

        """
        pass
    def ValidateCablewayAssembliesUpToDate(self, objectsToValidate: List[CablewayAssembly]) -> bool:
        """
          Validates that the given NXOpen.CableRouter.Managed.CablewayAssembly and its dependent objects are up to date
         Returns updateTriggered (bool): .
        """
        pass
    def ValidateFillRules(self) -> Tuple[str, List[str]]:
        """
          Validates whether the fill rules were properly initialized
         Returns A tuple consisting of (filePath, missingFillRules). 
         - filePath is: str. The file found for the fill rules .
         - missingFillRules is: List[str]. The list of rule set names not properly assigned in the loaded data .

        """
        pass
    def ValidatePathUpToDate(self, cableToAccept: Cable) -> bool:
        """
          Validates that the given NXOpen.CableRouter.Managed.Cable and its dependent objects are up to date
         Returns updateTriggered (bool): .
        """
        pass
    def ValidateStructuralItemsUpToDate(self, objectsToValidate: List[StructuralItem]) -> bool:
        """
          Validates that the given NXOpen.CableRouter.Managed.StructuralItem and its dependent objects are up to date
         Returns updateTriggered (bool): .
        """
        pass
class SegmentPath(BaseData): 
    """ Represents a collection of NXOpen.CableRouter.Managed.ContainerReference for a continous path. """
    def GetContainerReferences(self) -> List[ContainerReference]:
        """
         This method returns the NXOpen.CableRouter.Managed.ContainerReference set for this object 
         Returns containerReferences ( ContainerReference List[NXOpen.Cab): .
        """
        pass
import NXOpen
class SettingsBuilder(NXOpen.Builder): 
    """ Builder class to modify the settings of the current session. """
    @property
    def AutomaticRouteColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AutomaticRouteColor
         Returns a set of values for the color of the  NXOpen::CableRouter::Managed::Cable  selected by the automatic route process  
            
         
        """
        pass
    @AutomaticRouteColor.setter
    def AutomaticRouteColor(self, automaticCableSelectionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AutomaticRouteColor
         Returns a set of values for the color of the  NXOpen::CableRouter::Managed::Cable  selected by the automatic route process  
            
         
        """
        pass
    @property
    def AvailableColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AvailableColor
         Returns the color of an available  NXOpen::CableRouter::Managed::LineSegment   
            
         
        """
        pass
    @AvailableColor.setter
    def AvailableColor(self, availableColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AvailableColor
         Returns the color of an available  NXOpen::CableRouter::Managed::LineSegment   
            
         
        """
        pass
    @property
    def BasicDisplayProperties(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) BasicDisplayProperties
         Returns a set of values for color, width, and line font of the nodal network   
            
         
        """
        pass
    @property
    def CableSelectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CableSelectionColor
         Returns a set of values for the color of the selected  NXOpen::CableRouter::Managed::Cable   
            
         
        """
        pass
    @CableSelectionColor.setter
    def CableSelectionColor(self, cableSelectionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CableSelectionColor
         Returns a set of values for the color of the selected  NXOpen::CableRouter::Managed::Cable   
            
         
        """
        pass
    @property
    def EndObjectColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) EndObjectColor
         Returns the color for end objects  
            
         
        """
        pass
    @EndObjectColor.setter
    def EndObjectColor(self, endObjectColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) EndObjectColor
         Returns the color for end objects  
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name of the data set from the native file system  
            
         
        """
        pass
    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file name of the data set from the native file system  
            
         
        """
        pass
    @property
    def LabelFontSize(self) -> float:
        """
        Getter for property: (float) LabelFontSize
         Returns a number for the font size of the nodal network labels  
            
         
        """
        pass
    @LabelFontSize.setter
    def LabelFontSize(self, selectionColor: float):
        """
        Setter for property: (float) LabelFontSize
         Returns a number for the font size of the nodal network labels  
            
         
        """
        pass
    @property
    def LabelTextProperties(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) LabelTextProperties
         Returns a set of values for color, width, and font of the nodal network labels   
            
         
        """
        pass
    @property
    def LayerNumber(self) -> int:
        """
        Getter for property: (int) LayerNumber
         Returns a number for the layer to draw the generated objects  
            
         
        """
        pass
    @LayerNumber.setter
    def LayerNumber(self, layerNumber: int):
        """
        Setter for property: (int) LayerNumber
         Returns a number for the layer to draw the generated objects  
            
         
        """
        pass
    @property
    def LimitDevicesShown(self) -> bool:
        """
        Getter for property: (bool) LimitDevicesShown
         Returns a flag for whether the amount of  NXOpen::CableRouter::Managed::Device  drawn to screen should be limited   
            
         
        """
        pass
    @LimitDevicesShown.setter
    def LimitDevicesShown(self, shouldObjectsBeLimited: bool):
        """
        Setter for property: (bool) LimitDevicesShown
         Returns a flag for whether the amount of  NXOpen::CableRouter::Managed::Device  drawn to screen should be limited   
            
         
        """
        pass
    @property
    def LimitLabelsShown(self) -> bool:
        """
        Getter for property: (bool) LimitLabelsShown
         Returns a flag for whether the amount of labels drawn to screen should be limited   
            
         
        """
        pass
    @LimitLabelsShown.setter
    def LimitLabelsShown(self, shouldObjectsBeLimited: bool):
        """
        Setter for property: (bool) LimitLabelsShown
         Returns a flag for whether the amount of labels drawn to screen should be limited   
            
         
        """
        pass
    @property
    def LimitNodesShown(self) -> bool:
        """
        Getter for property: (bool) LimitNodesShown
         Returns a flag for whether the amount of  NXOpen::CableRouter::Managed::Node  drawn to screen should be limited   
            
         
        """
        pass
    @LimitNodesShown.setter
    def LimitNodesShown(self, shouldObjectsBeLimited: bool):
        """
        Setter for property: (bool) LimitNodesShown
         Returns a flag for whether the amount of  NXOpen::CableRouter::Managed::Node  drawn to screen should be limited   
            
         
        """
        pass
    @property
    def MaxDevicesShown(self) -> int:
        """
        Getter for property: (int) MaxDevicesShown
         Returns a number for max number of  NXOpen::CableRouter::Managed::Device  to draw  
            
         
        """
        pass
    @MaxDevicesShown.setter
    def MaxDevicesShown(self, numberOfDevices: int):
        """
        Setter for property: (int) MaxDevicesShown
         Returns a number for max number of  NXOpen::CableRouter::Managed::Device  to draw  
            
         
        """
        pass
    @property
    def MaxLabelsShown(self) -> int:
        """
        Getter for property: (int) MaxLabelsShown
         Returns a number for max number of labels to draw  
            
         
        """
        pass
    @MaxLabelsShown.setter
    def MaxLabelsShown(self, numberOfLabels: int):
        """
        Setter for property: (int) MaxLabelsShown
         Returns a number for max number of labels to draw  
            
         
        """
        pass
    @property
    def MaxNodesShown(self) -> int:
        """
        Getter for property: (int) MaxNodesShown
         Returns a number for max number of  NXOpen::CableRouter::Managed::Node  to draw  
            
         
        """
        pass
    @MaxNodesShown.setter
    def MaxNodesShown(self, numberOfNode: int):
        """
        Setter for property: (int) MaxNodesShown
         Returns a number for max number of  NXOpen::CableRouter::Managed::Node  to draw  
            
         
        """
        pass
    @property
    def ShowDeviceLabels(self) -> bool:
        """
        Getter for property: (bool) ShowDeviceLabels
         Returns a flag for whether  NXOpen::CableRouter::Managed::Device  labels are displayed   
            
         
        """
        pass
    @ShowDeviceLabels.setter
    def ShowDeviceLabels(self, showDeviceLabels: bool):
        """
        Setter for property: (bool) ShowDeviceLabels
         Returns a flag for whether  NXOpen::CableRouter::Managed::Device  labels are displayed   
            
         
        """
        pass
    @property
    def ShowDevices(self) -> bool:
        """
        Getter for property: (bool) ShowDevices
         Returns a flag for whether  NXOpen::CableRouter::Managed::Device  are displayed   
            
         
        """
        pass
    @ShowDevices.setter
    def ShowDevices(self, showDevices: bool):
        """
        Setter for property: (bool) ShowDevices
         Returns a flag for whether  NXOpen::CableRouter::Managed::Device  are displayed   
            
         
        """
        pass
    @property
    def ShowNodeLabels(self) -> bool:
        """
        Getter for property: (bool) ShowNodeLabels
         Returns a flag for whether  NXOpen::CableRouter::Managed::Node  labels are displayed   
            
         
        """
        pass
    @ShowNodeLabels.setter
    def ShowNodeLabels(self, showNodeLabels: bool):
        """
        Setter for property: (bool) ShowNodeLabels
         Returns a flag for whether  NXOpen::CableRouter::Managed::Node  labels are displayed   
            
         
        """
        pass
    @property
    def ShowNodes(self) -> bool:
        """
        Getter for property: (bool) ShowNodes
         Returns a flag for whether  NXOpen::CableRouter::Managed::Node  are displayed   
            
         
        """
        pass
    @ShowNodes.setter
    def ShowNodes(self, showNodes: bool):
        """
        Setter for property: (bool) ShowNodes
         Returns a flag for whether  NXOpen::CableRouter::Managed::Node  are displayed   
            
         
        """
        pass
    @property
    def ShowSegmentLabels(self) -> bool:
        """
        Getter for property: (bool) ShowSegmentLabels
         Returns a flag for whether  NXOpen::CableRouter::Managed::LineSegment  labels are displayed   
            
         
        """
        pass
    @ShowSegmentLabels.setter
    def ShowSegmentLabels(self, showSegmentLabels: bool):
        """
        Setter for property: (bool) ShowSegmentLabels
         Returns a flag for whether  NXOpen::CableRouter::Managed::LineSegment  labels are displayed   
            
         
        """
        pass
    @property
    def ShowSegments(self) -> bool:
        """
        Getter for property: (bool) ShowSegments
         Returns a flag for whether  NXOpen::CableRouter::Managed::LineSegment  are displayed   
            
         
        """
        pass
    @ShowSegments.setter
    def ShowSegments(self, showSegments: bool):
        """
        Setter for property: (bool) ShowSegments
         Returns a flag for whether  NXOpen::CableRouter::Managed::LineSegment  are displayed   
            
         
        """
        pass
    @property
    def StartObjectColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) StartObjectColor
         Returns the color for start objects  
            
         
        """
        pass
    @StartObjectColor.setter
    def StartObjectColor(self, startObjectColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) StartObjectColor
         Returns the color for start objects  
            
         
        """
        pass
    def LoadFromJSON(self, json: str) -> None:
        """
         Loads the rules and rule sets from the provided json string
        """
        pass
import NXOpen
class StructuralItemCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CableRouter.Managed.StructuralItem. """
    def FindObject(self, journalIdentifier: str) -> StructuralItem:
        """
         Finds the NXOpen.CableRouter.Managed.StructuralItem with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns node ( StructuralItem NXOpen.Cable):  NXOpen.CableRouter.Managed.StructuralItem with this name. .
        """
        pass
import NXOpen
class StructuralItem(NXOpen.NXObject): 
    """ Represents the items shown in Cable Router navigators. """
    @property
    def HasChildren(self) -> bool:
        """
        Getter for property: (bool) HasChildren
         Returns whether the  NXOpen::CableRouter::Managed::StructuralItem   has any items belonging to it  
            
         
        """
        pass
    @property
    def HasChildrenCables(self) -> bool:
        """
        Getter for property: (bool) HasChildrenCables
         Returns whether the  NXOpen::CableRouter::Managed::StructuralItem   has any cables belonging to it  
            
         
        """
        pass
    @property
    def HasChildrenDevices(self) -> bool:
        """
        Getter for property: (bool) HasChildrenDevices
         Returns whether the  NXOpen::CableRouter::Managed::StructuralItem   has any devices belonging to it  
            
         
        """
        pass
    @property
    def Parent(self) -> StructuralItem:
        """
        Getter for property: ( StructuralItem NXOpen.Cable) Parent
         Returns the  NXOpen::CableRouter::Managed::StructuralItem   this items belongs to  
            
         
        """
        pass
    @property
    def SelectionState(self) -> CableRouterManagedStructuralItemSelectionstate:
        """
        Getter for property: ( CableRouterManagedStructuralItemSelectionstate NXOpen.Cable) SelectionState
         Returns whether the  NXOpen::CableRouter::Managed::StructuralItem   is fully, partially, or not selected to load  
            
         
        """
        pass
    def AreChildrenExpanded(self) -> bool:
        """
         Returns if the NXOpen.CableRouter.Managed.StructuralItem  children are created 
         Returns areChildrenExpanded (bool): .
        """
        pass
    def ExpandChildren(self) -> None:
        """
         Expands the NXOpen.CableRouter.Managed.StructuralItem  children if necessary 
        """
        pass
    def ExpandGrandchildren(self) -> None:
        """
         Expands the NXOpen.CableRouter.Managed.StructuralItem  grandchildren if necessary 
        """
        pass
    def GetChildFolders(self) -> List[Folder]:
        """
         Returns the NXOpen.CableRouter.Managed.Folder  belonging to this object 
         Returns folders ( Folder List[NXOpen.Cab): .
        """
        pass
    def GetChildrenCables(self) -> List[Cable]:
        """
         Returns the NXOpen.CableRouter.Managed.Cable  belonging to this object 
         Returns items ( Cable List[NXOpen.Cab): .
        """
        pass
    def GetChildrenDevices(self) -> List[Device]:
        """
         Returns the NXOpen.CableRouter.Managed.Device belonging to this object 
         Returns items ( Device List[NXOpen.Cab): .
        """
        pass
    def GetChildrenItems(self) -> List[StructuralItem]:
        """
         Returns the NXOpen.CableRouter.Managed.StructuralItem  belonging to this object 
         Returns items ( StructuralItem List[NXOpen.Cab): .
        """
        pass
    def ToggleSelectionState(self) -> List[StructuralItem]:
        """
         Toggles the selection state of the NXOpen.CableRouter.Managed.StructuralItem  object 
         Returns itemsEffected ( StructuralItem List[NXOpen.Cab): .
        """
        pass
