from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##         Represents a @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink 
##      <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Circle(Element): 
    """
        Represents a <ja_class>NXOpen.Markup.Circle</ja_class>
    """


    ##  Gets center and radius 
    ##  @return A tuple consisting of (center, radius). 
    ##  - center is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - radius is: float.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetCenterAndRadius(self) -> Tuple[NXOpen.Point3d, float]:
        """
         Gets center and radius 
         @return A tuple consisting of (center, radius). 
         - center is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - radius is: float.

        """
        pass
    
    ##  Sets center and radius 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="radius"> (float) </param>
    def SetCenterAndRadius(self, center: NXOpen.Point3d, radius: float) -> None:
        """
         Sets center and radius 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  The @link NXOpen::Markup::EditElementDisplayBuilder NXOpen::Markup::EditElementDisplayBuilder@endlink  is used to edit display settings of the markup objects.  <br> To create a new instance of this class, use @link NXOpen::Markup::ElementCollection::CreateEditElementDisplayBuilder  NXOpen::Markup::ElementCollection::CreateEditElementDisplayBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class EditElementDisplayBuilder(NXOpen.Builder): 
    """ The <ja_class>NXOpen.Markup.EditElementDisplayBuilder</ja_class> is used to edit display settings of the markup objects. """


    ## Getter for property: (bool) EnableBackground
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def EnableBackground(self) -> bool:
        """
        Getter for property: (bool) EnableBackground
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableBackground

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EnableBackground.setter
    def EnableBackground(self, enableBackground: bool):
        """
        Setter for property: (bool) EnableBackground
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (int) LineColor
    ##  Returns the line color index value of the markup object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def LineColor(self) -> int:
        """
        Getter for property: (int) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Setter for property: (int) LineColor

    ##  Returns the line color index value of the markup object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LineColor.setter
    def LineColor(self, colorIndex: int):
        """
        Setter for property: (int) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
    ##  Returns the line font of the markup object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont

    ##  Returns the line font of the markup object.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
    ##  Returns the line width of the markup object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth

    ##  Returns the line width of the markup object.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Strikethrough
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Strikethrough(self) -> bool:
        """
        Getter for property: (bool) Strikethrough
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) Strikethrough

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Strikethrough.setter
    def Strikethrough(self, strikethrough: bool):
        """
        Setter for property: (bool) Strikethrough
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor
    ##  Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def TextColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor
         Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor

    ##  Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TextColor.setter
    def TextColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor
         Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Getter for property: (str) TextFont
    ##  Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def TextFont(self) -> str:
        """
        Getter for property: (str) TextFont
         Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (str) TextFont

    ##  Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextFont.setter
    def TextFont(self, textFont: str):
        """
        Setter for property: (str) TextFont
         Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle
    ##  Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Features.TextBuilder.FontStyleOptions
    @property
    def TextFontStyle(self) -> NXOpen.Features.TextBuilder.FontStyleOptions:
        """
        Getter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle
         Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle

    ##  Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextFontStyle.setter
    def TextFontStyle(self, textFontStyle: NXOpen.Features.TextBuilder.FontStyleOptions):
        """
        Setter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle
         Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale
    ##  Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Text.ScaleOptions
    @property
    def TextScale(self) -> Text.ScaleOptions:
        """
        Getter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale
         Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
         
        """
        pass
    
    ## Setter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale

    ##  Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextScale.setter
    def TextScale(self, textScale: Text.ScaleOptions):
        """
        Setter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale
         Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
         
        """
        pass
    
    ## Getter for property: (bool) Underline
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Underline(self) -> bool:
        """
        Getter for property: (bool) Underline
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) Underline

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Underline.setter
    def Underline(self, underline: bool):
        """
        Setter for property: (bool) Underline
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  The @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  which is used to edit properties of or create @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink .  <br> To create a new instance of this class, use @link NXOpen::Markup::ElementCollection::CreateElementBuilder  NXOpen::Markup::ElementCollection::CreateElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class ElementBuilder(NXOpen.Builder): 
    """ The <ja_class>NXOpen.Markup.ElementBuilder</ja_class> which is used to edit properties of or create <ja_class>NXOpen.Markup.Element</ja_class>. """


    ##  Specifies the style of @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink . 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Freehand</term><description> 
    ##  Freehand style</description> </item><item><term> 
    ## Text</term><description> 
    ##  Text style</description> </item><item><term> 
    ## Circle</term><description> 
    ##  Circle style</description> </item><item><term> 
    ## Ellipse</term><description> 
    ##  Ellipse style</description> </item><item><term> 
    ## Rectangle</term><description> 
    ##  Rectangle style</description> </item><item><term> 
    ## Icon</term><description> 
    ##  Icon style, reserved for future use </description> </item><item><term> 
    ## Polyline</term><description> 
    ##  Polyline style, reserved for future use </description> </item><item><term> 
    ## Polygon</term><description> 
    ##  Polygon style, reserved for future use </description> </item><item><term> 
    ## Line</term><description> 
    ##  Line style, reserved for future use </description> </item><item><term> 
    ## InsetImage</term><description> 
    ##  Inset Image style, reserved for future use </description> </item></list>
    class Styles(Enum):
        """
        Members Include: <Freehand> <Text> <Circle> <Ellipse> <Rectangle> <Icon> <Polyline> <Polygon> <Line> <InsetImage>
        """
        Freehand: int
        Text: int
        Circle: int
        Ellipse: int
        Rectangle: int
        Icon: int
        Polyline: int
        Polygon: int
        Line: int
        InsetImage: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementBuilder.Styles:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) CircleSize
    ##  Returns  @brief  the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  .  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def CircleSize(self) -> float:
        """
        Getter for property: (float) CircleSize
         Returns  @brief  the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  .  
            
        
            
         
        """
        pass
    
    ## Setter for property: (float) CircleSize

    ##  Returns  @brief  the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  .  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CircleSize.setter
    def CircleSize(self, radius: float):
        """
        Setter for property: (float) CircleSize
         Returns  @brief  the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  .  
            
        
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableBackground
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def EnableBackground(self) -> bool:
        """
        Getter for property: (bool) EnableBackground
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableBackground

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EnableBackground.setter
    def EnableBackground(self, enableBackground: bool):
        """
        Setter for property: (bool) EnableBackground
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  enable background setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Geometries
    ##  Returns  @brief  the geometry of interest that was created or edited by @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Geometries(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Geometries
         Returns  @brief  the geometry of interest that was created or edited by @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
            
        
            
         
        """
        pass
    
    ## Getter for property: (str) IconName
    ##  Returns  @brief  the name of icon used by the @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def IconName(self) -> str:
        """
        Getter for property: (str) IconName
         Returns  @brief  the name of icon used by the @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
            
        
            
         
        """
        pass
    
    ## Setter for property: (str) IconName

    ##  Returns  @brief  the name of icon used by the @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @IconName.setter
    def IconName(self, iconBitmap: str):
        """
        Setter for property: (str) IconName
         Returns  @brief  the name of icon used by the @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
            
        
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeLabels
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  show label setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def IncludeLabels(self) -> bool:
        """
        Getter for property: (bool) IncludeLabels
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  show label setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) IncludeLabels

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  show label setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @IncludeLabels.setter
    def IncludeLabels(self, includeLabels: bool):
        """
        Setter for property: (bool) IncludeLabels
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  show label setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LeaderLineColor
    ##  Returns the leader line color index value of the markup object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def LeaderLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LeaderLineColor
         Returns the leader line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LeaderLineColor

    ##  Returns the leader line color index value of the markup object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @LeaderLineColor.setter
    def LeaderLineColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LeaderLineColor
         Returns the leader line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LeaderLineFont
    ##  Returns the leader line font of the markup object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    def LeaderLineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LeaderLineFont
         Returns the leader line font of the markup object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LeaderLineFont

    ##  Returns the leader line font of the markup object.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @LeaderLineFont.setter
    def LeaderLineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LeaderLineFont
         Returns the leader line font of the markup object.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LeaderLineWidth
    ##  Returns the leader line width of the markup object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def LeaderLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LeaderLineWidth
         Returns the leader line width of the markup object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LeaderLineWidth

    ##  Returns the leader line width of the markup object.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @LeaderLineWidth.setter
    def LeaderLineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LeaderLineWidth
         Returns the leader line width of the markup object.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor
    ##  Returns the line color index value of the markup object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def LineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor

    ##  Returns the line color index value of the markup object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @LineColor.setter
    def LineColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
    ##  Returns the line font of the markup object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont

    ##  Returns the line font of the markup object.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
    ##  Returns the line width of the markup object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth

    ##  Returns the line width of the markup object.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Location
    ##  Returns  @brief  the location that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ##     
    ## 
    ##  
    ##         <remark> For different style of @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink , the definitions of location are:
    ##          <br> 
    ##         <ol>
    ##         <li>@link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink : the circle center.</li>
    ##         <li>@link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink : the ellipse center.</li>
    ##         <li>@link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink : the bitmap position.</li>
    ##         <li>@link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink : the initial point in drawing the freehand shape.</li>
    ##         <li>@link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink : the rectangle center.</li>
    ##         <li>@link NXOpen::Markup::Text NXOpen::Markup::Text@endlink : the text/anchored position.</li>
    ##         </ol>
    ##          <br> 
    ##         </remark>  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Location(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Location
         Returns  @brief  the location that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
            
        
         
                <remark> For different style of @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink , the definitions of location are:
                 <br> 
                <ol>
                <li>@link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink : the circle center.</li>
                <li>@link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink : the ellipse center.</li>
                <li>@link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink : the bitmap position.</li>
                <li>@link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink : the initial point in drawing the freehand shape.</li>
                <li>@link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink : the rectangle center.</li>
                <li>@link NXOpen::Markup::Text NXOpen::Markup::Text@endlink : the text/anchored position.</li>
                </ol>
                 <br> 
                </remark>  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Location

    ##  Returns  @brief  the location that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ##     
    ## 
    ##  
    ##         <remark> For different style of @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink , the definitions of location are:
    ##          <br> 
    ##         <ol>
    ##         <li>@link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink : the circle center.</li>
    ##         <li>@link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink : the ellipse center.</li>
    ##         <li>@link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink : the bitmap position.</li>
    ##         <li>@link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink : the initial point in drawing the freehand shape.</li>
    ##         <li>@link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink : the rectangle center.</li>
    ##         <li>@link NXOpen::Markup::Text NXOpen::Markup::Text@endlink : the text/anchored position.</li>
    ##         </ol>
    ##          <br> 
    ##         </remark>  
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Location.setter
    def Location(self, point: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Location
         Returns  @brief  the location that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
            
        
         
                <remark> For different style of @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink , the definitions of location are:
                 <br> 
                <ol>
                <li>@link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink : the circle center.</li>
                <li>@link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink : the ellipse center.</li>
                <li>@link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink : the bitmap position.</li>
                <li>@link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink : the initial point in drawing the freehand shape.</li>
                <li>@link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink : the rectangle center.</li>
                <li>@link NXOpen::Markup::Text NXOpen::Markup::Text@endlink : the text/anchored position.</li>
                </ol>
                 <br> 
                </remark>  
         
        """
        pass
    
    ## Getter for property: (bool) PinToScreen
    ##  Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  will pinned to screen.  
    ##     
    ## 
    ##  
    ##         <remark>Only applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .</remark>  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PinToScreen(self) -> bool:
        """
        Getter for property: (bool) PinToScreen
         Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  will pinned to screen.  
            
        
         
                <remark>Only applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .</remark>  
         
        """
        pass
    
    ## Setter for property: (bool) PinToScreen

    ##  Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  will pinned to screen.  
    ##     
    ## 
    ##  
    ##         <remark>Only applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .</remark>  
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PinToScreen.setter
    def PinToScreen(self, pinToScreen: bool):
        """
        Setter for property: (bool) PinToScreen
         Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  will pinned to screen.  
            
        
         
                <remark>Only applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .</remark>  
         
        """
        pass
    
    ## Getter for property: (bool) Strikethrough
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Strikethrough(self) -> bool:
        """
        Getter for property: (bool) Strikethrough
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) Strikethrough

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Strikethrough.setter
    def Strikethrough(self, strikethrough: bool):
        """
        Setter for property: (bool) Strikethrough
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  strikethrough setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link ElementBuilder.Styles NXOpen.Markup.ElementBuilder.Styles@endlink) Style
    ##  Returns  @brief  the style that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return ElementBuilder.Styles
    @property
    def Style(self) -> ElementBuilder.Styles:
        """
        Getter for property: (@link ElementBuilder.Styles NXOpen.Markup.ElementBuilder.Styles@endlink) Style
         Returns  @brief  the style that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link ElementBuilder.Styles NXOpen.Markup.ElementBuilder.Styles@endlink) Style

    ##  Returns  @brief  the style that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Style.setter
    def Style(self, markupStyle: ElementBuilder.Styles):
        """
        Setter for property: (@link ElementBuilder.Styles NXOpen.Markup.ElementBuilder.Styles@endlink) Style
         Returns  @brief  the style that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) TerminatingObjects
    ##  Returns  @brief  the terminating objects that was created or edited by @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for the leader line of the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ##     
    ## 
    ##  
    ##         <remark>Only applies to @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  that has leader lines, namely @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  and @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .</remark>  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def TerminatingObjects(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) TerminatingObjects
         Returns  @brief  the terminating objects that was created or edited by @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for the leader line of the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
            
        
         
                <remark>Only applies to @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  that has leader lines, namely @link NXOpen::Markup::Icon NXOpen::Markup::Icon@endlink  and @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .</remark>  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor
    ##  Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def TextColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor
         Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor

    ##  Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
    ##      
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TextColor.setter
    def TextColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TextColor
         Returns the text color index value of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  object, whose range is from 1 to 216.  
             
         
        """
        pass
    
    ## Getter for property: (str) TextFont
    ##  Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def TextFont(self) -> str:
        """
        Getter for property: (str) TextFont
         Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (str) TextFont

    ##  Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TextFont.setter
    def TextFont(self, textFont: str):
        """
        Setter for property: (str) TextFont
         Returns the font for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle
    ##  Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Features.TextBuilder.FontStyleOptions
    @property
    def TextFontStyle(self) -> NXOpen.Features.TextBuilder.FontStyleOptions:
        """
        Getter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle
         Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle

    ##  Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TextFontStyle.setter
    def TextFontStyle(self, textFontStyle: NXOpen.Features.TextBuilder.FontStyleOptions):
        """
        Setter for property: (@link NXOpen.Features.TextBuilder.FontStyleOptions NXOpen.Features.TextBuilder.FontStyleOptions@endlink) TextFontStyle
         Returns the font style for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Getter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale
    ##  Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return Text.ScaleOptions
    @property
    def TextScale(self) -> Text.ScaleOptions:
        """
        Getter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale
         Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
         
        """
        pass
    
    ## Setter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale

    ##  Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TextScale.setter
    def TextScale(self, textScale: Text.ScaleOptions):
        """
        Setter for property: (@link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink) TextScale
         Returns the scale for the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink .  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink   only.   
         
        """
        pass
    
    ## Getter for property: (bool) Underline
    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Underline(self) -> bool:
        """
        Getter for property: (bool) Underline
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ## Setter for property: (bool) Underline

    ##  Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
    ##    It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Underline.setter
    def Underline(self, underline: bool):
        """
        Setter for property: (bool) Underline
         Returns the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  underline setting.  
           It applies to @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  only.   
         
        """
        pass
    
    ##   @brief  Returns the comments that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ## 
    ##   
    ##  @return comment (List[str]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetComment(self) -> List[str]:
        """
          @brief  Returns the comments that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
        
          
         @return comment (List[str]): .
        """
        pass
    
    ##   @brief  Returns the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  .  
    ## 
    ##   
    ##  @return A tuple consisting of (majorRadius, minorRadius). 
    ##  - majorRadius is: float. The major radius of the @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink .
    ##  - minorRadius is: float. The minor radius of the @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetEllipseSize(self) -> Tuple[float, float]:
        """
          @brief  Returns the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  .  
        
          
         @return A tuple consisting of (majorRadius, minorRadius). 
         - majorRadius is: float. The major radius of the @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink .
         - minorRadius is: float. The minor radius of the @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink .

        """
        pass
    
    ##   @brief  Returns the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  .  
    ## 
    ##   
    ##  @return A tuple consisting of (length, width). 
    ##  - length is: float. The length of the @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink .
    ##  - width is: float. The width of the @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetRectangleSize(self) -> Tuple[float, float]:
        """
          @brief  Returns the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  .  
        
          
         @return A tuple consisting of (length, width). 
         - length is: float. The length of the @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink .
         - width is: float. The width of the @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink .

        """
        pass
    
    ##   @brief  Returns the content of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
    ## 
    ##   
    ##  @return comment (List[str]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetTextContent(self) -> List[str]:
        """
          @brief  Returns the content of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
        
          
         @return comment (List[str]): .
        """
        pass
    
    ##   @brief  Sets the comments that waas created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="comment"> (List[str]) </param>
    def SetComment(self, comment: List[str]) -> None:
        """
          @brief  Sets the comments that waas created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  .  
        
          
        """
        pass
    
    ##   @brief  Sets the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  .  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="majorRadius"> (float)  The major radius of the @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink </param>
    ## <param name="minorRadius"> (float)  The minor radius of the @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink </param>
    def SetEllipseSize(self, majorRadius: float, minorRadius: float) -> None:
        """
          @brief  Sets the size that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  .  
        
          
        """
        pass
    
    ##   @brief  Sets the points that defines the shaped of @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink .  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="controlPoints"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink)  An array of control points that defines the shape of @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink </param>
    def SetFreehandShape(self, controlPoints: List[NXOpen.Point3d]) -> None:
        """
          @brief  Sets the points that defines the shaped of @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink .  
        
          
        """
        pass
    
    ##   @brief  Sets the size that was created or edited by @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  .  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="length"> (float)  The length of the @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink </param>
    ## <param name="width"> (float)  The width of the @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink </param>
    def SetRectangleSize(self, length: float, width: float) -> None:
        """
          @brief  Sets the size that was created or edited by @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  for: @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  .  
        
          
        """
        pass
    
    ##   @brief  Sets the content of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="comment"> (List[str]) </param>
    def SetTextContent(self, comment: List[str]) -> None:
        """
          @brief  Sets the content of the @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  that was created or edited from @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink .  
        
          
        """
        pass
    
import NXOpen
##  This collects all the markups in the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::Markup::Markup  NXOpen::Markup::Markup @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class ElementCollection(NXOpen.TaggedObjectCollection): 
    """ This collects all the markups in the <ja_class>NXOpen.Markup.Markup</ja_class> """


    ##  Creates copies of input @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  objects into the markup. 
    ##              <br> 
    ##             Client must perform update @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink  after calling 
    ##             this method.  <br>  
    ##  @return output_objects (@link Element List[NXOpen.Markup.Element]@endlink):  Copies of Markup Elements .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="input_objects"> (@link Element List[NXOpen.Markup.Element]@endlink)  Markup Elements to be copied </param>
    def CopyObjects(self, input_objects: List[Element]) -> List[Element]:
        """
         Creates copies of input @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  objects into the markup. 
                     <br> 
                    Client must perform update @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink  after calling 
                    this method.  <br>  
         @return output_objects (@link Element List[NXOpen.Markup.Element]@endlink):  Copies of Markup Elements .
        """
        pass
    
    ##  Creates a pin to screen @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  
    ##  @return circle (@link Circle NXOpen.Markup.Circle@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="radius"> (float) </param>
    @overload
    def CreateCircle(self, center: NXOpen.Point3d, radius: float) -> Circle:
        """
         Creates a pin to screen @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  
         @return circle (@link Circle NXOpen.Markup.Circle@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  with anchor point 
    ##  @return circle (@link Circle NXOpen.Markup.Circle@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="anchorPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="radius"> (float) </param>
    @overload
    def CreateCircle(self, anchorPoint: NXOpen.Point3d, center: NXOpen.Point3d, radius: float) -> Circle:
        """
         Creates a @link NXOpen::Markup::Circle NXOpen::Markup::Circle@endlink  with anchor point 
         @return circle (@link Circle NXOpen.Markup.Circle@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::EditElementDisplayBuilder NXOpen::Markup::EditElementDisplayBuilder@endlink  
    ##  @return builder (@link EditElementDisplayBuilder NXOpen.Markup.EditElementDisplayBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="objects"> (@link Element List[NXOpen.Markup.Element]@endlink)  </param>
    def CreateEditElementDisplayBuilder(self, objects: List[Element]) -> EditElementDisplayBuilder:
        """
         Creates a @link NXOpen::Markup::EditElementDisplayBuilder NXOpen::Markup::EditElementDisplayBuilder@endlink  
         @return builder (@link EditElementDisplayBuilder NXOpen.Markup.EditElementDisplayBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  
    ##  @return builder (@link ElementBuilder NXOpen.Markup.ElementBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="annotation"> (@link Element NXOpen.Markup.Element@endlink)  </param>
    def CreateElementBuilder(self, annotation: Element) -> ElementBuilder:
        """
         Creates a @link NXOpen::Markup::ElementBuilder NXOpen::Markup::ElementBuilder@endlink  
         @return builder (@link ElementBuilder NXOpen.Markup.ElementBuilder@endlink):  .
        """
        pass
    
    ##  Creates a pin to screen @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  
    ##  @return ellipse (@link Ellipse NXOpen.Markup.Ellipse@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="major"> (float) </param>
    ## <param name="minor"> (float) </param>
    @overload
    def CreateEllipse(self, center: NXOpen.Point3d, major: float, minor: float) -> Ellipse:
        """
         Creates a pin to screen @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  
         @return ellipse (@link Ellipse NXOpen.Markup.Ellipse@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  with anchor point 
    ##  @return ellipse (@link Ellipse NXOpen.Markup.Ellipse@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="anchorPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="major"> (float) </param>
    ## <param name="minor"> (float) </param>
    @overload
    def CreateEllipse(self, anchorPoint: NXOpen.Point3d, center: NXOpen.Point3d, major: float, minor: float) -> Ellipse:
        """
         Creates a @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink  with anchor point 
         @return ellipse (@link Ellipse NXOpen.Markup.Ellipse@endlink): .
        """
        pass
    
    ##  Creates a pin to screen @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  
    ##  @return freehand (@link Freehand NXOpen.Markup.Freehand@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="points"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink)  Points in absolute coordinate </param>
    @overload
    def CreateFreehand(self, points: List[NXOpen.Point3d]) -> Freehand:
        """
         Creates a pin to screen @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  
         @return freehand (@link Freehand NXOpen.Markup.Freehand@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  with anchor point 
    ##  @return freehand (@link Freehand NXOpen.Markup.Freehand@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="anchorPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="points"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink)  Points in absolute coordinate </param>
    @overload
    def CreateFreehand(self, anchorPoint: NXOpen.Point3d, points: List[NXOpen.Point3d]) -> Freehand:
        """
         Creates a @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink  with anchor point 
         @return freehand (@link Freehand NXOpen.Markup.Freehand@endlink): .
        """
        pass
    
    ##  Creates a pin to screen @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  
    ##  @return rectangle (@link Rectangle NXOpen.Markup.Rectangle@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="length"> (float) </param>
    ## <param name="width"> (float) </param>
    @overload
    def CreateRectangle(self, center: NXOpen.Point3d, length: float, width: float) -> Rectangle:
        """
         Creates a pin to screen @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  
         @return rectangle (@link Rectangle NXOpen.Markup.Rectangle@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  with anchor point 
    ##  @return rectangle (@link Rectangle NXOpen.Markup.Rectangle@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="markup"> (@link ElementCollection NXOpen.Markup.ElementCollection@endlink) </param>
    ## <param name="anchorPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="length"> (float) </param>
    ## <param name="width"> (float) </param>
    @overload
    def CreateRectangle(self, anchorPoint: NXOpen.Point3d, center: NXOpen.Point3d, length: float, width: float) -> Rectangle:
        """
         Creates a @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink  with anchor point 
         @return rectangle (@link Rectangle NXOpen.Markup.Rectangle@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  
    ##  @return text (@link Text NXOpen.Markup.Text@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="position"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Point in absolute coordinate </param>
    ## <param name="textContent"> (str) </param>
    def CreateText(self, position: NXOpen.Point3d, textContent: str) -> Text:
        """
         Creates a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  
         @return text (@link Text NXOpen.Markup.Text@endlink): .
        """
        pass
    
    ##  Cuts the input @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  objects into the markup. 
    ##              <br> 
    ##             Client must perform update @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink  after calling 
    ##             this method.  <br>  
    ##  @return output_objects (@link Element List[NXOpen.Markup.Element]@endlink):  Markup Elements moved to new Markup .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="input_objects"> (@link Element List[NXOpen.Markup.Element]@endlink)  Markup Elements to be cut </param>
    def CutObjects(self, input_objects: List[Element]) -> List[Element]:
        """
         Cuts the input @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  objects into the markup. 
                     <br> 
                    Client must perform update @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink  after calling 
                    this method.  <br>  
         @return output_objects (@link Element List[NXOpen.Markup.Element]@endlink):  Markup Elements moved to new Markup .
        """
        pass
    
    ##  Finds the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with the given id in current markup.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return markupElement (@link Element NXOpen.Markup.Element@endlink):  @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with this id .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="id"> (str)  The id of the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  </param>
    def FindObject(self, id: str) -> Element:
        """
         Finds the @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with the given id in current markup.
                    An exception will be thrown if no object can be found with given name. 
         @return markupElement (@link Element NXOpen.Markup.Element@endlink):  @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  with this id .
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::Markup::Element NXOpen::Markup::Element@endlink  on the screen.
##      <br> This is an abstract class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Element(NXOpen.DisplayableObject): 
    """
        Represents a <ja_class>NXOpen.Markup.Element</ja_class> on the screen.
    """


    ## Getter for property: (str) Comment
    ##  Returns the comment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
         Returns the comment   
            
         
        """
        pass
    
    ## Setter for property: (str) Comment

    ##  Returns the comment   
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
         Returns the comment   
            
         
        """
        pass
    
    ## Getter for property: (bool) PinToScreen
    ##  Returns the pin to screen   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PinToScreen(self) -> bool:
        """
        Getter for property: (bool) PinToScreen
         Returns the pin to screen   
            
         
        """
        pass
    
    ## Setter for property: (bool) PinToScreen

    ##  Returns the pin to screen   
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PinToScreen.setter
    def PinToScreen(self, pin: bool):
        """
        Setter for property: (bool) PinToScreen
         Returns the pin to screen   
            
         
        """
        pass
    
    ##  Gets the anchor objects 
    ##  @return anchorObjs (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetAnchorObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the anchor objects 
         @return anchorObjs (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Gets the anchor point 
    ##  @return anchorPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetAnchorPoint(self) -> NXOpen.Point3d:
        """
         Gets the anchor point 
         @return anchorPoint (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets the location 
    ##  @return location (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetLocation(self) -> NXOpen.Point3d:
        """
         Gets the location 
         @return location (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Gets parent @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  
    ##  @return markup (@link Markup NXOpen.Markup.Markup@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetParentMarkup(self) -> Markup:
        """
         Gets parent @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  
         @return markup (@link Markup NXOpen.Markup.Markup@endlink): .
        """
        pass
    
    ##  Gets the terminating objects 
    ##  @return terminatingObjs (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetTerminatingObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the terminating objects 
         @return terminatingObjs (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Sets the anchor objects 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="anchorObjs"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def SetAnchorObjects(self, anchorObjs: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the anchor objects 
        """
        pass
    
    ##  Sets the anchor point 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="anchorPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def SetAnchorPoint(self, anchorPoint: NXOpen.Point3d) -> None:
        """
         Sets the anchor point 
        """
        pass
    
    ##  Sets the location 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="location"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def SetLocation(self, location: NXOpen.Point3d) -> None:
        """
         Sets the location 
        """
        pass
    
    ##  Sets the terminating objects 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="terminatingObjs"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def SetTerminatingObjects(self, terminatingObjs: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the terminating objects 
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::Markup::Ellipse NXOpen::Markup::Ellipse@endlink 
##      <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Ellipse(Element): 
    """
        Represents a <ja_class>NXOpen.Markup.Ellipse</ja_class>
    """


    ##  Gets center and radius 
    ##  @return A tuple consisting of (center, majorRadius, minorRadius). 
    ##  - center is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - majorRadius is: float.
    ##  - minorRadius is: float.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetCenterAndRadius(self) -> Tuple[NXOpen.Point3d, float, float]:
        """
         Gets center and radius 
         @return A tuple consisting of (center, majorRadius, minorRadius). 
         - center is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - majorRadius is: float.
         - minorRadius is: float.

        """
        pass
    
    ##  Sets center and radius 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="majorRadius"> (float) </param>
    ## <param name="minorRadius"> (float) </param>
    def SetCenterAndRadius(self, center: NXOpen.Point3d, majorRadius: float, minorRadius: float) -> None:
        """
         Sets center and radius 
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::Markup::Freehand NXOpen::Markup::Freehand@endlink 
##      <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Freehand(Element): 
    """
        Represents a <ja_class>NXOpen.Markup.Freehand</ja_class>
    """


    ##  Gets a list of points 
    ##  @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets a list of points 
         @return points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
        """
        pass
    
    ##  Sets a list of points 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="points"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink) </param>
    def SetPoints(self, points: List[NXOpen.Point3d]) -> None:
        """
         Sets a list of points 
        """
        pass
    
## 
##         Represents a @link NXOpen::Markup::InsetImage NXOpen::Markup::InsetImage@endlink 
##      <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class InsetImage(Element): 
    """
        Represents a <ja_class>NXOpen.Markup.InsetImage</ja_class>
    """
    pass


import NXOpen
##  The @link NXOpen::Markup::MarkupBuilder NXOpen::Markup::MarkupBuilder@endlink  which is used to edit properties of or create @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  <br> To create a new instance of this class, use @link NXOpen::Markup::MarkupCollection::CreateMarkupBuilder  NXOpen::Markup::MarkupCollection::CreateMarkupBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class MarkupBuilder(NXOpen.Builder): 
    """ The <ja_class>NXOpen.Markup.MarkupBuilder</ja_class> which is used to edit properties of or create <ja_class>NXOpen.Markup.Markup</ja_class>. """


    ## Getter for property: (bool) Active
    ##  Returns  @brief  the active status of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns  @brief  the active status of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
            
        
           
         
        """
        pass
    
    ## Setter for property: (bool) Active

    ##  Returns  @brief  the active status of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Active.setter
    def Active(self, active: bool):
        """
        Setter for property: (bool) Active
         Returns  @brief  the active status of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
            
        
           
         
        """
        pass
    
    ## Getter for property: (bool) CaptureView
    ##  Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  will capture current view.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def CaptureView(self) -> bool:
        """
        Getter for property: (bool) CaptureView
         Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  will capture current view.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) CaptureView

    ##  Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  will capture current view.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CaptureView.setter
    def CaptureView(self, captureView: bool):
        """
        Setter for property: (bool) CaptureView
         Returns  @brief  a value that, if true, indicates that the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  will capture current view.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (str) MarkupName
    ##  Returns  @brief  the name of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def MarkupName(self) -> str:
        """
        Getter for property: (str) MarkupName
         Returns  @brief  the name of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
            
        
            
         
        """
        pass
    
    ## Setter for property: (str) MarkupName

    ##  Returns  @brief  the name of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MarkupName.setter
    def MarkupName(self, markupName: str):
        """
        Setter for property: (str) MarkupName
         Returns  @brief  the name of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink .  
            
        
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Markup::MarkupCollection NXOpen::Markup::MarkupCollection@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class MarkupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a <ja_class>NXOpen.Markup.MarkupCollection</ja_class> """


    ##  Adds a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with a default markup name
    ##  @return layer (@link Markup NXOpen.Markup.Markup@endlink):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="part"> (@link MarkupCollection NXOpen.Markup.MarkupCollection@endlink) </param>
    @overload
    def CreateMarkup(self) -> Markup:
        """
         Adds a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with a default markup name
         @return layer (@link Markup NXOpen.Markup.Markup@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Markup::MarkupBuilder NXOpen::Markup::MarkupBuilder@endlink  
    ##  @return builder (@link MarkupBuilder NXOpen.Markup.MarkupBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="layer"> (@link Markup NXOpen.Markup.Markup@endlink)  </param>
    def CreateMarkupBuilder(self, layer: Markup) -> MarkupBuilder:
        """
         Creates a @link NXOpen::Markup::MarkupBuilder NXOpen::Markup::MarkupBuilder@endlink  
         @return builder (@link MarkupBuilder NXOpen.Markup.MarkupBuilder@endlink):  .
        """
        pass
    
    ##  Adds a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with a customized markup name
    ##  @return layer (@link Markup NXOpen.Markup.Markup@endlink):  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## <param name="part"> (@link MarkupCollection NXOpen.Markup.MarkupCollection@endlink) </param>
    ## <param name="markupName"> (str) </param>
    @overload
    def CreateMarkup(self, markupName: str) -> Markup:
        """
         Adds a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with a customized markup name
         @return layer (@link Markup NXOpen.Markup.Markup@endlink):  .
        """
        pass
    
    ##  Finds the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with the given id.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return layer (@link Markup NXOpen.Markup.Markup@endlink):  @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with this id .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="id"> (str)  The id of the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  </param>
    def FindObject(self, id: str) -> Markup:
        """
         Finds the @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with the given id.
                    An exception will be thrown if no object can be found with given name. 
         @return layer (@link Markup NXOpen.Markup.Markup@endlink):  @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  with this id .
        """
        pass
    
    ##  Gets the active @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink 
    ##  @return layer (@link Markup NXOpen.Markup.Markup@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetActive(self) -> Markup:
        """
         Gets the active @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink 
         @return layer (@link Markup NXOpen.Markup.Markup@endlink): .
        """
        pass
    
    ##  Activates a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="layer"> (@link Markup NXOpen.Markup.Markup@endlink)  </param>
    def MakeActive(self, layer: Markup) -> None:
        """
         Activates a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  
        """
        pass
    
    ##  Deactivates a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="layer"> (@link Markup NXOpen.Markup.Markup@endlink)  </param>
    def MakeInactive(self, layer: Markup) -> None:
        """
         Deactivates a @link NXOpen::Markup::Markup NXOpen::Markup::Markup@endlink  
        """
        pass
    
    ##  Restores the unpasted Markup elements in the part.
    ##              <br> 
    ##             This method is used in an interactive NX session to restore Markup elements that
    ##             were cut but not pasted.  <br>  
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def RestoreUnpastedObjects(self) -> None:
        """
         Restores the unpasted Markup elements in the part.
                     <br> 
                    This method is used in an interactive NX session to restore Markup elements that
                    were cut but not pasted.  <br>  
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink 
##      <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Rectangle(Element): 
    """
        Represents a <ja_class>NXOpen.Markup.Rectangle</ja_class>
    """


    ##  Gets center length and width 
    ##  @return A tuple consisting of (center, length, width). 
    ##  - center is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - length is: float.
    ##  - width is: float.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetCenterLengthAndWidth(self) -> Tuple[NXOpen.Point3d, float, float]:
        """
         Gets center length and width 
         @return A tuple consisting of (center, length, width). 
         - center is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - length is: float.
         - width is: float.

        """
        pass
    
    ##  Sets center length and width 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="center"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="length"> (float) </param>
    ## <param name="width"> (float) </param>
    def SetCenterLengthAndWidth(self, center: NXOpen.Point3d, length: float, width: float) -> None:
        """
         Sets center length and width 
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink 
##      <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Text(Element): 
    """
        Represents a <ja_class>NXOpen.Markup.Text</ja_class>
    """


    ##  Text scale options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## One</term><description> 
    ## </description> </item><item><term> 
    ## Two</term><description> 
    ## </description> </item><item><term> 
    ## Three</term><description> 
    ## </description> </item><item><term> 
    ## Four</term><description> 
    ## </description> </item><item><term> 
    ## Five</term><description> 
    ## </description> </item></list>
    class ScaleOptions(Enum):
        """
        Members Include: <One> <Two> <Three> <Four> <Five>
        """
        One: int
        Two: int
        Three: int
        Four: int
        Five: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Text.ScaleOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IncludeLabels
    ##  Returns  @brief  a value that, if true, indicates that the lable of Text Recipe (like Part Name, Part Heritage, etc.  
    ##   .) is included in the text.  
    ## 
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def IncludeLabels(self) -> bool:
        """
        Getter for property: (bool) IncludeLabels
         Returns  @brief  a value that, if true, indicates that the lable of Text Recipe (like Part Name, Part Heritage, etc.  
          .) is included in the text.  
        
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeLabels

    ##  Returns  @brief  a value that, if true, indicates that the lable of Text Recipe (like Part Name, Part Heritage, etc.  
    ##   .) is included in the text.  
    ## 
    ##     
    ##  
    ## Setter License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @IncludeLabels.setter
    def IncludeLabels(self, includeLabels: bool):
        """
        Setter for property: (bool) IncludeLabels
         Returns  @brief  a value that, if true, indicates that the lable of Text Recipe (like Part Name, Part Heritage, etc.  
          .) is included in the text.  
        
            
         
        """
        pass
    
    ##   @brief  Gets the 2D location  
    ## 
    ##  
    ##             <remark> Only applies to pin-to-screen @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  elements.
    ##             2D points are in the range of [0, 1] where origin point (0, 0) is lower-left corner of current screen,
    ##             and (1, 1) is upper-right corner.</remark>
    ##  @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def Get2DLocation(self) -> NXOpen.Point2d:
        """
          @brief  Gets the 2D location  
        
         
                    <remark> Only applies to pin-to-screen @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  elements.
                    2D points are in the range of [0, 1] where origin point (0, 0) is lower-left corner of current screen,
                    and (1, 1) is upper-right corner.</remark>
         @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
        """
        pass
    
    ##   @brief  Sets the 2D location  
    ## 
    ##  
    ##             <remark> Only applies to pin-to-screen @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  elements.
    ##             2D points are in the range of [0, 1] where origin point (0, 0) is lower-left corner of current screen,
    ##             and (1, 1) is upper-right corner.</remark>
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: dmu_markup ("License to expose DMU functionality in NX desktop")
    ## 
    ## <param name="location"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def Set2DLocation(self, location: NXOpen.Point2d) -> None:
        """
          @brief  Sets the 2D location  
        
         
                    <remark> Only applies to pin-to-screen @link NXOpen::Markup::Text NXOpen::Markup::Text@endlink  elements.
                    2D points are in the range of [0, 1] where origin point (0, 0) is lower-left corner of current screen,
                    and (1, 1) is upper-right corner.</remark>
        """
        pass
    
## @package NXOpen.Markup
## Classes, Enums and Structs under NXOpen.Markup namespace

##  @link ElementBuilderStyles NXOpen.Markup.ElementBuilderStyles @endlink is an alias for @link ElementBuilder.Styles NXOpen.Markup.ElementBuilder.Styles@endlink
ElementBuilderStyles = ElementBuilder.Styles


##  @link TextScaleOptions NXOpen.Markup.TextScaleOptions @endlink is an alias for @link Text.ScaleOptions NXOpen.Markup.Text.ScaleOptions@endlink
TextScaleOptions = Text.ScaleOptions


