from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class ActiveSetScope(Enum):
    """
    Members Include: 
     |NoMembers| 
     |SelectMembers| 
     |AllMembers| 

    """
    NoMembers: int
    SelectMembers: int
    AllMembers: int
    @staticmethod
    def ValueOf(value: int) -> ActiveSetScope:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AssemblyCreationSettingsBuilder(NXOpen.TaggedObject): 
    """
     Represents a NXOpen.Layout2d.AssemblyCreationSettingsBuilder
    """
    @property
    def AutomaticallyStartModelingApplication(self) -> bool:
        """
        Getter for property: (bool) AutomaticallyStartModelingApplication
         Returns  the settings todetermines whether or not automatically start modeling application  
            
         
        """
        pass
    @AutomaticallyStartModelingApplication.setter
    def AutomaticallyStartModelingApplication(self, automaticallyStartModelingApplication: bool):
        """
        Setter for property: (bool) AutomaticallyStartModelingApplication
         Returns  the settings todetermines whether or not automatically start modeling application  
            
         
        """
        pass
    @property
    def Transfer2dComponentAnnotation(self) -> bool:
        """
        Getter for property: (bool) Transfer2dComponentAnnotation
         Returns the settings to determines whether or not transfer 2d component annotation  
            
         
        """
        pass
    @Transfer2dComponentAnnotation.setter
    def Transfer2dComponentAnnotation(self, transfer2dComponentAnnotation: bool):
        """
        Setter for property: (bool) Transfer2dComponentAnnotation
         Returns the settings to determines whether or not transfer 2d component annotation  
            
         
        """
        pass
    @property
    def TransferTopLevelSketchAnnotation(self) -> bool:
        """
        Getter for property: (bool) TransferTopLevelSketchAnnotation
         Returns the settings to determines whether or not transfer top level sketch annotation   
            
         
        """
        pass
    @TransferTopLevelSketchAnnotation.setter
    def TransferTopLevelSketchAnnotation(self, transferTopLevelSketchAnnotation: bool):
        """
        Setter for property: (bool) TransferTopLevelSketchAnnotation
         Returns the settings to determines whether or not transfer top level sketch annotation   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
import NXOpen
class AssemblyFromLayout2dBuilder(NXOpen.Builder): 
    """ Represents a Builder for create assembly from Layout functionality which will create a
       new assembly from the selected Layout """
    @property
    def AssemblyPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) AssemblyPart
         Returns the destination part for the Layout assembly   
            
         
        """
        pass
    @AssemblyPart.setter
    def AssemblyPart(self, assemblyPart: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) AssemblyPart
         Returns the destination part for the Layout assembly   
            
         
        """
        pass
    @property
    def Layout2dObject(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) Layout2dObject
         Returns the select Layout object to create assembly   
            
         
        """
        pass
    @property
    def Settings(self) -> AssemblyCreationSettingsBuilder:
        """
        Getter for property: ( AssemblyCreationSettingsBuilder NXOpen.) Settings
         Returns the settings of the assembly creation   
            
         
        """
        pass
import NXOpen
class AssemblyRelation(NXOpen.NXObject): 
    """ Represents Assembly::Relation object"""
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns a flag indicating associativity state   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns a flag indicating associativity state   
            
         
        """
        pass
    @property
    def PrototypeFileSpec(self) -> str:
        """
        Getter for property: (str) PrototypeFileSpec
         Returns the prototype file spec   
            
         
        """
        pass
    @PrototypeFileSpec.setter
    def PrototypeFileSpec(self, fileSpec: str):
        """
        Setter for property: (str) PrototypeFileSpec
         Returns the prototype file spec   
            
         
        """
        pass
    @property
    def SyncContent(self) -> bool:
        """
        Getter for property: (bool) SyncContent
         Returns a flag indicating whether the prototype content will be syncronized   
            
         
        """
        pass
    @SyncContent.setter
    def SyncContent(self, syncContent: bool):
        """
        Setter for property: (bool) SyncContent
         Returns a flag indicating whether the prototype content will be syncronized   
            
         
        """
        pass
    @property
    def SyncStructure(self) -> bool:
        """
        Getter for property: (bool) SyncStructure
         Returns a flag indicating whether the prototype structure will be syncronized   
            
         
        """
        pass
    @SyncStructure.setter
    def SyncStructure(self, syncStructure: bool):
        """
        Setter for property: (bool) SyncStructure
         Returns a flag indicating whether the prototype structure will be syncronized   
            
         
        """
        pass
    def GetPrototypeInferred(self) -> bool:
        """
         Returns the flag indicating whether the prototype is inferred from 2D component 
         Returns inferred (bool): .
        """
        pass
import NXOpen
class AssociativeAssemblyBuilder(NXOpen.Builder): 
    """ Represents a Builder for Layout associative assembly """
    class UpdateDirection(Enum):
        """
        Members Include: 
         |LayoutToAssembly|  Update 3D model from 2D 
         |AssemblyToLayout|  Update 2D model from 3D 

        """
        LayoutToAssembly: int
        AssemblyToLayout: int
        @staticmethod
        def ValueOf(value: int) -> AssociativeAssemblyBuilder.UpdateDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Direction(self) -> AssociativeAssemblyBuilder.UpdateDirection:
        """
        Getter for property: ( AssociativeAssemblyBuilder.UpdateDirection NXOpen.) Direction
         Returns the update direction   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: AssociativeAssemblyBuilder.UpdateDirection):
        """
        Setter for property: ( AssociativeAssemblyBuilder.UpdateDirection NXOpen.) Direction
         Returns the update direction   
            
         
        """
        pass
    def GetAssemblyRelations(self) -> List[AssemblyRelation]:
        """
         Gets the assembly relations 
         Returns relations ( AssemblyRelation List[NXOpe): .
        """
        pass
    def ResetAssemblyRelations(self) -> None:
        """
         Resets the assembly relations to initial state 
        """
        pass
