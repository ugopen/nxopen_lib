from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CadManager(NXOpen.Object): 
    """ Represents the Stage Model CAD Manager class."""
    pass
import NXOpen
class CharacteristicAuditResult(NXOpen.NXObject): 
    """ Represents a Characteristic audit result object. """
    def GetStageSet(self) -> StageSet:
        """
         Returns stage set associated with audit result
         Returns stageSet ( StageSet NXOpen.S): .
        """
        pass
    def GetTimeStamp(self) -> int:
        """
         Returns date and time the audit was created or updated.
                   The time stamp is number of seconds since the UNIX epoch (midnight GMT, 1 January 1970).
                 
         Returns timeStamp (int): .
        """
        pass
    def GetUnusedDesignCharacteristicInstances(self) -> List[NXOpen.NXObject]:
        """
         Returns list of unused design characteristic instances
         Returns instances ( NXOpen.NXObject Li):  List of Product Characteristic Instances .
        """
        pass
import NXOpen
class ChrObjectStateManager(NXOpen.BaseObjectStateManager): 
    """ Represents Stage Model characteristic object state manager which manages state of reused, wave-linked, copied objects.
    """
    pass
import NXOpen.Tooling
class DeriveStockBuilder(NXOpen.Tooling.StockSizeBuilder): 
    """ Represents a StageModel.Stage builder """
    @property
    def StockStageDetails(self) -> StockStageDetailsBuilder:
        """
        Getter for property: ( StockStageDetailsBuilder NXOpen.S) StockStageDetails
         Returns the Stock Stage Detaild Builder as  StageModel::StockStageDetailsBuilder    
            
         
        """
        pass
    @StockStageDetails.setter
    def StockStageDetails(self, stageDetails: StockStageDetailsBuilder):
        """
        Setter for property: ( StockStageDetailsBuilder NXOpen.S) StockStageDetails
         Returns the Stock Stage Detaild Builder as  StageModel::StockStageDetailsBuilder    
            
         
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents the Stage Model Manager class."""
    @property
    def ObjectUpdateStateManager() -> ObjectUpdateStateManager:
        """
         Returns the  NXOpen::StageModel::ObjectUpdateStateManager  belonging to this manager 
        """
        pass
    def AuditCharacteristics(stageSet: StageSet) -> CharacteristicAuditResult:
        """
         Generate a characteristic audit result for stage set.
         Returns auditResult ( CharacteristicAuditResult NXOpen.S): .
        """
        pass
    def ClearCharacteristicsAuditResult(stageSet: StageSet) -> None:
        """
         Clear a characteristic audit result for stage set.
        """
        pass
    def CreateChrObjectStateManager() -> ChrObjectStateManager:
        """
         Creates Stage Model characteristic object state manager 
         Returns manager ( ChrObjectStateManager NXOpen.S): .
        """
        pass
    def CreateDeriveStockBuilder(part: NXOpen.Part, stage: Stage) -> DeriveStockBuilder:
        """
         Creates a StageModel.DeriveStockBuilder 
         Returns builder ( DeriveStockBuilder NXOpen.S): .
        """
        pass
    def CreateObjectStateManager() -> ObjectStateManager:
        """
         Creates Stage Model object state manager 
         Returns manager ( ObjectStateManager NXOpen.S): .
        """
        pass
    def CreateOrientStockBuilder(part: NXOpen.Part, stage: Stage, sourceFileName: str) -> OrientStockBuilder:
        """
         Creates a StageModel.OrientStockBuilder 
         Returns builder ( OrientStockBuilder NXOpen.S): .
        """
        pass
    def CreatePositionComponentBuilder(part: NXOpen.Part) -> PositionComponentBuilder:
        """
         Creates Stage Model position component builder 
         Returns builder ( PositionComponentBuilder NXOpen.S): .
        """
        pass
    def CreateReferenceStockAssembly() -> Stage:
        """
         Creates a StageModel.Stage object in an active stage set and activates the stage created
         Returns stockAssembly ( Stage NXOpen.S): .
        """
        pass
    def CreateReferenceStockBuilder(part: NXOpen.Part, stage: Stage, sourceFileName: str) -> ReferenceStockBuilder:
        """
         Creates a StageModel.ReferenceStockBuilder 
         Returns builder ( ReferenceStockBuilder NXOpen.S): .
        """
        pass
    def CreateReplacePartBuilder(part: NXOpen.Part) -> ReplacePartBuilder:
        """
         Creates a StageModel.ReplacePartBuilder 
         Returns builder ( ReplacePartBuilder NXOpen.S): .
        """
        pass
    def CreateStageBuilder(part: NXOpen.Part, stage: Stage) -> StageBuilder:
        """
         Creates a StageModel.StageBuilder 
         Returns builder ( StageBuilder NXOpen.S): .
        """
        pass
    def CreateStageSetBuilder(part: NXOpen.Part, stageSet: StageSet) -> StageSetBuilder:
        """
         Creates a StageModel.StageSetBuilder 
         Returns builder ( StageSetBuilder NXOpen.S): .
        """
        pass
    def CreateStandardStockBuilder(part: NXOpen.Part, stage: Stage, surceFileName: str) -> StandardStockBuilder:
        """
         Creates a StageModel.StandardStockBuilder 
         Returns builder ( StandardStockBuilder NXOpen.S): .
        """
        pass
    def CreateStockStageDetailsBuilder(part: NXOpen.Part, stagedetails: StockStageDetails) -> StockStageDetailsBuilder:
        """
         Creates a StageModel.StockStageDetailsBuilder 
         Returns builder ( StockStageDetailsBuilder NXOpen.S): .
        """
        pass
    def GetActiveStage() -> Stage:
        """
         Get the active stage 
         Returns activeStage ( Stage NXOpen.S): .
        """
        pass
    def GetActiveStageSet() -> StageSet:
        """
         Get the active stage set 
         Returns activeStageSet ( StageSet NXOpen.S): .
        """
        pass
    def GetLoadedStageSets() -> List[StageSet]:
        """
         Get loaded stage sets 
         Returns stageSets ( StageSet List[NXOpen): .
        """
        pass
    def ReuseCharacteristics(stage: Stage) -> None:
        """
         Reuse all characteristic for stage.
        """
        pass
