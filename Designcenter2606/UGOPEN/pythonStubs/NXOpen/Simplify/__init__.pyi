from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class InputsToSimplifyBuilder(NXOpen.Builder): 
    """ Represents a Simplify.InputsToSimplifyBuilder builder """
    @property
    def BodiesToAlwaysKeep(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodiesToAlwaysKeep
         Returns the bodies to always keep in the simplification even though they would be excluded 
                    because of minimum body size or because of being an internal body.  
           The bodies have to be from
                    the source assembly.   
         
        """
        pass
    @property
    def BodiesToAlwaysRemove(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodiesToAlwaysRemove
         Returns the bodies to always remove from the simplification even though the active body simplification 
                    rules would include them.  
           This will exclude bodies that would otherwise be included 
                    because they belong to a component that is included. The bodies have to be from the source assembly.   
         
        """
        pass
    @property
    def FacesToAlwaysKeep(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FacesToAlwaysKeep
         Returns the faces to explicitly include or retain in the simplification result even though
                    the active geometry simplification rules (like removal based on hole diameter size) would remove them.  
          
                    The faces can only be either from the selected bodies or from the selected components and they have to be from the
                    source assembly.   
         
        """
        pass
    @property
    def FacesToAlwaysRemove(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FacesToAlwaysRemove
         Returns the faces to explicitly exclude or delete from the simplification result even though
                    the active geometry simplification rules would include them.  
           This can be used to remove 
                    unwanted faces without using any geometry-based simplifications.
                    The faces can only be either from the selected bodies or from the selected components 
                    and they have to be from the source assembly.   
         
        """
        pass
    @property
    def IncludeChildComponents(self) -> bool:
        """
        Getter for property: (bool) IncludeChildComponents
         Returns whether to include child components   
            
         
        """
        pass
    @IncludeChildComponents.setter
    def IncludeChildComponents(self, includeChildComponents: bool):
        """
        Setter for property: (bool) IncludeChildComponents
         Returns whether to include child components   
            
         
        """
        pass
    @property
    def ObjectsToSimplify(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectsToSimplify
         Returns the objects for performing simplification.  
           The Objects can be components or solid bodies from the source assembly.   
         
        """
        pass
    @property
    def ObjectsToSimplifyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ObjectsToSimplifyCollector
         Returns the collector of bodies for performing assembly simplification.  
             
         
        """
        pass
    def FindInvalidInputsForBodiesToAlwaysKeep(self, inputList: List[NXOpen.NXObject]) -> NXOpen.ErrorList:
        """
         Given a list of input NXObjects, this method returns an ErrorList of all objects which do not pass validation
                as bodies to always keep, supplying reasons as error codes and descriptions within the ErrorList. 
         Returns invalidInputErrorList ( NXOpen.ErrorList): .
        """
        pass
    def FindInvalidInputsForBodiesToAlwaysRemove(self, inputList: List[NXOpen.NXObject]) -> NXOpen.ErrorList:
        """
         Given a list of input NXObjects, this method returns an ErrorList of all objects which do not pass validation
                as bodies to always remove, supplying reasons as error codes and descriptions within the ErrorList. 
         Returns invalidInputErrorList ( NXOpen.ErrorList): .
        """
        pass
    def FindInvalidInputsForFacesToAlwaysKeep(self, inputList: List[NXOpen.NXObject]) -> NXOpen.ErrorList:
        """
         Given a list of input NXObjects, this method returns an ErrorList of all objects which do not pass validation
                as faces to always keep, supplying reasons as error codes and descriptions within the ErrorList. 
         Returns invalidInputErrorList ( NXOpen.ErrorList): .
        """
        pass
    def FindInvalidInputsForFacesToAlwaysRemove(self, inputList: List[NXOpen.NXObject]) -> NXOpen.ErrorList:
        """
         Given a list of input NXObjects, this method returns an ErrorList of all objects which do not pass validation
                as faces to always remove, supplying reasons as error codes and descriptions within the ErrorList. 
         Returns invalidInputErrorList ( NXOpen.ErrorList): .
        """
        pass
    def FindInvalidInputsForObjectsToSimplify(self, inputList: List[NXOpen.NXObject]) -> NXOpen.ErrorList:
        """
         Given a list of input NXObjects, this method returns an ErrorList of all objects which do not pass validation
                as objects to simplify, supplying reasons as error codes and descriptions within the ErrorList. 
         Returns invalidInputErrorList ( NXOpen.ErrorList): .
        """
        pass
import NXOpen
import NXOpen.Annotations
class KeepPmiBuilder(NXOpen.Builder): 
    """ Represents a Simplify.KeepPmiBuilder builder """
    @property
    def SelectedPMIs(self) -> NXOpen.Annotations.SelectAnnotationList:
        """
        Getter for property: ( NXOpen.Annotations.SelectAnnotationList) SelectedPMIs
         Returns the selected pmis   
            
         
        """
        pass
import NXOpen
class RemoveBodiesBuilder(NXOpen.Builder): 
    """ Represents a Simplify.RemoveBodiesBuilder builder """
    @property
    def MaximumBodySize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumBodySize
         Returns the maximum body size up-to-and-including which bodies are removed while simplifying the selected bodies.  
             
         
        """
        pass
    @property
    def RemoveInternalBodies(self) -> bool:
        """
        Getter for property: (bool) RemoveInternalBodies
         Returns the toggle that controls whether internal bodies are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveInternalBodies.setter
    def RemoveInternalBodies(self, removeInternalBodies: bool):
        """
        Setter for property: (bool) RemoveInternalBodies
         Returns the toggle that controls whether internal bodies are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def RemoveSmallBodies(self) -> bool:
        """
        Getter for property: (bool) RemoveSmallBodies
         Returns the toggle that controls whether small bodies are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveSmallBodies.setter
    def RemoveSmallBodies(self, removeSmallBodies: bool):
        """
        Setter for property: (bool) RemoveSmallBodies
         Returns the toggle that controls whether small bodies are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
import NXOpen
class RemoveFeaturesBuilder(NXOpen.Builder): 
    """ Represents a Simplify.RemoveFeaturesBuilder builder """
    @property
    def MaximumBlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumBlendRadius
         Returns the blend radius up-to-and-including which blends are removed simplifying the selected bodies.  
             
         
        """
        pass
    @property
    def MaximumHoleDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumHoleDiameter
         Returns the hole diameter size up-to-and-including which holes are removed while simplifying the selected bodies.  
             
         
        """
        pass
    @property
    def RemoveBlends(self) -> bool:
        """
        Getter for property: (bool) RemoveBlends
         Returns the toggle that controls whether blends are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveBlends.setter
    def RemoveBlends(self, removeBlends: bool):
        """
        Setter for property: (bool) RemoveBlends
         Returns the toggle that controls whether blends are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def RemoveHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveHoles
         Returns the toggle that controls whether holes are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveHoles.setter
    def RemoveHoles(self, removeHoles: bool):
        """
        Setter for property: (bool) RemoveHoles
         Returns the toggle that controls whether holes are deleted from the selected bodies in the simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @property
    def RemoveInternalVoid(self) -> bool:
        """
        Getter for property: (bool) RemoveInternalVoid
         Returns the toggle to remove internal enclosed voids from bodies included in simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
    @RemoveInternalVoid.setter
    def RemoveInternalVoid(self, removeInternalVoid: bool):
        """
        Setter for property: (bool) RemoveInternalVoid
         Returns the toggle to remove internal enclosed voids from bodies included in simplification.  
           
                    the default value of this toggle is true   
         
        """
        pass
import NXOpen
class SaveAsTemplateBuilder(NXOpen.FileNew): 
    """ Represents a Simplify.SaveAsTemplateBuilder builder """
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the template name   
            
         
        """
        pass
    @PresentationName.setter
    def PresentationName(self, templateName: str):
        """
        Setter for property: (str) PresentationName
         Returns the template name   
            
         
        """
        pass
    def GetTemplateDescription(self) -> List[str]:
        """
         Returns the template description 
         Returns templateDescription (List[str]): .
        """
        pass
    def SetTemplateDescription(self, templateDescription: List[str]) -> None:
        """
         Sets the template description 
        """
        pass
import NXOpen
class SimplifyManager(NXOpen.Object): 
    """ Collection of simplify operations. """
    @property
    def SimplifiedPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) SimplifiedPart
         Returns the simplified part containing the result of simplification.  
             
         
        """
        pass
    @SimplifiedPart.setter
    def SimplifiedPart(self, simplifiedPart: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) SimplifiedPart
         Returns the simplified part containing the result of simplification.  
             
         
        """
        pass
    @property
    def SourcePart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) SourcePart
         Returns the source part containing input bodies for simplification.  
             
         
        """
        pass
    @SourcePart.setter
    def SourcePart(self, sourcePart: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) SourcePart
         Returns the source part containing input bodies for simplification.  
             
         
        """
        pass
    def ClearAllData() -> None:
        """
         Clear the data (include rules) When you switch the application tofrom Simplify Application. 
        """
        pass
    def ClearAllDataExceptRules() -> None:
        """
         Clear the data after the execute operation except for the option values. 
        """
        pass
    def CreateInputsToSimplifyBuilder(sourceAssembly: NXOpen.Part) -> InputsToSimplifyBuilder:
        """
         Creates a NXOpen.Simplify.InputsToSimplifyBuilder. Only one simplication can
                be "in progress" at a time, therefore the same sourceAssembly needs to be passed to each builder.
                First one that is created will be effectively "setting" the source assembly. 
                this builder cannot be used within the simplify template application.
         Returns builder ( InputsToSimplifyBuilder NXOpen.): .
        """
        pass
    def CreateKeepPmiBuilder(sourceAssembly: NXOpen.Part) -> KeepPmiBuilder:
        """
         Creates a NXOpen.Simplify.KeepPmiBuilder.
                this builder cannot be used within the simplify template application.
         Returns builder ( KeepPmiBuilder NXOpen.): .
        """
        pass
    def CreateRemoveBodiesBuilder(sourceAssembly: NXOpen.Part) -> RemoveBodiesBuilder:
        """
         Creates a NXOpen.Simplify.RemoveBodiesBuilder. Only one simplication can
                be "in progress" at a time, therefore the same sourceAssembly needs to be passed to each builder.
                First one that is created will be effectively "setting" the source assembly. 
                this builder can also be used within the simplify template application to edit template properties.
         Returns builder ( RemoveBodiesBuilder NXOpen.): .
        """
        pass
    def CreateRemoveFeaturesBuilder(sourceAssembly: NXOpen.Part) -> RemoveFeaturesBuilder:
        """
         Creates a NXOpen.Simplify.RemoveFeaturesBuilder. Only one simplication can
                be "in progress" at a time, therefore the same sourceAssembly needs to be passed to each builder.
                First one that is created will be effectively "setting" the source assembly.
                this builder can also be used within the simplify template application to edit template properties.
         Returns builder ( RemoveFeaturesBuilder NXOpen.): .
        """
        pass
    def CreateSaveAsTemplateBuilder(sourceAssembly: NXOpen.Part) -> SaveAsTemplateBuilder:
        """
         Creates a NXOpen.Simplify.SaveAsTemplateBuilder. 
                this builder cannot be used within the simplify template application.
         Returns builder ( SaveAsTemplateBuilder NXOpen.): .
        """
        pass
    def CreateSimplifySettingsBuilder(sourceAssembly: NXOpen.Part) -> SimplifySettingsBuilder:
        """
         Creates a NXOpen.Simplify.SimplifySettingsBuilder. Only one simplication can
                be "in progress" at a time, therefore the same sourceAssembly needs to be passed to each builder.
                First one that is created will be effectively "setting" the source assembly. 
                this builder can also be used within the simplify template application to edit template properties.
         Returns builder ( SimplifySettingsBuilder NXOpen.): .
        """
        pass
    def CreateTemplatePropertiesBuilder(sourceAssembly: NXOpen.Part) -> TemplatePropertiesBuilder:
        """
         Creates a NXOpen.Simplify.TemplatePropertiesBuilder .
                this builder can also be used within the simplify template application to edit template properties.
         Returns builder ( TemplatePropertiesBuilder NXOpen.): .
        """
        pass
    def CreateUseTemplateBuilder(sourceAssembly: NXOpen.Part) -> UseTemplateBuilder:
        """
         Creates a NXOpen.Simplify.UseTemplateBuilder.
                this builder cannot be used within the simplify template application.
         Returns builder ( UseTemplateBuilder NXOpen.): .
        """
        pass
    def EnterSimplifyTemplateApp(templatePart: NXOpen.Part) -> None:
        """
         Enter into the  simplify template application with the template part. 
                the user cannot perform a simplification while they are in the template app.
        """
        pass
    def Execute() -> None:
        """
         Execute the simplification process. User need to commit each builder and set the 
                simplified part before perform simplification. 
        """
        pass
    def ExitSimplifyTemplateApp() -> None:
        """
         Exit from the  simplify template application.
                the template part must be saved using JA_BASE_PART_close API before calling this method, this "exit" method will not do it.
        """
        pass
    def Preview() -> None:
        """
         Previews the result of simplification based on the inputs in each builder. The user needs to commit each 
                    builder and set the simplified part before preview. This API is primarily intended for interactive NX session.
                    During preview, simplified bodies are created in the destination part without uniting the bodies,
                    and the destination part is made a displayed part. An error code is returned if the preview was
                    successfully created but had minor issues. In an NXOpen program, invoking this preview API is not necessary. 
                    The new bodies in the destination part after preview are intermediate and their part is not suitable for any operation.
                    Only after the user successfully performs Execute is the destination part suitable for any operation. 
        """
        pass
import NXOpen
class SimplifySettingsBuilder(NXOpen.Builder): 
    """ Represents a Simplify.SimplifySettingsBuilder builder """
    class MassPropertiesOptionValue(Enum):
        """
        Members Include: 
         |StoreCalculated|  Calculate and save the mass properties of the source assembly on the simplified part 
         |StoreZero|  Set the mass properties of the simplified part to zero 

        """
        StoreCalculated: int
        StoreZero: int
        @staticmethod
        def ValueOf(value: int) -> SimplifySettingsBuilder.MassPropertiesOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SimplifiedPartOptionValue(Enum):
        """
        Members Include: 
         |CreateNewPart|  Create new part for simplify operation 
         |UseCurrentPart|  Use current part for simplify operation 
         |SelectExistingPart|  Use user selected existing part for simplify operation 

        """
        CreateNewPart: int
        UseCurrentPart: int
        SelectExistingPart: int
        @staticmethod
        def ValueOf(value: int) -> SimplifySettingsBuilder.SimplifiedPartOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns whether to create associative 
                the default value of this toggle is true   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns whether to create associative 
                the default value of this toggle is true   
            
         
        """
        pass
    @property
    def ExistingSimplifiedPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) ExistingSimplifiedPart
         Returns the simplified part containing the result of simplification.  
           It must be fully loaded. Only specify this
                    part if the simplified part option is set to
                     NXOpen::Simplify::SimplifySettingsBuilder::SimplifiedPartOptionValueSelectExistingPart 
                    If the simplified part option is set to
                     NXOpen::Simplify::SimplifySettingsBuilder::SimplifiedPartOptionValueCreateNewPart  or
                     NXOpen::Simplify::SimplifySettingsBuilder::SimplifiedPartOptionValueUseCurrentPart 
                    This part will get ignored.
                  
         
        """
        pass
    @ExistingSimplifiedPart.setter
    def ExistingSimplifiedPart(self, destinationPart: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) ExistingSimplifiedPart
         Returns the simplified part containing the result of simplification.  
           It must be fully loaded. Only specify this
                    part if the simplified part option is set to
                     NXOpen::Simplify::SimplifySettingsBuilder::SimplifiedPartOptionValueSelectExistingPart 
                    If the simplified part option is set to
                     NXOpen::Simplify::SimplifySettingsBuilder::SimplifiedPartOptionValueCreateNewPart  or
                     NXOpen::Simplify::SimplifySettingsBuilder::SimplifiedPartOptionValueUseCurrentPart 
                    This part will get ignored.
                  
         
        """
        pass
    @property
    def MassPropertiesOption(self) -> SimplifySettingsBuilder.MassPropertiesOptionValue:
        """
        Getter for property: ( SimplifySettingsBuilder.MassPropertiesOptionValue NXOpen.) MassPropertiesOption
         Returns the mass property options for the simplify operation.  
           This property has no effect if the
                    simplified bodies are created in the source assembly.   
         
        """
        pass
    @MassPropertiesOption.setter
    def MassPropertiesOption(self, massPropertiesOption: SimplifySettingsBuilder.MassPropertiesOptionValue):
        """
        Setter for property: ( SimplifySettingsBuilder.MassPropertiesOptionValue NXOpen.) MassPropertiesOption
         Returns the mass property options for the simplify operation.  
           This property has no effect if the
                    simplified bodies are created in the source assembly.   
         
        """
        pass
    @property
    def SimplifiedPartOption(self) -> SimplifySettingsBuilder.SimplifiedPartOptionValue:
        """
        Getter for property: ( SimplifySettingsBuilder.SimplifiedPartOptionValue NXOpen.) SimplifiedPartOption
         Returns the simplified part option for the simplify operation.  
             
         
        """
        pass
    @SimplifiedPartOption.setter
    def SimplifiedPartOption(self, simplifiedPartOption: SimplifySettingsBuilder.SimplifiedPartOptionValue):
        """
        Setter for property: ( SimplifySettingsBuilder.SimplifiedPartOptionValue NXOpen.) SimplifiedPartOption
         Returns the simplified part option for the simplify operation.  
             
         
        """
        pass
    @property
    def SynchronizeView(self) -> bool:
        """
        Getter for property: (bool) SynchronizeView
         Returns whether the view of the displayed simplified part will be synchronized
                with the view of the displayed source part.  
           This option is only applicable in an interactive session.  
         
        """
        pass
    @SynchronizeView.setter
    def SynchronizeView(self, synchronizeView: bool):
        """
        Setter for property: (bool) SynchronizeView
         Returns whether the view of the displayed simplified part will be synchronized
                with the view of the displayed source part.  
           This option is only applicable in an interactive session.  
         
        """
        pass
    @property
    def UniteBodies(self) -> bool:
        """
        Getter for property: (bool) UniteBodies
         Returns whether unite overlapping bodies included in simplification.  
           
                    the default value of this toggle is false   
         
        """
        pass
    @UniteBodies.setter
    def UniteBodies(self, uniteBodies: bool):
        """
        Setter for property: (bool) UniteBodies
         Returns whether unite overlapping bodies included in simplification.  
           
                    the default value of this toggle is false   
         
        """
        pass
import NXOpen
class TemplatePropertiesBuilder(NXOpen.Builder): 
    """ Represents a Simplify.TemplatePropertiesBuilder builder """
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the template name   
            
         
        """
        pass
    @PresentationName.setter
    def PresentationName(self, templateName: str):
        """
        Setter for property: (str) PresentationName
         Returns the template name   
            
         
        """
        pass
    def GetTemplateDescription(self) -> List[str]:
        """
         Returns the template description 
         Returns templateDescription (List[str]): .
        """
        pass
    def SetTemplateDescription(self, templateDescription: List[str]) -> None:
        """
         Sets the template description 
        """
        pass
import NXOpen
import NXOpen.ModlUtils
class UseTemplateBuilder(NXOpen.Builder): 
    """ Represents a Simplify.UseTemplateBuilder builder """
    def RegisterImportTemplatePartBuilder(self, templateBuilder: NXOpen.ModlUtils.ImportTemplatePartBuilder) -> None:
        """
         Register an ImportTemplatePartBuilder with UseTemplateBuilder. User need to register 
                    ImportTemplatePartBuilder after creating builder. ImportTemplatePartBuilder will be 
                    used to set template Part file spec whose recepie to be used for simplification. 
                    User do not need to commit ImportTemplatePartBuilder. UseTemplateBuilder builder
                    commit will handle ImportTemplatePartBuilder commit. 
        """
        pass
