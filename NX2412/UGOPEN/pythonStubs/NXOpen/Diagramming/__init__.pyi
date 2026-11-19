from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AnnotationBuilder(ConnectableElementBuilder): 
    """
    Represents a AnnotationBuilder.
    """
    class TextTypeOption(Enum):
        """
        Members Include: 
         |Fixed|  Setting the text type fixed
         |Parametric|  Setting the text type parametric

        """
        Fixed: int
        Parametric: int
        @staticmethod
        def ValueOf(value: int) -> AnnotationBuilder.TextTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryDisplay(self) -> bool:
        """
        Getter for property: (bool) BoundaryDisplay
         Returns the visibility of boundary.  
           If return true, the annotation will show its boundary if it has one.   
         
        """
        pass
    @BoundaryDisplay.setter
    def BoundaryDisplay(self, boundaryDisplay: bool):
        """
        Setter for property: (bool) BoundaryDisplay
         Returns the visibility of boundary.  
           If return true, the annotation will show its boundary if it has one.   
         
        """
        pass
    @property
    def BoundaryType(self) -> DiagrammingAnnotationboundarytype:
        """
        Getter for property: ( DiagrammingAnnotationboundarytype NXOpen.D) BoundaryType
         Returns the boundary type of the annotation   
            
         
        """
        pass
    @BoundaryType.setter
    def BoundaryType(self, boundaryType: DiagrammingAnnotationboundarytype):
        """
        Setter for property: ( DiagrammingAnnotationboundarytype NXOpen.D) BoundaryType
         Returns the boundary type of the annotation   
            
         
        """
        pass
    @property
    def FormattedStringBuilder(self) -> FormattedStringBuilder:
        """
        Getter for property: ( FormattedStringBuilder NXOpen.D) FormattedStringBuilder
         Returns the formatted string of the text.  
             
         
        """
        pass
    @property
    def Text(self) -> str:
        """
        Getter for property: (str) Text
         Returns the text should be used only when textType is Diagramming.  
          AnnotationBuilder.TextTypeOption.Fixed   
         
        """
        pass
    @Text.setter
    def Text(self, strValue: str):
        """
        Setter for property: (str) Text
         Returns the text should be used only when textType is Diagramming.  
          AnnotationBuilder.TextTypeOption.Fixed   
         
        """
        pass
    @property
    def TextStyleBuilder(self) -> TextStyleBuilder:
        """
        Getter for property: ( TextStyleBuilder NXOpen.D) TextStyleBuilder
         Returns the text style of the annotation.  
             
         
        """
        pass
    @property
    def TextType(self) -> AnnotationBuilder.TextTypeOption:
        """
        Getter for property: ( AnnotationBuilder.TextTypeOption NXOpen.D) TextType
         Returns the text type.  
           If  NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed , the text
                    of annotation is stored in  NXOpen::Diagramming::AnnotationBuilder . 
                    If  NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric , the text
                    of annotation is stored in  NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder .  
         
        """
        pass
    @TextType.setter
    def TextType(self, textType: AnnotationBuilder.TextTypeOption):
        """
        Setter for property: ( AnnotationBuilder.TextTypeOption NXOpen.D) TextType
         Returns the text type.  
           If  NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed , the text
                    of annotation is stored in  NXOpen::Diagramming::AnnotationBuilder . 
                    If  NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric , the text
                    of annotation is stored in  NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder .  
         
        """
        pass