import NXOpen
import NXOpen.Annotations
class MapGeometryBuilder(NXOpen.Builder): 
    """ Represents a  NXOpen.StageModel.MapGeometryBuilder."""
    @property
    def Pmi(self) -> NXOpen.Annotations.PmiInterpartSelectionBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PmiInterpartSelectionBuilder) Pmi
         Returns the pmi   
            
         
        """
        pass
    def Add(self, sourceGeometry: NXOpen.DisplayableObject, mappedGeometry: NXOpen.DisplayableObject) -> None:
        """
         Adds the mapping of the source geometry to mapped geometry 
        """
        pass
    def Remove(self, sourceGeometry: NXOpen.DisplayableObject) -> None:
        """
         Removes the mapping of source geometry 
        """
        pass
import NXOpen
class ObjectStateManager(NXOpen.BaseObjectStateManager): 
    """ Represents Stage Model object state manager which manages state of reused, wave-linked, copied objects.
    """
    pass
import NXOpen
class ObjectUpdateStateManager(NXOpen.Object): 
    """ Provides interface for objtects up to date status. """
    class Status(Enum):
        """
        Members Include: 
         |InvalidUpToDate| 
         |UpToDate| 
         |UpToDateToOodParent| 
         |OutOfDateCannotUpdate| 
         |Failed| 
         |OutOfDateCanUpdate| 
         |NoState| 
         |UpdateFrozen| 
         |ParentNotLoaded| 
         |InterPartAssoBroken| 

        """
        InvalidUpToDate: int
        UpToDate: int
        UpToDateToOodParent: int
        OutOfDateCannotUpdate: int
        Failed: int
        OutOfDateCanUpdate: int
        NoState: int
        UpdateFrozen: int
        ParentNotLoaded: int
        InterPartAssoBroken: int
        @staticmethod
        def ValueOf(value: int) -> ObjectUpdateStateManager.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetStatus(objectValue: NXOpen.TaggedObject) -> ObjectUpdateStateManager.Status:
        """
         Get up to date status of the object.
         Returns upTodateStatus ( ObjectUpdateStateManager.Status NXOpen.S): .
        """
        pass
    def MakeUpToDate(objects: List[NXOpen.TaggedObject], undoMarkId: int) -> None:
        """
         Updates all given out-of-date objects to make them up to date 
        """
        pass
import NXOpen
class OrientStockBuilder(NXOpen.Builder): 
    """
    Represents a builder class that performs add existing component operation in current context.
    Context can be Assembly.
    """
    @property
    def LinkGeometrySource(self) -> str:
        """
        Getter for property: (str) LinkGeometrySource
         Returns the orient stock part   
            
         
        """
        pass
    @LinkGeometrySource.setter
    def LinkGeometrySource(self, linkGeometrySource: str):
        """
        Setter for property: (str) LinkGeometrySource
         Returns the orient stock part   
            
         
        """
        pass
    @property
    def PositionComponent(self) -> PositionComponentBuilder:
        """
        Getter for property: ( PositionComponentBuilder NXOpen.S) PositionComponent
         Returns the Position Component Builder   
            
         
        """
        pass
    @PositionComponent.setter
    def PositionComponent(self, positionComponenet: PositionComponentBuilder):
        """
        Setter for property: ( PositionComponentBuilder NXOpen.S) PositionComponent
         Returns the Position Component Builder   
            
         
        """
        pass
    @property
    def ReferenceStock(self) -> ReferenceStockBuilder:
        """
        Getter for property: ( ReferenceStockBuilder NXOpen.S) ReferenceStock
         Returns the reference stock builder   
            
         
        """
        pass
    @ReferenceStock.setter
    def ReferenceStock(self, stageDetails: ReferenceStockBuilder):
        """
        Setter for property: ( ReferenceStockBuilder NXOpen.S) ReferenceStock
         Returns the reference stock builder   
            
         
        """
        pass
import NXOpen
class PmiManager(NXOpen.Object): 
    """ Represents the Stage Model PMI Manager class."""
    def CreateMapGeometryBuilder(stage: Stage) -> MapGeometryBuilder:
        """
         Creates a StageModel.MapGeometryBuilder 
         Returns builder ( MapGeometryBuilder NXOpen.S): .
        """
        pass
    def CreateReusePmiBuilder(stage: Stage) -> ReusePmiBuilder:
        """
         Creates a StageModel.ReusePmiBuilder 
         Returns builder ( ReusePmiBuilder NXOpen.S): .
        """
        pass
    def CreateReuseViewBuilder(stage: Stage) -> ReuseViewBuilder:
        """
         Creates a StageModel.ReuseViewBuilder 
         Returns builder ( ReuseViewBuilder NXOpen.S): .
        """
        pass
import NXOpen
import NXOpen.Assemblies.ProductInterface
class PositionComponentBuilder(NXOpen.Builder): 
    """
    Represents a builder class that performs add existing component operation in current context.
    Context can be Assembly or 4GD.   
    """
    class LocationType(Enum):
        """
        Members Include: 
         |Snap|  Snap as initial location type 
         |WorkPartAbsolute|  Absolute of work part as initial location type 
         |DisplayedPartAbsolute|  Absolute of displayed part as initial location type 
         |DisplayedPartWCS|  WCS as initial location type 

        """
        Snap: int
        WorkPartAbsolute: int
        DisplayedPartAbsolute: int
        DisplayedPartWCS: int
        @staticmethod
        def ValueOf(value: int) -> PositionComponentBuilder.LocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAllProductInterfaceObjects(self) -> List[NXOpen.Assemblies.ProductInterface.InterfaceObject]:
        """
         Returns all product interface objects available, sorted by name. One of these can be used as component anchor
         Returns productInterfaceObjects ( NXOpen.Assemblies.ProductInterface.InterfaceObject Li): .
        """
        pass
    def GetComponentAnchor(self) -> NXOpen.Assemblies.ProductInterface.InterfaceObject:
        """
         Returns the component anchor used for adding component
         Returns componentAnchor ( NXOpen.Assemblies.ProductInterface.InterfaceObject): .
        """
        pass
    def GetComponentAndAsssemblyPart(self) -> Tuple[NXOpen.Part, NXOpen.Part]:
        """
         Returns the component anchor used for adding component
         Returns A tuple consisting of (component, assembly). 
         - component is:  NXOpen.Part.
         - assembly is:  NXOpen.Part.

        """
        pass
    def GetInitialLocationAndOrientation(self) -> Tuple[NXOpen.Point, NXOpen.CoordinateSystem]:
        """
         Returns the location and orientation used for adding component
         Returns A tuple consisting of (initialLocation, initialOrientation). 
         - initialLocation is:  NXOpen.Point.
         - initialOrientation is:  NXOpen.CoordinateSystem.

        """
        pass
    def GetInitialLocationType(self) -> PositionComponentBuilder.LocationType:
        """
         Get the initial location type during add component.
         Returns locationType ( PositionComponentBuilder.LocationType NXOpen.S): .
        """
        pass
    def OrientToWCS(self) -> None:
        """
         Orient added components to the WCS 
        """
        pass
    def ResetToSnapped(self) -> None:
        """
         Resets the component to snapped position and orientation 
        """
        pass
    def ReverseZDirection(self) -> None:
        """
         Reverse the Z direction of added components 
        """
        pass
    def RotateAlongZDirection(self) -> None:
        """
         Rotate added components along Z direction by 90 degrees 
        """
        pass
    def SetComponentAnchor(self, componentAnchor: NXOpen.Assemblies.ProductInterface.InterfaceObject) -> None:
        """
         Sets the component anchor to be used for adding component
        """
        pass
    def SetComponentAndAsssemblyPart(self, component: NXOpen.Part, assembly: NXOpen.Part) -> None:
        """
         Sets the component anchor to be used for adding component.
        """
        pass
    def SetInitialLocationAndOrientation(self, initialLocation: NXOpen.Point, initialOrientation: NXOpen.CoordinateSystem) -> None:
        """
         Sets the location and orientation to be used for adding component. Orientation is optional and user can pass .
        """
        pass
    def SetInitialLocationAndOrientationcoords(self, point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3) -> None:
        """
         Sets the location and orientation to be used for add component. Orientation is optional and user can pass .
        """
        pass
    def SetInitialLocationType(self, locationType: PositionComponentBuilder.LocationType) -> None:
        """
         Set the initial location type during add component.
        """
        pass
import NXOpen
class ReferenceStockBuilder(NXOpen.Builder): 
    """ Represents a StageModel.Stage builder """
    @property
    def ReferencePart(self) -> str:
        """
        Getter for property: (str) ReferencePart
         Returns the reference part   
            
         
        """
        pass
    @ReferencePart.setter
    def ReferencePart(self, referencePart: str):
        """
        Setter for property: (str) ReferencePart
         Returns the reference part   
            
         
        """
        pass
    @property
    def StockStageDetails(self) -> StockStageDetailsBuilder:
        """
        Getter for property: ( StockStageDetailsBuilder NXOpen.S) StockStageDetails
         Returns the Stock Stage Details Builder as  StageModel::StockStageDetailsBuilder    
            
         
        """
        pass
    @StockStageDetails.setter
    def StockStageDetails(self, stageDetails: StockStageDetailsBuilder):
        """
        Setter for property: ( StockStageDetailsBuilder NXOpen.S) StockStageDetails
         Returns the Stock Stage Details Builder as  StageModel::StockStageDetailsBuilder    
            
         
        """
        pass
import NXOpen
class ReplacePartBuilder(NXOpen.Builder): 
    """ Represents a StageModel.ReplacePartBuilder."""
    class DesignPartTypes(Enum):
        """
        Members Include: 
         |DesignPart| 
         |ReferencePart| 

        """
        DesignPart: int
        ReferencePart: int
        @staticmethod
        def ValueOf(value: int) -> ReplacePartBuilder.DesignPartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnumDesignReference(self) -> ReplacePartBuilder.DesignPartTypes:
        """
        Getter for property: ( ReplacePartBuilder.DesignPartTypes NXOpen.S) EnumDesignReference
         Returns the enum design reference   
            
         
        """
        pass
    @EnumDesignReference.setter
    def EnumDesignReference(self, enumDesignReference: ReplacePartBuilder.DesignPartTypes):
        """
        Setter for property: ( ReplacePartBuilder.DesignPartTypes NXOpen.S) EnumDesignReference
         Returns the enum design reference   
            
         
        """
        pass
    def SetReferencePart(self, reference: str) -> None:
        """
         Set reference part. 
        """
        pass
    def SetReplacementPart(self, replacementPart: str) -> None:
        """
         Set replacement part. 
        """
        pass
import NXOpen
import NXOpen.Annotations
class ReusePmiBuilder(NXOpen.Builder): 
    """ Represents a  NXOpen.StageModel.ReusePmiBuilder."""
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative setting   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative setting   
            
         
        """
        pass
    @property
    def DestinationStage(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) DestinationStage
         Returns the destination stage   
            
         
        """
        pass
    @DestinationStage.setter
    def DestinationStage(self, destinationStage: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) DestinationStage
         Returns the destination stage   
            
         
        """
        pass
    @property
    def IncludeCharacteristic(self) -> bool:
        """
        Getter for property: (bool) IncludeCharacteristic
         Returns the include characteristic setting   
            
         
        """
        pass
    @IncludeCharacteristic.setter
    def IncludeCharacteristic(self, reuseCharacteristic: bool):
        """
        Setter for property: (bool) IncludeCharacteristic
         Returns the include characteristic setting   
            
         
        """
        pass
    @property
    def ReusePMI(self) -> NXOpen.Annotations.PmiInterpartSelectionBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PmiInterpartSelectionBuilder) ReusePMI
         Returns the list of selected PMI to be re-used   
            
         
        """
        pass
    def GetPmiParent(self, child: NXOpen.TaggedObject) -> None:
        """
         The parent of a reused PMI 
        """
        pass
    def GetReusedCharacteristicInstance(self, referencedObject: NXOpen.TaggedObject) -> NXOpen.NXObject:
        """
         Return the reused characteristic Instance referrenced by reference object, such as PMI. 
         Returns reusedCharacteristicInstance ( NXOpen.NXObject):  reused Characteristic Instance .
        """
        pass
    def RemoveReusedCharacteristicInstance(self, referencedObject: NXOpen.TaggedObject) -> None:
        """
         Remove the reused characteristic Instance from the referrenced object. 
        """
        pass
import NXOpen
class ReuseViewBuilder(NXOpen.Builder): 
    """ Represents a  NXOpen.StageModel.ReuseViewBuilder."""
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative setting   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative setting   
            
         
        """
        pass
    @property
    def IncludeCharacteristic(self) -> bool:
        """
        Getter for property: (bool) IncludeCharacteristic
         Returns the include characteristic setting   
            
         
        """
        pass
    @IncludeCharacteristic.setter
    def IncludeCharacteristic(self, reuseCharacteristic: bool):
        """
        Setter for property: (bool) IncludeCharacteristic
         Returns the include characteristic setting   
            
         
        """
        pass
    @property
    def IncludePmi(self) -> bool:
        """
        Getter for property: (bool) IncludePmi
         Returns the include pmi setting   
            
         
        """
        pass
    @IncludePmi.setter
    def IncludePmi(self, includePmi: bool):
        """
        Setter for property: (bool) IncludePmi
         Returns the include pmi setting   
            
         
        """
        pass
    def GetSelectedViews(self) -> List[NXOpen.View]:
        """
         The selected views 
         Returns selectedViews ( NXOpen.View Li): .
        """
        pass
    def SetSelectedViews(self, selectedViews: List[NXOpen.View]) -> None:
        """
         The selected views 
        """
        pass
