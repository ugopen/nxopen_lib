from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AbsolutePositionBuilder(NXOpen.Builder): 
    """ Represents a builder class that absolutely positions the specified objects.
    """
    @property
    def AbsolutelyPosition(self) -> bool:
        """
        Getter for property: (bool) AbsolutelyPosition
         Returns the option to know whether the object is absolutely positioned or not
                  
            
         
        """
        pass
    @AbsolutelyPosition.setter
    def AbsolutelyPosition(self, absolutePositioned: bool):
        """
        Setter for property: (bool) AbsolutelyPosition
         Returns the option to know whether the object is absolutely positioned or not
                  
            
         
        """
        pass
    @property
    def ObjectsToAbsolutePosition(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectsToAbsolutePosition
         Returns the object list selected for absolute position   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies.ProductInterface
import NXOpen.PDM
class AddComponentBuilder(NXOpen.Builder): 
    """
    Represents a builder class that performs add existing component operation in current context.
    Context can be Assembly or 4GD.   
    """
    class CamComponentType(Enum):
        """
        Members Include: 
         |Target|  Target type 
         |Resource|  Resource type 
         |Workpiece|  Workpiece type 

        """
        Target: int
        Resource: int
        Workpiece: int
        @staticmethod
        def ValueOf(value: int) -> AddComponentBuilder.CamComponentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
        def ValueOf(value: int) -> AddComponentBuilder.LocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the component name for added components.  
            
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, componentName: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name for added components.  
            
         
        """
        pass
    @property
    def DesignElementType(self) -> str:
        """
        Getter for property: (str) DesignElementType
         Returns the type of a add component  
            
         
        """
        pass
    @DesignElementType.setter
    def DesignElementType(self, deType: str):
        """
        Setter for property: (str) DesignElementType
         Returns the type of a add component  
            
         
        """
        pass
    @property
    def FileNewDescriptor(self) -> NXOpen.FileNew:
        """
        Getter for property: ( NXOpen.FileNew) FileNewDescriptor
         Returns the file new descriptor to identify an added component in 4GD   
            
         
        """
        pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer for added components.  
            
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer for added components.  
            
         
        """
        pass
    @property
    def ReferenceSet(self) -> str:
        """
        Getter for property: (str) ReferenceSet
         Returns the reference set for added components.  
            
         
        """
        pass
    @ReferenceSet.setter
    def ReferenceSet(self, referenceSet: str):
        """
        Setter for property: (str) ReferenceSet
         Returns the reference set for added components.  
            
         
        """
        pass
    def AllowMultipleAssemblyLocations(self) -> bool:
        """
         Gets allow multiple assembly location option for adding components.
         Returns allow (bool): .
        """
        pass
    def GetAllProductInterfaceObjects(self) -> List[NXOpen.Assemblies.ProductInterface.InterfaceObject]:
        """
         Returns all product interface objects available, sorted by name. One of these can be used as component anchor
         Returns productInterfaceObjects ( NXOpen.Assemblies.ProductInterface.InterfaceObject Li): .
        """
        pass
    def GetCamComponentType(self) -> AddComponentBuilder.CamComponentType:
        """
         Get the CAM component type during add component.
         Returns camCompType ( AddComponentBuilder.CamComponentType NXOpen.A): .
        """
        pass
    def GetComponentAnchor(self) -> NXOpen.Assemblies.ProductInterface.InterfaceObject:
        """
         Returns the component anchor used for adding component
         Returns componentAnchor ( NXOpen.Assemblies.ProductInterface.InterfaceObject): .
        """
        pass
    def GetCount(self) -> int:
        """
         Gets the number of components to be added.
         Returns count (int): .
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
    def GetInitialLocationType(self) -> AddComponentBuilder.LocationType:
        """
         Get the initial location type during add component.
         Returns locationType ( AddComponentBuilder.LocationType NXOpen.A): .
        """
        pass
    def GetKeepConstraintsOption(self) -> bool:
        """
         Gets the keep constraints option for added components.
         Returns keepConstraintsOption (bool): .
        """
        pass
    def GetLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns the pre-creation objects 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns the pre-creation objects which have unassign required attributes
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns add component operation failures 
         Returns operationFailures ( NXOpen.ErrorList): .
        """
        pass
    def GetPartsToAdd(self) -> List[NXOpen.BasePart]:
        """
         Returns the parts to be used for adding components
         Returns partsToUse ( NXOpen.BasePart Li): .
        """
        pass
    def GetScatterOption(self) -> bool:
        """
         Gets the scatter option for added components.
         Returns scatterOption (bool): .
        """
        pass
    def OrientToWCS(self) -> None:
        """
         Orient added components to the WCS 
        """
        pass
    def RemoveAddedComponents(self) -> None:
        """
         Removes the components added through add component
        """
        pass
    def RemovePartsFromSelection(self, partsToRemove: List[NXOpen.BasePart]) -> None:
        """
         Removes the specified parts from the selected parts list
        """
        pass
    def ResetPartsToAdd(self) -> None:
        """
         Resets the parts list specified for the add component operation 
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
    def SetAllowMultipleAssemblyLocations(self, allow: bool) -> None:
        """
         Sets allow multiple assembly location option for adding components.
        """
        pass
    def SetCamComponentType(self, camCompType: AddComponentBuilder.CamComponentType) -> None:
        """
         Set the CAM component type during add component.
        """
        pass
    def SetComponentAnchor(self, componentAnchor: NXOpen.Assemblies.ProductInterface.InterfaceObject) -> None:
        """
         Sets the component anchor to be used for adding component
        """
        pass
    def SetCount(self, count: int) -> None:
        """
         Sets the number of components to be added.
        """
        pass
    @overload
    def SetInitialLocationAndOrientation(self, initialLocation: NXOpen.Point, initialOrientation: NXOpen.CoordinateSystem) -> None:
        """
         Sets the location and orientation to be used for adding component. Orientation is optional and user can pass .
        """
        pass
    @overload
    def SetInitialLocationAndOrientation(self, point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3) -> None:
        """
         Sets the location and orientation to be used for add component. Orientation is optional and user can pass .
        """
        pass
    def SetInitialLocationType(self, locationType: AddComponentBuilder.LocationType) -> None:
        """
         Set the initial location type during add component.
        """
        pass
    def SetKeepConstraintsOption(self, keepConstraintsOption: bool) -> None:
        """
         Sets the keep constraints option for added components.
        """
        pass
    def SetPartsToAdd(self, partsToUse: List[NXOpen.BasePart]) -> None:
        """
         Sets the parts to be used for adding components
        """
        pass
    def SetPendingInstance(self, pendingInstance: NXOpen.NXObject) -> None:
        """
         Sets the allocate pending instance at time of instance creation for manage pending component.
        """
        pass
    def SetScatterOption(self, scatterOption: bool) -> None:
        """
         Sets the scatter option for added components.
        """
        pass
    def SetSynchDisplayProperties(self, synchDisplayProperties: bool) -> None:
        """
         Sets the option to synchronize display properties with the component to be added 
        """
        pass
    def SetUseReferenceSetAndApplyInitialLocation(self, useRefSetCSYS: bool) -> None:
        """
        Enables the use of the CSYS transform associated with a reference set in a legacy part and applies it to the position of added component
        """
        pass
import NXOpen
class ArrangementCollection(NXOpen.TaggedObjectCollection): 
    """ a collection of arrangements """
    def Create(self, template_arrangement: Arrangement, name: str) -> Arrangement:
        """
         Creates a standard NXOpen.Assemblies.Arrangement, based on an existing standard NXOpen.Assemblies.Arrangement. 
            
                Note that any NXOpen.Assemblies.ComponentAssembly that contains components will have at least one standard NXOpen.Assemblies.Arrangement. 
                
                See NXOpen.Assemblies.ComponentAssembly.ActiveArrangement.
                Note that the existing NXOpen.Assemblies.Arrangement must not be isolated.
             
         Returns new_arrangement ( Arrangement NXOpen.A):  The new arrangement .
        """
        pass
    def CreateIsolated(self, template_arrangement: Arrangement, name: str) -> Arrangement:
        """
         Creates an isolated NXOpen.Assemblies.Arrangement, based on an existing NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement. 
            
                Note that any NXOpen.Assemblies.ComponentAssembly that contains components will have at least one standard NXOpen.Assemblies.Arrangement. 
                
                See Assemblies.ComponentAssembly.ActiveArrangement.
                Note that the existing NXOpen.Assemblies.Arrangement must not be isolated.
             
         Returns new_arrangement ( Arrangement NXOpen.A):  The new NXOpen.Assemblies.Arrangement.
        """
        pass
    def FindObject(self, journal_identifier: str) -> Arrangement:
        """
         Finds the  NXOpen.Assemblies.Arrangement  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
            An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( Arrangement NXOpen.A):  Arrangement found, or null if no such arrangement exists.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ArrangementsBuilder(NXOpen.TaggedObject): 
    """ Represents an arrangements builder that selects an arrangement
    """
    @property
    def InheritArrangementFromParent(self) -> bool:
        """
        Getter for property: (bool) InheritArrangementFromParent
         Returns the inherit arrangement from parent flag   
            
         
        """
        pass
    @InheritArrangementFromParent.setter
    def InheritArrangementFromParent(self, inheritArrangementFromParent: bool):
        """
        Setter for property: (bool) InheritArrangementFromParent
         Returns the inherit arrangement from parent flag   
            
         
        """
        pass
    @property
    def SelectedArrangement(self) -> Arrangement:
        """
        Getter for property: ( Arrangement NXOpen.A) SelectedArrangement
         Returns the selected arrangement   
            
         
        """
        pass
    @SelectedArrangement.setter
    def SelectedArrangement(self, arrangement: Arrangement):
        """
        Setter for property: ( Arrangement NXOpen.A) SelectedArrangement
         Returns the selected arrangement   
            
         
        """
        pass
import NXOpen
class Arrangement(NXOpen.NXObject): 
    """ 
    Manages the suppression of NXOpen.Assemblies.Components within a
    NXOpen.Assemblies.ComponentAssembly. Currently, an Arrangement simply acts as a
    context within which a Component can be suppressed, unsuppressed, or positioned. 
    
    To create an NXOpen.Assemblies.Arrangement, use the NXOpen.Assemblies.ArrangementCollection class.
    
    
    An isolated NXOpen.Assemblies.Arrangement is an NXOpen.Assemblies.Arrangement that is capable of supporting 
    isolated positions and isolated position overrides. 
    
     
    A standard NXOpen.Assemblies.Arrangement is an NXOpen.Assemblies.Arrangement that does not support isolated 
    position or isolated position overrides. All NXOpen.Assemblies.Arrangements created in NX 8.5 or earlier are standard NXOpen.Assemblies.Arrangements.
    
 """
    @property
    def IgnoringConstraints(self) -> bool:
        """
        Getter for property: (bool) IgnoringConstraints
         Returns
                the flag indicating whether this  NXOpen::Assemblies::Arrangement  is ignoring constraints.  
           
              
         
        """
        pass
    @IgnoringConstraints.setter
    def IgnoringConstraints(self, is_ignoring_constraints: bool):
        """
        Setter for property: (bool) IgnoringConstraints
         Returns
                the flag indicating whether this  NXOpen::Assemblies::Arrangement  is ignoring constraints.  
           
              
         
        """
        pass
    @property
    def Owner(self) -> ComponentAssembly:
        """
        Getter for property: ( ComponentAssembly NXOpen.A) Owner
         Returns the  NXOpen::Assemblies::ComponentAssembly  which owns this arrangement   
            
         
        """
        pass
    def Delete(self, forget_positioning: bool) -> None:
        """
         Delete the given NXOpen.Assemblies.Arrangement. If the forget_positioning flag is set to
            TRUE then components will not maintain their positions, otherwise variable component positioning
            will be created to maintain the components current positions.  If the part containing the 
            NXOpen.Assemblies.Arrangement is not already fully loaded this method will cause it to be. 
        """
        pass
    def GetHasPostponedConstraints(self) -> bool:
        """
                Get whether this NXOpen.Assemblies.Arrangement has postponed its solve.
                The solving of constraints is postponed in an NXOpen.Assemblies.Arrangement that is not currently used in the session.
                The constraints will solve when the component positions in the NXOpen.Assemblies.Arrangement are needed.
            
         Returns postpones_constraints (bool):  Whether this NXOpen.Assemblies.Arrangement has postponed solving its constraints.
        """
        pass
    def GetMaintainsConstraints(self) -> bool:
        """
                Get whether this NXOpen.Assemblies.Arrangement is currently used in the session. 
                If it is, it will be kept up to date.
            
         Returns maintains_constraints (bool):  Whether this NXOpen.Assemblies.Arrangement is currently used in the session.
        """
        pass
    def IsIsolated(self) -> bool:
        """
                Get whether this NXOpen.Assemblies.Arrangement is isolated. 
                An isolated NXOpen.Assemblies.Arrangement is an NXOpen.Assemblies.Arrangement that is capable of supporting 
                isolated positions and isolated position overrides. 
            
         Returns is_isolated (bool):  Whether this NXOpen.Assemblies.Arrangement is isolated.
        """
        pass
    def SolvePostponedConstraints(self) -> None:
        """
                Forces a postponed NXOpen.Assemblies.Arrangement, that is not currently used in the session,
                to solve its constraints. This could lead to updating the model if required. 
            
        """
        pass
class AssembliesChildRevisionOptions(Enum):
    """
    Members Include: 
     |AllRevisions|  show all revisions of the child parts 
     |UseRevRule|  show revision of the child parts based on the revision rule 
     |LatestRevisionWithRelation|  show the latest revision of the child part that has an interpart relation 

    """
    AllRevisions: int
    UseRevRule: int
    LatestRevisionWithRelation: int
    @staticmethod
    def ValueOf(value: int) -> AssembliesChildRevisionOptions:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AssembliesEventTypes(Enum):
    """
    Members Include: 
     |BrowserUpdate|  update all relations in the browser event 
     |DeselectAll|  deselect all that is currently selected event 
     |PartSelectAll|  select all parts event 
     |PartDeselectAll|  deselect all parts event 
     |PartSelect|  select specified parts event 
     |PartDeselect|  deselect specified parts event 
     |PartFullyLoad|  part fully load event 
     |PartMakeDisplayed|  part make displayed part event 
     |PartMakeWork|  part make work part event 
     |LinkedObjectSelectAll|  select all linked objects event 
     |LinkedObjectDeselectAll|  deselect all linked objects event 
     |LinkedObjectSelect|  select specified linked objects event 
     |LinkedObjectDeselect|  deselect specified linked objects event 
     |LinkedFeatureEdit|  linked feature edit event 
     |LinkedFeatureBreak|  linked feature break event 
     |LinkedFeatureAcceptBroken|  linked feature accept broken event 
     |Launch|  browser successfully launched event 
     |Exit|  browser exit event 

    """
    BrowserUpdate: int
    DeselectAll: int
    PartSelectAll: int
    PartDeselectAll: int
    PartSelect: int
    PartDeselect: int
    PartFullyLoad: int
    PartMakeDisplayed: int
    PartMakeWork: int
    LinkedObjectSelectAll: int
    LinkedObjectDeselectAll: int
    LinkedObjectSelect: int
    LinkedObjectDeselect: int
    LinkedFeatureEdit: int
    LinkedFeatureBreak: int
    LinkedFeatureAcceptBroken: int
    Launch: int
    Exit: int
    @staticmethod
    def ValueOf(value: int) -> AssembliesEventTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class AssembliesGeneralPropertiesBuilder(NXOpen.Builder): 
    """
    Represents an NXOpen.Assemblies.AssembliesGeneralPropertiesBuilder to be used for changing the
    general properties of a component.
    """
    class HiddenOptions(Enum):
        """
        Members Include: 
         |No|  Do not hide the objects 
         |Yes|  Hide the objects 
         |Mixed|  Objects hidden properties differ and will not change 

        """
        No: int
        Yes: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> AssembliesGeneralPropertiesBuilder.HiddenOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LayerOptions(Enum):
        """
        Members Include: 
         |OriginalLayer|  Objects will be placed on original layer 
         |SpecifiedLayer|  Objects will be placed on a user specified layer 
         |Mixed|  Objects are on different layers and will not be changed 

        """
        OriginalLayer: int
        SpecifiedLayer: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> AssembliesGeneralPropertiesBuilder.LayerOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class QuantityOptions(Enum):
        """
        Members Include: 
         |Number|  Use either the integer or real value to set the quantity 
         |AsRequired|  Set the as-required quantity on this component. 
         |Mixed|  Set the No Change(Mixed) quantity type if selected components have different quantity type and value 

        """
        Number: int
        AsRequired: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> AssembliesGeneralPropertiesBuilder.QuantityOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceComponentOptions(Enum):
        """
        Members Include: 
         |No|  Objects will be non reference-only components 
         |Yes|  Objects will be reference-only components 
         |Mixed|  Objects are a mixture of reference-only and non reference-only components, and will not be changed 

        """
        No: int
        Yes: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> AssembliesGeneralPropertiesBuilder.ReferenceComponentOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Hidden(self) -> AssembliesGeneralPropertiesBuilder.HiddenOptions:
        """
        Getter for property: ( AssembliesGeneralPropertiesBuilder.HiddenOptions NXOpen.A) Hidden
         Returns the hidden option.  
            The hidden option will be "Yes" if all the objects are hidden, 
                    "No" if all the objects are not hidden, and "Mixed" if there is a combination.   
         
        """
        pass
    @Hidden.setter
    def Hidden(self, hidden: AssembliesGeneralPropertiesBuilder.HiddenOptions):
        """
        Setter for property: ( AssembliesGeneralPropertiesBuilder.HiddenOptions NXOpen.A) Hidden
         Returns the hidden option.  
            The hidden option will be "Yes" if all the objects are hidden, 
                    "No" if all the objects are not hidden, and "Mixed" if there is a combination.   
         
        """
        pass
    @property
    def IntegerQuantity(self) -> int:
        """
        Getter for property: (int) IntegerQuantity
         Returns the integer quantity.  
            This value will be used if the Quantity Type is set to Number
                    and the DB_UNITS attribute is not set.   
         
        """
        pass
    @IntegerQuantity.setter
    def IntegerQuantity(self, integerQuantity: int):
        """
        Setter for property: (int) IntegerQuantity
         Returns the integer quantity.  
            This value will be used if the Quantity Type is set to Number
                    and the DB_UNITS attribute is not set.   
         
        """
        pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer.  
            Used if the layer option is set to specified.   
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer.  
            Used if the layer option is set to specified.   
         
        """
        pass
    @property
    def LayerOption(self) -> AssembliesGeneralPropertiesBuilder.LayerOptions:
        """
        Getter for property: ( AssembliesGeneralPropertiesBuilder.LayerOptions NXOpen.A) LayerOption
         Returns the layer option.  
            If specified layer is set, then the layer will be used.   
         
        """
        pass
    @LayerOption.setter
    def LayerOption(self, layerOption: AssembliesGeneralPropertiesBuilder.LayerOptions):
        """
        Setter for property: ( AssembliesGeneralPropertiesBuilder.LayerOptions NXOpen.A) LayerOption
         Returns the layer option.  
            If specified layer is set, then the layer will be used.   
         
        """
        pass
    @property
    def NonGeometric(self) -> bool:
        """
        Getter for property: (bool) NonGeometric
         Returns the non geometric flag.  
            Sets the components to either geometric or non-geometric.   
         
        """
        pass
    @NonGeometric.setter
    def NonGeometric(self, nonGeometric: bool):
        """
        Setter for property: (bool) NonGeometric
         Returns the non geometric flag.  
            Sets the components to either geometric or non-geometric.   
         
        """
        pass
    @property
    def QuantityType(self) -> AssembliesGeneralPropertiesBuilder.QuantityOptions:
        """
        Getter for property: ( AssembliesGeneralPropertiesBuilder.QuantityOptions NXOpen.A) QuantityType
         Returns the quantity type.  
            If the quantity type is set to number than either the integer 
                    quantity or the real quantity values will be used.  Otherwise the quantity will
                    be set to as-required.   
         
        """
        pass
    @QuantityType.setter
    def QuantityType(self, quantityType: AssembliesGeneralPropertiesBuilder.QuantityOptions):
        """
        Setter for property: ( AssembliesGeneralPropertiesBuilder.QuantityOptions NXOpen.A) QuantityType
         Returns the quantity type.  
            If the quantity type is set to number than either the integer 
                    quantity or the real quantity values will be used.  Otherwise the quantity will
                    be set to as-required.   
         
        """
        pass
    @property
    def RealQuantity(self) -> float:
        """
        Getter for property: (float) RealQuantity
         Returns the real quantity.  
            This value will be used if the Quantity Type is set to Number
                    and the DB_UNITS attribute has been set.   
         
        """
        pass
    @RealQuantity.setter
    def RealQuantity(self, realQuantity: float):
        """
        Setter for property: (float) RealQuantity
         Returns the real quantity.  
            This value will be used if the Quantity Type is set to Number
                    and the DB_UNITS attribute has been set.   
         
        """
        pass
    @property
    def ReferenceComponent(self) -> AssembliesGeneralPropertiesBuilder.ReferenceComponentOptions:
        """
        Getter for property: ( AssembliesGeneralPropertiesBuilder.ReferenceComponentOptions NXOpen.A) ReferenceComponent
         Returns the reference-only component flag.  
            This option determines whether the components will
                    be reference-only or not.   
         
        """
        pass
    @ReferenceComponent.setter
    def ReferenceComponent(self, referenceComponent: AssembliesGeneralPropertiesBuilder.ReferenceComponentOptions):
        """
        Setter for property: ( AssembliesGeneralPropertiesBuilder.ReferenceComponentOptions NXOpen.A) ReferenceComponent
         Returns the reference-only component flag.  
            This option determines whether the components will
                    be reference-only or not.   
         
        """
        pass
    @property
    def SelectedObjects(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) SelectedObjects
         Returns the selected object(s) list.  
            This is the active list of components that will be
                    modified by any changes.   
         
        """
        pass
    @property
    def SpecificColor(self) -> bool:
        """
        Getter for property: (bool) SpecificColor
         Returns the specific color flag.  
            The explicit color display property will be discarded from all
                    components.   
         
        """
        pass
    @SpecificColor.setter
    def SpecificColor(self, specificColor: bool):
        """
        Setter for property: (bool) SpecificColor
         Returns the specific color flag.  
            The explicit color display property will be discarded from all
                    components.   
         
        """
        pass
    @property
    def SpecificLineFont(self) -> bool:
        """
        Getter for property: (bool) SpecificLineFont
         Returns the specific line font flag.  
            The explicit line font display property will be discarded from all
                    components.   
         
        """
        pass
    @SpecificLineFont.setter
    def SpecificLineFont(self, specificLineFont: bool):
        """
        Setter for property: (bool) SpecificLineFont
         Returns the specific line font flag.  
            The explicit line font display property will be discarded from all
                    components.   
         
        """
        pass
    @property
    def SpecificPartialShade(self) -> bool:
        """
        Getter for property: (bool) SpecificPartialShade
         Returns the specific partial shade flag.  
            The explicit partial shade display property will be 
                    discarded from all components.   
         
        """
        pass
    @SpecificPartialShade.setter
    def SpecificPartialShade(self, specificPartialShade: bool):
        """
        Setter for property: (bool) SpecificPartialShade
         Returns the specific partial shade flag.  
            The explicit partial shade display property will be 
                    discarded from all components.   
         
        """
        pass
    @property
    def SpecificTranslucency(self) -> bool:
        """
        Getter for property: (bool) SpecificTranslucency
         Returns the specific translucency flag.  
            The explicit translucency display property will be 
                    discarded from all components.   
         
        """
        pass
    @SpecificTranslucency.setter
    def SpecificTranslucency(self, specificTranslucency: bool):
        """
        Setter for property: (bool) SpecificTranslucency
         Returns the specific translucency flag.  
            The explicit translucency display property will be 
                    discarded from all components.   
         
        """
        pass
    @property
    def SpecificWidth(self) -> bool:
        """
        Getter for property: (bool) SpecificWidth
         Returns the specific width flag.  
            The explicit width display property will be discarded from all
                   components.   
         
        """
        pass
    @SpecificWidth.setter
    def SpecificWidth(self, specificWidth: bool):
        """
        Setter for property: (bool) SpecificWidth
         Returns the specific width flag.  
            The explicit width display property will be discarded from all
                   components.   
         
        """
        pass
    def SynchronizeAttributes(self) -> None:
        """
         Synchronize the attributes on the components 
        """
        pass
    def SynchronizeDisplay(self) -> None:
        """
         Synchronize the display on the components 
        """
        pass
    def SynchronizeLayers(self) -> None:
        """
         Synchronize the layers on the components 
        """
        pass
import NXOpen
class AssembliesParameterPropertiesBuilder(NXOpen.Builder): 
    """
    Represents an NXOpen.Assemblies.AssembliesParameterPropertiesBuilder to be used for changing the
    name or modifying the positioning mixture status of a component.
    """
    class ArrangementOptions(Enum):
        """
        Members Include: 
         |IndividuallyPositioned|  All components are varied 
         |SamePositionInAll|  All components are unvaried 
         |Mixed|  All components are neither varied nor unvaried 

        """
        IndividuallyPositioned: int
        SamePositionInAll: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> AssembliesParameterPropertiesBuilder.ArrangementOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Arrangements(self) -> AssembliesParameterPropertiesBuilder.ArrangementOptions:
        """
        Getter for property: ( AssembliesParameterPropertiesBuilder.ArrangementOptions NXOpen.A) Arrangements
         Returns the arrangements.  
            The positioning mixture status for the selected components.
                    No action will take place if Mixed is set as the arrangement option.   
         
        """
        pass
    @Arrangements.setter
    def Arrangements(self, arrangements: AssembliesParameterPropertiesBuilder.ArrangementOptions):
        """
        Setter for property: ( AssembliesParameterPropertiesBuilder.ArrangementOptions NXOpen.A) Arrangements
         Returns the arrangements.  
            The positioning mixture status for the selected components.
                    No action will take place if Mixed is set as the arrangement option.   
         
        """
        pass
    @property
    def SelectedObjects(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) SelectedObjects
         Returns the selected object(s) list.  
            This is the active list of components that will be
                    modified by any parameter changes.   
         
        """
        pass
import NXOpen
class AssemblyManager(NXOpen.Object): 
    """  Represents the Assembly Manager """
    def CreateAddComponentBuilder(self) -> AddComponentBuilder:
        """
         Creates a Assemblies.AddComponentBuilder 
         Returns builder ( AddComponentBuilder NXOpen.A): .
        """
        pass
    def CreateClearanceAnalysisBuilder(self, clearanceSet: ClearanceSet) -> ClearanceAnalysisBuilder:
        """
         Creates a NXOpen.Assemblies.ClearanceAnalysisBuilder. The builder can be populated 
                 with an existing clearance set specified in clearanceSet.
            
         Returns builder ( ClearanceAnalysisBuilder NXOpen.A): .
        """
        pass
    def CreateConstraintDisplayBuilder(self) -> ConstraintDisplayBuilder:
        """
         Creates a NXOpen.Assemblies.ConstraintDisplayBuilder
         Returns builder ( ConstraintDisplayBuilder NXOpen.A): .
        """
        pass
    def CreateCreateComponentBuilder(self) -> CreateComponentBuilder:
        """
         Creates a Assemblies.CreateComponentBuilder 
         Returns builder ( CreateComponentBuilder NXOpen.A): .
        """
        pass
    def CreateHideComponentBuilder(self) -> HideComponentBuilder:
        """
         Creates a NXOpen.Assemblies.HideComponentBuilder 
         Returns builder ( HideComponentBuilder NXOpen.A): .
        """
        pass
    def CreateLoadInterpartDataBuilder(self) -> LoadInterpartDataBuilder:
        """
         Creates a NXOpen.Assemblies.LoadInterpartDataBuilder 
         Returns builder ( LoadInterpartDataBuilder NXOpen.A): .
        """
        pass
    def CreateMakeUniquePartBuilder(self) -> MakeUniquePartBuilder:
        """
         Creates a NXOpen.Assemblies.MakeUniquePartBuilder
         Returns builder ( MakeUniquePartBuilder NXOpen.A): .
        """
        pass
    def CreateNewComponentBuilder(self) -> CreateNewComponentBuilder:
        """
         Creates a NXOpen.Assemblies.CreateNewComponentBuilder 
         Returns builder ( CreateNewComponentBuilder NXOpen.A): .
        """
        pass
    def CreateOpenByProximityBuilder(self) -> OpenByProximityBuilder:
        """
         Creates a NXOpen.Assemblies.OpenByProximityBuilder  
         Returns builder ( OpenByProximityBuilder NXOpen.A): .
        """
        pass
    def CreateReflectComponentBuilder(self, sourcePart: NXOpen.Part, destinationPartOcc: Component) -> ReflectComponentBuilder:
        """
         Creates a Assemblies.ReflectComponentBuilder.
                destinationPart: Part under which reflected component will get created.
                sourcePart: Part from which component must be selected to create reflected component.
                destinationPartOcc: The occurrence of sourcePart inside destinationPart where reflected component
                will get created. If the destinationPart and the sourcePart are the same then destinationPartOcc must be NULL_TAG.
            
         Returns builder ( ReflectComponentBuilder NXOpen.A): .
        """
        pass
    def CreateReplaceComponentBuilder(self) -> ReplaceComponentBuilder:
        """
         Creates a NXOpen.Assemblies.ReplaceComponentBuilder 
         Returns builder ( ReplaceComponentBuilder NXOpen.A): .
        """
        pass
    def CreateShowComponentBuilder(self) -> ShowComponentBuilder:
        """
         Creates a NXOpen.Assemblies.ShowComponentBuilder 
         Returns builder ( ShowComponentBuilder NXOpen.A): .
        """
        pass
    def CreateSimplifyBuilder(self) -> SimplifyBuilder:
        """
         Creates a NXOpen.Assemblies.SimplifyBuilder.  This builder can be used
                if the work part is also the display part.  
         Returns builder ( SimplifyBuilder NXOpen.A): .
        """
        pass
    def CreateSimplifyBuilderWithContextComponent(self, contextComponent: Component) -> SimplifyBuilder:
        """
         Creates a NXOpen.Assemblies.SimplifyBuilder.  This builder takes a context
                NXOpen.Assemblies.Component that is used for smart collectors.  If the work
                part is also the display part this can be NULL_TAG.  Otherwise, it should be the current
                NXOpen.PartCollection.WorkComponent.  
         Returns builder ( SimplifyBuilder NXOpen.A): .
        """
        pass
    def CreateUpdateStructureBuilder(self) -> UpdateStructureBuilder:
        """
         Creates a NXOpen.Assemblies.UpdateStructureBuilder 
         Returns builder ( UpdateStructureBuilder NXOpen.A): .
        """
        pass
import NXOpen
class Assembly(NXOpen.NXObject): 
    """Assembly class   
    """
    pass
class AttributeSearchTermBuilder(SearchTermBuilder): 
    """
        An AttributeSearchTermBuilder is used to create or edit an NXOpen.Assemblies.AttributeSearchTerm.
    """
    @property
    def QueryName(self) -> str:
        """
        Getter for property: (str) QueryName
         Returns the name of the saved query upon which this search term is based.  
          
                  
         
        """
        pass
    @QueryName.setter
    def QueryName(self, queryName: str):
        """
        Setter for property: (str) QueryName
         Returns the name of the saved query upon which this search term is based.  
          
                  
         
        """
        pass
    @property
    def SearchTermLogic(self) -> SearchTerm.SearchTermLogicType:
        """
        Getter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns the search term logic.  
          
                  
         
        """
        pass
    @SearchTermLogic.setter
    def SearchTermLogic(self, searchTermLogic: SearchTerm.SearchTermLogicType):
        """
        Setter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns the search term logic.  
          
                  
         
        """
        pass
    def GetCriteria(self) -> Tuple[List[str], List[str]]:
        """
         Get the entry titles and values that are used to populate the saved query.
                
         Returns A tuple consisting of (titles, values). 
         - titles is: List[str]. search criteria titles .
         - values is: List[str]. search criteria values .

        """
        pass
    def SetCriteria(self, titles: List[str], values: List[str]) -> None:
        """
         Set the entry titles and values that are used to populate the saved query.
                
        """
        pass
class AttributeSearchTerm(SearchTerm): 
    """
        An attribute search term within a NXOpen.Assemblies.SubsetRecipe.
    """
    pass
import NXOpen
class BoxSearchTermBuilder(SearchTermBuilder): 
    """
        A BoxSearchTermBuilder is used to create or edit an NXOpen.Assemblies.BoxSearchTerm.
    """
    @property
    def BottomCorner(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) BottomCorner
         Returns 
                    the bottom corner of the box.  
          
                  
         
        """
        pass
    @BottomCorner.setter
    def BottomCorner(self, bottomCorner: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) BottomCorner
         Returns 
                    the bottom corner of the box.  
          
                  
         
        """
        pass
    @property
    def BoxOverlapLogic(self) -> BoxSearchTerm.BoxOverlapLogicType:
        """
        Getter for property: ( BoxSearchTerm.BoxOverlapLogicType NXOpen.A) BoxOverlapLogic
         Returns 
                    the box overlap logic.  
          
                  
         
        """
        pass
    @BoxOverlapLogic.setter
    def BoxOverlapLogic(self, boxOverlapLogic: BoxSearchTerm.BoxOverlapLogicType):
        """
        Setter for property: ( BoxSearchTerm.BoxOverlapLogicType NXOpen.A) BoxOverlapLogic
         Returns 
                    the box overlap logic.  
          
                  
         
        """
        pass
    @property
    def SearchTermLogic(self) -> SearchTerm.SearchTermLogicType:
        """
        Getter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @SearchTermLogic.setter
    def SearchTermLogic(self, searchTermLogic: SearchTerm.SearchTermLogicType):
        """
        Setter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @property
    def TopCorner(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) TopCorner
         Returns 
                    the top corner of the box.  
          
                  
         
        """
        pass
    @TopCorner.setter
    def TopCorner(self, topCorner: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) TopCorner
         Returns 
                    the top corner of the box.  
          
                  
         
        """
        pass
    @property
    def TrueShapeRefinement(self) -> bool:
        """
        Getter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
    @TrueShapeRefinement.setter
    def TrueShapeRefinement(self, trueShapeRefinement: bool):
        """
        Setter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
class BoxSearchTerm(SearchTerm): 
    """
        A volume search term within a NXOpen.Assemblies.SubsetRecipe.
        A volume search finds objects in a box with sides axis aligned in the space
        of the collaborative design.
    """
    class BoxOverlapLogicType(Enum):
        """
        Members Include: 
         |Inside|  Include objects residing inside the box defined by this search term 
         |Outside|  Include objects residing outside the box defined by this search term 
         |Intersects|  Include objects that intersect the box defined by this search term 
         |InsideOrIntersects|  Include objects residing inside or intersecting the box defined by this search term 
         |OutsideOrIntersects|  Include objects residing outside or intersecting the box defined by this search term 

        """
        Inside: int
        Outside: int
        Intersects: int
        InsideOrIntersects: int
        OutsideOrIntersects: int
        @staticmethod
        def ValueOf(value: int) -> BoxSearchTerm.BoxOverlapLogicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class ClearanceAnalysisBuilder(NXOpen.Builder): 
    """ 
        Represents NXOpen.Assemblies.ClearanceAnalysisBuilder.  The builder builds the clearance set
        which contains properties for the analysis.  The properties are:

        Clearance Set Name: the name of the clearance set.

        Clearance Type: either components or bodies or PSM facet objects.

        Number of collections: either one or two.  Where one collection is chosen, the analysis is performed 
        between all objects in the collection.  Where two collections are chosen, the analysis compares objects 
        from one collection with objects from the other.

        Exceptions:
            Select Subassemblies: Specific subassemblies selected within the displayed part can be treated as a single entity.

            Explicitly Ignore: A number of options to reduce the amount of results reported.

            Additional exceptions: Addtional pairs of objects to be excluded or included regardless of exception rules previously defined.
    """
    class CalculationMethodType(Enum):
        """
        Members Include: 
         |Lightweight| 
         |ExactifLoaded| 
         |Exact| 

        """
        Lightweight: int
        ExactifLoaded: int
        Exact: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.CalculationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ClearanceBetweenEntity(Enum):
        """
        Members Include: 
         |Components| 
         |Bodies| 

        """
        Components: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.ClearanceBetweenEntity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ClearanceComputation(Enum):
        """
        Members Include: 
         |Local| 
         |Distributed| 

        """
        Local: int
        Distributed: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.ClearanceComputation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ClearanceZoneSource(Enum):
        """
        Members Include: 
         |Pair| 
         |Object1| 
         |Object2| 
         |Default| 
         |Defined| 

        """
        Pair: int
        Object1: int
        Object2: int
        Default: int
        Defined: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.ClearanceZoneSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CollectionRange(Enum):
        """
        Members Include: 
         |AllObjects| 
         |AllVisibleObjects| 
         |SelectedObjects| 
         |AllButSelectedObjects| 

        """
        AllObjects: int
        AllVisibleObjects: int
        SelectedObjects: int
        AllButSelectedObjects: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.CollectionRange:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NumberOfCollections(Enum):
        """
        Members Include: 
         |One| 
         |Two| 

        """
        One: int
        Two: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.NumberOfCollections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PairExcludedReason(Enum):
        """
        Members Include: 
         |NoReason|  default behavior 
         |UserDefined|  user has explicitly included or excluded this pair 
         |SameCompRule|  global exclusion rule for same component applies 
         |SameGroupRule|  global exclusion rule for same group applies 
         |MatedCompRule|  global exclusion rule for mated component applies 
         |SamePartRule|  global exclusion rule for same part applies 
         |CompSuppressed|  suppressed component 
         |NonGeom|  no geometry 
         |UnitSubassy|  in unit subassembly 

        """
        NoReason: int
        UserDefined: int
        SameCompRule: int
        SameGroupRule: int
        MatedCompRule: int
        SamePartRule: int
        CompSuppressed: int
        NonGeom: int
        UnitSubassy: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.PairExcludedReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ZoneType(Enum):
        """
        Members Include: 
         |Object| 
         |Pair| 

        """
        Object: int
        Pair: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceAnalysisBuilder.ZoneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CalculationMethod(self) -> ClearanceAnalysisBuilder.CalculationMethodType:
        """
        Getter for property: ( ClearanceAnalysisBuilder.CalculationMethodType NXOpen.A) CalculationMethod
         Returns the setting for the clearance calculation method.  
             
         
        """
        pass
    @CalculationMethod.setter
    def CalculationMethod(self, calculateMethod: ClearanceAnalysisBuilder.CalculationMethodType):
        """
        Setter for property: ( ClearanceAnalysisBuilder.CalculationMethodType NXOpen.A) CalculationMethod
         Returns the setting for the clearance calculation method.  
             
         
        """
        pass
    @property
    def ClearanceBetween(self) -> ClearanceAnalysisBuilder.ClearanceBetweenEntity:
        """
        Getter for property: ( ClearanceAnalysisBuilder.ClearanceBetweenEntity NXOpen.A) ClearanceBetween
         Returns the setting to determine whether components or bodies should be used.  
          
                    Please note that changing the collection type will clear the collections, 
                    exceptions and clearance zones from the clearance set  
         
        """
        pass
    @ClearanceBetween.setter
    def ClearanceBetween(self, clearanceBetweenEntity: ClearanceAnalysisBuilder.ClearanceBetweenEntity):
        """
        Setter for property: ( ClearanceAnalysisBuilder.ClearanceBetweenEntity NXOpen.A) ClearanceBetween
         Returns the setting to determine whether components or bodies should be used.  
          
                    Please note that changing the collection type will clear the collections, 
                    exceptions and clearance zones from the clearance set  
         
        """
        pass
    @property
    def ClearanceSetName(self) -> str:
        """
        Getter for property: (str) ClearanceSetName
         Returns the clearance set name.  
             
         
        """
        pass
    @ClearanceSetName.setter
    def ClearanceSetName(self, clearanceSetName: str):
        """
        Setter for property: (str) ClearanceSetName
         Returns the clearance set name.  
             
         
        """
        pass
    @property
    def CollectionOneObjects(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) CollectionOneObjects
         Returns the selected objects for collection one.  
             
         
        """
        pass
    @property
    def CollectionOneRange(self) -> ClearanceAnalysisBuilder.CollectionRange:
        """
        Getter for property: ( ClearanceAnalysisBuilder.CollectionRange NXOpen.A) CollectionOneRange
         Returns the range setting for collection one.  
             
         
        """
        pass
    @CollectionOneRange.setter
    def CollectionOneRange(self, collectionRange: ClearanceAnalysisBuilder.CollectionRange):
        """
        Setter for property: ( ClearanceAnalysisBuilder.CollectionRange NXOpen.A) CollectionOneRange
         Returns the range setting for collection one.  
             
         
        """
        pass
    @property
    def CollectionTwoObjects(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) CollectionTwoObjects
         Returns the selected objects for collection two.  
             
         
        """
        pass
    @property
    def CollectionTwoRange(self) -> ClearanceAnalysisBuilder.CollectionRange:
        """
        Getter for property: ( ClearanceAnalysisBuilder.CollectionRange NXOpen.A) CollectionTwoRange
         Returns the range setting for collection two.  
             
         
        """
        pass
    @CollectionTwoRange.setter
    def CollectionTwoRange(self, collectionRange: ClearanceAnalysisBuilder.CollectionRange):
        """
        Setter for property: ( ClearanceAnalysisBuilder.CollectionRange NXOpen.A) CollectionTwoRange
         Returns the range setting for collection two.  
             
         
        """
        pass
    @property
    def InterferenceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) InterferenceColor
         Returns the color of the interference geometry.  
             
         
        """
        pass
    @InterferenceColor.setter
    def InterferenceColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) InterferenceColor
         Returns the color of the interference geometry.  
             
         
        """
        pass
    @property
    def IsCalculatePenetrationDepth(self) -> bool:
        """
        Getter for property: (bool) IsCalculatePenetrationDepth
         Returns the setting to determine whether penetration depth should be calculated.  
             
         
        """
        pass
    @IsCalculatePenetrationDepth.setter
    def IsCalculatePenetrationDepth(self, isCalculatePenetrationDepth: bool):
        """
        Setter for property: (bool) IsCalculatePenetrationDepth
         Returns the setting to determine whether penetration depth should be calculated.  
             
         
        """
        pass
    @property
    def IsIgnorePairsWithinSameGroup(self) -> bool:
        """
        Getter for property: (bool) IsIgnorePairsWithinSameGroup
         Returns the setting to determine whether to ignore pairs within same group.  
             
         
        """
        pass
    @IsIgnorePairsWithinSameGroup.setter
    def IsIgnorePairsWithinSameGroup(self, isIgnorePairsWithinSameGroup: bool):
        """
        Setter for property: (bool) IsIgnorePairsWithinSameGroup
         Returns the setting to determine whether to ignore pairs within same group.  
             
         
        """
        pass
    @property
    def IsIgnorePairsWithinSamePart(self) -> bool:
        """
        Getter for property: (bool) IsIgnorePairsWithinSamePart
         Returns the setting to determine whether to ignore pairs within same part.  
             
         
        """
        pass
    @IsIgnorePairsWithinSamePart.setter
    def IsIgnorePairsWithinSamePart(self, isIgnorePairsWithinSamePart: bool):
        """
        Setter for property: (bool) IsIgnorePairsWithinSamePart
         Returns the setting to determine whether to ignore pairs within same part.  
             
         
        """
        pass
    @property
    def IsIgnorePairsWithinSameSubassembly(self) -> bool:
        """
        Getter for property: (bool) IsIgnorePairsWithinSameSubassembly
         Returns the setting to determine whether to ignore pairs within same subassembly.  
             
         
        """
        pass
    @IsIgnorePairsWithinSameSubassembly.setter
    def IsIgnorePairsWithinSameSubassembly(self, isIgnorePairsWithinSameSubassembly: bool):
        """
        Setter for property: (bool) IsIgnorePairsWithinSameSubassembly
         Returns the setting to determine whether to ignore pairs within same subassembly.  
             
         
        """
        pass
    @property
    def IsIgnorePairsWithinSelectedSubassemblies(self) -> bool:
        """
        Getter for property: (bool) IsIgnorePairsWithinSelectedSubassemblies
         Returns the setting to determine whether to ignore pairs within the selected subassemblies.  
             
         
        """
        pass
    @IsIgnorePairsWithinSelectedSubassemblies.setter
    def IsIgnorePairsWithinSelectedSubassemblies(self, isIgnorePairsWithinSelectedSubassemblies: bool):
        """
        Setter for property: (bool) IsIgnorePairsWithinSelectedSubassemblies
         Returns the setting to determine whether to ignore pairs within the selected subassemblies.  
             
         
        """
        pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer for interference geometry.  
             
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer for interference geometry.  
             
         
        """
        pass
    @property
    def SaveInterferenceGeometry(self) -> bool:
        """
        Getter for property: (bool) SaveInterferenceGeometry
         Returns the setting to determine if interference geometry should be saved.  
             
         
        """
        pass
    @SaveInterferenceGeometry.setter
    def SaveInterferenceGeometry(self, saveInterferenceGeometry: bool):
        """
        Setter for property: (bool) SaveInterferenceGeometry
         Returns the setting to determine if interference geometry should be saved.  
             
         
        """
        pass
    @property
    def TotalCollectionCount(self) -> ClearanceAnalysisBuilder.NumberOfCollections:
        """
        Getter for property: ( ClearanceAnalysisBuilder.NumberOfCollections NXOpen.A) TotalCollectionCount
         Returns the setting to determine whether one collection or two collections should be used.  
             
         
        """
        pass
    @TotalCollectionCount.setter
    def TotalCollectionCount(self, totalCollectionCount: ClearanceAnalysisBuilder.NumberOfCollections):
        """
        Setter for property: ( ClearanceAnalysisBuilder.NumberOfCollections NXOpen.A) TotalCollectionCount
         Returns the setting to determine whether one collection or two collections should be used.  
             
         
        """
        pass
    @property
    def UnitSubassemblies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) UnitSubassemblies
         Returns the selected unit subassemblies.  
             
         
        """
        pass
    def AddException(self, isExclude: bool, comp1: NXOpen.DisplayableObject, comp2: NXOpen.DisplayableObject, text: str) -> None:
        """
         Add an exception. 
        """
        pass
    def AddObjectClearanceZone(self, objectValue: NXOpen.DisplayableObject, expression: NXOpen.Expression) -> None:
        """
         Add a Clearance Zone around an object.
                    Create the expression using CreateClearanceZoneExpression 
                    if the Clearance Zone expression naming convention is desired. 
        """
        pass
    def AddPairClearanceZone(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, expression: NXOpen.Expression) -> None:
        """
         Add a Clearance Zone between a pair of objects. 
                    Create the expression using CreateClearanceZoneExpression 
                    if the Clearance Zone expression naming convention is desired. 
        """
        pass
    def CreateClearanceZoneExpression(self, rhsExpression: str) -> NXOpen.Expression:
        """
         Create an expression using the Clearance Zone naming convention.
                    The expression is intended for use in the following methods:
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.SetDefaultClearanceZone 
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.AddPairClearanceZone 
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.AddObjectClearanceZone 
         Returns expression ( NXOpen.Expression):  the new expression .
        """
        pass
    def DeleteException(self, comp1: NXOpen.DisplayableObject, comp2: NXOpen.DisplayableObject) -> None:
        """
         Delete an exception. 
        """
        pass
    def DeleteObjectClearanceZone(self, objectValue: NXOpen.DisplayableObject) -> None:
        """
         Delete an existing Clearance Zone from around an object. 
        """
        pass
    def DeletePairClearanceZone(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> None:
        """
         Delete an existing Clearance Zone between the given pair of objects. 
        """
        pass
    def GetDefaultClearanceZone(self) -> NXOpen.Expression:
        """
         Get the default Clearance Zone expression. 
                    If there is no expression set previously, a  will be returned. 
         Returns expression ( NXOpen.Expression):  the expression .
        """
        pass
    def GetIsPairIncluded(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> Tuple[bool, ClearanceAnalysisBuilder.PairExcludedReason, str]:
        """
                  Inquires if an object pair is to be included in the analysis. Both objects
                  must be solid bodies or facet models that are members of the
                  clearance analysis data set. If the pair is to be analyzed, the includeIt
                  is returned as TRUE. The reason parameter signifies why the pair is
                  included or excluded.
                  The text parameter is only returned for the NXOpen.Assemblies.ClearanceAnalysisBuilder.PairExcludedReason.UserDefined reason.
                
         Returns A tuple consisting of (includeIt, reason, text). 
         - includeIt is: bool. the flag .
         - reason is:  ClearanceAnalysisBuilder.PairExcludedReason NXOpen.A. the reason .
         - text is: str. the text .

        """
        pass
    def GetObjectClearanceZone(self, objectValue: NXOpen.DisplayableObject) -> Tuple[ClearanceAnalysisBuilder.ClearanceZoneSource, NXOpen.Expression]:
        """
          Inquire the Clearance Zone assigned to a given object.  The object must be
                    a member of the dataset.  The expression, the distance, and the source 
                    are the outputs.  If no expression has ever been set, the part of the given object is 
                    checked for a Clearance Zone expression, if none is found,  will be returned
                    for the expression. Interpret its value as 0.0 (this is the default value). The
                    source parameter tells where the clearance zone comes from.
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource.Defined specifies 
                    that the object has its own Clearance Zone.  
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource.Default means the 
                    default clearance zone is used.
                
         Returns A tuple consisting of (source, expression). 
         - source is:  ClearanceAnalysisBuilder.ClearanceZoneSource NXOpen.A. the source of the clearance zone .
         - expression is:  NXOpen.Expression. the expression .

        """
        pass
    def GetPairClearanceZone(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> Tuple[ClearanceAnalysisBuilder.ClearanceZoneSource, NXOpen.Expression]:
        """
         Inquire the Clearance Zone for a specific pair of objects.  Both objects
                    must be members of the Clearance Set.  The source parameter tells where the 
                    clearance zone comes from.  The clearance zone could be the greater of the zones 
                    from object 1 or 2 (NXOpen.Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource.Object1
                    or NXOpen.Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource.Object2.
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource.Pair
                    means this pair has its own explicit clearance zone. 
                    NXOpen.Assemblies.ClearanceAnalysisBuilder.ClearanceZoneSource.Default means the default clearance zone is used.. 
         Returns A tuple consisting of (source, expression). 
         - source is:  ClearanceAnalysisBuilder.ClearanceZoneSource NXOpen.A. the source of the clearance zone .
         - expression is:  NXOpen.Expression. the corresponding expression .

        """
        pass
    def SetDefaultClearanceZone(self, expression: NXOpen.Expression) -> None:
        """
         Set the expression as the default Clearance Zone. 
                    Create the expression using CreateClearanceZoneExpression 
                    if the Clearance Zone expression naming convention is desired. 
        """
        pass
import NXOpen
class ClearanceSetCollection(NXOpen.TaggedObjectCollection): 
    """ 
    Represents NXOpen.Assemblies.ClearanceSetCollection.
    """
    def CountClearanceSets(self) -> int:
        """
         Determines the number of clearance analysis datasets in the specified part. 
         Returns numberOfClearanceSets (int):  the number of clearance sets .
        """
        pass
    def DeleteAllAnalysisData(self) -> None:
        """
         Deletes all clearance analysis data from the given part, including all
                    clearance analysis data sets, analysis results, and interference bodies. 
        """
        pass
    def FindObject(self, name: str) -> ClearanceSet:
        """
         Finds the  NXOpen.Assemblies.ClearanceSet  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of the software. 
                    However newer versions of the software should find the same object when FindObject is passed older versions of its journal identifier. 
                    In general, this method should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
                
         Returns foundSet ( ClearanceSet NXOpen.A):  the clearance set found, or null if no such clearance set exists.
        """
        pass
import NXOpen
class ClearanceSet(NXOpen.NXObject): 
    """ Represents NXOpen.Assemblies.ClearanceSet. Input to this class can be PSM facet objects.
 """
    class CopyMode(Enum):
        """
        Members Include: 
         |NoResults| 
         |Results| 
         |InterfBodies| 

        """
        NoResults: int
        Results: int
        InterfBodies: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.CopyMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterferenceStatus(Enum):
        """
        Members Include: 
         |Undetermined| 
         |Resolved| 
         |Irrelevant| 
         |Pending| 

        """
        Undetermined: int
        Resolved: int
        Irrelevant: int
        Pending: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.InterferenceStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterferenceType(Enum):
        """
        Members Include: 
         |Soft| 
         |Touch| 
         |Hard| 
         |Cont1In2| 
         |Cont2In1| 
         |NoInterference| 

        """
        Soft: int
        Touch: int
        Hard: int
        Cont1In2: int
        Cont2In1: int
        NoInterference: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.InterferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JobStatus(Enum):
        """
        Members Include: 
         |NotAborted| 
         |AbortedByUser| 
         |AbortedOnError| 

        """
        NotAborted: int
        AbortedByUser: int
        AbortedOnError: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.JobStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PenetrationDepthResult(Enum):
        """
        Members Include: 
         |NotAttempted| 
         |Success| 
         |NoClash| 
         |Touching| 
         |BothSheets| 
         |UnspecifiedError| 

        """
        NotAttempted: int
        Success: int
        NoClash: int
        Touching: int
        BothSheets: int
        UnspecifiedError: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.PenetrationDepthResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReanalyzeOutOfDateExcludedPairs(Enum):
        """
        Members Include: 
         |CustomerDefault| 
         |TrueValue| 
         |FalseValue| 

        """
        CustomerDefault: int
        TrueValue: int
        FalseValue: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.ReanalyzeOutOfDateExcludedPairs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReanalyzePairCalculationMethod(Enum):
        """
        Members Include: 
         |UseStoredMethod|  Use the clearance set's defined analysis method. 
         |Lightweight| 
         |ExactIfLoaded| 
         |Exact| 

        """
        UseStoredMethod: int
        Lightweight: int
        ExactIfLoaded: int
        Exact: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceSet.ReanalyzePairCalculationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Summary:
        """
         Summary of the most recent Clearance Analysis results 
         ClearanceSetSummary_Struct NXOpen.A is an alias for  ClearanceSet.Summary NXOpen.A.
        """
        @property
        def StartTime(self) -> int:
            """
            Getter for property StartTime
            The starting time of the last                                           analysis run (in seconds since                                           00:00:00 111970.

            """
            pass
        @StartTime.setter
        def StartTime(self, value: int):
            """
            Getter for property StartTime
            The starting time of the last                                           analysis run (in seconds since                                           00:00:00 111970.
            Setter for property StartTime
            The starting time of the last                                           analysis run (in seconds since                                           00:00:00 111970.

            """
            pass
        @property
        def EndTime(self) -> int:
            """
            Getter for property EndTime
            The ending time of the last                                           analysis run (in seconds since                                           00:00:00 111970.

            """
            pass
        @EndTime.setter
        def EndTime(self, value: int):
            """
            Getter for property EndTime
            The ending time of the last                                           analysis run (in seconds since                                           00:00:00 111970.
            Setter for property EndTime
            The ending time of the last                                           analysis run (in seconds since                                           00:00:00 111970.

            """
            pass
        @property
        def RunTime(self) -> int:
            """
            Getter for property RunTime
            the total analysis time (in secs.

            """
            pass
        @RunTime.setter
        def RunTime(self, value: int):
            """
            Getter for property RunTime
            the total analysis time (in secs.
            Setter for property RunTime
            the total analysis time (in secs.

            """
            pass
        @property
        def Version(self) -> int:
            """
            Getter for property Version
            The version of this analysis run.

            """
            pass
        @Version.setter
        def Version(self, value: int):
            """
            Getter for property Version
            The version of this analysis run.
            Setter for property Version
            The version of this analysis run.

            """
            pass
        @property
        def AnalysisMode(self) -> ClearanceAnalysisBuilder.CalculationMethodType:
            """
            Getter for property AnalysisMode
            The analysis mode.

            """
            pass
        @AnalysisMode.setter
        def AnalysisMode(self, value: ClearanceAnalysisBuilder.CalculationMethodType):
            """
            Getter for property AnalysisMode
            The analysis mode.
            Setter for property AnalysisMode
            The analysis mode.

            """
            pass
        @property
        def NumCollections(self) -> int:
            """
            Getter for property NumCollections
            Number of collections analyzed.

            """
            pass
        @NumCollections.setter
        def NumCollections(self, value: int):
            """
            Getter for property NumCollections
            Number of collections analyzed.
            Setter for property NumCollections
            Number of collections analyzed.

            """
            pass
        @property
        def NumCollection1(self) -> int:
            """
            Getter for property NumCollection1
            The number of objects in collection 1.

            """
            pass
        @NumCollection1.setter
        def NumCollection1(self, value: int):
            """
            Getter for property NumCollection1
            The number of objects in collection 1.
            Setter for property NumCollection1
            The number of objects in collection 1.

            """
            pass
        @property
        def NumCollection2(self) -> int:
            """
            Getter for property NumCollection2
            The number of objects in collection 2.

            """
            pass
        @NumCollection2.setter
        def NumCollection2(self, value: int):
            """
            Getter for property NumCollection2
            The number of objects in collection 2.
            Setter for property NumCollection2
            The number of objects in collection 2.

            """
            pass
        @property
        def NumPairs(self) -> int:
            """
            Getter for property NumPairs
            The number of pairs built from                                           the object collections.

            """
            pass
        @NumPairs.setter
        def NumPairs(self, value: int):
            """
            Getter for property NumPairs
            The number of pairs built from                                           the object collections.
            Setter for property NumPairs
            The number of pairs built from                                           the object collections.

            """
            pass
        @property
        def NumExcludedPairs(self) -> int:
            """
            Getter for property NumExcludedPairs
            The number of pairs that were                                           excluded from analysis, either                                           due to exclusion rules or                                           explicit pair exclusion.

            """
            pass
        @NumExcludedPairs.setter
        def NumExcludedPairs(self, value: int):
            """
            Getter for property NumExcludedPairs
            The number of pairs that were                                           excluded from analysis, either                                           due to exclusion rules or                                           explicit pair exclusion.
            Setter for property NumExcludedPairs
            The number of pairs that were                                           excluded from analysis, either                                           due to exclusion rules or                                           explicit pair exclusion.

            """
            pass
        @property
        def NumChangedPairs(self) -> int:
            """
            Getter for property NumChangedPairs
            The number of pairs that had                                           changed since the previous                                           clearance analysis.

            """
            pass
        @NumChangedPairs.setter
        def NumChangedPairs(self, value: int):
            """
            Getter for property NumChangedPairs
            The number of pairs that had                                           changed since the previous                                           clearance analysis.
            Setter for property NumChangedPairs
            The number of pairs that had                                           changed since the previous                                           clearance analysis.

            """
            pass
        @property
        def NumChangedObjs(self) -> int:
            """
            Getter for property NumChangedObjs
            The number of objects that had                                           changed since the previous                                           clearance analysis.

            """
            pass
        @NumChangedObjs.setter
        def NumChangedObjs(self, value: int):
            """
            Getter for property NumChangedObjs
            The number of objects that had                                           changed since the previous                                           clearance analysis.
            Setter for property NumChangedObjs
            The number of objects that had                                           changed since the previous                                           clearance analysis.

            """
            pass
        @property
        def NumCheckedPairs(self) -> int:
            """
            Getter for property NumCheckedPairs
            The total number of pairs that                                           underwent analysis.

            """
            pass
        @NumCheckedPairs.setter
        def NumCheckedPairs(self, value: int):
            """
            Getter for property NumCheckedPairs
            The total number of pairs that                                           underwent analysis.
            Setter for property NumCheckedPairs
            The total number of pairs that                                           underwent analysis.

            """
            pass
        @property
        def NumNewHard(self) -> int:
            """
            Getter for property NumNewHard
            The total number of new hard                                           interferences.

            """
            pass
        @NumNewHard.setter
        def NumNewHard(self, value: int):
            """
            Getter for property NumNewHard
            The total number of new hard                                           interferences.
            Setter for property NumNewHard
            The total number of new hard                                           interferences.

            """
            pass
        @property
        def NumNewSoft(self) -> int:
            """
            Getter for property NumNewSoft
            The total number of new soft                                           interferences.

            """
            pass
        @NumNewSoft.setter
        def NumNewSoft(self, value: int):
            """
            Getter for property NumNewSoft
            The total number of new soft                                           interferences.
            Setter for property NumNewSoft
            The total number of new soft                                           interferences.

            """
            pass
        @property
        def NumNewTouching(self) -> int:
            """
            Getter for property NumNewTouching
            The total number of new touching                                           interferences.

            """
            pass
        @NumNewTouching.setter
        def NumNewTouching(self, value: int):
            """
            Getter for property NumNewTouching
            The total number of new touching                                           interferences.
            Setter for property NumNewTouching
            The total number of new touching                                           interferences.

            """
            pass
        @property
        def NumNewContainment(self) -> int:
            """
            Getter for property NumNewContainment
            The total number of new containment                                           interferences.

            """
            pass
        @NumNewContainment.setter
        def NumNewContainment(self, value: int):
            """
            Getter for property NumNewContainment
            The total number of new containment                                           interferences.
            Setter for property NumNewContainment
            The total number of new containment                                           interferences.

            """
            pass
        @property
        def NumNewAllInterf(self) -> int:
            """
            Getter for property NumNewAllInterf
            The total number of new                                           interferences.

            """
            pass
        @NumNewAllInterf.setter
        def NumNewAllInterf(self, value: int):
            """
            Getter for property NumNewAllInterf
            The total number of new                                           interferences.
            Setter for property NumNewAllInterf
            The total number of new                                           interferences.

            """
            pass
        @property
        def NumHard(self) -> int:
            """
            Getter for property NumHard
            The total number of hard                                           interferences.

            """
            pass
        @NumHard.setter
        def NumHard(self, value: int):
            """
            Getter for property NumHard
            The total number of hard                                           interferences.
            Setter for property NumHard
            The total number of hard                                           interferences.

            """
            pass
        @property
        def NumSoft(self) -> int:
            """
            Getter for property NumSoft
            The total number of soft                                           interferences.

            """
            pass
        @NumSoft.setter
        def NumSoft(self, value: int):
            """
            Getter for property NumSoft
            The total number of soft                                           interferences.
            Setter for property NumSoft
            The total number of soft                                           interferences.

            """
            pass
        @property
        def NumTouching(self) -> int:
            """
            Getter for property NumTouching
            The total number of touching                                           interferences.

            """
            pass
        @NumTouching.setter
        def NumTouching(self, value: int):
            """
            Getter for property NumTouching
            The total number of touching                                           interferences.
            Setter for property NumTouching
            The total number of touching                                           interferences.

            """
            pass
        @property
        def NumContainment(self) -> int:
            """
            Getter for property NumContainment
            The total number of containment                                           interferences.

            """
            pass
        @NumContainment.setter
        def NumContainment(self, value: int):
            """
            Getter for property NumContainment
            The total number of containment                                           interferences.
            Setter for property NumContainment
            The total number of containment                                           interferences.

            """
            pass
        @property
        def NumAllInterf(self) -> int:
            """
            Getter for property NumAllInterf
            The total number of interferences.

            """
            pass
        @NumAllInterf.setter
        def NumAllInterf(self, value: int):
            """
            Getter for property NumAllInterf
            The total number of interferences.
            Setter for property NumAllInterf
            The total number of interferences.

            """
            pass
        @property
        def JobStatus(self) -> ClearanceSet.JobStatus:
            """
            Getter for property JobStatus
            Indicates if the analysis was                                                                   aborted.

            """
            pass
        @JobStatus.setter
        def JobStatus(self, value: ClearanceSet.JobStatus):
            """
            Getter for property JobStatus
            Indicates if the analysis was                                                                   aborted.
            Setter for property JobStatus
            Indicates if the analysis was                                                                   aborted.

            """
            pass
        @property
        def NumZones(self) -> int:
            """
            Getter for property NumZones
            The number of assembly zones used                                           by the analysis (batch only).

            """
            pass
        @NumZones.setter
        def NumZones(self, value: int):
            """
            Getter for property NumZones
            The number of assembly zones used                                           by the analysis (batch only).
            Setter for property NumZones
            The number of assembly zones used                                           by the analysis (batch only).

            """
            pass
    def CalculatePenetrationDepth(self, firstObjects: List[NXOpen.DisplayableObject], secondObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Calculate penetration depth for a set of hard interferences.  The interferences
                must be specified using two parallel arrays: the objects in the first interference should
                be given in the first elements of the arrays, the objects in the second interference should
                be given in the second elements of the arrays, etc. 
        """
        pass
    def Copy(self, name: str, mode: ClearanceSet.CopyMode) -> ClearanceSet:
        """
         Makes a copy of a dataset.  You must supply a unique name.  There are three
                modes in which to copy the dataset: NXOpen.Assemblies.ClearanceSet.CopyMode.NoResults 
                only copies the setup data.  The version of the new dataset is set to zero (meaning clearance analysis 
                has not been run);  NXOpen.Assemblies.ClearanceSet.CopyMode.Results makes a copy of the current 
                analysis results, but not the interference bodies; NXOpen.Assemblies.ClearanceSet.CopyMode.InterfBodies 
                makes a complete copy of the results. The name must  be less than MAX_LINE_SIZE characters long 
         Returns newSet ( ClearanceSet NXOpen.A):  the dataset that is copied .
        """
        pass
    def CreateInterferenceGeometry(self, firstObjects: List[NXOpen.DisplayableObject], secondObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Construct interference geometry for a set of hard interferences.  The interferences
                must be specified using two parallel arrays: the objects in the first interference should
                be given in the first elements of the arrays, the objects in the second interference should
                be given in the second elements of the arrays, etc. 
        """
        pass
    def Delete(self) -> None:
        """
         Delete this clearance set 
        """
        pass
    def DeleteAllInterferences(self) -> None:
        """
         Deletes all interference results stored in this clearance set. 
        """
        pass
    def DeleteExcludedPair(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, markOutOfDate: bool) -> None:
        """
         Deletes the excluded pair along with all data associated with it. Both objects
                must be members of the given clearance set. If the object pair does not refer
                to an excluded pair, an error is returned. It is recommended to set
                markOutOfDate to true, else the deleted pair will not partake in reanalyses
                until either object1 or object2 are marked out-of-date.
            
        """
        pass
    def DeleteInterference(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> None:
        """
         Deletes the interference for a given object pair. Both objects must be
                members of the given data set. If the object pair does not refer to an
                existing interference, an error is returned. All data associated with the
                interference is deleted. 
        """
        pass
    def DetectObsoleteSettings(self, doCleanupNow: bool) -> bool:
        """
         Detects whether a clearance set was defined with settings which are obsoleteno longer supported.  For example,
                prior to NX 9.0, an optional setting "ignore mated pairs" was available.  Existing results may still be read
                from a clearance set with obsolete settings, but the next time analysis is performed, the obsolete settings
                will be removed and all existing results cleared.
                Optionally, this method can perform any required cleanup now, instead of waiting until the next analysis. 
         Returns containsObsoleteSettings (bool):  whether the clearance set contains obsolete settings .
        """
        pass
    def ExcludePairs(self, firstObjects: List[NXOpen.DisplayableObject], secondObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Excludes the set of object pairs if they are not already excluded pairs.
                Both objects must be members of the given clearance set. If any of the
                object pairs are existing interferences, then those interferences along
                with all data associated with them are deleted.
            
        """
        pass
    def GetExcludedPairText(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> str:
        """
         Inquires the text string associated with the excluded pair. Both objects
                must be members of the given clearance set. If the object pair does not
                refer to an existing excluded pair, an error is returned. 
         Returns text (str):  The text associated with the excluded pair .
        """
        pass
    def GetInterferenceData(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> Tuple[ClearanceSet.InterferenceType, bool, List[NXOpen.DisplayableObject], NXOpen.Point3d, NXOpen.Point3d, str, int, int, int, float, NXOpen.Vector3d, NXOpen.Point3d, NXOpen.Point3d]:
        """
         Inquires the data associated with a given pair of interfering objects. 
         Returns A tuple consisting of (type, newInterference, interfBodies, point1, point2, text, interfNum, config, depthResult, depth, direction, minPoint, maxPoint). 
         - type is:  ClearanceSet.InterferenceType NXOpen.A. the interference type .
         - newInterference is: bool. the flag for new interference .
         - interfBodies is:  NXOpen.DisplayableObject Li. the list of interference bodies .
         - point1 is:  NXOpen.Point3d. a point on the first object .
         - point2 is:  NXOpen.Point3d. a point on the second object .
         - text is: str. text associated with the interference .
         - interfNum is: int. a unique number for the interference .
         - config is: int. the configuration index .
         - depthResult is: int. result status of penetration depth calculation .
         - depth is: float. depth of penetration .
         - direction is:  NXOpen.Vector3d. a unit vector indicating the direction of penetration .
         - minPoint is:  NXOpen.Point3d. the points on the interference region at the extremes of depth .
         - maxPoint is:  NXOpen.Point3d. the points on the interference region at the extremes of depth .

        """
        pass
    def GetInterferenceStatus(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> ClearanceSet.InterferenceStatus:
        """
         Inquires the status associated with a given pair of interfering objects. 
                The status is only retrieved if an interference exists between the two objects. 
         Returns status ( ClearanceSet.InterferenceStatus NXOpen.A):  the current status of the interference .
        """
        pass
    def GetIsPairChanged(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> bool:
        """
         Inquires if an object pair has changed since the last analysis run. Both
                objects must be solid bodies or facet models that are members of the
                clearance analysis data set. If either object has changed since the last
                analysis run, then isChanged is returned as TRUE. If no analysis has
                been run on either of the objects, TRUE is returned. 
         Returns isChanged (bool):  Has this pair changed since the last analysis run? .
        """
        pass
    def GetNextInterference(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> Tuple[NXOpen.DisplayableObject, NXOpen.DisplayableObject]:
        """
         Cycles the interference in a clearance analysis data set. Interferences
                are stored as object pairs. Start the cycling using  as the
                input values for both object1 and object2. This routine passes back the
                tags of the objects that define the next interference. 
                returned for either object indicates the end of the cycling. 
         Returns A tuple consisting of (nextObject1, nextObject2). 
         - nextObject1 is:  NXOpen.DisplayableObject. the first object in the pair of the next interference .
         - nextObject2 is:  NXOpen.DisplayableObject. the second object in the pair of the next interference .

        """
        pass
    def GetNumberOfInterferences(self) -> int:
        """
         Inquires the number of interferences stored in a clearance analysis
                data set. If clearance analysis has never been run on the data set, an
                error is returned. 
         Returns numberOfInterferences (int):  the number of interferences associated with the dataset .
        """
        pass
    def GetResults(self) -> ClearanceSet.Summary:
        """
         Inquires a summary of the results of the most recent clearance analysis run. 
                The NXOpen.Assemblies.ClearanceSet.Summary structure is 
                filled with analysis statistics, including numbers of objects, number of pairs,
                number of checked pairs, and number of interferences of each type. If
                clearance analysis has never been run on the data set, an error is
                returned. 
         Returns results ( ClearanceSet.Summary NXOpen.A):  the summary structure .
        """
        pass
    def GetVersion(self) -> int:
        """
         Gets the version of a clearance analysis dataset. The version indicates
                how many times clearance analysis has been run on a data set. If the
                version is zero, then the analysis has never been run. 
         Returns version (int): .
        """
        pass
    def MarkExcludedPairsUpToDate(self, firstObjects: List[NXOpen.DisplayableObject], secondObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Marks the set of excluded pairs up-to-date if they are out-of-date. 
                Both objects must be members of the given clearance set. If any object
                pair does not refer to an existing excluded pair, an error is returned. 
        """
        pass
    def PerformAnalysis(self, reanalyzeOption: ClearanceSet.ReanalyzeOutOfDateExcludedPairs) -> None:
        """
         Perform an analysis on this clearance set with option to specify whether
                out-of-date excluded pairs will be reanalyzed. You can specify to use the
                Customer Default setting, or you can specify a true or false option to override
                the Customer Default. 
        """
        pass
    def ReanalyzePairs(self, firstObjects: List[NXOpen.DisplayableObject], secondObjects: List[NXOpen.DisplayableObject], calculationMethod: ClearanceSet.ReanalyzePairCalculationMethod) -> None:
        """
         Reanalyze a set of interferences using the specified analysis method.  The interferences
                must be specified using two parallel arrays: the objects in the first interference should
                be given in the first elements of the arrays, the objects in the second interference should
                be given in the second elements of the arrays, etc. 
        """
        pass
    def SetExcludedPairText(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, text: str) -> None:
        """
         Associates a text string to an excluded pair. Both objects must be
                members of the given clearance set. If the object pair does not refer
                to an existing excluded pair, an error is returned. 
        """
        pass
    def SetInterferenceStatus(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, status: ClearanceSet.InterferenceStatus) -> None:
        """
         Set the status associated with a given pair of interfering objects. 
                The status is only filled if an interference exists between the two objects. 
        """
        pass
    def SetInterferenceText(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, text: str) -> None:
        """
         Associates a text string to an interfering object pair. Both objects must
                be members of the given dataset. If the object pair does not refer to
                an existing interference, an error is returned. 
        """
        pass
class CollaborativeContentType(Enum):
    """
    Members Include: 
     |Workset|  Workset 
     |Subset|  Subset 
     |ShapeDesignElement|  Shape Design Element in a Workset
     |ReuseDesignElement|  Reuse Design Element in a Workset
     |PromissoryDesignElement|  Promissory Design Element in a Workset
     |Subordinate|  Subordinate Design Element in a Workset
     |DesignFeature|  Design Feature
     |DesignControlElement|  Design Control Element
     |NotAssigned|  Non-collaborative content such as items

    """
    Workset: int
    Subset: int
    ShapeDesignElement: int
    ReuseDesignElement: int
    PromissoryDesignElement: int
    Subordinate: int
    DesignFeature: int
    DesignControlElement: int
    NotAssigned: int
    @staticmethod
    def ValueOf(value: int) -> CollaborativeContentType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Positioning
class ComponentAssembly(NXOpen.NXObject): 
    """
  Represents the set of NXOpen.Assemblies.Components that make up an
  assembly. Components are arranged in a tree structure, with a single component at the
  root. (See NXOpen.Assemblies.ComponentAssembly.RootComponent.) The
  components directly below the root are added to this assembly by calling
  NXOpen.Assemblies.ComponentAssembly.AddComponent. These "Top Level" components are
  said to be owned directly by this assembly. Top Level components may themselves have
  subcomponents.

  
  Certain methods in this class will only operate on Top Level components. For example,
  NXOpen.Assemblies.ComponentAssembly.MoveComponent will throw an exception if the
  input component is not owned directly by this assembly.  
  

  
  Note, however, that input components will be mapped onto the correct component in the
  assembly. See NXOpen.Assemblies.ComponentAssembly.MapComponentFromParent.
  

  
  For any methods that specify a component's position, the orientation matrix is in column order. 
  The first column of the matrix specifies the X axis, the second the Y axis, and the third the Z
  axis.
  
"""
    class CheckinCheckoutOption(Enum):
        """
        Members Include: 
         |DesignElement|  Checks in or Checks out the design element 
         |SourceItem|  Checks in or Checks out the source item that is referenced by a reuse design element or subordinate design element 
         |Both|  Checks in or Checks out the design element and its referenced source item 
         |Default|  Check In or Check Out option is determined by the system using whatever option is appropriate for the selected object type. For Reuse design element, the system defaults to checking out both the design element and the underlying item. 

        """
        DesignElement: int
        SourceItem: int
        Both: int
        Default: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.CheckinCheckoutOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CloseModified(Enum):
        """
        Members Include: 
         |FalseValue|  Close only unmodified parts, not modified parts 
         |TrueValue|  Close all parts, modified and unmodified 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.CloseModified:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OpenComponentStatus(Enum):
        """
        Members Include: 
         |SuccessfullyOpened|  The component was opened as expected 
         |DeletedByOpen|  The component was deleted on load as a result of the open 
         |CouldNotOpen|  The component could not be opened 

        """
        SuccessfullyOpened: int
        DeletedByOpen: int
        CouldNotOpen: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.OpenComponentStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OpenOption(Enum):
        """
        Members Include: 
         |ComponentOnly|  Open the component but none of its children.
                                                                        This option does not generally affect the representation state or reference set of already loaded
                                                                        components even if they are input components.
                                                                    
         |ImmediateChildren|  Open the immediate children of an already open component.
                                                                              This option does not generally affect the load state, representation state or reference set
                                                                              of components that are already loaded even if they are immediate children of the input components.
                                                                        
         |WholeAssembly|  Open the component and all of its children.
                                                                        This option does not generally affect the load state, representation state or reference set
                                                                        of components that are already loaded even if they are children of the input components.
                                                                    
         |ReapplyRevRule|  Reconfigure and open components based on current revision rules. 
                                                                        If this option is used in native mode, it will behave just like Open Component. 
                                                                        This option does not generally affect the representation state or reference set
                                                                        of components that are already loaded even if they are children of the input components.
                                                                    

        """
        ComponentOnly: int
        ImmediateChildren: int
        WholeAssembly: int
        ReapplyRevRule: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.OpenOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrderTargetLocation(Enum):
        """
        Members Include: 
         |PlaceBefore|  Move reordered NXOpen.Assemblies.Components before the target NXOpen.Assemblies.Component 
         |PlaceAfter|  Move reordered NXOpen.Assemblies.Components after the target NXOpen.Assemblies.Component 

        """
        PlaceBefore: int
        PlaceAfter: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.OrderTargetLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubstitutionMode(Enum):
        """
        Members Include: 
         |NonAssociative|  The old component is deleted, and the new one is added 
         |SingleComponent|  An associative substitution is performed. As far as possible,
                                                                                this will attempt to preserve assembly constraints and interpart
                                                                                links. 
         |All|  An associative substitution is performed on all components that
                                                                                represent the same prototype part. This effectively substitutes
                                                                                one child part for a new one. 

        """
        NonAssociative: int
        SingleComponent: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.SubstitutionMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SuppressedState(Enum):
        """
        Members Include: 
         |Inherit|  Inherit 
         |Suppressed|  Suppressed 
         |Unsuppressed|  Unsuppressed 
         |SuppressedByExp|  Suppressed by expression 
         |UnsuppressedByExp|  Unsuppressed by expression 

        """
        Inherit: int
        Suppressed: int
        Unsuppressed: int
        SuppressedByExp: int
        UnsuppressedByExp: int
        @staticmethod
        def ValueOf(value: int) -> ComponentAssembly.SuppressedState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveArrangement(self) -> Arrangement:
        """
        Getter for property: ( Arrangement NXOpen.A) ActiveArrangement
         Returns
                the currently active  NXOpen::Assemblies::Arrangement  for this ComponentAssembly
              
            
         
        """
        pass
    @ActiveArrangement.setter
    def ActiveArrangement(self, arrangement: Arrangement):
        """
        Setter for property: ( Arrangement NXOpen.A) ActiveArrangement
         Returns
                the currently active  NXOpen::Assemblies::Arrangement  for this ComponentAssembly
              
            
         
        """
        pass
    @property
    def Positioner(self) -> NXOpen.Positioning.ComponentPositioner:
        """
        Getter for property: ( NXOpen.Positioning.ComponentPositioner) Positioner
         Returns the component positioner for this assembly.  
            The positioner manages the component constraints.
              
         
        """
        pass
    @property
    def RootComponent(self) -> Component:
        """
        Getter for property: ( Component NXOpen.A) RootComponent
         Returns    the top-level component, i.  
          e. the component at the root of the component
                tree.  
           This component corresponds to the part that owns this
                 NXOpen::Assemblies::ComponentAssembly . The components below this will correspond to
                parts added by calling  NXOpen::Assemblies::ComponentAssembly::AddComponent .
                  
                Note that this will be NULL if there are no components in the tree. (I.e. if the part
                that owns this ComponentAssembly is a piece part.)
                  
              
         
        """
        pass
    @property
    def Arrangements() -> ArrangementCollection:
        """
         The collection of  NXOpen::Assemblies::Arrangement s defined in the ComponentAssembly 
        """
        pass
    @property
    def Explosions() -> ExplosionCollection:
        """
         The collection of  NXOpen::Assemblies::Explosion s defined in the ComponentAssembly 
        """
        pass
    @property
    def DrawingExplosions() -> DrawingExplosionCollection:
        """
         The collection of  NXOpen::Assemblies::DrawingExplosion s defined in the ComponentAssembly 
        """
        pass
    @property
    def ComponentPatterns() -> ComponentPatternCollection:
        """
         The collection of  NXOpen::Assemblies::ComponentPattern  defined in the ComponentAssembly 
        """
        pass
    @property
    def Subsets() -> SubsetCollection:
        """
         The collection of  NXOpen::Assemblies::Subset s defined in the ComponentAssembly 
        """
        pass
    @property
    def ClearanceSets() -> ClearanceSetCollection:
        """
         The collection of  NXOpen::Assemblies::ClearanceSet s defined in the ComponentAssembly 
        """
        pass
    @property
    def OrdersSet() -> OrderCollection:
        """
         The collection of  NXOpen::Assemblies::Order s defined in the ComponentAssembly 
        """
        pass
    @overload
    def AddComponent(self, part_to_add: str, reference_set_name: str, component_name: str, base_point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> Tuple[Component, NXOpen.PartLoadStatus]:
        """
         
                Creates a new NXOpen.Assemblies.Component in this assembly, based on an existing part file.
            
         Returns A tuple consisting of (component, load_status). 
         - component is:  Component NXOpen.A. The new Component .
         - load_status is:  NXOpen.PartLoadStatus. Result of loading the
                                                                                            part_to_add .

        """
        pass
    @overload
    def AddComponent(self, part_to_add: str, reference_set_name: str, component_name: str, base_point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int, uom_as_ngc: bool) -> Tuple[Component, NXOpen.PartLoadStatus]:
        """
         
                Creates a new NXOpen.Assemblies.Component in this assembly, based on an existing part file.
            
         Returns A tuple consisting of (component, load_status). 
         - component is:  Component NXOpen.A. The new Component .
         - load_status is:  NXOpen.PartLoadStatus. Result of loading the
                                                                                            part_to_add .

        """
        pass
    @overload
    def AddComponent(self, part_to_add: NXOpen.BasePart, reference_set_name: str, component_name: str, base_point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> Tuple[Component, NXOpen.PartLoadStatus]:
        """
         
                Creates a new NXOpen.Assemblies.Component in this assembly, based on an existing part file.
            
         Returns A tuple consisting of (component, load_status). 
         - component is:  Component NXOpen.A. The new Component .
         - load_status is:  NXOpen.PartLoadStatus. Result of loading the
                                                                                            part_to_add .

        """
        pass
    def AddComponents(self, partsToAdd: List[NXOpen.Part], point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int, referenceSetName: str, count: int, scatter: bool) -> List[Component]:
        """
         
                Creates new NXOpen.Assemblies.Component in this assembly, based on existing part files.
            
         Returns components ( Component List[NXOpen):  The array of components added to the parent part .
        """
        pass
    @overload
    def AddMasterPartComponent(self, part_to_add: str, reference_set_name: str, component_name: str, base_point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> Tuple[Component, NXOpen.PartLoadStatus]:
        """
         
                Creates a new NXOpen.Assemblies.Component in this assembly as master part.
            
         Returns A tuple consisting of (component, load_status). 
         - component is:  Component NXOpen.A. The new Component .
         - load_status is:  NXOpen.PartLoadStatus. Result of loading the part_to_add .

        """
        pass
    @overload
    def AddMasterPartComponent(self, part_to_add: NXOpen.Part, reference_set_name: str, component_name: str, base_point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> Tuple[Component, NXOpen.PartLoadStatus]:
        """
         
                Creates a new NXOpen.Assemblies.Component in this assembly as master part.
            
         Returns A tuple consisting of (component, load_status). 
         - component is:  Component NXOpen.A. The new Component .
         - load_status is:  NXOpen.PartLoadStatus. Result of loading the part_to_add .

        """
        pass
    def AddPendingComponent(self, part_to_add: str, pending_component: NXOpen.NXObject, reference_set_name: str, component_name: str, base_point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int, uom_as_ngc: bool) -> NXOpen.PartLoadStatus:
        """
                
                Add a pending NXOpen.Assemblies.Component in this assembly.
            
         Returns load_status ( NXOpen.PartLoadStatus):  Result of loading the
                                                                                            part_to_add .
        """
        pass
    def ChangeByName(self, name: str, part_occs: List[Component]) -> None:
        """
         Changes the current NXOpen.Assemblies.Arrangement of the given NXOpen.Assemblies.Components to the
            NXOpen.Assemblies.Arrangement with the given name.
        """
        pass
    def CheckinComponents(self, part_occs: List[Component], checkinInputOption: ComponentAssembly.CheckinCheckoutOption) -> NXOpen.ErrorList:
        """
                
                Checks in array of components as per the option NXOpen.Assemblies.ComponentAssembly.CheckinCheckoutOption.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during the check in  .
        """
        pass
    def CheckinDesignSession(self) -> NXOpen.ErrorList:
        """
                
                Checks in DesignSession.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during checking in of DesignSession  .
        """
        pass
    def CheckinWorkset(self) -> NXOpen.ErrorList:
        """
                
                Checks in workset.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during checking in of workset  .
        """
        pass
    def CheckoutAllModifiedObjects(self) -> Tuple[NXOpen.ErrorList, List[NXOpen.NXObject]]:
        """
                Checks out all modified objects in the current session. checkedOutObjects collection will be type of NXOpen.BasePart or  NXOpen.PDM.DesignElementRevision
            
         Returns A tuple consisting of (error_list, checkedOutObjects). 
         - error_list is:  NXOpen.ErrorList. Any errors that occurred during checking out of objects  .
         - checkedOutObjects is:  NXOpen.NXObject Li. Array of NXObjects checked out  .

        """
        pass
    def CheckoutAllModifiedObjectsWithChangeIdAndComments(self, comment: str, change_id: str) -> Tuple[NXOpen.ErrorList, List[NXOpen.NXObject]]:
        """
                Checks out all modified objects in the current session. checkedOutObjects collection will be type of NXOpen.BasePart or  NXOpen.PDM.DesignElementRevision
                and and user can provide comments and change id for the check-out operation
            
         Returns A tuple consisting of (error_list, checkedOutObjects). 
         - error_list is:  NXOpen.ErrorList. Any errors that occurred during checking out of objects  .
         - checkedOutObjects is:  NXOpen.NXObject Li. Array of NXObjects checked out  .

        """
        pass
    def CheckoutComponents(self, part_occs: List[Component], checkoutInputOption: ComponentAssembly.CheckinCheckoutOption) -> NXOpen.ErrorList:
        """
                
                Checks out array of components as per the option NXOpen.Assemblies.ComponentAssembly.CheckinCheckoutOption.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during the check out  .
        """
        pass
    def CheckoutComponentsWithChangeIdAndComments(self, change_id: str, comment: str, part_occs: List[Component], checkoutInputOption: ComponentAssembly.CheckinCheckoutOption) -> NXOpen.ErrorList:
        """
                
                Checks out array of components as per the option NXOpen.Assemblies.ComponentAssembly.CheckinCheckoutOption.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during the check out  .
        """
        pass
    def CheckoutDesignSession(self) -> NXOpen.ErrorList:
        """
                
                Checks out DesignSession.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during checking out of DesignSession  .
        """
        pass
    def CheckoutDesignSessionWithChangeIdAndComments(self, change_id: str, comment: str) -> NXOpen.ErrorList:
        """
                
                Checks out DesignSession with comment and change id
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during checking out of DesignSession  .
        """
        pass
    def CheckoutWorkset(self) -> NXOpen.ErrorList:
        """
                
                Checks out workset.
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during checking out of workset  .
        """
        pass
    def CheckoutWorksetWithChangeIdAndComments(self, comment: str, change_id: str) -> NXOpen.ErrorList:
        """
                
                Checks out workset with comment and change id
            
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred during checking out of workset  .
        """
        pass
    def CloseComponents(self, components_to_close: List[Component], whole_tree: NXOpen.BasePart.CloseWholeTree, close_modified: ComponentAssembly.CloseModified) -> NXOpen.PartCloseStatus:
        """
         
                Given an array of components, close the components. 
                This close of the components will check for different reasons that the part cannot be closed. 
                The reasons will be returned in the PartCloseStatus object.    
            
         Returns close_status ( NXOpen.PartCloseStatus):  Close status for the parts  .
        """
        pass
    def ConvertRememberedMcs(self) -> None:
        """
         Converts all remembered mating constraints in the part of this assembly to remembered
                assembly constraints
            
        """
        pass
    def CopyComponents(self, components: List[Component]) -> List[Component]:
        """
                Given an array of components, creates copies of the components such that each copy is created
                under the parent assembly of the original component. The original components do not need to be
                under the same parent assembly as each other.
                
                The number of new components may be different from the original number of components if problems
                occurred during the copy.
                
            
         Returns new_components ( Component List[NXOpen):  The newly created copies. .
        """
        pass
    def CreateComponentPatternBuilder(self, compPattern: ComponentPattern) -> ComponentPatternBuilder:
        """
                
                Creates a NXOpen.Assemblies.ComponentPatternBuilder object 
                This can be used to create or edit a component pattern.
            
         Returns builder ( ComponentPatternBuilder NXOpen.A): .
        """
        pass
    def CreateConstraintGroupBuilder(self, group: NXOpen.Positioning.ComponentConstraintGroup, context_component: Component) -> NXOpen.Positioning.ComponentConstraintGroupBuilder:
        """
                
                Creates a NXOpen.Positioning.ComponentConstraintGroupBuilder object.
                This can be used to create a constraint group or edit an existing constraint group.
                The context component decides which displayed constraints are to be used from
                the member constraints of an existing constraint group. If the context component
                is  the displayed constraints used are in the same part as the member
                constraints.
            
         Returns builder ( NXOpen.Positioning.ComponentConstraintGroupBuilder): .
        """
        pass
    def CreateIsolateViewWithComponents(self, components: List[Component]) -> Tuple[NXOpen.ErrorList, NXOpen.View]:
        """
                  Creates a temporary NXOpen.View and shows array of components in it 
                  and treats this as Isolate view till it gets undisplayed. Only one Isolate view can be created
                  for the assembly.
                  Returns NXOpen.View which is treated as Isolate View.
            
         Returns A tuple consisting of (errors, view). 
         - errors is:  NXOpen.ErrorList. list of errors encountered during components shown in isolate view .
         - view is:  NXOpen.View. Return the isolate view .

        """
        pass
    def CreateMatingConverter(self) -> NXOpen.Positioning.MatingConverter:
        """
         Creates a NXOpen.Positioning.MatingConverter object for this assembly.
                This can be used to convert Mating Conditions in this part and in its child components
                to Assembly Constraints. Note that this part need not be the work part for this. 
            
         Returns converter ( NXOpen.Positioning.MatingConverter):  The new Mating Converter .
        """
        pass
    def DeleteMatingConditions(self) -> None:
        """
         Delete all the mating conditions in this assembly.  This can be used before creating
                assembly constraints in the assembly, if the mating conditions are not being converted.
                Component-component mating conditions and inherited mating conditions are not deleted.
                Update should be called afterwards.
            
        """
        pass
    def DesignWorksetProductForceRecipeReplay(self, components: List[Component]) -> None:
        """
                This api performs force recipe replay of products in design workset. if input context assembly is not design workset or input products is not
                a child component of the input "assembly" then it will error out. If design workset is having multiple configuration of same product assembly,
                then only the primary configured product can be a replay candidate.
                Note: This operation clears all the existing undo mark if replay is succesfully completed or if replay fails during load of product.
            
        """
        pass
    def GetActiveOrder(self) -> Order:
        """
         Returns the active order in the part
         Returns activeOrder ( Order NXOpen.A): .
        """
        pass
    def GetAsRequiredQuantity(self, component: Component) -> str:
        """
                Gets the as-required quantity on this component.
            
         Returns as_required_string (str):  As-Required string "AR".
        """
        pass
    def GetCheckedoutStatusOfObjects(self) -> Tuple[List[NXOpen.NXObject], List[NXOpen.NXObject]]:
        """
               Returns the checkedout status (checkedoutnon checkedout) of all the objects open in NX.
            
         Returns A tuple consisting of (checkedOutObjects, uncheckedOutObjects). 
         - checkedOutObjects is:  NXOpen.NXObject Li. Array of NXObjects which are open in session and checked out .
         - uncheckedOutObjects is:  NXOpen.NXObject Li. Array of NXObjects which are open in session but not checkout .

        """
        pass
    def GetComponentOrders(self) -> List[ComponentOrder]:
        """
         Returns all NXOpen.Assemblies.ComponentOrders available in the part
         Returns orders ( ComponentOrder List[NXOpen):  Returns array of NXOpen.Assemblies.ComponentOrders in part .
        """
        pass
    def GetComponentQuantityType(self, component: Component) -> ComponentQuantity:
        """
                Gets the quantity type of the components. Returns NXOpen.Assemblies.ComponentQuantity.
            
         Returns component_quantity_type ( ComponentQuantity NXOpen.A):  Quantity type an enumeration value .
        """
        pass
    def GetIntegerQuantity(self, component: Component) -> int:
        """
                Gets the value of the integer quantity of component.
            
         Returns integer_quantity (int):  Integer quantity value .
        """
        pass
    def GetNonGeometricState(self, component: Component) -> bool:
        """
                Gets the component state as Geometric or Non-Geometric. 
            
         Returns non_geometric_state (bool):  True if the component is non-geometric, false otherwise .
        """
        pass
    def GetRealQuantity(self, component: Component) -> Tuple[float, str]:
        """
                Gets the value of real quantity and corresponding units on this component.
            
         Returns A tuple consisting of (real_quantity, units). 
         - real_quantity is: float. Real quantity value .
         - units is: str. Units .

        """
        pass
    @overload
    def GetSuppressedState(self, component: Component) -> Tuple[ComponentAssembly.SuppressedState, bool]:
        """
                Gets the suppression state of the component in its controlling arrangement
            
         Returns A tuple consisting of (suppressedState, controlled). 
         - suppressedState is:  ComponentAssembly.SuppressedState NXOpen.A. The suppressed state .
         - controlled is: bool. Is the suppression state controlled at the level of arrangement? .

        """
        pass
    @overload
    def GetSuppressedState(self, component: Component, arrangement: Arrangement) -> Tuple[ComponentAssembly.SuppressedState, bool]:
        """
                Gets the suppression state of the component in the given arrangement.
            
         Returns A tuple consisting of (suppressedState, controlled). 
         - suppressedState is:  ComponentAssembly.SuppressedState NXOpen.A. The suppressed state .
         - controlled is: bool. Is the suppression state controlled at 
                                                the level of arrangement?
                                            .

        """
        pass
    @overload
    def GetSuppressionExpression(self, component: Component) -> NXOpen.Expression:
        """
                Gets the expression controlling the suppression of the component in its
                controlling arrangement
            
         Returns expression ( NXOpen.Expression):  The suppression expression. .
        """
        pass
    @overload
    def GetSuppressionExpression(self, component: Component, arrangement: Arrangement) -> NXOpen.Expression:
        """
                Gets the expression controlling the suppression of the component in the given
                arrangment
            
         Returns expression ( NXOpen.Expression):  The suppression expression. .
        """
        pass
    def HideComponentsInIsolateView(self, components: List[Component]) -> Tuple[NXOpen.ErrorList, NXOpen.View]:
        """
                  Hides array of components in Isolate view NXOpen.View.
                  If Isolate view doesn't exist then this API doesn't do anything.
                  Returns NXOpen.View which is treated as Isolate View.
            
         Returns A tuple consisting of (errors, view). 
         - errors is:  NXOpen.ErrorList. list of errors encountered during components shown in isolate view .
         - view is:  NXOpen.View. Return the isolate view .

        """
        pass
    def InsertProduct(self, productPart: NXOpen.Part, layer: int) -> Tuple[Component, NXOpen.PartLoadStatus]:
        """
         
                Adds a product into workset part at identity location.
            
         Returns A tuple consisting of (component, load_status). 
         - component is:  Component NXOpen.A. The new Component .
         - load_status is:  NXOpen.PartLoadStatus. Result of loading the
                                                                                            part_to_add .

        """
        pass
    def MapComponentFromParent(self, component: Component) -> Component:
        """
         Maps a component in a parent assembly onto a corresponding component in this
                assembly. For example, given an Axle assembly: 
                
                                       
                       Axle
                           \          
                            \         
                 Left        Right     
                 Wheel       Wheel     
                 
                and a Car assembly containing two Axle components:
                
                 
                                   Car
                            _______ |_______                   
                                           \                  
                                            \                 
                     Front                     Rear            
                     Axle                      Axle            
                         \                        \          
                          \                        \         
             Front Left  Front Right    Rear Left   Rear Right 
               Wheel       Wheel         Wheel       Wheel     
                
                then calling Axle.MapComponentFromParent with the Front Left Wheel component will
                return the Left Wheel component. Note that calling Car.MapComponentFromParent on
                Left Wheel will not work. See NXOpen.Assemblies.ComponentAssembly.MapComponentsFromSubassembly.
                
                
                Calling Axle.MapComponent with the Left Wheel component will simply return Left
                Wheel, i.e. it is a null operation.
                
                
                Note that calling this method may load additional assembly data from the Axle part. 
                
            
         Returns mapped_component ( Component NXOpen.A):  The mapped component. This will be defined in the
                                                                             component tree of this assembly parameter.
                                                                        .
        """
        pass
    def MapComponentsFromSubassembly(self, component: Component) -> List[Component]:
        """
         Maps a component in a subassembly onto the corresponding components in this
                parent assembly. For example, given an Axle assembly: 
                
                                       
                       Axle
                           \          
                            \         
                 Left        Right     
                 Wheel       Wheel     
                 
                and a Car assembly containing two Axle components:
                
                 
                                   Car
                            _______ |_______                   
                                           \                  
                                            \                 
                     Front                     Rear            
                     Axle                      Axle            
                         \                        \          
                          \                        \         
             Front Left  Front Right    Rear Left   Rear Right 
               Wheel       Wheel         Wheel       Wheel     
                
                then calling Car.MapComponentsFromSubassembly on Left Wheel will return
                Front Left Wheel and Rear Left Wheel.
                See also NXOpen.Assemblies.ComponentAssembly.MapComponentFromParent.
                
            
         Returns mapped_components ( Component List[NXOpen):  The mapped components. 
                                                                                 .
        """
        pass
    def MoveComponent(self, component: Component, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
         Moves a component by specifying a translation and rotation. Note that these are
                specified in the coordinates of this assembly, which are not necessarily the
                coordinates of the displayed part. Note that the rotation matrix is expected to 
                be stored in a column order fashion.
            
        """
        pass
    def MoveToPendingComponent(self, component: NXOpen.NXObject) -> None:
        """
                
                Move a NXOpen.Assemblies.Component in this assembly to a pending list.
                The NXOpen.Assemblies.Component should be previously in the pending list and
                just got added into the assembly.
            
        """
        pass
    def OpenComponents(self, open_option: ComponentAssembly.OpenOption, components_to_open: List[Component]) -> Tuple[NXOpen.PartLoadStatus, List[ComponentAssembly.OpenComponentStatus]]:
        """
         Given an array of components, open the components using the NXOpen.Assemblies.ComponentAssembly.OpenOption.
                This function will also take current NXOpen.LoadOptions into account, but may not necessarily affect the state of already loaded components.
                Specifically, the NXOpen.Assemblies.ComponentAssembly.OpenOption.WholeAssembly and 
                NXOpen.Assemblies.ComponentAssembly.OpenOption.ImmediateChildren do not generally affect the load state of
                already loaded components. If you intend to load both unloaded and already loaded components fully, 
                then you need to use the NXOpen.Assemblies.ComponentAssembly.OpenOption.ComponentOnly option for
                all components you need to fully load, together with setting the NXOpen.LoadOptions.UsePartialLoading property to false.
            
         Returns A tuple consisting of (load_status, open_status). 
         - load_status is:  NXOpen.PartLoadStatus. If any components could not be loaded, this object contains the error information. .
         - open_status is:  ComponentAssembly.OpenComponentStatus List[NXOpen. Shows the status of the objects in an indexed array according to if they could be opened .

        """
        pass
    @overload
    def ReleaseSuppression(self, components: List[Component], arrangements: List[Arrangement]) -> NXOpen.ErrorList:
        """
                Release control of the suppression state of an array of components. The components
                will no longer have their suppression state controlled by the given arrangements. (Note
                that it is not an error if the given arrangements do not control the components.)
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the release .
        """
        pass
    @overload
    def ReleaseSuppression(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                Release control of the suppression state of an array of components. The components
                will no longer have their suppression state controlled by any of the arrangements
                in the ComponentAssembly.
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the release .
        """
        pass
    def RemoveComponent(self, component: Component) -> None:
        """
         Removes a component from this assemebly.  
        """
        pass
    def ReorderChildrenOfParent(self, order: ComponentOrder, parentComponent: Component, componentsToReorder: List[Component]) -> None:
        """
         Assigns a new order to immediate children NXOpen.Assemblies.Components of parent NXOpen.Assemblies.Component.
        """
        pass
    def ReorderComponents(self, order: ComponentOrder, componentsToReorder: List[Component], targetComponent: Component, beforeOrAfter: ComponentAssembly.OrderTargetLocation) -> None:
        """
         Reorders the array of NXOpen.Assemblies.Components before or after the target NXOpen.Assemblies.Component.
               NXOpen.Assemblies.Components to reorder and the target NXOpen.Assemblies.Component should be children of 
               the same immediate parent.
            
        """
        pass
    def ReplaceReferenceSet(self, component: Component, new_reference_set: str) -> None:
        """
         Replaces the reference set used by a component.  Note that the names of the default reference sets Empty and Entire Part can be
                obtained from NXOpen.Assemblies.Component.EmptyPartRefsetName or
                NXOpen.Assemblies.Component.EntirePartRefsetName. 
        """
        pass
    def ReplaceReferenceSetInOwners(self, new_reference_set: str, components: List[Component]) -> NXOpen.ErrorList:
        """
         
                Sets the reference set used to represent each component in an array. This is the equivalent of calling:
                
                NXOpen.Assemblies.Component.DirectOwner
                
                
                NXOpen.Assemblies.ComponentAssembly.ReplaceReferenceSet
                
                
                on each component in the array. However, this method will ensure that the reference set operations
                are carried out in the correct order, so that any effects caused by a parent's reference set change will
                be correctly reflected in the children. If changing reference set on components at various levels in the
                assembly, use this method.
                
                Note that the names of the default reference sets Empty and Entire Part can be
                obtained from NXOpen.Assemblies.Component.EmptyPartRefsetName or
                NXOpen.Assemblies.Component.EntirePartRefsetName.
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the edit.
        """
        pass
    def RestructureComponents(self, orig_components: List[Component], new_parent_component: Component, delete_flag: bool) -> Tuple[List[Component], NXOpen.ErrorList]:
        """
                Given an array of components and a specified parent this function will transfer the given components to the parent. 
                The original components do not need to be under the same parent assembly as each other.
                
                The number of new components may be different from the original number of components if problems occurred during the transfer
                
            
         Returns A tuple consisting of (new_components, error_list). 
         - new_components is:  Component List[NXOpen. Restructured components .
         - error_list is:  NXOpen.ErrorList. Any errors that occurred during the restructure  .

        """
        pass
    def SetAsRequiredQuantity(self, component: Component) -> None:
        """
                Sets the as-required quantity on this component.
            
        """
        pass
    def SetDefault(self, arrangement: Arrangement) -> None:
        """
         Set the default NXOpen.Assemblies.Arrangement for the given NXOpen.Assemblies.ComponentAssembly. 
        """
        pass
    def SetEmptyRefset(self, component: Component) -> None:
        """
         
                Convenience method for setting the reference set used to represent a component
                to be empty
            
        """
        pass
    def SetEntirePartRefset(self, component: Component) -> None:
        """
         
                Convenience method for setting the reference set used to represent a component
                to be the entire part.
            
        """
        pass
    def SetIntegerQuantity(self, component: Component, integer_quantity: int) -> None:
        """
                Sets the integer quantity on this component.
            
        """
        pass
    def SetNonGeometricState(self, component: Component, non_geometric_state: bool) -> None:
        """
                Sets the component state to Geometric or Non-Geometric.
                Component which are made non-geometric are undrawn from graphics area.
            
        """
        pass
    def SetRealQuantity(self, component: Component, real_quantity: float, quantity_units: str) -> None:
        """
                Sets the real quantity and corresponding units on this component.
            
        """
        pass
    def ShowComponentsInIsolateView(self, components: List[Component]) -> Tuple[NXOpen.ErrorList, NXOpen.View]:
        """
                  Shows array of components in Isolate view NXOpen.View.
                  If Isolate view doesn't exist then this API doesn't do anything.
                  Returns NXOpen.View which is treated as Isolate View.
            
         Returns A tuple consisting of (errors, view). 
         - errors is:  NXOpen.ErrorList. list of errors encountered during components shown in isolate view .
         - view is:  NXOpen.View. Return the isolate view .

        """
        pass
    def SubstituteComponent(self, component: Component, part: NXOpen.BasePart, new_name: str, reference_set: str, layer: int, mode: ComponentAssembly.SubstitutionMode) -> Component:
        """
                Substitutes an old component with a new component. The new component represents a new part, but 
                will be placed in the same location as the original.
            
         Returns new_component ( Component NXOpen.A):  The new Component that replaces the old one. .
        """
        pass
    @overload
    def SuppressComponents(self, components: List[Component], arrangements: List[Arrangement]) -> NXOpen.ErrorList:
        """
                Suppresses an array of components
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the suppress .
        """
        pass
    @overload
    def SuppressComponents(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                Suppresses an array of components in all NXOpen.Assemblies.Arrangement s in this ComponentAssembly
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the suppress .
        """
        pass
    @overload
    def SuppressComponents(self, components: List[Component], arrangements: List[Arrangement], expression: str) -> NXOpen.ErrorList:
        """
                Suppresses an array of components in all NXOpen.Assemblies.Arrangement s in this ComponentAssembly
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the suppress .
        """
        pass
    @overload
    def UnsuppressComponents(self, components: List[Component], arrangements: List[Arrangement]) -> NXOpen.ErrorList:
        """
                Unsuppresses an array of components in this ComponentAssembly
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the unsuppress .
        """
        pass
    @overload
    def UnsuppressComponents(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                Unsuppresses an array of components in all NXOpen.Assemblies.Arrangement s in this ComponentAssembly
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the unsuppress .
        """
        pass
import NXOpen
class ComponentGroupCollection(NXOpen.TaggedObjectCollection): 
    """ 
     Contains a collection of Component Groups a NXOpen.Assemblies.ComponentGroup
    that are defined within an Assembly part. 
    """
    def CreateComponentGroup(self, name: str) -> ComponentGroup:
        """
         Creates a NXOpen.Assemblies.ComponentGroup with the given name 
         Returns component_group ( ComponentGroup NXOpen.A):  the ComponentGroup created .
        """
        pass
    def FindObject(self, journal_identifier: str) -> ComponentGroup:
        """
         Finds the  NXOpen.Assemblies.ComponentGroup  with the given identifier as recorded in a journal. 
               An object may not return the same value as its JournalIdentifier in different versions of 
               the software. However newer versions of the software should find the same object when 
               FindObject is passed older versions of its journal identifier. In general, this method 
               should not be used in handwritten code and exists to support record and playback of journals.
               An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( ComponentGroup NXOpen.A):  ComponentGroup with this identifier .
        """
        pass
import NXOpen
class ComponentGroup(NXOpen.NXObject): 
    """ 
   Represents a Component Group that is defined within an Assembly.
   """
    @property
    def NumberOfComponents(self) -> int:
        """
        Getter for property: (int) NumberOfComponents
         Returns the number of Components within this Component Group   
            
         
        """
        pass
    def AddComponent(self, component: Component, and_children: bool) -> None:
        """
         Adds a component to a component group.  If add chilren is true, the children of the added component
                   are also added.
               
        """
        pass
    def GetComponents(self) -> List[Component]:
        """
         Returns the Components within this Component Group 
         Returns components ( Component List[NXOpen):  the components .
        """
        pass
    def Open(self) -> NXOpen.PartLoadStatus:
        """
         
               Loads a selected component group by name during Assembly part file open.
               
               This operation is used in conjunction with the NXOpen.LoadOptions
               enumerator NXOpen.LoadOptions.LoadComponents and using the
               specify filter option.
               This method is not intented to be used after an Assembly has been
               loaded but during the loading operations.
               
               
         Returns load_status ( NXOpen.PartLoadStatus):  Parts
                                         that could not be loaded and their associated errors. .
        """
        pass
    def RemoveComponent(self, component: Component) -> None:
        """
         Removes a component from a component group 
        """
        pass
class ComponentOrder(Order): 
    """  Represents an order object that stores the order of child NXOpen.Assemblies.Components in context
       of parent NXOpen.Assemblies.ComponentAssembly. Typically, an NXOpen.Assemblies.ComponentAssembly 
       can have multiple NXOpen.Assemblies.ComponentOrders and user can switch between 
       NXOpen.Assemblies.ComponentOrders to display different order of the assembly in the tree. 
  """
    def AskChildrenOrder(self, parent: Component) -> List[Component]:
        """
         Given a parent NXOpen.Assemblies.Component this method
                returns immediate child NXOpen.Assemblies.Components in the same order in
                which they are ordered in this NXOpen.Assemblies.ComponentOrder
         Returns children ( Component List[NXOpen):  Children of NXOpen.Assemblies.Component  .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ComponentPatternBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs various NXOpen.Assemblies.ComponentPattern operations.
        Input to this class can be PSM facet objects.
    """
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option to specify whether the  NXOpen::Assemblies::ComponentPattern  is 
                    associative or not.  
                     
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, isAssociative: bool):
        """
        Setter for property: (bool) Associative
         Returns the option to specify whether the  NXOpen::Assemblies::ComponentPattern  is 
                    associative or not.  
                     
                  
         
        """
        pass
    @property
    def ComponentPatternSet(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ComponentPatternSet
         Returns the  NXOpen::Assemblies::Component  for pattern.  
          
                  
         
        """
        pass
    @property
    def CopyConstraintPattern(self) -> bool:
        """
        Getter for property: (bool) CopyConstraintPattern
         Returns the copy constraint option.  
           The copy constraint type of pattern is created 
                    when this option is enabled otherwise Pure Reference pattern is created.
                  
         
        """
        pass
    @CopyConstraintPattern.setter
    def CopyConstraintPattern(self, isCopyConstraintReferencePattern: bool):
        """
        Setter for property: (bool) CopyConstraintPattern
         Returns the copy constraint option.  
           The copy constraint type of pattern is created 
                    when this option is enabled otherwise Pure Reference pattern is created.
                  
         
        """
        pass
    @property
    def PatternService(self) -> NXOpen.GeometricUtilities.PatternDefinition:
        """
        Getter for property: ( NXOpen.GeometricUtilities.PatternDefinition) PatternService
         Returns the  NXOpen::GeometricUtilities::PatternDefinition .  
          
                  
         
        """
        pass
    def GetDynamicPositioning(self) -> bool:
        """
         Returns the dynamic positioning flag.
                 
         Returns isDynamicPositioning (bool): .
        """
        pass
    def SetDynamicPositioning(self, isDynamicPositioning: bool) -> None:
        """
         Sets the dynamic positioning flag. It will enable or disable the dynamic preview of the components. 
                
        """
        pass
    def SetObject(self, compPattern: ComponentPattern) -> None:
        """
         Sets the object selected for pattern definition 
        """
        pass
import NXOpen
class ComponentPatternCollection(NXOpen.TaggedObjectCollection): 
    """ Represents the collection object for all component patterns.
        An instance of this class can be obtained from the NXOpen.Assemblies.ComponentAssembly.
     """
    def FindObject(self, journal_identifier: str) -> ComponentPattern:
        """
         Finds the  NXOpen.Assemblies.ComponentPattern  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
                
         Returns found ( ComponentPattern NXOpen.A):  Component pattern with this identifier, or  if no such pattern exists .
        """
        pass
    def GetAllComponentPatterns(self) -> List[ComponentPattern]:
        """
         Returns all the component patterns in an assembly.
         Returns componentPatterns ( ComponentPattern List[NXOpen): .
        """
        pass
import NXOpen
class ComponentPattern(NXOpen.NXObject): 
    """ Represents the component pattern class. Input to this class can be PSM facet objects. 
    """
    def ChangeReferencePatternTemplate(self, firstBaseInstanceIndex: int, secondBaseInstanceIndex: int) -> None:
        """
         Changes the template component of a reference pattern to a pattern member at indices (firstBaseInstanceIndex, secondBaseInstanceIndex).
                
        """
        pass
    def Delete(self, deleteComponents: bool) -> None:
        """
         Deletes the component pattern object.
                
        """
        pass
    def DisplayInformation(self) -> None:
        """
         Displays the information of the component pattern.
                
        """
        pass
    def GetAllPatternMembers(self) -> List[PatternMember]:
        """
         Returns all the pattern members.
                
         Returns patternMembers ( PatternMember List[NXOpen): .
        """
        pass
    def GetComponentsToPattern(self) -> List[Component]:
        """
         Gets all the Assemblies.Component that are selected for component pattern.
                
         Returns components ( Component List[NXOpen): .
        """
        pass
    def GetPatternDeferredStatus(self) -> bool:
        """
          Gets the deferred status of the component pattern.
                
         Returns isPatternDeferred (bool): .
        """
        pass
    def GetPatternName(self) -> str:
        """
         Gets the component pattern name.
                
         Returns name (str): .
        """
        pass
    def GetPatternSuppressedStatus(self) -> bool:
        """
         Gets the suppressed status of the component pattern. 
                
         Returns isPatternSuppressed (bool): .
        """
        pass
    def LoadRelatedGeometry(self) -> NXOpen.PartLoadStatus:
        """
         Loads the parts containing data referenced by this pattern, 
                    including the parts that are patterned and parts containing 
                    the objects that define the pattern parameters.
                
         Returns loadStatus ( NXOpen.PartLoadStatus):  Error information for any part that could not be loaded. .
        """
        pass
    def Suppress(self) -> None:
        """
         Suppresses the component pattern object.
                
        """
        pass
    def Unsuppress(self) -> None:
        """
         Unsuppresses the component pattern object.
                
        """
        pass
class ComponentQuantity(Enum):
    """
    Members Include: 
     |NotSet|  No quantity 
     |Integer|  Integer quantity 
     |Real|  Real quantity 
     |AsRequired|  Quantity As required. 

    """
    NotSet: int
    Integer: int
    Real: int
    AsRequired: int
    @staticmethod
    def ValueOf(value: int) -> ComponentQuantity:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.PDM
import NXOpen.Positioning
import NXOpen.Routing
class Component(NXOpen.DisplayableObject): 
    """ 
    Represents a component in a NXOpen.Assemblies.ComponentAssembly. Note that a
    Component is an occurrence whose prototype is a NXOpen.Part. See
    NXOpen.NXObject.Prototype.

    

    Components are arranged in a tree, with each component having a single parent, and one
    or more children. The top of the tree is the Root Component (see
    NXOpen.Assemblies.ComponentAssembly.RootComponent which has a 
    parent. The components below the root are referred to as "Top Level" components, which
    represent the component parts that have been added directly to the
    ComponentAssembly. (Calling NXOpen.Assemblies.ComponentAssembly.AddComponent will
    create a new Top Level component.) Components beneath the top level represent
    components defined in sub-assemblies of the main assembly.

    
    
   """
    class RepresentationMode(Enum):
        """
        Members Include: 
         |Lightweight|  The component's solid bodies are all displayed using the lightweight representation 
         |Partial|  The component's solid bodies are displayed with some being exact and some being shown lightweight 
         |Exact|  The component's solid bodies are displayed with the exact data 
         |NotSet|  There are no bodies to display for the current component 

        """
        Lightweight: int
        Partial: int
        Exact: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> Component.RepresentationMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CollaborativeContentType(self) -> CollaborativeContentType:
        """
        Getter for property: ( CollaborativeContentType NXOpen.A) CollaborativeContentType
         Returns the collaborative content type of this component.  
            
         
        """
        pass
    @property
    def DesignElementRevision(self) -> NXOpen.PDM.DesignElementRevision:
        """
        Getter for property: ( NXOpen.PDM.DesignElementRevision) DesignElementRevision
         Returns the  NXOpen::PDM::DesignElementRevision  that corresponds to this component.  
          
                This can be NULL if the component is not a design element.
                This will return parent reuse design element revision if this component represent a  NXOpen::PDM::DesignSubordinateRevision  .
               
         
        """
        pass
    @property
    def DesignSubordinateRevision(self) -> NXOpen.PDM.DesignSubordinateRevision:
        """
        Getter for property: ( NXOpen.PDM.DesignSubordinateRevision) DesignSubordinateRevision
         Returns the  NXOpen::PDM::DesignSubordinateRevision  that corresponds to this component.  
          
                This can be NULL if the component is not a subordinate design element.
               
         
        """
        pass
    @property
    def DirectOwner(self) -> ComponentAssembly:
        """
        Getter for property: ( ComponentAssembly NXOpen.A) DirectOwner
         Returns the  NXOpen::Assemblies::ComponentAssembly  which owns this component as a "Top Level" component.  
          
                For components in a multi-level assembly, this is NOT the same the part that owns this component object. 
                I.e. it is not the same as calling:
                 @code 
                 NXOpen.NXObject.OwningPart()
                 @endcode 
                 @code 
                NXOpen.BasePart.ComponentAssembly()
                 @endcode 
                An exception will be thrown if the owner of the component is not loaded.
               
         
        """
        pass
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the displayable name of the prototype part.  
          
              
         
        """
        pass
    @property
    def EmptyPartRefsetName(self) -> str:
        """
        Getter for property: (str) EmptyPartRefsetName
         Returns the name of the reference set which represents the empty set.  
           This
                can be used as a parameter to  NXOpen::Assemblies::ComponentAssembly::ReplaceReferenceSet .
              
         
        """
        pass
    @property
    def EntirePartRefsetName(self) -> str:
        """
        Getter for property: (str) EntirePartRefsetName
         Returns the name of the reference set which represents the entire part.  
           This
                can be used as a parameter to  NXOpen::Assemblies::ComponentAssembly::ReplaceReferenceSet .
              
         
        """
        pass
    @property
    def FixConstraint(self) -> NXOpen.Positioning.ComponentConstraint:
        """
        Getter for property: ( NXOpen.Positioning.ComponentConstraint) FixConstraint
         Returns a fix  NXOpen::Positioning::ComponentConstraint  of this component.  
          
                The constraint may be suppressed or NULL.  If the part 
                controlling the position of this component is not loaded then NULL
                will be returned.
              
         
        """
        pass
    @property
    def IsComponentOrAncestorSuppressed(self) -> bool:
        """
        Getter for property: (bool) IsComponentOrAncestorSuppressed
         Returns
                the suppressed state of the component in its assembly context.  
           
                This will reflect whether the component itself is explicitly suppressed in its
                controlling parent or is suppressed just on the basis of one of its ancestors
                being explicitly suppressed.  
                (See  NXOpen::Assemblies::Component::IsSuppressed .)
              
         
        """
        pass
    @property
    def IsFixed(self) -> bool:
        """
        Getter for property: (bool) IsFixed
         Returns the fixed state of this component.  
            True if there is an unsuppressed
                 NXOpen::Positioning::ComponentConstraint  fix constraint on this component
                and false otherwise.  If the part controlling the position of this
                component is not loaded then false will be returned.
              
         
        """
        pass
    @property
    def IsSuppressed(self) -> bool:
        """
        Getter for property: (bool) IsSuppressed
         Returns
                the suppressed state of the component in its controlling arrangement.  
           
                This only returns whether or not the component was explicitly suppressed and does not
                reflect when the component is suppressed due to the suppression of an ancestor.
                (See  NXOpen::Assemblies::Component::IsComponentOrAncestorSuppressed .)
              
         
        """
        pass
    @property
    def ModelElementRevision(self) -> NXOpen.PDM.ModelElementRevision:
        """
        Getter for property: ( NXOpen.PDM.ModelElementRevision) ModelElementRevision
         Returns the  NXOpen::PDM::ModelElementRevision  that corresponds to this component.  
          
                This can be NULL if the component is not a model element.
                This will return parent reuse design element revision if this component represent a  NXOpen::PDM::DesignSubordinateRevision  .
                If component is independent design feature then this will return  NXOpen::PDM::DesignFeatureRevision .
               
         
        """
        pass
    @property
    def Parent(self) -> Component:
        """
        Getter for property: ( Component NXOpen.A) Parent
         Returns the parent of the component.  
           For the root component of an assembly, this
                will be NULL. See  NXOpen::Assemblies::ComponentAssembly::RootComponent .
               
         
        """
        pass
    @property
    def PartitionSchemeInstance(self) -> PartitionSchemeInstance:
        """
        Getter for property: ( PartitionSchemeInstance NXOpen.A) PartitionSchemeInstance
         Returns the  NXOpen::Assemblies::PartitionSchemeInstance  associated with this component, if it exists.  
                          
               
         
        """
        pass
    @property
    def ReferenceSet(self) -> str:
        """
        Getter for property: (str) ReferenceSet
         Returns 
                the name of the reference set used for this component
              
            
         
        """
        pass
    @property
    def Subset(self) -> Subset:
        """
        Getter for property: ( Subset NXOpen.A) Subset
         Returns the  NXOpen::Assemblies::Subset  that corresponds to this component.  
          
                This can be NULL if the component is not a subset.   
         
        """
        pass
    @property
    def SuppressingArrangement(self) -> Arrangement:
        """
        Getter for property: ( Arrangement NXOpen.A) SuppressingArrangement
         Returns
                the  NXOpen::Assemblies::Arrangement  that controls this component's
                suppression state.  
            The controlling Arrangement will be defined in a
                 NXOpen::Assemblies::ComponentAssembly  in the tree above this Component.
                  
                Note: In the current release, Arrangements are only used for controlling a
                component's suppression state. In future releases, further attributes will be
                controlled via Arrangements.
                  
              
         
        """
        pass
    @property
    def UsedArrangement(self) -> Arrangement:
        """
        Getter for property: ( Arrangement NXOpen.A) UsedArrangement
         Returns
                the Arrangement used for this component.  
           See  NXOpen::Assemblies::Component::SetUsedArrangement 
              
         
        """
        pass
    def AddToPartitions(self, components: List[Component], partitions: List[Partition]) -> None:
        """
         Add partitions for the selected NXOpen.Assemblies.Components across all possible 
                NXOpen.Assemblies.Partitions.
        """
        pass
    def CreateEmptyPartFamilyInstanceSelectionCriteria(self, family: Template) -> InstanceSelectionCriteria:
        """
         Creates an empty NXOpen.PartFamily.InstanceSelectionCriteria 
         Returns selectionCriteria ( InstanceSelectionCriteria NXOpen.P): .
        """
        pass
    def DeleteInstanceUserAttribute(self, type: NXOpen.NXObject.AttributeType, title: str, delete_entire_array: bool, option: NXOpen.Update.Option) -> None:
        """
         Deletes the first attribute encountered with the given Type, Title and Index.
                If a candidate attribute is not an array attribute, the DeleteEntireArray input is ignored,
                otherwise the last element of the array is deleted.
                NOTE: This method does not support the use of NXOpen.NXObject.AttributeType.Reference. 
        """
        pass
    def DeleteInstanceUserAttributes(self, type: NXOpen.NXObject.AttributeType, option: NXOpen.Update.Option) -> None:
        """
         Deletes the attributes encountered with the given Type with option to update or not.
                NOTE: This method does not support the use of NXOpen.NXObject.AttributeType.Reference. 
        """
        pass
    def DeletePartFamilyInstanceSelectionCriteria(self) -> None:
        """
         Deletes NXOpen.PartFamily.InstanceSelectionCriteria associated with this component 
        """
        pass
    def DisplayComponentsExact(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                Sets an array of components to display using the exact representation.
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the display as exact .
        """
        pass
    def DisplayComponentsLightweight(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                  Sets an array of components to display using the lightweight representation.
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the display as lightweight .
        """
        pass
    def EstablishIsolatedPositionOverride(self, parent: Component, arrangement: Arrangement) -> None:
        """
                Ensures there is an isolated positioning override for the NXOpen.Assemblies.Component in the given part of
                the given parent.  This method does nothing if the NXOpen.Assemblies.Component already has an isolated
                positioning override in the parent, or if any necessary data is unloaded.
                If parent is , the isolated positioning override will be created in the same part as the NXOpen.Assemblies.Component.
                
        """
        pass
    def EstablishPositionOverride(self, parent: Component) -> None:
        """
                Ensures there is a positioning override on component in the given part of
                the given parent.  This method does nothing if the component already has a
                positioning override in the parent, or if any necessary data is unloaded.
                If parent is , the positioning override will be created in the same part 
                as the NXOpen.Assemblies.Component.
            
        """
        pass
    def EvaluatePartFamilyInstanceSelectionCriteria(self) -> Tuple[bool, NXOpen.Part, str]:
        """
         Evaluate the NXOpen.PartFamily.InstanceSelectionCriteria associated with this component, and update the part family member 
         Returns A tuple consisting of (componentChanged, newPartFamilyMember, errorinfo). 
         - componentChanged is: bool. A flag indicating whether the part family member has changed .
         - newPartFamilyMember is:  NXOpen.Part. New part family member if the component is changed .
         - errorinfo is: str. error information .

        """
        pass
    def FindComponentPatterns(self) -> Tuple[ComponentPattern, List[ComponentPattern]]:
        """
         Finds NXOpen.Assemblies.ComponentPattern associated with this component.
                De-allocation of memory used for list of pattern definitions is responsibility of user. 
         Returns A tuple consisting of (patternDefinition, patternDefinitions). 
         - patternDefinition is:  ComponentPattern NXOpen.A. A Pattern which refers 'component' as one of its output instances .
         - patternDefinitions is:  ComponentPattern List[NXOpen. List of patterns which refer 'component' as its master component .

        """
        pass
    def FindOccurrence(self, proto: NXOpen.NXObject) -> NXOpen.NXObject:
        """
         Given a prototype object, returns the corresponding occurrence
              in this component. If the prototype is in the reference set used for this component
              an occurrence will always be returned, which may be transient or persistent.
              If the prototype is not in the reference set used for this component 
              an occurrence will only be returned if a persistent occurrence exists. 
              For an explanation of transient and persistent occurrences see the 
              Displayable UF Objects in an Assembly Context of the
              UF Objects chapter in the Open C Programmers Guide 
         Returns occurrence ( NXOpen.NXObject):  the occurrence of the prototype in this component .
        """
        pass
    def GetArrangements(self) -> List[Arrangement]:
        """
         Outputs the NXOpen.Assemblies.Arrangement objects within the NXOpen.Assemblies.Component.
                They are output in alphabetic order.
            
         Returns arrangements ( Arrangement List[NXOpen):  Alphabetically sorted arrangements .
        """
        pass
    def GetAsRequiredQuantity(self) -> str:
        """
                Gets the as-required quantity on this component.
            
         Returns as_required_string (str):  As-Required string "AR".
        """
        pass
    def GetChildren(self) -> List[Component]:
        """
         Returns the child components of this component 
                However, it does not return non-geometric components (NGCs)
                To enable this method to also return NGCs, set the following environment variable:
                UGII_ALLOW_NGC_IN_UGOPEN=YES 
         Returns children ( Component List[NXOpen):  .
        """
        pass
    def GetComponentQuantityType(self) -> ComponentQuantity:
        """
                Gets the quantity type of the components. Returns NXOpen.Assemblies.ComponentQuantity.
            
         Returns component_quantity_type ( ComponentQuantity NXOpen.A):  Quantity type an enumeration value .
        """
        pass
    def GetComponentRepresentationMode(self) -> Component.RepresentationMode:
        """
               Returns the representation mode for the component's bodies.
               This mode is dependent on the currently used reference set for the component.
            
         Returns representation_mode ( Component.RepresentationMode NXOpen.A):  The mode for the components display. An enumeration value. .
        """
        pass
    def GetConstraints(self) -> List[NXOpen.Positioning.ComponentConstraint]:
        """
         Returns the NXOpen.Positioning.ComponentConstraints directly connected to this component.  If
                the part containing those constraints is not loaded then no constraints will be 
                returned.
            
         Returns constraints ( NXOpen.Positioning.ComponentConstraint Li):  Constraints directly connected to this component .
        """
        pass
    @overload
    def GetDegreesOfFreedom(self) -> DegreesOfFreedom:
        """
         Returns the NXOpen.Assemblies.DegreesOfFreedom for this component. 
                Any constraints that reference unloaded data are ignored in the degrees of freedom calculation. An example
                would be if a constraint was referencing geometry in an unloaded component. When this occurs there may be
                a greater number of degrees of freedom than if all the data were loaded.
            
         Returns degrees_of_freedom ( DegreesOfFreedom NXOpen.A):  The degrees of freedom of this component. .
        """
        pass
    @overload
    def GetDegreesOfFreedom(self, components: List[Component]) -> DegreesOfFreedom:
        """
         Returns the NXOpen.Assemblies.DegreesOfFreedom for this component. 
                The degrees of freedom are found relative to the components passed in.
                Those components are regarded as fixed and only constraints directly 
                connecting this component with those in the array are considered.
                Note that any directly connected constraints that reference unloaded data
                are ignored in the degrees of freedom calculation. An example would be if
                a constraint was referencing geometry in an unloaded component. When this
                occurs there may be a greater number of degrees of freedom than if all
                the data were loaded.         
            
         Returns degrees_of_freedom ( DegreesOfFreedom NXOpen.A):  The degrees of freedom of this component. .
        """
        pass
    def GetInstanceBooleanUserAttribute(self, title: str, index: int) -> bool:
        """
         Gets a boolean attribute by Title and array Index.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributes. 
         Returns value (bool):   .
        """
        pass
    def GetInstanceIntegerUserAttribute(self, title: str, index: int) -> int:
        """
         Gets an integer attribute by Title and array Index.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributes. 
         Returns value (int):   .
        """
        pass
    def GetInstanceRealUserAttribute(self, title: str, index: int) -> float:
        """
         Gets a real attribute by Title and array Index.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributes. 
         Returns value (float):   .
        """
        pass
    def GetInstanceStringUserAttribute(self, title: str, index: int) -> str:
        """
         Gets a string attribute by Title and array Index.
                For reference type string attributes, the calculated StringValue is returned.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributes.
                Gets a string attribute value by title. 
         Returns value (str):   .
        """
        pass
    def GetInstanceTimeUserAttribute(self, title: str, index: int) -> str:
        """
         Gets a time attribute by Title and array Index.
                The date format set by the Customer Defaults is used.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributes. 
                Gets a time attribute by title. 
         Returns value (str):   .
        """
        pass
    def GetInstanceUserAttribute(self, title: str, type: NXOpen.NXObject.AttributeType, index: int) -> NXOpen.NXObject.AttributeInformation:
        """
         Gets the first attribute encountered on the object, if any, with a given Title, Type and array Index.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributes.
                The date format set by the Customer Defaults is used for attributes of type time.
                NOTE: This method does not support the use of NXOpen.NXObject.AttributeType.Reference.
                      Instead, use NXOpen.NXObject.AttributeType.String.
                      For reference type string attributes, both the ReferenceValue and the calculated StringValue are returned. 
         Returns info ( NXOpen.NXObject.AttributeInformation):   .
        """
        pass
    def GetInstanceUserAttributeAsString(self, title: str, type: NXOpen.NXObject.AttributeType, index: int) -> str:
        """
         Gets the first attribute encountered on the object, if any, with a given title, type and array index.
                The value of the attribute is converted to and returned as a string.
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                To get all the array elements of an array, please use NXOpen.NXObject.GetUserAttributesAsStrings.
                The date format set by the Customer Defaults is used for attributes of type time.
                NOTE: This method does not support the use of NXOpen.NXObject.AttributeType.Reference.
                      Instead, use NXOpen.NXObject.AttributeType.String.
                      For reference type string attributes, the calculated StringValue is returned. 
         Returns value (str):   .
        """
        pass
    def GetInstanceUserAttributeLock(self, title: str, type: NXOpen.NXObject.AttributeType) -> bool:
        """
         Determine the lock of the given attribute.
                For array attributes, the Title should be set to the array title, without the appended index.
                Individual array elements cannot be separately locked 
         Returns lock (bool):  .
        """
        pass
    @overload
    def GetInstanceUserAttributes(self) -> List[NXOpen.NXObject.AttributeInformation]:
        """
         Gets all the attributes that have been set on the given object.
                The elements of array attributes are returned individually in order of increasing indices. 
                The returned Title of an array element is the array title (without index). The Index data member holds the index.
                The date format set by the Customer Defaults is used.
                Reference type attributes are returned as being of type NXOpen.NXObject.AttributeType.String,
                and both the ReferenceValue and the calculated StringValue are returned. 
         Returns info ( NXOpen.NXObject.AttributeInformation Li):   .
        """
        pass
    def GetInstanceUserAttributesAsStrings(self) -> List[str]:
        """
         Gets all the attributes that have been set on the given object.
                The values are returned as strings.
                The elements of array attributes are returned individually in order of increasing indices. 
                The returned Title of an array element is the array title (without index). The Index data member holds the index.
                This method does not support the use of NXOpen.NXObject.AttributeType.Reference.
                Reference type attributes return the calculated StringValue.
                The date format set by the Customer Defaults is used. 
         Returns values (List[str]):   .
        """
        pass
    @overload
    def GetInstanceUserAttributes(self, includeUnset: bool) -> List[NXOpen.NXObject.AttributeInformation]:
        """
         Gets all the attributes that have been set on the given object, 
                as well as information from attribute templates that have not been set (if 'IncludeUnset' is 'true').
                The elements of array attributes are returned individually in order of increasing indices. 
                The returned Title of an array element is the array title (without index). The Index data member holds the index.
                The date format set by the Customer Defaults is used.
                Reference type attributes are returnes as being of type NXOpen.NXObject.AttributeType.String,
                and both the ReferenceValue and the calculated StringValue are returned. 
         Returns info ( NXOpen.NXObject.AttributeInformation Li):   .
        """
        pass
    def GetIntegerQuantity(self) -> int:
        """
                Gets the value of the integer quantity of component.
            
         Returns integer_quantity (int):  Integer quantity value .
        """
        pass
    def GetLayerOption(self) -> int:
        """
         
                Gets the layer option. This controls which layer the component's geometry will appear on in its parent part.
            
         Returns layer (int):  The layer option of the component in its parent part
                                             -1 Means that the component's geometry has the layer settings defined in its orginal part
                                              1-255 Means the components geometry is on the specified layer
                                      .
        """
        pass
    def GetNonGeometricState(self) -> bool:
        """
                Gets the component state as Geometric or Non-Geometric.
            
         Returns non_geometric_state (bool):  True if the component is non-geometric, false otherwise .
        """
        pass
    def GetPartFamilyInstanceSelectionCriteria(self) -> InstanceSelectionCriteria:
        """
         Obtains theNXOpen.PartFamily.InstanceSelectionCriteria, if it exists.
         Returns selectionCriteria ( InstanceSelectionCriteria NXOpen.P): .
        """
        pass
    def GetPosition(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
                Gets the position of a component
            
         Returns A tuple consisting of (position, orientation). 
         - position is:  NXOpen.Point3d. The origin of this component .
         - orientation is:  NXOpen.Matrix3x3. The orientation of this component .

        """
        pass
    def GetPositionOverrideParent(self) -> Component:
        """
                Find the highest level parent in which the position of component is
                overridden.  This will be  if the component is not overridden.
                It will be the root component if the component is overridden in
                the same part as itself.  It will be  if the position of the
                component is overridden in a parent assembly which is currently
                unloaded.
            
         Returns parent ( Component NXOpen.A): .
        """
        pass
    def GetPositionOverrideType(self) -> PositionOverrideType:
        """
                Gets the type of the highest level positioning override on the component.
            
         Returns override_type ( PositionOverrideType NXOpen.A): .
        """
        pass
    def GetRealQuantity(self) -> Tuple[float, str]:
        """
                Gets the value of real quantity and corresponding units on this component.
            
         Returns A tuple consisting of (real_quantity, quantity_units). 
         - real_quantity is: float. Real quantity value .
         - quantity_units is: str. Units .

        """
        pass
    def HasInstanceUserAttribute(self, title: str, type: NXOpen.NXObject.AttributeType, index: int) -> bool:
        """
         Determines if and attribute with the given Title, Type and array Index is present on the object
                If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
                The first element of an array has Index 0 (zero).
                NOTE: This method does not support the use of NXOpen.NXObject.AttributeType.Reference.
                      Instead, use NXOpen.NXObject.AttributeType.String. 
         Returns hasAttribute (bool):  .
        """
        pass
    def IsPartitionable(self, components: List[Component], partitions: List[Partition]) -> List[IsPartitionableResult]:
        """
         Validates and returns results for IsPartitionable for all input NXOpen.Assemblies.Component across all possible 
                NXOpen.Assemblies.Partition.
                All the components and partitions inputs should be unique and belong to same product assembly.
            
         Returns is_partitionable_results ( IsPartitionableResult List[NXOpen): .
        """
        pass
    def IsPositioningIsolated(self, arrangement: Arrangement) -> bool:
        """
         Get whether positioning for the selected NXOpen.Assemblies.Component is isolated in the specified 
                NXOpen.Assemblies.Arrangement. 
            
         Returns is_isolated (bool):  Whether positioning for the selected NXOpen.Assemblies.Component is isolated 
                                                                in the specified NXOpen.Assemblies.Arrangement.
        """
        pass
    def RecallAndListConstraints(self) -> List[NXOpen.Positioning.ComponentConstraint]:
        """
         Recalls the NXOpen.Positioning.ComponentConstraints previously remembered on the part
                of this component, creating new constraints from them.  The new constraints are
                incomplete and refer to the component.
            
         Returns recalled_constraints ( NXOpen.Positioning.ComponentConstraint Li):  The constraints created by the recall operation .
        """
        pass
    def RecallConstraints(self) -> None:
        """
         Recalls the NXOpen.Positioning.ComponentConstraints previously remembered on the part
                of this component, creating new constraints from them.  The new constraints are
                incomplete and refer to the component.
            
        """
        pass
    def RemoveFromPartitions(self, components: List[Component], partitions: List[Partition]) -> None:
        """
         Remove partitions for the selected NXOpen.Assemblies.Components across all possible 
                NXOpen.Assemblies.Partitions.
        """
        pass
    def RemovePositionOverride(self, parent: Component) -> None:
        """
                Removes the highest level positioning override on component in or below
                the given parent.  parent may be , in which case the highest level
                positioning override on component is removed.  This method does nothing
                if there is no positioning override on the component, or if any necessary
                data is unloaded.  The parent in which this component is overridden will be
                fully loaded as a result of this override removal.
            
        """
        pass
    def RemoveRememberedConstraints(self) -> None:
        """
         Remove all the remembered constraints stored on the part of this component.
            
        """
        pass
    def SetInstanceBooleanUserAttribute(self, title: str, index: int, value: bool, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies a boolean attribute with the option to update or not. 
        """
        pass
    def SetInstanceTimeUserAttribute(self, title: str, index: int, value: str, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies a time attribute with the option to update or not. 
                The time value is assumed to be in the current time zone of the machine running the program. 
                NX will store the value in UTC. 
        """
        pass
    @overload
    def SetInstanceUserAttribute(self, info: NXOpen.NXObject.AttributeInformation, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies an attribute with the option to update or not. 
                NOTE: This method does not support the use of NXOpen.NXObject.AttributeType.Reference.
                      Instead, set the type to NXOpen.NXObject.AttributeType.String and specify a ReferenceValue.
                The following data members of the Info structure are ignored by this method:
                    Alias
                    Inherited
                    Required
                    Unset
                    Locked
                The following data members of an attribute cannot be edited once the attribute is set:
                    Type 
                    Title
                    TitleAlias
                    Array
                    ArrayElementIndex
                    The dimensionality of the Unit specification (cannot change from mm to microA, but from mm to cm is fine) 
                The following data members can be set and modified only if the attribute is not associated with a template:
                    Category
                The following data of an attribute can be set if and only if the attribute is not associated with a template. It cannot be modified once set.
                    Array 
        """
        pass
    def SetInstanceUserAttributeLock(self, title: str, type: NXOpen.NXObject.AttributeType, lock: bool) -> None:
        """
         Lock or unlock the given attribute.
                For array attributes, the Title should be set to the array title, without the appended index.
                Individual array elements cannot be separately locked 
        """
        pass
    @overload
    def SetInstanceUserAttribute(self, title: str, index: int, value: int, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies an integer attribute with the option to update or not. 
        """
        pass
    @overload
    def SetInstanceUserAttribute(self, title: str, index: int, value: float, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies a real attribute with the option to update or not. 
        """
        pass
    @overload
    def SetInstanceUserAttribute(self, title: str, index: int, value: str, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies a string attribute with the option to update or not. 
        """
        pass
    @overload
    def SetInstanceUserAttribute(self, title: str, index: int, option: NXOpen.Update.Option) -> None:
        """
         Creates or modifies a null attribute with the option to update or not. 
        """
        pass
    def SetLayerOption(self, layer: int) -> None:
        """
         
                Sets the layer option. This controls which layer the component's geometry will appear on in its parent part.
            
        """
        pass
    def SetPartFamilyInstanceSelectionCriteria(self, selectionCriteria: InstanceSelectionCriteria) -> None:
        """
         Hooks NXOpen.PartFamily.InstanceSelectionCriteria to this component 
        """
        pass
    def SetPositioningIsolated(self, arrangement: Arrangement) -> None:
        """
         Set positioning for the selected NXOpen.Assemblies.Component as isolated in the specified 
                NXOpen.Assemblies.Arrangement. 
                
                The arrangement must be an isolated arrangement defined in the same part as the component.
            
        """
        pass
    def SetPositioningVaried(self, components: List[Component], set_as_varied: bool) -> None:
        """
         Set positioning for the selected NXOpen.Assemblies.Components across all possible 
                NXOpen.Assemblies.Arrangements.  Positioning can be set to either the same in all
                NXOpen.Assemblies.Arrangements, set_as_varied = FALSE, or individually positioned in each,
                set_as_varied = TRUE. 
        """
        pass
    def SetUsedArrangement(self, new_arrangement: Arrangement) -> None:
        """
                Changes the Arrangement used for this component. If this is the root component
                (i.e. it has no parent) then this is equivalent to setting the active arrangement
                in the owner. (See NXOpen.Assemblies.Component.DirectOwner and
                NXOpen.Assemblies.ComponentAssembly.ActiveArrangement.) For
                non-root components, this sets the arrangement used for this component in the
                context of its parent component. Note that this method should only be used for
                components which have children.
                
            
        """
        pass
    @overload
    def Suppress(self) -> None:
        """
                Suppresses the component in the ComponentAssembly that contains its controlling Arrangement. 
                The component will be suppressed in all Arrangements in the ComponentAssembly, not just
                in the controlling arrangement.
                This is equivalent to calling:
                NXOpen.Assemblies.Component.SuppressingArrangement
                NXOpen.Assemblies.Arrangement.Owner
                NXOpen.Assemblies.ComponentAssembly.SuppressComponents
            
        """
        pass
    @overload
    def Suppress(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                Suppresses an array of components in the ComponentAssembly that contains their
                controlling Arrangement.  The component will be suppressed in all Arrangements in
                the ComponentAssembly.  
                This is equivalent to calling:
                NXOpen.Assemblies.Component.SuppressingArrangement
                NXOpen.Assemblies.Arrangement.Owner
                And then calling 
                NXOpen.Assemblies.ComponentAssembly.SuppressComponents
                on the component array. Note that all components should have
                the same suppressing Arrangement.
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the suppress .
        """
        pass
    @overload
    def Unsuppress(self) -> None:
        """
                Unsuppresses the component in the ComponentAssembly that contains its controlling Arrangement. 
                The component will be unsuppressed in all Arrangements in the ComponentAssembly.
                This is equivalent to calling:
                NXOpen.Assemblies.Component.SuppressingArrangement
                NXOpen.Assemblies.Arrangement.Owner
                NXOpen.Assemblies.ComponentAssembly.UnsuppressComponents
            
        """
        pass
    @overload
    def Unsuppress(self, components: List[Component]) -> NXOpen.ErrorList:
        """
                Unsuppresses an array of components in the ComponentAssembly that contains their
                controlling Arrangement.  The component will be unsuppressed in all Arrangements in
                the ComponentAssembly.  This is equivalent to calling:
                NXOpen.Assemblies.Component.SuppressingArrangement
                NXOpen.Assemblies.Arrangement.Owner
                NXOpen.Assemblies.ComponentAssembly.UnsuppressComponents
                on the component array. Note that all components should have
                the same suppressing Arrangement.
            
         Returns errors ( NXOpen.ErrorList):  list of errors encountered during the unsuppress .
        """
        pass
    @overload
    def UpdateStructure(self, components: List[Component], n_levels: int) -> None:
        """
         Update the assembly structure for this assembly in the 
                context of the displayed part to the specified number of
                levels, ignoring components already processed by previous
                calls.
            
        """
        pass
    @overload
    def UpdateStructure(self, components: List[Component], n_levels: int, checkComponentsVisited: bool) -> None:
        """
         Update the assembly structure for this assembly in the 
                context of the displayed part to the specified number of
                levels.
            
        """
        pass
import NXOpen
class ConstraintDisplayBuilder(NXOpen.Builder): 
    """ The NXOpen.Assemblies.ConstraintDisplayBuilder can be used to control visibility
        of constraints and optionally components.  Any selected constraint is shown, and any
        constraint that refers to geometry in selected components is shown (subject to the
        setting of the VisibleConstraintsRule).  All other constraints are hidden.

        If ChangeComponentVisibility is on, then selected components and components positioned by
        selected constraints are shown, and all other components are hidden.  If
        ChangeComponentVisibility is off, then component visibility is not affected.


        This builder operates on displayed constraints.  A displayed constraint represents a single
        assembly constraint in a given assembly, and need not be in the same part as the assembly
        constraint it represents.  An assembly may contain more than one displayed constraint for a
        given assembly constraint.

    """
    class VisibleConstraintsRuleOptions(Enum):
        """
        Members Include: 
         |BetweenComponents|  Show only constraints that refer only to selected components 
         |ConnectedToComponents|  Show only constraints that refer at least once to a selected component 

        """
        BetweenComponents: int
        ConnectedToComponents: int
        @staticmethod
        def ValueOf(value: int) -> ConstraintDisplayBuilder.VisibleConstraintsRuleOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ChangeComponentVisibility(self) -> bool:
        """
        Getter for property: (bool) ChangeComponentVisibility
         Returns the flag indicating whether or not a Show Only operation should be done on the connecting
                    components.  
             
         
        """
        pass
    @ChangeComponentVisibility.setter
    def ChangeComponentVisibility(self, changeComponentVisibility: bool):
        """
        Setter for property: (bool) ChangeComponentVisibility
         Returns the flag indicating whether or not a Show Only operation should be done on the connecting
                    components.  
             
         
        """
        pass
    @property
    def FilterNavigator(self) -> bool:
        """
        Getter for property: (bool) FilterNavigator
         Returns the flag indicating whether the assembly navigator should filter hidden constraints.  
             
         
        """
        pass
    @FilterNavigator.setter
    def FilterNavigator(self, filterNavigator: bool):
        """
        Setter for property: (bool) FilterNavigator
         Returns the flag indicating whether the assembly navigator should filter hidden constraints.  
             
         
        """
        pass
    @property
    def ObjectSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectSelection
         Returns the selected constraints and components.  
            All selected constraints and components are shown
                    when the builder is committed, and so are constraints and components connected to them.   
         
        """
        pass
    @property
    def VisibleConstraintsRule(self) -> ConstraintDisplayBuilder.VisibleConstraintsRuleOptions:
        """
        Getter for property: ( ConstraintDisplayBuilder.VisibleConstraintsRuleOptions NXOpen.A) VisibleConstraintsRule
         Returns the rule determining which constraints are treated as connected to the selected components.  
             
         
        """
        pass
    @VisibleConstraintsRule.setter
    def VisibleConstraintsRule(self, visibleConstraintsRule: ConstraintDisplayBuilder.VisibleConstraintsRuleOptions):
        """
        Setter for property: ( ConstraintDisplayBuilder.VisibleConstraintsRuleOptions NXOpen.A) VisibleConstraintsRule
         Returns the rule determining which constraints are treated as connected to the selected components.  
             
         
        """
        pass
import NXOpen
import NXOpen.PDM
class CopyDesignElementBuilder(NXOpen.Builder): 
    """
    Represents a builder class that performs copying design element operation in 4GD.
    """
    @property
    def DesignElementsToCopy(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) DesignElementsToCopy
         Returns the design elements to copy   
            
         
        """
        pass
    def CreateDesignElementLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Creates the pre-creation objects for the design elements to be copied 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def DeleteCopiedComponents(self) -> None:
        """
         Removes the copied components created during the copy operation 
        """
        pass
    def GetLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns the pre-creation objects 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns the pre-creation objects which have unassign required attributes
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns the design element copy operation failures 
         Returns operationFailures ( NXOpen.ErrorList): .
        """
        pass
    def PartiallyCommit(self) -> None:
        """
         Copy design elements with minimal required information.Call to builder Commit is required after this to Commit creation.
        """
        pass
import NXOpen
class CreateComponentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.CreateComponentBuilder builder class.
    This builder class will perform various component creation operations under assembly, workset or subset. """
    pass
import NXOpen
class CreateNewComponentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.CreateNewComponentBuilder builder class. Input to this class can be PSM facet objects.
      """
    class ComponentCamType(Enum):
        """
        Members Include: 
         |Target|  Set the origin type to target
         |Resource|  Set the component type to resource
         |Workpiece|  Set the component type to workpiece

        """
        Target: int
        Resource: int
        Workpiece: int
        @staticmethod
        def ValueOf(value: int) -> CreateNewComponentBuilder.ComponentCamType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentLayerOptionType(Enum):
        """
        Members Include: 
         |Original|  Set the layer option type to original
         |Work|  Set the layer option type to work
         |AsSpecified|  Set the layer option type to as specified

        """
        Original: int
        Work: int
        AsSpecified: int
        @staticmethod
        def ValueOf(value: int) -> CreateNewComponentBuilder.ComponentLayerOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentOriginType(Enum):
        """
        Members Include: 
         |Wcs|  Set the origin type to wcs
         |Absolute|  Set the origin type to absolute
         |Newcsys|  Set the origin type to new csys

        """
        Wcs: int
        Absolute: int
        Newcsys: int
        @staticmethod
        def ValueOf(value: int) -> CreateNewComponentBuilder.ComponentOriginType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentReferenceSetType(Enum):
        """
        Members Include: 
         |Model|  Set the reference set to model
         |EntirePartOnly|  Set the reference set to entire part only
         |Other|  Set the reference to other 

        """
        Model: int
        EntirePartOnly: int
        Other: int
        @staticmethod
        def ValueOf(value: int) -> CreateNewComponentBuilder.ComponentReferenceSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentCam(self) -> CreateNewComponentBuilder.ComponentCamType:
        """
        Getter for property: ( CreateNewComponentBuilder.ComponentCamType NXOpen.A) ComponentCam
         Returns the cam component cam type   
            
         
        """
        pass
    @ComponentCam.setter
    def ComponentCam(self, componentCam: CreateNewComponentBuilder.ComponentCamType):
        """
        Setter for property: ( CreateNewComponentBuilder.ComponentCamType NXOpen.A) ComponentCam
         Returns the cam component cam type   
            
         
        """
        pass
    @property
    def ComponentOrigin(self) -> CreateNewComponentBuilder.ComponentOriginType:
        """
        Getter for property: ( CreateNewComponentBuilder.ComponentOriginType NXOpen.A) ComponentOrigin
         Returns the component origin   
            
         
        """
        pass
    @ComponentOrigin.setter
    def ComponentOrigin(self, componentOrigin: CreateNewComponentBuilder.ComponentOriginType):
        """
        Setter for property: ( CreateNewComponentBuilder.ComponentOriginType NXOpen.A) ComponentOrigin
         Returns the component origin   
            
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the destination coordinate system   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the destination coordinate system   
            
         
        """
        pass
    @property
    def DefiningObjectsAdded(self) -> bool:
        """
        Getter for property: (bool) DefiningObjectsAdded
         Returns the defining objects added toggle  
            
         
        """
        pass
    @DefiningObjectsAdded.setter
    def DefiningObjectsAdded(self, definingObjectsAdded: bool):
        """
        Setter for property: (bool) DefiningObjectsAdded
         Returns the defining objects added toggle  
            
         
        """
        pass
    @property
    def LayerNumber(self) -> int:
        """
        Getter for property: (int) LayerNumber
         Returns the layer number   
            
         
        """
        pass
    @LayerNumber.setter
    def LayerNumber(self, layerNumber: int):
        """
        Setter for property: (int) LayerNumber
         Returns the layer number   
            
         
        """
        pass
    @property
    def LayerOption(self) -> CreateNewComponentBuilder.ComponentLayerOptionType:
        """
        Getter for property: ( CreateNewComponentBuilder.ComponentLayerOptionType NXOpen.A) LayerOption
         Returns the layer option   
            
         
        """
        pass
    @LayerOption.setter
    def LayerOption(self, layerOption: CreateNewComponentBuilder.ComponentLayerOptionType):
        """
        Setter for property: ( CreateNewComponentBuilder.ComponentLayerOptionType NXOpen.A) LayerOption
         Returns the layer option   
            
         
        """
        pass
    @property
    def NewComponentName(self) -> str:
        """
        Getter for property: (str) NewComponentName
         Returns the new component name   
            
         
        """
        pass
    @NewComponentName.setter
    def NewComponentName(self, newComponentName: str):
        """
        Setter for property: (str) NewComponentName
         Returns the new component name   
            
         
        """
        pass
    @property
    def NewFile(self) -> NXOpen.FileNew:
        """
        Getter for property: ( NXOpen.FileNew) NewFile
         Returns the file new object is get and set   
            
         
        """
        pass
    @NewFile.setter
    def NewFile(self, fileNew: NXOpen.FileNew):
        """
        Setter for property: ( NXOpen.FileNew) NewFile
         Returns the file new object is get and set   
            
         
        """
        pass
    @property
    def ObjectForNewComponent(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectForNewComponent
         Returns the objects for select block   
            
         
        """
        pass
    @property
    def OriginalObjectsDeleted(self) -> bool:
        """
        Getter for property: (bool) OriginalObjectsDeleted
         Returns the original objects deleted   
            
         
        """
        pass
    @OriginalObjectsDeleted.setter
    def OriginalObjectsDeleted(self, originalObjectsDeleted: bool):
        """
        Setter for property: (bool) OriginalObjectsDeleted
         Returns the original objects deleted   
            
         
        """
        pass
    @property
    def ReferenceSet(self) -> CreateNewComponentBuilder.ComponentReferenceSetType:
        """
        Getter for property: ( CreateNewComponentBuilder.ComponentReferenceSetType NXOpen.A) ReferenceSet
         Returns the reference set   
            
         
        """
        pass
    @ReferenceSet.setter
    def ReferenceSet(self, referenceSet: CreateNewComponentBuilder.ComponentReferenceSetType):
        """
        Setter for property: ( CreateNewComponentBuilder.ComponentReferenceSetType NXOpen.A) ReferenceSet
         Returns the reference set   
            
         
        """
        pass
    @property
    def ReferenceSetName(self) -> str:
        """
        Getter for property: (str) ReferenceSetName
         Returns the reference set name.  
           This should be used when reference set type is set to other  
         
        """
        pass
    @ReferenceSetName.setter
    def ReferenceSetName(self, referenceSetName: str):
        """
        Setter for property: (str) ReferenceSetName
         Returns the reference set name.  
           This should be used when reference set type is set to other  
         
        """
        pass
import NXOpen
class CreateOverridePartBuilder(NXOpen.Builder): 
    """ Represents a builder class that creates empty override part in the specified design elements.
    """
    @property
    def ComponentSelectionList(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) ComponentSelectionList
         Returns the list that contains components of reuse design element or subordinates
                    in which to create an empty override part.  
          
                  
         
        """
        pass
    @property
    def MakeWorkPart(self) -> bool:
        """
        Getter for property: (bool) MakeWorkPart
         Returns the state to determine whether to make the new override part as work part.  
          
                  
         
        """
        pass
    @MakeWorkPart.setter
    def MakeWorkPart(self, makeWorkPart: bool):
        """
        Setter for property: (bool) MakeWorkPart
         Returns the state to determine whether to make the new override part as work part.  
          
                  
         
        """
        pass
import NXOpen
class DeformBuilder(NXOpen.Builder): 
    """ A deform builder is used to create, edit, update and query deform.
        This buidler is slightly different from other common builders in that it does not really
        commit, e.g. the client does not need to commit. Instead, it holds some data and methods 
        to process the data for launching seconday UIBuilder to create or edit template-based deforms.
        For delete and query, the builder's methods will perform the operation immediately. 
    """
    def PostCreateNewDeform(self) -> None:
        """
         Postprocess for Creating a new deform
        """
        pass
    def PostUpdateDeform(self, isInErrorRecovery: bool) -> None:
        """
         Postprocess for Update an existed deform feature
        """
        pass
    def PreCreateNewDeform(self) -> bool:
        """
         Preprocess for Creating a new deform 
                    Preprocessing before creating a new deform.
                    Steps for create a new deform feature include: 
                    1. Pre-process the deform defintion part by invoking NXOpen.Assemblies.DeformManager.PreProcessDefinitionPart
                    2. Create a NXOpen.Assemblies.DeformBuilder using NXOpen.Assemblies.DeformManager.CreateDeformBuilder
                    3. Invoke NXOpen.Assemblies.DeformBuilder.PreCreateNewDeform
                    4. Create a NXOpen.UserDefinedTemplate.InstantiationBuilder using NXOpen.UserDefinedTemplate.Collection.CreateInstantiationBuilder
                    5. Set expressions and references for the instantiation builder 
                    6. Commit by calling NXOpen.Builder.Commit
                    7. Post-process by invoking NXOpen.Assemblies.DeformBuilder.PostCreateNewDeform
                
         Returns unitConvertHasWarning (bool): .
        """
        pass
    def PreUpdateDeform(self) -> bool:
        """
         Preprocess for Update an existed deform feature
                    Steps for update an existed deform feature include: 
                    1. Pre-process the deform defintion part by invoking NXOpen.Assemblies.DeformManager.PreProcessDefinitionPart 
                    2. Create a NXOpen.Assemblies.DeformBuilder using NXOpen.Assemblies.DeformManager.CreateDeformBuilder
                    3. Invoke NXOpen.Assemblies.DeformBuilder.PreUpdateDeform
                    4. Create a NXOpen.UserDefinedTemplate.InstantiationBuilder using NXOpen.UserDefinedTemplate.Collection.CreateInstantiationBuilder
                    5. Set expressions and references for the instantiation builder
                    6. Commit by calling NXOpen.Builder.Commit
                    7. Call NXOpen.Assemblies.DeformManager.DeleteReplacedFeature to delete the old deform feature 
                    8. Post-process by invoking NXOpen.Assemblies.DeformBuilder.PostUpdateDeform
                
         Returns unitConvertHasWarning (bool): .
        """
        pass
import NXOpen
import NXOpen.Features
class DeformManager(NXOpen.Object): 
    """ Represents the Deform Manager class """
    def CreateDeformBuilder(part: NXOpen.Part, deformComponent: Component) -> DeformBuilder:
        """
         Creates a Assemblies.DeformBuilder.
                    This builder holds data for deformation operations and utility functions to process the data 
                    specifically for deformation workflows.  
                    part: The part whhere the build is created, also where the new created deform feature will be created
                          or the updated deform feature belongs 
                    deformComponent: the component of the deform definition part.              
                
         Returns builder ( DeformBuilder NXOpen.A):  Assemblies.DeformBuilder  object .
        """
        pass
    def DeleteReplacedFeature(oldFlex: NXOpen.Features.Feature) -> None:
        """
         Replace flex feature 
        """
        pass
    def LoadOccurrenceData(part: NXOpen.Part) -> None:
        """
         Load part with occurrence data 
        """
        pass
    def PostProcessReplaceFlexFeature(oldReplacedFlexName: str) -> None:
        """
         Post Process Replace flex feature 
        """
        pass
    def PreProcessDefinitionPart(partOcc: Component, targetPart: NXOpen.Part, isReplaceMode: bool) -> NXOpen.Part:
        """
         Preprocessing the deform definition part 
         Returns reopenedPart ( NXOpen.Part): .
        """
        pass
    def SetReplaceDeformMode(isReplacingDeformation: bool) -> bool:
        """
         The replacing deformation of the deformation  
         Returns oldDeformationState (bool): .
        """
        pass
class DegreesOfFreedomResult(Enum):
    """
    Members Include: 
     |Unknown|  The calculation failed to produce a result, possibly because the component
                                                                                           is inconsistently constrained. 
     |Success|  The degrees of freedom calculation succeeded. 

    """
    Unknown: int
    Success: int
    @staticmethod
    def ValueOf(value: int) -> DegreesOfFreedomResult:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DegreesOfFreedomStatus(Enum):
    """
    Members Include: 
     |NotUsed|  The field is not used. 
     |Static|  The point or direction is well defined. 
     |Free|  The point or direction is under defined. 
     |Instantaneous|  The point or direction is instantaneous. 
     |StaticNormal|  The direction represents a normal to two translational degrees of freedom. The direction is well defined. 
     |FreeNormal|  The direction represents a normal to two translational degrees of freedom. The direction is under defined. 
     |InstantaneousNormal|  The direction represents a normal to two translational degrees of freedom. The direction is instantaneous. 

    """
    NotUsed: int
    Static: int
    Free: int
    Instantaneous: int
    StaticNormal: int
    FreeNormal: int
    InstantaneousNormal: int
    @staticmethod
    def ValueOf(value: int) -> DegreesOfFreedomStatus:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DegreesOfFreedom:
    """
     Structure used to report the Degrees of Freedom of a component.
            If there is one rational degrees of freedom then axis is determined by base_point1
            and rotation_direction1. 
            If there are 2 rotational degrees of freedom then one axis is determined by base_point1
            and rotation_direction1 and the other by base_point2 and rotation_direction2.
            If there are 3 rotational degrees of freedom then the fixed point for the rotations
            is in base_point1 and there is no axis direction given.
            The translational degrees of freedom are given in translation_direction1 and
            translation_direction2, with the possibility that one of these may be a "normal" 
            to 2 degrees of freedom, as specified in the associated status. 
    """
    @property
    def Result(self) -> DegreesOfFreedomResult:
        """
        Getter for property Result
        The success or otherwise of the degrees of freedom calculation

        """
        pass
    @Result.setter
    def Result(self, value: DegreesOfFreedomResult):
        """
        Getter for property Result
        The success or otherwise of the degrees of freedom calculation
        Setter for property Result
        The success or otherwise of the degrees of freedom calculation

        """
        pass
    @property
    def NumRotational(self) -> int:
        """
        Getter for property NumRotational
        Number of static and free rotational degrees of freedom.

        """
        pass
    @NumRotational.setter
    def NumRotational(self, value: int):
        """
        Getter for property NumRotational
        Number of static and free rotational degrees of freedom.
        Setter for property NumRotational
        Number of static and free rotational degrees of freedom.

        """
        pass
    @property
    def NumTranslational(self) -> int:
        """
        Getter for property NumTranslational
        Number of static and free translational degrees of freedom.

        """
        pass
    @NumTranslational.setter
    def NumTranslational(self, value: int):
        """
        Getter for property NumTranslational
        Number of static and free translational degrees of freedom.
        Setter for property NumTranslational
        Number of static and free translational degrees of freedom.

        """
        pass
    @property
    def NumInstantaneousRotational(self) -> int:
        """
        Getter for property NumInstantaneousRotational
        Number of instantaneous rotational degrees of freedom.

        """
        pass
    @NumInstantaneousRotational.setter
    def NumInstantaneousRotational(self, value: int):
        """
        Getter for property NumInstantaneousRotational
        Number of instantaneous rotational degrees of freedom.
        Setter for property NumInstantaneousRotational
        Number of instantaneous rotational degrees of freedom.

        """
        pass
    @property
    def NumInstantaneousTranslational(self) -> int:
        """
        Getter for property NumInstantaneousTranslational
        Number of instantaneous translational degrees of freedom.

        """
        pass
    @NumInstantaneousTranslational.setter
    def NumInstantaneousTranslational(self, value: int):
        """
        Getter for property NumInstantaneousTranslational
        Number of instantaneous translational degrees of freedom.
        Setter for property NumInstantaneousTranslational
        Number of instantaneous translational degrees of freedom.

        """
        pass
    @property
    def BasePoint1Status(self) -> DegreesOfFreedomStatus:
        """
        Getter for property BasePoint1Status
        First rotation base point status.

        """
        pass
    @BasePoint1Status.setter
    def BasePoint1Status(self, value: DegreesOfFreedomStatus):
        """
        Getter for property BasePoint1Status
        First rotation base point status.
        Setter for property BasePoint1Status
        First rotation base point status.

        """
        pass
    @property
    def BasePoint1(self) -> NXOpen.Point3d:
        """
        Getter for property BasePoint1
        First rotation base point.

        """
        pass
    @BasePoint1.setter
    def BasePoint1(self, value: NXOpen.Point3d):
        """
        Getter for property BasePoint1
        First rotation base point.
        Setter for property BasePoint1
        First rotation base point.

        """
        pass
    @property
    def RotationDirection1Status(self) -> DegreesOfFreedomStatus:
        """
        Getter for property RotationDirection1Status
        First rotation direction status.

        """
        pass
    @RotationDirection1Status.setter
    def RotationDirection1Status(self, value: DegreesOfFreedomStatus):
        """
        Getter for property RotationDirection1Status
        First rotation direction status.
        Setter for property RotationDirection1Status
        First rotation direction status.

        """
        pass
    @property
    def RotationDirection1(self) -> NXOpen.Vector3d:
        """
        Getter for property RotationDirection1
        First rotation direction.

        """
        pass
    @RotationDirection1.setter
    def RotationDirection1(self, value: NXOpen.Vector3d):
        """
        Getter for property RotationDirection1
        First rotation direction.
        Setter for property RotationDirection1
        First rotation direction.

        """
        pass
    @property
    def BasePoint2Status(self) -> DegreesOfFreedomStatus:
        """
        Getter for property BasePoint2Status
        Second rotation base point status.

        """
        pass
    @BasePoint2Status.setter
    def BasePoint2Status(self, value: DegreesOfFreedomStatus):
        """
        Getter for property BasePoint2Status
        Second rotation base point status.
        Setter for property BasePoint2Status
        Second rotation base point status.

        """
        pass
    @property
    def BasePoint2(self) -> NXOpen.Point3d:
        """
        Getter for property BasePoint2
        Second rotation base point.

        """
        pass
    @BasePoint2.setter
    def BasePoint2(self, value: NXOpen.Point3d):
        """
        Getter for property BasePoint2
        Second rotation base point.
        Setter for property BasePoint2
        Second rotation base point.

        """
        pass
    @property
    def RotationDirection2Status(self) -> DegreesOfFreedomStatus:
        """
        Getter for property RotationDirection2Status
        Second rotation direction status.

        """
        pass
    @RotationDirection2Status.setter
    def RotationDirection2Status(self, value: DegreesOfFreedomStatus):
        """
        Getter for property RotationDirection2Status
        Second rotation direction status.
        Setter for property RotationDirection2Status
        Second rotation direction status.

        """
        pass
    @property
    def RotationDirection2(self) -> NXOpen.Vector3d:
        """
        Getter for property RotationDirection2
        Second rotation direction.

        """
        pass
    @RotationDirection2.setter
    def RotationDirection2(self, value: NXOpen.Vector3d):
        """
        Getter for property RotationDirection2
        Second rotation direction.
        Setter for property RotationDirection2
        Second rotation direction.

        """
        pass
    @property
    def TranslationDirection1Status(self) -> DegreesOfFreedomStatus:
        """
        Getter for property TranslationDirection1Status
        First translation direction status.

        """
        pass
    @TranslationDirection1Status.setter
    def TranslationDirection1Status(self, value: DegreesOfFreedomStatus):
        """
        Getter for property TranslationDirection1Status
        First translation direction status.
        Setter for property TranslationDirection1Status
        First translation direction status.

        """
        pass
    @property
    def TranslationDirection1(self) -> NXOpen.Vector3d:
        """
        Getter for property TranslationDirection1
        First translation direction.

        """
        pass
    @TranslationDirection1.setter
    def TranslationDirection1(self, value: NXOpen.Vector3d):
        """
        Getter for property TranslationDirection1
        First translation direction.
        Setter for property TranslationDirection1
        First translation direction.

        """
        pass
    @property
    def TranslationDirection2Status(self) -> DegreesOfFreedomStatus:
        """
        Getter for property TranslationDirection2Status
        Second translation direction status.

        """
        pass
    @TranslationDirection2Status.setter
    def TranslationDirection2Status(self, value: DegreesOfFreedomStatus):
        """
        Getter for property TranslationDirection2Status
        Second translation direction status.
        Setter for property TranslationDirection2Status
        Second translation direction status.

        """
        pass
    @property
    def TranslationDirection2(self) -> NXOpen.Vector3d:
        """
        Getter for property TranslationDirection2
        Second translation direction.

        """
        pass
    @TranslationDirection2.setter
    def TranslationDirection2(self, value: NXOpen.Vector3d):
        """
        Getter for property TranslationDirection2
        Second translation direction.
        Setter for property TranslationDirection2
        Second translation direction.

        """
        pass
import NXOpen
class DeleteOverridePartBuilder(NXOpen.Builder): 
    """ Represents a builder class that deletes override part in the specified design elements.
    """
    @property
    def ComponentSelectionList(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) ComponentSelectionList
         Returns the list that contains components of reuse design element or subordinates
                    of which override part is to be deleted.  
          
                  
         
        """
        pass
import NXOpen
import NXOpen.PDM
class DesignElementBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs various design element operations. 
        The operation can be one of NXOpen.Assemblies.DesignElementBuilder.OperationType """
    class EditActionType(Enum):
        """
        Members Include: 
         |Category| 
         |Partitions| 
         |Effectivity| 

        """
        Category: int
        Partitions: int
        Effectivity: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.EditActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LayerOptionType(Enum):
        """
        Members Include: 
         |Original|  Original layer 
         |Work|  Work layer 
         |AsSpecified|  As specified layer 

        """
        Original: int
        Work: int
        AsSpecified: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.LayerOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OperationType(Enum):
        """
        Members Include: 
         |Create|  Creates a design element 
         |Edit|  Edits a design element 
         |SaveAs|  Save as a design element 
         |Save|  Saves a design element 
         |SaveAndClose|  Saves a design element and if it is a reuse closes the reused part 
         |Undefined| 

        """
        Create: int
        Edit: int
        SaveAs: int
        Save: int
        SaveAndClose: int
        Undefined: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.OperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositioningOption(Enum):
        """
        Members Include: 
         |AbsoluteOrigin|  Applies absolute origin position on the design elements
         |Maintain|  Maintains the existing positions of the design elements.
                                                                                      Applicable only if the edit action type is set to 
                                                                                      DesignElementBuilder.EditActionType.Category 
         |AsSpecified|  Applies the specified position on the design elements

        """
        AbsoluteOrigin: int
        Maintain: int
        AsSpecified: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.PositioningOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceSetType(Enum):
        """
        Members Include: 
         |Model|  Model 
         |EntirePart|  Entire part 
         |AsSpecified|  As specified reference set 

        """
        Model: int
        EntirePart: int
        AsSpecified: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.ReferenceSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveAsActionType(Enum):
        """
        Members Include: 
         |NewRevision| 
         |NewDesignElement| 

        """
        NewRevision: int
        NewDesignElement: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.SaveAsActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StateType(Enum):
        """
        Members Include: 
         |Shape|  Shape design element 
         |Reuse|  Reuse design element 
         |Promissory|  Promissory design element 

        """
        Shape: int
        Reuse: int
        Promissory: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementBuilder.StateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Count(self) -> int:
        """
        Getter for property: (int) Count
         Returns the number of design elements to be created.  
           Applicable only if the operation type is set to 
                     DesignElementBuilder::OperationTypeCreate   
         
        """
        pass
    @Count.setter
    def Count(self, count: int):
        """
        Setter for property: (int) Count
         Returns the number of design elements to be created.  
           Applicable only if the operation type is set to 
                     DesignElementBuilder::OperationTypeCreate   
         
        """
        pass
    @property
    def DesignElementType(self) -> str:
        """
        Getter for property: (str) DesignElementType
         Returns the type of a design element  
            
         
        """
        pass
    @DesignElementType.setter
    def DesignElementType(self, deType: str):
        """
        Setter for property: (str) DesignElementType
         Returns the type of a design element  
            
         
        """
        pass
    @property
    def DesignElementsToOperate(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) DesignElementsToOperate
         Returns the design elements to operate upon   
            
         
        """
        pass
    @property
    def EditAction(self) -> DesignElementBuilder.EditActionType:
        """
        Getter for property: ( DesignElementBuilder.EditActionType NXOpen.A) EditAction
         Returns the edit action type on a design element   
            
         
        """
        pass
    @EditAction.setter
    def EditAction(self, actionType: DesignElementBuilder.EditActionType):
        """
        Setter for property: ( DesignElementBuilder.EditActionType NXOpen.A) EditAction
         Returns the edit action type on a design element   
            
         
        """
        pass
    @property
    def EffectivityTable(self) -> NXOpen.PDM.EffectivityTableBuilder:
        """
        Getter for property: ( NXOpen.PDM.EffectivityTableBuilder) EffectivityTable
         Returns the effectivity interface of a design element   
            
         
        """
        pass
    @property
    def FileNewDescriptor(self) -> NXOpen.FileNew:
        """
        Getter for property: ( NXOpen.FileNew) FileNewDescriptor
         Returns the file new descriptor to identify a design element   
            
         
        """
        pass
    @property
    def KeepOriginalDesignElement(self) -> bool:
        """
        Getter for property: (bool) KeepOriginalDesignElement
         Returns the option determines whether to keep the original design element in the subset during save as
                  
            
         
        """
        pass
    @KeepOriginalDesignElement.setter
    def KeepOriginalDesignElement(self, valueType: bool):
        """
        Setter for property: (bool) KeepOriginalDesignElement
         Returns the option determines whether to keep the original design element in the subset during save as
                  
            
         
        """
        pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer value of a design element.  
           Applicable only if the layer option is set to 
                     DesignElementBuilder::LayerOptionTypeAsSpecified 
                  
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer value of a design element.  
           Applicable only if the layer option is set to 
                     DesignElementBuilder::LayerOptionTypeAsSpecified 
                  
         
        """
        pass
    @property
    def LayerOption(self) -> DesignElementBuilder.LayerOptionType:
        """
        Getter for property: ( DesignElementBuilder.LayerOptionType NXOpen.A) LayerOption
         Returns the layer option of a design element   
            
         
        """
        pass
    @LayerOption.setter
    def LayerOption(self, layerOption: DesignElementBuilder.LayerOptionType):
        """
        Setter for property: ( DesignElementBuilder.LayerOptionType NXOpen.A) LayerOption
         Returns the layer option of a design element   
            
         
        """
        pass
    @property
    def OwningSubsetInstance(self) -> Subset:
        """
        Getter for property: ( Subset NXOpen.A) OwningSubsetInstance
         Returns the owning subset instance  
            
         
        """
        pass
    @OwningSubsetInstance.setter
    def OwningSubsetInstance(self, subsetInstance: Subset):
        """
        Setter for property: ( Subset NXOpen.A) OwningSubsetInstance
         Returns the owning subset instance  
            
         
        """
        pass
    @property
    def PartToUse(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) PartToUse
         Returns the part to use of a reuse design element.  
           Applicable only if the state is set to 
                     DesignElementBuilder::StateTypeReuse 
                  
         
        """
        pass
    @PartToUse.setter
    def PartToUse(self, partToUse: NXOpen.BasePart):
        """
        Setter for property: ( NXOpen.BasePart) PartToUse
         Returns the part to use of a reuse design element.  
           Applicable only if the state is set to 
                     DesignElementBuilder::StateTypeReuse 
                  
         
        """
        pass
    @property
    def PositioningOptionValue(self) -> DesignElementBuilder.PositioningOption:
        """
        Getter for property: ( DesignElementBuilder.PositioningOption NXOpen.A) PositioningOptionValue
         Returns the positioning option of a design element  
            
         
        """
        pass
    @PositioningOptionValue.setter
    def PositioningOptionValue(self, positioningOption: DesignElementBuilder.PositioningOption):
        """
        Setter for property: ( DesignElementBuilder.PositioningOption NXOpen.A) PositioningOptionValue
         Returns the positioning option of a design element  
            
         
        """
        pass
    @property
    def ReferenceSet(self) -> DesignElementBuilder.ReferenceSetType:
        """
        Getter for property: ( DesignElementBuilder.ReferenceSetType NXOpen.A) ReferenceSet
         Returns the reference set of a design element   
            
         
        """
        pass
    @ReferenceSet.setter
    def ReferenceSet(self, referenceSet: DesignElementBuilder.ReferenceSetType):
        """
        Setter for property: ( DesignElementBuilder.ReferenceSetType NXOpen.A) ReferenceSet
         Returns the reference set of a design element   
            
         
        """
        pass
    @property
    def ReferenceSetName(self) -> str:
        """
        Getter for property: (str) ReferenceSetName
         Returns the reference set name of a design element.  
           Applicable only if the reference set is
                    set to  DesignElementBuilder::ReferenceSetTypeAsSpecified 
                   
         
        """
        pass
    @ReferenceSetName.setter
    def ReferenceSetName(self, referenceSetName: str):
        """
        Setter for property: (str) ReferenceSetName
         Returns the reference set name of a design element.  
           Applicable only if the reference set is
                    set to  DesignElementBuilder::ReferenceSetTypeAsSpecified 
                   
         
        """
        pass
    @property
    def SaveAsAction(self) -> DesignElementBuilder.SaveAsActionType:
        """
        Getter for property: ( DesignElementBuilder.SaveAsActionType NXOpen.A) SaveAsAction
         Returns the save as action type of a design element   
            
         
        """
        pass
    @SaveAsAction.setter
    def SaveAsAction(self, actionType: DesignElementBuilder.SaveAsActionType):
        """
        Setter for property: ( DesignElementBuilder.SaveAsActionType NXOpen.A) SaveAsAction
         Returns the save as action type of a design element   
            
         
        """
        pass
    @property
    def Scatter(self) -> bool:
        """
        Getter for property: (bool) Scatter
         Returns the option to determine whether to scatter design elements during creation  
            
         
        """
        pass
    @Scatter.setter
    def Scatter(self, scatterValue: bool):
        """
        Setter for property: (bool) Scatter
         Returns the option to determine whether to scatter design elements during creation  
            
         
        """
        pass
    @property
    def State(self) -> DesignElementBuilder.StateType:
        """
        Getter for property: ( DesignElementBuilder.StateType NXOpen.A) State
         Returns the state of a design element  
            
         
        """
        pass
    @State.setter
    def State(self, state: DesignElementBuilder.StateType):
        """
        Setter for property: ( DesignElementBuilder.StateType NXOpen.A) State
         Returns the state of a design element  
            
         
        """
        pass
    def AddToPartitions(self, partitions: List[Partition]) -> None:
        """
         Specify partitions to which the design elements will be added.  The design elements
                    will remain a member of any partitions to which they already belongs. The partitions
                    to which the design elements will be added accumulate if this method is called more
                    than once.  If both Assemblies.DesignElementBuilder.AddToPartitions
                    and Assemblies.DesignElementBuilder.RemoveFromPartitions are called
                    with the same partition then the design elements will be added or removed from that partition
                    depending upon which was the last method called.
                
        """
        pass
    def CreateLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Creates the pre-creation objects for the design elements 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetAddPartitions(self) -> List[Partition]:
        """
         Get the partitions to which the design elements will be added.
                
         Returns partitions ( Partition List[NXOpen): .
        """
        pass
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns design element operation failures 
         Returns operationFailures ( NXOpen.ErrorList): .
        """
        pass
    def GetPosition(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
         Gets the position of design element 
         Returns A tuple consisting of (position, orientation). 
         - position is:  NXOpen.Point3d.
         - orientation is:  NXOpen.Matrix3x3.

        """
        pass
    def GetRemovePartitions(self) -> List[Partition]:
        """
         Get the partitions from which the design elements will be removed.
                
         Returns partitions ( Partition List[NXOpen): .
        """
        pass
    def PartiallyCommit(self, logicalObjects: List[NXOpen.PDM.LogicalObject]) -> None:
        """
         Equivalent to builder Commit call but this one would create design elements with minimal required 
                information. Can be used only when this NXOpen.Assemblies.DesignElementBuilder has 
                been created with NXOpen.Assemblies.DesignElementBuilder.OperationType.Create. 
                Call to builder Commit is required after this to Commit creation.
                
        """
        pass
    def RemoveFromPartitions(self, partitions: List[Partition]) -> None:
        """
         Specify partitions from which the design elements will be removed. The partitions
                    from which the design elements will be removed accumulate if this method is called more
                    than once.  If both Assemblies.DesignElementBuilder.AddToPartitions
                    and Assemblies.DesignElementBuilder.RemoveFromPartitions are called
                    with the same partition then the design elements will be added or removed from that partition
                    depending upon which was the last method called.
                
        """
        pass
    def SetPosition(self, position: NXOpen.Point3d, orientation: NXOpen.Matrix3x3) -> None:
        """
         Sets the position of design element. This value is used only when positioning option is 
                    DesignElementBuilder.PositioningOption.AsSpecified
        """
        pass
import NXOpen
class DrawingExplosionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of drawing explosions """
    def FindObject(self, name: str) -> DrawingExplosion:
        """
         Finds the NXOpen.Assemblies.DrawingExplosion with the given identifier as recorded in a journal. 
                    This method should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier.
                
         Returns found ( DrawingExplosion NXOpen.A):  DrawingExplosion found, or null if no such DrawingExplosion exists.
        """
        pass
import NXOpen
class DrawingExplosion(NXOpen.NXObject): 
    """ Represents an explosion used in a drawing view of an arrangement.
    """
    @property
    def RootComponent(self) -> ExplodedComponent:
        """
        Getter for property: ( ExplodedComponent NXOpen.A) RootComponent
         Returns the root component of the drawing explosion.  
           The root component is the exploded component at the top of the exploded component
                    tree. The exploded component tree has the same structure as that of the component tree in  NXOpen::Assemblies::ComponentAssembly .
                  
         
        """
        pass
class ExplicitSearchTerm(SearchTerm): 
    """
        A NXOpen.Assemblies.SubsetRecipe search term that refers explicitly to
        a design element.
    """
    @property
    def SearchResultElement(self) -> SearchResultElement:
        """
        Getter for property: ( SearchResultElement NXOpen.A) SearchResultElement
         Returns the search result element of this search term.  
          
                  
         
        """
        pass
class ExplodedComponent(Component): 
    """ Represents a NXOpen.Assemblies.Component within an explosion.
    """
    def GetComponent(self) -> Component:
        """
         Gets the NXOpen.Assemblies.Component associated with the exploded component.
                
         Returns component ( Component NXOpen.A): .
        """
        pass
    def GetExplosion(self) -> Explosion:
        """
         Gets the NXOpen.Assemblies.Explosion associated with the exploded component.
                
         Returns explosion ( Explosion NXOpen.A): .
        """
        pass
import NXOpen
class ExplosionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of explosions """
    def Create(self, explosionName: str) -> Explosion:
        """
         Creates an explosion based upon the default arrangement in the given OCC part.
                
         Returns explosion ( Explosion NXOpen.A):  the new explosion .
        """
        pass
    def FindObject(self, name: str) -> Explosion:
        """
         Finds the NXOpen.Assemblies.Explosion with the given identifier as recorded in a journal. 
                    This method should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier.
                
         Returns found ( Explosion NXOpen.A):  Explosion found, or null if no such Explosion exists.
        """
        pass
import NXOpen
import NXOpen.Positioning
class Explosion(NXOpen.NXObject): 
    """ Represents an explosion. An explosion is a view containing parts or subassemblies
        that have been displaced from their real model positions.
    """
    class BlockingOptions:
        """
         Represents the Blocking Graph option 
         ExplosionBlockingOptions_Struct NXOpen.A is an alias for  Explosion.BlockingOptions NXOpen.A.
        """
        @property
        def SearchAdditionalDirections(self) -> bool:
            """
            Getter for property SearchAdditionalDirections
            Search additional blocking direction using component's local csys

            """
            pass
        @SearchAdditionalDirections.setter
        def SearchAdditionalDirections(self, value: bool):
            """
            Getter for property SearchAdditionalDirections
            Search additional blocking direction using component's local csys
            Setter for property SearchAdditionalDirections
            Search additional blocking direction using component's local csys

            """
            pass
        @property
        def CheckSmallInterferences(self) -> bool:
            """
            Getter for property CheckSmallInterferences
            Check for small interferences

            """
            pass
        @CheckSmallInterferences.setter
        def CheckSmallInterferences(self, value: bool):
            """
            Getter for property CheckSmallInterferences
            Check for small interferences
            Setter for property CheckSmallInterferences
            Check for small interferences

            """
            pass
    class ExplosionOptions:
        """
         Represents the Explosion Graph option 
         ExplosionExplosionOptions_Struct NXOpen.A is an alias for  Explosion.ExplosionOptions NXOpen.A.
        """
        @property
        def ForceInterferingComponentsApart(self) -> bool:
            """
            Getter for property ForceInterferingComponentsApart
            Forcibly move interfering components apart with best guess

            """
            pass
        @ForceInterferingComponentsApart.setter
        def ForceInterferingComponentsApart(self, value: bool):
            """
            Getter for property ForceInterferingComponentsApart
            Forcibly move interfering components apart with best guess
            Setter for property ForceInterferingComponentsApart
            Forcibly move interfering components apart with best guess

            """
            pass
        @property
        def PreferConstraintsForDirection(self) -> bool:
            """
            Getter for property PreferConstraintsForDirection
            Prefer using constraints to pick explosion direction

            """
            pass
        @PreferConstraintsForDirection.setter
        def PreferConstraintsForDirection(self, value: bool):
            """
            Getter for property PreferConstraintsForDirection
            Prefer using constraints to pick explosion direction
            Setter for property PreferConstraintsForDirection
            Prefer using constraints to pick explosion direction

            """
            pass
        @property
        def IgnoreConstraints(self) -> bool:
            """
            Getter for property IgnoreConstraints
            Ignore constraints in all computations

            """
            pass
        @IgnoreConstraints.setter
        def IgnoreConstraints(self, value: bool):
            """
            Getter for property IgnoreConstraints
            Ignore constraints in all computations
            Setter for property IgnoreConstraints
            Ignore constraints in all computations

            """
            pass
    @property
    def RootComponent(self) -> ExplodedComponent:
        """
        Getter for property: ( ExplodedComponent NXOpen.A) RootComponent
         Returns the root component of the explosion.  
           The root component is the exploded component at the top of the exploded component
                    tree. The exploded component tree has the same structure as that of the component tree in  NXOpen::Assemblies::ComponentAssembly .
                  
         
        """
        pass
    def AutoExplodeAllComponents(self, useAdditionalDirections: bool) -> int:
        """
         Attempts to auto explode all leaf components of assembly which is not hidden or suppressed in NXOpen.Assemblies.Explosion 
                    with or without using additional directions from components local CSYS and constraints.
                    Sub-assembly components will not be auto-exploded. 
                    Note: Using additional direction will increase auto-explosion computation time. 
                
         Returns numberOfComponentsExploded (int): .
        """
        pass
    def AutoExplodeAssembly(self, autoExplodeDistance: float) -> int:
        """
         Attempts to auto explode all NXOpen.Assemblies.ExplodedComponent to given distance in NXOpen.Assemblies.Explosion.
                
         Returns noOfCompExploded (int): .
        """
        pass
    def AutoExplodeComponents(self, selectedComponents: List[ExplodedComponent], autoExplodeDistance: float) -> int:
        """
         Attempts to auto explode the given array of NXOpen.Assemblies.ExplodedComponent  to given distance in NXOpen.Assemblies.Explosion.
                
         Returns noOfCompExploded (int): .
        """
        pass
    def AutoExplodeSelectedComponents(self, useAdditionalDirections: bool, selectedComponents: List[ExplodedComponent]) -> int:
        """
         Attempts to auto explode the given array of NXOpen.Assemblies.ExplodedComponent  in NXOpen.Assemblies.Explosion 
                    with or without using additional directions from components local CSYS and constraints.
                    Using additional direction will increase auto-explosion computation time. 
                
         Returns numberOfComponentsExploded (int): .
        """
        pass
    def Copy(self, destinationExplosion: Explosion) -> None:
        """
         Copies the component transformations in the source explosion onto the destination explosion.
                
        """
        pass
    def Delete(self) -> None:
        """
         Deletes the given NXOpen.Assemblies.Explosion.
                
        """
        pass
    def DeleteExplosions(self, explosions: List[Explosion]) -> int:
        """
         Attempts to delete the given array of NXOpen.Assemblies.Explosions.
                    An explosion cannot be deleted if it is being used in a model view which is not visible in active layout.
                
         Returns nDeletedExplosions (int): .
        """
        pass
    def GetPositioner(self) -> NXOpen.Positioning.ComponentPositioner:
        """
         Establish the Component Positioner for NXOpen.Assemblies.Explosion.
                     The positioner manages the component constraints.
                
         Returns positioner ( NXOpen.Positioning.ComponentPositioner): .
        """
        pass
    def Hide(self, view: NXOpen.View) -> None:
        """
         Changes the view so that it no longer shows an exploded view.
                
        """
        pass
    def MoveComponentsToOriginalPosition(self, selectedComponents: List[ExplodedComponent]) -> None:
        """
         Repositions given array of NXOpen.Assemblies.ExplodedComponent leaf component to their original unexploded position on parent assemblies
                
        """
        pass
    def Rename(self, occPart: ComponentAssembly, explosionName: str) -> None:
        """
         Renames the given NXOpen.Assemblies.Explosion.
                
        """
        pass
    def Show(self, view: NXOpen.View) -> None:
        """
         Changes the view so that it shows the explosion.
                
        """
        pass
    def UnexplodeAllComponents(self) -> None:
        """
         Unexplode all the NXOpen.Assemblies.ExplodedComponent of currently active assembly in NXOpen.Assemblies.Explosion.
                
        """
        pass
    def UnexplodeComponents(self, selectedComponents: List[ExplodedComponent]) -> None:
        """
         Unexplode the given array of NXOpen.Assemblies.ExplodedComponent in NXOpen.Assemblies.Explosion.
                
        """
        pass
import NXOpen
class FindInCollaborativeDesign(NXOpen.NXObject): 
    """
        FindInCollaborativeDesign is a searcher for performing simple searches in the context of a subset.
    """
    class ObjectType(Enum):
        """
        Members Include: 
         |Partition|  Search for partitions 
         |DesignElement|  Search for Design Elements 
         |RunElement|  Search for Run Elements 

        """
        Partition: int
        DesignElement: int
        RunElement: int
        @staticmethod
        def ValueOf(value: int) -> FindInCollaborativeDesign.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SearchType(Enum):
        """
        Members Include: 
         |ItemQuery|  Match text with item name or id 

        """
        ItemQuery: int
        @staticmethod
        def ValueOf(value: int) -> FindInCollaborativeDesign.SearchType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetPartitions(self) -> List[Partition]:
        """
         Retrieve the NXOpen.Assemblies.Partitions found in the last search.
                
         Returns partitions ( Partition List[NXOpen): .
        """
        pass
    def GetSearchResultElements(self) -> List[SearchResultElement]:
        """
         Retrieve the NXOpen.Assemblies.SearchResultElements found in the last search.
                
         Returns searchResultElements ( SearchResultElement List[NXOpen): .
        """
        pass
    @overload
    def PerformFind(self, objectType: FindInCollaborativeDesign.ObjectType, searchType: FindInCollaborativeDesign.SearchType, searchText: str) -> None:
        """
         Generate the search results according to the search text.
                
        """
        pass
    @overload
    def PerformFind(self, partition: Partition, objectType: FindInCollaborativeDesign.ObjectType, searchType: FindInCollaborativeDesign.SearchType, searchText: str) -> None:
        """
         Generate the search results according to the search text, searching only
                    within the partition.
                
        """
        pass
    @overload
    def PerformFind(self, objectType: FindInCollaborativeDesign.ObjectType, searchType: FindInCollaborativeDesign.SearchType, criteriaTitles: List[str], criteriaValues: List[str]) -> None:
        """
         Generate the search results according to the search criteria of advance search.
                    Advanced search takes in detailed inputs to perform the search. The parameters "criteriaTitles" 
                    and "criteriaValues" are the internal property names and their values to be searched. 
                    The attributevalue pairs are combined logically using AND so that only objects matching 
                    ALL of the specified criteria are returned. The method can only be used to search for matches 
                    on Teamcenter properties that are string valued. It does not work for properties which are ObjectLOV valued.
                    To see how to spell the "real" attribute names rather than the displayed attribute (column) names,
                    use Edit- Options...- General- UI- Sys Admin- Real Property Name in the Rich Client.
                
        """
        pass
class GroupSearchTerm(SearchTerm): 
    """
        A group of NXOpen.Assemblies.SearchTerms within a NXOpen.Assemblies.SubsetRecipe.
    """
    pass
import NXOpen
import NXOpen.Drawings
class HideComponentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.HideComponentBuilder """
    @property
    def Components(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Components
         Returns the components to hide   
            
         
        """
        pass
    @property
    def Views(self) -> NXOpen.Drawings.SelectDraftingViewList:
        """
        Getter for property: ( NXOpen.Drawings.SelectDraftingViewList) Views
         Returns the drafting views from which components to hide   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class IsPartitionableResult(NXOpen.TransientObject): 
    """ 
    Represents the class that contains IsPartitionable information for given Partition and Collection of components
    """
    class MemberInfo:
        """
         Structure of IsPartitionable results for each component member to be added in Partition. 
         IsPartitionableResultMemberInfo_Struct NXOpen.A is an alias for  IsPartitionableResult.MemberInfo NXOpen.A.
        """
        @property
        def Component(self) -> NXOpen.Annotations.NXOpen.Assemblies.Component:
            """
            Getter for property Component
            Component checked for IsPartitionable against Partition in IsPartitionableResult

            """
            pass
        @Component.setter
        def Component(self, value: NXOpen.Annotations.NXOpen.Assemblies.Component):
            """
            Getter for property Component
            Component checked for IsPartitionable against Partition in IsPartitionableResult
            Setter for property Component
            Component checked for IsPartitionable against Partition in IsPartitionableResult

            """
            pass
        @property
        def IsPartitionable(self) -> bool:
            """
            Getter for property IsPartitionable
            False = the given component can not be added to Partition.

            """
            pass
        @IsPartitionable.setter
        def IsPartitionable(self, value: bool):
            """
            Getter for property IsPartitionable
            False = the given component can not be added to Partition.
            Setter for property IsPartitionable
            False = the given component can not be added to Partition.

            """
            pass
        @property
        def Reason(self) -> str:
            """
            Getter for property Reason
            Reason why member cannot be added.

            """
            pass
        @Reason.setter
        def Reason(self, value: str):
            """
            Getter for property Reason
            Reason why member cannot be added.
            Setter for property Reason
            Reason why member cannot be added.

            """
            pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method is called, it is illegal to use the object. In .NET, this method is automatically called when the object is deleted by the garbage collector. 
        """
        pass
    def GetMemberInfo(self) -> List[IsPartitionableResult.MemberInfo]:
        """
         Returns the array of MemberInfo for each Component checked against partition for IsPartitionable. 
         Returns members ( IsPartitionableResult.MemberInfo List[NXOpen):  Returns NXOpen.Assemblies.IsPartitionableResult.MemberInfo collection. .
        """
        pass
    def GetPartition(self) -> Partition:
        """
         Returns the Partition for whose IsPartitionable Result are returned. 
         Returns partition ( Partition NXOpen.A): .
        """
        pass
import NXOpen
class LoadInterpartDataBuilder(NXOpen.Builder): 
    """ Represents a builderNXOpen.Assemblies.LoadInterpartDataBuilder """
    class OpenUnloadedParentsType(Enum):
        """
        Members Include: 
         |NotSet| Load all partially loaded parts 
                                                                                                  that contain links and all immediate 
                                                                                                  level parents parts if they are
                                                                                                  partially loaded
         |ImmediateLevel| Load all partially loaded parts 
                                                                                                  that contain links and all immediate 
                                                                                                  level parents parts regardless 
                                                                                                  of load status
         |AllLevels| Load all partially loaded parts 
                                                                                                  that contain links and all level 
                                                                                                  parent parts regardless of load status

        """
        NotSet: int
        ImmediateLevel: int
        AllLevels: int
        @staticmethod
        def ValueOf(value: int) -> LoadInterpartDataBuilder.OpenUnloadedParentsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionScopeType(Enum):
        """
        Members Include: 
         |AllPartsInDisplayedAssembly|  Load interpart data 
                                                                                                             for all parts in 
                                                                                                             displayed assembly 
         |AllPartsInSession|  Load interpart data 
                                                                                                             for all parts in session 

        """
        AllPartsInDisplayedAssembly: int
        AllPartsInSession: int
        @staticmethod
        def ValueOf(value: int) -> LoadInterpartDataBuilder.SelectionScopeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OpenUnloadedParents(self) -> LoadInterpartDataBuilder.OpenUnloadedParentsType:
        """
        Getter for property: ( LoadInterpartDataBuilder.OpenUnloadedParentsType NXOpen.A) OpenUnloadedParents
         Returns the open unloaded parents level type   
            
         
        """
        pass
    @OpenUnloadedParents.setter
    def OpenUnloadedParents(self, openUnloadedParents: LoadInterpartDataBuilder.OpenUnloadedParentsType):
        """
        Setter for property: ( LoadInterpartDataBuilder.OpenUnloadedParentsType NXOpen.A) OpenUnloadedParents
         Returns the open unloaded parents level type   
            
         
        """
        pass
    @property
    def SelectionScope(self) -> LoadInterpartDataBuilder.SelectionScopeType:
        """
        Getter for property: ( LoadInterpartDataBuilder.SelectionScopeType NXOpen.A) SelectionScope
         Returns the selection scope type  
            
         
        """
        pass
    @SelectionScope.setter
    def SelectionScope(self, selectionScope: LoadInterpartDataBuilder.SelectionScopeType):
        """
        Setter for property: ( LoadInterpartDataBuilder.SelectionScopeType NXOpen.A) SelectionScope
         Returns the selection scope type  
            
         
        """
        pass
    def GetFailedParts(self) -> List[NXOpen.BasePart]:
        """
        Returns an array of the parts that failed to load and update 
         Returns part ( NXOpen.BasePart Li):  Array of the part tags failed to 
                                                                                            load and update.
        """
        pass
    def GetLoadInterpartDataStatus(self, part: NXOpen.BasePart) -> Tuple[NXOpen.PartLoadStatus, NXOpen.PartDelayedUpdateStatus]:
        """
        Returns part load status and delayed update status for the part which failed to load and update
         Returns A tuple consisting of (load_status, delayed_update_status). 
         - load_status is:  NXOpen.PartLoadStatus. Part load status for the failed part.
         - delayed_update_status is:  NXOpen.PartDelayedUpdateStatus. Delayed update status data status for the failed part.

        """
        pass
import NXOpen
class MakeUniquePartBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.MakeUniquePartBuilder builder. Input to this class can be PSM facet objects.
     """
    class Option(Enum):
        """
        Members Include: 
         |CopyAssemblyOnly| 

        """
        CopyAssemblyOnly: int
        @staticmethod
        def ValueOf(value: int) -> MakeUniquePartBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CopyChoices(self) -> MakeUniquePartBuilder.Option:
        """
        Getter for property: ( MakeUniquePartBuilder.Option NXOpen.A) CopyChoices
         Returns the copy choices returned.  
             
         
        """
        pass
    @CopyChoices.setter
    def CopyChoices(self, copyChoices: MakeUniquePartBuilder.Option):
        """
        Setter for property: ( MakeUniquePartBuilder.Option NXOpen.A) CopyChoices
         Returns the copy choices returned.  
             
         
        """
        pass
    @property
    def SelectedComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectedComponents
         Returns the selected components to be made unique are returned.  
              
         
        """
        pass
import NXOpen
import NXOpen.PDM
class MechanicalRoutingSubsetBuilder(NXOpen.Builder): 
    """ A MechanicalRoutingSubsetBuilder is used to createedit Subsets NXOpen.Assemblies.Subset 
        that are used to define the context needed to perform a Mechanical Routing Design activity. The builder may 
        generate multiple subsets. The content of these subsets can be classified into "Work" content - the elements
        of the Routing design that the user would like to focus on and "Surrounding Data" content - the 3D content that
        surrounds the Routing design. The subset definition process utilizes the concept of a Run ja class TBD by NX P and ID
        while defining the recipe terms needed for the subsets. """
    class SurroundingDataRecipeMethod(Enum):
        """
        Members Include: 
         |NotSet| 
         |ProximitytoRoutingContent| 
         |Manual| 

        """
        NotSet: int
        ProximitytoRoutingContent: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> MechanicalRoutingSubsetBuilder.SurroundingDataRecipeMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Fixtures(self) -> bool:
        """
        Getter for property: (bool) Fixtures
         Returns an option for inclusion of fixtures DE's in the Routing Work.  
            
         
        """
        pass
    @Fixtures.setter
    def Fixtures(self, includeFixtures: bool):
        """
        Setter for property: (bool) Fixtures
         Returns an option for inclusion of fixtures DE's in the Routing Work.  
            
         
        """
        pass
    @property
    def Insulation(self) -> bool:
        """
        Getter for property: (bool) Insulation
         Returns an option for inclusion of insulation DE's in the Routing Work Subset.  
            
         
        """
        pass
    @Insulation.setter
    def Insulation(self, includeInsulation: bool):
        """
        Setter for property: (bool) Insulation
         Returns an option for inclusion of insulation DE's in the Routing Work Subset.  
            
         
        """
        pass
    @property
    def SurroundingDataProximityDistance(self) -> float:
        """
        Getter for property: (float) SurroundingDataProximityDistance
         Returns a proximity to Routing Content method has been selected to determine the surrounding content then 
                    this is the distance value used to perform the evaluation.  
           The units are in meters  
         
        """
        pass
    @SurroundingDataProximityDistance.setter
    def SurroundingDataProximityDistance(self, surroundingDataProximityDistance: float):
        """
        Setter for property: (float) SurroundingDataProximityDistance
         Returns a proximity to Routing Content method has been selected to determine the surrounding content then 
                    this is the distance value used to perform the evaluation.  
           The units are in meters  
         
        """
        pass
    @property
    def SurroundingDataRecipeMethodType(self) -> MechanicalRoutingSubsetBuilder.SurroundingDataRecipeMethod:
        """
        Getter for property: ( MechanicalRoutingSubsetBuilder.SurroundingDataRecipeMethod NXOpen.A) SurroundingDataRecipeMethodType
         Returns the routing recipes  Assemblies::MechanicalRoutingSubsetBuilder   
            
         
        """
        pass
    @SurroundingDataRecipeMethodType.setter
    def SurroundingDataRecipeMethodType(self, surroundingDataRecipeMethod: MechanicalRoutingSubsetBuilder.SurroundingDataRecipeMethod):
        """
        Setter for property: ( MechanicalRoutingSubsetBuilder.SurroundingDataRecipeMethod NXOpen.A) SurroundingDataRecipeMethodType
         Returns the routing recipes  Assemblies::MechanicalRoutingSubsetBuilder   
            
         
        """
        pass
    def AppendSearchResultElementToSelectedList(self, runID: str) -> None:
        """
         Appends the Search Result Element corresponding to the given Run ID to the SelectedSearchResultElement list on NXOpen.Assemblies.MechanicalRoutingSubsetBuilder.
        """
        pass
    def GetConfigurationContextBuilder(self) -> NXOpen.PDM.ConfigurationContextBuilder:
        """
         Returns the configuration context builder which will be used by user to set revision rule or effectivity and then user
                    needs to use NXOpen.Assemblies.FindInCollaborativeDesign to search for runs 
                    using object type RunElement. This is the builder which will be returned whenever you are creating new subsets.
                    This will be NULL in edit mode scenario. 
         Returns configurationContext ( NXOpen.PDM.ConfigurationContextBuilder): .
        """
        pass
    def GetSearchSubsetBuilder(self) -> SubsetBuilder:
        """
         The subset builder which is used for searching runs, the user will have to use
                     NXOpen.Assemblies.FindInCollaborativeDesign to search for runs 
                     using object type RunElement.
         Returns subsetBuilder ( SubsetBuilder NXOpen.A): .
        """
        pass
    def RemoveAllSearchResultElementsFromSelectedList(self) -> None:
        """
         Removes all the Search Result Element from the SelectedSearchResultElement list on NXOpen.Assemblies.MechanicalRoutingSubsetBuilder.
        """
        pass
    def RemoveSearchResultElementFromSelectedList(self, runID: str) -> None:
        """
         Removes the Search Result Element corresponding to the given Run ID from the SelectedSearchResultElement list on NXOpen.Assemblies.MechanicalRoutingSubsetBuilder.
        """
        pass
    def SetRoutingSubsetAsWorkPart(self) -> None:
        """
         The builder may generate multiple subsets.
                    This API will set the Routing Design Subset as the work part. 
        """
        pass
    def SetSearchSubsetBuilder(self, subsetBuilder: SubsetBuilder) -> None:
        """
         Sets the subset builder which needs to be set by user to search runs, the user will have to use
                    NXOpen.Assemblies.FindInCollaborativeDesign to search for runs 
                    using object type RunElement.
        """
        pass
    def UpdateSubsetUsingConfigurationContext(self, inputSubsetBuilder: SubsetBuilder) -> SubsetBuilder:
        """
         The routing subsets will be updated (e.g. revision rule, effectivity) using the information available on the 
                ConfigurationContext if the input is NULL. In case of valid input the corresponding subset will be updated with
                the information available on the ConfigurationContext. 
         Returns outputSubsetBuilder ( SubsetBuilder NXOpen.A): .
        """
        pass
import NXOpen
class OpenByProximityBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.OpenByProximityBuilder """
    class ProximityEvalLevel(Enum):
        """
        Members Include: 
         |BoundingBox| 
         |TrueShape| 

        """
        BoundingBox: int
        TrueShape: int
        @staticmethod
        def ValueOf(value: int) -> OpenByProximityBuilder.ProximityEvalLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetValidity(Enum):
        """
        Members Include: 
         |Valid| 
         |LacksBBox| 
         |CannotMapToTC| 
         |ReferenceOnly| 
         |NativePartInManagedMode| 

        """
        Valid: int
        LacksBBox: int
        CannotMapToTC: int
        ReferenceOnly: int
        NativePartInManagedMode: int
        @staticmethod
        def ValueOf(value: int) -> OpenByProximityBuilder.TargetValidity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |ProximityInformationFromPartFile| 
         |ProximityInformationFromTeamcenter| 

        """
        ProximityInformationFromPartFile: int
        ProximityInformationFromTeamcenter: int
        @staticmethod
        def ValueOf(value: int) -> OpenByProximityBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def PreviewProximityResults(self) -> bool:
        """
        Getter for property: (bool) PreviewProximityResults
         Returns the preview proximity results   
            
         
        """
        pass
    @PreviewProximityResults.setter
    def PreviewProximityResults(self, previewProximityResults: bool):
        """
        Setter for property: (bool) PreviewProximityResults
         Returns the preview proximity results   
            
         
        """
        pass
    @property
    def ProximityEvalType(self) -> OpenByProximityBuilder.ProximityEvalLevel:
        """
        Getter for property: ( OpenByProximityBuilder.ProximityEvalLevel NXOpen.A) ProximityEvalType
         Returns the proximity eval type   
            
         
        """
        pass
    @ProximityEvalType.setter
    def ProximityEvalType(self, proximityEvalType: OpenByProximityBuilder.ProximityEvalLevel):
        """
        Setter for property: ( OpenByProximityBuilder.ProximityEvalLevel NXOpen.A) ProximityEvalType
         Returns the proximity eval type   
            
         
        """
        pass
    @property
    def ProximityExclusionSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProximityExclusionSize
         Returns the proximity exclusion size   
            
         
        """
        pass
    @property
    def ProximityRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProximityRange
         Returns the proximity range from specified targets   
            
         
        """
        pass
    @property
    def ProximityTargets(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) ProximityTargets
         Returns the proximity target selection   
            
         
        """
        pass
    @property
    def Type(self) -> OpenByProximityBuilder.Types:
        """
        Getter for property: ( OpenByProximityBuilder.Types NXOpen.A) Type
         Returns the type of proximity evaluation to be performed   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: OpenByProximityBuilder.Types):
        """
        Setter for property: ( OpenByProximityBuilder.Types NXOpen.A) Type
         Returns the type of proximity evaluation to be performed   
            
         
        """
        pass
    def EvaluateProximity(self) -> None:
        """
         Evaluate the currently defined proximity operation 
        """
        pass
import NXOpen
class OrderCollection(NXOpen.TaggedObjectCollection): 
    """ a collection of  NXOpen.Assemblies.Orders """
    def FindObject(self, journalIdentifier: str) -> Order:
        """
         Finds the NXOpen.Assemblies.Order with the given identifier as recorded in a journal. 
            This method should not be used in handwritten code and exists to support record and playback of journals.
            An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( Order NXOpen.A):  Order found, or null if no such Order exists.
        """
        pass
import NXOpen
class Order(NXOpen.NXObject): 
    """ Represents base class for all Order classes. It is an abstract class and
        cannot be instantiated on its own. All Order classes should inherit from this class."""
    class State(Enum):
        """
        Members Include: 
         |UnSaved|  Order is unsaved 
         |Saved|  Order is saved 

        """
        UnSaved: int
        Saved: int
        @staticmethod
        def ValueOf(value: int) -> Order.State:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |UserDefinedComponent|  User defined component order
         |SequentialComponent|  System defined sequential component order 
         |ChronologicalComponent|  System defined chronological component order 
         |AlphanumericComponent|  System defined alphanumeric component order 
         |AlphabeticComponent|  System defined alphabetic component order 

        """
        UserDefinedComponent: int
        SequentialComponent: int
        ChronologicalComponent: int
        AlphanumericComponent: int
        AlphabeticComponent: int
        @staticmethod
        def ValueOf(value: int) -> Order.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OrderState(self) -> Order.State:
        """
        Getter for property: ( Order.State NXOpen.A) OrderState
         Returns the state of  NXOpen::Assemblies::Order .  
           An order can be in one of the 
                     NXOpen::Assemblies::Order::State .
                  
         
        """
        pass
    @property
    def OrderType(self) -> Order.Type:
        """
        Getter for property: ( Order.Type NXOpen.A) OrderType
         Returns the type of  NXOpen::Assemblies::Order .  
           An order can be of
                     NXOpen::Assemblies::Order::Type  
                  
         
        """
        pass
    def Activate(self) -> None:
        """
         Applies this order
        """
        pass
    def CanUseSubAssemblyOrder(self) -> bool:
        """
         Returns true if this order has 'UseSubAssembly' state set in owning NXOpen.Assemblies.ComponentAssembly
         Returns useSubAssemblyOrder (bool):  True if the sub-assembly order can be used to determine order of children.
        """
        pass
    def Delete(self) -> None:
        """
         Deletes an order 
        """
        pass
    def GetChildrenOrder(self, parent: Component) -> List[Component]:
        """
         Returns immediate children of input NXOpen.Assemblies.Component
                as they are ordered in this NXOpen.Assemblies.ComponentOrder 
         Returns children ( Component List[NXOpen):  Returns children in order .
        """
        pass
    def GetReversed(self) -> bool:
        """
         Gets the reverse state of the NXOpen.Assemblies.Order
         Returns isReversed (bool):  True if order is reversed else False .
        """
        pass
    def IsActive(self) -> bool:
        """
         Returns true if this order is the active order in owning NXOpen.Assemblies.ComponentAssembly
         Returns isActiveOrder (bool):  True if the current order is active.
        """
        pass
    def Save(self) -> None:
        """
         Saves an order
        """
        pass
    def SaveAs(self, newName: str) -> Order:
        """
         Creates a copy of the order, and gives the copy a new name.
                Each NXOpen.Assemblies.ComponentAssembly contains a set of system defined orders,
                which could be queried using NXOpen.Assemblies.ComponentAssembly.GetComponentOrders method.
                A new NXOpen.Assemblies.Order.Type.UserDefinedComponent order can only be created using this method.
                
         Returns newOrder ( Order NXOpen.A):  The new Order .
        """
        pass
    def SetReversed(self, isReversed: bool) -> None:
        """
         Sets the reverse state of the NXOpen.Assemblies.Order
        """
        pass
    def SetUseSubAssemblyOrder(self, useSubAssemblyOrder: bool) -> None:
        """
         Sets the UseSubAssembly' state of the NXOpen.Assemblies.Order
        """
        pass
import NXOpen
class PartitionList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[Partition]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: Partition) -> None:
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
    def Erase(self, obj: Partition) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: Partition, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: Partition) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> Partition:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( Partition NXOpen.A):  object found at input index .
        """
        pass
    def GetContents(self) -> List[Partition]:
        """
         Gets the contents of the entire list 
         Returns objects ( Partition List[NXOpen):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: Partition) -> None:
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
    def SetContents(self, objects: List[Partition]) -> None:
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
    def Swap(self, object1: Partition, object2: Partition) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PartitionSchemeInstance(NXOpen.NXObject): 
    """ Represents the partition scheme instance class. Partition scheme instance is associated with a product on which 
        partition scheme can be set.
    """
    @property
    def IncludeImplicitMembers(self) -> bool:
        """
        Getter for property: (bool) IncludeImplicitMembers
         Returns the include implicit members property.  
          
                    If it is set to false, then the assembly navigator displays only the explicit members of a partition.
                    If it is set to true, then the assembly navigator displays the explicit as well as implicit members of a partition.
                    Implicit members are the children of explicit members of a partition in the assembly structure.
                  
         
        """
        pass
    @IncludeImplicitMembers.setter
    def IncludeImplicitMembers(self, includeImplicit: bool):
        """
        Setter for property: (bool) IncludeImplicitMembers
         Returns the include implicit members property.  
          
                    If it is set to false, then the assembly navigator displays only the explicit members of a partition.
                    If it is set to true, then the assembly navigator displays the explicit as well as implicit members of a partition.
                    Implicit members are the children of explicit members of a partition in the assembly structure.
                  
         
        """
        pass
    @property
    def PartitionViewStyle(self) -> Subset.PartitionViewStyleType:
        """
        Getter for property: ( Subset.PartitionViewStyleType NXOpen.A) PartitionViewStyle
         Returns 
                    the partition view style to show.  
          
                  
         
        """
        pass
    @PartitionViewStyle.setter
    def PartitionViewStyle(self, partitionViewStyle: Subset.PartitionViewStyleType):
        """
        Setter for property: ( Subset.PartitionViewStyleType NXOpen.A) PartitionViewStyle
         Returns 
                    the partition view style to show.  
          
                  
         
        """
        pass
    @property
    def ViewedPartitionScheme(self) -> PartitionScheme:
        """
        Getter for property: ( PartitionScheme NXOpen.A) ViewedPartitionScheme
         Returns the viewed  NXOpen::Assemblies::PartitionScheme  on this partition scheme instance.  
          
                  
         
        """
        pass
    @ViewedPartitionScheme.setter
    def ViewedPartitionScheme(self, partitionScheme: PartitionScheme):
        """
        Setter for property: ( PartitionScheme NXOpen.A) ViewedPartitionScheme
         Returns the viewed  NXOpen::Assemblies::PartitionScheme  on this partition scheme instance.  
          
                  
         
        """
        pass
import NXOpen
class PartitionSchemeManager(NXOpen.NXObject): 
    """
        A partition scheme manager is associated to the part and allows to obtain information about partition schemes.
    """
    def FindPartition(self, partitionName: str, partitionType: str) -> Partition:
        """
         
                    Get the partition  by name and partition type.
                
         Returns partitions ( Partition NXOpen.A): .
        """
        pass
    def FindPartitionScheme(self, schemeName: str, schemeType: str) -> PartitionScheme:
        """
         
                    Get the partition scheme by name.
                
         Returns partitionScheme ( PartitionScheme NXOpen.A): .
        """
        pass
    def GetAllPartitionSchemes(self) -> List[PartitionScheme]:
        """
         
                    Get all partition schemes.
                
         Returns partitionSchemes ( PartitionScheme List[NXOpen): .
        """
        pass
import NXOpen
class PartitionScheme(NXOpen.NXObject): 
    """
        A partition scheme is a Teamcenter object in a Collaborative Design.  A partition scheme 
        contains partitions.
    """
    @property
    def CollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: ( NXOpen.CollaborativeDesign) CollaborativeDesign
         Returns
                    the owning collaborative design.  
          
                  
         
        """
        pass
    def GetRootPartitions(self) -> List[Partition]:
        """
                    Get the root partitions of partition scheme. 
                
         Returns rootPartitions ( Partition List[NXOpen): .
        """
        pass
class PartitionSearchTerm(SearchTerm): 
    """
        A Assemblies.SubsetRecipe search term that refers to a partition.
    """
    class IncludeChildren(Enum):
        """
        Members Include: 
         |FalseValue|  Do not include Partition children while finding results by this search term 
         |TrueValue|  Include Partition children while finding results by this search term 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> PartitionSearchTerm.IncludeChildren:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Partition(self) -> Partition:
        """
        Getter for property: ( Partition NXOpen.A) Partition
         Returns the partition of this search term.  
          
                  
         
        """
        pass
import NXOpen
class Partition(NXOpen.NXObject): 
    """
        A partition is a Teamcenter object in a Collaborative Design. A partition can
        contain design elements and other partitions.
    """
    def GetImmediateChildPartitions(self) -> List[Partition]:
        """
         
                    Get all immediate children which are currently loaded. This method needs to be called recursively to get full list of 
                    loaded children. If immediate child partitions are not loaded then call NXOpen.Assemblies.Partition.LoadImmediateChildPartitions
                    to load them.
                
         Returns partitionChildren ( Partition List[NXOpen): .
        """
        pass
    def LoadImmediateChildPartitions(self) -> None:
        """
                    Load all immediate children for the given partition. This may involve server calls in case data needs to be fetched from the database.
                    Call this method at each level to load all partitions.
                
        """
        pass
    def LoadPartitionMembers(self, rootPart: NXOpen.Part, loadMembers: bool) -> None:
        """
                    Retrieves the partition membership information of the input partition and optionally loads all partition members.
                    The load operation will use the currently set assembly load options
                
        """
        pass
class PatternInstance(PatternMember): 
    """
        Represents the pattern instance object.
    """
    def GetClockedStatus(self) -> bool:
        """
         Gets the clocked status of pattern instance.
                
         Returns isClocked (bool): .
        """
        pass
    def GetDeletedStatus(self) -> bool:
        """
         Gets the deleted status of pattern instance.
                
         Returns isDeleted (bool): .
        """
        pass
    def GetIndices(self) -> Tuple[int, int]:
        """
         Gets the indices of pattern instance.
                
         Returns A tuple consisting of (index2, index1). 
         - index2 is: int.
         - index1 is: int.

        """
        pass
    def GetSuppressedStatus(self) -> bool:
        """
         Gets the suppressed status of pattern instance.
                
         Returns isSuppressed (bool): .
        """
        pass
class PatternMaster(PatternMember): 
    """
        Represents the pattern master object.
    """
    pass
import NXOpen
class PatternMember(NXOpen.NXObject): 
    """
        Represents the pattern member object.
    """
    def GetAllComponents(self) -> List[Component]:
        """
         Returns all the NXOpen.Assemblies.Component of pattern member.
         Returns components ( Component List[NXOpen): .
        """
        pass
    def IsPatternMaster(self) -> bool:
        """
         Indicates whether this member is the NXOpen.Assemblies.PatternMaster or not.
         Returns isPatternMaster (bool): .
        """
        pass
import NXOpen
class PlaneSearchTermBuilder(SearchTermBuilder): 
    """
        A PlaneSearchTermBuilder is used to create or edit an NXOpen.Assemblies.PlaneSearchTerm.
    """
    @property
    def Displacement(self) -> float:
        """
        Getter for property: (float) Displacement
         Returns 
                    the displacement of the plane from the origin.  
          
                  
         
        """
        pass
    @Displacement.setter
    def Displacement(self, displacement: float):
        """
        Setter for property: (float) Displacement
         Returns 
                    the displacement of the plane from the origin.  
          
                  
         
        """
        pass
    @property
    def Normal(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) Normal
         Returns 
                    the normal of the plane.  
          
                  
         
        """
        pass
    @Normal.setter
    def Normal(self, normal: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) Normal
         Returns 
                    the normal of the plane.  
          
                  
         
        """
        pass
    @property
    def PlaneOverlapLogic(self) -> PlaneSearchTerm.PlaneOverlapLogicType:
        """
        Getter for property: ( PlaneSearchTerm.PlaneOverlapLogicType NXOpen.A) PlaneOverlapLogic
         Returns 
                    the plane overlap logic.  
          
                  
         
        """
        pass
    @PlaneOverlapLogic.setter
    def PlaneOverlapLogic(self, planeOverlapLogic: PlaneSearchTerm.PlaneOverlapLogicType):
        """
        Setter for property: ( PlaneSearchTerm.PlaneOverlapLogicType NXOpen.A) PlaneOverlapLogic
         Returns 
                    the plane overlap logic.  
          
                  
         
        """
        pass
    @property
    def PointOnPlane(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PointOnPlane
         Returns 
                    the normal of the plane.  
          
                  
         
        """
        pass
    @PointOnPlane.setter
    def PointOnPlane(self, pointOnPlane: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PointOnPlane
         Returns 
                    the normal of the plane.  
          
                  
         
        """
        pass
    @property
    def SearchTermLogic(self) -> SearchTerm.SearchTermLogicType:
        """
        Getter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @SearchTermLogic.setter
    def SearchTermLogic(self, searchTermLogic: SearchTerm.SearchTermLogicType):
        """
        Setter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @property
    def TrueShapeRefinement(self) -> bool:
        """
        Getter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
    @TrueShapeRefinement.setter
    def TrueShapeRefinement(self, trueShapeRefinement: bool):
        """
        Setter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
class PlaneSearchTerm(SearchTerm): 
    """
        A plane search term within a NXOpen.Assemblies.SubsetRecipe.
    """
    class PlaneOverlapLogicType(Enum):
        """
        Members Include: 
         |Above|  Include objects residing above the plane defined by this search term 
         |Below|  Include objects residing below the plane defined by this search term 
         |Intersects|  Include objects intersecting the plane defined by this search term 
         |AboveOrIntersects|  Include objects residing above or intersecting the plane defined by this search term 
         |BelowOrIntersects|  Include objects residing below or intersecting the plane defined by this search term 

        """
        Above: int
        Below: int
        Intersects: int
        AboveOrIntersects: int
        BelowOrIntersects: int
        @staticmethod
        def ValueOf(value: int) -> PlaneSearchTerm.PlaneOverlapLogicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class PositioningGroupBuilder(NXOpen.Builder): 
    """ 
        Represents builder class for positioning group which is used to store constraints for design element.
    """
    @property
    def MakeActive(self) -> bool:
        """
        Getter for property: (bool) MakeActive
         Returns the option to specify whether a newly created positioning group 
                    should be made active after creation or not.  
          
                   
         
        """
        pass
    @MakeActive.setter
    def MakeActive(self, makeActive: bool):
        """
        Setter for property: (bool) MakeActive
         Returns the option to specify whether a newly created positioning group 
                    should be made active after creation or not.  
          
                   
         
        """
        pass
    @property
    def OwningPositioningTask(self) -> PositioningTask:
        """
        Getter for property: ( PositioningTask NXOpen.A) OwningPositioningTask
         Returns the owning positioning task.  
           During creation set method should be called with the positioning task
                    in which new  NXOpen::Assemblies::PositioningGroup  has to be created. During edit operation set 
                    method should not be called. An error would be raised if during edit operation set method is called with a positioning task
                    which is different from the owning positioning task of  NXOpen::Assemblies::PositioningGroup .
                  
         
        """
        pass
    @OwningPositioningTask.setter
    def OwningPositioningTask(self, positioningTask: PositioningTask):
        """
        Setter for property: ( PositioningTask NXOpen.A) OwningPositioningTask
         Returns the owning positioning task.  
           During creation set method should be called with the positioning task
                    in which new  NXOpen::Assemblies::PositioningGroup  has to be created. During edit operation set 
                    method should not be called. An error would be raised if during edit operation set method is called with a positioning task
                    which is different from the owning positioning task of  NXOpen::Assemblies::PositioningGroup .
                  
         
        """
        pass
    @property
    def PositioningGroupDataMembers(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) PositioningGroupDataMembers
         Returns the members for positioning group   
            
         
        """
        pass
    @property
    def PositioningGroupName(self) -> str:
        """
        Getter for property: (str) PositioningGroupName
         Returns the name of positioning group.  
           The user of this API is responcible to free the text pointer   
         
        """
        pass
    @PositioningGroupName.setter
    def PositioningGroupName(self, nameOfPositioningGroup: str):
        """
        Setter for property: (str) PositioningGroupName
         Returns the name of positioning group.  
           The user of this API is responcible to free the text pointer   
         
        """
        pass
import NXOpen
class PositioningGroup(NXOpen.NXObject): 
    """ 
       Represents the class for positioning group.       
    """
    class Status(Enum):
        """
        Members Include: 
         |OutOfDate| 
         |UpToDate| 
         |Unknown| 

        """
        OutOfDate: int
        UpToDate: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> PositioningGroup.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplayConstraints
         Returns
                    the flag indicating whether constraints of member design elements 
                    of this positioning group are to be displayed on the graphics window or not.  
          
                    (This is a separate system from hiding and showing individual constraints.)
                    This flag controls the visibility of both suppressed and unsuppressed constraints.
                  
         
        """
        pass
    @DisplayConstraints.setter
    def DisplayConstraints(self, displayConstraints: bool):
        """
        Setter for property: (bool) DisplayConstraints
         Returns
                    the flag indicating whether constraints of member design elements 
                    of this positioning group are to be displayed on the graphics window or not.  
          
                    (This is a separate system from hiding and showing individual constraints.)
                    This flag controls the visibility of both suppressed and unsuppressed constraints.
                  
         
        """
        pass
    @property
    def DisplaySuppressedConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplaySuppressedConstraints
         Returns
                    the flag indicating whether suppressed constraints of member design elements 
                    of this positioning group are to be displayed on the graphics window or not.  
           
                    (This is a separate system from hiding and showing individual constraints.)
                  
         
        """
        pass
    @DisplaySuppressedConstraints.setter
    def DisplaySuppressedConstraints(self, displaySuppressedConstraints: bool):
        """
        Setter for property: (bool) DisplaySuppressedConstraints
         Returns
                    the flag indicating whether suppressed constraints of member design elements 
                    of this positioning group are to be displayed on the graphics window or not.  
           
                    (This is a separate system from hiding and showing individual constraints.)
                  
         
        """
        pass
    def GetStatus(self) -> PositioningGroup.Status:
        """
         Returns status of positioning group. The status can be one of 
                    NXOpen.Assemblies.PositioningGroup.Status.
                
         Returns positioningStatus ( PositioningGroup.Status NXOpen.A): .
        """
        pass
import NXOpen
class PositioningTaskBuilder(NXOpen.Builder): 
    """ 
       Represents the class for positioning task builder
    """
    @property
    def ContextCollection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ContextCollection
         Returns the context collection   
            
         
        """
        pass
    @property
    def OwningSubset(self) -> Subset:
        """
        Getter for property: ( Subset NXOpen.A) OwningSubset
         Returns the owning subset.  
           During creation set method should be called with the subset instance
                    in which new  NXOpen::Assemblies::PositioningTask  has to be created. During edit operation set 
                    method should not be called. An error would be raised if during edit operation set method is called with a subset instance 
                    which is different from the owning subset instance of  NXOpen::Assemblies::PositioningTask .
                  
         
        """
        pass
    @OwningSubset.setter
    def OwningSubset(self, subsetInstance: Subset):
        """
        Setter for property: ( Subset NXOpen.A) OwningSubset
         Returns the owning subset.  
           During creation set method should be called with the subset instance
                    in which new  NXOpen::Assemblies::PositioningTask  has to be created. During edit operation set 
                    method should not be called. An error would be raised if during edit operation set method is called with a subset instance 
                    which is different from the owning subset instance of  NXOpen::Assemblies::PositioningTask .
                  
         
        """
        pass
    @property
    def WorkCollection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) WorkCollection
         Returns the work collection   
            
         
        """
        pass
import NXOpen
class PositioningTask(NXOpen.NXObject): 
    """ 
       Represents the class for positioning task.       
    """
    @property
    def DisplayConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplayConstraints
         Returns
                    the flag indicating whether constraints of work collection design elements 
                    of this positioning task are to be displayed on the graphics window or not.  
           
                    (This is a separate system from hiding and showing individual constraints.) 
                    This flag controls the visibility of both suppressed and unsuppressed constraints.
                  
         
        """
        pass
    @DisplayConstraints.setter
    def DisplayConstraints(self, displayConstraints: bool):
        """
        Setter for property: (bool) DisplayConstraints
         Returns
                    the flag indicating whether constraints of work collection design elements 
                    of this positioning task are to be displayed on the graphics window or not.  
           
                    (This is a separate system from hiding and showing individual constraints.) 
                    This flag controls the visibility of both suppressed and unsuppressed constraints.
                  
         
        """
        pass
    @property
    def DisplaySuppressedConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplaySuppressedConstraints
         Returns
                    the flag indicating whether suppressed constraints of work collection design  
                    elements of this positioning task are to be displayed on the graphics window   
                    or not.  
           (This is a separate system from hiding and showing individual constraints.)
                  
         
        """
        pass
    @DisplaySuppressedConstraints.setter
    def DisplaySuppressedConstraints(self, displaySuppressedConstraints: bool):
        """
        Setter for property: (bool) DisplaySuppressedConstraints
         Returns
                    the flag indicating whether suppressed constraints of work collection design  
                    elements of this positioning task are to be displayed on the graphics window   
                    or not.  
           (This is a separate system from hiding and showing individual constraints.)
                  
         
        """
        pass
    def Activate(self) -> None:
        """
         Activates the NXOpen.Assemblies.PositioningTask.
                
        """
        pass
    def ActivatePositioningGroup(self, positioningGroup: PositioningGroup) -> None:
        """
         Activates the NXOpen.Assemblies.PositioningGroup in the positioning task.
                
        """
        pass
    def CheckInPositioningGroups(self, positioningGroups: List[PositioningGroup]) -> NXOpen.ErrorList:
        """
                    Checks in the specified NXOpen.Assemblies.PositioningGroups which must be 
                    associated with this positioning task.
                
         Returns errors ( NXOpen.ErrorList):  Any errors that occurred during check in of the Positioning Groups .
        """
        pass
    def CheckOutPositioningGroups(self, positioningGroups: List[PositioningGroup]) -> NXOpen.ErrorList:
        """
                    Checks out the specified NXOpen.Assemblies.PositioningGroups which must be 
                    associated with this positioning task.
                
         Returns errors ( NXOpen.ErrorList):  Any errors that occurred during check out of the Positioning Groups .
        """
        pass
    def Deactivate(self) -> None:
        """
         Deactivates the NXOpen.Assemblies.PositioningTask.
                
        """
        pass
    def DeactivatePositioningGroup(self, positioningGroup: PositioningGroup) -> None:
        """
         Deactivates the NXOpen.Assemblies.PositioningGroup in the positioning task.
                
        """
        pass
    def GetAllContextCollectionMembers(self) -> List[Component]:
        """
         Gets all context collection members of NXOpen.Assemblies.PositioningTask.  
                
         Returns contextCollectionMembers ( Component List[NXOpen): .
        """
        pass
    def GetAllPositioningGroups(self) -> List[PositioningGroup]:
        """
         Gets all NXOpen.Assemblies.PositioningGroups which are 
                    associated with this positioning task. 
                
         Returns positioningGroups ( PositioningGroup List[NXOpen): .
        """
        pass
    def GetAllWorkCollectionMembers(self) -> List[Component]:
        """
         Gets all work collection members of NXOpen.Assemblies.PositioningTask.  
                
         Returns workCollectionMembers ( Component List[NXOpen): .
        """
        pass
    def IsInContextCollection(self, component: Component) -> bool:
        """
         Checks whether the input NXOpen.Assemblies.Component 
                    is a part of NXOpen.Assemblies.PositioningTask context collection 
                    or not.
                
         Returns isInContextCollection (bool): .
        """
        pass
    def IsInWorkCollection(self, component: Component) -> bool:
        """
         Checks whether the input NXOpen.Assemblies.Component is 
                    a part of NXOpen.Assemblies.PositioningTask work collection or not.
                
         Returns isInWorkCollection (bool): .
        """
        pass
    def RemoveFromTask(self, positioningGroup: PositioningGroup) -> None:
        """
         
                    Removes specified NXOpen.Assemblies.PositioningGroup from 
                    NXOpen.Assemblies.PositioningTask.                        
                
        """
        pass
    def Ungroup(self, positioningGroup: PositioningGroup) -> None:
        """
          
                    Ungroups the positioning group. It will delete positioning group and move all its members 
                    to work collection of this NXOpen.Assemblies.PositioningTask.                          
                
        """
        pass
class PositionOverrideType(Enum):
    """
    Members Include: 
     |NotSet|  No position override 
     |Unloaded|  Position overridden, but in an unloaded parent 
     |Explicit|  Position explicitly overridden by user 
     |MatingImplicit|  Position implicitly overridden because of mating conditions 
     |ConstraintImplicit|  Position implicitly overridden because of assembly constraints 

    """
    NotSet: int
    Unloaded: int
    Explicit: int
    MatingImplicit: int
    ConstraintImplicit: int
    @staticmethod
    def ValueOf(value: int) -> PositionOverrideType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ProductOutlineBuilder(NXOpen.Builder): 
    """
       Represents a builder NXOpen.Assemblies.ProductOutlineBuilder. Input to this class can be PSM facet objects.
    """
    class LineFont(Enum):
        """
        Members Include: 
         |Solid|  Solid Line 
         |Dashed|  Dashed Line 
         |Phantom|  Phantom Line 
         |Centerline|  Center Line 
         |Dotted|  Dotted Line 
         |Longdash|  Longdash Line 
         |Dotdash|  Dotdash Line 
         |Eight|  Long Dashed Double Dotted 
         |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
         |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        Longdash: int
        Dotdash: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> ProductOutlineBuilder.LineFont:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LineFontType(self) -> ProductOutlineBuilder.LineFont:
        """
        Getter for property: ( ProductOutlineBuilder.LineFont NXOpen.A) LineFontType
         Returns the line font type for the objects defined in Product Outline.  
           The font types are mentioned in 
                     NXOpen::Assemblies::ProductOutlineBuilder::LineFont .
                     
         
        """
        pass
    @LineFontType.setter
    def LineFontType(self, lineFontType: ProductOutlineBuilder.LineFont):
        """
        Setter for property: ( ProductOutlineBuilder.LineFont NXOpen.A) LineFontType
         Returns the line font type for the objects defined in Product Outline.  
           The font types are mentioned in 
                     NXOpen::Assemblies::ProductOutlineBuilder::LineFont .
                     
         
        """
        pass
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OutlineColor
         Returns the color for all the objects defined in Product Outline.  
            The range is 1-216  
         
        """
        pass
    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OutlineColor
         Returns the color for all the objects defined in Product Outline.  
            The range is 1-216  
         
        """
        pass
    @property
    def OverrideColor(self) -> bool:
        """
        Getter for property: (bool) OverrideColor
         Returns the flag to override-color switch.  
           If "true" the facet representation is in original color of selected object, 
                    else representation is in the color defined by  NXOpen::Assemblies::ProductOutlineBuilder::OutlineColor .
                    
         
        """
        pass
    @OverrideColor.setter
    def OverrideColor(self, overrideColor: bool):
        """
        Setter for property: (bool) OverrideColor
         Returns the flag to override-color switch.  
           If "true" the facet representation is in original color of selected object, 
                    else representation is in the color defined by  NXOpen::Assemblies::ProductOutlineBuilder::OutlineColor .
                    
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObject
         Returns the objects defined in Product Outline.  
             
         
        """
        pass
    @property
    def Translucency(self) -> int:
        """
        Getter for property: (int) Translucency
         Returns the translucency of faceted bodiesobjects defined in Product Outline.  
           The range is 0-100.  
         
        """
        pass
    @Translucency.setter
    def Translucency(self, translucency: int):
        """
        Setter for property: (int) Translucency
         Returns the translucency of faceted bodiesobjects defined in Product Outline.  
           The range is 0-100.  
         
        """
        pass
import NXOpen
class ProductOutlineManager(NXOpen.Object): 
    """  Represents a collection of assemblies. Input to this class can be PSM facet objects.
     """
    @property
    def IsProductOutlineDefined(self) -> bool:
        """
        Getter for property: (bool) IsProductOutlineDefined
         Returns the status of the product outline.  
           If the product outline is already defined, it returns "true", else returns "false".
                  
         
        """
        pass
    def CreateProductOutlineBuilder(self) -> ProductOutlineBuilder:
        """
         Creates a NXOpen.Assemblies.ProductOutlineBuilder. Gives access to the attributes of the Product Outline 
         Returns builder ( ProductOutlineBuilder NXOpen.A): .
        """
        pass
    def ShowProductOutline(self, is_show: bool) -> None:
        """
        Controls the visibility of already defined product outline. Supply true to show the Product Outline, or false
                to hide the Product Outline.
        """
        pass
    def ShowSelectableProductOutline(self, is_selectable: bool) -> None:
        """
        Controls the visibility and selectability of already defined product outline. Supply true to show the selectable Product Outline, or false
                to hide the Product Outline. 
        """
        pass
class ProximitySearchTermBuilder(SearchTermBuilder): 
    """
        A ProximitySearchTermBuilder is used to create or edit an Assemblies.BoxSearchTerm.
    """
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns 
                    the distance.  
          
                  
         
        """
        pass
    @Distance.setter
    def Distance(self, distance: float):
        """
        Setter for property: (float) Distance
         Returns 
                    the distance.  
          
                  
         
        """
        pass
    @property
    def SearchTermLogic(self) -> SearchTerm.SearchTermLogicType:
        """
        Getter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @SearchTermLogic.setter
    def SearchTermLogic(self, searchTermLogic: SearchTerm.SearchTermLogicType):
        """
        Setter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @property
    def TrueShapeRefinement(self) -> bool:
        """
        Getter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
    @TrueShapeRefinement.setter
    def TrueShapeRefinement(self, trueShapeRefinement: bool):
        """
        Setter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
    def GetSeeds(self) -> List[SearchResultElement]:
        """
         Get the proximity search term seed elements.
                
         Returns seeds ( SearchResultElement List[NXOpen): .
        """
        pass
    def SetSeeds(self, seeds: List[SearchResultElement]) -> None:
        """
         Set the proximity search term seed elements.
                
        """
        pass
class ProximitySearchTerm(SearchTerm): 
    """
        A proximity search term within a NXOpen.Assemblies.SubsetRecipe.
    """
    pass
import NXOpen
class ReflectComponentBuilder(NXOpen.Builder): 
    """
    Represents a builder class that creates reflected component
    """
    def GetComponentsToReflect(self) -> List[Component]:
        """
         Returns the components to be used for creating reflected components
         Returns componentsToReflect ( Component List[NXOpen): .
        """
        pass
    def GetReflectedComponents(self) -> List[Component]:
        """
         Returns the reflected components
         Returns reflectedComponents ( Component List[NXOpen): .
        """
        pass
    def GetReflectionPlane(self) -> NXOpen.Plane:
        """
         Returns the reflection plane to be used for creating reflected components
         Returns reflectionPlane ( NXOpen.Plane): .
        """
        pass
    def SetComponentsToReflect(self, componentsToReflect: List[Component]) -> None:
        """
         Sets the components to be used for creating reflected components
        """
        pass
    def SetReflectionPlane(self, reflectionPlane: NXOpen.Plane) -> None:
        """
         Sets the reflection plane to be used for creating reflected components
        """
        pass
import NXOpen
import NXOpen.Features
class RelinkerBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Assemblies.RelinkerBuilder
    """
    class LinkCategory(Enum):
        """
        Members Include: 
         |WaveGeometry|  Indicate link category is wave geometry 
         |InterpartExpression|  Indicate link category is interpart expression 

        """
        WaveGeometry: int
        InterpartExpression: int
        @staticmethod
        def ValueOf(value: int) -> RelinkerBuilder.LinkCategory:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkOption(Enum):
        """
        Members Include: 
         |InterpartExpression|  Indicate relink option is interpart expression only 
         |WaveGeometry|  Indicate relink option is wave geometry only 
         |Both|  Indicate relink option is both interpart expression and wave link 

        """
        InterpartExpression: int
        WaveGeometry: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> RelinkerBuilder.LinkOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkScope(Enum):
        """
        Members Include: 
         |PartsInSession|  Indicate relink scope is parts in session 
         |PartsInAssembly|  Indicate relink scope is parts in assembly 
         |WorkPart|  Indicate relink scope is work part 
         |SelectedParts|  Indicate relink scope is selected parts 

        """
        PartsInSession: int
        PartsInAssembly: int
        WorkPart: int
        SelectedParts: int
        @staticmethod
        def ValueOf(value: int) -> RelinkerBuilder.LinkScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkType(Enum):
        """
        Members Include: 
         |All|  Indicate relink browser type is all 
         |NotBroken|  Indicate relink browser type is not broken only 
         |Broken|  Indicate relink browser type is broken only
         |AutoLinked|  Indicate relink browser type is auto-linked only
         |WithMultipleSource|  Indicate relink browser type is with multuple source 

        """
        All: int
        NotBroken: int
        Broken: int
        AutoLinked: int
        WithMultipleSource: int
        @staticmethod
        def ValueOf(value: int) -> RelinkerBuilder.LinkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BreakInterpartExpression(self) -> bool:
        """
        Getter for property: (bool) BreakInterpartExpression
         Returns the option to break interpart expression.  
           
                If it's true, relinker will break interpart expression after relinking. If it's false, relinker will not break interpart expression.  
         
        """
        pass
    @BreakInterpartExpression.setter
    def BreakInterpartExpression(self, breakInterPartExpression: bool):
        """
        Setter for property: (bool) BreakInterpartExpression
         Returns the option to break interpart expression.  
           
                If it's true, relinker will break interpart expression after relinking. If it's false, relinker will not break interpart expression.  
         
        """
        pass
    @property
    def BreakWaveLink(self) -> bool:
        """
        Getter for property: (bool) BreakWaveLink
         Returns the option to break WAVE links.  
          
                If it's true, relinker will break WAVE links after relinking. If it's false, relinker will not break WAVE links.  
         
        """
        pass
    @BreakWaveLink.setter
    def BreakWaveLink(self, breakWave: bool):
        """
        Setter for property: (bool) BreakWaveLink
         Returns the option to break WAVE links.  
          
                If it's true, relinker will break WAVE links after relinking. If it's false, relinker will not break WAVE links.  
         
        """
        pass
    @property
    def FaceCurveDirectionAdjustment(self) -> bool:
        """
        Getter for property: (bool) FaceCurveDirectionAdjustment
         Returns the option to adjust face or curve direction.  
          
                If it's true, relinker will check the linked curve direction or face normal and 
                either keep or automatically flip the direction of new source while relinking.  
         
        """
        pass
    @FaceCurveDirectionAdjustment.setter
    def FaceCurveDirectionAdjustment(self, adjustDir: bool):
        """
        Setter for property: (bool) FaceCurveDirectionAdjustment
         Returns the option to adjust face or curve direction.  
          
                If it's true, relinker will check the linked curve direction or face normal and 
                either keep or automatically flip the direction of new source while relinking.  
         
        """
        pass
    @property
    def IncludeNonBrokenWaveLinks(self) -> bool:
        """
        Getter for property: (bool) IncludeNonBrokenWaveLinks
         Returns the option to include non-broken WAVE links or not.  
          
                If it's true, relinker will include non-broken WAVE links. If it's false, non-broken WAVE links will not be included while relinking.
                The default behavior in the relinker is not to include non-broken WAVE links.   
         
        """
        pass
    @IncludeNonBrokenWaveLinks.setter
    def IncludeNonBrokenWaveLinks(self, includeNonBrokenWaveLinks: bool):
        """
        Setter for property: (bool) IncludeNonBrokenWaveLinks
         Returns the option to include non-broken WAVE links or not.  
          
                If it's true, relinker will include non-broken WAVE links. If it's false, non-broken WAVE links will not be included while relinking.
                The default behavior in the relinker is not to include non-broken WAVE links.   
         
        """
        pass
    @property
    def IncludeSuppressedComponents(self) -> bool:
        """
        Getter for property: (bool) IncludeSuppressedComponents
         Returns the option to include suppressed components as source candidates or not.  
          
                If it's true, relinker will include suppressed components as source candidates. If it's false, suppressed components will not be included as source candidates while relinking.
                The default behavior in the relinker is not to include suppressed components.   
         
        """
        pass
    @IncludeSuppressedComponents.setter
    def IncludeSuppressedComponents(self, includeSuppressedComponents: bool):
        """
        Setter for property: (bool) IncludeSuppressedComponents
         Returns the option to include suppressed components as source candidates or not.  
          
                If it's true, relinker will include suppressed components as source candidates. If it's false, suppressed components will not be included as source candidates while relinking.
                The default behavior in the relinker is not to include suppressed components.   
         
        """
        pass
    @property
    def RelinkCategory(self) -> RelinkerBuilder.LinkCategory:
        """
        Getter for property: ( RelinkerBuilder.LinkCategory NXOpen.A) RelinkCategory
         Returns the relink category either wave geometry or interpart expression.  
             
         
        """
        pass
    @RelinkCategory.setter
    def RelinkCategory(self, linkCategory: RelinkerBuilder.LinkCategory):
        """
        Setter for property: ( RelinkerBuilder.LinkCategory NXOpen.A) RelinkCategory
         Returns the relink category either wave geometry or interpart expression.  
             
         
        """
        pass
    @property
    def RelinkOption(self) -> RelinkerBuilder.LinkOption:
        """
        Getter for property: ( RelinkerBuilder.LinkOption NXOpen.A) RelinkOption
         Returns the link option.  
          
                Relinker will check this option to relink WAVE, interpart expression or both   
         
        """
        pass
    @RelinkOption.setter
    def RelinkOption(self, linkOption: RelinkerBuilder.LinkOption):
        """
        Setter for property: ( RelinkerBuilder.LinkOption NXOpen.A) RelinkOption
         Returns the link option.  
          
                Relinker will check this option to relink WAVE, interpart expression or both   
         
        """
        pass
    @property
    def RelinkType(self) -> RelinkerBuilder.LinkType:
        """
        Getter for property: ( RelinkerBuilder.LinkType NXOpen.A) RelinkType
         Returns the current link type.  
             
         
        """
        pass
    @RelinkType.setter
    def RelinkType(self, linkType: RelinkerBuilder.LinkType):
        """
        Setter for property: ( RelinkerBuilder.LinkType NXOpen.A) RelinkType
         Returns the current link type.  
             
         
        """
        pass
    @property
    def SearchExistingInterPartExpressionOnly(self) -> bool:
        """
        Getter for property: (bool) SearchExistingInterPartExpressionOnly
         Returns the option to search existing inter part expression only or all expressions including regular ones.  
            
         
        """
        pass
    @SearchExistingInterPartExpressionOnly.setter
    def SearchExistingInterPartExpressionOnly(self, searchExistingIPEOnly: bool):
        """
        Setter for property: (bool) SearchExistingInterPartExpressionOnly
         Returns the option to search existing inter part expression only or all expressions including regular ones.  
            
         
        """
        pass
    @property
    def SearchingDestinationObject(self) -> str:
        """
        Getter for property: (str) SearchingDestinationObject
         Returns the searching destination object string.  
          
                Used to specify the wildcard string to search the destination objects when cycling object by name.
                When cycling destination objects, relink scope will be used as the searching scope.  
         
        """
        pass
    @SearchingDestinationObject.setter
    def SearchingDestinationObject(self, destinationObjectStr: str):
        """
        Setter for property: (str) SearchingDestinationObject
         Returns the searching destination object string.  
          
                Used to specify the wildcard string to search the destination objects when cycling object by name.
                When cycling destination objects, relink scope will be used as the searching scope.  
         
        """
        pass
    @property
    def SearchingSourceObject(self) -> str:
        """
        Getter for property: (str) SearchingSourceObject
         Returns the searching source object string.  
          
                Used to specify the wildcard string to search the source objects when cycling object by name.
                When cycling source objects, source parts will define the searching scope.  
         
        """
        pass
    @SearchingSourceObject.setter
    def SearchingSourceObject(self, sourceObjectStr: str):
        """
        Setter for property: (str) SearchingSourceObject
         Returns the searching source object string.  
          
                Used to specify the wildcard string to search the source objects when cycling object by name.
                When cycling source objects, source parts will define the searching scope.  
         
        """
        pass
    @property
    def SearchingSourcePart(self) -> str:
        """
        Getter for property: (str) SearchingSourcePart
         Returns the searching source part string.  
          
                Used to specify the wildcard string to search source parts by file names.
                Source parts define the scope of searching source objects.  
         
        """
        pass
    @SearchingSourcePart.setter
    def SearchingSourcePart(self, sourcePartStr: str):
        """
        Setter for property: (str) SearchingSourcePart
         Returns the searching source part string.  
          
                Used to specify the wildcard string to search source parts by file names.
                Source parts define the scope of searching source objects.  
         
        """
        pass
    @property
    def SearchingSourcePartAttribute(self) -> str:
        """
        Getter for property: (str) SearchingSourcePartAttribute
         Returns the searching source part attribute string.  
          
                Used to specify the wildcard string to search source parts by part attribute predefined in source part.
                This criterial will furtherly narrow down the source part scope to avoid multiple source found.  
         
        """
        pass
    @SearchingSourcePartAttribute.setter
    def SearchingSourcePartAttribute(self, sourcePartAttribute: str):
        """
        Setter for property: (str) SearchingSourcePartAttribute
         Returns the searching source part attribute string.  
          
                Used to specify the wildcard string to search source parts by part attribute predefined in source part.
                This criterial will furtherly narrow down the source part scope to avoid multiple source found.  
         
        """
        pass
    @property
    def SelectComponent(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) SelectComponent
         Returns a list of the selected component as relink target scope.  
            
         
        """
        pass
    @property
    def SelectComponentSource(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.A) SelectComponentSource
         Returns a list of the selected component as relink source scope.  
            
         
        """
        pass
    @property
    def SourceScope(self) -> RelinkerBuilder.LinkScope:
        """
        Getter for property: ( RelinkerBuilder.LinkScope NXOpen.A) SourceScope
         Returns the current source scope.  
             
         
        """
        pass
    @SourceScope.setter
    def SourceScope(self, sourceScope: RelinkerBuilder.LinkScope):
        """
        Setter for property: ( RelinkerBuilder.LinkScope NXOpen.A) SourceScope
         Returns the current source scope.  
             
         
        """
        pass
    @property
    def TargetScope(self) -> RelinkerBuilder.LinkScope:
        """
        Getter for property: ( RelinkerBuilder.LinkScope NXOpen.A) TargetScope
         Returns the current target scope.  
             
         
        """
        pass
    @TargetScope.setter
    def TargetScope(self, targetScope: RelinkerBuilder.LinkScope):
        """
        Setter for property: ( RelinkerBuilder.LinkScope NXOpen.A) TargetScope
         Returns the current target scope.  
             
         
        """
        pass
    def ExecuteRelink(self) -> None:
        """
         Relink with new source, for WAVE links, interpart explression or both. 
        """
        pass
    def ExportToInformationWindow(self) -> None:
        """
         List all link information to the list window. 
        """
        pass
    def GetExpressionSourceCount(self, partID: NXOpen.Part, expID: NXOpen.Expression, sourceID: NXOpen.Expression) -> int:
        """
         Gets the total count of multiple candidate sources to re-parent the inter part expression. 
         Returns iSourceCount (int): .
        """
        pass
    def RelinkInterpartExpression(self, partID: NXOpen.Part, expID: NXOpen.Expression, sourceID: NXOpen.Expression) -> None:
        """
         Relinks the inter part expression using the specific expression from the specific part in case of multiple expression sources. 
        """
        pass
    def RelinkWaveFeature(self, partID: NXOpen.Part, featID: NXOpen.Features.Feature, sourceID: NXOpen.NXObject) -> None:
        """
         Relinks the wave feature using the specific geometry source from the specific part in case of multiple geometry sources. 
        """
        pass
    def SearchWavelinksInterpartExpressions(self) -> None:
        """
          Searches WAVE links and interpart expressions. 
                     This method does not actually change the link data and interpart expressions.
                    
                
        """
        pass
    def UpdateSession(self) -> None:
        """
         Updates the session. 
        """
        pass
    def UpdateSessionWithBreakDelayed(self) -> None:
        """
         Updates the session without immediately breaking wave links or inter part expressions. 
        """
        pass
    def ViewFeatureFailure(self) -> None:
        """
         Views the feature failure information.
                All failed features in assembly will be shown with detailed information. 
        """
        pass
import NXOpen
class RelinkerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of relinker """
    def CreateBuilder(self) -> RelinkerBuilder:
        """
         Creates a Relinker builder 
         Returns builder ( RelinkerBuilder NXOpen.A):  RelinkerBuilder  object object .
        """
        pass
import NXOpen
class ReplaceComponentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.ReplaceComponentBuilder builder. Input to this class can be PSM facet objects.
     """
    class ComponentLayerOption(Enum):
        """
        Members Include: 
         |Maintain|  Maintain the layer of the component being replaced out 
         |Original|  Set the layer to replacement part's original layer 
         |Work|  Set the layer to current work layer
         |AsSpecified|  Set the specified layer

        """
        Maintain: int
        Original: int
        Work: int
        AsSpecified: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceComponentBuilder.ComponentLayerOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentNameOption(Enum):
        """
        Members Include: 
         |Maintain|  Maintain the component name of the component being replaced out 
         |Original|  Use the replacement part name as the component name 
         |AsSpecified|  Set the specified component name

        """
        Maintain: int
        Original: int
        AsSpecified: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceComponentBuilder.ComponentNameOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentReferenceSet(Enum):
        """
        Members Include: 
         |Maintain|  Maintain the reference set of the component being replaced out 
         |EntirePart|  Set the reference set to Entire Part 
         |Empty|  Set the reference to Empty 
         |Others|  Set the specified reference set 

        """
        Maintain: int
        EntirePart: int
        Empty: int
        Others: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceComponentBuilder.ComponentReferenceSet:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowTemporaryPartsToReplace(self) -> bool:
        """
        Getter for property: (bool) AllowTemporaryPartsToReplace
         Returns the flag to determine whether unsaved parts are allowed to replace.  
           If set to true, then this may result in loss of unsaved data.  
         
        """
        pass
    @AllowTemporaryPartsToReplace.setter
    def AllowTemporaryPartsToReplace(self, allowTemporaryPartsToReplace: bool):
        """
        Setter for property: (bool) AllowTemporaryPartsToReplace
         Returns the flag to determine whether unsaved parts are allowed to replace.  
           If set to true, then this may result in loss of unsaved data.  
         
        """
        pass
    @property
    def ComponentLayer(self) -> int:
        """
        Getter for property: (int) ComponentLayer
         Returns the layer for the new replacement part.  
          
                    
                    -1 means use the original layers defined in the component.
                    0 means use the work layer.
                    1-256 means use the specified layer.
                   
                  
         
        """
        pass
    @ComponentLayer.setter
    def ComponentLayer(self, componentLayer: int):
        """
        Setter for property: (int) ComponentLayer
         Returns the layer for the new replacement part.  
          
                    
                    -1 means use the original layers defined in the component.
                    0 means use the work layer.
                    1-256 means use the specified layer.
                   
                  
         
        """
        pass
    @property
    def ComponentLayerOptionType(self) -> ReplaceComponentBuilder.ComponentLayerOption:
        """
        Getter for property: ( ReplaceComponentBuilder.ComponentLayerOption NXOpen.A) ComponentLayerOptionType
         Returns the layer options   
            
         
        """
        pass
    @ComponentLayerOptionType.setter
    def ComponentLayerOptionType(self, componentLayerOption: ReplaceComponentBuilder.ComponentLayerOption):
        """
        Setter for property: ( ReplaceComponentBuilder.ComponentLayerOption NXOpen.A) ComponentLayerOptionType
         Returns the layer options   
            
         
        """
        pass
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, componentName: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
    @property
    def ComponentNameType(self) -> ReplaceComponentBuilder.ComponentNameOption:
        """
        Getter for property: ( ReplaceComponentBuilder.ComponentNameOption NXOpen.A) ComponentNameType
         Returns the component name options   
            
         
        """
        pass
    @ComponentNameType.setter
    def ComponentNameType(self, componentNameOption: ReplaceComponentBuilder.ComponentNameOption):
        """
        Setter for property: ( ReplaceComponentBuilder.ComponentNameOption NXOpen.A) ComponentNameType
         Returns the component name options   
            
         
        """
        pass
    @property
    def ComponentsToReplace(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ComponentsToReplace
         Returns the objects to be replaced.  
             
         
        """
        pass
    @property
    def MaintainRelationships(self) -> bool:
        """
        Getter for property: (bool) MaintainRelationships
         Returns the maintain relationships   
            
         
        """
        pass
    @MaintainRelationships.setter
    def MaintainRelationships(self, maintainRelationships: bool):
        """
        Setter for property: (bool) MaintainRelationships
         Returns the maintain relationships   
            
         
        """
        pass
    @property
    def ReplaceAllOccurrences(self) -> bool:
        """
        Getter for property: (bool) ReplaceAllOccurrences
         Returns the replace all occurrences   
            
         
        """
        pass
    @ReplaceAllOccurrences.setter
    def ReplaceAllOccurrences(self, replaceAllOccurrences: bool):
        """
        Setter for property: (bool) ReplaceAllOccurrences
         Returns the replace all occurrences   
            
         
        """
        pass
    @property
    def ReplacementPart(self) -> str:
        """
        Getter for property: (str) ReplacementPart
         Returns the replacement part.  
             
         
        """
        pass
    @ReplacementPart.setter
    def ReplacementPart(self, replacementPart: str):
        """
        Setter for property: (str) ReplacementPart
         Returns the replacement part.  
             
         
        """
        pass
    def GetComponentReferenceSetType(self) -> Tuple[ReplaceComponentBuilder.ComponentReferenceSet, str]:
        """
         Get the  reference set 
         Returns A tuple consisting of (componentReferenceSet, referenceSetName). 
         - componentReferenceSet is:  ReplaceComponentBuilder.ComponentReferenceSet NXOpen.A.
         - referenceSetName is: str. Name of the reference set.

        """
        pass
    def GetErrorList(self) -> NXOpen.ErrorList:
        """
         Get the list of components that failed to replace with their corresponding error codes. Caller need to dispose the error list after processing it. 
         Returns errorList ( NXOpen.ErrorList): .
        """
        pass
    def RegisterReplacePartLoadStatus(self) -> NXOpen.PartLoadStatus:
        """
         Register the part load status with the replace operation. If during the operation
                    a part could not be loaded, then this object will be used to store error information.
                
         Returns replaceLoadStatus ( NXOpen.PartLoadStatus): .
        """
        pass
    def SetComponentReferenceSetType(self, componentReferenceSet: ReplaceComponentBuilder.ComponentReferenceSet, referenceSetName: str) -> None:
        """
         Set the reference set 
        """
        pass
class RunContentProximitySearchTermBuilder(SearchTermBuilder): 
    """
        A RunContentProximitySearchTermBuilder is used to create or edit an Assemblies.RunContentProximitySearchTerm.
    """
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns 
                    the distance for the proximity.  
          
                  
         
        """
        pass
    @Distance.setter
    def Distance(self, distance: float):
        """
        Setter for property: (float) Distance
         Returns 
                    the distance for the proximity.  
          
                  
         
        """
        pass
    @property
    def SearchTermLogic(self) -> SearchTerm.SearchTermLogicType:
        """
        Getter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @SearchTermLogic.setter
    def SearchTermLogic(self, searchTermLogic: SearchTerm.SearchTermLogicType):
        """
        Setter for property: ( SearchTerm.SearchTermLogicType NXOpen.A) SearchTermLogic
         Returns 
                    the search term logic.  
          
                  
         
        """
        pass
    @property
    def TrueShapeRefinement(self) -> bool:
        """
        Getter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
    @TrueShapeRefinement.setter
    def TrueShapeRefinement(self, trueShapeRefinement: bool):
        """
        Setter for property: (bool) TrueShapeRefinement
         Returns 
                    the true-shape refinement.  
          
                  
         
        """
        pass
    def GetSeedName(self) -> str:
        """
         Get the seed element name which is used in RunContentProximity search.
                    The seed in this case is the name of the Run object.
                    The 3D contents of this Run object will be used as seeds for the proximity search.
                
         Returns seedRunName (str): .
        """
        pass
    def SetSeedName(self, seedRunName: str) -> None:
        """
         Set the seed element name which is used in RunContentProximity search.
                    The seed in this case is the name of the Run object.
                    The 3D contents of this Run object will be used as seeds for the proximity search.
                
        """
        pass
class RunContentProximitySearchTerm(SearchTerm): 
    """
        A proximity search term within a NXOpen.Assemblies.SubsetRecipe.
    """
    pass
import NXOpen
class SearchResultCollection(NXOpen.TaggedObjectCollection): 
    """
        A collection of NXOpen.Assemblies.SearchResultElements.
    """
    def FindObject(self, journalIdentifier: str) -> SearchResultElement:
        """
         Finds the NXOpen.Assemblies.SearchResultElement with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
            
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns searchResultElement ( SearchResultElement NXOpen.A):  Element found, or null if no such search result element exists.
        """
        pass
import NXOpen
import NXOpen.PDM
class SearchResultElement(NXOpen.NXObject): 
    """
        A search result element can be produced as the result of a search performed in the context of a NXOpen.Assemblies.SubsetBuilder.
        They can be found through NXOpen.Assemblies.SubsetBuilder.SearchResults.
    """
    @property
    def ModelElementRevision(self) -> NXOpen.PDM.ModelElementRevision:
        """
        Getter for property: ( NXOpen.PDM.ModelElementRevision) ModelElementRevision
         Returns
                    the underlying design model revision associated with this search element.  
          
                  
         
        """
        pass
import NXOpen
class SearchTermBuilder(NXOpen.Builder): 
    """
        A SearchTermBuilder is used to create or edit an NXOpen.Assemblies.SearchTerm.
        This is the abstract base class for builders used to create search terms.
    """
    pass
import NXOpen
class SearchTerm(NXOpen.NXObject): 
    """
        A search term is used to specify a search for the contents of a NXOpen.Assemblies.Subset. 
        It is an element of a NXOpen.Assemblies.SubsetRecipe.
    """
    class SearchTermLogicType(Enum):
        """
        Members Include: 
         |Include|  Include results found by this search term 
         |Exclude|  Exclude results found by this search term 
         |Filter|  Filter using results found by this search term 

        """
        Include: int
        Exclude: int
        Filter: int
        @staticmethod
        def ValueOf(value: int) -> SearchTerm.SearchTermLogicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectComponentList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: Component) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[Component], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[Component]) -> bool:
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
    def Add(self, selection: Component, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: Component, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    def Contains(self, objectValue: Component) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[Component]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( Component List[NXOpen):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: Component) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[Component]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: Component, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[Component]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectComponent(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Component:
        """
        Getter for property: ( Component NXOpen.A) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Component):
        """
        Setter for property: ( Component NXOpen.A) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Component, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Component NXOpen.A. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Component, NXOpen.View, NXOpen.Point3d, Component, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Component NXOpen.A. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Component NXOpen.A. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Component, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Component NXOpen.A. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: Component, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: Component, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.Drawings
class ShowComponentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.ShowComponentBuilder """
    @property
    def Components(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Components
         Returns the components to show   
            
         
        """
        pass
    @property
    def MaintainComponentsShown(self) -> bool:
        """
        Getter for property: (bool) MaintainComponentsShown
         Returns the current status of the Maintain Components Shown in View option   
            
         
        """
        pass
    @MaintainComponentsShown.setter
    def MaintainComponentsShown(self, maintainComponents: bool):
        """
        Setter for property: (bool) MaintainComponentsShown
         Returns the current status of the Maintain Components Shown in View option   
            
         
        """
        pass
    @property
    def Views(self) -> NXOpen.Drawings.SelectDraftingViewList:
        """
        Getter for property: ( NXOpen.Drawings.SelectDraftingViewList) Views
         Returns the drafting views   
            
         
        """
        pass
import NXOpen
class SimplifyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.SimplifyBuilder builder class.
        This builder creates a simplification of an assembly in an existing part, which can be
        created by an NXOpen call or can already be loaded in the current session. The part
        must be fully loaded.
      """
    class MassPropertiesOptionValue(Enum):
        """
        Members Include: 
         |StoreCalculated|  Calculate and save the mass properties of the source assembly on the simplified part 
         |StoreZero|  Set the mass properties of the simplified part to zero 

        """
        StoreCalculated: int
        StoreZero: int
        @staticmethod
        def ValueOf(value: int) -> SimplifyBuilder.MassPropertiesOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContextComponent(self) -> Component:
        """
        Getter for property: ( Component NXOpen.A) ContextComponent
         Returns the context component used for the builder.  
            This will generally be the current
                     NXOpen::PartCollection::WorkComponent .  It can
                    be NULL_TAG if the builder is created when the work part is also the current
                    display part.   
         
        """
        pass
    @property
    def DestinationPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) DestinationPart
         Returns the destination part containing the result of simplification.  
           It must be fully loaded.   
         
        """
        pass
    @DestinationPart.setter
    def DestinationPart(self, destinationPart: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) DestinationPart
         Returns the destination part containing the result of simplification.  
           It must be fully loaded.   
         
        """
        pass
    @property
    def ExcludeBodiesCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ExcludeBodiesCollector
         Returns the excluded bodies collector, used to explicitly exclude bodies from the simplification even
                    though the active body simplification rules would include them.  
           This will exclude bodies that
                    would otherwise be included because they belong to a component that is included. The bodies
                    have to be from the source assembly.  
         
        """
        pass
    @property
    def ExcludeBodiesExceptions(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ExcludeBodiesExceptions
         Returns the bodies to explicitly exclude from the simplification even though the active body simplification 
                    rules would include them.  
           This will exclude bodies that would otherwise be included 
                    because they belong to a component that is included. The bodies have to be from the source assembly.   
         
        """
        pass
    @property
    def ExcludeFacesCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ExcludeFacesCollector
         Returns the excluded faces collector, used to exclude or delete faces from the simplification
                    result even though the active geometry simplification rules would include them.  
           This can
                    be used to remove unwanted faces without using any geometry-based simplifications.
                    The faces can only be either from the selected bodies or from the selected components and
                    they have to be from the source assembly.  
         
        """
        pass
    @property
    def ExcludeFacesExceptions(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ExcludeFacesExceptions
         Returns the faces to explicitly exclude or delete from the simplification result even though
                    the active geometry simplification rules would include them.  
           This can be used to remove 
                    unwanted faces without using any geometry-based simplifications.
                    The faces can only be either from the selected bodies or from the selected components 
                    and they have to be from the source assembly.  
         
        """
        pass
    @property
    def IncludeBodiesCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) IncludeBodiesCollector
         Returns the included bodies collector, used to explicitly include bodies in the simplification even
                    though they would be excluded because of minimum body size or because of being an internal body.  
          
                    The bodies have to be from the source assembly.  
         
        """
        pass
    @property
    def IncludeBodiesExceptions(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) IncludeBodiesExceptions
         Returns the bodies to explicitly include in the simplification even though they would be excluded 
                    because of minimum body size or because of being an internal body.  
           The bodies have to be from
                    the source assembly.   
         
        """
        pass
    @property
    def IncludeFacesCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) IncludeFacesCollector
         Returns the included faces collector, used to explicitly include or retain faces in the simplification
                    result even though the active geometry simplification rules (like removal based on hole diameter
                    size) would remove them.  
           The faces can only be from the selected bodies or from the selected
                    components and they have to be from the source assembly.  
         
        """
        pass
    @property
    def IncludeFacesExceptions(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) IncludeFacesExceptions
         Returns the faces to explicitly include or retain in the simplification result even though
                    the active geometry simplification rules (like removal based on hole diameter size) would remove them.  
          
                    The faces can only be either from the selected bodies or from the selected components and they have to be from the
                    source assembly.  
         
        """
        pass
    @property
    def MassPropertiesOption(self) -> SimplifyBuilder.MassPropertiesOptionValue:
        """
        Getter for property: ( SimplifyBuilder.MassPropertiesOptionValue NXOpen.A) MassPropertiesOption
         Returns the mass property options for the simplify operation.  
           This property has no effect if the
                    simplified bodies are created in the source assembly.   
         
        """
        pass
    @MassPropertiesOption.setter
    def MassPropertiesOption(self, massPropertiesOption: SimplifyBuilder.MassPropertiesOptionValue):
        """
        Setter for property: ( SimplifyBuilder.MassPropertiesOptionValue NXOpen.A) MassPropertiesOption
         Returns the mass property options for the simplify operation.  
           This property has no effect if the
                    simplified bodies are created in the source assembly.   
         
        """
        pass
    @property
    def MaximumBlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumBlendRadius
         Returns the blend radius up-to-and-including which blends are removed simplifying the selected bodies.  
             
         
        """
        pass
    @property
    def MaximumHoleSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumHoleSize
         Returns the hole diameter size up-to-and-including which holes are removed simplifying the selected bodies.  
             
         
        """
        pass
    @property
    def MinimumBodySize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumBodySize
         Returns the size of the body below which bodies are excluded from the simplification 
                    Size filtering is based on the minimum to maximum corner-to-corner diameter of the enclosing box   
            
         
        """
        pass
    @property
    def ObjectsToSimplify(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectsToSimplify
         Returns the objects for performing assembly simplification 
                    the objects can be components or solid bodies from the source assembly   
            
         
        """
        pass
    @property
    def ObjectsToSimplifyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ObjectsToSimplifyCollector
         Returns the collector of objects for performing assembly simplification.  
          
                    the objects can be components or solid bodies from the source assembly.   
         
        """
        pass
    @property
    def RemoveInternalBodies(self) -> bool:
        """
        Getter for property: (bool) RemoveInternalBodies
         Returns the toggle for removing bodies not visible based on being completely enclosed by other bodies.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveInternalBodies.setter
    def RemoveInternalBodies(self, removeInternalBodies: bool):
        """
        Setter for property: (bool) RemoveInternalBodies
         Returns the toggle for removing bodies not visible based on being completely enclosed by other bodies.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def RemoveInternalVoids(self) -> bool:
        """
        Getter for property: (bool) RemoveInternalVoids
         Returns the toggle to remove internal enclosed voids from bodies included in simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveInternalVoids.setter
    def RemoveInternalVoids(self, removeInternalVoids: bool):
        """
        Setter for property: (bool) RemoveInternalVoids
         Returns the toggle to remove internal enclosed voids from bodies included in simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def SourceAssembly(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) SourceAssembly
         Returns the source assembly which is being simplified   
            
         
        """
        pass
    @property
    def UniteBodies(self) -> bool:
        """
        Getter for property: (bool) UniteBodies
         Returns the toggle to unite overlapping bodies included in simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @UniteBodies.setter
    def UniteBodies(self, uniteBodies: bool):
        """
        Setter for property: (bool) UniteBodies
         Returns the toggle to unite overlapping bodies included in simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def UseBlendRadius(self) -> bool:
        """
        Getter for property: (bool) UseBlendRadius
         Returns the toggle that controls whether blends are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @UseBlendRadius.setter
    def UseBlendRadius(self, useBlendRadius: bool):
        """
        Setter for property: (bool) UseBlendRadius
         Returns the toggle that controls whether blends are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def UseBodySize(self) -> bool:
        """
        Getter for property: (bool) UseBodySize
         Returns the toggle controlling whether body size is used to filter out small bodies from the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @UseBodySize.setter
    def UseBodySize(self, useBodySize: bool):
        """
        Setter for property: (bool) UseBodySize
         Returns the toggle controlling whether body size is used to filter out small bodies from the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def UseHoleDiameter(self) -> bool:
        """
        Getter for property: (bool) UseHoleDiameter
         Returns the toggle that controls whether holes are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @UseHoleDiameter.setter
    def UseHoleDiameter(self, useHoleDiameter: bool):
        """
        Setter for property: (bool) UseHoleDiameter
         Returns the toggle that controls whether holes are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    def Preview(self) -> int:
        """
         Previews the result of simplification based on the inputs in the builder.
                    This API is primarily intended for interactive NX session.
                    During preview, simplified bodies are created in the destination part without uniting the bodies
                    and the destination part is made a displayed part. An error code will be returned in
                    previewStatusCode if the preview was successfully created but had minor issues. In an NXOpen
                    program, invoking this preview API is not necessary. The new bodies in the destination part after
                    preview are intermediate and their part is not suitable for any operation. Only after the user
                    successfully commits and destroys the builder is the destination part suitable for any
                    operation. 
         Returns previewStatusCode (int): .
        """
        pass
import NXOpen
import NXOpen.PDM
class SubsetBuilder(NXOpen.Builder): 
    """
        A SubsetBuilder is used to create or edit an NXOpen.Assemblies.Subset.
    """
    @property
    def AddAllSubordinates(self) -> bool:
        """
        Getter for property: (bool) AddAllSubordinates
         Returns the value which determines whether the subset will include all the subordinates of reuse design elements.  
             
         
        """
        pass
    @AddAllSubordinates.setter
    def AddAllSubordinates(self, addAllSubordinates: bool):
        """
        Setter for property: (bool) AddAllSubordinates
         Returns the value which determines whether the subset will include all the subordinates of reuse design elements.  
             
         
        """
        pass
    @property
    def CollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: ( NXOpen.CollaborativeDesign) CollaborativeDesign
         Returns the  NXOpen::CollaborativeDesign  of the subset.  
          
                  
         
        """
        pass
    @CollaborativeDesign.setter
    def CollaborativeDesign(self, collaborativeDesign: NXOpen.CollaborativeDesign):
        """
        Setter for property: ( NXOpen.CollaborativeDesign) CollaborativeDesign
         Returns the  NXOpen::CollaborativeDesign  of the subset.  
          
                  
         
        """
        pass
    @property
    def ConfigurationContext(self) -> NXOpen.PDM.ConfigurationContextBuilder:
        """
        Getter for property: ( NXOpen.PDM.ConfigurationContextBuilder) ConfigurationContext
         Returns the configuration context builder.  
             
         
        """
        pass
    @property
    def ContentDefinition(self) -> NXOpen.ContentDefinition:
        """
        Getter for property: ( NXOpen.ContentDefinition) ContentDefinition
         Returns the  NXOpen::ContentDefinition  used to define the context of the subset creation.  
           
                  
         
        """
        pass
    @ContentDefinition.setter
    def ContentDefinition(self, contentDefinition: NXOpen.ContentDefinition):
        """
        Setter for property: ( NXOpen.ContentDefinition) ContentDefinition
         Returns the  NXOpen::ContentDefinition  used to define the context of the subset creation.  
           
                  
         
        """
        pass
    @property
    def Finder(self) -> FindInCollaborativeDesign:
        """
        Getter for property: ( FindInCollaborativeDesign NXOpen.A) Finder
         Returns the  NXOpen::Assemblies::FindInCollaborativeDesign  for use in the context
                    determined by this builder.  
          
                  
         
        """
        pass
    @property
    def Subset(self) -> Subset:
        """
        Getter for property: ( Subset NXOpen.A) Subset
         Returns the  NXOpen::Assemblies::Subset  that we are building.  
          
                  
         
        """
        pass
    @property
    def SubsetConfiguration(self) -> SubsetConfigurationBuilder:
        """
        Getter for property: ( SubsetConfigurationBuilder NXOpen.A) SubsetConfiguration
         Returns the subset configuration.  
             
         
        """
        pass
    @property
    def SubsetDescription(self) -> str:
        """
        Getter for property: (str) SubsetDescription
         Returns the description of the  NXOpen::Assemblies::Subset .  
          
                  
         
        """
        pass
    @SubsetDescription.setter
    def SubsetDescription(self, description: str):
        """
        Setter for property: (str) SubsetDescription
         Returns the description of the  NXOpen::Assemblies::Subset .  
          
                  
         
        """
        pass
    @property
    def SubsetName(self) -> str:
        """
        Getter for property: (str) SubsetName
         Returns the name of the  NXOpen::Assemblies::Subset .  
          
                  
         
        """
        pass
    @SubsetName.setter
    def SubsetName(self, name: str):
        """
        Setter for property: (str) SubsetName
         Returns the name of the  NXOpen::Assemblies::Subset .  
          
                  
         
        """
        pass
    @property
    def SubsetType(self) -> Subset.ContentType:
        """
        Getter for property: ( Subset.ContentType NXOpen.A) SubsetType
         Returns the type of  PLM object used to create subset.  
          
                  
         
        """
        pass
    @property
    def TargetEffectivityTable(self) -> NXOpen.PDM.EffectivityTableBuilder:
        """
        Getter for property: ( NXOpen.PDM.EffectivityTableBuilder) TargetEffectivityTable
         Returns the  NXOpen::PDM::EffectivityTableBuilder  used to edit the target effectivity of the subset.  
          
                  
         
        """
        pass
    @property
    def TargetPartitionList(self) -> PartitionList:
        """
        Getter for property: ( PartitionList NXOpen.A) TargetPartitionList
         Returns the default target  NXOpen::Assemblies::Partition s for design elements created within the subset.  
          
                  
         
        """
        pass
    @property
    def ViewedPartitionScheme(self) -> PartitionScheme:
        """
        Getter for property: ( PartitionScheme NXOpen.A) ViewedPartitionScheme
         Returns the viewed  NXOpen::Assemblies::PartitionScheme  of the subset.  
          
                  
         
        """
        pass
    @ViewedPartitionScheme.setter
    def ViewedPartitionScheme(self, partitionScheme: PartitionScheme):
        """
        Setter for property: ( PartitionScheme NXOpen.A) ViewedPartitionScheme
         Returns the viewed  NXOpen::Assemblies::PartitionScheme  of the subset.  
          
                  
         
        """
        pass
    @property
    def Workset(self) -> ComponentAssembly:
        """
        Getter for property: ( ComponentAssembly NXOpen.A) Workset
         Returns the  NXOpen::Assemblies::ComponentAssembly  within which we are 
                    building an  NXOpen::Assemblies::Subset .  
           
                  
         
        """
        pass
    @property
    def SearchResults() -> SearchResultCollection:
        """
         Returns the  NXOpen::Assemblies::SearchResultCollection  that contains current search results 
                    associated with this subset builder.
                    SearchResults will be populated with the existing subset contents when the builder is created to
                    edit a subset.  These are replaced with results found by the last call to  SubsetBuilder::GenerateResults 
                    after that method is first called. 
                    In addition, the last results from  SubsetBuilder::Finder  are included in this
                    collection.
        """
        pass
    @property
    def Recipe() -> SubsetRecipe:
        """
         Returns the  NXOpen::Assemblies::SubsetRecipe  that contains the  NXOpen::Assemblies::SearchTerm s 
                    used to generate the contents of the subset 
        """
        pass
    def FindObject(self, journalIdentifier: str) -> NXOpen.NXObject:
        """
         Finds the NXOpen.NXObject with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
            
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns objectToBeFound ( NXOpen.NXObject):  Object found, or null if no such object exists .
        """
        pass
    def GenerateResults(self) -> None:
        """
         Generate the search results for the NXOpen.Assemblies.Subset according to the current
                    NXOpen.Assemblies.SubsetRecipe.
                
        """
        pass
    def GetSubsetLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns subset logical objects created by builder.
                
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetSubsets(self) -> List[Subset]:
        """
         Returns subsets held  created by this builder.
                
         Returns subsets ( Subset List[NXOpen): .
        """
        pass
    def UpdateConfigurationContext(self, logicalObject: NXOpen.PDM.LogicalObject) -> None:
        """
         Updates revision rule, effectivity and variant information on subset logical object of subset builder.
                    Input subset logical object must be member of this subset builder.
                
        """
        pass
    def UpdateSubsetConfigurationOfDependentSubset(self) -> None:
        """
         Updates revision rule, effectivity information on the dependent subsets if any.
                    The dependent subset evaluated for the subset represented by the builder.
                
        """
        pass
    def UpdateSubsetTargetPropertiesOfDependentSubset(self) -> None:
        """
         Updates target effectivity information on the dependent subsets if any.
                    The dependent subset evaluated for the subset represented by the builder.
                
        """
        pass
import NXOpen
class SubsetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of subset. """
    def CreateAttributeSearchTermBuilder(self, attributeSearchTerm: AttributeSearchTerm) -> AttributeSearchTermBuilder:
        """
         Creates a NXOpen.Assemblies.AttributeSearchTermBuilder.
                
         Returns attributeSearchTermBuilder ( AttributeSearchTermBuilder NXOpen.A): .
        """
        pass
    def CreateBoxSearchTermBuilder(self, boxSearchTerm: BoxSearchTerm) -> BoxSearchTermBuilder:
        """
         Creates a NXOpen.Assemblies.BoxSearchTermBuilder.
                
         Returns boxSearchTermBuilder ( BoxSearchTermBuilder NXOpen.A): .
        """
        pass
    def CreateMechanicalRoutingSubsetBuilder(self, subsetBuilderTag: SubsetBuilder) -> MechanicalRoutingSubsetBuilder:
        """
         Creates an NXOpen.Assemblies.MechanicalRoutingSubsetBuilder.
                    The SubsetBuilder parameter is for editing of the existing routing subset.
         Returns builder ( MechanicalRoutingSubsetBuilder NXOpen.A): .
        """
        pass
    def CreateMechanicalRoutingSubsetBuilderForSurroundingEdit(self, subsetBuilderTag: SubsetBuilder) -> MechanicalRoutingSubsetBuilder:
        """
         Creates an NXOpen.Assemblies.MechanicalRoutingSubsetBuilder.
                    The SubsetBuilder parameter is for editing of the existing surrounding subset's recipe.
         Returns builder ( MechanicalRoutingSubsetBuilder NXOpen.A): .
        """
        pass
    def CreatePlaneSearchTermBuilder(self, planeSearchTerm: PlaneSearchTerm) -> PlaneSearchTermBuilder:
        """
         Creates a NXOpen.Assemblies.PlaneSearchTermBuilder.
                
         Returns planeSearchTermBuilder ( PlaneSearchTermBuilder NXOpen.A): .
        """
        pass
    def CreatePositioningTaskBuilder(self, positioningTask: PositioningTask) -> PositioningTaskBuilder:
        """
         Creates a NXOpen.Assemblies.PositioningTaskBuilder 
                
         Returns builder ( PositioningTaskBuilder NXOpen.A): .
        """
        pass
    def CreateProximitySearchTermBuilder(self, proximitySearchTerm: ProximitySearchTerm) -> ProximitySearchTermBuilder:
        """
         Creates a NXOpen.Assemblies.ProximitySearchTermBuilder.
                
         Returns proximitySearchTermBuilder ( ProximitySearchTermBuilder NXOpen.A): .
        """
        pass
    def CreateRunContentProximitySearchTermBuilder(self, runContentProximitySearchTerm: RunContentProximitySearchTerm) -> RunContentProximitySearchTermBuilder:
        """
         Creates a NXOpen.Assemblies.RunContentProximitySearchTermBuilder.
                
         Returns runContentProximitySearchTermBuilder ( RunContentProximitySearchTermBuilder NXOpen.A): .
        """
        pass
    def CreateSubsetBuilder(self, subset: Subset) -> SubsetBuilder:
        """
         Creates an NXOpen.Assemblies.SubsetBuilder 
         Returns builder ( SubsetBuilder NXOpen.A): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SubsetConfigurationBuilder(NXOpen.TaggedObject): 
    """   A SubsetConfigurationBuilder is used to edit the revision rule and effectivity used
          to configure the contents of the subset.
    """
    @property
    def Effectivity(self) -> NXOpen.BasicEffectivityBuilder:
        """
        Getter for property: ( NXOpen.BasicEffectivityBuilder) Effectivity
         Returns the effectivity for use in searches for the contents of the  Assemblies::Subset .  
             
         
        """
        pass
    @property
    def RevisionRule(self) -> str:
        """
        Getter for property: (str) RevisionRule
         Returns the revision rule for use in searches for the contents of the  Assemblies::Subset .  
          
                  
         
        """
        pass
    @RevisionRule.setter
    def RevisionRule(self, revisionRule: str):
        """
        Setter for property: (str) RevisionRule
         Returns the revision rule for use in searches for the contents of the  Assemblies::Subset .  
          
                  
         
        """
        pass
    def Commit(self) -> None:
        """
         Commit the subset configuration changes to the Assemblies.SubsetBuilder 
        """
        pass
import NXOpen
class SubsetRecipe(NXOpen.TaggedObjectCollection): 
    """
        A subset recipe is used by a NXOpen.Assemblies.SubsetBuilder to collect NXOpen.Assemblies.SearchTerms.
        The search terms specify the search that defines the contents of a NXOpen.Assemblies.Subset.
    """
    def AddSearchTermBuilder(self, searchTermBuilder: SearchTermBuilder) -> None:
        """
         Add a NXOpen.Assemblies.SearchTermBuilder to the recipe.  When this search term builder
                    is committed the search term will be added to the recipe at the end of the list of search terms.
                
        """
        pass
    def CreateAttributeSearchTerm(self, logicType: SearchTerm.SearchTermLogicType, queryName: str, entries: List[str], values: List[str]) -> AttributeSearchTerm:
        """
         Creates a NXOpen.Assemblies.AttributeSearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns attributeSearchTerm ( AttributeSearchTerm NXOpen.A): .
        """
        pass
    def CreateBoxSearchTerm(self, logicType: SearchTerm.SearchTermLogicType, overlapType: BoxSearchTerm.BoxOverlapLogicType, bottomCorner: NXOpen.Point3d, topCorner: NXOpen.Point3d, trueShapeRefinement: bool) -> BoxSearchTerm:
        """
         Creates a NXOpen.Assemblies.BoxSearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns boxSearchTerm ( BoxSearchTerm NXOpen.A): .
        """
        pass
    def CreateExplicitSearchTerm(self, logicType: SearchTerm.SearchTermLogicType, searchResultElement: SearchResultElement) -> ExplicitSearchTerm:
        """
         Creates a NXOpen.Assemblies.ExplicitSearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns explicitSearchTerm ( ExplicitSearchTerm NXOpen.A): .
        """
        pass
    def CreateExplicitSearchTermGroup(self, logicType: SearchTerm.SearchTermLogicType, searchResultElements: List[SearchResultElement]) -> GroupSearchTerm:
        """
         Creates a NXOpen.Assemblies.GroupSearchTerm of NXOpen.Assemblies.ExplicitSearchTerms and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns groupTerm ( GroupSearchTerm NXOpen.A): .
        """
        pass
    @overload
    def CreatePartitionSearchTerm(self, logicType: SearchTerm.SearchTermLogicType, partition: Partition) -> PartitionSearchTerm:
        """
         Creates a NXOpen.Assemblies.PartitionSearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                    Child partitions of the partition being passed as a parameter are not included in the recipe.
                
         Returns partitionSearchTerm ( PartitionSearchTerm NXOpen.A): .
        """
        pass
    @overload
    def CreatePartitionSearchTermGroup(self, logicType: SearchTerm.SearchTermLogicType, partitions: List[Partition]) -> GroupSearchTerm:
        """
         Creates a NXOpen.Assemblies.GroupSearchTerm of NXOpen.Assemblies.PartitionSearchTerms and
                    adds it to the recipe at the end of the list of search terms.
                    Child partitions of the partitions being passed as a parameter are not included in the recipe.  
                
         Returns groupTerm ( GroupSearchTerm NXOpen.A): .
        """
        pass
    @overload
    def CreatePartitionSearchTermGroup(self, logicType: SearchTerm.SearchTermLogicType, includeChildrenLogic: PartitionSearchTerm.IncludeChildren, partitions: List[Partition]) -> GroupSearchTerm:
        """
         Creates a NXOpen.Assemblies.GroupSearchTerm of NXOpen.Assemblies.PartitionSearchTerms and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns groupTerm ( GroupSearchTerm NXOpen.A): .
        """
        pass
    @overload
    def CreatePartitionSearchTerm(self, logicType: SearchTerm.SearchTermLogicType, includeChildrenLogic: PartitionSearchTerm.IncludeChildren, partition: Partition) -> PartitionSearchTerm:
        """
         Creates a NXOpen.Assemblies.PartitionSearchTerm and
                     adds it to the recipe at the end of the list of search terms.
                
         Returns partitionSearchTerm ( PartitionSearchTerm NXOpen.A): .
        """
        pass
    def CreatePlaneSearchTerm(self, logicType: SearchTerm.SearchTermLogicType, overlapType: PlaneSearchTerm.PlaneOverlapLogicType, normal: NXOpen.Vector3d, displacement: float, pointOnPlane: NXOpen.Point3d, trueShapeRefinement: bool) -> PlaneSearchTerm:
        """
         Creates a NXOpen.Assemblies.PlaneSearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns planeSearchTerm ( PlaneSearchTerm NXOpen.A): .
        """
        pass
    def CreateProximitySearchTerm(self, logicType: SearchTerm.SearchTermLogicType, seeds: List[SearchResultElement], distance: float, trueShapeRefinement: bool) -> ProximitySearchTerm:
        """
         Creates a NXOpen.Assemblies.ProximitySearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns proximitySearchTerm ( ProximitySearchTerm NXOpen.A): .
        """
        pass
    def CreateRunContentProximitySearchTerm(self, logicType: SearchTerm.SearchTermLogicType, seedRunName: str, distance: float, trueShapeRefinement: bool) -> RunContentProximitySearchTerm:
        """
         Creates a NXOpen.Assemblies.RunContentProximitySearchTerm and
                    adds it to the recipe at the end of the list of search terms.
                
         Returns runContentProximitySearchTerm ( RunContentProximitySearchTerm NXOpen.A): .
        """
        pass
    def DeleteSearchTerms(self, searchTerms: List[SearchTerm]) -> None:
        """
         Removes the NXOpen.Assemblies.SearchTerms from the recipe and deletes them.
                
        """
        pass
    def FindObject(self, journalIdentifier: str) -> SearchTerm:
        """
         Finds the NXOpen.Assemblies.SearchTerm with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns searchTerm ( SearchTerm NXOpen.A):  Search term found, or null if no such search term exists.
        """
        pass
    def GetAllSearchOptionSets(self) -> List[str]:
        """
         Gets the internal names of all option sets defined in database.
                
         Returns optionSets (List[str]): .
        """
        pass
    def GetAllSearchOptions(self, optionSet: str) -> List[str]:
        """
         Gets the internal names of all search options from specified option set as defined in database. The option set should be
                    internal name as defined in database.
                    Use NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptionSets to get all the option sets internal name defined in database. 
                
         Returns searchOptions (List[str]): .
        """
        pass
    def GetSearchOptionValue(self, optionSet: str, searchOption: str) -> bool:
        """
         Gets value of specified search option from given option set. Both option set and search option should be internal name as
                    defined in database.
                    Use NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptionSets to get all the option set internal names defined in database. 
                    Use NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptions to get all the search option internal names defined in database. 
                
         Returns optionValue (bool): .
        """
        pass
    def Group(self, logicType: SearchTerm.SearchTermLogicType, searchTerms: List[SearchTerm]) -> None:
        """
         Put the NXOpen.Assemblies.SearchTerms in a new NXOpen.Assemblies.GroupSearchTerm.
                    The group is placed in the recipe at the location of the first search term.
                
        """
        pass
    def MoveDown(self, searchTerm: SearchTerm) -> None:
        """
         Move a NXOpen.Assemblies.SearchTerm down to another location in the recipe.
                
        """
        pass
    def MoveUp(self, searchTerm: SearchTerm) -> None:
        """
         Move a NXOpen.Assemblies.SearchTerm up to another location in the recipe.
                
        """
        pass
    def SetPartitionSearchTermLogic(self, logicType: SearchTerm.SearchTermLogicType, includeChildrenLogic: PartitionSearchTerm.IncludeChildren, searchTerms: List[SearchTerm]) -> None:
        """
         Changes the search term include children logic of each NXOpen.Assemblies.PartitionSearchTerms passed in.
                
        """
        pass
    def SetSearchOptionValue(self, optionSet: str, searchOption: str, optionValue: bool) -> None:
        """
         Sets value of specified search option from given option set. Both option set and search option should be internal name as
                    defined in database.
                    Use NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptionSets to get all the option set internal names defined in database. 
                    Use NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptions to get all the search option internal names defined in database. 
                
        """
        pass
    def SetSearchTermLogic(self, logicType: SearchTerm.SearchTermLogicType, searchTerms: List[SearchTerm]) -> None:
        """
         Changes the search term logic of each NXOpen.Assemblies.SearchTerms passed in.
                
        """
        pass
    def Ungroup(self, searchTerms: List[SearchTerm]) -> None:
        """
         Any NXOpen.Assemblies.GroupSearchTerms in the input search terms will be removed
                    from the recipe.  The members of the group will be re-parented as members of the
                    group's parent.
                
        """
        pass
import NXOpen
import NXOpen.PDM
class Subset(NXOpen.NXObject): 
    """
        A subset is a set of design elements within a collaborative design.
    """
    class ContentType(Enum):
        """
        Members Include: 
         |Public|  Represents a public content subset 
         |Baseline|  Represents a baseline content subset 
         |ChangeNotice|  Represents a change notice content subset

        """
        Public: int
        Baseline: int
        ChangeNotice: int
        @staticmethod
        def ValueOf(value: int) -> Subset.ContentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PartitionViewStyleType(Enum):
        """
        Members Include: 
         |NotSet|  Show no partition view style for subset 
         |Flat|  Show flat partition view style for subset 
         |Hierarchical|  Show hierachical view style for subset 

        """
        NotSet: int
        Flat: int
        Hierarchical: int
        @staticmethod
        def ValueOf(value: int) -> Subset.PartitionViewStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowMultipleTargetPartitions(self) -> bool:
        """
        Getter for property: (bool) AllowMultipleTargetPartitions
         Returns 
                    the allow multiple target partitions property, if set to false (default) only first target partition will be considered
                  
            
         
        """
        pass
    @AllowMultipleTargetPartitions.setter
    def AllowMultipleTargetPartitions(self, allowMultiplePartitions: bool):
        """
        Setter for property: (bool) AllowMultipleTargetPartitions
         Returns 
                    the allow multiple target partitions property, if set to false (default) only first target partition will be considered
                  
            
         
        """
        pass
    @property
    def ComponentInWorkset(self) -> Component:
        """
        Getter for property: ( Component NXOpen.A) ComponentInWorkset
         Returns the  NXOpen::Assemblies::Component  that corresponds to this subset in 
                    the workset  NXOpen::Assemblies::ComponentAssembly .  
          
                  
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of this subset.  
          
                  
         
        """
        pass
    @property
    def DisplayExcludedDesignElements(self) -> bool:
        """
        Getter for property: (bool) DisplayExcludedDesignElements
         Returns the design elements excluded from spatial search to be displayed or not
                  
            
         
        """
        pass
    @DisplayExcludedDesignElements.setter
    def DisplayExcludedDesignElements(self, displayExcluded: bool):
        """
        Setter for property: (bool) DisplayExcludedDesignElements
         Returns the design elements excluded from spatial search to be displayed or not
                  
            
         
        """
        pass
    @property
    def PartitionViewStyle(self) -> Subset.PartitionViewStyleType:
        """
        Getter for property: ( Subset.PartitionViewStyleType NXOpen.A) PartitionViewStyle
         Returns 
                    the partition view style to show.  
          
                  
         
        """
        pass
    @PartitionViewStyle.setter
    def PartitionViewStyle(self, partitionViewStyle: Subset.PartitionViewStyleType):
        """
        Setter for property: ( Subset.PartitionViewStyleType NXOpen.A) PartitionViewStyle
         Returns 
                    the partition view style to show.  
          
                  
         
        """
        pass
    @property
    def ShowSubsetStructure(self) -> bool:
        """
        Getter for property: (bool) ShowSubsetStructure
         Returns 
                    the subset structure to be shown or not.  
          
                  
         
        """
        pass
    @ShowSubsetStructure.setter
    def ShowSubsetStructure(self, showSubsetStructure: bool):
        """
        Setter for property: (bool) ShowSubsetStructure
         Returns 
                    the subset structure to be shown or not.  
          
                  
         
        """
        pass
    @property
    def SubsetType(self) -> Subset.ContentType:
        """
        Getter for property: ( Subset.ContentType NXOpen.A) SubsetType
         Returns the type of plm object used to create subset.  
          
                  
         
        """
        pass
    def AddAllChildrenToSubset(self, reuseDesignElements: List[Component]) -> None:
        """
         Adds all the child components of the selected Reuse Design Element to the owning subset.
                
        """
        pass
    def AddConnectedByElements(self) -> None:
        """
         Add Elements to a subset that reference the existing Design Elements in it by a Connection relation.
                    A typical example will be to add Weld Design Features that reference any of the Design Elements in this subset.
                    The recipe will be modified and explicit include terms will be added for each Element.
                    The modified recipe will be replayed at the end of the operation. 
                    See NXOpen.Assemblies.Subset.AddInterpartParents" 
                
        """
        pass
    def AddDesignElementsToSubset(self, designElements: List[NXOpen.PDM.ModelElementRevision]) -> NXOpen.PartLoadStatus:
        """
         Adds the specified NXOpen.PDM.ModelElementRevisions as members of the subset. 
                    The subset recipe will be edited to include these elements with explicit include terms. 
                    A replay of the entire recipe will not be performed. The specified elements will be appended to the 
                    subset. 
                    See NXOpen.Assemblies.Subset.ReplayRecipe
                
         Returns loadStatus ( NXOpen.PartLoadStatus): .
        """
        pass
    def AddInterpartParents(self) -> None:
        """
         Add sources of interpart relationships (wave links in the subset and Connected To relationships for design features)
                    that are not in the specified subset to the subset recipe. 
                    The recipe will be modified and explicit include terms will be added for each parent.
                    The modified recipe will be replayed at the end of the operation. 
                
        """
        pass
    def AddNewChildrenToSubset(self) -> None:
        """
          If the Reuse Design Elements in the subset contain any new components which were not added
                     to the subset because its owning workset was not the displayed part at the time of creation,
                     then add those new components to the subset now. 
                
        """
        pass
    def CanReplaceContentDefinition(self, contentDefinition: NXOpen.ContentDefinition) -> bool:
        """
         Checks if the NXOpen.ContentDefinition object on the Subset can be replaced with the specified NXOpen.ContentDefinition object.
                
         Returns canUpdate (bool): .
        """
        pass
    def DeleteFromCollaborativeDesign(self, designElement: List[NXOpen.NXObject]) -> None:
        """
         Deletes the design elements from the owning NXOpen.CollaborativeDesign.
                
        """
        pass
    def DeletePositioningTask(self, positioningTask: PositioningTask) -> None:
        """
         Deletes the NXOpen.Assemblies.PositioningTask from this subset.
                
        """
        pass
    def GetAllPositioningTasks(self) -> List[PositioningTask]:
        """
         Gets all NXOpen.Assemblies.PositioningTask 
                    that belong to this subset.
                
         Returns positioningTasks ( PositioningTask List[NXOpen): .
        """
        pass
    def GetDesignElementRevisionMembers(self) -> List[NXOpen.PDM.DesignElementRevision]:
        """
         The NXOpen.PDM.DesignElementRevisions that are members of this subset.
                    Note that this does not include elements that have been loaded only because they contain
                    a NXOpen.PDM.DesignSubordinateRevision that belongs to this subset.
                    See GetDesignElementRevisionParents
                
         Returns designElementRevisions ( NXOpen.PDM.DesignElementRevision Li): .
        """
        pass
    def GetDesignElementRevisionParents(self) -> List[NXOpen.PDM.DesignElementRevision]:
        """
         The NXOpen.PDM.DesignElementRevisions that have been loaded because they contain
                    a NXOpen.PDM.DesignSubordinateRevision that belongs to this subset.
                
         Returns designElementRevisions ( NXOpen.PDM.DesignElementRevision Li): .
        """
        pass
    def GetDesignSubordinateRevisionMembers(self) -> List[NXOpen.PDM.DesignSubordinateRevision]:
        """
         The NXOpen.PDM.DesignSubordinateRevisions that are members of this subset.
                    Note that this does not include elements that have been loaded only because they contain
                    a NXOpen.PDM.DesignSubordinateRevision that belongs to this subset.
                    See GetDesignSubordinateRevisionParents
                
         Returns designSubordinateRevisions ( NXOpen.PDM.DesignSubordinateRevision Li): .
        """
        pass
    def GetDesignSubordinateRevisionParents(self) -> List[NXOpen.PDM.DesignSubordinateRevision]:
        """
         The NXOpen.PDM.DesignSubordinateRevisions that have been loaded because they contain
                    a NXOpen.PDM.DesignSubordinateRevision that belongs to this subset.
                
         Returns designSubordinateRevisions ( NXOpen.PDM.DesignSubordinateRevision Li): .
        """
        pass
    def GetShowFullPartitionStructure(self) -> bool:
        """
         Gets the show full partition structure property.
                    If it is set to false, then the assembly navigator displays only the partitions having some partitionable contents.
                    If the property is set to true (default) and if the NXOpen.Assemblies.Subset.PartitionViewStyleType is set to NXOpen.Assemblies.Subset.PartitionViewStyleType.Hierarchical,
                    then the assembly navigator displays all partition in the viewed partititon scheme.
                    If the NXOpen.Assemblies.Subset.PartitionViewStyleType is NXOpen.Assemblies.Subset.PartitionViewStyleType.Flat
                    or NXOpen.Assemblies.Subset.PartitionViewStyleType.None or 
                    if the viewed partition scheme is not set, then this property is ignored.
                
         Returns showFullPartitionStructure (bool): .
        """
        pass
    def GetTargetPartitionSet(self) -> List[Partition]:
        """
                    Gets the list of array of target partitions that are set on the subsetInstance
                
         Returns partitions ( Partition List[NXOpen): .
        """
        pass
    def HideCollaborativeDesignPreview(self) -> None:
        """
         Hides the preview for the Collaborative Design in the graphics window if it was 
                    already displayed. 
                    See ShowCollaborativeDesignPreview. 
                
        """
        pass
    def IsCollaborativeDesignPreviewDisplayed(self) -> bool:
        """
         Is the preview for the Collaborative Design being displayed in the Graphics window.
                
         Returns isDisplayed (bool): .
        """
        pass
    def RemoveDesignElements(self, designElements: List[NXOpen.NXObject]) -> None:
        """
         Removes the design elements from this subset. This will not delete the design element from the
                    owning NXOpen.CollaborativeDesign.
                
        """
        pass
    def ReplaceContentDefinition(self, contentDefinition: NXOpen.ContentDefinition) -> None:
        """
         Replace the NXOpen.ContentDefinition object on the Subset.
                
        """
        pass
    def ReplayPartitionRecipeInTeamcenter(self, partitions: List[Partition]) -> None:
        """
         Replays the recipe on the partitions in teamcenter. The recipe can be replayed only for dynamic partitions
                    Replaying the recipe on the dynamic partition will update the subset contents based on the updated contents of the partitions
                
        """
        pass
    def ReplayRecipe(self) -> None:
        """
         Replay this subset.  This will perform a search using the current subset recipe 
                    and configuration.  The contents of the subset will be changed accordingly.
                
        """
        pass
    def SetContentDefinition(self, contentDefinition: NXOpen.ContentDefinition) -> None:
        """
         Set a new NXOpen.ContentDefinition object on the Subset.
                
        """
        pass
    def SetShowFullPartitionStructure(self, showFullPartitionStructure: bool) -> None:
        """
         Sets the property on the Subset. This property is used only when the viewed partition scheme is set.
                    If this property value is set to true, all the partitions in the viewed partition scheme will be displayed in the assembly navigator,
                    even if they do not have any contents.
                
        """
        pass
    def SetTargetPartitionSet(self, partitions: List[Partition]) -> None:
        """
                    Sets the list of array of target partitions on the subsetInstance
                
        """
        pass
    def ShowCollaborativeDesignPreview(self) -> bool:
        """
         Displays the preview for the Collaborative Design in the graphics window.
                    The preview is stored as a JT dataset on the Collaborative Design. 
                    Any transformation specific to this subset will also be applied to the preview. 
                    isPreviewAvailable will be false if no JT dataset could be found. 
                    See HideCollaborativeDesignPreview. 
                
         Returns isPreviewAvailable (bool): .
        """
        pass
import NXOpen
class UpdateDesignElementPositionBuilder(NXOpen.Builder): 
    """ Represents the builder class that updates positions of the DE's(ShapeReuse) or Subordinates with override that are out of date.
    """
    @property
    def DesignElementsToUpdatePosition(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) DesignElementsToUpdatePosition
         Returns the objects for update position   
            
         
        """
        pass
import NXOpen
class UpdateStructureBuilder(NXOpen.Builder): 
    """
       Represents a builder NXOpen.Assemblies.UpdateStructureBuilder.
    """
    @property
    def IsUpdateAllLevels(self) -> bool:
        """
        Getter for property: (bool) IsUpdateAllLevels
         Returns the all level toggled on for updating the assembly structure.  
            
         
        """
        pass
    @IsUpdateAllLevels.setter
    def IsUpdateAllLevels(self, isUpdateAllLevels: bool):
        """
        Setter for property: (bool) IsUpdateAllLevels
         Returns the all level toggled on for updating the assembly structure.  
            
         
        """
        pass
    @property
    def NumberOfLevels(self) -> int:
        """
        Getter for property: (int) NumberOfLevels
         Returns the particular selected level for updating the structure.  
            
         
        """
        pass
    @NumberOfLevels.setter
    def NumberOfLevels(self, numberOfLevels: int):
        """
        Setter for property: (int) NumberOfLevels
         Returns the particular selected level for updating the structure.  
            
         
        """
        pass
    @property
    def StructureToUpdate(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) StructureToUpdate
         Returns the component selection of the Assembly structure to Update.  
            
         
        """
        pass
import NXOpen
class WaveQuery(NXOpen.TransientObject): 
    """
        Provides information about the inter-part relations (e.g. WAVE, inter-part
        expressions) in a NX model. The returned XML string contains information from
        parts loaded in the NX session and from published TeamCenter data. The XML
        must be unmarshaled using the Browser_model_schema.xsd.The XML identifiers
        are valid for the life of the session and are used in sequent queries.
        
        For the selected parts, the queries return the first level parent (source) and
        child (target) parts. The object-object relations that comprise a part-part
        relation are included if the information is available. Each query provides a
        context for the meaning of a selected part. For example, the work part is the
        only selected part for GetWorkPartWithPartRelationsXml. However, the method
        GetPartsInContextAssemblyXml considers all the unique parts in the context
        assembly to be selected.
        
        Since the queries also return the first level parent and child parents, these
        non-selected parts could exist only in TeamCenter.
     """
    def AreAssemblyConstraintsDelayed(self) -> bool:
        """
                    Returns true if update of assembly constraints is delayed
                 
         Returns constraints_delayed (bool):  whether constraints are delayed .
        """
        pass
    def Dispose(self) -> None:
        """
                    Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector.
                 
        """
        pass
    def GetAllSelectedPartsXml(self, include_only_with_links: bool) -> str:
        """
                    Gets all the parts in the current selection list in the NX session.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetChildPartRelationsXml(self, parent_part_spec: str, parent_part_identifier: int, walk_all: bool) -> str:
        """
                    Gets the child parts for a given part. The parts are not necessarily fully loaded.
                    The specified part and its children are considered to be "selected" parts.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetChildRevisionOption(self) -> AssembliesChildRevisionOptions:
        """
                    Returns the child revision option
                 
         Returns option_type ( AssembliesChildRevisionOptions NXOpen.A):  the child revision option that is currently set .
        """
        pass
    def GetInSessionPartsXml(self, include_only_with_links: bool) -> str:
        """
                    Gets the parts that are in-session. The parts are not necessarily fully loaded.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetIncludeTeamcenterRelations(self) -> bool:
        """
                    Gets whether or not to include teamcenter relations.
                 
         Returns includeTeamcenterRelations (bool):  whether or not to include teamcenter relations .
        """
        pass
    def GetInterPartLinksXml(self, part_spec: str, part_identifier: int) -> str:
        """
                    Gets the inter-part links and their sources for a given part. The owning part is the
                    "selected" part.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetParentPartRelationsXml(self, child_part_spec: str, child_part_identifier: int, walk_all: bool) -> str:
        """
                    Gets the parent parts for a given part. The parts are not necessarily fully loaded.
                    The specified part and its parents are considered to be "selected" parts.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetPartFeatureDependenciesXml(self, part_spec: str, part_identifier: int) -> str:
        """
                    Gets the feature dependency lists for a fully loaded part.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetPartPreview(self, part_spec: str, part_identifier: int) -> Tuple[int, int, List[int]]:
        """
                    Gets the part's preview image.
                 
         Returns A tuple consisting of (height, width, pixels). 
         - height is: int. height of preview image .
         - width is: int. width of preview image .
         - pixels is: List[int]. the pixels .

        """
        pass
    def GetPartsInContextAssemblyXml(self, include_only_with_links: bool) -> str:
        """
                    Gets the parts that are in the context assembly. The parts are not necessarily fully loaded.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetProductInterfacesXml(self, part_spec: str, part_identifier: int) -> str:
        """
                    Gets the product interfaces and their references for a given part. The owning part is the
                    "selected" part.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetQueryProductInterfaces(self) -> bool:
        """
                    Gets whether or not to query product interaces from TC.
                 
         Returns queryProductInterfaces (bool):  whether or not to query product interaces from TC .
        """
        pass
    def GetReferencesToProductInterfaceXml(self, owning_part_spec: str, owning_part_identifier: int, prodint_handle: str, prodint_identifier: int) -> str:
        """
                    Gets a product interface's referencing objects. The owning part is the "selected" part.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    @overload
    def GetSpecifiedPartRelationsXml(self, part_specs: List[str], part_identifiers: List[int], include_only_with_links: bool) -> str:
        """
                    Gets information about the specified parts. The parts are not necessarily fully loaded.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    @overload
    def GetSpecifiedPartRelationsXml(self, part_specs: List[str], part_identifiers: List[int], include_only_with_links: bool, forceQuery: bool) -> str:
        """
                    Gets information about the specified parts. The parts are not necessarily fully loaded.
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def GetWorkPartWithPartRelationsXml(self) -> str:
        """
                    Gets the current work part. 
                 
         Returns xml_stream (str):  the XML .
        """
        pass
    def HandleApplicationEvents(self, event_type: AssembliesEventTypes, event_description: str, entity_specs: List[str], entity_identifiers: List[int]) -> int:
        """
                    Provides application (e.g. the graphical browser) event processing by NX.
                    Some events refer to part level actions while others refer to part object level actions.
                 
         Returns return_status (int):  the return status of this method .
        """
        pass
    def SetChildRevisionOption(self, option_type: AssembliesChildRevisionOptions) -> None:
        """
                    Specifies what child revisions to fetch from Teamcenter
                 
        """
        pass
    def SetIncludeTeamcenterRelations(self, includeTeamcenterRelations: bool) -> None:
        """
                    Sets whether or not to include teamcenter relations.
                 
        """
        pass
    def SetQueryProductInterfaces(self, queryProductInterfaces: bool) -> None:
        """
                    Sets whether or not to query product interaces from TC.
                 
        """
        pass
