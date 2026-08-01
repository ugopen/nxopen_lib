from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class CableRouterCableSettingsDeviceproperties(Enum):
    """
    Members Include: 
     |DeviceNull| 
     |DeviceArea| 
     |DeviceDescription| 
     |DeviceId| 
     |DeviceX| 
     |DeviceY| 
     |DeviceZ| 
     |DeviceNearNode| 
     |DeviceApplicability| 

    """
    DeviceNull: int
    DeviceArea: int
    DeviceDescription: int
    DeviceId: int
    DeviceX: int
    DeviceY: int
    DeviceZ: int
    DeviceNearNode: int
    DeviceApplicability: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterCableSettingsDeviceproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterCableSettingsLinesegmentproperties(Enum):
    """
    Members Include: 
     |LineNull| 
     |LineFill| 
     |LineFromArea| 
     |LineFromNode| 
     |LineId| 
     |LineLength| 
     |LineNrType| 
     |LineReason| 
     |LineSecondary| 
     |LineSegregation| 
     |LineThreshold| 
     |LineTierId| 
     |LineToArea| 
     |LineToNode| 
     |LineFillCalc| 
     |LineHeight| 
     |LineLocked| 
     |LinePenetration| 
     |LinePointSeg| 
     |LineWidth| 
     |LineApplicability| 
     |LineTierCount| 
     |LineCategory| 
     |LineCableStatus| 
     |LineWeightFill| 
     |LineWeightThreshhold| 

    """
    LineNull: int
    LineFill: int
    LineFromArea: int
    LineFromNode: int
    LineId: int
    LineLength: int
    LineNrType: int
    LineReason: int
    LineSecondary: int
    LineSegregation: int
    LineThreshold: int
    LineTierId: int
    LineToArea: int
    LineToNode: int
    LineFillCalc: int
    LineHeight: int
    LineLocked: int
    LinePenetration: int
    LinePointSeg: int
    LineWidth: int
    LineApplicability: int
    LineTierCount: int
    LineCategory: int
    LineCableStatus: int
    LineWeightFill: int
    LineWeightThreshhold: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterCableSettingsLinesegmentproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterCableSettingsNodeproperties(Enum):
    """
    Members Include: 
     |NodeNull| 
     |NodeArea| 
     |NodeId| 
     |NodeMajor| 
     |NodeX| 
     |NodeY| 
     |NodeZ| 
     |NodeApplicability| 

    """
    NodeNull: int
    NodeArea: int
    NodeId: int
    NodeMajor: int
    NodeX: int
    NodeY: int
    NodeZ: int
    NodeApplicability: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterCableSettingsNodeproperties:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterCableSettingsNumericcomparison(Enum):
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
    def ValueOf(value: int) -> CableRouterCableSettingsNumericcomparison:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterCableSettingsObjecttypes(Enum):
    """
    Members Include: 
     |NoObject| 
     |Node| 
     |Device| 
     |LineSegment| 

    """
    NoObject: int
    Node: int
    Device: int
    LineSegment: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterCableSettingsObjecttypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterCableSettingsStringcomparison(Enum):
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
    def ValueOf(value: int) -> CableRouterCableSettingsStringcomparison:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CableRouter.Managed
