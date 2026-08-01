from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AnchorLocation(Enum):
    """
    Members Include: 
     |TopLeft|  Top left anchor location 
     |TopRight|  Top right anchor location 
     |BottomLeft|  Bottom left anchor location 
     |BottomRight|  Bottom right anchor location 

    """
    TopLeft: int
    TopRight: int
    BottomLeft: int
    BottomRight: int
    @staticmethod
    def ValueOf(value: int) -> AnchorLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class CellBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a CellBuilder.
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
        def ValueOf(value: int) -> CellBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BottomBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) BottomBorder
         Returns the bottom border line rendering properties.  
             
         
        """
        pass
    @BottomBorder.setter
    def BottomBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) BottomBorder
         Returns the bottom border line rendering properties.  
             
         
        """
        pass
    @property
    def FormattedStringBuilder(self) -> NXOpen.Diagramming.FormattedStringBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.FormattedStringBuilder) FormattedStringBuilder
         Returns the formatted string of the text.  
             
         
        """
        pass
    @property
    def LeftBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) LeftBorder
         Returns the left border line rendering properties.  
             
         
        """
        pass
    @LeftBorder.setter
    def LeftBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) LeftBorder
         Returns the left border line rendering properties.  
             
         
        """
        pass
    @property
    def Locked(self) -> bool:
        """
        Getter for property: (bool) Locked
         Returns the locked flag.  
             
         
        """
        pass
    @Locked.setter
    def Locked(self, locked: bool):
        """
        Setter for property: (bool) Locked
         Returns the locked flag.  
             
         
        """
        pass
    @property
    def Padding(self) -> float:
        """
        Getter for property: (float) Padding
         Returns the cell padding.  
             
         
        """
        pass
    @Padding.setter
    def Padding(self, padding: float):
        """
        Setter for property: (float) Padding
         Returns the cell padding.  
             
         
        """
        pass
    @property
    def RightBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) RightBorder
         Returns the right border line rendering properties.  
             
         
        """
        pass
    @RightBorder.setter
    def RightBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) RightBorder
         Returns the right border line rendering properties.  
             
         
        """
        pass
    @property
    def Text(self) -> str:
        """
        Getter for property: (str) Text
         Returns the text on cell.  
             
         
        """
        pass
    @Text.setter
    def Text(self, strValue: str):
        """
        Setter for property: (str) Text
         Returns the text on cell.  
             
         
        """
        pass
    @property
    def TopBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) TopBorder
         Returns the top border line rendering properties.  
             
         
        """
        pass
    @TopBorder.setter
    def TopBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) TopBorder
         Returns the top border line rendering properties.  
             
         
        """
        pass
    def DeleteCellSettings(self) -> None:
        """
         Delete cellsettings. 
        """
        pass
    def DeleteContent(self) -> None:
        """
         Delete cell contents. 
        """
        pass
    def GetCellSettings(self) -> CellSettingsBuilder:
        """
         Gets cell settings. 
         Returns cellSettings ( CellSettingsBuilder NXOpen.Diagr): .
        """
        pass
    def GetContent(self) -> List[SizedSymbol]:
        """
         Gets cell content. 
         Returns symbols ( SizedSymbol List[NXOpen.Dia): .
        """
        pass
    def Inherit(self, inheritOption: CellBuilder.InheritOption, elementToInheritFrom: NXOpen.TaggedObject) -> None:
        """
         Inherit. elementToInheritFrom must be Table or Cell object
        """
        pass
    def SetContent(self, symbols: List[SizedSymbol]) -> None:
        """
         Sets cell content. 
        """
        pass
    def SetImageFileLocation(self, fileName: str) -> None:
        """
         Sets cell image file location. 
        """
        pass
    def SetSVG(self, strValue: str, width: float, height: float) -> None:
        """
         Sets the SVG image on the cell. Passing widthheight in as zero will use cells size. This will override any current SVG or Text 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class CellRangeBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a CellRangeBuilder.
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
        def ValueOf(value: int) -> CellRangeBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanHide(self) -> bool:
        """
        Getter for property: (bool) CanHide
         Returns the can hide flag.  
             
         
        """
        pass
    @CanHide.setter
    def CanHide(self, canHide: bool):
        """
        Setter for property: (bool) CanHide
         Returns the can hide flag.  
             
         
        """
        pass
    @property
    def Hidden(self) -> bool:
        """
        Getter for property: (bool) Hidden
         Returns the hidden flag.  
             
         
        """
        pass
    @Hidden.setter
    def Hidden(self, hidden: bool):
        """
        Setter for property: (bool) Hidden
         Returns the hidden flag.  
             
         
        """
        pass
    @property
    def Size(self) -> float:
        """
        Getter for property: (float) Size
         Returns the size.  
             
         
        """
        pass
    @Size.setter
    def Size(self, size: float):
        """
        Setter for property: (float) Size
         Returns the size.  
             
         
        """
        pass
    @property
    def SizingMethod(self) -> SizingMethod:
        """
        Getter for property: ( SizingMethod NXOpen.Diagr) SizingMethod
         Returns the sizing method.  
             
         
        """
        pass
    @SizingMethod.setter
    def SizingMethod(self, sizingMethod: SizingMethod):
        """
        Setter for property: ( SizingMethod NXOpen.Diagr) SizingMethod
         Returns the sizing method.  
             
         
        """
        pass
    def Inherit(self, inheritOption: CellRangeBuilder.InheritOption, elementToInheritFrom: NXOpen.TaggedObject) -> None:
        """
         Inherit. 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class CellSettingsBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a CellSettingsBuilder.
        """
    @property
    def ContentAlignment(self) -> ContentAlignment:
        """
        Getter for property: ( ContentAlignment NXOpen.Diagr) ContentAlignment
         Returns the content alignment of the cell settings.  
             
         
        """
        pass
    @ContentAlignment.setter
    def ContentAlignment(self, contentAlignment: ContentAlignment):
        """
        Setter for property: ( ContentAlignment NXOpen.Diagr) ContentAlignment
         Returns the content alignment of the cell settings.  
             
         
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
    def OverflowBehavior(self) -> OverflowBehavior:
        """
        Getter for property: ( OverflowBehavior NXOpen.Diagr) OverflowBehavior
         Returns the overflow behavior of the cell settings.  
             
         
        """
        pass
    @OverflowBehavior.setter
    def OverflowBehavior(self, overflowBehavior: OverflowBehavior):
        """
        Setter for property: ( OverflowBehavior NXOpen.Diagr) OverflowBehavior
         Returns the overflow behavior of the cell settings.  
             
         
        """
        pass
    @property
    def TextDirection(self) -> TextDirection:
        """
        Getter for property: ( TextDirection NXOpen.Diagr) TextDirection
         Returns the text direction.  
           The default text direction is 0 for horizontal left-reading text orientation.   
         
        """
        pass
    @TextDirection.setter
    def TextDirection(self, textDirection: TextDirection):
        """
        Setter for property: ( TextDirection NXOpen.Diagr) TextDirection
         Returns the text direction.  
           The default text direction is 0 for horizontal left-reading text orientation.   
         
        """
        pass
    @property
    def ZeroDisplay(self) -> ZeroDisplay:
        """
        Getter for property: ( ZeroDisplay NXOpen.Diagr) ZeroDisplay
         Returns the zero display of the cell settings.  
             
         
        """
        pass
    @ZeroDisplay.setter
    def ZeroDisplay(self, zeroDisplay: ZeroDisplay):
        """
        Setter for property: ( ZeroDisplay NXOpen.Diagr) ZeroDisplay
         Returns the zero display of the cell settings.  
             
         
        """
        pass
    def GetContentTextStyle(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
         Gets context text style . 
         Returns textStyle ( NXOpen.Diagramming.TextStyleBuilder): .
        """
        pass
import NXOpen
class Cell(NXOpen.TaggedObject): 
    """ Represents the Cell class. """
    pass
class ColumnBuilder(CellRangeBuilder): 
    """
        Represents a ColumnBuilder.
        """
    def SetWidth(self, size: float) -> None:
        """
         The method to set the width of a column. 
        """
        pass
class ContentAlignment(Enum):
    """
    Members Include: 
     |TopLeft|  Top left content alignment 
     |TopCenter|  Top center content alignment 
     |TopRight|  Top right content alignment 
     |MiddleLeft|  Middle left content alignment 
     |MiddleCenter|  Middle center content alignment 
     |MiddleRight|  Middle right content alignment 
     |BottomLeft|  Bottom left content alignment 
     |BottomCenter|  Bottom center content alignment 
     |BottomRight|  Bottom right content alignment 

    """
    TopLeft: int
    TopCenter: int
    TopRight: int
    MiddleLeft: int
    MiddleCenter: int
    MiddleRight: int
    BottomLeft: int
    BottomCenter: int
    BottomRight: int
    @staticmethod
    def ValueOf(value: int) -> ContentAlignment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.Diagramming
class ContinuationDataBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a ContinuationDataBuilder.
        """
    @property
    def Location(self) -> ContinuationLocation:
        """
        Getter for property: ( ContinuationLocation NXOpen.Diagr) Location
         Returns the location to continue a table if it won't fit.  
             
         
        """
        pass
    @Location.setter
    def Location(self, location: ContinuationLocation):
        """
        Setter for property: ( ContinuationLocation NXOpen.Diagr) Location
         Returns the location to continue a table if it won't fit.  
             
         
        """
        pass
    @property
    def MaximumSize(self) -> float:
        """
        Getter for property: (float) MaximumSize
         Returns the maximum size of any section of a table.  
             
         
        """
        pass
    @MaximumSize.setter
    def MaximumSize(self, maximumSize: float):
        """
        Setter for property: (float) MaximumSize
         Returns the maximum size of any section of a table.  
             
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns the spacing between sections of a table.  
             
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns the spacing between sections of a table.  
             
         
        """
        pass
class ContinuationLocation(Enum):
    """
    Members Include: 
     |Up|  Up continuation location 
     |Down|  Down continuation location 
     |Left|  Left continuation location 
     |Right|  Right continuation location 
     |NextSheet|  Next sheet continuation location 

    """
    Up: int
    Down: int
    Left: int
    Right: int
    NextSheet: int
    @staticmethod
    def ValueOf(value: int) -> ContinuationLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class HeaderLocation(Enum):
    """
    Members Include: 
     |Start|  Start header location 
     |End|  End header location 

    """
    Start: int
    End: int
    @staticmethod
    def ValueOf(value: int) -> HeaderLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class HeaderOrientation(Enum):
    """
    Members Include: 
     |Vertical|  Vertical header orientation 
     |Horizontal|  Horizontal header orientation 

    """
    Vertical: int
    Horizontal: int
    @staticmethod
    def ValueOf(value: int) -> HeaderOrientation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class OverflowBehavior(Enum):
    """
    Members Include: 
     |Wrap|  Wrap overflow behavior 
     |Truncate|  Truncate overflow behavior 
     |OverflowBorder|  Overflow border overflow behavior 
     |ShrinkToFit|  Shrink to fit overflow behavior 
     |Suffix|  Suffix overflow behavior 

    """
    Wrap: int
    Truncate: int
    OverflowBorder: int
    ShrinkToFit: int
    Suffix: int
    @staticmethod
    def ValueOf(value: int) -> OverflowBehavior:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class RowBuilder(CellRangeBuilder): 
    """
        Represents a RowBuilder.
        """
    def SetHeight(self, size: float) -> None:
        """
         The method to set the height of a row. 
        """
        pass
class SizedSymbol:
    """
     Represents sized symbol information. 
    """
    @property
    def PaddingFromLastSymbol(self) -> float:
        """
        Getter for property PaddingFromLastSymbol
        Padding from last symbol

        """
        pass
    @PaddingFromLastSymbol.setter
    def PaddingFromLastSymbol(self, value: float):
        """
        Getter for property PaddingFromLastSymbol
        Padding from last symbol
        Setter for property PaddingFromLastSymbol
        Padding from last symbol

        """
        pass
    @property
    def Symbol(self) -> NXOpen.TaggedObject:
        """
        Getter for property Symbol
        The symbol

        """
        pass
    @Symbol.setter
    def Symbol(self, value: NXOpen.TaggedObject):
        """
        Getter for property Symbol
        The symbol
        Setter for property Symbol
        The symbol

        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property Height
        The symbol height

        """
        pass
    @Height.setter
    def Height(self, value: float):
        """
        Getter for property Height
        The symbol height
        Setter for property Height
        The symbol height

        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property Width
        The symbol width

        """
        pass
    @Width.setter
    def Width(self, value: float):
        """
        Getter for property Width
        The symbol width
        Setter for property Width
        The symbol width

        """
        pass
class SizingMethod(Enum):
    """
    Members Include: 
     |Auto|  Auto sizing method 
     |Fixed|  Fixed sizing method 

    """
    Auto: int
    Fixed: int
    @staticmethod
    def ValueOf(value: int) -> SizingMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class TableBuilder(NXOpen.Diagramming.AnnotationBuilder): 
    """
        Represents a TableBuilder.
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
        def ValueOf(value: int) -> TableBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BottomBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) BottomBorder
         Returns the bottom border rendering properties.  
             
         
        """
        pass
    @property
    def CellSettingsBuilder(self) -> CellSettingsBuilder:
        """
        Getter for property: ( CellSettingsBuilder NXOpen.Diagr) CellSettingsBuilder
         Returns the default cell border settings.  
             
         
        """
        pass
    @property
    def ContinuationDataBuilder(self) -> ContinuationDataBuilder:
        """
        Getter for property: ( ContinuationDataBuilder NXOpen.Diagr) ContinuationDataBuilder
         Returns the continuation data.  
             
         
        """
        pass
    @property
    def DefaultBottomBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) DefaultBottomBorder
         Returns the default bottom border rendering properties.  
             
         
        """
        pass
    @property
    def DefaultRightBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) DefaultRightBorder
         Returns the default right border rendering properties.  
             
         
        """
        pass
    @property
    def InitialColumnWidth(self) -> float:
        """
        Getter for property: (float) InitialColumnWidth
         Returns the initial width of column.  
             
         
        """
        pass
    @InitialColumnWidth.setter
    def InitialColumnWidth(self, columnWidth: float):
        """
        Setter for property: (float) InitialColumnWidth
         Returns the initial width of column.  
             
         
        """
        pass
    @property
    def LeftBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) LeftBorder
         Returns the left border rendering properties.  
             
         
        """
        pass
    @property
    def Locked(self) -> bool:
        """
        Getter for property: (bool) Locked
         Returns the locked flag.  
             
         
        """
        pass
    @Locked.setter
    def Locked(self, locked: bool):
        """
        Setter for property: (bool) Locked
         Returns the locked flag.  
             
         
        """
        pass
    @property
    def RightBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) RightBorder
         Returns the right border rendering properties.  
             
         
        """
        pass
    @property
    def TableSettingsBuilder(self) -> TableSettingsBuilder:
        """
        Getter for property: ( TableSettingsBuilder NXOpen.Diagr) TableSettingsBuilder
         Returns the table settings.  
             
         
        """
        pass
    @property
    def TopBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) TopBorder
         Returns the top border rendering properties.  
             
         
        """
        pass
    def GetCell(self, rowIndex: int, columnIndex: int) -> CellBuilder:
        """
         The method to get the cell at the given row and column indexes. 
         Returns cell ( CellBuilder NXOpen.Diagr): .
        """
        pass
    def GetColumn(self, columnIndex: int) -> ColumnBuilder:
        """
         The method to get the column at the given column index. 
         Returns column ( ColumnBuilder NXOpen.Diagr): .
        """
        pass
    def GetFillColor(self) -> Tuple[NXOpen.NXColor, float]:
        """
         The method to get the fill color. 
         Returns A tuple consisting of (color, opacity). 
         - color is:  NXOpen.NXColor.
         - opacity is: float.

        """
        pass
    def GetHeader(self, headerIndex: int) -> CellRangeBuilder:
        """
         The method to get the header at the given header index. 
         Returns header ( CellRangeBuilder NXOpen.Diagr): .
        """
        pass
    def GetHeaderCell(self, rowIndex: int, columnIndex: int) -> CellBuilder:
        """
         The method to get the header cell at the given row and column indexes. 
         Returns cell ( CellBuilder NXOpen.Diagr): .
        """
        pass
    def GetNumberOfColumns(self) -> int:
        """
         Returns the initial number of columns. 
         Returns numColumns (int): .
        """
        pass
    def GetNumberOfHeaders(self) -> int:
        """
         Returns the number of headers. 
         Returns numHeaders (int): .
        """
        pass
    def GetNumberOfRows(self) -> int:
        """
         Returns the number of rows. 
         Returns numRows (int): .
        """
        pass
    def GetRow(self, rowIndex: int) -> RowBuilder:
        """
         The method to get the row at the given row index. 
         Returns row ( RowBuilder NXOpen.Diagr): .
        """
        pass
    def Inherit(self, inheritOption: TableBuilder.InheritOption, annotation: NXOpen.Diagramming.Annotation) -> None:
        """
         Inherit. 
        """
        pass
    def InsertColumns(self, columnIndex: int, numColumns: int) -> None:
        """
         The method to insert the given number of columns after the given column index. 
        """
        pass
    def InsertHeaders(self, headerIndex: int, numHeaders: int) -> None:
        """
         The method to insert the given number of headers after the given header index. 
        """
        pass
    def InsertRows(self, rowIndex: int, numRows: int) -> None:
        """
         The method to insert the given number of rows after the given row index. 
        """
        pass
    def MergeCells(self, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        """
         The method to merge the cells in the given ranges. 
        """
        pass
    def MergeHeaderCells(self, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        """
         The method to merge the header cells in the given ranges. 
        """
        pass
    def RemoveColumns(self, columnIndex: int, numColumns: int) -> None:
        """
         The method to remove the given number of columns starting with the given column index. 
        """
        pass
    def RemoveHeaders(self, headerIndex: int, numHeaders: int) -> None:
        """
         The method to remove the given number of headers starting with the given header index. 
        """
        pass
    def RemoveRows(self, rowIndex: int, numRows: int) -> None:
        """
         The method to remove the given number of rows starting with the given row index. 
        """
        pass
    def SetFillColor(self, color: NXOpen.NXColor, opacity: float) -> None:
        """
         The method to set the fill color. 
        """
        pass
    def UnMergeCell(self, rowIndex: int, columnIndex: int) -> None:
        """
         The method to unmerge the cell at the given row and column indexes. 
        """
        pass
    def UnMergeHeaderCell(self, rowIndex: int, columnIndex: int) -> None:
        """
         The method to unmerge the header cell at the given row and column indexes. 
        """
        pass
import NXOpen
class TableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Table. """
    def CreateTableBuilder(self, table: Table) -> TableBuilder:
        """
         Creates a NXOpen.Diagramming.Tables.TableBuilder. 
         Returns builder ( TableBuilder NXOpen.Diagr): .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Table:
        """
         Finds the NXOpen.Diagramming.Tables.Table with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         Returns table ( Table NXOpen.Diagr):  NXOpen.Diagramming.Tables.Table with this name. .
        """
        pass
import NXOpen.Diagramming
class TableSettingsBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a TableSettingsBuilder.
        """
    @property
    def AnchorLocation(self) -> AnchorLocation:
        """
        Getter for property: ( AnchorLocation NXOpen.Diagr) AnchorLocation
         Returns the anchor location of the table settings.  
             
         
        """
        pass
    @AnchorLocation.setter
    def AnchorLocation(self, anchorLocation: AnchorLocation):
        """
        Setter for property: ( AnchorLocation NXOpen.Diagr) AnchorLocation
         Returns the anchor location of the table settings.  
             
         
        """
        pass
    @property
    def HeaderLocation(self) -> HeaderLocation:
        """
        Getter for property: ( HeaderLocation NXOpen.Diagr) HeaderLocation
         Returns the header location of the table settings.  
             
         
        """
        pass
    @HeaderLocation.setter
    def HeaderLocation(self, headerLocation: HeaderLocation):
        """
        Setter for property: ( HeaderLocation NXOpen.Diagr) HeaderLocation
         Returns the header location of the table settings.  
             
         
        """
        pass
    @property
    def HeaderOrientation(self) -> HeaderOrientation:
        """
        Getter for property: ( HeaderOrientation NXOpen.Diagr) HeaderOrientation
         Returns the header orientation of the table settings.  
             
         
        """
        pass
    @HeaderOrientation.setter
    def HeaderOrientation(self, headerOrientation: HeaderOrientation):
        """
        Setter for property: ( HeaderOrientation NXOpen.Diagr) HeaderOrientation
         Returns the header orientation of the table settings.  
             
         
        """
        pass
    @property
    def ProtectedFlag(self) -> bool:
        """
        Getter for property: (bool) ProtectedFlag
         Returns the protected flag.  
             
         
        """
        pass
    @ProtectedFlag.setter
    def ProtectedFlag(self, flag: bool):
        """
        Setter for property: (bool) ProtectedFlag
         Returns the protected flag.  
             
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
class Table(NXOpen.Diagramming.Annotation): 
    """ Represents the Table class. """
    def GetCell(self, rowIndex: int, columnIndex: int, isHeader: bool) -> NXOpen.TaggedObject:
        """
         Gets the table cell by the row and column index.
         Returns cell ( NXOpen.TaggedObject): .
        """
        pass
    def GetTitleBlock(self) -> NXOpen.Diagramming.TitleBlock:
        """
         Get the title block attached to the table.
         Returns titleBlock ( NXOpen.Diagramming.TitleBlock): .
        """
        pass
    def RemoveTitleBlock(self) -> None:
        """
         Remove the title block attached to the table.
        """
        pass
class TextDirection(Enum):
    """
    Members Include: 
     |Horizontal|  Horizontal left-reading text orientation 
     |VerticalRightReading|  Vertical text rotated from horizontal 270 degrees clockwise 
     |VerticalLeftReading|  Vertical text rotated from horizontal 90 degrees clockwise 

    """
    Horizontal: int
    VerticalRightReading: int
    VerticalLeftReading: int
    @staticmethod
    def ValueOf(value: int) -> TextDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ZeroDisplay(Enum):
    """
    Members Include: 
     |Zero|  Zero filled display 
     |Dash|  Dash filled display 
     |Empty|  Empty zero display 

    """
    Zero: int
    Dash: int
    Empty: int
    @staticmethod
    def ValueOf(value: int) -> ZeroDisplay:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
