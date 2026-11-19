from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Represents the table anchor location. 
##  Top left anchor location 
class AnchorLocation(Enum):
    """
    Members Include: <TopLeft> <TopRight> <BottomLeft> <BottomRight>
    """
    TopLeft: int
    TopRight: int
    BottomLeft: int
    BottomRight: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AnchorLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Diagramming
## 
##         Represents a CellBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class CellBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a CellBuilder.
        """


    ##  Represents the inherit option.
    ##             
    ##  Setting the inherit from preferences option
    class InheritOption(Enum):
        """
        Members Include: <Preferences> <CustomerDefaults> <Selection>
        """
        Preferences: int
        CustomerDefaults: int
        Selection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CellBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) BottomBorder
    ##   the bottom border line rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def BottomBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) BottomBorder
          the bottom border line rendering properties.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) BottomBorder

    ##   the bottom border line rendering properties.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @BottomBorder.setter
    def BottomBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) BottomBorder
          the bottom border line rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.FormattedStringBuilder NXOpen.Diagramming.FormattedStringBuilder@endlink) FormattedStringBuilder
    ##   the formatted string of the text.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Diagramming.FormattedStringBuilder
    @property
    def FormattedStringBuilder(self) -> NXOpen.Diagramming.FormattedStringBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.FormattedStringBuilder NXOpen.Diagramming.FormattedStringBuilder@endlink) FormattedStringBuilder
          the formatted string of the text.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) LeftBorder
    ##   the left border line rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def LeftBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) LeftBorder
          the left border line rendering properties.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) LeftBorder

    ##   the left border line rendering properties.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LeftBorder.setter
    def LeftBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) LeftBorder
          the left border line rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Locked
    ##   the locked flag.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Locked(self) -> bool:
        """
        Getter for property: (bool) Locked
          the locked flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Locked

    ##   the locked flag.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Locked.setter
    def Locked(self, locked: bool):
        """
        Setter for property: (bool) Locked
          the locked flag.  
             
         
        """
        pass
    
    ## Getter for property: (float) Padding
    ##   the cell padding.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Padding(self) -> float:
        """
        Getter for property: (float) Padding
          the cell padding.  
             
         
        """
        pass
    
    ## Setter for property: (float) Padding

    ##   the cell padding.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Padding.setter
    def Padding(self, padding: float):
        """
        Setter for property: (float) Padding
          the cell padding.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RightBorder
    ##   the right border line rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def RightBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RightBorder
          the right border line rendering properties.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RightBorder

    ##   the right border line rendering properties.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @RightBorder.setter
    def RightBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RightBorder
          the right border line rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (str) Text
    ##   the text on cell.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Text(self) -> str:
        """
        Getter for property: (str) Text
          the text on cell.  
             
         
        """
        pass
    
    ## Setter for property: (str) Text

    ##   the text on cell.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Text.setter
    def Text(self, strValue: str):
        """
        Setter for property: (str) Text
          the text on cell.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TopBorder
    ##   the top border line rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def TopBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TopBorder
          the top border line rendering properties.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TopBorder

    ##   the top border line rendering properties.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TopBorder.setter
    def TopBorder(self, properties: NXOpen.Diagramming.RenderingPropertiesBuilder):
        """
        Setter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TopBorder
          the top border line rendering properties.  
             
         
        """
        pass
    
    ##  Delete cellsettings. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeleteCellSettings(builder: CellBuilder) -> None:
        """
         Delete cellsettings. 
        """
        pass
    
    ##  Delete cell contents. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeleteContent(builder: CellBuilder) -> None:
        """
         Delete cell contents. 
        """
        pass
    
    ##  Gets cell settings. 
    ##  @return cellSettings (@link CellSettingsBuilder NXOpen.Diagramming.Tables.CellSettingsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCellSettings(builder: CellBuilder) -> CellSettingsBuilder:
        """
         Gets cell settings. 
         @return cellSettings (@link CellSettingsBuilder NXOpen.Diagramming.Tables.CellSettingsBuilder@endlink): .
        """
        pass
    
    ##  Gets cell content. 
    ##  @return symbols (@link SizedSymbol List[NXOpen.Diagramming.Tables.SizedSymbol]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContent(builder: CellBuilder) -> List[SizedSymbol]:
        """
         Gets cell content. 
         @return symbols (@link SizedSymbol List[NXOpen.Diagramming.Tables.SizedSymbol]@endlink): .
        """
        pass
    
    ##  Inherit. elementToInheritFrom must be Table or Cell object
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inheritOption"> (@link CellBuilder.InheritOption NXOpen.Diagramming.Tables.CellBuilder.InheritOption@endlink) </param>
    ## <param name="elementToInheritFrom"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def Inherit(builder: CellBuilder, inheritOption: CellBuilder.InheritOption, elementToInheritFrom: NXOpen.TaggedObject) -> None:
        """
         Inherit. elementToInheritFrom must be Table or Cell object
        """
        pass
    
    ##  Sets cell content. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="symbols"> (@link SizedSymbol List[NXOpen.Diagramming.Tables.SizedSymbol]@endlink) </param>
    def SetContent(builder: CellBuilder, symbols: List[SizedSymbol]) -> None:
        """
         Sets cell content. 
        """
        pass
    
    ##  Sets cell image file location. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fileName"> (str) </param>
    def SetImageFileLocation(builder: CellBuilder, fileName: str) -> None:
        """
         Sets cell image file location. 
        """
        pass
    
    ##  Sets the SVG image on the cell. Passing width/height in as zero will use cells size. This will override any current SVG or Text 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="strValue"> (str) </param>
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    def SetSVG(builder: CellBuilder, strValue: str, width: float, height: float) -> None:
        """
         Sets the SVG image on the cell. Passing width/height in as zero will use cells size. This will override any current SVG or Text 
        """
        pass
    
