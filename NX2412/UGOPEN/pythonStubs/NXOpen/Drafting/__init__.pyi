from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AnnotateViewsBuilder(NXOpen.Builder): 
    """ This class is used to annotate views based on the knowledge fusion rules. """
    class ExistingAutomaticAnnotation(Enum):
        """
        Members Include: 
         |Delete| 
         |Preserve| 

        """
        Delete: int
        Preserve: int
        @staticmethod
        def ValueOf(value: int) -> AnnotateViewsBuilder.ExistingAutomaticAnnotation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExistingAutomaticAnnotationOption(self) -> AnnotateViewsBuilder.ExistingAutomaticAnnotation:
        """
        Getter for property: ( AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.) ExistingAutomaticAnnotationOption
         Returns the existing automatic annotation option   
            
         
        """
        pass
    @ExistingAutomaticAnnotationOption.setter
    def ExistingAutomaticAnnotationOption(self, existingAutomaticAnnotationOption: AnnotateViewsBuilder.ExistingAutomaticAnnotation):
        """
        Setter for property: ( AnnotateViewsBuilder.ExistingAutomaticAnnotation NXOpen.) ExistingAutomaticAnnotationOption
         Returns the existing automatic annotation option   
            
         
        """
        pass
    @property
    def Views(self) -> SelectDraftingViewList:
        """
        Getter for property: ( SelectDraftingViewList NXOpen.) Views
         Returns the views to annotate   
            
         
        """
        pass
