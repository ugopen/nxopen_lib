from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen.Diagramming
class ArcBuilder(BaseGeometryBuilder): 
    """
         Represents a ArcBuilder.
         """
    @property
    def Center(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) Center
         Returns the center location.  
            
         
        """
        pass
    @property
    def EndAngle(self) -> float:
        """
        Getter for property: (float) EndAngle
         Returns the end angle.  
            
         
        """
        pass
    @EndAngle.setter
    def EndAngle(self, endAngle: float):
        """
        Setter for property: (float) EndAngle
         Returns the end angle.  
            
         
        """
        pass
    @property
    def MinorRadius(self) -> float:
        """
        Getter for property: (float) MinorRadius
         Returns the minor radius.  
           If unset, it will inherit the value from  NXOpen::Diagramming::Geometry::ArcBuilder::Radius .   
         
        """
        pass
    @MinorRadius.setter
    def MinorRadius(self, radius: float):
        """
        Setter for property: (float) MinorRadius
         Returns the minor radius.  
           If unset, it will inherit the value from  NXOpen::Diagramming::Geometry::ArcBuilder::Radius .   
         
        """
        pass
    @property
    def Radius(self) -> float:
        """
        Getter for property: (float) Radius
         Returns the major radius.  
            
         
        """
        pass
    @Radius.setter
    def Radius(self, radius: float):
        """
        Setter for property: (float) Radius
         Returns the major radius.  
            
         
        """
        pass
    @property
    def StartAngle(self) -> float:
        """
        Getter for property: (float) StartAngle
         Returns the start angle.  
            
         
        """
        pass
    @StartAngle.setter
    def StartAngle(self, startAngle: float):
        """
        Setter for property: (float) StartAngle
         Returns the start angle.  
            
         
        """
        pass
import NXOpen
class ArcCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Arc. """
    def CreateArcBuilder(self, arcGeometry: Arc) -> ArcBuilder:
        """
         Creates a NXOpen.Diagramming.Geometry.ArcBuilder. 
         Returns builder ( ArcBuilder NXOpen.Diagra): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Arc:
        """
         Finds the NXOpen.Diagramming.Geometry.Arc with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         Returns arcGeometry ( Arc NXOpen.Diagra):  NXOpen.Diagramming.Geometry.Arc with this name. .
        """
        pass
class Arc(BaseGeometry): 
    """ Represents the Arc class. """
    pass
import NXOpen.Diagramming
class BaseGeometryBuilder(NXOpen.Diagramming.SheetElementBuilder): 
    """
         Represents a BaseGeometryBuilder.
         """
    pass
import NXOpen.Diagramming
class BaseGeometry(NXOpen.Diagramming.SheetElement): 
    """ Represents the BaseGeometry class. """
    pass
import NXOpen.Diagramming
class LineBuilder(BaseGeometryBuilder): 
    """
         Represents a LineBuilder.
         """
    @property
    def End(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) End
         Returns the end location of this line geometry.  
            
         
        """
        pass
    @property
    def Start(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) Start
         Returns the start location of this line geometry.  
            
         
        """
        pass
import NXOpen
class LineCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Line. """
    def CreateLineBuilder(self, lineGeometry: Line) -> LineBuilder:
        """
         Creates a NXOpen.Diagramming.Geometry.LineBuilder. 
         Returns builder ( LineBuilder NXOpen.Diagra): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Line:
        """
         Finds the NXOpen.Diagramming.Geometry.Line with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         Returns lineGeometry ( Line NXOpen.Diagra):  NXOpen.Diagramming.Geometry.Line with this name. .
        """
        pass
class Line(BaseGeometry): 
    """ Represents the Line class. """
    pass
import NXOpen.Diagramming
class PointBuilder(BaseGeometryBuilder): 
    """
         Represents a PointBuilder.
         """
    @property
    def Coordinate(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) Coordinate
         Returns the location of this point geometry.  
            
         
        """
        pass
import NXOpen
class PointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Point. """
    def CreatePointBuilder(self, pointGeometry: Point) -> PointBuilder:
        """
         Creates a NXOpen.Diagramming.Geometry.PointBuilder. 
         Returns builder ( PointBuilder NXOpen.Diagra): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Point:
        """
         Finds the NXOpen.Diagramming.Geometry.Point with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         Returns pointGeometry ( Point NXOpen.Diagra):  NXOpen.Diagramming.Geometry.Point with this name. .
        """
        pass
class Point(BaseGeometry): 
    """ Represents the Point class. """
    pass
import NXOpen.Diagramming
class RectangleBuilder(BaseGeometryBuilder): 
    """
         Represents a RectangleBuilder.
         """
    @property
    def FirstCorner(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) FirstCorner
         Returns the start location of this rectangle geometry.  
            
         
        """
        pass
    @property
    def SecondCorner(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) SecondCorner
         Returns the end location of this rectangle geometry.  
            
         
        """
        pass
import NXOpen
class RectangleCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Rectangle. """
    def CreateRectangleBuilder(self, rectangleGeometry: Rectangle) -> RectangleBuilder:
        """
         Creates a NXOpen.Diagramming.Geometry.RectangleBuilder. 
         Returns builder ( RectangleBuilder NXOpen.Diagra): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Rectangle:
        """
         Finds the NXOpen.Diagramming.Geometry.Rectangle with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         Returns rectangleGeometry ( Rectangle NXOpen.Diagra):  NXOpen.Diagramming.Geometry.Rectangle with this name. .
        """
        pass
class Rectangle(BaseGeometry): 
    """ Represents the Rectangle class. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectBaseGeometryList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: BaseGeometry) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[BaseGeometry], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[BaseGeometry]) -> bool:
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
    def Add(self, selection: BaseGeometry, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: BaseGeometry, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: BaseGeometry, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: BaseGeometry, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    def Contains(self, objectValue: BaseGeometry) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[BaseGeometry]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( BaseGeometry List[NXOpen.Diag):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: BaseGeometry) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[BaseGeometry]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: BaseGeometry, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: BaseGeometry, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: BaseGeometry, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[BaseGeometry]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