import NXOpen
class ComponentActiveSetBuilder(NXOpen.Builder): 
    """ Represents a Builder to edit 2D component active members set. """
    @property
    def ActiveSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ActiveSet
         Returns the select members of active set   
            
         
        """
        pass
    @property
    def ActiveSetScope(self) -> ActiveSetScope:
        """
        Getter for property: ( ActiveSetScope NXOpen.) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    @ActiveSetScope.setter
    def ActiveSetScope(self, scope: ActiveSetScope):
        """
        Setter for property: ( ActiveSetScope NXOpen.) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    def IsValidActiveSetMember(self, objectTag: NXOpen.DisplayableObject) -> bool:
        """
         Verifies whether specified object can be an active member 
         Returns isValid (bool): .
        """
        pass
import NXOpen
class ComponentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Layout2d.Components.   """
    @property
    def OrderManagers() -> OrderManager:
        """
         Returns the OrderManager for part 
        """
        pass
    def CreateAssemblyFromLayout2dBuilder(self) -> AssemblyFromLayout2dBuilder:
        """
         Creates a NXOpen.Layout2d.AssemblyFromLayout2dBuilder that can create assembly from  
                   the selected layout
                
         Returns builder ( AssemblyFromLayout2dBuilder NXOpen.): .
        """
        pass
    def CreateAssociativeAssemblyBuilder(self) -> AssociativeAssemblyBuilder:
        """
         Creates a NXOpen.Layout2d.AssociativeAssemblyBuilder 
         Returns builder ( AssociativeAssemblyBuilder NXOpen.): .
        """
        pass
    def CreateComponentActiveSetBuilder(self) -> ComponentActiveSetBuilder:
        """
         Creates a NXOpen.Layout2d.ComponentActiveSetBuilder 
         Returns builder ( ComponentActiveSetBuilder NXOpen.): .
        """
        pass
    def CreateComponentFrom3dBuilder(self, myView: NXOpen.View) -> CreateComponentFrom3DBuilder:
        """
         Creates a NXOpen.Layout2d.CreateComponentFrom3DBuilder that can create assembly from
                   the selected layout
                
         Returns builder ( CreateComponentFrom3DBuilder NXOpen.): .
        """
        pass
    def CreateDefineComponentAnchorPointBuilder(self) -> DefineComponentAnchorPointBuilder:
        """
         Creates a NXOpen.Layout2d.DefineComponentAnchorPointBuilder that can define the Anchor Point location of a
                   2D Component
                
         Returns builder ( DefineComponentAnchorPointBuilder NXOpen.): .
        """
        pass
    def CreateDefineComponentBuilder(self, component: Component) -> DefineComponentBuilder:
        """
         Creates a NXOpen.Layout2d.DefineComponentBuilder that can create a fully defined 2D 
                    Component with specified content, anchor point, name and reuse library destination folder.
                
         Returns builder ( DefineComponentBuilder NXOpen.): .
        """
        pass
    def CreateExportComponentHierarchyBuilder(self) -> ExportComponentHierarchyBuilder:
        """
         Creates a NXOpen.Layout2d.ExportComponentHierarchyBuilder 
         Returns builder ( ExportComponentHierarchyBuilder NXOpen.): .
        """
        pass
    def CreateInheritDisplayAttributesBuilder(self) -> InheritDisplayAttributesBuilder:
        """
         Creates a NXOpen.Layout2d.InheritDisplayAttributesBuilder 
         Returns builder ( InheritDisplayAttributesBuilder NXOpen.): .
        """
        pass
    def CreateInsertComponentBuilder(self) -> InsertComponentBuilder:
        """
         Creates a NXOpen.Layout2d.InsertComponentBuilder that inserts a 2D Component instance in the active
                   sketch.
                
         Returns builder ( InsertComponentBuilder NXOpen.): .
        """
        pass
    def CreateMakeComponentUniqueBuilder(self) -> MakeComponentUniqueBuilder:
        """
         Creates a NXOpen.Layout2d.MakeComponentUniqueBuilder that can create definition
                   for the selected 2D Component instance
                
         Returns builder ( MakeComponentUniqueBuilder NXOpen.): .
        """
        pass
    def CreateNewComponentBuilder(self) -> NewComponentBuilder:
        """
         Creates a NXOpen.Layout2d.NewComponentBuilder that creates an empty 2D Component instance and stores its
                   definition in local 2D Component folder
                
         Returns builder ( NewComponentBuilder NXOpen.): .
        """
        pass
    def CreatePublishComponentBuilder(self) -> PublishComponentBuilder:
        """
         Creates a NXOpen.Layout2d.PublishComponentBuilder that can export local definitions into external storage locations
                
         Returns builder ( PublishComponentBuilder NXOpen.): .
        """
        pass
    def CreateReparentComponentBuilder(self) -> ReparentComponentBuilder:
        """
         Creates a NXOpen.Layout2d.ReplaceComponentBuilder that can reparent the selected 2D Component
                   instance with another 2D Component or sketch 
         Returns builder ( ReparentComponentBuilder NXOpen.): .
        """
        pass
    def CreateReplaceComponentBuilder(self) -> ReplaceComponentBuilder:
        """
         Creates a NXOpen.Layout2d.ReplaceComponentBuilder that can replace the selected 2D Component
                    instance with another 2D Component definition
                
         Returns builder ( ReplaceComponentBuilder NXOpen.): .
        """
        pass
    def CreateSmashComponentBuilder(self) -> SmashComponentBuilder:
        """
         Creates a NXOpen.Layout2d.SmashComponentBuilder that can smash the selected 
                   2D Component instance
                
         Returns builder ( SmashComponentBuilder NXOpen.): .
        """
        pass
    def DeleteComponents(self, components: List[Component]) -> None:
        """
         Deletes a list of 2D Components
        """
        pass
    def FindObject(self, journal_identifier: str) -> Component:
        """
         Finds the  NXOpen.Layout2d.Component  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( Component NXOpen.):  2D Component with this identifier .
        """
        pass
    def IsComponentMember(self, disObject: NXOpen.DisplayableObject) -> bool:
        """
         Verify if the object belong to this component 
         Returns isMember (bool):  true if the object is component member .
        """
        pass
    def UpdateComponentHierarchy(self, components: List[Component]) -> None:
        """
         Updates 2D Components and propagates the changes to the hierarchy in given layout 
        """
        pass
    def UpdateComponents(self, components: List[Component]) -> None:
        """
         Updates 2D Components without propagating the changes to the hierarchy in given layout 
        """
        pass
