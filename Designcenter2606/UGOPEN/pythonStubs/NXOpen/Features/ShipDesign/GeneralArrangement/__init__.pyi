from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DrawingAutomationBuilder(NXOpen.Builder): 
    """ This builder allows you to define the general arrangement drawing automation information. 
            It represents NXOpen.Features.ShipDesign.GeneralArrangement.DrawingAutomationBuilder.
            This builder creates one or more General Arrangement View and just returns . 
            """
    @property
    def ViewList(self) -> DrawingItemBuilderList:
        """
        Getter for property: ( DrawingItemBuilderList NXOpen.Features.ShipDe) ViewList
         Returns the general arrangement view item list   
            
         
        """
        pass
    @property
    def ViewType(self) -> str:
        """
        Getter for property: (str) ViewType
         Returns the view type   
            
         
        """
        pass
    @ViewType.setter
    def ViewType(self, viewType: str):
        """
        Setter for property: (str) ViewType
         Returns the view type   
            
         
        """
        pass
    def CreateDrawingTableItemBuilder(self) -> DrawingTableItemBuilder:
        """
         Creates a NXOpen.Features.ShipDesign.GeneralArrangement.DrawingTableItemBuilder 
         Returns drawingTableItemBuilder ( DrawingTableItemBuilder NXOpen.Features.ShipDe): .
        """
        pass
    def CreateDrawingViewItemBuilder(self) -> DrawingViewItemBuilder:
        """
         Creates a NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder 
         Returns drawingViewItemBuilder ( DrawingViewItemBuilder NXOpen.Features.ShipDe): .
        """
        pass
    def Find(self, journal_identifier: str) -> NXOpen.TaggedObject:
        """
         Find the general arrangement view item builder by the name. 
         Returns found ( NXOpen.TaggedObject):  .
        """
        pass
