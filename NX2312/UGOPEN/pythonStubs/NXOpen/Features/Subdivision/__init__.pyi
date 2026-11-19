from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::CageFromFacetBodyBuilder NXOpen::Features::Subdivision::CageFromFacetBodyBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCageFromFacetBodyBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCageFromFacetBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AverageSize.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CageFromFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.CageFromFacetBodyBuilder</ja_class> builder.  """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AverageSize
    ##   the average size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AverageSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AverageSize
          the average size   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetRegion
    ##   the facets to be subdivisioned   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetRegion(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetRegion
          the facets to be subdivisioned   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowDeviationPlot
    ##   the deviation toggle  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ShowDeviationPlot(self) -> bool:
        """
        Getter for property: (bool) ShowDeviationPlot
          the deviation toggle  
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowDeviationPlot

    ##   the deviation toggle  
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ShowDeviationPlot.setter
    def ShowDeviationPlot(self, isShowDeviationPlot: bool):
        """
        Setter for property: (bool) ShowDeviationPlot
          the deviation toggle  
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Subdivision cage manipulation tool.
##         
## 
##   <br>  Created in NX9.0.0  <br> 

class CageManipulatorData(SelectCageObjectData): 
    """ Subdivision cage manipulation tool.
        """


    ##  Contains object movement information. 
    class ObjectMoveData:
        """
         Contains object movement information. 
        """
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) DraggedObject
        ## The dragged object.
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def DraggedObject(self) -> NXOpen.NXObject:
            """
            Getter for property DraggedObject
            The dragged object.

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) DraggedObject
        @DraggedObject.setter
        def DraggedObject(self, value: NXOpen.NXObject):
            """
            Getter for property DraggedObject
            The dragged object.
            Setter for property DraggedObject
            The dragged object.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) BeginDragCursorPosition
        ## The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def BeginDragCursorPosition(self) -> NXOpen.Point3d:
            """
            Getter for property BeginDragCursorPosition
            The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) BeginDragCursorPosition
        @BeginDragCursorPosition.setter
        def BeginDragCursorPosition(self, value: NXOpen.Point3d):
            """
            Getter for property BeginDragCursorPosition
            The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.
            Setter for property BeginDragCursorPosition
            The point from which object dragging is initiated, the point                                                              under the cursor when seen in view direction.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) BeginDragObjectPosition
        ## The point on object near cursor from which object dragging is initiated
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def BeginDragObjectPosition(self) -> NXOpen.Point3d:
            """
            Getter for property BeginDragObjectPosition
            The point on object near cursor from which object dragging is initiated

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) BeginDragObjectPosition
        @BeginDragObjectPosition.setter
        def BeginDragObjectPosition(self, value: NXOpen.Point3d):
            """
            Getter for property BeginDragObjectPosition
            The point on object near cursor from which object dragging is initiated
            Setter for property BeginDragObjectPosition
            The point on object near cursor from which object dragging is initiated

            """
            pass
        
        ## Getter for property :(@link NXOpen.View NXOpen.View@endlink) View
        ## The view in which object is dragged.
        ## @return @link NXOpen.View NXOpen.View@endlink
        @property
        def View(self) -> NXOpen.View:
            """
            Getter for property View
            The view in which object is dragged.

            """
            pass
        
        ## Setter for property :(@link NXOpen.View NXOpen.View@endlink) View
        @View.setter
        def View(self, value: NXOpen.View):
            """
            Getter for property View
            The view in which object is dragged.
            Setter for property View
            The view in which object is dragged.

            """
            pass
        
        ## Getter for property :(float) MicropositioningScale
        ## The micropositioning scale.
        ## @return float
        @property
        def MicropositioningScale(self) -> float:
            """
            Getter for property MicropositioningScale
            The micropositioning scale.

            """
            pass
        
        ## Setter for property :(float) MicropositioningScale
        @MicropositioningScale.setter
        def MicropositioningScale(self, value: float):
            """
            Getter for property MicropositioningScale
            The micropositioning scale.
            Setter for property MicropositioningScale
            The micropositioning scale.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
        ## The view direction.
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def ViewDirection(self) -> NXOpen.Vector3d:
            """
            Getter for property ViewDirection
            The view direction.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
        @ViewDirection.setter
        def ViewDirection(self, value: NXOpen.Vector3d):
            """
            Getter for property ViewDirection
            The view direction.
            Setter for property ViewDirection
            The view direction.

            """
            pass
        
    
    
    ##  Contains object selection information. 
    class ObjectSelectionData:
        """
         Contains object selection information. 
        """
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SelectedObject
        ## The selected object.
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def SelectedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SelectedObject
            The selected object.

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SelectedObject
        @SelectedObject.setter
        def SelectedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SelectedObject
            The selected object.
            Setter for property SelectedObject
            The selected object.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SelectionPosition
        ## The point at which object is selected, the point                                                         under the cursor when seen in view direction.
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def SelectionPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SelectionPosition
        @SelectionPosition.setter
        def SelectionPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.
            Setter for property SelectionPosition
            The point at which object is selected, the point                                                         under the cursor when seen in view direction.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
        ## The view direction.
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def ViewDirection(self) -> NXOpen.Vector3d:
            """
            Getter for property ViewDirection
            The view direction.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ViewDirection
        @ViewDirection.setter
        def ViewDirection(self, value: NXOpen.Vector3d):
            """
            Getter for property ViewDirection
            The view direction.
            Setter for property ViewDirection
            The view direction.

            """
            pass
        
        ## Getter for property :(bool) IsSnappedPosition
        ## Is SelectionPosition a snapped location.
        ## @return bool
        @property
        def IsSnappedPosition(self) -> bool:
            """
            Getter for property IsSnappedPosition
            Is SelectionPosition a snapped location.

            """
            pass
        
        ## Setter for property :(bool) IsSnappedPosition
        @IsSnappedPosition.setter
        def IsSnappedPosition(self, value: bool):
            """
            Getter for property IsSnappedPosition
            Is SelectionPosition a snapped location.
            Setter for property IsSnappedPosition
            Is SelectionPosition a snapped location.

            """
            pass
        
    
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ##  Releases the data prepared at the beginning of the move. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def EndMove(builder: CageManipulatorData) -> None:
        """
         Releases the data prepared at the beginning of the move. 
        """
        pass
    
    ##  Moves the objects by dragging. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Features::Subdivision::CageManipulatorData::Move NXOpen::Features::Subdivision::CageManipulatorData::Move@endlink  with optional constraint point instead.  <br> 

    ## License requirements: None.
    ##  
    @overload
    def Move(self, builder: CageManipulatorData, moveToPoint: NXOpen.Point3d, isSnapGesture: bool) -> None:
        """
         Moves the objects by dragging. 
        """
        pass
    
    ##  Moves the objects by dragging. A constraint point can be assigned when moving a vertex. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def Move(self, builder: CageManipulatorData, moveToPoint: NXOpen.Point3d, point: NXOpen.Point, isSnapGesture: bool) -> None:
        """
         Moves the objects by dragging. A constraint point can be assigned when moving a vertex. 
        """
        pass
    
    ##  Prepares data to move the objects. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  
    def PrepareToMove(builder: CageManipulatorData, moveData: CageManipulatorData.ObjectMoveData) -> None:
        """
         Prepares data to move the objects. 
        """
        pass
    
    ##  Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the centroid of the selected entities. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ResetTransformerToCentroidOfSelection(builder: CageManipulatorData) -> None:
        """
         Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the centroid of the selected entities. 
        """
        pass
    
    ##  Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetTransformerToObject(builder: CageManipulatorData, selectionData: CageManipulatorData.ObjectSelectionData) -> None:
        """
         Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
        """
        pass
    
    ##  Moves the objects by step value. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  
    def StepMove(builder: CageManipulatorData, step: float) -> None:
        """
         Moves the objects by step value. 
        """
        pass
    
import NXOpen.Features
##  Cage polyline builder class.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCagePolylineBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCagePolylineBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DrawingPlaneOption </term> <description> 
##  
## View </description> </item> 
## 
## <item><term> 
##  
## MovementMethod </term> <description> 
##  
## View </description> </item> 
## 
## <item><term> 
##  
## WCSOption </term> <description> 
##  
## X </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class CagePolylineBuilder(NXOpen.Features.PolylineBuilder): 
    """ Cage polyline builder class. """
    pass


import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class CageSectionDataList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: CageSectionDataList, objects: List[CageSectionData]) -> None:
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
    def Append(self, object_list: CageSectionDataList, objectValue: CageSectionData) -> None:
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
    def Clear(object_list: CageSectionDataList) -> None:
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
    def ClearIndex(object_list: CageSectionDataList, delete_idx: int) -> None:
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
    def Clear(object_list: CageSectionDataList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: CageSectionDataList, index: int) -> None:
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
    def Erase(self, object_list: CageSectionDataList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: CageSectionDataList, obj: CageSectionData) -> None:
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
    def Erase(self, object_list: CageSectionDataList, obj: CageSectionData, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: CageSectionDataList, obj: CageSectionData) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link CageSectionData NXOpen.Features.Subdivision.CageSectionData@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: CageSectionDataList, index: int) -> CageSectionData:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link CageSectionData NXOpen.Features.Subdivision.CageSectionData@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link CageSectionData List[NXOpen.Features.Subdivision.CageSectionData]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: CageSectionDataList) -> List[CageSectionData]:
        """
         Gets the contents of the entire list 
         @return objects (@link CageSectionData List[NXOpen.Features.Subdivision.CageSectionData]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: CageSectionDataList, location: int, objectValue: CageSectionData) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: CageSectionDataList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: CageSectionDataList, index: int) -> None:
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
    def SetContents(object_list: CageSectionDataList, objects: List[CageSectionData]) -> None:
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
    def Swap(self, object_list: CageSectionDataList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: CageSectionDataList, object1: CageSectionData, object2: CageSectionData) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents subdivision cage section selection. 
## 
##   <br>  Created in NX10.0.0  <br> 