import NXOpen
class ComponentDefinitionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Layout2d.ComponentDefinition objects."""
    def Delete(self, location: Layout2dDefinitionLocation, definitionPath: str) -> None:
        """
         Deletes definition
        """
        pass
    def FindObject(self, sid: str) -> ComponentDefinition:
        """
          Finds the  NXOpen.Layout2d.ComponentDefinition  with the given sid. 
                     An exception will be thrown if no object can be found with the given sid. 
                     This method can only be used to find Local definitions 
         Returns folder ( ComponentDefinition NXOpen.): .
        """
        pass
    def RefreshAllReferences(self) -> None:
        """
          Refreshes all definition references in part to obtain the actual out-of-date status of components 
        """
        pass
    def Rename(self, location: Layout2dDefinitionLocation, definitionPath: str, newName: str) -> None:
        """
         Renames definition
        """
        pass
    def SetAutomaticPreview(self, location: Layout2dDefinitionLocation, definitionPath: str, isAutomatic: bool) -> None:
        """
          Sets the automatic preview mode of definition with the given path 
        """
        pass
    def Update(self, location: Layout2dDefinitionLocation, definitionPath: str) -> None:
        """
          Updates definition with the given path 
        """
        pass
    def UpdateImage(self, location: Layout2dDefinitionLocation, definitionPath: str, imagePath: str) -> None:
        """
         Updates definition preview 
        """
        pass
import NXOpen
class ComponentDefinition(NXOpen.NXObject): 
    """ Represents a component definition. The definition contains sketch curves, sketch dimensions
        and drafting annotations representing a two dimensional reusable sketch component."""
    def Delete(self, definitionPath: str) -> None:
        """
         Deletes definition
        """
        pass
    def GetMembers(self, memberType: Layout2dComponentMemberType) -> List[NXOpen.DisplayableObject]:
        """
         Returns an array of specified members in this component definition
         Returns members ( NXOpen.DisplayableObject Li): .
        """
        pass
    def Rename(self, definitionPath: str, newName: str) -> None:
        """
         Renames definition
        """
        pass
    def UpdateImage(self, definitionPath: str, imagePath: str) -> None:
        """
         Updates definition preview 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.PDM