import NXOpen
class DrawingItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DrawingItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DrawingItemBuilder) -> None:
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
    def Erase(self, obj: DrawingItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DrawingItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DrawingItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DrawingItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DrawingItemBuilder NXOpen.Features.ShipDe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DrawingItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( DrawingItemBuilder List[NXOpen.Features.Ship):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DrawingItemBuilder) -> None:
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
    def SetContents(self, objects: List[DrawingItemBuilder]) -> None:
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
    def Swap(self, object1: DrawingItemBuilder, object2: DrawingItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class DrawingItemBuilder(NXOpen.Builder): 
    """ This builder allows you to define the general arrangement drawing item information. 
            It represents NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder.
            This builder won't create General Arrangement View and just returns . 
            """
    @property
    def CreateItem(self) -> bool:
        """
        Getter for property: (bool) CreateItem
         Returns the create item   
            
         
        """
        pass
    @CreateItem.setter
    def CreateItem(self, createItem: bool):
        """
        Setter for property: (bool) CreateItem
         Returns the create item   
            
         
        """
        pass
class DrawingTableItemBuilder(DrawingItemBuilder): 
    """ This builder allows you to define the general arrangement drawing table item information. 
            It represents NXOpen.Features.ShipDesign.GeneralArrangement.DrawingTableItemBuilder.
            This builder won't create Table and just returns . 
            """
    pass
class DrawingViewItemBuilder(DrawingItemBuilder): 
    """ This builder allows you to define the general arrangement drawing view item information. 
            It represents NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.
            This builder won't create General Arrangement View and just returns . 
            """
    class FrameBarPositionType(Enum):
        """
        Members Include: 
         |ViewTop| 
         |ViewCenterY| 
         |ViewBottom| 
         |ViewLeft| 
         |ViewCenterX| 
         |ViewRight| 

        """
        ViewTop: int
        ViewCenterY: int
        ViewBottom: int
        ViewLeft: int
        ViewCenterX: int
        ViewRight: int
        @staticmethod
        def ValueOf(value: int) -> DrawingViewItemBuilder.FrameBarPositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HorizontalFrameBarPosition(self) -> DrawingViewItemBuilder.FrameBarPositionType:
        """
        Getter for property: ( DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDe) HorizontalFrameBarPosition
         Returns the horizontal frame bar position   
            
         
        """
        pass
    @HorizontalFrameBarPosition.setter
    def HorizontalFrameBarPosition(self, horizontalFrameBarPosition: DrawingViewItemBuilder.FrameBarPositionType):
        """
        Setter for property: ( DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDe) HorizontalFrameBarPosition
         Returns the horizontal frame bar position   
            
         
        """
        pass
    @property
    def ShowFireAndSafetyPlanSymbol(self) -> bool:
        """
        Getter for property: (bool) ShowFireAndSafetyPlanSymbol
         Returns the flag to indicate whether to show the fire and safety plan symbol or not.  
             
         
        """
        pass
    @ShowFireAndSafetyPlanSymbol.setter
    def ShowFireAndSafetyPlanSymbol(self, showFireAndSafetyPlanSymbol: bool):
        """
        Setter for property: (bool) ShowFireAndSafetyPlanSymbol
         Returns the flag to indicate whether to show the fire and safety plan symbol or not.  
             
         
        """
        pass
    @property
    def ShowHorizontalFrameBar(self) -> bool:
        """
        Getter for property: (bool) ShowHorizontalFrameBar
         Returns the flag to indicate whether to show horizontal frame bar or not.  
             
         
        """
        pass
    @ShowHorizontalFrameBar.setter
    def ShowHorizontalFrameBar(self, showHorizontalFrameBar: bool):
        """
        Setter for property: (bool) ShowHorizontalFrameBar
         Returns the flag to indicate whether to show horizontal frame bar or not.  
             
         
        """
        pass
    @property
    def ShowOpeningFillingLine(self) -> bool:
        """
        Getter for property: (bool) ShowOpeningFillingLine
         Returns the flag to indicate whether to show the opening filling line or not.  
             
         
        """
        pass
    @ShowOpeningFillingLine.setter
    def ShowOpeningFillingLine(self, showOpeningFillingLine: bool):
        """
        Setter for property: (bool) ShowOpeningFillingLine
         Returns the flag to indicate whether to show the opening filling line or not.  
             
         
        """
        pass
    @property
    def ShowOverallDimension(self) -> bool:
        """
        Getter for property: (bool) ShowOverallDimension
         Returns the flag to indicate whether to show the overall dimension or not.  
             
         
        """
        pass
    @ShowOverallDimension.setter
    def ShowOverallDimension(self, showOverallDimension: bool):
        """
        Setter for property: (bool) ShowOverallDimension
         Returns the flag to indicate whether to show the overall dimension or not.  
             
         
        """
        pass
    @property
    def ShowPMILabel(self) -> bool:
        """
        Getter for property: (bool) ShowPMILabel
         Returns the flag to indicate whether to show the PMI labels or not.  
             
         
        """
        pass
    @ShowPMILabel.setter
    def ShowPMILabel(self, showPMILabel: bool):
        """
        Setter for property: (bool) ShowPMILabel
         Returns the flag to indicate whether to show the PMI labels or not.  
             
         
        """
        pass
    @property
    def ShowVerticalFrameBar(self) -> bool:
        """
        Getter for property: (bool) ShowVerticalFrameBar
         Returns the flag to indicate whether to show vertical frame bar or not.  
             
         
        """
        pass
    @ShowVerticalFrameBar.setter
    def ShowVerticalFrameBar(self, showVerticalFrameBar: bool):
        """
        Setter for property: (bool) ShowVerticalFrameBar
         Returns the flag to indicate whether to show vertical frame bar or not.  
             
         
        """
        pass
    @property
    def VerticalFrameBarPosition(self) -> DrawingViewItemBuilder.FrameBarPositionType:
        """
        Getter for property: ( DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDe) VerticalFrameBarPosition
         Returns the vertical frame bar position   
            
         
        """
        pass
    @VerticalFrameBarPosition.setter
    def VerticalFrameBarPosition(self, verticalFrameBarPosition: DrawingViewItemBuilder.FrameBarPositionType):
        """
        Setter for property: ( DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDe) VerticalFrameBarPosition
         Returns the vertical frame bar position   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class EvacuationPlanBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Features.ShipDesign.GeneralArrangement.EvacuationPlanBuilder builder . This builder returns . """
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns the color   
            
         
        """
        pass
    @property
    def HorizontalFlip(self) -> bool:
        """
        Getter for property: (bool) HorizontalFlip
         Returns the horizontal flip   
            
         
        """
        pass
    @HorizontalFlip.setter
    def HorizontalFlip(self, horizontalFlip: bool):
        """
        Setter for property: (bool) HorizontalFlip
         Returns the horizontal flip   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the annotation origin builder   
            
         
        """
        pass
    @property
    def Pattern(self) -> int:
        """
        Getter for property: (int) Pattern
         Returns the pattern   
            
         
        """
        pass
    @Pattern.setter
    def Pattern(self, pattern: int):
        """
        Setter for property: (int) Pattern
         Returns the pattern   
            
         
        """
        pass
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Scale
         Returns the scale   
            
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) Style
         Returns the annotation style builder.  
             
         
        """
        pass
    @property
    def VerticalFlip(self) -> bool:
        """
        Getter for property: (bool) VerticalFlip
         Returns the vertical flip   
            
         
        """
        pass
    @VerticalFlip.setter
    def VerticalFlip(self, verticalFlip: bool):
        """
        Setter for property: (bool) VerticalFlip
         Returns the vertical flip   
            
         
        """
        pass
    def AddExpressionData(self, strTitle: str, strFormular: str) -> None:
        """
         Adds expression data
        """
        pass
    def ClearExpressionsData(self) -> None:
        """
         Clears the expressions data
        """
        pass
import NXOpen
class FaceCharacteristicsBuilder(NXOpen.Builder): 
    """ Represents a builder to be used to add face characteristics attributes and color to specified faces. """
    @property
    def CharacteristicColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CharacteristicColor
         Returns the characteristic color to assign to the selected face.  
            
         
        """
        pass
    @CharacteristicColor.setter
    def CharacteristicColor(self, characteristicColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CharacteristicColor
         Returns the characteristic color to assign to the selected face.  
            
         
        """
        pass
    @property
    def CharacteristicValue(self) -> int:
        """
        Getter for property: (int) CharacteristicValue
         Returns the characteristic value to assign to the selected face.  
            
         
        """
        pass
    @CharacteristicValue.setter
    def CharacteristicValue(self, characteristicValue: int):
        """
        Setter for property: (int) CharacteristicValue
         Returns the characteristic value to assign to the selected face.  
            
         
        """
        pass
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFace
         Returns the face to assign the specific characteristics.  
            
         
        """
        pass
