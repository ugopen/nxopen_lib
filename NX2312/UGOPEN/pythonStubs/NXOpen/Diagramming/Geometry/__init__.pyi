from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen.Diagramming
## 
##          Represents a ArcBuilder.
##           <br> To create a new instance of this class, use @link NXOpen::Diagramming::Geometry::ArcCollection::CreateArcBuilder  NXOpen::Diagramming::Geometry::ArcCollection::CreateArcBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ArcBuilder(BaseGeometryBuilder): 
    """
         Represents a ArcBuilder.
         """


    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Center
    ##   the center location.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def Center(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Center
          the center location.  
            
         
        """
        pass
    
    ## Getter for property: (float) EndAngle
    ##   the end angle.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return float
    @property
    def EndAngle(self) -> float:
        """
        Getter for property: (float) EndAngle
          the end angle.  
            
         
        """
        pass
    
    ## Setter for property: (float) EndAngle

    ##   the end angle.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @EndAngle.setter
    def EndAngle(self, endAngle: float):
        """
        Setter for property: (float) EndAngle
          the end angle.  
            
         
        """
        pass
    
    ## Getter for property: (float) MinorRadius
    ##   the minor radius.  
    ##    If unset, it will inherit the value from @link NXOpen::Diagramming::Geometry::ArcBuilder::Radius NXOpen::Diagramming::Geometry::ArcBuilder::Radius@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def MinorRadius(self) -> float:
        """
        Getter for property: (float) MinorRadius
          the minor radius.  
           If unset, it will inherit the value from @link NXOpen::Diagramming::Geometry::ArcBuilder::Radius NXOpen::Diagramming::Geometry::ArcBuilder::Radius@endlink .   
         
        """
        pass
    
    ## Setter for property: (float) MinorRadius

    ##   the minor radius.  
    ##    If unset, it will inherit the value from @link NXOpen::Diagramming::Geometry::ArcBuilder::Radius NXOpen::Diagramming::Geometry::ArcBuilder::Radius@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MinorRadius.setter
    def MinorRadius(self, radius: float):
        """
        Setter for property: (float) MinorRadius
          the minor radius.  
           If unset, it will inherit the value from @link NXOpen::Diagramming::Geometry::ArcBuilder::Radius NXOpen::Diagramming::Geometry::ArcBuilder::Radius@endlink .   
         
        """
        pass
    
    ## Getter for property: (float) Radius
    ##   the major radius.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return float
    @property
    def Radius(self) -> float:
        """
        Getter for property: (float) Radius
          the major radius.  
            
         
        """
        pass
    
    ## Setter for property: (float) Radius

    ##   the major radius.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Radius.setter
    def Radius(self, radius: float):
        """
        Setter for property: (float) Radius
          the major radius.  
            
         
        """
        pass
    
    ## Getter for property: (float) StartAngle
    ##   the start angle.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return float
    @property
    def StartAngle(self) -> float:
        """
        Getter for property: (float) StartAngle
          the start angle.  
            
         
        """
        pass
    
    ## Setter for property: (float) StartAngle

    ##   the start angle.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @StartAngle.setter
    def StartAngle(self, startAngle: float):
        """
        Setter for property: (float) StartAngle
          the start angle.  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Arc.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ArcCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Arc. """


    ##  Creates a @link NXOpen::Diagramming::Geometry::ArcBuilder NXOpen::Diagramming::Geometry::ArcBuilder@endlink . 
    ##  @return builder (@link ArcBuilder NXOpen.Diagramming.Geometry.ArcBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Diagramming::Geometry::Arc NXOpen::Diagramming::Geometry::Arc@endlink  to be edited, if NULL then create a new one 
    def CreateArcBuilder(part: ArcCollection, arcGeometry: Arc) -> ArcBuilder:
        """
         Creates a @link NXOpen::Diagramming::Geometry::ArcBuilder NXOpen::Diagramming::Geometry::ArcBuilder@endlink . 
         @return builder (@link ArcBuilder NXOpen.Diagramming.Geometry.ArcBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Geometry::Arc NXOpen::Diagramming::Geometry::Arc@endlink  with the given identifier as recorded in a journal.
    ##                  An exception will be thrown if no object can be found with given name. 
    ##  @return arcGeometry (@link Arc NXOpen.Diagramming.Geometry.Arc@endlink):  @link NXOpen::Diagramming::Geometry::Arc NXOpen::Diagramming::Geometry::Arc@endlink  with this name. .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: ArcCollection, journalIdentifier: str) -> Arc:
        """
         Finds the @link NXOpen::Diagramming::Geometry::Arc NXOpen::Diagramming::Geometry::Arc@endlink  with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         @return arcGeometry (@link Arc NXOpen.Diagramming.Geometry.Arc@endlink):  @link NXOpen::Diagramming::Geometry::Arc NXOpen::Diagramming::Geometry::Arc@endlink  with this name. .
        """
        pass
    
##  Represents the Arc class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Geometry::ArcBuilder  NXOpen::Diagramming::Geometry::ArcBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Arc(BaseGeometry): 
    """ Represents the Arc class. """
    pass


import NXOpen.Diagramming
## 
##          Represents a BaseGeometryBuilder.
##           <br> This is an abstract class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BaseGeometryBuilder(NXOpen.Diagramming.SheetElementBuilder): 
    """
         Represents a BaseGeometryBuilder.
         """
    pass


import NXOpen.Diagramming
##  Represents the BaseGeometry class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Geometry::BaseGeometryBuilder  NXOpen::Diagramming::Geometry::BaseGeometryBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BaseGeometry(NXOpen.Diagramming.SheetElement): 
    """ Represents the BaseGeometry class. """
    pass


import NXOpen.Diagramming
## 
##          Represents a LineBuilder.
##           <br> To create a new instance of this class, use @link NXOpen::Diagramming::Geometry::LineCollection::CreateLineBuilder  NXOpen::Diagramming::Geometry::LineCollection::CreateLineBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class LineBuilder(BaseGeometryBuilder): 
    """
         Represents a LineBuilder.
         """


    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) End
    ##   the end location of this line geometry.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def End(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) End
          the end location of this line geometry.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Start
    ##   the start location of this line geometry.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def Start(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Start
          the start location of this line geometry.  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Line.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class LineCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Line. """


    ##  Creates a @link NXOpen::Diagramming::Geometry::LineBuilder NXOpen::Diagramming::Geometry::LineBuilder@endlink . 
    ##  @return builder (@link LineBuilder NXOpen.Diagramming.Geometry.LineBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Diagramming::Geometry::Line NXOpen::Diagramming::Geometry::Line@endlink  to be edited, if NULL then create a new one 
    def CreateLineBuilder(part: LineCollection, lineGeometry: Line) -> LineBuilder:
        """
         Creates a @link NXOpen::Diagramming::Geometry::LineBuilder NXOpen::Diagramming::Geometry::LineBuilder@endlink . 
         @return builder (@link LineBuilder NXOpen.Diagramming.Geometry.LineBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Geometry::Line NXOpen::Diagramming::Geometry::Line@endlink  with the given identifier as recorded in a journal.
    ##                  An exception will be thrown if no object can be found with given name. 
    ##  @return lineGeometry (@link Line NXOpen.Diagramming.Geometry.Line@endlink):  @link NXOpen::Diagramming::Geometry::Line NXOpen::Diagramming::Geometry::Line@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: LineCollection, journalIdentifier: str) -> Line:
        """
         Finds the @link NXOpen::Diagramming::Geometry::Line NXOpen::Diagramming::Geometry::Line@endlink  with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         @return lineGeometry (@link Line NXOpen.Diagramming.Geometry.Line@endlink):  @link NXOpen::Diagramming::Geometry::Line NXOpen::Diagramming::Geometry::Line@endlink  with this name. .
        """
        pass
    
##  Represents the Line class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Geometry::LineBuilder  NXOpen::Diagramming::Geometry::LineBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Line(BaseGeometry): 
    """ Represents the Line class. """
    pass


import NXOpen.Diagramming
## 
##          Represents a PointBuilder.
##           <br> To create a new instance of this class, use @link NXOpen::Diagramming::Geometry::PointCollection::CreatePointBuilder  NXOpen::Diagramming::Geometry::PointCollection::CreatePointBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PointBuilder(BaseGeometryBuilder): 
    """
         Represents a PointBuilder.
         """


    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Coordinate
    ##   the location of this point geometry.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def Coordinate(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Coordinate
          the location of this point geometry.  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Point.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Point. """


    ##  Creates a @link NXOpen::Diagramming::Geometry::PointBuilder NXOpen::Diagramming::Geometry::PointBuilder@endlink . 
    ##  @return builder (@link PointBuilder NXOpen.Diagramming.Geometry.PointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Diagramming::Geometry::Point NXOpen::Diagramming::Geometry::Point@endlink  to be edited, if NULL then create a new one 
    def CreatePointBuilder(part: PointCollection, pointGeometry: Point) -> PointBuilder:
        """
         Creates a @link NXOpen::Diagramming::Geometry::PointBuilder NXOpen::Diagramming::Geometry::PointBuilder@endlink . 
         @return builder (@link PointBuilder NXOpen.Diagramming.Geometry.PointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Geometry::Point NXOpen::Diagramming::Geometry::Point@endlink  with the given identifier as recorded in a journal.
    ##                  An exception will be thrown if no object can be found with given name. 
    ##  @return pointGeometry (@link Point NXOpen.Diagramming.Geometry.Point@endlink):  @link NXOpen::Diagramming::Geometry::Point NXOpen::Diagramming::Geometry::Point@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: PointCollection, journalIdentifier: str) -> Point:
        """
         Finds the @link NXOpen::Diagramming::Geometry::Point NXOpen::Diagramming::Geometry::Point@endlink  with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         @return pointGeometry (@link Point NXOpen.Diagramming.Geometry.Point@endlink):  @link NXOpen::Diagramming::Geometry::Point NXOpen::Diagramming::Geometry::Point@endlink  with this name. .
        """
        pass
    
##  Represents the Point class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Geometry::PointBuilder  NXOpen::Diagramming::Geometry::PointBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Point(BaseGeometry): 
    """ Represents the Point class. """
    pass


import NXOpen.Diagramming
## 
##          Represents a RectangleBuilder.
##           <br> To create a new instance of this class, use @link NXOpen::Diagramming::Geometry::RectangleCollection::CreateRectangleBuilder  NXOpen::Diagramming::Geometry::RectangleCollection::CreateRectangleBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class RectangleBuilder(BaseGeometryBuilder): 
    """
         Represents a RectangleBuilder.
         """


    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) FirstCorner
    ##   the start location of this rectangle geometry.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def FirstCorner(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) FirstCorner
          the start location of this rectangle geometry.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) SecondCorner
    ##   the end location of this rectangle geometry.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def SecondCorner(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) SecondCorner
          the end location of this rectangle geometry.  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Rectangle.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class RectangleCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Rectangle. """


    ##  Creates a @link NXOpen::Diagramming::Geometry::RectangleBuilder NXOpen::Diagramming::Geometry::RectangleBuilder@endlink . 
    ##  @return builder (@link RectangleBuilder NXOpen.Diagramming.Geometry.RectangleBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Diagramming::Geometry::Rectangle NXOpen::Diagramming::Geometry::Rectangle@endlink  to be edited, if NULL then create a new one 
    def CreateRectangleBuilder(part: RectangleCollection, rectangleGeometry: Rectangle) -> RectangleBuilder:
        """
         Creates a @link NXOpen::Diagramming::Geometry::RectangleBuilder NXOpen::Diagramming::Geometry::RectangleBuilder@endlink . 
         @return builder (@link RectangleBuilder NXOpen.Diagramming.Geometry.RectangleBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Geometry::Rectangle NXOpen::Diagramming::Geometry::Rectangle@endlink  with the given identifier as recorded in a journal.
    ##                  An exception will be thrown if no object can be found with given name. 
    ##  @return rectangleGeometry (@link Rectangle NXOpen.Diagramming.Geometry.Rectangle@endlink):  @link NXOpen::Diagramming::Geometry::Rectangle NXOpen::Diagramming::Geometry::Rectangle@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: RectangleCollection, journalIdentifier: str) -> Rectangle:
        """
         Finds the @link NXOpen::Diagramming::Geometry::Rectangle NXOpen::Diagramming::Geometry::Rectangle@endlink  with the given identifier as recorded in a journal.
                         An exception will be thrown if no object can be found with given name. 
         @return rectangleGeometry (@link Rectangle NXOpen.Diagramming.Geometry.Rectangle@endlink):  @link NXOpen::Diagramming::Geometry::Rectangle NXOpen::Diagramming::Geometry::Rectangle@endlink  with this name. .
        """
        pass
    
##  Represents the Rectangle class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Geometry::RectangleBuilder  NXOpen::Diagramming::Geometry::RectangleBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Rectangle(BaseGeometry): 
    """ Represents the Rectangle class. """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectBaseGeometryList(NXOpen.TaggedObject): 
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
    def Add(object_list: SelectBaseGeometryList, objectValue: BaseGeometry) -> bool:
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
    def AddWithViews(object_list: SelectBaseGeometryList, objects: List[BaseGeometry], views: List[NXOpen.View]) -> bool:
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
    def Add(self, object_list: SelectBaseGeometryList, objects: List[BaseGeometry]) -> bool:
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
    def Add(self, object_list: SelectBaseGeometryList, input_selection_method: NXOpen.SelectionMethod) -> bool:
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
    def Add(self, object_list: SelectBaseGeometryList, selection: BaseGeometry, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
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
    def Add(self, object_list: SelectBaseGeometryList, snap_type: NXOpen.InferSnapType.SnapType, selection1: BaseGeometry, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: BaseGeometry, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def Add(self, object_list: SelectBaseGeometryList, selection: BaseGeometry, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    def Clear(object_list: SelectBaseGeometryList) -> None:
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
    def Contains(object_list: SelectBaseGeometryList, objectValue: BaseGeometry) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link BaseGeometry List[NXOpen.Diagramming.Geometry.BaseGeometry]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArray(object_list: SelectBaseGeometryList) -> List[BaseGeometry]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link BaseGeometry List[NXOpen.Diagramming.Geometry.BaseGeometry]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectObjectArray(object_list: SelectBaseGeometryList) -> List[NXOpen.SelectObject]:
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
    def Remove(object_list: SelectBaseGeometryList, objectValue: BaseGeometry) -> bool:
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
    def RemoveArray(object_list: SelectBaseGeometryList, objects: List[BaseGeometry]) -> bool:
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
    def Remove(self, object_list: SelectBaseGeometryList, objectValue: BaseGeometry, view: NXOpen.View) -> bool:
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
    def Remove(self, object_list: SelectBaseGeometryList, snap_type: NXOpen.InferSnapType.SnapType, selection1: BaseGeometry, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: BaseGeometry, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def Remove(self, object_list: SelectBaseGeometryList, input_selection_method: NXOpen.SelectionMethod) -> bool:
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
    def SetArray(object_list: SelectBaseGeometryList, objects: List[BaseGeometry]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
    
## @package NXOpen.Diagramming.Geometry
## Classes, Enums and Structs under NXOpen.Diagramming.Geometry namespace