class ComponentNameBuilder(NXOpen.TaggedObject): 
    """ This class is used to construct the component name and part file name block, if it is in
        manage mode, we also have item number, item revision and item name . """
    @property
    def Location(self) -> Layout2dDefinitionLocation:
        """
        Getter for property: ( Layout2dDefinitionLocation NXOpen.) Location
         Returns the location type of the component indicating local, native or team center    
            
         
        """
        pass
    @Location.setter
    def Location(self, location: Layout2dDefinitionLocation):
        """
        Setter for property: ( Layout2dDefinitionLocation NXOpen.) Location
         Returns the location type of the component indicating local, native or team center    
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the JA method support for accessing and setting Component Name value,
                    NOTE: Client must free the returned TEXT_p_t with TEXT_free
                   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the JA method support for accessing and setting Component Name value,
                    NOTE: Client must free the returned TEXT_p_t with TEXT_free
                   
            
         
        """
        pass
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the JA method support for accessing and setting Component part file mame value,
                    NOTE: Client must free the returned TEXT_p_t with TEXT_free   
            
         
        """
        pass
    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the JA method support for accessing and setting Component part file mame value,
                    NOTE: Client must free the returned TEXT_p_t with TEXT_free   
            
         
        """
        pass
    def SetPartOperationBuilder(self, partOperationBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Sets NXOpen.PDM.PartOperationCreateBuilder 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ComponentSettingsBlockBuilder(NXOpen.TaggedObject): 
    """ Represents the Component Settings Button (Layout2d.ComponentSettingsBlockBuilder)
    """
    @property
    def ComponentSettings(self) -> ComponentSettingsBuilder:
        """
        Getter for property: ( ComponentSettingsBuilder NXOpen.) ComponentSettings
         Returns the Component settings builder which stores the component settings   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObject(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ComponentSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Layout2d.ComponentSettingsBuilder
    This builder stores the information of the 2D Component settings
    """
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the flag to do automatic update or not   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, toggle: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the flag to do automatic update or not   
            
         
        """
        pass
    @property
    def KeepEditedPartsOpen(self) -> bool:
        """
        Getter for property: (bool) KeepEditedPartsOpen
         Returns the flag indicating whether to keep edited parts open or not   
            
         
        """
        pass
    @KeepEditedPartsOpen.setter
    def KeepEditedPartsOpen(self, toggle: bool):
        """
        Setter for property: (bool) KeepEditedPartsOpen
         Returns the flag indicating whether to keep edited parts open or not   
            
         
        """
        pass
    @property
    def ShowAnnotations(self) -> bool:
        """
        Getter for property: (bool) ShowAnnotations
         Returns the flag to show annotations or not   
            
         
        """
        pass
    @ShowAnnotations.setter
    def ShowAnnotations(self, toggle: bool):
        """
        Setter for property: (bool) ShowAnnotations
         Returns the flag to show annotations or not   
            
         
        """
        pass
    @property
    def ShowDimensions(self) -> bool:
        """
        Getter for property: (bool) ShowDimensions
         Returns the flag to show dimensions or not   
            
         
        """
        pass
    @ShowDimensions.setter
    def ShowDimensions(self, toggle: bool):
        """
        Setter for property: (bool) ShowDimensions
         Returns the flag to show dimensions or not   
            
         
        """
        pass
    @property
    def ShowReferenceGeometry(self) -> bool:
        """
        Getter for property: (bool) ShowReferenceGeometry
         Returns the flag to show reference geometry or not   
            
         
        """
        pass
    @ShowReferenceGeometry.setter
    def ShowReferenceGeometry(self, toggle: bool):
        """
        Setter for property: (bool) ShowReferenceGeometry
         Returns the flag to show reference geometry or not   
            
         
        """
        pass
import NXOpen
class Component(NXOpen.DisplayableObject): 
    """ Represents the Component object. """
    @property
    def IsActive(self) -> bool:
        """
        Getter for property: (bool) IsActive
         Returns the active state of 2D Component.  
             
         
        """
        pass
    @property
    def LockUpdateStatus(self) -> bool:
        """
        Getter for property: (bool) LockUpdateStatus
         Returns the lock update status of 2D Component.  
            
         
        """
        pass
    @LockUpdateStatus.setter
    def LockUpdateStatus(self, lock: bool):
        """
        Setter for property: (bool) LockUpdateStatus
         Returns the lock update status of 2D Component.  
            
         
        """
        pass
    @property
    def UpgradeUponActivation(self) -> bool:
        """
        Getter for property: (bool) UpgradeUponActivation
         Returns the flag which causes the component to be upgraded upon activation  
            
         
        """
        pass
    @UpgradeUponActivation.setter
    def UpgradeUponActivation(self, upgrade: bool):
        """
        Setter for property: (bool) UpgradeUponActivation
         Returns the flag which causes the component to be upgraded upon activation  
            
         
        """
        pass
    def Activate(self) -> None:
        """
         Activates the component. 
        """
        pass
    def ActivateInIsolation(self) -> NXOpen.Sketch:
        """
         Activates the component while in edit in isolation task environment and
                    returns component internal sketch 
         Returns internalSketch ( NXOpen.Sketch): .
        """
        pass
    def AddExistingCurves(self, curves: List[NXOpen.DisplayableObject]) -> None:
        """
         Add an array of specified curves from top level sketch to this component 
        """
        pass
    def Deactivate(self) -> None:
        """
         Deactivates the component. 
        """
        pass
    def ExitActivate(self) -> None:
        """
         Exits the component active status without committing the changes. 
        """
        pass
    def GetAnchorPoint(self) -> Tuple[bool, NXOpen.Point3d]:
        """
         Gets the anchor point of a component if it exist 
         Returns A tuple consisting of (isAnchorPointExist, anchorPoint). 
         - isAnchorPointExist is: bool.
         - anchorPoint is:  NXOpen.Point3d.

        """
        pass
    def GetDefinition(self) -> ComponentDefinition:
        """
         Gets the component definition of a component 
         Returns definition ( ComponentDefinition NXOpen.): .
        """
        pass
    def GetDefinitionLocation(self) -> Layout2dDefinitionLocation:
        """
         Gets the location of the component definition 
         Returns location ( Layout2dDefinitionLocation NXOpen.): .
        """
        pass
    def GetDefinitionName(self) -> str:
        """
         Gets the component definition name of a component 
         Returns definitionName (str): .
        """
        pass
    def GetDefinitionPath(self) -> str:
        """
         Gets the path of the component definition 
         Returns definitionPath (str): .
        """
        pass
    def GetMembers(self, memberType: Layout2dComponentMemberType) -> List[NXOpen.DisplayableObject]:
        """
         Returns an array of specified members in this component 
         Returns members ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetTransform(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Vector3d]:
        """
         Gets the absolute transform of a component, as a rotation matrix and a translation vector
         Returns A tuple consisting of (rotation, translation). 
         - rotation is:  NXOpen.Matrix3x3.
         - translation is:  NXOpen.Vector3d.

        """
        pass
    def RenewSketch(self) -> None:
        """
         Renews component sketch to the latest solver version and updates component hierarchy for the changes to take effect. 
        """
        pass
    def SetTransform(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Vector3d) -> None:
        """
         Sets the absolute transform on a component, given a rotation matrix and a translation vector
        """
        pass
    def Transform(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Vector3d) -> None:
        """
         Transforms the component given a rotation matrix and a translation vector
        """
        pass
    def Update(self) -> None:
        """
         Updates the component and all of its sub components. 
        """
        pass
import NXOpen
class ConvertLayoutToSheetBuilder(NXOpen.Builder): 
    """ Represents a Builder for converting Layout to drawing sheet """
    class SheetProjectionAngleType(Enum):
        """
        Members Include: 
         |First|  first angle projection 
         |Third|  third angle projection 

        """
        First: int
        Third: int
        @staticmethod
        def ValueOf(value: int) -> ConvertLayoutToSheetBuilder.SheetProjectionAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the drawing sheet to be created   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the drawing sheet to be created   
            
         
        """
        pass
    @property
    def Number(self) -> str:
        """
        Getter for property: (str) Number
         Returns the number of the drawing sheet to be created   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: str):
        """
        Setter for property: (str) Number
         Returns the number of the drawing sheet to be created   
            
         
        """
        pass
    @property
    def ProjectionAngleType(self) -> ConvertLayoutToSheetBuilder.SheetProjectionAngleType:
        """
        Getter for property: ( ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.) ProjectionAngleType
         Returns the sheet projection angle option   
            
         
        """
        pass
    @ProjectionAngleType.setter
    def ProjectionAngleType(self, type: ConvertLayoutToSheetBuilder.SheetProjectionAngleType):
        """
        Setter for property: ( ConvertLayoutToSheetBuilder.SheetProjectionAngleType NXOpen.) ProjectionAngleType
         Returns the sheet projection angle option   
            
         
        """
        pass
    @property
    def Revision(self) -> str:
        """
        Getter for property: (str) Revision
         Returns the revision of the drawing sheet to be created   
            
         
        """
        pass
    @Revision.setter
    def Revision(self, revision: str):
        """
        Setter for property: (str) Revision
         Returns the revision of the drawing sheet to be created   
            
         
        """
        pass
    @property
    def SecondaryNumber(self) -> str:
        """
        Getter for property: (str) SecondaryNumber
         Returns the secondary number of the drawing sheet to be created   
            
         
        """
        pass
    @SecondaryNumber.setter
    def SecondaryNumber(self, secondaryNumber: str):
        """
        Setter for property: (str) SecondaryNumber
         Returns the secondary number of the drawing sheet to be created   
            
         
        """
        pass
    @property
    def SelectLayoutSheetView(self) -> NXOpen.SelectView:
        """
        Getter for property: ( NXOpen.SelectView) SelectLayoutSheetView
         Returns the select layout sheet view to convert  
            
         
        """
        pass
    def GetScale(self) -> Tuple[float, float]:
        """
         Gets the sheet scale 
         Returns A tuple consisting of (numerator, denominator). 
         - numerator is: float. the scale numerator .
         - denominator is: float. the scale denominator .

        """
        pass
    def SetScale(self, numerator: float, denominator: float) -> None:
        """
         Sets the sheet scale 
        """
        pass
import NXOpen
class ConvertSheetToLayoutBuilder(LayoutDrawingSheetBuilder): 
    """ Represents a Builder for converting a drawing sheet to Layout """
    @property
    def SelectSheetView(self) -> NXOpen.SelectView:
        """
        Getter for property: ( NXOpen.SelectView) SelectSheetView
         Returns the select drawing sheet to convert  
            
         
        """
        pass
