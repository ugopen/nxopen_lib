from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Circle(Element): 
    """
        Represents a NXOpen.Markup.Circle
    """
    def GetCenterAndRadius(self) -> Tuple[NXOpen.Point3d, float]:
        """
         Gets center and radius 
         Returns A tuple consisting of (center, radius). 
         - center is:  NXOpen.Point3d.
         - radius is: float.

        """
        pass
    def SetCenterAndRadius(self, center: NXOpen.Point3d, radius: float) -> None:
        """
         Sets center and radius 
        """
        pass
import NXOpen
import NXOpen.Features
class EditElementDisplayBuilder(NXOpen.Builder): 
    """ The NXOpen.Markup.EditElementDisplayBuilder is used to edit display settings of the markup objects. """
    @property
    def EnableBackground(self) -> bool:
        """
        Getter for property: (bool) EnableBackground
         Returns the  NXOpen::Markup::Text  enable background setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @EnableBackground.setter
    def EnableBackground(self, enableBackground: bool):
        """
        Setter for property: (bool) EnableBackground
         Returns the  NXOpen::Markup::Text  enable background setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def LineColor(self) -> int:
        """
        Getter for property: (int) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    @LineColor.setter
    def LineColor(self, colorIndex: int):
        """
        Setter for property: (int) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    @property
    def Strikethrough(self) -> bool:
        """
        Getter for property: (bool) Strikethrough
         Returns the  NXOpen::Markup::Text  strikethrough setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @Strikethrough.setter
    def Strikethrough(self, strikethrough: bool):
        """
        Setter for property: (bool) Strikethrough
         Returns the  NXOpen::Markup::Text  strikethrough setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def TextColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TextColor
         Returns the text color index value of the  NXOpen::Markup::Text  object, whose range is from 1 to 216.  
             
         
        """
        pass
    @TextColor.setter
    def TextColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TextColor
         Returns the text color index value of the  NXOpen::Markup::Text  object, whose range is from 1 to 216.  
             
         
        """
        pass
    @property
    def TextFont(self) -> str:
        """
        Getter for property: (str) TextFont
         Returns the font for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @TextFont.setter
    def TextFont(self, textFont: str):
        """
        Setter for property: (str) TextFont
         Returns the font for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def TextFontStyle(self) -> NXOpen.Features.TextBuilder.FontStyleOptions:
        """
        Getter for property: ( NXOpen.Features.TextBuilder.FontStyleOptions) TextFontStyle
         Returns the font style for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @TextFontStyle.setter
    def TextFontStyle(self, textFontStyle: NXOpen.Features.TextBuilder.FontStyleOptions):
        """
        Setter for property: ( NXOpen.Features.TextBuilder.FontStyleOptions) TextFontStyle
         Returns the font style for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def TextScale(self) -> Text.ScaleOptions:
        """
        Getter for property: ( Text.ScaleOptions NXOpen) TextScale
         Returns the scale for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text   only.   
         
        """
        pass
    @TextScale.setter
    def TextScale(self, textScale: Text.ScaleOptions):
        """
        Setter for property: ( Text.ScaleOptions NXOpen) TextScale
         Returns the scale for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text   only.   
         
        """
        pass
    @property
    def Underline(self) -> bool:
        """
        Getter for property: (bool) Underline
         Returns the  NXOpen::Markup::Text  underline setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @Underline.setter
    def Underline(self, underline: bool):
        """
        Setter for property: (bool) Underline
         Returns the  NXOpen::Markup::Text  underline setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