import NXOpen
import NXOpen.ModlUtils
import NXOpen.PDM
class StageBuilder(NXOpen.Builder): 
    """ Represents a StageModel.StageBuilder. """
    class StgaePartType(Enum):
        """
        Members Include: 
         |NewPart| 
         |ExistingPart| 

        """
        NewPart: int
        ExistingPart: int
        @staticmethod
        def ValueOf(value: int) -> StageBuilder.StgaePartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateStage(self, stageSet: StageSet, stageBefore: Stage, stageName: str, stageDescription: str) -> Stage:
        """
         Create a new stage in the specified staged model set and append it to the stage before, or in front of the staged model set list if no stage before is given
         Returns createdStage ( Stage NXOpen.S): .
        """
        pass
    def EditStageDescription(self, stageDescription: str) -> None:
        """
         Edit builder stage's description 
        """
        pass
    def EditStageName(self, stageName: str) -> None:
        """
         Edit builder stage's name
        """
        pass
    def RegisterImportTemplatePartObject(self, templateBuilder: NXOpen.ModlUtils.ImportTemplatePartBuilder) -> None:
        """
         Registers the import template part object 
        """
        pass
    def ReorderStage(self, stageBefore: Stage) -> None:
        """
         Place the builder stage behind the stage before, or in front of the staged model set list if no stage before is given
        """
        pass
    def SetNameOnPartOperationBuilder(self, stageSetName: str) -> None:
        """
         Update the name of the Object from the template 
        """
        pass
    def SetPartOperationCreateBuilder(self, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
import NXOpen
import NXOpen.ModlUtils
import NXOpen.PDM
class StageSetBuilder(NXOpen.Builder): 
    """ Represents a StageModel.StageSetBuilder """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the stage set name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the stage set name   
            
         
        """
        pass
    def CreateManagedStageSet(self, designPart: NXOpen.Part, stageSetName: str, stageSetLocation: str, numOfStages: int) -> StageSet:
        """
         Create a managed staged model set with the specified name and number of stages at the specified location
         Returns createdStageSet ( StageSet NXOpen.S): .
        """
        pass
    def CreateNativeStageSet(self, designPart: NXOpen.Part, stageSetName: str, numOfStages: int) -> StageSet:
        """
         Create a native staged model set with the specified name and number of stages in the directory of the design part
         Returns createdStageSet ( StageSet NXOpen.S): .
        """
        pass
    def EditStageSetName(self, stageSetName: str) -> None:
        """
         Edit builder staged model set's name
        """
        pass
    def RegisterImportTemplatePartObject(self, templateBuilder: NXOpen.ModlUtils.ImportTemplatePartBuilder) -> None:
        """
         Registers the import template part object 
        """
        pass
    def SetDesingPart(self, designPart: NXOpen.Part) -> None:
        """
         Registers the import template part object 
        """
        pass
    def SetNameOnPartOperationBuilder(self, stageSetName: str) -> None:
        """
         Update the name of the Object from the template 
        """
        pass
    def SetPartOperationCreateBuilder(self, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
import NXOpen
class StageSet(NXOpen.TaggedObject): 
    """ Represents a StageModel.StageSet object. """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the staged model set   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the staged model set   
            
         
        """
        pass
    def ActivateDesignPart(self, displayInNewWindow: bool) -> NXOpen.Part:
        """
         Load and activate the design part of the stage set 
         Returns designPart ( NXOpen.Part): .
        """
        pass
    def DeleteStages(self, stagesToDelete: List[Stage]) -> None:
        """
         Delete the stages from this staged model set
        """
        pass
    def DeleteStagesQuite(self, stagesToDelete: List[Stage]) -> None:
        """
         Delete the stages from this staged model set without any information.
        """
        pass
    def GetDeriveStockStageOfActiveStage(self) -> Stage:
        """
         Get the derive stock stage of the active stage part.
         Returns stockStage ( Stage NXOpen.S): .
        """
        pass
    def GetStageWithName(self, stageName: str) -> Stage:
        """
         Get the stage with the specified name in the staged model set if the stage exists 
         Returns stage ( Stage NXOpen.S): .
        """
        pass
    def GetStages(self, includeStockStage: bool) -> List[Stage]:
        """
         Get the list of stages in the staged model set 
         Returns stages ( Stage List[NXOpen): .
        """
        pass
    def GetStockStage(self) -> Stage:
        """
         Get the stock stage of the stage set 
         Returns stockStage ( Stage NXOpen.S): .
        """
        pass
    def GetStockStages(self) -> List[Stage]:
        """
         Get the list of stock stages in the staged model set 
         Returns stages ( Stage List[NXOpen): .
        """
        pass
    def NativeSaveAs(self, name: str) -> StageSet:
        """
         Save as to save an open stage model set as a new stage model set with a new name in native stage model environment. 
         Returns newStageSet ( StageSet NXOpen.S): .
        """
        pass
    def ReplaceDesignPart(self, replacementPart: NXOpen.Part) -> None:
        """
         Replace the design part of the stage set 
        """
        pass
    def SaveStageSet(self) -> None:
        """
         Save changes made to the staged model set, including all changes made to its stages 
        """
        pass
import NXOpen
class Stage(NXOpen.TaggedObject): 
    """ Represents a StageModel.Stage object."""
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of the stage   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description of the stage   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the stage   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the stage   
            
         
        """
        pass
    def Activate(self, displayInNewWindow: bool) -> None:
        """
         Activate the stage 
        """
        pass
    def IsActive(self) -> bool:
        """
         Whether the stage is active or not 
         Returns isActive (bool): .
        """
        pass
    def Reorder(self, stageBefore: Stage) -> None:
        """
         Place this stage behind the stage before, or in front of the staged model set list if no stage before is given
        """
        pass
    def SaveStageSetOfStage(self) -> None:
        """
         Save changes made to the staged model set of this stage, including all changes made to this stage 
        """
        pass
class StandardStockBuilder(StockStageDetailsBuilder): 
    """ Represents a StageModel.Stage builder """
    pass
import NXOpen
import NXOpen.PDM
class StockStageDetailsBuilder(NXOpen.Builder): 
    """ Represents a StageModel.StockStageDetailsBuilder."""
    @property
    def StockStageName(self) -> str:
        """
        Getter for property: (str) StockStageName
         Returns the stage name   
            
         
        """
        pass
    @StockStageName.setter
    def StockStageName(self, stageName: str):
        """
        Setter for property: (str) StockStageName
         Returns the stage name   
            
         
        """
        pass
    def GetStockStageDescription(self) -> List[str]:
        """
         Returns the stage description 
         Returns stageDescription (List[str]): .
        """
        pass
    def GetStockStageDetails(self) -> StockStageDetails:
        """
         Returns StageModel.StockStageDetails object 
         Returns stagedetails ( StockStageDetails NXOpen.S): .
        """
        pass
    def SetPartOperationCreateBuilder(self, createBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Set the NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
    def SetStockStageDescription(self, stageDescription: List[str]) -> None:
        """
         Sets the stage description 
        """
        pass
import NXOpen
class StockStageDetails(NXOpen.TaggedObject): 
    """ Represents the Stage details class """
    pass