import NXOpen
class AnnotationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Annotation. """
    def CreateAnnotationBuilder(self, annotation: Annotation) -> AnnotationBuilder:
        """
         Creates a NXOpen.Diagramming.AnnotationBuilder. 
         Returns builder ( AnnotationBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Annotation:
        """
         Finds the NXOpen.Diagramming.Annotation with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns annotation ( Annotation NXOpen.D):  NXOpen.Diagramming.Annotation with this name. .
        """
        pass
class Annotation(ConnectableElement): 
    """ Represents the Annotation class. """
    pass
class ArrowDirectionType(Enum):
    """
    Members Include: 
     |OutofSheet|  Out of Sheet 
     |IntoSheet| 

    """
    OutofSheet: int
    IntoSheet: int
    @staticmethod
    def ValueOf(value: int) -> ArrowDirectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ArrowStyleType(Enum):
    """
    Members Include: 
     |Filled|  Filled 
     |Closed|  Closed 
     |ClosedSolid|  Close Solid 
     |Open| 

    """
    Filled: int
    Closed: int
    ClosedSolid: int
    Open: int
    @staticmethod
    def ValueOf(value: int) -> ArrowStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Axis(Enum):
    """
    Members Include: 
     |X|  X axis 
     |Y|  Y axis 

    """
    X: int
    Y: int
    @staticmethod
    def ValueOf(value: int) -> Axis:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class BaseObjectBuilder(NXOpen.Builder): 
    """
    Represents a BaseObjectBuilder.
    """
    pass
import NXOpen
class BaseObject(NXOpen.DisplayableObject): 
    """ Represents the BaseObject class. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class BaseSubObjectBuilder(NXOpen.TaggedObject): 
    """
    Represents a BaseSubObjectBuilder.
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class BaseTaggedObjectBuilder(NXOpen.TaggedObject): 
    """
    Represents a BaseTaggedObjectBuilder.
    """
    pass
import NXOpen
class BulkEditBuilder(NXOpen.Builder): 
    """
    Represents a BulkEditBuilder to edit bulk of objects.
    """
    @property
    def EditRenderingProp(self) -> bool:
        """
        Getter for property: (bool) EditRenderingProp
         Returns the status of editing rendering properties.  
             
         
        """
        pass
    @EditRenderingProp.setter
    def EditRenderingProp(self, editStatus: bool):
        """
        Setter for property: (bool) EditRenderingProp
         Returns the status of editing rendering properties.  
             
         
        """
        pass
    @property
    def RenderingProperties(self) -> RenderingPropertiesBuilder:
        """
        Getter for property: ( RenderingPropertiesBuilder NXOpen.D) RenderingProperties
         Returns the line rendering properties.  
             
         
        """
        pass
    def SetDeltaXCoordinate(self, deltaXCoordinate: float) -> None:
        """
         Sets the delta value of X coordinate for bulk moving. 
        """
        pass
    def SetDeltaYCoordinate(self, deltaYCoordinate: float) -> None:
        """
         Sets the delta value of Y coordinate for bulk moving. 
        """
        pass
    def SetHide(self, hide: bool) -> None:
        """
         Sets the visibility of sheet elements. 
        """
        pass
    def SetHideLabel(self, hideLabel: bool) -> None:
        """
         Sets the visibility of labels. 
        """
        pass
    def SetSheetElements(self, sheetElements: List[SheetElement]) -> None:
        """
         Sets the sheet elements for bulk editing. 
        """
        pass
import NXOpen
class CannedAnnotationBuilder(NXOpen.Builder): 
    """
    Represents a CannedAnnotationBuilder.
    """
    class InheritOption(Enum):
        """
        Members Include: 
         |Preferences|  Setting the inherit from preferences option
         |CustomerDefaults|  Setting the inherit from customer defaults option
         |Selection|  Setting the inherit from selection option

        """
        Preferences: int
        CustomerDefaults: int
        Selection: int
        @staticmethod
        def ValueOf(value: int) -> CannedAnnotationBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnnotationBuilder(self) -> AnnotationBuilder:
        """
        Getter for property: ( AnnotationBuilder NXOpen.D) AnnotationBuilder
         Returns the annotation of this canned annotation.  
             
         
        """
        pass
    @property
    def LeaderLines(self) -> LeaderLineBuilderList:
        """
        Getter for property: ( LeaderLineBuilderList NXOpen.D) LeaderLines
         Returns the list of the leader lines.  
             
         
        """
        pass
    @property
    def TextBoxIndent(self) -> int:
        """
        Getter for property: (int) TextBoxIndent
         Returns the indent value of the text box in the canned annotation.  
             
         
        """
        pass
    @TextBoxIndent.setter
    def TextBoxIndent(self, indent: int):
        """
        Setter for property: (int) TextBoxIndent
         Returns the indent value of the text box in the canned annotation.  
             
         
        """
        pass
    @property
    def TextBoxModifiable(self) -> bool:
        """
        Getter for property: (bool) TextBoxModifiable
         Returns the flag that indicates if the text box in the canned annotation is modifiable.  
             
         
        """
        pass
    @TextBoxModifiable.setter
    def TextBoxModifiable(self, isModifiable: bool):
        """
        Setter for property: (bool) TextBoxModifiable
         Returns the flag that indicates if the text box in the canned annotation is modifiable.  
             
         
        """
        pass
    @property
    def TextBoxShadowBox(self) -> bool:
        """
        Getter for property: (bool) TextBoxShadowBox
         Returns the flag that indicates if the text box in the canned annotation has shadow box.  
             
         
        """
        pass
    @TextBoxShadowBox.setter
    def TextBoxShadowBox(self, isShadowBox: bool):
        """
        Setter for property: (bool) TextBoxShadowBox
         Returns the flag that indicates if the text box in the canned annotation has shadow box.  
             
         
        """
        pass
    def CreateLeaderLine(self) -> LeaderLineBuilder:
        """
         Create a new NXOpen.Diagramming.LeaderLineBuilder builder. 
         Returns leaderLine ( LeaderLineBuilder NXOpen.D): .
        """
        pass
    def Inherit(self, inheritOption: CannedAnnotationBuilder.InheritOption, annotation: Annotation) -> None:
        """
         Inherit. 
        """
        pass
class ConnectableElementBuilder(SheetElementBuilder): 
    """
    Represents a ConnectableElementBuilder.
    """
    def GetAllPorts(self) -> List[Port]:
        """
         Gets all ports of this connectable element. 
         Returns ports ( Port List[NXOpen): .
        """
        pass
    def GetPorts(self, direction: Direction) -> List[Port]:
        """
         Gets ports of this connectable element by the direction. 
         Returns ports ( Port List[NXOpen): .
        """
        pass
class ConnectableElement(SheetElement): 
    """ Represents the ConnectableElement class. """
    pass
import NXOpen
class ConnectionBuilder(SheetElementBuilder): 
    """
    Represents a ConnectionBuilder.
    """
    class ShapeOption(Enum):
        """
        Members Include: 
         |Orthogonal|  Orthogonal 
         |Quadratic|  Quadratic 
         |Spline|  Spline 
         |Arc|  Arc 

        """
        Orthogonal: int
        Quadratic: int
        Spline: int
        Arc: int
        @staticmethod
        def ValueOf(value: int) -> ConnectionBuilder.ShapeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the discipline of this connection.  
             
         
        """
        pass
    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
         Returns the discipline of this connection.  
             
         
        """
        pass
    @property
    def End(self) -> Port:
        """
        Getter for property: ( Port NXOpen.D) End
         Returns the end port of this connection.  
            
         
        """
        pass
    @End.setter
    def End(self, endPort: Port):
        """
        Setter for property: ( Port NXOpen.D) End
         Returns the end port of this connection.  
            
         
        """
        pass
    @property
    def EndLocation(self) -> LocationBuilder:
        """
        Getter for property: ( LocationBuilder NXOpen.D) EndLocation
         Returns the end location of this connection.  
           
                    This end location is applicable only when the  Diagramming::ConnectionBuilder::End  port is NULL.   
         
        """
        pass
    @property
    def ReverseEnd(self) -> bool:
        """
        Getter for property: (bool) ReverseEnd
         Returns the reversed flag of this connection.  
             
         
        """
        pass
    @property
    def Start(self) -> Port:
        """
        Getter for property: ( Port NXOpen.D) Start
         Returns the start port of this connection.  
             
         
        """
        pass
    @Start.setter
    def Start(self, startPort: Port):
        """
        Setter for property: ( Port NXOpen.D) Start
         Returns the start port of this connection.  
             
         
        """
        pass
    @property
    def StartLocation(self) -> LocationBuilder:
        """
        Getter for property: ( LocationBuilder NXOpen.D) StartLocation
         Returns the start location of this connection.  
           
                    This start location is applicable only when the  Diagramming::ConnectionBuilder::Start  is NULL.  
         
        """
        pass
    def GetBendPoints(self) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the connection. 
         Returns points ( NXOpen.Point2d Li): .
        """
        pass
    def GetShapeType(self) -> ConnectionBuilder.ShapeOption:
        """
         Gets the connection shape. 
         Returns shapeType ( ConnectionBuilder.ShapeOption NXOpen.D): .
        """
        pass
    def SetBendPoints(self, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the connection. 
        """
        pass
    def SetShapeType(self, shapeType: ConnectionBuilder.ShapeOption) -> None:
        """
         Sets the connection shape. 
        """
        pass
import NXOpen
class ConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of connection. """
    def CreateConnectionBuilder(self, connection: Connection) -> ConnectionBuilder:
        """
         Creates a NXOpen.Diagramming.ConnectionBuilder. 
         Returns builder ( ConnectionBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Connection:
        """
         Finds the NXOpen.Diagramming.Connection with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns connection ( Connection NXOpen.D):  NXOpen.Diagramming.Connection with this name. .
        """
        pass
import NXOpen
class ConnectionLocationBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ConnectionLocationBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ConnectionLocationBuilder) -> None:
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
    def Erase(self, obj: ConnectionLocationBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ConnectionLocationBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ConnectionLocationBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ConnectionLocationBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ConnectionLocationBuilder NXOpen.D):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ConnectionLocationBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ConnectionLocationBuilder List[NXOpen):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ConnectionLocationBuilder) -> None:
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
    def SetContents(self, objects: List[ConnectionLocationBuilder]) -> None:
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
    def Swap(self, object1: ConnectionLocationBuilder, object2: ConnectionLocationBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
class ConnectionLocationBuilder(LocationBuilder): 
    """
    Represents a ConnectionLocationBuilder.
    """
    @property
    def SegmentIdentifier(self) -> int:
        """
        Getter for property: (int) SegmentIdentifier
         Returns the segment identifier.  
            
         
        """
        pass
    @SegmentIdentifier.setter
    def SegmentIdentifier(self, segmentId: int):
        """
        Setter for property: (int) SegmentIdentifier
         Returns the segment identifier.  
            
         
        """
        pass
class Connection(SheetElement): 
    """ Represents the Connection class. """
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: ( Annotation NXOpen.D) Label
         Returns the label of the connection.  
             
         
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
class DefineTitleBlockBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Diagramming.DefineTitleBlockBuilder builder """
    @property
    def Cells(self) -> TitleBlockCellBuilderList:
        """
        Getter for property: ( TitleBlockCellBuilderList NXOpen.D) Cells
         Returns the cells   
            
         
        """
        pass
    def GetCell(self, table: NXOpen.Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> TitleBlockCellBuilder:
        """
         Get the cell builder. 
         Returns cell ( TitleBlockCellBuilder NXOpen.D): .
        """
        pass
    def GetTables(self) -> List[NXOpen.Diagramming.Tables.Table]:
        """
         Get tables. 
         Returns tables ( NXOpen.Diagramming.Tables.Table Li): .
        """
        pass
    def SetTables(self, tables: List[NXOpen.Diagramming.Tables.Table]) -> None:
        """
         Set tables. 
        """
        pass
class DiagrammingAlignment(Enum):
    """
    Members Include: 
     |Left|  Setting the left alignment 
     |Center|  Setting the center alignment 
     |Right|  Setting the right alignment 
     |Justify|  Setting the justify alignment 

    """
    Left: int
    Center: int
    Right: int
    Justify: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingAlignment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingAnnotationboundarytype(Enum):
    """
    Members Include: 
     |NotSet|  No Boundary Type 
     |Circle|  Circle Type 
     |Ellipse|  Ellipse Type 
     |Rectangle|  Rectangle Type 
     |RoundedRectangle|  Rounded Rectangle Type 

    """
    NotSet: int
    Circle: int
    Ellipse: int
    Rectangle: int
    RoundedRectangle: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingAnnotationboundarytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingArrowtype(Enum):
    """
    Members Include: 
     |NotSet|  Setting the arrow type none arrow
     |Open|  Setting the arrow type open arrow
     |Filled|  Setting the arrow type filled arrow
     |ClosedSolid|  Setting the arrow type closed solid arrow

    """
    NotSet: int
    Open: int
    Filled: int
    ClosedSolid: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingArrowtype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingConnectionlabelhorizontaloffsetposition(Enum):
    """
    Members Include: 
     |Above|  Above 
     |Below|  Below 

    """
    Above: int
    Below: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingConnectionlabelhorizontaloffsetposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingConnectionlabelposition(Enum):
    """
    Members Include: 
     |Start|  Start 
     |End|  End 
     |Center|  Centered 
     |Spaced|  Spaced 

    """
    Start: int
    End: int
    Center: int
    Spaced: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingConnectionlabelposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingConnectionlabelverticaloffsetposition(Enum):
    """
    Members Include: 
     |Left|  Left 
     |Right|  Right 

    """
    Left: int
    Right: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingConnectionlabelverticaloffsetposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingFlowdirectionarrowstyle(Enum):
    """
    Members Include: 
     |BottomFilledArrow| 
     |BottomOpenArrow| 
     |ClosedArrow| 
     |ClosedDoubleArrow| 
     |ClosedDoubleSolidArrow| 
     |ClosedSolidArrow| 
     |FilledArrow| 
     |FilledDoubleArrow| 
     |OpenArrow| 
     |OpenDoubleArrow| 
     |TopFilledArrow| 
     |TopOpenArrow| 

    """
    BottomFilledArrow: int
    BottomOpenArrow: int
    ClosedArrow: int
    ClosedDoubleArrow: int
    ClosedDoubleSolidArrow: int
    ClosedSolidArrow: int
    FilledArrow: int
    FilledDoubleArrow: int
    OpenArrow: int
    OpenDoubleArrow: int
    TopFilledArrow: int
    TopOpenArrow: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingFlowdirectionarrowstyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingGeometrypointmarker(Enum):
    """
    Members Include: 
     |Cross|  Cross Type 
     |Circle|  Circle Type 

    """
    Cross: int
    Circle: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingGeometrypointmarker:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingJumperprioritytype(Enum):
    """
    Members Include: 
     |Horizontal|  Horizontal 
     |Vertical|  Vertical 

    """
    Horizontal: int
    Vertical: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingJumperprioritytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingJumpertype(Enum):
    """
    Members Include: 
     |U|  U shape 
     |Break|  Break 

    """
    U: int
    Break: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingJumpertype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingLocationstyle(Enum):
    """
    Members Include: 
     |Absolute|  Absolute 
     |Relative|  Relative 

    """
    Absolute: int
    Relative: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingLocationstyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming.Geometry
import NXOpen.Diagramming.Tables
class DiagrammingManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    @property
    def ActiveSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOpen.D) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    @ActiveSheet.setter
    def ActiveSheet(self, sheet: Sheet):
        """
        Setter for property: ( Sheet NXOpen.D) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    @property
    def Nodes() -> NodeCollection:
        """
         Returns the  NXOpen::Diagramming::NodeCollection   belonging to this part 
        """
        pass
    @property
    def Sheets() -> SheetCollection:
        """
         Returns the  NXOpen::Diagramming::SheetCollection   belonging to this part 
        """
        pass
    @property
    def Connections() -> ConnectionCollection:
        """
         Returns the  NXOpen::Diagramming::ConnectionCollection   belonging to this part 
        """
        pass
    @property
    def Groups() -> GroupCollection:
        """
         Returns the  NXOpen::Diagramming::GroupCollection   belonging to this part 
        """
        pass
    @property
    def Shapes() -> ShapeCollection:
        """
         Returns the  NXOpen::Diagramming::ShapeCollection   belonging to this part 
        """
        pass
    @property
    def Ports() -> PortCollection:
        """
         Returns the  NXOpen::Diagramming::PortCollection   belonging to this part 
        """
        pass
    @property
    def Annotations() -> AnnotationCollection:
        """
         Returns the  NXOpen::Diagramming::AnnotationCollection   belonging to this part 
        """
        pass
    @property
    def Fills() -> FillCollection:
        """
         Returns the  NXOpen::Diagramming::FillCollection   belonging to this part 
        """
        pass
    @property
    def LeaderLines() -> LeaderLineCollection:
        """
         Returns the  NXOpen::Diagramming::LeaderLineCollection   belonging to this part 
        """
        pass
    @property
    def SheetBordersAndZones() -> SheetBordersAndZonesCollection:
        """
         Returns the  NXOpen::Diagramming::SheetBordersAndZonesCollection   belonging to this part 
        """
        pass
    @property
    def Tables() -> NXOpen.Diagramming.Tables.TableCollection:
        """
         Returns the  NXOpen::Diagramming::Tables::TableCollection   belonging to this part 
        """
        pass
    @property
    def TitleBlocks() -> TitleBlockCollection:
        """
         Returns the  NXOpen::Diagramming::TitleBlockCollection   belonging to this part 
        """
        pass
    @property
    def Lines() -> NXOpen.Diagramming.Geometry.LineCollection:
        """
         Returns the  NXOpen::Diagramming::Geometry::LineCollection   belonging to this part 
        """
        pass
    @property
    def Points() -> NXOpen.Diagramming.Geometry.PointCollection:
        """
         Returns the  NXOpen::Diagramming::Geometry::PointCollection   belonging to this part 
        """
        pass
    @property
    def Rectangles() -> NXOpen.Diagramming.Geometry.RectangleCollection:
        """
         Returns the  NXOpen::Diagramming::Geometry::RectangleCollection   belonging to this part 
        """
        pass
    @property
    def Arcs() -> NXOpen.Diagramming.Geometry.ArcCollection:
        """
         Returns the  NXOpen::Diagramming::Geometry::ArcCollection   belonging to this part 
        """
        pass
    def CopySheetElements(self, inputObjects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Copy the sheet elements. 
         Returns outputObjects ( NXOpen.NXObject Li):  The copies of sheet elements .
        """
        pass
    def CreateBulkEditBuilder(self) -> BulkEditBuilder:
        """
         Creates a NXOpen.Diagramming.BulkEditBuilder 
         Returns builder ( BulkEditBuilder NXOpen.D): .
        """
        pass
    def CreateCannedAnnotationBuilder(self, annotation: Annotation) -> CannedAnnotationBuilder:
        """
         Creates a NXOpen.Diagramming.CannedAnnotationBuilder. 
         Returns builder ( CannedAnnotationBuilder NXOpen.D): .
        """
        pass
    def CreateSheetSizeBuilder(self, sheet: Sheet) -> SheetSizeBuilder:
        """
         Creates a NXOpen.Diagramming.SheetSizeBuilder 
         Returns builder ( SheetSizeBuilder NXOpen.D): .
        """
        pass
    def CreateSheetTemplateBuilder(self, sheet: Sheet) -> SheetTemplateBuilder:
        """
         Creates a NXOpen.Diagramming.SheetTemplateBuilder 
         Returns builder ( SheetTemplateBuilder NXOpen.D): .
        """
        pass
    def OpenSheet(self, sheet: Sheet) -> None:
        """
         Opens a NXOpen.Diagramming.Sheet. 
        """
        pass
class DiagrammingRepeatstartposition(Enum):
    """
    Members Include: 
     |Center|  Center 
     |Start|  Start 
     |End|  End 

    """
    Center: int
    Start: int
    End: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingRepeatstartposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingSizingpolicy(Enum):
    """
    Members Include: 
     |Length|  Length policy 
     |Auto|  Auto policy 
     |Percent|  Percent policy 
     |Inherit|  Inherit policy 

    """
    Length: int
    Auto: int
    Percent: int
    Inherit: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingSizingpolicy:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagrammingStubsides(Enum):
    """
    Members Include: 
     |Auto|  Auto side 
     |Left|  Left side 
     |Right|  Right side 

    """
    Auto: int
    Left: int
    Right: int
    @staticmethod
    def ValueOf(value: int) -> DiagrammingStubsides:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Direction(Enum):
    """
    Members Include: 
     |In|  In direction 
     |Out|  Out direction 
     |Both|  Both direction 

    """
    In: int
    Out: int
    Both: int
    @staticmethod
    def ValueOf(value: int) -> Direction:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming.Geometry
class FillBuilder(SheetElementBuilder): 
    """
    Represents a FillBuilder.
    """
    class SelectionType(Enum):
        """
        Members Include: 
         |PointInRegion|  Fill by point 
         |BoundaryGeometries|  Boundary fill 

        """
        PointInRegion: int
        BoundaryGeometries: int
        @staticmethod
        def ValueOf(value: int) -> FillBuilder.SelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Geometries(self) -> NXOpen.Diagramming.Geometry.SelectBaseGeometryList:
        """
        Getter for property: ( NXOpen.Diagramming.Geometry.SelectBaseGeometryList) Geometries
         Returns the boundary geometries  
            
         
        """
        pass
    @property
    def SelectionMode(self) -> FillBuilder.SelectionType:
        """
        Getter for property: ( FillBuilder.SelectionType NXOpen.D) SelectionMode
         Returns the selection mode   
            
         
        """
        pass
    @SelectionMode.setter
    def SelectionMode(self, selectionMode: FillBuilder.SelectionType):
        """
        Setter for property: ( FillBuilder.SelectionType NXOpen.D) SelectionMode
         Returns the selection mode   
            
         
        """
        pass
    def GetSeedPoint(self) -> NXOpen.Point2d:
        """
         Gets the seed point. 
         Returns point ( NXOpen.Point2d): .
        """
        pass
    def SetIsFillByPoint(self, isFillByPoint: bool) -> None:
        """
         Sets the fill mode. 
        """
        pass
    def SetSeedPoint(self, point: NXOpen.Point2d) -> None:
        """
         Sets the seed point. 
        """
        pass
import NXOpen
class FillCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Fill. """
    def CreateFillBuilder(self, fill: Fill) -> FillBuilder:
        """
         Creates a NXOpen.Diagramming.FillBuilder. 
         Returns builder ( FillBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Fill:
        """
         Finds the NXOpen.Diagramming.Fill with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns fill ( Fill NXOpen.D):  NXOpen.Diagramming.Fill with this name. .
        """
        pass
class Fill(SheetElement): 
    """ Represents the Fill class. """
    pass
class FontEnum(Enum):
    """
    Members Include: 
     |Blockfont| 

    """
    Blockfont: int
    @staticmethod
    def ValueOf(value: int) -> FontEnum:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class FormattedStringBuilder(BaseSubObjectBuilder): 
    """
    Represents a FormattedStringBuilder.
    """
    @property
    def Format(self) -> str:
        """
        Getter for property: (str) Format
         Returns the format.  
             
         
        """
        pass
    @property
    def String(self) -> str:
        """
        Getter for property: (str) String
         Returns the string.  
             
         
        """
        pass
    def AppendFormat(self, objTags: List[NXOpen.NXObject], attrTitles: List[str], appendFormat: str) -> None:
        """
         Appends the format and related referenced attributes to this builder.
                
        """
        pass
    def ClearFormat(self) -> None:
        """
         Clears the format and related referenced attributes of this builder.
                
        """
        pass
    def GetReferencedAttributes(self) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Gets the referenced attributes.
                
         Returns A tuple consisting of (attrTitles, objTags). 
         - attrTitles is: List[str]. The titles of the referenced attributes .
         - objTags is:  NXOpen.NXObject Li. The owners of the referenced attributes .

        """
        pass
    @overload
    def SetFormatValue(self, objTags: List[NXOpen.NXObject], attrTitles: List[str], format: str) -> None:
        """
         Sets the format and related referenced attributes to this builder.
                
        """
        pass
    @overload
    def SetFormatValue(self, objTags: List[NXOpen.NXObject], parentTags: List[NXOpen.NXObject], attrTitles: List[str], format: str) -> None:
        """
         Sets the format and related referenced attributes to this builder in managed mode.
                
        """
        pass
class GroupBuilder(SheetElementBuilder): 
    """
    Represents a GroupBuilder.
    """
    def AddMember(self, sheetElement: SheetElement) -> None:
        """
         Add a member. 
        """
        pass
    def GetMember(self, memberSid: str) -> SheetElement:
        """
         Get the member by given member identifier SID. 
         Returns member ( SheetElement NXOpen.D): .
        """
        pass
    def GetMembers(self) -> List[SheetElement]:
        """
         Get all members. 
         Returns allMembers ( SheetElement List[NXOpen): .
        """
        pass
    def RemoveAllMembers(self) -> None:
        """
         Remove all members. 
        """
        pass
    def RemoveMember(self, member: SheetElement) -> None:
        """
         Remove a member. 
        """
        pass
import NXOpen
class GroupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of group. """
    def CreateGroupBuilder(self, group: Group) -> GroupBuilder:
        """
         Creates a NXOpen.Diagramming.GroupBuilder. 
         Returns builder ( GroupBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Group:
        """
         Finds the NXOpen.Diagramming.Group with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns group ( Group NXOpen.D):  NXOpen.Diagramming.Group with this name. .
        """
        pass
import NXOpen
class GroupManager(NXOpen.Object): 
    """ A manager to deal with group objects. """
    def Group(sheet: Sheet, elements: List[SheetElement]) -> None:
        """
         Creates a Group and adds the objects 
        """
        pass
    def Ungroup(group: Group, elements: List[SheetElement]) -> None:
        """
         Removes the objects from the group. 
        """
        pass
class Group(SheetElement): 
    """ Represents the Group class. """
    pass
class HorizontalCenteringMarkType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |LeftArrow|  Left Arrow 
     |RightArrow|   Right Arrow 
     |LeftandRightArrow|  Left and Right Arrow 
     |LeftandRightLine| 

    """
    NotSet: int
    LeftArrow: int
    RightArrow: int
    LeftandRightArrow: int
    LeftandRightLine: int
    @staticmethod
    def ValueOf(value: int) -> HorizontalCenteringMarkType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class LeaderLineBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[LeaderLineBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: LeaderLineBuilder) -> None:
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
    def Erase(self, obj: LeaderLineBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: LeaderLineBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: LeaderLineBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> LeaderLineBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( LeaderLineBuilder NXOpen.D):  object found at input index .
        """
        pass
    def GetContents(self) -> List[LeaderLineBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( LeaderLineBuilder List[NXOpen):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: LeaderLineBuilder) -> None:
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
    def SetContents(self, objects: List[LeaderLineBuilder]) -> None:
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
    def Swap(self, object1: LeaderLineBuilder, object2: LeaderLineBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class LeaderLineBuilder(SheetElementBuilder): 
    """
    Represents a LeaderLineBuilder.
    """
    class VerticalAlignmentOption(Enum):
        """
        Members Include: 
         |Top|  Setting the vertical alignment top
         |Middle|  Setting the vertical alignment middle
         |Bottom|  Setting the vertical alignment bottom

        """
        Top: int
        Middle: int
        Bottom: int
        @staticmethod
        def ValueOf(value: int) -> LeaderLineBuilder.VerticalAlignmentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrowType(self) -> DiagrammingArrowtype:
        """
        Getter for property: ( DiagrammingArrowtype NXOpen.D) ArrowType
         Returns the arrow type of the end arrow   
            
         
        """
        pass
    @ArrowType.setter
    def ArrowType(self, arrowTypeOption: DiagrammingArrowtype):
        """
        Setter for property: ( DiagrammingArrowtype NXOpen.D) ArrowType
         Returns the arrow type of the end arrow   
            
         
        """
        pass
    @property
    def StubLength(self) -> float:
        """
        Getter for property: (float) StubLength
         Returns the stub length of this leader line.  
           The negative value is not expected.  
         
        """
        pass
    @StubLength.setter
    def StubLength(self, stubLength: float):
        """
        Setter for property: (float) StubLength
         Returns the stub length of this leader line.  
           The negative value is not expected.  
         
        """
        pass
    @property
    def StubSides(self) -> DiagrammingStubsides:
        """
        Getter for property: ( DiagrammingStubsides NXOpen.D) StubSides
         Returns the stub sides of this leader line.  
            
         
        """
        pass
    @StubSides.setter
    def StubSides(self, stubSides: DiagrammingStubsides):
        """
        Setter for property: ( DiagrammingStubsides NXOpen.D) StubSides
         Returns the stub sides of this leader line.  
            
         
        """
        pass
    @property
    def VerticalAlignment(self) -> LeaderLineBuilder.VerticalAlignmentOption:
        """
        Getter for property: ( LeaderLineBuilder.VerticalAlignmentOption NXOpen.D) VerticalAlignment
         Returns the vertical alignment option.  
             
         
        """
        pass
    @VerticalAlignment.setter
    def VerticalAlignment(self, alignmentOption: LeaderLineBuilder.VerticalAlignmentOption):
        """
        Setter for property: ( LeaderLineBuilder.VerticalAlignmentOption NXOpen.D) VerticalAlignment
         Returns the vertical alignment option.  
             
         
        """
        pass
    def GetBendPoints(self) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the leader line. 
         Returns points ( NXOpen.Point2d Li): .
        """
        pass
    def GetTerminator(self) -> Tuple[SheetElement, int, float, float, float, float]:
        """
         Gets the terminator of the leader. 
         Returns A tuple consisting of (terminator, segmentId, percentX, inputX, percentY, inputY). 
         - terminator is:  SheetElement NXOpen.D.
         - segmentId is: int.
         - percentX is: float.
         - inputX is: float.
         - percentY is: float.
         - inputY is: float.

        """
        pass
    def SetBendPoints(self, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the leader line. 
        """
        pass
    def SetTerminator(self, terminator: SheetElement, segmentId: int, percentX: float, inputX: float, percentY: float, inputY: float) -> None:
        """
         Sets the terminator of the leader. 
        """
        pass
import NXOpen
class LeaderLineCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of leader line. """
    def CreateLeaderLineBuilder(self, leaderLine: LeaderLine) -> LeaderLineBuilder:
        """
         Creates a NXOpen.Diagramming.LeaderLineBuilder. 
         Returns builder ( LeaderLineBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> LeaderLine:
        """
         Finds the NXOpen.Diagramming.LeaderLine with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns leaderLine ( LeaderLine NXOpen.D):  NXOpen.Diagramming.LeaderLine with this name. .
        """
        pass
class LeaderLine(Connection): 
    """ Represents the LeaderLine class. """
    pass
class LocationBuilder(BaseSubObjectBuilder): 
    """
    Represents a LocationBuilder.
    """
    @property
    def EvaluatedValueX(self) -> float:
        """
        Getter for property: (float) EvaluatedValueX
         Returns the evaluated X coordinate value that is the result calculated by the input percentage and offset.  
             
         
        """
        pass
    @property
    def EvaluatedValueY(self) -> float:
        """
        Getter for property: (float) EvaluatedValueY
         Returns the evaluated Y coordinate value that is the result calculated by input percentage and offset.  
             
         
        """
        pass
    @property
    def InputPercentX(self) -> float:
        """
        Getter for property: (float) InputPercentX
         Returns the user input percentage (0.  
          0 to 1.0) of the width of the referenced object.   
         
        """
        pass
    @InputPercentX.setter
    def InputPercentX(self, inputPercentX: float):
        """
        Setter for property: (float) InputPercentX
         Returns the user input percentage (0.  
          0 to 1.0) of the width of the referenced object.   
         
        """
        pass
    @property
    def InputPercentY(self) -> float:
        """
        Getter for property: (float) InputPercentY
         Returns the user input percentage (0.  
          0 to 1.0) of the height of the referenced object.   
         
        """
        pass
    @InputPercentY.setter
    def InputPercentY(self, inputPercentY: float):
        """
        Setter for property: (float) InputPercentY
         Returns the user input percentage (0.  
          0 to 1.0) of the height of the referenced object.   
         
        """
        pass
    @property
    def InputValueX(self) -> float:
        """
        Getter for property: (float) InputValueX
         Returns the user input X coordinate.  
          
                    If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value.   
         
        """
        pass
    @InputValueX.setter
    def InputValueX(self, inputValueX: float):
        """
        Setter for property: (float) InputValueX
         Returns the user input X coordinate.  
          
                    If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value.   
         
        """
        pass
    @property
    def InputValueY(self) -> float:
        """
        Getter for property: (float) InputValueY
         Returns the user input Y coordinate.  
          
                    If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value.   
         
        """
        pass
    @InputValueY.setter
    def InputValueY(self, inputValueY: float):
        """
        Setter for property: (float) InputValueY
         Returns the user input Y coordinate.  
          
                    If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value.   
         
        """
        pass
    @property
    def Reference(self) -> SheetElement:
        """
        Getter for property: ( SheetElement NXOpen.D) Reference
         Returns the sheet element whose coordinate system the coordinate is specified in.  
           If this is NULL, the coordinate is in the Sheet's coordinate system.   
         
        """
        pass
    @Reference.setter
    def Reference(self, reference: SheetElement):
        """
        Setter for property: ( SheetElement NXOpen.D) Reference
         Returns the sheet element whose coordinate system the coordinate is specified in.  
           If this is NULL, the coordinate is in the Sheet's coordinate system.   
         
        """
        pass
    @property
    def UpToDate(self) -> bool:
        """
        Getter for property: (bool) UpToDate
         Returns the up to date flag.  
          
                    If true,  NXOpen::Diagramming::LocationBuilder::EvaluatedValueX  and  NXOpen::Diagramming::LocationBuilder::EvaluatedValueY 
                    of  NXOpen::Diagramming::LocationBuilder  may be used; Otherwise it must be evaluated.  
         
        """
        pass
    def SetValueX(self, inputPercent: float, inputValue: float) -> None:
        """
         Set the x value of the location. 
                    The inputPercent means of the x coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
                    The inputValue means the offset value of the x coordinate from the calculated location by the inputPercent value. 
        """
        pass
    def SetValueY(self, inputPercent: float, inputValue: float) -> None:
        """
         Set the y value of the location. 
                    The inputPercent means of the y coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
                    The inputValue means the offset value of the y coordinate from the calculated location by the inputPercent value. 
        """
        pass
class Method(Enum):
    """
    Members Include: 
     |NotSet|  To support legacy parts 
     |Standard|  Standard 
     |Custom| 

    """
    NotSet: int
    Standard: int
    Custom: int
    @staticmethod
    def ValueOf(value: int) -> Method:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NodeBuilder(ConnectableElementBuilder): 
    """
    Represents a NodeBuilder.
    """
    @property
    def Expanded(self) -> bool:
        """
        Getter for property: (bool) Expanded
         Returns the node state of expanded or collapsed.  
           If true the node is expanded.   
         
        """
        pass
    @Expanded.setter
    def Expanded(self, expanded: bool):
        """
        Setter for property: (bool) Expanded
         Returns the node state of expanded or collapsed.  
           If true the node is expanded.   
         
        """
        pass
    @property
    def Fullfillment(self) -> bool:
        """
        Getter for property: (bool) Fullfillment
         Returns the flag that indicates if the node is a fulfillment object.  
           If true the node represents a physical object such as a piece of equipment from a library.   
         
        """
        pass
    @property
    def GroupingAllowed(self) -> bool:
        """
        Getter for property: (bool) GroupingAllowed
         Returns the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
             
         
        """
        pass
    @GroupingAllowed.setter
    def GroupingAllowed(self, fulfillment: bool):
        """
        Setter for property: (bool) GroupingAllowed
         Returns the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
             
         
        """
        pass
    @property
    def OffsheetReference(self) -> Node:
        """
        Getter for property: ( Node NXOpen.D) OffsheetReference
         Returns the referenced offsheet node.  
           It could be elsewhere on the same sheet or on a different sheet and it can be NULL.   
         
        """
        pass
    @OffsheetReference.setter
    def OffsheetReference(self, offsheetReference: Node):
        """
        Setter for property: ( Node NXOpen.D) OffsheetReference
         Returns the referenced offsheet node.  
           It could be elsewhere on the same sheet or on a different sheet and it can be NULL.   
         
        """
        pass
    def AddGroupMember(self, member: SheetElement) -> None:
        """
         Adds a node to this node group. 
        """
        pass
    def RemoveAllGroupMembers(self) -> None:
        """
         Remove all members. 
        """
        pass
    def RemoveGroupMember(self, member: SheetElement) -> None:
        """
         Removes a node from this node group. 
        """
        pass
import NXOpen
class NodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Node. """
    def CreateNodeBuilder(self, node: Node) -> NodeBuilder:
        """
         Creates a NXOpen.Diagramming.NodeBuilder. 
         Returns builder ( NodeBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Node:
        """
         Finds the NXOpen.Diagramming.Node with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns node ( Node NXOpen.D):  NXOpen.Diagramming.Node with this name. .
        """
        pass
class Node(ConnectableElement): 
    """ Represents the Node class. """
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: ( Annotation NXOpen.D) Label
         Returns the label of the sheet element.  
             
         
        """
        pass
    def GetPorts(self) -> List[Port]:
        """
         Get the ports on the node.
         Returns ports ( Port List[NXOpen): .
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
class PopulateTitleBlockBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Diagramming.PopulateTitleBlockBuilder builder """
    def GetCell(self, table: NXOpen.Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> TitleBlockCellBuilder:
        """
         Get the cell builder. 
         Returns cell ( TitleBlockCellBuilder NXOpen.D): .
        """
        pass
    def GetCellValueForLabel(self, label: str) -> str:
        """
         Return the value of the cell for given label. If multiple title blocks are input, 
                then the value of the cell from the first title block, which has the cell with given label, is returned. 
         Returns value (str):  Value of the label .
        """
        pass
    def SetCellValueForLabel(self, label: str, value: str) -> None:
        """
         Sets the value of the cell for given label. If multiple title blocks are selected, 
                then values of cells with the given label in all the title blocks are set. 
        """
        pass
import NXOpen
class PortBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PortBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PortBuilder) -> None:
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
    def Erase(self, obj: PortBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PortBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PortBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PortBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PortBuilder NXOpen.D):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PortBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PortBuilder List[NXOpen):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PortBuilder) -> None:
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
    def SetContents(self, objects: List[PortBuilder]) -> None:
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
    def Swap(self, object1: PortBuilder, object2: PortBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
class PortBuilder(SheetElementBuilder): 
    """
    Represents a PortBuilder.
    """
    @property
    def Direction(self) -> Direction:
        """
        Getter for property: ( Direction NXOpen.D) Direction
         Returns the direction of the port.  
             
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: Direction):
        """
        Setter for property: ( Direction NXOpen.D) Direction
         Returns the direction of the port.  
             
         
        """
        pass
    @property
    def NumberAllowedConnections(self) -> int:
        """
        Getter for property: (int) NumberAllowedConnections
         Returns the maximum number of allowed connections the port may reference.  
             
         
        """
        pass
    @NumberAllowedConnections.setter
    def NumberAllowedConnections(self, numberAllowedConnections: int):
        """
        Setter for property: (int) NumberAllowedConnections
         Returns the maximum number of allowed connections the port may reference.  
             
         
        """
        pass
    @property
    def Pinned(self) -> bool:
        """
        Getter for property: (bool) Pinned
         Returns the flag that indicates the port is pinned.  
           If true the port is pinned and cannot be moved.   
         
        """
        pass
    @Pinned.setter
    def Pinned(self, isPinned: bool):
        """
        Setter for property: (bool) Pinned
         Returns the flag that indicates the port is pinned.  
           If true the port is pinned and cannot be moved.   
         
        """
        pass
    @property
    def Proxy(self) -> Port:
        """
        Getter for property: ( Port NXOpen.D) Proxy
         Returns the proxy port for the port inside the super node.  
             
         
        """
        pass
    @Proxy.setter
    def Proxy(self, proxy: Port):
        """
        Setter for property: ( Port NXOpen.D) Proxy
         Returns the proxy port for the port inside the super node.  
             
         
        """
        pass
    def CanAnotherConnectionBeAdded(self) -> bool:
        """
         Get whether another connection can be added or not. 
         Returns canAnotherConnectionBeAdded (bool): .
        """
        pass
    def GetAllowedParentSides(self) -> Tuple[bool, bool, bool, bool]:
        """
         Get allowed parent sides. 
         Returns A tuple consisting of (isAllowedLeftSide, isAllowedRightSide, isAllowedUpSide, isAllowedDownSide). 
         - isAllowedLeftSide is: bool.
         - isAllowedRightSide is: bool.
         - isAllowedUpSide is: bool.
         - isAllowedDownSide is: bool.

        """
        pass
    def GetConnections(self) -> List[Connection]:
        """
         Get associated connections. 
         Returns connections ( Connection List[NXOpen): .
        """
        pass
    def GetOwningConnectableElement(self) -> ConnectableElement:
        """
         Get the owner connectable element. 
         Returns owner ( ConnectableElement NXOpen.D): .
        """
        pass
    def IsNumberOfConnectionInfinite(self) -> bool:
        """
         Get if the number of connections to reference is infinite. If true it is infinite. 
         Returns isNumberOfConnectionInfinite (bool): .
        """
        pass
import NXOpen
class PortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Port. """
    def CreatePortBuilder(self, port: Port) -> PortBuilder:
        """
         Creates a NXOpen.Diagramming.PortBuilder. 
         Returns builder ( PortBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Port:
        """
         Finds the NXOpen.Diagramming.Port with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns port ( Port NXOpen.D):  NXOpen.Diagramming.Port with this name. .
        """
        pass
class Port(SheetElement): 
    """ Represents the Port class. """
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: ( Annotation NXOpen.D) Label
         Returns the label of the port.  
             
         
        """
        pass
import NXOpen
class ReferenceGeometryBuilder(AnnotationBuilder): 
    """ This builder is used to createedit Reference Geometry """
    @property
    def DisplayBorder(self) -> bool:
        """
        Getter for property: (bool) DisplayBorder
         Returns the setting that determines whether the border should be displayed or not.  
             
         
        """
        pass
    @DisplayBorder.setter
    def DisplayBorder(self, displayBorder: bool):
        """
        Setter for property: (bool) DisplayBorder
         Returns the setting that determines whether the border should be displayed or not.  
             
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale   
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale   
            
         
        """
        pass
    @property
    def Transparency(self) -> int:
        """
        Getter for property: (int) Transparency
         Returns the transparency (between 0 and 100)   
            
         
        """
        pass
    @Transparency.setter
    def Transparency(self, transparency: int):
        """
        Setter for property: (int) Transparency
         Returns the transparency (between 0 and 100)   
            
         
        """
        pass
    @property
    def View(self) -> str:
        """
        Getter for property: (str) View
         Returns the view to import from   
            
         
        """
        pass
    @View.setter
    def View(self, viewIdentifier: str):
        """
        Setter for property: (str) View
         Returns the view to import from   
            
         
        """
        pass
    def GetColor(self) -> List[float]:
        """
         Gets the color 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def RefreshFromView(self, refresh: bool) -> None:
        """
         When set will cause a refresh of the geometry from the drawing view during commit. 
        """
        pass
    def SetColor(self, color: List[float]) -> None:
        """
         Sets the color 
        """
        pass
class ReferenceGeometry(Annotation): 
    """ Represents the Reference Geometry class. """
    pass
import NXOpen
class RenderingPropertiesBuilder(BaseSubObjectBuilder): 
    """
    Represents a RenderingPropertiesBuilder.
    """
    class FillPatterns(Enum):
        """
        Members Include: 
         |NotSet|  No Fill    
         |SolidFill|  Solid Fill 

        """
        NotSet: int
        SolidFill: int
        @staticmethod
        def ValueOf(value: int) -> RenderingPropertiesBuilder.FillPatterns:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FillColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FillColor
         Returns the fill color.  
             
         
        """
        pass
    @FillColor.setter
    def FillColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FillColor
         Returns the fill color.  
             
         
        """
        pass
    @property
    def FillOpacity(self) -> float:
        """
        Getter for property: (float) FillOpacity
         Returns the fill opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    @FillOpacity.setter
    def FillOpacity(self, opacity: float):
        """
        Setter for property: (float) FillOpacity
         Returns the fill opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    @property
    def FillPattern(self) -> RenderingPropertiesBuilder.FillPatterns:
        """
        Getter for property: ( RenderingPropertiesBuilder.FillPatterns NXOpen.D) FillPattern
         Returns the fill type   
            
         
        """
        pass
    @FillPattern.setter
    def FillPattern(self, pattern: RenderingPropertiesBuilder.FillPatterns):
        """
        Setter for property: ( RenderingPropertiesBuilder.FillPatterns NXOpen.D) FillPattern
         Returns the fill type   
            
         
        """
        pass
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font.  
             
         
        """
        pass
    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font.  
             
         
        """
        pass
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @property
    def StrokeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) StrokeColor
         Returns the stroke color.  
             
         
        """
        pass
    @StrokeColor.setter
    def StrokeColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) StrokeColor
         Returns the stroke color.  
             
         
        """
        pass
    @property
    def StrokeOpacity(self) -> float:
        """
        Getter for property: (float) StrokeOpacity
         Returns the stroke opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    @StrokeOpacity.setter
    def StrokeOpacity(self, opacity: float):
        """
        Setter for property: (float) StrokeOpacity
         Returns the stroke opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
class ShapeBuilder(SheetElementBuilder): 
    """
    Represents a ShapeBuilder.
    """
    pass
import NXOpen
class ShapeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Shape. """
    def CreateShapeBuilder(self, shape: Shape) -> ShapeBuilder:
        """
         Creates a NXOpen.Diagramming.ShapeBuilder. 
         Returns builder ( ShapeBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Shape:
        """
         Finds the NXOpen.Diagramming.Shape with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns shape ( Shape NXOpen.D):  NXOpen.Diagramming.Shape with this name. .
        """
        pass
class Shape(ConnectableElement): 
    """ Represents the Shape class. """
    pass
import NXOpen
class SheetBordersAndZonesBuilder(NXOpen.Builder): 
    """ The SheetBordersAndZones builder """
    class ArrowDirectionType(Enum):
        """
        Members Include: 
         |OutofSheet|  Out of Sheet 
         |IntoSheet| 

        """
        OutofSheet: int
        IntoSheet: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ArrowDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ArrowStyleType(Enum):
        """
        Members Include: 
         |Filled|  Filled 
         |Closed|  Closed 
         |ClosedSolid|  Close Solid 
         |Open| 

        """
        Filled: int
        Closed: int
        ClosedSolid: int
        Open: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ArrowStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HorizontalCenteringMarkType(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |LeftArrow|  Left Arrow 
         |RightArrow|   Right Arrow 
         |LeftandRightArrow|  Left and Right Arrow 
         |LeftandRightLine| 

        """
        NotSet: int
        LeftArrow: int
        RightArrow: int
        LeftandRightArrow: int
        LeftandRightLine: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.HorizontalCenteringMarkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TrimmingMarkStyleType(Enum):
        """
        Members Include: 
         |Triangle|  Triangle 
         |Corner| 

        """
        Triangle: int
        Corner: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.TrimmingMarkStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VerticalCenteringMarkType(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |BottomArrow|  Bottom Arrow 
         |TopArrow|  Top Arrow 
         |BottomandTopArrow|  Bottom and Top Arrow 
         |BottomandTopLine| 

        """
        NotSet: int
        BottomArrow: int
        TopArrow: int
        BottomandTopArrow: int
        BottomandTopLine: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.VerticalCenteringMarkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ZoneMethod(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |Standard|  Standard 
         |Custom| 

        """
        NotSet: int
        Standard: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ZoneMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ZoneOrigin(Enum):
        """
        Members Include: 
         |BottomRight|  Bottom Right 
         |TopLeft|  Top Left 
         |TopRight|  Top Right 
         |BottomLeft| 

        """
        BottomRight: int
        TopLeft: int
        TopRight: int
        BottomLeft: int
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ZoneOrigin:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BottomMargin(self) -> float:
        """
        Getter for property: (float) BottomMargin
         Returns the value of the margin in bottom border.  
            
         
        """
        pass
    @BottomMargin.setter
    def BottomMargin(self, bottomMargin: float):
        """
        Setter for property: (float) BottomMargin
         Returns the value of the margin in bottom border.  
            
         
        """
        pass
    @property
    def CenteringMarkExtension(self) -> float:
        """
        Getter for property: (float) CenteringMarkExtension
         Returns the length of centering marks extension from inner border   
            
         
        """
        pass
    @CenteringMarkExtension.setter
    def CenteringMarkExtension(self, centeringMarkExtension: float):
        """
        Setter for property: (float) CenteringMarkExtension
         Returns the length of centering marks extension from inner border   
            
         
        """
        pass
    @property
    def CreateBorders(self) -> bool:
        """
        Getter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    @CreateBorders.setter
    def CreateBorders(self, createBorders: bool):
        """
        Setter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    @property
    def CreateTrimmingMarks(self) -> bool:
        """
        Getter for property: (bool) CreateTrimmingMarks
         Returns the flag that indicate if trimming marks are created.  
             
         
        """
        pass
    @CreateTrimmingMarks.setter
    def CreateTrimmingMarks(self, createTrimmingMarks: bool):
        """
        Setter for property: (bool) CreateTrimmingMarks
         Returns the flag that indicate if trimming marks are created.  
             
         
        """
        pass
    @property
    def CreateZoneLabels(self) -> bool:
        """
        Getter for property: (bool) CreateZoneLabels
         Returns the flag that indicates if zone labels are created.  
             
         
        """
        pass
    @CreateZoneLabels.setter
    def CreateZoneLabels(self, createZoneLabels: bool):
        """
        Setter for property: (bool) CreateZoneLabels
         Returns the flag that indicates if zone labels are created.  
             
         
        """
        pass
    @property
    def CreateZoneMarking(self) -> bool:
        """
        Getter for property: (bool) CreateZoneMarking
         Returns the flag that indicates if zone marking is create.  
             
         
        """
        pass
    @CreateZoneMarking.setter
    def CreateZoneMarking(self, createZoneMarking: bool):
        """
        Setter for property: (bool) CreateZoneMarking
         Returns the flag that indicates if zone marking is create.  
             
         
        """
        pass
    @property
    def HorizontalCenteringMark(self) -> SheetBordersAndZonesBuilder.HorizontalCenteringMarkType:
        """
        Getter for property: ( SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.D) HorizontalCenteringMark
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrowRightArrow.  
             
         
        """
        pass
    @HorizontalCenteringMark.setter
    def HorizontalCenteringMark(self, horizontalCenteringMarkType: SheetBordersAndZonesBuilder.HorizontalCenteringMarkType):
        """
        Setter for property: ( SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.D) HorizontalCenteringMark
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrowRightArrow.  
             
         
        """
        pass
    @property
    def HorizontalSize(self) -> float:
        """
        Getter for property: (float) HorizontalSize
         Returns the size of horizontal zones.  
           It should be greater than zero.   
         
        """
        pass
    @HorizontalSize.setter
    def HorizontalSize(self, horizontalSize: float):
        """
        Setter for property: (float) HorizontalSize
         Returns the size of horizontal zones.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def LabelFont(self) -> int:
        """
        Getter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    @LabelFont.setter
    def LabelFont(self, labelFont: int):
        """
        Setter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the height of the label(text).  
           It should be greater than zero.   
         
        """
        pass
    @LabelHeight.setter
    def LabelHeight(self, labelHeight: float):
        """
        Setter for property: (float) LabelHeight
         Returns the height of the label(text).  
           It should be greater than zero.   
         
        """
        pass
    @property
    def LeftMargin(self) -> float:
        """
        Getter for property: (float) LeftMargin
         Returns the value of the margin in left border.  
            
         
        """
        pass
    @LeftMargin.setter
    def LeftMargin(self, leftMargin: float):
        """
        Setter for property: (float) LeftMargin
         Returns the value of the margin in left border.  
            
         
        """
        pass
    @property
    def MarkingHeight(self) -> float:
        """
        Getter for property: (float) MarkingHeight
         Returns the height of marking.  
           It should be greater than zero.   
         
        """
        pass
    @MarkingHeight.setter
    def MarkingHeight(self, markingHeight: float):
        """
        Setter for property: (float) MarkingHeight
         Returns the height of marking.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def Method(self) -> SheetBordersAndZonesBuilder.ZoneMethod:
        """
        Getter for property: ( SheetBordersAndZonesBuilder.ZoneMethod NXOpen.D) Method
         Returns the type of methods to create the zones.  
             
         
        """
        pass
    @Method.setter
    def Method(self, method: SheetBordersAndZonesBuilder.ZoneMethod):
        """
        Setter for property: ( SheetBordersAndZonesBuilder.ZoneMethod NXOpen.D) Method
         Returns the type of methods to create the zones.  
             
         
        """
        pass
    @property
    def Origin(self) -> SheetBordersAndZonesBuilder.ZoneOrigin:
        """
        Getter for property: ( SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.D) Origin
         Returns the type of zone origin like TopLeftBottomRight.  
             
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: SheetBordersAndZonesBuilder.ZoneOrigin):
        """
        Setter for property: ( SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.D) Origin
         Returns the type of zone origin like TopLeftBottomRight.  
             
         
        """
        pass
    @property
    def RightMargin(self) -> float:
        """
        Getter for property: (float) RightMargin
         Returns the value of the margin in right border.  
            
         
        """
        pass
    @RightMargin.setter
    def RightMargin(self, rightMargin: float):
        """
        Setter for property: (float) RightMargin
         Returns the value of the margin in right border.  
            
         
        """
        pass
    @property
    def SheetBorderSettings(self) -> SheetBorderSettingsBuilder:
        """
        Getter for property: ( SheetBorderSettingsBuilder NXOpen.D) SheetBorderSettings
         Returns the sheet border settings builder used to get the values related to borders  
            
         
        """
        pass
    @property
    def SheetMarginSettings(self) -> SheetMarginSettingsBuilder:
        """
        Getter for property: ( SheetMarginSettingsBuilder NXOpen.D) SheetMarginSettings
         Returns the sheet margin settings builder used to get the values related to margins  
            
         
        """
        pass
    @property
    def SheetZoneSettings(self) -> SheetZoneSettingsBuilder:
        """
        Getter for property: ( SheetZoneSettingsBuilder NXOpen.D) SheetZoneSettings
         Returns the sheet zone settings builder used to get the values related to zones  
            
         
        """
        pass
    @property
    def TopMargin(self) -> float:
        """
        Getter for property: (float) TopMargin
         Returns the value of the margin in top border.  
            
         
        """
        pass
    @TopMargin.setter
    def TopMargin(self, topMargin: float):
        """
        Setter for property: (float) TopMargin
         Returns the value of the margin in top border.  
            
         
        """
        pass
    @property
    def TrimmingMarkLength(self) -> float:
        """
        Getter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @TrimmingMarkLength.setter
    def TrimmingMarkLength(self, trimmingMarkLength: float):
        """
        Setter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def TrimmingMarkThickness(self) -> float:
        """
        Getter for property: (float) TrimmingMarkThickness
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @TrimmingMarkThickness.setter
    def TrimmingMarkThickness(self, trimmingMarkThickness: float):
        """
        Setter for property: (float) TrimmingMarkThickness
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def VerticalCenteringMark(self) -> SheetBordersAndZonesBuilder.VerticalCenteringMarkType:
        """
        Getter for property: ( SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.D) VerticalCenteringMark
         Returns the vertical centering mark  used to show the type of centering mark like TopArrowBottomArrow.  
             
         
        """
        pass
    @VerticalCenteringMark.setter
    def VerticalCenteringMark(self, verticalCenteringMark: SheetBordersAndZonesBuilder.VerticalCenteringMarkType):
        """
        Setter for property: ( SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.D) VerticalCenteringMark
         Returns the vertical centering mark  used to show the type of centering mark like TopArrowBottomArrow.  
             
         
        """
        pass
    @property
    def VerticalSize(self) -> float:
        """
        Getter for property: (float) VerticalSize
         Returns the size of vertical zones.  
           It should be greater than zero.   
         
        """
        pass
    @VerticalSize.setter
    def VerticalSize(self, verticalSize: float):
        """
        Setter for property: (float) VerticalSize
         Returns the size of vertical zones.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    def SetOwningSheet(self, owningSheet: Sheet) -> None:
        """
         Set the owning sheet when the sheet element is created.
                It is not allowed to change the owning sheet when editing the borders and zones. 
        """
        pass
import NXOpen
class SheetBordersAndZonesCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Diagramming.SheetBordersAndZones objects """
    def CreateSheetBordersAndZonesBuilder(self, bordersAndZones: SheetBordersAndZones) -> SheetBordersAndZonesBuilder:
        """
         Creates a borders and zones builder 
         Returns builder ( SheetBordersAndZonesBuilder NXOpen.D):  SheetBordersAndZonesBuilder object .
        """
        pass
    def FindObject(self, name: str) -> SheetBordersAndZones:
        """
          Finds the  NXOpen.Diagramming.SheetBordersAndZones  with the given name. 
                     An exception will be thrown if no object can be found with the given name. 
         Returns bordersAndZones ( SheetBordersAndZones NXOpen.D):   Borders and zones object .
        """
        pass
import NXOpen
class SheetBordersAndZones(NXOpen.NXObject): 
    """ Represents Sheet Borders and Zones"""
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetBorderSettingsBuilder(NXOpen.TaggedObject): 
    """ The SheetBorderSettings builder """
    @property
    def ArrowAngle(self) -> float:
        """
        Getter for property: (float) ArrowAngle
         Returns the angle of arrow in the borders.  
             
         
        """
        pass
    @ArrowAngle.setter
    def ArrowAngle(self, arrowAngle: float):
        """
        Setter for property: (float) ArrowAngle
         Returns the angle of arrow in the borders.  
             
         
        """
        pass
    @property
    def ArrowDirection(self) -> ArrowDirectionType:
        """
        Getter for property: ( ArrowDirectionType NXOpen.D) ArrowDirection
         Returns the direction of arrow like Into Sheet or Out of Sheet.  
             
         
        """
        pass
    @ArrowDirection.setter
    def ArrowDirection(self, arrowDirection: ArrowDirectionType):
        """
        Setter for property: ( ArrowDirectionType NXOpen.D) ArrowDirection
         Returns the direction of arrow like Into Sheet or Out of Sheet.  
             
         
        """
        pass
    @property
    def ArrowHeadTail(self) -> float:
        """
        Getter for property: (float) ArrowHeadTail
         Returns the length of arrow tail.  
             
         
        """
        pass
    @ArrowHeadTail.setter
    def ArrowHeadTail(self, arrowHeadTail: float):
        """
        Setter for property: (float) ArrowHeadTail
         Returns the length of arrow tail.  
             
         
        """
        pass
    @property
    def ArrowLength(self) -> float:
        """
        Getter for property: (float) ArrowLength
         Returns the length of arrow in the borders.  
             
         
        """
        pass
    @ArrowLength.setter
    def ArrowLength(self, arrowLength: float):
        """
        Setter for property: (float) ArrowLength
         Returns the length of arrow in the borders.  
             
         
        """
        pass
    @property
    def ArrowStyle(self) -> ArrowStyleType:
        """
        Getter for property: ( ArrowStyleType NXOpen.D) ArrowStyle
         Returns the type of arrow style like Open, Closed.  
          ..   
         
        """
        pass
    @ArrowStyle.setter
    def ArrowStyle(self, arrowStyle: ArrowStyleType):
        """
        Setter for property: ( ArrowStyleType NXOpen.D) ArrowStyle
         Returns the type of arrow style like Open, Closed.  
          ..   
         
        """
        pass
    @property
    def BorderLineWidth(self) -> float:
        """
        Getter for property: (float) BorderLineWidth
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    @BorderLineWidth.setter
    def BorderLineWidth(self, borderLineWidth: float):
        """
        Setter for property: (float) BorderLineWidth
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def CenteringMarkLength(self) -> float:
        """
        Getter for property: (float) CenteringMarkLength
         Returns the length of centering mark.  
             
         
        """
        pass
    @CenteringMarkLength.setter
    def CenteringMarkLength(self, centeringMarkLength: float):
        """
        Setter for property: (float) CenteringMarkLength
         Returns the length of centering mark.  
             
         
        """
        pass
    @property
    def CenteringMarksColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) CenteringMarksColorWidth
         Returns the color and width of centering marks.  
             
         
        """
        pass
    @property
    def CenteringMarksExtension(self) -> float:
        """
        Getter for property: (float) CenteringMarksExtension
         Returns the length of centering marks extension from inner border.  
             
         
        """
        pass
    @CenteringMarksExtension.setter
    def CenteringMarksExtension(self, centeringMarksExtension: float):
        """
        Setter for property: (float) CenteringMarksExtension
         Returns the length of centering marks extension from inner border.  
             
         
        """
        pass
    @property
    def CenteringMarksHorizontal(self) -> HorizontalCenteringMarkType:
        """
        Getter for property: ( HorizontalCenteringMarkType NXOpen.D) CenteringMarksHorizontal
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrowRightArrow.  
             
         
        """
        pass
    @CenteringMarksHorizontal.setter
    def CenteringMarksHorizontal(self, centeringMarksHorizontal: HorizontalCenteringMarkType):
        """
        Setter for property: ( HorizontalCenteringMarkType NXOpen.D) CenteringMarksHorizontal
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrowRightArrow.  
             
         
        """
        pass
    @property
    def CenteringMarksVertical(self) -> VerticalCenteringMarkType:
        """
        Getter for property: ( VerticalCenteringMarkType NXOpen.D) CenteringMarksVertical
         Returns the vertical centering mark  used to show the type of centering mark like TopArrowBottomArrow.  
             
         
        """
        pass
    @CenteringMarksVertical.setter
    def CenteringMarksVertical(self, centeringMarksVertical: VerticalCenteringMarkType):
        """
        Setter for property: ( VerticalCenteringMarkType NXOpen.D) CenteringMarksVertical
         Returns the vertical centering mark  used to show the type of centering mark like TopArrowBottomArrow.  
             
         
        """
        pass
    @property
    def CreateBorders(self) -> bool:
        """
        Getter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    @CreateBorders.setter
    def CreateBorders(self, createBorders: bool):
        """
        Setter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    @property
    def CreateTrimmingMarks(self) -> bool:
        """
        Getter for property: (bool) CreateTrimmingMarks
         Returns the flag indicates to create trimming marks or not.  
             
         
        """
        pass
    @CreateTrimmingMarks.setter
    def CreateTrimmingMarks(self, createTrimmingMarks: bool):
        """
        Setter for property: (bool) CreateTrimmingMarks
         Returns the flag indicates to create trimming marks or not.  
             
         
        """
        pass
    @property
    def DisplaySheetSizeInBorder(self) -> bool:
        """
        Getter for property: (bool) DisplaySheetSizeInBorder
         Returns the flag indicates to display sheet size in border or not   
            
         
        """
        pass
    @DisplaySheetSizeInBorder.setter
    def DisplaySheetSizeInBorder(self, displaySheetSizeInBorder: bool):
        """
        Setter for property: (bool) DisplaySheetSizeInBorder
         Returns the flag indicates to display sheet size in border or not   
            
         
        """
        pass
    @property
    def DistanceFromInnerBorder(self) -> float:
        """
        Getter for property: (float) DistanceFromInnerBorder
         Returns the distance between inner border and arrow head.  
             
         
        """
        pass
    @DistanceFromInnerBorder.setter
    def DistanceFromInnerBorder(self, distanceInFromInnerBorder: float):
        """
        Setter for property: (float) DistanceFromInnerBorder
         Returns the distance between inner border and arrow head.  
             
         
        """
        pass
    @property
    def InnerLineCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) InnerLineCFW
         Returns the color, font and width of inner border line.  
             
         
        """
        pass
    @property
    def Method(self) -> Method:
        """
        Getter for property: ( Method NXOpen.D) Method
         Returns the type of method to display like StandardCustom   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: Method):
        """
        Setter for property: ( Method NXOpen.D) Method
         Returns the type of method to display like StandardCustom   
            
         
        """
        pass
    @property
    def OuterLineCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) OuterLineCFW
         Returns the color, font and width of outer border line.  
             
         
        """
        pass
    @property
    def TrimmingMarkColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TrimmingMarkColor
         Returns the color of trimming mark.  
             
         
        """
        pass
    @TrimmingMarkColor.setter
    def TrimmingMarkColor(self, trimmingMarkColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TrimmingMarkColor
         Returns the color of trimming mark.  
             
         
        """
        pass
    @property
    def TrimmingMarkLength(self) -> float:
        """
        Getter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @TrimmingMarkLength.setter
    def TrimmingMarkLength(self, trimmingMarkLength: float):
        """
        Setter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @property
    def TrimmingMarkStyle(self) -> TrimmingMarkStyleType:
        """
        Getter for property: ( TrimmingMarkStyleType NXOpen.D) TrimmingMarkStyle
         Returns the type of trimming mark style like Corner or Triangle.  
             
         
        """
        pass
    @TrimmingMarkStyle.setter
    def TrimmingMarkStyle(self, trimmingMarkStyle: TrimmingMarkStyleType):
        """
        Setter for property: ( TrimmingMarkStyleType NXOpen.D) TrimmingMarkStyle
         Returns the type of trimming mark style like Corner or Triangle.  
             
         
        """
        pass
    @property
    def TrimmingMarkWidth(self) -> float:
        """
        Getter for property: (float) TrimmingMarkWidth
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    @TrimmingMarkWidth.setter
    def TrimmingMarkWidth(self, trimmingMarkWidth: float):
        """
        Setter for property: (float) TrimmingMarkWidth
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
import NXOpen
class SheetBuilder(BaseObjectBuilder): 
    """
    Represents a SheetBuilder.
    """
    @property
    def AllowJumpers(self) -> bool:
        """
        Getter for property: (bool) AllowJumpers
         Returns the flag if jumpers are allowed to use where connections cross.  
             
         
        """
        pass
    @AllowJumpers.setter
    def AllowJumpers(self, allowJumper: bool):
        """
        Setter for property: (bool) AllowJumpers
         Returns the flag if jumpers are allowed to use where connections cross.  
             
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    @property
    def JumperType(self) -> DiagrammingJumpertype:
        """
        Getter for property: ( DiagrammingJumpertype NXOpen.D) JumperType
         Returns the jumper type of the sheet.  
             
         
        """
        pass
    @JumperType.setter
    def JumperType(self, jumperType: DiagrammingJumpertype):
        """
        Setter for property: ( DiagrammingJumpertype NXOpen.D) JumperType
         Returns the jumper type of the sheet.  
             
         
        """
        pass
    @property
    def Opacity(self) -> float:
        """
        Getter for property: (float) Opacity
         Returns the opacity of sheet.  
           0.0 is completely transparent and 1.0 is completely opaque  
         
        """
        pass
    @Opacity.setter
    def Opacity(self, opacity: float):
        """
        Setter for property: (float) Opacity
         Returns the opacity of sheet.  
           0.0 is completely transparent and 1.0 is completely opaque  
         
        """
        pass
    @property
    def PaxFileName(self) -> str:
        """
        Getter for property: (str) PaxFileName
         Returns the path name of the PAX file to which the template will be written to.  
             
         
        """
        pass
    @PaxFileName.setter
    def PaxFileName(self, paxFileName: str):
        """
        Setter for property: (str) PaxFileName
         Returns the path name of the PAX file to which the template will be written to.  
             
         
        """
        pass
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
             
         
        """
        pass
    @PresentationName.setter
    def PresentationName(self, presentationName: str):
        """
        Setter for property: (str) PresentationName
         Returns the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
             
         
        """
        pass
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the tooltip that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the tooltip that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    @property
    def Units(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) Units
         Returns the units of the sheet.  
           It could be either "meters" or "inches".   
         
        """
        pass
    @Units.setter
    def Units(self, unit: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) Units
         Returns the units of the sheet.  
           It could be either "meters" or "inches".   
         
        """
        pass
    @property
    def UpdatePAXFile(self) -> bool:
        """
        Getter for property: (bool) UpdatePAXFile
         Returns the flag to update pax file or not.  
            
         
        """
        pass
    @UpdatePAXFile.setter
    def UpdatePAXFile(self, updatePAXFile: bool):
        """
        Setter for property: (bool) UpdatePAXFile
         Returns the flag to update pax file or not.  
            
         
        """
        pass
    def GetFeatures(self) -> List[SheetElement]:
        """
         Gets all features. 
         Returns features ( SheetElement List[NXOpen): .
        """
        pass
    def GetSheetElements(self) -> List[SheetElement]:
        """
         Gets all sheet elements. 
         Returns sheetElements ( SheetElement List[NXOpen): .
        """
        pass
    def GetSize(self) -> Tuple[float, float]:
        """
         Gets the height and width of this sheet. 
         Returns A tuple consisting of (height, width). 
         - height is: float.
         - width is: float.

        """
        pass
    def SetSize(self, height: float, width: float) -> None:
        """
         Sets the height and width of this sheet. 
        """
        pass
import NXOpen
class SheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Sheet. """
    def CreateSheetBuilder(self, sheet: Sheet) -> SheetBuilder:
        """
         Creates a NXOpen.Diagramming.SheetBuilder. 
         Returns builder ( SheetBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Sheet:
        """
         Finds the NXOpen.Diagramming.Sheet with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns sheet ( Sheet NXOpen.D):  NXOpen.Diagramming.Sheet with this name. .
        """
        pass
    def GetWorkSheet(self) -> Sheet:
        """
         Returns the work sheet from part. 
         Returns sheet ( Sheet NXOpen.D): .
        """
        pass
class SheetElementBuilder(BaseObjectBuilder): 
    """
    Represents a SheetElementBuilder.
    """
    class ResizeOptionType(Enum):
        """
        Members Include: 
         |AnyDirection| 
         |OnAnchor| 
         |SameRatio| 
         |SameRationOnCorner| 
         |SameRatioOnEdge| 

        """
        AnyDirection: int
        OnAnchor: int
        SameRatio: int
        SameRationOnCorner: int
        SameRatioOnEdge: int
        @staticmethod
        def ValueOf(value: int) -> SheetElementBuilder.ResizeOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height.  
             
         
        """
        pass
    @property
    def HeightPolicy(self) -> DiagrammingSizingpolicy:
        """
        Getter for property: ( DiagrammingSizingpolicy NXOpen.D) HeightPolicy
         Returns the height policy.  
             
         
        """
        pass
    @HeightPolicy.setter
    def HeightPolicy(self, heightPolicy: DiagrammingSizingpolicy):
        """
        Setter for property: ( DiagrammingSizingpolicy NXOpen.D) HeightPolicy
         Returns the height policy.  
             
         
        """
        pass
    @property
    def Internal(self) -> bool:
        """
        Getter for property: (bool) Internal
         Returns the flag that indicates if the sheet element is internal.  
           If false it is not part of the user's data model; for example, an Annotation is not part of the user's model of Nodes and Connections.   
         
        """
        pass
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: ( Annotation NXOpen.D) Label
         Returns the label of this sheet element.  
             
         
        """
        pass
    @property
    def LabelName(self) -> str:
        """
        Getter for property: (str) LabelName
         Returns the label name of this sheet element.  
             
         
        """
        pass
    @LabelName.setter
    def LabelName(self, labelname: str):
        """
        Setter for property: (str) LabelName
         Returns the label name of this sheet element.  
             
         
        """
        pass
    @property
    def Location(self) -> LocationBuilder:
        """
        Getter for property: ( LocationBuilder NXOpen.D) Location
         Returns the location of the sheet element relative to another sheet element.  
             
         
        """
        pass
    @property
    def LocationStyle(self) -> DiagrammingLocationstyle:
        """
        Getter for property: ( DiagrammingLocationstyle NXOpen.D) LocationStyle
         Returns the location style.  
             
         
        """
        pass
    @LocationStyle.setter
    def LocationStyle(self, locationStyle: DiagrammingLocationstyle):
        """
        Setter for property: ( DiagrammingLocationstyle NXOpen.D) LocationStyle
         Returns the location style.  
             
         
        """
        pass
    @property
    def MirrorX(self) -> bool:
        """
        Getter for property: (bool) MirrorX
         Returns the sheet element to Mirror along the X axis.  
             
         
        """
        pass
    @MirrorX.setter
    def MirrorX(self, mirrorX: bool):
        """
        Setter for property: (bool) MirrorX
         Returns the sheet element to Mirror along the X axis.  
             
         
        """
        pass
    @property
    def MirrorY(self) -> bool:
        """
        Getter for property: (bool) MirrorY
         Returns the sheet element to Mirror along the Y axis.  
             
         
        """
        pass
    @MirrorY.setter
    def MirrorY(self, mirrorY: bool):
        """
        Setter for property: (bool) MirrorY
         Returns the sheet element to Mirror along the Y axis.  
             
         
        """
        pass
    @property
    def Owner(self) -> SheetElement:
        """
        Getter for property: ( SheetElement NXOpen.D) Owner
         Returns the owning sheet element.  
             
         
        """
        pass
    @Owner.setter
    def Owner(self, owner: SheetElement):
        """
        Setter for property: ( SheetElement NXOpen.D) Owner
         Returns the owning sheet element.  
             
         
        """
        pass
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOpen.D) OwningSheet
         Returns the owning sheet.  
             
         
        """
        pass
    @property
    def RenderingProperties(self) -> RenderingPropertiesBuilder:
        """
        Getter for property: ( RenderingPropertiesBuilder NXOpen.D) RenderingProperties
         Returns the renderingProperties of the sheet element.  
            
         
        """
        pass
    @property
    def ResizeOption(self) -> SheetElementBuilder.ResizeOptionType:
        """
        Getter for property: ( SheetElementBuilder.ResizeOptionType NXOpen.D) ResizeOption
         Returns the resize option of the sheet element   
            
         
        """
        pass
    @ResizeOption.setter
    def ResizeOption(self, resizeOption: SheetElementBuilder.ResizeOptionType):
        """
        Setter for property: ( SheetElementBuilder.ResizeOptionType NXOpen.D) ResizeOption
         Returns the resize option of the sheet element   
            
         
        """
        pass
    @property
    def Rotation(self) -> float:
        """
        Getter for property: (float) Rotation
         Returns the rotation angle that is counter clockwise and relative to the owner.  
             
         
        """
        pass
    @Rotation.setter
    def Rotation(self, angle: float):
        """
        Setter for property: (float) Rotation
         Returns the rotation angle that is counter clockwise and relative to the owner.  
             
         
        """
        pass
    @property
    def SourceElement(self) -> SheetElement:
        """
        Getter for property: ( SheetElement NXOpen.D) SourceElement
         Returns the source element that records which sheet element it is a copy of.  
             
         
        """
        pass
    @property
    def UpToDate(self) -> bool:
        """
        Getter for property: (bool) UpToDate
         Returns the flag that indicates if the sheet element is up to date.  
             
         
        """
        pass
    @property
    def Visible(self) -> bool:
        """
        Getter for property: (bool) Visible
         Returns the flag that indicates if the sheet element is visible.  
           If true it is visible.   
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width.  
             
         
        """
        pass
    @property
    def WidthPolicy(self) -> DiagrammingSizingpolicy:
        """
        Getter for property: ( DiagrammingSizingpolicy NXOpen.D) WidthPolicy
         Returns the width policy.  
             
         
        """
        pass
    @WidthPolicy.setter
    def WidthPolicy(self, widthPolicy: DiagrammingSizingpolicy):
        """
        Setter for property: ( DiagrammingSizingpolicy NXOpen.D) WidthPolicy
         Returns the width policy.  
             
         
        """
        pass
    @property
    def X(self) -> float:
        """
        Getter for property: (float) X
         Returns the absolute x coordinate.  
             
         
        """
        pass
    @X.setter
    def X(self, x: float):
        """
        Setter for property: (float) X
         Returns the absolute x coordinate.  
             
         
        """
        pass
    @property
    def Y(self) -> float:
        """
        Getter for property: (float) Y
         Returns the absolute y coordinate.  
             
         
        """
        pass
    @Y.setter
    def Y(self, y: float):
        """
        Setter for property: (float) Y
         Returns the absolute y coordinate.  
             
         
        """
        pass
    @property
    def ZDepth(self) -> int:
        """
        Getter for property: (int) ZDepth
         Returns the Z depth.  
           Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value.   
         
        """
        pass
    @ZDepth.setter
    def ZDepth(self, zDepth: int):
        """
        Setter for property: (int) ZDepth
         Returns the Z depth.  
           Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value.   
         
        """
        pass
    def GetAllowedTransformations(self) -> Tuple[bool, bool, bool, bool]:
        """
         Get the allowed transformations of the sheet element. 
         Returns A tuple consisting of (isAllowedTranslation, isAllowedRotation, isAllowedScale, isAllowedShear). 
         - isAllowedTranslation is: bool.
         - isAllowedRotation is: bool.
         - isAllowedScale is: bool.
         - isAllowedShear is: bool.

        """
        pass
    def GetMinNodeSize(self) -> List[float]:
        """
         Gets the minimum node size values 
         Returns sizeValues (List[float]):  Minimum node size values as output.
        """
        pass
    def SetMinNodeSize(self, sizeValues: List[float]) -> None:
        """
         Sets the minimum node size values 
        """
        pass
    def SetOwningSheet(self, owningSheet: Sheet) -> None:
        """
         Set the owning sheet when the sheet element is created.
                It is not allowed to change the owning sheet when editing the sheet element. 
        """
        pass
class SheetElement(BaseObject): 
    """ Represents the SheetElement class. """
    pass
import NXOpen
class SheetManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    @property
    def ActiveSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOpen.D) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    @ActiveSheet.setter
    def ActiveSheet(self, sheet: Sheet):
        """
        Setter for property: ( Sheet NXOpen.D) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    @property
    def ViewOperations() -> ViewOperations:
        """
         Returns the ViewOperations instance belonging to this session 
        """
        pass
    @property
    def GroupManager() -> GroupManager:
        """
         Returns the GroupManager instance belonging to this session 
        """
        pass
    def OpenSheet(sheet: Sheet) -> None:
        """
         Opens a NXOpen.Diagramming.Sheet. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetMarginSettingsBuilder(NXOpen.TaggedObject): 
    """ The SheetMarginSettings builder """
    @property
    def BottomTrimmedMargin(self) -> float:
        """
        Getter for property: (float) BottomTrimmedMargin
         Returns the value of the margin in bottom border.  
             
         
        """
        pass
    @BottomTrimmedMargin.setter
    def BottomTrimmedMargin(self, bottomTrimmedMargin: float):
        """
        Setter for property: (float) BottomTrimmedMargin
         Returns the value of the margin in bottom border.  
             
         
        """
        pass
    @property
    def BottomUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) BottomUntrimmedMargin
         Returns the distance between bottom of the sheet and bottom trimmed margin.  
             
         
        """
        pass
    @BottomUntrimmedMargin.setter
    def BottomUntrimmedMargin(self, bottomUntrimmedMargin: float):
        """
        Setter for property: (float) BottomUntrimmedMargin
         Returns the distance between bottom of the sheet and bottom trimmed margin.  
             
         
        """
        pass
    @property
    def CreateUntrimmedMargins(self) -> bool:
        """
        Getter for property: (bool) CreateUntrimmedMargins
         Returns the flag indicates to create untrimmed margins or not.  
            
         
        """
        pass
    @CreateUntrimmedMargins.setter
    def CreateUntrimmedMargins(self, createUntrimmedMargins: bool):
        """
        Setter for property: (bool) CreateUntrimmedMargins
         Returns the flag indicates to create untrimmed margins or not.  
            
         
        """
        pass
    @property
    def LeftTrimmedMargin(self) -> float:
        """
        Getter for property: (float) LeftTrimmedMargin
         Returns the value of the margin in left border.  
             
         
        """
        pass
    @LeftTrimmedMargin.setter
    def LeftTrimmedMargin(self, leftTrimmedMargin: float):
        """
        Setter for property: (float) LeftTrimmedMargin
         Returns the value of the margin in left border.  
             
         
        """
        pass
    @property
    def LeftUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) LeftUntrimmedMargin
         Returns the distance between left of the sheet and left trimmed margin.  
             
         
        """
        pass
    @LeftUntrimmedMargin.setter
    def LeftUntrimmedMargin(self, leftUntrimmedMargin: float):
        """
        Setter for property: (float) LeftUntrimmedMargin
         Returns the distance between left of the sheet and left trimmed margin.  
             
         
        """
        pass
    @property
    def MarginLineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) MarginLineColorFontWidth
         Returns the color, font and width of margin line.  
             
         
        """
        pass
    @property
    def RightTrimmedMargin(self) -> float:
        """
        Getter for property: (float) RightTrimmedMargin
         Returns the value of the margin in right border.  
             
         
        """
        pass
    @RightTrimmedMargin.setter
    def RightTrimmedMargin(self, rightTrimmedMargin: float):
        """
        Setter for property: (float) RightTrimmedMargin
         Returns the value of the margin in right border.  
             
         
        """
        pass
    @property
    def RightUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) RightUntrimmedMargin
         Returns the distance between right of the sheet and right trimmed margin.  
             
         
        """
        pass
    @RightUntrimmedMargin.setter
    def RightUntrimmedMargin(self, rightUntrimmedMargin: float):
        """
        Setter for property: (float) RightUntrimmedMargin
         Returns the distance between right of the sheet and right trimmed margin.  
             
         
        """
        pass
    @property
    def TopTrimmedMargin(self) -> float:
        """
        Getter for property: (float) TopTrimmedMargin
         Returns the value of the margin in top border.  
             
         
        """
        pass
    @TopTrimmedMargin.setter
    def TopTrimmedMargin(self, topMargin: float):
        """
        Setter for property: (float) TopTrimmedMargin
         Returns the value of the margin in top border.  
             
         
        """
        pass
    @property
    def TopUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) TopUntrimmedMargin
         Returns the distance between top of the sheet and top trimmed margin.  
             
         
        """
        pass
    @TopUntrimmedMargin.setter
    def TopUntrimmedMargin(self, topUntrimmedMargin: float):
        """
        Setter for property: (float) TopUntrimmedMargin
         Returns the distance between top of the sheet and top trimmed margin.  
             
         
        """
        pass
import NXOpen
class SheetSizeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Diagramming.SheetSizeBuilder builder, and the builder is used to model a sheet size. """
    @property
    def Sheet(self) -> SheetBuilder:
        """
        Getter for property: ( SheetBuilder NXOpen.D) Sheet
         Returns the diagramming sheet builder.  
             
         
        """
        pass
import NXOpen
class SheetTemplateBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Diagramming.SheetTemplateBuilder builder, and the builder is used to model a sheet template. """
    @property
    def Sheet(self) -> SheetBuilder:
        """
        Getter for property: ( SheetBuilder NXOpen.D) Sheet
         Returns the diagramming sheet builder.  
             
         
        """
        pass
    @property
    def SheetSize(self) -> SheetSizeBuilder:
        """
        Getter for property: ( SheetSizeBuilder NXOpen.D) SheetSize
         Returns    the sheet size builder   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetZoneSettingsBuilder(NXOpen.TaggedObject): 
    """ The SheetZoneSettings builder """
    @property
    def ContinueZoneIndexingAcrossSheets(self) -> bool:
        """
        Getter for property: (bool) ContinueZoneIndexingAcrossSheets
         Returns the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
             
         
        """
        pass
    @ContinueZoneIndexingAcrossSheets.setter
    def ContinueZoneIndexingAcrossSheets(self, continueZoneIndexingAcrossSheets: bool):
        """
        Setter for property: (bool) ContinueZoneIndexingAcrossSheets
         Returns the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
             
         
        """
        pass
    @property
    def CornerZoneModification(self) -> float:
        """
        Getter for property: (float) CornerZoneModification
         Returns the corner zone modification used as determine the size of the corner zone.  
             
         
        """
        pass
    @CornerZoneModification.setter
    def CornerZoneModification(self, cornerZoneModification: float):
        """
        Setter for property: (float) CornerZoneModification
         Returns the corner zone modification used as determine the size of the corner zone.  
             
         
        """
        pass
    @property
    def CreateZoneLabels(self) -> bool:
        """
        Getter for property: (bool) CreateZoneLabels
         Returns the flag indicates to create zone labels or not.  
             
         
        """
        pass
    @CreateZoneLabels.setter
    def CreateZoneLabels(self, createZoneLabels: bool):
        """
        Setter for property: (bool) CreateZoneLabels
         Returns the flag indicates to create zone labels or not.  
             
         
        """
        pass
    @property
    def CreateZoneMarkings(self) -> bool:
        """
        Getter for property: (bool) CreateZoneMarkings
         Returns the flag indicates to create zone markings or not.  
             
         
        """
        pass
    @CreateZoneMarkings.setter
    def CreateZoneMarkings(self, createZoneMarkings: bool):
        """
        Setter for property: (bool) CreateZoneMarkings
         Returns the flag indicates to create zone markings or not.  
             
         
        """
        pass
    @property
    def CreateZones(self) -> bool:
        """
        Getter for property: (bool) CreateZones
         Returns the flag indicates to create zones or not.  
             
         
        """
        pass
    @CreateZones.setter
    def CreateZones(self, createZones: bool):
        """
        Setter for property: (bool) CreateZones
         Returns the flag indicates to create zones or not.  
             
         
        """
        pass
    @property
    def HorizontalSize(self) -> float:
        """
        Getter for property: (float) HorizontalSize
         Returns the size of the horizontal zone.  
           It must be greater than zero.   
         
        """
        pass
    @HorizontalSize.setter
    def HorizontalSize(self, horizontalSize: float):
        """
        Setter for property: (float) HorizontalSize
         Returns the size of the horizontal zone.  
           It must be greater than zero.   
         
        """
        pass
    @property
    def LabelColor(self) -> int:
        """
        Getter for property: (int) LabelColor
         Returns the color of the label(text).  
             
         
        """
        pass
    @LabelColor.setter
    def LabelColor(self, labelColor: int):
        """
        Setter for property: (int) LabelColor
         Returns the color of the label(text).  
             
         
        """
        pass
    @property
    def LabelFont(self) -> int:
        """
        Getter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    @LabelFont.setter
    def LabelFont(self, labelFont: int):
        """
        Setter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the height of the label(text).  
             
         
        """
        pass
    @LabelHeight.setter
    def LabelHeight(self, labelHeight: float):
        """
        Setter for property: (float) LabelHeight
         Returns the height of the label(text).  
             
         
        """
        pass
    @property
    def LabelItalicized(self) -> bool:
        """
        Getter for property: (bool) LabelItalicized
         Returns the flag indicates the label(text) is italic or not.  
             
         
        """
        pass
    @LabelItalicized.setter
    def LabelItalicized(self, italic: bool):
        """
        Setter for property: (bool) LabelItalicized
         Returns the flag indicates the label(text) is italic or not.  
             
         
        """
        pass
    @property
    def LabelWidth(self) -> int:
        """
        Getter for property: (int) LabelWidth
         Returns the width of the label(text) like Regular, Bold.  
             
         
        """
        pass
    @LabelWidth.setter
    def LabelWidth(self, labelWidth: int):
        """
        Setter for property: (int) LabelWidth
         Returns the width of the label(text) like Regular, Bold.  
             
         
        """
        pass
    @property
    def LabelsToSkip(self) -> str:
        """
        Getter for property: (str) LabelsToSkip
         Returns the characters to skip in label(text).  
             
         
        """
        pass
    @LabelsToSkip.setter
    def LabelsToSkip(self, labelsToSkip: str):
        """
        Setter for property: (str) LabelsToSkip
         Returns the characters to skip in label(text).  
             
         
        """
        pass
    @property
    def MarkingHeight(self) -> float:
        """
        Getter for property: (float) MarkingHeight
         Returns the height of the marking.  
             
         
        """
        pass
    @MarkingHeight.setter
    def MarkingHeight(self, markingHeight: float):
        """
        Setter for property: (float) MarkingHeight
         Returns the height of the marking.  
             
         
        """
        pass
    @property
    def MarkingLineColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) MarkingLineColorWidth
         Returns the color and width of marking line.  
             
         
        """
        pass
    @property
    def Origin(self) -> ZoneOrigin:
        """
        Getter for property: ( ZoneOrigin NXOpen.D) Origin
         Returns the type of zone origin like TopLeftBottomRight.  
             
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: ZoneOrigin):
        """
        Setter for property: ( ZoneOrigin NXOpen.D) Origin
         Returns the type of zone origin like TopLeftBottomRight.  
             
         
        """
        pass
    @property
    def VerticalSize(self) -> float:
        """
        Getter for property: (float) VerticalSize
         Returns the size of the vertical zone.  
           It must be greater than zero.   
         
        """
        pass
    @VerticalSize.setter
    def VerticalSize(self, verticalSize: float):
        """
        Setter for property: (float) VerticalSize
         Returns the size of the vertical zone.  
           It must be greater than zero.   
         
        """
        pass
class Sheet(BaseObject): 
    """ Represents the Sheet class. """
    def LogGroupToDelete(self, group: Group) -> None:
        """
         Logs a group and all its members to delete. 
        """
        pass
import NXOpen
class SmartDiagrammingManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    def CreateReferenceGeometryBuilder(self, referenceGeometry: ReferenceGeometry) -> ReferenceGeometryBuilder:
        """
         Creates a NXOpen.Diagramming.ReferenceGeometryBuilder. 
         Returns builder ( ReferenceGeometryBuilder NXOpen.D): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TextStyleBuilder(NXOpen.TaggedObject): 
    """
    Represents a TextStyleBuilder.
    """
    class TextAlignmentType(Enum):
        """
        Members Include: 
         |Left| 
         |Center| 
         |Right| 

        """
        Left: int
        Center: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> TextStyleBuilder.TextAlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TextAutoFitType(Enum):
        """
        Members Include: 
         |NotSet| 
         |ResizeOutline| 
         |ShrinkText| 

        """
        NotSet: int
        ResizeOutline: int
        ShrinkText: int
        @staticmethod
        def ValueOf(value: int) -> TextStyleBuilder.TextAutoFitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TruncationModes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Trim| 
         |Suffix| 

        """
        NotSet: int
        Trim: int
        Suffix: int
        @staticmethod
        def ValueOf(value: int) -> TextStyleBuilder.TruncationModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def TextAlignment(self) -> TextStyleBuilder.TextAlignmentType:
        """
        Getter for property: ( TextStyleBuilder.TextAlignmentType NXOpen.D) TextAlignment
         Returns the text alignment of the annotation   
            
         
        """
        pass
    @TextAlignment.setter
    def TextAlignment(self, alignment: TextStyleBuilder.TextAlignmentType):
        """
        Setter for property: ( TextStyleBuilder.TextAlignmentType NXOpen.D) TextAlignment
         Returns the text alignment of the annotation   
            
         
        """
        pass
    @property
    def TextAllowWrapping(self) -> bool:
        """
        Getter for property: (bool) TextAllowWrapping
         Returns the text allow wrapping   
            
         
        """
        pass
    @TextAllowWrapping.setter
    def TextAllowWrapping(self, allowWrapping: bool):
        """
        Setter for property: (bool) TextAllowWrapping
         Returns the text allow wrapping   
            
         
        """
        pass
    @property
    def TextAutoFit(self) -> TextStyleBuilder.TextAutoFitType:
        """
        Getter for property: ( TextStyleBuilder.TextAutoFitType NXOpen.D) TextAutoFit
         Returns the text auto fit   
            
         
        """
        pass
    @TextAutoFit.setter
    def TextAutoFit(self, autoFit: TextStyleBuilder.TextAutoFitType):
        """
        Setter for property: ( TextStyleBuilder.TextAutoFitType NXOpen.D) TextAutoFit
         Returns the text auto fit   
            
         
        """
        pass
    @property
    def TextColorFontWidth(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextColorFontWidth
         Returns the text color font width   
            
         
        """
        pass
    @property
    def TextHeight(self) -> float:
        """
        Getter for property: (float) TextHeight
         Returns the height of the annotation   
            
         
        """
        pass
    @TextHeight.setter
    def TextHeight(self, height: float):
        """
        Setter for property: (float) TextHeight
         Returns the height of the annotation   
            
         
        """
        pass
    @property
    def TextOverlined(self) -> bool:
        """
        Getter for property: (bool) TextOverlined
         Returns whether the text is overlined   
            
         
        """
        pass
    @TextOverlined.setter
    def TextOverlined(self, overlined: bool):
        """
        Setter for property: (bool) TextOverlined
         Returns whether the text is overlined   
            
         
        """
        pass
    @property
    def TextUnderlined(self) -> bool:
        """
        Getter for property: (bool) TextUnderlined
         Returns whether the text is underlined   
            
         
        """
        pass
    @TextUnderlined.setter
    def TextUnderlined(self, underlined: bool):
        """
        Setter for property: (bool) TextUnderlined
         Returns whether the text is underlined   
            
         
        """
        pass
    @property
    def TruncationMode(self) -> TextStyleBuilder.TruncationModes:
        """
        Getter for property: ( TextStyleBuilder.TruncationModes NXOpen.D) TruncationMode
         Returns the text truncation mode   
            
         
        """
        pass
    @TruncationMode.setter
    def TruncationMode(self, truncation: TextStyleBuilder.TruncationModes):
        """
        Setter for property: ( TextStyleBuilder.TruncationModes NXOpen.D) TruncationMode
         Returns the text truncation mode   
            
         
        """
        pass
import NXOpen
class TitleBlockCellBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TitleBlockCellBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TitleBlockCellBuilder) -> None:
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
    def Erase(self, obj: TitleBlockCellBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TitleBlockCellBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TitleBlockCellBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TitleBlockCellBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TitleBlockCellBuilder NXOpen.D):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TitleBlockCellBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( TitleBlockCellBuilder List[NXOpen):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TitleBlockCellBuilder) -> None:
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
    def SetContents(self, objects: List[TitleBlockCellBuilder]) -> None:
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
    def Swap(self, object1: TitleBlockCellBuilder, object2: TitleBlockCellBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TitleBlockCellBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder to edit NXOpen.Diagramming.TitleBlock's cell 
    """
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the cell label   
            
         
        """
        pass
    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the cell label   
            
         
        """
        pass
    @property
    def Lock(self) -> bool:
        """
        Getter for property: (bool) Lock
         Returns the lock status   
            
         
        """
        pass
    @Lock.setter
    def Lock(self, lockStatus: bool):
        """
        Setter for property: (bool) Lock
         Returns the lock status   
            
         
        """
        pass
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the editable text of the cell   
            
         
        """
        pass
    @Value.setter
    def Value(self, text: str):
        """
        Setter for property: (str) Value
         Returns the editable text of the cell   
            
         
        """
        pass
import NXOpen
class TitleBlockCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Title Block. """
    def CreateDefineTitleBlockBuilder(self, titleBlock: TitleBlock) -> DefineTitleBlockBuilder:
        """
         Creates a NXOpen.Diagramming.DefineTitleBlockBuilder. 
         Returns builder ( DefineTitleBlockBuilder NXOpen.D): .
        """
        pass
    def CreatePopulateTitleBlockBuilder(self, titleBlocks: List[TitleBlock]) -> PopulateTitleBlockBuilder:
        """
         Creates a NXOpen.Diagramming.PopulateTitleBlockBuilder. 
         Returns builder ( PopulateTitleBlockBuilder NXOpen.D): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> TitleBlock:
        """
         Finds the NXOpen.Diagramming.TitleBlock with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns titleBlock ( TitleBlock NXOpen.D):  NXOpen.Diagramming.TitleBlock with this name. .
        """
        pass
import NXOpen
class TitleBlock(NXOpen.NXObject): 
    """ Represents a NXOpen.Diagramming.TitleBlock """
    pass
class TrimmingMarkStyleType(Enum):
    """
    Members Include: 
     |Triangle|  Triangle 
     |Corner| 

    """
    Triangle: int
    Corner: int
    @staticmethod
    def ValueOf(value: int) -> TrimmingMarkStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class VerticalCenteringMarkType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |BottomArrow|  Bottom Arrow 
     |TopArrow|  Top Arrow 
     |BottomandTopArrow|  Bottom and Top Arrow 
     |BottomandTopLine| 

    """
    NotSet: int
    BottomArrow: int
    TopArrow: int
    BottomandTopArrow: int
    BottomandTopLine: int
    @staticmethod
    def ValueOf(value: int) -> VerticalCenteringMarkType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ViewOperations(NXOpen.Object): 
    """
     View operations to be performed on a Diagramming.Sheet.
    """
    def Fit(sheet: Sheet) -> None:
        """
         Fits the sheet 
        """
        pass
    def FitToElements(sheet: Sheet, elements: List[SheetElement]) -> None:
        """
         Fits the sheet to the given objects 
        """
        pass
    def FitToSelection(sheet: Sheet) -> None:
        """
         Fits the sheet to the currently selected objects 
        """
        pass
    def Scale(sheet: Sheet, scale: float) -> None:
        """
         Zooms the sheet to a given scale 
        """
        pass
    def SetViewport(sheet: Sheet, x: float, y: float, width: float, height: float) -> None:
        """
         Pans the sheet to the given location 
        """
        pass
class ZoneOrigin(Enum):
    """
    Members Include: 
     |BottomRight|  Bottom Right 
     |TopLeft|  Top Left 
     |TopRight|  Top Right 
     |BottomLeft| 

    """
    BottomRight: int
    TopLeft: int
    TopRight: int
    BottomLeft: int
    @staticmethod
    def ValueOf(value: int) -> ZoneOrigin:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