class CageSectionData(NXOpen.TaggedObject): 
    """ Represents subdivision cage section selection. """


    ## Getter for property: (bool) CanReverseDirection
    ##   the flag indicating if section direction is reversed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanReverseDirection(self) -> bool:
        """
        Getter for property: (bool) CanReverseDirection
          the flag indicating if section direction is reversed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReverseDirection

    ##   the flag indicating if section direction is reversed.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanReverseDirection.setter
    def CanReverseDirection(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseDirection
          the flag indicating if section direction is reversed.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectionObject
    ##   the selection object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def SelectionObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectionObject
          the selection object.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Features::Subdivision::CopyCageBuilder NXOpen::Features::Subdivision::CopyCageBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCopyCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCopyCageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanRelocateToolToSelection </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CanReorientToolToSelection </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## NumberOfCopies </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class CopyCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.CopyCageBuilder</ja_class> builder. """


    ## Getter for property: (bool) CanMoveToolOnly
    ##   the flag indicating if tool can be moved alone without moving selected topology   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
          the flag indicating if tool can be moved alone without moving selected topology   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanMoveToolOnly

    ##   the flag indicating if tool can be moved alone without moving selected topology   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMoveToolOnly: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
          the flag indicating if tool can be moved alone without moving selected topology   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanRelocateToolToSelection
    ##   the flag indicating if tool should relocate to selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
          the flag indicating if tool should relocate to selection   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanRelocateToolToSelection

    ##   the flag indicating if tool should relocate to selection   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocateToolToSelection: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
          the flag indicating if tool should relocate to selection   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanReorientToolToSelection
    ##   the flag indicating if tool should reorient to selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
          the flag indicating if tool should reorient to selection   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanReorientToolToSelection

    ##   the flag indicating if tool should reorient to selection   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorientToolToSelection: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
          the flag indicating if tool should reorient to selection   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfCopies
    ##   the number of copies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
          the number of copies   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfCopies

    ##   the number of copies   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
          the number of copies   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
    ##   the objects to be copied   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
          the objects to be copied   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ##  Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the centroid of the selected entities. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    @staticmethod
    def ResetTransformerToCentroidOfSelection(builder: CopyCageBuilder) -> None:
        """
         Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the centroid of the selected entities. 
        """
        pass
    
    ##  Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    ##  
    def SetTransformerToObject(builder: CopyCageBuilder, selectionData: CageManipulatorData.ObjectSelectionData) -> None:
        """
         Repositions the @link NXOpen::GeometricUtilities::TransformerData NXOpen::GeometricUtilities::TransformerData@endlink  to the specified entity. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::CopyCageData NXOpen::Features::Subdivision::CopyCageData@endlink . 
##             Copies Control Cage, Cage Face and Cage Polyline type objects on the clipboard.
##          <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCopyCageData  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCopyCageData @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class CopyCageData(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.CopyCageData</ja_class>. 
            Copies Control Cage, Cage Face and Cage Polyline type objects on the clipboard.
        """


    ##  Returns the objects to be copied. 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjects(processor: CopyCageData) -> List[NXOpen.NXObject]:
        """
         Returns the objects to be copied. 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
        """
        pass
    
    ##  Sets the objects to be copied. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    ##  
    def SetObjects(processor: CopyCageData, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets the objects to be copied. 
        """
        pass
    
import NXOpen
##  Represents a @link Features::Subdivision::DefineWorkRegionBuilder Features::Subdivision::DefineWorkRegionBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateDefineWorkRegionBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateDefineWorkRegionBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DefineWorkRegionBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Features.Subdivision.DefineWorkRegionBuilder</ja_class> builder. """


    ##  Method of defining frozen region. 
    ##  Do not display the frozen region 
    class FrozenRegionDefinitionMethods(Enum):
        """
        Members Include: <Hidden> <Colored>
        """
        Hidden: int
        Colored: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefineWorkRegionBuilder.FrozenRegionDefinitionMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Method of defining work region. 
    ##  Treat all the region as work region 
    class WorkRegionDefinitionMethods(Enum):
        """
        Members Include: <All> <Selected>
        """
        All: int
        Selected: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefineWorkRegionBuilder.WorkRegionDefinitionMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FrozenColor
    ##   the frozen region color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FrozenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FrozenColor
          the frozen region color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FrozenColor

    ##   the frozen region color   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @FrozenColor.setter
    def FrozenColor(self, frozenColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FrozenColor
          the frozen region color   
            
         
        """
        pass
    
    ## Getter for property: (@link DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.FrozenRegionDefinitionMethods@endlink) FrozenRegionDefinitionMethod
    ##   the frozen region method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return DefineWorkRegionBuilder.FrozenRegionDefinitionMethods
    @property
    def FrozenRegionDefinitionMethod(self) -> DefineWorkRegionBuilder.FrozenRegionDefinitionMethods:
        """
        Getter for property: (@link DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.FrozenRegionDefinitionMethods@endlink) FrozenRegionDefinitionMethod
          the frozen region method   
            
         
        """
        pass
    
    ## Setter for property: (@link DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.FrozenRegionDefinitionMethods@endlink) FrozenRegionDefinitionMethod

    ##   the frozen region method   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @FrozenRegionDefinitionMethod.setter
    def FrozenRegionDefinitionMethod(self, frozenRegionDefinitionMethod: DefineWorkRegionBuilder.FrozenRegionDefinitionMethods):
        """
        Setter for property: (@link DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.FrozenRegionDefinitionMethods@endlink) FrozenRegionDefinitionMethod
          the frozen region method   
            
         
        """
        pass
    
    ## Getter for property: (@link DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.WorkRegionDefinitionMethods@endlink) WorkRegionDefinitionMethod
    ##   the work region definition method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return DefineWorkRegionBuilder.WorkRegionDefinitionMethods
    @property
    def WorkRegionDefinitionMethod(self) -> DefineWorkRegionBuilder.WorkRegionDefinitionMethods:
        """
        Getter for property: (@link DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.WorkRegionDefinitionMethods@endlink) WorkRegionDefinitionMethod
          the work region definition method   
            
         
        """
        pass
    
    ## Setter for property: (@link DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.WorkRegionDefinitionMethods@endlink) WorkRegionDefinitionMethod

    ##   the work region definition method   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @WorkRegionDefinitionMethod.setter
    def WorkRegionDefinitionMethod(self, workRegionDefinitionMethod: DefineWorkRegionBuilder.WorkRegionDefinitionMethods):
        """
        Setter for property: (@link DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.WorkRegionDefinitionMethods@endlink) WorkRegionDefinitionMethod
          the work region definition method   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) WorkRegionObjects
    ##   the work region objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def WorkRegionObjects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) WorkRegionObjects
          the work region objects   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::DeleteConstraintBuilder NXOpen::Features::Subdivision::DeleteConstraintBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateDeleteConstraintBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateDeleteConstraintBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DeleteConstraintBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.DeleteConstraintBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
    ##   the constrained objects whose constraint to be deleted.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
          the constrained objects whose constraint to be deleted.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::DrawCageData NXOpen::Features::Subdivision::DrawCageData@endlink  data.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateDrawCageData  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateDrawCageData @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class DrawCageData(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.DrawCageData</ja_class> data. """


    ##  The face shape type 
    ##  Quadrilateral shape 
    class FaceShapeType(Enum):
        """
        Members Include: <Quad> <Polygon>
        """
        Quad: int
        Polygon: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawCageData.FaceShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contains object selection information to be used to create a patch. 
    class SelectionData:
        """
         Contains object selection information to be used to create a patch. 
        """
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SnappedObject
        ## The selected or snapped object, can be an existing vertex or a point
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def SnappedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SnappedObject
            The selected or snapped object, can be an existing vertex or a point

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SnappedObject
        @SnappedObject.setter
        def SnappedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SnappedObject
            The selected or snapped object, can be an existing vertex or a point
            Setter for property SnappedObject
            The selected or snapped object, can be an existing vertex or a point

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SnappedPosition
        ## The point at which object is selected or snapped.
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def SnappedPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SnappedPosition
            The point at which object is selected or snapped.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SnappedPosition
        @SnappedPosition.setter
        def SnappedPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SnappedPosition
            The point at which object is selected or snapped.
            Setter for property SnappedPosition
            The point at which object is selected or snapped.

            """
            pass
        
        ## Getter for property :(bool) IsInferringPaused
        ## Flag indicating if inferring is paused.
        ## @return bool
        @property
        def IsInferringPaused(self) -> bool:
            """
            Getter for property IsInferringPaused
            Flag indicating if inferring is paused.

            """
            pass
        
        ## Setter for property :(bool) IsInferringPaused
        @IsInferringPaused.setter
        def IsInferringPaused(self, value: bool):
            """
            Getter for property IsInferringPaused
            Flag indicating if inferring is paused.
            Setter for property IsInferringPaused
            Flag indicating if inferring is paused.

            """
            pass
        
    
    
    ## Getter for property: (@link CageManipulatorData NXOpen.Features.Subdivision.CageManipulatorData@endlink) CageManipulator
    ##   the cage manipulation data.  
    ##    Cage manipulator helps create new and edit existing vertices.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return CageManipulatorData
    @property
    def CageManipulator(self) -> CageManipulatorData:
        """
        Getter for property: (@link CageManipulatorData NXOpen.Features.Subdivision.CageManipulatorData@endlink) CageManipulator
          the cage manipulation data.  
           Cage manipulator helps create new and edit existing vertices.   
         
        """
        pass
    
    ## Getter for property: (@link DrawCageData.FaceShapeType NXOpen.Features.Subdivision.DrawCageData.FaceShapeType@endlink) FaceShape
    ##   the face shape.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return DrawCageData.FaceShapeType
    @property
    def FaceShape(self) -> DrawCageData.FaceShapeType:
        """
        Getter for property: (@link DrawCageData.FaceShapeType NXOpen.Features.Subdivision.DrawCageData.FaceShapeType@endlink) FaceShape
          the face shape.  
             
         
        """
        pass
    
    ## Setter for property: (@link DrawCageData.FaceShapeType NXOpen.Features.Subdivision.DrawCageData.FaceShapeType@endlink) FaceShape

    ##   the face shape.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @FaceShape.setter
    def FaceShape(self, shape: DrawCageData.FaceShapeType):
        """
        Setter for property: (@link DrawCageData.FaceShapeType NXOpen.Features.Subdivision.DrawCageData.FaceShapeType@endlink) FaceShape
          the face shape.  
             
         
        """
        pass
    
    ##  Adds a vertex and creates a patch if possible. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    ##  
    def AddVertex(builder: DrawCageData, selectionData: DrawCageData.SelectionData) -> None:
        """
         Adds a vertex and creates a patch if possible. 
        """
        pass
    
    ##  Closes the polygon and creates a patch. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    @staticmethod
    def ClosePolygon(builder: DrawCageData) -> None:
        """
         Closes the polygon and creates a patch. 
        """
        pass
    
    ##  Discards the current polygon and restarts new. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    @staticmethod
    def ResetStartPoint(builder: DrawCageData) -> None:
        """
         Discards the current polygon and restarts new. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a @link NXOpen::Features::Subdivision::ExportSubdivisionGeometryBuilder NXOpen::Features::Subdivision::ExportSubdivisionGeometryBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateExportSubdivisionGeometryBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateExportSubdivisionGeometryBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjCreator NXOpen::WavefrontObjCreator@endlink  instead  <br> 

class ExportSubdivisionGeometryBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder</ja_class> builder. """


    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) FeatureSet
    ##   the Feature to export   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjCreator NXOpen::WavefrontObjCreator@endlink  instead  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def FeatureSet(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) FeatureSet
          the Feature to export   
            
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the file name.  
    ##    The export file will only store the topology and geometry positions of the Subdivision Cage, and 
    ##                 not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjCreator NXOpen::WavefrontObjCreator@endlink  instead  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the file name.  
           The export file will only store the topology and geometry positions of the Subdivision Cage, and 
                        not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
                      
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the file name.  
    ##    The export file will only store the topology and geometry positions of the Subdivision Cage, and 
    ##                 not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
    ##               
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjCreator NXOpen::WavefrontObjCreator@endlink  instead  <br> 

    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
          the file name.  
           The export file will only store the topology and geometry positions of the Subdivision Cage, and 
                        not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
                      
         
        """
        pass
    
import NXOpen
##  Extract cage polyline builder class.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateExtractCagePolylineBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateExtractCagePolylineBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## NumberOfSegments </term> <description> 
##  
## 4 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class ExtractCagePolylineBuilder(NXOpen.Builder): 
    """ Extract cage polyline builder class. """


    ##  Input curves options. 
    ##  Keep input curves as they are 
    class InputCurveOption(Enum):
        """
        Members Include: <Keep> <Hide> <Delete>
        """
        Keep: int
        Hide: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExtractCagePolylineBuilder.InputCurveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurveToExtract
    ##   the curve to extract   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def CurveToExtract(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurveToExtract
          the curve to extract   
            
         
        """
        pass
    
    ## Getter for property: (@link ExtractCagePolylineBuilder.InputCurveOption NXOpen.Features.Subdivision.ExtractCagePolylineBuilder.InputCurveOption@endlink) InputCurveOptions
    ##   the input curve options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ExtractCagePolylineBuilder.InputCurveOption
    @property
    def InputCurveOptions(self) -> ExtractCagePolylineBuilder.InputCurveOption:
        """
        Getter for property: (@link ExtractCagePolylineBuilder.InputCurveOption NXOpen.Features.Subdivision.ExtractCagePolylineBuilder.InputCurveOption@endlink) InputCurveOptions
          the input curve options   
            
         
        """
        pass
    
    ## Setter for property: (@link ExtractCagePolylineBuilder.InputCurveOption NXOpen.Features.Subdivision.ExtractCagePolylineBuilder.InputCurveOption@endlink) InputCurveOptions

    ##   the input curve options   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @InputCurveOptions.setter
    def InputCurveOptions(self, inputCurveOptions: ExtractCagePolylineBuilder.InputCurveOption):
        """
        Setter for property: (@link ExtractCagePolylineBuilder.InputCurveOption NXOpen.Features.Subdivision.ExtractCagePolylineBuilder.InputCurveOption@endlink) InputCurveOptions
          the input curve options   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfSegments
    ##   the number of segments   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
          the number of segments   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfSegments

    ##   the number of segments   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
          the number of segments   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::ImportSubdivisionGeometryBuilder NXOpen::Features::Subdivision::ImportSubdivisionGeometryBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateImportSubdivisionGeometryBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateImportSubdivisionGeometryBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjImporter NXOpen::WavefrontObjImporter@endlink  instead  <br> 

class ImportSubdivisionGeometryBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder</ja_class> builder. """


    ## Getter for property: (bool) CanCreateSingleFeature
    ##   the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
    ##    
    ##                 When false, separate feature will be created for each disjoint region.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjImporter NXOpen::WavefrontObjImporter@endlink  instead  <br> 

    ## @return bool
    @property
    def CanCreateSingleFeature(self) -> bool:
        """
        Getter for property: (bool) CanCreateSingleFeature
          the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
           
                        When false, separate feature will be created for each disjoint region.   
         
        """
        pass
    
    ## Setter for property: (bool) CanCreateSingleFeature

    ##   the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
    ##    
    ##                 When false, separate feature will be created for each disjoint region.   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjImporter NXOpen::WavefrontObjImporter@endlink  instead  <br> 

    @CanCreateSingleFeature.setter
    def CanCreateSingleFeature(self, canCreateSingleFeature: bool):
        """
        Setter for property: (bool) CanCreateSingleFeature
          the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
           
                        When false, separate feature will be created for each disjoint region.   
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the file name.  
    ##    Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
    ##                 Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
    ##                 subdivision mesh is not recommended to be used. The solid model created from such mesh will have
    ##                 excessive amount of topology and the import operation will be inefficient.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjImporter NXOpen::WavefrontObjImporter@endlink  instead  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the file name.  
           Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
                        Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
                        subdivision mesh is not recommended to be used. The solid model created from such mesh will have
                        excessive amount of topology and the import operation will be inefficient.
                      
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the file name.  
    ##    Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
    ##                 Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
    ##                 subdivision mesh is not recommended to be used. The solid model created from such mesh will have
    ##                 excessive amount of topology and the import operation will be inefficient.
    ##               
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjImporter NXOpen::WavefrontObjImporter@endlink  instead  <br> 

    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
          the file name.  
           Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
                        Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
                        subdivision mesh is not recommended to be used. The solid model created from such mesh will have
                        excessive amount of topology and the import operation will be inefficient.
                      
         
        """
        pass
    
import NXOpen
##  Represents a @link Features::Subdivision::MergeSubdivisionBodiesBuilder Features::Subdivision::MergeSubdivisionBodiesBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateMergeSubdivisionBodiesBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateMergeSubdivisionBodiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## InputBodyOption </term> <description> 
##  
## Delete </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 

class MergeSubdivisionBodiesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Features.Subdivision.MergeSubdivisionBodiesBuilder</ja_class> builder. """


    ##  Options indicating actions to be taken on input @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features 
    ##  Keep the features as they are 
    class InputBodyOptions(Enum):
        """
        Members Include: <Keep> <Hide> <Delete>
        """
        Keep: int
        Hide: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MergeSubdivisionBodiesBuilder.InputBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder.InputBodyOptions@endlink) InputBodyOption
    ##   the input body option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return MergeSubdivisionBodiesBuilder.InputBodyOptions
    @property
    def InputBodyOption(self) -> MergeSubdivisionBodiesBuilder.InputBodyOptions:
        """
        Getter for property: (@link MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder.InputBodyOptions@endlink) InputBodyOption
          the input body option   
            
         
        """
        pass
    
    ## Setter for property: (@link MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder.InputBodyOptions@endlink) InputBodyOption

    ##   the input body option   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @InputBodyOption.setter
    def InputBodyOption(self, inputBody: MergeSubdivisionBodiesBuilder.InputBodyOptions):
        """
        Setter for property: (@link MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder.InputBodyOptions@endlink) InputBodyOption
          the input body option   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectSubdivisionBodyList NXOpen.Features.Subdivision.SelectSubdivisionBodyList@endlink) SubdivisionBodiesToMerge
    ##   the @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features to merge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectSubdivisionBodyList
    @property
    def SubdivisionBodiesToMerge(self) -> SelectSubdivisionBodyList:
        """
        Getter for property: (@link SelectSubdivisionBodyList NXOpen.Features.Subdivision.SelectSubdivisionBodyList@endlink) SubdivisionBodiesToMerge
          the @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features to merge   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::MirrorCageBuilder NXOpen::Features::Subdivision::MirrorCageBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateMirrorCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateMirrorCageBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class MirrorCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.MirrorCageBuilder</ja_class> builder. """


    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane
    ##   the mirror plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane
          the mirror plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane

    ##   the mirror plane   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MirrorPlane.setter
    def MirrorPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MirrorPlane
          the mirror plane   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
    ##   the objects to be mirrored   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
          the objects to be mirrored   
            
         
        """
        pass
    
    ##  Updates the builder based on changes in the mirror plane. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    @staticmethod
    def UpdateOnMirrorPlane(builder: MirrorCageBuilder) -> None:
        """
         Updates the builder based on changes in the mirror plane. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::OffsetCageBuilder NXOpen::Features::Subdivision::OffsetCageBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateOffsetCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateOffsetCageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## NumberOfCopies </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## OffsetDistance.Value </term> <description> 
##  
## 10.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 

class OffsetCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.OffsetCageBuilder</ja_class> builder. """


    ## Getter for property: (bool) CanReverseOffsetDirection
    ##   the flag indicating if offset direction can be reversed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanReverseOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) CanReverseOffsetDirection
          the flag indicating if offset direction can be reversed.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReverseOffsetDirection

    ##   the flag indicating if offset direction can be reversed.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanReverseOffsetDirection.setter
    def CanReverseOffsetDirection(self, reverse: bool):
        """
        Setter for property: (bool) CanReverseOffsetDirection
          the flag indicating if offset direction can be reversed.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfCopies
    ##   the number of copies to offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
          the number of copies to offset   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfCopies

    ##   the number of copies to offset   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
          the number of copies to offset   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
    ##   the objects to be offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
          the objects to be offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##   the offset distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
          the offset distance.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Features::Subdivision::PasteCageData NXOpen::Features::Subdivision::PasteCageData@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreatePasteCageData  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreatePasteCageData @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class PasteCageData(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.PasteCageData</ja_class> builder. """


    ## Getter for property: (bool) CanMoveToolOnly
    ##   the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
          the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanMoveToolOnly

    ##   the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMove: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
          the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##    The tool allows user to transform the pasted topology.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
           The tool allows user to transform the pasted topology.   
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Features::Subdivision::SectionTubeData NXOpen::Features::Subdivision::SectionTubeData@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSectionTubeData  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSectionTubeData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Segments </term> <description> 
##  
## 4 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class SectionTubeData(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SectionTubeData</ja_class> builder. """


    ##  Contains object selection information to be used to create a section. 
    class SelectionData:
        """
         Contains object selection information to be used to create a section. 
        """
        ## Getter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SnappedObject
        ## The selected cage face or convergent face of snapped vertex
        ## @return @link NXOpen.NXObject NXOpen.NXObject@endlink
        @property
        def SnappedObject(self) -> NXOpen.NXObject:
            """
            Getter for property SnappedObject
            The selected cage face or convergent face of snapped vertex

            """
            pass
        
        ## Setter for property :(@link NXOpen.NXObject NXOpen.NXObject@endlink) SnappedObject
        @SnappedObject.setter
        def SnappedObject(self, value: NXOpen.NXObject):
            """
            Getter for property SnappedObject
            The selected cage face or convergent face of snapped vertex
            Setter for property SnappedObject
            The selected cage face or convergent face of snapped vertex

            """
            pass
        
        ## Getter for property :(bool) IsSnapped
        ## Flag indicating if snapping to a vertex of convergent face
        ## @return bool
        @property
        def IsSnapped(self) -> bool:
            """
            Getter for property IsSnapped
            Flag indicating if snapping to a vertex of convergent face

            """
            pass
        
        ## Setter for property :(bool) IsSnapped
        @IsSnapped.setter
        def IsSnapped(self, value: bool):
            """
            Getter for property IsSnapped
            Flag indicating if snapping to a vertex of convergent face
            Setter for property IsSnapped
            Flag indicating if snapping to a vertex of convergent face

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SnappedPosition
        ## The point at which vertex of face is snapped.
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def SnappedPosition(self) -> NXOpen.Point3d:
            """
            Getter for property SnappedPosition
            The point at which vertex of face is snapped.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) SnappedPosition
        @SnappedPosition.setter
        def SnappedPosition(self, value: NXOpen.Point3d):
            """
            Getter for property SnappedPosition
            The point at which vertex of face is snapped.
            Setter for property SnappedPosition
            The point at which vertex of face is snapped.

            """
            pass
        
    
    
    ## Getter for property: (int) Segments
    ##   the segments   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return int
    @property
    def Segments(self) -> int:
        """
        Getter for property: (int) Segments
          the segments   
            
         
        """
        pass
    
    ## Setter for property: (int) Segments

    ##   the segments   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Segments.setter
    def Segments(self, segments: int):
        """
        Setter for property: (int) Segments
          the segments   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ##  Adds a vertex and creates a section if possible. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    ##  Selection data 
    def AddSection(builder: SectionTubeData, selectionData: SectionTubeData.SelectionData) -> None:
        """
         Adds a vertex and creates a section if possible. 
        """
        pass
    
    ##  Recreates the section that is fitted to the convergent body section at the current csys location. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    @staticmethod
    def RefitSection(builder: SectionTubeData) -> None:
        """
         Recreates the section that is fitted to the convergent body section at the current csys location. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents subdivision cage topology object selection. 
## 
##   <br>  Created in NX9.0.0  <br> 