import NXOpen
import NXOpen.Features
class ElementBuilder(NXOpen.Builder): 
    """ The NXOpen.Markup.ElementBuilder which is used to edit properties of or create NXOpen.Markup.Element. """
    class Styles(Enum):
        """
        Members Include: 
         |Freehand|  Freehand style
         |Text|  Text style
         |Circle|  Circle style
         |Ellipse|  Ellipse style
         |Rectangle|  Rectangle style
         |Icon|  Icon style, reserved for future use 
         |Polyline|  Polyline style, reserved for future use 
         |Polygon|  Polygon style, reserved for future use 
         |Line|  Line style, reserved for future use 
         |InsetImage|  Inset Image style, reserved for future use 

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
        @staticmethod
        def ValueOf(value: int) -> ElementBuilder.Styles:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CircleSize(self) -> float:
        """
        Getter for property: (float) CircleSize
         Returns    the size that was created or edited from  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Circle  .  
            
            
         
        """
        pass
    @CircleSize.setter
    def CircleSize(self, radius: float):
        """
        Setter for property: (float) CircleSize
         Returns    the size that was created or edited from  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Circle  .  
            
            
         
        """
        pass
    @property
    def EnableBackground(self) -> bool:
        """
        Getter for property: (bool) EnableBackground
         Returns the  NXOpen::Markup::Text  enable background setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @EnableBackground.setter
    def EnableBackground(self, enableBackground: bool):
        """
        Setter for property: (bool) EnableBackground
         Returns the  NXOpen::Markup::Text  enable background setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def Geometries(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Geometries
         Returns    the geometry of interest that was created or edited by  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Element  .  
            
            
         
        """
        pass
    @property
    def IconName(self) -> str:
        """
        Getter for property: (str) IconName
         Returns    the name of icon used by the  NXOpen::Markup::Icon  that was created or edited from  NXOpen::Markup::ElementBuilder .  
            
            
         
        """
        pass
    @IconName.setter
    def IconName(self, iconBitmap: str):
        """
        Setter for property: (str) IconName
         Returns    the name of icon used by the  NXOpen::Markup::Icon  that was created or edited from  NXOpen::Markup::ElementBuilder .  
            
            
         
        """
        pass
    @property
    def IncludeLabels(self) -> bool:
        """
        Getter for property: (bool) IncludeLabels
         Returns the  NXOpen::Markup::Text  show label setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @IncludeLabels.setter
    def IncludeLabels(self, includeLabels: bool):
        """
        Setter for property: (bool) IncludeLabels
         Returns the  NXOpen::Markup::Text  show label setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def LeaderLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LeaderLineColor
         Returns the leader line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    @LeaderLineColor.setter
    def LeaderLineColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LeaderLineColor
         Returns the leader line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    @property
    def LeaderLineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) LeaderLineFont
         Returns the leader line font of the markup object.  
             
         
        """
        pass
    @LeaderLineFont.setter
    def LeaderLineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) LeaderLineFont
         Returns the leader line font of the markup object.  
             
         
        """
        pass
    @property
    def LeaderLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LeaderLineWidth
         Returns the leader line width of the markup object.  
             
         
        """
        pass
    @LeaderLineWidth.setter
    def LeaderLineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LeaderLineWidth
         Returns the leader line width of the markup object.  
             
         
        """
        pass
    @property
    def LineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    @LineColor.setter
    def LineColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LineColor
         Returns the line color index value of the markup object, whose range is from 1 to 216.  
             
         
        """
        pass
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font of the markup object.  
             
         
        """
        pass
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width of the markup object.  
             
         
        """
        pass
    @property
    def Location(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Location
         Returns    the location that was created or edited from  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Element  .  
            
         
                 For different style of  NXOpen::Markup::Element , the definitions of location are:
                  
                
                 NXOpen::Markup::Circle : the circle center.
                 NXOpen::Markup::Ellipse : the ellipse center.
                 NXOpen::Markup::Icon : the bitmap position.
                 NXOpen::Markup::Freehand : the initial point in drawing the freehand shape.
                 NXOpen::Markup::Rectangle : the rectangle center.
                 NXOpen::Markup::Text : the textanchored position.
                
                  
                  
         
        """
        pass
    @Location.setter
    def Location(self, point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Location
         Returns    the location that was created or edited from  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Element  .  
            
         
                 For different style of  NXOpen::Markup::Element , the definitions of location are:
                  
                
                 NXOpen::Markup::Circle : the circle center.
                 NXOpen::Markup::Ellipse : the ellipse center.
                 NXOpen::Markup::Icon : the bitmap position.
                 NXOpen::Markup::Freehand : the initial point in drawing the freehand shape.
                 NXOpen::Markup::Rectangle : the rectangle center.
                 NXOpen::Markup::Text : the textanchored position.
                
                  
                  
         
        """
        pass
    @property
    def PinToScreen(self) -> bool:
        """
        Getter for property: (bool) PinToScreen
         Returns    a value that, if true, indicates that the  NXOpen::Markup::Text  will pinned to screen.  
            
         
                Only applies to  NXOpen::Markup::Text .  
         
        """
        pass
    @PinToScreen.setter
    def PinToScreen(self, pinToScreen: bool):
        """
        Setter for property: (bool) PinToScreen
         Returns    a value that, if true, indicates that the  NXOpen::Markup::Text  will pinned to screen.  
            
         
                Only applies to  NXOpen::Markup::Text .  
         
        """
        pass
    @property
    def Strikethrough(self) -> bool:
        """
        Getter for property: (bool) Strikethrough
         Returns the  NXOpen::Markup::Text  strikethrough setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @Strikethrough.setter
    def Strikethrough(self, strikethrough: bool):
        """
        Setter for property: (bool) Strikethrough
         Returns the  NXOpen::Markup::Text  strikethrough setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def Style(self) -> ElementBuilder.Styles:
        """
        Getter for property: ( ElementBuilder.Styles NXOpen) Style
         Returns    the style that was created or edited from  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Element  .  
            
            
         
        """
        pass
    @Style.setter
    def Style(self, markupStyle: ElementBuilder.Styles):
        """
        Setter for property: ( ElementBuilder.Styles NXOpen) Style
         Returns    the style that was created or edited from  NXOpen::Markup::ElementBuilder  for:  NXOpen::Markup::Element  .  
            
            
         
        """
        pass
    @property
    def TerminatingObjects(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) TerminatingObjects
         Returns    the terminating objects that was created or edited by  NXOpen::Markup::ElementBuilder  for the leader line of the  NXOpen::Markup::Element  .  
            
         
                Only applies to  NXOpen::Markup::Element  that has leader lines, namely  NXOpen::Markup::Icon  and  NXOpen::Markup::Text .  
         
        """
        pass
    @property
    def TextColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TextColor
         Returns the text color index value of the  NXOpen::Markup::Text  object, whose range is from 1 to 216.  
             
         
        """
        pass
    @TextColor.setter
    def TextColor(self, colorIndex: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TextColor
         Returns the text color index value of the  NXOpen::Markup::Text  object, whose range is from 1 to 216.  
             
         
        """
        pass
    @property
    def TextFont(self) -> str:
        """
        Getter for property: (str) TextFont
         Returns the font for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @TextFont.setter
    def TextFont(self, textFont: str):
        """
        Setter for property: (str) TextFont
         Returns the font for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def TextFontStyle(self) -> NXOpen.Features.TextBuilder.FontStyleOptions:
        """
        Getter for property: ( NXOpen.Features.TextBuilder.FontStyleOptions) TextFontStyle
         Returns the font style for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @TextFontStyle.setter
    def TextFontStyle(self, textFontStyle: NXOpen.Features.TextBuilder.FontStyleOptions):
        """
        Setter for property: ( NXOpen.Features.TextBuilder.FontStyleOptions) TextFontStyle
         Returns the font style for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @property
    def TextScale(self) -> Text.ScaleOptions:
        """
        Getter for property: ( Text.ScaleOptions NXOpen) TextScale
         Returns the scale for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text   only.   
         
        """
        pass
    @TextScale.setter
    def TextScale(self, textScale: Text.ScaleOptions):
        """
        Setter for property: ( Text.ScaleOptions NXOpen) TextScale
         Returns the scale for the  NXOpen::Markup::Text .  
           It applies to  NXOpen::Markup::Text   only.   
         
        """
        pass
    @property
    def Underline(self) -> bool:
        """
        Getter for property: (bool) Underline
         Returns the  NXOpen::Markup::Text  underline setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    @Underline.setter
    def Underline(self, underline: bool):
        """
        Setter for property: (bool) Underline
         Returns the  NXOpen::Markup::Text  underline setting.  
           It applies to  NXOpen::Markup::Text  only.   
         
        """
        pass
    def GetComment(self) -> List[str]:
        """
          Returns the comments that was created or edited from NXOpen.Markup.ElementBuilder for: NXOpen.Markup.Element .  
         Returns comment (List[str]): .
        """
        pass
    def GetEllipseSize(self) -> Tuple[float, float]:
        """
          Returns the size that was created or edited from NXOpen.Markup.ElementBuilder for: NXOpen.Markup.Ellipse .  
         Returns A tuple consisting of (majorRadius, minorRadius). 
         - majorRadius is: float. The major radius of the NXOpen.Markup.Ellipse.
         - minorRadius is: float. The minor radius of the NXOpen.Markup.Ellipse.

        """
        pass
    def GetRectangleSize(self) -> Tuple[float, float]:
        """
          Returns the size that was created or edited from NXOpen.Markup.ElementBuilder for: NXOpen.Markup.Rectangle .  
         Returns A tuple consisting of (length, width). 
         - length is: float. The length of the NXOpen.Markup.Rectangle.
         - width is: float. The width of the NXOpen.Markup.Rectangle.

        """
        pass
    def GetTextContent(self) -> List[str]:
        """
          Returns the content of the NXOpen.Markup.Text that was created or edited from NXOpen.Markup.ElementBuilder.  
         Returns comment (List[str]): .
        """
        pass
    def SetComment(self, comment: List[str]) -> None:
        """
          Sets the comments that waas created or edited from NXOpen.Markup.ElementBuilder for: NXOpen.Markup.Element .  
        """
        pass
    def SetEllipseSize(self, majorRadius: float, minorRadius: float) -> None:
        """
          Sets the size that was created or edited from NXOpen.Markup.ElementBuilder for: NXOpen.Markup.Ellipse .  
        """
        pass
    def SetFreehandShape(self, controlPoints: List[NXOpen.Point3d]) -> None:
        """
          Sets the points that defines the shaped of NXOpen.Markup.Freehand.  
        """
        pass
    def SetRectangleSize(self, length: float, width: float) -> None:
        """
          Sets the size that was created or edited by NXOpen.Markup.ElementBuilder for: NXOpen.Markup.Rectangle .  
        """
        pass
    def SetTextContent(self, comment: List[str]) -> None:
        """
          Sets the content of the NXOpen.Markup.Text that was created or edited from NXOpen.Markup.ElementBuilder.  
        """
        pass
import NXOpen
class ElementCollection(NXOpen.TaggedObjectCollection): 
    """ This collects all the markups in the NXOpen.Markup.Markup """
    def CopyObjects(self, input_objects: List[Element]) -> List[Element]:
        """
         Creates copies of input NXOpen.Markup.Element objects into the markup. 
                    
                    Client must perform update NXOpen.Update.DoUpdate after calling 
                    this method.  
         Returns output_objects ( Element List[NXOp):  Copies of Markup Elements .
        """
        pass
    @overload
    def CreateCircle(self, center: NXOpen.Point3d, radius: float) -> Circle:
        """
         Creates a pin to screen NXOpen.Markup.Circle 
         Returns circle ( Circle NXOpen): .
        """
        pass
    @overload
    def CreateCircle(self, anchorPoint: NXOpen.Point3d, center: NXOpen.Point3d, radius: float) -> Circle:
        """
         Creates a NXOpen.Markup.Circle with anchor point 
         Returns circle ( Circle NXOpen): .
        """
        pass
    def CreateEditElementDisplayBuilder(self, objects: List[Element]) -> EditElementDisplayBuilder:
        """
         Creates a NXOpen.Markup.EditElementDisplayBuilder 
         Returns builder ( EditElementDisplayBuilder NXOpen):  .
        """
        pass
    def CreateElementBuilder(self, annotation: Element) -> ElementBuilder:
        """
         Creates a NXOpen.Markup.ElementBuilder 
         Returns builder ( ElementBuilder NXOpen):  .
        """
        pass
    @overload
    def CreateEllipse(self, center: NXOpen.Point3d, major: float, minor: float) -> Ellipse:
        """
         Creates a pin to screen NXOpen.Markup.Ellipse 
         Returns ellipse ( Ellipse NXOpen): .
        """
        pass
    @overload
    def CreateEllipse(self, anchorPoint: NXOpen.Point3d, center: NXOpen.Point3d, major: float, minor: float) -> Ellipse:
        """
         Creates a NXOpen.Markup.Ellipse with anchor point 
         Returns ellipse ( Ellipse NXOpen): .
        """
        pass
    @overload
    def CreateFreehand(self, points: List[NXOpen.Point3d]) -> Freehand:
        """
         Creates a pin to screen NXOpen.Markup.Freehand 
         Returns freehand ( Freehand NXOpen): .
        """
        pass
    @overload
    def CreateFreehand(self, anchorPoint: NXOpen.Point3d, points: List[NXOpen.Point3d]) -> Freehand:
        """
         Creates a NXOpen.Markup.Freehand with anchor point 
         Returns freehand ( Freehand NXOpen): .
        """
        pass
    @overload
    def CreateRectangle(self, center: NXOpen.Point3d, length: float, width: float) -> Rectangle:
        """
         Creates a pin to screen NXOpen.Markup.Rectangle 
         Returns rectangle ( Rectangle NXOpen): .
        """
        pass
    @overload
    def CreateRectangle(self, anchorPoint: NXOpen.Point3d, center: NXOpen.Point3d, length: float, width: float) -> Rectangle:
        """
         Creates a NXOpen.Markup.Rectangle with anchor point 
         Returns rectangle ( Rectangle NXOpen): .
        """
        pass
    def CreateText(self, position: NXOpen.Point3d, textContent: str) -> Text:
        """
         Creates a NXOpen.Markup.Text 
         Returns text ( Text NXOpen): .
        """
        pass
    def CutObjects(self, input_objects: List[Element]) -> List[Element]:
        """
         Cuts the input NXOpen.Markup.Element objects into the markup. 
                    
                    Client must perform update NXOpen.Update.DoUpdate after calling 
                    this method.  
         Returns output_objects ( Element List[NXOp):  Markup Elements moved to new Markup .
        """
        pass
    def FindObject(self, id: str) -> Element:
        """
         Finds the NXOpen.Markup.Element with the given id in current markup.
                    An exception will be thrown if no object can be found with given name. 
         Returns markupElement ( Element NXOpen):  NXOpen.Markup.Element with this id .
        """
        pass
import NXOpen
class Element(NXOpen.DisplayableObject): 
    """
        Represents a NXOpen.Markup.Element on the screen.
    """
    @property
    def Comment(self) -> str:
        """
        Getter for property: (str) Comment
         Returns the comment   
            
         
        """
        pass
    @Comment.setter
    def Comment(self, comment: str):
        """
        Setter for property: (str) Comment
         Returns the comment   
            
         
        """
        pass
    @property
    def PinToScreen(self) -> bool:
        """
        Getter for property: (bool) PinToScreen
         Returns the pin to screen   
            
         
        """
        pass
    @PinToScreen.setter
    def PinToScreen(self, pin: bool):
        """
        Setter for property: (bool) PinToScreen
         Returns the pin to screen   
            
         
        """
        pass
    def GetAnchorObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the anchor objects 
         Returns anchorObjs ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetAnchorPoint(self) -> NXOpen.Point3d:
        """
         Gets the anchor point 
         Returns anchorPoint ( NXOpen.Point3d): .
        """
        pass
    def GetLocation(self) -> NXOpen.Point3d:
        """
         Gets the location 
         Returns location ( NXOpen.Point3d): .
        """
        pass
    def GetParentMarkup(self) -> Markup:
        """
         Gets parent NXOpen.Markup.Markup 
         Returns markup ( Markup NXOpen): .
        """
        pass
    def GetTerminatingObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the terminating objects 
         Returns terminatingObjs ( NXOpen.DisplayableObject Li): .
        """
        pass
    def SetAnchorObjects(self, anchorObjs: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the anchor objects 
        """
        pass
    def SetAnchorPoint(self, anchorPoint: NXOpen.Point3d) -> None:
        """
         Sets the anchor point 
        """
        pass
    def SetLocation(self, location: NXOpen.Point3d) -> None:
        """
         Sets the location 
        """
        pass
    def SetTerminatingObjects(self, terminatingObjs: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the terminating objects 
        """
        pass
import NXOpen
class Ellipse(Element): 
    """
        Represents a NXOpen.Markup.Ellipse
    """
    def GetCenterAndRadius(self) -> Tuple[NXOpen.Point3d, float, float]:
        """
         Gets center and radius 
         Returns A tuple consisting of (center, majorRadius, minorRadius). 
         - center is:  NXOpen.Point3d.
         - majorRadius is: float.
         - minorRadius is: float.

        """
        pass
    def SetCenterAndRadius(self, center: NXOpen.Point3d, majorRadius: float, minorRadius: float) -> None:
        """
         Sets center and radius 
        """
        pass
import NXOpen
class Freehand(Element): 
    """
        Represents a NXOpen.Markup.Freehand
    """
    def GetPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets a list of points 
         Returns points ( NXOpen.Point3d Li): .
        """
        pass
    def SetPoints(self, points: List[NXOpen.Point3d]) -> None:
        """
         Sets a list of points 
        """
        pass
class InsetImage(Element): 
    """
        Represents a NXOpen.Markup.InsetImage
    """
    pass
import NXOpen
class MarkupBuilder(NXOpen.Builder): 
    """ The NXOpen.Markup.MarkupBuilder which is used to edit properties of or create NXOpen.Markup.Markup. """
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns    the active status of the  NXOpen::Markup::Markup .  
            
           
         
        """
        pass
    @Active.setter
    def Active(self, active: bool):
        """
        Setter for property: (bool) Active
         Returns    the active status of the  NXOpen::Markup::Markup .  
            
           
         
        """
        pass
    @property
    def CaptureView(self) -> bool:
        """
        Getter for property: (bool) CaptureView
         Returns    a value that, if true, indicates that the  NXOpen::Markup::Markup  will capture current view.  
            
            
         
        """
        pass
    @CaptureView.setter
    def CaptureView(self, captureView: bool):
        """
        Setter for property: (bool) CaptureView
         Returns    a value that, if true, indicates that the  NXOpen::Markup::Markup  will capture current view.  
            
            
         
        """
        pass
    @property
    def MarkupName(self) -> str:
        """
        Getter for property: (str) MarkupName
         Returns    the name of the  NXOpen::Markup::Markup .  
            
            
         
        """
        pass
    @MarkupName.setter
    def MarkupName(self, markupName: str):
        """
        Setter for property: (str) MarkupName
         Returns    the name of the  NXOpen::Markup::Markup .  
            
            
         
        """
        pass
import NXOpen
class MarkupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a NXOpen.Markup.MarkupCollection """
    @overload
    def CreateMarkup(self) -> Markup:
        """
         Adds a NXOpen.Markup.Markup with a default markup name
         Returns layer ( Markup NXOpen):  .
        """
        pass
    def CreateMarkupBuilder(self, layer: Markup) -> MarkupBuilder:
        """
         Creates a NXOpen.Markup.MarkupBuilder 
         Returns builder ( MarkupBuilder NXOpen):  .
        """
        pass
    @overload
    def CreateMarkup(self, markupName: str) -> Markup:
        """
         Adds a NXOpen.Markup.Markup with a customized markup name
         Returns layer ( Markup NXOpen):  .
        """
        pass
    def FindObject(self, id: str) -> Markup:
        """
         Finds the NXOpen.Markup.Markup with the given id.
                    An exception will be thrown if no object can be found with given name. 
         Returns layer ( Markup NXOpen):  NXOpen.Markup.Markup with this id .
        """
        pass
    def GetActive(self) -> Markup:
        """
         Gets the active NXOpen.Markup.Markup
         Returns layer ( Markup NXOpen): .
        """
        pass
    def MakeActive(self, layer: Markup) -> None:
        """
         Activates a NXOpen.Markup.Markup 
        """
        pass
    def MakeInactive(self, layer: Markup) -> None:
        """
         Deactivates a NXOpen.Markup.Markup 
        """
        pass
    def RestoreUnpastedObjects(self) -> None:
        """
         Restores the unpasted Markup elements in the part.
                    
                    This method is used in an interactive NX session to restore Markup elements that
                    were cut but not pasted.  
        """
        pass
import NXOpen
class Rectangle(Element): 
    """
        Represents a NXOpen.Markup.Rectangle
    """
    def GetCenterLengthAndWidth(self) -> Tuple[NXOpen.Point3d, float, float]:
        """
         Gets center length and width 
         Returns A tuple consisting of (center, length, width). 
         - center is:  NXOpen.Point3d.
         - length is: float.
         - width is: float.

        """
        pass
    def SetCenterLengthAndWidth(self, center: NXOpen.Point3d, length: float, width: float) -> None:
        """
         Sets center length and width 
        """
        pass
import NXOpen
class Text(Element): 
    """
        Represents a NXOpen.Markup.Text
    """
    class ScaleOptions(Enum):
        """
        Members Include: 
         |One| 
         |Two| 
         |Three| 
         |Four| 
         |Five| 

        """
        One: int
        Two: int
        Three: int
        Four: int
        Five: int
        @staticmethod
        def ValueOf(value: int) -> Text.ScaleOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IncludeLabels(self) -> bool:
        """
        Getter for property: (bool) IncludeLabels
         Returns    a value that, if true, indicates that the lable of Text Recipe (like Part Name, Part Heritage, etc.  
          .) is included in the text.  
            
         
        """
        pass
    @IncludeLabels.setter
    def IncludeLabels(self, includeLabels: bool):
        """
        Setter for property: (bool) IncludeLabels
         Returns    a value that, if true, indicates that the lable of Text Recipe (like Part Name, Part Heritage, etc.  
          .) is included in the text.  
            
         
        """
        pass
    def Get2DLocation(self) -> NXOpen.Point2d:
        """
          Gets the 2D location 
                     Only applies to pin-to-screen NXOpen.Markup.Text elements.
                    2D points are in the range of [0, 1] where origin point (0, 0) is lower-left corner of current screen,
                    and (1, 1) is upper-right corner.
         Returns location ( NXOpen.Point2d): .
        """
        pass
    def Set2DLocation(self, location: NXOpen.Point2d) -> None:
        """
          Sets the 2D location 
                     Only applies to pin-to-screen NXOpen.Markup.Text elements.
                    2D points are in the range of [0, 1] where origin point (0, 0) is lower-left corner of current screen,
                    and (1, 1) is upper-right corner.
        """
        pass