class CableRouterCollection(NXOpen.Object): 
    """ JA Collection object for containing CableRouter Builders """
    def CreateAutomaticRoutingBuilder(part: NXOpen.Part, cableBeingRouted: List[NXOpen.CableRouter.Managed.Cable]) -> NXOpen.CableRouter.Managed.AutomaticRoutingBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.AutomaticRoutingBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.AutomaticRoutingBuilder): .
        """
        pass
    def CreateEditAutomaticRoutingBuilder(part: NXOpen.Part, cableBeingRouted: List[NXOpen.CableRouter.Managed.Cable], parameterToEdit: NXOpen.CableRouter.Managed.EditAutomaticRoutingBuilder.RoutingParameter) -> NXOpen.CableRouter.Managed.EditAutomaticRoutingBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.EditAutomaticRoutingBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.EditAutomaticRoutingBuilder): .
        """
        pass
    def CreateManagedCopyRouteBuilder(part: NXOpen.Part, sourceCable: NXOpen.CableRouter.Managed.Cable) -> NXOpen.CableRouter.Managed.CopyRouteBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.CopyRouteBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.CopyRouteBuilder): .
        """
        pass
    def CreateManagedCreatePhysicalCableBuilder(part: NXOpen.Part, cableToAddPhysical: NXOpen.CableRouter.Managed.Cable) -> NXOpen.CableRouter.Managed.CreatePhysicalCableBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.CreatePhysicalCableBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.CreatePhysicalCableBuilder): .
        """
        pass
    def CreateManagedDesignContextBuilder(part: NXOpen.Part) -> NXOpen.CableRouter.Managed.DesignContextBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.DesignContextBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.DesignContextBuilder): .
        """
        pass
    def CreateManagedEditCablePropertiesBuilder(part: NXOpen.Part, cableBeingEdited: NXOpen.CableRouter.Managed.Cable) -> NXOpen.CableRouter.Managed.EditCablePropertiesBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.EditCablePropertiesBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.EditCablePropertiesBuilder): .
        """
        pass
    def CreateManagedEditEquipmentNodesBuilder(part: NXOpen.Part, deviceBeingEdited: NXOpen.CableRouter.Managed.Device) -> NXOpen.CableRouter.Managed.EditEquipmentNodesBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.EditEquipmentNodesBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.EditEquipmentNodesBuilder): .
        """
        pass
    def CreateManagedSettingsBuilder(part: NXOpen.Part) -> NXOpen.CableRouter.Managed.SettingsBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.SettingsBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.SettingsBuilder): .
        """
        pass
    def CreateManualRoutingBuilder(part: NXOpen.Part, cableBeingRouted: NXOpen.CableRouter.Managed.Cable) -> NXOpen.CableRouter.Managed.ManualRoutingBuilder:
        """
         Creates a NXOpen.CableRouter.Managed.ManualRoutingBuilder 
         Returns builder ( NXOpen.CableRouter.Managed.ManualRoutingBuilder): .
        """
        pass
import NXOpen
class CableRouterManager(NXOpen.Object): 
    """ Represents a NXOpen.CableRouter.CableRouterManager object.
     """
    @property
    def CableRouterCollection() -> CableRouterCollection:
        """
          Returns a  NXOpen::CableRouter::CableRouterCollection  object.
                
        """
        pass
    @property
    def VisibilityFrameManager() -> VisibilityFrameManager:
        """
         This is an internal API and can be changed at any time 
        """
        pass
class CableRouterVisibilityFramePrimarysecondary(Enum):
    """
    Members Include: 
     |Primary| 
     |Secondary| 
     |Both| 

    """
    Primary: int
    Secondary: int
    Both: int
    @staticmethod
    def ValueOf(value: int) -> CableRouterVisibilityFramePrimarysecondary:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CableRouterVisibilityFrameSelectionstate(Enum):
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
    def ValueOf(value: int) -> CableRouterVisibilityFrameSelectionstate:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CableRouter.Managed
class ObjectManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    @property
    def Nodes() -> NXOpen.CableRouter.Managed.NodeCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::NodeCollection   belonging to this part 
        """
        pass
    @property
    def Devices() -> NXOpen.CableRouter.Managed.DeviceCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::DeviceCollection   belonging to this part 
        """
        pass
    @property
    def LineSegments() -> NXOpen.CableRouter.Managed.LineSegmentCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::LineSegmentCollection   belonging to this part 
        """
        pass
    @property
    def Cables() -> NXOpen.CableRouter.Managed.CableCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::CableCollection   belonging to this part 
        """
        pass
    @property
    def Containers() -> NXOpen.CableRouter.Managed.ContainerCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::ContainerCollection   belonging to this part 
        """
        pass
    @property
    def Ports() -> NXOpen.CableRouter.Managed.PortCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    @property
    def RoutingOperations() -> NXOpen.CableRouter.Managed.RoutingOperations:
        """
         Returns the  NXOpen::CableRouter::Managed::RoutingOperations   belonging to this part 
        """
        pass
    @property
    def StructuralItems() -> NXOpen.CableRouter.Managed.StructuralItemCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::StructuralItem   belonging to this part 
        """
        pass
    @property
    def CablewayAssemblies() -> NXOpen.CableRouter.Managed.CablewayAssemblyCollection:
        """
         Returns the  NXOpen::CableRouter::Managed::CablewayAssembly   belonging to this part 
        """
        pass