import NXOpen.Diagramming
## 
##         Represents a CellRangeBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class CellRangeBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a CellRangeBuilder.
        """


    ## Getter for property: (bool) CanHide
    ##   the can hide flag.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CanHide(self) -> bool:
        """
        Getter for property: (bool) CanHide
          the can hide flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanHide

    ##   the can hide flag.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CanHide.setter
    def CanHide(self, canHide: bool):
        """
        Setter for property: (bool) CanHide
          the can hide flag.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Hidden
    ##   the hidden flag.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Hidden(self) -> bool:
        """
        Getter for property: (bool) Hidden
          the hidden flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Hidden

    ##   the hidden flag.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Hidden.setter
    def Hidden(self, hidden: bool):
        """
        Setter for property: (bool) Hidden
          the hidden flag.  
             
         
        """
        pass
    
    ## Getter for property: (float) Size
    ##   the size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Size(self) -> float:
        """
        Getter for property: (float) Size
          the size.  
             
         
        """
        pass
    
    ## Setter for property: (float) Size

    ##   the size.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Size.setter
    def Size(self, size: float):
        """
        Setter for property: (float) Size
          the size.  
             
         
        """
        pass
    
    ## Getter for property: (@link SizingMethod NXOpen.Diagramming.Tables.SizingMethod@endlink) SizingMethod
    ##   the sizing method.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SizingMethod
    @property
    def SizingMethod(self) -> SizingMethod:
        """
        Getter for property: (@link SizingMethod NXOpen.Diagramming.Tables.SizingMethod@endlink) SizingMethod
          the sizing method.  
             
         
        """
        pass
    
    ## Setter for property: (@link SizingMethod NXOpen.Diagramming.Tables.SizingMethod@endlink) SizingMethod

    ##   the sizing method.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @SizingMethod.setter
    def SizingMethod(self, sizingMethod: SizingMethod):
        """
        Setter for property: (@link SizingMethod NXOpen.Diagramming.Tables.SizingMethod@endlink) SizingMethod
          the sizing method.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
## 
##         Represents a CellSettingsBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class CellSettingsBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a CellSettingsBuilder.
        """


    ## Getter for property: (@link ContentAlignment NXOpen.Diagramming.Tables.ContentAlignment@endlink) ContentAlignment
    ##   the content alignment of the cell settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ContentAlignment
    @property
    def ContentAlignment(self) -> ContentAlignment:
        """
        Getter for property: (@link ContentAlignment NXOpen.Diagramming.Tables.ContentAlignment@endlink) ContentAlignment
          the content alignment of the cell settings.  
             
         
        """
        pass
    
    ## Setter for property: (@link ContentAlignment NXOpen.Diagramming.Tables.ContentAlignment@endlink) ContentAlignment

    ##   the content alignment of the cell settings.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ContentAlignment.setter
    def ContentAlignment(self, contentAlignment: ContentAlignment):
        """
        Setter for property: (@link ContentAlignment NXOpen.Diagramming.Tables.ContentAlignment@endlink) ContentAlignment
          the content alignment of the cell settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor
    ##   the fill color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FillColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor
          the fill color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor

    ##   the fill color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FillColor.setter
    def FillColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor
          the fill color.  
             
         
        """
        pass
    
    ## Getter for property: (float) FillOpacity
    ##   the fill opacity.  
    ##    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def FillOpacity(self) -> float:
        """
        Getter for property: (float) FillOpacity
          the fill opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    
    ## Setter for property: (float) FillOpacity

    ##   the fill opacity.  
    ##    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FillOpacity.setter
    def FillOpacity(self, opacity: float):
        """
        Setter for property: (float) FillOpacity
          the fill opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    
    ## Getter for property: (@link OverflowBehavior NXOpen.Diagramming.Tables.OverflowBehavior@endlink) OverflowBehavior
    ##   the overflow behavior of the cell settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return OverflowBehavior
    @property
    def OverflowBehavior(self) -> OverflowBehavior:
        """
        Getter for property: (@link OverflowBehavior NXOpen.Diagramming.Tables.OverflowBehavior@endlink) OverflowBehavior
          the overflow behavior of the cell settings.  
             
         
        """
        pass
    
    ## Setter for property: (@link OverflowBehavior NXOpen.Diagramming.Tables.OverflowBehavior@endlink) OverflowBehavior

    ##   the overflow behavior of the cell settings.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @OverflowBehavior.setter
    def OverflowBehavior(self, overflowBehavior: OverflowBehavior):
        """
        Setter for property: (@link OverflowBehavior NXOpen.Diagramming.Tables.OverflowBehavior@endlink) OverflowBehavior
          the overflow behavior of the cell settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link TextDirection NXOpen.Diagramming.Tables.TextDirection@endlink) TextDirection
    ##   the text direction.  
    ##    The default text direction is 0 for horizontal left-reading text orientation.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return TextDirection
    @property
    def TextDirection(self) -> TextDirection:
        """
        Getter for property: (@link TextDirection NXOpen.Diagramming.Tables.TextDirection@endlink) TextDirection
          the text direction.  
           The default text direction is 0 for horizontal left-reading text orientation.   
         
        """
        pass
    
    ## Setter for property: (@link TextDirection NXOpen.Diagramming.Tables.TextDirection@endlink) TextDirection

    ##   the text direction.  
    ##    The default text direction is 0 for horizontal left-reading text orientation.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @TextDirection.setter
    def TextDirection(self, textDirection: TextDirection):
        """
        Setter for property: (@link TextDirection NXOpen.Diagramming.Tables.TextDirection@endlink) TextDirection
          the text direction.  
           The default text direction is 0 for horizontal left-reading text orientation.   
         
        """
        pass
    
    ## Getter for property: (@link ZeroDisplay NXOpen.Diagramming.Tables.ZeroDisplay@endlink) ZeroDisplay
    ##   the zero display of the cell settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ZeroDisplay
    @property
    def ZeroDisplay(self) -> ZeroDisplay:
        """
        Getter for property: (@link ZeroDisplay NXOpen.Diagramming.Tables.ZeroDisplay@endlink) ZeroDisplay
          the zero display of the cell settings.  
             
         
        """
        pass
    
    ## Setter for property: (@link ZeroDisplay NXOpen.Diagramming.Tables.ZeroDisplay@endlink) ZeroDisplay

    ##   the zero display of the cell settings.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ZeroDisplay.setter
    def ZeroDisplay(self, zeroDisplay: ZeroDisplay):
        """
        Setter for property: (@link ZeroDisplay NXOpen.Diagramming.Tables.ZeroDisplay@endlink) ZeroDisplay
          the zero display of the cell settings.  
             
         
        """
        pass
    
    ##  Gets context text style . 
    ##  @return textStyle (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContentTextStyle(builder: CellSettingsBuilder) -> NXOpen.Diagramming.TextStyleBuilder:
        """
         Gets context text style . 
         @return textStyle (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents the Cell class.  <br> This is an abstract and sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Cell(NXOpen.TaggedObject): 
    """ Represents the Cell class. """
    pass


## 
##         Represents a ColumnBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ColumnBuilder(CellRangeBuilder): 
    """
        Represents a ColumnBuilder.
        """


    ##  The method to set the width of a column. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="size"> (float) </param>
    def SetWidth(builder: ColumnBuilder, size: float) -> None:
        """
         The method to set the width of a column. 
        """
        pass
    
##  Represents the cell content alignment. 
##  Top left content alignment 
class ContentAlignment(Enum):
    """
    Members Include: <TopLeft> <TopCenter> <TopRight> <MiddleLeft> <MiddleCenter> <MiddleRight> <BottomLeft> <BottomCenter> <BottomRight>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ContentAlignment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen.Diagramming
## 
##         Represents a ContinuationDataBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ContinuationDataBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a ContinuationDataBuilder.
        """


    ## Getter for property: (@link ContinuationLocation NXOpen.Diagramming.Tables.ContinuationLocation@endlink) Location
    ##   the location to continue a table if it won't fit.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ContinuationLocation
    @property
    def Location(self) -> ContinuationLocation:
        """
        Getter for property: (@link ContinuationLocation NXOpen.Diagramming.Tables.ContinuationLocation@endlink) Location
          the location to continue a table if it won't fit.  
             
         
        """
        pass
    
    ## Setter for property: (@link ContinuationLocation NXOpen.Diagramming.Tables.ContinuationLocation@endlink) Location

    ##   the location to continue a table if it won't fit.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Location.setter
    def Location(self, location: ContinuationLocation):
        """
        Setter for property: (@link ContinuationLocation NXOpen.Diagramming.Tables.ContinuationLocation@endlink) Location
          the location to continue a table if it won't fit.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaximumSize
    ##   the maximum size of any section of a table.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def MaximumSize(self) -> float:
        """
        Getter for property: (float) MaximumSize
          the maximum size of any section of a table.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaximumSize

    ##   the maximum size of any section of a table.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MaximumSize.setter
    def MaximumSize(self, maximumSize: float):
        """
        Setter for property: (float) MaximumSize
          the maximum size of any section of a table.  
             
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##   the spacing between sections of a table.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
          the spacing between sections of a table.  
             
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##   the spacing between sections of a table.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
          the spacing between sections of a table.  
             
         
        """
        pass
    
##  Represents the table continuation location. 
##  Up continuation location 
class ContinuationLocation(Enum):
    """
    Members Include: <Up> <Down> <Left> <Right> <NextSheet>
    """
    Up: int
    Down: int
    Left: int
    Right: int
    NextSheet: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ContinuationLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the table header location. 
##  Start header location 
class HeaderLocation(Enum):
    """
    Members Include: <Start> <End>
    """
    Start: int
    End: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> HeaderLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the table header orientation. 
##  Vertical header orientation 
class HeaderOrientation(Enum):
    """
    Members Include: <Vertical> <Horizontal>
    """
    Vertical: int
    Horizontal: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> HeaderOrientation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the cell overflow behavior. 
##  Wrap overflow behavior 
class OverflowBehavior(Enum):
    """
    Members Include: <Wrap> <Truncate> <OverflowBorder> <ShrinkToFit> <Suffix>
    """
    Wrap: int
    Truncate: int
    OverflowBorder: int
    ShrinkToFit: int
    Suffix: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> OverflowBehavior:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## 
##         Represents a RowBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class RowBuilder(CellRangeBuilder): 
    """
        Represents a RowBuilder.
        """


    ##  The method to set the height of a row. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="size"> (float) </param>
    def SetHeight(builder: RowBuilder, size: float) -> None:
        """
         The method to set the height of a row. 
        """
        pass
    
##  Represents sized symbol information. 
class SizedSymbol:
    """
     Represents sized symbol information. 
    """
    ## Getter for property :(float) PaddingFromLastSymbol
    ## Padding from last symbol
    ## @return float
    @property
    def PaddingFromLastSymbol(self) -> float:
        """
        Getter for property PaddingFromLastSymbol
        Padding from last symbol

        """
        pass
    
    ## Setter for property :(float) PaddingFromLastSymbol
    @PaddingFromLastSymbol.setter
    def PaddingFromLastSymbol(self, value: float):
        """
        Getter for property PaddingFromLastSymbol
        Padding from last symbol
        Setter for property PaddingFromLastSymbol
        Padding from last symbol

        """
        pass
    
    ## Getter for property :(@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Symbol
    ## The symbol
    ## @return @link NXOpen.TaggedObject NXOpen.TaggedObject@endlink
    @property
    def Symbol(self) -> NXOpen.TaggedObject:
        """
        Getter for property Symbol
        The symbol

        """
        pass
    
    ## Setter for property :(@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) Symbol
    @Symbol.setter
    def Symbol(self, value: NXOpen.TaggedObject):
        """
        Getter for property Symbol
        The symbol
        Setter for property Symbol
        The symbol

        """
        pass
    
    ## Getter for property :(float) Height
    ## The symbol height
    ## @return float
    @property
    def Height(self) -> float:
        """
        Getter for property Height
        The symbol height

        """
        pass
    
    ## Setter for property :(float) Height
    @Height.setter
    def Height(self, value: float):
        """
        Getter for property Height
        The symbol height
        Setter for property Height
        The symbol height

        """
        pass
    
    ## Getter for property :(float) Width
    ## The symbol width
    ## @return float
    @property
    def Width(self) -> float:
        """
        Getter for property Width
        The symbol width

        """
        pass
    
    ## Setter for property :(float) Width
    @Width.setter
    def Width(self, value: float):
        """
        Getter for property Width
        The symbol width
        Setter for property Width
        The symbol width

        """
        pass
    


##  Represents the column/row sizing method. 
##  Auto sizing method 
class SizingMethod(Enum):
    """
    Members Include: <Auto> <Fixed>
    """
    Auto: int
    Fixed: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SizingMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Diagramming
## 
##         Represents a TableBuilder.
##          <br> To create a new instance of this class, use @link NXOpen::Diagramming::Tables::TableCollection::CreateTableBuilder  NXOpen::Diagramming::Tables::TableCollection::CreateTableBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class TableBuilder(NXOpen.Diagramming.AnnotationBuilder): 
    """
        Represents a TableBuilder.
        """


    ##  Represents the inherit option.
    ##             
    ##  Setting the inherit from preferences option
    class InheritOption(Enum):
        """
        Members Include: <Preferences> <CustomerDefaults> <Selection>
        """
        Preferences: int
        CustomerDefaults: int
        Selection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TableBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) BottomBorder
    ##   the bottom border rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def BottomBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) BottomBorder
          the bottom border rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (@link CellSettingsBuilder NXOpen.Diagramming.Tables.CellSettingsBuilder@endlink) CellSettingsBuilder
    ##   the default cell border settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return CellSettingsBuilder
    @property
    def CellSettingsBuilder(self) -> CellSettingsBuilder:
        """
        Getter for property: (@link CellSettingsBuilder NXOpen.Diagramming.Tables.CellSettingsBuilder@endlink) CellSettingsBuilder
          the default cell border settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link ContinuationDataBuilder NXOpen.Diagramming.Tables.ContinuationDataBuilder@endlink) ContinuationDataBuilder
    ##   the continuation data.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ContinuationDataBuilder
    @property
    def ContinuationDataBuilder(self) -> ContinuationDataBuilder:
        """
        Getter for property: (@link ContinuationDataBuilder NXOpen.Diagramming.Tables.ContinuationDataBuilder@endlink) ContinuationDataBuilder
          the continuation data.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) DefaultBottomBorder
    ##   the default bottom border rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def DefaultBottomBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) DefaultBottomBorder
          the default bottom border rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) DefaultRightBorder
    ##   the default right border rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def DefaultRightBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) DefaultRightBorder
          the default right border rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (float) InitialColumnWidth
    ##   the initial width of column.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def InitialColumnWidth(self) -> float:
        """
        Getter for property: (float) InitialColumnWidth
          the initial width of column.  
             
         
        """
        pass
    
    ## Setter for property: (float) InitialColumnWidth

    ##   the initial width of column.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @InitialColumnWidth.setter
    def InitialColumnWidth(self, columnWidth: float):
        """
        Setter for property: (float) InitialColumnWidth
          the initial width of column.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) LeftBorder
    ##   the left border rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def LeftBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) LeftBorder
          the left border rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Locked
    ##   the locked flag.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Locked(self) -> bool:
        """
        Getter for property: (bool) Locked
          the locked flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Locked

    ##   the locked flag.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Locked.setter
    def Locked(self, locked: bool):
        """
        Setter for property: (bool) Locked
          the locked flag.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RightBorder
    ##   the right border rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def RightBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RightBorder
          the right border rendering properties.  
             
         
        """
        pass
    
    ## Getter for property: (@link TableSettingsBuilder NXOpen.Diagramming.Tables.TableSettingsBuilder@endlink) TableSettingsBuilder
    ##   the table settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return TableSettingsBuilder
    @property
    def TableSettingsBuilder(self) -> TableSettingsBuilder:
        """
        Getter for property: (@link TableSettingsBuilder NXOpen.Diagramming.Tables.TableSettingsBuilder@endlink) TableSettingsBuilder
          the table settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TopBorder
    ##   the top border rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def TopBorder(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TopBorder
          the top border rendering properties.  
             
         
        """
        pass
    
    ##  The method to get the cell at the given row and column indexes. 
    ##  @return cell (@link CellBuilder NXOpen.Diagramming.Tables.CellBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    ## <param name="columnIndex"> (int) </param>
    def GetCell(builder: TableBuilder, rowIndex: int, columnIndex: int) -> CellBuilder:
        """
         The method to get the cell at the given row and column indexes. 
         @return cell (@link CellBuilder NXOpen.Diagramming.Tables.CellBuilder@endlink): .
        """
        pass
    
    ##  The method to get the column at the given column index. 
    ##  @return column (@link ColumnBuilder NXOpen.Diagramming.Tables.ColumnBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnIndex"> (int) </param>
    def GetColumn(builder: TableBuilder, columnIndex: int) -> ColumnBuilder:
        """
         The method to get the column at the given column index. 
         @return column (@link ColumnBuilder NXOpen.Diagramming.Tables.ColumnBuilder@endlink): .
        """
        pass
    
    ##  The method to get the fill color. 
    ##  @return A tuple consisting of (color, opacity). 
    ##  - color is: @link NXOpen.NXColor NXOpen.NXColor@endlink.
    ##  - opacity is: float.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFillColor(builder: TableBuilder) -> Tuple[NXOpen.NXColor, float]:
        """
         The method to get the fill color. 
         @return A tuple consisting of (color, opacity). 
         - color is: @link NXOpen.NXColor NXOpen.NXColor@endlink.
         - opacity is: float.

        """
        pass
    
    ##  The method to get the header at the given header index. 
    ##  @return header (@link CellRangeBuilder NXOpen.Diagramming.Tables.CellRangeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="headerIndex"> (int) </param>
    def GetHeader(builder: TableBuilder, headerIndex: int) -> CellRangeBuilder:
        """
         The method to get the header at the given header index. 
         @return header (@link CellRangeBuilder NXOpen.Diagramming.Tables.CellRangeBuilder@endlink): .
        """
        pass
    
    ##  The method to get the header cell at the given row and column indexes. 
    ##  @return cell (@link CellBuilder NXOpen.Diagramming.Tables.CellBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    ## <param name="columnIndex"> (int) </param>
    def GetHeaderCell(builder: TableBuilder, rowIndex: int, columnIndex: int) -> CellBuilder:
        """
         The method to get the header cell at the given row and column indexes. 
         @return cell (@link CellBuilder NXOpen.Diagramming.Tables.CellBuilder@endlink): .
        """
        pass
    
    ##  Returns the initial number of columns. 
    ##  @return numColumns (int): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNumberOfColumns(builder: TableBuilder) -> int:
        """
         Returns the initial number of columns. 
         @return numColumns (int): .
        """
        pass
    
    ##  Returns the number of headers. 
    ##  @return numHeaders (int): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNumberOfHeaders(builder: TableBuilder) -> int:
        """
         Returns the number of headers. 
         @return numHeaders (int): .
        """
        pass
    
    ##  Returns the number of rows. 
    ##  @return numRows (int): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNumberOfRows(builder: TableBuilder) -> int:
        """
         Returns the number of rows. 
         @return numRows (int): .
        """
        pass
    
    ##  The method to get the row at the given row index. 
    ##  @return row (@link RowBuilder NXOpen.Diagramming.Tables.RowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    def GetRow(builder: TableBuilder, rowIndex: int) -> RowBuilder:
        """
         The method to get the row at the given row index. 
         @return row (@link RowBuilder NXOpen.Diagramming.Tables.RowBuilder@endlink): .
        """
        pass
    
    ##  Inherit. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inheritOption"> (@link TableBuilder.InheritOption NXOpen.Diagramming.Tables.TableBuilder.InheritOption@endlink) </param>
    ## <param name="annotation"> (@link NXOpen.Diagramming.Annotation NXOpen.Diagramming.Annotation@endlink) </param>
    def Inherit(builder: TableBuilder, inheritOption: TableBuilder.InheritOption, annotation: NXOpen.Diagramming.Annotation) -> None:
        """
         Inherit. 
        """
        pass
    
    ##  The method to insert the given number of columns after the given column index. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnIndex"> (int) </param>
    ## <param name="numColumns"> (int) </param>
    def InsertColumns(builder: TableBuilder, columnIndex: int, numColumns: int) -> None:
        """
         The method to insert the given number of columns after the given column index. 
        """
        pass
    
    ##  The method to insert the given number of headers after the given header index. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="headerIndex"> (int) </param>
    ## <param name="numHeaders"> (int) </param>
    def InsertHeaders(builder: TableBuilder, headerIndex: int, numHeaders: int) -> None:
        """
         The method to insert the given number of headers after the given header index. 
        """
        pass
    
    ##  The method to insert the given number of rows after the given row index. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    ## <param name="numRows"> (int) </param>
    def InsertRows(builder: TableBuilder, rowIndex: int, numRows: int) -> None:
        """
         The method to insert the given number of rows after the given row index. 
        """
        pass
    
    ##  The method to merge the cells in the given ranges. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="topRow"> (int) </param>
    ## <param name="leftColumn"> (int) </param>
    ## <param name="bottomRow"> (int) </param>
    ## <param name="rightColumn"> (int) </param>
    def MergeCells(builder: TableBuilder, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        """
         The method to merge the cells in the given ranges. 
        """
        pass
    
    ##  The method to merge the header cells in the given ranges. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="topRow"> (int) </param>
    ## <param name="leftColumn"> (int) </param>
    ## <param name="bottomRow"> (int) </param>
    ## <param name="rightColumn"> (int) </param>
    def MergeHeaderCells(builder: TableBuilder, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        """
         The method to merge the header cells in the given ranges. 
        """
        pass
    
    ##  The method to remove the given number of columns starting with the given column index. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="columnIndex"> (int) </param>
    ## <param name="numColumns"> (int) </param>
    def RemoveColumns(builder: TableBuilder, columnIndex: int, numColumns: int) -> None:
        """
         The method to remove the given number of columns starting with the given column index. 
        """
        pass
    
    ##  The method to remove the given number of headers starting with the given header index. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="headerIndex"> (int) </param>
    ## <param name="numHeaders"> (int) </param>
    def RemoveHeaders(builder: TableBuilder, headerIndex: int, numHeaders: int) -> None:
        """
         The method to remove the given number of headers starting with the given header index. 
        """
        pass
    
    ##  The method to remove the given number of rows starting with the given row index. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    ## <param name="numRows"> (int) </param>
    def RemoveRows(builder: TableBuilder, rowIndex: int, numRows: int) -> None:
        """
         The method to remove the given number of rows starting with the given row index. 
        """
        pass
    
    ##  The method to set the fill color. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="color"> (@link NXOpen.NXColor NXOpen.NXColor@endlink) </param>
    ## <param name="opacity"> (float) </param>
    def SetFillColor(builder: TableBuilder, color: NXOpen.NXColor, opacity: float) -> None:
        """
         The method to set the fill color. 
        """
        pass
    
    ##  The method to unmerge the cell at the given row and column indexes. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    ## <param name="columnIndex"> (int) </param>
    def UnMergeCell(builder: TableBuilder, rowIndex: int, columnIndex: int) -> None:
        """
         The method to unmerge the cell at the given row and column indexes. 
        """
        pass
    
    ##  The method to unmerge the header cell at the given row and column indexes. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int) </param>
    ## <param name="columnIndex"> (int) </param>
    def UnMergeHeaderCell(builder: TableBuilder, rowIndex: int, columnIndex: int) -> None:
        """
         The method to unmerge the header cell at the given row and column indexes. 
        """
        pass
    
import NXOpen
##  Represents a collection of Table.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class TableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Table. """


    ##  Creates a @link NXOpen::Diagramming::Tables::TableBuilder NXOpen::Diagramming::Tables::TableBuilder@endlink . 
    ##  @return builder (@link TableBuilder NXOpen.Diagramming.Tables.TableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  to be edited, if NULL then create a new one 
    def CreateTableBuilder(part: TableCollection, table: Table) -> TableBuilder:
        """
         Creates a @link NXOpen::Diagramming::Tables::TableBuilder NXOpen::Diagramming::Tables::TableBuilder@endlink . 
         @return builder (@link TableBuilder NXOpen.Diagramming.Tables.TableBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  with the given identifier as recorded in a journal.
    ##                 An exception will be thrown if no object can be found with given name. 
    ##  @return table (@link Table NXOpen.Diagramming.Tables.Table@endlink):  @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: TableCollection, journalIdentifier: str) -> Table:
        """
         Finds the @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  with the given identifier as recorded in a journal.
                        An exception will be thrown if no object can be found with given name. 
         @return table (@link Table NXOpen.Diagramming.Tables.Table@endlink):  @link NXOpen::Diagramming::Tables::Table NXOpen::Diagramming::Tables::Table@endlink  with this name. .
        """
        pass
    
import NXOpen.Diagramming
## 
##         Represents a TableSettingsBuilder.
##          <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class TableSettingsBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder): 
    """
        Represents a TableSettingsBuilder.
        """


    ## Getter for property: (@link AnchorLocation NXOpen.Diagramming.Tables.AnchorLocation@endlink) AnchorLocation
    ##   the anchor location of the table settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return AnchorLocation
    @property
    def AnchorLocation(self) -> AnchorLocation:
        """
        Getter for property: (@link AnchorLocation NXOpen.Diagramming.Tables.AnchorLocation@endlink) AnchorLocation
          the anchor location of the table settings.  
             
         
        """
        pass
    
    ## Setter for property: (@link AnchorLocation NXOpen.Diagramming.Tables.AnchorLocation@endlink) AnchorLocation

    ##   the anchor location of the table settings.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AnchorLocation.setter
    def AnchorLocation(self, anchorLocation: AnchorLocation):
        """
        Setter for property: (@link AnchorLocation NXOpen.Diagramming.Tables.AnchorLocation@endlink) AnchorLocation
          the anchor location of the table settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link HeaderLocation NXOpen.Diagramming.Tables.HeaderLocation@endlink) HeaderLocation
    ##   the header location of the table settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return HeaderLocation
    @property
    def HeaderLocation(self) -> HeaderLocation:
        """
        Getter for property: (@link HeaderLocation NXOpen.Diagramming.Tables.HeaderLocation@endlink) HeaderLocation
          the header location of the table settings.  
             
         
        """
        pass
    
    ## Setter for property: (@link HeaderLocation NXOpen.Diagramming.Tables.HeaderLocation@endlink) HeaderLocation

    ##   the header location of the table settings.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @HeaderLocation.setter
    def HeaderLocation(self, headerLocation: HeaderLocation):
        """
        Setter for property: (@link HeaderLocation NXOpen.Diagramming.Tables.HeaderLocation@endlink) HeaderLocation
          the header location of the table settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link HeaderOrientation NXOpen.Diagramming.Tables.HeaderOrientation@endlink) HeaderOrientation
    ##   the header orientation of the table settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return HeaderOrientation
    @property
    def HeaderOrientation(self) -> HeaderOrientation:
        """
        Getter for property: (@link HeaderOrientation NXOpen.Diagramming.Tables.HeaderOrientation@endlink) HeaderOrientation
          the header orientation of the table settings.  
             
         
        """
        pass
    
    ## Setter for property: (@link HeaderOrientation NXOpen.Diagramming.Tables.HeaderOrientation@endlink) HeaderOrientation

    ##   the header orientation of the table settings.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @HeaderOrientation.setter
    def HeaderOrientation(self, headerOrientation: HeaderOrientation):
        """
        Setter for property: (@link HeaderOrientation NXOpen.Diagramming.Tables.HeaderOrientation@endlink) HeaderOrientation
          the header orientation of the table settings.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ProtectedFlag
    ##   the protected flag.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ProtectedFlag(self) -> bool:
        """
        Getter for property: (bool) ProtectedFlag
          the protected flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ProtectedFlag

    ##   the protected flag.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ProtectedFlag.setter
    def ProtectedFlag(self, flag: bool):
        """
        Setter for property: (bool) ProtectedFlag
          the protected flag.  
             
         
        """
        pass
    
import NXOpen.Diagramming
##  Represents the Table class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::Tables::TableBuilder  NXOpen::Diagramming::Tables::TableBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Table(NXOpen.Diagramming.Annotation): 
    """ Represents the Table class. """


    ##  Get the title block attached to the table.
    ##  @return titleBlock (@link NXOpen.Diagramming.TitleBlock NXOpen.Diagramming.TitleBlock@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTitleBlock(table: Table) -> NXOpen.Diagramming.TitleBlock:
        """
         Get the title block attached to the table.
         @return titleBlock (@link NXOpen.Diagramming.TitleBlock NXOpen.Diagramming.TitleBlock@endlink): .
        """
        pass
    
    ##  Remove the title block attached to the table.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def RemoveTitleBlock(table: Table) -> None:
        """
         Remove the title block attached to the table.
        """
        pass
    
##  Represents the table text direction. 
##  Horizontal left-reading text orientation 
class TextDirection(Enum):
    """
    Members Include: <Horizontal> <VerticalRightReading> <VerticalLeftReading>
    """
    Horizontal: int
    VerticalRightReading: int
    VerticalLeftReading: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TextDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the cell zero display. 
##  Zero filled display 
class ZeroDisplay(Enum):
    """
    Members Include: <Zero> <Dash> <Empty>
    """
    Zero: int
    Dash: int
    Empty: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ZeroDisplay:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.Diagramming.Tables
## Classes, Enums and Structs under NXOpen.Diagramming.Tables namespace

##  @link CellBuilderInheritOption NXOpen.Diagramming.Tables.CellBuilderInheritOption @endlink is an alias for @link CellBuilder.InheritOption NXOpen.Diagramming.Tables.CellBuilder.InheritOption@endlink
CellBuilderInheritOption = CellBuilder.InheritOption


##  @link TableBuilderInheritOption NXOpen.Diagramming.Tables.TableBuilderInheritOption @endlink is an alias for @link TableBuilder.InheritOption NXOpen.Diagramming.Tables.TableBuilder.InheritOption@endlink
TableBuilderInheritOption = TableBuilder.InheritOption


