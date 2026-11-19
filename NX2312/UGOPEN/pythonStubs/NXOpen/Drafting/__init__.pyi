from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class is used to annotate views based on the knowledge fusion rules.  <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateAnnotateViewsBuilder  NXOpen::Drafting::AutomationManager::CreateAnnotateViewsBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class AnnotateViewsBuilder(NXOpen.Builder): 
    """ This class is used to annotate views based on the knowledge fusion rules. """


    ##  Option to delete or preserve existing automatic annotations when annotation views command
    ##         is run. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Delete</term><description> 
    ## </description> </item><item><term> 
    ## Preserve</term><description> 
    ## </description> </item></list>
    class ExistingAutomaticAnnotation(Enum):
        """
        Members Include: <Delete> <Preserve>
        """
        Delete: int
        Preserve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnnotateViewsBuilder.ExistingAutomaticAnnotation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.Drafting.AnnotateViewsBuilder.ExistingAutomaticAnnotation@endlink) ExistingAutomaticAnnotationOption
    ##   the existing automatic annotation option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return AnnotateViewsBuilder.ExistingAutomaticAnnotation
    @property
    def ExistingAutomaticAnnotationOption(self) -> AnnotateViewsBuilder.ExistingAutomaticAnnotation:
        """
        Getter for property: (@link AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.Drafting.AnnotateViewsBuilder.ExistingAutomaticAnnotation@endlink) ExistingAutomaticAnnotationOption
          the existing automatic annotation option   
            
         
        """
        pass
    
    ## Setter for property: (@link AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.Drafting.AnnotateViewsBuilder.ExistingAutomaticAnnotation@endlink) ExistingAutomaticAnnotationOption

    ##   the existing automatic annotation option   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ExistingAutomaticAnnotationOption.setter
    def ExistingAutomaticAnnotationOption(self, existingAutomaticAnnotationOption: AnnotateViewsBuilder.ExistingAutomaticAnnotation):
        """
        Setter for property: (@link AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.Drafting.AnnotateViewsBuilder.ExistingAutomaticAnnotation@endlink) ExistingAutomaticAnnotationOption
          the existing automatic annotation option   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectDraftingViewList NXOpen.Drawings.SelectDraftingViewList@endlink) Views
    ##   the views to annotate   
    ##     
    ##  
    ## Getter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return SelectDraftingViewList
    @property
    def Views(self) -> SelectDraftingViewList:
        """
        Getter for property: (@link SelectDraftingViewList NXOpen.Drawings.SelectDraftingViewList@endlink) Views
          the views to annotate   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class AttributeItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##   the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
          the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  items to append 
    @overload
    def Append(self, object_list: AttributeItemBuilderList, objects: List[AttributeItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  item to append 
    @overload
    def Append(self, object_list: AttributeItemBuilderList, objectValue: AttributeItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: AttributeItemBuilderList) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be deleted 
    def ClearIndex(object_list: AttributeItemBuilderList, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  whether to delete the objects when removing them 
    def Clear(object_list: AttributeItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: AttributeItemBuilderList, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: AttributeItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: AttributeItemBuilderList, obj: AttributeItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: AttributeItemBuilderList, obj: AttributeItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  Object to find index for 
    def FindIndex(object_list: AttributeItemBuilderList, obj: AttributeItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link AttributeItemBuilder NXOpen.Drafting.AttributeItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: AttributeItemBuilderList, index: int) -> AttributeItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link AttributeItemBuilder NXOpen.Drafting.AttributeItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link AttributeItemBuilder List[NXOpen.Drafting.AttributeItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: AttributeItemBuilderList) -> List[AttributeItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link AttributeItemBuilder List[NXOpen.Drafting.AttributeItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: AttributeItemBuilderList, location: int, objectValue: AttributeItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: AttributeItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: AttributeItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The list contents 
    def SetContents(object_list: AttributeItemBuilderList, objects: List[AttributeItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location of the first item 
    @overload
    def Swap(self, object_list: AttributeItemBuilderList, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  first item 
    @overload
    def Swap(self, object_list: AttributeItemBuilderList, object1: AttributeItemBuilder, object2: AttributeItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::Drafting::AttributeItemBuilder NXOpen::Drafting::AttributeItemBuilder@endlink .  This class is
##     used to specify information about a single NX attribute.
##      <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateAttributeItemBuilder  NXOpen::Drafting::AutomationManager::CreateAttributeItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class AttributeItemBuilder(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.Drafting.AttributeItemBuilder</ja_class>.  This class is
    used to specify information about a single NX attribute.
    """


    ## Getter for property: (str) Title
    ##   the title.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the title.  
             
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##   the title.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Title.setter
    def Title(self, attributeTitle: str):
        """
        Setter for property: (str) Title
          the title.  
             
         
        """
        pass
    
    ## Getter for property: (str) Value
    ##   the value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
          the value.  
             
         
        """
        pass
    
    ## Setter for property: (str) Value

    ##   the value.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Value.setter
    def Value(self, attributeValue: str):
        """
        Setter for property: (str) Value
          the value.  
             
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Drafting::AutomationManager NXOpen::Drafting::AutomationManager@endlink .  This class is
##     used to create objects which are used in the automation of drawing creation.
##      <br> Use @link NXOpen::DraftingManager::AutomationManager NXOpen::DraftingManager::AutomationManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class AutomationManager(NXOpen.Object): 
    """
    Represents a <ja_class>NXOpen.Drafting.AutomationManager</ja_class>.  This class is
    used to create objects which are used in the automation of drawing creation.
    """


    ##  Returns the RegionCollection instance  
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @link DrawingRegionCollection NXOpen.Drawings.DrawingRegionCollection@endlink
    @property
    def DrawingRegions() -> DrawingRegionCollection:
        """
         Returns the RegionCollection instance  
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::AnnotateViewsBuilder NXOpen::Drafting::AnnotateViewsBuilder@endlink  
    ##  @return builder (@link AnnotateViewsBuilder NXOpen.Drafting.AnnotateViewsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreateAnnotateViewsBuilder(part: AutomationManager) -> AnnotateViewsBuilder:
        """
         Creates a @link NXOpen::Drafting::AnnotateViewsBuilder NXOpen::Drafting::AnnotateViewsBuilder@endlink  
         @return builder (@link AnnotateViewsBuilder NXOpen.Drafting.AnnotateViewsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::AttributeItemBuilder NXOpen::Drafting::AttributeItemBuilder@endlink  
    ##  @return builder (@link AttributeItemBuilder NXOpen.Drafting.AttributeItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreateAttributeItemBuilder(part: AutomationManager) -> AttributeItemBuilder:
        """
         Creates a @link NXOpen::Drafting::AttributeItemBuilder NXOpen::Drafting::AttributeItemBuilder@endlink  
         @return builder (@link AttributeItemBuilder NXOpen.Drafting.AttributeItemBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::DistributeAnnotationsBuilder NXOpen::Drafting::DistributeAnnotationsBuilder@endlink  
    ##  @return builder (@link DistributeAnnotationsBuilder NXOpen.Drafting.DistributeAnnotationsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreateDistributeAnnotationsBuilder(part: AutomationManager) -> DistributeAnnotationsBuilder:
        """
         Creates a @link NXOpen::Drafting::DistributeAnnotationsBuilder NXOpen::Drafting::DistributeAnnotationsBuilder@endlink  
         @return builder (@link DistributeAnnotationsBuilder NXOpen.Drafting.DistributeAnnotationsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::DrawingCreationWizardBuilder NXOpen::Drafting::DrawingCreationWizardBuilder@endlink  
    ##  @return builder (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  If this is set to true then the builder will be configured for edit mode, otherwise it will be configured for create mode.
    ##                         Please see the @link NXOpen::Drafting::DrawingCreationWizardBuilder NXOpen::Drafting::DrawingCreationWizardBuilder@endlink  class documentation for more information on how
    ##                         to use the builder in these different modes. 
    def CreateDrawingCreationWizardBuilder(part: AutomationManager, isEditing: bool) -> DrawingCreationWizardBuilder:
        """
         Creates a @link NXOpen::Drafting::DrawingCreationWizardBuilder NXOpen::Drafting::DrawingCreationWizardBuilder@endlink  
         @return builder (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::DrawingCreationWizardBuilder NXOpen::Drafting::DrawingCreationWizardBuilder@endlink  
    ##  @return builder (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  Drawing Booklet class used to populate the builder 
    def CreateDrawingCreationWizardBuilderFromRule(part: AutomationManager, className: str) -> DrawingCreationWizardBuilder:
        """
         Creates a @link NXOpen::Drafting::DrawingCreationWizardBuilder NXOpen::Drafting::DrawingCreationWizardBuilder@endlink  
         @return builder (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::AutomationPreferencesBuilder NXOpen::Drafting::AutomationPreferencesBuilder@endlink  
    ##  @return builder (@link AutomationPreferencesBuilder NXOpen.Drafting.AutomationPreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_drawing_auto ("NX Drawing Automation")
    def CreatePreferencesBuilder(part: AutomationManager) -> AutomationPreferencesBuilder:
        """
         Creates a @link NXOpen::Drafting::AutomationPreferencesBuilder NXOpen::Drafting::AutomationPreferencesBuilder@endlink  
         @return builder (@link AutomationPreferencesBuilder NXOpen.Drafting.AutomationPreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::PrimaryContentItemBuilder NXOpen::Drafting::PrimaryContentItemBuilder@endlink  
    ##  @return builder (@link PrimaryContentItemBuilder NXOpen.Drafting.PrimaryContentItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreatePrimaryContentItemBuilder(part: AutomationManager) -> PrimaryContentItemBuilder:
        """
         Creates a @link NXOpen::Drafting::PrimaryContentItemBuilder NXOpen::Drafting::PrimaryContentItemBuilder@endlink  
         @return builder (@link PrimaryContentItemBuilder NXOpen.Drafting.PrimaryContentItemBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::RulesBuilder NXOpen::Drafting::RulesBuilder@endlink  
    ##  @return builder (@link RulesBuilder NXOpen.Drafting.RulesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreateRulesBuilder(part: AutomationManager) -> RulesBuilder:
        """
         Creates a @link NXOpen::Drafting::RulesBuilder NXOpen::Drafting::RulesBuilder@endlink  
         @return builder (@link RulesBuilder NXOpen.Drafting.RulesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::SpecifyRuleBuilder NXOpen::Drafting::SpecifyRuleBuilder@endlink  
    ##  @return builder (@link SpecifyRuleBuilder NXOpen.Drafting.SpecifyRuleBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreateSpecifyRuleBuilder(part: AutomationManager) -> SpecifyRuleBuilder:
        """
         Creates a @link NXOpen::Drafting::SpecifyRuleBuilder NXOpen::Drafting::SpecifyRuleBuilder@endlink  
         @return builder (@link SpecifyRuleBuilder NXOpen.Drafting.SpecifyRuleBuilder@endlink): .
        """
        pass
    
    ##  Returns the remaining loaded parts and remaining unloaded parts full names from the booklet 
    ##  @return A tuple consisting of (remainingParts, remainingPartFileSpecs). 
    ##  - remainingParts is: @link NXOpen.Part List[NXOpen.Part]@endlink.
    ##  - remainingPartFileSpecs is: List[str].

    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRemainingPartsOfBooklet(part: AutomationManager) -> Tuple[List[NXOpen.Part], List[str]]:
        """
         Returns the remaining loaded parts and remaining unloaded parts full names from the booklet 
         @return A tuple consisting of (remainingParts, remainingPartFileSpecs). 
         - remainingParts is: @link NXOpen.Part List[NXOpen.Part]@endlink.
         - remainingPartFileSpecs is: List[str].

        """
        pass
    
import NXOpen
import NXOpen.Preferences
## the builder for Drafting Automation Preferences  <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreatePreferencesBuilder  NXOpen::Drafting::AutomationManager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class AutomationPreferencesBuilder(NXOpen.Builder): 
    """the builder for Drafting Automation Preferences """


    ## Getter for property: (bool) AllowFeetInchFractionForDimensionGreaterThan
    ##   the determination of the feet inch fraction display for dimension greater than   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def AllowFeetInchFractionForDimensionGreaterThan(self) -> bool:
        """
        Getter for property: (bool) AllowFeetInchFractionForDimensionGreaterThan
          the determination of the feet inch fraction display for dimension greater than   
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowFeetInchFractionForDimensionGreaterThan

    ##   the determination of the feet inch fraction display for dimension greater than   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @AllowFeetInchFractionForDimensionGreaterThan.setter
    def AllowFeetInchFractionForDimensionGreaterThan(self, allowFeetInchFractionForDimensionGreaterThan: bool):
        """
        Setter for property: (bool) AllowFeetInchFractionForDimensionGreaterThan
          the determination of the feet inch fraction display for dimension greater than   
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowInchFractionToNearest
    ##   the determination of the display for inch fraction to nearest   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def AllowInchFractionToNearest(self) -> bool:
        """
        Getter for property: (bool) AllowInchFractionToNearest
          the determination of the display for inch fraction to nearest   
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowInchFractionToNearest

    ##   the determination of the display for inch fraction to nearest   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @AllowInchFractionToNearest.setter
    def AllowInchFractionToNearest(self, allowInchFractionToNearest: bool):
        """
        Setter for property: (bool) AllowInchFractionToNearest
          the determination of the display for inch fraction to nearest   
            
         
        """
        pass
    
    ## Getter for property: (bool) AnnotationInsideGeometry
    ##   the annotation inside geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def AnnotationInsideGeometry(self) -> bool:
        """
        Getter for property: (bool) AnnotationInsideGeometry
          the annotation inside geometry   
            
         
        """
        pass
    
    ## Setter for property: (bool) AnnotationInsideGeometry

    ##   the annotation inside geometry   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @AnnotationInsideGeometry.setter
    def AnnotationInsideGeometry(self, annotationInsideGeometry: bool):
        """
        Setter for property: (bool) AnnotationInsideGeometry
          the annotation inside geometry   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayRegion
    ##   the display in non template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def DisplayRegion(self) -> bool:
        """
        Getter for property: (bool) DisplayRegion
          the display in non template   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayRegion

    ##   the display in non template   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DisplayRegion.setter
    def DisplayRegion(self, displayRegion: bool):
        """
        Setter for property: (bool) DisplayRegion
          the display in non template   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayRegionLabel
    ##   the display region label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def DisplayRegionLabel(self) -> bool:
        """
        Getter for property: (bool) DisplayRegionLabel
          the display region label   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayRegionLabel

    ##   the display region label   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DisplayRegionLabel.setter
    def DisplayRegionLabel(self, displayRegionLabel: bool):
        """
        Setter for property: (bool) DisplayRegionLabel
          the display region label   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceBetweenAnnotations
    ##   the distance between annotations   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def DistanceBetweenAnnotations(self) -> float:
        """
        Getter for property: (float) DistanceBetweenAnnotations
          the distance between annotations   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceBetweenAnnotations

    ##   the distance between annotations   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DistanceBetweenAnnotations.setter
    def DistanceBetweenAnnotations(self, distanceBetweenAnnotations: float):
        """
        Setter for property: (float) DistanceBetweenAnnotations
          the distance between annotations   
            
         
        """
        pass
    
    ## Getter for property: (float) EqualDimensionCompareTolerance
    ##   the equal dimension compare tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def EqualDimensionCompareTolerance(self) -> float:
        """
        Getter for property: (float) EqualDimensionCompareTolerance
          the equal dimension compare tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) EqualDimensionCompareTolerance

    ##   the equal dimension compare tolerance   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @EqualDimensionCompareTolerance.setter
    def EqualDimensionCompareTolerance(self, equalDimensionCompareTolerance: float):
        """
        Setter for property: (float) EqualDimensionCompareTolerance
          the equal dimension compare tolerance   
            
         
        """
        pass
    
    ## Getter for property: (float) FeetInchFractionForDimensionGreaterThan
    ##   the feet inch fraction for dimension greater than   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def FeetInchFractionForDimensionGreaterThan(self) -> float:
        """
        Getter for property: (float) FeetInchFractionForDimensionGreaterThan
          the feet inch fraction for dimension greater than   
            
         
        """
        pass
    
    ## Setter for property: (float) FeetInchFractionForDimensionGreaterThan

    ##   the feet inch fraction for dimension greater than   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @FeetInchFractionForDimensionGreaterThan.setter
    def FeetInchFractionForDimensionGreaterThan(self, feetInchFractionForDimensionGreaterThan: float):
        """
        Setter for property: (float) FeetInchFractionForDimensionGreaterThan
          the feet inch fraction for dimension greater than   
            
         
        """
        pass
    
    ## Getter for property: (bool) HideFeetInchMark
    ##   the hide feet inch mark   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def HideFeetInchMark(self) -> bool:
        """
        Getter for property: (bool) HideFeetInchMark
          the hide feet inch mark   
            
         
        """
        pass
    
    ## Setter for property: (bool) HideFeetInchMark

    ##   the hide feet inch mark   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @HideFeetInchMark.setter
    def HideFeetInchMark(self, hideFeetInchMark: bool):
        """
        Setter for property: (bool) HideFeetInchMark
          the hide feet inch mark   
            
         
        """
        pass
    
    ## Getter for property: (float) InchFractionToNearest
    ##   the inch fraction to nearest   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def InchFractionToNearest(self) -> float:
        """
        Getter for property: (float) InchFractionToNearest
          the inch fraction to nearest   
            
         
        """
        pass
    
    ## Setter for property: (float) InchFractionToNearest

    ##   the inch fraction to nearest   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @InchFractionToNearest.setter
    def InchFractionToNearest(self, inchFractionToNearest: float):
        """
        Setter for property: (float) InchFractionToNearest
          the inch fraction to nearest   
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumDistanceToGeometry
    ##   the maximum distance to geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def MaximumDistanceToGeometry(self) -> float:
        """
        Getter for property: (float) MaximumDistanceToGeometry
          the maximum distance to geometry   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumDistanceToGeometry

    ##   the maximum distance to geometry   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @MaximumDistanceToGeometry.setter
    def MaximumDistanceToGeometry(self, maximumDistanceToGeometry: float):
        """
        Setter for property: (float) MaximumDistanceToGeometry
          the maximum distance to geometry   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumDistanceToGeometry
    ##   the minimum distance to geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def MinimumDistanceToGeometry(self) -> float:
        """
        Getter for property: (float) MinimumDistanceToGeometry
          the minimum distance to geometry   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumDistanceToGeometry

    ##   the minimum distance to geometry   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @MinimumDistanceToGeometry.setter
    def MinimumDistanceToGeometry(self, minimumDistanceToGeometry: float):
        """
        Setter for property: (float) MinimumDistanceToGeometry
          the minimum distance to geometry   
            
         
        """
        pass
    
    ## Getter for property: (float) ReferenceGeometrySearchDistance
    ##   the reference geometry search distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def ReferenceGeometrySearchDistance(self) -> float:
        """
        Getter for property: (float) ReferenceGeometrySearchDistance
          the reference geometry search distance   
            
         
        """
        pass
    
    ## Setter for property: (float) ReferenceGeometrySearchDistance

    ##   the reference geometry search distance   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReferenceGeometrySearchDistance.setter
    def ReferenceGeometrySearchDistance(self, referenceGeometrySearchDistance: float):
        """
        Setter for property: (float) ReferenceGeometrySearchDistance
          the reference geometry search distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RegionColor
    ##   the region color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def RegionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RegionColor
          the region color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RegionColor

    ##   the region color   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @RegionColor.setter
    def RegionColor(self, regionColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RegionColor
          the region color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) RegionFont
    ##   the region font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Preferences.PartDrafting.FontType
    @property
    def RegionFont(self) -> NXOpen.Preferences.PartDrafting.FontType:
        """
        Getter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) RegionFont
          the region font   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) RegionFont

    ##   the region font   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @RegionFont.setter
    def RegionFont(self, regionFont: NXOpen.Preferences.PartDrafting.FontType):
        """
        Setter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) RegionFont
          the region font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) RegionWidth
    ##   the region width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Preferences.PartDrafting.WidthType
    @property
    def RegionWidth(self) -> NXOpen.Preferences.PartDrafting.WidthType:
        """
        Getter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) RegionWidth
          the region width   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) RegionWidth

    ##   the region width   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @RegionWidth.setter
    def RegionWidth(self, regionWidth: NXOpen.Preferences.PartDrafting.WidthType):
        """
        Setter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) RegionWidth
          the region width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentHiddenLineColor
    ##   the secondary content hidden line color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SecondaryContentHiddenLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentHiddenLineColor
          the secondary content hidden line color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentHiddenLineColor

    ##   the secondary content hidden line color   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SecondaryContentHiddenLineColor.setter
    def SecondaryContentHiddenLineColor(self, secondaryContentHiddenLineColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentHiddenLineColor
          the secondary content hidden line color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentHiddenLineFont
    ##   the secondary content hidden line font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Preferences.PartDrafting.FontType
    @property
    def SecondaryContentHiddenLineFont(self) -> NXOpen.Preferences.PartDrafting.FontType:
        """
        Getter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentHiddenLineFont
          the secondary content hidden line font   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentHiddenLineFont

    ##   the secondary content hidden line font   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SecondaryContentHiddenLineFont.setter
    def SecondaryContentHiddenLineFont(self, secondaryContentHiddenLineFont: NXOpen.Preferences.PartDrafting.FontType):
        """
        Setter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentHiddenLineFont
          the secondary content hidden line font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentHiddenLineWidth
    ##   the secondary content hidden line width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Preferences.PartDrafting.WidthType
    @property
    def SecondaryContentHiddenLineWidth(self) -> NXOpen.Preferences.PartDrafting.WidthType:
        """
        Getter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentHiddenLineWidth
          the secondary content hidden line width   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentHiddenLineWidth

    ##   the secondary content hidden line width   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SecondaryContentHiddenLineWidth.setter
    def SecondaryContentHiddenLineWidth(self, secondaryContentHiddenLineWidth: NXOpen.Preferences.PartDrafting.WidthType):
        """
        Setter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentHiddenLineWidth
          the secondary content hidden line width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentVisibleLineColor
    ##   the secondary content visible line color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SecondaryContentVisibleLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentVisibleLineColor
          the secondary content visible line color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentVisibleLineColor

    ##   the secondary content visible line color   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SecondaryContentVisibleLineColor.setter
    def SecondaryContentVisibleLineColor(self, secondaryContentVisibleLineColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SecondaryContentVisibleLineColor
          the secondary content visible line color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentVisibleLineFont
    ##   the secondary content visible line font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Preferences.PartDrafting.FontType
    @property
    def SecondaryContentVisibleLineFont(self) -> NXOpen.Preferences.PartDrafting.FontType:
        """
        Getter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentVisibleLineFont
          the secondary content visible line font   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentVisibleLineFont

    ##   the secondary content visible line font   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SecondaryContentVisibleLineFont.setter
    def SecondaryContentVisibleLineFont(self, secondaryContentVisibleLineFont: NXOpen.Preferences.PartDrafting.FontType):
        """
        Setter for property: (@link NXOpen.Preferences.PartDrafting.FontType NXOpen.Preferences.PartDrafting.FontType@endlink) SecondaryContentVisibleLineFont
          the secondary content visible line font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentVisibleLineWidth
    ##   the secondary content visible line width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Preferences.PartDrafting.WidthType
    @property
    def SecondaryContentVisibleLineWidth(self) -> NXOpen.Preferences.PartDrafting.WidthType:
        """
        Getter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentVisibleLineWidth
          the secondary content visible line width   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentVisibleLineWidth

    ##   the secondary content visible line width   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SecondaryContentVisibleLineWidth.setter
    def SecondaryContentVisibleLineWidth(self, secondaryContentVisibleLineWidth: NXOpen.Preferences.PartDrafting.WidthType):
        """
        Setter for property: (@link NXOpen.Preferences.PartDrafting.WidthType NXOpen.Preferences.PartDrafting.WidthType@endlink) SecondaryContentVisibleLineWidth
          the secondary content visible line width   
            
         
        """
        pass
    
    ##  Get the ordered rules list 
    ##  @return rules (List[str]):  Rules list .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRulesList(builder: AutomationPreferencesBuilder) -> List[str]:
        """
         Get the ordered rules list 
         @return rules (List[str]):  Rules list .
        """
        pass
    
    ##   Set the ordered rules list 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: nx_drawing_auto ("NX Drawing Automation")
    ##  Rules list 
    def SetRulesList(builder: AutomationPreferencesBuilder, rules: List[str]) -> None:
        """
          Set the ordered rules list 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Drafting::AutomationRuleBuilder NXOpen::Drafting::AutomationRuleBuilder@endlink  
## 
##   <br>  Created in NX9.0.0  <br> 

class AutomationRuleBuilder(NXOpen.TaggedObject): 
    """ Represents a <ja_class>NXOpen.Drafting.AutomationRuleBuilder</ja_class> """


    ## Getter for property: (bool) AllowInsideGeometry
    ##   the allow inside geometry option allows annotation inside geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AllowInsideGeometry(self) -> bool:
        """
        Getter for property: (bool) AllowInsideGeometry
          the allow inside geometry option allows annotation inside geometry   
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowInsideGeometry

    ##   the allow inside geometry option allows annotation inside geometry   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AllowInsideGeometry.setter
    def AllowInsideGeometry(self, allowInsideGeometry: bool):
        """
        Setter for property: (bool) AllowInsideGeometry
          the allow inside geometry option allows annotation inside geometry   
            
         
        """
        pass
    
    ## Getter for property: (float) EqualDimensionTolerance
    ##   the equal dimension comparison tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def EqualDimensionTolerance(self) -> float:
        """
        Getter for property: (float) EqualDimensionTolerance
          the equal dimension comparison tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) EqualDimensionTolerance

    ##   the equal dimension comparison tolerance   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @EqualDimensionTolerance.setter
    def EqualDimensionTolerance(self, equalDimensionTolerance: float):
        """
        Setter for property: (float) EqualDimensionTolerance
          the equal dimension comparison tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) HideFeetAndInchMarks
    ##   the hide feet and inch marks option Show/Hide feet and inch marks.  
    ##    True to hide and False to show   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def HideFeetAndInchMarks(self) -> bool:
        """
        Getter for property: (bool) HideFeetAndInchMarks
          the hide feet and inch marks option Show/Hide feet and inch marks.  
           True to hide and False to show   
         
        """
        pass
    
    ## Setter for property: (bool) HideFeetAndInchMarks

    ##   the hide feet and inch marks option Show/Hide feet and inch marks.  
    ##    True to hide and False to show   
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @HideFeetAndInchMarks.setter
    def HideFeetAndInchMarks(self, hideFeetAndInchMarks: bool):
        """
        Setter for property: (bool) HideFeetAndInchMarks
          the hide feet and inch marks option Show/Hide feet and inch marks.  
           True to hide and False to show   
         
        """
        pass
    
    ## Getter for property: (float) Increment
    ##   the increment Display dimension value in inches and fractions to nearest specified value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
          the increment Display dimension value in inches and fractions to nearest specified value   
            
         
        """
        pass
    
    ## Setter for property: (float) Increment

    ##   the increment Display dimension value in inches and fractions to nearest specified value   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
          the increment Display dimension value in inches and fractions to nearest specified value   
            
         
        """
        pass
    
    ## Getter for property: (float) LowerThreshold
    ##   the lower threshold display dimension value in feet, inches and fractions if
    ##             it is greater than the specified value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LowerThreshold(self) -> float:
        """
        Getter for property: (float) LowerThreshold
          the lower threshold display dimension value in feet, inches and fractions if
                    it is greater than the specified value   
            
         
        """
        pass
    
    ## Setter for property: (float) LowerThreshold

    ##   the lower threshold display dimension value in feet, inches and fractions if
    ##             it is greater than the specified value   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LowerThreshold.setter
    def LowerThreshold(self, lowerThreshold: float):
        """
        Setter for property: (float) LowerThreshold
          the lower threshold display dimension value in feet, inches and fractions if
                    it is greater than the specified value   
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumGapToGeometry
    ##   the maximum gap from the view geometry to the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def MaximumGapToGeometry(self) -> float:
        """
        Getter for property: (float) MaximumGapToGeometry
          the maximum gap from the view geometry to the annotation   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumGapToGeometry

    ##   the maximum gap from the view geometry to the annotation   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MaximumGapToGeometry.setter
    def MaximumGapToGeometry(self, maximumGapToGeometry: float):
        """
        Setter for property: (float) MaximumGapToGeometry
          the maximum gap from the view geometry to the annotation   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumGapBetweenAnnotations
    ##   the minimum gap between annotations   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def MinimumGapBetweenAnnotations(self) -> float:
        """
        Getter for property: (float) MinimumGapBetweenAnnotations
          the minimum gap between annotations   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumGapBetweenAnnotations

    ##   the minimum gap between annotations   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MinimumGapBetweenAnnotations.setter
    def MinimumGapBetweenAnnotations(self, minimumGapBetweenAnnotations: float):
        """
        Setter for property: (float) MinimumGapBetweenAnnotations
          the minimum gap between annotations   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumGapToGeometry
    ##   the minimum gap from the view geometry to the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def MinimumGapToGeometry(self) -> float:
        """
        Getter for property: (float) MinimumGapToGeometry
          the minimum gap from the view geometry to the annotation   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumGapToGeometry

    ##   the minimum gap from the view geometry to the annotation   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MinimumGapToGeometry.setter
    def MinimumGapToGeometry(self, minimumGapToGeometry: float):
        """
        Setter for property: (float) MinimumGapToGeometry
          the minimum gap from the view geometry to the annotation   
            
         
        """
        pass
    
    ## Getter for property: (float) ReferenceGeometryGapTolerance
    ##   the reference geometry search gap tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def ReferenceGeometryGapTolerance(self) -> float:
        """
        Getter for property: (float) ReferenceGeometryGapTolerance
          the reference geometry search gap tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) ReferenceGeometryGapTolerance

    ##   the reference geometry search gap tolerance   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ReferenceGeometryGapTolerance.setter
    def ReferenceGeometryGapTolerance(self, referenceGeometryGapTolerance: float):
        """
        Setter for property: (float) ReferenceGeometryGapTolerance
          the reference geometry search gap tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) RoundFeetAndInches
    ##   the round feet and inches determine wheather or not to display dimension value 
    ##             in inches and fractions to nearest specified value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def RoundFeetAndInches(self) -> bool:
        """
        Getter for property: (bool) RoundFeetAndInches
          the round feet and inches determine wheather or not to display dimension value 
                    in inches and fractions to nearest specified value   
            
         
        """
        pass
    
    ## Setter for property: (bool) RoundFeetAndInches

    ##   the round feet and inches determine wheather or not to display dimension value 
    ##             in inches and fractions to nearest specified value   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @RoundFeetAndInches.setter
    def RoundFeetAndInches(self, roundFeetAndInches: bool):
        """
        Setter for property: (bool) RoundFeetAndInches
          the round feet and inches determine wheather or not to display dimension value 
                    in inches and fractions to nearest specified value   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseFeetInchesAndFraction
    ##   the use feet inches and fraction determine wheather or not to display dimension value 
    ##             in feet, inches and fractions if it is greater than the specified value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def UseFeetInchesAndFraction(self) -> bool:
        """
        Getter for property: (bool) UseFeetInchesAndFraction
          the use feet inches and fraction determine wheather or not to display dimension value 
                    in feet, inches and fractions if it is greater than the specified value   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseFeetInchesAndFraction

    ##   the use feet inches and fraction determine wheather or not to display dimension value 
    ##             in feet, inches and fractions if it is greater than the specified value   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UseFeetInchesAndFraction.setter
    def UseFeetInchesAndFraction(self, useFeetInchesAndFraction: bool):
        """
        Setter for property: (bool) UseFeetInchesAndFraction
          the use feet inches and fraction determine wheather or not to display dimension value 
                    in feet, inches and fractions if it is greater than the specified value   
            
         
        """
        pass
    
    ##  The automation rules in the order of decreasing priorities. So, the first
    ##             rule in the VLA has the highest priority 
    ##  @return rules (List[str]):  Rules list .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRulesList(builder: AutomationRuleBuilder) -> List[str]:
        """
         The automation rules in the order of decreasing priorities. So, the first
                    rule in the VLA has the highest priority 
         @return rules (List[str]):  Rules list .
        """
        pass
    
    ##  The set of order list 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_drawing_auto ("NX Drawing Automation")
    ##  Rules list 
    def SetRulesList(builder: AutomationRuleBuilder, rules: List[str]) -> None:
        """
         The set of order list 
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::Drafting::BaseEditSettingsBuilder NXOpen::Drafting::BaseEditSettingsBuilder@endlink .
##     It provides an interface for editing settings.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BaseEditSettingsBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Drafting.BaseEditSettingsBuilder</ja_class>.
    It provides an interface for editing settings.
    """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##         Represents a paste in Drafting.
##      <br> To create a new instance of this class, use @link NXOpen::Drafting::DraftingApplicationManager::CreateCutCopyPasteBuilder  NXOpen::Drafting::DraftingApplicationManager::CreateCutCopyPasteBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Transform.DeltaEnum </term> <description> 
##  
## ReferenceWcsWorkPart </description> </item> 
## 
## <item><term> 
##  
## Transform.DeltaXc.Value </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## Transform.DeltaYc.Value </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## Transform.DeltaZc.Value </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## Transform.Option </term> <description> 
##  
## Distance </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class CutCopyPasteBuilder(NXOpen.Builder): 
    """
        Represents a paste in Drafting.
    """


    ##  Specifies the copy cut operation type. 
    ##  Copy type 
    class TypeOperation(Enum):
        """
        Members Include: <Copy> <Cut>
        """
        Copy: int
        Cut: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CutCopyPasteBuilder.TypeOperation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the paste type. 
    ##  Transform type 
    class TypePaste(Enum):
        """
        Members Include: <Transform> <Tracking>
        """
        Transform: int
        Tracking: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CutCopyPasteBuilder.TypePaste:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CutCopyPasteLeaderBuilder NXOpen.Drafting.CutCopyPasteLeaderBuilder@endlink) CutCopyPasteLeader
    ##   the leader builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return CutCopyPasteLeaderBuilder
    @property
    def CutCopyPasteLeader(self) -> CutCopyPasteLeaderBuilder:
        """
        Getter for property: (@link CutCopyPasteLeaderBuilder NXOpen.Drafting.CutCopyPasteLeaderBuilder@endlink) CutCopyPasteLeader
          the leader builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView
    ##   the destination view.  
    ##     Either a drafting view or sheet view.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.View
    @property
    def DestinationView(self) -> NXOpen.View:
        """
        Getter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView
          the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView

    ##   the destination view.  
    ##     Either a drafting view or sheet view.   
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DestinationView.setter
    def DestinationView(self, destinationView: NXOpen.View):
        """
        Setter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView
          the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ObjectsToCopy
    ##   the objects list to copy.  
    ##    May include drafting geometry, sketch objects
    ##             and simple annotations. Note that PMI, feature, view, and table objects
    ##             are not supported by this class.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def ObjectsToCopy(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ObjectsToCopy
          the objects list to copy.  
           May include drafting geometry, sketch objects
                    and simple annotations. Note that PMI, feature, view, and table objects
                    are not supported by this class.   
         
        """
        pass
    
    ## Getter for property: (@link CutCopyPasteBuilder.TypeOperation NXOpen.Drafting.CutCopyPasteBuilder.TypeOperation@endlink) Originals
    ##   the operation type.  
    ##    If it is copy, we will keept the originals. If it is cut, we will delete the originals   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return CutCopyPasteBuilder.TypeOperation
    @property
    def Originals(self) -> CutCopyPasteBuilder.TypeOperation:
        """
        Getter for property: (@link CutCopyPasteBuilder.TypeOperation NXOpen.Drafting.CutCopyPasteBuilder.TypeOperation@endlink) Originals
          the operation type.  
           If it is copy, we will keept the originals. If it is cut, we will delete the originals   
         
        """
        pass
    
    ## Setter for property: (@link CutCopyPasteBuilder.TypeOperation NXOpen.Drafting.CutCopyPasteBuilder.TypeOperation@endlink) Originals

    ##   the operation type.  
    ##    If it is copy, we will keept the originals. If it is cut, we will delete the originals   
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Originals.setter
    def Originals(self, originals: CutCopyPasteBuilder.TypeOperation):
        """
        Setter for property: (@link CutCopyPasteBuilder.TypeOperation NXOpen.Drafting.CutCopyPasteBuilder.TypeOperation@endlink) Originals
          the operation type.  
           If it is copy, we will keept the originals. If it is cut, we will delete the originals   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) OutputObjects
    ##    the output Objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def OutputObjects(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) OutputObjects
           the output Objects   
            
         
        """
        pass
    
    ## Getter for property: (@link CutCopyPasteBuilder.TypePaste NXOpen.Drafting.CutCopyPasteBuilder.TypePaste@endlink) PasteType
    ##   the paste type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return CutCopyPasteBuilder.TypePaste
    @property
    def PasteType(self) -> CutCopyPasteBuilder.TypePaste:
        """
        Getter for property: (@link CutCopyPasteBuilder.TypePaste NXOpen.Drafting.CutCopyPasteBuilder.TypePaste@endlink) PasteType
          the paste type   
            
         
        """
        pass
    
    ## Setter for property: (@link CutCopyPasteBuilder.TypePaste NXOpen.Drafting.CutCopyPasteBuilder.TypePaste@endlink) PasteType

    ##   the paste type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @PasteType.setter
    def PasteType(self, pasteType: CutCopyPasteBuilder.TypePaste):
        """
        Setter for property: (@link CutCopyPasteBuilder.TypePaste NXOpen.Drafting.CutCopyPasteBuilder.TypePaste@endlink) PasteType
          the paste type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneToRestrictMotion
    ##    the plane to restrict motion   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Plane
    @property
    def PlaneToRestrictMotion(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneToRestrictMotion
           the plane to restrict motion   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneToRestrictMotion

    ##    the plane to restrict motion   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @PlaneToRestrictMotion.setter
    def PlaneToRestrictMotion(self, plan: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneToRestrictMotion
           the plane to restrict motion   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.ModlMotion NXOpen.GeometricUtilities.ModlMotion@endlink) Transform
    ##   the motion from the default paste position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.GeometricUtilities.ModlMotion
    @property
    def Transform(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.ModlMotion NXOpen.GeometricUtilities.ModlMotion@endlink) Transform
          the motion from the default paste position   
            
         
        """
        pass
    
    ##  Get the default to point. The drop location. 
    ##  @return dropLocation (@link NXOpen.Point3d NXOpen.Point3d@endlink):  the drop location .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultToPoint(builder: CutCopyPasteBuilder) -> NXOpen.Point3d:
        """
         Get the default to point. The drop location. 
         @return dropLocation (@link NXOpen.Point3d NXOpen.Point3d@endlink):  the drop location .
        """
        pass
    
    ##  Make the initial drop. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    @staticmethod
    def InitPaste(builder: CutCopyPasteBuilder) -> None:
        """
         Make the initial drop. 
        """
        pass
    
    ##  Set the default to point.  The drop location. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  the drop location 
    def SetDefaultToPoint(builder: CutCopyPasteBuilder, dropLocation: NXOpen.Point3d) -> None:
        """
         Set the default to point.  The drop location. 
        """
        pass
    
    ##  Set the final motion from the drop location. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  rotational part of motion 
    def SetMoveOnCommit(builder: CutCopyPasteBuilder, rot: NXOpen.Matrix3x3, trans: NXOpen.Vector3d) -> None:
        """
         Set the final motion from the drop location. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##         Represents a Drafting Paste, especially when reassociating a leader on paste.
##     
## 
##   <br>  Created in NX8.0.0  <br> 

class CutCopyPasteLeaderBuilder(NXOpen.TaggedObject): 
    """
        Represents a Drafting Paste, especially when reassociating a leader on paste.
    """


    ## Getter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView
    ##   the destination view.  
    ##     Either a drafting view or sheet view.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.View
    @property
    def DestinationView(self) -> NXOpen.View:
        """
        Getter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView
          the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView

    ##   the destination view.  
    ##     Either a drafting view or sheet view.   
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DestinationView.setter
    def DestinationView(self, destinationView: NXOpen.View):
        """
        Setter for property: (@link NXOpen.View NXOpen.View@endlink) DestinationView
          the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    
    ## Getter for property: (bool) IsLeaderSelection
    ##   the variable of is leader selection or not  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def IsLeaderSelection(self) -> bool:
        """
        Getter for property: (bool) IsLeaderSelection
          the variable of is leader selection or not  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsLeaderSelection

    ##   the variable of is leader selection or not  
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @IsLeaderSelection.setter
    def IsLeaderSelection(self, isLeaderSelection: bool):
        """
        Setter for property: (bool) IsLeaderSelection
          the variable of is leader selection or not  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) LeaderSelection
    ##   the selection to reassociate single leader   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def LeaderSelection(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) LeaderSelection
          the selection to reassociate single leader   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReassociateLeader
    ##   the flag to reassociate a leader   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def ReassociateLeader(self) -> bool:
        """
        Getter for property: (bool) ReassociateLeader
          the flag to reassociate a leader   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReassociateLeader

    ##   the flag to reassociate a leader   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReassociateLeader.setter
    def ReassociateLeader(self, reassociateLeader: bool):
        """
        Setter for property: (bool) ReassociateLeader
          the flag to reassociate a leader   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) Selection
    ##   the selection to reassociate leader   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def Selection(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) Selection
          the selection to reassociate leader   
            
         
        """
        pass
    
    ##  Set the final motion from the drop location. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  rotational part of motion 
    def SetMoveOnCommit(builder: CutCopyPasteLeaderBuilder, rot: NXOpen.Matrix3x3, trans: NXOpen.Vector3d) -> None:
        """
         Set the final motion from the drop location. 
        """
        pass
    
import NXOpen
##  This class is used to distribute annotations associated to a view.  <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateDistributeAnnotationsBuilder  NXOpen::Drafting::AutomationManager::CreateDistributeAnnotationsBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DistributeAnnotationsBuilder(NXOpen.Builder): 
    """ This class is used to distribute annotations associated to a view. """


    ## Getter for property: (@link SelectDraftingViewList NXOpen.Drawings.SelectDraftingViewList@endlink) Views
    ##   the views in which to distribute annotations.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return SelectDraftingViewList
    @property
    def Views(self) -> SelectDraftingViewList:
        """
        Getter for property: (@link SelectDraftingViewList NXOpen.Drawings.SelectDraftingViewList@endlink) Views
          the views in which to distribute annotations.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents an object that manages drafting objects and member views.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class DraftingApplicationManager(NXOpen.Object): 
    """ Represents an object that manages drafting objects and member views. """


    ##  Returns the TitleBlockCollection belonging to this part 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @link NXOpen.Annotations.TitleBlockCollection NXOpen.Annotations.TitleBlockCollection@endlink
    @property
    def TitleBlocks() -> NXOpen.Annotations.TitleBlockCollection:
        """
         Returns the TitleBlockCollection belonging to this part 
        """
        pass
    
    ##  Creates the CutCopyPaste builder 
    ##  @return builder (@link CutCopyPasteBuilder NXOpen.Drafting.CutCopyPasteBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def CreateCutCopyPasteBuilder(objectValue: DraftingApplicationManager) -> CutCopyPasteBuilder:
        """
         Creates the CutCopyPaste builder 
         @return builder (@link CutCopyPasteBuilder NXOpen.Drafting.CutCopyPasteBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::MoveToDrawingViewBuilder NXOpen::Drafting::MoveToDrawingViewBuilder@endlink  
    ##  @return builder (@link MoveToDrawingViewBuilder NXOpen.Drafting.MoveToDrawingViewBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateMoveToDrawingViewBuilder(part: DraftingApplicationManager) -> MoveToDrawingViewBuilder:
        """
         Creates a @link NXOpen::Drafting::MoveToDrawingViewBuilder NXOpen::Drafting::MoveToDrawingViewBuilder@endlink  
         @return builder (@link MoveToDrawingViewBuilder NXOpen.Drafting.MoveToDrawingViewBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::SmashDrawingViewBuilder NXOpen::Drafting::SmashDrawingViewBuilder@endlink  
    ##  @return builder (@link SmashDrawingViewBuilder NXOpen.Drafting.SmashDrawingViewBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    def CreateSmashDrawingViewBuilder(part: DraftingApplicationManager) -> SmashDrawingViewBuilder:
        """
         Creates a @link NXOpen::Drafting::SmashDrawingViewBuilder NXOpen::Drafting::SmashDrawingViewBuilder@endlink  
         @return builder (@link SmashDrawingViewBuilder NXOpen.Drafting.SmashDrawingViewBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents callback data for the drawing automation wizard. 
## 
##   <br>  Created in NX8.5.3  <br> 

class DrawingAutomationWizard(NXOpen.TransientObject): 
    """ Represents callback data for the drawing automation wizard. """


    ## Getter for property: (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink) Builder
    ##   the drawing automation wizard builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## @return DrawingCreationWizardBuilder
    @property
    def Builder(self) -> DrawingCreationWizardBuilder:
        """
        Getter for property: (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink) Builder
          the drawing automation wizard builder   
            
         
        """
        pass
    
    ## Setter for property: (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink) Builder

    ##   the drawing automation wizard builder   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    @Builder.setter
    def Builder(self, builder: DrawingCreationWizardBuilder):
        """
        Setter for property: (@link DrawingCreationWizardBuilder NXOpen.Drafting.DrawingCreationWizardBuilder@endlink) Builder
          the drawing automation wizard builder   
            
         
        """
        pass
    
    ## Getter for property: (bool) ContinueProcessing
    ##   the flag denoting whether or not to create the booklet in the current session   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## @return bool
    @property
    def ContinueProcessing(self) -> bool:
        """
        Getter for property: (bool) ContinueProcessing
          the flag denoting whether or not to create the booklet in the current session   
            
         
        """
        pass
    
    ## Setter for property: (bool) ContinueProcessing

    ##   the flag denoting whether or not to create the booklet in the current session   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    @ContinueProcessing.setter
    def ContinueProcessing(self, continueProcessing: bool):
        """
        Setter for property: (bool) ContinueProcessing
          the flag denoting whether or not to create the booklet in the current session   
            
         
        """
        pass
    
    ## Getter for property: (int) ErrorCode
    ##   the error code to be returned from the callback   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## @return int
    @property
    def ErrorCode(self) -> int:
        """
        Getter for property: (int) ErrorCode
          the error code to be returned from the callback   
            
         
        """
        pass
    
    ## Setter for property: (int) ErrorCode

    ##   the error code to be returned from the callback   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    @ErrorCode.setter
    def ErrorCode(self, errorCode: int):
        """
        Setter for property: (int) ErrorCode
          the error code to be returned from the callback   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) Part
    ##   the part from which the booklet drawings are created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## @return NXOpen.Part
    @property
    def Part(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) Part
          the part from which the booklet drawings are created   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) Part

    ##   the part from which the booklet drawings are created   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    @Part.setter
    def Part(self, part: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) Part
          the part from which the booklet drawings are created   
            
         
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(data: DrawingAutomationWizard) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.PDM
## 
##     Represents a @link NXOpen::Drafting::DrawingCreationWizardBuilder NXOpen::Drafting::DrawingCreationWizardBuilder@endlink .  This class is
##     used to create Booklets (i.e. a set of fully populated drawings).  The builder operates
##     in both create and edit modes as well as in native and managed (Teamcenter) modes.  The
##     following information is important when using this builder in edit mode:<br/>
##     <ul>
##         <li>
##         Native Mode
##             <ul>
##                 <li>
##                 The @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetFolder NXOpen::Drafting::DrawingCreationWizardBuilder::SetFolder@endlink  must be the first thing set after creating the builder.
##                 Setting this will populate the builder with the booklet's information.
##                 </li>
##             </ul>
##         </li>
##         <li>
##         Managed Mode
##             <ul>
##                 <li>
##                 The @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetRevision NXOpen::Drafting::DrawingCreationWizardBuilder::SetRevision@endlink  must be the first things set after
##                 creating the builder (in that order).  The setting of the @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetRevision NXOpen::Drafting::DrawingCreationWizardBuilder::SetRevision@endlink  will populate the builder with the booklet's information.
##                 </li>
##             </ul>
##         </li>
##     </ul>
##      <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateDrawingCreationWizardBuilder  NXOpen::Drafting::AutomationManager::CreateDrawingCreationWizardBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ApplyTemplateToAll </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.0.0  <br> 

class DrawingCreationWizardBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.Drafting.DrawingCreationWizardBuilder</ja_class>.  This class is
    used to create Booklets (i.e. a set of fully populated drawings).  The builder operates
    in both create and edit modes as well as in native and managed (Teamcenter) modes.  The
    following information is important when using this builder in edit mode:<br/>
    <ul>
        <li>
        Native Mode
            <ul>
                <li>
                The <ja_property_set>NXOpen.Drafting.DrawingCreationWizardBuilder.Folder</ja_property_set> must be the first thing set after creating the builder.
                Setting this will populate the builder with the booklet's information.
                </li>
            </ul>
        </li>
        <li>
        Managed Mode
            <ul>
                <li>
                The <ja_property_set>NXOpen.Drafting.DrawingCreationWizardBuilder.Number</ja_property_set> and <ja_property_set>NXOpen.Drafting.DrawingCreationWizardBuilder.Revision</ja_property_set> must be the first things set after
                creating the builder (in that order).  The setting of the <ja_property_set>NXOpen.Drafting.DrawingCreationWizardBuilder.Revision</ja_property_set> will populate the builder with the booklet's information.
                </li>
            </ul>
        </li>
    </ul>
    """


    ## Getter for property: (bool) ApplyTemplateToAll
    ##   the flag which controls the behavior of setting @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink 
    ##             on an item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink .  
    ##    When set to true the builder
    ##             will respond to the setting of @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on an item in
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  by setting the same value on
    ##             @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on all of the other items in
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def ApplyTemplateToAll(self) -> bool:
        """
        Getter for property: (bool) ApplyTemplateToAll
          the flag which controls the behavior of setting @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink 
                    on an item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink .  
           When set to true the builder
                    will respond to the setting of @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on an item in
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  by setting the same value on
                    @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on all of the other items in
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink    
         
        """
        pass
    
    ## Setter for property: (bool) ApplyTemplateToAll

    ##   the flag which controls the behavior of setting @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink 
    ##             on an item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink .  
    ##    When set to true the builder
    ##             will respond to the setting of @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on an item in
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  by setting the same value on
    ##             @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on all of the other items in
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink    
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ApplyTemplateToAll.setter
    def ApplyTemplateToAll(self, applyTemplateToAll: bool):
        """
        Setter for property: (bool) ApplyTemplateToAll
          the flag which controls the behavior of setting @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink 
                    on an item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink .  
           When set to true the builder
                    will respond to the setting of @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on an item in
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  by setting the same value on
                    @link NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate@endlink  on all of the other items in
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink    
         
        """
        pass
    
    ## Getter for property: (@link AttributeItemBuilderList NXOpen.Drafting.AttributeItemBuilderList@endlink) Attributes
    ##   the attributes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return AttributeItemBuilderList
    @property
    def Attributes(self) -> AttributeItemBuilderList:
        """
        Getter for property: (@link AttributeItemBuilderList NXOpen.Drafting.AttributeItemBuilderList@endlink) Attributes
          the attributes.  
             
         
        """
        pass
    
    ## Getter for property: (str) DetailID
    ##   the detail id.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DetailID(self) -> str:
        """
        Getter for property: (str) DetailID
          the detail id.  
             
         
        """
        pass
    
    ## Setter for property: (str) DetailID

    ##   the detail id.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DetailID.setter
    def DetailID(self, detailID: str):
        """
        Setter for property: (str) DetailID
          the detail id.  
             
         
        """
        pass
    
    ## Getter for property: (str) Discipline
    ##   the discipline.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
          the discipline.  
             
         
        """
        pass
    
    ## Setter for property: (str) Discipline

    ##   the discipline.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
          the discipline.  
             
         
        """
        pass
    
    ## Getter for property: (str) DrawingStyle
    ##   the drawing style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DrawingStyle(self) -> str:
        """
        Getter for property: (str) DrawingStyle
          the drawing style.  
             
         
        """
        pass
    
    ## Setter for property: (str) DrawingStyle

    ##   the drawing style.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DrawingStyle.setter
    def DrawingStyle(self, drawingStyle: str):
        """
        Setter for property: (str) DrawingStyle
          the drawing style.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) ExcludedContent
    ##   the excluded content.  
    ##    Setting a component into @link NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  
    ##             will cause that component to be removed from @link NXOpen::Drafting::PrimaryContentItemBuilder::Content NXOpen::Drafting::PrimaryContentItemBuilder::Content@endlink 
    ##             of each item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  and 
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  if they contain that component.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def ExcludedContent(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) ExcludedContent
          the excluded content.  
           Setting a component into @link NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  
                    will cause that component to be removed from @link NXOpen::Drafting::PrimaryContentItemBuilder::Content NXOpen::Drafting::PrimaryContentItemBuilder::Content@endlink 
                    of each item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  and 
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  if they contain that component.   
         
        """
        pass
    
    ## Getter for property: (str) Folder
    ##   the folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Folder(self) -> str:
        """
        Getter for property: (str) Folder
          the folder.  
             
         
        """
        pass
    
    ## Setter for property: (str) Folder

    ##   the folder.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Folder.setter
    def Folder(self, foldername: str):
        """
        Setter for property: (str) Folder
          the folder.  
             
         
        """
        pass
    
    ## Getter for property: (str) IntroductoryTemplate
    ##   the introductory template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def IntroductoryTemplate(self) -> str:
        """
        Getter for property: (str) IntroductoryTemplate
          the introductory template.  
             
         
        """
        pass
    
    ## Setter for property: (str) IntroductoryTemplate

    ##   the introductory template.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @IntroductoryTemplate.setter
    def IntroductoryTemplate(self, introductoryTemplate: str):
        """
        Setter for property: (str) IntroductoryTemplate
          the introductory template.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Getter for property: (str) Number
    ##   the number.  
    ##    This property is only used in managed mode and must be set before anything else.    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Number(self) -> str:
        """
        Getter for property: (str) Number
          the number.  
           This property is only used in managed mode and must be set before anything else.    
         
        """
        pass
    
    ## Setter for property: (str) Number

    ##   the number.  
    ##    This property is only used in managed mode and must be set before anything else.    
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Number.setter
    def Number(self, number: str):
        """
        Setter for property: (str) Number
          the number.  
           This property is only used in managed mode and must be set before anything else.    
         
        """
        pass
    
    ## Getter for property: (@link PrimaryContentItemBuilderList NXOpen.Drafting.PrimaryContentItemBuilderList@endlink) PrimaryContent
    ##   the primary content.  
    ##    Setting a component into @link NXOpen::Drafting::PrimaryContentItemBuilder::Content NXOpen::Drafting::PrimaryContentItemBuilder::Content@endlink  of an item in
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  will cause that component to be removed from 
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  and 
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  if they contain that component.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return PrimaryContentItemBuilderList
    @property
    def PrimaryContent(self) -> PrimaryContentItemBuilderList:
        """
        Getter for property: (@link PrimaryContentItemBuilderList NXOpen.Drafting.PrimaryContentItemBuilderList@endlink) PrimaryContent
          the primary content.  
           Setting a component into @link NXOpen::Drafting::PrimaryContentItemBuilder::Content NXOpen::Drafting::PrimaryContentItemBuilder::Content@endlink  of an item in
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  will cause that component to be removed from 
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  and 
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  if they contain that component.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) References
    ##   the references.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def References(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) References
          the references.  
             
         
        """
        pass
    
    ## Getter for property: (str) Revision
    ##   the revision.  
    ##    This is only used in managed mode. In edit mode it must be set after the @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
    ##             is set it will populate the builder with the booklet's information.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Revision(self) -> str:
        """
        Getter for property: (str) Revision
          the revision.  
           This is only used in managed mode. In edit mode it must be set after the @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
                    is set it will populate the builder with the booklet's information.   
         
        """
        pass
    
    ## Setter for property: (str) Revision

    ##   the revision.  
    ##    This is only used in managed mode. In edit mode it must be set after the @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
    ##             is set it will populate the builder with the booklet's information.   
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Revision.setter
    def Revision(self, revision: str):
        """
        Setter for property: (str) Revision
          the revision.  
           This is only used in managed mode. In edit mode it must be set after the @link NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber@endlink  and at the time
                    is set it will populate the builder with the booklet's information.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SecondaryContent
    ##   the secondary content.  
    ##    Setting a component into @link NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  
    ##             will cause that component to be removed from @link NXOpen::Drafting::PrimaryContentItemBuilder::Content NXOpen::Drafting::PrimaryContentItemBuilder::Content@endlink 
    ##             of each item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  and 
    ##             @link NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  if they contain that component.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def SecondaryContent(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SecondaryContent
          the secondary content.  
           Setting a component into @link NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent@endlink  
                    will cause that component to be removed from @link NXOpen::Drafting::PrimaryContentItemBuilder::Content NXOpen::Drafting::PrimaryContentItemBuilder::Content@endlink 
                    of each item in @link NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent@endlink  and 
                    @link NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent@endlink  if they contain that component.   
         
        """
        pass
    
    ##  Returns the summary.  This is in HTML format. 
    ##  @return summary (List[str]): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetSummary(self) -> List[str]:
        """
         Returns the summary.  This is in HTML format. 
         @return summary (List[str]): .
        """
        pass
    
    ##  Sets @link NXOpen::PDM::ObjectCreateBuilder NXOpen::PDM::ObjectCreateBuilder@endlink  
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ## <param name="objectCreateBuilder"> (@link NXOpen.PDM.ObjectCreateBuilder NXOpen.PDM.ObjectCreateBuilder@endlink) </param>
    def SetObjectCreateBuilder(builder: DrawingCreationWizardBuilder, objectCreateBuilder: NXOpen.PDM.ObjectCreateBuilder) -> None:
        """
         Sets @link NXOpen::PDM::ObjectCreateBuilder NXOpen::PDM::ObjectCreateBuilder@endlink  
        """
        pass
    
    ##  Sets the summary 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: nx_drawing_auto ("NX Drawing Automation")
    ##  
    def SetSummary(self, summary: List[str]) -> None:
        """
         Sets the summary 
        """
        pass
    
import NXOpen
##  This builder allows the user to extract contents from a sheet and transfer them to a new Drawing
##         view, also provide some other options for view creation
##       <br> To create a new instance of this class, use @link NXOpen::Drafting::DraftingApplicationManager::CreateMoveToDrawingViewBuilder  NXOpen::Drafting::DraftingApplicationManager::CreateMoveToDrawingViewBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ViewScale.Denominator </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## ViewScale.Numerator </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## ViewScale.ScaleType </term> <description> 
##  
## Ratio </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.AngleSetting.Angle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.AngleSetting.Associative </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.AngleSetting.EvaluationPlane </term> <description> 
##  
## DrawingSheet </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleOrientation.HingeLine.ReverseDirection </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleOrientation.HingeLine.VectorOption </term> <description> 
##  
## Inferred </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleOrientation.Ovt.AssociativeOrientation </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## XCoordinate </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## YCoordinate </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.5.0  <br> 

class MoveToDrawingViewBuilder(NXOpen.Builder): 
    """ This builder allows the user to extract contents from a sheet and transfer them to a new Drawing
        view, also provide some other options for view creation
     """


    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectObjects
    ##   the select objects from the current sheet  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectObjects(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectObjects
          the select objects from the current sheet  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
    ##   the select point to calculate the new created drawing view's reference point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Point
    @property
    def SelectPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
          the select point to calculate the new created drawing view's reference point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint

    ##   the select point to calculate the new created drawing view's reference point  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SelectPoint.setter
    def SelectPoint(self, selectPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
          the select point to calculate the new created drawing view's reference point  
            
         
        """
        pass
    
    ## Getter for property: (@link View2dOrientBuilder NXOpen.Drawings.View2dOrientBuilder@endlink) TwoDOrientation
    ##   the view orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return View2dOrientBuilder
    @property
    def TwoDOrientation(self) -> View2dOrientBuilder:
        """
        Getter for property: (@link View2dOrientBuilder NXOpen.Drawings.View2dOrientBuilder@endlink) TwoDOrientation
          the view orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewScaleBuilder NXOpen.Drawings.ViewScaleBuilder@endlink) ViewScale
    ##   the view scale   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ViewScaleBuilder
    @property
    def ViewScale(self) -> ViewScaleBuilder:
        """
        Getter for property: (@link ViewScaleBuilder NXOpen.Drawings.ViewScaleBuilder@endlink) ViewScale
          the view scale   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewStyleBuilder NXOpen.Drawings.ViewStyleBuilder@endlink) ViewStyle
    ##   the view style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ViewStyleBuilder
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: (@link ViewStyleBuilder NXOpen.Drawings.ViewStyleBuilder@endlink) ViewStyle
          the view style   
            
         
        """
        pass
    
    ## Getter for property: (float) XCoordinate
    ##   the x coordinate to calculate the new created drawing view's reference point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def XCoordinate(self) -> float:
        """
        Getter for property: (float) XCoordinate
          the x coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    
    ## Setter for property: (float) XCoordinate

    ##   the x coordinate to calculate the new created drawing view's reference point  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @XCoordinate.setter
    def XCoordinate(self, xCoordinate: float):
        """
        Setter for property: (float) XCoordinate
          the x coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    
    ## Getter for property: (float) YCoordinate
    ##   the y coordinate to calculate the new created drawing view's reference point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def YCoordinate(self) -> float:
        """
        Getter for property: (float) YCoordinate
          the y coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    
    ## Setter for property: (float) YCoordinate

    ##   the y coordinate to calculate the new created drawing view's reference point  
    ##     
    ##  
    ## Setter License requirements: nx_layout ("NX Layout")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @YCoordinate.setter
    def YCoordinate(self, yCoordinate: float):
        """
        Setter for property: (float) YCoordinate
          the y coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents a @link NXOpen::Drafting::PreferencesBuilder NXOpen::Drafting::PreferencesBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Drafting::SettingsManager::CreatePreferencesBuilder  NXOpen::Drafting::SettingsManager::CreatePreferencesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.AngleSetting.Angle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.AngleSetting.Associative </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.AngleSetting.EvaluationPlane </term> <description> 
##  
## DrawingSheet </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.Scale.Denominator </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.Scale.Numerator </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleGeneral.Scale.ScaleType </term> <description> 
##  
## Ratio </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleOrientation.HingeLine.ReverseDirection </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleOrientation.HingeLine.VectorOption </term> <description> 
##  
## Inferred </description> </item> 
## 
## <item><term> 
##  
## ViewStyle.ViewStyleOrientation.Ovt.AssociativeOrientation </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Drafting.PreferencesBuilder</ja_class> builder """


    ## Getter for property: (@link NXOpen.Annotations.OriginAlignmentBuilder NXOpen.Annotations.OriginAlignmentBuilder@endlink) AnnotationOriginAlignment
    ##   the annotation origin alignment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Annotations.OriginAlignmentBuilder
    @property
    def AnnotationOriginAlignment(self) -> NXOpen.Annotations.OriginAlignmentBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginAlignmentBuilder NXOpen.Annotations.OriginAlignmentBuilder@endlink) AnnotationOriginAlignment
          the annotation origin alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) AnnotationStyle
    ##   the annotation style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.StyleBuilder
    @property
    def AnnotationStyle(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) AnnotationStyle
          the annotation style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link AssemblyCreationSettingsBuilder NXOpen.Layout2d.AssemblyCreationSettingsBuilder@endlink) AssemblyCreationSettingsBuilder
    ##   the assembly creation from 2d component builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return AssemblyCreationSettingsBuilder
    @property
    def AssemblyCreationSettingsBuilder(self) -> AssemblyCreationSettingsBuilder:
        """
        Getter for property: (@link AssemblyCreationSettingsBuilder NXOpen.Layout2d.AssemblyCreationSettingsBuilder@endlink) AssemblyCreationSettingsBuilder
          the assembly creation from 2d component builder   
            
         
        """
        pass
    
    ## Getter for property: (@link AutomationBookletBuilder NXOpen.Drawings.AutomationBookletBuilder@endlink) AutomationBooklet
    ##      the AutomationBookletBuilder builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return AutomationBookletBuilder
    @property
    def AutomationBooklet(self) -> AutomationBookletBuilder:
        """
        Getter for property: (@link AutomationBookletBuilder NXOpen.Drawings.AutomationBookletBuilder@endlink) AutomationBooklet
             the AutomationBookletBuilder builder   
            
         
        """
        pass
    
    ## Getter for property: (@link AutomationRuleBuilder NXOpen.Drafting.AutomationRuleBuilder@endlink) AutomationRule
    ##   the drafting automation rule builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return AutomationRuleBuilder
    @property
    def AutomationRule(self) -> AutomationRuleBuilder:
        """
        Getter for property: (@link AutomationRuleBuilder NXOpen.Drafting.AutomationRuleBuilder@endlink) AutomationRule
          the drafting automation rule builder   
            
         
        """
        pass
    
    ## Getter for property: (@link AutomationTemplateRegionBuilder NXOpen.Drawings.AutomationTemplateRegionBuilder@endlink) AutomationTemplateRegion
    ##      the AutomationTemplateRegion builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return AutomationTemplateRegionBuilder
    @property
    def AutomationTemplateRegion(self) -> AutomationTemplateRegionBuilder:
        """
        Getter for property: (@link AutomationTemplateRegionBuilder NXOpen.Drawings.AutomationTemplateRegionBuilder@endlink) AutomationTemplateRegion
             the AutomationTemplateRegion builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.BendTableSettingsBuilder NXOpen.Annotations.BendTableSettingsBuilder@endlink) BendTable
    ##   the Bend table settings builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.BendTableSettingsBuilder
    @property
    def BendTable(self) -> NXOpen.Annotations.BendTableSettingsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.BendTableSettingsBuilder NXOpen.Annotations.BendTableSettingsBuilder@endlink) BendTable
          the Bend table settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link BorderAndZoneStyleBuilder NXOpen.Drawings.BorderAndZoneStyleBuilder@endlink) BorderAndZoneStyle
    ##   the border and zone style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return BorderAndZoneStyleBuilder
    @property
    def BorderAndZoneStyle(self) -> BorderAndZoneStyleBuilder:
        """
        Getter for property: (@link BorderAndZoneStyleBuilder NXOpen.Drawings.BorderAndZoneStyleBuilder@endlink) BorderAndZoneStyle
          the border and zone style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.CommonWorkflowBuilder NXOpen.Annotations.CommonWorkflowBuilder@endlink) CommonWorkflow
    ##   the common workflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.CommonWorkflowBuilder
    @property
    def CommonWorkflow(self) -> NXOpen.Annotations.CommonWorkflowBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.CommonWorkflowBuilder NXOpen.Annotations.CommonWorkflowBuilder@endlink) CommonWorkflow
          the common workflow builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ComponentSettingsBlockBuilder NXOpen.Layout2d.ComponentSettingsBlockBuilder@endlink) Component2dSettings
    ##   the 2d component settings block builder, this builder stores the settings of the 2d component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ComponentSettingsBlockBuilder
    @property
    def Component2dSettings(self) -> ComponentSettingsBlockBuilder:
        """
        Getter for property: (@link ComponentSettingsBlockBuilder NXOpen.Layout2d.ComponentSettingsBlockBuilder@endlink) Component2dSettings
          the 2d component settings block builder, this builder stores the settings of the 2d component   
            
         
        """
        pass
    
    ## Getter for property: (@link CreateComponentFrom3DSettingsBuilder NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder@endlink) CreateComponentFrom3DSettingsBuilder
    ##   the create component from 3d builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CreateComponentFrom3DSettingsBuilder
    @property
    def CreateComponentFrom3DSettingsBuilder(self) -> CreateComponentFrom3DSettingsBuilder:
        """
        Getter for property: (@link CreateComponentFrom3DSettingsBuilder NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder@endlink) CreateComponentFrom3DSettingsBuilder
          the create component from 3d builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginAlignmentBuilder NXOpen.Annotations.OriginAlignmentBuilder@endlink) DimensionOriginAlignment
    ##   the dimension origin alignment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Annotations.OriginAlignmentBuilder
    @property
    def DimensionOriginAlignment(self) -> NXOpen.Annotations.OriginAlignmentBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginAlignmentBuilder NXOpen.Annotations.OriginAlignmentBuilder@endlink) DimensionOriginAlignment
          the dimension origin alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.DimensionWorkflowBuilder NXOpen.Annotations.DimensionWorkflowBuilder@endlink) DimensionWorkflow
    ##   the Dimension Workflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Annotations.DimensionWorkflowBuilder
    @property
    def DimensionWorkflow(self) -> NXOpen.Annotations.DimensionWorkflowBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.DimensionWorkflowBuilder NXOpen.Annotations.DimensionWorkflowBuilder@endlink) DimensionWorkflow
          the Dimension Workflow builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.DrawingFormatTitleBuilder NXOpen.Annotations.DrawingFormatTitleBuilder@endlink) DrawingFormatTitle
    ##      the drawing format title block builder    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.DrawingFormatTitleBuilder
    @property
    def DrawingFormatTitle(self) -> NXOpen.Annotations.DrawingFormatTitleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.DrawingFormatTitleBuilder NXOpen.Annotations.DrawingFormatTitleBuilder@endlink) DrawingFormatTitle
             the drawing format title block builder    
            
         
        """
        pass
    
    ## Getter for property: (@link DrawingFormatSheetBuilder NXOpen.Drawings.DrawingFormatSheetBuilder@endlink) DrawingFormatsheet
    ##      the drawing format sheet builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return DrawingFormatSheetBuilder
    @property
    def DrawingFormatsheet(self) -> DrawingFormatSheetBuilder:
        """
        Getter for property: (@link DrawingFormatSheetBuilder NXOpen.Drawings.DrawingFormatSheetBuilder@endlink) DrawingFormatsheet
             the drawing format sheet builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder@endlink) FramebarGeneral
    ##      the framebar general builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder
    @property
    def FramebarGeneral(self) -> NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder@endlink) FramebarGeneral
             the framebar general builder   
            
         
        """
        pass
    
    ## Getter for property: (@link GeneralPreferencesBuilder NXOpen.Layout2d.GeneralPreferencesBuilder@endlink) GeneralLayoutPreferencesBuilder
    ##   the general layout preferences builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return GeneralPreferencesBuilder
    @property
    def GeneralLayoutPreferencesBuilder(self) -> GeneralPreferencesBuilder:
        """
        Getter for property: (@link GeneralPreferencesBuilder NXOpen.Layout2d.GeneralPreferencesBuilder@endlink) GeneralLayoutPreferencesBuilder
          the general layout preferences builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.HoleTableSettingsContentBuilder NXOpen.Annotations.HoleTableSettingsContentBuilder@endlink) HoleTableContent
    ##   the Hole table settings content builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.HoleTableSettingsContentBuilder
    @property
    def HoleTableContent(self) -> NXOpen.Annotations.HoleTableSettingsContentBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.HoleTableSettingsContentBuilder NXOpen.Annotations.HoleTableSettingsContentBuilder@endlink) HoleTableContent
          the Hole table settings content builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.HoleTableSettingsFormatBuilder NXOpen.Annotations.HoleTableSettingsFormatBuilder@endlink) HoleTableFormat
    ##   the Hole table settings format builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.HoleTableSettingsFormatBuilder
    @property
    def HoleTableFormat(self) -> NXOpen.Annotations.HoleTableSettingsFormatBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.HoleTableSettingsFormatBuilder NXOpen.Annotations.HoleTableSettingsFormatBuilder@endlink) HoleTableFormat
          the Hole table settings format builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder@endlink) HoleTableHoleFilters
    ##   the Hole table settings hole filters builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder
    @property
    def HoleTableHoleFilters(self) -> NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder@endlink) HoleTableHoleFilters
          the Hole table settings hole filters builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.HoleTableSettingsLabelBuilder NXOpen.Annotations.HoleTableSettingsLabelBuilder@endlink) HoleTableLabel
    ##   the Hole table settings label builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.HoleTableSettingsLabelBuilder
    @property
    def HoleTableLabel(self) -> NXOpen.Annotations.HoleTableSettingsLabelBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.HoleTableSettingsLabelBuilder NXOpen.Annotations.HoleTableSettingsLabelBuilder@endlink) HoleTableLabel
          the Hole table settings label builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.HoleTableSettingsWorkflowBuilder NXOpen.Annotations.HoleTableSettingsWorkflowBuilder@endlink) HoleTableWorkflow
    ##   the Hole table settings workflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.HoleTableSettingsWorkflowBuilder
    @property
    def HoleTableWorkflow(self) -> NXOpen.Annotations.HoleTableSettingsWorkflowBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.HoleTableSettingsWorkflowBuilder NXOpen.Annotations.HoleTableSettingsWorkflowBuilder@endlink) HoleTableWorkflow
          the Hole table settings workflow builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.PartFamilyTableSettingsBuilder NXOpen.Annotations.PartFamilyTableSettingsBuilder@endlink) PartFamilyTable
    ##   the Part Family table settings builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Annotations.PartFamilyTableSettingsBuilder
    @property
    def PartFamilyTable(self) -> NXOpen.Annotations.PartFamilyTableSettingsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.PartFamilyTableSettingsBuilder NXOpen.Annotations.PartFamilyTableSettingsBuilder@endlink) PartFamilyTable
          the Part Family table settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.PartsListBuilder NXOpen.Annotations.PartsListBuilder@endlink) PartsList
    ##      the parts list style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.PartsListBuilder
    @property
    def PartsList(self) -> NXOpen.Annotations.PartsListBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.PartsListBuilder NXOpen.Annotations.PartsListBuilder@endlink) PartsList
             the parts list style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.RetainedAnnotationsBuilder NXOpen.Annotations.RetainedAnnotationsBuilder@endlink) RetainedAnnotations
    ##      the General Retained Annotations builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.RetainedAnnotationsBuilder
    @property
    def RetainedAnnotations(self) -> NXOpen.Annotations.RetainedAnnotationsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.RetainedAnnotationsBuilder NXOpen.Annotations.RetainedAnnotationsBuilder@endlink) RetainedAnnotations
             the General Retained Annotations builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.SymbolWorkflowBuilder NXOpen.Annotations.SymbolWorkflowBuilder@endlink) SymbolWorkflow
    ##      the SymbolWorkflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.SymbolWorkflowBuilder
    @property
    def SymbolWorkflow(self) -> NXOpen.Annotations.SymbolWorkflowBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.SymbolWorkflowBuilder NXOpen.Annotations.SymbolWorkflowBuilder@endlink) SymbolWorkflow
             the SymbolWorkflow builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.TableCellStyleBuilder NXOpen.Annotations.TableCellStyleBuilder@endlink) TableCellStyle
    ##   the table cell style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.TableCellStyleBuilder
    @property
    def TableCellStyle(self) -> NXOpen.Annotations.TableCellStyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TableCellStyleBuilder NXOpen.Annotations.TableCellStyleBuilder@endlink) TableCellStyle
          the table cell style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginAlignmentBuilder NXOpen.Annotations.OriginAlignmentBuilder@endlink) TableOriginAlignment
    ##   the table origin alignment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Annotations.OriginAlignmentBuilder
    @property
    def TableOriginAlignment(self) -> NXOpen.Annotations.OriginAlignmentBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginAlignmentBuilder NXOpen.Annotations.OriginAlignmentBuilder@endlink) TableOriginAlignment
          the table origin alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.TableSectionStyleBuilder NXOpen.Annotations.TableSectionStyleBuilder@endlink) TableSection
    ##      the table section style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.TableSectionStyleBuilder
    @property
    def TableSection(self) -> NXOpen.Annotations.TableSectionStyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TableSectionStyleBuilder NXOpen.Annotations.TableSectionStyleBuilder@endlink) TableSection
             the table section style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.TabularNoteStyleBuilder NXOpen.Annotations.TabularNoteStyleBuilder@endlink) TabularNoteStyle
    ##   the tabular note style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Annotations.TabularNoteStyleBuilder
    @property
    def TabularNoteStyle(self) -> NXOpen.Annotations.TabularNoteStyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TabularNoteStyleBuilder NXOpen.Annotations.TabularNoteStyleBuilder@endlink) TabularNoteStyle
          the tabular note style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link TrackDrawingChangesGeneralBuilder NXOpen.Drawings.TrackDrawingChangesGeneralBuilder@endlink) TrackDrawingChangesGeneral
    ##   the track drawing changes general settings builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return TrackDrawingChangesGeneralBuilder
    @property
    def TrackDrawingChangesGeneral(self) -> TrackDrawingChangesGeneralBuilder:
        """
        Getter for property: (@link TrackDrawingChangesGeneralBuilder NXOpen.Drawings.TrackDrawingChangesGeneralBuilder@endlink) TrackDrawingChangesGeneral
          the track drawing changes general settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link TrackDrawingChangesReportFilterBuilder NXOpen.Drawings.TrackDrawingChangesReportFilterBuilder@endlink) TrackDrawingChangesReportFilter
    ##   the track drawing changes report filter builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return TrackDrawingChangesReportFilterBuilder
    @property
    def TrackDrawingChangesReportFilter(self) -> TrackDrawingChangesReportFilterBuilder:
        """
        Getter for property: (@link TrackDrawingChangesReportFilterBuilder NXOpen.Drawings.TrackDrawingChangesReportFilterBuilder@endlink) TrackDrawingChangesReportFilter
          the track drawing changes report filter builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewBreakBuilder NXOpen.Drawings.ViewBreakBuilder@endlink) ViewBreak
    ##   the view break builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewBreakBuilder
    @property
    def ViewBreak(self) -> ViewBreakBuilder:
        """
        Getter for property: (@link ViewBreakBuilder NXOpen.Drawings.ViewBreakBuilder@endlink) ViewBreak
          the view break builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewDetailLabelBuilder NXOpen.Drawings.ViewDetailLabelBuilder@endlink) ViewDetailLabel
    ##      the view detail label builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewDetailLabelBuilder
    @property
    def ViewDetailLabel(self) -> ViewDetailLabelBuilder:
        """
        Getter for property: (@link ViewDetailLabelBuilder NXOpen.Drawings.ViewDetailLabelBuilder@endlink) ViewDetailLabel
             the view detail label builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewLabelBuilder NXOpen.Drawings.ViewLabelBuilder@endlink) ViewLabel
    ##      the view label builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewLabelBuilder
    @property
    def ViewLabel(self) -> ViewLabelBuilder:
        """
        Getter for property: (@link ViewLabelBuilder NXOpen.Drawings.ViewLabelBuilder@endlink) ViewLabel
             the view label builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewProjectedLabelBuilder NXOpen.Drawings.ViewProjectedLabelBuilder@endlink) ViewProjectedLabel
    ##      the view projected label builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewProjectedLabelBuilder
    @property
    def ViewProjectedLabel(self) -> ViewProjectedLabelBuilder:
        """
        Getter for property: (@link ViewProjectedLabelBuilder NXOpen.Drawings.ViewProjectedLabelBuilder@endlink) ViewProjectedLabel
             the view projected label builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewSectionLabelBuilder NXOpen.Drawings.ViewSectionLabelBuilder@endlink) ViewSectionLabel
    ##      the view section label builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewSectionLabelBuilder
    @property
    def ViewSectionLabel(self) -> ViewSectionLabelBuilder:
        """
        Getter for property: (@link ViewSectionLabelBuilder NXOpen.Drawings.ViewSectionLabelBuilder@endlink) ViewSectionLabel
             the view section label builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewSectionLineBuilder NXOpen.Drawings.ViewSectionLineBuilder@endlink) ViewSectionLine
    ##      the Section Line builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Drawings::ViewStyleBuilder::ViewSectionLineStyleBuilder NXOpen::Drawings::ViewStyleBuilder::ViewSectionLineStyleBuilder@endlink  instead.  <br> 

    ## @return ViewSectionLineBuilder
    @property
    def ViewSectionLine(self) -> ViewSectionLineBuilder:
        """
        Getter for property: (@link ViewSectionLineBuilder NXOpen.Drawings.ViewSectionLineBuilder@endlink) ViewSectionLine
             the Section Line builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewStyleBuilder NXOpen.Drawings.ViewStyleBuilder@endlink) ViewStyle
    ##   the view style builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewStyleBuilder
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: (@link ViewStyleBuilder NXOpen.Drawings.ViewStyleBuilder@endlink) ViewStyle
          the view style builder   
            
         
        """
        pass
    
    ## Getter for property: (@link ViewWorkflowBuilder NXOpen.Drawings.ViewWorkflowBuilder@endlink) ViewWorkflow
    ##   the view workflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ViewWorkflowBuilder
    @property
    def ViewWorkflow(self) -> ViewWorkflowBuilder:
        """
        Getter for property: (@link ViewWorkflowBuilder NXOpen.Drawings.ViewWorkflowBuilder@endlink) ViewWorkflow
          the view workflow builder   
            
         
        """
        pass
    
    ## Getter for property: (@link VisualDrawingComparePrefsBuilder NXOpen.Drawings.VisualDrawingComparePrefsBuilder@endlink) VisualDrawingCompare
    ##   the visual drawing compare settings builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return VisualDrawingComparePrefsBuilder
    @property
    def VisualDrawingCompare(self) -> VisualDrawingComparePrefsBuilder:
        """
        Getter for property: (@link VisualDrawingComparePrefsBuilder NXOpen.Drawings.VisualDrawingComparePrefsBuilder@endlink) VisualDrawingCompare
          the visual drawing compare settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link GeneralWorkFlowBuilder NXOpen.Drawings.GeneralWorkFlowBuilder@endlink) Workflow
    ##      the general workflow builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return GeneralWorkFlowBuilder
    @property
    def Workflow(self) -> GeneralWorkFlowBuilder:
        """
        Getter for property: (@link GeneralWorkFlowBuilder NXOpen.Drawings.GeneralWorkFlowBuilder@endlink) Workflow
             the general workflow builder   
            
         
        """
        pass
    
    ##  Inherit Settings From Customer Default 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    @staticmethod
    def InheritSettingsFromCustomerDefault(builder: PreferencesBuilder) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    
    ##  Inherit Settings From Preference 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    @staticmethod
    def InheritSettingsFromPreferences(builder: PreferencesBuilder) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    
    ##  Inherit Settings From Selected Objects 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  The selected annotation or table or view instance object. 
    ##                                                                NULL is not allowed. 
    def InheritSettingsFromSelectedObjects(builder: PreferencesBuilder, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
    
    ##  Synchronize fcf symbol sequence 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    @staticmethod
    def SynchronizeFCFSymbolSequence(builder: PreferencesBuilder) -> None:
        """
         Synchronize fcf symbol sequence 
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PrimaryContentItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##   the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
          the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  items to append 
    @overload
    def Append(self, object_list: PrimaryContentItemBuilderList, objects: List[PrimaryContentItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  item to append 
    @overload
    def Append(self, object_list: PrimaryContentItemBuilderList, objectValue: PrimaryContentItemBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: PrimaryContentItemBuilderList) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be deleted 
    def ClearIndex(object_list: PrimaryContentItemBuilderList, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  whether to delete the objects when removing them 
    def Clear(object_list: PrimaryContentItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: PrimaryContentItemBuilderList, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  index of item to be removed from the list 
    @overload
    def Erase(self, object_list: PrimaryContentItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: PrimaryContentItemBuilderList, obj: PrimaryContentItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to be removed from the list 
    @overload
    def Erase(self, object_list: PrimaryContentItemBuilderList, obj: PrimaryContentItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  Object to find index for 
    def FindIndex(object_list: PrimaryContentItemBuilderList, obj: PrimaryContentItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link PrimaryContentItemBuilder NXOpen.Drafting.PrimaryContentItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: PrimaryContentItemBuilderList, index: int) -> PrimaryContentItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link PrimaryContentItemBuilder NXOpen.Drafting.PrimaryContentItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link PrimaryContentItemBuilder List[NXOpen.Drafting.PrimaryContentItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: PrimaryContentItemBuilderList) -> List[PrimaryContentItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link PrimaryContentItemBuilder List[NXOpen.Drafting.PrimaryContentItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: PrimaryContentItemBuilderList, location: int, objectValue: PrimaryContentItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: PrimaryContentItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: PrimaryContentItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The list contents 
    def SetContents(object_list: PrimaryContentItemBuilderList, objects: List[PrimaryContentItemBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location of the first item 
    @overload
    def Swap(self, object_list: PrimaryContentItemBuilderList, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  first item 
    @overload
    def Swap(self, object_list: PrimaryContentItemBuilderList, object1: PrimaryContentItemBuilder, object2: PrimaryContentItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::Drafting::PrimaryContentItemBuilder NXOpen::Drafting::PrimaryContentItemBuilder@endlink .  This class is
##     used to specify information pertaining to the primary content of a Drawing Booklet.
##     Each instance represents a single drawing in a booklet.
##      <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreatePrimaryContentItemBuilder  NXOpen::Drafting::AutomationManager::CreatePrimaryContentItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class PrimaryContentItemBuilder(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.Drafting.PrimaryContentItemBuilder</ja_class>.  This class is
    used to specify information pertaining to the primary content of a Drawing Booklet.
    Each instance represents a single drawing in a booklet.
    """


    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) Content
    ##   the content.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def Content(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) Content
          the content.  
             
         
        """
        pass
    
    ## Getter for property: (str) GeometryTemplate
    ##   the geometry template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def GeometryTemplate(self) -> str:
        """
        Getter for property: (str) GeometryTemplate
          the geometry template.  
             
         
        """
        pass
    
    ## Setter for property: (str) GeometryTemplate

    ##   the geometry template.  
    ##      
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @GeometryTemplate.setter
    def GeometryTemplate(self, geometryTemplate: str):
        """
        Setter for property: (str) GeometryTemplate
          the geometry template.  
             
         
        """
        pass
    
import NXOpen
##  This class is used to specify knowledge fusion rules in a drawing template. The rules are 
##         executed when the template is instantiated.  <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateRulesBuilder  NXOpen::Drafting::AutomationManager::CreateRulesBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class RulesBuilder(NXOpen.Builder): 
    """ This class is used to specify knowledge fusion rules in a drawing template. The rules are 
        executed when the template is instantiated. """


    ## Getter for property: (str) DimensionRule
    ##   the dimension rule   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def DimensionRule(self) -> str:
        """
        Getter for property: (str) DimensionRule
          the dimension rule   
            
         
        """
        pass
    
    ## Setter for property: (str) DimensionRule

    ##   the dimension rule   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DimensionRule.setter
    def DimensionRule(self, dimensionRule: str):
        """
        Setter for property: (str) DimensionRule
          the dimension rule   
            
         
        """
        pass
    
    ## Getter for property: (str) NoteRule
    ##   the note rule   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def NoteRule(self) -> str:
        """
        Getter for property: (str) NoteRule
          the note rule   
            
         
        """
        pass
    
    ## Setter for property: (str) NoteRule

    ##   the note rule   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @NoteRule.setter
    def NoteRule(self, noteRule: str):
        """
        Setter for property: (str) NoteRule
          the note rule   
            
         
        """
        pass
    
    ## Getter for property: (str) SymbolRule
    ##   the symbol rule   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def SymbolRule(self) -> str:
        """
        Getter for property: (str) SymbolRule
          the symbol rule   
            
         
        """
        pass
    
    ## Setter for property: (str) SymbolRule

    ##   the symbol rule   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @SymbolRule.setter
    def SymbolRule(self, symbolRule: str):
        """
        Setter for property: (str) SymbolRule
          the symbol rule   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents an object that manages drafting settings.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SettingsManager(NXOpen.Object): 
    """ Represents an object that manages drafting settings. """


    ##  Creates a @link NXOpen::Annotations::EditSettingsBuilder NXOpen::Annotations::EditSettingsBuilder@endlink 
    ##              <br> 
    ##             For multiple object settings, first create primary settings builder by passing all 
    ##             selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
    ##             object starting from second selected object.
    ##             Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
    ##             after creating all settings builder for selected objects.  <br>  
    ##         
    ##  @return builder (@link NXOpen.Annotations.EditSettingsBuilder NXOpen.Annotations.EditSettingsBuilder@endlink):  The annotations settings builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  the array of objects for style, NULL not allowed
    def CreateAnnotationEditSettingsBuilder(part: SettingsManager, objects: List[NXOpen.DisplayableObject]) -> NXOpen.Annotations.EditSettingsBuilder:
        """
         Creates a @link NXOpen::Annotations::EditSettingsBuilder NXOpen::Annotations::EditSettingsBuilder@endlink 
                     <br> 
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                    after creating all settings builder for selected objects.  <br>  
                
         @return builder (@link NXOpen.Annotations.EditSettingsBuilder NXOpen.Annotations.EditSettingsBuilder@endlink):  The annotations settings builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Drawings::EditSectionLineSettingsBuilder NXOpen::Drawings::EditSectionLineSettingsBuilder@endlink 
    ##              <br> 
    ##             For multiple object settings, first create primary settings builder by passing all 
    ##             selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
    ##             object starting from second selected object.
    ##             Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
    ##             after creating all settings builder for selected objects.  <br>  
    ##         
    ##  @return builder (@link EditSectionLineSettingsBuilder NXOpen.Drawings.EditSectionLineSettingsBuilder@endlink):  The section line settings builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  The array of object for section line style, NULL is allowed. 
    def CreateDrawingEditSectionLineSettingsBuilder(part: SettingsManager, sectionLines: List[SectionLine]) -> EditSectionLineSettingsBuilder:
        """
         Creates a @link NXOpen::Drawings::EditSectionLineSettingsBuilder NXOpen::Drawings::EditSectionLineSettingsBuilder@endlink 
                     <br> 
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                    after creating all settings builder for selected objects.  <br>  
                
         @return builder (@link EditSectionLineSettingsBuilder NXOpen.Drawings.EditSectionLineSettingsBuilder@endlink):  The section line settings builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Drawings::EditViewLabelSettingsBuilder NXOpen::Drawings::EditViewLabelSettingsBuilder@endlink 
    ##              <br> 
    ##             For multiple object settings, first create primary settings builder by passing all 
    ##             selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
    ##             object starting from second selected object.
    ##             Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
    ##             after creating all settings builder for selected objects.  <br> 
    ##         
    ##  @return builder (@link EditViewLabelSettingsBuilder NXOpen.Drawings.EditViewLabelSettingsBuilder@endlink):  The view label settings builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  the array of view labels to edit, NULL is not allowed. 
    def CreateDrawingEditViewLabelSettingsBuilder(part: SettingsManager, viewLabels: List[NXOpen.DisplayableObject]) -> EditViewLabelSettingsBuilder:
        """
         Creates a @link NXOpen::Drawings::EditViewLabelSettingsBuilder NXOpen::Drawings::EditViewLabelSettingsBuilder@endlink 
                     <br> 
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                    after creating all settings builder for selected objects.  <br> 
                
         @return builder (@link EditViewLabelSettingsBuilder NXOpen.Drawings.EditViewLabelSettingsBuilder@endlink):  The view label settings builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Drawings::EditViewSettingsBuilder NXOpen::Drawings::EditViewSettingsBuilder@endlink 
    ##              <br> 
    ##             For multiple object settings, first create primary settings builder by passing all 
    ##             selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
    ##             object starting from second selected object.
    ##             Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
    ##             after creating all settings builder for selected objects.  <br> 
    ##         
    ##  @return builder (@link EditViewSettingsBuilder NXOpen.Drawings.EditViewSettingsBuilder@endlink):  The view settings builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  The array of objects for view style, NULL not allowed. 
    def CreateDrawingEditViewSettingsBuilder(part: SettingsManager, views: List[NXOpen.View]) -> EditViewSettingsBuilder:
        """
         Creates a @link NXOpen::Drawings::EditViewSettingsBuilder NXOpen::Drawings::EditViewSettingsBuilder@endlink 
                     <br> 
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                    after creating all settings builder for selected objects.  <br> 
                
         @return builder (@link EditViewSettingsBuilder NXOpen.Drawings.EditViewSettingsBuilder@endlink):  The view settings builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Layout2d::EditComponentSettingsBuilder NXOpen::Layout2d::EditComponentSettingsBuilder@endlink  
    ##             This builder is the interface to edit the 2d component settings of layout
    ##              <br> 
    ##             For multiple object settings, first create primary settings builder by passing all 
    ##             selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
    ##             object starting from second selected object.
    ##             Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
    ##             after creating all settings builder for selected objects.  <br> 
    ##         
    ##  @return builder (@link EditComponentSettingsBuilder NXOpen.Layout2d.EditComponentSettingsBuilder@endlink):  The layout2d component settings builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_layout ("NX Layout")
    ##  The array of components to edit.  NULL is not allowed 
    def CreateLayout2dEditComponentSettingsBuilder(part: SettingsManager, components: List[Component]) -> EditComponentSettingsBuilder:
        """
         Creates a @link NXOpen::Layout2d::EditComponentSettingsBuilder NXOpen::Layout2d::EditComponentSettingsBuilder@endlink  
                    This builder is the interface to edit the 2d component settings of layout
                     <br> 
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                    after creating all settings builder for selected objects.  <br> 
                
         @return builder (@link EditComponentSettingsBuilder NXOpen.Layout2d.EditComponentSettingsBuilder@endlink):  The layout2d component settings builder .
        """
        pass
    
    ##  Creates a @link NXOpen::Drafting::PreferencesBuilder NXOpen::Drafting::PreferencesBuilder@endlink  
    ##         
    ##  @return builder (@link PreferencesBuilder NXOpen.Drafting.PreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    def CreatePreferencesBuilder(part: SettingsManager) -> PreferencesBuilder:
        """
         Creates a @link NXOpen::Drafting::PreferencesBuilder NXOpen::Drafting::PreferencesBuilder@endlink  
                
         @return builder (@link PreferencesBuilder NXOpen.Drafting.PreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Annotations::TableEditSettingsBuilder NXOpen::Annotations::TableEditSettingsBuilder@endlink 
    ##              <br> 
    ##             For multiple object settings, first create primary settings builder by passing all 
    ##             selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
    ##             object starting from second selected object.
    ##             Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
    ##             after creating all settings builder for selected objects.  <br> 
    ##         
    ##  @return builder (@link NXOpen.Annotations.TableEditSettingsBuilder NXOpen.Annotations.TableEditSettingsBuilder@endlink):  The table settings builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ##  the array of objects for style, If NULL, section or cell preferences for all sections or cells will be set. 
    def CreateTableEditSettingsBuilder(part: SettingsManager, objects: List[NXOpen.DisplayableObject]) -> NXOpen.Annotations.TableEditSettingsBuilder:
        """
         Creates a @link NXOpen::Annotations::TableEditSettingsBuilder NXOpen::Annotations::TableEditSettingsBuilder@endlink 
                     <br> 
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  
                    after creating all settings builder for selected objects.  <br> 
                
         @return builder (@link NXOpen.Annotations.TableEditSettingsBuilder NXOpen.Annotations.TableEditSettingsBuilder@endlink):  The table settings builder .
        """
        pass
    
    ##  Creates a @link Annotations::TableRowSortingBuilder Annotations::TableRowSortingBuilder@endlink  
    ##  @return builder (@link NXOpen.Annotations.TableRowSortingBuilder NXOpen.Annotations.TableRowSortingBuilder@endlink):  The table sorting builder .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  the array of table row objects 
    @overload
    def CreateTableRowSortingBuilder(self, part: SettingsManager, objects: List[NXOpen.DisplayableObject]) -> NXOpen.Annotations.TableRowSortingBuilder:
        """
         Creates a @link Annotations::TableRowSortingBuilder Annotations::TableRowSortingBuilder@endlink  
         @return builder (@link NXOpen.Annotations.TableRowSortingBuilder NXOpen.Annotations.TableRowSortingBuilder@endlink):  The table sorting builder .
        """
        pass
    
    ##  Creates a @link Annotations::TableRowSortingBuilder Annotations::TableRowSortingBuilder@endlink  from Table
    ##  @return builder (@link NXOpen.Annotations.TableRowSortingBuilder NXOpen.Annotations.TableRowSortingBuilder@endlink):  The table sorting builder .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  the table object 
    @overload
    def CreateTableRowSortingBuilder(self, part: SettingsManager, tableObject: NXOpen.Annotations.Table) -> NXOpen.Annotations.TableRowSortingBuilder:
        """
         Creates a @link Annotations::TableRowSortingBuilder Annotations::TableRowSortingBuilder@endlink  from Table
         @return builder (@link NXOpen.Annotations.TableRowSortingBuilder NXOpen.Annotations.TableRowSortingBuilder@endlink):  The table sorting builder .
        """
        pass
    
    ##  Process edit settings builders for multiple objects
    ##             User must call this API for multiple object settings and pass all edit settings builders for selected objects
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ## 
    ## <param name="editSettingsBuilders"> (@link BaseEditSettingsBuilder List[NXOpen.Drafting.BaseEditSettingsBuilder]@endlink) </param>
    def ProcessForMultipleObjectsSettings(part: SettingsManager, editSettingsBuilders: List[BaseEditSettingsBuilder]) -> None:
        """
         Process edit settings builders for multiple objects
                    User must call this API for multiple object settings and pass all edit settings builders for selected objects
                
        """
        pass
    
    ##  Process edit settings builders for mutiple objects
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link Drafting::SettingsManager::ProcessForMultipleObjectsSettings Drafting::SettingsManager::ProcessForMultipleObjectsSettings@endlink  instead.  <br> 

    ## License requirements: drafting ("DRAFTING")
    ## 
    ## <param name="editSettingsBuilders"> (@link BaseEditSettingsBuilder List[NXOpen.Drafting.BaseEditSettingsBuilder]@endlink) </param>
    def ProcessForMutipleObjectsSettings(part: SettingsManager, editSettingsBuilders: List[BaseEditSettingsBuilder]) -> None:
        """
         Process edit settings builders for mutiple objects
                
        """
        pass
    
import NXOpen
##  
##     This builder allows the user to break a Drawing View into its parts and delete the Drawing View
##       <br> To create a new instance of this class, use @link NXOpen::Drafting::DraftingApplicationManager::CreateSmashDrawingViewBuilder  NXOpen::Drafting::DraftingApplicationManager::CreateSmashDrawingViewBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class SmashDrawingViewBuilder(NXOpen.Builder): 
    """ 
    This builder allows the user to break a Drawing View into its parts and delete the Drawing View
     """


    ## Getter for property: (@link SelectDraftingView NXOpen.Drawings.SelectDraftingView@endlink) SelectView
    ##   the select drawing views to smash  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return SelectDraftingView
    @property
    def SelectView(self) -> SelectDraftingView:
        """
        Getter for property: (@link SelectDraftingView NXOpen.Drawings.SelectDraftingView@endlink) SelectView
          the select drawing views to smash  
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  This class is used to specify knowledge fusion rule for a note object in a drawing template. 
##         The rule is stored on the note and is executed when the template is instantiated.  <br> To create a new instance of this class, use @link NXOpen::Drafting::AutomationManager::CreateSpecifyRuleBuilder  NXOpen::Drafting::AutomationManager::CreateSpecifyRuleBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class SpecifyRuleBuilder(NXOpen.Builder): 
    """ This class is used to specify knowledge fusion rule for a note object in a drawing template. 
        The rule is stored on the note and is executed when the template is instantiated. """


    ## Getter for property: (@link NXOpen.Annotations.Note NXOpen.Annotations.Note@endlink) Note
    ##   the note to add rule to  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Annotations.Note
    @property
    def Note(self) -> NXOpen.Annotations.Note:
        """
        Getter for property: (@link NXOpen.Annotations.Note NXOpen.Annotations.Note@endlink) Note
          the note to add rule to  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Annotations.Note NXOpen.Annotations.Note@endlink) Note

    ##   the note to add rule to  
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Note.setter
    def Note(self, note: NXOpen.Annotations.Note):
        """
        Setter for property: (@link NXOpen.Annotations.Note NXOpen.Annotations.Note@endlink) Note
          the note to add rule to  
            
         
        """
        pass
    
    ## Getter for property: (str) Rule
    ##   the rule   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Rule(self) -> str:
        """
        Getter for property: (str) Rule
          the rule   
            
         
        """
        pass
    
    ## Setter for property: (str) Rule

    ##   the rule   
    ##     
    ##  
    ## Setter License requirements: nx_drawing_auto ("NX Drawing Automation")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Rule.setter
    def Rule(self, rule: str):
        """
        Setter for property: (str) Rule
          the rule   
            
         
        """
        pass
    
## @package NXOpen.Drafting
## Classes, Enums and Structs under NXOpen.Drafting namespace

##  @link AnnotateViewsBuilderExistingAutomaticAnnotation NXOpen.Drafting.AnnotateViewsBuilderExistingAutomaticAnnotation @endlink is an alias for @link AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.Drafting.AnnotateViewsBuilder.ExistingAutomaticAnnotation@endlink
AnnotateViewsBuilderExistingAutomaticAnnotation = AnnotateViewsBuilder.ExistingAutomaticAnnotation


##  @link CutCopyPasteBuilderTypeOperation NXOpen.Drafting.CutCopyPasteBuilderTypeOperation @endlink is an alias for @link CutCopyPasteBuilder.TypeOperation NXOpen.Drafting.CutCopyPasteBuilder.TypeOperation@endlink
CutCopyPasteBuilderTypeOperation = CutCopyPasteBuilder.TypeOperation


##  @link CutCopyPasteBuilderTypePaste NXOpen.Drafting.CutCopyPasteBuilderTypePaste @endlink is an alias for @link CutCopyPasteBuilder.TypePaste NXOpen.Drafting.CutCopyPasteBuilder.TypePaste@endlink
CutCopyPasteBuilderTypePaste = CutCopyPasteBuilder.TypePaste