import NXOpen
import NXOpen.Display
class CreateComponentFrom3DBuilder(NXOpen.Display.DynamicSectionBuilder): 
    """ Represents a Builder that creates NXOpen.Layout2d.Component from Assembly"""
    class CreateMethod(Enum):
        """
        Members Include: 
         |Section|  use section 
         |Plane|  use plane 

        """
        Section: int
        Plane: int
        @staticmethod
        def ValueOf(value: int) -> CreateComponentFrom3DBuilder.CreateMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
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
    def ComponentName(self, name: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
    @property
    def Method(self) -> CreateComponentFrom3DBuilder.CreateMethod:
        """
        Getter for property: ( CreateComponentFrom3DBuilder.CreateMethod NXOpen.) Method
         Returns the method to utilize in create Component from 3D  
            
         
        """
        pass
    @Method.setter
    def Method(self, method: CreateComponentFrom3DBuilder.CreateMethod):
        """
        Setter for property: ( CreateComponentFrom3DBuilder.CreateMethod NXOpen.) Method
         Returns the method to utilize in create Component from 3D  
            
         
        """
        pass
    @property
    def SelectedObjects(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectedObjects
         Returns the selected objects of Solid body or Component type   
            
         
        """
        pass
    @property
    def Settings(self) -> CreateComponentFrom3DSettingsBuilder:
        """
        Getter for property: ( CreateComponentFrom3DSettingsBuilder NXOpen.) Settings
         Returns the settings of create component from 3D   
            
         
        """
        pass
    @Settings.setter
    def Settings(self, settings: CreateComponentFrom3DSettingsBuilder):
        """
        Setter for property: ( CreateComponentFrom3DSettingsBuilder NXOpen.) Settings
         Returns the settings of create component from 3D   
            
         
        """
        pass
    def GetProjectionPlane(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
         Gets the projection plane origin and orientation matrix 
         Returns A tuple consisting of (origin, orientation). 
         - origin is:  NXOpen.Point3d.
         - orientation is:  NXOpen.Matrix3x3.

        """
        pass
    def GetSourcePart(self) -> NXOpen.Part:
        """
         Returns the current source part 
         Returns part ( NXOpen.Part): .
        """
        pass
    def SetProjectionPlane(self, origin: NXOpen.Point3d, yAxis: NXOpen.Vector3d, zAxis: NXOpen.Vector3d) -> None:
        """
         Sets the projection plane specified by origin, y and z vectors, where z is the plane normal and
                    the x vector is computed.
        """
        pass
    def SetSourcePart(self, part: NXOpen.Part) -> None:
        """
         Sets the source part to create 2D component from. The part may be the current work part or other part loaded in session. 
        """
        pass
import NXOpen
import NXOpen.Display
import NXOpen.GeometricUtilities
class CreateComponentFrom3DSettingsBuilder(NXOpen.TaggedObject): 
    """
     Represents a NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder
    """
    @property
    def ActiveSetScope(self) -> ActiveSetScope:
        """
        Getter for property: ( ActiveSetScope NXOpen.) ActiveSetScope
         Returns the option whether each 2D component will be created with no active set or an active set for the entire 2D component.  
             
         
        """
        pass
    @ActiveSetScope.setter
    def ActiveSetScope(self, scope: ActiveSetScope):
        """
        Setter for property: ( ActiveSetScope NXOpen.) ActiveSetScope
         Returns the option whether each 2D component will be created with no active set or an active set for the entire 2D component.  
             
         
        """
        pass
    @property
    def AutomaticallyStartInsert2DComponentCommand(self) -> bool:
        """
        Getter for property: (bool) AutomaticallyStartInsert2DComponentCommand
         Returns the settings to determines whether or not automatically start insert 2D component command.  
            
         
        """
        pass
    @AutomaticallyStartInsert2DComponentCommand.setter
    def AutomaticallyStartInsert2DComponentCommand(self, automaticallyStartInsert2DComponentCommand: bool):
        """
        Setter for property: (bool) AutomaticallyStartInsert2DComponentCommand
         Returns the settings to determines whether or not automatically start insert 2D component command.  
            
         
        """
        pass
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns  the settings to specifies the 2D component curves color.  
            
         
        """
        pass
    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns  the settings to specifies the 2D component curves color.  
            
         
        """
        pass
    @property
    def ColorOption(self) -> NXOpen.Display.DynamicSectionTypes.CurveColorOption:
        """
        Getter for property: ( NXOpen.Display.DynamicSectionTypes.CurveColorOption) ColorOption
         Returns  the settings to specifies how the color of the 2D component curves is defined.  
            
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: NXOpen.Display.DynamicSectionTypes.CurveColorOption):
        """
        Setter for property: ( NXOpen.Display.DynamicSectionTypes.CurveColorOption) ColorOption
         Returns  the settings to specifies how the color of the 2D component curves is defined.  
            
         
        """
        pass
    @property
    def CreateSingle2DComponentDefinition(self) -> bool:
        """
        Getter for property: (bool) CreateSingle2DComponentDefinition
         Returns the settings to determines whether or not create single 2D component definition.  
            
         
        """
        pass
    @CreateSingle2DComponentDefinition.setter
    def CreateSingle2DComponentDefinition(self, createSingle2DComponentDefinition: bool):
        """
        Setter for property: (bool) CreateSingle2DComponentDefinition
         Returns the settings to determines whether or not create single 2D component definition.  
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
import NXOpen
class DefineComponentAnchorPointBuilder(NXOpen.Builder): 
    """ Represents a Builder for Define Component Anchor Point functionality which will define the anchor
       point location of a 2D Component instance """
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point of a 2D Component   
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point of a 2D Component   
            
         
        """
        pass
import NXOpen
import NXOpen.Gateway
class DefineComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Define 2D component functionality which will define
       a 2D Component and stores its definition in the Reuse Library             """
    @property
    def ActiveSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ActiveSet
         Returns the select members of active set   
            
         
        """
        pass
    @property
    def ActiveSetScope(self) -> ActiveSetScope:
        """
        Getter for property: ( ActiveSetScope NXOpen.) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    @ActiveSetScope.setter
    def ActiveSetScope(self, scope: ActiveSetScope):
        """
        Setter for property: ( ActiveSetScope NXOpen.) ActiveSetScope
         Returns the active members scope   
            
         
        """
        pass
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point to define the 2D Component  
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point to define the 2D Component  
            
         
        """
        pass
    @property
    def ComponentName(self) -> ComponentNameBuilder:
        """
        Getter for property: ( ComponentNameBuilder NXOpen.) ComponentName
         Returns the 2D Component Name defines the name for the new created definition   
            
         
        """
        pass
    @property
    def Contents(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Contents
         Returns the select objects to create a 2D Component definition  
            
         
        """
        pass
    @property
    def ImageCapture(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: ( NXOpen.Gateway.ImageCaptureBuilder) ImageCapture
         Returns the image capture builder used to create an image for the definition   
            
         
        """
        pass
    @property
    def ImageName(self) -> str:
        """
        Getter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    @ImageName.setter
    def ImageName(self, imageName: str):
        """
        Setter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    def IsValidActiveSetMember(self, objectValue: NXOpen.DisplayableObject) -> bool:
        """
         Verifies whether specified object can be an active member 
         Returns result (bool): .
        """
        pass
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
         Sets the location type of the component indicating local, native or team center
        """
        pass
    def SetPath(self, path: str) -> None:
        """
         Sets the path to store the 2D Component 
        """
        pass
import NXOpen
class EditComponentSettingsBuilder(BaseEditSettingsBuilder): 
    """ Represents a NXOpen.Layout2d.EditComponentSettingsBuilder builder.
        It provides an interface for editing layout2d component settings. 
        The committed object is the component with the new settings """
    @property
    def ComponentSettings(self) -> ComponentSettingsBlockBuilder:
        """
        Getter for property: ( ComponentSettingsBlockBuilder NXOpen.) ComponentSettings
         Returns the 2D Component settings block builder which holds the component settings builder   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObject(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
class ExportComponentHierarchyBuilder(NXOpen.Builder): 
    """ Represents a Builder for export component 2D hierarchy """
    @property
    def ChildComponentsForComponents(self) -> bool:
        """
        Getter for property: (bool) ChildComponentsForComponents
         Returns the flag indicating whether to export child components for components   
            
         
        """
        pass
    @ChildComponentsForComponents.setter
    def ChildComponentsForComponents(self, childComponentsForComponents: bool):
        """
        Setter for property: (bool) ChildComponentsForComponents
         Returns the flag indicating whether to export child components for components   
            
         
        """
        pass
    @property
    def ChildComponentsForDefinitions(self) -> bool:
        """
        Getter for property: (bool) ChildComponentsForDefinitions
         Returns the flag indicating whether to export child components for definitions   
            
         
        """
        pass
    @ChildComponentsForDefinitions.setter
    def ChildComponentsForDefinitions(self, childComponentsForDefinitions: bool):
        """
        Setter for property: (bool) ChildComponentsForDefinitions
         Returns the flag indicating whether to export child components for definitions   
            
         
        """
        pass
    @property
    def Contents(self) -> bool:
        """
        Getter for property: (bool) Contents
         Returns the flag indicating whether to export contents for components   
            
         
        """
        pass
    @Contents.setter
    def Contents(self, contents: bool):
        """
        Setter for property: (bool) Contents
         Returns the flag indicating whether to export contents for components   
            
         
        """
        pass
    @property
    def DefinitionReferenceProperties(self) -> bool:
        """
        Getter for property: (bool) DefinitionReferenceProperties
         Returns the flag indicating whether to export definition reference properties for components   
            
         
        """
        pass
    @DefinitionReferenceProperties.setter
    def DefinitionReferenceProperties(self, definitionReferenceProperties: bool):
        """
        Setter for property: (bool) DefinitionReferenceProperties
         Returns the flag indicating whether to export definition reference properties for components   
            
         
        """
        pass
    @property
    def Definitions(self) -> bool:
        """
        Getter for property: (bool) Definitions
         Returns the flag indicating whether to export definitions for components   
            
         
        """
        pass
    @Definitions.setter
    def Definitions(self, definitions: bool):
        """
        Setter for property: (bool) Definitions
         Returns the flag indicating whether to export definitions for components   
            
         
        """
        pass
    @property
    def OutputFileName(self) -> str:
        """
        Getter for property: (str) OutputFileName
         Returns the selected output file   
            
         
        """
        pass
    @OutputFileName.setter
    def OutputFileName(self, outputFileName: str):
        """
        Setter for property: (str) OutputFileName
         Returns the selected output file   
            
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Selection
         Returns the selected objects which may be of  NXOpen::Layout2d::Component  or  NXOpen::Sketch  type   
            
         
        """
        pass
    @property
    def SoftwareProperties(self) -> bool:
        """
        Getter for property: (bool) SoftwareProperties
         Returns the flag indicating whether to export software properties for components   
            
         
        """
        pass
    @SoftwareProperties.setter
    def SoftwareProperties(self, softwareProperties: bool):
        """
        Setter for property: (bool) SoftwareProperties
         Returns the flag indicating whether to export software properties for components   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class GeneralPreferencesBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Layout2d.GeneralPreferencesBuilder
    This builder stores the general layout preferences
    """
    @property
    def ShowLayoutOrigin(self) -> bool:
        """
        Getter for property: (bool) ShowLayoutOrigin
         Returns the flag controling the visibility of layout origin symbols in the session  
            
         
        """
        pass
    @ShowLayoutOrigin.setter
    def ShowLayoutOrigin(self, toggle: bool):
        """
        Setter for property: (bool) ShowLayoutOrigin
         Returns the flag controling the visibility of layout origin symbols in the session  
            
         
        """
        pass
import NXOpen
class InheritDisplayAttributesBuilder(NXOpen.Builder): 
    """ Represents a Builder to inherit geometry display attributes (color, font, width) from and to component definition. """
    class InheritDirection(Enum):
        """
        Members Include: 
         |DefinitionToComponent|  Inherit from Definition 
         |ComponentToDefinition|  Inherit from Component  

        """
        DefinitionToComponent: int
        ComponentToDefinition: int
        @staticmethod
        def ValueOf(value: int) -> InheritDisplayAttributesBuilder.InheritDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.) Components
         Returns the selected 2D Components for inherit   
            
         
        """
        pass
    @property
    def Direction(self) -> InheritDisplayAttributesBuilder.InheritDirection:
        """
        Getter for property: ( InheritDisplayAttributesBuilder.InheritDirection NXOpen.) Direction
         Returns the inherit direction.  
           The default direction is definition to component.   
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: InheritDisplayAttributesBuilder.InheritDirection):
        """
        Setter for property: ( InheritDisplayAttributesBuilder.InheritDirection NXOpen.) Direction
         Returns the inherit direction.  
           The default direction is definition to component.   
         
        """
        pass
import NXOpen
class InsertComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Insert Component functionality which will insert a 2D
       Component instance in the active sketch  """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis   
            
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis   
            
         
        """
        pass
    @property
    def Settings(self) -> ComponentSettingsBlockBuilder:
        """
        Getter for property: ( ComponentSettingsBlockBuilder NXOpen.) Settings
         Returns the Component settings block builder which holds the component settings builder   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Sketch:
        """
        Getter for property: ( NXOpen.Sketch) Sketch
         Returns the sketch to insert the 2D Component   
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sketch: NXOpen.Sketch):
        """
        Setter for property: ( NXOpen.Sketch) Sketch
         Returns the sketch to insert the 2D Component   
            
         
        """
        pass
    @property
    def SpecifyPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SpecifyPoint
         Returns the point specified to put the 2D Component instance  
            
         
        """
        pass
    @SpecifyPoint.setter
    def SpecifyPoint(self, specifyPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SpecifyPoint
         Returns the point specified to put the 2D Component instance  
            
         
        """
        pass
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
         Sets the location type of the 2D Component indicating local, native or team center
        """
        pass
    def SetPath(self, path: str) -> None:
        """
         Sets the path of the reuse library for the 2D Component 
        """
        pass
class Layout2dComponentMemberType(Enum):
    """
    Members Include: 
     |NotSet| 
     |SketchGeometryNonReference| 
     |SketchGeometryReference| 
     |SketchGeometry| 
     |SketchDimension| 
     |SketchConstraint| 
     |Sketch| 
     |Component| 
     |DraftingDimension| 
     |Dimension| 
     |DraftingAnnotationNonDimension| 
     |DraftingAnnotation| 
     |Annotation| 
     |MiscOthers| 
     |Misc| 
     |ExemptRelationsSet| 
     |All| 

    """
    NotSet: int
    SketchGeometryNonReference: int
    SketchGeometryReference: int
    SketchGeometry: int
    SketchDimension: int
    SketchConstraint: int
    Sketch: int
    Component: int
    DraftingDimension: int
    Dimension: int
    DraftingAnnotationNonDimension: int
    DraftingAnnotation: int
    Annotation: int
    MiscOthers: int
    Misc: int
    ExemptRelationsSet: int
    All: int
    @staticmethod
    def ValueOf(value: int) -> Layout2dComponentMemberType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Layout2dDefinitionLocation(Enum):
    """
    Members Include: 
     |Unspecified| 
     |Local| 
     |Native| 
     |TcEng| 

    """
    Unspecified: int
    Local: int
    Native: int
    TcEng: int
    @staticmethod
    def ValueOf(value: int) -> Layout2dDefinitionLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Layout2dDefinitionStatus(Enum):
    """
    Members Include: 
     |Unknown| 
     |Synced| 
     |NotSynced| 
     |Missing| 

    """
    Unknown: int
    Synced: int
    NotSynced: int
    Missing: int
    @staticmethod
    def ValueOf(value: int) -> Layout2dDefinitionStatus:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LayoutDrawingSheetBuilder(DrawingSheetBuilder): 
    """ Represents a Builder for creating Layout2d.LayoutDrawingSheets """
    pass
import NXOpen
class LayoutDrawingSheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Layout2d.LayoutDrawingSheets. """
    @property
    def CurrentDrawingSheet(self) -> LayoutDrawingSheet:
        """
        Getter for property: ( LayoutDrawingSheet NXOpen.) CurrentDrawingSheet
         Returns the currently opened layout drawing sheet.  
           This will return NULL if no layout drawing sheet is opened.   
         
        """
        pass
    def CreateConvertLayoutToSheetBuilder(self) -> ConvertLayoutToSheetBuilder:
        """
         Creates a NXOpen.Layout2d.ConvertLayoutToSheetBuilder 
         Returns builder ( ConvertLayoutToSheetBuilder NXOpen.):  the convert layout to sheet builder .
        """
        pass
    def CreateConvertSheetToLayoutBuilder(self) -> ConvertSheetToLayoutBuilder:
        """
         Creates a NXOpen.Layout2d.ConvertSheetToLayoutBuilder 
         Returns builder ( ConvertSheetToLayoutBuilder NXOpen.):  the convert sheet to layout builder .
        """
        pass
    def CreateLayoutDrawingSheetBuilder(self, layoutDrawingSheet: LayoutDrawingSheet) -> LayoutDrawingSheetBuilder:
        """
         Creates a NXOpen.Layout2d.LayoutDrawingSheetBuilder 
         Returns builder ( LayoutDrawingSheetBuilder NXOpen.):  the layout drawing sheet builder .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> LayoutDrawingSheet:
        """
         Finds the NXOpen.Layout2d.LayoutDrawingSheet with the given identifier 
                as recorded in a journal.  An object may not return the same value as its JournalIdentifier in 
                different versions of  the software. However newer versions of the software should find the same 
                object when  FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns layoutDrawingSheet ( LayoutDrawingSheet NXOpen.):  Layout drawing sheet with this identifier .
        """
        pass
    def InsertSheet(self, name: str, units: DrawingSheet.Unit, numerator: float, denominator: float, projectionAngle: DrawingSheet.ProjectionAngleType) -> LayoutDrawingSheet:
        """
         Inserts a layout drawing sheet into a part. 
         Returns layoutDrawingSheet ( LayoutDrawingSheet NXOpen.):  the inserted layout drawing sheet .
        """
        pass
class LayoutDrawingSheet(DrawingSheet): 
    """ Represents a Layout drawing sheet. """
    pass
import NXOpen
class LocalDefinitionFolderBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Layout2d.LocalDefinitionFolderBuilder. A local definition folder contains 2D Component definitions stored in 
    the current part.
    """
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the current folder name  
            
         
        """
        pass
    @FolderName.setter
    def FolderName(self, folderName: str):
        """
        Setter for property: (str) FolderName
         Returns the current folder name  
            
         
        """
        pass
    @property
    def Parent(self) -> LocalDefinitionFolder:
        """
        Getter for property: ( LocalDefinitionFolder NXOpen.) Parent
         Returns the current folder's parent   
            
         
        """
        pass
    @Parent.setter
    def Parent(self, parentfolder: LocalDefinitionFolder):
        """
        Setter for property: ( LocalDefinitionFolder NXOpen.) Parent
         Returns the current folder's parent   
            
         
        """
        pass
import NXOpen
class LocalDefinitionFolderCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Layout2d.LocalDefinitionFolder objects. A local definition folder contains 2D Component definitions stored in 
    the current part """
    def CreateLocalDefinitionFolderBuilder(self, currentFolder: LocalDefinitionFolder) -> LocalDefinitionFolderBuilder:
        """
         Creates local definition folder builder instance. The builder allows operations such as Creation, Edit and Deletion
                    of local definition folders. These operations are UndoRedo supported.
                
         Returns builder ( LocalDefinitionFolderBuilder NXOpen.): .
        """
        pass
    def FindObject(self, name: str) -> LocalDefinitionFolder:
        """
          Finds the  NXOpen.Layout2d.LocalDefinitionFolder  with the given name. 
                     An exception will be thrown if no object can be found with the given name. 
         Returns folder ( LocalDefinitionFolder NXOpen.): .
        """
        pass
import NXOpen
class LocalDefinitionFolder(NXOpen.NXObject): 
    """ Represents a local definition folder. This folder contains 2D Component definitions stored in 
    the current part """
    pass
import NXOpen
import NXOpen.Gateway
class MakeComponentUniqueBuilder(NXOpen.Builder): 
    """ Represents a Builder for Make 2D Component unique functionality which will create a
       new definition of the selected 2D Component instance """
    @property
    def Component(self) -> SelectComponent:
        """
        Getter for property: ( SelectComponent NXOpen.) Component
         Returns the select 2D Comoponent instance to create definition   
            
         
        """
        pass
    @property
    def ComponentName(self) -> ComponentNameBuilder:
        """
        Getter for property: ( ComponentNameBuilder NXOpen.) ComponentName
         Returns the 2D Component Name defines the name for the new created definition   
            
         
        """
        pass
    @property
    def ImageCapture(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: ( NXOpen.Gateway.ImageCaptureBuilder) ImageCapture
         Returns the image capture builder used to create an image for the new definition   
            
         
        """
        pass
    @property
    def ImageName(self) -> str:
        """
        Getter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    @ImageName.setter
    def ImageName(self, imageName: str):
        """
        Setter for property: (str) ImageName
         Returns the 2D Component image name for the new created definition   
            
         
        """
        pass
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
         Sets the location type of the 2D Component indicating local, native or team center
        """
        pass
    def SetPath(self, path: str) -> None:
        """
         Sets the path to store the 2D Component
        """
        pass
import NXOpen
class NewComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for New 2D Component functionality which will create an empty 2D Component 
        instance and stores its definition in the local 2D Component folder
    """
    @property
    def Owner(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) Owner
         Returns the owner to create the 2D Component, can be either a drawing sheet, a drawing view
                    a sketch or a 2D Component 
                  
            
         
        """
        pass
    @Owner.setter
    def Owner(self, owner: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) Owner
         Returns the owner to create the 2D Component, can be either a drawing sheet, a drawing view
                    a sketch or a 2D Component 
                  
            
         
        """
        pass
import NXOpen
class PublishComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Publish 2D Component functionality which will allow
        local definitions to be exported into external storage locations """
    @property
    def DestinationPath(self) -> str:
        """
        Getter for property: (str) DestinationPath
         Returns the path of folder to publish into   
            
         
        """
        pass
    @DestinationPath.setter
    def DestinationPath(self, destinationPath: str):
        """
        Setter for property: (str) DestinationPath
         Returns the path of folder to publish into   
            
         
        """
        pass
    @property
    def IsFolder(self) -> bool:
        """
        Getter for property: (bool) IsFolder
         Returns the type of object to pblish.  
           Can be definition or folder   
         
        """
        pass
    @IsFolder.setter
    def IsFolder(self, isFolder: bool):
        """
        Setter for property: (bool) IsFolder
         Returns the type of object to pblish.  
           Can be definition or folder   
         
        """
        pass
    @property
    def Location(self) -> Layout2dDefinitionLocation:
        """
        Getter for property: ( Layout2dDefinitionLocation NXOpen.) Location
         Returns the location type of folder to publish into   
            
         
        """
        pass
    @Location.setter
    def Location(self, locationType: Layout2dDefinitionLocation):
        """
        Setter for property: ( Layout2dDefinitionLocation NXOpen.) Location
         Returns the location type of folder to publish into   
            
         
        """
        pass
    @property
    def OriginPath(self) -> str:
        """
        Getter for property: (str) OriginPath
         Returns the path of folder or definition to publish   
            
         
        """
        pass
    @OriginPath.setter
    def OriginPath(self, originPath: str):
        """
        Setter for property: (str) OriginPath
         Returns the path of folder or definition to publish   
            
         
        """
        pass
import NXOpen
class ReparentComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Reparent 2D Component functionality which will reparents
       the selected 2D Component contents from another 2D Component definition.
    """
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.) Components
         Returns the select 2D Components to reparent the definitions   
            
         
        """
        pass
    @property
    def CreateCopy(self) -> bool:
        """
        Getter for property: (bool) CreateCopy
         Returns the flag to distinguish copy and cut operations   
            
         
        """
        pass
    @CreateCopy.setter
    def CreateCopy(self, createCopy: bool):
        """
        Setter for property: (bool) CreateCopy
         Returns the flag to distinguish copy and cut operations   
            
         
        """
        pass
    @property
    def Target(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: ( NXOpen.DisplayableObject) Target
         Returns the target of 2D Components reparent operation   
            
         
        """
        pass
    @Target.setter
    def Target(self, target: NXOpen.DisplayableObject):
        """
        Setter for property: ( NXOpen.DisplayableObject) Target
         Returns the target of 2D Components reparent operation   
            
         
        """
        pass
    def AddComponents(self, components: List[Component]) -> None:
        """
         Add a list of 2D Components
        """
        pass
import NXOpen
class ReplaceComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Replace 2D Component functionality which will replaces
       the selected 2D Component contents from another 2D Component definition.
    """
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.) Components
         Returns the select 2D Components to replace the definitions   
            
         
        """
        pass
    @property
    def Location(self) -> Layout2dDefinitionLocation:
        """
        Getter for property: ( Layout2dDefinitionLocation NXOpen.) Location
         Returns the location type of the 2D Component definition to replace 
                   indicating local, native or team center
                  
            
         
        """
        pass
    @Location.setter
    def Location(self, locationType: Layout2dDefinitionLocation):
        """
        Setter for property: ( Layout2dDefinitionLocation NXOpen.) Location
         Returns the location type of the 2D Component definition to replace 
                   indicating local, native or team center
                  
            
         
        """
        pass
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
         Returns the path of the 2D Component definition to replace   
            
         
        """
        pass
    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
         Returns the path of the 2D Component definition to replace   
            
         
        """
        pass
    @property
    def ReplaceAll(self) -> bool:
        """
        Getter for property: (bool) ReplaceAll
         Returns the flag indicating whether to replace all instances of selected components   
            
         
        """
        pass
    @ReplaceAll.setter
    def ReplaceAll(self, replaceAll: bool):
        """
        Setter for property: (bool) ReplaceAll
         Returns the flag indicating whether to replace all instances of selected components   
            
         
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
            
         Returns objects ( Component List[NXOpe):  items in list .
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
        Getter for property: ( Component NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Component):
        """
        Setter for property: ( Component NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Component, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Component NXOpen.. selected object .
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
         - selection1 is:  Component NXOpen.. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Component NXOpen.. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Component, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Component NXOpen.. selected object .
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
class SmashComponentBuilder(NXOpen.Builder): 
    """ Represents a Builder for Smash 2D Component functionality which will break instances
       of 2D Components into its constituent pieces, we can have multiple committed objects """
    @property
    def Components(self) -> SelectComponentList:
        """
        Getter for property: ( SelectComponentList NXOpen.) Components
         Returns the select 2D Component instances to smash   
            
         
        """
        pass
