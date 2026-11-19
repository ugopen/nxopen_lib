from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This builder allows you to define the general arrangement drawing automation information. 
##             It represents @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder@endlink .
##             This builder creates one or more General Arrangement View and just returns NULL. 
##              <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateGeneralArrangementDrawingAutomationBuilder  NXOpen::Features::ShipCollection::CreateGeneralArrangementDrawingAutomationBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class DrawingAutomationBuilder(NXOpen.Builder): 
    """ This builder allows you to define the general arrangement drawing automation information. 
            It represents <ja_class>NXOpen.Features.ShipDesign.GeneralArrangement.DrawingAutomationBuilder</ja_class>.
            This builder creates one or more General Arrangement View and just returns <ja_NULL>. 
            """


    ## Getter for property: (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) ViewList
    ##  Returns the general arrangement view item list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return DrawingItemBuilderList
    @property
    def ViewList(self) -> DrawingItemBuilderList:
        """
        Getter for property: (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) ViewList
         Returns the general arrangement view item list   
            
         
        """
        pass
    
    ## Getter for property: (str) ViewType
    ##  Returns the view type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def ViewType(self) -> str:
        """
        Getter for property: (str) ViewType
         Returns the view type   
            
         
        """
        pass
    
    ## Setter for property: (str) ViewType

    ##  Returns the view type   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ViewType.setter
    def ViewType(self, viewType: str):
        """
        Setter for property: (str) ViewType
         Returns the view type   
            
         
        """
        pass
    
    ##  Creates a @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder@endlink  
    ##  @return drawingTableItemBuilder (@link DrawingTableItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingTableItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    def CreateDrawingTableItemBuilder(self) -> DrawingTableItemBuilder:
        """
         Creates a @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder@endlink  
         @return drawingTableItemBuilder (@link DrawingTableItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingTableItemBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingViewItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingViewItemBuilder@endlink  
    ##  @return drawingViewItemBuilder (@link DrawingViewItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    def CreateDrawingViewItemBuilder(self) -> DrawingViewItemBuilder:
        """
         Creates a @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingViewItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingViewItemBuilder@endlink  
         @return drawingViewItemBuilder (@link DrawingViewItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder@endlink): .
        """
        pass
    
    ##  Find the general arrangement view item builder by the name. 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Journal identifier of the object </param>
    def Find(self, journal_identifier: str) -> NXOpen.TaggedObject:
        """
         Find the general arrangement view item builder by the name. 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class DrawingItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
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
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="objects"> (@link DrawingItemBuilder List[NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[DrawingItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: DrawingItemBuilder) -> None:
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
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
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
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
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
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="obj"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: DrawingItemBuilder) -> None:
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
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="obj"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: DrawingItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## 
    ## <param name="obj"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: DrawingItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> DrawingItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link DrawingItemBuilder List[NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[DrawingItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link DrawingItemBuilder List[NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: DrawingItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
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
    ## 
    ## <param name="objects"> (@link DrawingItemBuilder List[NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[DrawingItemBuilder]) -> None:
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
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
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
    ## <param name="object_list"> (@link DrawingItemBuilderList NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilderList@endlink) </param>
    ## <param name="object1"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link DrawingItemBuilder NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: DrawingItemBuilder, object2: DrawingItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  This builder allows you to define the general arrangement drawing item information. 
##             It represents @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingItemBuilder@endlink .
##             This builder won't create General Arrangement View and just returns NULL. 
##              <br> To obtain an instance of this class use @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingViewItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingViewItemBuilder@endlink  or @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder@endlink .  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class DrawingItemBuilder(NXOpen.Builder): 
    """ This builder allows you to define the general arrangement drawing item information. 
            It represents <ja_class>NXOpen.Features.ShipDesign.GeneralArrangement.DrawingItemBuilder</ja_class>.
            This builder won't create General Arrangement View and just returns <ja_NULL>. 
            """


    ## Getter for property: (bool) CreateItem
    ##  Returns the create item   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def CreateItem(self) -> bool:
        """
        Getter for property: (bool) CreateItem
         Returns the create item   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateItem

    ##  Returns the create item   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @CreateItem.setter
    def CreateItem(self, createItem: bool):
        """
        Setter for property: (bool) CreateItem
         Returns the create item   
            
         
        """
        pass
    
##  This builder allows you to define the general arrangement drawing table item information. 
##             It represents @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder@endlink .
##             This builder won't create Table and just returns NULL. 
##              <br> To create a new instance of this class, use @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder  NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class DrawingTableItemBuilder(DrawingItemBuilder): 
    """ This builder allows you to define the general arrangement drawing table item information. 
            It represents <ja_class>NXOpen.Features.ShipDesign.GeneralArrangement.DrawingTableItemBuilder</ja_class>.
            This builder won't create Table and just returns <ja_NULL>. 
            """
    pass


##  This builder allows you to define the general arrangement drawing view item information. 
##             It represents @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingViewItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingViewItemBuilder@endlink .
##             This builder won't create General Arrangement View and just returns NULL. 
##              <br> To create a new instance of this class, use @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingViewItemBuilder  NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingViewItemBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## HorizontalFrameBarPosition </term> <description> 
##  
## ViewTop </description> </item> 
## 
## <item><term> 
##  
## ShowFireAndSafetyPlanSymbol </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowHorizontalFrameBar </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowOpeningFillingLine </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowOverallDimension </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowPMILabel </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowVerticalFrameBar </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VerticalFrameBarPosition </term> <description> 
##  
## ViewLeft </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.2  <br> 

class DrawingViewItemBuilder(DrawingItemBuilder): 
    """ This builder allows you to define the general arrangement drawing view item information. 
            It represents <ja_class>NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder</ja_class>.
            This builder won't create General Arrangement View and just returns <ja_NULL>. 
            """


    ##  Settings to indicate the position of Frame Bar in X direction
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ViewTop</term><description> 
    ## </description> </item><item><term> 
    ## ViewCenterY</term><description> 
    ## </description> </item><item><term> 
    ## ViewBottom</term><description> 
    ## </description> </item><item><term> 
    ## ViewLeft</term><description> 
    ## </description> </item><item><term> 
    ## ViewCenterX</term><description> 
    ## </description> </item><item><term> 
    ## ViewRight</term><description> 
    ## </description> </item></list>
    class FrameBarPositionType(Enum):
        """
        Members Include: <ViewTop> <ViewCenterY> <ViewBottom> <ViewLeft> <ViewCenterX> <ViewRight>
        """
        ViewTop: int
        ViewCenterY: int
        ViewBottom: int
        ViewLeft: int
        ViewCenterX: int
        ViewRight: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawingViewItemBuilder.FrameBarPositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) HorizontalFrameBarPosition
    ##  Returns the horizontal frame bar position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return DrawingViewItemBuilder.FrameBarPositionType
    @property
    def HorizontalFrameBarPosition(self) -> DrawingViewItemBuilder.FrameBarPositionType:
        """
        Getter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) HorizontalFrameBarPosition
         Returns the horizontal frame bar position   
            
         
        """
        pass
    
    ## Setter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) HorizontalFrameBarPosition

    ##  Returns the horizontal frame bar position   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @HorizontalFrameBarPosition.setter
    def HorizontalFrameBarPosition(self, horizontalFrameBarPosition: DrawingViewItemBuilder.FrameBarPositionType):
        """
        Setter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) HorizontalFrameBarPosition
         Returns the horizontal frame bar position   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFireAndSafetyPlanSymbol
    ##  Returns the flag to indicate whether to show the fire and safety plan symbol or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def ShowFireAndSafetyPlanSymbol(self) -> bool:
        """
        Getter for property: (bool) ShowFireAndSafetyPlanSymbol
         Returns the flag to indicate whether to show the fire and safety plan symbol or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowFireAndSafetyPlanSymbol

    ##  Returns the flag to indicate whether to show the fire and safety plan symbol or not.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ShowFireAndSafetyPlanSymbol.setter
    def ShowFireAndSafetyPlanSymbol(self, showFireAndSafetyPlanSymbol: bool):
        """
        Setter for property: (bool) ShowFireAndSafetyPlanSymbol
         Returns the flag to indicate whether to show the fire and safety plan symbol or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowHorizontalFrameBar
    ##  Returns the flag to indicate whether to show horizontal frame bar or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def ShowHorizontalFrameBar(self) -> bool:
        """
        Getter for property: (bool) ShowHorizontalFrameBar
         Returns the flag to indicate whether to show horizontal frame bar or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowHorizontalFrameBar

    ##  Returns the flag to indicate whether to show horizontal frame bar or not.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ShowHorizontalFrameBar.setter
    def ShowHorizontalFrameBar(self, showHorizontalFrameBar: bool):
        """
        Setter for property: (bool) ShowHorizontalFrameBar
         Returns the flag to indicate whether to show horizontal frame bar or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowOpeningFillingLine
    ##  Returns the flag to indicate whether to show the opening filling line or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def ShowOpeningFillingLine(self) -> bool:
        """
        Getter for property: (bool) ShowOpeningFillingLine
         Returns the flag to indicate whether to show the opening filling line or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowOpeningFillingLine

    ##  Returns the flag to indicate whether to show the opening filling line or not.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ShowOpeningFillingLine.setter
    def ShowOpeningFillingLine(self, showOpeningFillingLine: bool):
        """
        Setter for property: (bool) ShowOpeningFillingLine
         Returns the flag to indicate whether to show the opening filling line or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowOverallDimension
    ##  Returns the flag to indicate whether to show the overall dimension or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def ShowOverallDimension(self) -> bool:
        """
        Getter for property: (bool) ShowOverallDimension
         Returns the flag to indicate whether to show the overall dimension or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowOverallDimension

    ##  Returns the flag to indicate whether to show the overall dimension or not.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ShowOverallDimension.setter
    def ShowOverallDimension(self, showOverallDimension: bool):
        """
        Setter for property: (bool) ShowOverallDimension
         Returns the flag to indicate whether to show the overall dimension or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowPMILabel
    ##  Returns the flag to indicate whether to show the PMI labels or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def ShowPMILabel(self) -> bool:
        """
        Getter for property: (bool) ShowPMILabel
         Returns the flag to indicate whether to show the PMI labels or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowPMILabel

    ##  Returns the flag to indicate whether to show the PMI labels or not.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ShowPMILabel.setter
    def ShowPMILabel(self, showPMILabel: bool):
        """
        Setter for property: (bool) ShowPMILabel
         Returns the flag to indicate whether to show the PMI labels or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowVerticalFrameBar
    ##  Returns the flag to indicate whether to show vertical frame bar or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def ShowVerticalFrameBar(self) -> bool:
        """
        Getter for property: (bool) ShowVerticalFrameBar
         Returns the flag to indicate whether to show vertical frame bar or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowVerticalFrameBar

    ##  Returns the flag to indicate whether to show vertical frame bar or not.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ShowVerticalFrameBar.setter
    def ShowVerticalFrameBar(self, showVerticalFrameBar: bool):
        """
        Setter for property: (bool) ShowVerticalFrameBar
         Returns the flag to indicate whether to show vertical frame bar or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) VerticalFrameBarPosition
    ##  Returns the vertical frame bar position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return DrawingViewItemBuilder.FrameBarPositionType
    @property
    def VerticalFrameBarPosition(self) -> DrawingViewItemBuilder.FrameBarPositionType:
        """
        Getter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) VerticalFrameBarPosition
         Returns the vertical frame bar position   
            
         
        """
        pass
    
    ## Setter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) VerticalFrameBarPosition

    ##  Returns the vertical frame bar position   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @VerticalFrameBarPosition.setter
    def VerticalFrameBarPosition(self, verticalFrameBarPosition: DrawingViewItemBuilder.FrameBarPositionType):
        """
        Setter for property: (@link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink) VerticalFrameBarPosition
         Returns the vertical frame bar position   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents a @link NXOpen::Features::ShipDesign::GeneralArrangement::EvacuationPlanBuilder NXOpen::Features::ShipDesign::GeneralArrangement::EvacuationPlanBuilder@endlink  builder . This builder returns NULL.  <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateEvacuationPlanBuilder  NXOpen::Features::ShipCollection::CreateEvacuationPlanBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class EvacuationPlanBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.ShipDesign.GeneralArrangement.EvacuationPlanBuilder</ja_class> builder . This builder returns <ja_NULL>. """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Angle
    ##  Returns the angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Angle
         Returns the angle   
            
         
        """
        pass
    
    ## Getter for property: (int) Color
    ##  Returns the color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return int
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the color   
            
         
        """
        pass
    
    ## Setter for property: (int) Color

    ##  Returns the color   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns the color   
            
         
        """
        pass
    
    ## Getter for property: (bool) HorizontalFlip
    ##  Returns the horizontal flip   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def HorizontalFlip(self) -> bool:
        """
        Getter for property: (bool) HorizontalFlip
         Returns the horizontal flip   
            
         
        """
        pass
    
    ## Setter for property: (bool) HorizontalFlip

    ##  Returns the horizontal flip   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @HorizontalFlip.setter
    def HorizontalFlip(self, horizontalFlip: bool):
        """
        Setter for property: (bool) HorizontalFlip
         Returns the horizontal flip   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
    ##  Returns the annotation origin builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Annotations.OriginBuilder
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
         Returns the annotation origin builder   
            
         
        """
        pass
    
    ## Getter for property: (int) Pattern
    ##  Returns the pattern   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return int
    @property
    def Pattern(self) -> int:
        """
        Getter for property: (int) Pattern
         Returns the pattern   
            
         
        """
        pass
    
    ## Setter for property: (int) Pattern

    ##  Returns the pattern   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Pattern.setter
    def Pattern(self, pattern: int):
        """
        Setter for property: (int) Pattern
         Returns the pattern   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
    ##  Returns the scale   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
         Returns the scale   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
    ##  Returns the annotation style builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Annotations.StyleBuilder
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
         Returns the annotation style builder.  
             
         
        """
        pass
    
    ## Getter for property: (bool) VerticalFlip
    ##  Returns the vertical flip   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def VerticalFlip(self) -> bool:
        """
        Getter for property: (bool) VerticalFlip
         Returns the vertical flip   
            
         
        """
        pass
    
    ## Setter for property: (bool) VerticalFlip

    ##  Returns the vertical flip   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @VerticalFlip.setter
    def VerticalFlip(self, verticalFlip: bool):
        """
        Setter for property: (bool) VerticalFlip
         Returns the vertical flip   
            
         
        """
        pass
    
    ##  Adds expression data
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ## <param name="strTitle"> (str) </param>
    ## <param name="strFormular"> (str) </param>
    def AddExpressionData(self, strTitle: str, strFormular: str) -> None:
        """
         Adds expression data
        """
        pass
    
    ##  Clears the expressions data
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    def ClearExpressionsData(self) -> None:
        """
         Clears the expressions data
        """
        pass
    
import NXOpen
##  Represents a builder to be used to add face characteristics attributes and color to specified faces.  <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateFaceCharacteristicsBuilder  NXOpen::Features::ShipCollection::CreateFaceCharacteristicsBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FaceCharacteristicsBuilder(NXOpen.Builder): 
    """ Represents a builder to be used to add face characteristics attributes and color to specified faces. """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CharacteristicColor
    ##  Returns the characteristic color to assign to the selected face.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def CharacteristicColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CharacteristicColor
         Returns the characteristic color to assign to the selected face.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CharacteristicColor

    ##  Returns the characteristic color to assign to the selected face.  
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CharacteristicColor.setter
    def CharacteristicColor(self, characteristicColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CharacteristicColor
         Returns the characteristic color to assign to the selected face.  
            
         
        """
        pass
    
    ## Getter for property: (int) CharacteristicValue
    ##  Returns the characteristic value to assign to the selected face.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def CharacteristicValue(self) -> int:
        """
        Getter for property: (int) CharacteristicValue
         Returns the characteristic value to assign to the selected face.  
            
         
        """
        pass
    
    ## Setter for property: (int) CharacteristicValue

    ##  Returns the characteristic value to assign to the selected face.  
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CharacteristicValue.setter
    def CharacteristicValue(self, characteristicValue: int):
        """
        Setter for property: (int) CharacteristicValue
         Returns the characteristic value to assign to the selected face.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
    ##  Returns the face to assign the specific characteristics.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectFace
         Returns the face to assign the specific characteristics.  
            
         
        """
        pass
    
## @package NXOpen.Features.ShipDesign.GeneralArrangement
## Classes, Enums and Structs under NXOpen.Features.ShipDesign.GeneralArrangement namespace

##  @link DrawingViewItemBuilderFrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilderFrameBarPositionType @endlink is an alias for @link DrawingViewItemBuilder.FrameBarPositionType NXOpen.Features.ShipDesign.GeneralArrangement.DrawingViewItemBuilder.FrameBarPositionType@endlink
DrawingViewItemBuilderFrameBarPositionType = DrawingViewItemBuilder.FrameBarPositionType


