from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AccessorEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates an object based on a property value or an index """
    class AccessType(Enum):
        """
        Members Include: 
         |Property| 
         |Index| 

        """
        Property: int
        Index: int
        @staticmethod
        def ValueOf(value: int) -> AccessorEvaluatorBuilder.AccessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositionTypeValue(Enum):
        """
        Members Include: 
         |Begin| 
         |End| 
         |Index| 

        """
        Begin: int
        End: int
        Index: int
        @staticmethod
        def ValueOf(value: int) -> AccessorEvaluatorBuilder.PositionTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AccessTypeValue(self) -> AccessorEvaluatorBuilder.AccessType:
        """
        Getter for property: ( AccessorEvaluatorBuilder.AccessType NXOp) AccessTypeValue
         Returns the access type   
            
         
        """
        pass
    @AccessTypeValue.setter
    def AccessTypeValue(self, accessType: AccessorEvaluatorBuilder.AccessType):
        """
        Setter for property: ( AccessorEvaluatorBuilder.AccessType NXOp) AccessTypeValue
         Returns the access type   
            
         
        """
        pass
    @property
    def CompareValue(self) -> str:
        """
        Getter for property: (str) CompareValue
         Returns the comparative value given by user   
            
         
        """
        pass
    @CompareValue.setter
    def CompareValue(self, compareValue: str):
        """
        Setter for property: (str) CompareValue
         Returns the comparative value given by user   
            
         
        """
        pass
    @property
    def ObjectPosition(self) -> int:
        """
        Getter for property: (int) ObjectPosition
         Returns the object index value given by the user   
            
         
        """
        pass
    @ObjectPosition.setter
    def ObjectPosition(self, objectPosition: int):
        """
        Setter for property: (int) ObjectPosition
         Returns the object index value given by the user   
            
         
        """
        pass
    @property
    def PositionValue(self) -> AccessorEvaluatorBuilder.PositionTypeValue:
        """
        Getter for property: ( AccessorEvaluatorBuilder.PositionTypeValue NXOp) PositionValue
         Returns the position value given by the user   
            
         
        """
        pass
    @PositionValue.setter
    def PositionValue(self, positionValue: AccessorEvaluatorBuilder.PositionTypeValue):
        """
        Setter for property: ( AccessorEvaluatorBuilder.PositionTypeValue NXOp) PositionValue
         Returns the position value given by the user   
            
         
        """
        pass
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the property name given by the user   
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the property name given by the user   
            
         
        """
        pass
import NXOpen
class AddEplanPropertyBuilder(NXOpen.Builder): 
    """ Class to add new Eplan property to Eplan productfunction template node."""
    @property
    def PropertySelection(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) PropertySelection
         Returns the Target node selection   
            
         
        """
        pass
    def SetParent(self, parentEplanNode: AMEBaseNode) -> None:
        """
         Set the parent Eplan node. 
        """
        pass
import NXOpen
class AddEplanValueSetBuilder(NXOpen.Builder): 
    """ Represents a value set creation class Builder  """
    @property
    def SelectEplanMacro(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectEplanMacro
         Returns the selected engineering object   
            
         
        """
        pass
import NXOpen
class AddPlaceholderBuilder(NXOpen.Builder): 
    """ the builder for adding placeholder """
    class Category(Enum):
        """
        Members Include: 
         |Objects| 
         |ObjectPortsA| 
         |ObjectPortsB| 
         |ObjectParents| 
         |Connections| 
         |ConnectionParents| 
         |ConnectionsA| 
         |ConnectionParentsA| 
         |ConnectionsB| 
         |ConnectionParentsB| 
         |Sources| 
         |SourcePorts| 
         |SourceParents| 
         |Targets| 
         |TargetPorts| 
         |TargetParents| 
         |TargetsA| 
         |TargetPortsA| 
         |TargetParentsA| 
         |TargetsB| 
         |TargetPortsB| 
         |TargetParentsB| 
         |Placeholder| 
         |MatrixConnectionsA| 
         |MatrixConnectionsB| 
         |MatrixConnectionParentsA| 
         |MatrixConnectionParentsB| 
         |MatrixPlaceholder| 

        """
        Objects: int
        ObjectPortsA: int
        ObjectPortsB: int
        ObjectParents: int
        Connections: int
        ConnectionParents: int
        ConnectionsA: int
        ConnectionParentsA: int
        ConnectionsB: int
        ConnectionParentsB: int
        Sources: int
        SourcePorts: int
        SourceParents: int
        Targets: int
        TargetPorts: int
        TargetParents: int
        TargetsA: int
        TargetPortsA: int
        TargetParentsA: int
        TargetsB: int
        TargetPortsB: int
        TargetParentsB: int
        Placeholder: int
        MatrixConnectionsA: int
        MatrixConnectionsB: int
        MatrixConnectionParentsA: int
        MatrixConnectionParentsB: int
        MatrixPlaceholder: int
        @staticmethod
        def ValueOf(value: int) -> AddPlaceholderBuilder.Category:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContentPropertyType(Enum):
        """
        Members Include: 
         |Value| 
         |Sum| 

        """
        Value: int
        Sum: int
        @staticmethod
        def ValueOf(value: int) -> AddPlaceholderBuilder.ContentPropertyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Flp(Enum):
        """
        Members Include: 
         |Function| 
         |Location| 
         |Product| 
         |Automation| 

        """
        Function: int
        Location: int
        Product: int
        Automation: int
        @staticmethod
        def ValueOf(value: int) -> AddPlaceholderBuilder.Flp:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Property(Enum):
        """
        Members Include: 
         |Type| 
         |Product| 
         |ProductOrType| 
         |General| 
         |Aspect| 
         |Page| 
         |Tag| 

        """
        Type: int
        Product: int
        ProductOrType: int
        General: int
        Aspect: int
        Page: int
        Tag: int
        @staticmethod
        def ValueOf(value: int) -> AddPlaceholderBuilder.Property:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CategorySelector(self) -> AddPlaceholderBuilder.Category:
        """
        Getter for property: ( AddPlaceholderBuilder.Category NXOp) CategorySelector
         Returns the select category   
            
         
        """
        pass
    @CategorySelector.setter
    def CategorySelector(self, categoryValue: AddPlaceholderBuilder.Category):
        """
        Setter for property: ( AddPlaceholderBuilder.Category NXOp) CategorySelector
         Returns the select category   
            
         
        """
        pass
    @property
    def FLPSelector(self) -> AddPlaceholderBuilder.Flp:
        """
        Getter for property: ( AddPlaceholderBuilder.Flp NXOp) FLPSelector
         Returns the select flp   
            
         
        """
        pass
    @FLPSelector.setter
    def FLPSelector(self, flpValue: AddPlaceholderBuilder.Flp):
        """
        Setter for property: ( AddPlaceholderBuilder.Flp NXOp) FLPSelector
         Returns the select flp   
            
         
        """
        pass
    @property
    def PropertySelector(self) -> AddPlaceholderBuilder.Property:
        """
        Getter for property: ( AddPlaceholderBuilder.Property NXOp) PropertySelector
         Returns the select property   
            
         
        """
        pass
    @PropertySelector.setter
    def PropertySelector(self, propertyValue: AddPlaceholderBuilder.Property):
        """
        Setter for property: ( AddPlaceholderBuilder.Property NXOp) PropertySelector
         Returns the select property   
            
         
        """
        pass
    @property
    def SelectClassification(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the select classification builder   
            
         
        """
        pass
    @SelectClassification.setter
    def SelectClassification(self, selectClassification: SelectClassificationBuilder):
        """
        Setter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the select classification builder   
            
         
        """
        pass
    @property
    def SelectLibraryObject(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectLibraryObject
         Returns the select library object  
            
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
class AddPlcOperatorBuilder(AMEBaseBuilder): 
    """ Represents builder for the Add Plc Operator Object """
    @property
    def OperatorType(self) -> PlcLogicBlockNodeType:
        """
        Getter for property: ( PlcLogicBlockNodeType NXOp) OperatorType
         Returns the operator type for logic block   
            
         
        """
        pass
    @OperatorType.setter
    def OperatorType(self, operatorType: PlcLogicBlockNodeType):
        """
        Setter for property: ( PlcLogicBlockNodeType NXOp) OperatorType
         Returns the operator type for logic block   
            
         
        """
        pass
    def CreatePlcLogicBlockOperator(self) -> NXOpen.Diagramming.Node:
        """
         Create Plc Logic Block Operator
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetPlacementLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set node location of operator on the sheet. 
        """
        pass
import NXOpen
class AddPropertyColumnBuilder(NXOpen.Builder): 
    """ Represents configure result table class builder """
    class ParentObjectTypes(Enum):
        """
        Members Include: 
         |Function| 
         |Location| 
         |Product| 
         |Automation| 

        """
        Function: int
        Location: int
        Product: int
        Automation: int
        @staticmethod
        def ValueOf(value: int) -> AddPropertyColumnBuilder.ParentObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Objects| 
         |Targets| 
         |Sources| 
         |Connections| 
         |ObjectPorts| 
         |TargetPorts| 
         |SourcePorts| 
         |ObjectParents| 
         |TargetParents| 
         |SourceParents| 
         |ConnectionParents| 

        """
        Objects: int
        Targets: int
        Sources: int
        Connections: int
        ObjectPorts: int
        TargetPorts: int
        SourcePorts: int
        ObjectParents: int
        TargetParents: int
        SourceParents: int
        ConnectionParents: int
        @staticmethod
        def ValueOf(value: int) -> AddPropertyColumnBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ParentObjectType(self) -> AddPropertyColumnBuilder.ParentObjectTypes:
        """
        Getter for property: ( AddPropertyColumnBuilder.ParentObjectTypes NXOp) ParentObjectType
         Returns the Parent Object Type   
            
         
        """
        pass
    @ParentObjectType.setter
    def ParentObjectType(self, type: AddPropertyColumnBuilder.ParentObjectTypes):
        """
        Setter for property: ( AddPropertyColumnBuilder.ParentObjectTypes NXOp) ParentObjectType
         Returns the Parent Object Type   
            
         
        """
        pass
    @property
    def PropertyOf(self) -> AddPropertyColumnBuilder.Types:
        """
        Getter for property: ( AddPropertyColumnBuilder.Types NXOp) PropertyOf
         Returns the Property Of type   
            
         
        """
        pass
    @PropertyOf.setter
    def PropertyOf(self, type: AddPropertyColumnBuilder.Types):
        """
        Setter for property: ( AddPropertyColumnBuilder.Types NXOp) PropertyOf
         Returns the Property Of type   
            
         
        """
        pass
    def Add(self, propertyOf: str, groupName: str, propertyName: str) -> None:
        """
         The action to add properties 
        """
        pass
class AddressObjectIotype(Enum):
    """
    Members Include: 
     |Empty| 
     |Input| 
     |Output| 

    """
    Empty: int
    Input: int
    Output: int
    @staticmethod
    def ValueOf(value: int) -> AddressObjectIotype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Tooling
class AddressRuleSettingsBuilder(NXOpen.Builder): 
    """ Assign default plc address rule set"""
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library selection item  
            
         
        """
        pass
import NXOpen
class ADPropertyData(NXOpen.NXObject): 
    """ AD Property Data class """
    pass
import NXOpen
class AMEBaseBuilder(NXOpen.Builder): 
    """ JA class for builder which creates one journal able object"""
    pass
class AMEBaseNode(AMEExtendedObject): 
    """ Represents Base Node """
    class NodeType(Enum):
        """
        Members Include: 
         |Project| 
         |Aspect| 

        """
        Project: int
        Aspect: int
        @staticmethod
        def ValueOf(value: int) -> AMEBaseNode.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetEngObject(self) -> IEngObject:
        """
         Returns AME.IEngObject 
         Returns engObject ( IEngObject NXOp): .
        """
        pass
class AMEConnection(AMEExtendedObject): 
    """ Represents Connection """
    def GetSource(self) -> AMEEngObject:
        """
         Get the source 
         Returns sourceEngObject ( AMEEngObject NXOp): .
        """
        pass
    def GetTarget(self) -> AMEEngObject:
        """
         Get the target 
         Returns targetEngObject ( AMEEngObject NXOp): .
        """
        pass
class AmeElectricalConnectionPotentialType(Enum):
    """
    Members Include: 
     |L| 
     |N| 
     |Pe| 
     |LPlus| 
     |LDash| 
     |Shield| 
     |Undefined| 
     |Invalid| 

    """
    L: int
    N: int
    Pe: int
    LPlus: int
    LDash: int
    Shield: int
    Undefined: int
    Invalid: int
    @staticmethod
    def ValueOf(value: int) -> AmeElectricalConnectionPotentialType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Annotations
class AMEEngineeringObjectLabel(NXOpen.NXObject): 
    """ Represents Engineering Object Label Object """
    @property
    def PmiFromLabel(self) -> NXOpen.Annotations.PmiNote:
        """
        Getter for property: ( NXOpen.Annotations.PmiNote) PmiFromLabel
         Returns the PMI note object stored by AME Engineering object label   
            
         
        """
        pass
import NXOpen.Assemblies
class AMEEngObject(AMEExtendedObject): 
    """ Represents Engineering Object """
    def GetAllAmePorts(self) -> List[AMEPort]:
        """
         Get all AME ports of this engineering object, sorted by their order index
         Returns ports ( AMEPort List[NX): .
        """
        pass
    def GetAllPhysicalConnectionObjects(self) -> List[AMEConnection]:
        """
         Get all Physical Connections with this Engineering Object as source or target device
         Returns physicalConnections ( AMEConnection List[NX): .
        """
        pass
    def GetAllPhysicalConnections(self) -> List[AMEExtendedObject]:
        """
         Get all Physical Connections with this Engineering Object as source or target device
         Returns physicalConnections ( AMEExtendedObject List[NX): .
        """
        pass
    def GetCableConnectionObjects(self) -> List[AMEConnection]:
        """
         Get all Physical Connections inside this Cable - Egineering Object (if this object is of cable type)
         Returns physicalConnections ( AMEConnection List[NX): .
        """
        pass
    def GetCableConnections(self) -> List[AMEExtendedObject]:
        """
         Get all Physical Connections inside this Cable - Egineering Object (if this object is of cable type)
         Returns physicalConnections ( AMEExtendedObject List[NX): .
        """
        pass
    def GetMappedExternalImportObject(self) -> ImportObject:
        """
         Returns the mapped external import object NXOpen.AME.ImportObject of Engineering Object
         Returns extImportObject ( ImportObject NXOp): .
        """
        pass
    def GetMappedExternalObject(self) -> NXOpen.Assemblies.Component:
        """
         Returns the mapped external object NXOpen.Assemblies.Component of engineering object
         Returns extObject ( NXOpen.Assemblies.Component): .
        """
        pass
    def GetZoneInformationOnGivenPage(self, pageObject: AMEExtendedObject) -> List[str]:
        """
         Get the horizontal or vertical zone information, based on page standard of its placement on given page
         Returns zones (List[str]): .
        """
        pass
    def IsProductAssigned(self) -> bool:
        """
         Returns whether product is assigned to Engineering Object 
         Returns isProductAssigned (bool): .
        """
        pass
    def PerformPlcsymbolMemoryrecordMatching(self) -> None:
        """
         Matching for Tag and Telegram MemoryRecord 
        """
        pass
import NXOpen
class AMEExtendedObject(NXOpen.NXObject): 
    """ Represents Extended Object """
    pass
class AmeFluidicConnectionOccupancyType(Enum):
    """
    Members Include: 
     |SupplyLine| 
     |ReturnLine| 
     |PilotLine| 
     |DrainLine| 
     |FlushingLine| 
     |BleedLine| 
     |Undefined| 
     |Invalid| 

    """
    SupplyLine: int
    ReturnLine: int
    PilotLine: int
    DrainLine: int
    FlushingLine: int
    BleedLine: int
    Undefined: int
    Invalid: int
    @staticmethod
    def ValueOf(value: int) -> AmeFluidicConnectionOccupancyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AMEGroupFolder(AMEBaseNode): 
    """ Group Folder Journaling class """
    pass
class AMEGroup(AMEBaseNode): 
    """ Group Journaling class """
    pass
class AmeJunctionRepresentationStyleType(Enum):
    """
    Members Include: 
     |Point| 
     |TargetSpecific| 
     |Invalid| 

    """
    Point: int
    TargetSpecific: int
    Invalid: int
    @staticmethod
    def ValueOf(value: int) -> AmeJunctionRepresentationStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Features
class AMEManager(NXOpen.Object): 
    """ Represents a manager of automation designer objects """
    class CreateStationType(Enum):
        """
        Members Include: 
         |Central| 
         |Dio| 

        """
        Central: int
        Dio: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.CreateStationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DeleteType(Enum):
        """
        Members Include: 
         |DeleteObject| 
         |DeleteTemplate| 
         |RemoveLastAspect| 
         |DeleteSymbolicRepresentation| 

        """
        DeleteObject: int
        DeleteTemplate: int
        RemoveLastAspect: int
        DeleteSymbolicRepresentation: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.DeleteType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaNativeLibType(Enum):
        """
        Members Include: 
         |All|  enables a lookup call to iterate through every known library type 
         |Type|  type objects from type library 
         |Product|  product objects from product library 
         |Symbol|  symbol objects from symbol library 
         |Template|  template objects from template library 
         |Setting|  setting objects from settings library 
         |Connection|  connection objects from connection library 
         |Port|  port objects from port library 
         |FormSheet|  form sheet objects from form sheet library 
         |System|  system objects from system library
         |ReportTemplate|  report template objects from report templates library 
         |ReportDefinition|  report definition objects from report templates definition 

        """
        All: int
        Type: int
        Product: int
        Symbol: int
        Template: int
        Setting: int
        Connection: int
        Port: int
        FormSheet: int
        System: int
        ReportTemplate: int
        ReportDefinition: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.JaNativeLibType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaNavigatorSortedState(Enum):
        """
        Members Include: 
         |Ascending| 
         |Descending| 
         |Unsorted| 

        """
        Ascending: int
        Descending: int
        Unsorted: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.JaNavigatorSortedState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaOrderType(Enum):
        """
        Members Include: 
         |Chronological|  System defined chronological order 
         |Alphanumeric|  System defined alphanumeric order 
         |Alphabetic|  System defined alphabetic order 
         |Manual|  User defined order

        """
        Chronological: int
        Alphanumeric: int
        Alphabetic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.JaOrderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MoveNavigatorNodesType(Enum):
        """
        Members Include: 
         |Movebefore| 
         |Moveafter| 

        """
        Movebefore: int
        Moveafter: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.MoveNavigatorNodesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PasteStatus(Enum):
        """
        Members Include: 
         |Successful| 
         |NoValidObjectToPaste| 
         |NameUnderParentExists| 
         |AdditionalObjectsInvolved| 

        """
        Successful: int
        NoValidObjectToPaste: int
        NameUnderParentExists: int
        AdditionalObjectsInvolved: int
        @staticmethod
        def ValueOf(value: int) -> AMEManager.PasteStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddAsComponentToCurrentProject(partName: str) -> None:
        """
         Add the given part as child componet to project 
        """
        pass
    def AddFreeTextObjectToContainer(objectTag: NXOpen.TaggedObject) -> None:
        """
         Adds the object(NXOpen.Diagramming.Annotation or NXOpen.Diagramming.Tables.CellBuilder)
                    holding free text to FreeTextContainer object for translation 
        """
        pass
    def AddressRuleSettingsBuilder(part: NXOpen.Part) -> AddressRuleSettingsBuilder:
        """
         Creates a NXOpen.AME.AddressRuleSettingsBuilder 
         Returns builder ( AddressRuleSettingsBuilder NXOp): .
        """
        pass
    def ApplyNamingRule(obj: NXOpen.NXObject) -> None:
        """
         Apply naming rule 
        """
        pass
    def AssignCableCore(sourceConnection: AMEExtendedObject, coreToAssign: AMEExtendedObject) -> None:
        """
         Assign cable core 
        """
        pass
    def AssignEplanMacros() -> None:
        """
         Assign all eplan macros 
        """
        pass
    def AssignMacros() -> Tuple[int, int]:
        """
         Assign all eplan macros 
         Returns A tuple consisting of (numPlacedObjs, numUnAssignedObjs). 
         - numPlacedObjs is: int.
         - numUnAssignedObjs is: int.

        """
        pass
    def AssignPlcAddressRuleSetBuilder(part: NXOpen.Part) -> AssignPlcAddressRuleSetBuilder:
        """
         Creates a NXOpen.AME.AssignPlcAddressRuleSetBuilder 
         Returns builder ( AssignPlcAddressRuleSetBuilder NXOp): .
        """
        pass
    def CaptureSymbolImage(part: NXOpen.Part, margin: float, scaledPixelHeight: int, zoomFactor: float) -> None:
        """
         Capture a symbol's preview image and assign it to currently active symbol variant 
        """
        pass
    def ChangeDescription(obj: INodeObject, text: str) -> None:
        """
         Change the description of the node 
        """
        pass
    def ChangeEngineeringObjectDescription(eoTag: IEngObject, text: str) -> None:
        """
         Change the description of an Engineering Object 
        """
        pass
    def ChangeName(obj: INodeObject, text: str) -> None:
        """
         Change the name of the node
        """
        pass
    def ChangeNativeDirectory(newDir: str) -> str:
        """
         Changes the default directory with the given path and returns an SM_alloc'd old directory path 
         Returns oldDir (str): .
        """
        pass
    def ChangeParent(obj: NXOpen.NXObject, newParent: NXOpen.NXObject) -> None:
        """
         Change the parent of a node in navigator
        """
        pass
    def ClearClipboard() -> None:
        """
         Clears clipboard 
        """
        pass
    def CloseAmeProject() -> None:
        """
         Close AME project
        """
        pass
    def CollectEosFromNavigator(navName: str) -> List[AMEEngObject]:
        """
         Collect the EOs from project based on the given navigator name 
         Returns eosInNav ( AMEEngObject List[NX): .
        """
        pass
    def CollectPlcstationsNameidFromAuomationNavigator() -> List[str]:
        """
         Collect the plcstation name and id from Automation navigator 
         Returns stationNameId (List[str]): .
        """
        pass
    def ConfigureMemoryAreas(obj: NXOpen.NXObject) -> List[AMEBaseNode]:
        """
         Creates memory areas and memory records for given product definition
         Returns newObjects ( AMEBaseNode List[NX): .
        """
        pass
    def ConnectGlobalSymbols(plcStationNode: AMEBaseNode, softwareObjects: List[AMEBaseNode]) -> None:
        """
         Connect Global Symbols for given objects to available objects under the same PLC 
        """
        pass
    def ConnectToLibraryItemBuilder(part: NXOpen.Part, port: SoftwareBlockDataTypePort) -> ConnectToLibraryItemBuilder:
        """
         Creates a connect to library item builder 
         Returns builder ( ConnectToLibraryItemBuilder NXOp): .
        """
        pass
    def ConvertStationToXml(selectedStations: List[AMEBaseNode], objectsToExport: List[str], stationsToUpdateInTia: List[str], sendWithDistributedIOs: bool, targetEnv: str) -> str:
        """
         Converts Plcstation to XML 
         Returns projectXML (str): .
        """
        pass
    def CopyObjects(objectsToCopy: List[INodeObject]) -> None:
        """
         Copies objects on the clipboard 
        """
        pass
    def CreateAccessorEvaluatorBuilder(part: NXOpen.Part, accessorEvaluator: ExpressionEvaluator) -> AccessorEvaluatorBuilder:
        """
         Creates a NXOpen.AME.AccessorEvaluatorBuilder 
         Returns builder ( AccessorEvaluatorBuilder NXOp): .
        """
        pass
    def CreateAddEplanPropertyBuilder(part: NXOpen.Part) -> AddEplanPropertyBuilder:
        """
         Creates a NXOpen.AME.AddEplanPropertyBuilder 
         Returns builder ( AddEplanPropertyBuilder NXOp): .
        """
        pass
    def CreateAddEplanValueSetBuilder(part: NXOpen.Part) -> AddEplanValueSetBuilder:
        """
         Creates a NXOpen.AME.AddEplanValueSetBuilder 
         Returns builder ( AddEplanValueSetBuilder NXOp): .
        """
        pass
    def CreateAddPlaceholderBuilder(part: NXOpen.Part) -> AddPlaceholderBuilder:
        """
         Creates a NXOpen.AME.AddPlaceholderBuilder 
         Returns builder ( AddPlaceholderBuilder NXOp): .
        """
        pass
    def CreateAddPlcOperatorBuilder(part: NXOpen.Part) -> AddPlcOperatorBuilder:
        """
         Creates a AME.AddPlcOperatorBuilder 
         Returns builder ( AddPlcOperatorBuilder NXOp): .
        """
        pass
    def CreateAddPropertyColumnBuilder(queryObject: AMEQuery) -> AddPropertyColumnBuilder:
        """
         Creates a NXOpen.AME.AddPropertyColumnBuilder 
         Returns builder ( AddPropertyColumnBuilder NXOp): .
        """
        pass
    def CreateAncestorEvaluatorBuilder(part: NXOpen.Part, ancestorEvaluator: ExpressionEvaluator) -> AncestorEvaluatorBuilder:
        """
         Creates a NXOpen.AME.AncestorEvaluatorBuilder 
         Returns builder ( AncestorEvaluatorBuilder NXOp): .
        """
        pass
    def CreateApplicationBuilder(part: NXOpen.Part) -> ApplicationBuilder:
        """
         Creates a NXOpen.AME.ApplicationBuilder 
         Returns builder ( ApplicationBuilder NXOp): .
        """
        pass
    def CreateAspectBoxBuilder(part: NXOpen.Part, aspectBox: AspectBox) -> AspectBoxBuilder:
        """
         Creates a AME.AspectBoxBuilder 
         Returns builder ( AspectBoxBuilder NXOp): .
        """
        pass
    def CreateAspectNavigatorPreferencesBuilder(part: NXOpen.Part) -> AspectNavigatorPreferencesBuilder:
        """
         Creates a builder for the aspect navigator preferences dialog
         Returns builder ( AspectNavigatorPreferencesBuilder NXOp): .
        """
        pass
    def CreateAspectPrefixBuilder(part: NXOpen.Part) -> AspectPrefixBuilder:
        """
         Creates a NXOpen.AME.AspectPrefixBuilder 
         Returns builder ( AspectPrefixBuilder NXOp): .
        """
        pass
    def CreateAssignAspectBuilder(part: NXOpen.Part) -> AssignAspectBuilder:
        """
         Creates a NXOpen.AME.AssignAspectBuilder 
         Returns builder ( AssignAspectBuilder NXOp): .
        """
        pass
    def CreateAssignSubnetBuilder(part: NXOpen.Part) -> AssignSubnetBuilder:
        """
         Creates a NXOpen.AME.AssignSubnetBuilder 
         Returns builder ( AssignSubnetBuilder NXOp): .
        """
        pass
    def CreateAssignTemplateToProductBuilder(productDef: ProductDefinition) -> AssignTemplateToProductBuilder:
        """
         Creates a NXOpen.AME.AssignTemplateToProductBuilder 
         Returns builder ( AssignTemplateToProductBuilder NXOp): .
        """
        pass
    def CreateAssignTypeBuilder(part: NXOpen.Part) -> AssignTypeBuilder:
        """
         Creates a NXOpen.AME.AssignTypeBuilder 
         Returns builder ( AssignTypeBuilder NXOp): .
        """
        pass
    def CreateAutomationControlScopeBuilder(part: NXOpen.Part) -> AutomationControlScopeBuilder:
        """
         Creates a NXOpen.AME.AutomationControlScopeBuilder 
         Returns builder ( AutomationControlScopeBuilder NXOp): .
        """
        pass
    def CreateBomBuilder(part: NXOpen.Part) -> CreateBOMBuilder:
        """
         Creates a NXOpen.AME.CreateBOMBuilder 
         Returns builder ( CreateBOMBuilder NXOp): .
        """
        pass
    def CreateBreakTemplateBuilder(part: NXOpen.Part, engObj: AMEEngObject) -> BreakTemplateBuilder:
        """
         Creates a NXOpen.AME.BreakTemplateBuilder 
         Returns builder ( BreakTemplateBuilder NXOp): .
        """
        pass
    def CreateBulk3dplacementBuilder(part: NXOpen.Part) -> Bulk3DPlacementBuilder:
        """
         Creates a AME.Bulk3DPlacementBuilder 
         Returns builder ( Bulk3DPlacementBuilder NXOp): .
        """
        pass
    def CreateBulkConnectionBuilder(part: NXOpen.Part) -> BulkConnectionBuilder:
        """
         Creates a NXOpen.AME.BulkConnectionBuilder 
         Returns builder ( BulkConnectionBuilder NXOp): .
        """
        pass
    def CreateBulkEditAnnotationBuilder(part: NXOpen.Part) -> BulkEditAnnotationBuilder:
        """
         Creates NXOpen.AME.BulkEditAnnotationBuilder 
         Returns builder ( BulkEditAnnotationBuilder NXOp): .
        """
        pass
    def CreateBulkEngineeringObjectBuilder(part: NXOpen.Part) -> BulkEngineeringObjectBuilder:
        """
         Creates a NXOpen.AME.BulkEngineeringObjectBuilder 
         Returns builder ( BulkEngineeringObjectBuilder NXOp): .
        """
        pass
    def CreateCabinetDesignBuilder(part: NXOpen.Part) -> CabinetDesignBuilder:
        """
         Creates a NXOpen.AME.CabinetDesignBuilder 
         Returns builder ( CabinetDesignBuilder NXOp): .
        """
        pass
    def CreateCabinetObjectLabelBuilder(part: NXOpen.Part, engObject: AMEEngObject, label: NXOpen.NXObject) -> CabinetObjectLabelBuilder:
        """
         Creates a AME.CabinetObjectLabelBuilder 
         Returns builder ( CabinetObjectLabelBuilder NXOp): .
        """
        pass
    def CreateCallMethodRuleBuilder(part: NXOpen.Part, editedRule: PlcCodePosition, block: PlcBlock, ruleType: PlcRule.Type, refObjectType: PlcRule.RefObjectType, replacementType: PlcRule.ReplacementType, compileUnitIndex: int, startIndex: int, endIndex: int) -> CallMethodRuleBuilder:
        """
         Creates a NXOpen.AME.CallMethodRuleBuilder 
         Returns builder ( CallMethodRuleBuilder NXOp): .
        """
        pass
    def CreateChangeProductTypeBuilder(part: NXOpen.Part) -> ChangeProductTypeBuilder:
        """
         Creates a NXOpen.AME.ChangeProductTypeBuilder 
         Returns builder ( ChangeProductTypeBuilder NXOp): .
        """
        pass
    def CreateChangeSymbolVariantBuilder(part: NXOpen.Part) -> ChangeSymbolVariantBuilder:
        """
         Creates a NXOpen.AME.ChangeSymbolVariantBuilder 
         Returns builder ( ChangeSymbolVariantBuilder NXOp): .
        """
        pass
    def CreateChildrenEvaluatorBuilder(part: NXOpen.Part, childrenEvaluator: ExpressionEvaluator) -> ChildrenEvaluatorBuilder:
        """
         Creates a NXOpen.AME.ChildrenEvaluatorBuilder 
         Returns builder ( ChildrenEvaluatorBuilder NXOp): .
        """
        pass
    def CreateCollaborationProjectSettingsBuilder(part: NXOpen.Part) -> CollaborationProjectSettingsBuilder:
        """
         Creates a builder for Collaboration Project Settings 
         Returns builder ( CollaborationProjectSettingsBuilder NXOp): .
        """
        pass
    def CreateConfigureResultTableBuilder(queryObject: AMEQuery) -> ConfigureResultTableBuilder:
        """
         Creates a NXOpen.AME.ConfigureResultTableBuilder 
         Returns builder ( ConfigureResultTableBuilder NXOp): .
        """
        pass
    def CreateConnectedObjectsEvaluatorBuilder(part: NXOpen.Part, connectedObjectsEvaluator: ExpressionEvaluator) -> ConnectedObjectsEvaluatorBuilder:
        """
         Creates a NXOpen.AME.ConnectedObjectsEvaluatorBuilder 
         Returns builder ( ConnectedObjectsEvaluatorBuilder NXOp): .
        """
        pass
    def CreateCreateEplanNodeBuilder(part: NXOpen.Part) -> CreateEplanNodeBuilder:
        """
         Creates a NXOpen.AME.CreateEplanNodeBuilder 
         Returns builder ( CreateEplanNodeBuilder NXOp): .
        """
        pass
    def CreateCreateFciBuilder(part: NXOpen.Part, node: PlcBlock, mode: InstanceDataBlockBuilder.CreateMode) -> CreateFCIBuilder:
        """
         Creates an function call instance builder 
         Returns builder ( CreateFCIBuilder NXOp): .
        """
        pass
    def CreateCreateIdbBuilder(part: NXOpen.Part, node: PlcBlock, mode: InstanceDataBlockBuilder.CreateMode) -> CreateIDBBuilder:
        """
         Creates an function call instance builder 
         Returns builder ( CreateIDBBuilder NXOp): .
        """
        pass
    def CreateCreateNamingSchemeBuilder(part: NXOpen.Part) -> CreateNamingSchemeBuilder:
        """
         Creates a builder for the Set Naming Rules dialog
         Returns builder ( CreateNamingSchemeBuilder NXOp): .
        """
        pass
    def CreateCreateRuleSetBuilder(part: NXOpen.Part) -> CreateRuleSetBuilder:
        """
         Creates a NXOpen.AME.CreateRuleSetBuilder 
         Returns builder ( CreateRuleSetBuilder NXOp): .
        """
        pass
    def CreateCreateSystemIdbBuilder(part: NXOpen.Part, idbName: str, typeFB: str, idbScope: InstanceDataBlockBuilder.ActionType, failSafe: bool) -> CreateSystemIDBBuilder:
        """
         JA class to create system idb builder 
         Returns builder ( CreateSystemIDBBuilder NXOp): .
        """
        pass
    def CreateCreateValueSetBuilder(part: NXOpen.Part) -> CreateValueSetBuilder:
        """
         Creates a AME.CreateValueSetBuilder 
         Returns builder ( CreateValueSetBuilder NXOp): .
        """
        pass
    def CreateDiagramNodeBuilder(part: NXOpen.Part) -> DiagramNodeBuilder:
        """
         Creates a AME.DiagramNodeBuilder 
         Returns builder ( DiagramNodeBuilder NXOp): .
        """
        pass
    def CreateDocumentStructureBuilder(part: NXOpen.Part) -> DocumentStructureBuilder:
        """
         Creates a NXOpen.AME.DocumentStructureBuilder 
         Returns builder ( DocumentStructureBuilder NXOp): .
        """
        pass
    def CreateDrawingStandardSettingsBuilder(part: NXOpen.Part) -> DrawingStandardSettingsBuilder:
        """
         Creates an DrawingStandardSettingsBuilder 
         Returns builder ( DrawingStandardSettingsBuilder NXOp): .
        """
        pass
    def CreateDrive(stationTag: NXOpen.NXObject, text: str) -> List[AMEExtendedObject]:
        """
         Creates a object of drive under provided station 
         Returns drive ( AMEExtendedObject List[NX): .
        """
        pass
    def CreateDxfdwgExportBuilder(part: NXOpen.Part) -> DxfdwgExportBuilder:
        """
         Creates a NXOpen.AME.DxfdwgExportBuilder 
         Returns builder ( DxfdwgExportBuilder NXOp): .
        """
        pass
    def CreateEditAnnotationBuilder(part: NXOpen.Part, extObject: AMEExtendedObject) -> EditAnnotationBuilder:
        """
         Creates a NXOpen.AME.EditAnnotationBuilder 
         Returns builder ( EditAnnotationBuilder NXOp): .
        """
        pass
    def CreateEditClauseBuilder(part: NXOpen.Part, queryObject: AMEQuery, queryClause: QueryClause) -> EditClauseBuilder:
        """
         Creates a NXOpen.AME.EditClauseBuilder 
         Returns builder ( EditClauseBuilder NXOp): .
        """
        pass
    def CreateEditDisplaySettingsBuilder(part: NXOpen.Part) -> EditDisplaySettingsBuilder:
        """
         Creates a AME.EditDisplaySettingsBuilder 
         Returns builder ( EditDisplaySettingsBuilder NXOp): .
        """
        pass
    def CreateEditEngineeringObjectBuilder(part: NXOpen.Part, editObject: AMEEngObject) -> EditEngineeringObjectBuilder:
        """
         Creates a NXOpen.AME.EditEngineeringObjectBuilder 
         Returns builder ( EditEngineeringObjectBuilder NXOp): .
        """
        pass
    def CreateEditInEplanBuilder(part: NXOpen.Part) -> EditInEplanBuilder:
        """
         Creates a AME.EditInEplanBuilder 
         Returns builder ( EditInEplanBuilder NXOp): .
        """
        pass
    def CreateEditOrderBuilder(part: NXOpen.Part, portContainer: NXOpen.NXObject) -> EditOrderBuilder:
        """
         Creates a NXOpen.AME.EditOrderBuilder 
         Returns builder ( EditOrderBuilder NXOp): .
        """
        pass
    def CreateEditQueryScopeBuilder(part: NXOpen.Part, queryObject: AMEQuery, queryClause: QueryClause) -> TCSavedQueriesBuilder:
        """
         Creates a NXOpen.AME.TCSavedQueriesBuilder 
         Returns builder ( TCSavedQueriesBuilder NXOp): .
        """
        pass
    def CreateElectricalAnnotationSettingsBuilder(part: NXOpen.Part) -> ElectricalAnnotationSettingsBuilder:
        """
         Creates a NXOpen.AME.ElectricalAnnotationSettingsBuilder 
         Returns builder ( ElectricalAnnotationSettingsBuilder NXOp): .
        """
        pass
    def CreateElectricalConnectionSettingsBuilder(part: NXOpen.Part) -> ElectricalConnectionSettingsBuilder:
        """
         Creates a NXOpen.AME.ElectricalConnectionSettingsBuilder 
         Returns builder ( ElectricalConnectionSettingsBuilder NXOp): .
        """
        pass
    def CreateEngObjectDefinitionBuilder(part: NXOpen.Part) -> CreateEngObjectDefinitionBuilder:
        """
         Creates a NXOpen.AME.CreateEngObjectDefinitionBuilder 
         Returns builder ( CreateEngObjectDefinitionBuilder NXOp): .
        """
        pass
    def CreateEngineeringObject(obj: INodeObject, filename: str) -> List[NXOpen.NXObject]:
        """
         Creates engineering object under given parent
         Returns newObjects ( NXOpen.NXObject Li): .
        """
        pass
    def CreateEngineeringObjectAndMapLdObject(ldObject: NXOpen.NXObject) -> None:
        """
         Create an eo and map it to a LD object 
        """
        pass
    def CreateEngineeringObjectBuilder(part: NXOpen.Part) -> EngineeringObjectBuilder:
        """
         Creates a NXOpen.AME.EngineeringObjectBuilder 
         Returns builder ( EngineeringObjectBuilder NXOp): .
        """
        pass
    def CreateEngineeringObjectDefinitionLabelBuilder(part: NXOpen.Part) -> EngineeringObjectDefinitionLabelBuilder:
        """
         Creates a NXOpen.AME.EngineeringObjectDefinitionLabelBuilder 
         Returns builder ( EngineeringObjectDefinitionLabelBuilder NXOp): .
        """
        pass
    def CreateEngineeringObjectsAndMapLdObjects(ldObjects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Create engineering objects and map them to external objects in bulk 
         Returns adObjects ( NXOpen.NXObject Li):  Mapped automation designer objects .
        """
        pass
    def CreateEplanImportProjectTemplateBuilder(part: NXOpen.Part) -> EplanImportProjectTemplateBuilder:
        """
         Creates a NXOpen.AME.EplanImportProjectTemplateBuilder 
         Returns builder ( EplanImportProjectTemplateBuilder NXOp): .
        """
        pass
    def CreateEplanProjectGenerationBuilder(part: NXOpen.Part) -> EplanProjectGenerationBuilder:
        """
         Creates a builder for the EPLAN project generation dialog
         Returns builder ( EplanProjectGenerationBuilder NXOp): .
        """
        pass
    def CreateEplanProjectTemplateAndStructureBuilder(part: NXOpen.Part) -> EplanProjectTemplateAndStructureBuilder:
        """
         Creates an EplanProjectTemplateAndStructureBuilder 
         Returns builder ( EplanProjectTemplateAndStructureBuilder NXOp): .
        """
        pass
    def CreateEplanSettingsBuilder(part: NXOpen.Part, node: AMEBaseNode) -> EplanSettingsBuilder:
        """
         Creates an EplanSettingsBuilder 
         Returns builder ( EplanSettingsBuilder NXOp): .
        """
        pass
    def CreateEplanStructureIdentifierOrderBuilder(part: NXOpen.Part) -> EplanStructureIdentifierOrderBuilder:
        """
         Creates a NXOpen.AME.EplanStructureIdentifierOrderBuilder 
         Returns builder ( EplanStructureIdentifierOrderBuilder NXOp): .
        """
        pass
    def CreateEplanValueSetBuilder(part: NXOpen.Part) -> EplanValueSetBuilder:
        """
         Creates a NXOpen.AME.EplanValueSetBuilder 
         Returns builder ( EplanValueSetBuilder NXOp): .
        """
        pass
    def CreateEvaluatorCopyToBuilder(part: NXOpen.Part) -> EvaluatorCopyToBuilder:
        """
         Creates a NXOpen.AME.EvaluatorCopyToBuilder 
         Returns builder ( EvaluatorCopyToBuilder NXOp): .
        """
        pass
    def CreateExportCmctopoProjectBuilder(part: NXOpen.Part) -> ExportCMCTopoProjectBuilder:
        """
         Creates a NXOpen.AME.ExportCMCTopoProjectBuilder 
         Returns builder ( ExportCMCTopoProjectBuilder NXOp): .
        """
        pass
    def CreateExportEclassMappingBuilder(part: NXOpen.Part) -> ExportEClassMappingBuilder:
        """
         Creates a NXOpen.AME.ExportEClassMappingBuilder 
         Returns builder ( ExportEClassMappingBuilder NXOp): .
        """
        pass
    def CreateExportEplanMappingBuilder(part: NXOpen.Part) -> ExportEplanMappingBuilder:
        """
         Creates a NXOpen.AME.ExportEplanMappingBuilder 
         Returns builder ( ExportEplanMappingBuilder NXOp): .
        """
        pass
    def CreateExternalObjectsTypeMappingBuilder(part: NXOpen.Part) -> ExternalObjectsTypeMappingBuilder:
        """
         Creates a NXOpen.AME.ExternalObjectsTypeMappingBuilder 
         Returns builder ( ExternalObjectsTypeMappingBuilder NXOp): .
        """
        pass
    def CreateExtractAttributeBuilder(part: NXOpen.Part, extractAttribute: ExtractAttribute) -> ExtractAttributeBuilder:
        """
         Creates an extract attribute builder 
         Returns builder ( ExtractAttributeBuilder NXOp): .
        """
        pass
    def CreateExtractAttributeEvaluator(uiExp: NXOpen.Expression, targetCategoryName: str, targetPropName: str, targetObj: NXOpen.NXObject) -> ExpressionEvaluator:
        """
         Create Extract Attribute Evaluator 
         Returns extEval ( ExpressionEvaluator NXOp): .
        """
        pass
    def CreateFindByConditionEvaluatorBuilder(part: NXOpen.Part, conditionEvaluator: ExpressionEvaluator) -> FindByConditionEvaluatorBuilder:
        """
         Creates a AME.FindByConditionEvaluatorBuilder 
         Returns builder ( FindByConditionEvaluatorBuilder NXOp): .
        """
        pass
    def CreateFluidicAnnotationSettingsBuilder(part: NXOpen.Part) -> FluidicAnnotationSettingsBuilder:
        """
         Creates a NXOpen.AME.FluidicAnnotationSettingsBuilder 
         Returns builder ( FluidicAnnotationSettingsBuilder NXOp): .
        """
        pass
    def CreateFluidicConnectionSettingsBuilder(part: NXOpen.Part) -> FluidicConnectionSettingsBuilder:
        """
         Creates a NXOpen.AME.FluidicConnectionSettingsBuilder 
         Returns builder ( FluidicConnectionSettingsBuilder NXOp): .
        """
        pass
    def CreateFormSheetBuilder(part: NXOpen.Part, formSheetObject: FormSheetObject) -> FormSheetBuilder:
        """
         Creates a NXOpen.AME.FormSheetBuilder 
         Returns builder ( FormSheetBuilder NXOp): .
        """
        pass
    def CreateFormSheetSettingsBuilder(part: NXOpen.Part) -> FormSheetSettingsBuilder:
        """
         Creates a NXOpen.AME.FormSheetSettingsBuilder 
         Returns builder ( FormSheetSettingsBuilder NXOp): .
        """
        pass
    def CreateFragmentBuilder(part: NXOpen.Part) -> FragmentBuilder:
        """
         Creates a NXOpen.AME.FragmentBuilder 
         Returns builder ( FragmentBuilder NXOp): .
        """
        pass
    def CreateGeneralAnnotationSettingsBuilder(part: NXOpen.Part) -> GeneralAnnotationSettingsBuilder:
        """
         Creates a NXOpen.AME.GeneralAnnotationSettingsBuilder 
         Returns builder ( GeneralAnnotationSettingsBuilder NXOp): .
        """
        pass
    def CreateGeneralConnectionSettingsBuilder(part: NXOpen.Part) -> GeneralConnectionSettingsBuilder:
        """
         Creates a NXOpen.AME.GeneralConnectionSettingsBuilder 
         Returns builder ( GeneralConnectionSettingsBuilder NXOp): .
        """
        pass
    def CreateGeneralNamingRuleBuilder(part: NXOpen.Part) -> GeneralNamingRuleBuilder:
        """
         Creates a NXOpen.AME.GeneralNamingRuleBuilder 
         Returns builder ( GeneralNamingRuleBuilder NXOp): .
        """
        pass
    def CreateGenerateReportsBuilder(part: NXOpen.Part) -> GenerateReportsBuilder:
        """
         Creates a NXOpen.AME.GenerateReportsBuilder 
         Returns builder ( GenerateReportsBuilder NXOp): .
        """
        pass
    def CreateGlobalSelectionBuilder(part: NXOpen.Part) -> GlobalSelectionBuilder:
        """
         Creates a  global selection builder 
         Returns builder ( GlobalSelectionBuilder NXOp): .
        """
        pass
    def CreateGroupBuilder(part: NXOpen.Part, group: AMEGroup) -> GroupBuilder:
        """
         Creates a NXOpen.AME.GroupBuilder 
         Returns builder ( GroupBuilder NXOp): .
        """
        pass
    def CreateGroupFolder(parentNode: AMEBaseNode) -> AMEGroupFolder:
        """
         Creates a NXOpen.AME.AMEGroupFolder 
         Returns newFolder ( AMEGroupFolder NXOp): .
        """
        pass
    def CreateImportBmecatSchemaBuilder(part: NXOpen.Part) -> ImportBMECatSchemaBuilder:
        """
         Creates a NXOpen.AME.ImportBMECatSchemaBuilder 
         Returns builder ( ImportBMECatSchemaBuilder NXOp): .
        """
        pass
    def CreateImportEclassMappingBuilder(part: NXOpen.Part) -> ImportEClassMappingBuilder:
        """
         Creates a NXOpen.AME.ImportEClassMappingBuilder 
         Returns builder ( ImportEClassMappingBuilder NXOp): .
        """
        pass
    def CreateImportEclassProductBuilder(part: NXOpen.Part) -> ImportEClassProductBuilder:
        """
         Creates a NXOpen.AME.ImportEClassProductBuilder 
         Returns builder ( ImportEClassProductBuilder NXOp): .
        """
        pass
    def CreateImportEclassProductListBuilder(part: NXOpen.Part) -> ImportEClassProductListBuilder:
        """
         Creates a NXOpen.AME.ImportEClassProductListBuilder 
         Returns builder ( ImportEClassProductListBuilder NXOp): .
        """
        pass
    def CreateImportEclassSchemaBuilder(part: NXOpen.Part) -> ImportEClassSchemaBuilder:
        """
         Creates a NXOpen.AME.ImportEClassSchemaBuilder 
         Returns builder ( ImportEClassSchemaBuilder NXOp): .
        """
        pass
    def CreateImportEplanMappingBuilder(part: NXOpen.Part) -> ImportEplanMappingBuilder:
        """
         Creates a NXOpen.AME.ImportEplanMappingBuilder 
         Returns builder ( ImportEplanMappingBuilder NXOp): .
        """
        pass
    def CreateImportEplanPageMacroBuilder(part: NXOpen.Part) -> ImportEplanPageMacroBuilder:
        """
         Creates a NXOpen.AME.ImportEplanPageMacroBuilder 
         Returns builder ( ImportEplanPageMacroBuilder NXOp): .
        """
        pass
    def CreateImportEplanProductBuilder(part: NXOpen.Part) -> ImportEplanProductBuilder:
        """
         Creates a NXOpen.AME.ImportEplanProductBuilder 
         Returns builder ( ImportEplanProductBuilder NXOp): .
        """
        pass
    def CreateImportEplanProductListBuilder(part: NXOpen.Part) -> ImportEplanProductListBuilder:
        """
         Creates a NXOpen.AME.ImportEplanProductListBuilder 
         Returns builder ( ImportEplanProductListBuilder NXOp): .
        """
        pass
    def CreateImportGlobalMappingBuilder(part: NXOpen.Part) -> ImportGlobalMappingBuilder:
        """
         Creates a NXOpen.AME.ImportGlobalMappingBuilder 
         Returns builder ( ImportGlobalMappingBuilder NXOp): .
        """
        pass
    def CreateImportHwxmlBuilder(part: NXOpen.Part, parentNode: AMEBaseNode) -> ImportHWXmlBuilder:
        """
         Creates an HWXml import builder 
         Returns builder ( ImportHWXmlBuilder NXOp): .
        """
        pass
    def CreateInsertObjectBuilder(part: NXOpen.Part) -> InsertObjectBuilder:
        """
         Creates a NXOpen.AME.InsertObjectBuilder 
         Returns builder ( InsertObjectBuilder NXOp): .
        """
        pass
    def CreateInspectSnapshotBuilder(part: NXOpen.Part) -> InspectSnapshotBuilder:
        """
         Creates a NXOpen.AME.InspectSnapshotBuilder 
         Returns builder ( InspectSnapshotBuilder NXOp): .
        """
        pass
    def CreateInstantiateTemplateBulkBuilder(part: NXOpen.Part, reusePartName: str) -> InstantiateTemplateBulkBuilder:
        """
         Creates a NXOpen.AME.InstantiateTemplateBulkBuilder 
         Returns builder ( InstantiateTemplateBulkBuilder NXOp): .
        """
        pass
    def CreateInterfaceMemberBuilder(part: NXOpen.Part, parentSection: AMEExtendedObject, editInterfaceMember: AMEExtendedObject) -> InterfaceMemberBuilder:
        """
         Creates a NXOpen.AME.InterfaceMemberBuilder 
         Returns builder ( InterfaceMemberBuilder NXOp): .
        """
        pass
    def CreateInterruptionPointBuilder(part: NXOpen.Part, interruptionPoint: AMEExtendedObject) -> InterruptionPointBuilder:
        """
         Creates a NXOpen.AME.InterruptionPointBuilder 
         Returns builder ( InterruptionPointBuilder NXOp): .
        """
        pass
    def CreateLabel(eo: AMEEngObject, targetPosition: NXOpen.Point3d) -> AMEEngineeringObjectLabel:
        """
         Creates an Engineering Object Label 
         Returns label ( AMEEngineeringObjectLabel NXOp): .
        """
        pass
    def CreateLayoutDefinitionBuilder(part: NXOpen.Part) -> LayoutDefinitionBuilder:
        """
         Creates a NXOpen.AME.LayoutDefinitionBuilder 
         Returns builder ( LayoutDefinitionBuilder NXOp): .
        """
        pass
    def CreateLineDesignerMappingBuilder(part: NXOpen.Part) -> LineDesignerMappingBuilder:
        """
         Creates a NXOpen.AME.LineDesignerMappingBuilder 
         Returns builder ( LineDesignerMappingBuilder NXOp): .
        """
        pass
    def CreateLinearDimensionBuilder(part: NXOpen.Part) -> LinearDimensionBuilder:
        """
         Creates a AME.LinearDimensionBuilder 
         Returns builder ( LinearDimensionBuilder NXOp): .
        """
        pass
    def CreateLoadLineDesignerBuilder(part: NXOpen.Part) -> LoadLineDesignerBuilder:
        """
         Creates a NXOpen.AME.LoadLineDesignerBuilder 
         Returns builder ( LoadLineDesignerBuilder NXOp): .
        """
        pass
    def CreateManage2dSymbolsBuilder(part: NXOpen.Part) -> Manage2dSymbolsBuilder:
        """
         Creates a NXOpen.AME.Manage2dSymbolsBuilder 
         Returns builder ( Manage2dSymbolsBuilder NXOp): .
        """
        pass
    def CreateManage3dmodelsBuilder(part: NXOpen.Part) -> Manage3DModelsBuilder:
        """
         Creates a NXOpen.AME.Manage3DModelsBuilder 
         Returns builder ( Manage3DModelsBuilder NXOp): .
        """
        pass
    def CreateManageDimensionPointsBuilder(part: NXOpen.Part) -> ManageDimensionPointsBuilder:
        """
         Creates a NXOpen.AME.ManageDimensionPointsBuilder 
         Returns builder ( ManageDimensionPointsBuilder NXOp): .
        """
        pass
    def CreateManageEclassmappingBuilder(part: NXOpen.Part) -> ManageEclassMappingBuilder:
        """
         Creates a NXOpen.AME.ManageEclassMappingBuilder 
         Returns builder ( ManageEclassMappingBuilder NXOp): .
        """
        pass
    def CreateManageEplanGlobalMappingBuilder(part: NXOpen.Part) -> ManageEplanGlobalMappingBuilder:
        """
         Creates a AME.ManageEplanGlobalMappingBuilder 
         Returns builder ( ManageEplanGlobalMappingBuilder NXOp): .
        """
        pass
    def CreateManageEplanmappingBuilder(part: NXOpen.Part) -> ManageEplanMappingBuilder:
        """
         Creates a NXOpen.AME.ManageEplanMappingBuilder 
         Returns builder ( ManageEplanMappingBuilder NXOp): .
        """
        pass
    def CreateManageGlobalMappingBuilder(part: NXOpen.Part) -> ManageGlobalMappingBuilder:
        """
         Creates a AME.ManageGlobalMappingBuilder 
         Returns builder ( ManageGlobalMappingBuilder NXOp): .
        """
        pass
    def CreateManageInterruptionPointsBuilder(part: NXOpen.Part) -> ManageInterruptionPointsBuilder:
        """
         Creates a AME.ManageInterruptionPointsBuilder 
         Returns builder ( ManageInterruptionPointsBuilder NXOp): .
        """
        pass
    def CreateManageObjectTypeBuilder(part: NXOpen.Part) -> ManageObjectTypeBuilder:
        """
         Creates a NXOpen.AME.ManageObjectTypeBuilder 
         Returns builder ( ManageObjectTypeBuilder NXOp): .
        """
        pass
    def CreateManageVariantBuilder(part: NXOpen.Part) -> ManageVariantBuilder:
        """
         Creates a AME.ManageVariantBuilder 
         Returns builder ( ManageVariantBuilder NXOp): .
        """
        pass
    def CreateMapToExistingObjectBuilder(part: NXOpen.Part) -> MapToExistingObjectBuilder:
        """
         Creates a Map To Existing Builder 
         Returns builder ( MapToExistingObjectBuilder NXOp): .
        """
        pass
    def CreateMemoryAreaBulkAddressingBuilder(part: NXOpen.Part) -> MemoryAreaBulkAddressingBuilder:
        """
         Creates a AME.MemoryAreaBulkAddressingBuilder 
         Returns builder ( MemoryAreaBulkAddressingBuilder NXOp): .
        """
        pass
    def CreateMethodBuilder(part: NXOpen.Part) -> CreateMethodBuilder:
        """
         Creates a AME.CreateMethodBuilder 
         Returns builder ( CreateMethodBuilder NXOp): .
        """
        pass
    def CreateMountingInterfaceBuilder(part: NXOpen.Part) -> MountingInterfaceBuilder:
        """
         Creates a NXOpen.AME.MountingInterfaceBuilder 
         Returns builder ( MountingInterfaceBuilder NXOp): .
        """
        pass
    def CreateNamingRuleSettingsBuilder(part: NXOpen.Part) -> NamingRuleSettingsBuilder:
        """
         Creates a builder for the Set Naming Rules dialog
         Returns builder ( NamingRuleSettingsBuilder NXOp): .
        """
        pass
    def CreateNamingSchemeAspectNamingBuilder(part: NXOpen.Part) -> NamingSchemeAspectNamingBuilder:
        """
         Creates a builder for the Naming Scheme Aspect Naming tab dialog
         Returns builder ( NamingSchemeAspectNamingBuilder NXOp): .
        """
        pass
    def CreateNamingSchemeGeneralBuilder(part: NXOpen.Part) -> NamingSchemeGeneralBuilder:
        """
         Creates a NXOpen.AME.NamingSchemeGeneralBuilder 
         Returns builder ( NamingSchemeGeneralBuilder NXOp): .
        """
        pass
    def CreateObjectEvaluatorBuilder(part: NXOpen.Part, objectEvaluator: ExpressionEvaluator) -> ObjectEvaluatorBuilder:
        """
         Creates a NXOpen.AME.ObjectEvaluatorBuilder 
         Returns builder ( ObjectEvaluatorBuilder NXOp): .
        """
        pass
    def CreateOperandRuleBuilder(part: NXOpen.Part, editedRule: PlcCodePosition, block: PlcBlock, indexOfCompileUnit: int, indexOfStatement: int, innerIndexOfOperand: int, ruleType: PlcRule.Type) -> OperandRuleBuilder:
        """
         Creates a NXOpen.AME.OperandRuleBuilder 
         Returns builder ( OperandRuleBuilder NXOp): .
        """
        pass
    def CreateOperatorRuleBuilder(part: NXOpen.Part, editedRule: PlcCodePosition, block: PlcBlock, ruleType: PlcRule.Type, refObjectType: PlcRule.RefObjectType, replacementType: PlcRule.ReplacementType, startIndex: int, endIndex: int, compileUnitIndex: int) -> OperatorRuleBuilder:
        """
         Creates a NXOpen.AME.OperatorRuleBuilder 
         Returns builder ( OperatorRuleBuilder NXOp): .
        """
        pass
    def CreateOpticalAnnotationSettingsBuilder(part: NXOpen.Part) -> OpticalAnnotationSettingsBuilder:
        """
         Creates a NXOpen.AME.OpticalAnnotationSettingsBuilder 
         Returns builder ( OpticalAnnotationSettingsBuilder NXOp): .
        """
        pass
    def CreateOpticalConnectionSettingsBuilder(part: NXOpen.Part) -> OpticalConnectionSettingsBuilder:
        """
         Creates a NXOpen.AME.OpticalConnectionSettingsBuilder 
         Returns builder ( OpticalConnectionSettingsBuilder NXOp): .
        """
        pass
    def CreateOrEditViews(selObject: AMEBaseNode) -> None:
        """
         Creates or Edits the Drafting views for selected cabinet or mechanical data 
        """
        pass
    def CreateOrGetObjectEvaluator(evaluatorBuilder: BaseEvaluatorBuilder) -> ExpressionEvaluator:
        """
         Create or get a AME.ExpressionEvaluator 
         Returns objEval ( ExpressionEvaluator NXOp): .
        """
        pass
    def CreateOrderAspectsBuilder(part: NXOpen.Part) -> OrderAspectsBuilder:
        """
         Creates a NXOpen.AME.OrderAspectsBuilder 
         Returns builder ( OrderAspectsBuilder NXOp): .
        """
        pass
    def CreatePageBuilder(part: NXOpen.Part) -> PageBuilder:
        """
         Creates a NXOpen.AME.PageBuilder 
         Returns builder ( PageBuilder NXOp): .
        """
        pass
    def CreatePageNamingBuilder(part: NXOpen.Part) -> PageNamingBuilder:
        """
         Creates a NXOpen.AME.PageNamingBuilder 
         Returns builder ( PageNamingBuilder NXOp): .
        """
        pass
    def CreateParameterRuleBuilder(part: NXOpen.Part, mvoPort: MultiValueObjectsPort, ruleType: PlcRule.Type, usageType: MultiValueObjectsPort.JaAmeValueObjectUsageType) -> ParameterRuleBuilder:
        """
         Creates a NXOpen.AME.ParameterRuleBuilder 
         Returns builder ( ParameterRuleBuilder NXOp): .
        """
        pass
    def CreateParentEvaluatorBuilder(part: NXOpen.Part, parentEvaluator: ExpressionEvaluator) -> ParentEvaluatorBuilder:
        """
         Creates a NXOpen.AME.ParentEvaluatorBuilder 
         Returns builder ( ParentEvaluatorBuilder NXOp): .
        """
        pass
    def CreatePhysicalConnectionBuilder(part: NXOpen.Part) -> PhysicalConnectionBuilder:
        """
         Creates a NXOpen.AME.PhysicalConnectionBuilder 
         Returns builder ( PhysicalConnectionBuilder NXOp): .
        """
        pass
    def CreatePlaceAutomationBuilder(part: NXOpen.Part) -> PlaceAutomationBuilder:
        """
         Creates a NXOpen.AME.PlaceAutomationBuilder 
         Returns builder ( PlaceAutomationBuilder NXOp): .
        """
        pass
    def CreatePlcAddressRuleSetupBuilder(part: NXOpen.Part) -> PlcAddressRuleSetupBuilder:
        """
         Creates a NXOpen.AME.PlcAddressRuleSetupBuilder 
         Returns builder ( PlcAddressRuleSetupBuilder NXOp): .
        """
        pass
    def CreatePlcChangeInstanceBlockMasterBuilder(instanceDataBlockToEdit: PlcBlock) -> PlcChangeInstanceBlockMasterBuilder:
        """
         Creates a AME.PlcChangeInstanceBlockMasterBuilder 
         Returns builder ( PlcChangeInstanceBlockMasterBuilder NXOp): .
        """
        pass
    def CreatePlcEditStateNoteBuilder(part: NXOpen.Part, plcStateChartBaseElement: AMEExtendedObject) -> PlcEditStateNoteBuilder:
        """
         Creates a AME.PlcEditStateNoteBuilder 
         Returns builder ( PlcEditStateNoteBuilder NXOp): .
        """
        pass
    def CreatePlcFlowChartConstantTextBuilder(part: NXOpen.Part, plcFlowChartOperandNodeObj: AMEExtendedObject, ruleType: PlcRule.Type) -> PlcFlowChartConstantTextBuilder:
        """
         Creates a NXOpen.AME.PlcFlowChartConstantTextBuilder 
         Returns builder ( PlcFlowChartConstantTextBuilder NXOp): .
        """
        pass
    def CreatePlcFlowChartOperatorBuilder(part: NXOpen.Part, extObject: AMEExtendedObject) -> PlcFlowChartOperatorBuilder:
        """
         Creates a NXOpen.AME.PlcFlowChartOperatorBuilder 
         Returns builder ( PlcFlowChartOperatorBuilder NXOp): .
        """
        pass
    def CreatePlcFunctionBlockBuilder(part: NXOpen.Part, block: PlcBlock) -> PlcFunctionBlockBuilder:
        """
         Creates a AME.PlcFunctionBlockBuilder 
         Returns builder ( PlcFunctionBlockBuilder NXOp): .
        """
        pass
    def CreatePlcInterfaceVariableBuilder(part: NXOpen.Part, node: AMEBaseNode) -> PlcInterfaceVariableBuilder:
        """
         Creates a NXOpen.AME.PlcInterfaceVariableBuilder 
         Returns builder ( PlcInterfaceVariableBuilder NXOp): .
        """
        pass
    def CreatePlcMemoryAreaBuilder(part: NXOpen.Part, memoryArea: AMEBaseNode) -> PlcMemoryAreaBuilder:
        """
         Creates a NXOpen.AME.PlcMemoryAreaBuilder 
         Returns builder ( PlcMemoryAreaBuilder NXOp): .
        """
        pass
    def CreatePlcMethodBuilder(part: NXOpen.Part, method: PlcMethod) -> PlcMethodBuilder:
        """
         Creates a NXOpen.AME.PlcMethodBuilder 
         Returns builder ( PlcMethodBuilder NXOp): .
        """
        pass
    def CreatePlcRack(stationTag: NXOpen.NXObject, text: str) -> AMEBaseNode:
        """
         Creates a object of plc rack under provided station 
         Returns rack ( AMEBaseNode NXOp): .
        """
        pass
    def CreatePlcStateChartActionBuilder(part: NXOpen.Part, stateObject: AMEExtendedObject, actionType: PlcStateChartActionBuilder.ActionType) -> PlcStateChartActionBuilder:
        """
         Creates a AME.PlcStateChartActionBuilder 
         Returns builder ( PlcStateChartActionBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartCreateElementBuilder(part: NXOpen.Part) -> PlcStateChartCreateElementBuilder:
        """
         Creates a NXOpen.AME.PlcStateChartCreateElementBuilder 
         Returns builder ( PlcStateChartCreateElementBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartDefineCallBuilder(part: NXOpen.Part, actionValue: AMEExtendedObject) -> PlcStateChartDefineCallBuilder:
        """
         Creates a NXOpen.AME.PlcStateChartDefineCallBuilder 
         Returns builder ( PlcStateChartDefineCallBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartFunctionBlockBuilder(part: NXOpen.Part, block: PlcBlock) -> PlcStateChartFunctionBlockBuilder:
        """
         Creates a AME.PlcStateChartFunctionBlockBuilder 
         Returns builder ( PlcStateChartFunctionBlockBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartItemValueBuilder(part: NXOpen.Part, plcStateChartBeseConditionItem: AMEExtendedObject, ruleType: PlcRule.Type) -> PlcStateChartItemValueBuilder:
        """
         Creates a NXOpen.AME.PlcStateChartItemValueBuilder 
         Returns builder ( PlcStateChartItemValueBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartStateBuilder(part: NXOpen.Part, plcStateObject: AMEExtendedObject) -> PlcStateChartStateBuilder:
        """
         Creates a AME.PlcStateChartStateBuilder 
         Returns builder ( PlcStateChartStateBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartTransitionBuilder(part: NXOpen.Part, transitionObject: AMEExtendedObject) -> PlcStateChartTransitionBuilder:
        """
         Creates a AME.PlcStateChartTransitionBuilder 
         Returns builder ( PlcStateChartTransitionBuilder NXOp): .
        """
        pass
    def CreatePlcStateChartTransitionPrioritiesBuilder(part: NXOpen.Part, plcStateObject: AMEExtendedObject) -> PlcStateChartTransitionPrioritiesBuilder:
        """
         Creates a AME.PlcStateChartTransitionPrioritiesBuilder 
         Returns builder ( PlcStateChartTransitionPrioritiesBuilder NXOp): .
        """
        pass
    def CreatePlcStation(text: str, stationType: AMEManager.CreateStationType) -> List[AMEBaseNode]:
        """
         Creates a object of plc central station 
         Returns stations ( AMEBaseNode List[NX): .
        """
        pass
    def CreatePlcSubFolder(parentNode: AMEBaseNode) -> AutomationFolder:
        """
         Creates a AME.AutomationFolder 
         Returns newFolder ( AutomationFolder NXOp): .
        """
        pass
    def CreatePlcSymbolBuilder(part: NXOpen.Part, node: AMEBaseNode) -> PlcSymbolBuilder:
        """
         Creates a NXOpen.AME.PlcSymbolBuilder 
         Returns builder ( PlcSymbolBuilder NXOp): .
        """
        pass
    def CreatePlcSymbolsEvaluatorBuilder(part: NXOpen.Part, plcSymbolsEvaluator: ExpressionEvaluator) -> PlcSymbolsEvaluatorBuilder:
        """
         Creates a NXOpen.AME.PlcSymbolsEvaluatorBuilder 
         Returns builder ( PlcSymbolsEvaluatorBuilder NXOp): .
        """
        pass
    def CreatePlcTelegramBuilder(part: NXOpen.Part, engObject: AMEEngObject) -> PlcTelegramBuilder:
        """
         Creates a NXOpen.AME.PlcTelegramBuilder 
         Returns builder ( PlcTelegramBuilder NXOp): .
        """
        pass
    def CreatePlcTelegramBuilderFromTelegramdef(part: NXOpen.Part, telegramDef: PlcTelegramDefinition) -> PlcTelegramBuilder:
        """
         Creates a NXOpen.AME.PlcTelegramBuilder 
         Returns builder ( PlcTelegramBuilder NXOp): .
        """
        pass
    def CreatePlcVendorSymbolBuilder(part: NXOpen.Part, memoryAreaTag: NXOpen.NXObject) -> PlcVendorSymbolBuilder:
        """
         Creates a NXOpen.AME.PlcVendorSymbolBuilder 
         Returns builder ( PlcVendorSymbolBuilder NXOp): .
        """
        pass
    def CreatePmiNoteBuilder(part: NXOpen.Part) -> CreatePmiNoteBuilder:
        """
         Creates a NXOpen.AME.CreatePmiNoteBuilder 
         Returns builder ( CreatePmiNoteBuilder NXOp): .
        """
        pass
    def CreatePortBuilder(part: NXOpen.Part, parent: NXOpen.NXObject, port: NXOpen.NXObject) -> PortBuilder:
        """
         Creates a port builder 
         Returns builder ( PortBuilder NXOp): .
        """
        pass
    def CreatePortConnectionBuilder(part: NXOpen.Part, port: NXOpen.NXObject) -> PortConnectionBuilder:
        """
         Creates a port builder 
         Returns builder ( PortConnectionBuilder NXOp): .
        """
        pass
    def CreatePortEvaluatorBuilder(part: NXOpen.Part, portEvaluator: ExpressionEvaluator) -> PortEvaluatorBuilder:
        """
         Creates a NXOpen.AME.PortEvaluatorBuilder 
         Returns builder ( PortEvaluatorBuilder NXOp): .
        """
        pass
    def CreatePortsManagerBuilder(part: NXOpen.Part, portsContainer: NXOpen.NXObject) -> PortsManagerBuilder:
        """
         Creates a ports manager builder 
         Returns builder ( PortsManagerBuilder NXOp): .
        """
        pass
    def CreatePrimitiveSheetElementBuilder(part: NXOpen.Part) -> PrimitiveSheetElementBuilder:
        """
         Creates a AME.PrimitiveSheetElementBuilder 
         Returns builder ( PrimitiveSheetElementBuilder NXOp): .
        """
        pass
    def CreatePrintPagesBuilder(part: NXOpen.Part) -> PrintPagesBuilder:
        """
         Creates aAME.PrintPagesBuilder 
         Returns builder ( PrintPagesBuilder NXOp): .
        """
        pass
    def CreateProductBuilder(part: NXOpen.Part) -> CreateProductBuilder:
        """
         Creates a NXOpen.AME.CreateProductBuilder 
         Returns builder ( CreateProductBuilder NXOp): .
        """
        pass
    def CreateProductMatchingRulesBuilder(part: NXOpen.Part) -> ProductMatchingRulesBuilder:
        """
         Creates a NXOpen.AME.ProductMatchingRulesBuilder 
         Returns builder ( ProductMatchingRulesBuilder NXOp): .
        """
        pass
    def CreateProductPropertyRulesBuilder(part: NXOpen.Part) -> ProductPropertyRulesBuilder:
        """
         Creates a AME.ProductPropertyRulesBuilder 
         Returns builder ( ProductPropertyRulesBuilder NXOp): .
        """
        pass
    def CreateProductSelectionBuilder(part: NXOpen.Part) -> ProductSelectionBuilder:
        """
         Creates a NXOpen.AME.ProductSelectionBuilder 
         Returns builder ( ProductSelectionBuilder NXOp): .
        """
        pass
    def CreateProjectEngineeringObjectBuilder(part: NXOpen.Part) -> ProjectEngineeringObjectBuilder:
        """
         Creates a NXOpen.AME.ProjectEngineeringObjectBuilder 
         Returns builder ( ProjectEngineeringObjectBuilder NXOp): .
        """
        pass
    def CreateProjectSymbolAnnotationBuilder(part: NXOpen.Part, annotation: NXOpen.NXObject) -> ProjectSymbolAnnotationBuilder:
        """
         Creates a NXOpen.AME.ProjectSymbolAnnotationBuilder 
         Returns builder ( ProjectSymbolAnnotationBuilder NXOp): .
        """
        pass
    def CreatePropertyEvaluatorBuilder(part: NXOpen.Part, propertyEvaluator: ExpressionEvaluator) -> PropertyEvaluatorBuilder:
        """
         Creates a NXOpen.AME.PropertyEvaluatorBuilder 
         Returns builder ( PropertyEvaluatorBuilder NXOp): .
        """
        pass
    def CreateQueryBuilder(part: NXOpen.Part) -> QueryBuilder:
        """
        Creates a NXOpen.AME.QueryBuilder
         Returns builder ( QueryBuilder NXOp): .
        """
        pass
    def CreateQueryFolder(parentNode: AMEBaseNode) -> QueryFolder:
        """
         Creates a NXOpen.AME.QueryFolder 
         Returns newFolder ( QueryFolder NXOp): .
        """
        pass
    def CreateRenamePlugsAndStripsBuilder(part: NXOpen.Part) -> RenamePlugsAndStripsBuilder:
        """
         Creates a builder for the user nming using rename plugs and strips dialog
         Returns builder ( RenamePlugsAndStripsBuilder NXOp): .
        """
        pass
    def CreateReportBuilder(part: NXOpen.Part) -> CreateReportBuilder:
        """
         Creates a NXOpen.AME.CreateReportBuilder. This is only for native mode.
         Returns builder ( CreateReportBuilder NXOp): .
        """
        pass
    def CreateReportDefinitionBuilder(part: NXOpen.Part) -> ReportDefinitionBuilder:
        """
        Creates a NXOpen.AME.ReportDefinitionBuilder
         Returns builder ( ReportDefinitionBuilder NXOp): .
        """
        pass
    def CreateReportDefinitionFolder(parentNode: AMEBaseNode) -> ReportDefinitionFolder:
        """
         Creates a NXOpen.AME.ReportDefinitionFolder 
         Returns newFolder ( ReportDefinitionFolder NXOp): .
        """
        pass
    def CreateReportSettingsBuilder(part: NXOpen.Part) -> ReportSettingsBuilder:
        """
         Creates a builder for the report settings dialog
         Returns builder ( ReportSettingsBuilder NXOp): .
        """
        pass
    def CreateReportTemplateBuilder(part: NXOpen.Part) -> ReportTemplateBuilder:
        """
         Creates a NXOpen.AME.ReportTemplateBuilder 
         Returns builder ( ReportTemplateBuilder NXOp): .
        """
        pass
    def CreateReportsSettingsBuilder(part: NXOpen.Part) -> ReportsSettingsBuilder:
        """
         Creates a NXOpen.AME.ReportsSettingsBuilder 
         Returns builder ( ReportsSettingsBuilder NXOp): .
        """
        pass
    def CreateSaveToLibraryBuilder(part: NXOpen.Part) -> SaveToLibraryBuilder:
        """
         Creates a NXOpen.AME.SaveToLibraryBuilder 
         Returns builder ( SaveToLibraryBuilder NXOp): .
        """
        pass
    def CreateSchematicSymbolConfigurationBuilder(part: NXOpen.Part) -> SchematicSymbolConfigurationBuilder:
        """
         Creates a NXOpen.AME.SchematicSymbolConfigurationBuilder 
         Returns builder ( SchematicSymbolConfigurationBuilder NXOp): .
        """
        pass
    def CreateSelectAttrPropSourceBuilder(part: NXOpen.Part) -> SelectAttrPropSourceBuilder:
        """
         Creates a AME.SelectAttrPropSourceBuilder 
         Returns builder ( SelectAttrPropSourceBuilder NXOp): .
        """
        pass
    def CreateSelectConditionBuilder(part: NXOpen.Part) -> SelectConditionBuilder:
        """
         Creates a NXOpen.AME.SelectConditionBuilder 
         Returns builder ( SelectConditionBuilder NXOp): .
        """
        pass
    def CreateShieldBuilder(part: NXOpen.Part, shield: AMEExtendedObject) -> ShieldBuilder:
        """
         Creates a NXOpen.AME.ShieldBuilder 
         Returns builder ( ShieldBuilder NXOp): .
        """
        pass
    def CreateShowHideObjectsBuilder(part: NXOpen.Part) -> ShowHideObjectsBuilder:
        """
         Create ShowHide Objects Builder 
         Returns builder ( ShowHideObjectsBuilder NXOp): .
        """
        pass
    def CreateSinCatMappingBuilder(part: NXOpen.Part) -> SinCatMappingBuilder:
        """
         Creates a NXOpen.AME.SinCatMappingBuilder 
         Returns builder ( SinCatMappingBuilder NXOp): .
        """
        pass
    def CreateSmartPdfPrintPagesBuilder(part: NXOpen.Part) -> SmartPDFPrintPagesBuilder:
        """
         Creates a AME.SmartPDFPrintPagesBuilder 
         Returns builder ( SmartPDFPrintPagesBuilder NXOp): .
        """
        pass
    def CreateSnap3dmodelsBuilder(part: NXOpen.Part) -> Snap3DModelsBuilder:
        """
         Creates a NXOpen.AME.Snap3DModelsBuilder 
         Returns builder ( Snap3DModelsBuilder NXOp): .
        """
        pass
    def CreateSubnetBuilder(part: NXOpen.Part) -> SubnetBuilder:
        """
         Creates a NXOpen.AME.SubnetBuilder 
         Returns builder ( SubnetBuilder NXOp): .
        """
        pass
    def CreateSumEvaluatorBuilder(part: NXOpen.Part, sumEvaluator: ExpressionEvaluator) -> SumEvaluatorBuilder:
        """
         Creates a AME.SumEvaluatorBuilder 
         Returns builder ( SumEvaluatorBuilder NXOp): .
        """
        pass
    def CreateSymbolAnnotationBuilder(part: NXOpen.Part) -> SymbolAnnotationBuilder:
        """
         Creates a NXOpen.AME.SymbolAnnotationBuilder 
         Returns builder ( SymbolAnnotationBuilder NXOp): .
        """
        pass
    def CreateSymbolAuthoringBuilder(part: NXOpen.Part) -> SymbolAuthoringBuilder:
        """
         Creates a NXOpen.AME.SymbolAuthoringBuilder 
         Returns builder ( SymbolAuthoringBuilder NXOp): .
        """
        pass
    def CreateSymbolNoteBuilder(part: NXOpen.Part, annotation: NXOpen.Annotations.SimpleDraftingAid) -> SymbolNoteBuilder:
        """
         Creates a AME.SymbolNoteBuilder 
         Returns builder ( SymbolNoteBuilder NXOp): .
        """
        pass
    def CreateSymbolVariantBuilder(part: NXOpen.Part) -> SymbolVariantBuilder:
        """
         Creates a AME.SymbolVariantBuilder 
         Returns builder ( SymbolVariantBuilder NXOp): .
        """
        pass
    def CreateTagtable(plcFolder: AMEBaseNode, name: str, isDefaultTagTable: bool) -> AMEBaseNode:
        """
         Creates a object of plc tag 
         Returns tagTableNode ( AMEBaseNode NXOp): .
        """
        pass
    def CreateTeeJunctionBuilder(part: NXOpen.Part) -> TeeJunctionBuilder:
        """
         Creates a NXOpen.AME.TeeJunctionBuilder 
         Returns builder ( TeeJunctionBuilder NXOp): .
        """
        pass
    def CreateTemplateBuilder(part: NXOpen.Part) -> CreateTemplateBuilder:
        """
         Creates a NXOpen.AME.CreateTemplateBuilder 
         Returns builder ( CreateTemplateBuilder NXOp): .
        """
        pass
    def CreateTemplateDefinitionBuilder(part: NXOpen.Part) -> CreateTemplateDefinitionBuilder:
        """
         Creates a NXOpen.AME.CreateTemplateDefinitionBuilder 
         Returns builder ( CreateTemplateDefinitionBuilder NXOp): .
        """
        pass
    def CreateTiaPortalProjectSettingsBuilder(part: NXOpen.Part) -> TiaPortalProjectSettingsBuilder:
        """
         Creates an TiaPortalSettingsBuilder 
         Returns builder ( TiaPortalProjectSettingsBuilder NXOp): .
        """
        pass
    def CreateTransferFileDataBuilder(part: NXOpen.Part, importNodeTag: ImportNode) -> TransferFileDataBuilder:
        """
         Creates a NXOpen.AME.TransferFileDataBuilder 
         Returns builder ( TransferFileDataBuilder NXOp): .
        """
        pass
    def CreateTypeMappingListBuilder(part: NXOpen.Part) -> TypeMappingListBuilder:
        """
         Creates a NXOpen.AME.TypeMappingListBuilder 
         Returns builder ( TypeMappingListBuilder NXOp): .
        """
        pass
    def CreateUnloadLineDesignerBuilder(part: NXOpen.Part) -> UnloadLineDesignerBuilder:
        """
         Creates a NXOpen.AME.UnloadLineDesignerBuilder 
         Returns builder ( UnloadLineDesignerBuilder NXOp): .
        """
        pass
    def CreateUpdateLibraryObjectsBuilder(part: NXOpen.Part) -> UpdateLibraryObjectsBuilder:
        """
         Creates a AME.UpdateLibraryObjectsBuilder 
         Returns builder ( UpdateLibraryObjectsBuilder NXOp): .
        """
        pass
    def CreateUpdateObjectsBuilder(part: NXOpen.Part) -> UpdateObjectsBuilder:
        """
         Creates a AME.UpdateObjectsBuilder 
         Returns builder ( UpdateObjectsBuilder NXOp): .
        """
        pass
    def CreateUserConstants(parent: AMEBaseNode) -> List[AMEBaseNode]:
        """
         Create plc user constants under provided node 
         Returns newObjects ( AMEBaseNode List[NX): .
        """
        pass
    def CreateValueSetBuilder(part: NXOpen.Part) -> ValueSetBuilder:
        """
         Creates a AME.ValueSetBuilder 
         Returns builder ( ValueSetBuilder NXOp): .
        """
        pass
    def CreateVariableInterfaceMember(parentVariable: PlcInterfaceVariable, sourceIMP: InterfaceMemberPort, sourceImpPath: str) -> VariableInterfaceMemberPort:
        """
         JA class to create variable interface member 
         Returns varMember ( VariableInterfaceMemberPort NXOp): .
        """
        pass
    def CreateViewPages() -> None:
        """
         Creates Cabinet and Mechanical Data View Pages
        """
        pass
    def CutObjects(objectsToCut: List[INodeObject]) -> None:
        """
         Cuts objects and places them on the clipboard 
        """
        pass
    def DefineAspectBuilder(part: NXOpen.Part) -> DefineAspectBuilder:
        """
         Creates a NXOpen.AME.DefineAspectBuilder 
         Returns builder ( DefineAspectBuilder NXOp): .
        """
        pass
    def DeleteApplicationBuilder() -> None:
        """
         Deletes the NXOpen.AME.ApplicationBuilder 
        """
        pass
    def DeleteBrokenEoLinkToLdObject(engObj: IEngObject) -> None:
        """
         Delete a Broken EO - LD Mapping Link 
        """
        pass
    def DeleteBrokenTemplateLinkToLdObject(tc: NXOpen.NXObject) -> None:
        """
         Delete a Broken template - LD Mapping Link 
        """
        pass
    def DeleteEnd() -> None:
        """
         End of the delete
        """
        pass
    def DeleteExpressionEvaluatornode(evaluator: ExpressionEvaluator) -> None:
        """
         Delete a AME.ExpressionEvaluator 
        """
        pass
    def DeleteLabel(label: AMEEngineeringObjectLabel) -> None:
        """
         Deletes an Engineering Object Label 
        """
        pass
    def DeleteObject(obj: NXOpen.NXObject) -> None:
        """
         Delete the AME object 
        """
        pass
    def DeleteSingleAspect(obj: AspectNode) -> None:
        """
         Delete the AME aspect node object and the connected EO as well as all children in all aspects 
        """
        pass
    def DeregisterVisualreportingObjects() -> None:
        """
         Deregister Visual Reporting Objects 
        """
        pass
    def DoDelete() -> None:
        """
         Start to delete
        """
        pass
    def DoDeleteWithUpdate() -> None:
        """
         Start to delete with update
        """
        pass
    def EditTarget(targetID: str) -> NXOpen.Part:
        """
         Set the target to be edited, target can be Type or Template, targetID is the DB id from the Teamcenter 
         Returns workSet ( NXOpen.Part): .
        """
        pass
    def EnterEclassEnv() -> NXOpen.Part:
        """
         Entering an eClass environment 
         Returns workSet ( NXOpen.Part): .
        """
        pass
    def EnterEplanEnv() -> NXOpen.Part:
        """
         Entering an Eplan environment 
         Returns workSet ( NXOpen.Part): .
        """
        pass
    def EstablishChildren(parent: NXOpen.NXObject) -> None:
        """
         Establish the children 
        """
        pass
    def ExportPartialTiaProject(selectedStations: List[AMEBaseNode], fullPath: str, isExistingProject: bool, openInTia: bool, compileInTia: bool, objectsToExport: List[str], stationsToUpdateInTia: List[str], sendWithDistributedIOs: bool, ignoreConfigureError: bool, overwriteOnCollision: bool) -> str:
        """
         Exports tia to external tool 
         Returns compileResult (str): .
        """
        pass
    def ExportTiaProject(selectedStations: List[AMEBaseNode], fullPath: str, isExistingProject: bool, openInTia: bool, compileInTia: bool, sendWithSwAndTags: bool, sendWithDistributedIOs: bool, ignoreConfigureError: bool) -> str:
        """
         Exports tia to external tool 
         Returns compileResult (str): .
        """
        pass
    def ExportToAutomationMl(selectedStations: List[AMEBaseNode], objectsToExport: List[str], sendWithDistributedIOs: bool, automationMLFileFullPath: str, targetSystem: str) -> str:
        """
         Exports to AutomationML 
         Returns compileResult (str): .
        """
        pass
    def FindPartfile(prtFileName: str, libType: AMEManager.JaNativeLibType) -> str:
        """
         Find a partfile's absolute path  
         Returns prtFilePath (str):  returns absolute file path of mypart.prt, will be an empty string if no .prt was found .
        """
        pass
    def FindPartfileInDirs(prtFileName: str, dirs: List[str]) -> str:
        """
         Find a partfile's absolute path in a given list of directory paths
         Returns prtFilePath (str):  returns absolute file path of mypart.prt, will be an empty string if no .prt was found .
        """
        pass
    def FullLoadStations(stations: List[AMEBaseNode]) -> None:
        """
         Full load station objects 
        """
        pass
    def GetAllTemplateSolutions(part: NXOpen.Part) -> List[NXOpen.NXObject]:
        """
          Gets all the solution templates in the input template part 
         Returns templateSolutions ( NXOpen.NXObject Li): .
        """
        pass
    def GetAllTemplateVariantObjects(part: NXOpen.Part) -> List[NXOpen.NXObject]:
        """
          Gets all the variants and variant selections in the input template part 
         Returns templateVariantObjects ( NXOpen.NXObject Li): .
        """
        pass
    def GetApplicationBuilder() -> ApplicationBuilder:
        """
         Return the NXOpen.AME.ApplicationBuilder 
         Returns builder ( ApplicationBuilder NXOp): .
        """
        pass
    def GetCopiedExtractAttributeEvaluatorInBulk(uiExp: NXOpen.Expression, targetCategoryName: str, targetPropName: str, destinationCellObjectTag: NXOpen.NXObject) -> Tuple[ExpressionEvaluator, List[NXOpen.Expression]]:
        """
         Get Copied Extract Attribute Evaluator 
         Returns A tuple consisting of (outputExtractEval, copiedExp). 
         - outputExtractEval is:  ExpressionEvaluator NXOp.
         - copiedExp is:  NXOpen.Expression Li.

        """
        pass
    def GetCurrentDrawingsHeight(part: NXOpen.Part) -> int:
        """
         Return a Symbol's drawing's heights in pixels
                
         Returns sheetHeightPx (int):  sheet height in pixels .
        """
        pass
    def GetFeatureRecord(part: NXOpen.Part) -> NXOpen.Features.Feature:
        """
         Get feature record 
         Returns feature ( NXOpen.Features.Feature): .
        """
        pass
    def GetLatestItemRevision(itemId: str) -> str:
        """
         Find an item id's recent available revision
         Returns latestRevision (str):  returns latest revision or empty string if itemId could not be found .
        """
        pass
    def GetLdCachedAttribute(eo: NXOpen.NXObject) -> LDCachedAttribute:
        """
         Returns the AME.LDCachedAttribute
         Returns extObject ( LDCachedAttribute NXOp): .
        """
        pass
    def GetOwningCable(physicalConnection: AMEExtendedObject) -> IEngObject:
        """
         Get owning cable from given Physical Connection
         Returns cable ( IEngObject NXOp): .
        """
        pass
    def GetSelectedQueryFromLibrary() -> AMEQuery:
        """
         Get the selected query from Reuse Library 
         Returns queryObject ( AMEQuery NXOp): .
        """
        pass
    def GetSelectedReportdefinitionFromLibrary() -> ReportDefinition:
        """
         Get the selected report definition from Reuse Library  
         Returns reportDefinition ( ReportDefinition NXOp): .
        """
        pass
    def GetValueSetsPopertyOwners(valueSets: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
          Gets the value set property owner objects 
         Returns copiedObjects ( NXOpen.NXObject Li): .
        """
        pass
    def HideShowLdObject(ldObject: NXOpen.NXObject, hide: bool) -> None:
        """
         HideShow a LD object 
        """
        pass
    def LadderDataBuilder(part: NXOpen.Part) -> LadderDataBuilder:
        """
         Creates a AME.LadderDataBuilder 
         Returns builder ( LadderDataBuilder NXOp): .
        """
        pass
    def LoadConnectedEos(objects: List[IEngObject]) -> None:
        """
         Loads connected Engineering objects 
        """
        pass
    def LoadExternalObjects(project: Project) -> None:
        """
         Load external objects 
        """
        pass
    def LoadPartfile(prtFileName: str, libType: AMEManager.JaNativeLibType) -> NXOpen.Part:
        """
         Find a partfile's absolute path and load it if not loaded already 
         Returns loadedPart ( NXOpen.Part): .
        """
        pass
    def LoadProductDefinition(reusePartName: str) -> ProductDefinition:
        """
         Loads the Product Defintion
         Returns product ( ProductDefinition NXOp): .
        """
        pass
    def LoadStationSymbols(plcStationNode: AMEBaseNode) -> None:
        """
         Load objects related to tag tables
        """
        pass
    def MapLdObject(ldObject: NXOpen.NXObject, eo: IEngObject) -> None:
        """
         Map a LD object to an eo 
        """
        pass
    def MapLdObjectToTemplate(ldObject: NXOpen.NXObject, tc: NXOpen.NXObject) -> None:
        """
         Map a LD object to a template
        """
        pass
    def MigrateProject(project: Project) -> None:
        """
         Migrate input project 
        """
        pass
    def MoveLabel(label: AMEEngineeringObjectLabel, targetPosition: NXOpen.Point3d) -> None:
        """
         Moves an Engineering Object Label 
        """
        pass
    def MoveNavigatorNodes(obj: INodeObject, nodesToMove: List[INodeObject], dropType: AMEManager.MoveNavigatorNodesType) -> None:
        """
         Moves Navigator nodes under same parent 
        """
        pass
    def PasteObjects(parent: INodeObject) -> Tuple[AMEManager.PasteStatus, List[INodeObject]]:
        """
         Pastes objects from the clipboard under given parent 
         Returns A tuple consisting of (pasteStatus, copiedObjects). 
         - pasteStatus is:  AMEManager.PasteStatus NXOp.
         - copiedObjects is:  INodeObject List[NX.

        """
        pass
    def PlaceInAspect(objects: List[AMEExtendedObject], parent: INodeObject) -> None:
        """
         Place objects under object present in another aspect navigator  
        """
        pass
    def PopulateEoPropertiesOnBomline(project: Project) -> None:
        """
         Populates mapped Engineering properties on linked BOM line 
        """
        pass
    def PublishCollaborationContextToProject(project: Project) -> None:
        """
         Publishes collaboration context of the input project 
        """
        pass
    def PublishGlobalDefaultProjectSettings() -> None:
        """
         Save default project settings item 
        """
        pass
    def PublishSubsetConfiguration(subsetInstance: NXOpen.Assemblies.Subset) -> None:
        """
         Publish subset configuration 
        """
        pass
    def RecalculatePlcAddresses(node: AMEBaseNode) -> None:
        """
         Calculates addresses of all the plc related objects inside stations
        """
        pass
    def ReevaluateEvaluators(objects: List[ExpressionEvaluator]) -> None:
        """
         Reevaluate given evaluators
        """
        pass
    def ReevaluateTagtable(baseNode: AMEBaseNode) -> None:
        """
         Reevaluate tag table in selected Plc Station or Plc Symbol Folder
        """
        pass
    def RegisterVisualreportingObjects() -> None:
        """
         Register Visual Reporting Objects 
        """
        pass
    def ReloadProject(projectTag: NXOpen.NXObject) -> Project:
        """
         Reload of project 
         Returns project ( Project NXOp): .
        """
        pass
    def RemoveComponent(component: NXOpen.Assemblies.Component) -> None:
        """
         Removes component from given assembly 
        """
        pass
    def RemoveExternalLibraryReference(tagOfplcHwItems: List[AMEBaseNode]) -> None:
        """
         Remove external library reference 
        """
        pass
    def RemoveFolders(folder: AMEBaseNode) -> None:
        """
         Removes all folders under selected subfolder folder without deleting blocks
        """
        pass
    def RemoveFreeTextObjectFromContainer(objectTag: NXOpen.TaggedObject) -> None:
        """
         Removes the object(NXOpen.Diagramming.Annotation or NXOpen.Diagramming.Tables.CellBuilder)
                    holding free text from FreeTextContainer object 
        """
        pass
    def RemoveFromGroup(group: AMEGroup, eoTag: IEngObject) -> None:
        """
         Removes an engineering object from a group 
        """
        pass
    def RemoveHwItemFromAutomationNavigator(obj: NXOpen.NXObject) -> None:
        """
          Remove hw item and assigned tags from automation navigator 
        """
        pass
    def RemoveTagtable(selectedSymbolTables: List[AMEBaseNode]) -> None:
        """
         Remove a selected tag-table objects
        """
        pass
    def RemoveTagtables(selectedSymbolFolders: List[AMEBaseNode]) -> None:
        """
         Remove the tag tables in selected Plc symbol folders
        """
        pass
    def ReportThisProperty(propertDescriptorID: str, userData: str) -> None:
        """
         Creates a visual report for given attribute 
        """
        pass
    def ReportValueSets() -> None:
        """
         Generates the report for value set data 
        """
        pass
    def ResetEclassDataMapping(versionNode: AMEBaseNode) -> None:
        """
         Reset Eplan Data Mapping
        """
        pass
    def ResetEplanDataMapping() -> None:
        """
         Reset Eplan Data Mapping
        """
        pass
    def ResetNaming(obj: NXOpen.NXObject) -> None:
        """
         Apply naming rule 
        """
        pass
    def RevaluateFolders(node: AMEBaseNode) -> None:
        """
         Removes all folders under selected subfolder folder without deleting blocks
        """
        pass
    def SelectAndHighlightBuilder(part: NXOpen.Part) -> SelectAndHighlightBuilder:
        """
         Creates a NXOpen.AME.SelectAndHighlightBuilder 
         Returns builder ( SelectAndHighlightBuilder NXOp): .
        """
        pass
    def SetCopyAdditionalObjects(copyOption: bool) -> None:
        """
         Set the copy additional object option
        """
        pass
    def SetCutLength(editObject: AMEEngObject, cutLength: float) -> None:
        """
         Set cut Length 
        """
        pass
    def SetDeleteConditionalObject(deleteOption: bool) -> None:
        """
         Set the delete option
        """
        pass
    @overload
    def SetDomainRelevancyNotRelevant(partOccTag: NXOpen.Assemblies.Component) -> None:
        """
         Set the external object domain relevancy not relevant to automation domain 
        """
        pass
    @overload
    def SetDomainRelevancyNotRelevantToNoStatus(partOccTag: NXOpen.Assemblies.Component) -> None:
        """
         Set the external object domain relevancy from not relevant to no status in context to automation domain 
        """
        pass
    @overload
    def SetDomainRelevancyNotRelevantToNoStatus(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the external object domain relevancy from not relevant to no status in context to automation domain for a list of external objects 
        """
        pass
    @overload
    def SetDomainRelevancyNotRelevant(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the external object domain relevancy not relevant to automation domain for a list of external objects 
        """
        pass
    @overload
    def SetDomainRelevancyRelevant(partOccTag: NXOpen.Assemblies.Component) -> None:
        """
         Set the external object domain relevancy to relevant in context to automation domain 
        """
        pass
    @overload
    def SetDomainRelevancyRelevantToNoStatus(partOccTag: NXOpen.Assemblies.Component) -> None:
        """
         Set the external object domain relevancy from relevant to no status in context to automation domain 
        """
        pass
    @overload
    def SetDomainRelevancyRelevantToNoStatus(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the external object domain relevancy from relevant to no status in context to automation domain for a list of external objects 
        """
        pass
    @overload
    def SetDomainRelevancyRelevant(components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the external object domain relevancy to relevant in context to automation domain for a list of external objects 
        """
        pass
    def SetHostName(hostName: str) -> None:
        """
         Set the host name 
        """
        pass
    def SetObjectsToBeDeleted(objects: List[NXOpen.NXObject], deleteType: AMEManager.DeleteType) -> None:
        """
         Set the objects to be deleted
        """
        pass
    def SetWorkPart(workpart: NXOpen.Part) -> NXOpen.Part:
        """
         Set work part 
         Returns oldWorkpart ( NXOpen.Part): .
        """
        pass
    def ShowOnly(objects: List[NXOpen.Assemblies.Component]) -> None:
        """
         Show only object 
        """
        pass
    def SubmitEngObjectDelete() -> None:
        """
         Submit the delete of EOs 
        """
        pass
    def SubmitQueryObjectDelete() -> None:
        """
         Submit the delete of Query Objects 
        """
        pass
    def SwapCableCores(sourceObject: AMEExtendedObject, targetObject: AMEExtendedObject) -> None:
        """
         Swaps cable cores 
        """
        pass
    def UnassignEplanMacros(isUnassignedAll: bool) -> None:
        """
         Unassign all eplan macros 
        """
        pass
    def UnassignMacros(isUnassignedAll: bool) -> int:
        """
         Unassign all eplan macros 
         Returns numUnAssignedObjs (int): .
        """
        pass
    def UnassignPlcblock(obj: PlcBlock) -> None:
        """
         Unassign the Plc Block to from a PLC
        """
        pass
    def UnloadExternalObjects(project: Project) -> None:
        """
         Unload external objects 
        """
        pass
    def UnloadPart(partTag: NXOpen.NXObject) -> None:
        """
         Unloads a part even if modified
        """
        pass
    def UnloadProject(project: NXOpen.NXObject) -> None:
        """
         Unload of template or definition project  
        """
        pass
    def UnmapLdObject(ldObject: NXOpen.NXObject, keepTypeMapped: bool) -> None:
        """
         Unmap a LD object 
        """
        pass
    def UnmapTemplate(templateId: str) -> None:
        """
         Unmap a template 
        """
        pass
    def UpdateAllNames() -> None:
        """
         Update all the node's name based on the naming rule 
        """
        pass
    def UpdateCollaborationContext() -> None:
        """
         Updates the collaboration context 
        """
        pass
    def UpdateEclassProductDataMapping(versionNode: AMEBaseNode, overrideMapping: bool) -> None:
        """
         Update the product data mapping
        """
        pass
    def UpdateEvaluators(objects: List[AMEExtendedObject]) -> None:
        """
         Log evaluators for update from given objects
        """
        pass
    def UpdateSortingPreferences(navKey: str, navOrder: AMEManager.JaOrderType, sorted: AMEManager.JaNavigatorSortedState) -> None:
        """
         Update navigator sorting order on sorting manager 
        """
        pass
    def UpgradeMappingsRevision() -> None:
        """
         Upgrade all the instance mappings of the project to the new loaded revision
        """
        pass
    def ValidateForModification(objectTag: NXOpen.NXObject) -> None:
        """
         Validate if object is modifiable
        """
        pass
    def ValidatePlcStation(objectsToExport: List[str]) -> None:
        """
         Validate Station 
        """
        pass
import NXOpen
class AMENamingRule(NXOpen.NXObject): 
    """ Represents Naming Rule Object """
    pass
class AmeOpticalConnectionFiberType(Enum):
    """
    Members Include: 
     |SingleMode| 
     |MultiMode| 
     |Undefined| 
     |Invalid| 

    """
    SingleMode: int
    MultiMode: int
    Undefined: int
    Invalid: int
    @staticmethod
    def ValueOf(value: int) -> AmeOpticalConnectionFiberType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AMEPlcHwItem(AMEBaseNode): 
    """ Represents Plc Hw Item """
    pass
class AmePlcStatechartConditionOperatortype(Enum):
    """
    Members Include: 
     |And| 
     |Or| 
     |Equal| 
     |NotEqual| 
     |LessThan| 
     |GreaterThan| 
     |LessThanOrEqual| 
     |GreaterThanOrEqual| 

    """
    And: int
    Or: int
    Equal: int
    NotEqual: int
    LessThan: int
    GreaterThan: int
    LessThanOrEqual: int
    GreaterThanOrEqual: int
    @staticmethod
    def ValueOf(value: int) -> AmePlcStatechartConditionOperatortype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AMEPort(AMEExtendedObject): 
    """ Represents Port """
    def GetPhysicalConnections(self) -> List[AMEExtendedObject]:
        """
         Get the physical connections with this port as one of the end - either source or target port
         Returns physicalConnections ( AMEExtendedObject List[NX): .
        """
        pass
import NXOpen
class AMEQueryGroup(NXOpen.NXObject): 
    """ The Query Group """
    pass
import NXOpen
class AMEQuery(NXOpen.NXObject): 
    """ The Query Object """
    @overload
    def ExecuteQuery(self) -> List[AMEEngObject]:
        """
         Execute query and get engineering objects as result 
         Returns engObjects ( AMEEngObject List[NX): .
        """
        pass
    def ExecuteQueryWithTargetsWithoutLoading(self) -> QueryResult:
        """
         Execute query and get result without loading 
         Returns queryResult ( QueryResult NXOp): .
        """
        pass
    @overload
    def ExecuteQuery(self, isPreview: bool) -> List[AMEEngObject]:
        """
         Execute query. 
         Returns engObjects ( AMEEngObject List[NX): .
        """
        pass
    @overload
    def ExecuteQuery(self) -> QueryResult:
        """
         Execute query and get result 
         Returns queryResult ( QueryResult NXOp): .
        """
        pass
    def GetDescription(self) -> str:
        """
         Get the description 
         Returns text (str): .
        """
        pass
    def GetName(self) -> str:
        """
         Get the Name 
         Returns text (str): .
        """
        pass
    def GroupClauses(self, clauses: List[NXOpen.NXObject]) -> None:
        """
         Group query clauses 
        """
        pass
    def InsertClauseBefore(self, referenceClause: NXOpen.NXObject, clause: QueryClause) -> None:
        """
         Insert clause before reference clause 
        """
        pass
    def ModifySearchScope(self, text: str) -> None:
        """
         Change the search scope of query object 
        """
        pass
    def RemoveClause(self, removedClauses: List[int]) -> None:
        """
         Remove clause from Query 
        """
        pass
    def RemoveClauses(self, clauses: List[NXOpen.NXObject]) -> None:
        """
         Remove clauses from Query 
        """
        pass
    def SetDescription(self, text: str) -> None:
        """
         Set the modified description 
        """
        pass
    def SetName(self, text: str) -> None:
        """
         Set the modified name 
        """
        pass
    def SetPreview(self, isPreview: bool) -> None:
        """
         Set preview flag 
        """
        pass
    def UngroupClauses(self, clauses: List[NXOpen.NXObject]) -> None:
        """
         Ungroup query clauses 
        """
        pass
import NXOpen
class AMEReportRule(NXOpen.NXObject): 
    """ Represents Report Rule Object """
    pass
class AmeSymbolAnnotationAnchor(Enum):
    """
    Members Include: 
     |TopLeft| 
     |TopCenter| 
     |TopRight| 
     |MiddleLeft| 
     |MiddleCenter| 
     |MiddleRight| 
     |BottomLeft| 
     |BottomCenter| 
     |BottomRight| 

    """
    TopLeft: int
    TopCenter: int
    TopRight: int
    MiddleLeft: int
    MiddleCenter: int
    MiddleRight: int
    BottomLeft: int
    BottomCenter: int
    BottomRight: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationAnchor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationAttributesource(Enum):
    """
    Members Include: 
     |Unknown|  Should not be used 
     |Type| 
     |Product| 
     |General| 
     |AspectFunction| 
     |AspectLocation| 
     |AspectProduct| 
     |CrossReference| 

    """
    Unknown: int
    Type: int
    Product: int
    General: int
    AspectFunction: int
    AspectLocation: int
    AspectProduct: int
    CrossReference: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationAttributesource:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationContactblock(Enum):
    """
    Members Include: 
     |InPath| 
     |OnComponent| 

    """
    InPath: int
    OnComponent: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationContactblock:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationJustification(Enum):
    """
    Members Include: 
     |Left| 
     |Center| 
     |Right| 

    """
    Left: int
    Center: int
    Right: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationJustification:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationLetteringangle(Enum):
    """
    Members Include: 
     |Degree0| 
     |Degree45| 
     |Degree90| 
     |Degree135| 
     |Degree180| 
     |Degree270| 
     |Degree315| 

    """
    Degree0: int
    Degree45: int
    Degree90: int
    Degree135: int
    Degree180: int
    Degree270: int
    Degree315: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationLetteringangle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationPropertytype(Enum):
    """
    Members Include: 
     |ObjectProperties| 
     |CrossReferences| 
     |AspectProperties| 

    """
    ObjectProperties: int
    CrossReferences: int
    AspectProperties: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationPropertytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationTextOverflowMethod(Enum):
    """
    Members Include: 
     |Default| 
     |Wrap| 
     |Truncate| 
     |Overflowborder| 
     |Suffix| 

    """
    Default: int
    Wrap: int
    Truncate: int
    Overflowborder: int
    Suffix: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationTextOverflowMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeSymbolAnnotationType(Enum):
    """
    Members Include: 
     |Properties| 
     |ContactBlock| 

    """
    Properties: int
    ContactBlock: int
    @staticmethod
    def ValueOf(value: int) -> AmeSymbolAnnotationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeTeeJunctionType(Enum):
    """
    Members Include: 
     |HorizontalDown| 
     |HorizontalUp| 
     |VerticalLeft| 
     |VerticalRight| 
     |Invalid| 

    """
    HorizontalDown: int
    HorizontalUp: int
    VerticalLeft: int
    VerticalRight: int
    Invalid: int
    @staticmethod
    def ValueOf(value: int) -> AmeTeeJunctionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AmeTeeJunctionVariant(Enum):
    """
    Members Include: 
     |One| 
     |Two| 
     |Three| 

    """
    One: int
    Two: int
    Three: int
    @staticmethod
    def ValueOf(value: int) -> AmeTeeJunctionVariant:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AncestorEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates an ancestor for a given aspect and a starting point """
    class JaAspectEvaluatorBuilderNavCriteria(Enum):
        """
        Members Include: 
         |ByLevels| 
         |ByProperty| 

        """
        ByLevels: int
        ByProperty: int
        @staticmethod
        def ValueOf(value: int) -> AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavCriteria:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaAspectEvaluatorBuilderNavDirection(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 

        """
        Up: int
        Down: int
        @staticmethod
        def ValueOf(value: int) -> AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectSelection(self) -> BaseEvaluatorBuilder.ContextType:
        """
        Getter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @AspectSelection.setter
    def AspectSelection(self, aspectSelection: BaseEvaluatorBuilder.ContextType):
        """
        Setter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @property
    def NavCriteria(self) -> AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavCriteria:
        """
        Getter for property: ( AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavCriteria NXOp) NavCriteria
         Returns the navigation criteria   
            
         
        """
        pass
    @NavCriteria.setter
    def NavCriteria(self, navCriteria: AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavCriteria):
        """
        Setter for property: ( AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavCriteria NXOp) NavCriteria
         Returns the navigation criteria   
            
         
        """
        pass
    @property
    def NavDirection(self) -> AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavDirection:
        """
        Getter for property: ( AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavDirection NXOp) NavDirection
         Returns the navigation direction   
            
         
        """
        pass
    @NavDirection.setter
    def NavDirection(self, navDirection: AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavDirection):
        """
        Setter for property: ( AncestorEvaluatorBuilder.JaAspectEvaluatorBuilderNavDirection NXOp) NavDirection
         Returns the navigation direction   
            
         
        """
        pass
    @property
    def NumLevels(self) -> int:
        """
        Getter for property: (int) NumLevels
         Returns the navigation direction   
            
         
        """
        pass
    @NumLevels.setter
    def NumLevels(self, numLevels: int):
        """
        Setter for property: (int) NumLevels
         Returns the navigation direction   
            
         
        """
        pass
    @property
    def SelectedType(self) -> SelectionEngineeringObjectDefinitionBuilder:
        """
        Getter for property: ( SelectionEngineeringObjectDefinitionBuilder NXOp) SelectedType
         Returns the selected type  
            
         
        """
        pass
import NXOpen
class ApplicationBuilder(NXOpen.NXObject): 
    """ Create the AD application builder see AMEApplicationBuilder"""
    @overload
    def CreateCollaborativeDesign(self, workSet: NXOpen.Part) -> Project:
        """
          Create a CD for workset part.
         Returns project ( Project NXOp): .
        """
        pass
    @overload
    def CreateCollaborativeDesign(self, workSet: NXOpen.Part, cdID: str) -> Project:
        """
          Create a CD for workset part with predefined ID
         Returns project ( Project NXOp): .
        """
        pass
    def Enter(self) -> None:
        """
          Enter the Automation Designer application. 
        """
        pass
    def EstablishNewProject(self, workSet: NXOpen.Part) -> Project:
        """
          Create a new project for workset part.
         Returns project ( Project NXOp): .
        """
        pass
    def EstablishProject(self, uid: str) -> None:
        """
         Set collaborative design
        """
        pass
    def Exit(self) -> None:
        """
          Exit the Automation Designer application and delete builder.
        """
        pass
    def GetGlobalSelectionBuilder(self) -> GlobalSelectionBuilder:
        """
         Get the global selection builder
         Returns selectionBuilder ( GlobalSelectionBuilder NXOp): .
        """
        pass
    def GetProject(self) -> Project:
        """
         Get the project object
         Returns project ( Project NXOp): .
        """
        pass
    def SaveProject(self) -> None:
        """
          Save the current Automation Designer project.
        """
        pass
    def SetPartAttributes(self, workPart: NXOpen.Part, name: str, desc: str, id: str) -> None:
        """
          Set attributes on part.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class AspectBoxBuilder(NXOpen.Builder): 
    """ Represents builder for creating aspect box """
    class Variant(Enum):
        """
        Members Include: 
         |Vertical| 
         |Horizontal| 

        """
        Vertical: int
        Horizontal: int
        @staticmethod
        def ValueOf(value: int) -> AspectBoxBuilder.Variant:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectBoxVariant(self) -> AspectBoxBuilder.Variant:
        """
        Getter for property: ( AspectBoxBuilder.Variant NXOp) AspectBoxVariant
         Returns the aspect box variant   
            
         
        """
        pass
    @AspectBoxVariant.setter
    def AspectBoxVariant(self, aspectBoxVariant: AspectBoxBuilder.Variant):
        """
        Setter for property: ( AspectBoxBuilder.Variant NXOp) AspectBoxVariant
         Returns the aspect box variant   
            
         
        """
        pass
    @property
    def AspectDetails(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) AspectDetails
         Returns the aspect detail   
            
         
        """
        pass
    def CreateAspectBox(self, pageObject: PageObject) -> NXOpen.Diagramming.SheetElement:
        """
         Method to create the Sheet Element for Aspect Box 
         Returns sheetElement ( NXOpen.Diagramming.SheetElement): .
        """
        pass
    def SetLocation(self, cursorLocation: NXOpen.Point2d) -> None:
        """
         Set the location of aspect box
        """
        pass
class AspectBox(AMEExtendedObject): 
    """ Represents the AspectBox class. """
    pass
import NXOpen
class AspectDetailsBuilder(NXOpen.TaggedObject): 
    """
        JA Class for the Aspect Details UI Block
    """
    @property
    def SelectionParent(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionParent
         Returns the selection parent   
            
         
        """
        pass
    @property
    def ShowInAutomation(self) -> bool:
        """
        Getter for property: (bool) ShowInAutomation
         Returns the availability in Automation Navigator   
            
         
        """
        pass
    @ShowInAutomation.setter
    def ShowInAutomation(self, showInAutomation: bool):
        """
        Setter for property: (bool) ShowInAutomation
         Returns the availability in Automation Navigator   
            
         
        """
        pass
    @property
    def ShowInFunction(self) -> bool:
        """
        Getter for property: (bool) ShowInFunction
         Returns the availability in Function Aspect   
            
         
        """
        pass
    @ShowInFunction.setter
    def ShowInFunction(self, showInFunction: bool):
        """
        Setter for property: (bool) ShowInFunction
         Returns the availability in Function Aspect   
            
         
        """
        pass
    @property
    def ShowInLocation(self) -> bool:
        """
        Getter for property: (bool) ShowInLocation
         Returns the availability in Location Aspect   
            
         
        """
        pass
    @ShowInLocation.setter
    def ShowInLocation(self, showInLocation: bool):
        """
        Setter for property: (bool) ShowInLocation
         Returns the availability in Location Aspect   
            
         
        """
        pass
    @property
    def ShowInProduct(self) -> bool:
        """
        Getter for property: (bool) ShowInProduct
         Returns the availability in Product Aspect   
            
         
        """
        pass
    @ShowInProduct.setter
    def ShowInProduct(self, showInProduct: bool):
        """
        Setter for property: (bool) ShowInProduct
         Returns the availability in Product Aspect   
            
         
        """
        pass
import NXOpen
class AspectNavigatorPreferencesBuilder(NXOpen.Builder): 
    """
        JA class for aspect navigator builder
    """
    @property
    def OrderAspects(self) -> OrderAspectsBuilder:
        """
        Getter for property: ( OrderAspectsBuilder NXOp) OrderAspects
         Returns the order aspects builder   
            
         
        """
        pass
    @property
    def ShowHideObjects(self) -> ShowHideObjectsBuilder:
        """
        Getter for property: ( ShowHideObjectsBuilder NXOp) ShowHideObjects
         Returns the show hide objects builder   
            
         
        """
        pass
class AspectNode(AMEBaseNode): 
    """ Aspect Node Journaling class """
    pass
import NXOpen
class AspectPrefixBuilder(NXOpen.Builder): 
    """ represents the builder class which is used to define Aspect Prefixes and Delimiter for NXOpen.AME.Project """
    class DelimiterType(Enum):
        """
        Members Include: 
         |Dot|  A dot (.) is used as the delimiter 
         |AspectPrefix|  Aspect Prefix is used as the delimiter 
         |NoDelimiter|  No delimiter will be used 

        """
        Dot: int
        AspectPrefix: int
        NoDelimiter: int
        @staticmethod
        def ValueOf(value: int) -> AspectPrefixBuilder.DelimiterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoRenameOnMapping(self) -> bool:
        """
        Getter for property: (bool) AutoRenameOnMapping
         Returns the option to automatically rename AD object and its aspect names to mechanicallayout name upon mapping   
            
         
        """
        pass
    @AutoRenameOnMapping.setter
    def AutoRenameOnMapping(self, autoRenameOnMapping: bool):
        """
        Setter for property: (bool) AutoRenameOnMapping
         Returns the option to automatically rename AD object and its aspect names to mechanicallayout name upon mapping   
            
         
        """
        pass
    @property
    def Delimiter(self) -> AspectPrefixBuilder.DelimiterType:
        """
        Getter for property: ( AspectPrefixBuilder.DelimiterType NXOp) Delimiter
         Returns the  NXOpen::AME::AspectPrefixBuilder::DelimiterType    
            
         
        """
        pass
    @Delimiter.setter
    def Delimiter(self, delimiter: AspectPrefixBuilder.DelimiterType):
        """
        Setter for property: ( AspectPrefixBuilder.DelimiterType NXOp) Delimiter
         Returns the  NXOpen::AME::AspectPrefixBuilder::DelimiterType    
            
         
        """
        pass
    @property
    def Function(self) -> str:
        """
        Getter for property: (str) Function
         Returns the aspect prefix of function aspect   
            
         
        """
        pass
    @Function.setter
    def Function(self, functionPrefix: str):
        """
        Setter for property: (str) Function
         Returns the aspect prefix of function aspect   
            
         
        """
        pass
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
         Returns the aspect prefix of location aspect   
            
         
        """
        pass
    @Location.setter
    def Location(self, location: str):
        """
        Setter for property: (str) Location
         Returns the aspect prefix of location aspect   
            
         
        """
        pass
    @property
    def Product(self) -> str:
        """
        Getter for property: (str) Product
         Returns the aspect prefix of product aspect   
            
         
        """
        pass
    @Product.setter
    def Product(self, product: str):
        """
        Setter for property: (str) Product
         Returns the aspect prefix of product aspect   
            
         
        """
        pass
class AspectRoot(AMEBaseNode): 
    """ AspectRoot Node Journaling class """
    pass
import NXOpen
class AssignAspectBuilder(NXOpen.Builder): 
    """ Reassign a single aspect of an Engineering Object """
    @property
    def SelectionObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionObjects
         Returns the selection of objects to be reassigned   
            
         
        """
        pass
    @property
    def SelectionParent(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectionParent
         Returns the selection where the object will be reassigned.  
             
         
        """
        pass
class AssignmentPort(AMEExtendedObject): 
    """ Represents AssignmentPort """
    pass
import NXOpen
class AssignPlcAddressRuleSetBuilder(NXOpen.Builder): 
    """ Reassign plc address rule set to station """
    @property
    def SelectedRuleSettings(self) -> AddressRuleSettingsBuilder:
        """
        Getter for property: ( AddressRuleSettingsBuilder NXOp) SelectedRuleSettings
         Returns the selected rule settings  
            
         
        """
        pass
    def SetSelectedStations(self, stationNodes: List[AMEBaseNode]) -> None:
        """
         Set the selected stations
        """
        pass
import NXOpen
class AssignSubnetBuilder(NXOpen.Builder): 
    """ Reassign a single aspect of an Engineering Object """
    @property
    def SelectedComInterfaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedComInterfaces
         Returns the selection of com.  
           interfaces to be assigned  
         
        """
        pass
    @property
    def SelectedSubnet(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectedSubnet
         Returns the selection where the object will be reassigned.  
             
         
        """
        pass
import NXOpen.Tooling
class AssignTemplateToProductBuilder(AMEBaseBuilder): 
    """ Builder class to assign a template object to NXOpen.AME.ProductDefinition"""
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library item  
            
         
        """
        pass
class AssignTypeBuilder(AMEBaseBuilder): 
    """ Builder for selecting an engineering object definition"""
    @property
    def SelectBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectBaseDefinition
         Returns the base definition  
            
         
        """
        pass
import NXOpen
class AttributeHolder(NXOpen.NXObject): 
    """ JA class for the AttributeHolder object"""
    pass
import NXOpen
class AutomationControlScopeBuilder(NXOpen.Builder): 
    """ AssignUnassing the automation elevant objects of a Plc"""
    class Aspect(Enum):
        """
        Members Include: 
         |Function| 
         |Location| 
         |Product| 
         |Automation| 
         |NotSet| 

        """
        Function: int
        Location: int
        Product: int
        Automation: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> AutomationControlScopeBuilder.Aspect:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SourceDescendantOptions(self) -> AutomationControlScopeBuilder.Aspect:
        """
        Getter for property: ( AutomationControlScopeBuilder.Aspect NXOp) SourceDescendantOptions
         Returns the descendant scope for searching automation elevant objects basen on SourceObjects  
            
         
        """
        pass
    @SourceDescendantOptions.setter
    def SourceDescendantOptions(self, descendantType: AutomationControlScopeBuilder.Aspect):
        """
        Setter for property: ( AutomationControlScopeBuilder.Aspect NXOp) SourceDescendantOptions
         Returns the descendant scope for searching automation elevant objects basen on SourceObjects  
            
         
        """
        pass
    @property
    def SourceObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SourceObjects
         Returns the selection of objects to be assignedunassign   
            
         
        """
        pass
    @property
    def TargetObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) TargetObject
         Returns the selection where the object will be assigned.  
             
         
        """
        pass
    def Assign(self, assignObjects: List[AMEBaseNode]) -> None:
        """
         Assgin the given automation elevant objects into target Plc object 
        """
        pass
    def CollectAutomationRelatedObjects(self) -> List[AMEBaseNode]:
        """
         Collect all automation related objects based on selected source objects, and Cleanup the assign list 
         Returns automationRelatedObjects ( AMEBaseNode List[NX): .
        """
        pass
    def Unassign(self, unassignObjects: List[AMEBaseNode]) -> None:
        """
         Unassgin the given automation elevant objects from the current related Plc
        """
        pass
class AutomationFolder(AMEBaseNode): 
    """ Software Sub Folder Journaling class """
    pass
class BaseDefinitionAttributeHolder(AttributeHolder): 
    """ JA class for the BaseDefinitionAttributeHolder object"""
    def SetBasedefinition(self, baseDefinition: BaseDefinition) -> None:
        """
         Set BaseDefinition 
        """
        pass
import NXOpen
class BaseDefinition(NXOpen.NXObject): 
    """ JA class for the Base Definition object"""
    pass
import NXOpen
class BaseEvaluatorBuilder(NXOpen.Builder): 
    """ Represents the builder for all the evaluators. Contains mostly the common inputs. """
    class ConditionType(Enum):
        """
        Members Include: 
         |Contains| 
         |Equals| 
         |NotEquals| 
         |LessThan| 
         |GreaterThan| 
         |LessThanEquals| 
         |GreaterThanEquals| 

        """
        Contains: int
        Equals: int
        NotEquals: int
        LessThan: int
        GreaterThan: int
        LessThanEquals: int
        GreaterThanEquals: int
        @staticmethod
        def ValueOf(value: int) -> BaseEvaluatorBuilder.ConditionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContextType(Enum):
        """
        Members Include: 
         |Function| 
         |Location| 
         |Product| 
         |Automation| 

        """
        Function: int
        Location: int
        Product: int
        Automation: int
        @staticmethod
        def ValueOf(value: int) -> BaseEvaluatorBuilder.ContextType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BasicProperties(self) -> BasicPropertiesBuilder:
        """
        Getter for property: ( BasicPropertiesBuilder NXOp) BasicProperties
         Returns the name and description   
            
         
        """
        pass
    @property
    def ReferenceObject(self) -> ReferenceObjectBuilder:
        """
        Getter for property: ( ReferenceObjectBuilder NXOp) ReferenceObject
         Returns the context and source object selection   
            
         
        """
        pass
    @property
    def SortingBlock(self) -> SortingBlockBuilder:
        """
        Getter for property: ( SortingBlockBuilder NXOp) SortingBlock
         Returns the sorting block   
            
         
        """
        pass
    def EstablishEvaluator(self) -> ExpressionEvaluator:
        """
        Establishes the evaluator
         Returns expressionEvaluator ( ExpressionEvaluator NXOp): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class BasicPropertiesBuilder(NXOpen.TaggedObject): 
    """ Represents a re-usable component for basic properties such as name and description """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
import NXOpen
class BasicTemplateData(NXOpen.NXObject): 
    """ JA class for the Basic Template Data object"""
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the solution template description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the solution template description   
            
         
        """
        pass
    @property
    def DisplayId(self) -> str:
        """
        Getter for property: (str) DisplayId
         Returns the solution template display id   
            
         
        """
        pass
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the solution template display name   
            
         
        """
        pass
    @DisplayName.setter
    def DisplayName(self, displayName: str):
        """
        Setter for property: (str) DisplayName
         Returns the solution template display name   
            
         
        """
        pass
class BMECatVersionNode(AMEBaseNode): 
    """ BMECat Version Node class """
    pass
import NXOpen
class BreakTemplateBuilder(NXOpen.Builder): 
    """ JA class for the insert Eng object dialog"""
    def SetTemplateObjects(self, templateObjects: List[AMEBaseNode]) -> None:
        """
         Selected objects those are part of templates to break 
        """
        pass
import NXOpen
class Bulk3DPlacementBuilder(NXOpen.Builder): 
    """ Represents a Bulk3DPlacementBuilder class Builder """
    class PlacementAnglePolicy(Enum):
        """
        Members Include: 
         |ZeroDegree| 
         |NinetyDegree| 
         |OneEightyDegree| 
         |TwoSeventyDegree| 

        """
        ZeroDegree: int
        NinetyDegree: int
        OneEightyDegree: int
        TwoSeventyDegree: int
        @staticmethod
        def ValueOf(value: int) -> Bulk3DPlacementBuilder.PlacementAnglePolicy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlacementTypePolicy(Enum):
        """
        Members Include: 
         |LefttoRight| 
         |RighttoLeft| 
         |ToptoBottom| 
         |BottomtoTop| 

        """
        LefttoRight: int
        RighttoLeft: int
        ToptoBottom: int
        BottomtoTop: int
        @staticmethod
        def ValueOf(value: int) -> Bulk3DPlacementBuilder.PlacementTypePolicy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns the  AME::Bulk3DPlacementBuilder::Distance   
            
         
        """
        pass
    @Distance.setter
    def Distance(self, distance: float):
        """
        Setter for property: (float) Distance
         Returns the  AME::Bulk3DPlacementBuilder::Distance   
            
         
        """
        pass
    @property
    def PlacementAngle(self) -> Bulk3DPlacementBuilder.PlacementAnglePolicy:
        """
        Getter for property: ( Bulk3DPlacementBuilder.PlacementAnglePolicy NXOp) PlacementAngle
         Returns the  AME::Bulk3DPlacementBuilder::PlacementAngle    
            
         
        """
        pass
    @PlacementAngle.setter
    def PlacementAngle(self, placementAngle: Bulk3DPlacementBuilder.PlacementAnglePolicy):
        """
        Setter for property: ( Bulk3DPlacementBuilder.PlacementAnglePolicy NXOp) PlacementAngle
         Returns the  AME::Bulk3DPlacementBuilder::PlacementAngle    
            
         
        """
        pass
    @property
    def PlacementType(self) -> Bulk3DPlacementBuilder.PlacementTypePolicy:
        """
        Getter for property: ( Bulk3DPlacementBuilder.PlacementTypePolicy NXOp) PlacementType
         Returns the  AME::Bulk3DPlacementBuilder::PlacementType    
            
         
        """
        pass
    @PlacementType.setter
    def PlacementType(self, type: Bulk3DPlacementBuilder.PlacementTypePolicy):
        """
        Setter for property: ( Bulk3DPlacementBuilder.PlacementTypePolicy NXOp) PlacementType
         Returns the  AME::Bulk3DPlacementBuilder::PlacementType    
            
         
        """
        pass
    @property
    def SelectMountingInterfaceLocation(self) -> SelectMountingInterfaceLocationBuilder:
        """
        Getter for property: ( SelectMountingInterfaceLocationBuilder NXOp) SelectMountingInterfaceLocation
         Returns the co-ordinate of target location  
            
         
        """
        pass
    @SelectMountingInterfaceLocation.setter
    def SelectMountingInterfaceLocation(self, miLocationBuilder: SelectMountingInterfaceLocationBuilder):
        """
        Setter for property: ( SelectMountingInterfaceLocationBuilder NXOp) SelectMountingInterfaceLocation
         Returns the co-ordinate of target location  
            
         
        """
        pass
    def GetEngobjectsToBePlaced(self) -> List[NXOpen.NXObject]:
        """
         Get the dragged engobjects 
         Returns eos ( NXOpen.NXObject Li): .
        """
        pass
    def SetEngobjectsToBePlaced(self, eos: List[NXOpen.NXObject]) -> None:
        """
         Set the dragged engobjects 
        """
        pass
import NXOpen
class BulkConnectionBuilder(AMEBaseBuilder): 
    """ builder for the bulk connection dialog"""
    @property
    def SourceObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SourceObject
         Returns the source object   
            
         
        """
        pass
    @property
    def TargetObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) TargetObject
         Returns the target object   
            
         
        """
        pass
    def ConnectOneToOne(self, sourcePorts: List[IPort], targetPorts: List[IPort], overrideExistingConnection: bool) -> None:
        """
         Make the Connection between the source and target ports 
        """
        pass
    def ConnectOneVsMany(self, sourcePorts: List[IPort], targetPorts: List[IPort], overrideExistingConnection: bool) -> None:
        """
         Make the Connection between 1 port of N cardinality and Many ports of 1 cardinality 
        """
        pass
    def Disconnect(self, sourcePorts: List[IPort], targetPorts: List[IPort]) -> None:
        """
         Disconnect the Connections 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class BulkEditAnnotationBuilder(NXOpen.Builder): 
    """ Represents builder to edit annotations """
    @property
    def Anchor(self) -> AmeSymbolAnnotationAnchor:
        """
        Getter for property: ( AmeSymbolAnnotationAnchor NXOp) Anchor
         Returns the TextAnchor   
            
         
        """
        pass
    @Anchor.setter
    def Anchor(self, anchor: AmeSymbolAnnotationAnchor):
        """
        Setter for property: ( AmeSymbolAnnotationAnchor NXOp) Anchor
         Returns the TextAnchor   
            
         
        """
        pass
    @property
    def AnnotationBuilder(self) -> NXOpen.Diagramming.CannedAnnotationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.CannedAnnotationBuilder) AnnotationBuilder
         Returns the AnnotationBuilder.  
             
         
        """
        pass
    @AnnotationBuilder.setter
    def AnnotationBuilder(self, annotation: NXOpen.Diagramming.CannedAnnotationBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.CannedAnnotationBuilder) AnnotationBuilder
         Returns the AnnotationBuilder.  
             
         
        """
        pass
    @property
    def LetteringAngle(self) -> AmeSymbolAnnotationLetteringangle:
        """
        Getter for property: ( AmeSymbolAnnotationLetteringangle NXOp) LetteringAngle
         Returns the LetteringAngle   
            
         
        """
        pass
    @LetteringAngle.setter
    def LetteringAngle(self, letteringAngle: AmeSymbolAnnotationLetteringangle):
        """
        Setter for property: ( AmeSymbolAnnotationLetteringangle NXOp) LetteringAngle
         Returns the LetteringAngle   
            
         
        """
        pass
    @property
    def TextBoxWidth(self) -> float:
        """
        Getter for property: (float) TextBoxWidth
         Returns the Text box width  
            
         
        """
        pass
    @TextBoxWidth.setter
    def TextBoxWidth(self, width: float):
        """
        Setter for property: (float) TextBoxWidth
         Returns the Text box width  
            
         
        """
        pass
    @property
    def TextOverflow(self) -> AmeSymbolAnnotationTextOverflowMethod:
        """
        Getter for property: ( AmeSymbolAnnotationTextOverflowMethod NXOp) TextOverflow
         Returns the Text Overflow method  
            
         
        """
        pass
    @TextOverflow.setter
    def TextOverflow(self, overflowMethod: AmeSymbolAnnotationTextOverflowMethod):
        """
        Setter for property: ( AmeSymbolAnnotationTextOverflowMethod NXOp) TextOverflow
         Returns the Text Overflow method  
            
         
        """
        pass
    def ResetAnnotationToDefault(self) -> None:
        """
         Reset Annotation to default 
        """
        pass
    def SetChangedSettings(self, settingName: List[str], isSettingChanged: List[str]) -> None:
        """
         The Settings change list 
        """
        pass
    def SetSelectedAnnotations(self, selectedNodes: List[NXOpen.Diagramming.Annotation]) -> None:
        """
         The SelectedNodeTags 
        """
        pass
import NXOpen
import NXOpen.Tooling
class BulkEngineeringObjectBuilder(MultipleObjectsBuilder): 
    """ BulkEngineeringObjectBuilder class will be used for bulk Engineering Object Operation.
    """
    class PlacementType(Enum):
        """
        Members Include: 
         |Navigator| 
         |Page| 
         |Cabinet| 

        """
        Navigator: int
        Page: int
        Cabinet: int
        @staticmethod
        def ValueOf(value: int) -> BulkEngineeringObjectBuilder.PlacementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectPlacement(self) -> bool:
        """
        Getter for property: (bool) AspectPlacement
         Returns the aspect placement   
            
         
        """
        pass
    @AspectPlacement.setter
    def AspectPlacement(self, aspectPlacement: bool):
        """
        Setter for property: (bool) AspectPlacement
         Returns the aspect placement   
            
         
        """
        pass
    @property
    def Bulk3DPlacement(self) -> Bulk3DPlacementBuilder:
        """
        Getter for property: ( Bulk3DPlacementBuilder NXOp) Bulk3DPlacement
         Returns the bulk 3d placement cabinet builder   
            
         
        """
        pass
    @property
    def EOAttributeHolder(self) -> EOAttributeHolder:
        """
        Getter for property: ( EOAttributeHolder NXOp) EOAttributeHolder
         Returns the container for definition holders   
            
         
        """
        pass
    @property
    def EOName(self) -> EngineeringObjectNameBuilder:
        """
        Getter for property: ( EngineeringObjectNameBuilder NXOp) EOName
         Returns the eo name and description ui block  
            
         
        """
        pass
    @property
    def EoDefAttributeHolder(self) -> EODefAttributeHolder:
        """
        Getter for property: ( EODefAttributeHolder NXOp) EoDefAttributeHolder
         Returns the EO definition attribute holder   
            
         
        """
        pass
    @property
    def InsertSettings(self) -> InsertSettingsBuilder:
        """
        Getter for property: ( InsertSettingsBuilder NXOp) InsertSettings
         Returns the settings group having the aspect placement and copies per parent   
            
         
        """
        pass
    @property
    def IsFromMapping(self) -> bool:
        """
        Getter for property: (bool) IsFromMapping
         Returns the is from mapping flag indicates if bulk engineering object instantiation is initiated from mapping   
            
         
        """
        pass
    @IsFromMapping.setter
    def IsFromMapping(self, isFromMapping: bool):
        """
        Setter for property: (bool) IsFromMapping
         Returns the is from mapping flag indicates if bulk engineering object instantiation is initiated from mapping   
            
         
        """
        pass
    @property
    def PlacementValue(self) -> BulkEngineeringObjectBuilder.PlacementType:
        """
        Getter for property: ( BulkEngineeringObjectBuilder.PlacementType NXOp) PlacementValue
         Returns the placement type   
            
         
        """
        pass
    @PlacementValue.setter
    def PlacementValue(self, placementType: BulkEngineeringObjectBuilder.PlacementType):
        """
        Setter for property: ( BulkEngineeringObjectBuilder.PlacementType NXOp) PlacementValue
         Returns the placement type   
            
         
        """
        pass
    @property
    def ProductDefAttributeHolder(self) -> ProductDefAttributeHolder:
        """
        Getter for property: ( ProductDefAttributeHolder NXOp) ProductDefAttributeHolder
         Returns the Product definition attribute holder   
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the selection definition builder  
            
         
        """
        pass
    @property
    def SelectedBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectedBaseDefinition
         Returns the selected base definition  
            
         
        """
        pass
    @property
    def SelectedObjects(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedObjects
         Returns the select object   
            
         
        """
        pass
    @property
    def ShowInAutomation(self) -> bool:
        """
        Getter for property: (bool) ShowInAutomation
         Returns the show in automation   
            
         
        """
        pass
    @ShowInAutomation.setter
    def ShowInAutomation(self, showInAutomation: bool):
        """
        Setter for property: (bool) ShowInAutomation
         Returns the show in automation   
            
         
        """
        pass
    @property
    def ShowInFunction(self) -> bool:
        """
        Getter for property: (bool) ShowInFunction
         Returns the show in function   
            
         
        """
        pass
    @ShowInFunction.setter
    def ShowInFunction(self, showInFunction: bool):
        """
        Setter for property: (bool) ShowInFunction
         Returns the show in function   
            
         
        """
        pass
    @property
    def ShowInLocation(self) -> bool:
        """
        Getter for property: (bool) ShowInLocation
         Returns the show in location   
            
         
        """
        pass
    @ShowInLocation.setter
    def ShowInLocation(self, showInLocation: bool):
        """
        Setter for property: (bool) ShowInLocation
         Returns the show in location   
            
         
        """
        pass
    @property
    def ShowInProduct(self) -> bool:
        """
        Getter for property: (bool) ShowInProduct
         Returns the show in product   
            
         
        """
        pass
    @ShowInProduct.setter
    def ShowInProduct(self, showInProduct: bool):
        """
        Setter for property: (bool) ShowInProduct
         Returns the show in product   
            
         
        """
        pass
    @property
    def SymbolLocation(self) -> SymbolLocationBuilder:
        """
        Getter for property: ( SymbolLocationBuilder NXOp) SymbolLocation
         Returns the symbol location builder  
            
         
        """
        pass
    @property
    def SymbolPlacement(self) -> SymbolPlacementBuilder:
        """
        Getter for property: ( SymbolPlacementBuilder NXOp) SymbolPlacement
         Returns the symbol placement builder  
            
         
        """
        pass
    def SetExternalObjectsToMap(self, externalObjects: List[NXOpen.NXObject]) -> None:
        """
         Selected external objects to be mapped 
        """
        pass
class BusInterfaceType(Enum):
    """
    Members Include: 
     |ProfibusDp| 
     |Mpi| 
     |Profinet| 
     |AsInterface| 

    """
    ProfibusDp: int
    Mpi: int
    Profinet: int
    AsInterface: int
    @staticmethod
    def ValueOf(value: int) -> BusInterfaceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CabinetComponentNode(AMEBaseNode): 
    """ Cabinet Component Node class """
    def DisconnectFromEngineeringObject(self) -> None:
        """
         Disconnects Cabinet Component from Engineering Object 
        """
        pass
import NXOpen
class CabinetDesignBuilder(NXOpen.Builder): 
    """ the builder for creating cabinet design """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of cabinet design   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description of cabinet design   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of cabinet design    
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of cabinet design    
            
         
        """
        pass
class CabinetNode(AMEBaseNode): 
    """ Cabinet Node class """
    def RemoveObjects(self, cabinetComponentNodes: List[CabinetComponentNode]) -> None:
        """
         Removes cabinet component 
        """
        pass
import NXOpen
import NXOpen.Annotations
class CabinetObjectLabelBuilder(NXOpen.Builder): 
    """ JA class for the cabinet object label dialog """
    @property
    def CabinetObjectLabel(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) CabinetObjectLabel
         Returns the cabinet object label   
            
         
        """
        pass
    @CabinetObjectLabel.setter
    def CabinetObjectLabel(self, eoLabel: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) CabinetObjectLabel
         Returns the cabinet object label   
            
         
        """
        pass
    @property
    def CursorLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CursorLocation
         Returns a cursor location  
            
         
        """
        pass
    @CursorLocation.setter
    def CursorLocation(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) CursorLocation
         Returns a cursor location  
            
         
        """
        pass
    @property
    def EngObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) EngObject
         Returns a component selected  
            
         
        """
        pass
    @EngObject.setter
    def EngObject(self, eo: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) EngObject
         Returns a component selected  
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def ToggleFunction(self) -> bool:
        """
        Getter for property: (bool) ToggleFunction
         Returns the toggle function   
            
         
        """
        pass
    @ToggleFunction.setter
    def ToggleFunction(self, toggleFunction: bool):
        """
        Setter for property: (bool) ToggleFunction
         Returns the toggle function   
            
         
        """
        pass
    @property
    def ToggleLocation(self) -> bool:
        """
        Getter for property: (bool) ToggleLocation
         Returns the toggle location   
            
         
        """
        pass
    @ToggleLocation.setter
    def ToggleLocation(self, toggleLocation: bool):
        """
        Setter for property: (bool) ToggleLocation
         Returns the toggle location   
            
         
        """
        pass
    @property
    def ToggleProduct(self) -> bool:
        """
        Getter for property: (bool) ToggleProduct
         Returns the toggle product   
            
         
        """
        pass
    @ToggleProduct.setter
    def ToggleProduct(self, toggleProduct: bool):
        """
        Setter for property: (bool) ToggleProduct
         Returns the toggle product   
            
         
        """
        pass
    @property
    def ToggleReferenceDesignationSet(self) -> bool:
        """
        Getter for property: (bool) ToggleReferenceDesignationSet
         Returns the toggle reference designation set   
            
         
        """
        pass
    @ToggleReferenceDesignationSet.setter
    def ToggleReferenceDesignationSet(self, toggleReferenceDesignationSet: bool):
        """
        Setter for property: (bool) ToggleReferenceDesignationSet
         Returns the toggle reference designation set   
            
         
        """
        pass
import NXOpen
class CabinetObject(NXOpen.NXObject): 
    """ Cabinet Object class """
    pass
import NXOpen
class CabinetRoot(AMEBaseNode): 
    """ Cabinet Root Node class """
    class CabinetState(Enum):
        """
        Members Include: 
         |Active| 
         |Inactive| 

        """
        Active: int
        Inactive: int
        @staticmethod
        def ValueOf(value: int) -> CabinetRoot.CabinetState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def PlaceProductInActiveCabinet(self, product3DModelFileName: str, location: NXOpen.Point3d, parentEngObj: AMEEngObject, receptacleObject: NXOpen.NXObject) -> None:
        """
         Places the product in active cabinet 
        """
        pass
    def PlaceProductsInActiveCabinet(self, location: NXOpen.Point3d, engObjects: List[AMEEngObject], receptacleObject: NXOpen.NXObject, distance: float, placementType: Bulk3DPlacementBuilder.PlacementTypePolicy, placementAngle: Bulk3DPlacementBuilder.PlacementAnglePolicy) -> None:
        """
         Places the selection of products in active cabinet 
        """
        pass
    def SetCabinetState(self, cabinetNode: CabinetNode, state: CabinetRoot.CabinetState) -> None:
        """
         Updates the cabinet according to its new state 
        """
        pass
import NXOpen
class CallMethodRuleBuilder(NXOpen.Builder): 
    """ JA class for the call method rule dialog"""
    @property
    def Conditions(self) -> ConditionsBuilder:
        """
        Getter for property: ( ConditionsBuilder NXOp) Conditions
         Returns the object condition ui block  
            
         
        """
        pass
    @property
    def CurrentParameterRuleType(self) -> PlcRule.Type:
        """
        Getter for property: ( PlcRule.Type NXOp) CurrentParameterRuleType
         Returns the rule type of selected parameter  
            
         
        """
        pass
    @CurrentParameterRuleType.setter
    def CurrentParameterRuleType(self, type: PlcRule.Type):
        """
        Setter for property: ( PlcRule.Type NXOp) CurrentParameterRuleType
         Returns the rule type of selected parameter  
            
         
        """
        pass
    @property
    def IterativeMethodSelectionType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) IterativeMethodSelectionType
         Returns the iterative method selection type  
            
         
        """
        pass
    @IterativeMethodSelectionType.setter
    def IterativeMethodSelectionType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) IterativeMethodSelectionType
         Returns the iterative method selection type  
            
         
        """
        pass
    @property
    def IterativeObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) IterativeObjectConnection
         Returns the iterative object connection block  
            
         
        """
        pass
    @property
    def IterativeSelectedPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) IterativeSelectedPort
         Returns the eo any port selection   
            
         
        """
        pass
    @property
    def ObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ObjectConnection
         Returns the object connection ui block  
            
         
        """
        pass
    @property
    def ObjectConnectionDetail(self) -> ObjectConnectionDetailBuilder:
        """
        Getter for property: ( ObjectConnectionDetailBuilder NXOp) ObjectConnectionDetail
         Returns the object connection detail ui block  
            
         
        """
        pass
    @property
    def ParameterObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ParameterObjectConnection
         Returns the parameter object connection ui block  
            
         
        """
        pass
    @property
    def ParameterSelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) ParameterSelectionPort
         Returns the parameter port selection   
            
         
        """
        pass
    @property
    def ParameterSelectionType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) ParameterSelectionType
         Returns the external object selection type  
            
         
        """
        pass
    @ParameterSelectionType.setter
    def ParameterSelectionType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) ParameterSelectionType
         Returns the external object selection type  
            
         
        """
        pass
    @property
    def ParameterText(self) -> str:
        """
        Getter for property: (str) ParameterText
         Returns the constantText of a parameter   
            
         
        """
        pass
    @ParameterText.setter
    def ParameterText(self, resultText: str):
        """
        Setter for property: (str) ParameterText
         Returns the constantText of a parameter   
            
         
        """
        pass
    @property
    def RuleCreationType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) RuleCreationType
         Returns the creation type by creating a position  
            
         
        """
        pass
    @RuleCreationType.setter
    def RuleCreationType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) RuleCreationType
         Returns the creation type by creating a position  
            
         
        """
        pass
    @property
    def RuleName(self) -> str:
        """
        Getter for property: (str) RuleName
         Returns the rule name   
            
         
        """
        pass
    @RuleName.setter
    def RuleName(self, resultText: str):
        """
        Setter for property: (str) RuleName
         Returns the rule name   
            
         
        """
        pass
    @property
    def SelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) SelectionPort
         Returns the replacement port selection   
            
         
        """
        pass
    def RefreshContent(self, paramOwnerId: str, paramName: str) -> None:
        """
         Update the builder of the reuse blocks
        """
        pass
    def RefreshParameterDetail(self) -> None:
        """
         Refresh the content of the detail builder
        """
        pass
    def SetAnchorInfo(self, anchroPosition: PlcCodePosition, insertBefore: bool) -> None:
        """
         Set anchor object and insertBefore info 
        """
        pass
    def UpdateAllParameters(self) -> None:
        """
         Update the selected parameter list
        """
        pass
    def UpdateSelectedParameter(self, paramOwnerId: str, paramName: str) -> None:
        """
         Update the selected parameter
        """
        pass
import NXOpen
class ChangeProductTypeBuilder(NXOpen.Builder): 
    """ JA class for Change Type of product dialog"""
    class Types(Enum):
        """
        Members Include: 
         |Product| 
         |DeviceFunction| 

        """
        Product: int
        DeviceFunction: int
        @staticmethod
        def ValueOf(value: int) -> ChangeProductTypeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SelectedObjects(self) -> SelectINodeObjectList:
        """
        Getter for property: ( SelectINodeObjectList NXOp) SelectedObjects
         Returns the target node selection   
            
         
        """
        pass
    @property
    def SelectedType(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectedType
         Returns the selection base definition  
            
         
        """
        pass
    @property
    def TypeList(self) -> ChangeProductTypeBuilder.Types:
        """
        Getter for property: ( ChangeProductTypeBuilder.Types NXOp) TypeList
         Returns the representation type which could be of  NXOpen::AME::ChangeProductTypeBuilder::TypeList    
            
         
        """
        pass
    @TypeList.setter
    def TypeList(self, typeList: ChangeProductTypeBuilder.Types):
        """
        Setter for property: ( ChangeProductTypeBuilder.Types NXOp) TypeList
         Returns the representation type which could be of  NXOpen::AME::ChangeProductTypeBuilder::TypeList    
            
         
        """
        pass
import NXOpen
class ChangeSymbolVariantBuilder(NXOpen.Builder): 
    """ JA class for the change symbol variant dialog"""
    @property
    def SymbolPlacement(self) -> SymbolPlacementBuilder:
        """
        Getter for property: ( SymbolPlacementBuilder NXOp) SymbolPlacement
         Returns the Node Builder used for creating Symbol for EO  
            
         
        """
        pass
    def ClearCreatedDiagrammingNode(self) -> None:
        """
         Clear the already created diagramming node in case of symbol variant changes
        """
        pass
class ChildrenEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the children objects for a given aspect and a starting point """
    class FilterType(Enum):
        """
        Members Include: 
         |LocalModules| 
         |ProgramBlocks| 
         |PlcDatatypes| 
         |Tags| 
         |All| 

        """
        LocalModules: int
        ProgramBlocks: int
        PlcDatatypes: int
        Tags: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ChildrenEvaluatorBuilder.FilterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectSelection(self) -> BaseEvaluatorBuilder.ContextType:
        """
        Getter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @AspectSelection.setter
    def AspectSelection(self, aspectSelection: BaseEvaluatorBuilder.ContextType):
        """
        Setter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @property
    def ObjectType(self) -> ChildrenEvaluatorBuilder.FilterType:
        """
        Getter for property: ( ChildrenEvaluatorBuilder.FilterType NXOp) ObjectType
         Returns the object type filter selection   
            
         
        """
        pass
    @ObjectType.setter
    def ObjectType(self, objectType: ChildrenEvaluatorBuilder.FilterType):
        """
        Setter for property: ( ChildrenEvaluatorBuilder.FilterType NXOp) ObjectType
         Returns the object type filter selection   
            
         
        """
        pass
import NXOpen
class CollaborationProjectSettingsBuilder(NXOpen.Builder): 
    """ This builder class is used for setting type mapping configurations
        for external mechanical and excel data. It is also used for setting
        smart filter configurations.
    """
    class FilterMode(Enum):
        """
        Members Include: 
         |FilterOnClassificationClass| 
         |FilterOnProperty| 

        """
        FilterOnClassificationClass: int
        FilterOnProperty: int
        @staticmethod
        def ValueOf(value: int) -> CollaborationProjectSettingsBuilder.FilterMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultsSetting(Enum):
        """
        Members Include: 
         |DefineFilterValues| 
         |ShowObjectsIfNotEmpty| 

        """
        DefineFilterValues: int
        ShowObjectsIfNotEmpty: int
        @staticmethod
        def ValueOf(value: int) -> CollaborationProjectSettingsBuilder.ResultsSetting:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnableSmartFilter(self) -> bool:
        """
        Getter for property: (bool) EnableSmartFilter
         Returns the property to enable or disable smart filter   
            
         
        """
        pass
    @EnableSmartFilter.setter
    def EnableSmartFilter(self, enableFilterSetting: bool):
        """
        Setter for property: (bool) EnableSmartFilter
         Returns the property to enable or disable smart filter   
            
         
        """
        pass
    @property
    def FilterType(self) -> CollaborationProjectSettingsBuilder.FilterMode:
        """
        Getter for property: ( CollaborationProjectSettingsBuilder.FilterMode NXOp) FilterType
         Returns the functions to GetSet the  NXOpen::AME::CollaborationProjectSettingsBuilder::FilterMode  for filter type   
            
         
        """
        pass
    @FilterType.setter
    def FilterType(self, filterType: CollaborationProjectSettingsBuilder.FilterMode):
        """
        Setter for property: ( CollaborationProjectSettingsBuilder.FilterMode NXOp) FilterType
         Returns the functions to GetSet the  NXOpen::AME::CollaborationProjectSettingsBuilder::FilterMode  for filter type   
            
         
        """
        pass
    @property
    def MappingPropertyForExcelData(self) -> str:
        """
        Getter for property: (str) MappingPropertyForExcelData
         Returns the property to use for type mapping by mechanical or automation id for Excel Data   
            
         
        """
        pass
    @MappingPropertyForExcelData.setter
    def MappingPropertyForExcelData(self, mappingProperty: str):
        """
        Setter for property: (str) MappingPropertyForExcelData
         Returns the property to use for type mapping by mechanical or automation id for Excel Data   
            
         
        """
        pass
    @property
    def MappingPropertyForMechanicalData(self) -> str:
        """
        Getter for property: (str) MappingPropertyForMechanicalData
         Returns the property to use for type mapping by mechanical or automation id for Mechanical Data   
            
         
        """
        pass
    @MappingPropertyForMechanicalData.setter
    def MappingPropertyForMechanicalData(self, mappingProperty: str):
        """
        Setter for property: (str) MappingPropertyForMechanicalData
         Returns the property to use for type mapping by mechanical or automation id for Mechanical Data   
            
         
        """
        pass
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the property to get or set the property name   
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the property to get or set the property name   
            
         
        """
        pass
    @property
    def ShowObjectsSetting(self) -> CollaborationProjectSettingsBuilder.ResultsSetting:
        """
        Getter for property: ( CollaborationProjectSettingsBuilder.ResultsSetting NXOp) ShowObjectsSetting
         Returns the property to get or set  NXOpen::AME::CollaborationProjectSettingsBuilder::ResultsSetting  show objects setting   
            
         
        """
        pass
    @ShowObjectsSetting.setter
    def ShowObjectsSetting(self, showObjectsSetting: CollaborationProjectSettingsBuilder.ResultsSetting):
        """
        Setter for property: ( CollaborationProjectSettingsBuilder.ResultsSetting NXOp) ShowObjectsSetting
         Returns the property to get or set  NXOpen::AME::CollaborationProjectSettingsBuilder::ResultsSetting  show objects setting   
            
         
        """
        pass
    @property
    def TypeMappingModeForExcelData(self) -> MappingSourceBuilder.MappingMode:
        """
        Getter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingModeForExcelData
         Returns the functions to GetSet the  NXOpen::AME::MappingSourceBuilder::MappingMode  for Excel Data   
            
         
        """
        pass
    @TypeMappingModeForExcelData.setter
    def TypeMappingModeForExcelData(self, mode: MappingSourceBuilder.MappingMode):
        """
        Setter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingModeForExcelData
         Returns the functions to GetSet the  NXOpen::AME::MappingSourceBuilder::MappingMode  for Excel Data   
            
         
        """
        pass
    @property
    def TypeMappingModeForMechanicalData(self) -> MappingSourceBuilder.MappingMode:
        """
        Getter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingModeForMechanicalData
         Returns the functions to GetSet the  NXOpen::AME::MappingSourceBuilder::MappingMode  for Mechanical Data   
            
         
        """
        pass
    @TypeMappingModeForMechanicalData.setter
    def TypeMappingModeForMechanicalData(self, mode: MappingSourceBuilder.MappingMode):
        """
        Setter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingModeForMechanicalData
         Returns the functions to GetSet the  NXOpen::AME::MappingSourceBuilder::MappingMode  for Mechanical Data   
            
         
        """
        pass
    def GetFilterValues(self) -> List[str]:
        """
         The filter values for smart filter settings 
         Returns filterValues (List[str]): .
        """
        pass
    def SetFilterValues(self, filterValues: List[str]) -> None:
        """
         The filter values for smart filter settings 
        """
        pass
import NXOpen
class ConditionBlockBuilder(NXOpen.TaggedObject): 
    """ Represents an object that is used to specify conditions based on the property name, value and comparison operator"""
    @property
    def ComparativeValueNumeric(self) -> float:
        """
        Getter for property: (float) ComparativeValueNumeric
         Returns the comparison numeric value  
            
         
        """
        pass
    @ComparativeValueNumeric.setter
    def ComparativeValueNumeric(self, comparativeValueNumeric: float):
        """
        Setter for property: (float) ComparativeValueNumeric
         Returns the comparison numeric value  
            
         
        """
        pass
    @property
    def ComparativeValueString(self) -> str:
        """
        Getter for property: (str) ComparativeValueString
         Returns the comparison string value   
            
         
        """
        pass
    @ComparativeValueString.setter
    def ComparativeValueString(self, comparativeValueString: str):
        """
        Setter for property: (str) ComparativeValueString
         Returns the comparison string value   
            
         
        """
        pass
    @property
    def ComparatorType(self) -> BaseEvaluatorBuilder.ConditionType:
        """
        Getter for property: ( BaseEvaluatorBuilder.ConditionType NXOp) ComparatorType
         Returns the condition type   
            
         
        """
        pass
    @ComparatorType.setter
    def ComparatorType(self, comparatorType: BaseEvaluatorBuilder.ConditionType):
        """
        Setter for property: ( BaseEvaluatorBuilder.ConditionType NXOp) ComparatorType
         Returns the condition type   
            
         
        """
        pass
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the property name   
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the property name   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ConditionsBuilder(NXOpen.TaggedObject): 
    """ JA class for the conditions dialog"""
    def RemoveCondition(self) -> None:
        """
         Remove the condition for the rule 
        """
        pass
    def SetCondition(self, exp: NXOpen.Expression) -> None:
        """
         Set the condition for the rule 
        """
        pass
import NXOpen
class ConfigureResultTableBuilder(NXOpen.Builder): 
    """ Represents configure result table class builder """
    def Add(self, objectTypeName: str, groupName: str, propertyName: str) -> None:
        """
         The action to add properties 
        """
        pass
    def AddSortingCriteria(self, objectType: str, categoryType: str, propertyName: str, sortType: str) -> None:
        """
         The action to add sorting criteria 
        """
        pass
    def ClearSortingCriteria(self) -> None:
        """
         The action to clear sorting criteria
        """
        pass
    def MoveDown(self, objectTypeName: str, groupName: str, propertyName: str) -> None:
        """
         The action to move added column down 
        """
        pass
    def MoveUp(self, objectTypeName: str, groupName: str, propertyName: str) -> None:
        """
         The action to move added column up 
        """
        pass
    def Remove(self, objectTypeName: str, groupName: str, propertyName: str) -> None:
        """
         The action to move earlier added column 
        """
        pass
    def SetVisibility(self, objectTypeName: str, groupName: str, propertyName: str, visibility: bool) -> None:
        """
         The visibility status of each column or group 
        """
        pass
class ConnectedObjectsEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the connected objects for the given port and a starting point """
    class Type(Enum):
        """
        Members Include: 
         |EngineeringObject|  Engineer Object 
         |Port|  Port

        """
        EngineeringObject: int
        Port: int
        @staticmethod
        def ValueOf(value: int) -> ConnectedObjectsEvaluatorBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Port(self) -> str:
        """
        Getter for property: (str) Port
         Returns the expression that will determine the port.  
             
         
        """
        pass
    @Port.setter
    def Port(self, port: str):
        """
        Setter for property: (str) Port
         Returns the expression that will determine the port.  
             
         
        """
        pass
    @property
    def ScopeType(self) -> ConnectedObjectsEvaluatorBuilder.Type:
        """
        Getter for property: ( ConnectedObjectsEvaluatorBuilder.Type NXOp) ScopeType
         Returns the method to return type   
            
         
        """
        pass
    @ScopeType.setter
    def ScopeType(self, scope: ConnectedObjectsEvaluatorBuilder.Type):
        """
        Setter for property: ( ConnectedObjectsEvaluatorBuilder.Type NXOp) ScopeType
         Returns the method to return type   
            
         
        """
        pass
class ConnectionProductComponentInstance(AMEExtendedObject): 
    """ Connection Product Component Instance class """
    pass
class ConnectionProductComponent(ProductComponent): 
    """ Connection Product Component class """
    pass
import NXOpen
import NXOpen.Tooling
class ConnectToLibraryItemBuilder(NXOpen.Builder): 
    """ JA class for the connect to library item dialog"""
    @property
    def SelectedPOUFromLibrary(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedPOUFromLibrary
         Returns the library pou selection  
            
         
        """
        pass
    @property
    def SelectedSoftwareBlockDataTypePort(self) -> SoftwareBlockDataTypePort:
        """
        Getter for property: ( SoftwareBlockDataTypePort NXOp) SelectedSoftwareBlockDataTypePort
         Returns the interface member selection  
            
         
        """
        pass
    @SelectedSoftwareBlockDataTypePort.setter
    def SelectedSoftwareBlockDataTypePort(self, imPort: SoftwareBlockDataTypePort):
        """
        Setter for property: ( SoftwareBlockDataTypePort NXOp) SelectedSoftwareBlockDataTypePort
         Returns the interface member selection  
            
         
        """
        pass
class ConstantType(Enum):
    """
    Members Include: 
     |Bool| 
     |Byte| 
     |Word| 
     |Dword| 
     |Int| 
     |Dint| 
     |Aref| 
     |Unknown| 

    """
    Bool: int
    Byte: int
    Word: int
    Dword: int
    Int: int
    Dint: int
    Aref: int
    Unknown: int
    @staticmethod
    def ValueOf(value: int) -> ConstantType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CreateBOMBuilder(NXOpen.Builder): 
    """ Represents a BOM Creation class Builder  """
    class BomScopes(Enum):
        """
        Members Include: 
         |EntireProject| 
         |Partial| 

        """
        EntireProject: int
        Partial: int
        @staticmethod
        def ValueOf(value: int) -> CreateBOMBuilder.BomScopes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |CreateNew| 
         |Update| 

        """
        CreateNew: int
        Update: int
        @staticmethod
        def ValueOf(value: int) -> CreateBOMBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BomScope(self) -> CreateBOMBuilder.BomScopes:
        """
        Getter for property: ( CreateBOMBuilder.BomScopes NXOp) BomScope
         Returns the BOM scope   
            
         
        """
        pass
    @BomScope.setter
    def BomScope(self, bomScope: CreateBOMBuilder.BomScopes):
        """
        Setter for property: ( CreateBOMBuilder.BomScopes NXOp) BomScope
         Returns the BOM scope   
            
         
        """
        pass
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
         Returns the project name to get existing BOMs     
            
         
        """
        pass
    @ProjectName.setter
    def ProjectName(self, projectCD: str):
        """
        Setter for property: (str) ProjectName
         Returns the project name to get existing BOMs     
            
         
        """
        pass
    @property
    def TcFolderBrowser(self) -> str:
        """
        Getter for property: (str) TcFolderBrowser
         Returns the bom file location in TC    
            
         
        """
        pass
    @TcFolderBrowser.setter
    def TcFolderBrowser(self, bomLocationInTC: str):
        """
        Setter for property: (str) TcFolderBrowser
         Returns the bom file location in TC    
            
         
        """
        pass
    @property
    def Type(self) -> CreateBOMBuilder.Types:
        """
        Getter for property: ( CreateBOMBuilder.Types NXOp) Type
         Returns the bom type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: CreateBOMBuilder.Types):
        """
        Setter for property: ( CreateBOMBuilder.Types NXOp) Type
         Returns the bom type   
            
         
        """
        pass
    def GetNewBOMProperties(self) -> PartOperationCreateBuilder:
        """
         Gets NXOpen.PDM.PartOperationCreateBuilder 
         Returns partOperationCreateBuilder ( PartOperationCreateBuilder NXOp): .
        """
        pass
    def SetAspectsListForFullBOM(self) -> None:
        """
         Collect all EOs for full BOM 
        """
        pass
    def SetAspectsListForPartialBOM(self, aspectNodes: List[AspectNode]) -> None:
        """
         Add the selected aspects for partial BOM. 
        """
        pass
    def SetBomItemToUpdate(self, bomItem: NXOpen.NXObject) -> None:
        """
         Sets the BOM top line item to be updated 
        """
        pass
    def SetNewBOMProperties(self, partOperationCreateBuilder: PartOperationCreateBuilder) -> None:
        """
         Sets NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
import NXOpen
class CreateDefinitionBuilder(NXOpen.Builder): 
    """ Create and classify definition """
    @property
    def SelectClassificationFromTree(self) -> SelectClassificationFromTreeBuilder:
        """
        Getter for property: ( SelectClassificationFromTreeBuilder NXOp) SelectClassificationFromTree
         Returns the select classification from tree builder  
            
         
        """
        pass
class CreateEngObjectDefinitionBuilder(CreateDefinitionBuilder): 
    """ Create and classify engineering object definition """
    pass
import NXOpen
class CreateEplanNodeBuilder(NXOpen.Builder): 
    """ Class to add new Eplan propertyproductfunction node and new propery value depending of the type."""
    class DataTypeOptions(Enum):
        """
        Members Include: 
         |Bool|  Boolean, the value will be true or false 
         |Integer|  Integer, the value is a whole number 
         |Number|  Number, the value is a floating point number and may contain units 
         |String|  String, the value will be a textual string 
         |StringTranslatable|  String, the value will be a textual string which is translatable 
         |Date|  Date, the value will be date and time 

        """
        Bool: int
        Integer: int
        Number: int
        String: int
        StringTranslatable: int
        Date: int
        @staticmethod
        def ValueOf(value: int) -> CreateEplanNodeBuilder.DataTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Mode(Enum):
        """
        Members Include: 
         |Create| 
         |Edit| 

        """
        Create: int
        Edit: int
        @staticmethod
        def ValueOf(value: int) -> CreateEplanNodeBuilder.Mode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Property| 
         |PropertyValue| 
         |Product| 
         |FunctionTemplate| 

        """
        Property: int
        PropertyValue: int
        Product: int
        FunctionTemplate: int
        @staticmethod
        def ValueOf(value: int) -> CreateEplanNodeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConditionName(self) -> str:
        """
        Getter for property: (str) ConditionName
         Returns the Condition name   
            
         
        """
        pass
    @ConditionName.setter
    def ConditionName(self, conditionName: str):
        """
        Setter for property: (str) ConditionName
         Returns the Condition name   
            
         
        """
        pass
    @property
    def ConditionValue(self) -> str:
        """
        Getter for property: (str) ConditionValue
         Returns the Condition value   
            
         
        """
        pass
    @ConditionValue.setter
    def ConditionValue(self, conditionValue: str):
        """
        Setter for property: (str) ConditionValue
         Returns the Condition value   
            
         
        """
        pass
    @property
    def CreationMode(self) -> CreateEplanNodeBuilder.Mode:
        """
        Getter for property: ( CreateEplanNodeBuilder.Mode NXOp) CreationMode
         Returns the Creation mode   
            
         
        """
        pass
    @CreationMode.setter
    def CreationMode(self, type: CreateEplanNodeBuilder.Mode):
        """
        Setter for property: ( CreateEplanNodeBuilder.Mode NXOp) CreationMode
         Returns the Creation mode   
            
         
        """
        pass
    @property
    def CzechName(self) -> str:
        """
        Getter for property: (str) CzechName
         Returns the Czech name or value   
            
         
        """
        pass
    @CzechName.setter
    def CzechName(self, germanName: str):
        """
        Setter for property: (str) CzechName
         Returns the Czech name or value   
            
         
        """
        pass
    @property
    def DataType(self) -> CreateEplanNodeBuilder.DataTypeOptions:
        """
        Getter for property: ( CreateEplanNodeBuilder.DataTypeOptions NXOp) DataType
         Returns the Data type   
            
         
        """
        pass
    @DataType.setter
    def DataType(self, propertyDataType: CreateEplanNodeBuilder.DataTypeOptions):
        """
        Setter for property: ( CreateEplanNodeBuilder.DataTypeOptions NXOp) DataType
         Returns the Data type   
            
         
        """
        pass
    @property
    def EnglishName(self) -> str:
        """
        Getter for property: (str) EnglishName
         Returns the English name or value  
            
         
        """
        pass
    @EnglishName.setter
    def EnglishName(self, englishName: str):
        """
        Setter for property: (str) EnglishName
         Returns the English name or value  
            
         
        """
        pass
    @property
    def EplanId(self) -> str:
        """
        Getter for property: (str) EplanId
         Returns the Eplan id   
            
         
        """
        pass
    @EplanId.setter
    def EplanId(self, eplanId: str):
        """
        Setter for property: (str) EplanId
         Returns the Eplan id   
            
         
        """
        pass
    @property
    def FrenchName(self) -> str:
        """
        Getter for property: (str) FrenchName
         Returns the French name or value   
            
         
        """
        pass
    @FrenchName.setter
    def FrenchName(self, germanName: str):
        """
        Setter for property: (str) FrenchName
         Returns the French name or value   
            
         
        """
        pass
    @property
    def GermanName(self) -> str:
        """
        Getter for property: (str) GermanName
         Returns the German name or value   
            
         
        """
        pass
    @GermanName.setter
    def GermanName(self, germanName: str):
        """
        Setter for property: (str) GermanName
         Returns the German name or value   
            
         
        """
        pass
    @property
    def ItalianName(self) -> str:
        """
        Getter for property: (str) ItalianName
         Returns the Italian name or value   
            
         
        """
        pass
    @ItalianName.setter
    def ItalianName(self, germanName: str):
        """
        Setter for property: (str) ItalianName
         Returns the Italian name or value   
            
         
        """
        pass
    @property
    def JapaneseName(self) -> str:
        """
        Getter for property: (str) JapaneseName
         Returns the Japanese name or value   
            
         
        """
        pass
    @JapaneseName.setter
    def JapaneseName(self, germanName: str):
        """
        Setter for property: (str) JapaneseName
         Returns the Japanese name or value   
            
         
        """
        pass
    @property
    def KoreanName(self) -> str:
        """
        Getter for property: (str) KoreanName
         Returns the Korean name or value   
            
         
        """
        pass
    @KoreanName.setter
    def KoreanName(self, germanName: str):
        """
        Setter for property: (str) KoreanName
         Returns the Korean name or value   
            
         
        """
        pass
    @property
    def ParentSelection(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) ParentSelection
         Returns the Parent node selection   
            
         
        """
        pass
    @property
    def PolishName(self) -> str:
        """
        Getter for property: (str) PolishName
         Returns the Polish name or value   
            
         
        """
        pass
    @PolishName.setter
    def PolishName(self, germanName: str):
        """
        Setter for property: (str) PolishName
         Returns the Polish name or value   
            
         
        """
        pass
    @property
    def PortugueseName(self) -> str:
        """
        Getter for property: (str) PortugueseName
         Returns the Portuguese name or value   
            
         
        """
        pass
    @PortugueseName.setter
    def PortugueseName(self, germanName: str):
        """
        Setter for property: (str) PortugueseName
         Returns the Portuguese name or value   
            
         
        """
        pass
    @property
    def PropertySelection(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) PropertySelection
         Returns the Property node selection   
            
         
        """
        pass
    @property
    def RussianName(self) -> str:
        """
        Getter for property: (str) RussianName
         Returns the Russian name or value  
            
         
        """
        pass
    @RussianName.setter
    def RussianName(self, germanName: str):
        """
        Setter for property: (str) RussianName
         Returns the Russian name or value  
            
         
        """
        pass
    @property
    def SelectedobjectToEdit(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) SelectedobjectToEdit
         Returns the selected object   
            
         
        """
        pass
    @SelectedobjectToEdit.setter
    def SelectedobjectToEdit(self, selectedObject: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) SelectedobjectToEdit
         Returns the selected object   
            
         
        """
        pass
    @property
    def SimplifiedChineseName(self) -> str:
        """
        Getter for property: (str) SimplifiedChineseName
         Returns the SimplifiedChinese name or value   
            
         
        """
        pass
    @SimplifiedChineseName.setter
    def SimplifiedChineseName(self, germanName: str):
        """
        Setter for property: (str) SimplifiedChineseName
         Returns the SimplifiedChinese name or value   
            
         
        """
        pass
    @property
    def SpanishName(self) -> str:
        """
        Getter for property: (str) SpanishName
         Returns the Spanish name or value   
            
         
        """
        pass
    @SpanishName.setter
    def SpanishName(self, germanName: str):
        """
        Setter for property: (str) SpanishName
         Returns the Spanish name or value   
            
         
        """
        pass
    @property
    def TraditionalChineseName(self) -> str:
        """
        Getter for property: (str) TraditionalChineseName
         Returns the TraditionalChinese name or value   
            
         
        """
        pass
    @TraditionalChineseName.setter
    def TraditionalChineseName(self, germanName: str):
        """
        Setter for property: (str) TraditionalChineseName
         Returns the TraditionalChinese name or value   
            
         
        """
        pass
    @property
    def Type(self) -> CreateEplanNodeBuilder.Types:
        """
        Getter for property: ( CreateEplanNodeBuilder.Types NXOp) Type
         Returns the Eplan node type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: CreateEplanNodeBuilder.Types):
        """
        Setter for property: ( CreateEplanNodeBuilder.Types NXOp) Type
         Returns the Eplan node type   
            
         
        """
        pass
    @property
    def Unit(self) -> str:
        """
        Getter for property: (str) Unit
         Returns the Unit   
            
         
        """
        pass
    @Unit.setter
    def Unit(self, units: str):
        """
        Setter for property: (str) Unit
         Returns the Unit   
            
         
        """
        pass
class CreateFCIBuilder(InstanceDataBlockBuilder): 
    """ JA class for the reuse rule dialog"""
    pass
class CreateIDBBuilder(InstanceDataBlockBuilder): 
    """ JA class for the reuse rule dialog"""
    pass
import NXOpen
class CreateMethodBuilder(NXOpen.Builder): 
    """ Represents a method used in the software blocks"""
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @property
    def InsertMethodAuto(self) -> bool:
        """
        Getter for property: (bool) InsertMethodAuto
         Returns the method automatically insertion   
            
         
        """
        pass
    @InsertMethodAuto.setter
    def InsertMethodAuto(self, insertMethodAuto: bool):
        """
        Setter for property: (bool) InsertMethodAuto
         Returns the method automatically insertion   
            
         
        """
        pass
    @property
    def MethodName(self) -> str:
        """
        Getter for property: (str) MethodName
         Returns the string method name   
            
         
        """
        pass
    @MethodName.setter
    def MethodName(self, methodName: str):
        """
        Setter for property: (str) MethodName
         Returns the string method name   
            
         
        """
        pass
    @property
    def SelectedObjects(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedObjects
         Returns the select object   
            
         
        """
        pass
    @property
    def ShowInAutomation(self) -> bool:
        """
        Getter for property: (bool) ShowInAutomation
         Returns the show in automation   
            
         
        """
        pass
    @ShowInAutomation.setter
    def ShowInAutomation(self, showInAutomation: bool):
        """
        Setter for property: (bool) ShowInAutomation
         Returns the show in automation   
            
         
        """
        pass
    @property
    def ShowInFunction(self) -> bool:
        """
        Getter for property: (bool) ShowInFunction
         Returns the show in function   
            
         
        """
        pass
    @ShowInFunction.setter
    def ShowInFunction(self, showInFunction: bool):
        """
        Setter for property: (bool) ShowInFunction
         Returns the show in function   
            
         
        """
        pass
    @property
    def ShowInLocation(self) -> bool:
        """
        Getter for property: (bool) ShowInLocation
         Returns the show in location   
            
         
        """
        pass
    @ShowInLocation.setter
    def ShowInLocation(self, showInLocation: bool):
        """
        Setter for property: (bool) ShowInLocation
         Returns the show in location   
            
         
        """
        pass
    @property
    def ShowInProduct(self) -> bool:
        """
        Getter for property: (bool) ShowInProduct
         Returns the show in product   
            
         
        """
        pass
    @ShowInProduct.setter
    def ShowInProduct(self, showInProduct: bool):
        """
        Setter for property: (bool) ShowInProduct
         Returns the show in product   
            
         
        """
        pass
    def AddCompileUnitIndex(self, compileUnitStartIndex: int, compileUnitEndIndex: int) -> None:
        """
         Add a index of network that will be in a method
                with this function is possible to add several network  
        """
        pass
    def AddStatementIndexes(self, compileUnitIndex: int, startStatementIndex: int, endStatementIndex: int) -> None:
        """
         Add a index of start statment in a network and index of end of statment 
        """
        pass
    def AddStatementUnitUIdRange(self, startUId: int, endUId: int) -> None:
        """
         Add the selected statement unit UIds to selection list within the range of given start- and endUId. 
        """
        pass
    def SetPlcCodeBlock(self, plcBlock: PlcBlock) -> None:
        """
         Set selected PlcCodeBlock 
        """
        pass
import NXOpen
class CreateNamingSchemeBuilder(NXOpen.Builder): 
    """
        JA class for dialog for naming rule settings
    """
    pass
import NXOpen
class CreatePmiNoteBuilder(NXOpen.Builder): 
    """Create PMINote dialog JA class """
    @property
    def SelectedEngObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedEngObject
         Returns the selected engobject from project  
            
         
        """
        pass
import NXOpen
class CreateProductBuilder(AMEBaseBuilder): 
    """ Create and classify product """
    @property
    def SelectionBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectionBaseDefinition
         Returns  the base definition selection builder i.  
          e. Creates  AME::SelectionBaseDefinitionBuilder    
         
        """
        pass
    @property
    def SelectionEngObjectDefinition(self) -> SelectionEngineeringObjectDefinitionBuilder:
        """
        Getter for property: ( SelectionEngineeringObjectDefinitionBuilder NXOp) SelectionEngObjectDefinition
         Returns the engineering object definition  
            
         
        """
        pass
    def CreateTypeAttribute(self) -> NXOpen.NXObject:
        """
         Creates a new type attribute object 
         Returns typeAtt ( NXOpen.NXObject): .
        """
        pass
    def SetObjectNameOnTypeAttr(self) -> None:
        """
         Sets the Object Name on Type Attribute Object.
        """
        pass
import NXOpen
class CreateReportBuilder(NXOpen.Builder): 
    """ Represents a Report Creation class Builder  """
    class Types(Enum):
        """
        Members Include: 
         |AspectListFunction| 
         |AspectListLocation| 
         |BillOfMaterial| 
         |BillOfMaterialCrossref| 
         |CableDiagram| 
         |CableList| 
         |ConnectionListBomElectrical| 
         |ConnectionListElectrical| 
         |ConnectionListHose| 
         |ConnectionListTube| 
         |TableOfContents| 
         |ProjectTitlePage| 
         |TerminalDiagram| 
         |TerminalDiagramCrossref| 
         |TerminalMatrixDiagram| 
         |TerminalMatrixDiagramCrossref| 
         |ConnectionBomHose| 
         |ConnectionBomTube| 
         |DevicePurchaseList| 
         |CablePurchaseList| 

        """
        AspectListFunction: int
        AspectListLocation: int
        BillOfMaterial: int
        BillOfMaterialCrossref: int
        CableDiagram: int
        CableList: int
        ConnectionListBomElectrical: int
        ConnectionListElectrical: int
        ConnectionListHose: int
        ConnectionListTube: int
        TableOfContents: int
        ProjectTitlePage: int
        TerminalDiagram: int
        TerminalDiagramCrossref: int
        TerminalMatrixDiagram: int
        TerminalMatrixDiagramCrossref: int
        ConnectionBomHose: int
        ConnectionBomTube: int
        DevicePurchaseList: int
        CablePurchaseList: int
        @staticmethod
        def ValueOf(value: int) -> CreateReportBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Type(self) -> CreateReportBuilder.Types:
        """
        Getter for property: ( CreateReportBuilder.Types NXOp) Type
         Returns the report type  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: CreateReportBuilder.Types):
        """
        Setter for property: ( CreateReportBuilder.Types NXOp) Type
         Returns the report type  
            
         
        """
        pass
import NXOpen
class CreateRuleSetBuilder(NXOpen.Builder): 
    """
        JA class for crete rule set
    """
    class RulesType(Enum):
        """
        Members Include: 
         |NamingScheme| 
         |PlcAddressingRule| 

        """
        NamingScheme: int
        PlcAddressingRule: int
        @staticmethod
        def ValueOf(value: int) -> CreateRuleSetBuilder.RulesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def RuleType(self) -> CreateRuleSetBuilder.RulesType:
        """
        Getter for property: ( CreateRuleSetBuilder.RulesType NXOp) RuleType
         Returns the enum to rule set type   
            
         
        """
        pass
    @RuleType.setter
    def RuleType(self, ruleType: CreateRuleSetBuilder.RulesType):
        """
        Setter for property: ( CreateRuleSetBuilder.RulesType NXOp) RuleType
         Returns the enum to rule set type   
            
         
        """
        pass
class CreateSystemIDBBuilder(InstanceDataBlockBuilder): 
    """ JA class for the reuse rule dialog"""
    pass
import NXOpen
class CreateTemplateBuilder(NXOpen.Builder): 
    """Create Template dialog JA class """
    @property
    def CreateFragmentToggle(self) -> bool:
        """
        Getter for property: (bool) CreateFragmentToggle
         Returns the template toggle for create fragment  
            
         
        """
        pass
    @CreateFragmentToggle.setter
    def CreateFragmentToggle(self, createFragmentToggle: bool):
        """
        Setter for property: (bool) CreateFragmentToggle
         Returns the template toggle for create fragment  
            
         
        """
        pass
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedObjects
         Returns the selected objects from project  
            
         
        """
        pass
    @property
    def TemplateNameAndDescription(self) -> ObjectNameBuilder:
        """
        Getter for property: ( ObjectNameBuilder NXOp) TemplateNameAndDescription
         Returns the template name and description ui block  
            
         
        """
        pass
    def CreateTemplateProject(self) -> Project:
        """
        Creates the template project
         Returns templateProject ( Project NXOp): .
        """
        pass
class CreateTemplateDefinitionBuilder(CreateDefinitionBuilder): 
    """ Create and classify template definition """
    def SetTemplateProject(self, templateProject: Project) -> None:
        """
        Set the template part 
        """
        pass
import NXOpen
class CreateValueSetBuilder(NXOpen.Builder): 
    """  Creates the value set data give name and description """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description for the value set   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description for the value set   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name for the value set   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name for the value set   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Tooling
class DataTypeBuilder(NXOpen.TaggedObject): 
    """ JA class for the data type dialog"""
    @property
    def DataLength(self) -> int:
        """
        Getter for property: (int) DataLength
         Returns the int datalength    
            
         
        """
        pass
    @DataLength.setter
    def DataLength(self, dataLength: int):
        """
        Setter for property: (int) DataLength
         Returns the int datalength    
            
         
        """
        pass
    @property
    def DataTypeSource(self) -> PlcDataTypeSource:
        """
        Getter for property: ( PlcDataTypeSource NXOp) DataTypeSource
         Returns the DataTypeSource   
            
         
        """
        pass
    @DataTypeSource.setter
    def DataTypeSource(self, dataTypeSource: PlcDataTypeSource):
        """
        Setter for property: ( PlcDataTypeSource NXOp) DataTypeSource
         Returns the DataTypeSource   
            
         
        """
        pass
    @property
    def SelectedDataTypePosition(self) -> int:
        """
        Getter for property: (int) SelectedDataTypePosition
         Returnsthe  DataType   
            
         
        """
        pass
    @SelectedDataTypePosition.setter
    def SelectedDataTypePosition(self, dataTypePos: int):
        """
        Setter for property: (int) SelectedDataTypePosition
         Returnsthe  DataType   
            
         
        """
        pass
    @property
    def SelectedUDTFromLibrary(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedUDTFromLibrary
         Returns the library UDT selection  
            
         
        """
        pass
    @property
    def UdtByName(self) -> str:
        """
        Getter for property: (str) UdtByName
         Returns the string udt by name data type   
            
         
        """
        pass
    @UdtByName.setter
    def UdtByName(self, udtByName: str):
        """
        Setter for property: (str) UdtByName
         Returns the string udt by name data type   
            
         
        """
        pass
    @property
    def UdtFromProject(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) UdtFromProject
         Returns the project UDT selection   
            
         
        """
        pass
    def GetPopulatedDataTypes(self, sectionType: MemorySectionType) -> List[str]:
        """
         The PopulatedDataTypes 
         Returns dataTypes (List[str]): .
        """
        pass
import NXOpen
class DefineAspectBuilder(NXOpen.Builder): 
    """ Define Aspects for Engineering Object Definition """
    @property
    def Function(self) -> bool:
        """
        Getter for property: (bool) Function
         Returns the value for Function Aspect  
            
         
        """
        pass
    @Function.setter
    def Function(self, val: bool):
        """
        Setter for property: (bool) Function
         Returns the value for Function Aspect  
            
         
        """
        pass
    @property
    def FunctionDesignation(self) -> bool:
        """
        Getter for property: (bool) FunctionDesignation
         Returns the value for Function Aspect  
            
         
        """
        pass
    @FunctionDesignation.setter
    def FunctionDesignation(self, val: bool):
        """
        Setter for property: (bool) FunctionDesignation
         Returns the value for Function Aspect  
            
         
        """
        pass
    @property
    def Location(self) -> bool:
        """
        Getter for property: (bool) Location
         Returns the value for Function Aspect  
            
         
        """
        pass
    @Location.setter
    def Location(self, val: bool):
        """
        Setter for property: (bool) Location
         Returns the value for Function Aspect  
            
         
        """
        pass
    @property
    def LocationDesignation(self) -> bool:
        """
        Getter for property: (bool) LocationDesignation
         Returns the value for Function Aspect  
            
         
        """
        pass
    @LocationDesignation.setter
    def LocationDesignation(self, val: bool):
        """
        Setter for property: (bool) LocationDesignation
         Returns the value for Function Aspect  
            
         
        """
        pass
    @property
    def Product(self) -> bool:
        """
        Getter for property: (bool) Product
         Returns the value for Function Aspect  
            
         
        """
        pass
    @Product.setter
    def Product(self, val: bool):
        """
        Setter for property: (bool) Product
         Returns the value for Function Aspect  
            
         
        """
        pass
    @property
    def ProductDesignation(self) -> bool:
        """
        Getter for property: (bool) ProductDesignation
         Returns the value for Function Aspect  
            
         
        """
        pass
    @ProductDesignation.setter
    def ProductDesignation(self, val: bool):
        """
        Setter for property: (bool) ProductDesignation
         Returns the value for Function Aspect  
            
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.Diagramming.Tables
class DiagramManager(NXOpen.Object): 
    """ Represents an object that manages sheet elements. """
    def AddFragmentPlacedSheetElement(fragmentObject: FragmentObject, sheetElement: NXOpen.Diagramming.SheetElement) -> None:
        """
         Add placed sheet element to fragment object 
        """
        pass
    def CloseDiagramSheet(sheet: NXOpen.Diagramming.Sheet, appId: int) -> None:
        """
         Close diagram sheet
        """
        pass
    def CopySchematicObjects(elements: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Copy schematic object 
        """
        pass
    def CreateConnection(sheet: NXOpen.Diagramming.Sheet, startPort: AMEExtendedObject, endPort: AMEExtendedObject, p2dBendPoints: List[NXOpen.Point2d]) -> NXOpen.Diagramming.Connection:
        """
         Create Diagramming Connection.
                    This is deprecated no longer should be used for future use cases
         Returns connection ( NXOpen.Diagramming.Connection): .
        """
        pass
    def CreateDiagramSheet(partTag: NXOpen.NXObject) -> NXOpen.Diagramming.Sheet:
        """
         Get diagram sheet
         Returns sheet ( NXOpen.Diagramming.Sheet): .
        """
        pass
    def CreatePlcFlowChartConnection(sheet: NXOpen.Diagramming.Sheet, targetPort: NXOpen.Diagramming.Port, connection: NXOpen.Diagramming.Connection, connectionEndType: int) -> None:
        """
         Create Plc transition Connection
        """
        pass
    def CreatePlcFlowChartNode(sheet: NXOpen.Diagramming.Sheet, locationX: float, locationY: float, selectedNode: AMEExtendedObject) -> NXOpen.Diagramming.Node:
        """
         Create plc flow chart node
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def CreatePlcFlowChartOperandNode(operandType: PlcFlowChartNodeType, sheet: NXOpen.Diagramming.Sheet, locationX: float, locationY: float) -> NXOpen.Diagramming.Node:
        """
         Creates the sheet element depending on the variable type
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def CreatePlcStateChartNode(sheet: NXOpen.Diagramming.Sheet, locationX: float, locationY: float, isEndStateInCreation: bool) -> NXOpen.Diagramming.Node:
        """
         Create Plc state chart node
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def CreatePlcStateChartTransition(sheet: NXOpen.Diagramming.Sheet, targetPort: NXOpen.Diagramming.Port, connection: NXOpen.Diagramming.Connection, isDetachedTransition: bool, connectionEndType: int) -> None:
        """
         Create Plc transition Connection
        """
        pass
    def CreateSchematicConnection(sheet: NXOpen.Diagramming.Sheet, startPort: NXOpen.Diagramming.Port, endPort: NXOpen.Diagramming.Port, p2dBendPoints: List[NXOpen.Point2d]) -> List[NXOpen.NXObject]:
        """
         Create Diagramming Connection 
         Returns objects ( NXOpen.NXObject Li): .
        """
        pass
    def CreateSchematicNode(sheet: NXOpen.Diagramming.Sheet, engObject: AMEEngObject, locationX: float, locationY: float, symbolVariantName: str) -> NXOpen.Diagramming.Node:
        """
         Create Schematic Diagram Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def CreateSocket(sheet: NXOpen.Diagramming.Sheet, locationX: float, locationY: float) -> NXOpen.Diagramming.Node:
        """
         Create Socket Diagram Node Copy
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def CreateTopologyNode(sheet: NXOpen.Diagramming.Sheet, engObject: AMEEngObject, locationX: float, locationY: float) -> NXOpen.Diagramming.Node:
        """
         Create Topology Diagram Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def CutSchematicObjects(elements: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Cut schematic object 
        """
        pass
    def DeleteConnections(elements: List[NXOpen.Diagramming.Connection]) -> None:
        """
         Delete Connections 
        """
        pass
    def DeletePlacedSheetElements(fragment: FragmentObject) -> None:
        """
         Delete placed sheet elements from page
        """
        pass
    def DeleteSheetElements(elements: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Delete Sheet Element
        """
        pass
    def DisconnectConnection(connection: NXOpen.Diagramming.Connection) -> None:
        """
         Detach Diagramming Connection 
        """
        pass
    def GetSheetPartFromPage(pageObject: PageObject) -> NXOpen.NXObject:
        """
         Get Diagramming Sheet's Part From Page 
         Returns partTag ( NXOpen.NXObject): .
        """
        pass
    def InstantiateTypedProductComponentInstance(pageObject: PageObject, instanceObject: TypedProductComponentInstance, locationX: float, locationY: float, symbolVariantName: str) -> NXOpen.Diagramming.Node:
        """
         Instantiate Product Component instance and create Schematic Diagram Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def LaunchPage(pageObject: PageObject, isNewWindow: bool) -> None:
        """
         Launch fragment diagram sheet
        """
        pass
    def PasteSchematicObjects(page: PageObject, locationX: float, locationY: float) -> List[NXOpen.NXObject]:
        """
         Paste schematic object 
         Returns newObjects ( NXOpen.NXObject Li): .
        """
        pass
    def PlaceFragmentOnPage(fragment: FragmentObject, page: PageObject, locationX: float, locationY: float) -> None:
        """
         Place Copied Fragment on page
        """
        pass
    def ReconnectConnection(sheet: NXOpen.Diagramming.Sheet, connection: NXOpen.Diagramming.Connection, targetPort: AMEExtendedObject, connectionLocationType: int) -> None:
        """
         Reconnect Diagramming Connection 
        """
        pass
    def ReconnectSchematicConnection(sheet: NXOpen.Diagramming.Sheet, connection: NXOpen.Diagramming.Connection, targetPort: NXOpen.Diagramming.Port, connectionLocationType: int) -> None:
        """
         Reconnect Diagramming Connection 
        """
        pass
    def RefreshFragmentBoundingBox(sheet: NXOpen.Diagramming.Sheet) -> None:
        """
         Creating or Updating fragment Sheet Bounding Box in Template 
        """
        pass
    def RemovePlugPort(sheet: NXOpen.Diagramming.Sheet) -> None:
        """
         Remove plug from object 
        """
        pass
    def ResetContactBlockBoundingBox(node: NXOpen.Diagramming.Node) -> None:
        """
         Reset contact block bounding box 
        """
        pass
    def SetFragmentBoundingBoxAnchorPoint(fragment: FragmentObject, anchorX: float, anchorY: float) -> None:
        """
         Creating or Updating fragment Sheet Bounding Box in Template 
        """
        pass
    def SetReportTableName(table: NXOpen.Diagramming.Tables.Table) -> None:
        """
         Set report table name
        """
        pass
    def SetStartPortForTransition(sheet: NXOpen.Diagramming.Sheet, startPort: NXOpen.Diagramming.Port) -> NXOpen.Diagramming.Connection:
        """
         To set port for Plc transition Connection
         Returns connection ( NXOpen.Diagramming.Connection): .
        """
        pass
    def SetTeeJunctionRepresentationStyle(elements: List[NXOpen.Diagramming.Node], representationStyle: AmeJunctionRepresentationStyleType) -> None:
        """
         Set representation style for tee Junction  
        """
        pass
    def SetTeeJunctionVariant(elements: List[NXOpen.Diagramming.Node], variantIndex: AmeTeeJunctionVariant) -> None:
        """
         Set variant for tee Junction  
        """
        pass
    def ShowHideConnectionDirection(showHideConnectionDirection: bool) -> None:
        """
         ShowHide Connection Direction symbol of ports on schematics pages.
        """
        pass
    def SwapConnectionSourceTarget(connections: List[NXOpen.NXObject]) -> None:
        """
         Swap source target for ame connections 
        """
        pass
    def SwitchMountingOrientation(engObject: AMEEngObject) -> None:
        """
         Switch Mounting Orientation of the input NXOpen.AME.AMEEngObject object.
        """
        pass
    def UpdateCableInformation(cableEO: AMEEngObject, pageObjects: List[PageObject]) -> None:
        """
         Update Cable information like Cores and Core Order Indices
        """
        pass
    def UpdateConnectionBendPoints(connection: NXOpen.Diagramming.Connection, bendPoints: List[NXOpen.Point2d]) -> None:
        """
         Update Diagramming Connection with new bend points
        """
        pass
    def UpdateDeviceAnnotations(annotation: NXOpen.Diagramming.Annotation, location: NXOpen.Point2d) -> None:
        """
         Update annotation location of the instantiated types
        """
        pass
    def UpdateLinePoints(sheetElement: NXOpen.Diagramming.SheetElement, startPoint: NXOpen.Point2d, endPoint: NXOpen.Point2d) -> None:
        """
         Update Line start and end points
        """
        pass
    def UpdateNodeLocation(node: NXOpen.Diagramming.Node, cordinateX: float, cordinateY: float) -> None:
        """
         Update node location
        """
        pass
    def UpdateNodeRotation(node: NXOpen.Diagramming.Node, rotation: float) -> None:
        """
         Update node rotation 
        """
        pass
    def UpdateNodeSize(node: NXOpen.Diagramming.Node, coordinateX: float, coordinateY: float, height: float, width: float) -> None:
        """
         Update node size 
        """
        pass
    def UpdateTextNote(annotation: NXOpen.Diagramming.Annotation, location: NXOpen.Point2d, anchor: NXOpen.Point2d, height: float, width: float, angle: float, isUpdateBoundingBox: bool) -> None:
        """
         Update textnote annotation location, Height, width and update fragment bounding box
        """
        pass
import NXOpen
import NXOpen.Diagramming
class DiagramNodeBuilder(NXOpen.Builder): 
    """ Represents builder for  Diagramming::Node """
    def CreateDiagramNode(self, pageObject: PageObject, symbolVariantName: str) -> NXOpen.Diagramming.Node:
        """
         Method to create the Diagramming Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetDrawingStandard(self, drawingStandard: Manage2dSymbolsBuilder.SymbolDrawingStandard) -> None:
        """
         Set the Symbol Drawing Standard 
        """
        pass
    def SetReferenceObject(self, objTag: NXOpen.NXObject) -> None:
        """
         Set the Object for which Node is to be created 
        """
        pass
    def SetSymbolLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set the symbol location on page. 
        """
        pass
    def UpdateDiagramNode(self, pageObject: PageObject, updatedSymbolVariantName: str) -> NXOpen.Diagramming.Node:
        """
         Method to update the Diagramming Node with given symbol variant 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
class DocumentRoot(AMEBaseNode): 
    """ Document Root Node class """
    pass
import NXOpen
import NXOpen.AME.DB
class DocumentStructureBuilder(NXOpen.Builder): 
    """ Class to define Document Structure """
    def GetDocumentStructureObject(self, documetType: DocumentType) -> NXOpen.AME.DB.DocumentStructure:
        """
         Get the Document Structure object for a given Document type. 
         Returns docStruct ( NXOpen.AME.DB.DocumentStructure): .
        """
        pass
    def ResetDocumentStructure(self, documetType: DocumentType) -> None:
        """
         Reset the Document Structure for a given Document type. 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Reset the Document Structure for all Document types. 
        """
        pass
class DocumentType(Enum):
    """
    Members Include: 
     |AspectStructureOverview| 
     |CableDiagram| 
     |CableList| 
     |OrderList| 
     |PartListBom| 
     |PlugList| 
     |TableOfContent| 
     |TerminalDiagram| 
     |TerminalStripList| 
     |TitlePage| 
     |WireTubeConnectionLists| 
     |WireList| 
     |MultiLineDiagram| 
     |SingleLineDiagram| 
     |BusTopologyDiagram| 
     |PowerSupplyDiagram| 
     |ViewPage| 
     |FluidicDiagram| 
     |CabinetLayout| 
     |SummarizeBom| 

    """
    AspectStructureOverview: int
    CableDiagram: int
    CableList: int
    OrderList: int
    PartListBom: int
    PlugList: int
    TableOfContent: int
    TerminalDiagram: int
    TerminalStripList: int
    TitlePage: int
    WireTubeConnectionLists: int
    WireList: int
    MultiLineDiagram: int
    SingleLineDiagram: int
    BusTopologyDiagram: int
    PowerSupplyDiagram: int
    ViewPage: int
    FluidicDiagram: int
    CabinetLayout: int
    SummarizeBom: int
    @staticmethod
    def ValueOf(value: int) -> DocumentType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class DrawingStandardSettingsBuilder(NXOpen.Builder): 
    """ DrawingStandardSettingsBuilder """
    class DrawingStandardType(Enum):
        """
        Members Include: 
         |IEC| 
         |ANSI| 
         |NonStandard| 

        """
        IEC: int
        ANSI: int
        NonStandard: int
        @staticmethod
        def ValueOf(value: int) -> DrawingStandardSettingsBuilder.DrawingStandardType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DrawingStandard(self) -> DrawingStandardSettingsBuilder.DrawingStandardType:
        """
        Getter for property: ( DrawingStandardSettingsBuilder.DrawingStandardType NXOp) DrawingStandard
         Returns the current drawing standar   
            
         
        """
        pass
    @DrawingStandard.setter
    def DrawingStandard(self, version: DrawingStandardSettingsBuilder.DrawingStandardType):
        """
        Setter for property: ( DrawingStandardSettingsBuilder.DrawingStandardType NXOp) DrawingStandard
         Returns the current drawing standar   
            
         
        """
        pass
import NXOpen
class DxfdwgExportBuilder(NXOpen.DxfdwgCreator): 
    """ Represents builder for  AME::DxfdwgExportBuilder """
    def ConvertSheetTo2dpart(self, draftingSheet: NXOpen.NXObject, unloadPart: bool) -> str:
        """
         Converts and sets the pages to be exported.
         Returns temp2dpartFilename (str): .
        """
        pass
    def CreateTemp2dpartsDir(self) -> str:
        """
         Creates a temp dir for 2d parts.
         Returns temp2dpartsDir (str): .
        """
        pass
    def SetOutputDxfdwgFolder(self, outputDxfdwgFolder: str) -> None:
        """
         Sets output dir for dxfdwg files.
        """
        pass
class EClassClassNode(EClassObjectNode): 
    """ EClassData Tree Node class """
    pass
class EClassDataRoot(AMEBaseNode): 
    """ EClassData Root Node class """
    pass
class EClassFolderNode(AMEBaseNode): 
    """ EClass Folder Node class """
    pass
class EClassGlobalObjectNode(AMEBaseNode): 
    """ EClassGlobalObject Tree Node class """
    pass
class EClassNode(AMEBaseNode): 
    """ EClassData Tree Node class """
    pass
class EClassObjectNode(EClassNode): 
    """ EClassData Tree Node class """
    pass
class EClassPropertyNode(EClassGlobalObjectNode): 
    """ EClassProperty Tree Node class """
    pass
class EClassSegmentNode(AMEBaseNode): 
    """ EClass Segment Node class """
    pass
class EClassValueListNode(EClassGlobalObjectNode): 
    """ EClassValueList Tree Node class """
    pass
class EClassVersionNode(AMEBaseNode): 
    """ EClass Version Node class """
    pass
import NXOpen
class EditAnnotationBuilder(NXOpen.Builder): 
    """ the builder for creating edit annotation """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of diagramming node    
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of diagramming node    
            
         
        """
        pass
class EditClauseBuilder(MultipleObjectsBuilder): 
    """ Naming Rule Builder """
    class CableAssigmentOperator(Enum):
        """
        Members Include: 
         |Equal| 

        """
        Equal: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.CableAssigmentOperator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CableAssigmentValue(Enum):
        """
        Members Include: 
         |TrueValue| 
         |FalseValue| 

        """
        TrueValue: int
        FalseValue: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.CableAssigmentValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MathOperatorsType(Enum):
        """
        Members Include: 
         |IsEqual| 
         |IsNotEqual| 
         |IsGreaterThanOrEqual| 
         |IsGreaterThan| 
         |IsLessThanOrEqual| 
         |IsLessThan| 

        """
        IsEqual: int
        IsNotEqual: int
        IsGreaterThanOrEqual: int
        IsGreaterThan: int
        IsLessThanOrEqual: int
        IsLessThan: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.MathOperatorsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Operator(Enum):
        """
        Members Include: 
         |As| 
         |Under| 
         |OfType| 

        """
        As: int
        Under: int
        OfType: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.Operator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParentPropertyAspect(Enum):
        """
        Members Include: 
         |FunctionAspect| 
         |LocationAspect| 
         |ProductAspect| 
         |AutomationAspect| 

        """
        FunctionAspect: int
        LocationAspect: int
        ProductAspect: int
        AutomationAspect: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.ParentPropertyAspect:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProductAssignmentOperator(Enum):
        """
        Members Include: 
         |Equal| 
         |NotEqual| 

        """
        Equal: int
        NotEqual: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.ProductAssignmentOperator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProductAssignmentValue(Enum):
        """
        Members Include: 
         |TrueValue| 
         |FalseValue| 

        """
        TrueValue: int
        FalseValue: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.ProductAssignmentValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QueryClauseOperatorType(Enum):
        """
        Members Include: 
         |And| 
         |Or| 
         |NotSet| 

        """
        And: int
        Or: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.QueryClauseOperatorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QueryConnectedValue(Enum):
        """
        Members Include: 
         |TrueValue| 
         |FalseValue| 

        """
        TrueValue: int
        FalseValue: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.QueryConnectedValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QueryPortCondition(Enum):
        """
        Members Include: 
         |Exists| 
         |IsConnected| 

        """
        Exists: int
        IsConnected: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.QueryPortCondition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QueryPropertyAppliedTo(Enum):
        """
        Members Include: 
         |Classification| 
         |LibraryObject| 
         |Aspect| 
         |General| 
         |Tag| 

        """
        Classification: int
        LibraryObject: int
        Aspect: int
        General: int
        Tag: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.QueryPropertyAppliedTo:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QueryPropertyOfCategory(Enum):
        """
        Members Include: 
         |FunctionAspect| 
         |LocationAspect| 
         |ProductAspect| 

        """
        FunctionAspect: int
        LocationAspect: int
        ProductAspect: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.QueryPropertyOfCategory:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QueryPropertyOfClassLibCategory(Enum):
        """
        Members Include: 
         |Type| 
         |Product| 

        """
        Type: int
        Product: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.QueryPropertyOfClassLibCategory:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Classification| 
         |LibraryObject| 
         |Aspect| 
         |Property| 
         |Port| 
         |ProductAssignment| 
         |ParentProperty| 
         |CableAssignment| 

        """
        Classification: int
        LibraryObject: int
        Aspect: int
        Property: int
        Port: int
        ProductAssignment: int
        ParentProperty: int
        CableAssignment: int
        @staticmethod
        def ValueOf(value: int) -> EditClauseBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllAspects(self) -> bool:
        """
        Getter for property: (bool) AllAspects
         Returns the all aspects option status whether ON or OFF   
            
         
        """
        pass
    @AllAspects.setter
    def AllAspects(self, toggleAllAspects: bool):
        """
        Setter for property: (bool) AllAspects
         Returns the all aspects option status whether ON or OFF   
            
         
        """
        pass
    @property
    def AspectOperator(self) -> EditClauseBuilder.Operator:
        """
        Getter for property: ( EditClauseBuilder.Operator NXOp) AspectOperator
         Returns the query operator for Aspect object   
            
         
        """
        pass
    @AspectOperator.setter
    def AspectOperator(self, aspectOperator: EditClauseBuilder.Operator):
        """
        Setter for property: ( EditClauseBuilder.Operator NXOp) AspectOperator
         Returns the query operator for Aspect object   
            
         
        """
        pass
    @property
    def CableAssignmentOperator(self) -> EditClauseBuilder.CableAssigmentOperator:
        """
        Getter for property: ( EditClauseBuilder.CableAssigmentOperator NXOp) CableAssignmentOperator
         Returns the query operator for cable assignment object   
            
         
        """
        pass
    @CableAssignmentOperator.setter
    def CableAssignmentOperator(self, cableAssignmentOperator: EditClauseBuilder.CableAssigmentOperator):
        """
        Setter for property: ( EditClauseBuilder.CableAssigmentOperator NXOp) CableAssignmentOperator
         Returns the query operator for cable assignment object   
            
         
        """
        pass
    @property
    def CableAssignmentValue(self) -> EditClauseBuilder.CableAssigmentValue:
        """
        Getter for property: ( EditClauseBuilder.CableAssigmentValue NXOp) CableAssignmentValue
         Returns the query value for cable assignment object   
            
         
        """
        pass
    @CableAssignmentValue.setter
    def CableAssignmentValue(self, cableAssignmentValue: EditClauseBuilder.CableAssigmentValue):
        """
        Setter for property: ( EditClauseBuilder.CableAssigmentValue NXOp) CableAssignmentValue
         Returns the query value for cable assignment object   
            
         
        """
        pass
    @property
    def ClassificationOperator(self) -> EditClauseBuilder.Operator:
        """
        Getter for property: ( EditClauseBuilder.Operator NXOp) ClassificationOperator
         Returns the query operator for Classification object  
            
         
        """
        pass
    @ClassificationOperator.setter
    def ClassificationOperator(self, classificationOperator: EditClauseBuilder.Operator):
        """
        Setter for property: ( EditClauseBuilder.Operator NXOp) ClassificationOperator
         Returns the query operator for Classification object  
            
         
        """
        pass
    @property
    def ClauseOperatorType(self) -> EditClauseBuilder.QueryClauseOperatorType:
        """
        Getter for property: ( EditClauseBuilder.QueryClauseOperatorType NXOp) ClauseOperatorType
         Returns the clause operator of query  
            
         
        """
        pass
    @ClauseOperatorType.setter
    def ClauseOperatorType(self, clauseOperator: EditClauseBuilder.QueryClauseOperatorType):
        """
        Setter for property: ( EditClauseBuilder.QueryClauseOperatorType NXOp) ClauseOperatorType
         Returns the clause operator of query  
            
         
        """
        pass
    @property
    def ConditionType(self) -> EditClauseBuilder.Types:
        """
        Getter for property: ( EditClauseBuilder.Types NXOp) ConditionType
         Returns the condition type  
            
         
        """
        pass
    @ConditionType.setter
    def ConditionType(self, conditionType: EditClauseBuilder.Types):
        """
        Setter for property: ( EditClauseBuilder.Types NXOp) ConditionType
         Returns the condition type  
            
         
        """
        pass
    @property
    def ConnectedValue(self) -> EditClauseBuilder.QueryConnectedValue:
        """
        Getter for property: ( EditClauseBuilder.QueryConnectedValue NXOp) ConnectedValue
         Returns the value truefalse  
            
         
        """
        pass
    @ConnectedValue.setter
    def ConnectedValue(self, connectedValue: EditClauseBuilder.QueryConnectedValue):
        """
        Setter for property: ( EditClauseBuilder.QueryConnectedValue NXOp) ConnectedValue
         Returns the value truefalse  
            
         
        """
        pass
    @property
    def MathOperator(self) -> EditClauseBuilder.MathOperatorsType:
        """
        Getter for property: ( EditClauseBuilder.MathOperatorsType NXOp) MathOperator
         Returns the math operatos  
            
         
        """
        pass
    @MathOperator.setter
    def MathOperator(self, mathOperatorsType: EditClauseBuilder.MathOperatorsType):
        """
        Setter for property: ( EditClauseBuilder.MathOperatorsType NXOp) MathOperator
         Returns the math operatos  
            
         
        """
        pass
    @property
    def NumberOfConnectedPorts(self) -> int:
        """
        Getter for property: (int) NumberOfConnectedPorts
         Returns the query value number of connected ports   
            
         
        """
        pass
    @NumberOfConnectedPorts.setter
    def NumberOfConnectedPorts(self, numberOfConnectedPorts: int):
        """
        Setter for property: (int) NumberOfConnectedPorts
         Returns the query value number of connected ports   
            
         
        """
        pass
    @property
    def ParentPropertySelectedAspect(self) -> EditClauseBuilder.ParentPropertyAspect:
        """
        Getter for property: ( EditClauseBuilder.ParentPropertyAspect NXOp) ParentPropertySelectedAspect
         Returns the selected aspect for parent property   
            
         
        """
        pass
    @ParentPropertySelectedAspect.setter
    def ParentPropertySelectedAspect(self, parentPropertySelectedAspect: EditClauseBuilder.ParentPropertyAspect):
        """
        Setter for property: ( EditClauseBuilder.ParentPropertyAspect NXOp) ParentPropertySelectedAspect
         Returns the selected aspect for parent property   
            
         
        """
        pass
    @property
    def PortCondition(self) -> EditClauseBuilder.QueryPortCondition:
        """
        Getter for property: ( EditClauseBuilder.QueryPortCondition NXOp) PortCondition
         Returns the port operator  
            
         
        """
        pass
    @PortCondition.setter
    def PortCondition(self, portCondition: EditClauseBuilder.QueryPortCondition):
        """
        Setter for property: ( EditClauseBuilder.QueryPortCondition NXOp) PortCondition
         Returns the port operator  
            
         
        """
        pass
    @property
    def PortDomain(self) -> str:
        """
        Getter for property: (str) PortDomain
         Returns the port domain  
            
         
        """
        pass
    @PortDomain.setter
    def PortDomain(self, portDomain: str):
        """
        Setter for property: (str) PortDomain
         Returns the port domain  
            
         
        """
        pass
    @property
    def ProductAssigmentOperator(self) -> EditClauseBuilder.ProductAssignmentOperator:
        """
        Getter for property: ( EditClauseBuilder.ProductAssignmentOperator NXOp) ProductAssigmentOperator
         Returns the query operator for product assignment object   
            
         
        """
        pass
    @ProductAssigmentOperator.setter
    def ProductAssigmentOperator(self, productAssigmentOperator: EditClauseBuilder.ProductAssignmentOperator):
        """
        Setter for property: ( EditClauseBuilder.ProductAssignmentOperator NXOp) ProductAssigmentOperator
         Returns the query operator for product assignment object   
            
         
        """
        pass
    @property
    def ProductAssigmentValue(self) -> EditClauseBuilder.ProductAssignmentValue:
        """
        Getter for property: ( EditClauseBuilder.ProductAssignmentValue NXOp) ProductAssigmentValue
         Returns the query value for product assignment object   
            
         
        """
        pass
    @ProductAssigmentValue.setter
    def ProductAssigmentValue(self, productAssigmentValue: EditClauseBuilder.ProductAssignmentValue):
        """
        Setter for property: ( EditClauseBuilder.ProductAssignmentValue NXOp) ProductAssigmentValue
         Returns the query value for product assignment object   
            
         
        """
        pass
    @property
    def PropertyAppliedTo(self) -> EditClauseBuilder.QueryPropertyAppliedTo:
        """
        Getter for property: ( EditClauseBuilder.QueryPropertyAppliedTo NXOp) PropertyAppliedTo
         Returns the property applied to  
            
         
        """
        pass
    @PropertyAppliedTo.setter
    def PropertyAppliedTo(self, propertyAppliedTo: EditClauseBuilder.QueryPropertyAppliedTo):
        """
        Setter for property: ( EditClauseBuilder.QueryPropertyAppliedTo NXOp) PropertyAppliedTo
         Returns the property applied to  
            
         
        """
        pass
    @property
    def PropertyOfCategory(self) -> int:
        """
        Getter for property: (int) PropertyOfCategory
         Returns the property of  
            
         
        """
        pass
    @PropertyOfCategory.setter
    def PropertyOfCategory(self, propertyOfCategory: int):
        """
        Setter for property: (int) PropertyOfCategory
         Returns the property of  
            
         
        """
        pass
    @property
    def ReuseLibraryOperator(self) -> EditClauseBuilder.Operator:
        """
        Getter for property: ( EditClauseBuilder.Operator NXOp) ReuseLibraryOperator
         Returns the query operator for Reuse Library object  
            
         
        """
        pass
    @ReuseLibraryOperator.setter
    def ReuseLibraryOperator(self, reuseLibraryOperator: EditClauseBuilder.Operator):
        """
        Setter for property: ( EditClauseBuilder.Operator NXOp) ReuseLibraryOperator
         Returns the query operator for Reuse Library object  
            
         
        """
        pass
    @property
    def SelectAspect(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectAspect
         Returns the selected aspect   
            
         
        """
        pass
    @property
    def SelectClassification(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the selected classification   
            
         
        """
        pass
    @property
    def SelectFromMemberSelect(self) -> SelectionEngineeringObjectDefinitionBuilder:
        """
        Getter for property: ( SelectionEngineeringObjectDefinitionBuilder NXOp) SelectFromMemberSelect
         Returns the engineering object definition  
            
         
        """
        pass
    @property
    def SelectLibraryObject(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectLibraryObject
         Returns the engineering object definition or product definition  
            
         
        """
        pass
    @property
    def SelectedQuery(self) -> AMEQuery:
        """
        Getter for property: ( AMEQuery NXOp) SelectedQuery
         Returns the query object  
            
         
        """
        pass
    @SelectedQuery.setter
    def SelectedQuery(self, selectedQuery: AMEQuery):
        """
        Setter for property: ( AMEQuery NXOp) SelectedQuery
         Returns the query object  
            
         
        """
        pass
    @property
    def SelectedQueryClause(self) -> QueryClause:
        """
        Getter for property: ( QueryClause NXOp) SelectedQueryClause
         Returns the selected query clause  
            
         
        """
        pass
    @SelectedQueryClause.setter
    def SelectedQueryClause(self, selectedClause: QueryClause):
        """
        Setter for property: ( QueryClause NXOp) SelectedQueryClause
         Returns the selected query clause  
            
         
        """
        pass
    @property
    def SubType(self) -> str:
        """
        Getter for property: (str) SubType
         Returns the port sub type  
            
         
        """
        pass
    @SubType.setter
    def SubType(self, subType: str):
        """
        Setter for property: (str) SubType
         Returns the port sub type  
            
         
        """
        pass
    @property
    def Type(self) -> EditClauseBuilder.Types:
        """
        Getter for property: ( EditClauseBuilder.Types NXOp) Type
         Returns the type of object to be used for edit clause
                     NXOpen::AME::EditClauseBuilder::Type 
                  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: EditClauseBuilder.Types):
        """
        Setter for property: ( EditClauseBuilder.Types NXOp) Type
         Returns the type of object to be used for edit clause
                     NXOpen::AME::EditClauseBuilder::Type 
                  
            
         
        """
        pass
    @property
    def ValueCount(self) -> int:
        """
        Getter for property: (int) ValueCount
         Returns the value count  
            
         
        """
        pass
    @ValueCount.setter
    def ValueCount(self, valueCount: int):
        """
        Setter for property: (int) ValueCount
         Returns the value count  
            
         
        """
        pass
    def SetClassificationPropertyId(self, classificationPropertyID: int) -> None:
        """
         Set the classification property id 
        """
        pass
    def SetClassificationPropertyIdAt(self, index: int, classificationPropertyID: int) -> None:
        """
         Set the classification property id 
        """
        pass
    def SetProperty(self, index: int, propertyName: str) -> None:
        """
         Set the property
        """
        pass
    def SetPropertyOperator(self, index: int, propertyOperator: str) -> None:
        """
         Set the property operator
        """
        pass
    def SetPropertyValue(self, index: int, propertyValue: str) -> None:
        """
         Set the property value
        """
        pass
import NXOpen
import NXOpen.Diagramming
class EditDisplaySettingsBuilder(NXOpen.Builder): 
    """ Display settings builder for primitive geometry on page """
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineColorFontWidth
         Returns the line color font width settings of primitive geometry i.  
          e. line, circle and rectangle   
         
        """
        pass
    def SetElements(self, selectedNodes: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         The SelectedNodeTags 
        """
        pass
import NXOpen
class EditEngineeringObjectBuilder(NXOpen.Builder): 
    """ JA class for the Eng object dialog"""
    class SourceType(Enum):
        """
        Members Include: 
         |AssignEos| 
         |AssignPous| 

        """
        AssignEos: int
        AssignPous: int
        @staticmethod
        def ValueOf(value: int) -> EditEngineeringObjectBuilder.SourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EngObjDescription(self) -> str:
        """
        Getter for property: (str) EngObjDescription
         Returns the string description   
            
         
        """
        pass
    @EngObjDescription.setter
    def EngObjDescription(self, stringDescription: str):
        """
        Setter for property: (str) EngObjDescription
         Returns the string description   
            
         
        """
        pass
    @property
    def EngObjName(self) -> str:
        """
        Getter for property: (str) EngObjName
         Returns the string name   
            
         
        """
        pass
    @EngObjName.setter
    def EngObjName(self, stringName: str):
        """
        Setter for property: (str) EngObjName
         Returns the string name   
            
         
        """
        pass
    @property
    def ListAspectDetail(self) -> EngineeringObjectAspectDetailBuilder:
        """
        Getter for property: ( EngineeringObjectAspectDetailBuilder NXOp) ListAspectDetail
         Returns the aspect detail ui block  
            
         
        """
        pass
    @property
    def SelectedPlcBaseSymbols(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedPlcBaseSymbols
         Returns the selected plc symbols   
            
         
        """
        pass
    @property
    def SelectionParent(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectionParent
         Returns the selection where the object will be reassigned.  
             
         
        """
        pass
    def SetAspectStates(self, roots: List[NXOpen.NXObject], states: List[int]) -> None:
        """
        Pass Aspect States To Builder
        """
        pass
    def SetEngobjectsToEdit(self, engObject: List[AMEEngObject]) -> None:
        """
        Adds selected objects for Edit an aspect
        """
        pass
import NXOpen
class EditInEplanBuilder(NXOpen.Builder): 
    """ Represents a Edit in Eplan creation class Builder  """
    @property
    def SelectEplanMacro(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectEplanMacro
         Returns the selected engineering object   
            
         
        """
        pass
    @property
    def UpdateAllInstance(self) -> bool:
        """
        Getter for property: (bool) UpdateAllInstance
         Returns the flag to repesent update all instances of edited eplan macro   
            
         
        """
        pass
    @UpdateAllInstance.setter
    def UpdateAllInstance(self, updateAllInstance: bool):
        """
        Setter for property: (bool) UpdateAllInstance
         Returns the flag to repesent update all instances of edited eplan macro   
            
         
        """
        pass
    def AbortAction(self) -> None:
        """
         Abort Eplan Action 
        """
        pass
    def ReceiveEditedEplanMacro(self) -> None:
        """
         Receive Edited Eplan Macro 
        """
        pass
    def SetEditedMacroFilePath(self, macroFilePath: str) -> None:
        """
         Set Macro File Path 
        """
        pass
import NXOpen
class EditOrderBuilder(NXOpen.Builder): 
    """ JA class for the Edit Order dialog"""
    def UpdateOrder(self, ports: List[NXOpen.NXObject]) -> None:
        """
         Update the Order index of ports.
        """
        pass
import NXOpen
class ElectricalAnnotationSettingsBuilder(NXOpen.Builder): 
    """ JA class for the Electrical Annotation Settings dialog"""
    class AnnotationAttrType(Enum):
        """
        Members Include: 
         |SourceTarget| 
         |CrossSection| 
         |Color| 
         |WireType| 
         |ObjectName| 
         |CutLength| 
         |PotentialType| 

        """
        SourceTarget: int
        CrossSection: int
        Color: int
        WireType: int
        ObjectName: int
        CutLength: int
        PotentialType: int
        @staticmethod
        def ValueOf(value: int) -> ElectricalAnnotationSettingsBuilder.AnnotationAttrType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAnnotationAttributes(self, potentialType: AmeElectricalConnectionPotentialType) -> List[ElectricalAnnotationSettingsBuilder.AnnotationAttrType]:
        """
         The annotation attributes for a given connection type.
         Returns annotationAttrs ( ElectricalAnnotationSettingsBuilder.AnnotationAttrType List[NX):  User needs to free this memory.
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Reset to default. 
        """
        pass
    def SetAnnotationAttributes(self, potentialType: AmeElectricalConnectionPotentialType, annotationAttrs: List[ElectricalAnnotationSettingsBuilder.AnnotationAttrType]) -> None:
        """
         
        """
        pass
import NXOpen
class ElectricalConnectionSettingsBuilder(NXOpen.Builder): 
    """ Builder object for changing electrical connection settings on diagramming pages associated with the NXOpen.AME.Project. """
    @property
    def SelectedBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectedBaseDefinition
         Returns the selection base definition  
            
         
        """
        pass
    def GetDefaultConnectionProduct(self, potentialType: AmeElectricalConnectionPotentialType) -> ProductDefinition:
        """
         Get assigned connection product for provided connection subtype in Connection Project Settings
         Returns prodDef ( ProductDefinition NXOp): .
        """
        pass
    def GetStyleColorCode(self, potentialType: AmeElectricalConnectionPotentialType) -> NXOpen.NXColor:
        """
         Style color code property of a given electrical connection sub-type. 
         Returns styleColorCode ( NXOpen.NXColor): .
        """
        pass
    def GetStyleFont(self, potentialType: AmeElectricalConnectionPotentialType) -> NXOpen.DisplayableObject.ObjectFont:
        """
         Style font property of a given electrical connection sub-type. 
         Returns styleFont ( NXOpen.DisplayableObject.ObjectFont): .
        """
        pass
    def GetStyleWidth(self, potentialType: AmeElectricalConnectionPotentialType) -> NXOpen.DisplayableObject.ObjectWidth:
        """
         Style width property of a given electrical connection sub-type. 
         Returns styleWidth ( NXOpen.DisplayableObject.ObjectWidth): .
        """
        pass
    def GetWireColorCode(self, potentialType: AmeElectricalConnectionPotentialType) -> str:
        """
         Wire color code property of a given electrical connection sub-type. 
         Returns wireColorCode (str):  Caller needs to free this memory. .
        """
        pass
    def GetWireCrossSection(self, potentialType: AmeElectricalConnectionPotentialType) -> float:
        """
         Wire cross section property of a given electrical connection sub-type. 
         Returns wireCrossSection (float): .
        """
        pass
    def GetWireType(self, potentialType: AmeElectricalConnectionPotentialType) -> str:
        """
         Wire type property of a given electrical connection sub-type. 
         Returns wireType (str):  Caller needs to free this memory. .
        """
        pass
    def RemoveConnectionProductAssignment(self, potentialType: AmeElectricalConnectionPotentialType) -> None:
        """
         Remove the assigned product from provided connection subtype 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets electrical connection settings to default 
        """
        pass
    def SetDefaultConnectionProduct(self, potentialType: AmeElectricalConnectionPotentialType, prodDef: ProductDefinition) -> None:
        """
         Assign selected connection product 
        """
        pass
    def SetStyleColorCode(self, potentialType: AmeElectricalConnectionPotentialType, styleColorCode: NXOpen.NXColor) -> None:
        """
          
        """
        pass
    def SetStyleFont(self, potentialType: AmeElectricalConnectionPotentialType, styleFont: NXOpen.DisplayableObject.ObjectFont) -> None:
        """
          
        """
        pass
    def SetStyleWidth(self, potentialType: AmeElectricalConnectionPotentialType, styleWidth: NXOpen.DisplayableObject.ObjectWidth) -> None:
        """
          
        """
        pass
    def SetWireColorCode(self, potentialType: AmeElectricalConnectionPotentialType, wireColorCode: str) -> None:
        """
          
        """
        pass
    def SetWireCrossSection(self, potentialType: AmeElectricalConnectionPotentialType, wireCrossSection: float) -> None:
        """
          
        """
        pass
    def SetWireType(self, potentialType: AmeElectricalConnectionPotentialType, wireType: str) -> None:
        """
          
        """
        pass
    def ValidateMatchingRules(self, potentialTypeValue: str, propertyToValidate: str, prodDef: ProductDefinition) -> bool:
        """
         Validate matching rules for selected connection product 
         Returns isMatched (bool): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class EngineeringObjectAspectDetailBuilder(NXOpen.TaggedObject): 
    """
        JA class for the Engineering Object Aspect Detail UI block
    """
    class Columns(Enum):
        """
        Members Include: 
         |Type| 
         |Parent| 
         |Name| 

        """
        Type: int
        Parent: int
        Name: int
        @staticmethod
        def ValueOf(value: int) -> EngineeringObjectAspectDetailBuilder.Columns:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NameSource(Enum):
        """
        Members Include: 
         |Default| 
         |NamingRule| 
         |UserInput| 
         |Mapping| 

        """
        Default: int
        NamingRule: int
        UserInput: int
        Mapping: int
        @staticmethod
        def ValueOf(value: int) -> EngineeringObjectAspectDetailBuilder.NameSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SelectionParent(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectionParent
         Returns the selection parent   
            
         
        """
        pass
    def AddNameAspect(self, aspectType: str, nameAspect: str) -> None:
        """
        Adds a specific name for an aspect
        """
        pass
    def AssignParent(self, aspectName: str, aspectType: NXOpen.NXObject) -> None:
        """
        Sets a parent aspect
        """
        pass
    def GetParent(self, aspectType: str) -> NXOpen.NXObject:
        """
         The parent aspect 
         Returns aspectParent ( NXOpen.NXObject): .
        """
        pass
    def SetNameSource(self, aspectType: str, source: EngineeringObjectAspectDetailBuilder.NameSource) -> None:
        """
        Sets the source for aspect name
        """
        pass
    def UnassignParent(self, aspectType: str) -> None:
        """
        Deletes a parent aspect
        """
        pass
class EngineeringObjectBaseBuilder(MultipleObjectsBuilder): 
    """ JA class for the insert Eng object dialog"""
    pass
import NXOpen
import NXOpen.Tooling
class EngineeringObjectBuilder(EngineeringObjectBaseBuilder): 
    """ JA class for the insert Eng object dialog"""
    @property
    def CreatedEo(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) CreatedEo
         Returns the created eo  
            
         
        """
        pass
    @property
    def ProjectEngObject(self) -> ProjectEngineeringObjectBuilder:
        """
        Getter for property: ( ProjectEngineeringObjectBuilder NXOp) ProjectEngObject
         Returns the project eo ui block  
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the selection base definition builder  
            
         
        """
        pass
    @property
    def SelectionBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectionBaseDefinition
         Returns the selection base definition builder  
            
         
        """
        pass
import NXOpen
class EngineeringObjectDefinitionLabelBuilder(NXOpen.Builder): 
    """ JA class for the insert Engineering object definition label dialog"""
    @property
    def ToggleDescription(self) -> bool:
        """
        Getter for property: (bool) ToggleDescription
         Returns the toggle description   
            
         
        """
        pass
    @ToggleDescription.setter
    def ToggleDescription(self, toggleDescription: bool):
        """
        Setter for property: (bool) ToggleDescription
         Returns the toggle description   
            
         
        """
        pass
    @property
    def ToggleFunction(self) -> bool:
        """
        Getter for property: (bool) ToggleFunction
         Returns the toggle function   
            
         
        """
        pass
    @ToggleFunction.setter
    def ToggleFunction(self, toggleFunction: bool):
        """
        Setter for property: (bool) ToggleFunction
         Returns the toggle function   
            
         
        """
        pass
    @property
    def ToggleLocation(self) -> bool:
        """
        Getter for property: (bool) ToggleLocation
         Returns the toggle location   
            
         
        """
        pass
    @ToggleLocation.setter
    def ToggleLocation(self, toggleLocation: bool):
        """
        Setter for property: (bool) ToggleLocation
         Returns the toggle location   
            
         
        """
        pass
    @property
    def ToggleProduct(self) -> bool:
        """
        Getter for property: (bool) ToggleProduct
         Returns the toggle product   
            
         
        """
        pass
    @ToggleProduct.setter
    def ToggleProduct(self, toggleProduct: bool):
        """
        Setter for property: (bool) ToggleProduct
         Returns the toggle product   
            
         
        """
        pass
    @property
    def ToggleRDS(self) -> bool:
        """
        Getter for property: (bool) ToggleRDS
         Returns the toggle rds   
            
         
        """
        pass
    @ToggleRDS.setter
    def ToggleRDS(self, toggleRDS: bool):
        """
        Setter for property: (bool) ToggleRDS
         Returns the toggle rds   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class EngineeringObjectNameBuilder(NXOpen.TaggedObject): 
    """
        JA class for the Engineering Object and Engineering Object def name and description superclass UI block
    """
    @property
    def ObjectDescription(self) -> str:
        """
        Getter for property: (str) ObjectDescription
         Returns the eo def description   
            
         
        """
        pass
    @ObjectDescription.setter
    def ObjectDescription(self, objectDescription: str):
        """
        Setter for property: (str) ObjectDescription
         Returns the eo def description   
            
         
        """
        pass
    @property
    def ObjectName(self) -> str:
        """
        Getter for property: (str) ObjectName
         Returns the eo def name   
            
         
        """
        pass
    @ObjectName.setter
    def ObjectName(self, objectName: str):
        """
        Setter for property: (str) ObjectName
         Returns the eo def name   
            
         
        """
        pass
    def GenerateName(self, baseName: str) -> None:
        """
         Geneate a new unique name 
        """
        pass
class EngObjectDefinition(BaseDefinition): 
    """ JA class for the Engineering Object Definition object"""
    pass
class EOAttributeHolder(AttributeHolder): 
    """ EOAttributeHolder Atributes Holder Object """
    pass
import NXOpen
class EODataItemAttributeHolder(NXOpen.NXObject): 
    """ EODef Atributes Holder Object """
    def SetEoDataItem(self, eodef: NXOpen.NXObject) -> None:
        """
         Set EODataItem 
        """
        pass
import NXOpen
class EODefAttributeHolder(AttributeHolder): 
    """ EODef Atributes Holder Object """
    def SetEodef(self, eodef: NXOpen.NXObject) -> None:
        """
         Set EOdef 
        """
        pass
class EplanDataRoot(AMEBaseNode): 
    """ EplanData Root Node class """
    pass
class EplanFolderNode(AMEBaseNode): 
    """ Eplan Folder Node class """
    pass
class EplanFunctionTemplateNode(AMEBaseNode): 
    """ Eplan Value List Node class """
    pass
import NXOpen
class EplanImportProjectTemplateBuilder(NXOpen.Builder): 
    """ EplanImportProjectTemplateBuilder """
    @property
    def ProjectTemplateFilePath(self) -> str:
        """
        Getter for property: (str) ProjectTemplateFilePath
         Returns the project template file path  
            
         
        """
        pass
    @ProjectTemplateFilePath.setter
    def ProjectTemplateFilePath(self, filename: str):
        """
        Setter for property: (str) ProjectTemplateFilePath
         Returns the project template file path  
            
         
        """
        pass
    def ImportProjectTemplateFile(self) -> None:
        """
         Import eplan project template 
        """
        pass
    def ReadProjectTemplateSettings(self) -> None:
        """
         Read eplan project template settings 
        """
        pass
class EplanImportType(Enum):
    """
    Members Include: 
     |AddType| 
     |AddChildren| 
     |AddPort| 
     |AddPortAndType| 
     |AddConnection| 

    """
    AddType: int
    AddChildren: int
    AddPort: int
    AddPortAndType: int
    AddConnection: int
    @staticmethod
    def ValueOf(value: int) -> EplanImportType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class EPLANPlug(AMEExtendedObject): 
    """ Represents EPLANPlug """
    pass
class EplanProductNode(AMEBaseNode): 
    """ Eplan Product Node class """
    pass
import NXOpen
class EplanProjectGenerationBuilder(NXOpen.Builder): 
    """ the eplan project generation dialog builder """
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
         Returns the project name   
            
         
        """
        pass
    @ProjectName.setter
    def ProjectName(self, projectName: str):
        """
        Setter for property: (str) ProjectName
         Returns the project name   
            
         
        """
        pass
    @property
    def SelectedEplanMacros(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedEplanMacros
         Returns the selected aspect node   
            
         
        """
        pass
    @property
    def TargetPathFolderBrowser(self) -> str:
        """
        Getter for property: (str) TargetPathFolderBrowser
         Returns the generation target folder path   
            
         
        """
        pass
    @TargetPathFolderBrowser.setter
    def TargetPathFolderBrowser(self, filename: str):
        """
        Setter for property: (str) TargetPathFolderBrowser
         Returns the generation target folder path   
            
         
        """
        pass
    @property
    def ToggleOpenInEplan(self) -> bool:
        """
        Getter for property: (bool) ToggleOpenInEplan
         Returns the toggle whether to open EPLAN project after generation   
            
         
        """
        pass
    @ToggleOpenInEplan.setter
    def ToggleOpenInEplan(self, toggleOpenInEplan: bool):
        """
        Setter for property: (bool) ToggleOpenInEplan
         Returns the toggle whether to open EPLAN project after generation   
            
         
        """
        pass
    @property
    def ToggleOverwrite(self) -> bool:
        """
        Getter for property: (bool) ToggleOverwrite
         Returns the toggle whether to overwrite existing EPLAN project   
            
         
        """
        pass
    @ToggleOverwrite.setter
    def ToggleOverwrite(self, toggleOverwrite: bool):
        """
        Setter for property: (bool) ToggleOverwrite
         Returns the toggle whether to overwrite existing EPLAN project   
            
         
        """
        pass
    @property
    def ToggleOverwritePages(self) -> bool:
        """
        Getter for property: (bool) ToggleOverwritePages
         Returns the toggle whether to overwrite existing pages   
            
         
        """
        pass
    @ToggleOverwritePages.setter
    def ToggleOverwritePages(self, toggleOverwritePages: bool):
        """
        Setter for property: (bool) ToggleOverwritePages
         Returns the toggle whether to overwrite existing pages   
            
         
        """
        pass
    @property
    def ToggleSaveNameChanges(self) -> bool:
        """
        Getter for property: (bool) ToggleSaveNameChanges
         Returns the toggle whether to save the project name changes to EPLAN project settings   
            
         
        """
        pass
    @ToggleSaveNameChanges.setter
    def ToggleSaveNameChanges(self, toggleSaveNameChanges: bool):
        """
        Setter for property: (bool) ToggleSaveNameChanges
         Returns the toggle whether to save the project name changes to EPLAN project settings   
            
         
        """
        pass
    @property
    def ToggleSavePathChanges(self) -> bool:
        """
        Getter for property: (bool) ToggleSavePathChanges
         Returns the toggle whether to save the target path changes to EPLAN project settings   
            
         
        """
        pass
    @ToggleSavePathChanges.setter
    def ToggleSavePathChanges(self, toggleSavePathChanges: bool):
        """
        Setter for property: (bool) ToggleSavePathChanges
         Returns the toggle whether to save the target path changes to EPLAN project settings   
            
         
        """
        pass
    def GenerateEplanProject(self) -> None:
        """
          Generate EPLAN project 
        """
        pass
import NXOpen
class EPLANProjectSettings(NXOpen.NXObject): 
    """ Eplan project settings Node Journaling class """
    pass
import NXOpen
class EplanProjectTemplateAndStructureBuilder(NXOpen.Builder): 
    """ JA class for the Eplan project template dialog"""
    @property
    def StructureOrderDocumentTypeIndex(self) -> int:
        """
        Getter for property: (int) StructureOrderDocumentTypeIndex
         Returns the structure order index for document type   
            
         
        """
        pass
    @StructureOrderDocumentTypeIndex.setter
    def StructureOrderDocumentTypeIndex(self, structureOrderDocumentTypeState: int):
        """
        Setter for property: (int) StructureOrderDocumentTypeIndex
         Returns the structure order index for document type   
            
         
        """
        pass
    @property
    def StructureOrderFunctionIndex(self) -> int:
        """
        Getter for property: (int) StructureOrderFunctionIndex
         Returns the structure order index for function   
            
         
        """
        pass
    @StructureOrderFunctionIndex.setter
    def StructureOrderFunctionIndex(self, structureOrderFunctionState: int):
        """
        Setter for property: (int) StructureOrderFunctionIndex
         Returns the structure order index for function   
            
         
        """
        pass
    @property
    def StructureOrderFunctionalAssignmentIndex(self) -> int:
        """
        Getter for property: (int) StructureOrderFunctionalAssignmentIndex
         Returns the structure order index for functional assignment   
            
         
        """
        pass
    @StructureOrderFunctionalAssignmentIndex.setter
    def StructureOrderFunctionalAssignmentIndex(self, structureOrderFunctionalAssignmentState: int):
        """
        Setter for property: (int) StructureOrderFunctionalAssignmentIndex
         Returns the structure order index for functional assignment   
            
         
        """
        pass
    @property
    def StructureOrderInstallationSiteIndex(self) -> int:
        """
        Getter for property: (int) StructureOrderInstallationSiteIndex
         Returns the structure order index for installation site   
            
         
        """
        pass
    @StructureOrderInstallationSiteIndex.setter
    def StructureOrderInstallationSiteIndex(self, structureOrderInstallationSiteState: int):
        """
        Setter for property: (int) StructureOrderInstallationSiteIndex
         Returns the structure order index for installation site   
            
         
        """
        pass
    @property
    def StructureOrderLocationIndex(self) -> int:
        """
        Getter for property: (int) StructureOrderLocationIndex
         Returns the structure order index for location   
            
         
        """
        pass
    @StructureOrderLocationIndex.setter
    def StructureOrderLocationIndex(self, structureOrderLocationState: int):
        """
        Setter for property: (int) StructureOrderLocationIndex
         Returns the structure order index for location   
            
         
        """
        pass
    @property
    def StructureOrderUserDefinedStructureIndex(self) -> int:
        """
        Getter for property: (int) StructureOrderUserDefinedStructureIndex
         Returns the structure order index for user-defined structure   
            
         
        """
        pass
    @StructureOrderUserDefinedStructureIndex.setter
    def StructureOrderUserDefinedStructureIndex(self, structureOrderUserDefinedStructureState: int):
        """
        Setter for property: (int) StructureOrderUserDefinedStructureIndex
         Returns the structure order index for user-defined structure   
            
         
        """
        pass
class EplanPropertyNode(AMEBaseNode): 
    """ Eplan Property Node class """
    pass
class EplanPropertyType(Enum):
    """
    Members Include: 
     |FunctionalAssignment| 
     |HigherLevelFunction| 
     |InstallationSite| 
     |MountingLocation| 
     |DocumentType| 
     |UserDefinedStructure| 
     |Max| 

    """
    FunctionalAssignment: int
    HigherLevelFunction: int
    InstallationSite: int
    MountingLocation: int
    DocumentType: int
    UserDefinedStructure: int
    Max: int
    @staticmethod
    def ValueOf(value: int) -> EplanPropertyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class EplanSettingsBuilder(NXOpen.Builder): 
    """ EplanSettingsBuilder """
    @property
    def Commission(self) -> str:
        """
        Getter for property: (str) Commission
         Returns the commission   
            
         
        """
        pass
    @Commission.setter
    def Commission(self, commission: str):
        """
        Setter for property: (str) Commission
         Returns the commission   
            
         
        """
        pass
    @property
    def ControlVoltage(self) -> str:
        """
        Getter for property: (str) ControlVoltage
         Returns the control voltage   
            
         
        """
        pass
    @ControlVoltage.setter
    def ControlVoltage(self, controlVoltage: str):
        """
        Setter for property: (str) ControlVoltage
         Returns the control voltage   
            
         
        """
        pass
    @property
    def Customer(self) -> str:
        """
        Getter for property: (str) Customer
         Returns the customer   
            
         
        """
        pass
    @Customer.setter
    def Customer(self, customer: str):
        """
        Setter for property: (str) Customer
         Returns the customer   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id   
            
         
        """
        pass
    @Id.setter
    def Id(self, id: str):
        """
        Setter for property: (str) Id
         Returns the id   
            
         
        """
        pass
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
         Returns the location   
            
         
        """
        pass
    @Location.setter
    def Location(self, location: str):
        """
        Setter for property: (str) Location
         Returns the location   
            
         
        """
        pass
    @property
    def ManufacturingYear(self) -> str:
        """
        Getter for property: (str) ManufacturingYear
         Returns the manufacturing year   
            
         
        """
        pass
    @ManufacturingYear.setter
    def ManufacturingYear(self, manufacturingYear: str):
        """
        Setter for property: (str) ManufacturingYear
         Returns the manufacturing year   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def PowerInput(self) -> str:
        """
        Getter for property: (str) PowerInput
         Returns the power input   
            
         
        """
        pass
    @PowerInput.setter
    def PowerInput(self, powerInput: str):
        """
        Setter for property: (str) PowerInput
         Returns the power input   
            
         
        """
        pass
    @property
    def ProjectTargetPath(self) -> str:
        """
        Getter for property: (str) ProjectTargetPath
         Returns the generation path   
            
         
        """
        pass
    @ProjectTargetPath.setter
    def ProjectTargetPath(self, projectTargetPath: str):
        """
        Setter for property: (str) ProjectTargetPath
         Returns the generation path   
            
         
        """
        pass
    @property
    def ProjectTemplateFile(self) -> str:
        """
        Getter for property: (str) ProjectTemplateFile
         Returns the project template file   
            
         
        """
        pass
    @ProjectTemplateFile.setter
    def ProjectTemplateFile(self, filename: str):
        """
        Setter for property: (str) ProjectTemplateFile
         Returns the project template file   
            
         
        """
        pass
    def GetDetails(self) -> List[str]:
        """
         Returns the details 
         Returns details (List[str]): .
        """
        pass
    def ResetProjectTemplate(self) -> None:
        """
         Reset the eplan project template information 
        """
        pass
    def SetDetails(self, details: List[str]) -> None:
        """
         Sets the details 
        """
        pass
class EPLANSocket(AMEExtendedObject): 
    """ Represents EPLANSocket """
    pass
import NXOpen
class EplanStructureIdentifierOrderBuilder(NXOpen.Builder): 
    """Represents a Eplan Structure identifier order Builder """
    def GetDocumentTypeIdentifierOrder(self) -> List[str]:
        """
         The structure order index for document type 
         Returns rowStrings (List[str]): .
        """
        pass
    def GetFunctionIdentifierOrder(self) -> List[str]:
        """
         The structure order index for function 
         Returns rowStrings (List[str]): .
        """
        pass
    def GetFunctionalAssignmentIdentifierOrder(self) -> List[str]:
        """
         The structure order index for functional assignment 
         Returns rowStrings (List[str]): .
        """
        pass
    def GetInstallationSiteIdentifierOrder(self) -> List[str]:
        """
         The structure order index for installation site 
         Returns rowStrings (List[str]): .
        """
        pass
    def GetLocationIdentifierOrder(self) -> List[str]:
        """
         The structure order index for location 
         Returns rowStrings (List[str]): .
        """
        pass
    def GetUserDefinedStructureIdentifierOrder(self) -> List[str]:
        """
         The structure order index for user-defined structure 
         Returns rowStrings (List[str]): .
        """
        pass
    def SetDocumentTypeIdentifierOrder(self, rowStrings: List[str]) -> None:
        """
         The structure order index for document type 
        """
        pass
    def SetFunctionIdentifierOrder(self, rowStrings: List[str]) -> None:
        """
         The structure order index for function 
        """
        pass
    def SetFunctionalAssignmentIdentifierOrder(self, rowStrings: List[str]) -> None:
        """
         The structure order index for functional assignment 
        """
        pass
    def SetInstallationSiteIdentifierOrder(self, rowStrings: List[str]) -> None:
        """
         The structure order index for installation site 
        """
        pass
    def SetLocationIdentifierOrder(self, rowStrings: List[str]) -> None:
        """
         The structure order index for location 
        """
        pass
    def SetUserDefinedStructureIdentifierOrder(self, rowStrings: List[str]) -> None:
        """
         The structure order index for user-defined structure 
        """
        pass
    def UpdateStructureIdentifierOrder(self) -> None:
        """
         Update structure identifier order. 
        """
        pass
import NXOpen
class EplanStructureSettings(NXOpen.NXObject): 
    """ Eplan structure settings Journaling class """
    pass
class EplanValueListNode(AMEBaseNode): 
    """ Eplan Value List Node class """
    pass
import NXOpen
class EplanValueSetBuilder(NXOpen.Builder): 
    """ Represents a value set creation class Builder  """
    @property
    def SelectEplanMacro(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectEplanMacro
         Returns the selected engineering object   
            
         
        """
        pass
    @property
    def SelectedPlaceHolderName(self) -> str:
        """
        Getter for property: (str) SelectedPlaceHolderName
         Returns the placeholder name for selected value set name   
            
         
        """
        pass
    @SelectedPlaceHolderName.setter
    def SelectedPlaceHolderName(self, name: str):
        """
        Setter for property: (str) SelectedPlaceHolderName
         Returns the placeholder name for selected value set name   
            
         
        """
        pass
    @property
    def SelectedValueSetName(self) -> str:
        """
        Getter for property: (str) SelectedValueSetName
         Returns the selected value set name   
            
         
        """
        pass
    @SelectedValueSetName.setter
    def SelectedValueSetName(self, name: str):
        """
        Setter for property: (str) SelectedValueSetName
         Returns the selected value set name   
            
         
        """
        pass
class EplanVersionNode(AMEBaseNode): 
    """ Eplan Version Node class """
    pass
import NXOpen
class EvaluatorCopyToBuilder(NXOpen.Builder): 
    """ Copies evaluator and its dependents from one engineering object to another """
    @property
    def TargetObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) TargetObject
         Returns the selected target object to copy evaluator to   
            
         
        """
        pass
    def SetEvaluatorObjects(self, evaluatorObjects: List[ExpressionEvaluator]) -> None:
        """
         Selected evaluators that will be copied 
        """
        pass
    def SetExpressionObjects(self, evaluatorObjects: List[NXOpen.Expression]) -> None:
        """
         Expressions that will be copied 
        """
        pass
import NXOpen
class ExportCMCTopoProjectBuilder(NXOpen.Builder): 
    """ Export CMC topology into file"""
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the output file name   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the output file name   
            
         
        """
        pass
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
         Returns the output folder path to save CMC topology file  
            
         
        """
        pass
    @FolderPath.setter
    def FolderPath(self, folderPath: str):
        """
        Setter for property: (str) FolderPath
         Returns the output folder path to save CMC topology file  
            
         
        """
        pass
    @property
    def SelectStationNode(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectStationNode
         Returns the Station node selection   
            
         
        """
        pass
    @property
    def ToggleOverwriteExistingFile(self) -> bool:
        """
        Getter for property: (bool) ToggleOverwriteExistingFile
         Returns the toggle overwrite existing file   
            
         
        """
        pass
    @ToggleOverwriteExistingFile.setter
    def ToggleOverwriteExistingFile(self, toggleOverwriteExistingFile: bool):
        """
        Setter for property: (bool) ToggleOverwriteExistingFile
         Returns the toggle overwrite existing file   
            
         
        """
        pass
    def GenerateCMCProject(self) -> None:
        """
         Generate CMC Topo Project 
        """
        pass
import NXOpen
class ExportEClassMappingBuilder(NXOpen.Builder): 
    """ Export eclass mapping into file"""
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
         Returns the output folder path to save eclass mapping file  
            
         
        """
        pass
    @FolderPath.setter
    def FolderPath(self, folderPath: str):
        """
        Setter for property: (str) FolderPath
         Returns the output folder path to save eclass mapping file  
            
         
        """
        pass
    @property
    def SelectEClassNode(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectEClassNode
         Returns the EClass node selection   
            
         
        """
        pass
    def ValidateFolderPath(self) -> None:
        """
         Validate directory path for export eClass mapping
        """
        pass
import NXOpen
class ExportEplanMappingBuilder(NXOpen.Builder): 
    """ Export Eplan mapping into file"""
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
         Returns the output folder path to save Eplan mapping file  
            
         
        """
        pass
    @FolderPath.setter
    def FolderPath(self, folderPath: str):
        """
        Setter for property: (str) FolderPath
         Returns the output folder path to save Eplan mapping file  
            
         
        """
        pass
    @property
    def SelectEplanNode(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectEplanNode
         Returns the Eplan node selection   
            
         
        """
        pass
    def ValidateFolderPath(self) -> None:
        """
         Validate directory path for export Eplan mapping
        """
        pass
import NXOpen
class ExpressionEvaluator(NXOpen.NXObject): 
    """ Represents an Expression Evaluator """
    class RenderOptions(Enum):
        """
        Members Include: 
         |All| 
         |Cached| 
         |Evaluated| 
         |Failed| 
         |Unsupported| 

        """
        All: int
        Cached: int
        Evaluated: int
        Failed: int
        Unsupported: int
        @staticmethod
        def ValueOf(value: int) -> ExpressionEvaluator.RenderOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class ExternalObjectsTypeMappingBuilder(AMEBaseBuilder): 
    """ This builder class is used to update domain relevancy information on the external objects.
        This is also used to do the type mapping and filter the external objects by its source.
    """
    @property
    def ManageTypeMapping(self) -> ManageTypeMappingBuilder:
        """
        Getter for property: ( ManageTypeMappingBuilder NXOp) ManageTypeMapping
         Returns the builder for the manage type mapping   
            
         
        """
        pass
    @property
    def MappingSource(self) -> MappingSourceBuilder:
        """
        Getter for property: ( MappingSourceBuilder NXOp) MappingSource
         Returns the builder for the mapping source selection   
            
         
        """
        pass
    @property
    def SelectADType(self) -> SelectADTypeBuilder:
        """
        Getter for property: ( SelectADTypeBuilder NXOp) SelectADType
         Returns the builder for the selection of AD type item   
            
         
        """
        pass
    @property
    def SelectExternalObject(self) -> SelectExternalObjectBuilder:
        """
        Getter for property: ( SelectExternalObjectBuilder NXOp) SelectExternalObject
         Returns the builder for the selection of external type object   
            
         
        """
        pass
    @property
    def SelectSolutionTemplate(self) -> SelectSolutionTemplateBuilder:
        """
        Getter for property: ( SelectSolutionTemplateBuilder NXOp) SelectSolutionTemplate
         Returns the builder for the select solution template block  
            
         
        """
        pass
    @property
    def SpecifiedTemplateVariant(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) SpecifiedTemplateVariant
         Returns the specifed template variant  
            
         
        """
        pass
    @SpecifiedTemplateVariant.setter
    def SpecifiedTemplateVariant(self, specifiedTemplateVariant: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) SpecifiedTemplateVariant
         Returns the specifed template variant  
            
         
        """
        pass
    def MapToSelectedObject(self, components: List[NXOpen.NXObject]) -> None:
        """
         Add type mapping with an automation designer type for the list of external object types 
        """
        pass
import NXOpen
class ExtractAttributeAbsoluteBuilder(ExtractAttributeSourceObjectBuilder): 
    """ Create a extract attribute  """
    @property
    def Selection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Selection
         Returns the selection for the source object of reference property.  
             
         
        """
        pass
import NXOpen
class ExtractAttributeBaseBuilder(NXOpen.Builder): 
    """ Create a extract attribute  """
    @property
    def Context(self) -> str:
        """
        Getter for property: (str) Context
         Returns the object context  
            
         
        """
        pass
    @Context.setter
    def Context(self, context: str):
        """
        Setter for property: (str) Context
         Returns the object context  
            
         
        """
        pass
    @property
    def ContextObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ContextObject
         Returns the context object in source object to extract the attribute from    
            
         
        """
        pass
    @ContextObject.setter
    def ContextObject(self, contextObject: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) ContextObject
         Returns the context object in source object to extract the attribute from    
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the extracted attribute name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the extracted attribute name   
            
         
        """
        pass
    @property
    def SourceObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) SourceObject
         Returns the object to extract the attribute from   
            
         
        """
        pass
    @SourceObject.setter
    def SourceObject(self, selection: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) SourceObject
         Returns the object to extract the attribute from   
            
         
        """
        pass
import NXOpen
class ExtractAttributeBuilder(NXOpen.Builder): 
    """ Create a extract attribute  """
    class Type(Enum):
        """
        Members Include: 
         |CurrentObject| 
         |SelectObject| 
         |DetermineByExpression| 
         |Port| 
         |ExternalObject| 

        """
        CurrentObject: int
        SelectObject: int
        DetermineByExpression: int
        Port: int
        ExternalObject: int
        @staticmethod
        def ValueOf(value: int) -> ExtractAttributeBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AbsoluteAttributeBuilder(self) -> ExtractAttributeAbsoluteBuilder:
        """
        Getter for property: ( ExtractAttributeAbsoluteBuilder NXOp) AbsoluteAttributeBuilder
         Returns the absolute attribute builder   
            
         
        """
        pass
    @property
    def CurrentObjectAttributeBuilder(self) -> ExtractAttributeCurrentObjectBuilder:
        """
        Getter for property: ( ExtractAttributeCurrentObjectBuilder NXOp) CurrentObjectAttributeBuilder
         Returns the current object attribute builder   
            
         
        """
        pass
    @property
    def ExternalObjectAttributeBuilder(self) -> ExtractAttributeExternalObjectBuilder:
        """
        Getter for property: ( ExtractAttributeExternalObjectBuilder NXOp) ExternalObjectAttributeBuilder
         Returns the external object attribute builder   
            
         
        """
        pass
    @property
    def ExtractType(self) -> ExtractAttributeBuilder.Type:
        """
        Getter for property: ( ExtractAttributeBuilder.Type NXOp) ExtractType
         Returns the object type extraction  
            
         
        """
        pass
    @ExtractType.setter
    def ExtractType(self, type: ExtractAttributeBuilder.Type):
        """
        Setter for property: ( ExtractAttributeBuilder.Type NXOp) ExtractType
         Returns the object type extraction  
            
         
        """
        pass
    @property
    def PortAttributeBuilder(self) -> ExtractAttributePortBuilder:
        """
        Getter for property: ( ExtractAttributePortBuilder NXOp) PortAttributeBuilder
         Returns the port attribute builder   
            
         
        """
        pass
class ExtractAttributeCurrentObjectBuilder(ExtractAttributeSourceObjectBuilder): 
    """ Create a extract attribute  """
    pass
import NXOpen
class ExtractAttributeExternalObjectBuilder(ExtractAttributeBaseBuilder): 
    """ Creates a NXOpen.AME.ExtractAttribute object between an automation designer object and an external application object. """
    @property
    def SelectExternalObject(self) -> SelectExternalObjectBuilder:
        """
        Getter for property: ( SelectExternalObjectBuilder NXOp) SelectExternalObject
         Returns the external object block   
            
         
        """
        pass
    def GetCachedAttributeObject(self) -> NXOpen.TaggedObject:
        """
         Gets the cached attribute object for currently selected external object 
         Returns cachedObject ( NXOpen.TaggedObject): .
        """
        pass
class ExtractAttributePortBuilder(ExtractAttributeBaseBuilder): 
    """ Create a extract port attribute builder """
    pass
class ExtractAttributeSourceObjectBuilder(ExtractAttributeBaseBuilder): 
    """ Create a extract attribute  """
    class SourceType(Enum):
        """
        Members Include: 
         |SelectObject| 
         |MemoryArea| 
         |UserPorts| 
         |TypedPorts| 

        """
        SelectObject: int
        MemoryArea: int
        UserPorts: int
        TypedPorts: int
        @staticmethod
        def ValueOf(value: int) -> ExtractAttributeSourceObjectBuilder.SourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SourceObjectType(self) -> ExtractAttributeSourceObjectBuilder.SourceType:
        """
        Getter for property: ( ExtractAttributeSourceObjectBuilder.SourceType NXOp) SourceObjectType
         Returns the source object Type    
            
         
        """
        pass
    @SourceObjectType.setter
    def SourceObjectType(self, sourceObjectType: ExtractAttributeSourceObjectBuilder.SourceType):
        """
        Setter for property: ( ExtractAttributeSourceObjectBuilder.SourceType NXOp) SourceObjectType
         Returns the source object Type    
            
         
        """
        pass
class ExtractAttribute(AMEExtendedObject): 
    """ Extract Attribute Journaling class """
    pass
class FilterObjectsBuilder(AMEBaseBuilder): 
    """ Represents a FilterObjectsBuilder class Builder  """
    class SelectionMethod(Enum):
        """
        Members Include: 
         |Type| 
         |List| 

        """
        Type: int
        List: int
        @staticmethod
        def ValueOf(value: int) -> FilterObjectsBuilder.SelectionMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SelectClassification(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the selected classification   
            
         
        """
        pass
    def AddFilter(self, filterName: str) -> None:
        """
         Adds the given Filter to the Filter Combination 
        """
        pass
    def RemoveFilter(self, index: int) -> None:
        """
         Remove the given Filter from the Filter Combination 
        """
        pass
class FindByConditionEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates an object based on a property """
    @property
    def ConditionBlock(self) -> ConditionBlockBuilder:
        """
        Getter for property: ( ConditionBlockBuilder NXOp) ConditionBlock
         Returns the condition block   
            
         
        """
        pass
import NXOpen
class FluidicAnnotationSettingsBuilder(NXOpen.Builder): 
    """ JA class for the Fluidic Annotation Settings dialog"""
    class AnnotationAttrType(Enum):
        """
        Members Include: 
         |SourceTarget| 
         |ObjectName| 
         |Size| 
         |ColorCode| 
         |CutLength| 

        """
        SourceTarget: int
        ObjectName: int
        Size: int
        ColorCode: int
        CutLength: int
        @staticmethod
        def ValueOf(value: int) -> FluidicAnnotationSettingsBuilder.AnnotationAttrType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAnnotationAttributes(self, occupancyType: AmeFluidicConnectionOccupancyType) -> List[FluidicAnnotationSettingsBuilder.AnnotationAttrType]:
        """
         The annotation attributes for a given Occupancy type.
         Returns annotationAttrs ( FluidicAnnotationSettingsBuilder.AnnotationAttrType List[NX): .
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Reset to default. 
        """
        pass
    def SetAnnotationAttributes(self, occupancyType: AmeFluidicConnectionOccupancyType, annotationAttrs: List[FluidicAnnotationSettingsBuilder.AnnotationAttrType]) -> None:
        """
         The annotation attributes for a given Occupancy type.
        """
        pass
import NXOpen
class FluidicConnectionSettingsBuilder(NXOpen.Builder): 
    """ Builder object for changing fluidic connection settings on diagramming pages associated with the NXOpen.AME.Project. """
    @property
    def SelectedBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectedBaseDefinition
         Returns the selection base definition  
            
         
        """
        pass
    def GetDefaultConnectionProduct(self, occupancyType: AmeFluidicConnectionOccupancyType) -> ProductDefinition:
        """
         Get assigned connection product for provided connection subtype in Connection Project Settings
         Returns prodDef ( ProductDefinition NXOp): .
        """
        pass
    def GetPipeColorCode(self, occupancyType: AmeFluidicConnectionOccupancyType) -> str:
        """
         Color Code property of fluidic connection for the given occupancy type. 
         Returns pipeColorCode (str):  Caller needs to free this memory. .
        """
        pass
    def GetPipeSize(self, occupancyType: AmeFluidicConnectionOccupancyType) -> str:
        """
         Size property of fluidic connection for the given occupancy type. 
         Returns pipeSize (str):  Caller needs to free this memory. .
        """
        pass
    def GetStyleColor(self, occupancyType: AmeFluidicConnectionOccupancyType) -> NXOpen.NXColor:
        """
         Style Color property of fluidic connection for the given occupancy type. 
         Returns styleColor ( NXOpen.NXColor): .
        """
        pass
    def GetStyleFont(self, occupancyType: AmeFluidicConnectionOccupancyType) -> NXOpen.DisplayableObject.ObjectFont:
        """
         Style Font property of fluidic connection for the given occupancy type. 
         Returns styleFont ( NXOpen.DisplayableObject.ObjectFont): .
        """
        pass
    def GetStyleWidth(self, occupancyType: AmeFluidicConnectionOccupancyType) -> NXOpen.DisplayableObject.ObjectWidth:
        """
         Style Width property of fluidic connection for the given occupancy type. 
         Returns styleWidth ( NXOpen.DisplayableObject.ObjectWidth): .
        """
        pass
    def RemoveConnectionProductAssignment(self, occupancyType: AmeFluidicConnectionOccupancyType) -> None:
        """
         Remove the assigned product from provided connection subtype 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets fluidic connection settings to default 
        """
        pass
    def SetDefaultConnectionProduct(self, occupancyType: AmeFluidicConnectionOccupancyType, prodDef: ProductDefinition) -> None:
        """
         Assign selected connection product 
        """
        pass
    def SetPipeColorCode(self, occupancyType: AmeFluidicConnectionOccupancyType, pipeColorCode: str) -> None:
        """
          
        """
        pass
    def SetPipeSize(self, occupancyType: AmeFluidicConnectionOccupancyType, pipeSize: str) -> None:
        """
          
        """
        pass
    def SetStyleColor(self, occupancyType: AmeFluidicConnectionOccupancyType, styleColor: NXOpen.NXColor) -> None:
        """
          
        """
        pass
    def SetStyleFont(self, occupancyType: AmeFluidicConnectionOccupancyType, styleFont: NXOpen.DisplayableObject.ObjectFont) -> None:
        """
          
        """
        pass
    def SetStyleWidth(self, occupancyType: AmeFluidicConnectionOccupancyType, styleWidth: NXOpen.DisplayableObject.ObjectWidth) -> None:
        """
          
        """
        pass
    def ValidateMatchingRules(self, fluidOccupancy: str, propertyToValidate: str, prodDef: ProductDefinition) -> bool:
        """
         Validate matching rules for selected connection product 
         Returns isMatched (bool): .
        """
        pass
import NXOpen
class FormSheetBuilder(NXOpen.Builder): 
    """ JA class for the Form Sheet dialog"""
    class AnsiStandardMetricSize(Enum):
        """
        Members Include: 
         |A| 
         |B| 
         |C| 
         |D| 
         |E| 

        """
        A: int
        B: int
        C: int
        D: int
        E: int
        @staticmethod
        def ValueOf(value: int) -> FormSheetBuilder.AnsiStandardMetricSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SizeOption(Enum):
        """
        Members Include: 
         |Standard| 
         |Custom| 

        """
        Standard: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> FormSheetBuilder.SizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StandardMetricSize(Enum):
        """
        Members Include: 
         |A4landscape| 
         |A3landscape| 
         |A2landscape| 
         |A1landscape| 
         |A0landscape| 
         |A4portrait| 

        """
        A4landscape: int
        A3landscape: int
        A2landscape: int
        A1landscape: int
        A0landscape: int
        A4portrait: int
        @staticmethod
        def ValueOf(value: int) -> FormSheetBuilder.StandardMetricSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StandardTypes(Enum):
        """
        Members Include: 
         |Iec| 
         |Ansi| 

        """
        Iec: int
        Ansi: int
        @staticmethod
        def ValueOf(value: int) -> FormSheetBuilder.StandardTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnsiFormSheetStandardMetricSize(self) -> FormSheetBuilder.AnsiStandardMetricSize:
        """
        Getter for property: ( FormSheetBuilder.AnsiStandardMetricSize NXOp) AnsiFormSheetStandardMetricSize
         Returns the standard metric size of type  NXOpen::AME::FormSheetBuilder::AnsiFormSheetStandardMetricSize    
            
         
        """
        pass
    @AnsiFormSheetStandardMetricSize.setter
    def AnsiFormSheetStandardMetricSize(self, standardMetricSize: FormSheetBuilder.AnsiStandardMetricSize):
        """
        Setter for property: ( FormSheetBuilder.AnsiStandardMetricSize NXOp) AnsiFormSheetStandardMetricSize
         Returns the standard metric size of type  NXOpen::AME::FormSheetBuilder::AnsiFormSheetStandardMetricSize    
            
         
        """
        pass
    @property
    def BasicProperties(self) -> BasicPropertiesBuilder:
        """
        Getter for property: ( BasicPropertiesBuilder NXOp) BasicProperties
         Returns the name and description   
            
         
        """
        pass
    @property
    def FormSheetSizeOption(self) -> FormSheetBuilder.SizeOption:
        """
        Getter for property: ( FormSheetBuilder.SizeOption NXOp) FormSheetSizeOption
         Returns the size option type of type  NXOpen::AME::FormSheetBuilder::SizeOption    
            
         
        """
        pass
    @FormSheetSizeOption.setter
    def FormSheetSizeOption(self, sizeOption: FormSheetBuilder.SizeOption):
        """
        Setter for property: ( FormSheetBuilder.SizeOption NXOp) FormSheetSizeOption
         Returns the size option type of type  NXOpen::AME::FormSheetBuilder::SizeOption    
            
         
        """
        pass
    @property
    def FormSheetStandardMetricSize(self) -> FormSheetBuilder.StandardMetricSize:
        """
        Getter for property: ( FormSheetBuilder.StandardMetricSize NXOp) FormSheetStandardMetricSize
         Returns the standard metric size of type  NXOpen::AME::FormSheetBuilder::StandardMetricSize    
            
         
        """
        pass
    @FormSheetStandardMetricSize.setter
    def FormSheetStandardMetricSize(self, standardMetricSize: FormSheetBuilder.StandardMetricSize):
        """
        Setter for property: ( FormSheetBuilder.StandardMetricSize NXOp) FormSheetStandardMetricSize
         Returns the standard metric size of type  NXOpen::AME::FormSheetBuilder::StandardMetricSize    
            
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height   
            
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height   
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length   
            
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length   
            
         
        """
        pass
    @property
    def StandardType(self) -> FormSheetBuilder.StandardTypes:
        """
        Getter for property: ( FormSheetBuilder.StandardTypes NXOp) StandardType
         Returns the standard type   
            
         
        """
        pass
    @StandardType.setter
    def StandardType(self, actionType: FormSheetBuilder.StandardTypes):
        """
        Setter for property: ( FormSheetBuilder.StandardTypes NXOp) StandardType
         Returns the standard type   
            
         
        """
        pass
import NXOpen
class FormSheetObject(NXOpen.NXObject): 
    """ JA class for the FormSheetObject"""
    pass
import NXOpen
class FormSheetSettingsBuilder(NXOpen.Builder): 
    """ JA class for the Form Sheet Settings dialog"""
    class SymbolDrawingStandard(Enum):
        """
        Members Include: 
         |Iec| 
         |Ansi| 
         |NonStandard| 

        """
        Iec: int
        Ansi: int
        NonStandard: int
        @staticmethod
        def ValueOf(value: int) -> FormSheetSettingsBuilder.SymbolDrawingStandard:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DrawingStandard(self) -> FormSheetSettingsBuilder.SymbolDrawingStandard:
        """
        Getter for property: ( FormSheetSettingsBuilder.SymbolDrawingStandard NXOp) DrawingStandard
         Returns the representation type which could be of  NXOpen::AME::FormSheetSettingsBuilder::DrawingStandard    
            
         
        """
        pass
    @DrawingStandard.setter
    def DrawingStandard(self, drawingStandard: FormSheetSettingsBuilder.SymbolDrawingStandard):
        """
        Setter for property: ( FormSheetSettingsBuilder.SymbolDrawingStandard NXOp) DrawingStandard
         Returns the representation type which could be of  NXOpen::AME::FormSheetSettingsBuilder::DrawingStandard    
            
         
        """
        pass
    def AddFormSheetMapping(self, documentType: DocumentType, formSheetName: str) -> None:
        """
         Adds form sheet mapping with document type
        """
        pass
    def ResetFormSheetMapping(self, documentType: DocumentType) -> None:
        """
         Reset the form sheet mapping for a given document type. 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Reset the form sheet mapping for all document types. 
        """
        pass
import NXOpen
class FragmentAttributeHolder(NXOpen.NXObject): 
    """ Fragment Object Atributes Holder"""
    pass
import NXOpen
class FragmentBuilder(NXOpen.Builder): 
    """ Represents a Fragment creation class Builder  """
    @property
    def AspectDetailsBuilder(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) AspectDetailsBuilder
         Returns the fragment aspect details  
            
         
        """
        pass
    @property
    def FragmentAttributeHolder(self) -> FragmentAttributeHolder:
        """
        Getter for property: ( FragmentAttributeHolder NXOp) FragmentAttributeHolder
         Returns the attribute holder   
            
         
        """
        pass
    @property
    def FragmentDescription(self) -> str:
        """
        Getter for property: (str) FragmentDescription
         Returns the fragment description   
            
         
        """
        pass
    @FragmentDescription.setter
    def FragmentDescription(self, fragmentDescription: str):
        """
        Setter for property: (str) FragmentDescription
         Returns the fragment description   
            
         
        """
        pass
    @property
    def FragmentName(self) -> str:
        """
        Getter for property: (str) FragmentName
         Returns the fragment name   
            
         
        """
        pass
    @FragmentName.setter
    def FragmentName(self, fragmentName: str):
        """
        Setter for property: (str) FragmentName
         Returns the fragment name   
            
         
        """
        pass
    @property
    def Type(self) -> PageBuilder.Types:
        """
        Getter for property: ( PageBuilder.Types NXOp) Type
         Returns the fragment type   
            
         
        """
        pass
    @Type.setter
    def Type(self, fragmentType: PageBuilder.Types):
        """
        Setter for property: ( PageBuilder.Types NXOp) Type
         Returns the fragment type   
            
         
        """
        pass
class FragmentObject(PageObject): 
    """ Represents a Fragment Object """
    pass
import NXOpen
class GeneralAnnotationSettingsBuilder(NXOpen.Builder): 
    """ builder for the general annotation settings dialog"""
    class AnnotationSeparator(Enum):
        """
        Members Include: 
         |SemiColon| 
         |Comma| 
         |Multiline| 

        """
        SemiColon: int
        Comma: int
        Multiline: int
        @staticmethod
        def ValueOf(value: int) -> GeneralAnnotationSettingsBuilder.AnnotationSeparator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HorizontalTextPosition(Enum):
        """
        Members Include: 
         |Above| 
         |Below| 

        """
        Above: int
        Below: int
        @staticmethod
        def ValueOf(value: int) -> GeneralAnnotationSettingsBuilder.HorizontalTextPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SourceAndTargetSeparator(Enum):
        """
        Members Include: 
         |LessthanGreaterthan| 
         |SemiColon| 

        """
        LessthanGreaterthan: int
        SemiColon: int
        @staticmethod
        def ValueOf(value: int) -> GeneralAnnotationSettingsBuilder.SourceAndTargetSeparator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VerticalTextPosition(Enum):
        """
        Members Include: 
         |Left| 
         |Right| 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> GeneralAnnotationSettingsBuilder.VerticalTextPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnnotationSetSeparator(self) -> GeneralAnnotationSettingsBuilder.AnnotationSeparator:
        """
        Getter for property: ( GeneralAnnotationSettingsBuilder.AnnotationSeparator NXOp) AnnotationSetSeparator
         Returns the separator for annotation set   
            
         
        """
        pass
    @AnnotationSetSeparator.setter
    def AnnotationSetSeparator(self, type: GeneralAnnotationSettingsBuilder.AnnotationSeparator):
        """
        Setter for property: ( GeneralAnnotationSettingsBuilder.AnnotationSeparator NXOp) AnnotationSetSeparator
         Returns the separator for annotation set   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the text offset   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, textOffset: float):
        """
        Setter for property: (float) Offset
         Returns the text offset   
            
         
        """
        pass
    @property
    def SourceTargetSeparator(self) -> GeneralAnnotationSettingsBuilder.SourceAndTargetSeparator:
        """
        Getter for property: ( GeneralAnnotationSettingsBuilder.SourceAndTargetSeparator NXOp) SourceTargetSeparator
         Returns the separator between source and target   
            
         
        """
        pass
    @SourceTargetSeparator.setter
    def SourceTargetSeparator(self, type: GeneralAnnotationSettingsBuilder.SourceAndTargetSeparator):
        """
        Setter for property: ( GeneralAnnotationSettingsBuilder.SourceAndTargetSeparator NXOp) SourceTargetSeparator
         Returns the separator between source and target   
            
         
        """
        pass
    @property
    def TextCFW(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextCFW
         Returns the text color font width   
            
         
        """
        pass
    @property
    def TextHeight(self) -> float:
        """
        Getter for property: (float) TextHeight
         Returns the text height   
            
         
        """
        pass
    @TextHeight.setter
    def TextHeight(self, textHeight: float):
        """
        Setter for property: (float) TextHeight
         Returns the text height   
            
         
        """
        pass
    @property
    def TextPositionHorizontal(self) -> GeneralAnnotationSettingsBuilder.HorizontalTextPosition:
        """
        Getter for property: ( GeneralAnnotationSettingsBuilder.HorizontalTextPosition NXOp) TextPositionHorizontal
         Returns the horizontal text position   
            
         
        """
        pass
    @TextPositionHorizontal.setter
    def TextPositionHorizontal(self, type: GeneralAnnotationSettingsBuilder.HorizontalTextPosition):
        """
        Setter for property: ( GeneralAnnotationSettingsBuilder.HorizontalTextPosition NXOp) TextPositionHorizontal
         Returns the horizontal text position   
            
         
        """
        pass
    @property
    def TextPositionVertical(self) -> GeneralAnnotationSettingsBuilder.VerticalTextPosition:
        """
        Getter for property: ( GeneralAnnotationSettingsBuilder.VerticalTextPosition NXOp) TextPositionVertical
         Returns the vertical text position   
            
         
        """
        pass
    @TextPositionVertical.setter
    def TextPositionVertical(self, type: GeneralAnnotationSettingsBuilder.VerticalTextPosition):
        """
        Setter for property: ( GeneralAnnotationSettingsBuilder.VerticalTextPosition NXOp) TextPositionVertical
         Returns the vertical text position   
            
         
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Set the default values 
        """
        pass
import NXOpen
class GeneralConnectionSettingsBuilder(NXOpen.Builder): 
    """ Builder for the General Connection Settings dialog """
    @property
    def AutoConnection(self) -> bool:
        """
        Getter for property: (bool) AutoConnection
         Returns the setting for Auto-Connection between symbols   
            
         
        """
        pass
    @AutoConnection.setter
    def AutoConnection(self, autoConnection: bool):
        """
        Setter for property: (bool) AutoConnection
         Returns the setting for Auto-Connection between symbols   
            
         
        """
        pass
    @property
    def EnablePointWiring(self) -> bool:
        """
        Getter for property: (bool) EnablePointWiring
         Returns the point wiring setting   
            
         
        """
        pass
    @EnablePointWiring.setter
    def EnablePointWiring(self, pointWiring: bool):
        """
        Setter for property: (bool) EnablePointWiring
         Returns the point wiring setting   
            
         
        """
        pass
    @property
    def JunctionRepresentationStyle(self) -> AmeJunctionRepresentationStyleType:
        """
        Getter for property: ( AmeJunctionRepresentationStyleType NXOp) JunctionRepresentationStyle
         Returns the representation style for TeeJunction   
            
         
        """
        pass
    @JunctionRepresentationStyle.setter
    def JunctionRepresentationStyle(self, junctionRepresentationStyle: AmeJunctionRepresentationStyleType):
        """
        Setter for property: ( AmeJunctionRepresentationStyleType NXOp) JunctionRepresentationStyle
         Returns the representation style for TeeJunction   
            
         
        """
        pass
    @property
    def KeepConnectionOnMove(self) -> bool:
        """
        Getter for property: (bool) KeepConnectionOnMove
         Returns the setting for keep connection on moving the symbols   
            
         
        """
        pass
    @KeepConnectionOnMove.setter
    def KeepConnectionOnMove(self, keepConnection: bool):
        """
        Setter for property: (bool) KeepConnectionOnMove
         Returns the setting for keep connection on moving the symbols   
            
         
        """
        pass
    @property
    def MinimalSegmentLength(self) -> float:
        """
        Getter for property: (float) MinimalSegmentLength
         Returns the minimal segment length setting   
            
         
        """
        pass
    @MinimalSegmentLength.setter
    def MinimalSegmentLength(self, segmentLength: float):
        """
        Setter for property: (float) MinimalSegmentLength
         Returns the minimal segment length setting   
            
         
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets general connection settings to default 
        """
        pass
import NXOpen
import NXOpen.Tooling
class GeneralNamingRuleBuilder(NXOpen.Builder): 
    """ Assign general naming rule set"""
    @property
    def ApplyAspectNamingRule(self) -> bool:
        """
        Getter for property: (bool) ApplyAspectNamingRule
         Returns the option to automatically rename its aspect names to mechanicallayout name upon mapping   
            
         
        """
        pass
    @ApplyAspectNamingRule.setter
    def ApplyAspectNamingRule(self, aspectNamingRule: bool):
        """
        Setter for property: (bool) ApplyAspectNamingRule
         Returns the option to automatically rename its aspect names to mechanicallayout name upon mapping   
            
         
        """
        pass
    @property
    def ExternalObjectsOnMapping(self) -> bool:
        """
        Getter for property: (bool) ExternalObjectsOnMapping
         Returns the option to automatically rename AD object and its aspect names to mechanicallayout name upon mapping   
            
         
        """
        pass
    @ExternalObjectsOnMapping.setter
    def ExternalObjectsOnMapping(self, externalObjectsOnMapping: bool):
        """
        Setter for property: (bool) ExternalObjectsOnMapping
         Returns the option to automatically rename AD object and its aspect names to mechanicallayout name upon mapping   
            
         
        """
        pass
    @property
    def SelectedItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedItem
         Returns the library UDT selection  
            
         
        """
        pass
import NXOpen
class GenerateReportsBuilder(NXOpen.Builder): 
    """ Comment"""
    @property
    def GenerateToProjectToggle(self) -> bool:
        """
        Getter for property: (bool) GenerateToProjectToggle
         Returns the generate to project toggle   
            
         
        """
        pass
    @GenerateToProjectToggle.setter
    def GenerateToProjectToggle(self, generateToProjectToggle: bool):
        """
        Setter for property: (bool) GenerateToProjectToggle
         Returns the generate to project toggle   
            
         
        """
        pass
    @property
    def GenerateToSystemToggle(self) -> bool:
        """
        Getter for property: (bool) GenerateToSystemToggle
         Returns the generate to system toggle   
            
         
        """
        pass
    @GenerateToSystemToggle.setter
    def GenerateToSystemToggle(self, generateToSystemToggle: bool):
        """
        Setter for property: (bool) GenerateToSystemToggle
         Returns the generate to system toggle   
            
         
        """
        pass
    @property
    def NativeFolderBrowser(self) -> str:
        """
        Getter for property: (str) NativeFolderBrowser
         Returns the native folder browser   
            
         
        """
        pass
    @NativeFolderBrowser.setter
    def NativeFolderBrowser(self, foldername: str):
        """
        Setter for property: (str) NativeFolderBrowser
         Returns the native folder browser   
            
         
        """
        pass
    def UpdateReportRuleStatus(self, ruleTag: int, status: bool) -> None:
        """
         The function updates the report rule status 
        """
        pass
import NXOpen
class GlobalSelectionBuilder(NXOpen.Builder): 
    """ GlobalSelectionBuilder """
    @property
    def Selection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Selection
         Returns the selected objects   
            
         
        """
        pass
import NXOpen
class GroupBuilder(NXOpen.Builder): 
    """ JA class for groups"""
    @property
    def NameDescription(self) -> ObjectNameBuilder:
        """
        Getter for property: ( ObjectNameBuilder NXOp) NameDescription
         Returns the eo name and description ui block  
            
         
        """
        pass
    @property
    def SelectFolder(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectFolder
         Returns the select folder   
            
         
        """
        pass
    @property
    def SelectObject(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectObject
         Returns the select object   
            
         
        """
        pass
class GroupRoot(AMEBaseNode): 
    """ Group Root Node Journaling class """
    pass
class Height(Enum):
    """
    Members Include: 
     |Two|  Height = 2    
     |Twopointfive|  Height = 2.5  
     |Threepointfive|  Height = 3.5  
     |Five|  Height = 5    
     |Seven|  Height = 7    
     |Ten|  Height = 10   
     |Forteen|  Height = 14   
     |Twenty|  Height = 20   
     |Seventy|  Height = 70   
     |Hundred|  Height = 100  
     |Onehundredforty|  Height = 140  
     |Twohundred|  Height = 200  
     |Twohundredfifty|  Height = 250  

    """
    Two: int
    Twopointfive: int
    Threepointfive: int
    Five: int
    Seven: int
    Ten: int
    Forteen: int
    Twenty: int
    Seventy: int
    Hundred: int
    Onehundredforty: int
    Twohundred: int
    Twohundredfifty: int
    @staticmethod
    def ValueOf(value: int) -> Height:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class IEngObject(IPortsContainer): 
    """ Represents Engineering Object """
    @abstractmethod
    def GetAspects(self) -> List[AspectNode]:
        """
         Get the Engineering Object aspects
         Returns aspects ( AspectNode List[NX): .
        """
        pass
    @abstractmethod
    def GetEngObjectPart(self) -> NXOpen.Part:
        """
         Returns part file of AME.IEngObject 
         Returns part ( NXOpen.Part): .
        """
        pass
    @abstractmethod
    def GetSymbolPlacements(self, pageType: PageBuilder.Types) -> Tuple[List[str], List[PageObject]]:
        """
         Returns the pages on which AME.IEngObject is placed 
         Returns A tuple consisting of (pageFullPageNames, pageObjects). 
         - pageFullPageNames is: List[str].
         - pageObjects is:  PageObject List[NX.

        """
        pass
import NXOpen
class ImportBMECatSchemaBuilder(NXOpen.Builder): 
    """ Imports a eclass schema xml file"""
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    def ValidateAndPopulateSchemaData(self) -> None:
        """
         Validate the xml file which is being imported and populate required data
        """
        pass
import NXOpen
class ImportEClassMappingBuilder(NXOpen.Builder): 
    """ Import eClass mapping"""
    @property
    def EclassVersion(self) -> str:
        """
        Getter for property: (str) EclassVersion
         Returns the eClass version  
            
         
        """
        pass
    @EclassVersion.setter
    def EclassVersion(self, eclassVersion: str):
        """
        Setter for property: (str) EclassVersion
         Returns the eClass version  
            
         
        """
        pass
    @property
    def FilePath(self) -> str:
        """
        Getter for property: (str) FilePath
         Returns the eClass mapping file  
            
         
        """
        pass
    @FilePath.setter
    def FilePath(self, filePath: str):
        """
        Setter for property: (str) FilePath
         Returns the eClass mapping file  
            
         
        """
        pass
    @property
    def ImportMappingType(self) -> ImportMappingType:
        """
        Getter for property: ( ImportMappingType NXOp) ImportMappingType
         Returns the enum for import mapping type  
            
         
        """
        pass
    @ImportMappingType.setter
    def ImportMappingType(self, importMappingType: ImportMappingType):
        """
        Setter for property: ( ImportMappingType NXOp) ImportMappingType
         Returns the enum for import mapping type  
            
         
        """
        pass
    @property
    def ImportMode(self) -> ImportEclassMappingMode:
        """
        Getter for property: ( ImportEclassMappingMode NXOp) ImportMode
         Returns the enum for import eClass mapping mode  
            
         
        """
        pass
    @ImportMode.setter
    def ImportMode(self, importEClassMappingMode: ImportEclassMappingMode):
        """
        Setter for property: ( ImportEclassMappingMode NXOp) ImportMode
         Returns the enum for import eClass mapping mode  
            
         
        """
        pass
    def ValidateFilePath(self) -> None:
        """
         Validate import eClass xml file path
        """
        pass
    def ValidateXmlFormat(self) -> None:
        """
         Validate import eClass xml format
        """
        pass
class ImportEclassMappingMode(Enum):
    """
    Members Include: 
     |Override| 
     |DontOverride| 

    """
    Override: int
    DontOverride: int
    @staticmethod
    def ValueOf(value: int) -> ImportEclassMappingMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ImportEClassProductBuilder(NXOpen.Builder): 
    """ Imports a eclass product xml file"""
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    def ValidateEClassProductXmlData(self) -> None:
        """
         Validate the eClass Product xml import data. This should be called prior to commit. 
        """
        pass
import NXOpen
class ImportEClassProductListBuilder(NXOpen.Builder): 
    """ Represents the Import eclass product list class Builder """
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    def PopulateExistingProductsVector(self) -> None:
        """
         Populate the Existing Products vector. 
        """
        pass
    def SetRowSelected(self, index: int) -> None:
        """
         Sets the eClass product row as selected. 
        """
        pass
    def ValidateEClassProductXmlData(self) -> None:
        """
         Validate the eClass Product xml import data. This should be called prior to commit. 
        """
        pass
import NXOpen
class ImportEClassSchemaBuilder(NXOpen.Builder): 
    """ Imports a eclass schema xml file"""
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    def ValidateAndPopulateSchemaData(self) -> None:
        """
         Validate the xml file which is being imported and populate required data
        """
        pass
import NXOpen
class ImportEplanMappingBuilder(NXOpen.Builder): 
    """ Import eplan mapping"""
    @property
    def FilePath(self) -> str:
        """
        Getter for property: (str) FilePath
         Returns the eplan mapping file  
            
         
        """
        pass
    @FilePath.setter
    def FilePath(self, filePath: str):
        """
        Setter for property: (str) FilePath
         Returns the eplan mapping file  
            
         
        """
        pass
    @property
    def ImportMode(self) -> ImportEplanMappingMode:
        """
        Getter for property: ( ImportEplanMappingMode NXOp) ImportMode
         Returns the enum for import eplan mapping mode  
            
         
        """
        pass
    @ImportMode.setter
    def ImportMode(self, importEplanMappingMode: ImportEplanMappingMode):
        """
        Setter for property: ( ImportEplanMappingMode NXOp) ImportMode
         Returns the enum for import eplan mapping mode  
            
         
        """
        pass
    def ValidateFilePath(self) -> None:
        """
         Validate import eplan xml file path
        """
        pass
    def ValidateXmlFormat(self) -> None:
        """
         Validate import eplan xml format
        """
        pass
class ImportEplanMappingMode(Enum):
    """
    Members Include: 
     |Override| 
     |DontOverride| 

    """
    Override: int
    DontOverride: int
    @staticmethod
    def ValueOf(value: int) -> ImportEplanMappingMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ImportEplanPageMacroBuilder(NXOpen.Builder): 
    """ ImportEplanPageMacroBuilder """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description   
            
         
        """
        pass
    @property
    def MacroFile(self) -> str:
        """
        Getter for property: (str) MacroFile
         Returns the eplan page macro template file   
            
         
        """
        pass
    @MacroFile.setter
    def MacroFile(self, macroFile: str):
        """
        Setter for property: (str) MacroFile
         Returns the eplan page macro template file   
            
         
        """
        pass
    @property
    def MacroType(self) -> int:
        """
        Getter for property: (int) MacroType
         Returns the macro type   
            
         
        """
        pass
    @MacroType.setter
    def MacroType(self, macroType: int):
        """
        Setter for property: (int) MacroType
         Returns the macro type   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def SelectedAspectNode(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedAspectNode
         Returns the selected engineering object   
            
         
        """
        pass
    def ImportMacro(self, segmentsOfResponseMessage: List[str]) -> None:
        """
         Imports an eplan page macro 
        """
        pass
    def ReadMacroInformation(self) -> None:
        """
         Read device properties 
        """
        pass
import NXOpen
class ImportEplanProductBuilder(NXOpen.Builder): 
    """ Imports a eplan product xml file"""
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    def ValidateEplanProductXmlData(self) -> None:
        """
         Validate the Eplan Product xml import data. This should be called prior to commit. 
        """
        pass
import NXOpen
class ImportEplanProductListBuilder(NXOpen.Builder): 
    """ Represents the Import eplan product list class Builder """
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    def PopulateExistingProductsVector(self) -> None:
        """
         Populate the Existing Products vector. 
        """
        pass
    def SetRowSelected(self, index: int) -> None:
        """
         Sets the eClass product row as selected. 
        """
        pass
    def ValidateEplanProductXmlData(self) -> None:
        """
         Validate the eClass Product xml import data. This should be called prior to commit. 
        """
        pass
import NXOpen
class ImportGlobalMappingBuilder(NXOpen.Builder): 
    """ Imports a global mapping xml file"""
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the xml file which is being imported   
            
         
        """
        pass
import NXOpen
class ImportHWXmlBuilder(NXOpen.Builder): 
    """ the Import HW Xml builder """
    @property
    def CurrentlySelectedSWBlockItemName(self) -> str:
        """
        Getter for property: (str) CurrentlySelectedSWBlockItemName
         Returns the currently selected TIA software block item name   
            
         
        """
        pass
    @CurrentlySelectedSWBlockItemName.setter
    def CurrentlySelectedSWBlockItemName(self, swBlockName: str):
        """
        Setter for property: (str) CurrentlySelectedSWBlockItemName
         Returns the currently selected TIA software block item name   
            
         
        """
        pass
    @property
    def CurrentlySelectedStationItemName(self) -> str:
        """
        Getter for property: (str) CurrentlySelectedStationItemName
         Returns the currently selected TIA station item name   
            
         
        """
        pass
    @CurrentlySelectedStationItemName.setter
    def CurrentlySelectedStationItemName(self, stationName: str):
        """
        Setter for property: (str) CurrentlySelectedStationItemName
         Returns the currently selected TIA station item name   
            
         
        """
        pass
    @property
    def CurrentlySelectedTiaLibraryName(self) -> str:
        """
        Getter for property: (str) CurrentlySelectedTiaLibraryName
         Returns the currently selected TIA library item name   
            
         
        """
        pass
    @CurrentlySelectedTiaLibraryName.setter
    def CurrentlySelectedTiaLibraryName(self, libraryName: str):
        """
        Setter for property: (str) CurrentlySelectedTiaLibraryName
         Returns the currently selected TIA library item name   
            
         
        """
        pass
    @property
    def CurrentlySelectedTiaLibraryPath(self) -> str:
        """
        Getter for property: (str) CurrentlySelectedTiaLibraryPath
         Returns the currently selected TIA library item path   
            
         
        """
        pass
    @CurrentlySelectedTiaLibraryPath.setter
    def CurrentlySelectedTiaLibraryPath(self, libraryPath: str):
        """
        Setter for property: (str) CurrentlySelectedTiaLibraryPath
         Returns the currently selected TIA library item path   
            
         
        """
        pass
    @property
    def CurrentlySelectedTiaProjectName(self) -> str:
        """
        Getter for property: (str) CurrentlySelectedTiaProjectName
         Returns the currently selected TIA project item name   
            
         
        """
        pass
    @CurrentlySelectedTiaProjectName.setter
    def CurrentlySelectedTiaProjectName(self, projectName: str):
        """
        Setter for property: (str) CurrentlySelectedTiaProjectName
         Returns the currently selected TIA project item name   
            
         
        """
        pass
    @property
    def CurrentlySelectedTiaProjectPath(self) -> str:
        """
        Getter for property: (str) CurrentlySelectedTiaProjectPath
         Returns the currently selected TIA project item path   
            
         
        """
        pass
    @CurrentlySelectedTiaProjectPath.setter
    def CurrentlySelectedTiaProjectPath(self, projectPath: str):
        """
        Setter for property: (str) CurrentlySelectedTiaProjectPath
         Returns the currently selected TIA project item path   
            
         
        """
        pass
    @property
    def SelectLibraryObject(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectLibraryObject
         Returns the engineering object definition or product definition  
            
         
        """
        pass
    @property
    def SelectionTarget(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectionTarget
         Returns the selected engineering object   
            
         
        """
        pass
    def GetLibraryPreview(self) -> None:
        """
         Get library preview 
        """
        pass
    def GetStationList(self) -> None:
        """
         Import Tia project with option get station list 
        """
        pass
    def GetStationPreview(self, stationName: str) -> None:
        """
         Import Tia project with option get station preview 
        """
        pass
    def GetSystemLibrary(self) -> None:
        """
         Get System library 
        """
        pass
    def GetSystemLibraryList(self) -> List[str]:
        """
         Get library list 
         Returns systemLibraryList (List[str]): .
        """
        pass
    def ImportHwLibraryMasterCopies(self, masterCopyIds: List[str]) -> None:
        """
         Import master copy from hardware library 
        """
        pass
    def ImportPlcStations(self, stationNames: List[str]) -> List[AMEBaseNode]:
        """
         Import plc station 
         Returns stations ( AMEBaseNode List[NX): .
        """
        pass
    def ImportStation(self, stationId: str) -> AMEBaseNode:
        """
         Import station 
         Returns station ( AMEBaseNode NXOp): .
        """
        pass
    def ImportSwBlocks(self, swBlockIds: List[str], isOnline: bool) -> None:
        """
         Import sw blocks 
        """
        pass
    def ImportSwLibraryTypes(self, swTypeIds: List[str]) -> None:
        """
         Import sw blocks and UDTs from TIA library 
        """
        pass
    def ImportSwSystemLibraryMasterCopies(self, masterCopyIds: List[str], importFolderAsMasterCopy: bool) -> None:
        """
         Import master copy from System library 
        """
        pass
    def ReimportSingleSwBlock(self, nameOfMainBlockToImport: str, namesOfSubBlocksToImport: List[str], blockToUpdate: PlcBlock, isOnline: bool) -> None:
        """
         Reimport a single sw block 
        """
        pass
    def ReimportSingleSwLibraryType(self, swTypeId: str, swTypeVersionId: str, blockToUpdate: PlcBlock) -> None:
        """
         Reimport a single sw block from a TIA Portal Global Library 
        """
        pass
    def SetProjectXml(self, projectXmlParts: List[str]) -> None:
        """
         Set project xml 
        """
        pass
    def SetTiaPortalVersion(self, tiaPortalVersion: str) -> None:
        """
         The Tia Portal Version 
        """
        pass
class ImportMappingType(Enum):
    """
    Members Include: 
     |Eclass| 
     |Bmecat| 

    """
    Eclass: int
    Bmecat: int
    @staticmethod
    def ValueOf(value: int) -> ImportMappingType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ImportNode(AMEBaseNode): 
    """ Import Object Journaling class """
    pass
class ImportObject(AMEBaseNode): 
    """ Import Object Journaling class """
    def GetMappedEO(self) -> AMEEngObject:
        """
         Returns the mapped eng object NXOpen.AME.AMEEngObject of import object
         Returns engObject ( AMEEngObject NXOp): .
        """
        pass
class ImportType(Enum):
    """
    Members Include: 
     |AddType| 
     |AddFunction| 
     |AddChildren| 

    """
    AddType: int
    AddFunction: int
    AddChildren: int
    @staticmethod
    def ValueOf(value: int) -> ImportType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class INodeObject(NXOpen.Object): 
    """ Represents INode Object """
    @abstractmethod
    def GetChildren(self) -> List[INodeObject]:
        """
         Returns children of object 
         Returns children ( INodeObject List[NX): .
        """
        pass
    @abstractmethod
    def GetChildrenByNavigatorOrder(self) -> List[INodeObject]:
        """
         Returns children of object sorted by navigator order 
         Returns children ( INodeObject List[NX): .
        """
        pass
    @abstractmethod
    def GetName(self) -> str:
        """
         Get the Name 
         Returns name (str): .
        """
        pass
    @abstractmethod
    def GetParent(self) -> INodeObject:
        """
         Get the Parent Node 
         Returns parentNode ( INodeObject NXOp): .
        """
        pass
import NXOpen
class InsertObjectBuilder(MultipleObjectsBuilder): 
    """ JA class for Insert Object dialog"""
    @property
    def BaseDefAttributeHolder(self) -> BaseDefinitionAttributeHolder:
        """
        Getter for property: ( BaseDefinitionAttributeHolder NXOp) BaseDefAttributeHolder
         Returns the base definition attribute holder   
            
         
        """
        pass
    @property
    def InsertSettings(self) -> InsertSettingsBuilder:
        """
        Getter for property: ( InsertSettingsBuilder NXOp) InsertSettings
         Returns the aspect placement toggle setting   
            
         
        """
        pass
    @property
    def NameIndex(self) -> ObjectNameIndexBuilder:
        """
        Getter for property: ( ObjectNameIndexBuilder NXOp) NameIndex
         Returns the name, index and description  
            
         
        """
        pass
    @property
    def SelectedBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectedBaseDefinition
         Returns the selection base definition  
            
         
        """
        pass
    @property
    def SelectionParent(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionParent
         Returns the selected parents where the object will be assigned.  
             
         
        """
        pass
    def SetDefaultsOnBaseDefinitionAttributeHolder(self) -> None:
        """
         Set default properties on base def attr holder
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class InsertSettingsBuilder(NXOpen.TaggedObject): 
    """ Re-usable UI for Settings properties in Insert EO and Insert Template dialog """
    @property
    def AspectPlacement(self) -> bool:
        """
        Getter for property: (bool) AspectPlacement
         Returns the aspect placement   
            
         
        """
        pass
    @AspectPlacement.setter
    def AspectPlacement(self, aspectPlacement: bool):
        """
        Setter for property: (bool) AspectPlacement
         Returns the aspect placement   
            
         
        """
        pass
    @property
    def CopiesPerParent(self) -> int:
        """
        Getter for property: (int) CopiesPerParent
         Returns the number of copies to insert per parent   
            
         
        """
        pass
    @CopiesPerParent.setter
    def CopiesPerParent(self, copiesPerParent: int):
        """
        Setter for property: (int) CopiesPerParent
         Returns the number of copies to insert per parent   
            
         
        """
        pass
import NXOpen
class InspectSnapshotBuilder(NXOpen.Builder): 
    """ Inspects snapshot for AD project"""
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
         Returns the project name for which we want to inspect snapshot  
            
         
        """
        pass
    @ProjectName.setter
    def ProjectName(self, projectName: str):
        """
        Setter for property: (str) ProjectName
         Returns the project name for which we want to inspect snapshot  
            
         
        """
        pass
    @property
    def SelectedSnapshotId(self) -> str:
        """
        Getter for property: (str) SelectedSnapshotId
         Returns the snapshot id which we want to inspect  
            
         
        """
        pass
    @SelectedSnapshotId.setter
    def SelectedSnapshotId(self, selectedSnapshotId: str):
        """
        Setter for property: (str) SelectedSnapshotId
         Returns the snapshot id which we want to inspect  
            
         
        """
        pass
import NXOpen
import NXOpen.Tooling
class InstanceDataBlockBuilder(NXOpen.Builder): 
    """ JA class for the reuse rule dialog"""
    class ActionType(Enum):
        """
        Members Include: 
         |Global| 
         |Local| 

        """
        Global: int
        Local: int
        @staticmethod
        def ValueOf(value: int) -> InstanceDataBlockBuilder.ActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateMode(Enum):
        """
        Members Include: 
         |Aspect| 
         |Library| 

        """
        Aspect: int
        Library: int
        @staticmethod
        def ValueOf(value: int) -> InstanceDataBlockBuilder.CreateMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreationMode(self) -> InstanceDataBlockBuilder.CreateMode:
        """
        Getter for property: ( InstanceDataBlockBuilder.CreateMode NXOp) CreationMode
         Returns the create mode   
            
         
        """
        pass
    @CreationMode.setter
    def CreationMode(self, createMode: InstanceDataBlockBuilder.CreateMode):
        """
        Setter for property: ( InstanceDataBlockBuilder.CreateMode NXOp) CreationMode
         Returns the create mode   
            
         
        """
        pass
    @property
    def EoDataItemAttributeHolder(self) -> EODataItemAttributeHolder:
        """
        Getter for property: ( EODataItemAttributeHolder NXOp) EoDataItemAttributeHolder
         Returns the data item   
            
         
        """
        pass
    @property
    def InstanceDescription(self) -> str:
        """
        Getter for property: (str) InstanceDescription
         Returns the defined idb text description  
            
         
        """
        pass
    @InstanceDescription.setter
    def InstanceDescription(self, resultText: str):
        """
        Setter for property: (str) InstanceDescription
         Returns the defined idb text description  
            
         
        """
        pass
    @property
    def InstanceName(self) -> str:
        """
        Getter for property: (str) InstanceName
         Returns the defined idb text name  
            
         
        """
        pass
    @InstanceName.setter
    def InstanceName(self, resultText: str):
        """
        Setter for property: (str) InstanceName
         Returns the defined idb text name  
            
         
        """
        pass
    @property
    def SelectedBlock(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedBlock
         Returns the PlcBlock selection   
            
         
        """
        pass
    @property
    def SelectedEngObject(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedEngObject
         Returns the EngObject selection   
            
         
        """
        pass
    @property
    def SelectedFBFromLibrary(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedFBFromLibrary
         Returns the library pou selection  
            
         
        """
        pass
    @property
    def Type(self) -> InstanceDataBlockBuilder.ActionType:
        """
        Getter for property: ( InstanceDataBlockBuilder.ActionType NXOp) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: InstanceDataBlockBuilder.ActionType):
        """
        Setter for property: ( InstanceDataBlockBuilder.ActionType NXOp) Type
         Returns the type   
            
         
        """
        pass
    @property
    def TypeOfIDB(self) -> InstanceDataBlockBuilder.ActionType:
        """
        Getter for property: ( InstanceDataBlockBuilder.ActionType NXOp) TypeOfIDB
         Returns the defined rule type   
            
         
        """
        pass
    @TypeOfIDB.setter
    def TypeOfIDB(self, type: InstanceDataBlockBuilder.ActionType):
        """
        Setter for property: ( InstanceDataBlockBuilder.ActionType NXOp) TypeOfIDB
         Returns the defined rule type   
            
         
        """
        pass
    def SetSymbolicName(self, symbolicName: str) -> None:
        """
         Updates the idb symbolic name 
        """
        pass
    def UpdateSourceBlock(self, selBlock: PlcBlock) -> None:
        """
         Updates the source block selection
        """
        pass
    def UpdateSourceBlockByName(self, fileName: str) -> None:
        """
         Updates the source block by using given file name of reuse library item 
        """
        pass
import NXOpen
import NXOpen.Tooling
class InstantiateBaseDefinitionReuseSelectionBuilder(NXOpen.TaggedObject): 
    """ Builder for selecting base definition"""
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library item selection  
            
         
        """
        pass
    def SetSelection(self, path: str) -> None:
        """
         Sets the selection item
        """
        pass
import NXOpen
import NXOpen.Tooling
class InstantiateTemplateBulkBuilder(MultipleObjectsBuilder): 
    """ JA class for the insert Eng object dialog"""
    class PlacementType(Enum):
        """
        Members Include: 
         |Navigator| 
         |Page| 

        """
        Navigator: int
        Page: int
        @staticmethod
        def ValueOf(value: int) -> InstantiateTemplateBulkBuilder.PlacementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectDetails(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) AspectDetails
         Returns the aspect details ui block  
            
         
        """
        pass
    @property
    def CopyDocumentStructure(self) -> bool:
        """
        Getter for property: (bool) CopyDocumentStructure
         Returns the copy document structure flag to decide whether to copy document structure  
            
         
        """
        pass
    @CopyDocumentStructure.setter
    def CopyDocumentStructure(self, copyDocumentStructure: bool):
        """
        Setter for property: (bool) CopyDocumentStructure
         Returns the copy document structure flag to decide whether to copy document structure  
            
         
        """
        pass
    @property
    def FragmentLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) FragmentLocation
         Returns the co-ordinate of fragment placement location  
            
         
        """
        pass
    @FragmentLocation.setter
    def FragmentLocation(self, fragmentLocation: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) FragmentLocation
         Returns the co-ordinate of fragment placement location  
            
         
        """
        pass
    @property
    def FromMapping(self) -> bool:
        """
        Getter for property: (bool) FromMapping
         Returns the from mapping dialog flag to indicate if bulk template instantiation is initiated from mapping   
            
         
        """
        pass
    @FromMapping.setter
    def FromMapping(self, fromMapping: bool):
        """
        Setter for property: (bool) FromMapping
         Returns the from mapping dialog flag to indicate if bulk template instantiation is initiated from mapping   
            
         
        """
        pass
    @property
    def InsertSettings(self) -> InsertSettingsBuilder:
        """
        Getter for property: ( InsertSettingsBuilder NXOp) InsertSettings
         Returns the aspect placement toggle setting   
            
         
        """
        pass
    @property
    def PlacementValue(self) -> InstantiateTemplateBulkBuilder.PlacementType:
        """
        Getter for property: ( InstantiateTemplateBulkBuilder.PlacementType NXOp) PlacementValue
         Returns the placement type   
            
         
        """
        pass
    @PlacementValue.setter
    def PlacementValue(self, placementType: InstantiateTemplateBulkBuilder.PlacementType):
        """
        Setter for property: ( InstantiateTemplateBulkBuilder.PlacementType NXOp) PlacementValue
         Returns the placement type   
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library selection item  
            
         
        """
        pass
    @property
    def SelectSolutionTemplate(self) -> SelectSolutionTemplateBuilder:
        """
        Getter for property: ( SelectSolutionTemplateBuilder NXOp) SelectSolutionTemplate
         Returns the select solution template ui block  
            
         
        """
        pass
    @property
    def SelectedFragmentTag(self) -> FragmentObject:
        """
        Getter for property: ( FragmentObject NXOp) SelectedFragmentTag
         Returns the tag of selected fragment object  
            
         
        """
        pass
    @SelectedFragmentTag.setter
    def SelectedFragmentTag(self, selectedFragmentTag: FragmentObject):
        """
        Setter for property: ( FragmentObject NXOp) SelectedFragmentTag
         Returns the tag of selected fragment object  
            
         
        """
        pass
    @property
    def SelectedObjects(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedObjects
         Returns the select object   
            
         
        """
        pass
    @property
    def SelectedVariantId(self) -> str:
        """
        Getter for property: (str) SelectedVariantId
         Returns the selected variant CLI specification   
            
         
        """
        pass
    @SelectedVariantId.setter
    def SelectedVariantId(self, variantCliName: str):
        """
        Setter for property: (str) SelectedVariantId
         Returns the selected variant CLI specification   
            
         
        """
        pass
    @property
    def ShowInAutomation(self) -> bool:
        """
        Getter for property: (bool) ShowInAutomation
         Returns the show in automation   
            
         
        """
        pass
    @ShowInAutomation.setter
    def ShowInAutomation(self, showInAutomation: bool):
        """
        Setter for property: (bool) ShowInAutomation
         Returns the show in automation   
            
         
        """
        pass
    @property
    def ShowInFunction(self) -> bool:
        """
        Getter for property: (bool) ShowInFunction
         Returns the show in function   
            
         
        """
        pass
    @ShowInFunction.setter
    def ShowInFunction(self, showInFunction: bool):
        """
        Setter for property: (bool) ShowInFunction
         Returns the show in function   
            
         
        """
        pass
    @property
    def ShowInLocation(self) -> bool:
        """
        Getter for property: (bool) ShowInLocation
         Returns the show in location   
            
         
        """
        pass
    @ShowInLocation.setter
    def ShowInLocation(self, showInLocation: bool):
        """
        Setter for property: (bool) ShowInLocation
         Returns the show in location   
            
         
        """
        pass
    @property
    def ShowInProduct(self) -> bool:
        """
        Getter for property: (bool) ShowInProduct
         Returns the show in product   
            
         
        """
        pass
    @ShowInProduct.setter
    def ShowInProduct(self, showInProduct: bool):
        """
        Setter for property: (bool) ShowInProduct
         Returns the show in product   
            
         
        """
        pass
    @property
    def TemplateInstance(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) TemplateInstance
         Returns the created instance  
            
         
        """
        pass
    @property
    def UnloadTemplate(self) -> bool:
        """
        Getter for property: (bool) UnloadTemplate
         Returns the unload template flag to indicate if template should be unloaded after instantiation  
            
         
        """
        pass
    @UnloadTemplate.setter
    def UnloadTemplate(self, unloadTemplate: bool):
        """
        Setter for property: (bool) UnloadTemplate
         Returns the unload template flag to indicate if template should be unloaded after instantiation  
            
         
        """
        pass
    def ApplyDecisionLogicToTemplateInstance(self, ignoreProductExchange: bool, templateInstanceTag: NXOpen.NXObject) -> List[NXOpen.NXObject]:
        """
         Apply decision logic to value sets in the selected template instance 
         Returns createdObjects ( NXOpen.NXObject Li): .
        """
        pass
    def ApplyDecisionLogicToTemplateInstances(self, isDuringTemplateInstantiation: bool, templateInstanceTags: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Apply decision logic to value sets in the selected multiple template instances 
         Returns createdObjects ( NXOpen.NXObject Li): .
        """
        pass
    def ApplyDecisionLogicToValueSetGroups(self, ignoreProductExchange: bool, valueSetGroupTags: List[NXOpen.NXObject], templateInstanceTags: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Apply decision logic to value sets in the selected value set groups 
         Returns createdObjects ( NXOpen.NXObject Li): .
        """
        pass
    def CollectCreatedTemplateInstances(self) -> List[NXOpen.NXObject]:
        """
         Access Created template instances
         Returns createdInstances ( NXOpen.NXObject Li): .
        """
        pass
    def GetProjectFromPartFileName(self) -> Project:
        """
         Get Project from part file
         Returns project ( Project NXOp): .
        """
        pass
    def ReevaluateDecisionLogicForTemplateInstances(self, templateInstances: List[NXOpen.NXObject]) -> None:
        """
         Load the selected template instances and Re-evaluate the decision logic for the value sets 
        """
        pass
    def ReevaluateDecisionLogicForValueSetGroups(self, valueSetGroupTags: List[NXOpen.NXObject], templateInstanceTags: List[NXOpen.NXObject]) -> None:
        """
         Load the selected context engObjects and Re-evaluate the decision logic for the value set groups 
        """
        pass
    def SetApplyDecisionLogicToValueSets(self) -> List[NXOpen.NXObject]:
        """
         Apply value sets to the instance 
         Returns createdObjects ( NXOpen.NXObject Li): .
        """
        pass
    def SetExternalObjectsToMap(self, externalObjects: List[NXOpen.NXObject]) -> None:
        """
         Selected external objects to be mapped 
        """
        pass
    def UnloadTemplateInstance(self) -> None:
        """
          Unloads the current template.
        """
        pass
class InterfaceAccessType(Enum):
    """
    Members Include: 
     |Undef| 
     |Bool| 
     |Byte| 
     |Word| 
     |Int| 
     |Dint| 
     |Time| 
     |Struct| 
     |BlockDb| 
     |Any| 
     |Unknown| 

    """
    Undef: int
    Bool: int
    Byte: int
    Word: int
    Int: int
    Dint: int
    Time: int
    Struct: int
    BlockDb: int
    Any: int
    Unknown: int
    @staticmethod
    def ValueOf(value: int) -> InterfaceAccessType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class InterfaceMemberBuilder(AMEBaseBuilder): 
    """ InterfaceMemberBuilder class will be used for interface member object creation and editing """
    @property
    def Category(self) -> PlcInterfaceSectionType:
        """
        Getter for property: ( PlcInterfaceSectionType NXOp) Category
         Returns the selected interface member category  
            
         
        """
        pass
    @Category.setter
    def Category(self, section: PlcInterfaceSectionType):
        """
        Setter for property: ( PlcInterfaceSectionType NXOp) Category
         Returns the selected interface member category  
            
         
        """
        pass
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
         Returns the interface member comment   
            
         
        """
        pass
    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
         Returns the interface member comment   
            
         
        """
        pass
    @property
    def DataTypeComp(self) -> DataTypeBuilder:
        """
        Getter for property: ( DataTypeBuilder NXOp) DataTypeComp
         Returns the object data type builder  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the interface member name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the interface member name   
            
         
        """
        pass
class InterfaceMemberPort(MultiValueObjectsPort): 
    """ InterfaceMemberPort Journaling class """
    def Addtextvalue(self, usageType: MultiValueObjectsPort.JaAmeValueObjectUsageType, newValue: List[str]) -> None:
        """
         Add text value 
        """
        pass
    def Insertcomment(self, comment: str) -> None:
        """
         Add comment value 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class InterruptionPointBuilder(AMEBaseBuilder): 
    """ Represents builder for  AME::DB::InterruptionPoint """
    class Variant(Enum):
        """
        Members Include: 
         |A| 
         |B| 
         |C| 
         |D| 
         |E| 
         |F| 
         |G| 
         |H| 

        """
        A: int
        B: int
        C: int
        D: int
        E: int
        F: int
        G: int
        H: int
        @staticmethod
        def ValueOf(value: int) -> InterruptionPointBuilder.Variant:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InterruptionPointName(self) -> str:
        """
        Getter for property: (str) InterruptionPointName
         Returns the interruption point name   
            
         
        """
        pass
    @InterruptionPointName.setter
    def InterruptionPointName(self, interruptionPointName: str):
        """
        Setter for property: (str) InterruptionPointName
         Returns the interruption point name   
            
         
        """
        pass
    @property
    def InterruptionPointVariant(self) -> InterruptionPointBuilder.Variant:
        """
        Getter for property: ( InterruptionPointBuilder.Variant NXOp) InterruptionPointVariant
         Returns the interrupt point variant   
            
         
        """
        pass
    @InterruptionPointVariant.setter
    def InterruptionPointVariant(self, interruptionPointVariant: InterruptionPointBuilder.Variant):
        """
        Setter for property: ( InterruptionPointBuilder.Variant NXOp) InterruptionPointVariant
         Returns the interrupt point variant   
            
         
        """
        pass
    def CreateInterruptionPointNode(self, pageObject: PageObject) -> NXOpen.Diagramming.Node:
        """
         Method to create the Interruption Point Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetDestinationInterruptionPoint(self, interruptionPoint: AMEExtendedObject) -> None:
        """
         Set the destination interruption point to link to 
        """
        pass
    def SetInterruptionPointLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set node location of Interruption Point on page. 
        """
        pass
    def SetStarSource(self, starSource: bool) -> None:
        """
         Set the interruption point type to star source 
        """
        pass
import NXOpen
class IPlcEditableParameterInterface(NXOpen.Object): 
    """ Represents an IPlcEditableParameterInterface """
    @abstractmethod
    def AddDefaultParameter(self) -> IPlcEditableParameter:
        """
         Add a new default parameter to the logic block 
         Returns theResult ( IPlcEditableParameter NXOp): .
        """
        pass
    @abstractmethod
    def DeleteParameter(self, parameter: IPlcEditableParameter) -> None:
        """
         Delete a parameter from the logic block 
        """
        pass
class IPlcEditableParameter(IPlcParameter): 
    """ Represents an IPlcEditableParameter """
    @abstractmethod
    def DataType(self, dataType: str) -> None:
        """
         Set data type
        """
        pass
    @abstractmethod
    def SetName(self, name: str) -> None:
        """
         Set parameter name
        """
        pass
import NXOpen
class IPlcParameter(NXOpen.Object): 
    """ Represents an IPlcParameter """
    pass
import NXOpen
class IPortsContainer(NXOpen.Object): 
    """ Represents Ports Container """
    @abstractmethod
    def GetPorts(self) -> List[IPort]:
        """
         Returns ports assigned to Object 
         Returns ports ( IPort List[NX): .
        """
        pass
import NXOpen
class IPort(NXOpen.Object): 
    """ Represents an IPort """
    @abstractmethod
    def ConnectViaExpression(self, exp: NXOpen.Expression) -> None:
        """
         Connect given ports via expression 
        """
        pass
    @abstractmethod
    @overload
    def Disconnect(self, rhs: IPort) -> None:
        """
         Disconnets lhs from rhs port 
        """
        pass
    @abstractmethod
    @overload
    def Disconnect(self, keepUnmanaged: bool) -> None:
        """
         Disconnects given port 
        """
        pass
    @abstractmethod
    def GetConnections(self) -> List[IPort]:
        """
         Get connected ports 
         Returns ports ( IPort List[NX): .
        """
        pass
    @abstractmethod
    def GetOwningParent(self) -> IPortsContainer:
        """
         Returns owning Parent 
         Returns obj ( IPortsContainer NXOp): .
        """
        pass
    @abstractmethod
    def GetPortCardinality(self) -> str:
        """
         Get the Port Name 
         Returns portCardinality (str): .
        """
        pass
    @abstractmethod
    def GetPortDirection(self) -> str:
        """
         Get the Port Name 
         Returns portDirection (str): .
        """
        pass
    @abstractmethod
    def GetPortName(self) -> str:
        """
         Get the Port Name 
         Returns portName (str): .
        """
        pass
    @abstractmethod
    def GetPortType(self) -> str:
        """
         Get the Port Type 
         Returns portType (str): .
        """
        pass
    @abstractmethod
    def IsConnected(self) -> bool:
        """
         Is Port Connected 
         Returns isConnected (bool): .
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
class LadderDataBuilder(NXOpen.Builder): 
    """ Represents a method used in the ladder data"""
    class Ladders(Enum):
        """
        Members Include: 
         |One| 
         |Two| 

        """
        One: int
        Two: int
        @staticmethod
        def ValueOf(value: int) -> LadderDataBuilder.Ladders:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayDigit(self) -> int:
        """
        Getter for property: (int) DisplayDigit
         Returns the height of the divisions   
            
         
        """
        pass
    @DisplayDigit.setter
    def DisplayDigit(self, display: int):
        """
        Setter for property: (int) DisplayDigit
         Returns the height of the divisions   
            
         
        """
        pass
    @property
    def LinesPerLadder(self) -> int:
        """
        Getter for property: (int) LinesPerLadder
         Returns  the number of ladders   
            
         
        """
        pass
    @LinesPerLadder.setter
    def LinesPerLadder(self, lines: int):
        """
        Setter for property: (int) LinesPerLadder
         Returns  the number of ladders   
            
         
        """
        pass
    @property
    def NumberOfLadders(self) -> int:
        """
        Getter for property: (int) NumberOfLadders
         Returns  the number of ladders   
            
         
        """
        pass
    @NumberOfLadders.setter
    def NumberOfLadders(self, ladders: int):
        """
        Setter for property: (int) NumberOfLadders
         Returns  the number of ladders   
            
         
        """
        pass
    @property
    def StartValueLadder1(self) -> str:
        """
        Getter for property: (str) StartValueLadder1
         Returns the devisions start value for ladder1   
            
         
        """
        pass
    @StartValueLadder1.setter
    def StartValueLadder1(self, value1: str):
        """
        Setter for property: (str) StartValueLadder1
         Returns the devisions start value for ladder1   
            
         
        """
        pass
    @property
    def StartValueLadder2(self) -> str:
        """
        Getter for property: (str) StartValueLadder2
         Returns the devisions start value for ladder2   
            
         
        """
        pass
    @StartValueLadder2.setter
    def StartValueLadder2(self, value2: str):
        """
        Setter for property: (str) StartValueLadder2
         Returns the devisions start value for ladder2   
            
         
        """
        pass
    def MakeLadderDataTable(self, table: NXOpen.Diagramming.Tables.Table) -> None:
        """
         Create ladder data table 
        """
        pass
    def SetLadderStartLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set cursor location on the sheet 
        """
        pass
import NXOpen
class LadderData(NXOpen.NXObject): 
    """ JA class for the LadderData object"""
    pass
import NXOpen
class LayoutDefinitionBuilder(NXOpen.Builder): 
    """ interface for the LayoutDefinitionBuilder"""
    @property
    def SelectClassification(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the selected classification   
            
         
        """
        pass
class LDCachedAttribute(AMEExtendedObject): 
    """ JA class for the Line Design cache Attribute object"""
    pass
import NXOpen
import NXOpen.Diagramming
class LinearDimensionBuilder(NXOpen.Builder): 
    """ Represents a Linear Dimension class Builder  """
    class Dimensionset(Enum):
        """
        Members Include: 
         |Single| 
         |Chain| 
         |Baseline| 

        """
        Single: int
        Chain: int
        Baseline: int
        @staticmethod
        def ValueOf(value: int) -> LinearDimensionBuilder.Dimensionset:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MeasurementDirection(Enum):
        """
        Members Include: 
         |Horizontal| 
         |Vertical| 

        """
        Horizontal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> LinearDimensionBuilder.MeasurementDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DimensionSetType(self) -> LinearDimensionBuilder.Dimensionset:
        """
        Getter for property: ( LinearDimensionBuilder.Dimensionset NXOp) DimensionSetType
         Returns the Dimension Set type   
            
         
        """
        pass
    @DimensionSetType.setter
    def DimensionSetType(self, dimenset: LinearDimensionBuilder.Dimensionset):
        """
        Setter for property: ( LinearDimensionBuilder.Dimensionset NXOp) DimensionSetType
         Returns the Dimension Set type   
            
         
        """
        pass
    @property
    def MeasurementDirectionType(self) -> LinearDimensionBuilder.MeasurementDirection:
        """
        Getter for property: ( LinearDimensionBuilder.MeasurementDirection NXOp) MeasurementDirectionType
         Returns the Measurement Direction type   
            
         
        """
        pass
    @MeasurementDirectionType.setter
    def MeasurementDirectionType(self, measurementdirectn: LinearDimensionBuilder.MeasurementDirection):
        """
        Setter for property: ( LinearDimensionBuilder.MeasurementDirection NXOp) MeasurementDirectionType
         Returns the Measurement Direction type   
            
         
        """
        pass
    def SetSourceDimensionPoint(self, sourceDimensionPoint: NXOpen.Diagramming.Port) -> None:
        """
         Sets the Selected Source Dimension Point 
        """
        pass
    def SetTargetDimensionPoint(self, targetDimensionPoint: NXOpen.Diagramming.Port) -> None:
        """
         Sets the Selected Target Dimension Point 
        """
        pass
import NXOpen
class LineDesignerMappingBuilder(NXOpen.Builder): 
    """ Line Designer mapping dialog JA interface """
    class FilterType(Enum):
        """
        Members Include: 
         |Unhidden| 
         |Hidden| 
         |Unmapped| 
         |Mapped| 
         |Deleted| 
         |TypeMapped| 
         |All| 

        """
        Unhidden: int
        Hidden: int
        Unmapped: int
        Mapped: int
        Deleted: int
        TypeMapped: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> LineDesignerMappingBuilder.FilterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnumFilter(self) -> LineDesignerMappingBuilder.FilterType:
        """
        Getter for property: ( LineDesignerMappingBuilder.FilterType NXOp) EnumFilter
         Returns the enum filter   
            
         
        """
        pass
    @EnumFilter.setter
    def EnumFilter(self, enumFilter: LineDesignerMappingBuilder.FilterType):
        """
        Setter for property: ( LineDesignerMappingBuilder.FilterType NXOp) EnumFilter
         Returns the enum filter   
            
         
        """
        pass
    @overload
    def CreateEngineeringObjectAndMap(self, ldObject: NXOpen.NXObject) -> NXOpen.NXObject:
        """
         Creates a new automation designer object and maps it to a line designer object.
         Returns mappedObject ( NXOpen.NXObject): .
        """
        pass
    @overload
    def CreateEngineeringObjectAndMap(self, ldObjects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
        Creates new automation designer objects and maps them to line designer objects in bulk.
         Returns adObjects ( NXOpen.NXObject Li):  Mapped automation designer objects .
        """
        pass
    def Hide(self, ldObject: NXOpen.NXObject) -> None:
        """
        Hide a ld object
        """
        pass
    def Unhide(self, ldObject: NXOpen.NXObject) -> None:
        """
        Unhide a ld object
        """
        pass
import NXOpen
class LoadLineDesignerBuilder(NXOpen.Builder): 
    """ JA class for the insert LoadLineDesigner dialog"""
    class RevisionRuleType(Enum):
        """
        Members Include: 
         |Working| 
         |NoWorking| 

        """
        Working: int
        NoWorking: int
        @staticmethod
        def ValueOf(value: int) -> LoadLineDesignerBuilder.RevisionRuleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnumRevisionRule(self) -> LoadLineDesignerBuilder.RevisionRuleType:
        """
        Getter for property: ( LoadLineDesignerBuilder.RevisionRuleType NXOp) EnumRevisionRule
         Returns the revision rule   
            
         
        """
        pass
    @EnumRevisionRule.setter
    def EnumRevisionRule(self, enumRevisionRule: LoadLineDesignerBuilder.RevisionRuleType):
        """
        Setter for property: ( LoadLineDesignerBuilder.RevisionRuleType NXOp) EnumRevisionRule
         Returns the revision rule   
            
         
        """
        pass
    @property
    def Perimeter(self) -> float:
        """
        Getter for property: (float) Perimeter
         Returns the perimeter   
            
         
        """
        pass
    @Perimeter.setter
    def Perimeter(self, perimeter: float):
        """
        Setter for property: (float) Perimeter
         Returns the perimeter   
            
         
        """
        pass
    @property
    def SelectionEngObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionEngObject
         Returns the selected objects  
            
         
        """
        pass
    @property
    def ToggleAdditionalObjects(self) -> bool:
        """
        Getter for property: (bool) ToggleAdditionalObjects
         Returns the toggle for additional objects   
            
         
        """
        pass
    @ToggleAdditionalObjects.setter
    def ToggleAdditionalObjects(self, toggleAdditionalObjects: bool):
        """
        Setter for property: (bool) ToggleAdditionalObjects
         Returns the toggle for additional objects   
            
         
        """
        pass
import NXOpen
class Manage2dSymbolsBuilder(AMEBaseBuilder): 
    """ Represents a Manage2dSymbolsBuilder class Builder  """
    class SymbolDrawingStandard(Enum):
        """
        Members Include: 
         |Iec| 
         |Ansi| 
         |NonStandard| 

        """
        Iec: int
        Ansi: int
        NonStandard: int
        @staticmethod
        def ValueOf(value: int) -> Manage2dSymbolsBuilder.SymbolDrawingStandard:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SymbolRepresentationTypes(Enum):
        """
        Members Include: 
         |MultiLineSchematic| 
         |SingleLineSchematic| 
         |BusTopologyDiagram| 
         |PowerSupplyTopologyDiagram| 
         |FluidicDiagram| 
         |Cabinet2d| 
         |GenericSchematic| 

        """
        MultiLineSchematic: int
        SingleLineSchematic: int
        BusTopologyDiagram: int
        PowerSupplyTopologyDiagram: int
        FluidicDiagram: int
        Cabinet2d: int
        GenericSchematic: int
        @staticmethod
        def ValueOf(value: int) -> Manage2dSymbolsBuilder.SymbolRepresentationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DrawingStandard(self) -> Manage2dSymbolsBuilder.SymbolDrawingStandard:
        """
        Getter for property: ( Manage2dSymbolsBuilder.SymbolDrawingStandard NXOp) DrawingStandard
         Returns the representation type which could be of  NXOpen::AME::Manage2dSymbolsBuilder::DrawingStandard    
            
         
        """
        pass
    @DrawingStandard.setter
    def DrawingStandard(self, drawingStandard: Manage2dSymbolsBuilder.SymbolDrawingStandard):
        """
        Setter for property: ( Manage2dSymbolsBuilder.SymbolDrawingStandard NXOp) DrawingStandard
         Returns the representation type which could be of  NXOpen::AME::Manage2dSymbolsBuilder::DrawingStandard    
            
         
        """
        pass
    @property
    def ImmediateCommit(self) -> bool:
        """
        Getter for property: (bool) ImmediateCommit
         Returns the immediate commit option of manage 2D symbol builder  
            
         
        """
        pass
    @ImmediateCommit.setter
    def ImmediateCommit(self, selectAll: bool):
        """
        Setter for property: (bool) ImmediateCommit
         Returns the immediate commit option of manage 2D symbol builder  
            
         
        """
        pass
    @property
    def SelectedObjects(self) -> SelectINodeObjectList:
        """
        Getter for property: ( SelectINodeObjectList NXOp) SelectedObjects
         Returns the Target node selection   
            
         
        """
        pass
    @property
    def SymbolRepresentationType(self) -> Manage2dSymbolsBuilder.SymbolRepresentationTypes:
        """
        Getter for property: ( Manage2dSymbolsBuilder.SymbolRepresentationTypes NXOp) SymbolRepresentationType
         Returns the representation type which could be of  NXOpen::AME::Manage2dSymbolsBuilder::SymbolRepresentationTypes    
            
         
        """
        pass
    @SymbolRepresentationType.setter
    def SymbolRepresentationType(self, symbolRepresentationType: Manage2dSymbolsBuilder.SymbolRepresentationTypes):
        """
        Setter for property: ( Manage2dSymbolsBuilder.SymbolRepresentationTypes NXOp) SymbolRepresentationType
         Returns the representation type which could be of  NXOpen::AME::Manage2dSymbolsBuilder::SymbolRepresentationTypes    
            
         
        """
        pass
    @property
    def SymbolSelection(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SymbolSelection
         Returns the symbol selection builder  
            
         
        """
        pass
    def AddAssignedSymbol(self, symbolNameString: str) -> None:
        """
         Adds the given 2d symbol to the assigned symbols list 
        """
        pass
    def GetAssignedSymbols(self, objTag: NXOpen.TaggedObject) -> List[str]:
        """
         Get assigned symbols 
         Returns assignedSymbols (List[str]): .
        """
        pass
    def GetDefaultSymbol(self, inputObject: NXOpen.TaggedObject) -> str:
        """
         Gets the default 2d symbol assigned to the input object 
         Returns symbolNameString (str): .
        """
        pass
    def RemoveAssignedSymbol(self, symbolNameString: str) -> None:
        """
         Removes the given 2d symbol from the assigned symbols list 
        """
        pass
    def ResetDefaultSymbol(self) -> None:
        """
         Reset the default 2d symbol from the associated NXOpen.AME.ProductDefinition 
        """
        pass
    def SetDefaultSymbol(self, symbolNameString: str) -> None:
        """
         Sets the given 2d symbol as default on the input object  
        """
        pass
import NXOpen
class Manage3DModelsBuilder(NXOpen.Builder): 
    """ Represents the builder that is used to assign 3D models to a NXOpen.AME.ProductDefinition  
    """
    @property
    def SelectedProduct(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedProduct
         Returns the selected  NXOpen::AME::AspectNode    
            
         
        """
        pass
    def Add3dModel(self, fileNameString: str) -> None:
        """
          Assigns the given 3d model to the associated NXOpen.AME.ProductDefinition 
        """
        pass
    def GetDefaultModel(self) -> str:
        """
         Gets the default 3d model from the associated NXOpen.AME.ProductDefinition 
         Returns fileNameString (str): .
        """
        pass
    def Remove3dModel(self, fileNameString: str) -> None:
        """
          Removes the given 3D Model from the associated NXOpen.AME.ProductDefinition 
        """
        pass
    def ResetDefaultModel(self) -> None:
        """
         Reset the default 3d model from the associated NXOpen.AME.ProductDefinition 
        """
        pass
    def SetDefaultModel(self, fileNameString: str) -> None:
        """
         Sets the given 3d model as default to the associated NXOpen.AME.ProductDefinition 
        """
        pass
import NXOpen
class ManageDimensionPointsBuilder(NXOpen.Builder): 
    """ Represents a Manage Dimension Points class Builder  """
    class Types(Enum):
        """
        Members Include: 
         |Automatic| 
         |Manual| 

        """
        Automatic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> ManageDimensionPointsBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Type(self) -> ManageDimensionPointsBuilder.Types:
        """
        Getter for property: ( ManageDimensionPointsBuilder.Types NXOp) Type
         Returns the symbol type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ManageDimensionPointsBuilder.Types):
        """
        Setter for property: ( ManageDimensionPointsBuilder.Types NXOp) Type
         Returns the symbol type   
            
         
        """
        pass
    def CreateDimensionPoint(self) -> str:
        """
         Creates a new dimension point 
         Returns dimensionPt (str): .
        """
        pass
    def DeleteDimensionPoint(self, dimensionPtID: str) -> None:
        """
         Deletes the dimension point 
        """
        pass
    def GetDimensionPointLocation(self, dimensionPtID: str) -> NXOpen.Point2d:
        """
         Gets the dimension point location 
         Returns dimensionPtLocation ( NXOpen.Point2d): .
        """
        pass
    def SetDimensionPointLocation(self, dimensionPtID: str, dimensionPtLocation: NXOpen.Point2d) -> None:
        """
         Sets the dimension point location 
        """
        pass
import NXOpen.Tooling
class ManageEclassMappingBuilder(AMEBaseBuilder): 
    """ Represents a ManageEclassMappingBuilder class Builder  """
    @property
    def ImportType(self) -> ImportType:
        """
        Getter for property: ( ImportType NXOp) ImportType
         Returns the enum import type   
            
         
        """
        pass
    @ImportType.setter
    def ImportType(self, importType: ImportType):
        """
        Setter for property: ( ImportType NXOp) ImportType
         Returns the enum import type   
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library selection item  
            
         
        """
        pass
    @property
    def SelectedEclassNode(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedEclassNode
         Returns the EClass node selection   
            
         
        """
        pass
    def MapEClassObjectToADLibraryObject(self) -> None:
        """
         Map selected EClass object 
        """
        pass
    def MapEClassPropValueToADLibraryObjectPropValue(self, selectedEClassPropertyId: str, selectedEClassPropValueId: str, selectedADLibraryObjectPropValueName: str) -> None:
        """
         Map selected EClass property value with AD Library Object property value
        """
        pass
    def MapEClassPropertyToADLibraryObjectProperty(self, selectedEClassProperty: str, selectedADPropertyId: str, selectedADPropertyName: str) -> None:
        """
         Map selected EClass property with AD Library Object property 
        """
        pass
    def SetAdPropertyIdToDefaultValueMap(self, adPropId: List[str], adDefaultValue: List[str]) -> None:
        """
         Set a map of for all AD properties and their respective Default values
        """
        pass
    def TransferGroupMappingToClass(self) -> None:
        """
         Transfer group level mapping to class level
        """
        pass
    def UnMapEClassObject(self) -> None:
        """
         Unmap selected EClass object 
        """
        pass
    def UnMapEClassPropertyToADLibraryObjectProperty(self, selectedEClassProperty: str) -> None:
        """
         Unmap selected EClass property with AD Library Object property
        """
        pass
    def UnMapEClassPropertyValue(self, selectedEClassPropId: str, selectedEclassPropValueId: str) -> None:
        """
         Unmap selected EClass property value with AD Library Object property value
        """
        pass
class ManageEplanGlobalMappingBuilder(AMEBaseBuilder): 
    """ Represents a ManageEplanGlobalMappingBuilder class Builder  """
    @property
    def AdPropertyData(self) -> ADPropertyData:
        """
        Getter for property: ( ADPropertyData NXOp) AdPropertyData
         Returns the selected AD property   
            
         
        """
        pass
    @AdPropertyData.setter
    def AdPropertyData(self, adPropData: ADPropertyData):
        """
        Setter for property: ( ADPropertyData NXOp) AdPropertyData
         Returns the selected AD property   
            
         
        """
        pass
    @property
    def SelectedEplanProperty(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedEplanProperty
         Returns the Eplan property node selection   
            
         
        """
        pass
    def DeleteEplanPropertyValue(self, selectedEplanValue: str) -> None:
        """
         Delete selected Eplan property value and its mapping if present
        """
        pass
    def MapEplanGlobalValues(self, selectedEplanValueListId: str, selectedEplanValueId: str, selAdValueName: str) -> None:
        """
         Map selected Eplan global values with AD Library Object property values
        """
        pass
    def MapEplanPropertyToADLibraryObjectProperty(self, selectedEplanProperty: str, selectedADPropertyId: str, selectedADPropertyName: str, selectedADPropertyDataType: str) -> None:
        """
         Map selected Eplan property with AD Library Object property 
        """
        pass
    def MapEplanPropertyValueToAdPropertyValue(self, selectedEplanValue: str, selectedADValue: str) -> None:
        """
         Map selected Eplan property value with AD Library Object property value 
        """
        pass
    def UnMapEplanProperty(self) -> None:
        """
         Unmaps selected Eplan property with AD Library Object property 
        """
        pass
    def UnMapEplanPropertyValue(self, selectedADValue: str) -> None:
        """
         Unmaps selected Eplan property value 
        """
        pass
    def UnmapEplanGlobalValue(self, selectedEplanValueId: str) -> None:
        """
         Unmaps selected Eplan values with AD Library Object property values
        """
        pass
import NXOpen
import NXOpen.Tooling
class ManageEplanMappingBuilder(AMEBaseBuilder): 
    """ Represents a ManageEplanMappingBuilder class Builder  """
    @property
    def ImportType(self) -> EplanImportType:
        """
        Getter for property: ( EplanImportType NXOp) ImportType
         Returns the enum import type   
            
         
        """
        pass
    @ImportType.setter
    def ImportType(self, importType: EplanImportType):
        """
        Setter for property: ( EplanImportType NXOp) ImportType
         Returns the enum import type   
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library selection item  
            
         
        """
        pass
    @property
    def ReuseLibraryPort(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryPort
         Returns the reuse library selection port  
            
         
        """
        pass
    @property
    def SelectedEplanNode(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedEplanNode
         Returns the Eplan node selection   
            
         
        """
        pass
    def DeleteEplanProperty(self, selectedEplanPropId: str, isPort: bool) -> None:
        """
         Delete selected Eplan property and its mapping if present
        """
        pass
    def DeleteEplanPropertyValue(self, eplanPropertyObject: NXOpen.NXObject, selectedEplanPropId: str, selectedEplanValue: str, isPort: bool) -> None:
        """
         Delete selected Eplan property value and its mapping if present
        """
        pass
    def MapEplanObjectToADLibraryObject(self) -> None:
        """
         Map selected Eplan object 
        """
        pass
    def MapEplanPropValueToADLibraryObjectPropValue(self, selectedEplanPropertyId: str, selectedEplanPropValueId: str, selectedADLibraryObjectPropValueName: str, isPort: bool) -> None:
        """
         Map selected Eplan property value with AD Library Object property value
        """
        pass
    def MapEplanPropertyToADLibraryObjectProperty(self, selectedEplanProperty: str, selectedADPropertyId: str, selectedADPropertyName: str, isPort: bool) -> None:
        """
         Map selected Eplan property with AD Library Object property 
        """
        pass
    def SetAdPropertyIdToDefaultValueMap(self, adPropId: List[str], adPropName: List[str], adDefaultValue: List[str], adDefaultValueID: List[str], isPort: bool) -> None:
        """
         Set a map of for all AD properties and their respective Default values
        """
        pass
    def UnMapEplanObject(self) -> None:
        """
         Unmap selected Eplan object 
        """
        pass
    def UnMapEplanPropertyToADLibraryObjectProperty(self, selectedEplanProperty: str, isPort: bool) -> None:
        """
         Unmap selected Eplan property with AD Library Object property
        """
        pass
    def UnMapEplanPropertyValue(self, selectedEplanPropId: str, selectedEplanPropValueId: str, isPort: bool) -> None:
        """
         Unmap selected Eplan property value with AD Library Object property value
        """
        pass
class ManageGlobalMappingBuilder(AMEBaseBuilder): 
    """ Represents a ManageGlobalMappingBuilder class Builder  """
    @property
    def AdPropertyData(self) -> ADPropertyData:
        """
        Getter for property: ( ADPropertyData NXOp) AdPropertyData
         Returns the selected AD property   
            
         
        """
        pass
    @AdPropertyData.setter
    def AdPropertyData(self, adPropData: ADPropertyData):
        """
        Setter for property: ( ADPropertyData NXOp) AdPropertyData
         Returns the selected AD property   
            
         
        """
        pass
    @property
    def SelectedEclassProperty(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedEclassProperty
         Returns the EClass property node selection   
            
         
        """
        pass
    def MapBMECatPropertyToADLibraryObjectProperty(self, selectedBMECatProperty: str, selectedADPropertyId: str, selectedADPropertyName: str, selectedADPropertyDataType: str) -> None:
        """
         Map selected BMECat property with AD Library Object property 
        """
        pass
    def MapEClassGlobalValues(self, selectedEClassValueListId: str, selectedEClassValueId: str, selAdValueName: str) -> None:
        """
         Map selected EClass global values with AD Library Object property values
        """
        pass
    def MapEClassPropertyToADLibraryObjectProperty(self, selectedEClassProperty: str, selectedADPropertyId: str, selectedADPropertyName: str, selectedADPropertyDataType: str) -> None:
        """
         Map selected EClass property with AD Library Object property 
        """
        pass
    def MapEClassPropertyValueToAdPropertyValue(self, selectedEClassValue: str, selectedADValue: str) -> None:
        """
         Map selected EClass property value with AD Library Object property value 
        """
        pass
    def UnMapEClassProperty(self) -> None:
        """
         Unmaps selected EClass property with AD Library Object property 
        """
        pass
    def UnMapEClassPropertyValue(self, selectedADValue: str) -> None:
        """
         Unmaps selected EClass property value 
        """
        pass
    def UnmapBMECatProperty(self) -> None:
        """
         Unmaps selected BMECat property with AD Library Object property 
        """
        pass
    def UnmapEClassGlobalValue(self, selectedEClassValueId: str) -> None:
        """
         Unmaps selected EClass values with AD Library Object property values
        """
        pass
import NXOpen
class ManageInterruptionPointsBuilder(NXOpen.Builder): 
    """ JA class for the Manage Interruption Points builder"""
    class ActionTypes(Enum):
        """
        Members Include: 
         |Link| 
         |Unlink| 
         |UnlinkAutolinked| 

        """
        Link: int
        Unlink: int
        UnlinkAutolinked: int
        @staticmethod
        def ValueOf(value: int) -> ManageInterruptionPointsBuilder.ActionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionType(self) -> ManageInterruptionPointsBuilder.ActionTypes:
        """
        Getter for property: ( ManageInterruptionPointsBuilder.ActionTypes NXOp) ActionType
         Returns the action type   
            
         
        """
        pass
    @ActionType.setter
    def ActionType(self, actionType: ManageInterruptionPointsBuilder.ActionTypes):
        """
        Setter for property: ( ManageInterruptionPointsBuilder.ActionTypes NXOp) ActionType
         Returns the action type   
            
         
        """
        pass
    def SetPages(self, pages: List[PageObject]) -> None:
        """
         Set the pages on which interruption points will be linked to builder.
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ManageObjectTypeBuilder(NXOpen.Builder): 
    """ Builder class for assigning AD type to NXOpen.Part and  name to NXOpen.Assemblies.Component """
    def AssignNewType(self, parts: List[NXOpen.Part], newType: str) -> None:
        """
         Assigns AD Type to input parts 
        """
        pass
    def AssignNewTypeName(self, parts: List[NXOpen.Part], newTypeName: str) -> None:
        """
         Assigns AD Type name to input parts 
        """
        pass
    def RemoveType(self, parts: List[NXOpen.Part]) -> None:
        """
         Removes AD Type from input parts 
        """
        pass
    def RenameComponent(self, partOccurrence: NXOpen.Assemblies.Component, name: str) -> None:
        """
         Assigns new name to the input component 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ManageTypeMappingBuilder(NXOpen.Builder): 
    """ This builder class is used to update relevancy information on the external objects.
        This is also used to do the type mapping.
    """
    class DomainRelevancy(Enum):
        """
        Members Include: 
         |Relevant| 
         |Undefined| 
         |Irrelevant| 

        """
        Relevant: int
        Undefined: int
        Irrelevant: int
        @staticmethod
        def ValueOf(value: int) -> ManageTypeMappingBuilder.DomainRelevancy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DomainRelevancyOption(self) -> ManageTypeMappingBuilder.DomainRelevancy:
        """
        Getter for property: ( ManageTypeMappingBuilder.DomainRelevancy NXOp) DomainRelevancyOption
         Returns the functions to GetSet the value of domain relevancy option   
            
         
        """
        pass
    @DomainRelevancyOption.setter
    def DomainRelevancyOption(self, domainRelevancyOption: ManageTypeMappingBuilder.DomainRelevancy):
        """
        Setter for property: ( ManageTypeMappingBuilder.DomainRelevancy NXOp) DomainRelevancyOption
         Returns the functions to GetSet the value of domain relevancy option   
            
         
        """
        pass
    @property
    def ExternalObjectsSource(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ExternalObjectsSource
         Returns the tag of the external objects source   
            
         
        """
        pass
    @ExternalObjectsSource.setter
    def ExternalObjectsSource(self, externalObjectsSource: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ExternalObjectsSource
         Returns the tag of the external objects source   
            
         
        """
        pass
    @property
    def PropertyForMapping(self) -> str:
        """
        Getter for property: (str) PropertyForMapping
         Returns the property to use for type mapping   
            
         
        """
        pass
    @PropertyForMapping.setter
    def PropertyForMapping(self, propertyName: str):
        """
        Setter for property: (str) PropertyForMapping
         Returns the property to use for type mapping   
            
         
        """
        pass
    @property
    def TypeMappingMode(self) -> MappingSourceBuilder.MappingMode:
        """
        Getter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingMode
         Returns the mode to use for type mapping   
            
         
        """
        pass
    @TypeMappingMode.setter
    def TypeMappingMode(self, mode: MappingSourceBuilder.MappingMode):
        """
        Setter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingMode
         Returns the mode to use for type mapping   
            
         
        """
        pass
    def DeleteTypeMapping(self, components: List[NXOpen.NXObject]) -> None:
        """
         Delete existing type mappings for the list of external objects 
        """
        pass
    def GetExternalObjects(self) -> List[NXOpen.NXObject]:
        """
         Get list of external objects for type mapping 
         Returns externalObjects ( NXOpen.NXObject Li): .
        """
        pass
    def UpdateDomainRelevancy(self, components: List[NXOpen.Assemblies.Component], domainRelevancy: ManageTypeMappingBuilder.DomainRelevancy) -> None:
        """
         Sets the domain relevancy for the list of external objects 
        """
        pass
import NXOpen
class ManageVariantBuilder(NXOpen.Builder): 
    """ Builder class for creatingdeletingediting of variant and variant selection objects. """
    def CreateVariant(self) -> Tuple[List[TemplateVariant], TemplateVariantSelection]:
        """
          Method to create variant along with it's parent variant selection
         Returns A tuple consisting of (createdVariants, parentVariantSelection). 
         - createdVariants is:  TemplateVariant List[NX.
         - parentVariantSelection is:  TemplateVariantSelection NXOp.

        """
        pass
    def DeleteVariantsAndVariantSelections(self, objectsToDelete: List[NXOpen.NXObject]) -> None:
        """
          Method to delete variants and variant selections
        """
        pass
    def DuplicateVariants(self, inputVariants: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Method to duplicate input variants under a variant selection 
         Returns copiedVariants ( NXOpen.NXObject Li): .
        """
        pass
    def EditVariant(self) -> None:
        """
          Method to edit existing variant 
        """
        pass
    def GetDefaultTemplateSolutionPartToEdit(self, contextVariant: NXOpen.NXObject) -> Tuple[NXOpen.Part, Project]:
        """
         Method to get default template solution Part for editing  
         Returns A tuple consisting of (templateSolutionPartToEdit, project). 
         - templateSolutionPartToEdit is:  NXOpen.Part.
         - project is:  Project NXOp.

        """
        pass
    def GetVariantProject(self, variantObject: NXOpen.NXObject) -> NXOpen.NXObject:
        """
         Method to get the variant's project 
         Returns variantProject ( NXOpen.NXObject): .
        """
        pass
    def PropagateChanges(self) -> None:
        """
          Method to propagate base template changes  
        """
        pass
    def SetDefaultVariant(self, variantObject: TemplateVariant) -> None:
        """
          Method to set default variant for a variant selection 
        """
        pass
    def SetVariantDescription(self, variantObject: NXOpen.NXObject, newDescription: str) -> None:
        """
          Method to set description of the variant 
        """
        pass
    def SetVariantName(self, variantObject: NXOpen.NXObject, newName: str) -> None:
        """
          Method to set name of the variant 
        """
        pass
    def SetVariantSelectionDescription(self, variantSelectionObject: NXOpen.NXObject, newDescription: str) -> None:
        """
          Method to set description of the variant selection 
        """
        pass
    def SetVariantSelectionName(self, variantSelectionObject: NXOpen.NXObject, newName: str) -> None:
        """
          Method to set name of the variant selection 
        """
        pass
import NXOpen
class MappingSourceBuilder(NXOpen.TaggedObject): 
    """ This builder class is a re-usable component used to filter 
        external objects by discipline.
        This is also used to select the type mapping mode preference.
    """
    class MappingMode(Enum):
        """
        Members Include: 
         |MechanicalObject| 
         |AutomationIdAsProperty| 
         |MechanicalTypeAsProperty| 

        """
        MechanicalObject: int
        AutomationIdAsProperty: int
        MechanicalTypeAsProperty: int
        @staticmethod
        def ValueOf(value: int) -> MappingSourceBuilder.MappingMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExternalObjectsSource(self) -> int:
        """
        Getter for property: (int) ExternalObjectsSource
         Returns the functions to GetSet the mapping source input   
            
         
        """
        pass
    @ExternalObjectsSource.setter
    def ExternalObjectsSource(self, externalObjectSourceIndex: int):
        """
        Setter for property: (int) ExternalObjectsSource
         Returns the functions to GetSet the mapping source input   
            
         
        """
        pass
    @property
    def MappingProperty(self) -> str:
        """
        Getter for property: (str) MappingProperty
         Returns the property to use for type mapping by mechanical or automation id   
            
         
        """
        pass
    @MappingProperty.setter
    def MappingProperty(self, mappingProperty: str):
        """
        Setter for property: (str) MappingProperty
         Returns the property to use for type mapping by mechanical or automation id   
            
         
        """
        pass
    @property
    def TypeMappingMode(self) -> MappingSourceBuilder.MappingMode:
        """
        Getter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingMode
         Returns the functions to GetSet the  NXOpen::AME::MappingSourceBuilder::MappingMode    
            
         
        """
        pass
    @TypeMappingMode.setter
    def TypeMappingMode(self, mode: MappingSourceBuilder.MappingMode):
        """
        Setter for property: ( MappingSourceBuilder.MappingMode NXOp) TypeMappingMode
         Returns the functions to GetSet the  NXOpen::AME::MappingSourceBuilder::MappingMode    
            
         
        """
        pass
import NXOpen
class MapToExistingObjectBuilder(NXOpen.Builder): 
    """ Line Designer map to existing (EO) dialog JA interface """
    @property
    def MapTemplateToggle(self) -> bool:
        """
        Getter for property: (bool) MapTemplateToggle
         Returns the toggle whether to map to template   
            
         
        """
        pass
    @MapTemplateToggle.setter
    def MapTemplateToggle(self, mapTemplateToggle: bool):
        """
        Setter for property: (bool) MapTemplateToggle
         Returns the toggle whether to map to template   
            
         
        """
        pass
    @property
    def SelectionAD(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectionAD
         Returns the get selectionAD   
            
         
        """
        pass
    @property
    def SelectionLD(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectionLD
         Returns the get selectionLD   
            
         
        """
        pass
    def InsertIntoSelectionAD(self, adObject: NXOpen.NXObject) -> None:
        """
         The insert into selectionAD 
        """
        pass
    def InsertIntoSelectionLD(self, ldObject: NXOpen.NXObject) -> None:
        """
         The insert into selectionAD 
        """
        pass
import NXOpen
class MemoryAreaBulkAddressingBuilder(MultipleObjectsBuilder): 
    """ JA class for MemoryAreaBulkAddressing dialog"""
    @property
    def SelectionObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionObject
         Returns the selected object whose start address will be changed.  
             
         
        """
        pass
    @property
    def StartAddress(self) -> int:
        """
        Getter for property: (int) StartAddress
         Returns the first start address   
            
         
        """
        pass
    @StartAddress.setter
    def StartAddress(self, startAddress: int):
        """
        Setter for property: (int) StartAddress
         Returns the first start address   
            
         
        """
        pass
    @property
    def SyncAddress(self) -> bool:
        """
        Getter for property: (bool) SyncAddress
         Returns the Synchonize modules  
            
         
        """
        pass
    @SyncAddress.setter
    def SyncAddress(self, syncAddress: bool):
        """
        Setter for property: (bool) SyncAddress
         Returns the Synchonize modules  
            
         
        """
        pass
class MemorySectionType(Enum):
    """
    Members Include: 
     |Input| 
     |Output| 
     |Memory| 
     |Timer| 
     |Counter| 
     |NotSet| 
     |Periphery| 
     |PeripheryInput| 
     |PeripheryOutput| 
     |Fb| 
     |Fc| 
     |Db| 
     |Di| 
     |Localc| 
     |Localn| 
     |Dbc| 
     |Dbr| 
     |Dbv| 

    """
    Input: int
    Output: int
    Memory: int
    Timer: int
    Counter: int
    NotSet: int
    Periphery: int
    PeripheryInput: int
    PeripheryOutput: int
    Fb: int
    Fc: int
    Db: int
    Di: int
    Localc: int
    Localn: int
    Dbc: int
    Dbr: int
    Dbv: int
    @staticmethod
    def ValueOf(value: int) -> MemorySectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class MountingInterfaceBuilder(NXOpen.Builder): 
    """ Builder class for creating mounting interface object in NXOpen.Part """
    class FixingPolicy(Enum):
        """
        Members Include: 
         |Point| 
         |Face| 

        """
        Point: int
        Face: int
        @staticmethod
        def ValueOf(value: int) -> MountingInterfaceBuilder.FixingPolicy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterfaceType(Enum):
        """
        Members Include: 
         |Fixing| 
         |ComponentReceptacle| 

        """
        Fixing: int
        ComponentReceptacle: int
        @staticmethod
        def ValueOf(value: int) -> MountingInterfaceBuilder.InterfaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReceptaclePolicy(Enum):
        """
        Members Include: 
         |Fixed| 
         |AxisMovement| 
         |PlaneMovement| 

        """
        Fixed: int
        AxisMovement: int
        PlaneMovement: int
        @staticmethod
        def ValueOf(value: int) -> MountingInterfaceBuilder.ReceptaclePolicy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DirectionOfInterface(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DirectionOfInterface
         Returns the direction of interface   
            
         
        """
        pass
    @DirectionOfInterface.setter
    def DirectionOfInterface(self, directionOfInterface: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DirectionOfInterface
         Returns the direction of interface   
            
         
        """
        pass
    @property
    def FixingType(self) -> MountingInterfaceBuilder.FixingPolicy:
        """
        Getter for property: ( MountingInterfaceBuilder.FixingPolicy NXOp) FixingType
         Returns the  NXOpen::AME::MountingInterfaceBuilder::FixingPolicy    
            
         
        """
        pass
    @FixingType.setter
    def FixingType(self, type: MountingInterfaceBuilder.FixingPolicy):
        """
        Setter for property: ( MountingInterfaceBuilder.FixingPolicy NXOp) FixingType
         Returns the  NXOpen::AME::MountingInterfaceBuilder::FixingPolicy    
            
         
        """
        pass
    @property
    def MountingInterfaceType(self) -> MountingInterfaceBuilder.InterfaceType:
        """
        Getter for property: ( MountingInterfaceBuilder.InterfaceType NXOp) MountingInterfaceType
         Returns the  NXOpen::AME::MountingInterfaceBuilder::InterfaceType    
            
         
        """
        pass
    @MountingInterfaceType.setter
    def MountingInterfaceType(self, type: MountingInterfaceBuilder.InterfaceType):
        """
        Setter for property: ( MountingInterfaceBuilder.InterfaceType NXOp) MountingInterfaceType
         Returns the  NXOpen::AME::MountingInterfaceBuilder::InterfaceType    
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def ParallelReferenceObject(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ParallelReferenceObject
         Returns the parallel reference object   
            
         
        """
        pass
    @ParallelReferenceObject.setter
    def ParallelReferenceObject(self, parallelReferenceObject: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ParallelReferenceObject
         Returns the parallel reference object   
            
         
        """
        pass
    @property
    def ReceptacleType(self) -> MountingInterfaceBuilder.ReceptaclePolicy:
        """
        Getter for property: ( MountingInterfaceBuilder.ReceptaclePolicy NXOp) ReceptacleType
         Returns the  NXOpen::AME::MountingInterfaceBuilder::ReceptaclePolicy    
            
         
        """
        pass
    @ReceptacleType.setter
    def ReceptacleType(self, receptacleType: MountingInterfaceBuilder.ReceptaclePolicy):
        """
        Setter for property: ( MountingInterfaceBuilder.ReceptaclePolicy NXOp) ReceptacleType
         Returns the  NXOpen::AME::MountingInterfaceBuilder::ReceptaclePolicy    
            
         
        """
        pass
    @property
    def SpecifyFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SpecifyFace
         Returns the specify face   
            
         
        """
        pass
    @SpecifyFace.setter
    def SpecifyFace(self, collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) SpecifyFace
         Returns the specify face   
            
         
        """
        pass
    @property
    def SpecifyLine(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SpecifyLine
         Returns the specify line   
            
         
        """
        pass
    @property
    def SpecifyPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SpecifyPoint
         Returns the specify point   
            
         
        """
        pass
    @SpecifyPoint.setter
    def SpecifyPoint(self, specifyPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SpecifyPoint
         Returns the specify point   
            
         
        """
        pass
    def AddInterface(self) -> None:
        """
         Adds a NXOpen.AME.MountingInterface object 
        """
        pass
    def RemoveInterfaces(self, mountingInterfaces: List[str]) -> None:
        """
         Delete input NXOpen.AME.MountingInterface objects 
        """
        pass
    def SetDefaultFixingInterface(self, fixingName: str) -> None:
        """
         Sets input NXOpen.AME.MountingInterface as default 
        """
        pass
import NXOpen
class MountingInterface(NXOpen.NXObject): 
    """ Represents a Mounting Interface"""
    pass
class MultipleObjectsBuilder(AMEBaseBuilder): 
    """ JA class for for builder which creates more than one journal able objects"""
    pass
class MultiValueObjectsPort(PlcSoftwareGenPort): 
    """ MultiValueObjectsPort Journaling class """
    class JaAmeValueObjectUsageType(Enum):
        """
        Members Include: 
         |PreDefinition| 
         |DefaultValue| 
         |DataType| 

        """
        PreDefinition: int
        DefaultValue: int
        DataType: int
        @staticmethod
        def ValueOf(value: int) -> MultiValueObjectsPort.JaAmeValueObjectUsageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Inserttextvalue(self, usageType: MultiValueObjectsPort.JaAmeValueObjectUsageType, newValue: List[str]) -> None:
        """
         Add text value 
        """
        pass
    def Reset(self, usageType: MultiValueObjectsPort.JaAmeValueObjectUsageType) -> None:
        """
         Reset the rule 
        """
        pass
import NXOpen
class NamingRuleBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[NamingRuleBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: NamingRuleBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: NamingRuleBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: NamingRuleBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: NamingRuleBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> NamingRuleBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( NamingRuleBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[NamingRuleBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( NamingRuleBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: NamingRuleBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[NamingRuleBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: NamingRuleBuilder, object2: NamingRuleBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class NamingRuleBuilder(NXOpen.Builder): 
    """ Naming Rule Builder """
    @property
    def ClassificationItem(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) ClassificationItem
         Returns the classification item   
            
         
        """
        pass
    @property
    def EoName(self) -> str:
        """
        Getter for property: (str) EoName
         Returns the engineering object name  
            
         
        """
        pass
    @EoName.setter
    def EoName(self, eoName: str):
        """
        Setter for property: (str) EoName
         Returns the engineering object name  
            
         
        """
        pass
    @property
    def IndexDigitsInFunction(self) -> int:
        """
        Getter for property: (int) IndexDigitsInFunction
         Returns the index display digits in function aspect  
            
         
        """
        pass
    @IndexDigitsInFunction.setter
    def IndexDigitsInFunction(self, indexIncrement: int):
        """
        Setter for property: (int) IndexDigitsInFunction
         Returns the index display digits in function aspect  
            
         
        """
        pass
    @property
    def IndexDigitsInLocation(self) -> int:
        """
        Getter for property: (int) IndexDigitsInLocation
         Returns the index display digits in location aspect  
            
         
        """
        pass
    @IndexDigitsInLocation.setter
    def IndexDigitsInLocation(self, indexIncrement: int):
        """
        Setter for property: (int) IndexDigitsInLocation
         Returns the index display digits in location aspect  
            
         
        """
        pass
    @property
    def IndexDigitsInProduct(self) -> int:
        """
        Getter for property: (int) IndexDigitsInProduct
         Returns the index display digits in product aspect  
            
         
        """
        pass
    @IndexDigitsInProduct.setter
    def IndexDigitsInProduct(self, indexIncrement: int):
        """
        Setter for property: (int) IndexDigitsInProduct
         Returns the index display digits in product aspect  
            
         
        """
        pass
    @property
    def IndexIncrementInFunction(self) -> int:
        """
        Getter for property: (int) IndexIncrementInFunction
         Returns the index increment in function aspect  
            
         
        """
        pass
    @IndexIncrementInFunction.setter
    def IndexIncrementInFunction(self, indexIncrement: int):
        """
        Setter for property: (int) IndexIncrementInFunction
         Returns the index increment in function aspect  
            
         
        """
        pass
    @property
    def IndexIncrementInLocation(self) -> int:
        """
        Getter for property: (int) IndexIncrementInLocation
         Returns the index increment in location aspect  
            
         
        """
        pass
    @IndexIncrementInLocation.setter
    def IndexIncrementInLocation(self, indexIncrement: int):
        """
        Setter for property: (int) IndexIncrementInLocation
         Returns the index increment in location aspect  
            
         
        """
        pass
    @property
    def IndexIncrementInProduct(self) -> int:
        """
        Getter for property: (int) IndexIncrementInProduct
         Returns the index increment in product aspect  
            
         
        """
        pass
    @IndexIncrementInProduct.setter
    def IndexIncrementInProduct(self, indexIncrement: int):
        """
        Setter for property: (int) IndexIncrementInProduct
         Returns the index increment in product aspect  
            
         
        """
        pass
    @property
    def NameInFunction(self) -> str:
        """
        Getter for property: (str) NameInFunction
         Returns the name in function aspect  
            
         
        """
        pass
    @NameInFunction.setter
    def NameInFunction(self, nameInFunction: str):
        """
        Setter for property: (str) NameInFunction
         Returns the name in function aspect  
            
         
        """
        pass
    @property
    def NameInLocation(self) -> str:
        """
        Getter for property: (str) NameInLocation
         Returns the name in location aspect  
            
         
        """
        pass
    @NameInLocation.setter
    def NameInLocation(self, nameInLocation: str):
        """
        Setter for property: (str) NameInLocation
         Returns the name in location aspect  
            
         
        """
        pass
    @property
    def NameInProduct(self) -> str:
        """
        Getter for property: (str) NameInProduct
         Returns the name in product aspect  
            
         
        """
        pass
    @NameInProduct.setter
    def NameInProduct(self, nameInProduct: str):
        """
        Setter for property: (str) NameInProduct
         Returns the name in product aspect  
            
         
        """
        pass
    @property
    def SelectedClassification(self) -> str:
        """
        Getter for property: (str) SelectedClassification
         Returns the Classification ID   
            
         
        """
        pass
    @SelectedClassification.setter
    def SelectedClassification(self, classification: str):
        """
        Setter for property: (str) SelectedClassification
         Returns the Classification ID   
            
         
        """
        pass
    @property
    def StartIndexInFunction(self) -> int:
        """
        Getter for property: (int) StartIndexInFunction
         Returns the start index in function aspect  
            
         
        """
        pass
    @StartIndexInFunction.setter
    def StartIndexInFunction(self, startIndex: int):
        """
        Setter for property: (int) StartIndexInFunction
         Returns the start index in function aspect  
            
         
        """
        pass
    @property
    def StartIndexInLocation(self) -> int:
        """
        Getter for property: (int) StartIndexInLocation
         Returns the start index in location aspect  
            
         
        """
        pass
    @StartIndexInLocation.setter
    def StartIndexInLocation(self, startIndex: int):
        """
        Setter for property: (int) StartIndexInLocation
         Returns the start index in location aspect  
            
         
        """
        pass
    @property
    def StartIndexInProduct(self) -> int:
        """
        Getter for property: (int) StartIndexInProduct
         Returns the start index in product aspect  
            
         
        """
        pass
    @StartIndexInProduct.setter
    def StartIndexInProduct(self, startIndex: int):
        """
        Setter for property: (int) StartIndexInProduct
         Returns the start index in product aspect  
            
         
        """
        pass
import NXOpen
class NamingRuleListBuilder(NXOpen.TaggedObject): 
    """ Classification to Engineering Object Name Map Builder """
    @property
    def List(self) -> NamingRuleBuilderList:
        """
        Getter for property: ( NamingRuleBuilderList NXOp) List
         Returns the pair list   
            
         
        """
        pass
    def CreateRule(self) -> NamingRuleBuilder:
        """
         Create a new rule builder 
         Returns ruleBuilder ( NamingRuleBuilder NXOp): .
        """
        pass
    def DeleteRule(self, ruleBuilder: NamingRuleBuilder) -> None:
        """
         Delete rule 
        """
        pass
import NXOpen
class NamingRuleSettingsBuilder(NXOpen.Builder): 
    """
        JA class for dialog for naming rule settings
    """
    class Sources(Enum):
        """
        Members Include: 
         |Period| 
         |AspectPrefix| 
         |Nothing| 

        """
        Period: int
        AspectPrefix: int
        Nothing: int
        @staticmethod
        def ValueOf(value: int) -> NamingRuleSettingsBuilder.Sources:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdvancedAspectNaming(self) -> NamingRuleListBuilder:
        """
        Getter for property: ( NamingRuleListBuilder NXOp) AdvancedAspectNaming
         Returns the advanced aspect naming builder   
            
         
        """
        pass
    @property
    def EngObjectName(self) -> NamingRuleListBuilder:
        """
        Getter for property: ( NamingRuleListBuilder NXOp) EngObjectName
         Returns the engineering object name builder   
            
         
        """
        pass
import NXOpen
class NamingSchemeAspectNamingBuilder(NXOpen.Builder): 
    """
        JA class for Naming Scheme Aspect Naming Builder
    """
    @property
    def ClassificationItem(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) ClassificationItem
         Returns the classification item   
            
         
        """
        pass
    @property
    def NameInFunction(self) -> str:
        """
        Getter for property: (str) NameInFunction
         Returns the name in function aspect  
            
         
        """
        pass
    @NameInFunction.setter
    def NameInFunction(self, nameInFunction: str):
        """
        Setter for property: (str) NameInFunction
         Returns the name in function aspect  
            
         
        """
        pass
    @property
    def NameInLocation(self) -> str:
        """
        Getter for property: (str) NameInLocation
         Returns the name in location aspect  
            
         
        """
        pass
    @NameInLocation.setter
    def NameInLocation(self, nameInLocation: str):
        """
        Setter for property: (str) NameInLocation
         Returns the name in location aspect  
            
         
        """
        pass
    @property
    def NameInProduct(self) -> str:
        """
        Getter for property: (str) NameInProduct
         Returns the name in product aspect  
            
         
        """
        pass
    @NameInProduct.setter
    def NameInProduct(self, nameInProduct: str):
        """
        Setter for property: (str) NameInProduct
         Returns the name in product aspect  
            
         
        """
        pass
    @property
    def SameNameInAllAspect(self) -> str:
        """
        Getter for property: (str) SameNameInAllAspect
         Returns the name in function aspect  
            
         
        """
        pass
    @SameNameInAllAspect.setter
    def SameNameInAllAspect(self, sameNameInAllAspect: str):
        """
        Setter for property: (str) SameNameInAllAspect
         Returns the name in function aspect  
            
         
        """
        pass
    @property
    def SelectLibraryObject(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectLibraryObject
         Returns the library item   
            
         
        """
        pass
    def CreateOrUpdateNamingRuleAndSetData(self) -> None:
        """
         CreateUpdate naming rule 
        """
        pass
    def FillFunctionAspectData(self, startIndex: int, increment: int, displayDigits: int) -> None:
        """
         Fills function aspect data 
        """
        pass
    def FillLocationAspectData(self, startIndex: int, increment: int, displayDigits: int) -> None:
        """
         Fills location aspect data 
        """
        pass
    def FillProductAspectData(self, startIndex: int, increment: int, displayDigits: int) -> None:
        """
         Fills product aspect data 
        """
        pass
    def RemoveNamingRule(self, namingRuleTag: NXOpen.NXObject) -> None:
        """
         Remove naming rule from list 
        """
        pass
import NXOpen
class NamingSchemeGeneralBuilder(NXOpen.Builder): 
    """
        JA class for Naming Scheme General Builder
    """
    class DelimiterType(Enum):
        """
        Members Include: 
         |Dot|  A dot (.) is used as the delimiter 
         |AspectPrefix|  Aspect Prefix is used as the delimiter 
         |NoDelimiter|  No delimiter will be used 

        """
        Dot: int
        AspectPrefix: int
        NoDelimiter: int
        @staticmethod
        def ValueOf(value: int) -> NamingSchemeGeneralBuilder.DelimiterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Delimiter(self) -> NamingSchemeGeneralBuilder.DelimiterType:
        """
        Getter for property: ( NamingSchemeGeneralBuilder.DelimiterType NXOp) Delimiter
         Returns the  NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType    
            
         
        """
        pass
    @Delimiter.setter
    def Delimiter(self, delimiter: NamingSchemeGeneralBuilder.DelimiterType):
        """
        Setter for property: ( NamingSchemeGeneralBuilder.DelimiterType NXOp) Delimiter
         Returns the  NXOpen::AME::NamingSchemeGeneralBuilder::DelimiterType    
            
         
        """
        pass
    @property
    def Function(self) -> str:
        """
        Getter for property: (str) Function
         Returns the aspect prefix of function aspect   
            
         
        """
        pass
    @Function.setter
    def Function(self, functionPrefix: str):
        """
        Setter for property: (str) Function
         Returns the aspect prefix of function aspect   
            
         
        """
        pass
    @property
    def Location(self) -> str:
        """
        Getter for property: (str) Location
         Returns the aspect prefix of location aspect   
            
         
        """
        pass
    @Location.setter
    def Location(self, location: str):
        """
        Setter for property: (str) Location
         Returns the aspect prefix of location aspect   
            
         
        """
        pass
    @property
    def Product(self) -> str:
        """
        Getter for property: (str) Product
         Returns the aspect prefix of product aspect   
            
         
        """
        pass
    @Product.setter
    def Product(self, product: str):
        """
        Setter for property: (str) Product
         Returns the aspect prefix of product aspect   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ObjectConnectionBuilder(NXOpen.TaggedObject): 
    """ JA class for the reuse object connection block"""
    class Type(Enum):
        """
        Members Include: 
         |Object| 
         |Port| 
         |Expression| 

        """
        Object: int
        Port: int
        Expression: int
        @staticmethod
        def ValueOf(value: int) -> ObjectConnectionBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ResultString(self) -> str:
        """
        Getter for property: (str) ResultString
         Returns the result string text   
            
         
        """
        pass
    @property
    def SortingBlock(self) -> SortingBlockBuilder:
        """
        Getter for property: ( SortingBlockBuilder NXOp) SortingBlock
         Returns the sorting block   
            
         
        """
        pass
    @property
    def TargetObjectSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) TargetObjectSelection
         Returns the selection of target objects  
            
         
        """
        pass
    def ConnectDynamic(self, exp: NXOpen.Expression) -> None:
        """
         Create a new dynamic connection
        """
        pass
    def ConnectFix(self) -> None:
        """
         Create a new fix connection
        """
        pass
    def Disconnect(self) -> None:
        """
         Disconnect the current connection
        """
        pass
    def GetConnectedObjects(self) -> List[NXOpen.NXObject]:
        """
         Get the actual connectedObjects
         Returns connencedObjects ( NXOpen.NXObject Li): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ObjectConnectionDetailBuilder(NXOpen.TaggedObject): 
    """ JA class for the reuse object connection detail block"""
    @property
    def PropertyString(self) -> str:
        """
        Getter for property: (str) PropertyString
         Returns the selected property name  
            
         
        """
        pass
    @PropertyString.setter
    def PropertyString(self, propertyName: str):
        """
        Setter for property: (str) PropertyString
         Returns the selected property name  
            
         
        """
        pass
    @property
    def ResultString(self) -> str:
        """
        Getter for property: (str) ResultString
         Returns the result string text   
            
         
        """
        pass
    def ChangeEditObject(self, newObject: NXOpen.NXObject) -> None:
        """
         Change the edit object
        """
        pass
    def DisconnectExpression(self) -> None:
        """
         Disconnect the expression 
        """
        pass
    def Populate(self, hierarchy: List[str]) -> None:
        """
         Populate selection 
        """
        pass
    def SetExpression(self, exp: NXOpen.Expression) -> None:
        """
         Set the condition for the value set 
        """
        pass
class ObjectEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the object given a starting point """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class ObjectNameBuilder(NXOpen.TaggedObject): 
    """Object Name JA class """
    @property
    def ObjectDescription(self) -> str:
        """
        Getter for property: (str) ObjectDescription
         Returns the object description   
            
         
        """
        pass
    @ObjectDescription.setter
    def ObjectDescription(self, objectDescription: str):
        """
        Setter for property: (str) ObjectDescription
         Returns the object description   
            
         
        """
        pass
    @property
    def ObjectName(self) -> str:
        """
        Getter for property: (str) ObjectName
         Returns the object name   
            
         
        """
        pass
    @ObjectName.setter
    def ObjectName(self, objectName: str):
        """
        Setter for property: (str) ObjectName
         Returns the object name   
            
         
        """
        pass
    def GenerateName(self, baseName: str) -> None:
        """
         Geneate a new unique name 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ObjectNameIndexBuilder(NXOpen.TaggedObject): 
    """Object Name Index JA class """
    @property
    def ObjectDescription(self) -> str:
        """
        Getter for property: (str) ObjectDescription
         Returns the object description   
            
         
        """
        pass
    @ObjectDescription.setter
    def ObjectDescription(self, objectDescription: str):
        """
        Setter for property: (str) ObjectDescription
         Returns the object description   
            
         
        """
        pass
    @property
    def ObjectIndex(self) -> str:
        """
        Getter for property: (str) ObjectIndex
         Returns the object index   
            
         
        """
        pass
    @property
    def ObjectName(self) -> str:
        """
        Getter for property: (str) ObjectName
         Returns the object name   
            
         
        """
        pass
    @ObjectName.setter
    def ObjectName(self, objectName: str):
        """
        Setter for property: (str) ObjectName
         Returns the object name   
            
         
        """
        pass
import NXOpen
class OperandRuleBuilder(NXOpen.Builder): 
    """ JA class for the parameter rule dialog"""
    @property
    def Conditions(self) -> ConditionsBuilder:
        """
        Getter for property: ( ConditionsBuilder NXOp) Conditions
         Returns the object condition ui block  
            
         
        """
        pass
    @property
    def ObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ObjectConnection
         Returns the object connection ui block  
            
         
        """
        pass
    @property
    def ObjectConnectionDetail(self) -> ObjectConnectionDetailBuilder:
        """
        Getter for property: ( ObjectConnectionDetailBuilder NXOp) ObjectConnectionDetail
         Returns the object connection detail ui block  
            
         
        """
        pass
    @property
    def PortCreationType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) PortCreationType
         Returns the creation type when creating a position  
            
         
        """
        pass
    @PortCreationType.setter
    def PortCreationType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) PortCreationType
         Returns the creation type when creating a position  
            
         
        """
        pass
    @property
    def RuleName(self) -> str:
        """
        Getter for property: (str) RuleName
         Returns the rule name   
            
         
        """
        pass
    @RuleName.setter
    def RuleName(self, resultText: str):
        """
        Setter for property: (str) RuleName
         Returns the rule name   
            
         
        """
        pass
    @property
    def SelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) SelectionPort
         Returns the operand replacement port selection   
            
         
        """
        pass
import NXOpen
class OperatorRuleBuilder(NXOpen.Builder): 
    """ OperatorRule Dialog """
    class NegationValue(Enum):
        """
        Members Include: 
         |FalseValue| 
         |TrueValue| 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> OperatorRuleBuilder.NegationValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterType(Enum):
        """
        Members Include: 
         |Input| 
         |Output| 

        """
        Input: int
        Output: int
        @staticmethod
        def ValueOf(value: int) -> OperatorRuleBuilder.ParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Conditions(self) -> ConditionsBuilder:
        """
        Getter for property: ( ConditionsBuilder NXOp) Conditions
         Returns the conditions block  
            
         
        """
        pass
    @property
    def Negation(self) -> OperatorRuleBuilder.NegationValue:
        """
        Getter for property: ( OperatorRuleBuilder.NegationValue NXOp) Negation
         Returns the Negation of parameter  
            
         
        """
        pass
    @Negation.setter
    def Negation(self, negation: OperatorRuleBuilder.NegationValue):
        """
        Setter for property: ( OperatorRuleBuilder.NegationValue NXOp) Negation
         Returns the Negation of parameter  
            
         
        """
        pass
    @property
    def ObjectConnectionDetail(self) -> ObjectConnectionDetailBuilder:
        """
        Getter for property: ( ObjectConnectionDetailBuilder NXOp) ObjectConnectionDetail
         Returns the Variable component  
            
         
        """
        pass
    @property
    def OperatorType(self) -> PlcRule.Type:
        """
        Getter for property: ( PlcRule.Type NXOp) OperatorType
         Returns the OperatorType   
            
         
        """
        pass
    @OperatorType.setter
    def OperatorType(self, operatorType: PlcRule.Type):
        """
        Setter for property: ( PlcRule.Type NXOp) OperatorType
         Returns the OperatorType   
            
         
        """
        pass
    @property
    def ParameterRuleType(self) -> PlcRule.Type:
        """
        Getter for property: ( PlcRule.Type NXOp) ParameterRuleType
         Returns the Select Parameter  
            
         
        """
        pass
    @ParameterRuleType.setter
    def ParameterRuleType(self, type: PlcRule.Type):
        """
        Setter for property: ( PlcRule.Type NXOp) ParameterRuleType
         Returns the Select Parameter  
            
         
        """
        pass
    @property
    def Port(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) Port
         Returns the Object Selection for Global Variable  
            
         
        """
        pass
    @property
    def RuleName(self) -> str:
        """
        Getter for property: (str) RuleName
         Returns the rule name   
            
         
        """
        pass
    @RuleName.setter
    def RuleName(self, ruleName: str):
        """
        Setter for property: (str) RuleName
         Returns the rule name   
            
         
        """
        pass
    def CreateParameter(self, parameterType: OperatorRuleBuilder.ParameterType, atIndex: int) -> NXOpen.NXObject:
        """
         Create new parameter
         Returns ruleParam ( NXOpen.NXObject): .
        """
        pass
    def DeleteParameter(self, parameterType: OperatorRuleBuilder.ParameterType, index: int) -> None:
        """
         Deletes parameter
        """
        pass
    def MoveParameter(self, parameterType: OperatorRuleBuilder.ParameterType, moveFromIndex: int, moveToIndex: int) -> None:
        """
         Move existing parameter
        """
        pass
    def UpdateParameter(self, parameterType: OperatorRuleBuilder.ParameterType, index: int) -> NXOpen.NXObject:
        """
         Update existing parameter
         Returns ruleParam ( NXOpen.NXObject): .
        """
        pass
import NXOpen
class OpticalAnnotationSettingsBuilder(NXOpen.Builder): 
    """ JA class for the Optical Annotation Settings dialog"""
    class AnnotationAttrType(Enum):
        """
        Members Include: 
         |SourceTarget| 
         |FiberType| 
         |CoreDiameter| 
         |CladdingDiameter| 
         |ObjectName| 
         |CutLength| 

        """
        SourceTarget: int
        FiberType: int
        CoreDiameter: int
        CladdingDiameter: int
        ObjectName: int
        CutLength: int
        @staticmethod
        def ValueOf(value: int) -> OpticalAnnotationSettingsBuilder.AnnotationAttrType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAnnotationAttributes(self, fiberType: AmeOpticalConnectionFiberType) -> List[OpticalAnnotationSettingsBuilder.AnnotationAttrType]:
        """
         The annotation attributes for a given fiber type.
         Returns annotationAttrs ( OpticalAnnotationSettingsBuilder.AnnotationAttrType List[NX):  User needs to free this memory.
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Reset to default. 
        """
        pass
    def SetAnnotationAttributes(self, fiberType: AmeOpticalConnectionFiberType, annotationAttrs: List[OpticalAnnotationSettingsBuilder.AnnotationAttrType]) -> None:
        """
         
        """
        pass
import NXOpen
class OpticalConnectionSettingsBuilder(NXOpen.Builder): 
    """ Builder object for changing optical connection settings on diagramming pages associated with the NXOpen.AME.Project """
    @property
    def SelectedBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectedBaseDefinition
         Returns the selection base definition  
            
         
        """
        pass
    def GetCladdingDiameter(self, fiberType: AmeOpticalConnectionFiberType) -> float:
        """
         Fiber cladding diameter property of a given optical connection sub-type. 
         Returns claddingDiameter (float): .
        """
        pass
    def GetCoreDiameter(self, fiberType: AmeOpticalConnectionFiberType) -> float:
        """
         Fiber core diameter property of a given optical connection sub-type. 
         Returns coreDiameter (float): .
        """
        pass
    def GetDefaultConnectionProduct(self, fiberType: AmeOpticalConnectionFiberType) -> ProductDefinition:
        """
         Get assigned connection product for provided connection subtype in Connection Project Settings
         Returns prodDef ( ProductDefinition NXOp): .
        """
        pass
    def GetStyleColorCode(self, fiberType: AmeOpticalConnectionFiberType) -> NXOpen.NXColor:
        """
         Style color code property of a given optical connection sub-type. 
         Returns styleColorCode ( NXOpen.NXColor): .
        """
        pass
    def GetStyleFont(self, fiberType: AmeOpticalConnectionFiberType) -> NXOpen.DisplayableObject.ObjectFont:
        """
         Style font property of a given optical connection sub-type. 
         Returns styleFont ( NXOpen.DisplayableObject.ObjectFont): .
        """
        pass
    def GetStyleWidth(self, fiberType: AmeOpticalConnectionFiberType) -> NXOpen.DisplayableObject.ObjectWidth:
        """
         Style width property of a given optical connection sub-type. 
         Returns styleWidth ( NXOpen.DisplayableObject.ObjectWidth): .
        """
        pass
    def RemoveConnectionProductAssignment(self, fiberType: AmeOpticalConnectionFiberType) -> None:
        """
         Remove the assigned product from provided connection subtype 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets optical connection settings to default 
        """
        pass
    def SetCladdingDiameter(self, fiberType: AmeOpticalConnectionFiberType, claddingDiameter: float) -> None:
        """
          
        """
        pass
    def SetCoreDiameter(self, fiberType: AmeOpticalConnectionFiberType, coreDiameter: float) -> None:
        """
          
        """
        pass
    def SetDefaultConnectionProduct(self, fiberType: AmeOpticalConnectionFiberType, prodDef: ProductDefinition) -> None:
        """
         Assign selected connection product 
        """
        pass
    def SetStyleColor(self, fiberType: AmeOpticalConnectionFiberType, styleColorCode: NXOpen.NXColor) -> None:
        """
          
        """
        pass
    def SetStyleFont(self, fiberType: AmeOpticalConnectionFiberType, styleFont: NXOpen.DisplayableObject.ObjectFont) -> None:
        """
          
        """
        pass
    def SetStyleWidth(self, fiberType: AmeOpticalConnectionFiberType, styleWidth: NXOpen.DisplayableObject.ObjectWidth) -> None:
        """
          
        """
        pass
    def ValidateMatchingRules(self, potentialTypeValue: str, propertyToValidate: str, prodDef: ProductDefinition) -> bool:
        """
         Validate matching rules for selected connection product 
         Returns isMatched (bool): .
        """
        pass
import NXOpen
class OrderAspectsBuilder(NXOpen.Builder): 
    """
    Represents a OrderAspectsBuilder for changing the order of Navigator
    """
    class OrderType(Enum):
        """
        Members Include: 
         |EngineeringObjects| 
         |Tag| 
         |Channel| 
         |UpstreamObjects| 
         |Page| 
         |Fragment| 
         |DocumentStructureNode| 
         |ProductComponentCore| 
         |ProductComponentBundle| 
         |ProductComponent| 
         |ConnectorNode| 
         |ProductMemoryArea| 
         |ProductTag| 
         |Product2dsymbolMultilineNode| 
         |Product2dsymbolSinglelineNode| 
         |Product2dsymbolBusTopologyNode| 
         |Product2dsymbolPowerTopologyNode| 
         |Product2dsymbolGenericNode| 
         |Product3dmodelNode| 
         |ProductTemplateLinkNode| 
         |EngineeringObjectsWithNoProduct| 
         |SymbolVariantNode| 
         |InterruptionPoint| 
         |TagTable| 

        """
        EngineeringObjects: int
        Tag: int
        Channel: int
        UpstreamObjects: int
        Page: int
        Fragment: int
        DocumentStructureNode: int
        ProductComponentCore: int
        ProductComponentBundle: int
        ProductComponent: int
        ConnectorNode: int
        ProductMemoryArea: int
        ProductTag: int
        Product2dsymbolMultilineNode: int
        Product2dsymbolSinglelineNode: int
        Product2dsymbolBusTopologyNode: int
        Product2dsymbolPowerTopologyNode: int
        Product2dsymbolGenericNode: int
        Product3dmodelNode: int
        ProductTemplateLinkNode: int
        EngineeringObjectsWithNoProduct: int
        SymbolVariantNode: int
        InterruptionPoint: int
        TagTable: int
        @staticmethod
        def ValueOf(value: int) -> OrderAspectsBuilder.OrderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SortType(Enum):
        """
        Members Include: 
         |SortbyCreation| 
         |SortbyName| 

        """
        SortbyCreation: int
        SortbyName: int
        @staticmethod
        def ValueOf(value: int) -> OrderAspectsBuilder.SortType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SortFunctionMode(self) -> OrderAspectsBuilder.SortType:
        """
        Getter for property: ( OrderAspectsBuilder.SortType NXOp) SortFunctionMode
         Returns   
            
         
        """
        pass
    @SortFunctionMode.setter
    def SortFunctionMode(self, sort: OrderAspectsBuilder.SortType):
        """
        Setter for property: ( OrderAspectsBuilder.SortType NXOp) SortFunctionMode
         Returns   
            
         
        """
        pass
    @property
    def SortLocationMode(self) -> OrderAspectsBuilder.SortType:
        """
        Getter for property: ( OrderAspectsBuilder.SortType NXOp) SortLocationMode
         Returns   
            
         
        """
        pass
    @SortLocationMode.setter
    def SortLocationMode(self, sort: OrderAspectsBuilder.SortType):
        """
        Setter for property: ( OrderAspectsBuilder.SortType NXOp) SortLocationMode
         Returns   
            
         
        """
        pass
    @property
    def SortProductMode(self) -> OrderAspectsBuilder.SortType:
        """
        Getter for property: ( OrderAspectsBuilder.SortType NXOp) SortProductMode
         Returns   
            
         
        """
        pass
    @SortProductMode.setter
    def SortProductMode(self, sort: OrderAspectsBuilder.SortType):
        """
        Setter for property: ( OrderAspectsBuilder.SortType NXOp) SortProductMode
         Returns   
            
         
        """
        pass
    def GetOrder(self) -> List[OrderAspectsBuilder.OrderType]:
        """
         The order for the aspects 
         Returns order ( OrderAspectsBuilder.OrderType List[NX):  .
        """
        pass
    def SetOrder(self, index: int, order: OrderAspectsBuilder.OrderType) -> None:
        """
         The order for the aspects 
        """
        pass
import NXOpen
class PageAttributeHolder(NXOpen.NXObject): 
    """ Page Object Atributes Holder"""
    pass
class PageBuilder(EngineeringObjectBaseBuilder): 
    """ Represents a Page creation class Builder  """
    class Types(Enum):
        """
        Members Include: 
         |AspectStructureOverview| 
         |CableDiagram| 
         |CableList| 
         |OrderList| 
         |PartListBom| 
         |PlugList| 
         |TableOfContent| 
         |TerminalDiagram| 
         |TerminalStripList| 
         |TitlePage| 
         |WireTubeConnectionLists| 
         |WireList| 
         |MultiLineSchematics| 
         |SingleLineSchematics| 
         |NetworkTopology| 
         |PowerSupplyTopology| 
         |ViewPage| 
         |FluidicDiagram| 
         |CabinetLayout| 
         |SummarizeBom| 

        """
        AspectStructureOverview: int
        CableDiagram: int
        CableList: int
        OrderList: int
        PartListBom: int
        PlugList: int
        TableOfContent: int
        TerminalDiagram: int
        TerminalStripList: int
        TitlePage: int
        WireTubeConnectionLists: int
        WireList: int
        MultiLineSchematics: int
        SingleLineSchematics: int
        NetworkTopology: int
        PowerSupplyTopology: int
        ViewPage: int
        FluidicDiagram: int
        CabinetLayout: int
        SummarizeBom: int
        @staticmethod
        def ValueOf(value: int) -> PageBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Aspects(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) Aspects
         Returns the Page aspect details  
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the Page description  
            
         
        """
        pass
    @Description.setter
    def Description(self, pageDescription: str):
        """
        Setter for property: (str) Description
         Returns the Page description  
            
         
        """
        pass
    @property
    def PageAttributeHolder(self) -> PageAttributeHolder:
        """
        Getter for property: ( PageAttributeHolder NXOp) PageAttributeHolder
         Returns the attribute holder   
            
         
        """
        pass
    @property
    def PageName(self) -> str:
        """
        Getter for property: (str) PageName
         Returns the Page name  
            
         
        """
        pass
    @PageName.setter
    def PageName(self, pageName: str):
        """
        Setter for property: (str) PageName
         Returns the Page name  
            
         
        """
        pass
    @property
    def Type(self) -> PageBuilder.Types:
        """
        Getter for property: ( PageBuilder.Types NXOp) Type
         Returns the Page type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: PageBuilder.Types):
        """
        Setter for property: ( PageBuilder.Types NXOp) Type
         Returns the Page type   
            
         
        """
        pass
    def SetClassificationCode(self, dccString: str) -> None:
        """
         Set user Classification Code. 
        """
        pass
    def SetDefaultClassificationCode(self) -> None:
        """
         Set default Classification Code. 
        """
        pass
import NXOpen
class PageNamingBuilder(NXOpen.Builder): 
    """ Class to define Page naming schema """
    @property
    def DisplayDigits(self) -> int:
        """
        Getter for property: (int) DisplayDigits
         Returns the Display Digits   
            
         
        """
        pass
    @DisplayDigits.setter
    def DisplayDigits(self, displayDigits: int):
        """
        Setter for property: (int) DisplayDigits
         Returns the Display Digits   
            
         
        """
        pass
    @property
    def Increment(self) -> int:
        """
        Getter for property: (int) Increment
         Returns the increment   
            
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: int):
        """
        Setter for property: (int) Increment
         Returns the increment   
            
         
        """
        pass
    @property
    def Start(self) -> int:
        """
        Getter for property: (int) Start
         Returns the start name  
            
         
        """
        pass
    @Start.setter
    def Start(self, start: int):
        """
        Setter for property: (int) Start
         Returns the start name  
            
         
        """
        pass
    @property
    def TargetSelection(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) TargetSelection
         Returns the Target node selection   
            
         
        """
        pass
class PageNode(AMEBaseNode): 
    """ Represents a Page Node """
    pass
class PageObject(AMEEngObject): 
    """ Represents a Page Object """
    pass
class PageTypes(Enum):
    """
    Members Include: 
     |AspectStructureOverview| 
     |CableDiagram| 
     |CableList| 
     |OrderList| 
     |PartListBom| 
     |PlugList| 
     |TableOfContent| 
     |TerminalDiagram| 
     |TerminalStripList| 
     |TitlePage| 
     |WireTubeConnectionLists| 
     |WireList| 
     |MultiLineSchematics| 
     |SingleLineSchematics| 
     |NetworkTopology| 
     |PowerSupplyTopology| 
     |ViewPage| 
     |FluidicDiagram| 
     |CabinetLayout| 
     |SummarizeBom| 

    """
    AspectStructureOverview: int
    CableDiagram: int
    CableList: int
    OrderList: int
    PartListBom: int
    PlugList: int
    TableOfContent: int
    TerminalDiagram: int
    TerminalStripList: int
    TitlePage: int
    WireTubeConnectionLists: int
    WireList: int
    MultiLineSchematics: int
    SingleLineSchematics: int
    NetworkTopology: int
    PowerSupplyTopology: int
    ViewPage: int
    FluidicDiagram: int
    CabinetLayout: int
    SummarizeBom: int
    @staticmethod
    def ValueOf(value: int) -> PageTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ParameterRuleBuilder(NXOpen.Builder): 
    """ JA class for the parameter rule dialog"""
    @property
    def ConnectionType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) ConnectionType
         Returns the connection type  
            
         
        """
        pass
    @ConnectionType.setter
    def ConnectionType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) ConnectionType
         Returns the connection type  
            
         
        """
        pass
    @property
    def ObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ObjectConnection
         Returns the object connection ui block  
            
         
        """
        pass
    @property
    def ObjectConnectionDetail(self) -> ObjectConnectionDetailBuilder:
        """
        Getter for property: ( ObjectConnectionDetailBuilder NXOp) ObjectConnectionDetail
         Returns the object connection detail ui block  
            
         
        """
        pass
    @property
    def SelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) SelectionPort
         Returns the eo any port selection   
            
         
        """
        pass
    def UpdateConnectionDetail(self, port: NXOpen.NXObject, propertyPath: str) -> None:
        """
         Update embedded connection detail comp
        """
        pass
    def UpdateConnectionDetails(self, ports: List[NXOpen.NXObject], propertyPath: str) -> None:
        """
         Update embedded connection detail comp with multi objects
        """
        pass
class ParentEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the parent object for a given aspect and a starting point """
    @property
    def AspectSelection(self) -> BaseEvaluatorBuilder.ContextType:
        """
        Getter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @AspectSelection.setter
    def AspectSelection(self, aspectSelection: BaseEvaluatorBuilder.ContextType):
        """
        Setter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
class PhysicalConnectionBuilder(MultipleObjectsBuilder): 
    """ JA class for creating Connection"""
    def SetBendPoints(self, p2dBendPoints: List[NXOpen.Point2d]) -> None:
        """
         Set Connection's Bend Points. 
        """
        pass
    def SetOwningSheet(self, owningSheet: NXOpen.Diagramming.Sheet) -> None:
        """
         Set connection's owning sheet 
        """
        pass
    def SetSourcePort(self, sourcePort: NXOpen.Diagramming.Port) -> None:
        """
         Set connection's source port 
        """
        pass
    def SetTargetPort(self, targetPort: NXOpen.Diagramming.Port) -> None:
        """
         Set connection's target port 
        """
        pass
import NXOpen
class PlaceAutomationBuilder(NXOpen.Builder): 
    """ Reassign a single aspect of an Engineering Object """
    @property
    def SelectionObjects(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectionObjects
         Returns the selection of objects to be reassigned   
            
         
        """
        pass
    @property
    def SelectionParent(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectionParent
         Returns the selection where the object will be reassigned.  
             
         
        """
        pass
import NXOpen
class PlcAddressRuleSetupBuilder(NXOpen.Builder): 
    """  """
    def SetPlcAddressRuleSetMap(self, propertyName: str, propertyValue: str) -> None:
        """
         Set the symbol properties
        """
        pass
class PlcAddressRuleSet(AMEExtendedObject): 
    """ Plc Address Rule Set Journaling class """
    pass
class PlcBlock(AMEBaseNode): 
    """ Plc Block Node Journaling class """
    def RemoveInterfaceMember(self, interfaceMember: MultiValueObjectsPort) -> None:
        """
         Remove a interface member port from the given block if the port is not used in other interfaces 
        """
        pass
    def RemoveMethod(self, node: PlcMethod) -> None:
        """
         Remove a method on the given block
        """
        pass
    def RemovePosition(self, node: PlcCodePosition) -> None:
        """
         Remove a rule position on the given block
        """
        pass
    def UpdateRules(self) -> None:
        """
         Update all rules
        """
        pass
import NXOpen
import NXOpen.Tooling
class PlcChangeInstanceBlockMasterBuilder(NXOpen.Builder): 
    """ This class provides a journalling interface for editing an Instance Data Block source
        revision.
    """
    @property
    def LibraryItemSelection(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) LibraryItemSelection
         Returns the library revision selection builder  
            
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
class PlcChartManager(NXOpen.Object): 
    """ Represents an object that manages sheet elements. """
    def AddPinToPlcLogicBlockOperator(selectedNode: NXOpen.Diagramming.Node) -> None:
        """
         Add Pin to Plc Logic Block Operator
        """
        pass
    def CreatePlcLogicBlockConnection(sheet: NXOpen.Diagramming.Sheet, targetPort: NXOpen.Diagramming.Port, connection: NXOpen.Diagramming.Connection, connectionEndType: int) -> None:
        """
         Create Plc Logic Block Connection
        """
        pass
    def CreatePlcLogicBlockOperand(sheet: NXOpen.Diagramming.Sheet, locationX: float, locationY: float, operandType: PlcLogicBlockNodeType) -> NXOpen.Diagramming.Node:
        """
         Create Plc Logic Block Operand
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def DeletePlcLogicBlockPin(selectedPort: NXOpen.Diagramming.Port) -> None:
        """
         Delete Input Pin of Plc Logic Block Operator
        """
        pass
    def DeletePlcLogicBlockPins(selectedPorts: List[NXOpen.Diagramming.Port]) -> None:
        """
         Delete multiple Input Pins of Plc Logic Block Operator
        """
        pass
    def GetDiagramSheetOfChartBlock(selectedNode: AMEExtendedObject) -> NXOpen.Diagramming.Sheet:
        """
         Get diagram sheet for chart code block
         Returns sheet ( NXOpen.Diagramming.Sheet): .
        """
        pass
    def NegatePlcLogicBlockPin(selectedPort: NXOpen.Diagramming.Port) -> None:
        """
         Negate Pin of Plc Logic Block Operator or Operand
        """
        pass
import NXOpen
class PlcCodePosition(NXOpen.NXObject): 
    """ Represents Plc Code Position Object """
    pass
class PlcDataTypeSource(Enum):
    """
    Members Include: 
     |Standard| 
     |UdtProject| 
     |UdtLibrary| 
     |UdtName| 
     |Struct| 
     |Unknown| 
     |Array| 

    """
    Standard: int
    UdtProject: int
    UdtLibrary: int
    UdtName: int
    Struct: int
    Unknown: int
    Array: int
    @staticmethod
    def ValueOf(value: int) -> PlcDataTypeSource:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PlcDataType(Enum):
    """
    Members Include: 
     |Db| 
     |Fb| 
     |Fc| 
     |BlockDb| 
     |BlockFb| 
     |BlockFc| 
     |BlockSdb| 
     |BlockSfb| 
     |BlockSfc| 
     |BlockOb| 
     |Bool| 
     |Byte| 
     |Char| 
     |Counter| 
     |Date| 
     |Dint| 
     |Dword| 
     |Int| 
     |Real| 
     |S5time| 
     |Time| 
     |TimeOfDay| 
     |Timer| 
     |Word| 
     |AomIdent| 
     |ConnAny| 
     |ConnOuc| 
     |ConnPrg| 
     |ConnRId| 
     |DbAny| 
     |DbDyn| 
     |DbWww| 
     |EventAny| 
     |EventAtt| 
     |EventHwint| 
     |HwAny| 
     |HwDevice| 
     |HwDpmaster| 
     |HwDpslave| 
     |HwHsc| 
     |HwIeport| 
     |HwInterface| 
     |HwIo| 
     |HwIosystem| 
     |HwModule| 
     |HwPto| 
     |HwPwm| 
     |HwSubmodule| 
     |Ldt| 
     |Lint| 
     |Lreal| 
     |Ltime| 
     |LtimeOfDay| 
     |Lword| 
     |ObAny| 
     |ObAtt| 
     |ObCyclic| 
     |ObDelay| 
     |ObDiag| 
     |ObHwint| 
     |ObPcycle| 
     |ObStartup| 
     |ObTimeerror| 
     |ObTod| 
     |Pip| 
     |Port| 
     |Rtm| 
     |Sint| 
     |Udint| 
     |Uint| 
     |Ulint| 
     |Usint| 
     |Wchar| 
     |Dtl| 
     |Wstring| 
     |Errorstruct| 
     |IecCounter| 
     |IecDcounter| 
     |IecLcounter| 
     |IecLtimer| 
     |IecScounter| 
     |IecTimer| 
     |IecUcounter| 
     |IecUdcounter| 
     |IecUlcounter| 
     |IecUscounter| 
     |Cref| 
     |Nref| 
     |Vref| 
     |HscPeriod| 
     |TaddrParam| 
     |SslHeader| 
     |Conditions| 
     |TconParam| 
     |DateAndTime| 
     |String| 
     |Udt| 
     |Any| 
     |Struct| 
     |Array| 
     |Ob| 
     |Variant| 
     |Undefined| 
     |Unknown| 

    """
    Db: int
    Fb: int
    Fc: int
    BlockDb: int
    BlockFb: int
    BlockFc: int
    BlockSdb: int
    BlockSfb: int
    BlockSfc: int
    BlockOb: int
    Bool: int
    Byte: int
    Char: int
    Counter: int
    Date: int
    Dint: int
    Dword: int
    Int: int
    Real: int
    S5time: int
    Time: int
    TimeOfDay: int
    Timer: int
    Word: int
    AomIdent: int
    ConnAny: int
    ConnOuc: int
    ConnPrg: int
    ConnRId: int
    DbAny: int
    DbDyn: int
    DbWww: int
    EventAny: int
    EventAtt: int
    EventHwint: int
    HwAny: int
    HwDevice: int
    HwDpmaster: int
    HwDpslave: int
    HwHsc: int
    HwIeport: int
    HwInterface: int
    HwIo: int
    HwIosystem: int
    HwModule: int
    HwPto: int
    HwPwm: int
    HwSubmodule: int
    Ldt: int
    Lint: int
    Lreal: int
    Ltime: int
    LtimeOfDay: int
    Lword: int
    ObAny: int
    ObAtt: int
    ObCyclic: int
    ObDelay: int
    ObDiag: int
    ObHwint: int
    ObPcycle: int
    ObStartup: int
    ObTimeerror: int
    ObTod: int
    Pip: int
    Port: int
    Rtm: int
    Sint: int
    Udint: int
    Uint: int
    Ulint: int
    Usint: int
    Wchar: int
    Dtl: int
    Wstring: int
    Errorstruct: int
    IecCounter: int
    IecDcounter: int
    IecLcounter: int
    IecLtimer: int
    IecScounter: int
    IecTimer: int
    IecUcounter: int
    IecUdcounter: int
    IecUlcounter: int
    IecUscounter: int
    Cref: int
    Nref: int
    Vref: int
    HscPeriod: int
    TaddrParam: int
    SslHeader: int
    Conditions: int
    TconParam: int
    DateAndTime: int
    String: int
    Udt: int
    Any: int
    Struct: int
    Array: int
    Ob: int
    Variant: int
    Undefined: int
    Unknown: int
    @staticmethod
    def ValueOf(value: int) -> PlcDataType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PlcEditStateNoteBuilder(AMEBaseBuilder): 
    """ Represents builder for AME::DB::PlcStateChartBaseElement """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the state or transition name   
            
         
        """
        pass
    @Name.setter
    def Name(self, resultText: str):
        """
        Setter for property: (str) Name
         Returns the state or transition name   
            
         
        """
        pass
import NXOpen
class PlcFlowChartConstantTextBuilder(NXOpen.Builder): 
    """ JA class for the constant text rule"""
    @property
    def ConstantText(self) -> str:
        """
        Getter for property: (str) ConstantText
         Returns the constanttext name   
            
         
        """
        pass
    @ConstantText.setter
    def ConstantText(self, resultText: str):
        """
        Setter for property: (str) ConstantText
         Returns the constanttext name   
            
         
        """
        pass
class PlcFlowChartNodeType(Enum):
    """
    Members Include: 
     |Invalid| 
     |Idb| 
     |Fc| 
     |Fci| 
     |And| 
     |Or| 
     |Not| 
     |Equal| 
     |Lessthan| 
     |Greaterthan| 
     |Lessthanequal| 
     |Greaterthanequal| 
     |Add| 
     |Sub| 
     |Read| 
     |Write| 
     |Readwrite| 

    """
    Invalid: int
    Idb: int
    Fc: int
    Fci: int
    And: int
    Or: int
    Not: int
    Equal: int
    Lessthan: int
    Greaterthan: int
    Lessthanequal: int
    Greaterthanequal: int
    Add: int
    Sub: int
    Read: int
    Write: int
    Readwrite: int
    @staticmethod
    def ValueOf(value: int) -> PlcFlowChartNodeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class PlcFlowChartOperatorBuilder(AMEBaseBuilder): 
    """ Represents builder for the Plc FlowChart Operator Object """
    class Input(Enum):
        """
        Members Include: 
         |Calculate| 
         |Compare| 
         |Logical| 

        """
        Calculate: int
        Compare: int
        Logical: int
        @staticmethod
        def ValueOf(value: int) -> PlcFlowChartOperatorBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def NumberOfInputs(self) -> int:
        """
        Getter for property: (int) NumberOfInputs
         Returns the number of inputs for the operator  
            
         
        """
        pass
    @NumberOfInputs.setter
    def NumberOfInputs(self, numberofInputs: int):
        """
        Setter for property: (int) NumberOfInputs
         Returns the number of inputs for the operator  
            
         
        """
        pass
    @property
    def SubOperatorType(self) -> PlcFlowChartNodeType:
        """
        Getter for property: ( PlcFlowChartNodeType NXOp) SubOperatorType
         Returns the operator type for flow chart   
            
         
        """
        pass
    @SubOperatorType.setter
    def SubOperatorType(self, operatorType: PlcFlowChartNodeType):
        """
        Setter for property: ( PlcFlowChartNodeType NXOp) SubOperatorType
         Returns the operator type for flow chart   
            
         
        """
        pass
    def CreateOperatorNode(self) -> NXOpen.Diagramming.Node:
        """
         Method to create the Operator Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetPlacementLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set node location of operator on the sheet. 
        """
        pass
import NXOpen
class PlcFunctionBlockBuilder(NXOpen.Builder): 
    """ PlcFunctionBlockBuilder class to create builder object. """
    @property
    def AspectDetails(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) AspectDetails
         Returns the aspect detail ui block  
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the function block description from ui block  
            
         
        """
        pass
    @Description.setter
    def Description(self, resultText: str):
        """
        Setter for property: (str) Description
         Returns the function block description from ui block  
            
         
        """
        pass
    @property
    def LanguageSelection(self) -> PlcFunctionBlockType:
        """
        Getter for property: ( PlcFunctionBlockType NXOp) LanguageSelection
         Returns the aspect detail ui block  
            
         
        """
        pass
    @LanguageSelection.setter
    def LanguageSelection(self, type: PlcFunctionBlockType):
        """
        Setter for property: ( PlcFunctionBlockType NXOp) LanguageSelection
         Returns the aspect detail ui block  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the aspect detail ui block  
            
         
        """
        pass
    @Name.setter
    def Name(self, resultText: str):
        """
        Setter for property: (str) Name
         Returns the aspect detail ui block  
            
         
        """
        pass
class PlcFunctionBlockType(Enum):
    """
    Members Include: 
     |StateChart| 
     |FlowChart| 
     |End| 

    """
    StateChart: int
    FlowChart: int
    End: int
    @staticmethod
    def ValueOf(value: int) -> PlcFunctionBlockType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PlcInterfaceSectionType(Enum):
    """
    Members Include: 
     |Input| 
     |Output| 
     |Inout| 
     |Static| 
     |Temp| 
     |Const| 
     |Return| 
     |NotSet| 
     |Unknown| 

    """
    Input: int
    Output: int
    Inout: int
    Static: int
    Temp: int
    Const: int
    Return: int
    NotSet: int
    Unknown: int
    @staticmethod
    def ValueOf(value: int) -> PlcInterfaceSectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PlcInterfaceSection(AMEBaseNode): 
    """ Represents PlcInterfaceSection """
    pass
class PlcInterfaceVariableBuilder(BulkEngineeringObjectBuilder): 
    """ PlcInterfaceVariableBuilder class will be used for (bulk) variable object creation and editing """
    @property
    def Array(self) -> bool:
        """
        Getter for property: (bool) Array
         Returns the Array type builder   
            
         
        """
        pass
    @Array.setter
    def Array(self, isArray: bool):
        """
        Setter for property: (bool) Array
         Returns the Array type builder   
            
         
        """
        pass
    @property
    def DataTypeComp(self) -> DataTypeBuilder:
        """
        Getter for property: ( DataTypeBuilder NXOp) DataTypeComp
         Returns the object data type builder  
            
         
        """
        pass
class PlcInterfaceVariable(AMEBaseNode): 
    """ Represents PlcInterfaceVariable """
    def RemoveInterfaceMember(self, variableMember: InterfaceMemberPort) -> None:
        """
         Remove a overridden interface member port value from the variable 
        """
        pass
class PlcLogicBlockNodeType(Enum):
    """
    Members Include: 
     |Invalid| 
     |And| 
     |Or| 
     |Read| 
     |Write| 

    """
    Invalid: int
    And: int
    Or: int
    Read: int
    Write: int
    @staticmethod
    def ValueOf(value: int) -> PlcLogicBlockNodeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class PlcLogicBlockOperand(NXOpen.NXObject): 
    """ Represents a PlcLogicBlockOperand """
    def AssignParameter(self, selectedParameter: IPlcParameter) -> None:
        """
         Assigns parameter to the operand
        """
        pass
    def SetSubvariableStructure(self, subVariablePath: List[str]) -> None:
        """
         Sets the sub-variable structure
        """
        pass
    def UnassignParameter(self) -> None:
        """
         Unassigns parameter from the operand
        """
        pass
class PlcLogicBlockParameter(MultiValueObjectsPort): 
    """ Represents an PlcLogicBlockParameter """
    pass
class PlcLogicBlock(AMEBaseNode): 
    """ Represents a PlcLogicBlock """
    pass
import NXOpen
class PlcMemoryAreaBuilder(NXOpen.Builder): 
    """ Represents a Subnet creation class Builder """
    @property
    def DataLengthBit(self) -> int:
        """
        Getter for property: (int) DataLengthBit
         Returns the DataLengthBit   
            
         
        """
        pass
    @DataLengthBit.setter
    def DataLengthBit(self, dataLengthBit: int):
        """
        Setter for property: (int) DataLengthBit
         Returns the DataLengthBit   
            
         
        """
        pass
    @property
    def DataLengthByte(self) -> int:
        """
        Getter for property: (int) DataLengthByte
         Returns the DataLengthByte   
            
         
        """
        pass
    @DataLengthByte.setter
    def DataLengthByte(self, dataLengthByte: int):
        """
        Setter for property: (int) DataLengthByte
         Returns the DataLengthByte   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the Description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the Description   
            
         
        """
        pass
    @property
    def IOType(self) -> str:
        """
        Getter for property: (str) IOType
         Returns the IOType   
            
         
        """
        pass
    @IOType.setter
    def IOType(self, ioType: str):
        """
        Setter for property: (str) IOType
         Returns the IOType   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the Name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the Name   
            
         
        """
        pass
    @property
    def StartAddress(self) -> int:
        """
        Getter for property: (int) StartAddress
         Returns the StartAddress   
            
         
        """
        pass
    @StartAddress.setter
    def StartAddress(self, startAddress: int):
        """
        Setter for property: (int) StartAddress
         Returns the StartAddress   
            
         
        """
        pass
class PlcMemoryArea(AMEBaseNode): 
    """ Plc Memory Area journaling class """
    def SetIndex(self, index: int) -> None:
        """
         Set index of memory area 
        """
        pass
    def SetSortIndex(self, sortIndex: int) -> None:
        """
         Set Sort Index of memory area 
        """
        pass
    def SetTelegramLength(self, length: int) -> None:
        """
         Set length of telegram 
        """
        pass
import NXOpen
class PlcMethodBuilder(NXOpen.Builder): 
    """ The Journalling class for PlcMethodBuilder"""
    class ParameterLevelType(Enum):
        """
        Members Include: 
         |All| 
         |First| 
         |Second| 
         |Third| 

        """
        All: int
        First: int
        Second: int
        Third: int
        @staticmethod
        def ValueOf(value: int) -> PlcMethodBuilder.ParameterLevelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InsertOnCreate(self) -> bool:
        """
        Getter for property: (bool) InsertOnCreate
         Returns the automatic insertion setting   
            
         
        """
        pass
    @InsertOnCreate.setter
    def InsertOnCreate(self, insertOnCreate: bool):
        """
        Setter for property: (bool) InsertOnCreate
         Returns the automatic insertion setting   
            
         
        """
        pass
    @property
    def Method(self) -> PlcMethod:
        """
        Getter for property: ( PlcMethod NXOp) Method
         Returns the method  
            
         
        """
        pass
    @property
    def MethodName(self) -> str:
        """
        Getter for property: (str) MethodName
         Returns the codedata block name   
            
         
        """
        pass
    @MethodName.setter
    def MethodName(self, name: str):
        """
        Setter for property: (str) MethodName
         Returns the codedata block name   
            
         
        """
        pass
    @property
    def ParameterLevel(self) -> PlcMethodBuilder.ParameterLevelType:
        """
        Getter for property: ( PlcMethodBuilder.ParameterLevelType NXOp) ParameterLevel
         Returns the level of the created or assigned parameter   
            
         
        """
        pass
    @ParameterLevel.setter
    def ParameterLevel(self, parameterLevel: PlcMethodBuilder.ParameterLevelType):
        """
        Setter for property: ( PlcMethodBuilder.ParameterLevelType NXOp) ParameterLevel
         Returns the level of the created or assigned parameter   
            
         
        """
        pass
    def AddCompileUnitIndex(self, idx: int) -> None:
        """
         Add a index of network that will be in a method
                with this function is possible to add several network  
        """
        pass
    def AddStatementIndexes(self, compileUnitIndex: int, startStatementIndex: int, endStatementIndex: int) -> None:
        """
         Add a index of start statment in a network and index of end of statment 
        """
        pass
    def AssignSoftwareGeneratableObjectToParameter(self, compileUnitIndex: int, statementLineIndex: int, statementLineInnerIndex: int, obj: NXOpen.NXObject) -> int:
        """
         Assign parameter to operand 
         Returns resultValue (int): .
        """
        pass
    def ChangeSubVariable(self, position: PlcCodePosition, subVariablePath: List[str]) -> None:
        """
         Change subvariable of method parameter 
        """
        pass
    def ClearCompileUnitIndexCountAndStatementIndexCount(self) -> None:
        """
         Clear the number of statments and networks which are saved to creating a method 
        """
        pass
    def CreateAndAssignParameter(self, compileUnitIndex: int, statementLineIndex: int, statementLineInnerIndex: int) -> NXOpen.NXObject:
        """
         Create and assigns a parameter. 
         Returns createdParameter ( NXOpen.NXObject): .
        """
        pass
    def CreateMethod(self) -> None:
        """
         To Create Method 
        """
        pass
    @overload
    def CreateParameter(self) -> NXOpen.NXObject:
        """
         Create a parameter 
         Returns obj ( NXOpen.NXObject): .
        """
        pass
    @overload
    def CreateParameter(self, parameterName: str) -> NXOpen.NXObject:
        """
         Create a parameter by a given  name 
         Returns obj ( NXOpen.NXObject): .
        """
        pass
    def CreateParametersByExternalRelation(self, swGenerationPort: PlcSoftwareGenPort) -> List[NXOpen.NXObject]:
        """
         Creates one ore more parameters by a given external relation port 
         Returns createdParameters ( NXOpen.NXObject Li): .
        """
        pass
    def DeleteParameter(self, obj: NXOpen.NXObject) -> None:
        """
         Delete Parameter 
        """
        pass
    def DeletePlcMethod(self) -> None:
        """
         To Delete Method 
        """
        pass
    def DeletePosition(self, position: NXOpen.NXObject) -> None:
        """
         Delete a position 
        """
        pass
    def DoesMethodNameAlreadyExist(self, methodName: str) -> int:
        """
         To find out that the given for method name already exist or not 
         Returns resultValue (int): .
        """
        pass
    def GetALLParameters(self) -> List[NXOpen.NXObject]:
        """
         Gets all existing parameter 
         Returns parameters ( NXOpen.NXObject Li): .
        """
        pass
    def GetSelectedCompileUnitIndexCount(self) -> int:
        """
         Get selected compileUnitIndex size 
         Returns resultValue (int): .
        """
        pass
    def SetNewParameterDataType(self, obj: NXOpen.NXObject, newDataType: str) -> int:
        """
         Set new data type to a parameter 
         Returns resultValue (int): .
        """
        pass
    def SetNewParameterName(self, obj: NXOpen.NXObject, newName: str) -> int:
        """
         Set new name to a parameter 
         Returns resultValue (int): .
        """
        pass
    def SetPlcCodeBlock(self, plcBlock: PlcBlock) -> None:
        """
         Set selected PlcCodeBlock 
        """
        pass
class PlcMethod(AMEExtendedObject): 
    """ Plc Method Node Journaling class """
    def ChangeMethodName(self, text: str) -> None:
        """
         Change the name of a PlcMethod
        """
        pass
class PlcRule(AMEBaseNode): 
    """ PlcRule Journaling class """
    class RefObjectType(Enum):
        """
        Members Include: 
         |Statement| 
         |Compileunit| 
         |Operand| 
         |StatementUnit| 
         |NotSet| 

        """
        Statement: int
        Compileunit: int
        Operand: int
        StatementUnit: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PlcRule.RefObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReplacementType(Enum):
        """
        Members Include: 
         |Replace| 
         |Insert| 
         |NotSet| 

        """
        Replace: int
        Insert: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PlcRule.ReplacementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |SymbolicReference| 
         |ConstantValue| 
         |Variable| 
         |LocalValue| 
         |LocalVariable| 
         |ConstantText| 
         |Call| 
         |SystemGlobalCall| 
         |SystemLocalCall| 
         |SystemFunctionCall| 
         |UserLocalCall| 
         |Method| 
         |PlaceholderVariable| 
         |PlaceholderSymbolicReference| 
         |PlaceholderConstantValue| 
         |OperatorAnd| 
         |OperatorOr| 
         |Iterative| 
         |Network| 
         |Parameter| 
         |OperatorNot| 
         |OperatorAdd| 
         |OperatorSubtract| 
         |OperatorEqual| 
         |OperatorLessThan| 
         |OperatorLessThanEqualTo| 
         |OperatorGreaterThan| 
         |OperatorGreaterThanEqualTo| 
         |NotSet| 
         |LogicBlock| 
         |HwModuleVariable| 
         |PlaceholderHwModuleVariable| 
         |SystemGlobalInstance| 
         |SystemLocalInstance| 

        """
        SymbolicReference: int
        ConstantValue: int
        Variable: int
        LocalValue: int
        LocalVariable: int
        ConstantText: int
        Call: int
        SystemGlobalCall: int
        SystemLocalCall: int
        SystemFunctionCall: int
        UserLocalCall: int
        Method: int
        PlaceholderVariable: int
        PlaceholderSymbolicReference: int
        PlaceholderConstantValue: int
        OperatorAnd: int
        OperatorOr: int
        Iterative: int
        Network: int
        Parameter: int
        OperatorNot: int
        OperatorAdd: int
        OperatorSubtract: int
        OperatorEqual: int
        OperatorLessThan: int
        OperatorLessThanEqualTo: int
        OperatorGreaterThan: int
        OperatorGreaterThanEqualTo: int
        NotSet: int
        LogicBlock: int
        HwModuleVariable: int
        PlaceholderHwModuleVariable: int
        SystemGlobalInstance: int
        SystemLocalInstance: int
        @staticmethod
        def ValueOf(value: int) -> PlcRule.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
class PlcSoftwareGenPort(AMEPort): 
    """ PlcSoftwareGenPort Journaling class """
    pass
class PlcStateChartActionBuilder(AMEBaseBuilder): 
    """ Represents builder for AME::UI::PlcStateChartAction """
    class ActionType(Enum):
        """
        Members Include: 
         |Entry| 
         |Doactivity| 
         |Exit| 

        """
        Entry: int
        Doactivity: int
        Exit: int
        @staticmethod
        def ValueOf(value: int) -> PlcStateChartActionBuilder.ActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MoveAction(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 

        """
        Up: int
        Down: int
        @staticmethod
        def ValueOf(value: int) -> PlcStateChartActionBuilder.MoveAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OperatorType(Enum):
        """
        Members Include: 
         |Assign| 
         |Add| 
         |Sub| 
         |Multiply| 
         |Divide| 
         |Equal| 
         |Between| 
         |Lessthan| 
         |Greaterthan| 
         |Lessthanequal| 
         |Greaterthanequal| 
         |And| 
         |Or| 

        """
        Assign: int
        Add: int
        Sub: int
        Multiply: int
        Divide: int
        Equal: int
        Between: int
        Lessthan: int
        Greaterthan: int
        Lessthanequal: int
        Greaterthanequal: int
        And: int
        Or: int
        @staticmethod
        def ValueOf(value: int) -> PlcStateChartActionBuilder.OperatorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QualifierType(Enum):
        """
        Members Include: 
         |N| 
         |S| 
         |R| 

        """
        N: int
        S: int
        R: int
        @staticmethod
        def ValueOf(value: int) -> PlcStateChartActionBuilder.QualifierType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddOperandValue(self, operandItem: AMEExtendedObject) -> None:
        """
         Add the action rule to Action Value
        """
        pass
    def AddQualifier(self) -> None:
        """
         Add a qualifier to state with default type as N 
        """
        pass
    def ChangeOperatorType(self, operatorItem: AMEExtendedObject, operatorType: PlcStateChartActionBuilder.OperatorType) -> None:
        """
         Set the operator type on operator item
        """
        pass
    def ChangeQualifierType(self, qualifier: AMEExtendedObject, qualifierType: PlcStateChartActionBuilder.QualifierType) -> None:
        """
         Set the qualifier type on actio item
        """
        pass
    def InsertOperand(self, qualifier: AMEExtendedObject) -> None:
        """
         Add a new operand to the qualifier N
        """
        pass
    def InsertOperator(self, operand: AMEExtendedObject) -> None:
        """
         Add a new operator
        """
        pass
    def MoveActionItem(self, actionItem: AMEExtendedObject, moveDirection: PlcStateChartActionBuilder.MoveAction) -> None:
        """
         Move the action Item 
        """
        pass
    def RemoveActionItem(self, conditionItem: AMEExtendedObject) -> None:
        """
         Remove action item 
        """
        pass
    def ResetActionValue(self, actionOperand: AMEExtendedObject) -> None:
        """
         Reset the operand value 
        """
        pass
    def SetOperandValueWithConstantText(self, operandItem: AMEExtendedObject, textValue: str) -> None:
        """
         Set the constant text value to the condition rule
        """
        pass
import NXOpen
class PlcStateChartCreateElementBuilder(AMEBaseBuilder): 
    """ Represents builder for the plc state chart element creation from the PlcBlockContent toolbar"""
    def SetPlacementLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set location on the sheet to create the element. 
        """
        pass
class PlcStateChartDefineCallBuilder(AMEBaseBuilder): 
    """ Represents builder for AME::UI::PlcStateChartDefineCall """
    @property
    def CurrentParameterRuleType(self) -> PlcRule.Type:
        """
        Getter for property: ( PlcRule.Type NXOp) CurrentParameterRuleType
         Returns the rule type of selected parameter  
            
         
        """
        pass
    @CurrentParameterRuleType.setter
    def CurrentParameterRuleType(self, type: PlcRule.Type):
        """
        Setter for property: ( PlcRule.Type NXOp) CurrentParameterRuleType
         Returns the rule type of selected parameter  
            
         
        """
        pass
    @property
    def ObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ObjectConnection
         Returns the object connection ui block  
            
         
        """
        pass
    @property
    def ObjectConnectionDetail(self) -> ObjectConnectionDetailBuilder:
        """
        Getter for property: ( ObjectConnectionDetailBuilder NXOp) ObjectConnectionDetail
         Returns the object connection detail ui block  
            
         
        """
        pass
    @property
    def ParameterObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ParameterObjectConnection
         Returns the parameter object connection ui block  
            
         
        """
        pass
    @property
    def ParameterSelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) ParameterSelectionPort
         Returns the parameter port selection   
            
         
        """
        pass
    @property
    def ParameterSelectionType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) ParameterSelectionType
         Returns the external object selection type  
            
         
        """
        pass
    @ParameterSelectionType.setter
    def ParameterSelectionType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) ParameterSelectionType
         Returns the external object selection type  
            
         
        """
        pass
    @property
    def ParameterText(self) -> str:
        """
        Getter for property: (str) ParameterText
         Returns the constantText of a parameter   
            
         
        """
        pass
    @ParameterText.setter
    def ParameterText(self, resultText: str):
        """
        Setter for property: (str) ParameterText
         Returns the constantText of a parameter   
            
         
        """
        pass
    @property
    def SelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) SelectionPort
         Returns the port selection   
            
         
        """
        pass
    def RefreshContent(self, paramOwnerId: str, paramName: str) -> None:
        """
         Update the builder of the reuse blocks
        """
        pass
    def UpdateSelectedParameter(self, paramOwnerId: str, paramName: str) -> None:
        """
         Update the selected parameter
        """
        pass
import NXOpen
class PlcStateChartFunctionBlockBuilder(NXOpen.Builder): 
    """ PlcStateChartFunctionBlockBuilder class to create builder object. """
    @property
    def AspectDetails(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) AspectDetails
         Returns the aspect detail ui block  
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the function block description from ui block  
            
         
        """
        pass
    @Description.setter
    def Description(self, resultText: str):
        """
        Setter for property: (str) Description
         Returns the function block description from ui block  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the aspect detail ui block  
            
         
        """
        pass
    @Name.setter
    def Name(self, resultText: str):
        """
        Setter for property: (str) Name
         Returns the aspect detail ui block  
            
         
        """
        pass
import NXOpen
class PlcStateChartItemValueBuilder(NXOpen.Builder): 
    """ JA class for the global variable rule"""
    @property
    def ConnectionType(self) -> ObjectConnectionBuilder.Type:
        """
        Getter for property: ( ObjectConnectionBuilder.Type NXOp) ConnectionType
         Returns the connection type  
            
         
        """
        pass
    @ConnectionType.setter
    def ConnectionType(self, type: ObjectConnectionBuilder.Type):
        """
        Setter for property: ( ObjectConnectionBuilder.Type NXOp) ConnectionType
         Returns the connection type  
            
         
        """
        pass
    @property
    def ObjectConnection(self) -> ObjectConnectionBuilder:
        """
        Getter for property: ( ObjectConnectionBuilder NXOp) ObjectConnection
         Returns the object connection ui block  
            
         
        """
        pass
    @property
    def ObjectConnectionDetail(self) -> ObjectConnectionDetailBuilder:
        """
        Getter for property: ( ObjectConnectionDetailBuilder NXOp) ObjectConnectionDetail
         Returns the object connection detail ui block  
            
         
        """
        pass
    @property
    def SelectionPort(self) -> SelectIPort:
        """
        Getter for property: ( SelectIPort NXOp) SelectionPort
         Returns the eo any port selection   
            
         
        """
        pass
    def UpdateConnectionDetail(self, port: NXOpen.NXObject, propertyPath: str) -> None:
        """
         Update embedded connection detail comp
        """
        pass
import NXOpen
class PlcStateChartStateBuilder(AMEBaseBuilder): 
    """ Represents builder for AME::DB::PlcStateChartState """
    @property
    def StateName(self) -> str:
        """
        Getter for property: (str) StateName
         Returns the state name   
            
         
        """
        pass
    @StateName.setter
    def StateName(self, resultText: str):
        """
        Setter for property: (str) StateName
         Returns the state name   
            
         
        """
        pass
    def SetStateLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set the location of the stATE on the PLC sheet 
        """
        pass
class PlcStateChartTransitionBuilder(AMEBaseBuilder): 
    """ Represents builder for AME::DB::PlcStateChartTransition """
    class MoveCondition(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 
         |Left| 
         |Right| 

        """
        Up: int
        Down: int
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> PlcStateChartTransitionBuilder.MoveCondition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EntryStateName(self) -> str:
        """
        Getter for property: (str) EntryStateName
         Returns the entry state name   
            
         
        """
        pass
    @EntryStateName.setter
    def EntryStateName(self, resultText: str):
        """
        Setter for property: (str) EntryStateName
         Returns the entry state name   
            
         
        """
        pass
    @property
    def ExitStateName(self) -> str:
        """
        Getter for property: (str) ExitStateName
         Returns the exit state name   
            
         
        """
        pass
    @ExitStateName.setter
    def ExitStateName(self, resultText: str):
        """
        Setter for property: (str) ExitStateName
         Returns the exit state name   
            
         
        """
        pass
    @property
    def TransitionName(self) -> str:
        """
        Getter for property: (str) TransitionName
         Returns the transition name   
            
         
        """
        pass
    @TransitionName.setter
    def TransitionName(self, resultText: str):
        """
        Setter for property: (str) TransitionName
         Returns the transition name   
            
         
        """
        pass
    def AddConditionValue(self, conditionItem: AMEExtendedObject) -> None:
        """
         Add the condition rule to the condition value
        """
        pass
    def AddRootConditionOperand(self) -> None:
        """
         Adds an operand as a root condition to the transition 
        """
        pass
    def AddRootConditionOperator(self) -> None:
        """
         Adds a root condition operator to the transition with default as AND type 
        """
        pass
    def AddSubConditionOperand(self, parentOperator: AMEExtendedObject, siblingOperand: AMEExtendedObject) -> AMEExtendedObject:
        """
         Adds a sub condition operand to the parent condition 
         Returns conditionValue ( AMEExtendedObject NXOp): .
        """
        pass
    def AddSubConditionOperator(self, parentOperator: AMEExtendedObject) -> None:
        """
         Adds a sub condition operator to the parent condition with default as AND type 
        """
        pass
    def ChangeConditionItemNegation(self, conditionItem: AMEExtendedObject, isNegation: bool) -> None:
        """
         Set the negation on the condition item
        """
        pass
    def ChangeConditionOperationType(self, conditionOperator: AMEExtendedObject, operatorType: AmePlcStatechartConditionOperatortype) -> None:
        """
         Set the operator type on the condition item
        """
        pass
    def MoveConditionItem(self, conditionItem: AMEExtendedObject, moveDirection: PlcStateChartTransitionBuilder.MoveCondition) -> None:
        """
         Move the condition Item 
        """
        pass
    def RemoveConditionItem(self, conditionItem: AMEExtendedObject) -> None:
        """
         Remove the condition value 
        """
        pass
    def ResetConditionValue(self, conditionItem: AMEExtendedObject) -> None:
        """
         Reset the condition value 
        """
        pass
    def SetConditionValueWithConstantText(self, conditionItem: AMEExtendedObject, textValue: str) -> None:
        """
         Set the constant text value to the condition rule
        """
        pass
class PlcStateChartTransitionPrioritiesBuilder(AMEBaseBuilder): 
    """ Represents builder for AME::PlcStateChartTransitionPrioritiesBuilder"""
    class Moving(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 

        """
        Up: int
        Down: int
        @staticmethod
        def ValueOf(value: int) -> PlcStateChartTransitionPrioritiesBuilder.Moving:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def UpdateTransitionPriorities(self, modifyingPriority: int, upOrDown: PlcStateChartTransitionPrioritiesBuilder.Moving) -> None:
        """
         Update the Priorities Of Outgoing transitions 
        """
        pass
class PlcSubFolder(AMEBaseNode): 
    """ Software Sub Folder Journaling class """
    pass
import NXOpen
import NXOpen.Tooling
class PlcSymbolBuilder(NXOpen.Builder): 
    """ Class to create Functional Tags and assign them to PLC Channels """
    @property
    def DataTypeComp(self) -> DataTypeBuilder:
        """
        Getter for property: ( DataTypeBuilder NXOp) DataTypeComp
         Returns the object data type builder  
            
         
        """
        pass
    @property
    def DataTypeSource(self) -> PlcDataTypeSource:
        """
        Getter for property: ( PlcDataTypeSource NXOp) DataTypeSource
         Returns the data type source   
            
         
        """
        pass
    @DataTypeSource.setter
    def DataTypeSource(self, dataTypeSource: PlcDataTypeSource):
        """
        Setter for property: ( PlcDataTypeSource NXOp) DataTypeSource
         Returns the data type source   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the string description   
            
         
        """
        pass
    @property
    def HWAddress(self) -> str:
        """
        Getter for property: (str) HWAddress
         Returns the string hwaddress   
            
         
        """
        pass
    @HWAddress.setter
    def HWAddress(self, hWAddress: str):
        """
        Setter for property: (str) HWAddress
         Returns the string hwaddress   
            
         
        """
        pass
    @property
    def HWAddressOffsetBit(self) -> int:
        """
        Getter for property: (int) HWAddressOffsetBit
         Returns the int hwaddress offset bit   
            
         
        """
        pass
    @HWAddressOffsetBit.setter
    def HWAddressOffsetBit(self, hWAddressOffsetBit: int):
        """
        Setter for property: (int) HWAddressOffsetBit
         Returns the int hwaddress offset bit   
            
         
        """
        pass
    @property
    def HWAddressOffsetByte(self) -> int:
        """
        Getter for property: (int) HWAddressOffsetByte
         Returns the int hwaddress offset byte   
            
         
        """
        pass
    @HWAddressOffsetByte.setter
    def HWAddressOffsetByte(self, hWAddress: int):
        """
        Setter for property: (int) HWAddressOffsetByte
         Returns the int hwaddress offset byte   
            
         
        """
        pass
    @property
    def Indicator(self) -> str:
        """
        Getter for property: (str) Indicator
         Returns the string indicator   
            
         
        """
        pass
    @Indicator.setter
    def Indicator(self, indicator: str):
        """
        Setter for property: (str) Indicator
         Returns the string indicator   
            
         
        """
        pass
    @property
    def MemorySection(self) -> MemorySectionType:
        """
        Getter for property: ( MemorySectionType NXOp) MemorySection
         Returns the enum io type   
            
         
        """
        pass
    @MemorySection.setter
    def MemorySection(self, memorySectionType: MemorySectionType):
        """
        Setter for property: ( MemorySectionType NXOp) MemorySection
         Returns the enum io type   
            
         
        """
        pass
    @property
    def SelectedUDTFromLibrary(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedUDTFromLibrary
         Returns the library UDT selection  
            
         
        """
        pass
    @property
    def SelectionParentObject(self) -> SelectINodeObject:
        """
        Getter for property: ( SelectINodeObject NXOp) SelectionParentObject
         Returns the selection ParentObject (parent of the plc symbol)   
            
         
        """
        pass
    @property
    def SymbolName(self) -> str:
        """
        Getter for property: (str) SymbolName
         Returns the string symbol name   
            
         
        """
        pass
    @SymbolName.setter
    def SymbolName(self, symbolName: str):
        """
        Setter for property: (str) SymbolName
         Returns the string symbol name   
            
         
        """
        pass
    @property
    def UdtByName(self) -> str:
        """
        Getter for property: (str) UdtByName
         Returns the string udt by name data type   
            
         
        """
        pass
    @UdtByName.setter
    def UdtByName(self, udtByName: str):
        """
        Setter for property: (str) UdtByName
         Returns the string udt by name data type   
            
         
        """
        pass
    @property
    def UdtFromProject(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) UdtFromProject
         Returns the project UDT selection   
            
         
        """
        pass
    def GetDataType(self) -> PlcDataType:
        """
         Get data type 
         Returns dataType ( PlcDataType NXOp): .
        """
        pass
    def SetDataType(self, dataType: PlcDataType) -> None:
        """
         Set data type 
        """
        pass
class PlcSymbolsEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the PLC tags for a given aspect and a starting point """
    class FilterType(Enum):
        """
        Members Include: 
         |Tags| 
         |Idbs| 
         |FunctionBlocks| 
         |Functions| 
         |PageMacros| 
         |WindowMacros| 
         |CallerInstance| 
         |All| 
         |LocalVariable| 
         |Methods| 
         |LocalModules| 
         |PlcDataTypes| 

        """
        Tags: int
        Idbs: int
        FunctionBlocks: int
        Functions: int
        PageMacros: int
        WindowMacros: int
        CallerInstance: int
        All: int
        LocalVariable: int
        Methods: int
        LocalModules: int
        PlcDataTypes: int
        @staticmethod
        def ValueOf(value: int) -> PlcSymbolsEvaluatorBuilder.FilterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SearchCriteriaByHierarchy(Enum):
        """
        Members Include: 
         |All| 
         |Levels| 

        """
        All: int
        Levels: int
        @staticmethod
        def ValueOf(value: int) -> PlcSymbolsEvaluatorBuilder.SearchCriteriaByHierarchy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectSelection(self) -> BaseEvaluatorBuilder.ContextType:
        """
        Getter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @AspectSelection.setter
    def AspectSelection(self, aspectSelection: BaseEvaluatorBuilder.ContextType):
        """
        Setter for property: ( BaseEvaluatorBuilder.ContextType NXOp) AspectSelection
         Returns the aspect navigator selection type   
            
         
        """
        pass
    @property
    def DepthCriteria(self) -> PlcSymbolsEvaluatorBuilder.SearchCriteriaByHierarchy:
        """
        Getter for property: ( PlcSymbolsEvaluatorBuilder.SearchCriteriaByHierarchy NXOp) DepthCriteria
         Returns the depth criteria   
            
         
        """
        pass
    @DepthCriteria.setter
    def DepthCriteria(self, depthCriteria: PlcSymbolsEvaluatorBuilder.SearchCriteriaByHierarchy):
        """
        Setter for property: ( PlcSymbolsEvaluatorBuilder.SearchCriteriaByHierarchy NXOp) DepthCriteria
         Returns the depth criteria   
            
         
        """
        pass
    @property
    def NumLevels(self) -> int:
        """
        Getter for property: (int) NumLevels
         Returns the num of levels of hierarchies min 1 to max 100   
            
         
        """
        pass
    @NumLevels.setter
    def NumLevels(self, numLevels: int):
        """
        Setter for property: (int) NumLevels
         Returns the num of levels of hierarchies min 1 to max 100   
            
         
        """
        pass
    @property
    def TypeSelection(self) -> PlcSymbolsEvaluatorBuilder.FilterType:
        """
        Getter for property: ( PlcSymbolsEvaluatorBuilder.FilterType NXOp) TypeSelection
         Returns the type filter selection   
            
         
        """
        pass
    @TypeSelection.setter
    def TypeSelection(self, typeSelection: PlcSymbolsEvaluatorBuilder.FilterType):
        """
        Setter for property: ( PlcSymbolsEvaluatorBuilder.FilterType NXOp) TypeSelection
         Returns the type filter selection   
            
         
        """
        pass
    def GetFilterObjectsBuilder(self) -> FilterObjectsBuilder:
        """
         Returns the FilterObjectsBuilder 
         Returns filterBuilder ( FilterObjectsBuilder NXOp): .
        """
        pass
import NXOpen
import NXOpen.Tooling
class PlcTelegramBuilder(NXOpen.Builder): 
    """ something """
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns a selection of reuse library item   
            
         
        """
        pass
    @property
    def SendReceiveType(self) -> SendReceiveType:
        """
        Getter for property: ( SendReceiveType NXOp) SendReceiveType
         Returns an enum sendreceive type   
            
         
        """
        pass
    @SendReceiveType.setter
    def SendReceiveType(self, sendReceiveType: SendReceiveType):
        """
        Setter for property: ( SendReceiveType NXOp) SendReceiveType
         Returns an enum sendreceive type   
            
         
        """
        pass
    @property
    def TelegramType(self) -> TelegramType:
        """
        Getter for property: ( TelegramType NXOp) TelegramType
         Returns an enum telegram type   
            
         
        """
        pass
    @TelegramType.setter
    def TelegramType(self, telegramType: TelegramType):
        """
        Setter for property: ( TelegramType NXOp) TelegramType
         Returns an enum telegram type   
            
         
        """
        pass
    def SetConfigurationType(self, configType: str) -> None:
        """
         Sets Configuration Type 
        """
        pass
    def SetSelectedTelegram(self, selectedTelegram: PlcMemoryArea) -> None:
        """
         Selected Telegram 
        """
        pass
class PlcTelegramDefinition(BaseDefinition): 
    """ JA class for the PlcTelegram Definition object"""
    pass
import NXOpen
import NXOpen.Tooling
class PlcVendorSymbolBuilder(NXOpen.Builder): 
    """ Represents a Subnet creation class Builder """
    @property
    def AddressPostFix(self) -> str:
        """
        Getter for property: (str) AddressPostFix
         Returns the AddressPostFix   
            
         
        """
        pass
    @AddressPostFix.setter
    def AddressPostFix(self, postfix: str):
        """
        Setter for property: (str) AddressPostFix
         Returns the AddressPostFix   
            
         
        """
        pass
    @property
    def BitOffset(self) -> int:
        """
        Getter for property: (int) BitOffset
         Returns the bit   
            
         
        """
        pass
    @BitOffset.setter
    def BitOffset(self, bitOffset: int):
        """
        Setter for property: (int) BitOffset
         Returns the bit   
            
         
        """
        pass
    @property
    def ByteOffset(self) -> int:
        """
        Getter for property: (int) ByteOffset
         Returns the byte   
            
         
        """
        pass
    @ByteOffset.setter
    def ByteOffset(self, byteOffset: int):
        """
        Setter for property: (int) ByteOffset
         Returns the byte   
            
         
        """
        pass
    @property
    def DataType(self) -> PlcDataType:
        """
        Getter for property: ( PlcDataType NXOp) DataType
         Returns the type   
            
         
        """
        pass
    @DataType.setter
    def DataType(self, type: PlcDataType):
        """
        Setter for property: ( PlcDataType NXOp) DataType
         Returns the type   
            
         
        """
        pass
    @property
    def DataTypeSource(self) -> PlcDataTypeSource:
        """
        Getter for property: ( PlcDataTypeSource NXOp) DataTypeSource
         Returns the DataTypeSource   
            
         
        """
        pass
    @DataTypeSource.setter
    def DataTypeSource(self, dataTypeSource: PlcDataTypeSource):
        """
        Setter for property: ( PlcDataTypeSource NXOp) DataTypeSource
         Returns the DataTypeSource   
            
         
        """
        pass
    @property
    def EnumDataLength(self) -> int:
        """
        Getter for property: (int) EnumDataLength
         Returns the EnumDataLength   
            
         
        """
        pass
    @EnumDataLength.setter
    def EnumDataLength(self, enum01: int):
        """
        Setter for property: (int) EnumDataLength
         Returns the EnumDataLength   
            
         
        """
        pass
    @property
    def Indicator(self) -> str:
        """
        Getter for property: (str) Indicator
         Returns the Indicator   
            
         
        """
        pass
    @Indicator.setter
    def Indicator(self, indicator: str):
        """
        Setter for property: (str) Indicator
         Returns the Indicator   
            
         
        """
        pass
    @property
    def SelectedDataTypePosition(self) -> int:
        """
        Getter for property: (int) SelectedDataTypePosition
         Returnsthe  DataType   
            
         
        """
        pass
    @SelectedDataTypePosition.setter
    def SelectedDataTypePosition(self, dataTypePos: int):
        """
        Setter for property: (int) SelectedDataTypePosition
         Returnsthe  DataType   
            
         
        """
        pass
    @property
    def SelectedUDTFromLibrary(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedUDTFromLibrary
         Returns the library UDT selection  
            
         
        """
        pass
    @property
    def SelectionChannel(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectionChannel
         Returns the selection ParentObject (parent of the plc symbol)   
            
         
        """
        pass
    @property
    def ShowDataType(self) -> bool:
        """
        Getter for property: (bool) ShowDataType
         Returns the showDataType   
            
         
        """
        pass
    @ShowDataType.setter
    def ShowDataType(self, showDataType: bool):
        """
        Setter for property: (bool) ShowDataType
         Returns the showDataType   
            
         
        """
        pass
    @property
    def UdtByName(self) -> str:
        """
        Getter for property: (str) UdtByName
         Returns the string udt by name data type   
            
         
        """
        pass
    @UdtByName.setter
    def UdtByName(self, udtByName: str):
        """
        Setter for property: (str) UdtByName
         Returns the string udt by name data type   
            
         
        """
        pass
import NXOpen.Tooling
class PortBuilder(AMEBaseBuilder): 
    """ builder for the software block properties dialog"""
    class ConnectableAttrProxyObjectType(Enum):
        """
        Members Include: 
         |All| 
         |Library| 
         |Tag| 

        """
        All: int
        Library: int
        Tag: int
        @staticmethod
        def ValueOf(value: int) -> PortBuilder.ConnectableAttrProxyObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreationModeType(Enum):
        """
        Members Include: 
         |New| 
         |Library| 

        """
        New: int
        Library: int
        @staticmethod
        def ValueOf(value: int) -> PortBuilder.CreationModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |All| 
         |Caller| 
         |Operand| 
         |Method| 
         |Block| 

        """
        All: int
        Caller: int
        Operand: int
        Method: int
        Block: int
        @staticmethod
        def ValueOf(value: int) -> PortBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConnectableProxyObjectType(self) -> PortBuilder.ConnectableAttrProxyObjectType:
        """
        Getter for property: ( PortBuilder.ConnectableAttrProxyObjectType NXOp) ConnectableProxyObjectType
         Returns the connectable object type   
            
         
        """
        pass
    @ConnectableProxyObjectType.setter
    def ConnectableProxyObjectType(self, connectableAttrObjectType: PortBuilder.ConnectableAttrProxyObjectType):
        """
        Setter for property: ( PortBuilder.ConnectableAttrProxyObjectType NXOp) ConnectableProxyObjectType
         Returns the connectable object type   
            
         
        """
        pass
    @property
    def CreationMode(self) -> PortBuilder.CreationModeType:
        """
        Getter for property: ( PortBuilder.CreationModeType NXOp) CreationMode
         Returns the creation mode   
            
         
        """
        pass
    @CreationMode.setter
    def CreationMode(self, creationMode: PortBuilder.CreationModeType):
        """
        Setter for property: ( PortBuilder.CreationModeType NXOp) CreationMode
         Returns the creation mode   
            
         
        """
        pass
    @property
    def EngObjectType(self) -> SelectionEngineeringObjectDefinitionBuilder:
        """
        Getter for property: ( SelectionEngineeringObjectDefinitionBuilder NXOp) EngObjectType
         Returns the engineering object type   
            
         
        """
        pass
    @property
    def PortClassId(self) -> str:
        """
        Getter for property: (str) PortClassId
         Returns the classification id of port   
            
         
        """
        pass
    @PortClassId.setter
    def PortClassId(self, type: str):
        """
        Setter for property: (str) PortClassId
         Returns the classification id of port   
            
         
        """
        pass
    @property
    def PortName(self) -> str:
        """
        Getter for property: (str) PortName
         Returns the name of port   
            
         
        """
        pass
    @PortName.setter
    def PortName(self, portName: str):
        """
        Setter for property: (str) PortName
         Returns the name of port   
            
         
        """
        pass
    @property
    def PortType(self) -> str:
        """
        Getter for property: (str) PortType
         Returns the type of port   
            
         
        """
        pass
    @PortType.setter
    def PortType(self, type: str):
        """
        Setter for property: (str) PortType
         Returns the type of port   
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library item   
            
         
        """
        pass
    def SetPortCardinality(self, portCardinality: str) -> None:
        """
         Set the cardinality 
        """
        pass
    def SetPortDirection(self, portDirection: str) -> None:
        """
         Set the direction 
        """
        pass
import NXOpen
class PortConnectionBuilder(NXOpen.Builder): 
    """ builder for the port connector dialog"""
    @property
    def AutoLinked(self) -> bool:
        """
        Getter for property: (bool) AutoLinked
         Returns   
            
         
        """
        pass
    @AutoLinked.setter
    def AutoLinked(self, autoLinked: bool):
        """
        Setter for property: (bool) AutoLinked
         Returns   
            
         
        """
        pass
    @property
    def SelectedSourcePort(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectedSourcePort
         Returns the source port   
            
         
        """
        pass
    @overload
    def Disconnect(self, port1: NXOpen.NXObject, port2: NXOpen.NXObject) -> None:
        """
         Disconnects given ports each other
        """
        pass
    @overload
    def Disconnect(self, portToDisconnect: NXOpen.NXObject) -> None:
        """
         Disconnects given port
        """
        pass
    def SetTargetPorts(self, ports: List[NXOpen.NXObject]) -> None:
        """
         Sets ports to connect 
        """
        pass
class PortEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the port objects for the given port and a starting point """
    @property
    def Port(self) -> str:
        """
        Getter for property: (str) Port
         Returns the expression that will determine the port.  
             
         
        """
        pass
    @Port.setter
    def Port(self, port: str):
        """
        Setter for property: (str) Port
         Returns the expression that will determine the port.  
             
         
        """
        pass
import NXOpen
class PortsManagerBuilder(NXOpen.Builder): 
    """ Provides journal methods for the ports manager dialog. """
    def CreateConnections(self, source: NXOpen.NXObject) -> List[NXOpen.NXObject]:
        """
         Creates the connections 
         Returns ports ( NXOpen.NXObject Li): .
        """
        pass
    def Disconnect(self, port: NXOpen.NXObject) -> None:
        """
         Disconnects port 
        """
        pass
    def GetExpression(self) -> NXOpen.NXObject:
        """
         Gets the dynamic connection expression
         Returns exp ( NXOpen.NXObject): .
        """
        pass
    def SetExpression(self, exp: NXOpen.NXObject) -> None:
        """
         Sets the dynamic connection expression
        """
        pass
    def SetPort(self, exp: NXOpen.NXObject) -> None:
        """
         Sets the source port of the connection
        """
        pass
    def UpdateSelection(self, port: NXOpen.NXObject) -> None:
        """
         Updates the IPortsContainer selection 
        """
        pass
class PrimitiveSheetElementBuilderOfNoteAnchor(Enum):
    """
    Members Include: 
     |Invalid| 
     |NoValue| 
     |TopLeft| 
     |TopCenter| 
     |TopRight| 
     |MiddleLeft| 
     |MiddleCenter| 
     |MiddleRight| 
     |BottomLeft| 
     |BottomCenter| 
     |BottomRight| 

    """
    Invalid: int
    NoValue: int
    TopLeft: int
    TopCenter: int
    TopRight: int
    MiddleLeft: int
    MiddleCenter: int
    MiddleRight: int
    BottomLeft: int
    BottomCenter: int
    BottomRight: int
    @staticmethod
    def ValueOf(value: int) -> PrimitiveSheetElementBuilderOfNoteAnchor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PrimitiveSheetElementBuilderOfNoteLetteringangle(Enum):
    """
    Members Include: 
     |Invalid| 
     |NoValue| 
     |Degree0| 
     |Degree45| 
     |Degree90| 
     |Degree135| 
     |Degree180| 
     |Degree225| 
     |Degree270| 
     |Degree315| 

    """
    Invalid: int
    NoValue: int
    Degree0: int
    Degree45: int
    Degree90: int
    Degree135: int
    Degree180: int
    Degree225: int
    Degree270: int
    Degree315: int
    @staticmethod
    def ValueOf(value: int) -> PrimitiveSheetElementBuilderOfNoteLetteringangle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class PrimitiveSheetElementBuilder(NXOpen.Builder): 
    """ Represents builder for  Primitive Sheet Element """
    class PrimitiveType(Enum):
        """
        Members Include: 
         |Line| 
         |Circle| 
         |Rectangle| 
         |Image| 
         |Note| 

        """
        Line: int
        Circle: int
        Rectangle: int
        Image: int
        Note: int
        @staticmethod
        def ValueOf(value: int) -> PrimitiveSheetElementBuilder.PrimitiveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Anchor(self) -> PrimitiveSheetElementBuilderOfNoteAnchor:
        """
        Getter for property: ( PrimitiveSheetElementBuilderOfNoteAnchor NXOp) Anchor
         Returns the TextAnchor   
            
         
        """
        pass
    @Anchor.setter
    def Anchor(self, anchor: PrimitiveSheetElementBuilderOfNoteAnchor):
        """
        Setter for property: ( PrimitiveSheetElementBuilderOfNoteAnchor NXOp) Anchor
         Returns the TextAnchor   
            
         
        """
        pass
    @property
    def AnnotationBuilder(self) -> NXOpen.Diagramming.CannedAnnotationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.CannedAnnotationBuilder) AnnotationBuilder
         Returns the AnnotationBuilder.  
             
         
        """
        pass
    @AnnotationBuilder.setter
    def AnnotationBuilder(self, annotation: NXOpen.Diagramming.CannedAnnotationBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.CannedAnnotationBuilder) AnnotationBuilder
         Returns the AnnotationBuilder.  
             
         
        """
        pass
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the path of image file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the path of image file which is being imported   
            
         
        """
        pass
    @property
    def LetteringAngle(self) -> PrimitiveSheetElementBuilderOfNoteLetteringangle:
        """
        Getter for property: ( PrimitiveSheetElementBuilderOfNoteLetteringangle NXOp) LetteringAngle
         Returns the LetteringAngle   
            
         
        """
        pass
    @LetteringAngle.setter
    def LetteringAngle(self, letteringAngle: PrimitiveSheetElementBuilderOfNoteLetteringangle):
        """
        Setter for property: ( PrimitiveSheetElementBuilderOfNoteLetteringangle NXOp) LetteringAngle
         Returns the LetteringAngle   
            
         
        """
        pass
    @property
    def Type(self) -> PrimitiveSheetElementBuilder.PrimitiveType:
        """
        Getter for property: ( PrimitiveSheetElementBuilder.PrimitiveType NXOp) Type
         Returns the type of primitive   
            
         
        """
        pass
    @Type.setter
    def Type(self, primitiveType: PrimitiveSheetElementBuilder.PrimitiveType):
        """
        Setter for property: ( PrimitiveSheetElementBuilder.PrimitiveType NXOp) Type
         Returns the type of primitive   
            
         
        """
        pass
    def CreatePrimitiveSheetElement(self, pageObject: PageObject) -> NXOpen.Diagramming.SheetElement:
        """
         Method to create the Sheet Element 
         Returns sheetElement ( NXOpen.Diagramming.SheetElement): .
        """
        pass
    def SelectedNodesTag(self, selectedNodes: List[NXOpen.Diagramming.Annotation]) -> None:
        """
         The SelectedNodeTags 
        """
        pass
    def SetCompareData(self, styleName: List[str], changedValues: List[str], isStyleChanged: List[str]) -> None:
        """
         The Compare Data list 
        """
        pass
    def SetLocations(self, locations: List[NXOpen.Point2d]) -> None:
        """
         Set the locations on page. 
        """
        pass
    def SetStringTranslatable(self, stringTranslatable: bool) -> None:
        """
         The String Translatable 
        """
        pass
import NXOpen
class PrintPagesBuilder(NXOpen.Builder): 
    """ JA class for the PrintPages dialog"""
    @property
    def Copies(self) -> int:
        """
        Getter for property: (int) Copies
         Returns the number of copies.  
            This option specifies the number of copies to
                    be printed
                  
         
        """
        pass
    @Copies.setter
    def Copies(self, copies: int):
        """
        Setter for property: (int) Copies
         Returns the number of copies.  
            This option specifies the number of copies to
                    be printed
                  
         
        """
        pass
    @property
    def PdfFileName(self) -> str:
        """
        Getter for property: (str) PdfFileName
         Returns the pdf file name.  
            The pdfFileName field represents the full path  of the
                    pdf which the user wishes to create as output of print.
                  
         
        """
        pass
    @PdfFileName.setter
    def PdfFileName(self, pdfFileName: str):
        """
        Setter for property: (str) PdfFileName
         Returns the pdf file name.  
            The pdfFileName field represents the full path  of the
                    pdf which the user wishes to create as output of print.
                  
         
        """
        pass
    @property
    def PrinterText(self) -> str:
        """
        Getter for property: (str) PrinterText
         Returns the printer text.  
            The printer field represents the full path name of the
                    printer the user wishes to print to.
                  
         
        """
        pass
    @PrinterText.setter
    def PrinterText(self, printer: str):
        """
        Setter for property: (str) PrinterText
         Returns the printer text.  
            The printer field represents the full path name of the
                    printer the user wishes to print to.
                  
         
        """
        pass
    def AddSelectedPages(self, pages: List[NXOpen.NXObject]) -> None:
        """
         Set the pages to be printed.
        """
        pass
class ProductComponent(AMEBaseNode): 
    """ Product Component class """
    pass
import NXOpen
class ProductDefAttributeHolder(AttributeHolder): 
    """ ProductDefinition Atributes Holder Object """
    def SetProductdefinition(self, productDef: NXOpen.NXObject) -> None:
        """
         Set ProductDefinition 
        """
        pass
class ProductDefinition(BaseDefinition): 
    """ JA class for the Product Definition object"""
    def GetTypeDefinition(self) -> EngObjectDefinition:
        """
         Get Type 
         Returns type ( EngObjectDefinition NXOp): .
        """
        pass
class ProductMatchingRulesBuilder(AMEBaseBuilder): 
    """ Represents Product Matching Rules class builder """
    class Condition(Enum):
        """
        Members Include: 
         |ValueIsEqual|  used if conditon is "Value is equal" 
         |Match|  used if conditon is "Match" 

        """
        ValueIsEqual: int
        Match: int
        @staticmethod
        def ValueOf(value: int) -> ProductMatchingRulesBuilder.Condition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddNewRule(self, index: int, propertyName: str, condition: ProductMatchingRulesBuilder.Condition, deviceValue: str, productValue: str) -> None:
        """
         Add new product matching rule 
        """
        pass
import NXOpen
class ProductPropertyRulesBuilder(NXOpen.Builder): 
    """ Represents builder for creating product property merging rules"""
    class PropertyMergeOption(Enum):
        """
        Members Include: 
         |Invalid| 
         |Yes| 
         |No| 
         |OnlyIfEmpty| 

        """
        Invalid: int
        Yes: int
        No: int
        OnlyIfEmpty: int
        @staticmethod
        def ValueOf(value: int) -> ProductPropertyRulesBuilder.PropertyMergeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddProductPropertyRules(self, propertyName: str, assignAction: ProductPropertyRulesBuilder.PropertyMergeOption, removeAction: ProductPropertyRulesBuilder.PropertyMergeOption) -> None:
        """
         Add connection product property rule 
        """
        pass
    def ClearProductPropertyRules(self) -> None:
        """
         Clear connection product property rule 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets connection property value assignment to default 
        """
        pass
import NXOpen
class ProductSelectionBuilder(MultipleObjectsBuilder): 
    """ JA class for Product Selection dialog"""
    class Type(Enum):
        """
        Members Include: 
         |SameEngineeringObjectDefinition| 
         |SameClassificationAndMoreDetailedClassification| 
         |AllCommonProducts| 

        """
        SameEngineeringObjectDefinition: int
        SameClassificationAndMoreDetailedClassification: int
        AllCommonProducts: int
        @staticmethod
        def ValueOf(value: int) -> ProductSelectionBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BreakUnLockedTemplate(self) -> bool:
        """
        Getter for property: (bool) BreakUnLockedTemplate
         Returns the option to exchange product by breaking unlocked template  
            
         
        """
        pass
    @BreakUnLockedTemplate.setter
    def BreakUnLockedTemplate(self, breakUnLockedTemplate: bool):
        """
        Setter for property: (bool) BreakUnLockedTemplate
         Returns the option to exchange product by breaking unlocked template  
            
         
        """
        pass
    @property
    def ClearTiaTypeIdentifierInType(self) -> bool:
        """
        Getter for property: (bool) ClearTiaTypeIdentifierInType
         Returns the option to clear tia type identifier property  
            
         
        """
        pass
    @ClearTiaTypeIdentifierInType.setter
    def ClearTiaTypeIdentifierInType(self, clearTiaTypeIdentifierInType: bool):
        """
        Setter for property: (bool) ClearTiaTypeIdentifierInType
         Returns the option to clear tia type identifier property  
            
         
        """
        pass
    @property
    def ExchangePLCRelevantProduct(self) -> bool:
        """
        Getter for property: (bool) ExchangePLCRelevantProduct
         Returns the option to exchange plc relevant product  
            
         
        """
        pass
    @ExchangePLCRelevantProduct.setter
    def ExchangePLCRelevantProduct(self, exchangePLCRelevantProduct: bool):
        """
        Setter for property: (bool) ExchangePLCRelevantProduct
         Returns the option to exchange plc relevant product  
            
         
        """
        pass
    @property
    def ExchangeProductForNotLockedTemplate(self) -> bool:
        """
        Getter for property: (bool) ExchangeProductForNotLockedTemplate
         Returns the option to exchange product for device which are not members of locked template  
            
         
        """
        pass
    @ExchangeProductForNotLockedTemplate.setter
    def ExchangeProductForNotLockedTemplate(self, exchangeProductForNotLockedTemplate: bool):
        """
        Setter for property: (bool) ExchangeProductForNotLockedTemplate
         Returns the option to exchange product for device which are not members of locked template  
            
         
        """
        pass
    @property
    def PlaceInProductAspect(self) -> bool:
        """
        Getter for property: (bool) PlaceInProductAspect
         Returns the option to create product aspect for device if not available  
            
         
        """
        pass
    @PlaceInProductAspect.setter
    def PlaceInProductAspect(self, placeInProductAspect: bool):
        """
        Setter for property: (bool) PlaceInProductAspect
         Returns the option to create product aspect for device if not available  
            
         
        """
        pass
    @property
    def ProductType(self) -> ProductSelectionBuilder.Type:
        """
        Getter for property: ( ProductSelectionBuilder.Type NXOp) ProductType
         Returns the product type for product selection  
            
         
        """
        pass
    @ProductType.setter
    def ProductType(self, productType: ProductSelectionBuilder.Type):
        """
        Setter for property: ( ProductSelectionBuilder.Type NXOp) ProductType
         Returns the product type for product selection  
            
         
        """
        pass
    @property
    def RemovePLCRelevantProduct(self) -> bool:
        """
        Getter for property: (bool) RemovePLCRelevantProduct
         Returns the option to remove plc relevant product  
            
         
        """
        pass
    @RemovePLCRelevantProduct.setter
    def RemovePLCRelevantProduct(self, removePLCRelevantProduct: bool):
        """
        Setter for property: (bool) RemovePLCRelevantProduct
         Returns the option to remove plc relevant product  
            
         
        """
        pass
    @property
    def SelectClassification(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the selected classification   
            
         
        """
        pass
    @property
    def SelectedDevices(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedDevices
         Returns the selected devices   
            
         
        """
        pass
    def RemoveTiaLibraryReference(self, plcHwItem: AMEPlcHwItem) -> None:
        """
         Remove tia library reference of hwItem
        """
        pass
    def RemoveTiaLibraryReferenceFromEngObject(self, engObject: AMEEngObject) -> None:
        """
         Remove tia library reference of hwItem
        """
        pass
    def SetAuxiliaryProducts(self, auxiliaryProducts: List[ProductDefinition]) -> None:
        """
         Set auxiliary product details
        """
        pass
    def SetSelectedProduct(self, selectedProduct: ProductDefinition) -> None:
        """
         Set selected product
        """
        pass
class ProgrammingLanguage(Enum):
    """
    Members Include: 
     |Db| 
     |Stl| 
     |Lad| 
     |Fbd| 
     |Scl| 
     |Unknown| 

    """
    Db: int
    Stl: int
    Lad: int
    Fbd: int
    Scl: int
    Unknown: int
    @staticmethod
    def ValueOf(value: int) -> ProgrammingLanguage:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.Diagramming
import NXOpen.Tooling
class ProjectEngineeringObjectBuilder(EngineeringObjectBaseBuilder): 
    """ JA class for the insert Project Eng object dialog"""
    @property
    def AspectDetails(self) -> AspectDetailsBuilder:
        """
        Getter for property: ( AspectDetailsBuilder NXOp) AspectDetails
         Returns the aspect detail ui block  
            
         
        """
        pass
    @property
    def DiagramNodeBuilder(self) -> DiagramNodeBuilder:
        """
        Getter for property: ( DiagramNodeBuilder NXOp) DiagramNodeBuilder
         Returns the Node Builder used for creating Symbol for EO  
            
         
        """
        pass
    @property
    def EOAttributeHolder(self) -> EOAttributeHolder:
        """
        Getter for property: ( EOAttributeHolder NXOp) EOAttributeHolder
         Returns the container for definition holders   
            
         
        """
        pass
    @property
    def EoDefAttributeHolder(self) -> EODefAttributeHolder:
        """
        Getter for property: ( EODefAttributeHolder NXOp) EoDefAttributeHolder
         Returns the EO definition attribute holder   
            
         
        """
        pass
    @property
    def EoNameIndex(self) -> ObjectNameIndexBuilder:
        """
        Getter for property: ( ObjectNameIndexBuilder NXOp) EoNameIndex
         Returns the eo name index and description ui block  
            
         
        """
        pass
    @property
    def ProductDefAttributeHolder(self) -> ProductDefAttributeHolder:
        """
        Getter for property: ( ProductDefAttributeHolder NXOp) ProductDefAttributeHolder
         Returns the Product definition attribute holder   
            
         
        """
        pass
    @property
    def SelectMountingInterfaceLocation(self) -> SelectMountingInterfaceLocationBuilder:
        """
        Getter for property: ( SelectMountingInterfaceLocationBuilder NXOp) SelectMountingInterfaceLocation
         Returns the select mounting interface location builder   
            
         
        """
        pass
    @property
    def SelectSymbolDefinition(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectSymbolDefinition
         Returns the select eo symbol  
            
         
        """
        pass
    @property
    def SymbolPlacement(self) -> SymbolPlacementBuilder:
        """
        Getter for property: ( SymbolPlacementBuilder NXOp) SymbolPlacement
         Returns the symbol placement builder  
            
         
        """
        pass
    def ClearCreatedSymbol(self, isClearAllSymbols: bool) -> None:
        """
         Clear the created Symbol
        """
        pass
    def PreviewNodeLocation(self, owningPage: PageObject, locationX: float, locationY: float, isNodePlaced: bool, index: int) -> None:
        """
         The preview node location on page. 
        """
        pass
    def SetCreatedSymbol(self, owningPage: PageObject, symbolTag: NXOpen.Diagramming.Node, locationX: float, locationY: float) -> None:
        """
         Set the created Symbol
        """
        pass
    def SetObjectName(self, objectName: str) -> None:
        """
         Set the Object Name. 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class ProjectSymbolAnnotationBuilder(NXOpen.Builder): 
    """ JA class for the Project Symbol Annotation dialog"""
    @property
    def Anchor(self) -> AmeSymbolAnnotationAnchor:
        """
        Getter for property: ( AmeSymbolAnnotationAnchor NXOp) Anchor
         Returns the TextAnchor   
            
         
        """
        pass
    @Anchor.setter
    def Anchor(self, anchor: AmeSymbolAnnotationAnchor):
        """
        Setter for property: ( AmeSymbolAnnotationAnchor NXOp) Anchor
         Returns the TextAnchor   
            
         
        """
        pass
    @property
    def AnnotationBuilder(self) -> NXOpen.Diagramming.AnnotationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.AnnotationBuilder) AnnotationBuilder
         Returns the AnnotationBuilder.  
             
         
        """
        pass
    @property
    def Height(self) -> Height:
        """
        Getter for property: ( Height NXOp) Height
         Returns the TextHeight   
            
         
        """
        pass
    @Height.setter
    def Height(self, textHeight: Height):
        """
        Setter for property: ( Height NXOp) Height
         Returns the TextHeight   
            
         
        """
        pass
    @property
    def LetteringAngle(self) -> AmeSymbolAnnotationLetteringangle:
        """
        Getter for property: ( AmeSymbolAnnotationLetteringangle NXOp) LetteringAngle
         Returns the LetteringAngle   
            
         
        """
        pass
    @LetteringAngle.setter
    def LetteringAngle(self, letteringAngle: AmeSymbolAnnotationLetteringangle):
        """
        Setter for property: ( AmeSymbolAnnotationLetteringangle NXOp) LetteringAngle
         Returns the LetteringAngle   
            
         
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Reset to default 
        """
        pass
import NXOpen
class Project(NXOpen.NXObject): 
    """ Project Journaling class """
    def GenerateValueSetReport(self) -> None:
        """
         Method to generate value set report
        """
        pass
    def GetTemplateInstanceOfId(self, templateInstanceAndValueSetGoupId: str) -> NXOpen.NXObject:
        """
         Method to get Template Instance in Project from Template Instance Id
         Returns templateInstance ( NXOpen.NXObject): .
        """
        pass
    def GetTemplateVariants(self) -> List[NXOpen.NXObject]:
        """
         Method to get Template Variants in a Template Project
         Returns templateVariants ( NXOpen.NXObject Li): .
        """
        pass
    def GetValueSetGroup(self, templateInstanceAndValueSetGoupId: str, templateInstance: NXOpen.NXObject) -> NXOpen.NXObject:
        """
         Method to get Value Set Group Instance in given Template Instance
         Returns valueSetGroup ( NXOpen.NXObject): .
        """
        pass
    def GetValueSets(self) -> List[NXOpen.NXObject]:
        """
         Method to get Value Sets in a Template or Template Variant Project
         Returns valueSets ( NXOpen.NXObject Li): .
        """
        pass
class PropertyEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates the property of an object given a category and property """
    @property
    def CategoryName(self) -> str:
        """
        Getter for property: (str) CategoryName
         Returns the category name given by the user   
            
         
        """
        pass
    @CategoryName.setter
    def CategoryName(self, categoryName: str):
        """
        Setter for property: (str) CategoryName
         Returns the category name given by the user   
            
         
        """
        pass
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the property name given by the user   
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the property name given by the user   
            
         
        """
        pass
import NXOpen.Tooling
class QueryBuilder(AMEBaseBuilder): 
    """ Represents query class builder """
    class Types(Enum):
        """
        Members Include: 
         |NewQuery| 
         |FromLibrary| 

        """
        NewQuery: int
        FromLibrary: int
        @staticmethod
        def ValueOf(value: int) -> QueryBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreationType(self) -> QueryBuilder.Types:
        """
        Getter for property: ( QueryBuilder.Types NXOp) CreationType
         Returns the defined rule type   
            
         
        """
        pass
    @CreationType.setter
    def CreationType(self, type: QueryBuilder.Types):
        """
        Setter for property: ( QueryBuilder.Types NXOp) CreationType
         Returns the defined rule type   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the query description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the query description   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the query name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the query name   
            
         
        """
        pass
    @property
    def Parent(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) Parent
         Returns the parent node of query node  
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the public query   
            
         
        """
        pass
    def GetPublicQueryDescription(self) -> str:
        """
         The selected public query description
         Returns description (str): .
        """
        pass
    def GetPublicQueryName(self) -> str:
        """
         The selected public query name
         Returns name (str): .
        """
        pass
import NXOpen
class QueryClause(NXOpen.NXObject): 
    """ JA class for the QueryClause object"""
    pass
class QueryFolder(AMEBaseNode): 
    """ Query Folder Journaling class """
    pass
class QueryNode(AMEBaseNode): 
    """ The Query Node """
    pass
import NXOpen
class QueryResult(NXOpen.NXObject): 
    """ The Query Result """
    def GetRows(self) -> List[NXOpen.NXObject]:
        """
         Get sorted rows data
         Returns rows ( NXOpen.NXObject Li): .
        """
        pass
    def LoadAll(self) -> None:
        """
         Load all results. 
        """
        pass
    def LoadAndRetrieveConnections(self, selectedResultObjects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Load connections of selected query result objects
         Returns connections ( NXOpen.NXObject Li): .
        """
        pass
    def LoadAndRetrieveEngineeringObjects(self, selectedResultObjects: List[NXOpen.NXObject]) -> List[AMEEngObject]:
        """
         Load engineering objects of selected query result objects
         Returns engObjects ( AMEEngObject List[NX): .
        """
        pass
    def LoadAndRetrievePlcSymbols(self, selectedResultObjects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Load plc symbols of selected query result objects
         Returns plcSymbols ( NXOpen.NXObject Li): .
        """
        pass
    def LoadEngineeringObjectsFromModelIds(self, selectedModelIDs: List[str]) -> List[AMEEngObject]:
        """
         Load engineering objects of selected model IDs
         Returns engObjects ( AMEEngObject List[NX): .
        """
        pass
    def LoadPreview(self) -> None:
        """
         Load results according to number of results in query preview setting. 
        """
        pass
    def PopulateRows(self) -> None:
        """
         Populate sorted rows 
        """
        pass
class ReferenceDesignationSetNode(AMEBaseNode): 
    """ Reference Designation Set Node Journaling class """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class ReferenceObjectBuilder(NXOpen.TaggedObject): 
    """ Re-usable UI consist of a context and source selection """
    class SourceSelectionType(Enum):
        """
        Members Include: 
         |ContextObject| 
         |SelectObject| 
         |DetermineByExpression| 

        """
        ContextObject: int
        SelectObject: int
        DetermineByExpression: int
        @staticmethod
        def ValueOf(value: int) -> ReferenceObjectBuilder.SourceSelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContextObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ContextObject
         Returns the selection for the object where the evaluator will be stored.  
             
         
        """
        pass
    @property
    def SourceExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SourceExpression
         Returns the expression that will determine the source object.  
             
         
        """
        pass
    @SourceExpression.setter
    def SourceExpression(self, sourceExpression: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) SourceExpression
         Returns the expression that will determine the source object.  
             
         
        """
        pass
    @property
    def SourceObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SourceObject
         Returns the selection for the object where the evaluation will start.  
             
         
        """
        pass
    @property
    def SourceTypeSelection(self) -> ReferenceObjectBuilder.SourceSelectionType:
        """
        Getter for property: ( ReferenceObjectBuilder.SourceSelectionType NXOp) SourceTypeSelection
         Returns the selection type for the source object   
            
         
        """
        pass
    @SourceTypeSelection.setter
    def SourceTypeSelection(self, typeSelection: ReferenceObjectBuilder.SourceSelectionType):
        """
        Setter for property: ( ReferenceObjectBuilder.SourceSelectionType NXOp) SourceTypeSelection
         Returns the selection type for the source object   
            
         
        """
        pass
    def GetSourceExpressionPart(self) -> NXOpen.Part:
        """
         Gets the source expression part. 
         Returns sourceExpressionPart ( NXOpen.Part): .
        """
        pass
import NXOpen
class RenamePlugsAndStripsBuilder(NXOpen.Builder): 
    """ JA class for the Rename Plugs And Strips dialog"""
    @property
    def EnablePotential(self) -> bool:
        """
        Getter for property: (bool) EnablePotential
         Returns the bool value which determine to allow potential based renaming or not   
            
         
        """
        pass
    @EnablePotential.setter
    def EnablePotential(self, potential: bool):
        """
        Setter for property: (bool) EnablePotential
         Returns the bool value which determine to allow potential based renaming or not   
            
         
        """
        pass
    @property
    def IndexIncrement(self) -> int:
        """
        Getter for property: (int) IndexIncrement
         Returns the index increment   
            
         
        """
        pass
    @IndexIncrement.setter
    def IndexIncrement(self, indexIncrement: int):
        """
        Setter for property: (int) IndexIncrement
         Returns the index increment   
            
         
        """
        pass
    @property
    def Merge(self) -> bool:
        """
        Getter for property: (bool) Merge
         Returns the bool value which determine if characters are to be merged with sequence number for renaming   
            
         
        """
        pass
    @Merge.setter
    def Merge(self, merge: bool):
        """
        Setter for property: (bool) Merge
         Returns the bool value which determine if characters are to be merged with sequence number for renaming   
            
         
        """
        pass
    @property
    def SelectNode(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectNode
         Returns the select node for renaming plugs and strips in product aspect navigator   
            
         
        """
        pass
    @property
    def StartIndex(self) -> int:
        """
        Getter for property: (int) StartIndex
         Returns the start index   
            
         
        """
        pass
    @StartIndex.setter
    def StartIndex(self, startIndex: int):
        """
        Setter for property: (int) StartIndex
         Returns the start index   
            
         
        """
        pass
    def SetPotentialTypeList(self, rowStrings: List[str]) -> None:
        """
         The potential type list 
        """
        pass
import NXOpen.Tooling
class ReportDefinitionBuilder(AMEBaseBuilder): 
    """ Represents ReportDefinitionBuilder class builder """
    class Types(Enum):
        """
        Members Include: 
         |NewReportDefinition| 
         |FromLibrary| 

        """
        NewReportDefinition: int
        FromLibrary: int
        @staticmethod
        def ValueOf(value: int) -> ReportDefinitionBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreationType(self) -> ReportDefinitionBuilder.Types:
        """
        Getter for property: ( ReportDefinitionBuilder.Types NXOp) CreationType
         Returns the defined creation type   
            
         
        """
        pass
    @CreationType.setter
    def CreationType(self, type: ReportDefinitionBuilder.Types):
        """
        Setter for property: ( ReportDefinitionBuilder.Types NXOp) CreationType
         Returns the defined creation type   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the report definition description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the report definition description   
            
         
        """
        pass
    @property
    def FileBrowserText(self) -> str:
        """
        Getter for property: (str) FileBrowserText
         Returns the name of create report template    
            
         
        """
        pass
    @FileBrowserText.setter
    def FileBrowserText(self, name: str):
        """
        Setter for property: (str) FileBrowserText
         Returns the name of create report template    
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the report definition name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the report definition name   
            
         
        """
        pass
    @property
    def Parent(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) Parent
         Returns the parent node of report definition node  
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the public report definition   
            
         
        """
        pass
    def GetPublicReportDefinitionDescription(self) -> str:
        """
         The selected public report definition description
         Returns description (str): .
        """
        pass
    def GetPublicReportDefinitionName(self) -> str:
        """
         The selected public report definition name
         Returns name (str): .
        """
        pass
    def GetPublicReportDefinitionTemplate(self) -> str:
        """
         The selected public report definition template 
         Returns reportTemplate (str): .
        """
        pass
class ReportDefinitionFolder(AMEBaseNode): 
    """ Report Definition Journaling class """
    pass
class ReportDefinitionNode(AMEBaseNode): 
    """ The Report Definition Node """
    def GetReportDefinition(self) -> ReportDefinition:
        """
         Get report definition from report definition node
         Returns reportDef ( ReportDefinition NXOp): .
        """
        pass
import NXOpen
class ReportDefinition(AMEExtendedObject): 
    """ The Report Definition """
    def AddMergeRowsCriteria(self, propertyOf: str, category: str, propertyTitle: str) -> None:
        """
         Add Merge Criteria 
        """
        pass
    def AddPageBreakCriteria(self, propertyOf: str, category: str, propertyTitle: str, targetDirection: int) -> None:
        """
         Add Page Break Criteria 
        """
        pass
    def AddReportSortingCriteria(self, propertyOf: str, category: str, propertyTitle: str, sort: bool) -> None:
        """
         Add Sorting Criteria 
        """
        pass
    def ChangeReportTemplate(self, reportTemplateItemName: str) -> None:
        """
         Change report template 
        """
        pass
    def ClearMergeRowsCriteria(self) -> None:
        """
         Clear Merge Criteria 
        """
        pass
    def ClearPageBreakCriteria(self) -> None:
        """
         Clear PageBreak Criteria 
        """
        pass
    def ClearReportSortingCriteria(self) -> None:
        """
         Clear Sorting Criteria 
        """
        pass
    def EditSortingProperty(self, index: int, isAscending: bool) -> None:
        """
         Edit Sorting Property 
        """
        pass
    def GenerateReport(self) -> Tuple[NXOpen.NXObject, NXOpen.NXObject]:
        """
         Execute query and get engineering objects as result 
         Returns A tuple consisting of (pageObject, pageNode). 
         - pageObject is:  NXOpen.NXObject.
         - pageNode is:  NXOpen.NXObject.

        """
        pass
    def GenerateReportAndExportToExcel(self) -> None:
        """
         Generate report and export it to Excel 
        """
        pass
    def GetDescription(self) -> str:
        """
         Get description 
         Returns description (str): .
        """
        pass
    def GetName(self) -> str:
        """
         Get name 
         Returns name (str): .
        """
        pass
    def GetPageAttributeHolder(self) -> NXOpen.NXObject:
        """
         Get report page Attribute Holder 
         Returns reportPageAttributeHolder ( NXOpen.NXObject): .
        """
        pass
    def GetReportPage(self) -> NXOpen.NXObject:
        """
         Get report first page 
         Returns pageObject ( NXOpen.NXObject): .
        """
        pass
    def MoveSortingProperty(self, index: int, toBeMovedUp: bool) -> None:
        """
         Move Sorting Property 
        """
        pass
    def RemoveMergeRowsCriteria(self, index: int) -> None:
        """
         Remove Merge Property 
        """
        pass
    def RemovePageBreakCriteria(self, index: int) -> None:
        """
         Remove Page Break Criteria 
        """
        pass
    def RemoveSortingProperty(self, index: int) -> None:
        """
         Remove Sorting Property 
        """
        pass
    def SetDescription(self, description: str) -> None:
        """
         Set Description 
        """
        pass
    def SetName(self, name: str) -> None:
        """
         Set Name 
        """
        pass
    def UpdateReportTemplateRelation(self, oldReportTemplate: NXOpen.Part, newReportTemplate: NXOpen.Part, relationName: str) -> None:
        """
         Update report template relation
        """
        pass
import NXOpen
class ReportHeaderPlaceHolderDataNode(NXOpen.NXObject): 
    """ JA class for the ReportHeaderPlaceHolderDataNode object"""
    def RemoveRefCells(self) -> None:
        """
         Remove referencing cells 
        """
        pass
    def SetHeadPlaceholderDataNode(self, headNode: ReportPlaceHolderData) -> None:
        """
         Set head node of linked list 
        """
        pass
class ReportPageAttributeHolder(AMEExtendedObject): 
    """ JA class for the ReportPageAttributeHolder object"""
    pass
import NXOpen
class ReportPlaceHolderData(NXOpen.NXObject): 
    """ JA class for the ReportPlaceHolderData object"""
    def SetMatrixDirection(self, matrixDirection: int) -> None:
        """
         Set Matrix Direction
        """
        pass
    def SetNextNodePlaceholderData(self, nextNode: ReportPlaceHolderData) -> None:
        """
         Set node of linked list 
        """
        pass
    def UpdateDataOnPlaceholder(self, objectType: str, propertyName: str, category: str, propertyType: str, targetDirection: int) -> None:
        """
         Update PlaceholderData
        """
        pass
import NXOpen
class ReportSettingsBuilder(NXOpen.Builder): 
    """
        Implements the report settings dialog.
    """
    @property
    def MaxBridgeLevel(self) -> int:
        """
        Getter for property: (int) MaxBridgeLevel
         Returns the maxBridgesLevel   
            
         
        """
        pass
    @MaxBridgeLevel.setter
    def MaxBridgeLevel(self, maxBridgesLevel: int):
        """
        Setter for property: (int) MaxBridgeLevel
         Returns the maxBridgesLevel   
            
         
        """
        pass
    @property
    def MaxJumperLength(self) -> int:
        """
        Getter for property: (int) MaxJumperLength
         Returns the maxJumperLength   
            
         
        """
        pass
    @MaxJumperLength.setter
    def MaxJumperLength(self, maxJumperLength: int):
        """
        Setter for property: (int) MaxJumperLength
         Returns the maxJumperLength   
            
         
        """
        pass
    @property
    def MaxJumperLevel(self) -> int:
        """
        Getter for property: (int) MaxJumperLevel
         Returns the maxJumperLevel   
            
         
        """
        pass
    @MaxJumperLevel.setter
    def MaxJumperLevel(self, maxJumperLevel: int):
        """
        Setter for property: (int) MaxJumperLevel
         Returns the maxJumperLevel   
            
         
        """
        pass
    @property
    def SelectedReportDefinition(self) -> ReportDefinition:
        """
        Getter for property: ( ReportDefinition NXOp) SelectedReportDefinition
         Returns the selected report definition  
            
         
        """
        pass
    @SelectedReportDefinition.setter
    def SelectedReportDefinition(self, reportDefinition: ReportDefinition):
        """
        Setter for property: ( ReportDefinition NXOp) SelectedReportDefinition
         Returns the selected report definition  
            
         
        """
        pass
import NXOpen
class ReportsSettingsBuilder(NXOpen.Builder): 
    """ interface for the ReportsSettingsBuilder"""
    @property
    def FunctionAspect(self) -> bool:
        """
        Getter for property: (bool) FunctionAspect
         Returns the function aspect   
            
         
        """
        pass
    @FunctionAspect.setter
    def FunctionAspect(self, functionAspect: bool):
        """
        Setter for property: (bool) FunctionAspect
         Returns the function aspect   
            
         
        """
        pass
    @property
    def LocationAspect(self) -> bool:
        """
        Getter for property: (bool) LocationAspect
         Returns the location aspect   
            
         
        """
        pass
    @LocationAspect.setter
    def LocationAspect(self, locationAspect: bool):
        """
        Setter for property: (bool) LocationAspect
         Returns the location aspect   
            
         
        """
        pass
    @property
    def ProductAspect(self) -> bool:
        """
        Getter for property: (bool) ProductAspect
         Returns the product aspect   
            
         
        """
        pass
    @ProductAspect.setter
    def ProductAspect(self, productAspect: bool):
        """
        Setter for property: (bool) ProductAspect
         Returns the product aspect   
            
         
        """
        pass
    @property
    def ReportName(self) -> str:
        """
        Getter for property: (str) ReportName
         Returns the string report name   
            
         
        """
        pass
    @ReportName.setter
    def ReportName(self, reportName: str):
        """
        Setter for property: (str) ReportName
         Returns the string report name   
            
         
        """
        pass
    @property
    def ReportTemplateName(self) -> str:
        """
        Getter for property: (str) ReportTemplateName
         Returns the report template name   
            
         
        """
        pass
    @ReportTemplateName.setter
    def ReportTemplateName(self, reportTemplateName: str):
        """
        Setter for property: (str) ReportTemplateName
         Returns the report template name   
            
         
        """
        pass
    @property
    def ReportType(self) -> PageBuilder.Types:
        """
        Getter for property: ( PageBuilder.Types NXOp) ReportType
         Returns the selected report template type  
            
         
        """
        pass
    @ReportType.setter
    def ReportType(self, reportType: PageBuilder.Types):
        """
        Setter for property: ( PageBuilder.Types NXOp) ReportType
         Returns the selected report template type  
            
         
        """
        pass
    @property
    def SelectClassification(self) -> SelectClassificationBuilder:
        """
        Getter for property: ( SelectClassificationBuilder NXOp) SelectClassification
         Returns the selected classification   
            
         
        """
        pass
    @property
    def SelectedRule(self) -> int:
        """
        Getter for property: (int) SelectedRule
         Returns the selected report rule  
            
         
        """
        pass
    @SelectedRule.setter
    def SelectedRule(self, productAspect: int):
        """
        Setter for property: (int) SelectedRule
         Returns the selected report rule  
            
         
        """
        pass
    @property
    def WholeProjectToggle(self) -> bool:
        """
        Getter for property: (bool) WholeProjectToggle
         Returns the whole project toggle   
            
         
        """
        pass
    @WholeProjectToggle.setter
    def WholeProjectToggle(self, wholeProjectToggle: bool):
        """
        Setter for property: (bool) WholeProjectToggle
         Returns the whole project toggle   
            
         
        """
        pass
    def AddRule(self) -> None:
        """
         Add new report rule 
        """
        pass
    def RemoveRule(self) -> None:
        """
         Remove report rule 
        """
        pass
import NXOpen
class ReportTemplateBuilder(NXOpen.Builder): 
    """ Class to create Report Template and assign the ReportQuery and Report Layout to them """
    class ReportType(Enum):
        """
        Members Include: 
         |ListReport| 
         |ReportsWithTargets| 
         |ConnectionReports| 
         |TitlePage| 

        """
        ListReport: int
        ReportsWithTargets: int
        ConnectionReports: int
        TitlePage: int
        @staticmethod
        def ValueOf(value: int) -> ReportTemplateBuilder.ReportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DocumentType(self) -> PageTypes:
        """
        Getter for property: ( PageTypes NXOp) DocumentType
         Returns the document type   
            
         
        """
        pass
    @DocumentType.setter
    def DocumentType(self, type: PageTypes):
        """
        Setter for property: ( PageTypes NXOp) DocumentType
         Returns the document type   
            
         
        """
        pass
    @property
    def FileBrowserText(self) -> str:
        """
        Getter for property: (str) FileBrowserText
         Returns the name of selected form sheet    
            
         
        """
        pass
    @FileBrowserText.setter
    def FileBrowserText(self, name: str):
        """
        Setter for property: (str) FileBrowserText
         Returns the name of selected form sheet    
            
         
        """
        pass
    @property
    def ReportTemplateType(self) -> ReportTemplateBuilder.ReportType:
        """
        Getter for property: ( ReportTemplateBuilder.ReportType NXOp) ReportTemplateType
         Returns the Report type of report Template  NXOpen::AME::ReportTemplateBuilder::ReportType    
            
         
        """
        pass
    @ReportTemplateType.setter
    def ReportTemplateType(self, type: ReportTemplateBuilder.ReportType):
        """
        Setter for property: ( ReportTemplateBuilder.ReportType NXOp) ReportTemplateType
         Returns the Report type of report Template  NXOpen::AME::ReportTemplateBuilder::ReportType    
            
         
        """
        pass
import NXOpen
class ReportTemplate(NXOpen.NXObject): 
    """ JA class for the ReportTemplate object"""
    def CreateHeaderPlaceholderData(self) -> ReportHeaderPlaceHolderDataNode:
        """
         Create header placeholder data node
         Returns dataObject ( ReportHeaderPlaceHolderDataNode NXOp): .
        """
        pass
    def CreatePlaceholderData(self) -> ReportPlaceHolderData:
        """
         Create content placeholder data 
         Returns dataObject ( ReportPlaceHolderData NXOp): .
        """
        pass
    def DeleteHeaderPlaceholderData(self, colIndex: int, rowIndex: int) -> None:
        """
         Delete header placeholder data node
        """
        pass
    def RemoveInputPlaceholderdata(self, allSelectedColumnsOfTable: List[int]) -> None:
        """
         Deletes placeholder data corresponding to input index 
        """
        pass
    def ResetContentPlaceholderDataAt(self, colIndex: int) -> None:
        """
         Reset placeholder data 
        """
        pass
    def SetContentPlaceholderDataAt(self, dataObject: ReportPlaceHolderData, colIndex: int) -> None:
        """
         Set content placeholder data 
        """
        pass
    def SetHeaderPlaceholderCellRefAt(self, dataObject: ReportHeaderPlaceHolderDataNode, colIndex: int, rowIndex: int) -> None:
        """
         Set header placeholder cell ref 
        """
        pass
    def SetHeaderPlaceholderDataAt(self, dataObject: ReportHeaderPlaceHolderDataNode, counter: int) -> None:
        """
         Set header placeholder data 
        """
        pass
    def UpdatePlaceholdersAndTextRotation(self, currentTxt: str, colIndex: int, rowIndex: int, isInHeader: bool, textDir: int) -> None:
        """
         Update Placeholder chain and text rotation
        """
        pass
import NXOpen
class SaveToLibraryBuilder(NXOpen.Builder): 
    """Create Software Block JA class """
    @property
    def Destination(self) -> str:
        """
        Getter for property: (str) Destination
         Returns the destination directory path contains public query   
            
         
        """
        pass
    @Destination.setter
    def Destination(self, name: str):
        """
        Setter for property: (str) Destination
         Returns the destination directory path contains public query   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name in the library   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name in the library   
            
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Selection
         Returns the selected objects from project  
            
         
        """
        pass
    def SetItemId(self, itemId: str) -> None:
        """
         The library item Id. 
        """
        pass
import NXOpen
class SchematicSymbolConfigurationBuilder(NXOpen.Builder): 
    """ JA class for SchematicSymbolConfigurationBuilder dialog"""
    @property
    def SelectBaseDef(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectBaseDef
         Returns the product or engineering object definition  
            
         
        """
        pass
    def SetSymbolPropertiesTable(self, propertyName: str, propertyValue: str) -> None:
        """
         Set the symbol properties
        """
        pass
class SchematicSymbol(BaseDefinition): 
    """ Represents a Schematic Symbol object"""
    def PreprocessSymbolGeometry(self) -> None:
        """
         Preprocess symbol geometry for editing purpose
        """
        pass
    def SetActiveVariant(self, activeVariant: SymbolVariantBuilder.Variant) -> None:
        """
         Set active symbol variant
        """
        pass
import NXOpen
import NXOpen.Tooling
class SelectADReuseLibraryItemBuilder(NXOpen.TaggedObject): 
    """ Builder for selecting automation designer reuse lirary item"""
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library item builder  
            
         
        """
        pass
import NXOpen
class SelectADTypeBuilder(NXOpen.TaggedObject): 
    """
        Journalling Interface class for Builder which allows selection of Type, Product or Template.
    """
    @property
    def ReuseLibraryItem(self) -> SelectADReuseLibraryItemBuilder:
        """
        Getter for property: ( SelectADReuseLibraryItemBuilder NXOp) ReuseLibraryItem
         Returns the builder for reuse library selection item  
            
         
        """
        pass
    @property
    def SelectedINodeObject(self) -> INodeObject:
        """
        Getter for property: ( INodeObject NXOp) SelectedINodeObject
         Returns the selected  NXOpen::AME::INodeObject   
            
         
        """
        pass
    @SelectedINodeObject.setter
    def SelectedINodeObject(self, nodeObject: INodeObject):
        """
        Setter for property: ( INodeObject NXOp) SelectedINodeObject
         Returns the selected  NXOpen::AME::INodeObject   
            
         
        """
        pass
    def GetSelectedBaseDefinitionFromNode(self) -> BaseDefinition:
        """
         Gets selected base definition from node
         Returns baseDefinition ( BaseDefinition NXOp): .
        """
        pass
    def GetSelectedBaseDefinitionFromReuseItem(self) -> BaseDefinition:
        """
         Gets selected base definition from reuse item
         Returns baseDefinition ( BaseDefinition NXOp): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectAMEBaseNodeList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    @overload
    def Add(self, objectValue: AMEBaseNode) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[AMEBaseNode], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[AMEBaseNode]) -> bool:
        """
         Adds a set of objects to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: AMEBaseNode, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: AMEBaseNode, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: AMEBaseNode, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: AMEBaseNode, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    def Contains(self, objectValue: AMEBaseNode) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[AMEBaseNode]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( AMEBaseNode List[NX):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: AMEBaseNode) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[AMEBaseNode]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: AMEBaseNode, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: AMEBaseNode, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: AMEBaseNode, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         Returns removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    def SetArray(self, objects: List[AMEBaseNode]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectAMEBaseNode(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> AMEBaseNode:
        """
        Getter for property: ( AMEBaseNode NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: AMEBaseNode):
        """
        Setter for property: ( AMEBaseNode NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[AMEBaseNode, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  AMEBaseNode NXOp. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, AMEBaseNode, NXOpen.View, NXOpen.Point3d, AMEBaseNode, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  AMEBaseNode NXOp. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  AMEBaseNode NXOp. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[AMEBaseNode, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  AMEBaseNode NXOp. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: AMEBaseNode, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: AMEBaseNode, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: AMEBaseNode, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: AMEBaseNode, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectAMEPort(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> AMEPort:
        """
        Getter for property: ( AMEPort NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: AMEPort):
        """
        Setter for property: ( AMEPort NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[AMEPort, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  AMEPort NXOp. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, AMEPort, NXOpen.View, NXOpen.Point3d, AMEPort, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  AMEPort NXOp. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  AMEPort NXOp. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[AMEPort, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  AMEPort NXOp. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: AMEPort, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: AMEPort, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: AMEPort, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: AMEPort, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SelectAndHighlightBuilder(NXOpen.Builder): 
    """
    Represents a SelectAndHighlightBuilder for select and highlight in the Navigators
    """
    class SelType(Enum):
        """
        Members Include: 
         |TemplateMembers| 
         |PagePlacedObjects| 
         |ObjectChildren| 
         |AspectChildren| 
         |GroupMembers| 
         |MappedAncestors| 
         |SymbolItems| 
         |NotSet| 

        """
        TemplateMembers: int
        PagePlacedObjects: int
        ObjectChildren: int
        AspectChildren: int
        GroupMembers: int
        MappedAncestors: int
        SymbolItems: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> SelectAndHighlightBuilder.SelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SelectHighlightMode(self) -> SelectAndHighlightBuilder.SelType:
        """
        Getter for property: ( SelectAndHighlightBuilder.SelType NXOp) SelectHighlightMode
         Returns   
            
         
        """
        pass
    @SelectHighlightMode.setter
    def SelectHighlightMode(self, sel: SelectAndHighlightBuilder.SelType):
        """
        Setter for property: ( SelectAndHighlightBuilder.SelType NXOp) SelectHighlightMode
         Returns   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectAspectNode(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> AspectNode:
        """
        Getter for property: ( AspectNode NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: AspectNode):
        """
        Setter for property: ( AspectNode NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[AspectNode, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  AspectNode NXOp. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, AspectNode, NXOpen.View, NXOpen.Point3d, AspectNode, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  AspectNode NXOp. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  AspectNode NXOp. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[AspectNode, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  AspectNode NXOp. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: AspectNode, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: AspectNode, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: AspectNode, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: AspectNode, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SelectAttrPropSourceBuilder(NXOpen.Builder): 
    """
        Journalling Interface class for Builder which allows selection of an 
        object which has attribute properties set on it. Source of object
        could be a reuse library item or the base node.
    """
    @property
    def ReuseLibraryItem(self) -> InstantiateBaseDefinitionReuseSelectionBuilder:
        """
        Getter for property: ( InstantiateBaseDefinitionReuseSelectionBuilder NXOp) ReuseLibraryItem
         Returns the builder for reuse library selection item  
            
         
        """
        pass
    @property
    def SelectedINodeObject(self) -> INodeObject:
        """
        Getter for property: ( INodeObject NXOp) SelectedINodeObject
         Returns the selected  NXOpen::AME::INodeObject   
            
         
        """
        pass
    @SelectedINodeObject.setter
    def SelectedINodeObject(self, nodeObject: INodeObject):
        """
        Setter for property: ( INodeObject NXOp) SelectedINodeObject
         Returns the selected  NXOpen::AME::INodeObject   
            
         
        """
        pass
    def GetAttrPropSourceFromNode(self) -> NXOpen.TaggedObject:
        """
         Gets attribute property source from base node 
         Returns attrPropSource ( NXOpen.TaggedObject): .
        """
        pass
    def GetAttrPropSourceFromReuseItem(self) -> NXOpen.TaggedObject:
        """
         Gets attribute property source from reuse library item 
         Returns attrPropSource ( NXOpen.TaggedObject): .
        """
        pass
import NXOpen
class SelectBaseDefinitionNodeBuilder(NXOpen.TaggedObject): 
    """ Builder for selecting base definition node from navigators"""
    @property
    def SelectObject(self) -> SelectAMEBaseNode:
        """
        Getter for property: ( SelectAMEBaseNode NXOp) SelectObject
         Returns the selected Object   
            
         
        """
        pass
    def SetSelectedNode(self, baseNode: NXOpen.NXObject) -> None:
        """
        Sets the selected base definition node object
        """
        pass
import NXOpen.Tooling
class SelectClassificationBuilder(NXOpen.Tooling.SelectReuseLibraryItemBuilder): 
    """ Select a part from the reuse library """
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
         Returns the class of the name from the reuse library classification   
            
         
        """
        pass
    @ClassName.setter
    def ClassName(self, path: str):
        """
        Setter for property: (str) ClassName
         Returns the class of the name from the reuse library classification   
            
         
        """
        pass
import NXOpen
class SelectClassificationFromTreeBuilder(NXOpen.Builder): 
    """ Select Type from the Classification Library """
    @property
    def Classification(self) -> str:
        """
        Getter for property: (str) Classification
         Returns the classification  
            
         
        """
        pass
    @Classification.setter
    def Classification(self, eType: str):
        """
        Setter for property: (str) Classification
         Returns the classification  
            
         
        """
        pass
    @property
    def ClassificationProperty(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ClassificationProperty
         Returns the classification property  
            
         
        """
        pass
import NXOpen
class SelectComponentBuilder(NXOpen.TaggedObject): 
    """ Builder for selection of external component"""
    @property
    def SelectObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectObject
         Returns the selected object  
            
         
        """
        pass
import NXOpen
class SelectConditionBuilder(NXOpen.Builder): 
    """ Defines conditions by using expressions for engineering objects """
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the string value of the property name    
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the string value of the property name    
            
         
        """
        pass
    @property
    def SelectedEngObject(self) -> AMEEngObject:
        """
        Getter for property: ( AMEEngObject NXOp) SelectedEngObject
         Returns the selected engineering object   
            
         
        """
        pass
    @SelectedEngObject.setter
    def SelectedEngObject(self, selectedEngObject: AMEEngObject):
        """
        Setter for property: ( AMEEngObject NXOp) SelectedEngObject
         Returns the selected engineering object   
            
         
        """
        pass
    def SetCondition(self, exp: NXOpen.Expression) -> None:
        """
         Set the condition for the value set 
        """
        pass
import NXOpen
class SelectExternalObjectBuilder(NXOpen.TaggedObject): 
    """ Journalling Interface class for Builder which allows selection of external objects. Source of object
        could be a ld reuse library item or the external object node.
    """
    @property
    def ExternalComponent(self) -> SelectComponentBuilder:
        """
        Getter for property: ( SelectComponentBuilder NXOp) ExternalComponent
         Returns the builder for selection of external component  
            
         
        """
        pass
    @property
    def ReuseLibraryItem(self) -> SelectExternalReuseLibraryItemBuilder:
        """
        Getter for property: ( SelectExternalReuseLibraryItemBuilder NXOp) ReuseLibraryItem
         Returns the builder for reuse library selection item  
            
         
        """
        pass
import NXOpen
import NXOpen.Tooling
class SelectExternalReuseLibraryItemBuilder(NXOpen.TaggedObject): 
    """ Builder for selecting external reuse lirary item"""
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library item builder  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectINodeObjectList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    @overload
    def Add(self, objectValue: INodeObject) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[INodeObject], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[INodeObject]) -> bool:
        """
         Adds a set of objects to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: INodeObject, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: INodeObject, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: INodeObject, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: INodeObject, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    def Contains(self, objectValue: INodeObject) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[INodeObject]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( INodeObject List[NX):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: INodeObject) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[INodeObject]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: INodeObject, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: INodeObject, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: INodeObject, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         Returns removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    def SetArray(self, objects: List[INodeObject]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectINodeObject(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> INodeObject:
        """
        Getter for property: ( INodeObject NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: INodeObject):
        """
        Setter for property: ( INodeObject NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[INodeObject, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  INodeObject NXOp. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, INodeObject, NXOpen.View, NXOpen.Point3d, INodeObject, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  INodeObject NXOp. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  INodeObject NXOp. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[INodeObject, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  INodeObject NXOp. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: INodeObject, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: INodeObject, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: INodeObject, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: INodeObject, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SelectionBaseDefinitionBuilder(NXOpen.TaggedObject): 
    """
        Journalling Interface class for Builder which allows selection of BaseDefinition.
    """
    @property
    def ReuseLibraryItem(self) -> InstantiateBaseDefinitionReuseSelectionBuilder:
        """
        Getter for property: ( InstantiateBaseDefinitionReuseSelectionBuilder NXOp) ReuseLibraryItem
         Returns the builder for reuse library selection item  
            
         
        """
        pass
    @property
    def SelectBaseDefinitionNode(self) -> SelectBaseDefinitionNodeBuilder:
        """
        Getter for property: ( SelectBaseDefinitionNodeBuilder NXOp) SelectBaseDefinitionNode
         Returns the builder for selected base definition node   
            
         
        """
        pass
    def GetSelectedBaseDefinition(self) -> BaseDefinition:
        """
         Gets selected base definition 
         Returns baseDefinition ( BaseDefinition NXOp): .
        """
        pass
    def SetSelectedBaseDefinition(self, baseDefinition: BaseDefinition) -> None:
        """
        Sets the selected base definition
        """
        pass
import NXOpen
import NXOpen.Tooling
class SelectionEngineeringObjectDefinitionBuilder(NXOpen.TaggedObject): 
    """
        JA class for the Engineering Object Definition Block
    """
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library selection item  
            
         
        """
        pass
    @property
    def SelectObject(self) -> SelectAspectNode:
        """
        Getter for property: ( SelectAspectNode NXOp) SelectObject
         Returns the get select Object   
            
         
        """
        pass
    def SetSelectedEngineeringObjectDefinition(self, selectedEoDef: NXOpen.NXObject) -> None:
        """
        Sets the selected eo def
        """
        pass
    def UpdateSelectedEngineeringObjectDefinition(self, fromProject: bool) -> None:
        """
        Updates the selected eo def
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectIPort(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> IPort:
        """
        Getter for property: ( IPort NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: IPort):
        """
        Setter for property: ( IPort NXOp) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[IPort, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  IPort NXOp. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, IPort, NXOpen.View, NXOpen.Point3d, IPort, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  IPort NXOp. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  IPort NXOp. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[IPort, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  IPort NXOp. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: IPort, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: IPort, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: IPort, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: IPort, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SelectMountingInterfaceLocationBuilder(NXOpen.Builder): 
    """ Builder for selecting mounting interface location from graphics window"""
    @property
    def FixingPlacementLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) FixingPlacementLocation
         Returns the co-ordinate of fixing placement location  
            
         
        """
        pass
    @FixingPlacementLocation.setter
    def FixingPlacementLocation(self, targetLocation: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) FixingPlacementLocation
         Returns the co-ordinate of fixing placement location  
            
         
        """
        pass
    @property
    def IsLocationSelected(self) -> bool:
        """
        Getter for property: (bool) IsLocationSelected
         Returns the logical value whether location is selected  
            
         
        """
        pass
    @IsLocationSelected.setter
    def IsLocationSelected(self, locationSelectedObject: bool):
        """
        Setter for property: (bool) IsLocationSelected
         Returns the logical value whether location is selected  
            
         
        """
        pass
    @property
    def SelectedReceptacleObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) SelectedReceptacleObject
         Returns the tag of selected receptacle object  
            
         
        """
        pass
    @SelectedReceptacleObject.setter
    def SelectedReceptacleObject(self, selectedObjectTag: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) SelectedReceptacleObject
         Returns the tag of selected receptacle object  
            
         
        """
        pass
import NXOpen
import NXOpen.Tooling
class SelectProductDefinitionBuilder(NXOpen.TaggedObject): 
    """
        JA class for the Product Definition Selection
    """
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the reuse library selection item  
            
         
        """
        pass
    def SetSelectedProductDefinition(self, productDefinition: NXOpen.NXObject) -> None:
        """
        Sets the selected product definition
        """
        pass
    def UpdateSelectedProductDefinition(self) -> None:
        """
        Updates the selected product definition
        """
        pass
import NXOpen
import NXOpen.Tooling
class SelectReuseLibraryItemBuilder(NXOpen.TaggedObject): 
    """ Builder for selecting base definition"""
    @property
    def ReuseLibraryItemBuilder(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItemBuilder
         Returns the reuse library item selection  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectSolutionTemplateBuilder(NXOpen.TaggedObject): 
    """ Represents a re-usable component for Select Solution Template """
    @property
    def SelectedSolutionTemplate(self) -> BasicTemplateData:
        """
        Getter for property: ( BasicTemplateData NXOp) SelectedSolutionTemplate
         Returns the selected solution template   
            
         
        """
        pass
    @SelectedSolutionTemplate.setter
    def SelectedSolutionTemplate(self, selectedSolutionTemplate: BasicTemplateData):
        """
        Setter for property: ( BasicTemplateData NXOp) SelectedSolutionTemplate
         Returns the selected solution template   
            
         
        """
        pass
    @property
    def TemplatePartCliName(self) -> str:
        """
        Getter for property: (str) TemplatePartCliName
         Returns the template part cli name   
            
         
        """
        pass
    @TemplatePartCliName.setter
    def TemplatePartCliName(self, templatePartCliName: str):
        """
        Setter for property: (str) TemplatePartCliName
         Returns the template part cli name   
            
         
        """
        pass
class SendReceiveType(Enum):
    """
    Members Include: 
     |SendAndReceive| 
     |Send| 
     |Receive| 

    """
    SendAndReceive: int
    Send: int
    Receive: int
    @staticmethod
    def ValueOf(value: int) -> SendReceiveType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class ShieldBuilder(AMEBaseBuilder): 
    """ Represents builder for  AME::DB::Shield """
    class Variant(Enum):
        """
        Members Include: 
         |H| 
         |V| 

        """
        H: int
        V: int
        @staticmethod
        def ValueOf(value: int) -> ShieldBuilder.Variant:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateShieldNode(self, pageObject: PageObject) -> NXOpen.Diagramming.Node:
        """
         Method to create the Shield Diagram Node 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetShieldLocation(self, point: NXOpen.Point2d) -> None:
        """
         Set node location of Shield on page. 
        """
        pass
    def SetShieldVariant(self, shieldVariant: ShieldBuilder.Variant) -> None:
        """
         Set shield variant on the page. 
        """
        pass
import NXOpen
class ShowHideObjectsBuilder(NXOpen.Builder): 
    """ JA class for ShowHideObjectsBuilder"""
    @property
    def ShowChannels(self) -> bool:
        """
        Getter for property: (bool) ShowChannels
         Returns the setting for showinghiding Plc Channels in aspect navigators  
            
         
        """
        pass
    @ShowChannels.setter
    def ShowChannels(self, showChannels: bool):
        """
        Setter for property: (bool) ShowChannels
         Returns the setting for showinghiding Plc Channels in aspect navigators  
            
         
        """
        pass
    @property
    def ShowConnectors(self) -> bool:
        """
        Getter for property: (bool) ShowConnectors
         Returns the setting for showinghiding connectors in aspect navigators  
            
         
        """
        pass
    @ShowConnectors.setter
    def ShowConnectors(self, showConnectors: bool):
        """
        Setter for property: (bool) ShowConnectors
         Returns the setting for showinghiding connectors in aspect navigators  
            
         
        """
        pass
    @property
    def ShowEPLAN(self) -> bool:
        """
        Getter for property: (bool) ShowEPLAN
         Returns the setting for showinghiding EPLAN objects in aspect navigators  
            
         
        """
        pass
    @ShowEPLAN.setter
    def ShowEPLAN(self, showEPLAN: bool):
        """
        Setter for property: (bool) ShowEPLAN
         Returns the setting for showinghiding EPLAN objects in aspect navigators  
            
         
        """
        pass
    @property
    def ShowPlacedFragments(self) -> bool:
        """
        Getter for property: (bool) ShowPlacedFragments
         Returns the setting for showinghiding placed fragments in aspect navigators  
            
         
        """
        pass
    @ShowPlacedFragments.setter
    def ShowPlacedFragments(self, showPlacedFragments: bool):
        """
        Setter for property: (bool) ShowPlacedFragments
         Returns the setting for showinghiding placed fragments in aspect navigators  
            
         
        """
        pass
    @property
    def ShowSoftwareBlocks(self) -> bool:
        """
        Getter for property: (bool) ShowSoftwareBlocks
         Returns the setting for showinghiding software blocks in aspect navigators  
            
         
        """
        pass
    @ShowSoftwareBlocks.setter
    def ShowSoftwareBlocks(self, showSoftwareBlocks: bool):
        """
        Setter for property: (bool) ShowSoftwareBlocks
         Returns the setting for showinghiding software blocks in aspect navigators  
            
         
        """
        pass
    @property
    def ShowTags(self) -> bool:
        """
        Getter for property: (bool) ShowTags
         Returns the setting for showinghiding Plc Tags in aspect navigators  
            
         
        """
        pass
    @ShowTags.setter
    def ShowTags(self, showTags: bool):
        """
        Setter for property: (bool) ShowTags
         Returns the setting for showinghiding Plc Tags in aspect navigators  
            
         
        """
        pass
    @property
    def ShowUnplacedFragments(self) -> bool:
        """
        Getter for property: (bool) ShowUnplacedFragments
         Returns the setting for showinghiding the setting for unplaced fragments in aspect navigators  
            
         
        """
        pass
    @ShowUnplacedFragments.setter
    def ShowUnplacedFragments(self, showUnplacedFragments: bool):
        """
        Setter for property: (bool) ShowUnplacedFragments
         Returns the setting for showinghiding the setting for unplaced fragments in aspect navigators  
            
         
        """
        pass
import NXOpen
class SinCatMappingBuilder(NXOpen.Builder): 
    """ Class is used to Map to SINAMICS Component Catalog  """
    def SetSinCatId(self, text: str) -> None:
        """
         Set SINAMICS Catalog ID
        """
        pass
class SmartPDFPrintPagesBuilder(PrintPagesBuilder): 
    """ JA class for the Smart PDF PrintPages """
    def AddSelectedPageObjects(self, pageObjects: List[PageObject]) -> None:
        """
         Set the page objects.
        """
        pass
import NXOpen
class Snap3DModelsBuilder(AMEBaseBuilder): 
    """ Represents a Snap3DModelsBuilder class Builder  """
    @property
    def FixingInterface(self) -> str:
        """
        Getter for property: (str) FixingInterface
         Returns the fixingInterface of selected product  
            
         
        """
        pass
    @FixingInterface.setter
    def FixingInterface(self, fixingInterface: str):
        """
        Setter for property: (str) FixingInterface
         Returns the fixingInterface of selected product  
            
         
        """
        pass
    @property
    def Select3dModel(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Select3dModel
         Returns the Target node selection   
            
         
        """
        pass
    @property
    def SelectMountingInterfaceLocation(self) -> SelectMountingInterfaceLocationBuilder:
        """
        Getter for property: ( SelectMountingInterfaceLocationBuilder NXOp) SelectMountingInterfaceLocation
         Returns the co-ordinate of target location  
            
         
        """
        pass
    @SelectMountingInterfaceLocation.setter
    def SelectMountingInterfaceLocation(self, targetLocation: SelectMountingInterfaceLocationBuilder):
        """
        Setter for property: ( SelectMountingInterfaceLocationBuilder NXOp) SelectMountingInterfaceLocation
         Returns the co-ordinate of target location  
            
         
        """
        pass
    def UpdateProduct3DModelPreview(self) -> None:
        """
         Update product 3d model preview
        """
        pass
class SoftwareBlockDataTypePort(PlcSoftwareGenPort): 
    """ SoftwareBlockDataTypePort Journaling class """
    def ResetLibraryItemLink(self) -> None:
        """
         Reset the library item link. Library link will be removed automaticaly via the OnConnectionUpdated in port itself. Use this function only in case of special behavior. 
        """
        pass
class SolutionTemplateData(BasicTemplateData): 
    """ JA class for the Solution Template Data object"""
    pass
import NXOpen
class SortingBlockBuilder(NXOpen.TaggedObject): 
    """ Sorts the list expression output according to the property """
    class Order(Enum):
        """
        Members Include: 
         |Ascending| 
         |Descending| 

        """
        Ascending: int
        Descending: int
        @staticmethod
        def ValueOf(value: int) -> SortingBlockBuilder.Order:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OrderValue(self) -> SortingBlockBuilder.Order:
        """
        Getter for property: ( SortingBlockBuilder.Order NXOp) OrderValue
         Returns the sorting order type   
            
         
        """
        pass
    @OrderValue.setter
    def OrderValue(self, orderValue: SortingBlockBuilder.Order):
        """
        Setter for property: ( SortingBlockBuilder.Order NXOp) OrderValue
         Returns the sorting order type   
            
         
        """
        pass
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the property name given by the user   
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the property name given by the user   
            
         
        """
        pass
import NXOpen
class SubnetBuilder(NXOpen.Builder): 
    """ Represents a Subnet creation class Builder """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the subnet description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the subnet description   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the subnet name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the subnet name   
            
         
        """
        pass
    @property
    def SelectionObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectionObject
         Returns the selection object which is parent station.  
             
         
        """
        pass
    @property
    def Types(self) -> str:
        """
        Getter for property: (str) Types
         Returns the subnet type  
            
         
        """
        pass
    @Types.setter
    def Types(self, types: str):
        """
        Setter for property: (str) Types
         Returns the subnet type  
            
         
        """
        pass
import NXOpen
class SumEvaluatorBuilder(BaseEvaluatorBuilder): 
    """ Evaluates sum of given property for list of objects"""
    @property
    def PropertyName(self) -> str:
        """
        Getter for property: (str) PropertyName
         Returns the property name   
            
         
        """
        pass
    @PropertyName.setter
    def PropertyName(self, propertyName: str):
        """
        Setter for property: (str) PropertyName
         Returns the property name   
            
         
        """
        pass
    @property
    def PropertyUnitTag(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) PropertyUnitTag
         Returns the property unit   
            
         
        """
        pass
    @property
    def SelectedObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) SelectedObject
         Returns the selected object   
            
         
        """
        pass
    @SelectedObject.setter
    def SelectedObject(self, selectedObject: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) SelectedObject
         Returns the selected object   
            
         
        """
        pass
import NXOpen
class SWStatusItem(NXOpen.NXObject): 
    """ Represents SW Status Item"""
    pass
import NXOpen
class SymbolAnnotationBuilder(NXOpen.Builder): 
    """ Represents a Symbol Annotation creation class Builder  """
    class Anchor(Enum):
        """
        Members Include: 
         |TopLeft| 
         |TopCenter| 
         |TopRight| 
         |MiddleLeft| 
         |MiddleCenter| 
         |MiddleRight| 
         |BottomLeft| 
         |BottomCenter| 
         |BottomRight| 

        """
        TopLeft: int
        TopCenter: int
        TopRight: int
        MiddleLeft: int
        MiddleCenter: int
        MiddleRight: int
        BottomLeft: int
        BottomCenter: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> SymbolAnnotationBuilder.Anchor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Orientation(Enum):
        """
        Members Include: 
         |Horizontal| 
         |Vertical| 

        """
        Horizontal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> SymbolAnnotationBuilder.Orientation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorPointLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) AnchorPointLocation
         Returns the symbol anchor point   
            
         
        """
        pass
    @property
    def SymbolAnnotationAnchor(self) -> SymbolAnnotationBuilder.Anchor:
        """
        Getter for property: ( SymbolAnnotationBuilder.Anchor NXOp) SymbolAnnotationAnchor
         Returns the anchor   
            
         
        """
        pass
    @SymbolAnnotationAnchor.setter
    def SymbolAnnotationAnchor(self, anchor: SymbolAnnotationBuilder.Anchor):
        """
        Setter for property: ( SymbolAnnotationBuilder.Anchor NXOp) SymbolAnnotationAnchor
         Returns the anchor   
            
         
        """
        pass
    @property
    def SymbolAnnotationOrientation(self) -> SymbolAnnotationBuilder.Orientation:
        """
        Getter for property: ( SymbolAnnotationBuilder.Orientation NXOp) SymbolAnnotationOrientation
         Returns the orientation   
            
         
        """
        pass
    @SymbolAnnotationOrientation.setter
    def SymbolAnnotationOrientation(self, orientation: SymbolAnnotationBuilder.Orientation):
        """
        Setter for property: ( SymbolAnnotationBuilder.Orientation NXOp) SymbolAnnotationOrientation
         Returns the orientation   
            
         
        """
        pass
    @property
    def SymbolAnnotationPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) SymbolAnnotationPoint
         Returns the symbol annotation point   
            
         
        """
        pass
    @SymbolAnnotationPoint.setter
    def SymbolAnnotationPoint(self, symbolAnnotationPoint: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) SymbolAnnotationPoint
         Returns the symbol annotation point   
            
         
        """
        pass
    def AddCheckedAttribute(self, propertyName: str, propertyReference: NXOpen.NXObject) -> None:
        """
         Add the checked attribute. 
        """
        pass
    def ResetPropertyList(self) -> None:
        """
         Reset the property list. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SymbolAnnotationStyleBuilder(NXOpen.TaggedObject): 
    """ Represents a re-usable component for Symbol annotation styles """
    @property
    def Anchor(self) -> AmeSymbolAnnotationAnchor:
        """
        Getter for property: ( AmeSymbolAnnotationAnchor NXOp) Anchor
         Returns the anchor   
            
         
        """
        pass
    @Anchor.setter
    def Anchor(self, anchor: AmeSymbolAnnotationAnchor):
        """
        Setter for property: ( AmeSymbolAnnotationAnchor NXOp) Anchor
         Returns the anchor   
            
         
        """
        pass
    @property
    def Bold(self) -> bool:
        """
        Getter for property: (bool) Bold
         Returns the bold   
            
         
        """
        pass
    @Bold.setter
    def Bold(self, bold: bool):
        """
        Setter for property: (bool) Bold
         Returns the bold   
            
         
        """
        pass
    @property
    def ColorFontWidth(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) ColorFontWidth
         Returns the color font width   
            
         
        """
        pass
    @property
    def Height(self) -> Height:
        """
        Getter for property: ( Height NXOp) Height
         Returns the height   
            
         
        """
        pass
    @Height.setter
    def Height(self, height: Height):
        """
        Setter for property: ( Height NXOp) Height
         Returns the height   
            
         
        """
        pass
    @property
    def Italics(self) -> bool:
        """
        Getter for property: (bool) Italics
         Returns the italics   
            
         
        """
        pass
    @Italics.setter
    def Italics(self, italics: bool):
        """
        Setter for property: (bool) Italics
         Returns the italics   
            
         
        """
        pass
    @property
    def Justification(self) -> AmeSymbolAnnotationJustification:
        """
        Getter for property: ( AmeSymbolAnnotationJustification NXOp) Justification
         Returns the justification   
            
         
        """
        pass
    @Justification.setter
    def Justification(self, justification: AmeSymbolAnnotationJustification):
        """
        Setter for property: ( AmeSymbolAnnotationJustification NXOp) Justification
         Returns the justification   
            
         
        """
        pass
    @property
    def LetteringAngle(self) -> AmeSymbolAnnotationLetteringangle:
        """
        Getter for property: ( AmeSymbolAnnotationLetteringangle NXOp) LetteringAngle
         Returns the lettering angle   
            
         
        """
        pass
    @LetteringAngle.setter
    def LetteringAngle(self, letteringAngle: AmeSymbolAnnotationLetteringangle):
        """
        Setter for property: ( AmeSymbolAnnotationLetteringangle NXOp) LetteringAngle
         Returns the lettering angle   
            
         
        """
        pass
    @property
    def Overline(self) -> bool:
        """
        Getter for property: (bool) Overline
         Returns the overline   
            
         
        """
        pass
    @Overline.setter
    def Overline(self, overline: bool):
        """
        Setter for property: (bool) Overline
         Returns the overline   
            
         
        """
        pass
    @property
    def Underline(self) -> bool:
        """
        Getter for property: (bool) Underline
         Returns the underline   
            
         
        """
        pass
    @Underline.setter
    def Underline(self, underline: bool):
        """
        Setter for property: (bool) Underline
         Returns the underline   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Gateway
import NXOpen.Tooling
class SymbolAuthoringBuilder(NXOpen.Builder): 
    """ Represents a Symbol Authoring class Builder  """
    class Types(Enum):
        """
        Members Include: 
         |StandardSymbol| 
         |CableDefinitionLine| 

        """
        StandardSymbol: int
        CableDefinitionLine: int
        @staticmethod
        def ValueOf(value: int) -> SymbolAuthoringBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorPointLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) AnchorPointLocation
         Returns the symbol anchor point   
            
         
        """
        pass
    @AnchorPointLocation.setter
    def AnchorPointLocation(self, symbolAnchorPoint: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) AnchorPointLocation
         Returns the symbol anchor point   
            
         
        """
        pass
    @property
    def CapturedImage(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: ( NXOpen.Gateway.ImageCaptureBuilder) CapturedImage
         Returns the image capture builder used to create an image for preview  
            
         
        """
        pass
    @property
    def SelectedCustomSymbol(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) SelectedCustomSymbol
         Returns the custom symbol selection  
            
         
        """
        pass
    @property
    def SelectedPort(self) -> SelectAMEPort:
        """
        Getter for property: ( SelectAMEPort NXOp) SelectedPort
         Returns the port selection   
            
         
        """
        pass
    @property
    def SymbolAnnotationPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) SymbolAnnotationPoint
         Returns the symbol annotation point   
            
         
        """
        pass
    @property
    def Type(self) -> SymbolAuthoringBuilder.Types:
        """
        Getter for property: ( SymbolAuthoringBuilder.Types NXOp) Type
         Returns the symbol type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SymbolAuthoringBuilder.Types):
        """
        Setter for property: ( SymbolAuthoringBuilder.Types NXOp) Type
         Returns the symbol type   
            
         
        """
        pass
    def CreateConnectionPoint(self, portToBeMapped: NXOpen.NXObject) -> str:
        """
         Creates a new connection point 
         Returns portID (str): .
        """
        pass
    def CreateDefaultPortAnnotation(self, portID: str, connPoint: NXOpen.Point3d) -> None:
        """
         Annotation for connection point 
        """
        pass
    def DeleteConnectionPoint(self, portToBeUnmapped: NXOpen.NXObject, portID: str) -> None:
        """
         Deletes the connection point 
        """
        pass
    def GetConnectionDirection(self, portID: str) -> NXOpen.Point2d:
        """
         Gets the connection direction 
         Returns connectionDirection ( NXOpen.Point2d): .
        """
        pass
    def GetConnectionPointLocation(self, portID: str) -> NXOpen.Point2d:
        """
         Gets the connection point location 
         Returns portLocation ( NXOpen.Point2d): .
        """
        pass
    def InsertSymbol(self, customSymbolPath: str) -> NXOpen.Annotations.CustomSymbol:
        """
         Insert the symbol 
         Returns custom_symbol ( NXOpen.Annotations.CustomSymbol): .
        """
        pass
    def SetConnectionDirection(self, portID: str, connectionDirection: NXOpen.Point2d) -> None:
        """
         Sets the connection direction 
        """
        pass
    def SetConnectionPointLocation(self, portID: str, portLocation: NXOpen.Point2d) -> None:
        """
         Sets the connection point location 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class SymbolLocationBuilder(NXOpen.TaggedObject): 
    """ JA class for the symbol location reusable component"""
    @property
    def DiagramNodeBuilder(self) -> DiagramNodeBuilder:
        """
        Getter for property: ( DiagramNodeBuilder NXOp) DiagramNodeBuilder
         Returns the Node Builder used for creating Symbol for EO  
            
         
        """
        pass
    def ClearCreatedSymbol(self, isClearAllSymbols: bool) -> None:
        """
         Clear the created Symbol
        """
        pass
    def ClearCreatedSymbolVariant(self, symbolTag: NXOpen.Diagramming.Node) -> None:
        """
         Clear the created Symbol Variants
        """
        pass
    def SetCreatedSymbol(self, owningPage: PageObject, symbolTag: NXOpen.Diagramming.Node, locationX: float, locationY: float) -> None:
        """
         Set the created Symbol
        """
        pass
import NXOpen
import NXOpen.Annotations
class SymbolNoteBuilder(NXOpen.Builder): 
    """ Represents a Symbol Note creation class Builder  """
    @property
    def ContactBlock(self) -> AmeSymbolAnnotationContactblock:
        """
        Getter for property: ( AmeSymbolAnnotationContactblock NXOp) ContactBlock
         Returns the contact block annotation type   
            
         
        """
        pass
    @ContactBlock.setter
    def ContactBlock(self, type: AmeSymbolAnnotationContactblock):
        """
        Setter for property: ( AmeSymbolAnnotationContactblock NXOp) ContactBlock
         Returns the contact block annotation type   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def SymbolAnnotationStyle(self) -> SymbolAnnotationStyleBuilder:
        """
        Getter for property: ( SymbolAnnotationStyleBuilder NXOp) SymbolAnnotationStyle
         Returns the symbolAnnotationStyle   
            
         
        """
        pass
    @property
    def TextBoxWidth(self) -> float:
        """
        Getter for property: (float) TextBoxWidth
         Returns the text textbox width   
            
         
        """
        pass
    @TextBoxWidth.setter
    def TextBoxWidth(self, type: float):
        """
        Setter for property: (float) TextBoxWidth
         Returns the text textbox width   
            
         
        """
        pass
    @property
    def TextOverflow(self) -> AmeSymbolAnnotationTextOverflowMethod:
        """
        Getter for property: ( AmeSymbolAnnotationTextOverflowMethod NXOp) TextOverflow
         Returns the text overflow method   
            
         
        """
        pass
    @TextOverflow.setter
    def TextOverflow(self, type: AmeSymbolAnnotationTextOverflowMethod):
        """
        Setter for property: ( AmeSymbolAnnotationTextOverflowMethod NXOp) TextOverflow
         Returns the text overflow method   
            
         
        """
        pass
    @property
    def Type(self) -> AmeSymbolAnnotationType:
        """
        Getter for property: ( AmeSymbolAnnotationType NXOp) Type
         Returns the Annotation type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AmeSymbolAnnotationType):
        """
        Setter for property: ( AmeSymbolAnnotationType NXOp) Type
         Returns the Annotation type   
            
         
        """
        pass
    def AddAttribute(self, propertyName: str, propertyReference: NXOpen.NXObject) -> None:
        """
         Add the attribute 
        """
        pass
    def AddNewAttribute(self, attrOwner: NXOpen.NXObject, attrTitle: str, attrCategory: AmeSymbolAnnotationAttributesource) -> None:
        """
         Add the new attribute 
        """
        pass
    def MoveDownAttribute(self, attrIndex: int) -> None:
        """
         Move down attribute 
        """
        pass
    def MoveUpAttribute(self, attrIndex: int) -> None:
        """
         Move up attribute 
        """
        pass
    def RemoveAttribute(self, attrIndex: int) -> None:
        """
         Remove the attribute 
        """
        pass
    def ResetPropertyList(self) -> None:
        """
         Reset the property list 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets the symbol annotation settings to default.
        """
        pass
    def SetNoteString(self, noteString: str) -> None:
        """
         Set the note string 
        """
        pass
    def UpdateAttributeCategory(self, attrIndex: int, attrCategory: AmeSymbolAnnotationAttributesource) -> None:
        """
         Update attribute category 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class SymbolPlacementBuilder(NXOpen.TaggedObject): 
    """ JA class for the symbol placement reusable component"""
    @property
    def DiagramNodeBuilder(self) -> DiagramNodeBuilder:
        """
        Getter for property: ( DiagramNodeBuilder NXOp) DiagramNodeBuilder
         Returns the Node Builder used for creating Symbol for EO  
            
         
        """
        pass
    @property
    def RectangularSymbol(self) -> bool:
        """
        Getter for property: (bool) RectangularSymbol
         Returns the rectangularSymbol   
            
         
        """
        pass
    @RectangularSymbol.setter
    def RectangularSymbol(self, rectangularSymbol: bool):
        """
        Setter for property: (bool) RectangularSymbol
         Returns the rectangularSymbol   
            
         
        """
        pass
    def ClearCreatedSymbol(self, isClearAllSymbols: bool) -> None:
        """
         Clear the created Symbol
        """
        pass
    def ClearCreatedSymbolVariant(self, symbolTag: NXOpen.Diagramming.Node) -> None:
        """
         Clear the created Symbol Variants
        """
        pass
    def SetCreatedSymbol(self, owningPage: PageObject, symbolTag: NXOpen.Diagramming.Node, locationX: float, locationY: float) -> None:
        """
         Set the created Symbol
        """
        pass
class SymbolRoot(AMEBaseNode): 
    """ Symbol Root Node class """
    pass
import NXOpen
class SymbolVariantBuilder(NXOpen.Builder): 
    """ Represents a Symbol Variant creation class Builder  """
    class Variant(Enum):
        """
        Members Include: 
         |A| 
         |B| 
         |C| 
         |D| 
         |E| 
         |F| 
         |G| 
         |H| 
         |ContactBlockInPath| 
         |ContactBlockOnComponent| 

        """
        A: int
        B: int
        C: int
        D: int
        E: int
        F: int
        G: int
        H: int
        ContactBlockInPath: int
        ContactBlockOnComponent: int
        @staticmethod
        def ValueOf(value: int) -> SymbolVariantBuilder.Variant:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the variant description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the variant description   
            
         
        """
        pass
    @property
    def EditMode(self) -> bool:
        """
        Getter for property: (bool) EditMode
         Returns the flag for edit mode   
            
         
        """
        pass
    @EditMode.setter
    def EditMode(self, editMode: bool):
        """
        Setter for property: (bool) EditMode
         Returns the flag for edit mode   
            
         
        """
        pass
    @property
    def SymbolVariant(self) -> SymbolVariantBuilder.Variant:
        """
        Getter for property: ( SymbolVariantBuilder.Variant NXOp) SymbolVariant
         Returns the variant type   
            
         
        """
        pass
    @SymbolVariant.setter
    def SymbolVariant(self, symbolVariant: SymbolVariantBuilder.Variant):
        """
        Setter for property: ( SymbolVariantBuilder.Variant NXOp) SymbolVariant
         Returns the variant type   
            
         
        """
        pass
import NXOpen
class TCSavedQueriesBuilder(NXOpen.Builder): 
    """ Represents a TC Saved Queries builder """
    def SetQueryCriteriaName(self, index: int, queryCriteriaName: str) -> None:
        """
         Set the tc query criteria name
        """
        pass
    def SetQueryCriteriaValue(self, index: int, queryCriteriaValue: str) -> None:
        """
         Set the tc query criteria value
        """
        pass
    def SetQueryName(self, queryName: str) -> None:
        """
         Set the tc query name
        """
        pass
import NXOpen
import NXOpen.Diagramming
class TeeJunctionBuilder(MultipleObjectsBuilder): 
    """ JA class for creating Tee Junction"""
    def CreateTeeJunctionDiagramNode(self) -> NXOpen.Diagramming.Node:
        """
         Create TeeJunction node. 
         Returns nodeObject ( NXOpen.Diagramming.Node): .
        """
        pass
    def SetContextConnectionData(self, contextConnectionPort: NXOpen.Diagramming.Port, p2dBendPoints: List[NXOpen.Point2d]) -> None:
        """
         Set Context Connection's Start Port and it's Bend Points. 
        """
        pass
    def SetContextConnectionPortAndBendPoints(self, contextConnectionPort: AMEExtendedObject, p2dBendPoints: List[NXOpen.Point2d]) -> None:
        """
         Set Context Connection's Start Port and it's Bend Points.
                This is deprecated no longer should be used for future use cases
        """
        pass
    def SetLocation(self, locationX: float, locationY: float) -> None:
        """
         Set Location of TeeJunction on Target Connection 
        """
        pass
    def SetOwningSheet(self, owningSheet: NXOpen.Diagramming.Sheet) -> None:
        """
         Set TeeJunction's owning sheet 
        """
        pass
    def SetTargetConnection(self, targetConnection: NXOpen.Diagramming.Connection) -> None:
        """
         Set Target Connection where TeeJunction must be created. 
        """
        pass
    def SetTargetSegmentId(self, segmentID: int) -> None:
        """
         Set Target Connection's segmentId 
        """
        pass
    def SetTeeJunctionType(self, junctionType: AmeTeeJunctionType) -> None:
        """
         Set TeeJunction type. 
        """
        pass
    def SetTeeJunctionVariant(self, variantIndex: AmeTeeJunctionVariant) -> None:
        """
         Set TeeJunction variant. 
        """
        pass
class TelegramType(Enum):
    """
    Members Include: 
     |Extension| 
     |Supplementary| 
     |Torque| 
     |SafetyTintegrated| 
     |Main| 

    """
    Extension: int
    Supplementary: int
    Torque: int
    SafetyTintegrated: int
    Main: int
    @staticmethod
    def ValueOf(value: int) -> TelegramType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class TemplateData(BasicTemplateData): 
    """ JA class for the Template Data object"""
    @property
    def DefaultSolutionTemplate(self) -> BasicTemplateData:
        """
        Getter for property: ( BasicTemplateData NXOp) DefaultSolutionTemplate
         Returns  the default solution template   
            
         
        """
        pass
    @DefaultSolutionTemplate.setter
    def DefaultSolutionTemplate(self, solutionTemplate: BasicTemplateData):
        """
        Setter for property: ( BasicTemplateData NXOp) DefaultSolutionTemplate
         Returns  the default solution template   
            
         
        """
        pass
    def MoveDownSolutionTemplate(self, solutionTemplate: BasicTemplateData) -> None:
        """
          Method to move down solution template 
        """
        pass
    def MoveUpSolutionTemplate(self, solutionTemplate: BasicTemplateData) -> None:
        """
          Method to move up solution template 
        """
        pass
    def RemoveSolutionTemplates(self, solutionTemplates: List[BasicTemplateData]) -> None:
        """
          Method to remove the solution template from the template data 
        """
        pass
class TemplateVariantSelection(AMEExtendedObject): 
    """ JA class for the Template Variant Selection object"""
    @property
    def DefaultVariant(self) -> TemplateVariant:
        """
        Getter for property: ( TemplateVariant NXOp) DefaultVariant
         Returns the default variant   
            
         
        """
        pass
    @DefaultVariant.setter
    def DefaultVariant(self, defaultVariant: TemplateVariant):
        """
        Setter for property: ( TemplateVariant NXOp) DefaultVariant
         Returns the default variant   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the variant selection description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the variant selection description   
            
         
        """
        pass
    @property
    def IsMandatory(self) -> bool:
        """
        Getter for property: (bool) IsMandatory
         Returns the variant selection necessity option   
            
         
        """
        pass
    @IsMandatory.setter
    def IsMandatory(self, isMandatory: bool):
        """
        Setter for property: (bool) IsMandatory
         Returns the variant selection necessity option   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the variant selection name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the variant selection name   
            
         
        """
        pass
    def CreateVariant(self) -> TemplateVariant:
        """
          Method to create a variant 
         Returns createdVariant ( TemplateVariant NXOp): .
        """
        pass
class TemplateVariant(AMEExtendedObject): 
    """ JA class for the Template Variant object"""
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the variant description   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the variant description   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the variant name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the variant name   
            
         
        """
        pass
import NXOpen
class TerminalReportSettings(NXOpen.NXObject): 
    """ JA class for the TerminalReportSettings object"""
    pass
import NXOpen
class TiaPortalProjectSettingsBuilder(NXOpen.Builder): 
    """ TiaPortalProjectSettingsBuilder """
    class TiaPortalVersionType(Enum):
        """
        Members Include: 
         |V14Sp1| 
         |V15| 
         |V151| 
         |V16| 
         |V17| 
         |V18| 
         |V19| 

        """
        V14Sp1: int
        V15: int
        V151: int
        V16: int
        V17: int
        V18: int
        V19: int
        @staticmethod
        def ValueOf(value: int) -> TiaPortalProjectSettingsBuilder.TiaPortalVersionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def TiaPortalVersion(self) -> TiaPortalProjectSettingsBuilder.TiaPortalVersionType:
        """
        Getter for property: ( TiaPortalProjectSettingsBuilder.TiaPortalVersionType NXOp) TiaPortalVersion
         Returns the current tia portal version   
            
         
        """
        pass
    @TiaPortalVersion.setter
    def TiaPortalVersion(self, version: TiaPortalProjectSettingsBuilder.TiaPortalVersionType):
        """
        Setter for property: ( TiaPortalProjectSettingsBuilder.TiaPortalVersionType NXOp) TiaPortalVersion
         Returns the current tia portal version   
            
         
        """
        pass
    def AddExternalLibraryAlias(self, libraryAlias: str, filePath: str) -> None:
        """
         Add an external library alias 
        """
        pass
    def ClearExternalLibraryAliases(self) -> None:
        """
         Clear external library aliases 
        """
        pass
    def GetExternalLibraryAlias(self, index: int) -> Tuple[str, str]:
        """
         Get an external library alias by index 
         Returns A tuple consisting of (libraryAlias, filePath). 
         - libraryAlias is: str.
         - filePath is: str.

        """
        pass
    def GetExternalLibraryAliasCount(self) -> int:
        """
         Get count of external library aliases 
         Returns count (int): .
        """
        pass
import NXOpen
class TiaPortalProjectSettings(NXOpen.NXObject): 
    """ Tia Portal project settings node journaling class """
    pass
import NXOpen
class TransferFileDataBuilder(MultipleObjectsBuilder): 
    """ Imports a new one or updates the existing configuration in AD Upstream Data Navigator from the external file. """
    @property
    def FileToImport(self) -> str:
        """
        Getter for property: (str) FileToImport
         Returns the excel file which is being imported   
            
         
        """
        pass
    @FileToImport.setter
    def FileToImport(self, fileToImport: str):
        """
        Setter for property: (str) FileToImport
         Returns the excel file which is being imported   
            
         
        """
        pass
    @property
    def NodeToUpdate(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) NodeToUpdate
         Returns the node which needs to update during import operation   
            
         
        """
        pass
    def ValidateAndPopulateExcelData(self) -> None:
        """
         Validate and populate excel import data. This should be called prior to commit. 
        """
        pass
class TypedProductComponentInstance(TypedProductComponent): 
    """ Product Component Instance class """
    pass
class TypedProductComponent(ProductComponent): 
    """ Typed Product Component class """
    pass
import NXOpen
class TypeMappingBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TypeMappingBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TypeMappingBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: TypeMappingBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TypeMappingBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TypeMappingBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TypeMappingBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TypeMappingBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TypeMappingBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( TypeMappingBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TypeMappingBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[TypeMappingBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: TypeMappingBuilder, object2: TypeMappingBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Tooling
class TypeMappingBuilder(NXOpen.Builder): 
    """ JA class for the type mapping dialog"""
    @property
    def AdType(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) AdType
         Returns the ad type selection  
            
         
        """
        pass
    @property
    def LdType(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) LdType
         Returns the ld type selection  
            
         
        """
        pass
    def Load(self, ldPath: str) -> Tuple[str, str]:
        """
         Load new type mapping base on part 
         Returns A tuple consisting of (adPath, adDescriptiveName). 
         - adPath is: str.
         - adDescriptiveName is: str.

        """
        pass
import NXOpen
class TypeMappingListBuilder(NXOpen.Builder): 
    """ Type Mapping List Builder """
    @property
    def List(self) -> TypeMappingBuilderList:
        """
        Getter for property: ( TypeMappingBuilderList NXOp) List
         Returns the pair list   
            
         
        """
        pass
    def CreateTypeMapping(self) -> TypeMappingBuilder:
        """
         Create a new type mapping 
         Returns mappingBuilder ( TypeMappingBuilder NXOp): .
        """
        pass
    def DeleteTypeMapping(self, mappingBuilder: TypeMappingBuilder) -> None:
        """
         Delete type mapping 
        """
        pass
    def LoadAd(self, adPath: str) -> List[TypeMappingBuilder]:
        """
         Loads the Ld types linked to the given AD type
         Returns builders ( TypeMappingBuilder List[NX): .
        """
        pass
    def LoadAllLdTypes(self) -> List[TypeMappingBuilder]:
        """
         Loads the Ld types in the project
         Returns builders ( TypeMappingBuilder List[NX): .
        """
        pass
class TypeRoot(AMEBaseNode): 
    """ Type Root Node class """
    pass
import NXOpen
class UnloadLineDesignerBuilder(NXOpen.Builder): 
    """ JA class for the insert UnloadLineDesigner dialog"""
    @property
    def SelectionObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionObjects
         Returns the selected objects  
            
         
        """
        pass
import NXOpen
class UpdateLibraryObjectsBuilder(NXOpen.Builder): 
    """ Class to define Update Library Objects """
    @property
    def SelectAll(self) -> bool:
        """
        Getter for property: (bool) SelectAll
         Returns the select all option of update objects builder  
            
         
        """
        pass
    @SelectAll.setter
    def SelectAll(self, selectAll: bool):
        """
        Setter for property: (bool) SelectAll
         Returns the select all option of update objects builder  
            
         
        """
        pass
    @property
    def SelectType(self) -> str:
        """
        Getter for property: (str) SelectType
         Returns the input type   
            
         
        """
        pass
    @SelectType.setter
    def SelectType(self, type: str):
        """
        Setter for property: (str) SelectType
         Returns the input type   
            
         
        """
        pass
    @property
    def SelectTypeRevision(self) -> str:
        """
        Getter for property: (str) SelectTypeRevision
         Returns the input type revision  
            
         
        """
        pass
    @SelectTypeRevision.setter
    def SelectTypeRevision(self, typeRevision: str):
        """
        Setter for property: (str) SelectTypeRevision
         Returns the input type revision  
            
         
        """
        pass
    def GetObjectsToUpdate(self) -> List[NXOpen.NXObject]:
        """
         Get objects to update
         Returns objectsToUpdate ( NXOpen.NXObject Li): .
        """
        pass
    def LoadTargetTypeRevision(self, typeRevision: str) -> NXOpen.NXObject:
        """
         Load target revision part
         Returns loadedObject ( NXOpen.NXObject): .
        """
        pass
    def SetObjectsToUpdate(self, objectsToUpdate: List[NXOpen.NXObject]) -> None:
        """
         Set objects to update
        """
        pass
import NXOpen
import NXOpen.Tooling
class UpdateObjectsBuilder(NXOpen.Builder): 
    """ Class to define Update Objects """
    class ObjectType(Enum):
        """
        Members Include: 
         |Engobject| 
         |Product| 
         |Symbol| 

        """
        Engobject: int
        Product: int
        Symbol: int
        @staticmethod
        def ValueOf(value: int) -> UpdateObjectsBuilder.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Definition| 
         |Query| 

        """
        Definition: int
        Query: int
        @staticmethod
        def ValueOf(value: int) -> UpdateObjectsBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ReuseLibraryItem(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) ReuseLibraryItem
         Returns the selection update objects builder  
            
         
        """
        pass
    @property
    def SelectAll(self) -> bool:
        """
        Getter for property: (bool) SelectAll
         Returns the select all option of update objects builder  
            
         
        """
        pass
    @SelectAll.setter
    def SelectAll(self, selectAll: bool):
        """
        Setter for property: (bool) SelectAll
         Returns the select all option of update objects builder  
            
         
        """
        pass
    @property
    def SelectionBaseDefinition(self) -> SelectionBaseDefinitionBuilder:
        """
        Getter for property: ( SelectionBaseDefinitionBuilder NXOp) SelectionBaseDefinition
         Returns the selection update objects builder  
            
         
        """
        pass
    @property
    def TargetRevision(self) -> str:
        """
        Getter for property: (str) TargetRevision
         Returns the target revision of update objects builder  
            
         
        """
        pass
    @TargetRevision.setter
    def TargetRevision(self, targetRevisionName: str):
        """
        Setter for property: (str) TargetRevision
         Returns the target revision of update objects builder  
            
         
        """
        pass
    @property
    def Type(self) -> UpdateObjectsBuilder.Types:
        """
        Getter for property: ( UpdateObjectsBuilder.Types NXOp) Type
         Returns the input type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: UpdateObjectsBuilder.Types):
        """
        Setter for property: ( UpdateObjectsBuilder.Types NXOp) Type
         Returns the input type   
            
         
        """
        pass
    def AddObjectToUpdate(self, objectToUpdate: NXOpen.NXObject) -> None:
        """
         Add the object to update
        """
        pass
    def LoadAllObjectsUsingQuery(self, queryObject: AMEQuery) -> List[AMEExtendedObject]:
        """
         Load all objects of selected query 
         Returns loadedObjects ( AMEExtendedObject List[NX): .
        """
        pass
    def LoadAllObjectsUsingType(self, selectionType: str) -> List[AMEExtendedObject]:
        """
         Load all objects of selected type 
         Returns loadedObjects ( AMEExtendedObject List[NX): .
        """
        pass
    def SetSourceEngineeringObjectDefinition(self, sourceDefinition: str) -> None:
        """
        Sets the source eo def
        """
        pass
class UpstreamDataRoot(AMEBaseNode): 
    """ UpstreamData Root Node class """
    pass
import NXOpen
class ValueSetBuilder(NXOpen.Builder): 
    """ Manages the value set by allowing them to be created and add new values """
    @property
    def BreakUnLockedTemplate(self) -> bool:
        """
        Getter for property: (bool) BreakUnLockedTemplate
         Returns  the option to exchange product by breaking unlocked template  
            
         
        """
        pass
    @BreakUnLockedTemplate.setter
    def BreakUnLockedTemplate(self, breakUnLockedTemplate: bool):
        """
        Setter for property: (bool) BreakUnLockedTemplate
         Returns  the option to exchange product by breaking unlocked template  
            
         
        """
        pass
    @property
    def ExchangePLCRelevantProduct(self) -> bool:
        """
        Getter for property: (bool) ExchangePLCRelevantProduct
         Returns  the option to exchange PLC relevant product on applying of value set   
            
         
        """
        pass
    @ExchangePLCRelevantProduct.setter
    def ExchangePLCRelevantProduct(self, exchangePLCRelevantProduct: bool):
        """
        Setter for property: (bool) ExchangePLCRelevantProduct
         Returns  the option to exchange PLC relevant product on applying of value set   
            
         
        """
        pass
    @property
    def SelectedTemplateMembers(self) -> SelectAMEBaseNodeList:
        """
        Getter for property: ( SelectAMEBaseNodeList NXOp) SelectedTemplateMembers
         Returns  the template instances   
            
         
        """
        pass
    def AddEplanPropertyToValueSet(self, valueSet: NXOpen.NXObject, propertyOwner: NXOpen.NXObject, propertyName: str, propertyCategory: str, eplanValueSet: NXOpen.NXObject, placeHolderName: str, isNewPlaceHolder: bool) -> NXOpen.NXObject:
        """
          The method  to allow a new property to be added to the eplan value set 
         Returns valueSetPropertyOwner ( NXOpen.NXObject): .
        """
        pass
    def AddOrUpdateProductSelection(self, owningValueSet: NXOpen.NXObject, inputDevices: List[AMEEngObject], mainProductPart: str, auxliaryProductParts: List[str]) -> None:
        """
          The method  to add or update product selection 
        """
        pass
    def AddPropertyToValueSet(self, valueSet: NXOpen.NXObject, propertyOwner: NXOpen.NXObject, propertyName: str, propertyCategory: str) -> NXOpen.NXObject:
        """
          The method  to allow a new property to be added to the value set 
         Returns valueSetPropertyOwner ( NXOpen.NXObject): .
        """
        pass
    def ApplyValueSetInProject(self, valueSet: NXOpen.NXObject) -> List[NXOpen.NXObject]:
        """
          Method to apply value set in a project environment 
         Returns createdObjects ( NXOpen.NXObject Li): .
        """
        pass
    def ApplyValueSetInTemplate(self, valueSet: NXOpen.NXObject) -> List[NXOpen.NXObject]:
        """
          Method to apply value set 
         Returns createdObjects ( NXOpen.NXObject Li): .
        """
        pass
    def CreateValueSet(self, valueSetGroup: NXOpen.NXObject) -> NXOpen.NXObject:
        """
          The method allows the value set to be created 
         Returns createdValueSet ( NXOpen.NXObject): .
        """
        pass
    def CreateValueSetGroup(self) -> NXOpen.NXObject:
        """
          The method allows the value set group to be created 
         Returns createdValueSetGroup ( NXOpen.NXObject): .
        """
        pass
    def DeleteValueSetGroups(self, objects: List[NXOpen.NXObject]) -> None:
        """
          Method to delete existing value set groups 
        """
        pass
    def DeleteValueSetProperties(self, properties: List[NXOpen.NXObject]) -> None:
        """
          Method to delete existing value set properties 
        """
        pass
    def DeleteValueSetPropertyOwners(self, propertyOwners: List[NXOpen.NXObject]) -> None:
        """
          Method to delete existing value set property owners 
        """
        pass
    def DeleteValueSets(self, objects: List[NXOpen.NXObject]) -> None:
        """
          Method to delete existing value sets 
        """
        pass
    def GetValueSetConditionExpression(self, valueSetGroup: NXOpen.NXObject) -> NXOpen.NXObject:
        """
          Method to get the condition expression for the value set group 
         Returns conditionExpression ( NXOpen.NXObject): .
        """
        pass
    def GetValueSetGroupsInTemplate(self) -> List[NXOpen.NXObject]:
        """
          Method to get value sets in selected template 
         Returns valueSetGroups ( NXOpen.NXObject Li): .
        """
        pass
    def GetValueSetObjects(self, project: Project) -> List[NXOpen.NXObject]:
        """
         Get value set objects from given template project 
         Returns valueSetObjects ( NXOpen.NXObject Li): .
        """
        pass
    def GetValueSetsInTemplate(self) -> List[NXOpen.NXObject]:
        """
          Method to get value sets in selected template 
         Returns valueSets ( NXOpen.NXObject Li): .
        """
        pass
    def PasteValueSetObjects(self) -> List[NXOpen.NXObject]:
        """
          Pastes copied value set objects 
         Returns copiedObjects ( NXOpen.NXObject Li): .
        """
        pass
    def RemoveProductSelection(self, propertyOwners: List[NXOpen.NXObject]) -> None:
        """
          Method to remove assigned main and auxiliary product selection from property owners 
        """
        pass
    def SetAsDefault(self, valueSet: NXOpen.NXObject) -> None:
        """
          A method that allows the value set to be used as default for a variant 
        """
        pass
    def SetValueSetConditionExpression(self, valueSetGroup: NXOpen.NXObject, conditionExpression: NXOpen.NXObject) -> None:
        """
          Method to set the condition expression on the value set group 
        """
        pass
    def SetValueSetGroupName(self, valueSetGroupObject: NXOpen.NXObject, newName: str) -> None:
        """
          Method to set name of the value set group 
        """
        pass
    def SetValueSetName(self, valueSetObject: NXOpen.NXObject, newName: str) -> None:
        """
          Method to set name of the value set 
        """
        pass
    def SetValueSetObjectsToCopy(self, objects: List[NXOpen.NXObject]) -> None:
        """
          Sets all value set objects to be copied 
        """
        pass
class VariableInterfaceMemberPort(InterfaceMemberPort): 
    """ VariableInterfaceMemberPort Journaling class """
    pass