import NXOpen
class AttributeItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[AttributeItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: AttributeItemBuilder) -> None:
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
    def Erase(self, obj: AttributeItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: AttributeItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: AttributeItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> AttributeItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( AttributeItemBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[AttributeItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( AttributeItemBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: AttributeItemBuilder) -> None:
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
    def SetContents(self, objects: List[AttributeItemBuilder]) -> None:
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
    def Swap(self, object1: AttributeItemBuilder, object2: AttributeItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AttributeItemBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drafting.AttributeItemBuilder.  This class is
    used to specify information about a single NX attribute.
    """
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title.  
             
         
        """
        pass
    @Title.setter
    def Title(self, attributeTitle: str):
        """
        Setter for property: (str) Title
         Returns the title.  
             
         
        """
        pass
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the value.  
             
         
        """
        pass
    @Value.setter
    def Value(self, attributeValue: str):
        """
        Setter for property: (str) Value
         Returns the value.  
             
         
        """
        pass
import NXOpen
class AutomationManager(NXOpen.Object): 
    """
    Represents a NXOpen.Drafting.AutomationManager.  This class is
    used to create objects which are used in the automation of drawing creation.
    """
    @property
    def DrawingRegions() -> DrawingRegionCollection:
        """
         Returns the RegionCollection instance  
        """
        pass
    def CreateAnnotateViewsBuilder(self) -> AnnotateViewsBuilder:
        """
         Creates a NXOpen.Drafting.AnnotateViewsBuilder 
         Returns builder ( AnnotateViewsBuilder NXOpen.): .
        """
        pass
    def CreateAttributeItemBuilder(self) -> AttributeItemBuilder:
        """
         Creates a NXOpen.Drafting.AttributeItemBuilder 
         Returns builder ( AttributeItemBuilder NXOpen.): .
        """
        pass
    def CreateDistributeAnnotationsBuilder(self) -> DistributeAnnotationsBuilder:
        """
         Creates a NXOpen.Drafting.DistributeAnnotationsBuilder 
         Returns builder ( DistributeAnnotationsBuilder NXOpen.): .
        """
        pass
    def CreateDrawingCreationWizardBuilder(self, isEditing: bool) -> DrawingCreationWizardBuilder:
        """
         Creates a NXOpen.Drafting.DrawingCreationWizardBuilder 
         Returns builder ( DrawingCreationWizardBuilder NXOpen.): .
        """
        pass
    def CreateDrawingCreationWizardBuilderFromRule(self, className: str) -> DrawingCreationWizardBuilder:
        """
         Creates a NXOpen.Drafting.DrawingCreationWizardBuilder 
         Returns builder ( DrawingCreationWizardBuilder NXOpen.): .
        """
        pass
    def CreatePreferencesBuilder(self) -> AutomationPreferencesBuilder:
        """
         Creates a NXOpen.Drafting.AutomationPreferencesBuilder 
         Returns builder ( AutomationPreferencesBuilder NXOpen.): .
        """
        pass
    def CreatePrimaryContentItemBuilder(self) -> PrimaryContentItemBuilder:
        """
         Creates a NXOpen.Drafting.PrimaryContentItemBuilder 
         Returns builder ( PrimaryContentItemBuilder NXOpen.): .
        """
        pass
    def CreateRulesBuilder(self) -> RulesBuilder:
        """
         Creates a NXOpen.Drafting.RulesBuilder 
         Returns builder ( RulesBuilder NXOpen.): .
        """
        pass
    def CreateSpecifyRuleBuilder(self) -> SpecifyRuleBuilder:
        """
         Creates a NXOpen.Drafting.SpecifyRuleBuilder 
         Returns builder ( SpecifyRuleBuilder NXOpen.): .
        """
        pass
    def GetRemainingPartsOfBooklet(self) -> Tuple[List[NXOpen.Part], List[str]]:
        """
         Returns the remaining loaded parts and remaining unloaded parts full names from the booklet 
         Returns A tuple consisting of (remainingParts, remainingPartFileSpecs). 
         - remainingParts is:  NXOpen.Part Li.
         - remainingPartFileSpecs is: List[str].

        """
        pass
import NXOpen
import NXOpen.Preferences
class AutomationPreferencesBuilder(NXOpen.Builder): 
    """the builder for Drafting Automation Preferences """
    @property
    def AllowFeetInchFractionForDimensionGreaterThan(self) -> bool:
        """
        Getter for property: (bool) AllowFeetInchFractionForDimensionGreaterThan
         Returns the determination of the feet inch fraction display for dimension greater than   
            
         
        """
        pass
    @AllowFeetInchFractionForDimensionGreaterThan.setter
    def AllowFeetInchFractionForDimensionGreaterThan(self, allowFeetInchFractionForDimensionGreaterThan: bool):
        """
        Setter for property: (bool) AllowFeetInchFractionForDimensionGreaterThan
         Returns the determination of the feet inch fraction display for dimension greater than   
            
         
        """
        pass
    @property
    def AllowInchFractionToNearest(self) -> bool:
        """
        Getter for property: (bool) AllowInchFractionToNearest
         Returns the determination of the display for inch fraction to nearest   
            
         
        """
        pass
    @AllowInchFractionToNearest.setter
    def AllowInchFractionToNearest(self, allowInchFractionToNearest: bool):
        """
        Setter for property: (bool) AllowInchFractionToNearest
         Returns the determination of the display for inch fraction to nearest   
            
         
        """
        pass
    @property
    def AnnotationInsideGeometry(self) -> bool:
        """
        Getter for property: (bool) AnnotationInsideGeometry
         Returns the annotation inside geometry   
            
         
        """
        pass
    @AnnotationInsideGeometry.setter
    def AnnotationInsideGeometry(self, annotationInsideGeometry: bool):
        """
        Setter for property: (bool) AnnotationInsideGeometry
         Returns the annotation inside geometry   
            
         
        """
        pass
    @property
    def DisplayRegion(self) -> bool:
        """
        Getter for property: (bool) DisplayRegion
         Returns the display in non template   
            
         
        """
        pass
    @DisplayRegion.setter
    def DisplayRegion(self, displayRegion: bool):
        """
        Setter for property: (bool) DisplayRegion
         Returns the display in non template   
            
         
        """
        pass
    @property
    def DisplayRegionLabel(self) -> bool:
        """
        Getter for property: (bool) DisplayRegionLabel
         Returns the display region label   
            
         
        """
        pass
    @DisplayRegionLabel.setter
    def DisplayRegionLabel(self, displayRegionLabel: bool):
        """
        Setter for property: (bool) DisplayRegionLabel
         Returns the display region label   
            
         
        """
        pass
    @property
    def DistanceBetweenAnnotations(self) -> float:
        """
        Getter for property: (float) DistanceBetweenAnnotations
         Returns the distance between annotations   
            
         
        """
        pass
    @DistanceBetweenAnnotations.setter
    def DistanceBetweenAnnotations(self, distanceBetweenAnnotations: float):
        """
        Setter for property: (float) DistanceBetweenAnnotations
         Returns the distance between annotations   
            
         
        """
        pass
    @property
    def EqualDimensionCompareTolerance(self) -> float:
        """
        Getter for property: (float) EqualDimensionCompareTolerance
         Returns the equal dimension compare tolerance   
            
         
        """
        pass
    @EqualDimensionCompareTolerance.setter
    def EqualDimensionCompareTolerance(self, equalDimensionCompareTolerance: float):
        """
        Setter for property: (float) EqualDimensionCompareTolerance
         Returns the equal dimension compare tolerance   
            
         
        """
        pass
    @property
    def FeetInchFractionForDimensionGreaterThan(self) -> float:
        """
        Getter for property: (float) FeetInchFractionForDimensionGreaterThan
         Returns the feet inch fraction for dimension greater than   
            
         
        """
        pass
    @FeetInchFractionForDimensionGreaterThan.setter
    def FeetInchFractionForDimensionGreaterThan(self, feetInchFractionForDimensionGreaterThan: float):
        """
        Setter for property: (float) FeetInchFractionForDimensionGreaterThan
         Returns the feet inch fraction for dimension greater than   
            
         
        """
        pass
    @property
    def HideFeetInchMark(self) -> bool:
        """
        Getter for property: (bool) HideFeetInchMark
         Returns the hide feet inch mark   
            
         
        """
        pass
    @HideFeetInchMark.setter
    def HideFeetInchMark(self, hideFeetInchMark: bool):
        """
        Setter for property: (bool) HideFeetInchMark
         Returns the hide feet inch mark   
            
         
        """
        pass
    @property
    def InchFractionToNearest(self) -> float:
        """
        Getter for property: (float) InchFractionToNearest
         Returns the inch fraction to nearest   
            
         
        """
        pass
    @InchFractionToNearest.setter
    def InchFractionToNearest(self, inchFractionToNearest: float):
        """
        Setter for property: (float) InchFractionToNearest
         Returns the inch fraction to nearest   
            
         
        """
        pass
    @property
    def MaximumDistanceToGeometry(self) -> float:
        """
        Getter for property: (float) MaximumDistanceToGeometry
         Returns the maximum distance to geometry   
            
         
        """
        pass
    @MaximumDistanceToGeometry.setter
    def MaximumDistanceToGeometry(self, maximumDistanceToGeometry: float):
        """
        Setter for property: (float) MaximumDistanceToGeometry
         Returns the maximum distance to geometry   
            
         
        """
        pass
    @property
    def MinimumDistanceToGeometry(self) -> float:
        """
        Getter for property: (float) MinimumDistanceToGeometry
         Returns the minimum distance to geometry   
            
         
        """
        pass
    @MinimumDistanceToGeometry.setter
    def MinimumDistanceToGeometry(self, minimumDistanceToGeometry: float):
        """
        Setter for property: (float) MinimumDistanceToGeometry
         Returns the minimum distance to geometry   
            
         
        """
        pass
    @property
    def ReferenceGeometrySearchDistance(self) -> float:
        """
        Getter for property: (float) ReferenceGeometrySearchDistance
         Returns the reference geometry search distance   
            
         
        """
        pass
    @ReferenceGeometrySearchDistance.setter
    def ReferenceGeometrySearchDistance(self, referenceGeometrySearchDistance: float):
        """
        Setter for property: (float) ReferenceGeometrySearchDistance
         Returns the reference geometry search distance   
            
         
        """
        pass
    @property
    def RegionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) RegionColor
         Returns the region color   
            
         
        """
        pass
    @RegionColor.setter
    def RegionColor(self, regionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) RegionColor
         Returns the region color   
            
         
        """
        pass
    @property
    def RegionFont(self) -> NXOpen.Preferences.PartDrafting.FontType:
        """
        Getter for property: ( NXOpen.Preferences.PartDrafting.FontType) RegionFont
         Returns the region font   
            
         
        """
        pass
    @RegionFont.setter
    def RegionFont(self, regionFont: NXOpen.Preferences.PartDrafting.FontType):
        """
        Setter for property: ( NXOpen.Preferences.PartDrafting.FontType) RegionFont
         Returns the region font   
            
         
        """
        pass
    @property
    def RegionWidth(self) -> NXOpen.Preferences.PartDrafting.WidthType:
        """
        Getter for property: ( NXOpen.Preferences.PartDrafting.WidthType) RegionWidth
         Returns the region width   
            
         
        """
        pass
    @RegionWidth.setter
    def RegionWidth(self, regionWidth: NXOpen.Preferences.PartDrafting.WidthType):
        """
        Setter for property: ( NXOpen.Preferences.PartDrafting.WidthType) RegionWidth
         Returns the region width   
            
         
        """
        pass
    @property
    def SecondaryContentHiddenLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SecondaryContentHiddenLineColor
         Returns the secondary content hidden line color   
            
         
        """
        pass
    @SecondaryContentHiddenLineColor.setter
    def SecondaryContentHiddenLineColor(self, secondaryContentHiddenLineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SecondaryContentHiddenLineColor
         Returns the secondary content hidden line color   
            
         
        """
        pass
    @property
    def SecondaryContentHiddenLineFont(self) -> NXOpen.Preferences.PartDrafting.FontType:
        """
        Getter for property: ( NXOpen.Preferences.PartDrafting.FontType) SecondaryContentHiddenLineFont
         Returns the secondary content hidden line font   
            
         
        """
        pass
    @SecondaryContentHiddenLineFont.setter
    def SecondaryContentHiddenLineFont(self, secondaryContentHiddenLineFont: NXOpen.Preferences.PartDrafting.FontType):
        """
        Setter for property: ( NXOpen.Preferences.PartDrafting.FontType) SecondaryContentHiddenLineFont
         Returns the secondary content hidden line font   
            
         
        """
        pass
    @property
    def SecondaryContentHiddenLineWidth(self) -> NXOpen.Preferences.PartDrafting.WidthType:
        """
        Getter for property: ( NXOpen.Preferences.PartDrafting.WidthType) SecondaryContentHiddenLineWidth
         Returns the secondary content hidden line width   
            
         
        """
        pass
    @SecondaryContentHiddenLineWidth.setter
    def SecondaryContentHiddenLineWidth(self, secondaryContentHiddenLineWidth: NXOpen.Preferences.PartDrafting.WidthType):
        """
        Setter for property: ( NXOpen.Preferences.PartDrafting.WidthType) SecondaryContentHiddenLineWidth
         Returns the secondary content hidden line width   
            
         
        """
        pass
    @property
    def SecondaryContentVisibleLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SecondaryContentVisibleLineColor
         Returns the secondary content visible line color   
            
         
        """
        pass
    @SecondaryContentVisibleLineColor.setter
    def SecondaryContentVisibleLineColor(self, secondaryContentVisibleLineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SecondaryContentVisibleLineColor
         Returns the secondary content visible line color   
            
         
        """
        pass
    @property
    def SecondaryContentVisibleLineFont(self) -> NXOpen.Preferences.PartDrafting.FontType:
        """
        Getter for property: ( NXOpen.Preferences.PartDrafting.FontType) SecondaryContentVisibleLineFont
         Returns the secondary content visible line font   
            
         
        """
        pass
    @SecondaryContentVisibleLineFont.setter
    def SecondaryContentVisibleLineFont(self, secondaryContentVisibleLineFont: NXOpen.Preferences.PartDrafting.FontType):
        """
        Setter for property: ( NXOpen.Preferences.PartDrafting.FontType) SecondaryContentVisibleLineFont
         Returns the secondary content visible line font   
            
         
        """
        pass
    @property
    def SecondaryContentVisibleLineWidth(self) -> NXOpen.Preferences.PartDrafting.WidthType:
        """
        Getter for property: ( NXOpen.Preferences.PartDrafting.WidthType) SecondaryContentVisibleLineWidth
         Returns the secondary content visible line width   
            
         
        """
        pass
    @SecondaryContentVisibleLineWidth.setter
    def SecondaryContentVisibleLineWidth(self, secondaryContentVisibleLineWidth: NXOpen.Preferences.PartDrafting.WidthType):
        """
        Setter for property: ( NXOpen.Preferences.PartDrafting.WidthType) SecondaryContentVisibleLineWidth
         Returns the secondary content visible line width   
            
         
        """
        pass
    def GetRulesList(self) -> List[str]:
        """
         Get the ordered rules list 
         Returns rules (List[str]):  Rules list .
        """
        pass
    def SetRulesList(self, rules: List[str]) -> None:
        """
          Set the ordered rules list 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AutomationRuleBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drafting.AutomationRuleBuilder """
    @property
    def AllowInsideGeometry(self) -> bool:
        """
        Getter for property: (bool) AllowInsideGeometry
         Returns the allow inside geometry option allows annotation inside geometry   
            
         
        """
        pass
    @AllowInsideGeometry.setter
    def AllowInsideGeometry(self, allowInsideGeometry: bool):
        """
        Setter for property: (bool) AllowInsideGeometry
         Returns the allow inside geometry option allows annotation inside geometry   
            
         
        """
        pass
    @property
    def EqualDimensionTolerance(self) -> float:
        """
        Getter for property: (float) EqualDimensionTolerance
         Returns the equal dimension comparison tolerance   
            
         
        """
        pass
    @EqualDimensionTolerance.setter
    def EqualDimensionTolerance(self, equalDimensionTolerance: float):
        """
        Setter for property: (float) EqualDimensionTolerance
         Returns the equal dimension comparison tolerance   
            
         
        """
        pass
    @property
    def HideFeetAndInchMarks(self) -> bool:
        """
        Getter for property: (bool) HideFeetAndInchMarks
         Returns the hide feet and inch marks option ShowHide feet and inch marks.  
           True to hide and False to show   
         
        """
        pass
    @HideFeetAndInchMarks.setter
    def HideFeetAndInchMarks(self, hideFeetAndInchMarks: bool):
        """
        Setter for property: (bool) HideFeetAndInchMarks
         Returns the hide feet and inch marks option ShowHide feet and inch marks.  
           True to hide and False to show   
         
        """
        pass
    @property
    def Increment(self) -> float:
        """
        Getter for property: (float) Increment
         Returns the increment Display dimension value in inches and fractions to nearest specified value   
            
         
        """
        pass
    @Increment.setter
    def Increment(self, increment: float):
        """
        Setter for property: (float) Increment
         Returns the increment Display dimension value in inches and fractions to nearest specified value   
            
         
        """
        pass
    @property
    def LowerThreshold(self) -> float:
        """
        Getter for property: (float) LowerThreshold
         Returns the lower threshold display dimension value in feet, inches and fractions if
                    it is greater than the specified value   
            
         
        """
        pass
    @LowerThreshold.setter
    def LowerThreshold(self, lowerThreshold: float):
        """
        Setter for property: (float) LowerThreshold
         Returns the lower threshold display dimension value in feet, inches and fractions if
                    it is greater than the specified value   
            
         
        """
        pass
    @property
    def MaximumGapToGeometry(self) -> float:
        """
        Getter for property: (float) MaximumGapToGeometry
         Returns the maximum gap from the view geometry to the annotation   
            
         
        """
        pass
    @MaximumGapToGeometry.setter
    def MaximumGapToGeometry(self, maximumGapToGeometry: float):
        """
        Setter for property: (float) MaximumGapToGeometry
         Returns the maximum gap from the view geometry to the annotation   
            
         
        """
        pass
    @property
    def MinimumGapBetweenAnnotations(self) -> float:
        """
        Getter for property: (float) MinimumGapBetweenAnnotations
         Returns the minimum gap between annotations   
            
         
        """
        pass
    @MinimumGapBetweenAnnotations.setter
    def MinimumGapBetweenAnnotations(self, minimumGapBetweenAnnotations: float):
        """
        Setter for property: (float) MinimumGapBetweenAnnotations
         Returns the minimum gap between annotations   
            
         
        """
        pass
    @property
    def MinimumGapToGeometry(self) -> float:
        """
        Getter for property: (float) MinimumGapToGeometry
         Returns the minimum gap from the view geometry to the annotation   
            
         
        """
        pass
    @MinimumGapToGeometry.setter
    def MinimumGapToGeometry(self, minimumGapToGeometry: float):
        """
        Setter for property: (float) MinimumGapToGeometry
         Returns the minimum gap from the view geometry to the annotation   
            
         
        """
        pass
    @property
    def ReferenceGeometryGapTolerance(self) -> float:
        """
        Getter for property: (float) ReferenceGeometryGapTolerance
         Returns the reference geometry search gap tolerance   
            
         
        """
        pass
    @ReferenceGeometryGapTolerance.setter
    def ReferenceGeometryGapTolerance(self, referenceGeometryGapTolerance: float):
        """
        Setter for property: (float) ReferenceGeometryGapTolerance
         Returns the reference geometry search gap tolerance   
            
         
        """
        pass
    @property
    def RoundFeetAndInches(self) -> bool:
        """
        Getter for property: (bool) RoundFeetAndInches
         Returns the round feet and inches determine wheather or not to display dimension value 
                    in inches and fractions to nearest specified value   
            
         
        """
        pass
    @RoundFeetAndInches.setter
    def RoundFeetAndInches(self, roundFeetAndInches: bool):
        """
        Setter for property: (bool) RoundFeetAndInches
         Returns the round feet and inches determine wheather or not to display dimension value 
                    in inches and fractions to nearest specified value   
            
         
        """
        pass
    @property
    def UseFeetInchesAndFraction(self) -> bool:
        """
        Getter for property: (bool) UseFeetInchesAndFraction
         Returns the use feet inches and fraction determine wheather or not to display dimension value 
                    in feet, inches and fractions if it is greater than the specified value   
            
         
        """
        pass
    @UseFeetInchesAndFraction.setter
    def UseFeetInchesAndFraction(self, useFeetInchesAndFraction: bool):
        """
        Setter for property: (bool) UseFeetInchesAndFraction
         Returns the use feet inches and fraction determine wheather or not to display dimension value 
                    in feet, inches and fractions if it is greater than the specified value   
            
         
        """
        pass
    def GetRulesList(self) -> List[str]:
        """
         The automation rules in the order of decreasing priorities. So, the first
                    rule in the VLA has the highest priority 
         Returns rules (List[str]):  Rules list .
        """
        pass
    def SetRulesList(self, rules: List[str]) -> None:
        """
         The set of order list 
        """
        pass
import NXOpen
class BaseEditSettingsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drafting.BaseEditSettingsBuilder.
    It provides an interface for editing settings.
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class CutCopyPasteBuilder(NXOpen.Builder): 
    """
        Represents a paste in Drafting.
    """
    class TypeOperation(Enum):
        """
        Members Include: 
         |Copy|  Copy type 
         |Cut|  Cut type 

        """
        Copy: int
        Cut: int
        @staticmethod
        def ValueOf(value: int) -> CutCopyPasteBuilder.TypeOperation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypePaste(Enum):
        """
        Members Include: 
         |Transform|  Transform type 
         |Tracking|  Tracking type 

        """
        Transform: int
        Tracking: int
        @staticmethod
        def ValueOf(value: int) -> CutCopyPasteBuilder.TypePaste:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CutCopyPasteLeader(self) -> CutCopyPasteLeaderBuilder:
        """
        Getter for property: ( CutCopyPasteLeaderBuilder NXOpen.) CutCopyPasteLeader
         Returns the leader builder.  
             
         
        """
        pass
    @property
    def DestinationView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) DestinationView
         Returns the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    @DestinationView.setter
    def DestinationView(self, destinationView: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) DestinationView
         Returns the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    @property
    def ObjectsToCopy(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) ObjectsToCopy
         Returns the objects list to copy.  
           May include drafting geometry, sketch objects
                    and simple annotations. Note that PMI, feature, view, and table objects
                    are not supported by this class.   
         
        """
        pass
    @property
    def Originals(self) -> CutCopyPasteBuilder.TypeOperation:
        """
        Getter for property: ( CutCopyPasteBuilder.TypeOperation NXOpen.) Originals
         Returns the operation type.  
           If it is copy, we will keept the originals. If it is cut, we will delete the originals   
         
        """
        pass
    @Originals.setter
    def Originals(self, originals: CutCopyPasteBuilder.TypeOperation):
        """
        Setter for property: ( CutCopyPasteBuilder.TypeOperation NXOpen.) Originals
         Returns the operation type.  
           If it is copy, we will keept the originals. If it is cut, we will delete the originals   
         
        """
        pass
    @property
    def OutputObjects(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) OutputObjects
         Returns  the output Objects   
            
         
        """
        pass
    @property
    def PasteType(self) -> CutCopyPasteBuilder.TypePaste:
        """
        Getter for property: ( CutCopyPasteBuilder.TypePaste NXOpen.) PasteType
         Returns the paste type   
            
         
        """
        pass
    @PasteType.setter
    def PasteType(self, pasteType: CutCopyPasteBuilder.TypePaste):
        """
        Setter for property: ( CutCopyPasteBuilder.TypePaste NXOpen.) PasteType
         Returns the paste type   
            
         
        """
        pass
    @property
    def PlaneToRestrictMotion(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) PlaneToRestrictMotion
         Returns  the plane to restrict motion   
            
         
        """
        pass
    @PlaneToRestrictMotion.setter
    def PlaneToRestrictMotion(self, plan: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) PlaneToRestrictMotion
         Returns  the plane to restrict motion   
            
         
        """
        pass
    @property
    def Transform(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ModlMotion) Transform
         Returns the motion from the default paste position   
            
         
        """
        pass
    def GetDefaultToPoint(self) -> NXOpen.Point3d:
        """
         Get the default to point. The drop location. 
         Returns dropLocation ( NXOpen.Point3d):  the drop location .
        """
        pass
    def InitPaste(self) -> None:
        """
         Make the initial drop. 
        """
        pass
    def SetDefaultToPoint(self, dropLocation: NXOpen.Point3d) -> None:
        """
         Set the default to point.  The drop location. 
        """
        pass
    def SetMoveOnCommit(self, rot: NXOpen.Matrix3x3, trans: NXOpen.Vector3d) -> None:
        """
         Set the final motion from the drop location. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CutCopyPasteLeaderBuilder(NXOpen.TaggedObject): 
    """
        Represents a Drafting Paste, especially when reassociating a leader on paste.
    """
    @property
    def DestinationView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) DestinationView
         Returns the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    @DestinationView.setter
    def DestinationView(self, destinationView: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) DestinationView
         Returns the destination view.  
            Either a drafting view or sheet view.   
         
        """
        pass
    @property
    def IsLeaderSelection(self) -> bool:
        """
        Getter for property: (bool) IsLeaderSelection
         Returns the variable of is leader selection or not  
            
         
        """
        pass
    @IsLeaderSelection.setter
    def IsLeaderSelection(self, isLeaderSelection: bool):
        """
        Setter for property: (bool) IsLeaderSelection
         Returns the variable of is leader selection or not  
            
         
        """
        pass
    @property
    def LeaderSelection(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) LeaderSelection
         Returns the selection to reassociate single leader   
            
         
        """
        pass
    @property
    def ReassociateLeader(self) -> bool:
        """
        Getter for property: (bool) ReassociateLeader
         Returns the flag to reassociate a leader   
            
         
        """
        pass
    @ReassociateLeader.setter
    def ReassociateLeader(self, reassociateLeader: bool):
        """
        Setter for property: (bool) ReassociateLeader
         Returns the flag to reassociate a leader   
            
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) Selection
         Returns the selection to reassociate leader   
            
         
        """
        pass
    def SetMoveOnCommit(self, rot: NXOpen.Matrix3x3, trans: NXOpen.Vector3d) -> None:
        """
         Set the final motion from the drop location. 
        """
        pass
import NXOpen
class DistributeAnnotationsBuilder(NXOpen.Builder): 
    """ This class is used to distribute annotations associated to a view. """
    @property
    def Views(self) -> SelectDraftingViewList:
        """
        Getter for property: ( SelectDraftingViewList NXOpen.) Views
         Returns the views in which to distribute annotations.  
             
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class DraftingApplicationManager(NXOpen.Object): 
    """ Represents an object that manages drafting objects and member views. """
    @property
    def TitleBlocks() -> NXOpen.Annotations.TitleBlockCollection:
        """
         Returns the TitleBlockCollection belonging to this part 
        """
        pass
    def CreateCutCopyPasteBuilder(self) -> CutCopyPasteBuilder:
        """
         Creates the CutCopyPaste builder 
         Returns builder ( CutCopyPasteBuilder NXOpen.): .
        """
        pass
    def CreateMoveToDrawingViewBuilder(self) -> MoveToDrawingViewBuilder:
        """
         Creates a NXOpen.Drafting.MoveToDrawingViewBuilder 
         Returns builder ( MoveToDrawingViewBuilder NXOpen.): .
        """
        pass
    def CreateSmashDrawingViewBuilder(self) -> SmashDrawingViewBuilder:
        """
         Creates a NXOpen.Drafting.SmashDrawingViewBuilder 
         Returns builder ( SmashDrawingViewBuilder NXOpen.): .
        """
        pass
import NXOpen
class DrawingAutomationWizard(NXOpen.TransientObject): 
    """ Represents callback data for the drawing automation wizard. """
    @property
    def Builder(self) -> DrawingCreationWizardBuilder:
        """
        Getter for property: ( DrawingCreationWizardBuilder NXOpen.) Builder
         Returns the drawing automation wizard builder   
            
         
        """
        pass
    @Builder.setter
    def Builder(self, builder: DrawingCreationWizardBuilder):
        """
        Setter for property: ( DrawingCreationWizardBuilder NXOpen.) Builder
         Returns the drawing automation wizard builder   
            
         
        """
        pass
    @property
    def ContinueProcessing(self) -> bool:
        """
        Getter for property: (bool) ContinueProcessing
         Returns the flag denoting whether or not to create the booklet in the current session   
            
         
        """
        pass
    @ContinueProcessing.setter
    def ContinueProcessing(self, continueProcessing: bool):
        """
        Setter for property: (bool) ContinueProcessing
         Returns the flag denoting whether or not to create the booklet in the current session   
            
         
        """
        pass
    @property
    def ErrorCode(self) -> int:
        """
        Getter for property: (int) ErrorCode
         Returns the error code to be returned from the callback   
            
         
        """
        pass
    @ErrorCode.setter
    def ErrorCode(self, errorCode: int):
        """
        Setter for property: (int) ErrorCode
         Returns the error code to be returned from the callback   
            
         
        """
        pass
    @property
    def Part(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Part
         Returns the part from which the booklet drawings are created   
            
         
        """
        pass
    @Part.setter
    def Part(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Part
         Returns the part from which the booklet drawings are created   
            
         
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
import NXOpen
import NXOpen.Assemblies
import NXOpen.PDM
class DrawingCreationWizardBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drafting.DrawingCreationWizardBuilder.  This class is
    used to create Booklets (i.e. a set of fully populated drawings).  The builder operates
    in both create and edit modes as well as in native and managed (Teamcenter) modes.  The
    following information is important when using this builder in edit mode:
    
        
        Native Mode
            
                
                The NXOpen.Drafting.DrawingCreationWizardBuilder.Folder must be the first thing set after creating the builder.
                Setting this will populate the builder with the booklet's information.
                
            
        
        
        Managed Mode
            
                
                The NXOpen.Drafting.DrawingCreationWizardBuilder.Number and NXOpen.Drafting.DrawingCreationWizardBuilder.Revision must be the first things set after
                creating the builder (in that order).  The setting of the NXOpen.Drafting.DrawingCreationWizardBuilder.Revision will populate the builder with the booklet's information.
                
            
        
    
    """
    @property
    def ApplyTemplateToAll(self) -> bool:
        """
        Getter for property: (bool) ApplyTemplateToAll
         Returns the flag which controls the behavior of setting  NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate 
                    on an item in  NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent .  
           When set to true the builder
                    will respond to the setting of  NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate  on an item in
                     NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent  by setting the same value on
                     NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate  on all of the other items in
                     NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent    
         
        """
        pass
    @ApplyTemplateToAll.setter
    def ApplyTemplateToAll(self, applyTemplateToAll: bool):
        """
        Setter for property: (bool) ApplyTemplateToAll
         Returns the flag which controls the behavior of setting  NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate 
                    on an item in  NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent .  
           When set to true the builder
                    will respond to the setting of  NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate  on an item in
                     NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent  by setting the same value on
                     NXOpen::Drafting::PrimaryContentItemBuilder::GeometryTemplate  on all of the other items in
                     NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent    
         
        """
        pass
    @property
    def Attributes(self) -> AttributeItemBuilderList:
        """
        Getter for property: ( AttributeItemBuilderList NXOpen.) Attributes
         Returns the attributes.  
             
         
        """
        pass
    @property
    def DetailID(self) -> str:
        """
        Getter for property: (str) DetailID
         Returns the detail id.  
             
         
        """
        pass
    @DetailID.setter
    def DetailID(self, detailID: str):
        """
        Setter for property: (str) DetailID
         Returns the detail id.  
             
         
        """
        pass
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the discipline.  
             
         
        """
        pass
    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
         Returns the discipline.  
             
         
        """
        pass
    @property
    def DrawingStyle(self) -> str:
        """
        Getter for property: (str) DrawingStyle
         Returns the drawing style.  
             
         
        """
        pass
    @DrawingStyle.setter
    def DrawingStyle(self, drawingStyle: str):
        """
        Setter for property: (str) DrawingStyle
         Returns the drawing style.  
             
         
        """
        pass
    @property
    def ExcludedContent(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) ExcludedContent
         Returns the excluded content.  
           Setting a component into  NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent  
                    will cause that component to be removed from  NXOpen::Drafting::PrimaryContentItemBuilder::Content 
                    of each item in  NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent  and 
                     NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent  if they contain that component.   
         
        """
        pass
    @property
    def Folder(self) -> str:
        """
        Getter for property: (str) Folder
         Returns the folder.  
             
         
        """
        pass
    @Folder.setter
    def Folder(self, foldername: str):
        """
        Setter for property: (str) Folder
         Returns the folder.  
             
         
        """
        pass
    @property
    def IntroductoryTemplate(self) -> str:
        """
        Getter for property: (str) IntroductoryTemplate
         Returns the introductory template.  
             
         
        """
        pass
    @IntroductoryTemplate.setter
    def IntroductoryTemplate(self, introductoryTemplate: str):
        """
        Setter for property: (str) IntroductoryTemplate
         Returns the introductory template.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def Number(self) -> str:
        """
        Getter for property: (str) Number
         Returns the number.  
           This property is only used in managed mode and must be set before anything else.    
         
        """
        pass
    @Number.setter
    def Number(self, number: str):
        """
        Setter for property: (str) Number
         Returns the number.  
           This property is only used in managed mode and must be set before anything else.    
         
        """
        pass
    @property
    def PrimaryContent(self) -> PrimaryContentItemBuilderList:
        """
        Getter for property: ( PrimaryContentItemBuilderList NXOpen.) PrimaryContent
         Returns the primary content.  
           Setting a component into  NXOpen::Drafting::PrimaryContentItemBuilder::Content  of an item in
                     NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent  will cause that component to be removed from 
                     NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent  and 
                     NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent  if they contain that component.   
         
        """
        pass
    @property
    def References(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) References
         Returns the references.  
             
         
        """
        pass
    @property
    def Revision(self) -> str:
        """
        Getter for property: (str) Revision
         Returns the revision.  
           This is only used in managed mode. In edit mode it must be set after the  NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber  and at the time
                    is set it will populate the builder with the booklet's information.   
         
        """
        pass
    @Revision.setter
    def Revision(self, revision: str):
        """
        Setter for property: (str) Revision
         Returns the revision.  
           This is only used in managed mode. In edit mode it must be set after the  NXOpen::Drafting::DrawingCreationWizardBuilder::SetNumber  and at the time
                    is set it will populate the builder with the booklet's information.   
         
        """
        pass
    @property
    def SecondaryContent(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) SecondaryContent
         Returns the secondary content.  
           Setting a component into  NXOpen::Drafting::DrawingCreationWizardBuilder::SecondaryContent  
                    will cause that component to be removed from  NXOpen::Drafting::PrimaryContentItemBuilder::Content 
                    of each item in  NXOpen::Drafting::DrawingCreationWizardBuilder::PrimaryContent  and 
                     NXOpen::Drafting::DrawingCreationWizardBuilder::ExcludedContent  if they contain that component.   
         
        """
        pass
    def GetSummary(self) -> List[str]:
        """
         Returns the summary.  This is in HTML format. 
         Returns summary (List[str]): .
        """
        pass
    def SetObjectCreateBuilder(self, objectCreateBuilder: NXOpen.PDM.ObjectCreateBuilder) -> None:
        """
         Sets NXOpen.PDM.ObjectCreateBuilder 
        """
        pass
    def SetSummary(self, summary: List[str]) -> None:
        """
         Sets the summary 
        """
        pass
import NXOpen
class MoveToDrawingViewBuilder(NXOpen.Builder): 
    """ This builder allows the user to extract contents from a sheet and transfer them to a new Drawing
        view, also provide some other options for view creation
     """
    @property
    def SelectObjects(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectObjects
         Returns the select objects from the current sheet  
            
         
        """
        pass
    @property
    def SelectPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SelectPoint
         Returns the select point to calculate the new created drawing view's reference point  
            
         
        """
        pass
    @SelectPoint.setter
    def SelectPoint(self, selectPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SelectPoint
         Returns the select point to calculate the new created drawing view's reference point  
            
         
        """
        pass
    @property
    def TwoDOrientation(self) -> View2dOrientBuilder:
        """
        Getter for property: ( View2dOrientBuilder NXOpen.) TwoDOrientation
         Returns the view orientation   
            
         
        """
        pass
    @property
    def ViewScale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) ViewScale
         Returns the view scale   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style   
            
         
        """
        pass
    @property
    def XCoordinate(self) -> float:
        """
        Getter for property: (float) XCoordinate
         Returns the x coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    @XCoordinate.setter
    def XCoordinate(self, xCoordinate: float):
        """
        Setter for property: (float) XCoordinate
         Returns the x coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    @property
    def YCoordinate(self) -> float:
        """
        Getter for property: (float) YCoordinate
         Returns the y coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
    @YCoordinate.setter
    def YCoordinate(self, yCoordinate: float):
        """
        Setter for property: (float) YCoordinate
         Returns the y coordinate to calculate the new created drawing view's reference point  
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drafting.PreferencesBuilder builder """
    @property
    def AnnotationOriginAlignment(self) -> NXOpen.Annotations.OriginAlignmentBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginAlignmentBuilder) AnnotationOriginAlignment
         Returns the annotation origin alignment   
            
         
        """
        pass
    @property
    def AnnotationStyle(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) AnnotationStyle
         Returns the annotation style builder   
            
         
        """
        pass
    @property
    def AssemblyCreationSettingsBuilder(self) -> AssemblyCreationSettingsBuilder:
        """
        Getter for property: ( AssemblyCreationSettingsBuilder NXOpen.) AssemblyCreationSettingsBuilder
         Returns the assembly creation from 2d component builder   
            
         
        """
        pass
    @property
    def AutomationBooklet(self) -> AutomationBookletBuilder:
        """
        Getter for property: ( AutomationBookletBuilder NXOpen.) AutomationBooklet
         Returns    the AutomationBookletBuilder builder   
            
         
        """
        pass
    @property
    def AutomationRule(self) -> AutomationRuleBuilder:
        """
        Getter for property: ( AutomationRuleBuilder NXOpen.) AutomationRule
         Returns the drafting automation rule builder   
            
         
        """
        pass
    @property
    def AutomationTemplateRegion(self) -> AutomationTemplateRegionBuilder:
        """
        Getter for property: ( AutomationTemplateRegionBuilder NXOpen.) AutomationTemplateRegion
         Returns    the AutomationTemplateRegion builder   
            
         
        """
        pass
    @property
    def BendTable(self) -> NXOpen.Annotations.BendTableSettingsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.BendTableSettingsBuilder) BendTable
         Returns the Bend table settings builder   
            
         
        """
        pass
    @property
    def BorderAndZoneStyle(self) -> BorderAndZoneStyleBuilder:
        """
        Getter for property: ( BorderAndZoneStyleBuilder NXOpen.) BorderAndZoneStyle
         Returns the border and zone style builder   
            
         
        """
        pass
    @property
    def CommonWorkflow(self) -> NXOpen.Annotations.CommonWorkflowBuilder:
        """
        Getter for property: ( NXOpen.Annotations.CommonWorkflowBuilder) CommonWorkflow
         Returns the common workflow builder   
            
         
        """
        pass
    @property
    def Component2dSettings(self) -> ComponentSettingsBlockBuilder:
        """
        Getter for property: ( ComponentSettingsBlockBuilder NXOpen.) Component2dSettings
         Returns the 2d component settings block builder, this builder stores the settings of the 2d component   
            
         
        """
        pass
    @property
    def CreateComponentFrom3DSettingsBuilder(self) -> CreateComponentFrom3DSettingsBuilder:
        """
        Getter for property: ( CreateComponentFrom3DSettingsBuilder NXOpen.) CreateComponentFrom3DSettingsBuilder
         Returns the create component from 3d builder   
            
         
        """
        pass
    @property
    def DimensionOriginAlignment(self) -> NXOpen.Annotations.OriginAlignmentBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginAlignmentBuilder) DimensionOriginAlignment
         Returns the dimension origin alignment   
            
         
        """
        pass
    @property
    def DimensionWorkflow(self) -> NXOpen.Annotations.DimensionWorkflowBuilder:
        """
        Getter for property: ( NXOpen.Annotations.DimensionWorkflowBuilder) DimensionWorkflow
         Returns the Dimension Workflow builder   
            
         
        """
        pass
    @property
    def DrawingFormatTitle(self) -> NXOpen.Annotations.DrawingFormatTitleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.DrawingFormatTitleBuilder) DrawingFormatTitle
         Returns    the drawing format title block builder    
            
         
        """
        pass
    @property
    def DrawingFormatsheet(self) -> DrawingFormatSheetBuilder:
        """
        Getter for property: ( DrawingFormatSheetBuilder NXOpen.) DrawingFormatsheet
         Returns    the drawing format sheet builder   
            
         
        """
        pass
    @property
    def FramebarGeneral(self) -> NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder:
        """
        Getter for property: ( NXOpen.Annotations.ShipDraftingFramebarGeneralBuilder) FramebarGeneral
         Returns    the framebar general builder   
            
         
        """
        pass
    @property
    def GeneralLayoutPreferencesBuilder(self) -> GeneralPreferencesBuilder:
        """
        Getter for property: ( GeneralPreferencesBuilder NXOpen.) GeneralLayoutPreferencesBuilder
         Returns the general layout preferences builder   
            
         
        """
        pass
    @property
    def HoleTableContent(self) -> NXOpen.Annotations.HoleTableSettingsContentBuilder:
        """
        Getter for property: ( NXOpen.Annotations.HoleTableSettingsContentBuilder) HoleTableContent
         Returns the Hole table settings content builder   
            
         
        """
        pass
    @property
    def HoleTableFormat(self) -> NXOpen.Annotations.HoleTableSettingsFormatBuilder:
        """
        Getter for property: ( NXOpen.Annotations.HoleTableSettingsFormatBuilder) HoleTableFormat
         Returns the Hole table settings format builder   
            
         
        """
        pass
    @property
    def HoleTableHoleFilters(self) -> NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder:
        """
        Getter for property: ( NXOpen.Annotations.HoleTableSettingsHoleFiltersBuilder) HoleTableHoleFilters
         Returns the Hole table settings hole filters builder   
            
         
        """
        pass
    @property
    def HoleTableLabel(self) -> NXOpen.Annotations.HoleTableSettingsLabelBuilder:
        """
        Getter for property: ( NXOpen.Annotations.HoleTableSettingsLabelBuilder) HoleTableLabel
         Returns the Hole table settings label builder   
            
         
        """
        pass
    @property
    def HoleTableWorkflow(self) -> NXOpen.Annotations.HoleTableSettingsWorkflowBuilder:
        """
        Getter for property: ( NXOpen.Annotations.HoleTableSettingsWorkflowBuilder) HoleTableWorkflow
         Returns the Hole table settings workflow builder   
            
         
        """
        pass
    @property
    def PartFamilyTable(self) -> NXOpen.Annotations.PartFamilyTableSettingsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PartFamilyTableSettingsBuilder) PartFamilyTable
         Returns the Part Family table settings builder   
            
         
        """
        pass
    @property
    def PartsList(self) -> NXOpen.Annotations.PartsListBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PartsListBuilder) PartsList
         Returns    the parts list style builder   
            
         
        """
        pass
    @property
    def RetainedAnnotations(self) -> NXOpen.Annotations.RetainedAnnotationsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.RetainedAnnotationsBuilder) RetainedAnnotations
         Returns    the General Retained Annotations builder   
            
         
        """
        pass
    @property
    def SymbolWorkflow(self) -> NXOpen.Annotations.SymbolWorkflowBuilder:
        """
        Getter for property: ( NXOpen.Annotations.SymbolWorkflowBuilder) SymbolWorkflow
         Returns    the SymbolWorkflow builder   
            
         
        """
        pass
    @property
    def TableCellStyle(self) -> NXOpen.Annotations.TableCellStyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TableCellStyleBuilder) TableCellStyle
         Returns the table cell style builder   
            
         
        """
        pass
    @property
    def TableOriginAlignment(self) -> NXOpen.Annotations.OriginAlignmentBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginAlignmentBuilder) TableOriginAlignment
         Returns the table origin alignment   
            
         
        """
        pass
    @property
    def TableSection(self) -> NXOpen.Annotations.TableSectionStyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TableSectionStyleBuilder) TableSection
         Returns    the table section style builder   
            
         
        """
        pass
    @property
    def TabularNoteStyle(self) -> NXOpen.Annotations.TabularNoteStyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TabularNoteStyleBuilder) TabularNoteStyle
         Returns the tabular note style builder   
            
         
        """
        pass
    @property
    def TrackDrawingChangesGeneral(self) -> TrackDrawingChangesGeneralBuilder:
        """
        Getter for property: ( TrackDrawingChangesGeneralBuilder NXOpen.) TrackDrawingChangesGeneral
         Returns the track drawing changes general settings builder   
            
         
        """
        pass
    @property
    def TrackDrawingChangesReportFilter(self) -> TrackDrawingChangesReportFilterBuilder:
        """
        Getter for property: ( TrackDrawingChangesReportFilterBuilder NXOpen.) TrackDrawingChangesReportFilter
         Returns the track drawing changes report filter builder   
            
         
        """
        pass
    @property
    def ViewBreak(self) -> ViewBreakBuilder:
        """
        Getter for property: ( ViewBreakBuilder NXOpen.) ViewBreak
         Returns the view break builder   
            
         
        """
        pass
    @property
    def ViewDetailLabel(self) -> ViewDetailLabelBuilder:
        """
        Getter for property: ( ViewDetailLabelBuilder NXOpen.) ViewDetailLabel
         Returns    the view detail label builder   
            
         
        """
        pass
    @property
    def ViewLabel(self) -> ViewLabelBuilder:
        """
        Getter for property: ( ViewLabelBuilder NXOpen.) ViewLabel
         Returns    the view label builder   
            
         
        """
        pass
    @property
    def ViewProjectedLabel(self) -> ViewProjectedLabelBuilder:
        """
        Getter for property: ( ViewProjectedLabelBuilder NXOpen.) ViewProjectedLabel
         Returns    the view projected label builder   
            
         
        """
        pass
    @property
    def ViewSectionLabel(self) -> ViewSectionLabelBuilder:
        """
        Getter for property: ( ViewSectionLabelBuilder NXOpen.) ViewSectionLabel
         Returns    the view section label builder   
            
         
        """
        pass
    @property
    def ViewSectionLine(self) -> ViewSectionLineBuilder:
        """
        Getter for property: ( ViewSectionLineBuilder NXOpen.) ViewSectionLine
         Returns    the Section Line builder   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style builder   
            
         
        """
        pass
    @property
    def ViewWorkflow(self) -> ViewWorkflowBuilder:
        """
        Getter for property: ( ViewWorkflowBuilder NXOpen.) ViewWorkflow
         Returns the view workflow builder   
            
         
        """
        pass
    @property
    def VisualDrawingCompare(self) -> VisualDrawingComparePrefsBuilder:
        """
        Getter for property: ( VisualDrawingComparePrefsBuilder NXOpen.) VisualDrawingCompare
         Returns the visual drawing compare settings builder   
            
         
        """
        pass
    @property
    def Workflow(self) -> GeneralWorkFlowBuilder:
        """
        Getter for property: ( GeneralWorkFlowBuilder NXOpen.) Workflow
         Returns    the general workflow builder   
            
         
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
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
    def SynchronizeFCFSymbolSequence(self) -> None:
        """
         Synchronize fcf symbol sequence 
        """
        pass
import NXOpen
class PrimaryContentItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PrimaryContentItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PrimaryContentItemBuilder) -> None:
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
    def Erase(self, obj: PrimaryContentItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PrimaryContentItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PrimaryContentItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PrimaryContentItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PrimaryContentItemBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PrimaryContentItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PrimaryContentItemBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PrimaryContentItemBuilder) -> None:
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
    def SetContents(self, objects: List[PrimaryContentItemBuilder]) -> None:
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
    def Swap(self, object1: PrimaryContentItemBuilder, object2: PrimaryContentItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities
class PrimaryContentItemBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drafting.PrimaryContentItemBuilder.  This class is
    used to specify information pertaining to the primary content of a Drawing Booklet.
    Each instance represents a single drawing in a booklet.
    """
    @property
    def Content(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) Content
         Returns the content.  
             
         
        """
        pass
    @property
    def GeometryTemplate(self) -> str:
        """
        Getter for property: (str) GeometryTemplate
         Returns the geometry template.  
             
         
        """
        pass
    @GeometryTemplate.setter
    def GeometryTemplate(self, geometryTemplate: str):
        """
        Setter for property: (str) GeometryTemplate
         Returns the geometry template.  
             
         
        """
        pass
import NXOpen
class RulesBuilder(NXOpen.Builder): 
    """ This class is used to specify knowledge fusion rules in a drawing template. The rules are 
        executed when the template is instantiated. """
    @property
    def DimensionRule(self) -> str:
        """
        Getter for property: (str) DimensionRule
         Returns the dimension rule   
            
         
        """
        pass
    @DimensionRule.setter
    def DimensionRule(self, dimensionRule: str):
        """
        Setter for property: (str) DimensionRule
         Returns the dimension rule   
            
         
        """
        pass
    @property
    def NoteRule(self) -> str:
        """
        Getter for property: (str) NoteRule
         Returns the note rule   
            
         
        """
        pass
    @NoteRule.setter
    def NoteRule(self, noteRule: str):
        """
        Setter for property: (str) NoteRule
         Returns the note rule   
            
         
        """
        pass
    @property
    def SymbolRule(self) -> str:
        """
        Getter for property: (str) SymbolRule
         Returns the symbol rule   
            
         
        """
        pass
    @SymbolRule.setter
    def SymbolRule(self, symbolRule: str):
        """
        Setter for property: (str) SymbolRule
         Returns the symbol rule   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class SettingsManager(NXOpen.Object): 
    """ Represents an object that manages drafting settings. """
    def CreateAnnotationEditSettingsBuilder(self, objects: List[NXOpen.DisplayableObject]) -> NXOpen.Annotations.EditSettingsBuilder:
        """
         Creates a NXOpen.Annotations.EditSettingsBuilder
                    
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call Drafting.SettingsManager.ProcessForMultipleObjectsSettings 
                    after creating all settings builder for selected objects.  
                
         Returns builder ( NXOpen.Annotations.EditSettingsBuilder):  The annotations settings builder .
        """
        pass
    def CreateDrawingEditSectionLineSettingsBuilder(self, sectionLines: List[SectionLine]) -> EditSectionLineSettingsBuilder:
        """
         Creates a NXOpen.Drawings.EditSectionLineSettingsBuilder
                    
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call Drafting.SettingsManager.ProcessForMultipleObjectsSettings 
                    after creating all settings builder for selected objects.  
                
         Returns builder ( EditSectionLineSettingsBuilder NXOpen.):  The section line settings builder .
        """
        pass
    def CreateDrawingEditViewLabelSettingsBuilder(self, viewLabels: List[NXOpen.DisplayableObject]) -> EditViewLabelSettingsBuilder:
        """
         Creates a NXOpen.Drawings.EditViewLabelSettingsBuilder
                    
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call Drafting.SettingsManager.ProcessForMultipleObjectsSettings 
                    after creating all settings builder for selected objects. 
                
         Returns builder ( EditViewLabelSettingsBuilder NXOpen.):  The view label settings builder .
        """
        pass
    def CreateDrawingEditViewSettingsBuilder(self, views: List[NXOpen.View]) -> EditViewSettingsBuilder:
        """
         Creates a NXOpen.Drawings.EditViewSettingsBuilder
                    
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call Drafting.SettingsManager.ProcessForMultipleObjectsSettings 
                    after creating all settings builder for selected objects. 
                
         Returns builder ( EditViewSettingsBuilder NXOpen.):  The view settings builder .
        """
        pass
    def CreateLayout2dEditComponentSettingsBuilder(self, components: List[Component]) -> EditComponentSettingsBuilder:
        """
         Creates a NXOpen.Layout2d.EditComponentSettingsBuilder 
                    This builder is the interface to edit the 2d component settings of layout
                    
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call Drafting.SettingsManager.ProcessForMultipleObjectsSettings 
                    after creating all settings builder for selected objects. 
                
         Returns builder ( EditComponentSettingsBuilder NXOpen.):  The layout2d component settings builder .
        """
        pass
    def CreatePreferencesBuilder(self) -> PreferencesBuilder:
        """
         Creates a NXOpen.Drafting.PreferencesBuilder 
                
         Returns builder ( PreferencesBuilder NXOpen.): .
        """
        pass
    def CreateTableEditSettingsBuilder(self, objects: List[NXOpen.DisplayableObject]) -> NXOpen.Annotations.TableEditSettingsBuilder:
        """
         Creates a NXOpen.Annotations.TableEditSettingsBuilder
                    
                    For multiple object settings, first create primary settings builder by passing all 
                    selected 'n' objects.Then create 'n-1' secondary builders by passing single selected 
                    object starting from second selected object.
                    Client must call Drafting.SettingsManager.ProcessForMultipleObjectsSettings 
                    after creating all settings builder for selected objects. 
                
         Returns builder ( NXOpen.Annotations.TableEditSettingsBuilder):  The table settings builder .
        """
        pass
    @overload
    def CreateTableRowSortingBuilder(self, objects: List[NXOpen.DisplayableObject]) -> NXOpen.Annotations.TableRowSortingBuilder:
        """
         Creates a Annotations.TableRowSortingBuilder 
         Returns builder ( NXOpen.Annotations.TableRowSortingBuilder):  The table sorting builder .
        """
        pass
    @overload
    def CreateTableRowSortingBuilder(self, tableObject: NXOpen.Annotations.Table) -> NXOpen.Annotations.TableRowSortingBuilder:
        """
         Creates a Annotations.TableRowSortingBuilder from Table
         Returns builder ( NXOpen.Annotations.TableRowSortingBuilder):  The table sorting builder .
        """
        pass
    def ProcessForMultipleObjectsSettings(self, editSettingsBuilders: List[BaseEditSettingsBuilder]) -> None:
        """
         Process edit settings builders for multiple objects
                    User must call this API for multiple object settings and pass all edit settings builders for selected objects
                
        """
        pass
    def ProcessForMutipleObjectsSettings(self, editSettingsBuilders: List[BaseEditSettingsBuilder]) -> None:
        """
         Process edit settings builders for mutiple objects
                
        """
        pass
import NXOpen
class SmashDrawingViewBuilder(NXOpen.Builder): 
    """ 
    This builder allows the user to break a Drawing View into its parts and delete the Drawing View
     """
    @property
    def SelectView(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) SelectView
         Returns the select drawing views to smash  
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class SpecifyRuleBuilder(NXOpen.Builder): 
    """ This class is used to specify knowledge fusion rule for a note object in a drawing template. 
        The rule is stored on the note and is executed when the template is instantiated. """
    @property
    def Note(self) -> NXOpen.Annotations.Note:
        """
        Getter for property: ( NXOpen.Annotations.Note) Note
         Returns the note to add rule to  
            
         
        """
        pass
    @Note.setter
    def Note(self, note: NXOpen.Annotations.Note):
        """
        Setter for property: ( NXOpen.Annotations.Note) Note
         Returns the note to add rule to  
            
         
        """
        pass
    @property
    def Rule(self) -> str:
        """
        Getter for property: (str) Rule
         Returns the rule   
            
         
        """
        pass
    @Rule.setter
    def Rule(self, rule: str):
        """
        Setter for property: (str) Rule
         Returns the rule   
            
         
        """
        pass