class SelectCageObjectData(NXOpen.TaggedObject): 
    """ Represents subdivision cage topology object selection. """


    ## Getter for property: (bool) CanDeselectObjectsAutomatically
    ##   the flag indicating if previously selected objects can be de-selected during selection of new objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  There is no replacement for this unused property.  <br> 

    ## @return bool
    @property
    def CanDeselectObjectsAutomatically(self) -> bool:
        """
        Getter for property: (bool) CanDeselectObjectsAutomatically
          the flag indicating if previously selected objects can be de-selected during selection of new objects.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanDeselectObjectsAutomatically

    ##   the flag indicating if previously selected objects can be de-selected during selection of new objects.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  There is no replacement for this unused property.  <br> 

    @CanDeselectObjectsAutomatically.setter
    def CanDeselectObjectsAutomatically(self, canDeselect: bool):
        """
        Setter for property: (bool) CanDeselectObjectsAutomatically
          the flag indicating if previously selected objects can be de-selected during selection of new objects.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectionList
    ##   the object list.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectionList
          the object list.  
             
         
        """
        pass
    
    ##  Clears the currently present objects and adds new objects. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Objects to process. 
    def ClearAndAdd(builder: SelectCageObjectData, objects: List[NXOpen.NXObject], view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         Clears the currently present objects and adds new objects. 
        """
        pass
    
    ##  Sets the cursor location in absolute coordinates. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetCursorLocation(builder: SelectCageObjectData, point: NXOpen.Point3d) -> None:
        """
         Sets the cursor location in absolute coordinates. 
        """
        pass
    
    ##  Sets the view direction. 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 

    ## License requirements: None.
    ##  
    def SetViewDirection(builder: SelectCageObjectData, direction: NXOpen.Vector3d) -> None:
        """
         Sets the view direction. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectSubdivisionBodyList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""


    ## Getter for property: (bool) DuplicatesAllowed
    ##   whether duplicate objects are allowed in the selection list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
          whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##   the number of objects in the list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
          the number of objects in the list.  
          
              
         
        """
        pass
    
    ##  Adds an object to the list
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to add 
    def Add(object_list: SelectSubdivisionBodyList, objectValue: SubdivisionBody) -> bool:
        """
         Adds an object to the list
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects with views to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  objects to add 
    def AddWithViews(object_list: SelectSubdivisionBodyList, objects: List[SubdivisionBody], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  objects to add 
    @overload
    def Add(self, object_list: SelectSubdivisionBodyList, objects: List[SubdivisionBody]) -> bool:
        """
         Adds a set of objects to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the objects from a SelectionMethod to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  selection method containing objects to add 
    @overload
    def Add(self, object_list: SelectSubdivisionBodyList, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the object with the objects view and objects point
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  selected object 
    @overload
    def Add(self, object_list: SelectSubdivisionBodyList, selection: SubdivisionBody, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##   snap point type
    @overload
    def Add(self, object_list: SelectSubdivisionBodyList, snap_type: NXOpen.InferSnapType.SnapType, selection1: SubdivisionBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SubdivisionBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObjectList::Add NXOpen::SelectObjectList::Add@endlink .  <br> 

    ## License requirements: None.
    ##  selected object 
    @overload
    def Add(self, object_list: SelectSubdivisionBodyList, selection: SubdivisionBody, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Removes all items from the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: SelectSubdivisionBodyList) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    
    ##  Returns whether the specified object is already in the list or not.
    ##     
    ##  @return list_contains (bool):  true if object is in the list, false otherwise .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  object to check 
    def Contains(object_list: SelectSubdivisionBodyList, objectValue: SubdivisionBody) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link SubdivisionBody List[NXOpen.Features.Subdivision.SubdivisionBody]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArray(object_list: SelectSubdivisionBodyList) -> List[SubdivisionBody]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link SubdivisionBody List[NXOpen.Features.Subdivision.SubdivisionBody]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectObjectArray(object_list: SelectSubdivisionBodyList) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Object to remove 
    def Remove(object_list: SelectSubdivisionBodyList, objectValue: SubdivisionBody) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified objects from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Objects to remove 
    def RemoveArray(object_list: SelectSubdivisionBodyList, objects: List[SubdivisionBody]) -> bool:
        """
         Remove specified objects from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object / view was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  Object to remove 
    @overload
    def Remove(self, object_list: SelectSubdivisionBodyList, objectValue: SubdivisionBody, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object / view was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##   snap point type
    @overload
    def Remove(self, object_list: SelectSubdivisionBodyList, snap_type: NXOpen.InferSnapType.SnapType, selection1: SubdivisionBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SubdivisionBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Removes the objects from a SelectionMethod from the list
    ##     
    ##  @return removed (bool):  True if successfully removed all objects from the list;
    ##                                     False if there was at least one object that was not a
    ##                                     member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ##  selection method containing objects to add 
    @overload
    def Remove(self, object_list: SelectSubdivisionBodyList, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         @return removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    
    ##  Sets the list of objects in the selection list. This will clear any existing
    ##     items in the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  items to put in the list
    def SetArray(object_list: SelectSubdivisionBodyList, objects: List[SubdivisionBody]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
    
import NXOpen
##  Represents a @link Features::Subdivision::SplitSubdivisionBodyBuilder Features::Subdivision::SplitSubdivisionBodyBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSplitSubdivisionBodyBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSplitSubdivisionBodyBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## InputBodyOption </term> <description> 
##  
## Delete </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 

class SplitSubdivisionBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Features.Subdivision.SplitSubdivisionBodyBuilder</ja_class> builder. """


    ##  Options indicating actions to be taken on input @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features 
    ##  Keep the feature as they are 
    class InputBodyOptions(Enum):
        """
        Members Include: <Keep> <Hide> <Delete>
        """
        Keep: int
        Hide: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SplitSubdivisionBodyBuilder.InputBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder.InputBodyOptions@endlink) InputBodyOption
    ##   the input body option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SplitSubdivisionBodyBuilder.InputBodyOptions
    @property
    def InputBodyOption(self) -> SplitSubdivisionBodyBuilder.InputBodyOptions:
        """
        Getter for property: (@link SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder.InputBodyOptions@endlink) InputBodyOption
          the input body option   
            
         
        """
        pass
    
    ## Setter for property: (@link SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder.InputBodyOptions@endlink) InputBodyOption

    ##   the input body option   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @InputBodyOption.setter
    def InputBodyOption(self, inputBody: SplitSubdivisionBodyBuilder.InputBodyOptions):
        """
        Setter for property: (@link SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder.InputBodyOptions@endlink) InputBodyOption
          the input body option   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectSubdivisionBodyList NXOpen.Features.Subdivision.SelectSubdivisionBodyList@endlink) SubdivisionBodiesToSplit
    ##   the @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features to split   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectSubdivisionBodyList
    @property
    def SubdivisionBodiesToSplit(self) -> SelectSubdivisionBodyList:
        """
        Getter for property: (@link SelectSubdivisionBodyList NXOpen.Features.Subdivision.SelectSubdivisionBodyList@endlink) SubdivisionBodiesToSplit
          the @link Features::Subdivision::SubdivisionBody Features::Subdivision::SubdivisionBody@endlink  features to split   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::StartSymmetricModelingBuilder NXOpen::Features::Subdivision::StartSymmetricModelingBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateStartSymmetricModelingBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateStartSymmetricModelingBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class StartSymmetricModelingBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.StartSymmetricModelingBuilder</ja_class> builder """


    ##  The options used to establish symmetric model 
    ##  Cuts the mesh 
    class MirrorProcedureOption(Enum):
        """
        Members Include: <CutBody> <ProjectEdge>
        """
        CutBody: int
        ProjectEdge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StartSymmetricModelingBuilder.MirrorProcedureOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) EdgesToProject
    ##   the edges to project   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def EdgesToProject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) EdgesToProject
          the edges to project   
            
         
        """
        pass
    
    ## Getter for property: (@link StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Features.Subdivision.StartSymmetricModelingBuilder.MirrorProcedureOption@endlink) MirrorProcedureOptions
    ##   the mirror procedure options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  This property is redundent and hence not necessary.  <br> 

    ## @return StartSymmetricModelingBuilder.MirrorProcedureOption
    @property
    def MirrorProcedureOptions(self) -> StartSymmetricModelingBuilder.MirrorProcedureOption:
        """
        Getter for property: (@link StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Features.Subdivision.StartSymmetricModelingBuilder.MirrorProcedureOption@endlink) MirrorProcedureOptions
          the mirror procedure options   
            
         
        """
        pass
    
    ## Setter for property: (@link StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Features.Subdivision.StartSymmetricModelingBuilder.MirrorProcedureOption@endlink) MirrorProcedureOptions

    ##   the mirror procedure options   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  This property is redundent and hence not necessary.  <br> 

    @MirrorProcedureOptions.setter
    def MirrorProcedureOptions(self, mirrorProcedureOptions: StartSymmetricModelingBuilder.MirrorProcedureOption):
        """
        Setter for property: (@link StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Features.Subdivision.StartSymmetricModelingBuilder.MirrorProcedureOption@endlink) MirrorProcedureOptions
          the mirror procedure options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##   the plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
          the plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##   the plane   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
          the plane   
            
         
        """
        pass
    
    ## Getter for property: (bool) SwitchSide
    ##   the flag indicating if the mirror side should be switched   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def SwitchSide(self) -> bool:
        """
        Getter for property: (bool) SwitchSide
          the flag indicating if the mirror side should be switched   
            
         
        """
        pass
    
    ## Setter for property: (bool) SwitchSide

    ##   the flag indicating if the mirror side should be switched   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SwitchSide.setter
    def SwitchSide(self, switchSide: bool):
        """
        Setter for property: (bool) SwitchSide
          the flag indicating if the mirror side should be switched   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of subdivision body feature tools.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionBodyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of subdivision body feature tools. """


    ##  Creates a @link NXOpen::Features::Subdivision::CageFromFacetBodyBuilder NXOpen::Features::Subdivision::CageFromFacetBodyBuilder@endlink . 
    ##  @return builder (@link CageFromFacetBodyBuilder NXOpen.Features.Subdivision.CageFromFacetBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateCageFromFacetBodyBuilder(part: SubdivisionBodyCollection) -> CageFromFacetBodyBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::CageFromFacetBodyBuilder NXOpen::Features::Subdivision::CageFromFacetBodyBuilder@endlink . 
         @return builder (@link CageFromFacetBodyBuilder NXOpen.Features.Subdivision.CageFromFacetBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::CagePolylineBuilder NXOpen::Features::Subdivision::CagePolylineBuilder@endlink . 
    ##  @return builder (@link CagePolylineBuilder NXOpen.Features.Subdivision.CagePolylineBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ##  @link NXOpen::Polyline NXOpen::Polyline@endlink 
    def CreateCagePolylineBuilder(part: SubdivisionBodyCollection, polyline: NXOpen.Polyline) -> CagePolylineBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::CagePolylineBuilder NXOpen::Features::Subdivision::CagePolylineBuilder@endlink . 
         @return builder (@link CagePolylineBuilder NXOpen.Features.Subdivision.CagePolylineBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::CopyCageBuilder NXOpen::Features::Subdivision::CopyCageBuilder@endlink . 
    ##  @return builder (@link CopyCageBuilder NXOpen.Features.Subdivision.CopyCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateCopyCageBuilder(part: SubdivisionBodyCollection) -> CopyCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::CopyCageBuilder NXOpen::Features::Subdivision::CopyCageBuilder@endlink . 
         @return builder (@link CopyCageBuilder NXOpen.Features.Subdivision.CopyCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::CopyCageData NXOpen::Features::Subdivision::CopyCageData@endlink . 
    ##  @return data (@link CopyCageData NXOpen.Features.Subdivision.CopyCageData@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateCopyCageData(part: SubdivisionBodyCollection) -> CopyCageData:
        """
         Creates a @link NXOpen::Features::Subdivision::CopyCageData NXOpen::Features::Subdivision::CopyCageData@endlink . 
         @return data (@link CopyCageData NXOpen.Features.Subdivision.CopyCageData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::DefineWorkRegionBuilder NXOpen::Features::Subdivision::DefineWorkRegionBuilder@endlink . 
    ##  @return data (@link DefineWorkRegionBuilder NXOpen.Features.Subdivision.DefineWorkRegionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateDefineWorkRegionBuilder(part: SubdivisionBodyCollection) -> DefineWorkRegionBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::DefineWorkRegionBuilder NXOpen::Features::Subdivision::DefineWorkRegionBuilder@endlink . 
         @return data (@link DefineWorkRegionBuilder NXOpen.Features.Subdivision.DefineWorkRegionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::DeleteConstraintBuilder NXOpen::Features::Subdivision::DeleteConstraintBuilder@endlink . 
    ##  @return builder (@link DeleteConstraintBuilder NXOpen.Features.Subdivision.DeleteConstraintBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateDeleteConstraintBuilder(part: SubdivisionBodyCollection) -> DeleteConstraintBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::DeleteConstraintBuilder NXOpen::Features::Subdivision::DeleteConstraintBuilder@endlink . 
         @return builder (@link DeleteConstraintBuilder NXOpen.Features.Subdivision.DeleteConstraintBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::DrawCageData NXOpen::Features::Subdivision::DrawCageData@endlink . 
    ##  @return data (@link DrawCageData NXOpen.Features.Subdivision.DrawCageData@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateDrawCageData(part: SubdivisionBodyCollection) -> DrawCageData:
        """
         Creates a @link NXOpen::Features::Subdivision::DrawCageData NXOpen::Features::Subdivision::DrawCageData@endlink . 
         @return data (@link DrawCageData NXOpen.Features.Subdivision.DrawCageData@endlink): .
        """
        pass
    
    ##  Creates an empty cage section builder object. 
    ##  @return builder (@link CageSectionData NXOpen.Features.Subdivision.CageSectionData@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateEmptyCageSectionBuilder(part: SubdivisionBodyCollection) -> CageSectionData:
        """
         Creates an empty cage section builder object. 
         @return builder (@link CageSectionData NXOpen.Features.Subdivision.CageSectionData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::ExportSubdivisionGeometryBuilder NXOpen::Features::Subdivision::ExportSubdivisionGeometryBuilder@endlink . 
    ##  @return builder (@link ExportSubdivisionGeometryBuilder NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjCreator NXOpen::WavefrontObjCreator@endlink  instead  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateExportSubdivisionGeometryBuilder(part: SubdivisionBodyCollection) -> ExportSubdivisionGeometryBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::ExportSubdivisionGeometryBuilder NXOpen::Features::Subdivision::ExportSubdivisionGeometryBuilder@endlink . 
         @return builder (@link ExportSubdivisionGeometryBuilder NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::ExtractCagePolylineBuilder NXOpen::Features::Subdivision::ExtractCagePolylineBuilder@endlink . 
    ##  @return builder (@link ExtractCagePolylineBuilder NXOpen.Features.Subdivision.ExtractCagePolylineBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateExtractCagePolylineBuilder(part: SubdivisionBodyCollection) -> ExtractCagePolylineBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::ExtractCagePolylineBuilder NXOpen::Features::Subdivision::ExtractCagePolylineBuilder@endlink . 
         @return builder (@link ExtractCagePolylineBuilder NXOpen.Features.Subdivision.ExtractCagePolylineBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::ImportSubdivisionGeometryBuilder NXOpen::Features::Subdivision::ImportSubdivisionGeometryBuilder@endlink . 
    ##  @return builder (@link ImportSubdivisionGeometryBuilder NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::WavefrontObjImporter NXOpen::WavefrontObjImporter@endlink  instead  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateImportSubdivisionGeometryBuilder(part: SubdivisionBodyCollection) -> ImportSubdivisionGeometryBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::ImportSubdivisionGeometryBuilder NXOpen::Features::Subdivision::ImportSubdivisionGeometryBuilder@endlink . 
         @return builder (@link ImportSubdivisionGeometryBuilder NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::MergeSubdivisionBodiesBuilder NXOpen::Features::Subdivision::MergeSubdivisionBodiesBuilder@endlink . 
    ##  @return builder (@link MergeSubdivisionBodiesBuilder NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateMergeSubdivisionBodiesBuilder(part: SubdivisionBodyCollection) -> MergeSubdivisionBodiesBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::MergeSubdivisionBodiesBuilder NXOpen::Features::Subdivision::MergeSubdivisionBodiesBuilder@endlink . 
         @return builder (@link MergeSubdivisionBodiesBuilder NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::MirrorCageBuilder NXOpen::Features::Subdivision::MirrorCageBuilder@endlink . 
    ##  @return builder (@link MirrorCageBuilder NXOpen.Features.Subdivision.MirrorCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateMirrorCageBuilder(part: SubdivisionBodyCollection) -> MirrorCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::MirrorCageBuilder NXOpen::Features::Subdivision::MirrorCageBuilder@endlink . 
         @return builder (@link MirrorCageBuilder NXOpen.Features.Subdivision.MirrorCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::OffsetCageBuilder NXOpen::Features::Subdivision::OffsetCageBuilder@endlink . 
    ##  @return builder (@link OffsetCageBuilder NXOpen.Features.Subdivision.OffsetCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateOffsetCageBuilder(part: SubdivisionBodyCollection) -> OffsetCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::OffsetCageBuilder NXOpen::Features::Subdivision::OffsetCageBuilder@endlink . 
         @return builder (@link OffsetCageBuilder NXOpen.Features.Subdivision.OffsetCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::PasteCageData NXOpen::Features::Subdivision::PasteCageData@endlink . 
    ##  @return data (@link PasteCageData NXOpen.Features.Subdivision.PasteCageData@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreatePasteCageData(part: SubdivisionBodyCollection) -> PasteCageData:
        """
         Creates a @link NXOpen::Features::Subdivision::PasteCageData NXOpen::Features::Subdivision::PasteCageData@endlink . 
         @return data (@link PasteCageData NXOpen.Features.Subdivision.PasteCageData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SectionTubeData NXOpen::Features::Subdivision::SectionTubeData@endlink . 
    ##  @return data (@link SectionTubeData NXOpen.Features.Subdivision.SectionTubeData@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSectionTubeData(part: SubdivisionBodyCollection) -> SectionTubeData:
        """
         Creates a @link NXOpen::Features::Subdivision::SectionTubeData NXOpen::Features::Subdivision::SectionTubeData@endlink . 
         @return data (@link SectionTubeData NXOpen.Features.Subdivision.SectionTubeData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SplitSubdivisionBodyBuilder NXOpen::Features::Subdivision::SplitSubdivisionBodyBuilder@endlink . 
    ##  @return builder (@link SplitSubdivisionBodyBuilder NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSplitSubdivisionBodyBuilder(part: SubdivisionBodyCollection) -> SplitSubdivisionBodyBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SplitSubdivisionBodyBuilder NXOpen::Features::Subdivision::SplitSubdivisionBodyBuilder@endlink . 
         @return builder (@link SplitSubdivisionBodyBuilder NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::StartSymmetricModelingBuilder NXOpen::Features::Subdivision::StartSymmetricModelingBuilder@endlink . 
    ##  @return builder (@link StartSymmetricModelingBuilder NXOpen.Features.Subdivision.StartSymmetricModelingBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateStartSymmetricModelingBuilder(part: SubdivisionBodyCollection) -> StartSymmetricModelingBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::StartSymmetricModelingBuilder NXOpen::Features::Subdivision::StartSymmetricModelingBuilder@endlink . 
         @return builder (@link StartSymmetricModelingBuilder NXOpen.Features.Subdivision.StartSymmetricModelingBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder@endlink . 
    ##  @return builder (@link SubdivisionBridgeFaceBuilder NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionBridgeFaceBuilder(part: SubdivisionBodyCollection) -> SubdivisionBridgeFaceBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder@endlink . 
         @return builder (@link SubdivisionBridgeFaceBuilder NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionConnectCageBuilder NXOpen::Features::Subdivision::SubdivisionConnectCageBuilder@endlink . 
    ##  @return builder (@link SubdivisionConnectCageBuilder NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionConnectCageBuilder(part: SubdivisionBodyCollection) -> SubdivisionConnectCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionConnectCageBuilder NXOpen::Features::Subdivision::SubdivisionConnectCageBuilder@endlink . 
         @return builder (@link SubdivisionConnectCageBuilder NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder@endlink . 
    ##  @return builder (@link SubdivisionDeleteCageBuilder NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link  Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteObjectBuilder   Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteObjectBuilder @endlink  instead.  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionDeleteCageBuilder(part: SubdivisionBodyCollection) -> SubdivisionDeleteCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder@endlink . 
         @return builder (@link SubdivisionDeleteCageBuilder NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionDeleteFaceBuilder NXOpen::Features::Subdivision::SubdivisionDeleteFaceBuilder@endlink . 
    ##  @return builder (@link SubdivisionDeleteFaceBuilder NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link  Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteCageBuilder   Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteCageBuilder @endlink  instead.  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionDeleteFaceBuilder(part: SubdivisionBodyCollection) -> SubdivisionDeleteFaceBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionDeleteFaceBuilder NXOpen::Features::Subdivision::SubdivisionDeleteFaceBuilder@endlink . 
         @return builder (@link SubdivisionDeleteFaceBuilder NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder@endlink . 
    ##  @return builder (@link SubdivisionDeleteObjectBuilder NXOpen.Features.Subdivision.SubdivisionDeleteObjectBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionDeleteObjectBuilder(part: SubdivisionBodyCollection) -> SubdivisionDeleteObjectBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder@endlink . 
         @return builder (@link SubdivisionDeleteObjectBuilder NXOpen.Features.Subdivision.SubdivisionDeleteObjectBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder@endlink . 
    ##  @return builder (@link SubdivisionExtrudeCageBuilder NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionExtrudeCageBuilder(part: SubdivisionBodyCollection) -> SubdivisionExtrudeCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder@endlink . 
         @return builder (@link SubdivisionExtrudeCageBuilder NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionFillBuilder NXOpen::Features::Subdivision::SubdivisionFillBuilder@endlink . 
    ##  @return builder (@link SubdivisionFillBuilder NXOpen.Features.Subdivision.SubdivisionFillBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionFillBuilder(part: SubdivisionBodyCollection) -> SubdivisionFillBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionFillBuilder NXOpen::Features::Subdivision::SubdivisionFillBuilder@endlink . 
         @return builder (@link SubdivisionFillBuilder NXOpen.Features.Subdivision.SubdivisionFillBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionLoftBuilder NXOpen::Features::Subdivision::SubdivisionLoftBuilder@endlink . 
    ##  @return builder (@link SubdivisionLoftBuilder NXOpen.Features.Subdivision.SubdivisionLoftBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionLoftBuilder(part: SubdivisionBodyCollection) -> SubdivisionLoftBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionLoftBuilder NXOpen::Features::Subdivision::SubdivisionLoftBuilder@endlink . 
         @return builder (@link SubdivisionLoftBuilder NXOpen.Features.Subdivision.SubdivisionLoftBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionMergeFaceBuilder NXOpen::Features::Subdivision::SubdivisionMergeFaceBuilder@endlink . 
    ##  @return builder (@link SubdivisionMergeFaceBuilder NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionMergeFaceBuilder(part: SubdivisionBodyCollection) -> SubdivisionMergeFaceBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionMergeFaceBuilder NXOpen::Features::Subdivision::SubdivisionMergeFaceBuilder@endlink . 
         @return builder (@link SubdivisionMergeFaceBuilder NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder@endlink . 
    ##  @return builder (@link SubdivisionPrimitiveShapeBuilder NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilderEx@endlink  instead  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionPrimitiveShapeBuilder(part: SubdivisionBodyCollection) -> SubdivisionPrimitiveShapeBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder@endlink . 
         @return builder (@link SubdivisionPrimitiveShapeBuilder NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink . 
    ##  @return builder (@link SubdivisionPrimitiveShapeBuilderEx NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionPrimitiveShapeBuilderEx(part: SubdivisionBodyCollection) -> SubdivisionPrimitiveShapeBuilderEx:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink . 
         @return builder (@link SubdivisionPrimitiveShapeBuilderEx NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionProjectCageBuilder NXOpen::Features::Subdivision::SubdivisionProjectCageBuilder@endlink . 
    ##  @return builder (@link SubdivisionProjectCageBuilder NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionProjectCageBuilder(part: SubdivisionBodyCollection) -> SubdivisionProjectCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionProjectCageBuilder NXOpen::Features::Subdivision::SubdivisionProjectCageBuilder@endlink . 
         @return builder (@link SubdivisionProjectCageBuilder NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionProjectCageBuilderEx@endlink . 
    ##  @return builder (@link SubdivisionProjectCageBuilderEx NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionProjectCageBuilderEx(part: SubdivisionBodyCollection) -> SubdivisionProjectCageBuilderEx:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionProjectCageBuilderEx@endlink . 
         @return builder (@link SubdivisionProjectCageBuilderEx NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionRevolveBuilder NXOpen::Features::Subdivision::SubdivisionRevolveBuilder@endlink . 
    ##  @return builder (@link SubdivisionRevolveBuilder NXOpen.Features.Subdivision.SubdivisionRevolveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionRevolveBuilder(part: SubdivisionBodyCollection) -> SubdivisionRevolveBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionRevolveBuilder NXOpen::Features::Subdivision::SubdivisionRevolveBuilder@endlink . 
         @return builder (@link SubdivisionRevolveBuilder NXOpen.Features.Subdivision.SubdivisionRevolveBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder@endlink . 
    ##  @return builder (@link SubdivisionSetContinuityBuilder NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionSetContinuityBuilder(part: SubdivisionBodyCollection) -> SubdivisionSetContinuityBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder@endlink . 
         @return builder (@link SubdivisionSetContinuityBuilder NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionSetWeightBuilder NXOpen::Features::Subdivision::SubdivisionSetWeightBuilder@endlink . 
    ##  @return builder (@link SubdivisionSetWeightBuilder NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionSetWeightBuilder(part: SubdivisionBodyCollection) -> SubdivisionSetWeightBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionSetWeightBuilder NXOpen::Features::Subdivision::SubdivisionSetWeightBuilder@endlink . 
         @return builder (@link SubdivisionSetWeightBuilder NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionSewCageBuilder NXOpen::Features::Subdivision::SubdivisionSewCageBuilder@endlink . 
    ##  @return builder (@link SubdivisionSewCageBuilder NXOpen.Features.Subdivision.SubdivisionSewCageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionSewCageBuilder(part: SubdivisionBodyCollection) -> SubdivisionSewCageBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionSewCageBuilder NXOpen::Features::Subdivision::SubdivisionSewCageBuilder@endlink . 
         @return builder (@link SubdivisionSewCageBuilder NXOpen.Features.Subdivision.SubdivisionSewCageBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionSplitFaceBuilder NXOpen::Features::Subdivision::SubdivisionSplitFaceBuilder@endlink . 
    ##  @return builder (@link SubdivisionSplitFaceBuilder NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionSplitFaceBuilder(part: SubdivisionBodyCollection) -> SubdivisionSplitFaceBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionSplitFaceBuilder NXOpen::Features::Subdivision::SubdivisionSplitFaceBuilder@endlink . 
         @return builder (@link SubdivisionSplitFaceBuilder NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionSubdivideFaceBuilder NXOpen::Features::Subdivision::SubdivisionSubdivideFaceBuilder@endlink . 
    ##  @return builder (@link SubdivisionSubdivideFaceBuilder NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    def CreateSubdivisionSubdivideFaceBuilder(part: SubdivisionBodyCollection) -> SubdivisionSubdivideFaceBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionSubdivideFaceBuilder NXOpen::Features::Subdivision::SubdivisionSubdivideFaceBuilder@endlink . 
         @return builder (@link SubdivisionSubdivideFaceBuilder NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionSweepBuilder NXOpen::Features::Subdivision::SubdivisionSweepBuilder@endlink . 
    ##  @return builder (@link SubdivisionSweepBuilder NXOpen.Features.Subdivision.SubdivisionSweepBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionSweepBuilder(part: SubdivisionBodyCollection) -> SubdivisionSweepBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionSweepBuilder NXOpen::Features::Subdivision::SubdivisionSweepBuilder@endlink . 
         @return builder (@link SubdivisionSweepBuilder NXOpen.Features.Subdivision.SubdivisionSweepBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::SubdivisionTubeBuilder NXOpen::Features::Subdivision::SubdivisionTubeBuilder@endlink . 
    ##  @return builder (@link SubdivisionTubeBuilder NXOpen.Features.Subdivision.SubdivisionTubeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateSubdivisionTubeBuilder(part: SubdivisionBodyCollection) -> SubdivisionTubeBuilder:
        """
         Creates a @link NXOpen::Features::Subdivision::SubdivisionTubeBuilder NXOpen::Features::Subdivision::SubdivisionTubeBuilder@endlink . 
         @return builder (@link SubdivisionTubeBuilder NXOpen.Features.Subdivision.SubdivisionTubeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::Subdivision::TransformCageData NXOpen::Features::Subdivision::TransformCageData@endlink . 
    ##  @return data (@link TransformCageData NXOpen.Features.Subdivision.TransformCageData@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    def CreateTransformCageData(part: SubdivisionBodyCollection) -> TransformCageData:
        """
         Creates a @link NXOpen::Features::Subdivision::TransformCageData NXOpen::Features::Subdivision::TransformCageData@endlink . 
         @return data (@link TransformCageData NXOpen.Features.Subdivision.TransformCageData@endlink): .
        """
        pass
    
    ##  Stops the symmetric modeling. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def StopSymmetricModeling(part: SubdivisionBodyCollection) -> None:
        """
         Stops the symmetric modeling. 
        """
        pass
    
import NXOpen.Features
##  Represents a subdivision body feature.  <br> An instance of this class can be obtained from @link SubdivisionTaskEnvironment::ActiveSubdivisionBodyFeature SubdivisionTaskEnvironment::ActiveSubdivisionBodyFeature@endlink   <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionBody(NXOpen.Features.BodyFeature): 
    """ Represents a subdivision body feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionBridgeFaceBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionBridgeFaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## NumSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionBridgeFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder</ja_class> builder.  """


    ##  Type of continuity. 
    ##  Smooth continuity 
    class ContinuityType(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionBridgeFaceBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.ContinuityType@endlink) Continuity
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to the outer
    ##                 edges of the faces specified by @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1@endlink  and 
    ##                 @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionBridgeFaceBuilder.ContinuityType
    @property
    def Continuity(self) -> SubdivisionBridgeFaceBuilder.ContinuityType:
        """
        Getter for property: (@link SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces specified by @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1@endlink  and 
                        @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.ContinuityType@endlink) Continuity

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to the outer
    ##                 edges of the faces specified by @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1@endlink  and 
    ##                 @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2@endlink .   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Continuity.setter
    def Continuity(self, continuity: SubdivisionBridgeFaceBuilder.ContinuityType):
        """
        Setter for property: (@link SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces specified by @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet1@endlink  and 
                        @link NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2 NXOpen::Features::Subdivision::SubdivisionBridgeFaceBuilder::FaceSet2@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FaceSet1
    ##   the first face set.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def FaceSet1(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FaceSet1
          the first face set.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FaceSet2
    ##   the second face set.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def FaceSet2(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FaceSet2
          the second face set.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumSegments
    ##   the number of segments in the output bridge faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumSegments(self) -> int:
        """
        Getter for property: (int) NumSegments
          the number of segments in the output bridge faces   
            
         
        """
        pass
    
    ## Setter for property: (int) NumSegments

    ##   the number of segments in the output bridge faces   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumSegments.setter
    def NumSegments(self, numSegments: int):
        """
        Setter for property: (int) NumSegments
          the number of segments in the output bridge faces   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionConnectCageBuilder NXOpen::Features::Subdivision::SubdivisionConnectCageBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionConnectCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionConnectCageBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SubdivisionConnectCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder</ja_class> builder.  """


    ##  Represents the continuity type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Smooth</term><description> 
    ## </description> </item><item><term> 
    ## Sharp</term><description> 
    ## </description> </item></list>
    class ContinuityTypes(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionConnectCageBuilder.ContinuityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) CageEdgeToEdit
    ##   the cage edge to edit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def CageEdgeToEdit(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) CageEdgeToEdit
          the cage edge to edit   
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder.ContinuityTypes@endlink) ContinuityType
    ##   the continuity.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionConnectCageBuilder.ContinuityTypes
    @property
    def ContinuityType(self) -> SubdivisionConnectCageBuilder.ContinuityTypes:
        """
        Getter for property: (@link SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder.ContinuityTypes@endlink) ContinuityType
          the continuity.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder.ContinuityTypes@endlink) ContinuityType

    ##   the continuity.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ContinuityType.setter
    def ContinuityType(self, continuityType: SubdivisionConnectCageBuilder.ContinuityTypes):
        """
        Setter for property: (@link SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder.ContinuityTypes@endlink) ContinuityType
          the continuity.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ExternalReference
    ##   the external edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def ExternalReference(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ExternalReference
          the external edges   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteCageBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder@endlink  instead.  <br> 

class SubdivisionDeleteCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectCageObject
    ##   the select cage object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder NXOpen::Features::Subdivision::SubdivisionDeleteObjectBuilder@endlink  instead.  <br> 

    ## @return SelectCageObjectData
    @property
    def SelectCageObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectCageObject
          the select cage object   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionDeleteFaceBuilder NXOpen::Features::Subdivision::SubdivisionDeleteFaceBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteFaceBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteFaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder@endlink  instead.  <br> 

class SubdivisionDeleteFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FaceToDelete
    ##   the face to delete.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder NXOpen::Features::Subdivision::SubdivisionDeleteCageBuilder@endlink  instead.  <br> 

    ## @return SelectCageObjectData
    @property
    def FaceToDelete(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FaceToDelete
          the face to delete.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link Features::Subdivision::SubdivisionDeleteObjectBuilder Features::Subdivision::SubdivisionDeleteObjectBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteObjectBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionDeleteObjectBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SubdivisionDeleteObjectBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Features.Subdivision.SubdivisionDeleteObjectBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
    ##   the objects to be deleted.  
    ##      
    ##  
    ## Getter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def Objects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) Objects
          the objects to be deleted.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionExtrudeCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionExtrudeCageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanRelocateToolToSelection </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## CanReorientToolToSelection </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## NumberOfSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionExtrudeCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder</ja_class> builder.  """


    ##  Type of continuity. 
    ##  Smooth continuity 
    class ContinuityType(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the extrude direction. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inferred</term><description> 
    ## </description> </item><item><term> 
    ## Vector</term><description> 
    ## </description> </item><item><term> 
    ## Perpendicular</term><description> 
    ## </description> </item></list>
    class DirectionType(Enum):
        """
        Members Include: <Inferred> <Vector> <Perpendicular>
        """
        Inferred: int
        Vector: int
        Perpendicular: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Scaling method 
    ##  Scale in the specified direction 
    class ScalingMethodType(Enum):
        """
        Members Include: <Linear> <Planar> <Uniform>
        """
        Linear: int
        Planar: int
        Uniform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Transformation method types 
    ##  Drag extruded topology in linear direction 
    class TransformationMethodType(Enum):
        """
        Members Include: <DragLinear> <Transform>
        """
        DragLinear: int
        Transform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionExtrudeCageBuilder.TransformationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanMoveToolOnly
    ##   the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
          the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanMoveToolOnly

    ##   the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMove: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
          the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanRelocateToolToSelection
    ##   the flag indicating if transformer tool can be relocated based on cage topology selection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
          the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanRelocateToolToSelection

    ##   the flag indicating if transformer tool can be relocated based on cage topology selection.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocate: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
          the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanReorientToolToSelection
    ##   the flag indicating if transformer tool can be reoriented based on cage topology selection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
          the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReorientToolToSelection

    ##   the flag indicating if transformer tool can be reoriented based on cage topology selection.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorient: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
          the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ContinuityType@endlink) Continuity
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to the outer
    ##                 edges of the faces or boundary edges specified by @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionExtrudeCageBuilder.ContinuityType
    @property
    def Continuity(self) -> SubdivisionExtrudeCageBuilder.ContinuityType:
        """
        Getter for property: (@link SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces or boundary edges specified by @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ContinuityType@endlink) Continuity

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to the outer
    ##                 edges of the faces or boundary edges specified by @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject@endlink .   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Continuity.setter
    def Continuity(self, continuity: SubdivisionExtrudeCageBuilder.ContinuityType):
        """
        Setter for property: (@link SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to the outer
                        edges of the faces or boundary edges specified by @link NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject NXOpen::Features::Subdivision::SubdivisionExtrudeCageBuilder::SelectionObject@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.DirectionType@endlink) DirectionOption
    ##   the direction option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SubdivisionExtrudeCageBuilder.DirectionType
    @property
    def DirectionOption(self) -> SubdivisionExtrudeCageBuilder.DirectionType:
        """
        Getter for property: (@link SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.DirectionType@endlink) DirectionOption
          the direction option   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.DirectionType@endlink) DirectionOption

    ##   the direction option   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DirectionOption.setter
    def DirectionOption(self, directionOption: SubdivisionExtrudeCageBuilder.DirectionType):
        """
        Setter for property: (@link SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.DirectionType@endlink) DirectionOption
          the direction option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
    ##   the distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
          the distance.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfSegments
    ##   the number of segments.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
          the number of segments.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfSegments

    ##   the number of segments.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberOfSegments.setter
    def NumberOfSegments(self, numOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
          the number of segments.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ScalingMethodType@endlink) ScalingMethod
    ##   the scaling method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionExtrudeCageBuilder.ScalingMethodType
    @property
    def ScalingMethod(self) -> SubdivisionExtrudeCageBuilder.ScalingMethodType:
        """
        Getter for property: (@link SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ScalingMethodType@endlink) ScalingMethod
          the scaling method.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ScalingMethodType@endlink) ScalingMethod

    ##   the scaling method.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SubdivisionExtrudeCageBuilder.ScalingMethodType):
        """
        Setter for property: (@link SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ScalingMethodType@endlink) ScalingMethod
          the scaling method.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectionObject
    ##   the selection object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def SelectionObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectionObject
          the selection object.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.TransformationMethodType@endlink) TransformationMethod
    ##   the transformation method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionExtrudeCageBuilder.TransformationMethodType
    @property
    def TransformationMethod(self) -> SubdivisionExtrudeCageBuilder.TransformationMethodType:
        """
        Getter for property: (@link SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.TransformationMethodType@endlink) TransformationMethod
          the transformation method.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.TransformationMethodType@endlink) TransformationMethod

    ##   the transformation method.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TransformationMethod.setter
    def TransformationMethod(self, method: SubdivisionExtrudeCageBuilder.TransformationMethodType):
        """
        Setter for property: (@link SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.TransformationMethodType@endlink) TransformationMethod
          the transformation method.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##   the vector for extrude.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
          the vector for extrude.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##   the vector for extrude.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
          the vector for extrude.  
             
         
        """
        pass
    
    ##  Perform extrude operation. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def Extrude(builder: SubdivisionExtrudeCageBuilder) -> None:
        """
         Perform extrude operation. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionFillBuilder NXOpen::Features::Subdivision::SubdivisionFillBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionFillBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionFillBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionFillBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionFillBuilder</ja_class> builder.  """


    ##  Type of continuity. 
    ##  Smooth continuity 
    class ContinuityType(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionFillBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanConnectSymmetrically
    ##   the flag indicating if selected edges are to be connected with their symmetric counterpart.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanConnectSymmetrically(self) -> bool:
        """
        Getter for property: (bool) CanConnectSymmetrically
          the flag indicating if selected edges are to be connected with their symmetric counterpart.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanConnectSymmetrically

    ##   the flag indicating if selected edges are to be connected with their symmetric counterpart.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanConnectSymmetrically.setter
    def CanConnectSymmetrically(self, connectSymmetrically: bool):
        """
        Setter for property: (bool) CanConnectSymmetrically
          the flag indicating if selected edges are to be connected with their symmetric counterpart.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionFillBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionFillBuilder.ContinuityType@endlink) Continuity
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 specified by @link NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionFillBuilder.ContinuityType
    @property
    def Continuity(self) -> SubdivisionFillBuilder.ContinuityType:
        """
        Getter for property: (@link SubdivisionFillBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionFillBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        specified by @link NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionFillBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionFillBuilder.ContinuityType@endlink) Continuity

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 specified by @link NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges@endlink .   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Continuity.setter
    def Continuity(self, continuity: SubdivisionFillBuilder.ContinuityType):
        """
        Setter for property: (@link SubdivisionFillBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionFillBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        specified by @link NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges NXOpen::Features::Subdivision::SubdivisionFillBuilder::SelectedEdges@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectedEdges
    ##   the edges to form a face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def SelectedEdges(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectedEdges
          the edges to form a face.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionLoftBuilder NXOpen::Features::Subdivision::SubdivisionLoftBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionLoftBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionLoftBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanSew </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## NumberOfSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class SubdivisionLoftBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionLoftBuilder</ja_class> builder. """


    ##  Type of continuity. 
    ##  Smooth continuity 
    class ContinuityType(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionLoftBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanSew
    ##   the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanSew(self) -> bool:
        """
        Getter for property: (bool) CanSew
          the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    
    ## Setter for property: (bool) CanSew

    ##   the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanSew.setter
    def CanSew(self, canSew: bool):
        """
        Setter for property: (bool) CanSew
          the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionLoftBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionLoftBuilder.ContinuityType@endlink) Continuity
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 of the lofted region that are sewn with the primary existing region.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionLoftBuilder.ContinuityType
    @property
    def Continuity(self) -> SubdivisionLoftBuilder.ContinuityType:
        """
        Getter for property: (@link SubdivisionLoftBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionLoftBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the lofted region that are sewn with the primary existing region.   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionLoftBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionLoftBuilder.ContinuityType@endlink) Continuity

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 of the lofted region that are sewn with the primary existing region.   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Continuity.setter
    def Continuity(self, continuity: SubdivisionLoftBuilder.ContinuityType):
        """
        Setter for property: (@link SubdivisionLoftBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionLoftBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the lofted region that are sewn with the primary existing region.   
         
        """
        pass
    
    ## Getter for property: (bool) IsClosed
    ##   the value indicating if the output mesh is closed.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IsClosed(self) -> bool:
        """
        Getter for property: (bool) IsClosed
          the value indicating if the output mesh is closed.  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsClosed

    ##   the value indicating if the output mesh is closed.  
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @IsClosed.setter
    def IsClosed(self, isClosed: bool):
        """
        Setter for property: (bool) IsClosed
          the value indicating if the output mesh is closed.  
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfSegments
    ##   the number of segments   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
          the number of segments   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfSegments

    ##   the number of segments   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
          the number of segments   
            
         
        """
        pass
    
    ## Getter for property: (@link CageSectionDataList NXOpen.Features.Subdivision.CageSectionDataList@endlink) Sections
    ##   the section objects for lofting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CageSectionDataList
    @property
    def Sections(self) -> CageSectionDataList:
        """
        Getter for property: (@link CageSectionDataList NXOpen.Features.Subdivision.CageSectionDataList@endlink) Sections
          the section objects for lofting   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionMergeFaceBuilder NXOpen::Features::Subdivision::SubdivisionMergeFaceBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionMergeFaceBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionMergeFaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionMergeFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FacesToMerge
    ##   the faces to merge.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def FacesToMerge(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FacesToMerge
          the faces to merge.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilderEx  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilderEx @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CircularSegments </term> <description> 
##  
## 4 </description> </item> 
## 
## <item><term> 
##  
## Height.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## HeightZ.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InnerSize.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LengthX.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## OuterSize.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RadialSegments </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## Size.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## WidthY.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## XSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## YSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ZSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 

class SubdivisionPrimitiveShapeBuilderEx(NXOpen.Builder): 
    """ Represents a <ja_class>Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx</ja_class> builder. """


    ##  Level of subdivisions of cubical cage to construct spherical primitive. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Base</term><description> 
    ## </description> </item><item><term> 
    ## First</term><description> 
    ## </description> </item><item><term> 
    ## Second</term><description> 
    ## </description> </item></list>
    class SphereSubdivisionLevel(Enum):
        """
        Members Include: <Base> <First> <Second>
        """
        Base: int
        First: int
        Second: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Type of primitive. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sphere</term><description> 
    ## </description> </item><item><term> 
    ## Cylinder</term><description> 
    ## </description> </item><item><term> 
    ## Block</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Torus</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Sphere> <Cylinder> <Block> <Circle> <Rectangle> <Torus>
        """
        Sphere: int
        Cylinder: int
        Block: int
        Circle: int
        Rectangle: int
        Torus: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionPrimitiveShapeBuilderEx.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) CircularSegments
    ##   the number of segments in circular direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def CircularSegments(self) -> int:
        """
        Getter for property: (int) CircularSegments
          the number of segments in circular direction.  
             
         
        """
        pass
    
    ## Setter for property: (int) CircularSegments

    ##   the number of segments in circular direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CircularSegments.setter
    def CircularSegments(self, numSegments: int):
        """
        Setter for property: (int) CircularSegments
          the number of segments in circular direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeightZ
    ##   the height in Z direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HeightZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeightZ
          the height in Z direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InnerSize
    ##   the inner size of torus.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InnerSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InnerSize
          the inner size of torus.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthX
    ##   the length in X direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthX
          the length in X direction.  
             
         
        """
        pass
    
    ## Getter for property: (int) LinearSegments
    ##   the number of segments in linear direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def LinearSegments(self) -> int:
        """
        Getter for property: (int) LinearSegments
          the number of segments in linear direction.  
             
         
        """
        pass
    
    ## Setter for property: (int) LinearSegments

    ##   the number of segments in linear direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @LinearSegments.setter
    def LinearSegments(self, numSegments: int):
        """
        Setter for property: (int) LinearSegments
          the number of segments in linear direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
    ##   the origin.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
          the origin.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin

    ##   the origin.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
          the origin.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OuterSize
    ##   the outer size of torus.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OuterSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OuterSize
          the outer size of torus.  
             
         
        """
        pass
    
    ## Getter for property: (int) RadialSegments
    ##   the number of segments in radial direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def RadialSegments(self) -> int:
        """
        Getter for property: (int) RadialSegments
          the number of segments in radial direction.  
             
         
        """
        pass
    
    ## Setter for property: (int) RadialSegments

    ##   the number of segments in radial direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @RadialSegments.setter
    def RadialSegments(self, numSegments: int):
        """
        Setter for property: (int) RadialSegments
          the number of segments in radial direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Size
    ##   the size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Size(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Size
          the size.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel@endlink) SphereSubdivisionLevelOption
    ##   the subdivision level.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel
    @property
    def SphereSubdivisionLevelOption(self) -> SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel:
        """
        Getter for property: (@link SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel@endlink) SphereSubdivisionLevelOption
          the subdivision level.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel@endlink) SphereSubdivisionLevelOption

    ##   the subdivision level.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @SphereSubdivisionLevelOption.setter
    def SphereSubdivisionLevelOption(self, level: SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel):
        """
        Setter for property: (@link SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel@endlink) SphereSubdivisionLevelOption
          the subdivision level.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.Types@endlink) Type
    ##   the type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionPrimitiveShapeBuilderEx.Types
    @property
    def Type(self) -> SubdivisionPrimitiveShapeBuilderEx.Types:
        """
        Getter for property: (@link SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.Types@endlink) Type
          the type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.Types@endlink) Type

    ##   the type.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Type.setter
    def Type(self, type: SubdivisionPrimitiveShapeBuilderEx.Types):
        """
        Setter for property: (@link SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.Types@endlink) Type
          the type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WidthY
    ##   the width in Y direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def WidthY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WidthY
          the width in Y direction.  
             
         
        """
        pass
    
    ## Getter for property: (int) XSegments
    ##   the number of segments in X direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def XSegments(self) -> int:
        """
        Getter for property: (int) XSegments
          the number of segments in X direction.  
             
         
        """
        pass
    
    ## Setter for property: (int) XSegments

    ##   the number of segments in X direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @XSegments.setter
    def XSegments(self, numSegments: int):
        """
        Setter for property: (int) XSegments
          the number of segments in X direction.  
             
         
        """
        pass
    
    ## Getter for property: (int) YSegments
    ##   the number of segments in Y direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def YSegments(self) -> int:
        """
        Getter for property: (int) YSegments
          the number of segments in Y direction.  
             
         
        """
        pass
    
    ## Setter for property: (int) YSegments

    ##   the number of segments in Y direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @YSegments.setter
    def YSegments(self, numSegments: int):
        """
        Setter for property: (int) YSegments
          the number of segments in Y direction.  
             
         
        """
        pass
    
    ## Getter for property: (int) ZSegments
    ##   the number of segments in Z direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def ZSegments(self) -> int:
        """
        Getter for property: (int) ZSegments
          the number of segments in Z direction.  
             
         
        """
        pass
    
    ## Setter for property: (int) ZSegments

    ##   the number of segments in Z direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ZSegments.setter
    def ZSegments(self, numSegments: int):
        """
        Setter for property: (int) ZSegments
          the number of segments in Z direction.  
             
         
        """
        pass
    
    ##  Updates the mesh data after changes in the origin. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def UpdateMesh(builder: SubdivisionPrimitiveShapeBuilderEx) -> None:
        """
         Updates the mesh data after changes in the origin. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionPrimitiveShapeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CircularSegments </term> <description> 
##  
## 4 </description> </item> 
## 
## <item><term> 
##  
## Height.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## HeightZ.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InnerSize.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LengthX.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OuterSize.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RadialSegments </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## Size.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## WidthY.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

class SubdivisionPrimitiveShapeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder</ja_class> builder. """


    ##  Type of primitive. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sphere</term><description> 
    ## </description> </item><item><term> 
    ## Cylinder</term><description> 
    ## </description> </item><item><term> 
    ## Block</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Torus</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Sphere> <Cylinder> <Block> <Circle> <Rectangle> <Torus>
        """
        Sphere: int
        Cylinder: int
        Block: int
        Circle: int
        Rectangle: int
        Torus: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionPrimitiveShapeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) CircularSegments
    ##   the number of segments in circular sectional direction of torus.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return int
    @property
    def CircularSegments(self) -> int:
        """
        Getter for property: (int) CircularSegments
          the number of segments in circular sectional direction of torus.  
             
         
        """
        pass
    
    ## Setter for property: (int) CircularSegments

    ##   the number of segments in circular sectional direction of torus.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    @CircularSegments.setter
    def CircularSegments(self, numSegments: int):
        """
        Setter for property: (int) CircularSegments
          the number of segments in circular sectional direction of torus.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeightZ
    ##   the height in z direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def HeightZ(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HeightZ
          the height in z direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InnerSize
    ##   the inner size of torus.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def InnerSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InnerSize
          the inner size of torus.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthX
    ##   the length in x direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def LengthX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LengthX
          the length in x direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
    ##   the origin.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Point
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
          the origin.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin

    ##   the origin.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
          the origin.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OuterSize
    ##   the outer size of torus.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def OuterSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OuterSize
          the outer size of torus.  
             
         
        """
        pass
    
    ## Getter for property: (int) RadialSegments
    ##   the number of segments in radial direction of torus.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return int
    @property
    def RadialSegments(self) -> int:
        """
        Getter for property: (int) RadialSegments
          the number of segments in radial direction of torus.  
             
         
        """
        pass
    
    ## Setter for property: (int) RadialSegments

    ##   the number of segments in radial direction of torus.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    @RadialSegments.setter
    def RadialSegments(self, numSegments: int):
        """
        Setter for property: (int) RadialSegments
          the number of segments in radial direction of torus.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Size
    ##   the size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def Size(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Size
          the size.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##   the transformation tool.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
          the transformation tool.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionPrimitiveShapeBuilder.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder.Types@endlink) Type
    ##   the type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return SubdivisionPrimitiveShapeBuilder.Types
    @property
    def Type(self) -> SubdivisionPrimitiveShapeBuilder.Types:
        """
        Getter for property: (@link SubdivisionPrimitiveShapeBuilder.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder.Types@endlink) Type
          the type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionPrimitiveShapeBuilder.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder.Types@endlink) Type

    ##   the type.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    @Type.setter
    def Type(self, type: SubdivisionPrimitiveShapeBuilder.Types):
        """
        Setter for property: (@link SubdivisionPrimitiveShapeBuilder.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder.Types@endlink) Type
          the type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WidthY
    ##   the width in y direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## @return NXOpen.Expression
    @property
    def WidthY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) WidthY
          the width in y direction.  
             
         
        """
        pass
    
    ##  Updates the mesh data after changes in the origin. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx NXOpen::Features::Subdivision::SubdivisionPrimitiveShapeBuilderEx@endlink  instead.  <br> 

    ## License requirements: None.
    @staticmethod
    def UpdateMesh(builder: SubdivisionPrimitiveShapeBuilder) -> None:
        """
         Updates the mesh data after changes in the origin. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionProjectCageBuilderEx@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Mode </term> <description> 
##  
## Planar </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class SubdivisionProjectCageBuilderEx(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx</ja_class> builder """


    ##  Best fit mode 
    ##  Fit a line 
    class ModeOptions(Enum):
        """
        Members Include: <Linear> <Planar>
        """
        Linear: int
        Planar: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.ModeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type of projection direction. 
    ##  Along normal 
    class ProjectionDirectionTypes(Enum):
        """
        Members Include: <AlongNormal> <AlongVector>
        """
        AlongNormal: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Target types 
    ##  Plane inferred from selected cage objects 
    class TargetTypes(Enum):
        """
        Members Include: <InferredPlane> <InferredAxis> <DynamicPlane> <Plane> <Axis> <Curve> <Face>
        """
        InferredPlane: int
        InferredAxis: int
        DynamicPlane: int
        Plane: int
        Axis: int
        Curve: int
        Face: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.TargetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type of projection 
    ##  Project on target 
    class Types(Enum):
        """
        Members Include: <ToTarget> <ToAverage> <AlignNormal>
        """
        ToTarget: int
        ToAverage: int
        AlignNormal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilderEx.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ModeOptions@endlink) Mode
    ##   the mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SubdivisionProjectCageBuilderEx.ModeOptions
    @property
    def Mode(self) -> SubdivisionProjectCageBuilderEx.ModeOptions:
        """
        Getter for property: (@link SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ModeOptions@endlink) Mode
          the mode   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ModeOptions@endlink) Mode

    ##   the mode   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Mode.setter
    def Mode(self, mode: SubdivisionProjectCageBuilderEx.ModeOptions):
        """
        Setter for property: (@link SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ModeOptions@endlink) Mode
          the mode   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) ObjectsToProject
    ##   the objects to project   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def ObjectsToProject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) ObjectsToProject
          the objects to project   
            
         
        """
        pass
    
    ## Getter for property: (bool) ProjectBothSides
    ##   the flag indicating if projection should be done in both the sides of vector direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ProjectBothSides(self) -> bool:
        """
        Getter for property: (bool) ProjectBothSides
          the flag indicating if projection should be done in both the sides of vector direction.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ProjectBothSides

    ##   the flag indicating if projection should be done in both the sides of vector direction.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ProjectBothSides.setter
    def ProjectBothSides(self, projectBothSides: bool):
        """
        Setter for property: (bool) ProjectBothSides
          the flag indicating if projection should be done in both the sides of vector direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes@endlink) ProjectionDirectionType
    ##   the type of projection on faces and facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes
    @property
    def ProjectionDirectionType(self) -> SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes:
        """
        Getter for property: (@link SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes@endlink) ProjectionDirectionType
          the type of projection on faces and facet body   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes@endlink) ProjectionDirectionType

    ##   the type of projection on faces and facet body   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ProjectionDirectionType.setter
    def ProjectionDirectionType(self, type: SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes):
        """
        Setter for property: (@link SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes@endlink) ProjectionDirectionType
          the type of projection on faces and facet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
    ##   the projection direction vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ProjectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
          the projection direction vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector

    ##   the projection direction vector   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ProjectionVector.setter
    def ProjectionVector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
          the projection direction vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TargetAxis
    ##   the target axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Axis
    @property
    def TargetAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TargetAxis
          the target axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TargetAxis

    ##   the target axis   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TargetAxis.setter
    def TargetAxis(self, axis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) TargetAxis
          the target axis   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetCageObjects
    ##   the target cage objects to infer a plane or axis from   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def TargetCageObjects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetCageObjects
          the target cage objects to infer a plane or axis from   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) TargetCurves
    ##   the target curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def TargetCurves(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) TargetCurves
          the target curves   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane
    ##   the target dynamic plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def TargetDynamicPlane(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane
          the target dynamic plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane

    ##   the target dynamic plane   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TargetDynamicPlane.setter
    def TargetDynamicPlane(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane
          the target dynamic plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) TargetFaces
    ##   the target faces or facet body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def TargetFaces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) TargetFaces
          the target faces or facet body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane
    ##   the target plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def TargetPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane
          the target plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane

    ##   the target plane   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TargetPlane.setter
    def TargetPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane
          the target plane   
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.TargetTypes@endlink) TargetType
    ##   the target type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SubdivisionProjectCageBuilderEx.TargetTypes
    @property
    def TargetType(self) -> SubdivisionProjectCageBuilderEx.TargetTypes:
        """
        Getter for property: (@link SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.TargetTypes@endlink) TargetType
          the target type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.TargetTypes@endlink) TargetType

    ##   the target type   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TargetType.setter
    def TargetType(self, targetType: SubdivisionProjectCageBuilderEx.TargetTypes):
        """
        Setter for property: (@link SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.TargetTypes@endlink) TargetType
          the target type   
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionProjectCageBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.Types@endlink) Type
    ##   the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SubdivisionProjectCageBuilderEx.Types
    @property
    def Type(self) -> SubdivisionProjectCageBuilderEx.Types:
        """
        Getter for property: (@link SubdivisionProjectCageBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.Types@endlink) Type

    ##   the type   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Type.setter
    def Type(self, type: SubdivisionProjectCageBuilderEx.Types):
        """
        Setter for property: (@link SubdivisionProjectCageBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ##  Update builder data based on target axis definition 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def OnTargetAxis(builder: SubdivisionProjectCageBuilderEx) -> None:
        """
         Update builder data based on target axis definition 
        """
        pass
    
    ##  Update builder data based on target dynamic plane definition 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def OnTargetDynamicPlane(builder: SubdivisionProjectCageBuilderEx) -> None:
        """
         Update builder data based on target dynamic plane definition 
        """
        pass
    
    ##  Update builder data based on target plane definition 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def OnTargetPlane(builder: SubdivisionProjectCageBuilderEx) -> None:
        """
         Update builder data based on target plane definition 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionProjectCageBuilder NXOpen::Features::Subdivision::SubdivisionProjectCageBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Mode </term> <description> 
##  
## Planar </description> </item> 
## 
## <item><term> 
##  
## TargetType </term> <description> 
##  
## InferredPlane </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

class SubdivisionProjectCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder</ja_class> builder """


    ##  Best fit mode 
    ##  Fit a line 
    class ModeOptions(Enum):
        """
        Members Include: <Linear> <Planar>
        """
        Linear: int
        Planar: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilder.ModeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Target types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InferredPlane</term><description> 
    ## </description> </item><item><term> 
    ## InferredAxis</term><description> 
    ## </description> </item><item><term> 
    ## YcZcPlane</term><description> 
    ## </description> </item><item><term> 
    ## XcZcPlane</term><description> 
    ## </description> </item><item><term> 
    ## XcYcPlane</term><description> 
    ## </description> </item><item><term> 
    ## XcAxis</term><description> 
    ## </description> </item><item><term> 
    ## YcAxis</term><description> 
    ## </description> </item><item><term> 
    ## ZcAxis</term><description> 
    ## </description> </item><item><term> 
    ## Object</term><description> 
    ## </description> </item><item><term> 
    ## Plane</term><description> 
    ## </description> </item><item><term> 
    ## DynamicPlane</term><description> 
    ## </description> </item></list>
    class TargetTypes(Enum):
        """
        Members Include: <InferredPlane> <InferredAxis> <YcZcPlane> <XcZcPlane> <XcYcPlane> <XcAxis> <YcAxis> <ZcAxis> <Object> <Plane> <DynamicPlane>
        """
        InferredPlane: int
        InferredAxis: int
        YcZcPlane: int
        XcZcPlane: int
        XcYcPlane: int
        XcAxis: int
        YcAxis: int
        ZcAxis: int
        Object: int
        Plane: int
        DynamicPlane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilder.TargetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The type of projection 
    ##  Project on target 
    class Types(Enum):
        """
        Members Include: <ToTarget> <ToAverage> <AlignNormal>
        """
        ToTarget: int
        ToAverage: int
        AlignNormal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionProjectCageBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SubdivisionProjectCageBuilder.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.ModeOptions@endlink) Mode
    ##   the mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return SubdivisionProjectCageBuilder.ModeOptions
    @property
    def Mode(self) -> SubdivisionProjectCageBuilder.ModeOptions:
        """
        Getter for property: (@link SubdivisionProjectCageBuilder.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.ModeOptions@endlink) Mode
          the mode   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilder.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.ModeOptions@endlink) Mode

    ##   the mode   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    @Mode.setter
    def Mode(self, mode: SubdivisionProjectCageBuilder.ModeOptions):
        """
        Setter for property: (@link SubdivisionProjectCageBuilder.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.ModeOptions@endlink) Mode
          the mode   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) ObjectsToProject
    ##   the objects to project   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return SelectCageObjectData
    @property
    def ObjectsToProject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) ObjectsToProject
          the objects to project   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) Target
    ##   the target   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def Target(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) Target
          the target   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetCageObjects
    ##   the target cage objects to infer a plane or axis from   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return SelectCageObjectData
    @property
    def TargetCageObjects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetCageObjects
          the target cage objects to infer a plane or axis from   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane
    ##   the target dynamic plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def TargetDynamicPlane(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane
          the target dynamic plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane

    ##   the target dynamic plane   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    @TargetDynamicPlane.setter
    def TargetDynamicPlane(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) TargetDynamicPlane
          the target dynamic plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane
    ##   the target plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return NXOpen.Plane
    @property
    def TargetPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane
          the target plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane

    ##   the target plane   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX9.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    @TargetPlane.setter
    def TargetPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) TargetPlane
          the target plane   
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionProjectCageBuilder.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.TargetTypes@endlink) TargetType
    ##   the target type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return SubdivisionProjectCageBuilder.TargetTypes
    @property
    def TargetType(self) -> SubdivisionProjectCageBuilder.TargetTypes:
        """
        Getter for property: (@link SubdivisionProjectCageBuilder.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.TargetTypes@endlink) TargetType
          the target type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilder.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.TargetTypes@endlink) TargetType

    ##   the target type   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    @TargetType.setter
    def TargetType(self, targetType: SubdivisionProjectCageBuilder.TargetTypes):
        """
        Setter for property: (@link SubdivisionProjectCageBuilder.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.TargetTypes@endlink) TargetType
          the target type   
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionProjectCageBuilder.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.Types@endlink) Type
    ##   the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## @return SubdivisionProjectCageBuilder.Types
    @property
    def Type(self) -> SubdivisionProjectCageBuilder.Types:
        """
        Getter for property: (@link SubdivisionProjectCageBuilder.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionProjectCageBuilder.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.Types@endlink) Type

    ##   the type   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    @Type.setter
    def Type(self, type: SubdivisionProjectCageBuilder.Types):
        """
        Setter for property: (@link SubdivisionProjectCageBuilder.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ##  Update builder data based on target dynamic plane definition 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def OnTargetDynamicPlane(builder: SubdivisionProjectCageBuilder) -> None:
        """
         Update builder data based on target dynamic plane definition 
        """
        pass
    
    ##  Update builder data based on target plane definition 
    ## 
    ##   <br>  Created in NX9.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionProjectCageBuilderEx@endlink  instead  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def OnTargetPlane(builder: SubdivisionProjectCageBuilder) -> None:
        """
         Update builder data based on target plane definition 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionRevolveBuilder NXOpen::Features::Subdivision::SubdivisionRevolveBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionRevolveBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionRevolveBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanSew </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## EndAngle.Value </term> <description> 
##  
## 360 </description> </item> 
## 
## <item><term> 
##  
## NumOfSegments </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## StartAngle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class SubdivisionRevolveBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionRevolveBuilder</ja_class> builder. """


    ##  Type of continuity. 
    ##  Smooth continuity 
    class ContinuityType(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionRevolveBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) AxisPoint
    ##   the origin of the axis of revolution.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def AxisPoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) AxisPoint
          the origin of the axis of revolution.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##   the axis of revolution.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
          the axis of revolution.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##   the axis of revolution.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
          the axis of revolution.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanSew
    ##   the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanSew(self) -> bool:
        """
        Getter for property: (bool) CanSew
          the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    
    ## Setter for property: (bool) CanSew

    ##   the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanSew.setter
    def CanSew(self, canSew: bool):
        """
        Setter for property: (bool) CanSew
          the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionRevolveBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionRevolveBuilder.ContinuityType@endlink) Continuity
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 of the revolved region that are sewn with the primary existing region.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionRevolveBuilder.ContinuityType
    @property
    def Continuity(self) -> SubdivisionRevolveBuilder.ContinuityType:
        """
        Getter for property: (@link SubdivisionRevolveBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionRevolveBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the revolved region that are sewn with the primary existing region.   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionRevolveBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionRevolveBuilder.ContinuityType@endlink) Continuity

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 of the revolved region that are sewn with the primary existing region.   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Continuity.setter
    def Continuity(self, continuity: SubdivisionRevolveBuilder.ContinuityType):
        """
        Setter for property: (@link SubdivisionRevolveBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionRevolveBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the revolved region that are sewn with the primary existing region.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndAngle
    ##   the end of angular dimension.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndAngle
          the end of angular dimension.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumOfSegments
    ##   the number of segments.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumOfSegments(self) -> int:
        """
        Getter for property: (int) NumOfSegments
          the number of segments.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumOfSegments

    ##   the number of segments.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumOfSegments.setter
    def NumOfSegments(self, numOfSegments: int):
        """
        Setter for property: (int) NumOfSegments
          the number of segments.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SectionObject
    ##   the section as revolving profile.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def SectionObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SectionObject
          the section as revolving profile.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartAngle
    ##   the start of angular dimension.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartAngle
          the start of angular dimension.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder NXOpen::Features::Subdivision::SubdivisionSetContinuityBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSetContinuityBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSetContinuityBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ContinuityType </term> <description> 
##  
## Smooth </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionSetContinuityBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder</ja_class> builder.  """


    ##  Represents the continuity type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Smooth</term><description> 
    ## </description> </item><item><term> 
    ## Sharp</term><description> 
    ## </description> </item></list>
    class ContinuityTypes(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSetContinuityBuilder.ContinuityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder.ContinuityTypes@endlink) ContinuityType
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SubdivisionSetContinuityBuilder.ContinuityTypes
    @property
    def ContinuityType(self) -> SubdivisionSetContinuityBuilder.ContinuityTypes:
        """
        Getter for property: (@link SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder.ContinuityTypes@endlink) ContinuityType
          the continuity.  
           The continuity is used to specify creases in the limit surface.   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder.ContinuityTypes@endlink) ContinuityType

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface.   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ContinuityType.setter
    def ContinuityType(self, continuityType: SubdivisionSetContinuityBuilder.ContinuityTypes):
        """
        Setter for property: (@link SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder.ContinuityTypes@endlink) ContinuityType
          the continuity.  
           The continuity is used to specify creases in the limit surface.   
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetObject
    ##   the target object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def TargetObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetObject
          the target object.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionSetWeightBuilder NXOpen::Features::Subdivision::SubdivisionSetWeightBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSetWeightBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSetWeightBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## WeightPercent </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionSetWeightBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetObject
    ##   the target object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def TargetObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) TargetObject
          the target object.  
             
         
        """
        pass
    
    ## Getter for property: (int) WeightPercent
    ##   the value indicating percentage weight.  
    ##    Weight defines attraction of the limit surface towards cage topology.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def WeightPercent(self) -> int:
        """
        Getter for property: (int) WeightPercent
          the value indicating percentage weight.  
           Weight defines attraction of the limit surface towards cage topology.   
         
        """
        pass
    
    ## Setter for property: (int) WeightPercent

    ##   the value indicating percentage weight.  
    ##    Weight defines attraction of the limit surface towards cage topology.   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @WeightPercent.setter
    def WeightPercent(self, weightPercent: int):
        """
        Setter for property: (int) WeightPercent
          the value indicating percentage weight.  
           Weight defines attraction of the limit surface towards cage topology.   
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionSewCageBuilder NXOpen::Features::Subdivision::SubdivisionSewCageBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSewCageBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSewCageBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SubdivisionSewCageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionSewCageBuilder</ja_class> builder """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectedEdges1
    ##   the first set of edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def SelectedEdges1(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectedEdges1
          the first set of edges   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectedEdges2
    ##   the second set of edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def SelectedEdges2(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) SelectedEdges2
          the second set of edges   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionSplitFaceBuilder NXOpen::Features::Subdivision::SubdivisionSplitFaceBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSplitFaceBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSplitFaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionSplitFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder</ja_class> builder. """


    ##  Represents the split type. 
    ##  Uniform split type. 
    class Types(Enum):
        """
        Members Include: <Uniform> <ThroughLines>
        """
        Uniform: int
        ThroughLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSplitFaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FacesToSplit
    ##   the faces to split.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def FacesToSplit(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FacesToSplit
          the faces to split.  
             
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   the desired split number in one face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          the desired split number in one face.  
             
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   the desired split number in one face.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          the desired split number in one face.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) ReferenceEdge
    ##   the reference edges.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def ReferenceEdge(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) ReferenceEdge
          the reference edges.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionSplitFaceBuilder.Types NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder.Types@endlink) Type
    ##   the split type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SubdivisionSplitFaceBuilder.Types
    @property
    def Type(self) -> SubdivisionSplitFaceBuilder.Types:
        """
        Getter for property: (@link SubdivisionSplitFaceBuilder.Types NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder.Types@endlink) Type
          the split type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionSplitFaceBuilder.Types NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder.Types@endlink) Type

    ##   the split type.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Type.setter
    def Type(self, type: SubdivisionSplitFaceBuilder.Types):
        """
        Setter for property: (@link SubdivisionSplitFaceBuilder.Types NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder.Types@endlink) Type
          the split type.  
             
         
        """
        pass
    
    ##  Add split face point. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ##  the loction on the object to split face. 
    def AddSplitPoint(builder: SubdivisionSplitFaceBuilder, location: NXOpen.Point3d, objectValue: NXOpen.DisplayableObject) -> None:
        """
         Add split face point. 
        """
        pass
    
    ##  Clear split face point. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def ClearSplitPoints(builder: SubdivisionSplitFaceBuilder) -> None:
        """
         Clear split face point. 
        """
        pass
    
    ##  Update split positions. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    ##  index to indicate which split line to update positions from. 
    def UpdateSplitPositions(builder: SubdivisionSplitFaceBuilder, splitLineIndex: int, positions: List[NXOpen.Point3d]) -> None:
        """
         Update split positions. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionSubdivideFaceBuilder NXOpen::Features::Subdivision::SubdivisionSubdivideFaceBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSubdivideFaceBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSubdivideFaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SubdivisionSubdivideFaceBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder</ja_class> builder.  """


    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FacesToSubdivide
    ##   the faces to subdivide.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def FacesToSubdivide(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FacesToSubdivide
          the faces to subdivide.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
    ##   the scale factor.  
    ##    The value is from 0 to 100. 0 refers to the original size of the face, 100 refers to the center of the face.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Scale
          the scale factor.  
           The value is from 0 to 100. 0 refers to the original size of the face, 100 refers to the center of the face.   
         
        """
        pass
    
    ##  Perform subdivide operation. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION") OR nx_polygon_modeling (" NX Polygon Modeling")
    @staticmethod
    def Subdivide(builder: SubdivisionSubdivideFaceBuilder) -> None:
        """
         Perform subdivide operation. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionSweepBuilder NXOpen::Features::Subdivision::SubdivisionSweepBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSweepBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionSweepBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanSew </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class SubdivisionSweepBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionSweepBuilder</ja_class> builder. """


    ##  Type of continuity. 
    ##  Smooth continuity 
    class ContinuityType(Enum):
        """
        Members Include: <Smooth> <Sharp>
        """
        Smooth: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionSweepBuilder.ContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanSew
    ##   the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanSew(self) -> bool:
        """
        Getter for property: (bool) CanSew
          the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    
    ## Setter for property: (bool) CanSew

    ##   the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanSew.setter
    def CanSew(self, canSew: bool):
        """
        Setter for property: (bool) CanSew
          the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionSweepBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionSweepBuilder.ContinuityType@endlink) Continuity
    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 of the swept region that are sewn with the primary existing region.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SubdivisionSweepBuilder.ContinuityType
    @property
    def Continuity(self) -> SubdivisionSweepBuilder.ContinuityType:
        """
        Getter for property: (@link SubdivisionSweepBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionSweepBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the swept region that are sewn with the primary existing region.   
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionSweepBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionSweepBuilder.ContinuityType@endlink) Continuity

    ##   the continuity.  
    ##    The continuity is used to specify creases in the limit surface corresponding to edges
    ##                 of the swept region that are sewn with the primary existing region.   
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Continuity.setter
    def Continuity(self, continuity: SubdivisionSweepBuilder.ContinuityType):
        """
        Setter for property: (@link SubdivisionSweepBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionSweepBuilder.ContinuityType@endlink) Continuity
          the continuity.  
           The continuity is used to specify creases in the limit surface corresponding to edges
                        of the swept region that are sewn with the primary existing region.   
         
        """
        pass
    
    ## Getter for property: (@link CageSectionDataList NXOpen.Features.Subdivision.CageSectionDataList@endlink) Guides
    ##   the guide objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CageSectionDataList
    @property
    def Guides(self) -> CageSectionDataList:
        """
        Getter for property: (@link CageSectionDataList NXOpen.Features.Subdivision.CageSectionDataList@endlink) Guides
          the guide objects.  
             
         
        """
        pass
    
    ## Getter for property: (@link CageSectionDataList NXOpen.Features.Subdivision.CageSectionDataList@endlink) Sections
    ##   the section objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CageSectionDataList
    @property
    def Sections(self) -> CageSectionDataList:
        """
        Getter for property: (@link CageSectionDataList NXOpen.Features.Subdivision.CageSectionDataList@endlink) Sections
          the section objects.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::SubdivisionTubeBuilder NXOpen::Features::Subdivision::SubdivisionTubeBuilder@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionTubeBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionTubeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CrossSection </term> <description> 
##  
## 4 </description> </item> 
## 
## <item><term> 
##  
## FalloffDistance.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## NodeSize.Value </term> <description> 
##  
## 2 (millimeters part), 0.08 (inches part) </description> </item> 
## 
## <item><term> 
##  
## NumberOfSegments </term> <description> 
##  
## 4 </description> </item> 
## 
## <item><term> 
##  
## Rod </term> <description> 
##  
## 3 </description> </item> 
## 
## <item><term> 
##  
## RodSize.Value </term> <description> 
##  
## 1 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Size.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class SubdivisionTubeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.SubdivisionTubeBuilder</ja_class> builder. """


    ##  End capping type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Flat</term><description> 
    ## </description> </item><item><term> 
    ## Round</term><description> 
    ## </description> </item></list>
    class EndCapsType(Enum):
        """
        Members Include: <NotSet> <Flat> <Round>
        """
        NotSet: int
        Flat: int
        Round: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionTubeBuilder.EndCapsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Tube Cage creation types 
    ##  Single Path 
    class Types(Enum):
        """
        Members Include: <SinglePath> <BranchedPath>
        """
        SinglePath: int
        BranchedPath: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SubdivisionTubeBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) CrossSection
    ##   the cross section   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def CrossSection(self) -> int:
        """
        Getter for property: (int) CrossSection
          the cross section   
            
         
        """
        pass
    
    ## Setter for property: (int) CrossSection

    ##   the cross section   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @CrossSection.setter
    def CrossSection(self, crossSection: int):
        """
        Setter for property: (int) CrossSection
          the cross section   
            
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionTubeBuilder.EndCapsType NXOpen.Features.Subdivision.SubdivisionTubeBuilder.EndCapsType@endlink) EndCaps
    ##   the end capping type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return SubdivisionTubeBuilder.EndCapsType
    @property
    def EndCaps(self) -> SubdivisionTubeBuilder.EndCapsType:
        """
        Getter for property: (@link SubdivisionTubeBuilder.EndCapsType NXOpen.Features.Subdivision.SubdivisionTubeBuilder.EndCapsType@endlink) EndCaps
          the end capping type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionTubeBuilder.EndCapsType NXOpen.Features.Subdivision.SubdivisionTubeBuilder.EndCapsType@endlink) EndCaps

    ##   the end capping type   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @EndCaps.setter
    def EndCaps(self, endCaps: SubdivisionTubeBuilder.EndCapsType):
        """
        Setter for property: (@link SubdivisionTubeBuilder.EndCapsType NXOpen.Features.Subdivision.SubdivisionTubeBuilder.EndCapsType@endlink) EndCaps
          the end capping type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FalloffDistance
    ##   the falloff distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FalloffDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FalloffDistance
          the falloff distance   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) GraphStructureObject
    ##   the object as branched path of tube.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def GraphStructureObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) GraphStructureObject
          the object as branched path of tube.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NodeSize
    ##   the node size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NodeSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NodeSize
          the node size   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfSegments
    ##   the number of segments.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
          the number of segments.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfSegments

    ##   the number of segments.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
          the number of segments.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) PathObject
    ##   the object as path of tube.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def PathObject(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) PathObject
          the object as path of tube.  
             
         
        """
        pass
    
    ## Getter for property: (int) Rod
    ##   the rod   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def Rod(self) -> int:
        """
        Getter for property: (int) Rod
          the rod   
            
         
        """
        pass
    
    ## Setter for property: (int) Rod

    ##   the rod   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Rod.setter
    def Rod(self, rod: int):
        """
        Setter for property: (int) Rod
          the rod   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodSize
    ##   the rod size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RodSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodSize
          the rod size   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Size
    ##   the size of tube in cross section.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Size(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Size
          the size of tube in cross section.  
             
         
        """
        pass
    
    ## Getter for property: (@link SubdivisionTubeBuilder.Types NXOpen.Features.Subdivision.SubdivisionTubeBuilder.Types@endlink) Type
    ##   the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return SubdivisionTubeBuilder.Types
    @property
    def Type(self) -> SubdivisionTubeBuilder.Types:
        """
        Getter for property: (@link SubdivisionTubeBuilder.Types NXOpen.Features.Subdivision.SubdivisionTubeBuilder.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ## Setter for property: (@link SubdivisionTubeBuilder.Types NXOpen.Features.Subdivision.SubdivisionTubeBuilder.Types@endlink) Type

    ##   the type   
    ##     
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Type.setter
    def Type(self, type: SubdivisionTubeBuilder.Types):
        """
        Setter for property: (@link SubdivisionTubeBuilder.Types NXOpen.Features.Subdivision.SubdivisionTubeBuilder.Types@endlink) Type
          the type   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Features::Subdivision::TransformCageData NXOpen::Features::Subdivision::TransformCageData@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateTransformCageData  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateTransformCageData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanRelocateToolToSelection </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## CanReorientToolToSelection </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class TransformCageData(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Features.Subdivision.TransformCageData</ja_class> builder. """


    ##  Falloff method types 
    ##  No falloff 
    class FallOffMethodType(Enum):
        """
        Members Include: <NotSet> <Selected> <All>
        """
        NotSet: int
        Selected: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.FallOffMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Movement types 
    ##  Movement along WCS principal axis or plane 
    class MovementMethodType(Enum):
        """
        Members Include: <WCS> <View> <Vector> <Plane> <Normal> <Edge>
        """
        WCS: int
        View: int
        Vector: int
        Plane: int
        Normal: int
        Edge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.MovementMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Scaling method 
    ##  Scale in the specified direction 
    class ScalingMethodType(Enum):
        """
        Members Include: <Linear> <Planar> <Uniform>
        """
        Linear: int
        Planar: int
        Uniform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Transformation method types 
    ##  Edit cage topology by direct dragging 
    class TransformationMethodType(Enum):
        """
        Members Include: <Drag> <Transform>
        """
        Drag: int
        Transform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.TransformationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  WCS principal axis or plane types 
    ##  Along axis inferred during movement 
    class WCSOptionType(Enum):
        """
        Members Include: <InferredAxis> <X> <Y> <Z> <YZ> <XZ> <XY>
        """
        InferredAxis: int
        X: int
        Y: int
        Z: int
        YZ: int
        XZ: int
        XY: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformCageData.WCSOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CageManipulatorData NXOpen.Features.Subdivision.CageManipulatorData@endlink) CageManipulator
    ##   the cage manipulation data.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return CageManipulatorData
    @property
    def CageManipulator(self) -> CageManipulatorData:
        """
        Getter for property: (@link CageManipulatorData NXOpen.Features.Subdivision.CageManipulatorData@endlink) CageManipulator
          the cage manipulation data.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanMoveToolOnly
    ##   the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
          the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanMoveToolOnly

    ##   the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMove: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
          the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanRelocateToolToSelection
    ##   the flag indicating if transformer tool can be relocated based on cage topology selection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
          the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanRelocateToolToSelection

    ##   the flag indicating if transformer tool can be relocated based on cage topology selection.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocate: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
          the flag indicating if transformer tool can be relocated based on cage topology selection.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CanReorientToolToSelection
    ##   the flag indicating if transformer tool can be reoriented based on cage topology selection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
          the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanReorientToolToSelection

    ##   the flag indicating if transformer tool can be reoriented based on cage topology selection.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorient: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
          the flag indicating if transformer tool can be reoriented based on cage topology selection.  
             
         
        """
        pass
    
    ## Getter for property: (float) FallOffFactor
    ##   the falloff factor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def FallOffFactor(self) -> float:
        """
        Getter for property: (float) FallOffFactor
          the falloff factor.  
             
         
        """
        pass
    
    ## Setter for property: (float) FallOffFactor

    ##   the falloff factor.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FallOffFactor.setter
    def FallOffFactor(self, factor: float):
        """
        Setter for property: (float) FallOffFactor
          the falloff factor.  
             
         
        """
        pass
    
    ## Getter for property: (@link TransformCageData.FallOffMethodType NXOpen.Features.Subdivision.TransformCageData.FallOffMethodType@endlink) FallOffMethod
    ##   the falloff method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return TransformCageData.FallOffMethodType
    @property
    def FallOffMethod(self) -> TransformCageData.FallOffMethodType:
        """
        Getter for property: (@link TransformCageData.FallOffMethodType NXOpen.Features.Subdivision.TransformCageData.FallOffMethodType@endlink) FallOffMethod
          the falloff method.  
             
         
        """
        pass
    
    ## Setter for property: (@link TransformCageData.FallOffMethodType NXOpen.Features.Subdivision.TransformCageData.FallOffMethodType@endlink) FallOffMethod

    ##   the falloff method.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FallOffMethod.setter
    def FallOffMethod(self, fallOffMethod: TransformCageData.FallOffMethodType):
        """
        Setter for property: (@link TransformCageData.FallOffMethodType NXOpen.Features.Subdivision.TransformCageData.FallOffMethodType@endlink) FallOffMethod
          the falloff method.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FallOffObjects
    ##   the falloff objects.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SelectCageObjectData
    @property
    def FallOffObjects(self) -> SelectCageObjectData:
        """
        Getter for property: (@link SelectCageObjectData NXOpen.Features.Subdivision.SelectCageObjectData@endlink) FallOffObjects
          the falloff objects.  
             
         
        """
        pass
    
    ## Getter for property: (@link TransformCageData.MovementMethodType NXOpen.Features.Subdivision.TransformCageData.MovementMethodType@endlink) MovementMethod
    ##   the movement method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TransformCageData.MovementMethodType
    @property
    def MovementMethod(self) -> TransformCageData.MovementMethodType:
        """
        Getter for property: (@link TransformCageData.MovementMethodType NXOpen.Features.Subdivision.TransformCageData.MovementMethodType@endlink) MovementMethod
          the movement method.  
             
         
        """
        pass
    
    ## Setter for property: (@link TransformCageData.MovementMethodType NXOpen.Features.Subdivision.TransformCageData.MovementMethodType@endlink) MovementMethod

    ##   the movement method.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MovementMethod.setter
    def MovementMethod(self, movementMethod: TransformCageData.MovementMethodType):
        """
        Setter for property: (@link TransformCageData.MovementMethodType NXOpen.Features.Subdivision.TransformCageData.MovementMethodType@endlink) MovementMethod
          the movement method.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MovementPlane
    ##   the movement plane.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def MovementPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MovementPlane
          the movement plane.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MovementPlane

    ##   the movement plane.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MovementPlane.setter
    def MovementPlane(self, movementPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) MovementPlane
          the movement plane.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovementVector
    ##   the movement vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def MovementVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovementVector
          the movement vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovementVector

    ##   the movement vector.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MovementVector.setter
    def MovementVector(self, movementVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovementVector
          the movement vector.  
             
         
        """
        pass
    
    ## Getter for property: (@link TransformCageData.ScalingMethodType NXOpen.Features.Subdivision.TransformCageData.ScalingMethodType@endlink) ScalingMethod
    ##   the scaling method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TransformCageData.ScalingMethodType
    @property
    def ScalingMethod(self) -> TransformCageData.ScalingMethodType:
        """
        Getter for property: (@link TransformCageData.ScalingMethodType NXOpen.Features.Subdivision.TransformCageData.ScalingMethodType@endlink) ScalingMethod
          the scaling method.  
             
         
        """
        pass
    
    ## Setter for property: (@link TransformCageData.ScalingMethodType NXOpen.Features.Subdivision.TransformCageData.ScalingMethodType@endlink) ScalingMethod

    ##   the scaling method.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: TransformCageData.ScalingMethodType):
        """
        Setter for property: (@link TransformCageData.ScalingMethodType NXOpen.Features.Subdivision.TransformCageData.ScalingMethodType@endlink) ScalingMethod
          the scaling method.  
             
         
        """
        pass
    
    ## Getter for property: (@link TransformCageData.TransformationMethodType NXOpen.Features.Subdivision.TransformCageData.TransformationMethodType@endlink) TransformationMethod
    ##   the transformation method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TransformCageData.TransformationMethodType
    @property
    def TransformationMethod(self) -> TransformCageData.TransformationMethodType:
        """
        Getter for property: (@link TransformCageData.TransformationMethodType NXOpen.Features.Subdivision.TransformCageData.TransformationMethodType@endlink) TransformationMethod
          the transformation method.  
             
         
        """
        pass
    
    ## Setter for property: (@link TransformCageData.TransformationMethodType NXOpen.Features.Subdivision.TransformCageData.TransformationMethodType@endlink) TransformationMethod

    ##   the transformation method.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TransformationMethod.setter
    def TransformationMethod(self, method: TransformCageData.TransformationMethodType):
        """
        Setter for property: (@link TransformCageData.TransformationMethodType NXOpen.Features.Subdivision.TransformCageData.TransformationMethodType@endlink) TransformationMethod
          the transformation method.  
             
         
        """
        pass
    
    ## Getter for property: (@link TransformCageData.WCSOptionType NXOpen.Features.Subdivision.TransformCageData.WCSOptionType@endlink) WCSOption
    ##   the WCS option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TransformCageData.WCSOptionType
    @property
    def WCSOption(self) -> TransformCageData.WCSOptionType:
        """
        Getter for property: (@link TransformCageData.WCSOptionType NXOpen.Features.Subdivision.TransformCageData.WCSOptionType@endlink) WCSOption
          the WCS option.  
             
         
        """
        pass
    
    ## Setter for property: (@link TransformCageData.WCSOptionType NXOpen.Features.Subdivision.TransformCageData.WCSOptionType@endlink) WCSOption

    ##   the WCS option.  
    ##      
    ##  
    ## Setter License requirements: nx_subdivision (" NX SUBDIVISION")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @WCSOption.setter
    def WCSOption(self, wcsOption: TransformCageData.WCSOptionType):
        """
        Setter for property: (@link TransformCageData.WCSOptionType NXOpen.Features.Subdivision.TransformCageData.WCSOptionType@endlink) WCSOption
          the WCS option.  
             
         
        """
        pass
    
    ##  Resets the falloff scale to linear. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_subdivision (" NX SUBDIVISION")
    @staticmethod
    def ResetFallOffToLinear(builder: TransformCageData) -> None:
        """
         Resets the falloff scale to linear. 
        """
        pass
    
## @package NXOpen.Features.Subdivision
## Classes, Enums and Structs under NXOpen.Features.Subdivision namespace

## @link CageManipulatorDataObjectMoveData_Struct NXOpen.Features.Subdivision.CageManipulatorDataObjectMoveData_Struct@endlink is an alias for @link CageManipulatorData.ObjectMoveData NXOpen.Features.Subdivision.CageManipulatorData.ObjectMoveData@endlink.
CageManipulatorDataObjectMoveData_Struct = CageManipulatorData.ObjectMoveData


## @link CageManipulatorDataObjectSelectionData_Struct NXOpen.Features.Subdivision.CageManipulatorDataObjectSelectionData_Struct@endlink is an alias for @link CageManipulatorData.ObjectSelectionData NXOpen.Features.Subdivision.CageManipulatorData.ObjectSelectionData@endlink.
CageManipulatorDataObjectSelectionData_Struct = CageManipulatorData.ObjectSelectionData


##  @link DefineWorkRegionBuilderFrozenRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilderFrozenRegionDefinitionMethods @endlink is an alias for @link DefineWorkRegionBuilder.FrozenRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.FrozenRegionDefinitionMethods@endlink
DefineWorkRegionBuilderFrozenRegionDefinitionMethods = DefineWorkRegionBuilder.FrozenRegionDefinitionMethods


##  @link DefineWorkRegionBuilderWorkRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilderWorkRegionDefinitionMethods @endlink is an alias for @link DefineWorkRegionBuilder.WorkRegionDefinitionMethods NXOpen.Features.Subdivision.DefineWorkRegionBuilder.WorkRegionDefinitionMethods@endlink
DefineWorkRegionBuilderWorkRegionDefinitionMethods = DefineWorkRegionBuilder.WorkRegionDefinitionMethods


##  @link DrawCageDataFaceShapeType NXOpen.Features.Subdivision.DrawCageDataFaceShapeType @endlink is an alias for @link DrawCageData.FaceShapeType NXOpen.Features.Subdivision.DrawCageData.FaceShapeType@endlink
DrawCageDataFaceShapeType = DrawCageData.FaceShapeType


## @link DrawCageDataSelectionData_Struct NXOpen.Features.Subdivision.DrawCageDataSelectionData_Struct@endlink is an alias for @link DrawCageData.SelectionData NXOpen.Features.Subdivision.DrawCageData.SelectionData@endlink.
DrawCageDataSelectionData_Struct = DrawCageData.SelectionData


##  @link ExtractCagePolylineBuilderInputCurveOption NXOpen.Features.Subdivision.ExtractCagePolylineBuilderInputCurveOption @endlink is an alias for @link ExtractCagePolylineBuilder.InputCurveOption NXOpen.Features.Subdivision.ExtractCagePolylineBuilder.InputCurveOption@endlink
ExtractCagePolylineBuilderInputCurveOption = ExtractCagePolylineBuilder.InputCurveOption


##  @link MergeSubdivisionBodiesBuilderInputBodyOptions NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilderInputBodyOptions @endlink is an alias for @link MergeSubdivisionBodiesBuilder.InputBodyOptions NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder.InputBodyOptions@endlink
MergeSubdivisionBodiesBuilderInputBodyOptions = MergeSubdivisionBodiesBuilder.InputBodyOptions


## @link SectionTubeDataSelectionData_Struct NXOpen.Features.Subdivision.SectionTubeDataSelectionData_Struct@endlink is an alias for @link SectionTubeData.SelectionData NXOpen.Features.Subdivision.SectionTubeData.SelectionData@endlink.
SectionTubeDataSelectionData_Struct = SectionTubeData.SelectionData


##  @link SplitSubdivisionBodyBuilderInputBodyOptions NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilderInputBodyOptions @endlink is an alias for @link SplitSubdivisionBodyBuilder.InputBodyOptions NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder.InputBodyOptions@endlink
SplitSubdivisionBodyBuilderInputBodyOptions = SplitSubdivisionBodyBuilder.InputBodyOptions


##  @link StartSymmetricModelingBuilderMirrorProcedureOption NXOpen.Features.Subdivision.StartSymmetricModelingBuilderMirrorProcedureOption @endlink is an alias for @link StartSymmetricModelingBuilder.MirrorProcedureOption NXOpen.Features.Subdivision.StartSymmetricModelingBuilder.MirrorProcedureOption@endlink
StartSymmetricModelingBuilderMirrorProcedureOption = StartSymmetricModelingBuilder.MirrorProcedureOption


##  @link SubdivisionBridgeFaceBuilderContinuityType NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilderContinuityType @endlink is an alias for @link SubdivisionBridgeFaceBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.ContinuityType@endlink
SubdivisionBridgeFaceBuilderContinuityType = SubdivisionBridgeFaceBuilder.ContinuityType


##  @link SubdivisionConnectCageBuilderContinuityTypes NXOpen.Features.Subdivision.SubdivisionConnectCageBuilderContinuityTypes @endlink is an alias for @link SubdivisionConnectCageBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder.ContinuityTypes@endlink
SubdivisionConnectCageBuilderContinuityTypes = SubdivisionConnectCageBuilder.ContinuityTypes


##  @link SubdivisionExtrudeCageBuilderContinuityType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderContinuityType @endlink is an alias for @link SubdivisionExtrudeCageBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ContinuityType@endlink
SubdivisionExtrudeCageBuilderContinuityType = SubdivisionExtrudeCageBuilder.ContinuityType


##  @link SubdivisionExtrudeCageBuilderDirectionType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderDirectionType @endlink is an alias for @link SubdivisionExtrudeCageBuilder.DirectionType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.DirectionType@endlink
SubdivisionExtrudeCageBuilderDirectionType = SubdivisionExtrudeCageBuilder.DirectionType


##  @link SubdivisionExtrudeCageBuilderScalingMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderScalingMethodType @endlink is an alias for @link SubdivisionExtrudeCageBuilder.ScalingMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.ScalingMethodType@endlink
SubdivisionExtrudeCageBuilderScalingMethodType = SubdivisionExtrudeCageBuilder.ScalingMethodType


##  @link SubdivisionExtrudeCageBuilderTransformationMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderTransformationMethodType @endlink is an alias for @link SubdivisionExtrudeCageBuilder.TransformationMethodType NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.TransformationMethodType@endlink
SubdivisionExtrudeCageBuilderTransformationMethodType = SubdivisionExtrudeCageBuilder.TransformationMethodType


##  @link SubdivisionFillBuilderContinuityType NXOpen.Features.Subdivision.SubdivisionFillBuilderContinuityType @endlink is an alias for @link SubdivisionFillBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionFillBuilder.ContinuityType@endlink
SubdivisionFillBuilderContinuityType = SubdivisionFillBuilder.ContinuityType


##  @link SubdivisionLoftBuilderContinuityType NXOpen.Features.Subdivision.SubdivisionLoftBuilderContinuityType @endlink is an alias for @link SubdivisionLoftBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionLoftBuilder.ContinuityType@endlink
SubdivisionLoftBuilderContinuityType = SubdivisionLoftBuilder.ContinuityType


##  @link SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel @endlink is an alias for @link SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel@endlink
SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel = SubdivisionPrimitiveShapeBuilderEx.SphereSubdivisionLevel


##  @link SubdivisionPrimitiveShapeBuilderExTypes NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderExTypes @endlink is an alias for @link SubdivisionPrimitiveShapeBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx.Types@endlink
SubdivisionPrimitiveShapeBuilderExTypes = SubdivisionPrimitiveShapeBuilderEx.Types


##  @link SubdivisionPrimitiveShapeBuilderTypes NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderTypes @endlink is an alias for @link SubdivisionPrimitiveShapeBuilder.Types NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder.Types@endlink
SubdivisionPrimitiveShapeBuilderTypes = SubdivisionPrimitiveShapeBuilder.Types


##  @link SubdivisionProjectCageBuilderExModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderExModeOptions @endlink is an alias for @link SubdivisionProjectCageBuilderEx.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ModeOptions@endlink
SubdivisionProjectCageBuilderExModeOptions = SubdivisionProjectCageBuilderEx.ModeOptions


##  @link SubdivisionProjectCageBuilderExProjectionDirectionTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderExProjectionDirectionTypes @endlink is an alias for @link SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes@endlink
SubdivisionProjectCageBuilderExProjectionDirectionTypes = SubdivisionProjectCageBuilderEx.ProjectionDirectionTypes


##  @link SubdivisionProjectCageBuilderExTargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderExTargetTypes @endlink is an alias for @link SubdivisionProjectCageBuilderEx.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.TargetTypes@endlink
SubdivisionProjectCageBuilderExTargetTypes = SubdivisionProjectCageBuilderEx.TargetTypes


##  @link SubdivisionProjectCageBuilderExTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderExTypes @endlink is an alias for @link SubdivisionProjectCageBuilderEx.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderEx.Types@endlink
SubdivisionProjectCageBuilderExTypes = SubdivisionProjectCageBuilderEx.Types


##  @link SubdivisionProjectCageBuilderModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderModeOptions @endlink is an alias for @link SubdivisionProjectCageBuilder.ModeOptions NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.ModeOptions@endlink
SubdivisionProjectCageBuilderModeOptions = SubdivisionProjectCageBuilder.ModeOptions


##  @link SubdivisionProjectCageBuilderTargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderTargetTypes @endlink is an alias for @link SubdivisionProjectCageBuilder.TargetTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.TargetTypes@endlink
SubdivisionProjectCageBuilderTargetTypes = SubdivisionProjectCageBuilder.TargetTypes


##  @link SubdivisionProjectCageBuilderTypes NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderTypes @endlink is an alias for @link SubdivisionProjectCageBuilder.Types NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder.Types@endlink
SubdivisionProjectCageBuilderTypes = SubdivisionProjectCageBuilder.Types


##  @link SubdivisionRevolveBuilderContinuityType NXOpen.Features.Subdivision.SubdivisionRevolveBuilderContinuityType @endlink is an alias for @link SubdivisionRevolveBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionRevolveBuilder.ContinuityType@endlink
SubdivisionRevolveBuilderContinuityType = SubdivisionRevolveBuilder.ContinuityType


##  @link SubdivisionSetContinuityBuilderContinuityTypes NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilderContinuityTypes @endlink is an alias for @link SubdivisionSetContinuityBuilder.ContinuityTypes NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder.ContinuityTypes@endlink
SubdivisionSetContinuityBuilderContinuityTypes = SubdivisionSetContinuityBuilder.ContinuityTypes


##  @link SubdivisionSplitFaceBuilderTypes NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilderTypes @endlink is an alias for @link SubdivisionSplitFaceBuilder.Types NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder.Types@endlink
SubdivisionSplitFaceBuilderTypes = SubdivisionSplitFaceBuilder.Types


##  @link SubdivisionSweepBuilderContinuityType NXOpen.Features.Subdivision.SubdivisionSweepBuilderContinuityType @endlink is an alias for @link SubdivisionSweepBuilder.ContinuityType NXOpen.Features.Subdivision.SubdivisionSweepBuilder.ContinuityType@endlink
SubdivisionSweepBuilderContinuityType = SubdivisionSweepBuilder.ContinuityType


##  @link SubdivisionTubeBuilderEndCapsType NXOpen.Features.Subdivision.SubdivisionTubeBuilderEndCapsType @endlink is an alias for @link SubdivisionTubeBuilder.EndCapsType NXOpen.Features.Subdivision.SubdivisionTubeBuilder.EndCapsType@endlink
SubdivisionTubeBuilderEndCapsType = SubdivisionTubeBuilder.EndCapsType


##  @link SubdivisionTubeBuilderTypes NXOpen.Features.Subdivision.SubdivisionTubeBuilderTypes @endlink is an alias for @link SubdivisionTubeBuilder.Types NXOpen.Features.Subdivision.SubdivisionTubeBuilder.Types@endlink
SubdivisionTubeBuilderTypes = SubdivisionTubeBuilder.Types


##  @link TransformCageDataFallOffMethodType NXOpen.Features.Subdivision.TransformCageDataFallOffMethodType @endlink is an alias for @link TransformCageData.FallOffMethodType NXOpen.Features.Subdivision.TransformCageData.FallOffMethodType@endlink
TransformCageDataFallOffMethodType = TransformCageData.FallOffMethodType


##  @link TransformCageDataMovementMethodType NXOpen.Features.Subdivision.TransformCageDataMovementMethodType @endlink is an alias for @link TransformCageData.MovementMethodType NXOpen.Features.Subdivision.TransformCageData.MovementMethodType@endlink
TransformCageDataMovementMethodType = TransformCageData.MovementMethodType


##  @link TransformCageDataScalingMethodType NXOpen.Features.Subdivision.TransformCageDataScalingMethodType @endlink is an alias for @link TransformCageData.ScalingMethodType NXOpen.Features.Subdivision.TransformCageData.ScalingMethodType@endlink
TransformCageDataScalingMethodType = TransformCageData.ScalingMethodType


##  @link TransformCageDataTransformationMethodType NXOpen.Features.Subdivision.TransformCageDataTransformationMethodType @endlink is an alias for @link TransformCageData.TransformationMethodType NXOpen.Features.Subdivision.TransformCageData.TransformationMethodType@endlink
TransformCageDataTransformationMethodType = TransformCageData.TransformationMethodType


##  @link TransformCageDataWCSOptionType NXOpen.Features.Subdivision.TransformCageDataWCSOptionType @endlink is an alias for @link TransformCageData.WCSOptionType NXOpen.Features.Subdivision.TransformCageData.WCSOptionType@endlink
TransformCageDataWCSOptionType = TransformCageData.WCSOptionType


