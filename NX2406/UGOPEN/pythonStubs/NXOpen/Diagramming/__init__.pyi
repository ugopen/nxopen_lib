from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
## 
##     Represents a AnnotationBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::AnnotationCollection::CreateAnnotationBuilder  NXOpen::Diagramming::AnnotationCollection::CreateAnnotationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class AnnotationBuilder(ConnectableElementBuilder): 
    """
    Represents a AnnotationBuilder.
    """


    ##  Represents the option @link NXOpen::Diagramming::AnnotationBuilder::TextType NXOpen::Diagramming::AnnotationBuilder::TextType@endlink 
    ##            for a @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fixed</term><description> 
    ##  Setting the text type fixed</description> </item><item><term> 
    ## Parametric</term><description> 
    ##  Setting the text type parametric</description> </item></list>
    class TextTypeOption(Enum):
        """
        Members Include: <Fixed> <Parametric>
        """
        Fixed: int
        Parametric: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnnotationBuilder.TextTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) BoundaryDisplay
    ##  Returns the visibility of boundary.  
    ##    If return true, the annotation will show its boundary if it has one.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def BoundaryDisplay(self) -> bool:
        """
        Getter for property: (bool) BoundaryDisplay
         Returns the visibility of boundary.  
           If return true, the annotation will show its boundary if it has one.   
         
        """
        pass
    
    ## Setter for property: (bool) BoundaryDisplay

    ##  Returns the visibility of boundary.  
    ##    If return true, the annotation will show its boundary if it has one.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @BoundaryDisplay.setter
    def BoundaryDisplay(self, boundaryDisplay: bool):
        """
        Setter for property: (bool) BoundaryDisplay
         Returns the visibility of boundary.  
           If return true, the annotation will show its boundary if it has one.   
         
        """
        pass
    
    ## Getter for property: (@link DiagrammingAnnotationboundarytype NXOpen.Diagramming.DiagrammingAnnotationboundarytype@endlink) BoundaryType
    ##  Returns the boundary type of the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagrammingAnnotationboundarytype
    @property
    def BoundaryType(self) -> DiagrammingAnnotationboundarytype:
        """
        Getter for property: (@link DiagrammingAnnotationboundarytype NXOpen.Diagramming.DiagrammingAnnotationboundarytype@endlink) BoundaryType
         Returns the boundary type of the annotation   
            
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingAnnotationboundarytype NXOpen.Diagramming.DiagrammingAnnotationboundarytype@endlink) BoundaryType

    ##  Returns the boundary type of the annotation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @BoundaryType.setter
    def BoundaryType(self, boundaryType: DiagrammingAnnotationboundarytype):
        """
        Setter for property: (@link DiagrammingAnnotationboundarytype NXOpen.Diagramming.DiagrammingAnnotationboundarytype@endlink) BoundaryType
         Returns the boundary type of the annotation   
            
         
        """
        pass
    
    ## Getter for property: (@link FormattedStringBuilder NXOpen.Diagramming.FormattedStringBuilder@endlink) FormattedStringBuilder
    ##  Returns the formatted string of the text.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return FormattedStringBuilder
    @property
    def FormattedStringBuilder(self) -> FormattedStringBuilder:
        """
        Getter for property: (@link FormattedStringBuilder NXOpen.Diagramming.FormattedStringBuilder@endlink) FormattedStringBuilder
         Returns the formatted string of the text.  
             
         
        """
        pass
    
    ## Getter for property: (str) Text
    ##  Returns the text should be used only when textType is Diagramming.  
    ##   AnnotationBuilder.TextTypeOption.Fixed   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Text(self) -> str:
        """
        Getter for property: (str) Text
         Returns the text should be used only when textType is Diagramming.  
          AnnotationBuilder.TextTypeOption.Fixed   
         
        """
        pass
    
    ## Setter for property: (str) Text

    ##  Returns the text should be used only when textType is Diagramming.  
    ##   AnnotationBuilder.TextTypeOption.Fixed   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Text.setter
    def Text(self, strValue: str):
        """
        Setter for property: (str) Text
         Returns the text should be used only when textType is Diagramming.  
          AnnotationBuilder.TextTypeOption.Fixed   
         
        """
        pass
    
    ## Getter for property: (@link TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
    ##  Returns the text style of the annotation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return TextStyleBuilder
    @property
    def TextStyleBuilder(self) -> TextStyleBuilder:
        """
        Getter for property: (@link TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
         Returns the text style of the annotation.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnnotationBuilder.TextTypeOption NXOpen.Diagramming.AnnotationBuilder.TextTypeOption@endlink) TextType
    ##  Returns the text type.  
    ##    If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed@endlink , the text
    ##             of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink . 
    ##             If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric@endlink , the text
    ##             of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return AnnotationBuilder.TextTypeOption
    @property
    def TextType(self) -> AnnotationBuilder.TextTypeOption:
        """
        Getter for property: (@link AnnotationBuilder.TextTypeOption NXOpen.Diagramming.AnnotationBuilder.TextTypeOption@endlink) TextType
         Returns the text type.  
           If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed@endlink , the text
                    of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink . 
                    If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric@endlink , the text
                    of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder@endlink .  
         
        """
        pass
    
    ## Setter for property: (@link AnnotationBuilder.TextTypeOption NXOpen.Diagramming.AnnotationBuilder.TextTypeOption@endlink) TextType

    ##  Returns the text type.  
    ##    If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed@endlink , the text
    ##             of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink . 
    ##             If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric@endlink , the text
    ##             of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder@endlink .  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextType.setter
    def TextType(self, textType: AnnotationBuilder.TextTypeOption):
        """
        Setter for property: (@link AnnotationBuilder.TextTypeOption NXOpen.Diagramming.AnnotationBuilder.TextTypeOption@endlink) TextType
         Returns the text type.  
           If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionFixed@endlink , the text
                    of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink . 
                    If @link NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric NXOpen::Diagramming::AnnotationBuilder::TextTypeOptionParametric@endlink , the text
                    of annotation is stored in @link NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder NXOpen::Diagramming::AnnotationBuilder::FormattedStringBuilder@endlink .  
         
        """
        pass
    
import NXOpen
##  Represents a collection of Annotation.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class AnnotationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Annotation. """


    ##  Creates a @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink . 
    ##  @return builder (@link AnnotationBuilder NXOpen.Diagramming.AnnotationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="annotation"> (@link Annotation NXOpen.Diagramming.Annotation@endlink)  @link NXOpen::Diagramming::Annotation NXOpen::Diagramming::Annotation@endlink  to be edited, if NULL then create a new one </param>
    def CreateAnnotationBuilder(self, annotation: Annotation) -> AnnotationBuilder:
        """
         Creates a @link NXOpen::Diagramming::AnnotationBuilder NXOpen::Diagramming::AnnotationBuilder@endlink . 
         @return builder (@link AnnotationBuilder NXOpen.Diagramming.AnnotationBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Annotation NXOpen::Diagramming::Annotation@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return annotation (@link Annotation NXOpen.Diagramming.Annotation@endlink):  @link NXOpen::Diagramming::Annotation NXOpen::Diagramming::Annotation@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Annotation:
        """
         Finds the @link NXOpen::Diagramming::Annotation NXOpen::Diagramming::Annotation@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return annotation (@link Annotation NXOpen.Diagramming.Annotation@endlink):  @link NXOpen::Diagramming::Annotation NXOpen::Diagramming::Annotation@endlink  with this name. .
        """
        pass
    
##  Represents the Annotation class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::AnnotationBuilder  NXOpen::Diagramming::AnnotationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Annotation(ConnectableElement): 
    """ Represents the Annotation class. """
    pass


##  the arrow direction type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## OutofSheet</term><description> 
##  Out of Sheet </description> </item><item><term> 
## IntoSheet</term><description> 
## </description> </item></list>
class ArrowDirectionType(Enum):
    """
    Members Include: <OutofSheet> <IntoSheet>
    """
    OutofSheet: int
    IntoSheet: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ArrowDirectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  the arrow style type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Filled</term><description> 
##  Filled </description> </item><item><term> 
## Closed</term><description> 
##  Closed </description> </item><item><term> 
## ClosedSolid</term><description> 
##  Close Solid </description> </item><item><term> 
## Open</term><description> 
## </description> </item></list>
class ArrowStyleType(Enum):
    """
    Members Include: <Filled> <Closed> <ClosedSolid> <Open>
    """
    Filled: int
    Closed: int
    ClosedSolid: int
    Open: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ArrowStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the axis type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## X</term><description> 
##  X axis </description> </item><item><term> 
## Y</term><description> 
##  Y axis </description> </item></list>
class Axis(Enum):
    """
    Members Include: <X> <Y>
    """
    X: int
    Y: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Axis:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
## 
##     Represents a BaseObjectBuilder.
##      <br> This is an abstract class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BaseObjectBuilder(NXOpen.Builder): 
    """
    Represents a BaseObjectBuilder.
    """
    pass


import NXOpen
##  Represents the BaseObject class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::BaseObjectBuilder  NXOpen::Diagramming::BaseObjectBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BaseObject(NXOpen.DisplayableObject): 
    """ Represents the BaseObject class. """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a BaseSubObjectBuilder.
##      <br> This is an abstract and sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BaseSubObjectBuilder(NXOpen.TaggedObject): 
    """
    Represents a BaseSubObjectBuilder.
    """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a BaseTaggedObjectBuilder.
##      <br> This is an abstract and sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BaseTaggedObjectBuilder(NXOpen.TaggedObject): 
    """
    Represents a BaseTaggedObjectBuilder.
    """
    pass


import NXOpen
## 
##     Represents a BulkEditBuilder to edit bulk of objects.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::DiagrammingManager::CreateBulkEditBuilder  NXOpen::Diagramming::DiagrammingManager::CreateBulkEditBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BulkEditBuilder(NXOpen.Builder): 
    """
    Represents a BulkEditBuilder to edit bulk of objects.
    """


    ## Getter for property: (@link RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RenderingProperties
    ##  Returns the line rendering properties.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return RenderingPropertiesBuilder
    @property
    def RenderingProperties(self) -> RenderingPropertiesBuilder:
        """
        Getter for property: (@link RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RenderingProperties
         Returns the line rendering properties.  
             
         
        """
        pass
    
    ##  Sets the delta value of X coordinate for bulk moving. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="deltaXCoordinate"> (float) </param>
    def SetDeltaXCoordinate(self, deltaXCoordinate: float) -> None:
        """
         Sets the delta value of X coordinate for bulk moving. 
        """
        pass
    
    ##  Sets the delta value of Y coordinate for bulk moving. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="deltaYCoordinate"> (float) </param>
    def SetDeltaYCoordinate(self, deltaYCoordinate: float) -> None:
        """
         Sets the delta value of Y coordinate for bulk moving. 
        """
        pass
    
    ##  Sets the visibility of sheet elements. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="hide"> (bool) </param>
    def SetHide(self, hide: bool) -> None:
        """
         Sets the visibility of sheet elements. 
        """
        pass
    
    ##  Sets the visibility of labels. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="hideLabel"> (bool) </param>
    def SetHideLabel(self, hideLabel: bool) -> None:
        """
         Sets the visibility of labels. 
        """
        pass
    
    ##  Sets the sheet elements for bulk editing. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheetElements"> (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink) </param>
    def SetSheetElements(self, sheetElements: List[SheetElement]) -> None:
        """
         Sets the sheet elements for bulk editing. 
        """
        pass
    
import NXOpen
## 
##     Represents a CannedAnnotationBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::DiagrammingManager::CreateCannedAnnotationBuilder  NXOpen::Diagramming::DiagrammingManager::CreateCannedAnnotationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class CannedAnnotationBuilder(NXOpen.Builder): 
    """
    Represents a CannedAnnotationBuilder.
    """


    ##  Represents the inherit option.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Preferences</term><description> 
    ##  Setting the inherit from preferences option</description> </item><item><term> 
    ## CustomerDefaults</term><description> 
    ##  Setting the inherit from customer defaults option</description> </item><item><term> 
    ## Selection</term><description> 
    ##  Setting the inherit from selection option</description> </item></list>
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
        def ValueOf(value: int) -> CannedAnnotationBuilder.InheritOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AnnotationBuilder NXOpen.Diagramming.AnnotationBuilder@endlink) AnnotationBuilder
    ##  Returns the annotation of this canned annotation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return AnnotationBuilder
    @property
    def AnnotationBuilder(self) -> AnnotationBuilder:
        """
        Getter for property: (@link AnnotationBuilder NXOpen.Diagramming.AnnotationBuilder@endlink) AnnotationBuilder
         Returns the annotation of this canned annotation.  
             
         
        """
        pass
    
    ## Getter for property: (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) LeaderLines
    ##  Returns the list of the leader lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LeaderLineBuilderList
    @property
    def LeaderLines(self) -> LeaderLineBuilderList:
        """
        Getter for property: (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) LeaderLines
         Returns the list of the leader lines.  
             
         
        """
        pass
    
    ## Getter for property: (int) TextBoxIndent
    ##  Returns the indent value of the text box in the canned annotation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def TextBoxIndent(self) -> int:
        """
        Getter for property: (int) TextBoxIndent
         Returns the indent value of the text box in the canned annotation.  
             
         
        """
        pass
    
    ## Setter for property: (int) TextBoxIndent

    ##  Returns the indent value of the text box in the canned annotation.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextBoxIndent.setter
    def TextBoxIndent(self, indent: int):
        """
        Setter for property: (int) TextBoxIndent
         Returns the indent value of the text box in the canned annotation.  
             
         
        """
        pass
    
    ## Getter for property: (bool) TextBoxModifiable
    ##  Returns the flag that indicates if the text box in the canned annotation is modifiable.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def TextBoxModifiable(self) -> bool:
        """
        Getter for property: (bool) TextBoxModifiable
         Returns the flag that indicates if the text box in the canned annotation is modifiable.  
             
         
        """
        pass
    
    ## Setter for property: (bool) TextBoxModifiable

    ##  Returns the flag that indicates if the text box in the canned annotation is modifiable.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextBoxModifiable.setter
    def TextBoxModifiable(self, isModifiable: bool):
        """
        Setter for property: (bool) TextBoxModifiable
         Returns the flag that indicates if the text box in the canned annotation is modifiable.  
             
         
        """
        pass
    
    ## Getter for property: (bool) TextBoxShadowBox
    ##  Returns the flag that indicates if the text box in the canned annotation has shadow box.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def TextBoxShadowBox(self) -> bool:
        """
        Getter for property: (bool) TextBoxShadowBox
         Returns the flag that indicates if the text box in the canned annotation has shadow box.  
             
         
        """
        pass
    
    ## Setter for property: (bool) TextBoxShadowBox

    ##  Returns the flag that indicates if the text box in the canned annotation has shadow box.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @TextBoxShadowBox.setter
    def TextBoxShadowBox(self, isShadowBox: bool):
        """
        Setter for property: (bool) TextBoxShadowBox
         Returns the flag that indicates if the text box in the canned annotation has shadow box.  
             
         
        """
        pass
    
    ##  Create a new @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink  builder. 
    ##  @return leaderLine (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def CreateLeaderLine(self) -> LeaderLineBuilder:
        """
         Create a new @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink  builder. 
         @return leaderLine (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink): .
        """
        pass
    
    ##  Inherit. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inheritOption"> (@link CannedAnnotationBuilder.InheritOption NXOpen.Diagramming.CannedAnnotationBuilder.InheritOption@endlink) </param>
    ## <param name="annotation"> (@link Annotation NXOpen.Diagramming.Annotation@endlink) </param>
    def Inherit(self, inheritOption: CannedAnnotationBuilder.InheritOption, annotation: Annotation) -> None:
        """
         Inherit. 
        """
        pass
    
## 
##     Represents a ConnectableElementBuilder.
##      <br> This is an abstract class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ConnectableElementBuilder(SheetElementBuilder): 
    """
    Represents a ConnectableElementBuilder.
    """


    ##  Gets all ports of this connectable element. 
    ##  @return ports (@link Port List[NXOpen.Diagramming.Port]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetAllPorts(self) -> List[Port]:
        """
         Gets all ports of this connectable element. 
         @return ports (@link Port List[NXOpen.Diagramming.Port]@endlink): .
        """
        pass
    
    ##  Gets ports of this connectable element by the direction. 
    ##  @return ports (@link Port List[NXOpen.Diagramming.Port]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="direction"> (@link Direction NXOpen.Diagramming.Direction@endlink) </param>
    def GetPorts(self, direction: Direction) -> List[Port]:
        """
         Gets ports of this connectable element by the direction. 
         @return ports (@link Port List[NXOpen.Diagramming.Port]@endlink): .
        """
        pass
    
##  Represents the ConnectableElement class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::ConnectableElementBuilder  NXOpen::Diagramming::ConnectableElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ConnectableElement(SheetElement): 
    """ Represents the ConnectableElement class. """
    pass


import NXOpen
## 
##     Represents a ConnectionBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::ConnectionCollection::CreateConnectionBuilder  NXOpen::Diagramming::ConnectionCollection::CreateConnectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ConnectionBuilder(SheetElementBuilder): 
    """
    Represents a ConnectionBuilder.
    """


    ##  Represents the shape type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Orthogonal</term><description> 
    ##  Orthogonal </description> </item><item><term> 
    ## Quadratic</term><description> 
    ##  Quadratic </description> </item><item><term> 
    ## Spline</term><description> 
    ##  Spline </description> </item><item><term> 
    ## Arc</term><description> 
    ##  Arc </description> </item></list>
    class ShapeOption(Enum):
        """
        Members Include: <Orthogonal> <Quadratic> <Spline> <Arc>
        """
        Orthogonal: int
        Quadratic: int
        Spline: int
        Arc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConnectionBuilder.ShapeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Discipline
    ##  Returns the discipline of this connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the discipline of this connection.  
             
         
        """
        pass
    
    ## Setter for property: (str) Discipline

    ##  Returns the discipline of this connection.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
         Returns the discipline of this connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link Port NXOpen.Diagramming.Port@endlink) End
    ##  Returns the end port of this connection.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Port
    @property
    def End(self) -> Port:
        """
        Getter for property: (@link Port NXOpen.Diagramming.Port@endlink) End
         Returns the end port of this connection.  
            
         
        """
        pass
    
    ## Setter for property: (@link Port NXOpen.Diagramming.Port@endlink) End

    ##  Returns the end port of this connection.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @End.setter
    def End(self, endPort: Port):
        """
        Setter for property: (@link Port NXOpen.Diagramming.Port@endlink) End
         Returns the end port of this connection.  
            
         
        """
        pass
    
    ## Getter for property: (@link LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) EndLocation
    ##  Returns the end location of this connection.  
    ##    
    ##             This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LocationBuilder
    @property
    def EndLocation(self) -> LocationBuilder:
        """
        Getter for property: (@link LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) EndLocation
         Returns the end location of this connection.  
           
                    This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL.   
         
        """
        pass
    
    ## Getter for property: (bool) ReverseEnd
    ##  Returns the reversed flag of this connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ReverseEnd(self) -> bool:
        """
        Getter for property: (bool) ReverseEnd
         Returns the reversed flag of this connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link Port NXOpen.Diagramming.Port@endlink) Start
    ##  Returns the start port of this connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Port
    @property
    def Start(self) -> Port:
        """
        Getter for property: (@link Port NXOpen.Diagramming.Port@endlink) Start
         Returns the start port of this connection.  
             
         
        """
        pass
    
    ## Setter for property: (@link Port NXOpen.Diagramming.Port@endlink) Start

    ##  Returns the start port of this connection.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Start.setter
    def Start(self, startPort: Port):
        """
        Setter for property: (@link Port NXOpen.Diagramming.Port@endlink) Start
         Returns the start port of this connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) StartLocation
    ##  Returns the start location of this connection.  
    ##    
    ##             This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LocationBuilder
    @property
    def StartLocation(self) -> LocationBuilder:
        """
        Getter for property: (@link LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) StartLocation
         Returns the start location of this connection.  
           
                    This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.  
         
        """
        pass
    
    ##  Get bending points for polyline to render the connection. 
    ##  @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetBendPoints(self) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the connection. 
         @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
        """
        pass
    
    ##  Gets the connection shape. 
    ##  @return shapeType (@link ConnectionBuilder.ShapeOption NXOpen.Diagramming.ConnectionBuilder.ShapeOption@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetShapeType(self) -> ConnectionBuilder.ShapeOption:
        """
         Gets the connection shape. 
         @return shapeType (@link ConnectionBuilder.ShapeOption NXOpen.Diagramming.ConnectionBuilder.ShapeOption@endlink): .
        """
        pass
    
    ##  Set bending points for polyline to render the connection. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="points"> (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink) </param>
    def SetBendPoints(self, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the connection. 
        """
        pass
    
    ##  Sets the connection shape. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="shapeType"> (@link ConnectionBuilder.ShapeOption NXOpen.Diagramming.ConnectionBuilder.ShapeOption@endlink) </param>
    def SetShapeType(self, shapeType: ConnectionBuilder.ShapeOption) -> None:
        """
         Sets the connection shape. 
        """
        pass
    
import NXOpen
##  Represents a collection of connection.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of connection. """


    ##  Creates a @link NXOpen::Diagramming::ConnectionBuilder NXOpen::Diagramming::ConnectionBuilder@endlink . 
    ##  @return builder (@link ConnectionBuilder NXOpen.Diagramming.ConnectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connection"> (@link Connection NXOpen.Diagramming.Connection@endlink)  @link NXOpen::Diagramming::Connection NXOpen::Diagramming::Connection@endlink  to be edited, if NULL then create a new one </param>
    def CreateConnectionBuilder(self, connection: Connection) -> ConnectionBuilder:
        """
         Creates a @link NXOpen::Diagramming::ConnectionBuilder NXOpen::Diagramming::ConnectionBuilder@endlink . 
         @return builder (@link ConnectionBuilder NXOpen.Diagramming.ConnectionBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Connection NXOpen::Diagramming::Connection@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return connection (@link Connection NXOpen.Diagramming.Connection@endlink):  @link NXOpen::Diagramming::Connection NXOpen::Diagramming::Connection@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Connection:
        """
         Finds the @link NXOpen::Diagramming::Connection NXOpen::Diagramming::Connection@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return connection (@link Connection NXOpen.Diagramming.Connection@endlink):  @link NXOpen::Diagramming::Connection NXOpen::Diagramming::Connection@endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class ConnectionLocationBuilderList(NXOpen.TaggedObject): 
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
    ## <param name="objects"> (@link ConnectionLocationBuilder List[NXOpen.Diagramming.ConnectionLocationBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[ConnectionLocationBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: ConnectionLocationBuilder) -> None:
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
    ## <param name="obj"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: ConnectionLocationBuilder) -> None:
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
    ## <param name="obj"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: ConnectionLocationBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="obj"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: ConnectionLocationBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> ConnectionLocationBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link ConnectionLocationBuilder List[NXOpen.Diagramming.ConnectionLocationBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[ConnectionLocationBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link ConnectionLocationBuilder List[NXOpen.Diagramming.ConnectionLocationBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: ConnectionLocationBuilder) -> None:
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
    ## <param name="objects"> (@link ConnectionLocationBuilder List[NXOpen.Diagramming.ConnectionLocationBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[ConnectionLocationBuilder]) -> None:
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link ConnectionLocationBuilderList NXOpen.Diagramming.ConnectionLocationBuilderList@endlink) </param>
    ## <param name="object1"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link ConnectionLocationBuilder NXOpen.Diagramming.ConnectionLocationBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: ConnectionLocationBuilder, object2: ConnectionLocationBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
## 
##     Represents a ConnectionLocationBuilder.
##      <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ConnectionLocationBuilder(LocationBuilder): 
    """
    Represents a ConnectionLocationBuilder.
    """


    ## Getter for property: (int) SegmentIdentifier
    ##  Returns the segment identifier.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def SegmentIdentifier(self) -> int:
        """
        Getter for property: (int) SegmentIdentifier
         Returns the segment identifier.  
            
         
        """
        pass
    
    ## Setter for property: (int) SegmentIdentifier

    ##  Returns the segment identifier.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @SegmentIdentifier.setter
    def SegmentIdentifier(self, segmentId: int):
        """
        Setter for property: (int) SegmentIdentifier
         Returns the segment identifier.  
            
         
        """
        pass
    
##  Represents the Connection class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::ConnectionBuilder  NXOpen::Diagramming::ConnectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Connection(SheetElement): 
    """ Represents the Connection class. """


    ## Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
    ##  Returns the label of the connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return Annotation
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
         Returns the label of the connection.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming.Tables
##  Represents a @link NXOpen::Diagramming::DefineTitleBlockBuilder NXOpen::Diagramming::DefineTitleBlockBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Diagramming::TitleBlockCollection::CreateDefineTitleBlockBuilder  NXOpen::Diagramming::TitleBlockCollection::CreateDefineTitleBlockBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class DefineTitleBlockBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Diagramming.DefineTitleBlockBuilder</ja_class> builder """


    ## Getter for property: (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) Cells
    ##  Returns the cells   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TitleBlockCellBuilderList
    @property
    def Cells(self) -> TitleBlockCellBuilderList:
        """
        Getter for property: (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) Cells
         Returns the cells   
            
         
        """
        pass
    
    ##  Get the cell builder. 
    ##  @return cell (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="table"> (@link NXOpen.Diagramming.Tables.Table NXOpen.Diagramming.Tables.Table@endlink) </param>
    ## <param name="rowIndex"> (int) </param>
    ## <param name="columnIndex"> (int) </param>
    def GetCell(self, table: NXOpen.Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> TitleBlockCellBuilder:
        """
         Get the cell builder. 
         @return cell (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink): .
        """
        pass
    
    ##  Get tables. 
    ##  @return tables (@link NXOpen.Diagramming.Tables.Table List[NXOpen.Diagramming.Tables.Table]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetTables(self) -> List[NXOpen.Diagramming.Tables.Table]:
        """
         Get tables. 
         @return tables (@link NXOpen.Diagramming.Tables.Table List[NXOpen.Diagramming.Tables.Table]@endlink): .
        """
        pass
    
    ##  Set tables. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tables"> (@link NXOpen.Diagramming.Tables.Table List[NXOpen.Diagramming.Tables.Table]@endlink) </param>
    def SetTables(self, tables: List[NXOpen.Diagramming.Tables.Table]) -> None:
        """
         Set tables. 
        """
        pass
    
##  Represents the alignment. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Left</term><description> 
##  Setting the left alignment </description> </item><item><term> 
## Center</term><description> 
##  Setting the center alignment </description> </item><item><term> 
## Right</term><description> 
##  Setting the right alignment </description> </item><item><term> 
## Justify</term><description> 
##  Setting the justify alignment </description> </item></list>
class DiagrammingAlignment(Enum):
    """
    Members Include: <Left> <Center> <Right> <Justify>
    """
    Left: int
    Center: int
    Right: int
    Justify: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingAlignment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the boundary type of annotation. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  No Boundary Type </description> </item><item><term> 
## Circle</term><description> 
##  Circle Type </description> </item><item><term> 
## Ellipse</term><description> 
##  Ellipse Type </description> </item><item><term> 
## Rectangle</term><description> 
##  Rectangle Type </description> </item><item><term> 
## RoundedRectangle</term><description> 
##  Rounded Rectangle Type </description> </item></list>
class DiagrammingAnnotationboundarytype(Enum):
    """
    Members Include: <NotSet> <Circle> <Ellipse> <Rectangle> <RoundedRectangle>
    """
    NotSet: int
    Circle: int
    Ellipse: int
    Rectangle: int
    RoundedRectangle: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingAnnotationboundarytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the arrow type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  Setting the arrow type none arrow</description> </item><item><term> 
## Open</term><description> 
##  Setting the arrow type open arrow</description> </item><item><term> 
## Filled</term><description> 
##  Setting the arrow type filled arrow</description> </item><item><term> 
## ClosedSolid</term><description> 
##  Setting the arrow type closed solid arrow</description> </item></list>
class DiagrammingArrowtype(Enum):
    """
    Members Include: <NotSet> <Open> <Filled> <ClosedSolid>
    """
    NotSet: int
    Open: int
    Filled: int
    ClosedSolid: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingArrowtype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the horizontal connection label offset position. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Above</term><description> 
##  Above </description> </item><item><term> 
## Below</term><description> 
##  Below </description> </item></list>
class DiagrammingConnectionlabelhorizontaloffsetposition(Enum):
    """
    Members Include: <Above> <Below>
    """
    Above: int
    Below: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingConnectionlabelhorizontaloffsetposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the connection label position. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Start</term><description> 
##  Start </description> </item><item><term> 
## End</term><description> 
##  End </description> </item><item><term> 
## Center</term><description> 
##  Centered </description> </item><item><term> 
## Spaced</term><description> 
##  Spaced </description> </item></list>
class DiagrammingConnectionlabelposition(Enum):
    """
    Members Include: <Start> <End> <Center> <Spaced>
    """
    Start: int
    End: int
    Center: int
    Spaced: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingConnectionlabelposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the vertical connection label offset position. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Left</term><description> 
##  Left </description> </item><item><term> 
## Right</term><description> 
##  Right </description> </item></list>
class DiagrammingConnectionlabelverticaloffsetposition(Enum):
    """
    Members Include: <Left> <Right>
    """
    Left: int
    Right: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingConnectionlabelverticaloffsetposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the flow direction arrow style. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## BottomFilledArrow</term><description> 
## </description> </item><item><term> 
## BottomOpenArrow</term><description> 
## </description> </item><item><term> 
## ClosedArrow</term><description> 
## </description> </item><item><term> 
## ClosedDoubleArrow</term><description> 
## </description> </item><item><term> 
## ClosedDoubleSolidArrow</term><description> 
## </description> </item><item><term> 
## ClosedSolidArrow</term><description> 
## </description> </item><item><term> 
## FilledArrow</term><description> 
## </description> </item><item><term> 
## FilledDoubleArrow</term><description> 
## </description> </item><item><term> 
## OpenArrow</term><description> 
## </description> </item><item><term> 
## OpenDoubleArrow</term><description> 
## </description> </item><item><term> 
## TopFilledArrow</term><description> 
## </description> </item><item><term> 
## TopOpenArrow</term><description> 
## </description> </item></list>
class DiagrammingFlowdirectionarrowstyle(Enum):
    """
    Members Include: <BottomFilledArrow> <BottomOpenArrow> <ClosedArrow> <ClosedDoubleArrow> <ClosedDoubleSolidArrow> <ClosedSolidArrow> <FilledArrow> <FilledDoubleArrow> <OpenArrow> <OpenDoubleArrow> <TopFilledArrow> <TopOpenArrow>
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
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingFlowdirectionarrowstyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the marker type of point. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Cross</term><description> 
##  Cross Type </description> </item><item><term> 
## Circle</term><description> 
##  Circle Type </description> </item></list>
class DiagrammingGeometrypointmarker(Enum):
    """
    Members Include: <Cross> <Circle>
    """
    Cross: int
    Circle: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingGeometrypointmarker:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the jumper priority. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Horizontal</term><description> 
##  Horizontal </description> </item><item><term> 
## Vertical</term><description> 
##  Vertical </description> </item></list>
class DiagrammingJumperprioritytype(Enum):
    """
    Members Include: <Horizontal> <Vertical>
    """
    Horizontal: int
    Vertical: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingJumperprioritytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the jumper type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## U</term><description> 
##  U shape </description> </item><item><term> 
## Break</term><description> 
##  Break </description> </item></list>
class DiagrammingJumpertype(Enum):
    """
    Members Include: <U> <Break>
    """
    U: int
    Break: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingJumpertype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the location style. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Absolute</term><description> 
##  Absolute </description> </item><item><term> 
## Relative</term><description> 
##  Relative </description> </item></list>
class DiagrammingLocationstyle(Enum):
    """
    Members Include: <Absolute> <Relative>
    """
    Absolute: int
    Relative: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingLocationstyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Diagramming.Geometry
import NXOpen.Diagramming.Tables
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class DiagrammingManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ## Getter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet
    ##  Returns the active sheet   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Moved to SheetManager  <br> 

    ## @return Sheet
    @property
    def ActiveSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet

    ##  Returns the active sheet   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Moved to SheetManager  <br> 

    @ActiveSheet.setter
    def ActiveSheet(self, sheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::NodeCollection  NXOpen::Diagramming::NodeCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link NodeCollection NXOpen.Diagramming.NodeCollection@endlink
    @property
    def Nodes() -> NodeCollection:
        """
         Returns the @link NXOpen::Diagramming::NodeCollection  NXOpen::Diagramming::NodeCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::SheetCollection  NXOpen::Diagramming::SheetCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link SheetCollection NXOpen.Diagramming.SheetCollection@endlink
    @property
    def Sheets() -> SheetCollection:
        """
         Returns the @link NXOpen::Diagramming::SheetCollection  NXOpen::Diagramming::SheetCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::ConnectionCollection  NXOpen::Diagramming::ConnectionCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link ConnectionCollection NXOpen.Diagramming.ConnectionCollection@endlink
    @property
    def Connections() -> ConnectionCollection:
        """
         Returns the @link NXOpen::Diagramming::ConnectionCollection  NXOpen::Diagramming::ConnectionCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::GroupCollection  NXOpen::Diagramming::GroupCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link GroupCollection NXOpen.Diagramming.GroupCollection@endlink
    @property
    def Groups() -> GroupCollection:
        """
         Returns the @link NXOpen::Diagramming::GroupCollection  NXOpen::Diagramming::GroupCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::ShapeCollection  NXOpen::Diagramming::ShapeCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link ShapeCollection NXOpen.Diagramming.ShapeCollection@endlink
    @property
    def Shapes() -> ShapeCollection:
        """
         Returns the @link NXOpen::Diagramming::ShapeCollection  NXOpen::Diagramming::ShapeCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::PortCollection  NXOpen::Diagramming::PortCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link PortCollection NXOpen.Diagramming.PortCollection@endlink
    @property
    def Ports() -> PortCollection:
        """
         Returns the @link NXOpen::Diagramming::PortCollection  NXOpen::Diagramming::PortCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::AnnotationCollection  NXOpen::Diagramming::AnnotationCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link AnnotationCollection NXOpen.Diagramming.AnnotationCollection@endlink
    @property
    def Annotations() -> AnnotationCollection:
        """
         Returns the @link NXOpen::Diagramming::AnnotationCollection  NXOpen::Diagramming::AnnotationCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::FillCollection  NXOpen::Diagramming::FillCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @link FillCollection NXOpen.Diagramming.FillCollection@endlink
    @property
    def Fills() -> FillCollection:
        """
         Returns the @link NXOpen::Diagramming::FillCollection  NXOpen::Diagramming::FillCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::LeaderLineCollection  NXOpen::Diagramming::LeaderLineCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link LeaderLineCollection NXOpen.Diagramming.LeaderLineCollection@endlink
    @property
    def LeaderLines() -> LeaderLineCollection:
        """
         Returns the @link NXOpen::Diagramming::LeaderLineCollection  NXOpen::Diagramming::LeaderLineCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::SheetBordersAndZonesCollection  NXOpen::Diagramming::SheetBordersAndZonesCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link SheetBordersAndZonesCollection NXOpen.Diagramming.SheetBordersAndZonesCollection@endlink
    @property
    def SheetBordersAndZones() -> SheetBordersAndZonesCollection:
        """
         Returns the @link NXOpen::Diagramming::SheetBordersAndZonesCollection  NXOpen::Diagramming::SheetBordersAndZonesCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::Tables::TableCollection  NXOpen::Diagramming::Tables::TableCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link NXOpen.Diagramming.Tables.TableCollection NXOpen.Diagramming.Tables.TableCollection@endlink
    @property
    def Tables() -> NXOpen.Diagramming.Tables.TableCollection:
        """
         Returns the @link NXOpen::Diagramming::Tables::TableCollection  NXOpen::Diagramming::Tables::TableCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::TitleBlockCollection  NXOpen::Diagramming::TitleBlockCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @link TitleBlockCollection NXOpen.Diagramming.TitleBlockCollection@endlink
    @property
    def TitleBlocks() -> TitleBlockCollection:
        """
         Returns the @link NXOpen::Diagramming::TitleBlockCollection  NXOpen::Diagramming::TitleBlockCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::Geometry::LineCollection  NXOpen::Diagramming::Geometry::LineCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link NXOpen.Diagramming.Geometry.LineCollection NXOpen.Diagramming.Geometry.LineCollection@endlink
    @property
    def Lines() -> NXOpen.Diagramming.Geometry.LineCollection:
        """
         Returns the @link NXOpen::Diagramming::Geometry::LineCollection  NXOpen::Diagramming::Geometry::LineCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::Geometry::PointCollection  NXOpen::Diagramming::Geometry::PointCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link NXOpen.Diagramming.Geometry.PointCollection NXOpen.Diagramming.Geometry.PointCollection@endlink
    @property
    def Points() -> NXOpen.Diagramming.Geometry.PointCollection:
        """
         Returns the @link NXOpen::Diagramming::Geometry::PointCollection  NXOpen::Diagramming::Geometry::PointCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::Geometry::RectangleCollection  NXOpen::Diagramming::Geometry::RectangleCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link NXOpen.Diagramming.Geometry.RectangleCollection NXOpen.Diagramming.Geometry.RectangleCollection@endlink
    @property
    def Rectangles() -> NXOpen.Diagramming.Geometry.RectangleCollection:
        """
         Returns the @link NXOpen::Diagramming::Geometry::RectangleCollection  NXOpen::Diagramming::Geometry::RectangleCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Diagramming::Geometry::ArcCollection  NXOpen::Diagramming::Geometry::ArcCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @link NXOpen.Diagramming.Geometry.ArcCollection NXOpen.Diagramming.Geometry.ArcCollection@endlink
    @property
    def Arcs() -> NXOpen.Diagramming.Geometry.ArcCollection:
        """
         Returns the @link NXOpen::Diagramming::Geometry::ArcCollection  NXOpen::Diagramming::Geometry::ArcCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Copy the sheet elements. 
    ##  @return outputObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The copies of sheet elements .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The sheet elements to be copied </param>
    def CopySheetElements(self, inputObjects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Copy the sheet elements. 
         @return outputObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The copies of sheet elements .
        """
        pass
    
    ##  Creates a @link NXOpen::Diagramming::BulkEditBuilder NXOpen::Diagramming::BulkEditBuilder@endlink  
    ##  @return builder (@link BulkEditBuilder NXOpen.Diagramming.BulkEditBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def CreateBulkEditBuilder(self) -> BulkEditBuilder:
        """
         Creates a @link NXOpen::Diagramming::BulkEditBuilder NXOpen::Diagramming::BulkEditBuilder@endlink  
         @return builder (@link BulkEditBuilder NXOpen.Diagramming.BulkEditBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Diagramming::CannedAnnotationBuilder NXOpen::Diagramming::CannedAnnotationBuilder@endlink . 
    ##  @return builder (@link CannedAnnotationBuilder NXOpen.Diagramming.CannedAnnotationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="annotation"> (@link Annotation NXOpen.Diagramming.Annotation@endlink)  @link NXOpen::Diagramming::Annotation NXOpen::Diagramming::Annotation@endlink  to be edited, if NULL then create a new one </param>
    def CreateCannedAnnotationBuilder(self, annotation: Annotation) -> CannedAnnotationBuilder:
        """
         Creates a @link NXOpen::Diagramming::CannedAnnotationBuilder NXOpen::Diagramming::CannedAnnotationBuilder@endlink . 
         @return builder (@link CannedAnnotationBuilder NXOpen.Diagramming.CannedAnnotationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Diagramming::SheetSizeBuilder NXOpen::Diagramming::SheetSizeBuilder@endlink  
    ##  @return builder (@link SheetSizeBuilder NXOpen.Diagramming.SheetSizeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def CreateSheetSizeBuilder(self, sheet: Sheet) -> SheetSizeBuilder:
        """
         Creates a @link NXOpen::Diagramming::SheetSizeBuilder NXOpen::Diagramming::SheetSizeBuilder@endlink  
         @return builder (@link SheetSizeBuilder NXOpen.Diagramming.SheetSizeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Diagramming::SheetTemplateBuilder NXOpen::Diagramming::SheetTemplateBuilder@endlink  
    ##  @return builder (@link SheetTemplateBuilder NXOpen.Diagramming.SheetTemplateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def CreateSheetTemplateBuilder(self, sheet: Sheet) -> SheetTemplateBuilder:
        """
         Creates a @link NXOpen::Diagramming::SheetTemplateBuilder NXOpen::Diagramming::SheetTemplateBuilder@endlink  
         @return builder (@link SheetTemplateBuilder NXOpen.Diagramming.SheetTemplateBuilder@endlink): .
        """
        pass
    
    ##  Opens a @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Moved to SheetManager  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def OpenSheet(self, sheet: Sheet) -> None:
        """
         Opens a @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink . 
        """
        pass
    
##  Represents the repeat start position. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Center</term><description> 
##  Center </description> </item><item><term> 
## Start</term><description> 
##  Start </description> </item><item><term> 
## End</term><description> 
##  End </description> </item></list>
class DiagrammingRepeatstartposition(Enum):
    """
    Members Include: <Center> <Start> <End>
    """
    Center: int
    Start: int
    End: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingRepeatstartposition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the sizing policy type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Length</term><description> 
##  Length policy </description> </item><item><term> 
## Auto</term><description> 
##  Auto policy </description> </item><item><term> 
## Percent</term><description> 
##  Percent policy </description> </item><item><term> 
## Inherit</term><description> 
##  Inherit policy </description> </item></list>
class DiagrammingSizingpolicy(Enum):
    """
    Members Include: <Length> <Auto> <Percent> <Inherit>
    """
    Length: int
    Auto: int
    Percent: int
    Inherit: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingSizingpolicy:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the stub side type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Auto</term><description> 
##  Auto side </description> </item><item><term> 
## Left</term><description> 
##  Left side </description> </item><item><term> 
## Right</term><description> 
##  Right side </description> </item></list>
class DiagrammingStubsides(Enum):
    """
    Members Include: <Auto> <Left> <Right>
    """
    Auto: int
    Left: int
    Right: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DiagrammingStubsides:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the direction type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## In</term><description> 
##  In direction </description> </item><item><term> 
## Out</term><description> 
##  Out direction </description> </item><item><term> 
## Both</term><description> 
##  Both direction </description> </item></list>
class Direction(Enum):
    """
    Members Include: <In> <Out> <Both>
    """
    In: int
    Out: int
    Both: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Direction:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen.Diagramming.Geometry
## 
##     Represents a FillBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::FillCollection::CreateFillBuilder  NXOpen::Diagramming::FillCollection::CreateFillBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class FillBuilder(SheetElementBuilder): 
    """
    Represents a FillBuilder.
    """


    ## Getter for property: (@link NXOpen.Diagramming.Geometry.SelectBaseGeometryList NXOpen.Diagramming.Geometry.SelectBaseGeometryList@endlink) Geometries
    ##  Returns the boundary geometries  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Diagramming.Geometry.SelectBaseGeometryList
    @property
    def Geometries(self) -> NXOpen.Diagramming.Geometry.SelectBaseGeometryList:
        """
        Getter for property: (@link NXOpen.Diagramming.Geometry.SelectBaseGeometryList NXOpen.Diagramming.Geometry.SelectBaseGeometryList@endlink) Geometries
         Returns the boundary geometries  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Fill.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class FillCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Fill. """


    ##  Creates a @link NXOpen::Diagramming::FillBuilder NXOpen::Diagramming::FillBuilder@endlink . 
    ##  @return builder (@link FillBuilder NXOpen.Diagramming.FillBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fill"> (@link Fill NXOpen.Diagramming.Fill@endlink)  @link NXOpen::Diagramming::Fill NXOpen::Diagramming::Fill@endlink  to be edited, if NULL then create a new one </param>
    def CreateFillBuilder(self, fill: Fill) -> FillBuilder:
        """
         Creates a @link NXOpen::Diagramming::FillBuilder NXOpen::Diagramming::FillBuilder@endlink . 
         @return builder (@link FillBuilder NXOpen.Diagramming.FillBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Fill NXOpen::Diagramming::Fill@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return fill (@link Fill NXOpen.Diagramming.Fill@endlink):  @link NXOpen::Diagramming::Fill NXOpen::Diagramming::Fill@endlink  with this name. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Fill:
        """
         Finds the @link NXOpen::Diagramming::Fill NXOpen::Diagramming::Fill@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return fill (@link Fill NXOpen.Diagramming.Fill@endlink):  @link NXOpen::Diagramming::Fill NXOpen::Diagramming::Fill@endlink  with this name. .
        """
        pass
    
##  Represents the Fill class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::FillBuilder  NXOpen::Diagramming::FillBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Fill(SheetElement): 
    """ Represents the Fill class. """
    pass


##  the font 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Blockfont</term><description> 
## </description> </item></list>
class FontEnum(Enum):
    """
    Members Include: <Blockfont>
    """
    Blockfont: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FontEnum:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
## 
##     Represents a FormattedStringBuilder.
##      <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class FormattedStringBuilder(BaseSubObjectBuilder): 
    """
    Represents a FormattedStringBuilder.
    """


    ## Getter for property: (str) Format
    ##  Returns the format.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def Format(self) -> str:
        """
        Getter for property: (str) Format
         Returns the format.  
             
         
        """
        pass
    
    ## Getter for property: (str) String
    ##  Returns the string.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def String(self) -> str:
        """
        Getter for property: (str) String
         Returns the string.  
             
         
        """
        pass
    
    ##  Appends the format and related referenced attributes to this builder.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The owners of the referenced attributes </param>
    ## <param name="attrTitles"> (List[str])  The titles of the referenced attributes </param>
    ## <param name="appendFormat"> (str) </param>
    def AppendFormat(self, objTags: List[NXOpen.NXObject], attrTitles: List[str], appendFormat: str) -> None:
        """
         Appends the format and related referenced attributes to this builder.
                
        """
        pass
    
    ##  Clears the format and related referenced attributes of this builder.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def ClearFormat(self) -> None:
        """
         Clears the format and related referenced attributes of this builder.
                
        """
        pass
    
    ##  Gets the referenced attributes.
    ##         
    ##  @return A tuple consisting of (attrTitles, objTags). 
    ##  - attrTitles is: List[str]. The titles of the referenced attributes .
    ##  - objTags is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. The owners of the referenced attributes .

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetReferencedAttributes(self) -> Tuple[List[str], List[NXOpen.NXObject]]:
        """
         Gets the referenced attributes.
                
         @return A tuple consisting of (attrTitles, objTags). 
         - attrTitles is: List[str]. The titles of the referenced attributes .
         - objTags is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. The owners of the referenced attributes .

        """
        pass
    
    ##  Sets the format and related referenced attributes to this builder.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="builder"> (@link FormattedStringBuilder NXOpen.Diagramming.FormattedStringBuilder@endlink) </param>
    ## <param name="objTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The owners of the referenced attributes </param>
    ## <param name="attrTitles"> (List[str])  The titles of the referenced attributes </param>
    ## <param name="format"> (str) </param>
    @overload
    def SetFormatValue(self, objTags: List[NXOpen.NXObject], attrTitles: List[str], format: str) -> None:
        """
         Sets the format and related referenced attributes to this builder.
                
        """
        pass
    
    ##  Sets the format and related referenced attributes to this builder in managed mode.
    ##         
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## <param name="builder"> (@link FormattedStringBuilder NXOpen.Diagramming.FormattedStringBuilder@endlink) </param>
    ## <param name="objTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The owners of the referenced attributes </param>
    ## <param name="parentTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The owner parents of the referenced attributes </param>
    ## <param name="attrTitles"> (List[str])  The titles of the referenced attributes </param>
    ## <param name="format"> (str) </param>
    @overload
    def SetFormatValue(self, objTags: List[NXOpen.NXObject], parentTags: List[NXOpen.NXObject], attrTitles: List[str], format: str) -> None:
        """
         Sets the format and related referenced attributes to this builder in managed mode.
                
        """
        pass
    
## 
##     Represents a GroupBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::GroupCollection::CreateGroupBuilder  NXOpen::Diagramming::GroupCollection::CreateGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class GroupBuilder(SheetElementBuilder): 
    """
    Represents a GroupBuilder.
    """


    ##  Add a member. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheetElement"> (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) </param>
    def AddMember(self, sheetElement: SheetElement) -> None:
        """
         Add a member. 
        """
        pass
    
    ##  Get the member by given member identifier SID. 
    ##  @return member (@link SheetElement NXOpen.Diagramming.SheetElement@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="memberSid"> (str) </param>
    def GetMember(self, memberSid: str) -> SheetElement:
        """
         Get the member by given member identifier SID. 
         @return member (@link SheetElement NXOpen.Diagramming.SheetElement@endlink): .
        """
        pass
    
    ##  Get all members. 
    ##  @return allMembers (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetMembers(self) -> List[SheetElement]:
        """
         Get all members. 
         @return allMembers (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink): .
        """
        pass
    
    ##  Remove all members. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def RemoveAllMembers(self) -> None:
        """
         Remove all members. 
        """
        pass
    
    ##  Remove a member. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="member"> (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) </param>
    def RemoveMember(self, member: SheetElement) -> None:
        """
         Remove a member. 
        """
        pass
    
import NXOpen
##  Represents a collection of group.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class GroupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of group. """


    ##  Creates a @link NXOpen::Diagramming::GroupBuilder NXOpen::Diagramming::GroupBuilder@endlink . 
    ##  @return builder (@link GroupBuilder NXOpen.Diagramming.GroupBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="group"> (@link Group NXOpen.Diagramming.Group@endlink)  @link NXOpen::Diagramming::Group NXOpen::Diagramming::Group@endlink  to be edited, if NULL then create a new one </param>
    def CreateGroupBuilder(self, group: Group) -> GroupBuilder:
        """
         Creates a @link NXOpen::Diagramming::GroupBuilder NXOpen::Diagramming::GroupBuilder@endlink . 
         @return builder (@link GroupBuilder NXOpen.Diagramming.GroupBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Group NXOpen::Diagramming::Group@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return group (@link Group NXOpen.Diagramming.Group@endlink):  @link NXOpen::Diagramming::Group NXOpen::Diagramming::Group@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Group:
        """
         Finds the @link NXOpen::Diagramming::Group NXOpen::Diagramming::Group@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return group (@link Group NXOpen.Diagramming.Group@endlink):  @link NXOpen::Diagramming::Group NXOpen::Diagramming::Group@endlink  with this name. .
        """
        pass
    
import NXOpen
##  A manager to deal with group objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::SheetManager  NXOpen::Diagramming::SheetManager @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class GroupManager(NXOpen.Object): 
    """ A manager to deal with group objects. """


    ##  Creates a Group and adds the objects 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    ## <param name="elements"> (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink)  The elements to be grouped </param>
    def Group(sheet: Sheet, elements: List[SheetElement]) -> None:
        """
         Creates a Group and adds the objects 
        """
        pass
    
    ##  Removes the objects from the group. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## <param name="group"> (@link Group NXOpen.Diagramming.Group@endlink) </param>
    ## <param name="elements"> (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink)  The elements to be removed from group </param>
    def Ungroup(group: Group, elements: List[SheetElement]) -> None:
        """
         Removes the objects from the group. 
        """
        pass
    
##  Represents the Group class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::GroupBuilder  NXOpen::Diagramming::GroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Group(SheetElement): 
    """ Represents the Group class. """
    pass


##  the horizontal centering mark type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## LeftArrow</term><description> 
##  Left Arrow </description> </item><item><term> 
## RightArrow</term><description> 
##   Right Arrow </description> </item><item><term> 
## LeftandRightArrow</term><description> 
##  Left and Right Arrow </description> </item><item><term> 
## LeftandRightLine</term><description> 
## </description> </item></list>
class HorizontalCenteringMarkType(Enum):
    """
    Members Include: <NotSet> <LeftArrow> <RightArrow> <LeftandRightArrow> <LeftandRightLine>
    """
    NotSet: int
    LeftArrow: int
    RightArrow: int
    LeftandRightArrow: int
    LeftandRightLine: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> HorizontalCenteringMarkType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class LeaderLineBuilderList(NXOpen.TaggedObject): 
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
    ## <param name="objects"> (@link LeaderLineBuilder List[NXOpen.Diagramming.LeaderLineBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[LeaderLineBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: LeaderLineBuilder) -> None:
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
    ## <param name="obj"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: LeaderLineBuilder) -> None:
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
    ## <param name="obj"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: LeaderLineBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="obj"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: LeaderLineBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> LeaderLineBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link LeaderLineBuilder List[NXOpen.Diagramming.LeaderLineBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[LeaderLineBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link LeaderLineBuilder List[NXOpen.Diagramming.LeaderLineBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: LeaderLineBuilder) -> None:
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
    ## <param name="objects"> (@link LeaderLineBuilder List[NXOpen.Diagramming.LeaderLineBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[LeaderLineBuilder]) -> None:
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link LeaderLineBuilderList NXOpen.Diagramming.LeaderLineBuilderList@endlink) </param>
    ## <param name="object1"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: LeaderLineBuilder, object2: LeaderLineBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
## 
##     Represents a LeaderLineBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::LeaderLineCollection::CreateLeaderLineBuilder  NXOpen::Diagramming::LeaderLineCollection::CreateLeaderLineBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LeaderLineBuilder(SheetElementBuilder): 
    """
    Represents a LeaderLineBuilder.
    """


    ##  Represents the option @link NXOpen::Diagramming::LeaderLineBuilder::VerticalAlignment NXOpen::Diagramming::LeaderLineBuilder::VerticalAlignment@endlink 
    ##            for a @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Top</term><description> 
    ##  Setting the vertical alignment top</description> </item><item><term> 
    ## Middle</term><description> 
    ##  Setting the vertical alignment middle</description> </item><item><term> 
    ## Bottom</term><description> 
    ##  Setting the vertical alignment bottom</description> </item></list>
    class VerticalAlignmentOption(Enum):
        """
        Members Include: <Top> <Middle> <Bottom>
        """
        Top: int
        Middle: int
        Bottom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LeaderLineBuilder.VerticalAlignmentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) ArrowType
    ##  Returns the arrow type of the end arrow   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagrammingArrowtype
    @property
    def ArrowType(self) -> DiagrammingArrowtype:
        """
        Getter for property: (@link DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) ArrowType
         Returns the arrow type of the end arrow   
            
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) ArrowType

    ##  Returns the arrow type of the end arrow   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ArrowType.setter
    def ArrowType(self, arrowTypeOption: DiagrammingArrowtype):
        """
        Setter for property: (@link DiagrammingArrowtype NXOpen.Diagramming.DiagrammingArrowtype@endlink) ArrowType
         Returns the arrow type of the end arrow   
            
         
        """
        pass
    
    ## Getter for property: (float) StubLength
    ##  Returns the stub length of this leader line.  
    ##    The negative value is not expected.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def StubLength(self) -> float:
        """
        Getter for property: (float) StubLength
         Returns the stub length of this leader line.  
           The negative value is not expected.  
         
        """
        pass
    
    ## Setter for property: (float) StubLength

    ##  Returns the stub length of this leader line.  
    ##    The negative value is not expected.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @StubLength.setter
    def StubLength(self, stubLength: float):
        """
        Setter for property: (float) StubLength
         Returns the stub length of this leader line.  
           The negative value is not expected.  
         
        """
        pass
    
    ## Getter for property: (@link DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) StubSides
    ##  Returns the stub sides of this leader line.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagrammingStubsides
    @property
    def StubSides(self) -> DiagrammingStubsides:
        """
        Getter for property: (@link DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) StubSides
         Returns the stub sides of this leader line.  
            
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) StubSides

    ##  Returns the stub sides of this leader line.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @StubSides.setter
    def StubSides(self, stubSides: DiagrammingStubsides):
        """
        Setter for property: (@link DiagrammingStubsides NXOpen.Diagramming.DiagrammingStubsides@endlink) StubSides
         Returns the stub sides of this leader line.  
            
         
        """
        pass
    
    ## Getter for property: (@link LeaderLineBuilder.VerticalAlignmentOption NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignmentOption@endlink) VerticalAlignment
    ##  Returns the vertical alignment option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LeaderLineBuilder.VerticalAlignmentOption
    @property
    def VerticalAlignment(self) -> LeaderLineBuilder.VerticalAlignmentOption:
        """
        Getter for property: (@link LeaderLineBuilder.VerticalAlignmentOption NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignmentOption@endlink) VerticalAlignment
         Returns the vertical alignment option.  
             
         
        """
        pass
    
    ## Setter for property: (@link LeaderLineBuilder.VerticalAlignmentOption NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignmentOption@endlink) VerticalAlignment

    ##  Returns the vertical alignment option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @VerticalAlignment.setter
    def VerticalAlignment(self, alignmentOption: LeaderLineBuilder.VerticalAlignmentOption):
        """
        Setter for property: (@link LeaderLineBuilder.VerticalAlignmentOption NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignmentOption@endlink) VerticalAlignment
         Returns the vertical alignment option.  
             
         
        """
        pass
    
    ##  Get bending points for polyline to render the leader line. 
    ##  @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetBendPoints(self) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the leader line. 
         @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
        """
        pass
    
    ##  Gets the terminator of the leader. 
    ##  @return A tuple consisting of (terminator, segmentId, percentX, inputX, percentY, inputY). 
    ##  - terminator is: @link SheetElement NXOpen.Diagramming.SheetElement@endlink.
    ##  - segmentId is: int.
    ##  - percentX is: float.
    ##  - inputX is: float.
    ##  - percentY is: float.
    ##  - inputY is: float.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetTerminator(self) -> Tuple[SheetElement, int, float, float, float, float]:
        """
         Gets the terminator of the leader. 
         @return A tuple consisting of (terminator, segmentId, percentX, inputX, percentY, inputY). 
         - terminator is: @link SheetElement NXOpen.Diagramming.SheetElement@endlink.
         - segmentId is: int.
         - percentX is: float.
         - inputX is: float.
         - percentY is: float.
         - inputY is: float.

        """
        pass
    
    ##  Set bending points for polyline to render the leader line. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="points"> (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink) </param>
    def SetBendPoints(self, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the leader line. 
        """
        pass
    
    ##  Sets the terminator of the leader. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="terminator"> (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) </param>
    ## <param name="segmentId"> (int) </param>
    ## <param name="percentX"> (float) </param>
    ## <param name="inputX"> (float) </param>
    ## <param name="percentY"> (float) </param>
    ## <param name="inputY"> (float) </param>
    def SetTerminator(self, terminator: SheetElement, segmentId: int, percentX: float, inputX: float, percentY: float, inputY: float) -> None:
        """
         Sets the terminator of the leader. 
        """
        pass
    
import NXOpen
##  Represents a collection of leader line.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LeaderLineCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of leader line. """


    ##  Creates a @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink . 
    ##  @return builder (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="leaderLine"> (@link LeaderLine NXOpen.Diagramming.LeaderLine@endlink)  @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  to be edited, if NULL then create a new one </param>
    def CreateLeaderLineBuilder(self, leaderLine: LeaderLine) -> LeaderLineBuilder:
        """
         Creates a @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink . 
         @return builder (@link LeaderLineBuilder NXOpen.Diagramming.LeaderLineBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return leaderLine (@link LeaderLine NXOpen.Diagramming.LeaderLine@endlink):  @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> LeaderLine:
        """
         Finds the @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return leaderLine (@link LeaderLine NXOpen.Diagramming.LeaderLine@endlink):  @link NXOpen::Diagramming::LeaderLine NXOpen::Diagramming::LeaderLine@endlink  with this name. .
        """
        pass
    
##  Represents the LeaderLine class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::LeaderLineBuilder  NXOpen::Diagramming::LeaderLineBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LeaderLine(Connection): 
    """ Represents the LeaderLine class. """
    pass


## 
##     Represents a LocationBuilder.
##      <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class LocationBuilder(BaseSubObjectBuilder): 
    """
    Represents a LocationBuilder.
    """


    ## Getter for property: (float) EvaluatedValueX
    ##  Returns the evaluated X coordinate value that is the result calculated by the input percentage and offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def EvaluatedValueX(self) -> float:
        """
        Getter for property: (float) EvaluatedValueX
         Returns the evaluated X coordinate value that is the result calculated by the input percentage and offset.  
             
         
        """
        pass
    
    ## Getter for property: (float) EvaluatedValueY
    ##  Returns the evaluated Y coordinate value that is the result calculated by input percentage and offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def EvaluatedValueY(self) -> float:
        """
        Getter for property: (float) EvaluatedValueY
         Returns the evaluated Y coordinate value that is the result calculated by input percentage and offset.  
             
         
        """
        pass
    
    ## Getter for property: (float) InputPercentX
    ##  Returns the user input percentage (0.  
    ##   0 to 1.0) of the width of the referenced object.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def InputPercentX(self) -> float:
        """
        Getter for property: (float) InputPercentX
         Returns the user input percentage (0.  
          0 to 1.0) of the width of the referenced object.   
         
        """
        pass
    
    ## Setter for property: (float) InputPercentX

    ##  Returns the user input percentage (0.  
    ##   0 to 1.0) of the width of the referenced object.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @InputPercentX.setter
    def InputPercentX(self, inputPercentX: float):
        """
        Setter for property: (float) InputPercentX
         Returns the user input percentage (0.  
          0 to 1.0) of the width of the referenced object.   
         
        """
        pass
    
    ## Getter for property: (float) InputPercentY
    ##  Returns the user input percentage (0.  
    ##   0 to 1.0) of the height of the referenced object.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def InputPercentY(self) -> float:
        """
        Getter for property: (float) InputPercentY
         Returns the user input percentage (0.  
          0 to 1.0) of the height of the referenced object.   
         
        """
        pass
    
    ## Setter for property: (float) InputPercentY

    ##  Returns the user input percentage (0.  
    ##   0 to 1.0) of the height of the referenced object.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @InputPercentY.setter
    def InputPercentY(self, inputPercentY: float):
        """
        Setter for property: (float) InputPercentY
         Returns the user input percentage (0.  
          0 to 1.0) of the height of the referenced object.   
         
        """
        pass
    
    ## Getter for property: (float) InputValueX
    ##  Returns the user input X coordinate.  
    ##   
    ##             If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def InputValueX(self) -> float:
        """
        Getter for property: (float) InputValueX
         Returns the user input X coordinate.  
          
                    If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value.   
         
        """
        pass
    
    ## Setter for property: (float) InputValueX

    ##  Returns the user input X coordinate.  
    ##   
    ##             If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @InputValueX.setter
    def InputValueX(self, inputValueX: float):
        """
        Setter for property: (float) InputValueX
         Returns the user input X coordinate.  
          
                    If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value.   
         
        """
        pass
    
    ## Getter for property: (float) InputValueY
    ##  Returns the user input Y coordinate.  
    ##   
    ##             If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def InputValueY(self) -> float:
        """
        Getter for property: (float) InputValueY
         Returns the user input Y coordinate.  
          
                    If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value.   
         
        """
        pass
    
    ## Setter for property: (float) InputValueY

    ##  Returns the user input Y coordinate.  
    ##   
    ##             If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @InputValueY.setter
    def InputValueY(self, inputValueY: float):
        """
        Setter for property: (float) InputValueY
         Returns the user input Y coordinate.  
          
                    If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value.   
         
        """
        pass
    
    ## Getter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Reference
    ##  Returns the sheet element whose coordinate system the coordinate is specified in.  
    ##    If this is NULL, the coordinate is in the Sheet's coordinate system.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SheetElement
    @property
    def Reference(self) -> SheetElement:
        """
        Getter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Reference
         Returns the sheet element whose coordinate system the coordinate is specified in.  
           If this is NULL, the coordinate is in the Sheet's coordinate system.   
         
        """
        pass
    
    ## Setter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Reference

    ##  Returns the sheet element whose coordinate system the coordinate is specified in.  
    ##    If this is NULL, the coordinate is in the Sheet's coordinate system.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Reference.setter
    def Reference(self, reference: SheetElement):
        """
        Setter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Reference
         Returns the sheet element whose coordinate system the coordinate is specified in.  
           If this is NULL, the coordinate is in the Sheet's coordinate system.   
         
        """
        pass
    
    ## Getter for property: (bool) UpToDate
    ##  Returns the up to date flag.  
    ##   
    ##             If true, @link NXOpen::Diagramming::LocationBuilder::EvaluatedValueX NXOpen::Diagramming::LocationBuilder::EvaluatedValueX@endlink  and @link NXOpen::Diagramming::LocationBuilder::EvaluatedValueY NXOpen::Diagramming::LocationBuilder::EvaluatedValueY@endlink 
    ##             of @link NXOpen::Diagramming::LocationBuilder NXOpen::Diagramming::LocationBuilder@endlink  may be used; Otherwise it must be evaluated.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def UpToDate(self) -> bool:
        """
        Getter for property: (bool) UpToDate
         Returns the up to date flag.  
          
                    If true, @link NXOpen::Diagramming::LocationBuilder::EvaluatedValueX NXOpen::Diagramming::LocationBuilder::EvaluatedValueX@endlink  and @link NXOpen::Diagramming::LocationBuilder::EvaluatedValueY NXOpen::Diagramming::LocationBuilder::EvaluatedValueY@endlink 
                    of @link NXOpen::Diagramming::LocationBuilder NXOpen::Diagramming::LocationBuilder@endlink  may be used; Otherwise it must be evaluated.  
         
        """
        pass
    
    ##  Set the x value of the location. 
    ##             The inputPercent means of the x coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
    ##             The inputValue means the offset value of the x coordinate from the calculated location by the inputPercent value. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputPercent"> (float) </param>
    ## <param name="inputValue"> (float) </param>
    def SetValueX(self, inputPercent: float, inputValue: float) -> None:
        """
         Set the x value of the location. 
                    The inputPercent means of the x coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
                    The inputValue means the offset value of the x coordinate from the calculated location by the inputPercent value. 
        """
        pass
    
    ##  Set the y value of the location. 
    ##             The inputPercent means of the y coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
    ##             The inputValue means the offset value of the y coordinate from the calculated location by the inputPercent value. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputPercent"> (float) </param>
    ## <param name="inputValue"> (float) </param>
    def SetValueY(self, inputPercent: float, inputValue: float) -> None:
        """
         Set the y value of the location. 
                    The inputPercent means of the y coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
                    The inputValue means the offset value of the y coordinate from the calculated location by the inputPercent value. 
        """
        pass
    
##  the zone method
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  To support legacy parts </description> </item><item><term> 
## Standard</term><description> 
##  Standard </description> </item><item><term> 
## Custom</term><description> 
## </description> </item></list>
class Method(Enum):
    """
    Members Include: <NotSet> <Standard> <Custom>
    """
    NotSet: int
    Standard: int
    Custom: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Method:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## 
##     Represents a NodeBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::NodeCollection::CreateNodeBuilder  NXOpen::Diagramming::NodeCollection::CreateNodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class NodeBuilder(ConnectableElementBuilder): 
    """
    Represents a NodeBuilder.
    """


    ## Getter for property: (bool) Expanded
    ##  Returns the node state of expanded or collapsed.  
    ##    If true the node is expanded.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Expanded(self) -> bool:
        """
        Getter for property: (bool) Expanded
         Returns the node state of expanded or collapsed.  
           If true the node is expanded.   
         
        """
        pass
    
    ## Setter for property: (bool) Expanded

    ##  Returns the node state of expanded or collapsed.  
    ##    If true the node is expanded.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Expanded.setter
    def Expanded(self, expanded: bool):
        """
        Setter for property: (bool) Expanded
         Returns the node state of expanded or collapsed.  
           If true the node is expanded.   
         
        """
        pass
    
    ## Getter for property: (bool) Fullfillment
    ##  Returns the flag that indicates if the node is a fulfillment object.  
    ##    If true the node represents a physical object such as a piece of equipment from a library.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Fullfillment(self) -> bool:
        """
        Getter for property: (bool) Fullfillment
         Returns the flag that indicates if the node is a fulfillment object.  
           If true the node represents a physical object such as a piece of equipment from a library.   
         
        """
        pass
    
    ## Getter for property: (bool) GroupingAllowed
    ##  Returns the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def GroupingAllowed(self) -> bool:
        """
        Getter for property: (bool) GroupingAllowed
         Returns the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
             
         
        """
        pass
    
    ## Setter for property: (bool) GroupingAllowed

    ##  Returns the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @GroupingAllowed.setter
    def GroupingAllowed(self, fulfillment: bool):
        """
        Setter for property: (bool) GroupingAllowed
         Returns the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
             
         
        """
        pass
    
    ## Getter for property: (@link Node NXOpen.Diagramming.Node@endlink) OffsheetReference
    ##  Returns the referenced offsheet node.  
    ##    It could be elsewhere on the same sheet or on a different sheet and it can be NULL.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Node
    @property
    def OffsheetReference(self) -> Node:
        """
        Getter for property: (@link Node NXOpen.Diagramming.Node@endlink) OffsheetReference
         Returns the referenced offsheet node.  
           It could be elsewhere on the same sheet or on a different sheet and it can be NULL.   
         
        """
        pass
    
    ## Setter for property: (@link Node NXOpen.Diagramming.Node@endlink) OffsheetReference

    ##  Returns the referenced offsheet node.  
    ##    It could be elsewhere on the same sheet or on a different sheet and it can be NULL.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @OffsheetReference.setter
    def OffsheetReference(self, offsheetReference: Node):
        """
        Setter for property: (@link Node NXOpen.Diagramming.Node@endlink) OffsheetReference
         Returns the referenced offsheet node.  
           It could be elsewhere on the same sheet or on a different sheet and it can be NULL.   
         
        """
        pass
    
    ##  Adds a node to this node group. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="member"> (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) </param>
    def AddGroupMember(self, member: SheetElement) -> None:
        """
         Adds a node to this node group. 
        """
        pass
    
    ##  Remove all members. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def RemoveAllGroupMembers(self) -> None:
        """
         Remove all members. 
        """
        pass
    
    ##  Removes a node from this node group. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="member"> (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) </param>
    def RemoveGroupMember(self, member: SheetElement) -> None:
        """
         Removes a node from this node group. 
        """
        pass
    
import NXOpen
##  Represents a collection of Node.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class NodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Node. """


    ##  Creates a @link NXOpen::Diagramming::NodeBuilder NXOpen::Diagramming::NodeBuilder@endlink . 
    ##  @return builder (@link NodeBuilder NXOpen.Diagramming.NodeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link Node NXOpen.Diagramming.Node@endlink)  @link NXOpen::Diagramming::Node NXOpen::Diagramming::Node@endlink  to be edited, if NULL then create a new one </param>
    def CreateNodeBuilder(self, node: Node) -> NodeBuilder:
        """
         Creates a @link NXOpen::Diagramming::NodeBuilder NXOpen::Diagramming::NodeBuilder@endlink . 
         @return builder (@link NodeBuilder NXOpen.Diagramming.NodeBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Node NXOpen::Diagramming::Node@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return node (@link Node NXOpen.Diagramming.Node@endlink):  @link NXOpen::Diagramming::Node NXOpen::Diagramming::Node@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Node:
        """
         Finds the @link NXOpen::Diagramming::Node NXOpen::Diagramming::Node@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return node (@link Node NXOpen.Diagramming.Node@endlink):  @link NXOpen::Diagramming::Node NXOpen::Diagramming::Node@endlink  with this name. .
        """
        pass
    
##  Represents the Node class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::NodeBuilder  NXOpen::Diagramming::NodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Node(ConnectableElement): 
    """ Represents the Node class. """


    ## Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
    ##  Returns the label of the sheet element.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return Annotation
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
         Returns the label of the sheet element.  
             
         
        """
        pass
    
    ##  Get the ports on the node.
    ##  @return ports (@link Port List[NXOpen.Diagramming.Port]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetPorts(self) -> List[Port]:
        """
         Get the ports on the node.
         @return ports (@link Port List[NXOpen.Diagramming.Port]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Diagramming.Tables
##  Represents a @link NXOpen::Diagramming::PopulateTitleBlockBuilder NXOpen::Diagramming::PopulateTitleBlockBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Diagramming::TitleBlockCollection::CreatePopulateTitleBlockBuilder  NXOpen::Diagramming::TitleBlockCollection::CreatePopulateTitleBlockBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PopulateTitleBlockBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Diagramming.PopulateTitleBlockBuilder</ja_class> builder """


    ##  Get the cell builder. 
    ##  @return cell (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="table"> (@link NXOpen.Diagramming.Tables.Table NXOpen.Diagramming.Tables.Table@endlink) </param>
    ## <param name="rowIndex"> (int) </param>
    ## <param name="columnIndex"> (int) </param>
    def GetCell(self, table: NXOpen.Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> TitleBlockCellBuilder:
        """
         Get the cell builder. 
         @return cell (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink): .
        """
        pass
    
    ##  Return the value of the cell for given label. If multiple title blocks are input, 
    ##         then the value of the cell from the first title block, which has the cell with given label, is returned. 
    ##  @return value (str):  Value of the label .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str)  Label whose value is queried </param>
    def GetCellValueForLabel(self, label: str) -> str:
        """
         Return the value of the cell for given label. If multiple title blocks are input, 
                then the value of the cell from the first title block, which has the cell with given label, is returned. 
         @return value (str):  Value of the label .
        """
        pass
    
    ##  Sets the value of the cell for given label. If multiple title blocks are selected, 
    ##         then values of cells with the given label in all the title blocks are set. 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str)  Label whose value is to be set </param>
    ## <param name="value"> (str)  Value of the label </param>
    def SetCellValueForLabel(self, label: str, value: str) -> None:
        """
         Sets the value of the cell for given label. If multiple title blocks are selected, 
                then values of cells with the given label in all the title blocks are set. 
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PortBuilderList(NXOpen.TaggedObject): 
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
    ## <param name="objects"> (@link PortBuilder List[NXOpen.Diagramming.PortBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[PortBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: PortBuilder) -> None:
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
    ## <param name="obj"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: PortBuilder) -> None:
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
    ## <param name="obj"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: PortBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="obj"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: PortBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> PortBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link PortBuilder List[NXOpen.Diagramming.PortBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[PortBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link PortBuilder List[NXOpen.Diagramming.PortBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: PortBuilder) -> None:
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
    ## <param name="objects"> (@link PortBuilder List[NXOpen.Diagramming.PortBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[PortBuilder]) -> None:
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link PortBuilderList NXOpen.Diagramming.PortBuilderList@endlink) </param>
    ## <param name="object1"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: PortBuilder, object2: PortBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
## 
##     Represents a PortBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::PortCollection::CreatePortBuilder  NXOpen::Diagramming::PortCollection::CreatePortBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PortBuilder(SheetElementBuilder): 
    """
    Represents a PortBuilder.
    """


    ## Getter for property: (@link Direction NXOpen.Diagramming.Direction@endlink) Direction
    ##  Returns the direction of the port.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Direction
    @property
    def Direction(self) -> Direction:
        """
        Getter for property: (@link Direction NXOpen.Diagramming.Direction@endlink) Direction
         Returns the direction of the port.  
             
         
        """
        pass
    
    ## Setter for property: (@link Direction NXOpen.Diagramming.Direction@endlink) Direction

    ##  Returns the direction of the port.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: Direction):
        """
        Setter for property: (@link Direction NXOpen.Diagramming.Direction@endlink) Direction
         Returns the direction of the port.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberAllowedConnections
    ##  Returns the maximum number of allowed connections the port may reference.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def NumberAllowedConnections(self) -> int:
        """
        Getter for property: (int) NumberAllowedConnections
         Returns the maximum number of allowed connections the port may reference.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberAllowedConnections

    ##  Returns the maximum number of allowed connections the port may reference.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberAllowedConnections.setter
    def NumberAllowedConnections(self, numberAllowedConnections: int):
        """
        Setter for property: (int) NumberAllowedConnections
         Returns the maximum number of allowed connections the port may reference.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Pinned
    ##  Returns the flag that indicates the port is pinned.  
    ##    If true the port is pinned and cannot be moved.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Pinned(self) -> bool:
        """
        Getter for property: (bool) Pinned
         Returns the flag that indicates the port is pinned.  
           If true the port is pinned and cannot be moved.   
         
        """
        pass
    
    ## Setter for property: (bool) Pinned

    ##  Returns the flag that indicates the port is pinned.  
    ##    If true the port is pinned and cannot be moved.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Pinned.setter
    def Pinned(self, isPinned: bool):
        """
        Setter for property: (bool) Pinned
         Returns the flag that indicates the port is pinned.  
           If true the port is pinned and cannot be moved.   
         
        """
        pass
    
    ## Getter for property: (@link Port NXOpen.Diagramming.Port@endlink) Proxy
    ##  Returns the proxy port for the port inside the super node.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Port
    @property
    def Proxy(self) -> Port:
        """
        Getter for property: (@link Port NXOpen.Diagramming.Port@endlink) Proxy
         Returns the proxy port for the port inside the super node.  
             
         
        """
        pass
    
    ## Setter for property: (@link Port NXOpen.Diagramming.Port@endlink) Proxy

    ##  Returns the proxy port for the port inside the super node.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Proxy.setter
    def Proxy(self, proxy: Port):
        """
        Setter for property: (@link Port NXOpen.Diagramming.Port@endlink) Proxy
         Returns the proxy port for the port inside the super node.  
             
         
        """
        pass
    
    ##  Get whether another connection can be added or not. 
    ##  @return canAnotherConnectionBeAdded (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def CanAnotherConnectionBeAdded(self) -> bool:
        """
         Get whether another connection can be added or not. 
         @return canAnotherConnectionBeAdded (bool): .
        """
        pass
    
    ##  Get allowed parent sides. 
    ##  @return A tuple consisting of (isAllowedLeftSide, isAllowedRightSide, isAllowedUpSide, isAllowedDownSide). 
    ##  - isAllowedLeftSide is: bool.
    ##  - isAllowedRightSide is: bool.
    ##  - isAllowedUpSide is: bool.
    ##  - isAllowedDownSide is: bool.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetAllowedParentSides(self) -> Tuple[bool, bool, bool, bool]:
        """
         Get allowed parent sides. 
         @return A tuple consisting of (isAllowedLeftSide, isAllowedRightSide, isAllowedUpSide, isAllowedDownSide). 
         - isAllowedLeftSide is: bool.
         - isAllowedRightSide is: bool.
         - isAllowedUpSide is: bool.
         - isAllowedDownSide is: bool.

        """
        pass
    
    ##  Get associated connections. 
    ##  @return connections (@link Connection List[NXOpen.Diagramming.Connection]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetConnections(self) -> List[Connection]:
        """
         Get associated connections. 
         @return connections (@link Connection List[NXOpen.Diagramming.Connection]@endlink): .
        """
        pass
    
    ##  Get the owner connectable element. 
    ##  @return owner (@link ConnectableElement NXOpen.Diagramming.ConnectableElement@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetOwningConnectableElement(self) -> ConnectableElement:
        """
         Get the owner connectable element. 
         @return owner (@link ConnectableElement NXOpen.Diagramming.ConnectableElement@endlink): .
        """
        pass
    
    ##  Get if the number of connections to reference is infinite. If true it is infinite. 
    ##  @return isNumberOfConnectionInfinite (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def IsNumberOfConnectionInfinite(self) -> bool:
        """
         Get if the number of connections to reference is infinite. If true it is infinite. 
         @return isNumberOfConnectionInfinite (bool): .
        """
        pass
    
import NXOpen
##  Represents a collection of Port.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Port. """


    ##  Creates a @link NXOpen::Diagramming::PortBuilder NXOpen::Diagramming::PortBuilder@endlink . 
    ##  @return builder (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="port"> (@link Port NXOpen.Diagramming.Port@endlink)  @link NXOpen::Diagramming::Port NXOpen::Diagramming::Port@endlink  to be edited, if NULL then create a new one </param>
    def CreatePortBuilder(self, port: Port) -> PortBuilder:
        """
         Creates a @link NXOpen::Diagramming::PortBuilder NXOpen::Diagramming::PortBuilder@endlink . 
         @return builder (@link PortBuilder NXOpen.Diagramming.PortBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Port NXOpen::Diagramming::Port@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return port (@link Port NXOpen.Diagramming.Port@endlink):  @link NXOpen::Diagramming::Port NXOpen::Diagramming::Port@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Port:
        """
         Finds the @link NXOpen::Diagramming::Port NXOpen::Diagramming::Port@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return port (@link Port NXOpen.Diagramming.Port@endlink):  @link NXOpen::Diagramming::Port NXOpen::Diagramming::Port@endlink  with this name. .
        """
        pass
    
##  Represents the Port class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::PortBuilder  NXOpen::Diagramming::PortBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Port(SheetElement): 
    """ Represents the Port class. """


    ## Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
    ##  Returns the label of the port.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return Annotation
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
         Returns the label of the port.  
             
         
        """
        pass
    
import NXOpen
##  This builder is used to create/edit Reference Geometry  <br> To create a new instance of this class, use @link NXOpen::Diagramming::SmartDiagrammingManager::CreateReferenceGeometryBuilder  NXOpen::Diagramming::SmartDiagrammingManager::CreateReferenceGeometryBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ReferenceGeometryBuilder(AnnotationBuilder): 
    """ This builder is used to create/edit Reference Geometry """


    ## Getter for property: (bool) DisplayBorder
    ##  Returns the setting that determines whether the border should be displayed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def DisplayBorder(self) -> bool:
        """
        Getter for property: (bool) DisplayBorder
         Returns the setting that determines whether the border should be displayed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DisplayBorder

    ##  Returns the setting that determines whether the border should be displayed or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @DisplayBorder.setter
    def DisplayBorder(self, displayBorder: bool):
        """
        Setter for property: (bool) DisplayBorder
         Returns the setting that determines whether the border should be displayed or not.  
             
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##  Returns the scale   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale   
            
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##  Returns the scale   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale   
            
         
        """
        pass
    
    ## Getter for property: (int) Transparency
    ##  Returns the transparency (between 0 and 100)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def Transparency(self) -> int:
        """
        Getter for property: (int) Transparency
         Returns the transparency (between 0 and 100)   
            
         
        """
        pass
    
    ## Setter for property: (int) Transparency

    ##  Returns the transparency (between 0 and 100)   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Transparency.setter
    def Transparency(self, transparency: int):
        """
        Setter for property: (int) Transparency
         Returns the transparency (between 0 and 100)   
            
         
        """
        pass
    
    ## Getter for property: (str) View
    ##  Returns the view to import from   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def View(self) -> str:
        """
        Getter for property: (str) View
         Returns the view to import from   
            
         
        """
        pass
    
    ## Setter for property: (str) View

    ##  Returns the view to import from   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @View.setter
    def View(self, viewIdentifier: str):
        """
        Setter for property: (str) View
         Returns the view to import from   
            
         
        """
        pass
    
    ##  Gets the color 
    ##  @return color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetColor(self) -> List[float]:
        """
         Gets the color 
         @return color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  When set will cause a refresh of the geometry from the drawing view during commit. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="refresh"> (bool)  true - a refresh will be performed, false - a refresh will not be performed </param>
    def RefreshFromView(self, refresh: bool) -> None:
        """
         When set will cause a refresh of the geometry from the drawing view during commit. 
        """
        pass
    
    ##  Sets the color 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="color"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetColor(self, color: List[float]) -> None:
        """
         Sets the color 
        """
        pass
    
##  Represents the Reference Geometry class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::ReferenceGeometryBuilder  NXOpen::Diagramming::ReferenceGeometryBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ReferenceGeometry(Annotation): 
    """ Represents the Reference Geometry class. """
    pass


import NXOpen
## 
##     Represents a RenderingPropertiesBuilder.
##      <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class RenderingPropertiesBuilder(BaseSubObjectBuilder): 
    """
    Represents a RenderingPropertiesBuilder.
    """


    ##  the fill patterns 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No Fill    </description> </item><item><term> 
    ## SolidFill</term><description> 
    ##  Solid Fill </description> </item></list>
    class FillPatterns(Enum):
        """
        Members Include: <NotSet> <SolidFill>
        """
        NotSet: int
        SolidFill: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RenderingPropertiesBuilder.FillPatterns:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor
    ##  Returns the fill color.  
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
         Returns the fill color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor

    ##  Returns the fill color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FillColor.setter
    def FillColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillColor
         Returns the fill color.  
             
         
        """
        pass
    
    ## Getter for property: (float) FillOpacity
    ##  Returns the fill opacity.  
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
         Returns the fill opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    
    ## Setter for property: (float) FillOpacity

    ##  Returns the fill opacity.  
    ##    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @FillOpacity.setter
    def FillOpacity(self, opacity: float):
        """
        Setter for property: (float) FillOpacity
         Returns the fill opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    
    ## Getter for property: (@link RenderingPropertiesBuilder.FillPatterns NXOpen.Diagramming.RenderingPropertiesBuilder.FillPatterns@endlink) FillPattern
    ##  Returns the fill type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RenderingPropertiesBuilder.FillPatterns
    @property
    def FillPattern(self) -> RenderingPropertiesBuilder.FillPatterns:
        """
        Getter for property: (@link RenderingPropertiesBuilder.FillPatterns NXOpen.Diagramming.RenderingPropertiesBuilder.FillPatterns@endlink) FillPattern
         Returns the fill type   
            
         
        """
        pass
    
    ## Setter for property: (@link RenderingPropertiesBuilder.FillPatterns NXOpen.Diagramming.RenderingPropertiesBuilder.FillPatterns@endlink) FillPattern

    ##  Returns the fill type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @FillPattern.setter
    def FillPattern(self, pattern: RenderingPropertiesBuilder.FillPatterns):
        """
        Setter for property: (@link RenderingPropertiesBuilder.FillPatterns NXOpen.Diagramming.RenderingPropertiesBuilder.FillPatterns@endlink) FillPattern
         Returns the fill type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
    ##  Returns the line font.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
         Returns the line font.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont

    ##  Returns the line font.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
         Returns the line font.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
    ##  Returns the line width.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth

    ##  Returns the line width.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) StrokeColor
    ##  Returns the stroke color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def StrokeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) StrokeColor
         Returns the stroke color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) StrokeColor

    ##  Returns the stroke color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @StrokeColor.setter
    def StrokeColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) StrokeColor
         Returns the stroke color.  
             
         
        """
        pass
    
    ## Getter for property: (float) StrokeOpacity
    ##  Returns the stroke opacity.  
    ##    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def StrokeOpacity(self) -> float:
        """
        Getter for property: (float) StrokeOpacity
         Returns the stroke opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    
    ## Setter for property: (float) StrokeOpacity

    ##  Returns the stroke opacity.  
    ##    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @StrokeOpacity.setter
    def StrokeOpacity(self, opacity: float):
        """
        Setter for property: (float) StrokeOpacity
         Returns the stroke opacity.  
           The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque.   
         
        """
        pass
    
## 
##     Represents a ShapeBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::ShapeCollection::CreateShapeBuilder  NXOpen::Diagramming::ShapeCollection::CreateShapeBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ShapeBuilder(SheetElementBuilder): 
    """
    Represents a ShapeBuilder.
    """
    pass


import NXOpen
##  Represents a collection of Shape.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ShapeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Shape. """


    ##  Creates a @link NXOpen::Diagramming::ShapeBuilder NXOpen::Diagramming::ShapeBuilder@endlink . 
    ##  @return builder (@link ShapeBuilder NXOpen.Diagramming.ShapeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="shape"> (@link Shape NXOpen.Diagramming.Shape@endlink)  @link NXOpen::Diagramming::Shape NXOpen::Diagramming::Shape@endlink  to be edited, if NULL then create a new one </param>
    def CreateShapeBuilder(self, shape: Shape) -> ShapeBuilder:
        """
         Creates a @link NXOpen::Diagramming::ShapeBuilder NXOpen::Diagramming::ShapeBuilder@endlink . 
         @return builder (@link ShapeBuilder NXOpen.Diagramming.ShapeBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Shape NXOpen::Diagramming::Shape@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return shape (@link Shape NXOpen.Diagramming.Shape@endlink):  @link NXOpen::Diagramming::Shape NXOpen::Diagramming::Shape@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Shape:
        """
         Finds the @link NXOpen::Diagramming::Shape NXOpen::Diagramming::Shape@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return shape (@link Shape NXOpen.Diagramming.Shape@endlink):  @link NXOpen::Diagramming::Shape NXOpen::Diagramming::Shape@endlink  with this name. .
        """
        pass
    
##  Represents the Shape class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::ShapeBuilder  NXOpen::Diagramming::ShapeBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Shape(ConnectableElement): 
    """ Represents the Shape class. """
    pass


import NXOpen
##  The SheetBordersAndZones builder  <br> To create a new instance of this class, use @link NXOpen::Diagramming::SheetBordersAndZonesCollection::CreateSheetBordersAndZonesBuilder  NXOpen::Diagramming::SheetBordersAndZonesCollection::CreateSheetBordersAndZonesBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetBordersAndZonesBuilder(NXOpen.Builder): 
    """ The SheetBordersAndZones builder """


    ##  Represents the arrow direction type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OutofSheet</term><description> 
    ##  Out of Sheet </description> </item><item><term> 
    ## IntoSheet</term><description> 
    ## </description> </item></list>
    class ArrowDirectionType(Enum):
        """
        Members Include: <OutofSheet> <IntoSheet>
        """
        OutofSheet: int
        IntoSheet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ArrowDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the arrow style type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Filled</term><description> 
    ##  Filled </description> </item><item><term> 
    ## Closed</term><description> 
    ##  Closed </description> </item><item><term> 
    ## ClosedSolid</term><description> 
    ##  Close Solid </description> </item><item><term> 
    ## Open</term><description> 
    ## </description> </item></list>
    class ArrowStyleType(Enum):
        """
        Members Include: <Filled> <Closed> <ClosedSolid> <Open>
        """
        Filled: int
        Closed: int
        ClosedSolid: int
        Open: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ArrowStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the horizontal centering mark type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None </description> </item><item><term> 
    ## LeftArrow</term><description> 
    ##  Left Arrow </description> </item><item><term> 
    ## RightArrow</term><description> 
    ##   Right Arrow </description> </item><item><term> 
    ## LeftandRightArrow</term><description> 
    ##  Left and Right Arrow </description> </item><item><term> 
    ## LeftandRightLine</term><description> 
    ## </description> </item></list>
    class HorizontalCenteringMarkType(Enum):
        """
        Members Include: <NotSet> <LeftArrow> <RightArrow> <LeftandRightArrow> <LeftandRightLine>
        """
        NotSet: int
        LeftArrow: int
        RightArrow: int
        LeftandRightArrow: int
        LeftandRightLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.HorizontalCenteringMarkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the trimming mark style type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Triangle</term><description> 
    ##  Triangle </description> </item><item><term> 
    ## Corner</term><description> 
    ## </description> </item></list>
    class TrimmingMarkStyleType(Enum):
        """
        Members Include: <Triangle> <Corner>
        """
        Triangle: int
        Corner: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.TrimmingMarkStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the vertical centering mark type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None </description> </item><item><term> 
    ## BottomArrow</term><description> 
    ##  Bottom Arrow </description> </item><item><term> 
    ## TopArrow</term><description> 
    ##  Top Arrow </description> </item><item><term> 
    ## BottomandTopArrow</term><description> 
    ##  Bottom and Top Arrow </description> </item><item><term> 
    ## BottomandTopLine</term><description> 
    ## </description> </item></list>
    class VerticalCenteringMarkType(Enum):
        """
        Members Include: <NotSet> <BottomArrow> <TopArrow> <BottomandTopArrow> <BottomandTopLine>
        """
        NotSet: int
        BottomArrow: int
        TopArrow: int
        BottomandTopArrow: int
        BottomandTopLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.VerticalCenteringMarkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the zone method. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  None </description> </item><item><term> 
    ## Standard</term><description> 
    ##  Standard </description> </item><item><term> 
    ## Custom</term><description> 
    ## </description> </item></list>
    class ZoneMethod(Enum):
        """
        Members Include: <NotSet> <Standard> <Custom>
        """
        NotSet: int
        Standard: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ZoneMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the zone origin. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BottomRight</term><description> 
    ##  Bottom Right </description> </item><item><term> 
    ## TopLeft</term><description> 
    ##  Top Left </description> </item><item><term> 
    ## TopRight</term><description> 
    ##  Top Right </description> </item><item><term> 
    ## BottomLeft</term><description> 
    ## </description> </item></list>
    class ZoneOrigin(Enum):
        """
        Members Include: <BottomRight> <TopLeft> <TopRight> <BottomLeft>
        """
        BottomRight: int
        TopLeft: int
        TopRight: int
        BottomLeft: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetBordersAndZonesBuilder.ZoneOrigin:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) BottomMargin
    ##  Returns the value of the margin in bottom border.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.BottomTrimmedMargin</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def BottomMargin(self) -> float:
        """
        Getter for property: (float) BottomMargin
         Returns the value of the margin in bottom border.  
            
         
        """
        pass
    
    ## Setter for property: (float) BottomMargin

    ##  Returns the value of the margin in bottom border.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.BottomTrimmedMargin</ja_property_set > instead.  <br> 

    @BottomMargin.setter
    def BottomMargin(self, bottomMargin: float):
        """
        Setter for property: (float) BottomMargin
         Returns the value of the margin in bottom border.  
            
         
        """
        pass
    
    ## Getter for property: (float) CenteringMarkExtension
    ##  Returns the length of centering marks extension from inner border   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksExtension</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def CenteringMarkExtension(self) -> float:
        """
        Getter for property: (float) CenteringMarkExtension
         Returns the length of centering marks extension from inner border   
            
         
        """
        pass
    
    ## Setter for property: (float) CenteringMarkExtension

    ##  Returns the length of centering marks extension from inner border   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksExtension</ja_property_set > instead.  <br> 

    @CenteringMarkExtension.setter
    def CenteringMarkExtension(self, centeringMarkExtension: float):
        """
        Setter for property: (float) CenteringMarkExtension
         Returns the length of centering marks extension from inner border   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateBorders
    ##  Returns the flag that indicates if borders are created.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateBorders</ja_property_get > instead.  <br> 

    ## @return bool
    @property
    def CreateBorders(self) -> bool:
        """
        Getter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateBorders

    ##  Returns the flag that indicates if borders are created.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateBorders</ja_property_set > instead.  <br> 

    @CreateBorders.setter
    def CreateBorders(self, createBorders: bool):
        """
        Setter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateTrimmingMarks
    ##  Returns the flag that indicate if trimming marks are created.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateTrimmingMarks</ja_property_get > instead.  <br> 

    ## @return bool
    @property
    def CreateTrimmingMarks(self) -> bool:
        """
        Getter for property: (bool) CreateTrimmingMarks
         Returns the flag that indicate if trimming marks are created.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateTrimmingMarks

    ##  Returns the flag that indicate if trimming marks are created.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CreateTrimmingMarks</ja_property_set > instead.  <br> 

    @CreateTrimmingMarks.setter
    def CreateTrimmingMarks(self, createTrimmingMarks: bool):
        """
        Setter for property: (bool) CreateTrimmingMarks
         Returns the flag that indicate if trimming marks are created.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateZoneLabels
    ##  Returns the flag that indicates if zone labels are created.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneLabels</ja_property_get > instead.  <br> 

    ## @return bool
    @property
    def CreateZoneLabels(self) -> bool:
        """
        Getter for property: (bool) CreateZoneLabels
         Returns the flag that indicates if zone labels are created.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateZoneLabels

    ##  Returns the flag that indicates if zone labels are created.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneLabels</ja_property_set > instead.  <br> 

    @CreateZoneLabels.setter
    def CreateZoneLabels(self, createZoneLabels: bool):
        """
        Setter for property: (bool) CreateZoneLabels
         Returns the flag that indicates if zone labels are created.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateZoneMarking
    ##  Returns the flag that indicates if zone marking is create.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneMarkings</ja_property_get > instead.  <br> 

    ## @return bool
    @property
    def CreateZoneMarking(self) -> bool:
        """
        Getter for property: (bool) CreateZoneMarking
         Returns the flag that indicates if zone marking is create.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateZoneMarking

    ##  Returns the flag that indicates if zone marking is create.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.CreateZoneMarkings</ja_property_set > instead.  <br> 

    @CreateZoneMarking.setter
    def CreateZoneMarking(self, createZoneMarking: bool):
        """
        Setter for property: (bool) CreateZoneMarking
         Returns the flag that indicates if zone marking is create.  
             
         
        """
        pass
    
    ## Getter for property: (@link SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.HorizontalCenteringMarkType@endlink) HorizontalCenteringMark
    ##  Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksHorizontal</ja_property_get > instead.  <br> 

    ## @return SheetBordersAndZonesBuilder.HorizontalCenteringMarkType
    @property
    def HorizontalCenteringMark(self) -> SheetBordersAndZonesBuilder.HorizontalCenteringMarkType:
        """
        Getter for property: (@link SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.HorizontalCenteringMarkType@endlink) HorizontalCenteringMark
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
             
         
        """
        pass
    
    ## Setter for property: (@link SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.HorizontalCenteringMarkType@endlink) HorizontalCenteringMark

    ##  Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksHorizontal</ja_property_set > instead.  <br> 

    @HorizontalCenteringMark.setter
    def HorizontalCenteringMark(self, horizontalCenteringMarkType: SheetBordersAndZonesBuilder.HorizontalCenteringMarkType):
        """
        Setter for property: (@link SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.HorizontalCenteringMarkType@endlink) HorizontalCenteringMark
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
             
         
        """
        pass
    
    ## Getter for property: (float) HorizontalSize
    ##  Returns the size of horizontal zones.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.HorizontalSize</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def HorizontalSize(self) -> float:
        """
        Getter for property: (float) HorizontalSize
         Returns the size of horizontal zones.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) HorizontalSize

    ##  Returns the size of horizontal zones.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.HorizontalSize</ja_property_set > instead.  <br> 

    @HorizontalSize.setter
    def HorizontalSize(self, horizontalSize: float):
        """
        Setter for property: (float) HorizontalSize
         Returns the size of horizontal zones.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (int) LabelFont
    ##  Returns the font of the label(text).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelFont</ja_property_get > instead.  <br> 

    ## @return int
    @property
    def LabelFont(self) -> int:
        """
        Getter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    
    ## Setter for property: (int) LabelFont

    ##  Returns the font of the label(text).  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelFont</ja_property_set > instead.  <br> 

    @LabelFont.setter
    def LabelFont(self, labelFont: int):
        """
        Setter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    
    ## Getter for property: (float) LabelHeight
    ##  Returns the height of the label(text).  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelHeight</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the height of the label(text).  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) LabelHeight

    ##  Returns the height of the label(text).  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.LabelHeight</ja_property_set > instead.  <br> 

    @LabelHeight.setter
    def LabelHeight(self, labelHeight: float):
        """
        Setter for property: (float) LabelHeight
         Returns the height of the label(text).  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (float) LeftMargin
    ##  Returns the value of the margin in left border.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.LeftTrimmedMargin</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def LeftMargin(self) -> float:
        """
        Getter for property: (float) LeftMargin
         Returns the value of the margin in left border.  
            
         
        """
        pass
    
    ## Setter for property: (float) LeftMargin

    ##  Returns the value of the margin in left border.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.LeftTrimmedMargin</ja_property_set > instead.  <br> 

    @LeftMargin.setter
    def LeftMargin(self, leftMargin: float):
        """
        Setter for property: (float) LeftMargin
         Returns the value of the margin in left border.  
            
         
        """
        pass
    
    ## Getter for property: (float) MarkingHeight
    ##  Returns the height of marking.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.MarkingHeight</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def MarkingHeight(self) -> float:
        """
        Getter for property: (float) MarkingHeight
         Returns the height of marking.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) MarkingHeight

    ##  Returns the height of marking.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.MarkingHeight</ja_property_set > instead.  <br> 

    @MarkingHeight.setter
    def MarkingHeight(self, markingHeight: float):
        """
        Setter for property: (float) MarkingHeight
         Returns the height of marking.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (@link SheetBordersAndZonesBuilder.ZoneMethod NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneMethod@endlink) Method
    ##  Returns the type of methods to create the zones.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.Method</ja_property_get > instead.  <br> 

    ## @return SheetBordersAndZonesBuilder.ZoneMethod
    @property
    def Method(self) -> SheetBordersAndZonesBuilder.ZoneMethod:
        """
        Getter for property: (@link SheetBordersAndZonesBuilder.ZoneMethod NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneMethod@endlink) Method
         Returns the type of methods to create the zones.  
             
         
        """
        pass
    
    ## Setter for property: (@link SheetBordersAndZonesBuilder.ZoneMethod NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneMethod@endlink) Method

    ##  Returns the type of methods to create the zones.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.Method</ja_property_set > instead.  <br> 

    @Method.setter
    def Method(self, method: SheetBordersAndZonesBuilder.ZoneMethod):
        """
        Setter for property: (@link SheetBordersAndZonesBuilder.ZoneMethod NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneMethod@endlink) Method
         Returns the type of methods to create the zones.  
             
         
        """
        pass
    
    ## Getter for property: (@link SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneOrigin@endlink) Origin
    ##  Returns the type of zone origin like TopLeft/BottomRight.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.Origin</ja_property_get > instead.  <br> 

    ## @return SheetBordersAndZonesBuilder.ZoneOrigin
    @property
    def Origin(self) -> SheetBordersAndZonesBuilder.ZoneOrigin:
        """
        Getter for property: (@link SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneOrigin@endlink) Origin
         Returns the type of zone origin like TopLeft/BottomRight.  
             
         
        """
        pass
    
    ## Setter for property: (@link SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneOrigin@endlink) Origin

    ##  Returns the type of zone origin like TopLeft/BottomRight.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.Origin</ja_property_set > instead.  <br> 

    @Origin.setter
    def Origin(self, origin: SheetBordersAndZonesBuilder.ZoneOrigin):
        """
        Setter for property: (@link SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneOrigin@endlink) Origin
         Returns the type of zone origin like TopLeft/BottomRight.  
             
         
        """
        pass
    
    ## Getter for property: (float) RightMargin
    ##  Returns the value of the margin in right border.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.RightTrimmedMargin</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def RightMargin(self) -> float:
        """
        Getter for property: (float) RightMargin
         Returns the value of the margin in right border.  
            
         
        """
        pass
    
    ## Setter for property: (float) RightMargin

    ##  Returns the value of the margin in right border.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.RightTrimmedMargin</ja_property_set > instead.  <br> 

    @RightMargin.setter
    def RightMargin(self, rightMargin: float):
        """
        Setter for property: (float) RightMargin
         Returns the value of the margin in right border.  
            
         
        """
        pass
    
    ## Getter for property: (@link SheetBorderSettingsBuilder NXOpen.Diagramming.SheetBorderSettingsBuilder@endlink) SheetBorderSettings
    ##  Returns the sheet border settings builder used to get the values related to borders  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return SheetBorderSettingsBuilder
    @property
    def SheetBorderSettings(self) -> SheetBorderSettingsBuilder:
        """
        Getter for property: (@link SheetBorderSettingsBuilder NXOpen.Diagramming.SheetBorderSettingsBuilder@endlink) SheetBorderSettings
         Returns the sheet border settings builder used to get the values related to borders  
            
         
        """
        pass
    
    ## Getter for property: (@link SheetMarginSettingsBuilder NXOpen.Diagramming.SheetMarginSettingsBuilder@endlink) SheetMarginSettings
    ##  Returns the sheet margin settings builder used to get the values related to margins  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return SheetMarginSettingsBuilder
    @property
    def SheetMarginSettings(self) -> SheetMarginSettingsBuilder:
        """
        Getter for property: (@link SheetMarginSettingsBuilder NXOpen.Diagramming.SheetMarginSettingsBuilder@endlink) SheetMarginSettings
         Returns the sheet margin settings builder used to get the values related to margins  
            
         
        """
        pass
    
    ## Getter for property: (@link SheetZoneSettingsBuilder NXOpen.Diagramming.SheetZoneSettingsBuilder@endlink) SheetZoneSettings
    ##  Returns the sheet zone settings builder used to get the values related to zones  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return SheetZoneSettingsBuilder
    @property
    def SheetZoneSettings(self) -> SheetZoneSettingsBuilder:
        """
        Getter for property: (@link SheetZoneSettingsBuilder NXOpen.Diagramming.SheetZoneSettingsBuilder@endlink) SheetZoneSettings
         Returns the sheet zone settings builder used to get the values related to zones  
            
         
        """
        pass
    
    ## Getter for property: (float) TopMargin
    ##  Returns the value of the margin in top border.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetMarginSettingsBuilder.TopTrimmedMargin</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def TopMargin(self) -> float:
        """
        Getter for property: (float) TopMargin
         Returns the value of the margin in top border.  
            
         
        """
        pass
    
    ## Setter for property: (float) TopMargin

    ##  Returns the value of the margin in top border.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetMarginSettingsBuilder.TopTrimmedMargin</ja_property_set > instead.  <br> 

    @TopMargin.setter
    def TopMargin(self, topMargin: float):
        """
        Setter for property: (float) TopMargin
         Returns the value of the margin in top border.  
            
         
        """
        pass
    
    ## Getter for property: (float) TrimmingMarkLength
    ##  Returns the length of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkLength</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def TrimmingMarkLength(self) -> float:
        """
        Getter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) TrimmingMarkLength

    ##  Returns the length of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkLength</ja_property_set > instead.  <br> 

    @TrimmingMarkLength.setter
    def TrimmingMarkLength(self, trimmingMarkLength: float):
        """
        Setter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (float) TrimmingMarkThickness
    ##  Returns the width of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkWidth</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def TrimmingMarkThickness(self) -> float:
        """
        Getter for property: (float) TrimmingMarkThickness
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) TrimmingMarkThickness

    ##  Returns the width of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.TrimmingMarkWidth</ja_property_set > instead.  <br> 

    @TrimmingMarkThickness.setter
    def TrimmingMarkThickness(self, trimmingMarkThickness: float):
        """
        Setter for property: (float) TrimmingMarkThickness
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (@link SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.VerticalCenteringMarkType@endlink) VerticalCenteringMark
    ##  Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksVertical</ja_property_get > instead.  <br> 

    ## @return SheetBordersAndZonesBuilder.VerticalCenteringMarkType
    @property
    def VerticalCenteringMark(self) -> SheetBordersAndZonesBuilder.VerticalCenteringMarkType:
        """
        Getter for property: (@link SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.VerticalCenteringMarkType@endlink) VerticalCenteringMark
         Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
             
         
        """
        pass
    
    ## Setter for property: (@link SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.VerticalCenteringMarkType@endlink) VerticalCenteringMark

    ##  Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.CenteringMarksVertical</ja_property_set > instead.  <br> 

    @VerticalCenteringMark.setter
    def VerticalCenteringMark(self, verticalCenteringMark: SheetBordersAndZonesBuilder.VerticalCenteringMarkType):
        """
        Setter for property: (@link SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.VerticalCenteringMarkType@endlink) VerticalCenteringMark
         Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
             
         
        """
        pass
    
    ## Getter for property: (float) VerticalSize
    ##  Returns the size of vertical zones.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetZoneSettingsBuilder.VerticalSize</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def VerticalSize(self) -> float:
        """
        Getter for property: (float) VerticalSize
         Returns the size of vertical zones.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) VerticalSize

    ##  Returns the size of vertical zones.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetZoneSettingsBuilder.VerticalSize</ja_property_set > instead.  <br> 

    @VerticalSize.setter
    def VerticalSize(self, verticalSize: float):
        """
        Setter for property: (float) VerticalSize
         Returns the size of vertical zones.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (float) Width
    ##  Returns the width of border.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_get >NXOpen.Diagramming.SheetBorderSettingsBuilder.BorderLineWidth</ja_property_get > instead.  <br> 

    ## @return float
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) Width

    ##  Returns the width of border.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.1.  Use <ja_property_set >NXOpen.Diagramming.SheetBorderSettingsBuilder.BorderLineWidth</ja_property_set > instead.  <br> 

    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    
    ##  Set the owning sheet when the sheet element is created.
    ##         It is not allowed to change the owning sheet when editing the borders and zones. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="owningSheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def SetOwningSheet(self, owningSheet: Sheet) -> None:
        """
         Set the owning sheet when the sheet element is created.
                It is not allowed to change the owning sheet when editing the borders and zones. 
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Diagramming::SheetBordersAndZones NXOpen::Diagramming::SheetBordersAndZones@endlink  objects  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetBordersAndZonesCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Diagramming.SheetBordersAndZones</ja_class> objects """


    ##  Creates a borders and zones builder 
    ##  @return builder (@link SheetBordersAndZonesBuilder NXOpen.Diagramming.SheetBordersAndZonesBuilder@endlink):  SheetBordersAndZonesBuilder object .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: drafting ("DRAFTING")
    ## 
    ## <param name="bordersAndZones"> (@link SheetBordersAndZones NXOpen.Diagramming.SheetBordersAndZones@endlink)  @link NXOpen::Diagramming::SheetBordersAndZones NXOpen::Diagramming::SheetBordersAndZones@endlink  to be redefined, if NULL then creates a new one </param>
    def CreateSheetBordersAndZonesBuilder(self, bordersAndZones: SheetBordersAndZones) -> SheetBordersAndZonesBuilder:
        """
         Creates a borders and zones builder 
         @return builder (@link SheetBordersAndZonesBuilder NXOpen.Diagramming.SheetBordersAndZonesBuilder@endlink):  SheetBordersAndZonesBuilder object .
        """
        pass
    
    ##   Finds the @link  NXOpen::Diagramming::SheetBordersAndZones   NXOpen::Diagramming::SheetBordersAndZones @endlink  with the given name. 
    ##              An exception will be thrown if no object can be found with the given name. 
    ##  @return bordersAndZones (@link SheetBordersAndZones NXOpen.Diagramming.SheetBordersAndZones@endlink):   Borders and zones object .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  Drawing sheet name </param>
    def FindObject(self, name: str) -> SheetBordersAndZones:
        """
          Finds the @link  NXOpen::Diagramming::SheetBordersAndZones   NXOpen::Diagramming::SheetBordersAndZones @endlink  with the given name. 
                     An exception will be thrown if no object can be found with the given name. 
         @return bordersAndZones (@link SheetBordersAndZones NXOpen.Diagramming.SheetBordersAndZones@endlink):   Borders and zones object .
        """
        pass
    
import NXOpen
##  Represents Sheet Borders and Zones <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::SheetBordersAndZonesBuilder  NXOpen::Diagramming::SheetBordersAndZonesBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetBordersAndZones(NXOpen.NXObject): 
    """ Represents Sheet Borders and Zones"""
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  The SheetBorderSettings builder 
## 
##   <br>  Created in NX11.0.1  <br> 

class SheetBorderSettingsBuilder(NXOpen.TaggedObject): 
    """ The SheetBorderSettings builder """


    ## Getter for property: (float) ArrowAngle
    ##  Returns the angle of arrow in the borders.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ArrowAngle(self) -> float:
        """
        Getter for property: (float) ArrowAngle
         Returns the angle of arrow in the borders.  
             
         
        """
        pass
    
    ## Setter for property: (float) ArrowAngle

    ##  Returns the angle of arrow in the borders.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ArrowAngle.setter
    def ArrowAngle(self, arrowAngle: float):
        """
        Setter for property: (float) ArrowAngle
         Returns the angle of arrow in the borders.  
             
         
        """
        pass
    
    ## Getter for property: (@link ArrowDirectionType NXOpen.Diagramming.ArrowDirectionType@endlink) ArrowDirection
    ##  Returns the direction of arrow like Into Sheet or Out of Sheet.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return ArrowDirectionType
    @property
    def ArrowDirection(self) -> ArrowDirectionType:
        """
        Getter for property: (@link ArrowDirectionType NXOpen.Diagramming.ArrowDirectionType@endlink) ArrowDirection
         Returns the direction of arrow like Into Sheet or Out of Sheet.  
             
         
        """
        pass
    
    ## Setter for property: (@link ArrowDirectionType NXOpen.Diagramming.ArrowDirectionType@endlink) ArrowDirection

    ##  Returns the direction of arrow like Into Sheet or Out of Sheet.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ArrowDirection.setter
    def ArrowDirection(self, arrowDirection: ArrowDirectionType):
        """
        Setter for property: (@link ArrowDirectionType NXOpen.Diagramming.ArrowDirectionType@endlink) ArrowDirection
         Returns the direction of arrow like Into Sheet or Out of Sheet.  
             
         
        """
        pass
    
    ## Getter for property: (float) ArrowHeadTail
    ##  Returns the length of arrow tail.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ArrowHeadTail(self) -> float:
        """
        Getter for property: (float) ArrowHeadTail
         Returns the length of arrow tail.  
             
         
        """
        pass
    
    ## Setter for property: (float) ArrowHeadTail

    ##  Returns the length of arrow tail.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ArrowHeadTail.setter
    def ArrowHeadTail(self, arrowHeadTail: float):
        """
        Setter for property: (float) ArrowHeadTail
         Returns the length of arrow tail.  
             
         
        """
        pass
    
    ## Getter for property: (float) ArrowLength
    ##  Returns the length of arrow in the borders.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ArrowLength(self) -> float:
        """
        Getter for property: (float) ArrowLength
         Returns the length of arrow in the borders.  
             
         
        """
        pass
    
    ## Setter for property: (float) ArrowLength

    ##  Returns the length of arrow in the borders.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ArrowLength.setter
    def ArrowLength(self, arrowLength: float):
        """
        Setter for property: (float) ArrowLength
         Returns the length of arrow in the borders.  
             
         
        """
        pass
    
    ## Getter for property: (@link ArrowStyleType NXOpen.Diagramming.ArrowStyleType@endlink) ArrowStyle
    ##  Returns the type of arrow style like Open, Closed.  
    ##   ..   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return ArrowStyleType
    @property
    def ArrowStyle(self) -> ArrowStyleType:
        """
        Getter for property: (@link ArrowStyleType NXOpen.Diagramming.ArrowStyleType@endlink) ArrowStyle
         Returns the type of arrow style like Open, Closed.  
          ..   
         
        """
        pass
    
    ## Setter for property: (@link ArrowStyleType NXOpen.Diagramming.ArrowStyleType@endlink) ArrowStyle

    ##  Returns the type of arrow style like Open, Closed.  
    ##   ..   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ArrowStyle.setter
    def ArrowStyle(self, arrowStyle: ArrowStyleType):
        """
        Setter for property: (@link ArrowStyleType NXOpen.Diagramming.ArrowStyleType@endlink) ArrowStyle
         Returns the type of arrow style like Open, Closed.  
          ..   
         
        """
        pass
    
    ## Getter for property: (float) BorderLineWidth
    ##  Returns the width of border.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def BorderLineWidth(self) -> float:
        """
        Getter for property: (float) BorderLineWidth
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) BorderLineWidth

    ##  Returns the width of border.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @BorderLineWidth.setter
    def BorderLineWidth(self, borderLineWidth: float):
        """
        Setter for property: (float) BorderLineWidth
         Returns the width of border.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (float) CenteringMarkLength
    ##  Returns the length of centering mark.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def CenteringMarkLength(self) -> float:
        """
        Getter for property: (float) CenteringMarkLength
         Returns the length of centering mark.  
             
         
        """
        pass
    
    ## Setter for property: (float) CenteringMarkLength

    ##  Returns the length of centering mark.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CenteringMarkLength.setter
    def CenteringMarkLength(self, centeringMarkLength: float):
        """
        Setter for property: (float) CenteringMarkLength
         Returns the length of centering mark.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) CenteringMarksColorWidth
    ##  Returns the color and width of centering marks.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def CenteringMarksColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) CenteringMarksColorWidth
         Returns the color and width of centering marks.  
             
         
        """
        pass
    
    ## Getter for property: (float) CenteringMarksExtension
    ##  Returns the length of centering marks extension from inner border.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def CenteringMarksExtension(self) -> float:
        """
        Getter for property: (float) CenteringMarksExtension
         Returns the length of centering marks extension from inner border.  
             
         
        """
        pass
    
    ## Setter for property: (float) CenteringMarksExtension

    ##  Returns the length of centering marks extension from inner border.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CenteringMarksExtension.setter
    def CenteringMarksExtension(self, centeringMarksExtension: float):
        """
        Setter for property: (float) CenteringMarksExtension
         Returns the length of centering marks extension from inner border.  
             
         
        """
        pass
    
    ## Getter for property: (@link HorizontalCenteringMarkType NXOpen.Diagramming.HorizontalCenteringMarkType@endlink) CenteringMarksHorizontal
    ##  Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return HorizontalCenteringMarkType
    @property
    def CenteringMarksHorizontal(self) -> HorizontalCenteringMarkType:
        """
        Getter for property: (@link HorizontalCenteringMarkType NXOpen.Diagramming.HorizontalCenteringMarkType@endlink) CenteringMarksHorizontal
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
             
         
        """
        pass
    
    ## Setter for property: (@link HorizontalCenteringMarkType NXOpen.Diagramming.HorizontalCenteringMarkType@endlink) CenteringMarksHorizontal

    ##  Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CenteringMarksHorizontal.setter
    def CenteringMarksHorizontal(self, centeringMarksHorizontal: HorizontalCenteringMarkType):
        """
        Setter for property: (@link HorizontalCenteringMarkType NXOpen.Diagramming.HorizontalCenteringMarkType@endlink) CenteringMarksHorizontal
         Returns the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
             
         
        """
        pass
    
    ## Getter for property: (@link VerticalCenteringMarkType NXOpen.Diagramming.VerticalCenteringMarkType@endlink) CenteringMarksVertical
    ##  Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return VerticalCenteringMarkType
    @property
    def CenteringMarksVertical(self) -> VerticalCenteringMarkType:
        """
        Getter for property: (@link VerticalCenteringMarkType NXOpen.Diagramming.VerticalCenteringMarkType@endlink) CenteringMarksVertical
         Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
             
         
        """
        pass
    
    ## Setter for property: (@link VerticalCenteringMarkType NXOpen.Diagramming.VerticalCenteringMarkType@endlink) CenteringMarksVertical

    ##  Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CenteringMarksVertical.setter
    def CenteringMarksVertical(self, centeringMarksVertical: VerticalCenteringMarkType):
        """
        Setter for property: (@link VerticalCenteringMarkType NXOpen.Diagramming.VerticalCenteringMarkType@endlink) CenteringMarksVertical
         Returns the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateBorders
    ##  Returns the flag that indicates if borders are created.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CreateBorders(self) -> bool:
        """
        Getter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateBorders

    ##  Returns the flag that indicates if borders are created.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CreateBorders.setter
    def CreateBorders(self, createBorders: bool):
        """
        Setter for property: (bool) CreateBorders
         Returns the flag that indicates if borders are created.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateTrimmingMarks
    ##  Returns the flag indicates to create trimming marks or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CreateTrimmingMarks(self) -> bool:
        """
        Getter for property: (bool) CreateTrimmingMarks
         Returns the flag indicates to create trimming marks or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateTrimmingMarks

    ##  Returns the flag indicates to create trimming marks or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CreateTrimmingMarks.setter
    def CreateTrimmingMarks(self, createTrimmingMarks: bool):
        """
        Setter for property: (bool) CreateTrimmingMarks
         Returns the flag indicates to create trimming marks or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) DisplaySheetSizeInBorder
    ##  Returns the flag indicates to display sheet size in border or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def DisplaySheetSizeInBorder(self) -> bool:
        """
        Getter for property: (bool) DisplaySheetSizeInBorder
         Returns the flag indicates to display sheet size in border or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplaySheetSizeInBorder

    ##  Returns the flag indicates to display sheet size in border or not   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @DisplaySheetSizeInBorder.setter
    def DisplaySheetSizeInBorder(self, displaySheetSizeInBorder: bool):
        """
        Setter for property: (bool) DisplaySheetSizeInBorder
         Returns the flag indicates to display sheet size in border or not   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceFromInnerBorder
    ##  Returns the distance between inner border and arrow head.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def DistanceFromInnerBorder(self) -> float:
        """
        Getter for property: (float) DistanceFromInnerBorder
         Returns the distance between inner border and arrow head.  
             
         
        """
        pass
    
    ## Setter for property: (float) DistanceFromInnerBorder

    ##  Returns the distance between inner border and arrow head.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @DistanceFromInnerBorder.setter
    def DistanceFromInnerBorder(self, distanceInFromInnerBorder: float):
        """
        Setter for property: (float) DistanceFromInnerBorder
         Returns the distance between inner border and arrow head.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) InnerLineCFW
    ##  Returns the color, font and width of inner border line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def InnerLineCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) InnerLineCFW
         Returns the color, font and width of inner border line.  
             
         
        """
        pass
    
    ## Getter for property: (@link Method NXOpen.Diagramming.Method@endlink) Method
    ##  Returns the type of method to display like Standard/Custom   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Method
    @property
    def Method(self) -> Method:
        """
        Getter for property: (@link Method NXOpen.Diagramming.Method@endlink) Method
         Returns the type of method to display like Standard/Custom   
            
         
        """
        pass
    
    ## Setter for property: (@link Method NXOpen.Diagramming.Method@endlink) Method

    ##  Returns the type of method to display like Standard/Custom   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Method.setter
    def Method(self, method: Method):
        """
        Setter for property: (@link Method NXOpen.Diagramming.Method@endlink) Method
         Returns the type of method to display like Standard/Custom   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) OuterLineCFW
    ##  Returns the color, font and width of outer border line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def OuterLineCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) OuterLineCFW
         Returns the color, font and width of outer border line.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrimmingMarkColor
    ##  Returns the color of trimming mark.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def TrimmingMarkColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrimmingMarkColor
         Returns the color of trimming mark.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrimmingMarkColor

    ##  Returns the color of trimming mark.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TrimmingMarkColor.setter
    def TrimmingMarkColor(self, trimmingMarkColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrimmingMarkColor
         Returns the color of trimming mark.  
             
         
        """
        pass
    
    ## Getter for property: (float) TrimmingMarkLength
    ##  Returns the length of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def TrimmingMarkLength(self) -> float:
        """
        Getter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) TrimmingMarkLength

    ##  Returns the length of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TrimmingMarkLength.setter
    def TrimmingMarkLength(self, trimmingMarkLength: float):
        """
        Setter for property: (float) TrimmingMarkLength
         Returns the length of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (@link TrimmingMarkStyleType NXOpen.Diagramming.TrimmingMarkStyleType@endlink) TrimmingMarkStyle
    ##  Returns the type of trimming mark style like Corner or Triangle.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return TrimmingMarkStyleType
    @property
    def TrimmingMarkStyle(self) -> TrimmingMarkStyleType:
        """
        Getter for property: (@link TrimmingMarkStyleType NXOpen.Diagramming.TrimmingMarkStyleType@endlink) TrimmingMarkStyle
         Returns the type of trimming mark style like Corner or Triangle.  
             
         
        """
        pass
    
    ## Setter for property: (@link TrimmingMarkStyleType NXOpen.Diagramming.TrimmingMarkStyleType@endlink) TrimmingMarkStyle

    ##  Returns the type of trimming mark style like Corner or Triangle.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TrimmingMarkStyle.setter
    def TrimmingMarkStyle(self, trimmingMarkStyle: TrimmingMarkStyleType):
        """
        Setter for property: (@link TrimmingMarkStyleType NXOpen.Diagramming.TrimmingMarkStyleType@endlink) TrimmingMarkStyle
         Returns the type of trimming mark style like Corner or Triangle.  
             
         
        """
        pass
    
    ## Getter for property: (float) TrimmingMarkWidth
    ##  Returns the width of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def TrimmingMarkWidth(self) -> float:
        """
        Getter for property: (float) TrimmingMarkWidth
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) TrimmingMarkWidth

    ##  Returns the width of trimming mark.  
    ##    It should be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TrimmingMarkWidth.setter
    def TrimmingMarkWidth(self, trimmingMarkWidth: float):
        """
        Setter for property: (float) TrimmingMarkWidth
         Returns the width of trimming mark.  
           It should be greater than zero.   
         
        """
        pass
    
import NXOpen
## 
##     Represents a SheetBuilder.
##      <br> To create a new instance of this class, use @link NXOpen::Diagramming::SheetCollection::CreateSheetBuilder  NXOpen::Diagramming::SheetCollection::CreateSheetBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetBuilder(BaseObjectBuilder): 
    """
    Represents a SheetBuilder.
    """


    ## Getter for property: (bool) AllowJumpers
    ##  Returns the flag if jumpers are allowed to use where connections cross.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def AllowJumpers(self) -> bool:
        """
        Getter for property: (bool) AllowJumpers
         Returns the flag if jumpers are allowed to use where connections cross.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AllowJumpers

    ##  Returns the flag if jumpers are allowed to use where connections cross.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AllowJumpers.setter
    def AllowJumpers(self, allowJumper: bool):
        """
        Setter for property: (bool) AllowJumpers
         Returns the flag if jumpers are allowed to use where connections cross.  
             
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##  Returns the description that will be visible when a template is selected in the Item Rev dialog.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##  Returns the description that will be visible when a template is selected in the Item Rev dialog.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    
    ## Getter for property: (@link DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType
    ##  Returns the jumper type of the sheet.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return DiagrammingJumpertype
    @property
    def JumperType(self) -> DiagrammingJumpertype:
        """
        Getter for property: (@link DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType
         Returns the jumper type of the sheet.  
             
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType

    ##  Returns the jumper type of the sheet.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @JumperType.setter
    def JumperType(self, jumperType: DiagrammingJumpertype):
        """
        Setter for property: (@link DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType
         Returns the jumper type of the sheet.  
             
         
        """
        pass
    
    ## Getter for property: (float) Opacity
    ##  Returns the opacity of sheet.  
    ##    0.0 is completely transparent and 1.0 is completely opaque  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Opacity(self) -> float:
        """
        Getter for property: (float) Opacity
         Returns the opacity of sheet.  
           0.0 is completely transparent and 1.0 is completely opaque  
         
        """
        pass
    
    ## Setter for property: (float) Opacity

    ##  Returns the opacity of sheet.  
    ##    0.0 is completely transparent and 1.0 is completely opaque  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Opacity.setter
    def Opacity(self, opacity: float):
        """
        Setter for property: (float) Opacity
         Returns the opacity of sheet.  
           0.0 is completely transparent and 1.0 is completely opaque  
         
        """
        pass
    
    ## Getter for property: (str) PaxFileName
    ##  Returns the path name of the PAX file to which the template will be written to.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def PaxFileName(self) -> str:
        """
        Getter for property: (str) PaxFileName
         Returns the path name of the PAX file to which the template will be written to.  
             
         
        """
        pass
    
    ## Setter for property: (str) PaxFileName

    ##  Returns the path name of the PAX file to which the template will be written to.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @PaxFileName.setter
    def PaxFileName(self, paxFileName: str):
        """
        Setter for property: (str) PaxFileName
         Returns the path name of the PAX file to which the template will be written to.  
             
         
        """
        pass
    
    ## Getter for property: (str) PresentationName
    ##  Returns the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
             
         
        """
        pass
    
    ## Setter for property: (str) PresentationName

    ##  Returns the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @PresentationName.setter
    def PresentationName(self, presentationName: str):
        """
        Setter for property: (str) PresentationName
         Returns the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
             
         
        """
        pass
    
    ## Getter for property: (str) ToolTip
    ##  Returns the tooltip that will be visible when a template is selected in the Item Rev dialog.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def ToolTip(self) -> str:
        """
        Getter for property: (str) ToolTip
         Returns the tooltip that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    
    ## Setter for property: (str) ToolTip

    ##  Returns the tooltip that will be visible when a template is selected in the Item Rev dialog.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ToolTip.setter
    def ToolTip(self, toolTip: str):
        """
        Setter for property: (str) ToolTip
         Returns the tooltip that will be visible when a template is selected in the Item Rev dialog.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Units
    ##  Returns the units of the sheet.  
    ##    It could be either "meters" or "inches".   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def Units(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Units
         Returns the units of the sheet.  
           It could be either "meters" or "inches".   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Units

    ##  Returns the units of the sheet.  
    ##    It could be either "meters" or "inches".   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Units.setter
    def Units(self, unit: NXOpen.Unit):
        """
        Setter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Units
         Returns the units of the sheet.  
           It could be either "meters" or "inches".   
         
        """
        pass
    
    ## Getter for property: (bool) UpdatePAXFile
    ##  Returns the flag to update pax file or not.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def UpdatePAXFile(self) -> bool:
        """
        Getter for property: (bool) UpdatePAXFile
         Returns the flag to update pax file or not.  
            
         
        """
        pass
    
    ## Setter for property: (bool) UpdatePAXFile

    ##  Returns the flag to update pax file or not.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @UpdatePAXFile.setter
    def UpdatePAXFile(self, updatePAXFile: bool):
        """
        Setter for property: (bool) UpdatePAXFile
         Returns the flag to update pax file or not.  
            
         
        """
        pass
    
    ##  Gets all features. 
    ##  @return features (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetFeatures(self) -> List[SheetElement]:
        """
         Gets all features. 
         @return features (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink): .
        """
        pass
    
    ##  Gets all sheet elements. 
    ##  @return sheetElements (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetSheetElements(self) -> List[SheetElement]:
        """
         Gets all sheet elements. 
         @return sheetElements (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink): .
        """
        pass
    
    ##  Gets the height and width of this sheet. 
    ##  @return A tuple consisting of (height, width). 
    ##  - height is: float.
    ##  - width is: float.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetSize(self) -> Tuple[float, float]:
        """
         Gets the height and width of this sheet. 
         @return A tuple consisting of (height, width). 
         - height is: float.
         - width is: float.

        """
        pass
    
    ##  Sets the height and width of this sheet. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="height"> (float) </param>
    ## <param name="width"> (float) </param>
    def SetSize(self, height: float, width: float) -> None:
        """
         Sets the height and width of this sheet. 
        """
        pass
    
import NXOpen
##  Represents a collection of Sheet.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Sheet. """


    ##  Creates a @link NXOpen::Diagramming::SheetBuilder NXOpen::Diagramming::SheetBuilder@endlink . 
    ##  @return builder (@link SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink)  @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink  to be edited, if NULL then create a new one </param>
    def CreateSheetBuilder(self, sheet: Sheet) -> SheetBuilder:
        """
         Creates a @link NXOpen::Diagramming::SheetBuilder NXOpen::Diagramming::SheetBuilder@endlink . 
         @return builder (@link SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return sheet (@link Sheet NXOpen.Diagramming.Sheet@endlink):  @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink  with this name. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> Sheet:
        """
         Finds the @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return sheet (@link Sheet NXOpen.Diagramming.Sheet@endlink):  @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink  with this name. .
        """
        pass
    
    ##  Returns the work sheet from part. 
    ##  @return sheet (@link Sheet NXOpen.Diagramming.Sheet@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetWorkSheet(self) -> Sheet:
        """
         Returns the work sheet from part. 
         @return sheet (@link Sheet NXOpen.Diagramming.Sheet@endlink): .
        """
        pass
    
## 
##     Represents a SheetElementBuilder.
##      <br> This is an abstract class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetElementBuilder(BaseObjectBuilder): 
    """
    Represents a SheetElementBuilder.
    """


    ##  Represents the resize option 
    ##            for a @link NXOpen::Diagramming::SheetElementBuilder NXOpen::Diagramming::SheetElementBuilder@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnyDirection</term><description> 
    ## </description> </item><item><term> 
    ## OnAnchor</term><description> 
    ## </description> </item><item><term> 
    ## SameRatio</term><description> 
    ## </description> </item><item><term> 
    ## SameRationOnCorner</term><description> 
    ## </description> </item><item><term> 
    ## SameRatioOnEdge</term><description> 
    ## </description> </item></list>
    class ResizeOptionType(Enum):
        """
        Members Include: <AnyDirection> <OnAnchor> <SameRatio> <SameRationOnCorner> <SameRatioOnEdge>
        """
        AnyDirection: int
        OnAnchor: int
        SameRatio: int
        SameRationOnCorner: int
        SameRatioOnEdge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SheetElementBuilder.ResizeOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) Height
    ##  Returns the height.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height.  
             
         
        """
        pass
    
    ## Setter for property: (float) Height

    ##  Returns the height.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height.  
             
         
        """
        pass
    
    ## Getter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) HeightPolicy
    ##  Returns the height policy.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagrammingSizingpolicy
    @property
    def HeightPolicy(self) -> DiagrammingSizingpolicy:
        """
        Getter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) HeightPolicy
         Returns the height policy.  
             
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) HeightPolicy

    ##  Returns the height policy.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @HeightPolicy.setter
    def HeightPolicy(self, heightPolicy: DiagrammingSizingpolicy):
        """
        Setter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) HeightPolicy
         Returns the height policy.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Internal
    ##  Returns the flag that indicates if the sheet element is internal.  
    ##    If false it is not part of the user's data model; for example, an Annotation is not part of the user's model of Nodes and Connections.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Internal(self) -> bool:
        """
        Getter for property: (bool) Internal
         Returns the flag that indicates if the sheet element is internal.  
           If false it is not part of the user's data model; for example, an Annotation is not part of the user's model of Nodes and Connections.   
         
        """
        pass
    
    ## Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
    ##  Returns the label of this sheet element.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Annotation
    @property
    def Label(self) -> Annotation:
        """
        Getter for property: (@link Annotation NXOpen.Diagramming.Annotation@endlink) Label
         Returns the label of this sheet element.  
             
         
        """
        pass
    
    ## Getter for property: (str) LabelName
    ##  Returns the label name of this sheet element.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def LabelName(self) -> str:
        """
        Getter for property: (str) LabelName
         Returns the label name of this sheet element.  
             
         
        """
        pass
    
    ## Setter for property: (str) LabelName

    ##  Returns the label name of this sheet element.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LabelName.setter
    def LabelName(self, labelname: str):
        """
        Setter for property: (str) LabelName
         Returns the label name of this sheet element.  
             
         
        """
        pass
    
    ## Getter for property: (@link LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Location
    ##  Returns the location of the sheet element relative to another sheet element.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LocationBuilder
    @property
    def Location(self) -> LocationBuilder:
        """
        Getter for property: (@link LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) Location
         Returns the location of the sheet element relative to another sheet element.  
             
         
        """
        pass
    
    ## Getter for property: (@link DiagrammingLocationstyle NXOpen.Diagramming.DiagrammingLocationstyle@endlink) LocationStyle
    ##  Returns the location style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagrammingLocationstyle
    @property
    def LocationStyle(self) -> DiagrammingLocationstyle:
        """
        Getter for property: (@link DiagrammingLocationstyle NXOpen.Diagramming.DiagrammingLocationstyle@endlink) LocationStyle
         Returns the location style.  
             
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingLocationstyle NXOpen.Diagramming.DiagrammingLocationstyle@endlink) LocationStyle

    ##  Returns the location style.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LocationStyle.setter
    def LocationStyle(self, locationStyle: DiagrammingLocationstyle):
        """
        Setter for property: (@link DiagrammingLocationstyle NXOpen.Diagramming.DiagrammingLocationstyle@endlink) LocationStyle
         Returns the location style.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MirrorX
    ##  Returns the sheet element to Mirror along the X axis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def MirrorX(self) -> bool:
        """
        Getter for property: (bool) MirrorX
         Returns the sheet element to Mirror along the X axis.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MirrorX

    ##  Returns the sheet element to Mirror along the X axis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MirrorX.setter
    def MirrorX(self, mirrorX: bool):
        """
        Setter for property: (bool) MirrorX
         Returns the sheet element to Mirror along the X axis.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MirrorY
    ##  Returns the sheet element to Mirror along the Y axis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def MirrorY(self) -> bool:
        """
        Getter for property: (bool) MirrorY
         Returns the sheet element to Mirror along the Y axis.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MirrorY

    ##  Returns the sheet element to Mirror along the Y axis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MirrorY.setter
    def MirrorY(self, mirrorY: bool):
        """
        Setter for property: (bool) MirrorY
         Returns the sheet element to Mirror along the Y axis.  
             
         
        """
        pass
    
    ## Getter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Owner
    ##  Returns the owning sheet element.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SheetElement
    @property
    def Owner(self) -> SheetElement:
        """
        Getter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Owner
         Returns the owning sheet element.  
             
         
        """
        pass
    
    ## Setter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Owner

    ##  Returns the owning sheet element.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Owner.setter
    def Owner(self, owner: SheetElement):
        """
        Setter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) Owner
         Returns the owning sheet element.  
             
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) OwningSheet
    ##  Returns the owning sheet.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return Sheet
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) OwningSheet
         Returns the owning sheet.  
             
         
        """
        pass
    
    ## Getter for property: (@link RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RenderingProperties
    ##  Returns the renderingProperties of the sheet element.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RenderingPropertiesBuilder
    @property
    def RenderingProperties(self) -> RenderingPropertiesBuilder:
        """
        Getter for property: (@link RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) RenderingProperties
         Returns the renderingProperties of the sheet element.  
            
         
        """
        pass
    
    ## Getter for property: (@link SheetElementBuilder.ResizeOptionType NXOpen.Diagramming.SheetElementBuilder.ResizeOptionType@endlink) ResizeOption
    ##  Returns the resize option of the sheet element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return SheetElementBuilder.ResizeOptionType
    @property
    def ResizeOption(self) -> SheetElementBuilder.ResizeOptionType:
        """
        Getter for property: (@link SheetElementBuilder.ResizeOptionType NXOpen.Diagramming.SheetElementBuilder.ResizeOptionType@endlink) ResizeOption
         Returns the resize option of the sheet element   
            
         
        """
        pass
    
    ## Setter for property: (@link SheetElementBuilder.ResizeOptionType NXOpen.Diagramming.SheetElementBuilder.ResizeOptionType@endlink) ResizeOption

    ##  Returns the resize option of the sheet element   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ResizeOption.setter
    def ResizeOption(self, resizeOption: SheetElementBuilder.ResizeOptionType):
        """
        Setter for property: (@link SheetElementBuilder.ResizeOptionType NXOpen.Diagramming.SheetElementBuilder.ResizeOptionType@endlink) ResizeOption
         Returns the resize option of the sheet element   
            
         
        """
        pass
    
    ## Getter for property: (float) Rotation
    ##  Returns the rotation angle that is counter clockwise and relative to the owner.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Rotation(self) -> float:
        """
        Getter for property: (float) Rotation
         Returns the rotation angle that is counter clockwise and relative to the owner.  
             
         
        """
        pass
    
    ## Setter for property: (float) Rotation

    ##  Returns the rotation angle that is counter clockwise and relative to the owner.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Rotation.setter
    def Rotation(self, angle: float):
        """
        Setter for property: (float) Rotation
         Returns the rotation angle that is counter clockwise and relative to the owner.  
             
         
        """
        pass
    
    ## Getter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) SourceElement
    ##  Returns the source element that records which sheet element it is a copy of.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return SheetElement
    @property
    def SourceElement(self) -> SheetElement:
        """
        Getter for property: (@link SheetElement NXOpen.Diagramming.SheetElement@endlink) SourceElement
         Returns the source element that records which sheet element it is a copy of.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UpToDate
    ##  Returns the flag that indicates if the sheet element is up to date.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def UpToDate(self) -> bool:
        """
        Getter for property: (bool) UpToDate
         Returns the flag that indicates if the sheet element is up to date.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visible
    ##  Returns the flag that indicates if the sheet element is visible.  
    ##    If true it is visible.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def Visible(self) -> bool:
        """
        Getter for property: (bool) Visible
         Returns the flag that indicates if the sheet element is visible.  
           If true it is visible.   
         
        """
        pass
    
    ## Getter for property: (float) Width
    ##  Returns the width.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width.  
             
         
        """
        pass
    
    ## Setter for property: (float) Width

    ##  Returns the width.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width.  
             
         
        """
        pass
    
    ## Getter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) WidthPolicy
    ##  Returns the width policy.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagrammingSizingpolicy
    @property
    def WidthPolicy(self) -> DiagrammingSizingpolicy:
        """
        Getter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) WidthPolicy
         Returns the width policy.  
             
         
        """
        pass
    
    ## Setter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) WidthPolicy

    ##  Returns the width policy.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @WidthPolicy.setter
    def WidthPolicy(self, widthPolicy: DiagrammingSizingpolicy):
        """
        Setter for property: (@link DiagrammingSizingpolicy NXOpen.Diagramming.DiagrammingSizingpolicy@endlink) WidthPolicy
         Returns the width policy.  
             
         
        """
        pass
    
    ## Getter for property: (float) X
    ##  Returns the absolute x coordinate.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def X(self) -> float:
        """
        Getter for property: (float) X
         Returns the absolute x coordinate.  
             
         
        """
        pass
    
    ## Setter for property: (float) X

    ##  Returns the absolute x coordinate.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @X.setter
    def X(self, x: float):
        """
        Setter for property: (float) X
         Returns the absolute x coordinate.  
             
         
        """
        pass
    
    ## Getter for property: (float) Y
    ##  Returns the absolute y coordinate.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def Y(self) -> float:
        """
        Getter for property: (float) Y
         Returns the absolute y coordinate.  
             
         
        """
        pass
    
    ## Setter for property: (float) Y

    ##  Returns the absolute y coordinate.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @Y.setter
    def Y(self, y: float):
        """
        Setter for property: (float) Y
         Returns the absolute y coordinate.  
             
         
        """
        pass
    
    ## Getter for property: (int) ZDepth
    ##  Returns the Z depth.  
    ##    Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def ZDepth(self) -> int:
        """
        Getter for property: (int) ZDepth
         Returns the Z depth.  
           Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value.   
         
        """
        pass
    
    ## Setter for property: (int) ZDepth

    ##  Returns the Z depth.  
    ##    Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ZDepth.setter
    def ZDepth(self, zDepth: int):
        """
        Setter for property: (int) ZDepth
         Returns the Z depth.  
           Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value.   
         
        """
        pass
    
    ##  Get the allowed transformations of the sheet element. 
    ##  @return A tuple consisting of (isAllowedTranslation, isAllowedRotation, isAllowedScale, isAllowedShear). 
    ##  - isAllowedTranslation is: bool.
    ##  - isAllowedRotation is: bool.
    ##  - isAllowedScale is: bool.
    ##  - isAllowedShear is: bool.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetAllowedTransformations(self) -> Tuple[bool, bool, bool, bool]:
        """
         Get the allowed transformations of the sheet element. 
         @return A tuple consisting of (isAllowedTranslation, isAllowedRotation, isAllowedScale, isAllowedShear). 
         - isAllowedTranslation is: bool.
         - isAllowedRotation is: bool.
         - isAllowedScale is: bool.
         - isAllowedShear is: bool.

        """
        pass
    
    ##  Gets the minimum node size values 
    ##  @return sizeValues (List[float]):  Minimum node size values as output.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetMinNodeSize(self) -> List[float]:
        """
         Gets the minimum node size values 
         @return sizeValues (List[float]):  Minimum node size values as output.
        """
        pass
    
    ##  Sets the minimum node size values 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sizeValues"> (List[float])  Minimum node size values as input</param>
    def SetMinNodeSize(self, sizeValues: List[float]) -> None:
        """
         Sets the minimum node size values 
        """
        pass
    
    ##  Set the owning sheet when the sheet element is created.
    ##         It is not allowed to change the owning sheet when editing the sheet element. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="owningSheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def SetOwningSheet(self, owningSheet: Sheet) -> None:
        """
         Set the owning sheet when the sheet element is created.
                It is not allowed to change the owning sheet when editing the sheet element. 
        """
        pass
    
##  Represents the SheetElement class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::SheetElementBuilder  NXOpen::Diagramming::SheetElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SheetElement(BaseObject): 
    """ Represents the SheetElement class. """
    pass


import NXOpen
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SheetManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ## Getter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet
    ##  Returns the active sheet   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return Sheet
    @property
    def ActiveSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet

    ##  Returns the active sheet   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ActiveSheet.setter
    def ActiveSheet(self, sheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.Diagramming.Sheet@endlink) ActiveSheet
         Returns the active sheet   
            
         
        """
        pass
    
    ##  Returns the ViewOperations instance belonging to this session 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link ViewOperations NXOpen.Diagramming.ViewOperations@endlink
    @property
    def ViewOperations() -> ViewOperations:
        """
         Returns the ViewOperations instance belonging to this session 
        """
        pass
    
    ##  Returns the GroupManager instance belonging to this session 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @link GroupManager NXOpen.Diagramming.GroupManager@endlink
    @property
    def GroupManager() -> GroupManager:
        """
         Returns the GroupManager instance belonging to this session 
        """
        pass
    
    ##  Opens a @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink . 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def OpenSheet(sheet: Sheet) -> None:
        """
         Opens a @link NXOpen::Diagramming::Sheet NXOpen::Diagramming::Sheet@endlink . 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  The SheetMarginSettings builder 
## 
##   <br>  Created in NX11.0.1  <br> 

class SheetMarginSettingsBuilder(NXOpen.TaggedObject): 
    """ The SheetMarginSettings builder """


    ## Getter for property: (float) BottomTrimmedMargin
    ##  Returns the value of the margin in bottom border.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def BottomTrimmedMargin(self) -> float:
        """
        Getter for property: (float) BottomTrimmedMargin
         Returns the value of the margin in bottom border.  
             
         
        """
        pass
    
    ## Setter for property: (float) BottomTrimmedMargin

    ##  Returns the value of the margin in bottom border.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @BottomTrimmedMargin.setter
    def BottomTrimmedMargin(self, bottomTrimmedMargin: float):
        """
        Setter for property: (float) BottomTrimmedMargin
         Returns the value of the margin in bottom border.  
             
         
        """
        pass
    
    ## Getter for property: (float) BottomUntrimmedMargin
    ##  Returns the distance between bottom of the sheet and bottom trimmed margin.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def BottomUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) BottomUntrimmedMargin
         Returns the distance between bottom of the sheet and bottom trimmed margin.  
             
         
        """
        pass
    
    ## Setter for property: (float) BottomUntrimmedMargin

    ##  Returns the distance between bottom of the sheet and bottom trimmed margin.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @BottomUntrimmedMargin.setter
    def BottomUntrimmedMargin(self, bottomUntrimmedMargin: float):
        """
        Setter for property: (float) BottomUntrimmedMargin
         Returns the distance between bottom of the sheet and bottom trimmed margin.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateUntrimmedMargins
    ##  Returns the flag indicates to create untrimmed margins or not.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def CreateUntrimmedMargins(self) -> bool:
        """
        Getter for property: (bool) CreateUntrimmedMargins
         Returns the flag indicates to create untrimmed margins or not.  
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateUntrimmedMargins

    ##  Returns the flag indicates to create untrimmed margins or not.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CreateUntrimmedMargins.setter
    def CreateUntrimmedMargins(self, createUntrimmedMargins: bool):
        """
        Setter for property: (bool) CreateUntrimmedMargins
         Returns the flag indicates to create untrimmed margins or not.  
            
         
        """
        pass
    
    ## Getter for property: (float) LeftTrimmedMargin
    ##  Returns the value of the margin in left border.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def LeftTrimmedMargin(self) -> float:
        """
        Getter for property: (float) LeftTrimmedMargin
         Returns the value of the margin in left border.  
             
         
        """
        pass
    
    ## Setter for property: (float) LeftTrimmedMargin

    ##  Returns the value of the margin in left border.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LeftTrimmedMargin.setter
    def LeftTrimmedMargin(self, leftTrimmedMargin: float):
        """
        Setter for property: (float) LeftTrimmedMargin
         Returns the value of the margin in left border.  
             
         
        """
        pass
    
    ## Getter for property: (float) LeftUntrimmedMargin
    ##  Returns the distance between left of the sheet and left trimmed margin.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def LeftUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) LeftUntrimmedMargin
         Returns the distance between left of the sheet and left trimmed margin.  
             
         
        """
        pass
    
    ## Setter for property: (float) LeftUntrimmedMargin

    ##  Returns the distance between left of the sheet and left trimmed margin.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LeftUntrimmedMargin.setter
    def LeftUntrimmedMargin(self, leftUntrimmedMargin: float):
        """
        Setter for property: (float) LeftUntrimmedMargin
         Returns the distance between left of the sheet and left trimmed margin.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) MarginLineColorFontWidth
    ##  Returns the color, font and width of margin line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def MarginLineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) MarginLineColorFontWidth
         Returns the color, font and width of margin line.  
             
         
        """
        pass
    
    ## Getter for property: (float) RightTrimmedMargin
    ##  Returns the value of the margin in right border.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def RightTrimmedMargin(self) -> float:
        """
        Getter for property: (float) RightTrimmedMargin
         Returns the value of the margin in right border.  
             
         
        """
        pass
    
    ## Setter for property: (float) RightTrimmedMargin

    ##  Returns the value of the margin in right border.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RightTrimmedMargin.setter
    def RightTrimmedMargin(self, rightTrimmedMargin: float):
        """
        Setter for property: (float) RightTrimmedMargin
         Returns the value of the margin in right border.  
             
         
        """
        pass
    
    ## Getter for property: (float) RightUntrimmedMargin
    ##  Returns the distance between right of the sheet and right trimmed margin.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def RightUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) RightUntrimmedMargin
         Returns the distance between right of the sheet and right trimmed margin.  
             
         
        """
        pass
    
    ## Setter for property: (float) RightUntrimmedMargin

    ##  Returns the distance between right of the sheet and right trimmed margin.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @RightUntrimmedMargin.setter
    def RightUntrimmedMargin(self, rightUntrimmedMargin: float):
        """
        Setter for property: (float) RightUntrimmedMargin
         Returns the distance between right of the sheet and right trimmed margin.  
             
         
        """
        pass
    
    ## Getter for property: (float) TopTrimmedMargin
    ##  Returns the value of the margin in top border.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def TopTrimmedMargin(self) -> float:
        """
        Getter for property: (float) TopTrimmedMargin
         Returns the value of the margin in top border.  
             
         
        """
        pass
    
    ## Setter for property: (float) TopTrimmedMargin

    ##  Returns the value of the margin in top border.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TopTrimmedMargin.setter
    def TopTrimmedMargin(self, topMargin: float):
        """
        Setter for property: (float) TopTrimmedMargin
         Returns the value of the margin in top border.  
             
         
        """
        pass
    
    ## Getter for property: (float) TopUntrimmedMargin
    ##  Returns the distance between top of the sheet and top trimmed margin.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def TopUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) TopUntrimmedMargin
         Returns the distance between top of the sheet and top trimmed margin.  
             
         
        """
        pass
    
    ## Setter for property: (float) TopUntrimmedMargin

    ##  Returns the distance between top of the sheet and top trimmed margin.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TopUntrimmedMargin.setter
    def TopUntrimmedMargin(self, topUntrimmedMargin: float):
        """
        Setter for property: (float) TopUntrimmedMargin
         Returns the distance between top of the sheet and top trimmed margin.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Diagramming::SheetSizeBuilder NXOpen::Diagramming::SheetSizeBuilder@endlink  builder, and the builder is used to model a sheet size.  <br> To create a new instance of this class, use @link NXOpen::Diagramming::DiagrammingManager::CreateSheetSizeBuilder  NXOpen::Diagramming::DiagrammingManager::CreateSheetSizeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class SheetSizeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Diagramming.SheetSizeBuilder</ja_class> builder, and the builder is used to model a sheet size. """


    ## Getter for property: (@link SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink) Sheet
    ##  Returns the diagramming sheet builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SheetBuilder
    @property
    def Sheet(self) -> SheetBuilder:
        """
        Getter for property: (@link SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink) Sheet
         Returns the diagramming sheet builder.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Diagramming::SheetTemplateBuilder NXOpen::Diagramming::SheetTemplateBuilder@endlink  builder, and the builder is used to model a sheet template.  <br> To create a new instance of this class, use @link NXOpen::Diagramming::DiagrammingManager::CreateSheetTemplateBuilder  NXOpen::Diagramming::DiagrammingManager::CreateSheetTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class SheetTemplateBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Diagramming.SheetTemplateBuilder</ja_class> builder, and the builder is used to model a sheet template. """


    ## Getter for property: (@link SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink) Sheet
    ##  Returns the diagramming sheet builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SheetBuilder
    @property
    def Sheet(self) -> SheetBuilder:
        """
        Getter for property: (@link SheetBuilder NXOpen.Diagramming.SheetBuilder@endlink) Sheet
         Returns the diagramming sheet builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link SheetSizeBuilder NXOpen.Diagramming.SheetSizeBuilder@endlink) SheetSize
    ##  Returns    the sheet size builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SheetSizeBuilder
    @property
    def SheetSize(self) -> SheetSizeBuilder:
        """
        Getter for property: (@link SheetSizeBuilder NXOpen.Diagramming.SheetSizeBuilder@endlink) SheetSize
         Returns    the sheet size builder   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  The SheetZoneSettings builder 
## 
##   <br>  Created in NX11.0.1  <br> 

class SheetZoneSettingsBuilder(NXOpen.TaggedObject): 
    """ The SheetZoneSettings builder """


    ## Getter for property: (bool) ContinueZoneIndexingAcrossSheets
    ##  Returns the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ContinueZoneIndexingAcrossSheets(self) -> bool:
        """
        Getter for property: (bool) ContinueZoneIndexingAcrossSheets
         Returns the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ContinueZoneIndexingAcrossSheets

    ##  Returns the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ContinueZoneIndexingAcrossSheets.setter
    def ContinueZoneIndexingAcrossSheets(self, continueZoneIndexingAcrossSheets: bool):
        """
        Setter for property: (bool) ContinueZoneIndexingAcrossSheets
         Returns the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
             
         
        """
        pass
    
    ## Getter for property: (float) CornerZoneModification
    ##  Returns the corner zone modification used as determine the size of the corner zone.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def CornerZoneModification(self) -> float:
        """
        Getter for property: (float) CornerZoneModification
         Returns the corner zone modification used as determine the size of the corner zone.  
             
         
        """
        pass
    
    ## Setter for property: (float) CornerZoneModification

    ##  Returns the corner zone modification used as determine the size of the corner zone.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CornerZoneModification.setter
    def CornerZoneModification(self, cornerZoneModification: float):
        """
        Setter for property: (float) CornerZoneModification
         Returns the corner zone modification used as determine the size of the corner zone.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateZoneLabels
    ##  Returns the flag indicates to create zone labels or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CreateZoneLabels(self) -> bool:
        """
        Getter for property: (bool) CreateZoneLabels
         Returns the flag indicates to create zone labels or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateZoneLabels

    ##  Returns the flag indicates to create zone labels or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CreateZoneLabels.setter
    def CreateZoneLabels(self, createZoneLabels: bool):
        """
        Setter for property: (bool) CreateZoneLabels
         Returns the flag indicates to create zone labels or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateZoneMarkings
    ##  Returns the flag indicates to create zone markings or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CreateZoneMarkings(self) -> bool:
        """
        Getter for property: (bool) CreateZoneMarkings
         Returns the flag indicates to create zone markings or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateZoneMarkings

    ##  Returns the flag indicates to create zone markings or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CreateZoneMarkings.setter
    def CreateZoneMarkings(self, createZoneMarkings: bool):
        """
        Setter for property: (bool) CreateZoneMarkings
         Returns the flag indicates to create zone markings or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateZones
    ##  Returns the flag indicates to create zones or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def CreateZones(self) -> bool:
        """
        Getter for property: (bool) CreateZones
         Returns the flag indicates to create zones or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateZones

    ##  Returns the flag indicates to create zones or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CreateZones.setter
    def CreateZones(self, createZones: bool):
        """
        Setter for property: (bool) CreateZones
         Returns the flag indicates to create zones or not.  
             
         
        """
        pass
    
    ## Getter for property: (float) HorizontalSize
    ##  Returns the size of the horizontal zone.  
    ##    It must be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def HorizontalSize(self) -> float:
        """
        Getter for property: (float) HorizontalSize
         Returns the size of the horizontal zone.  
           It must be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) HorizontalSize

    ##  Returns the size of the horizontal zone.  
    ##    It must be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @HorizontalSize.setter
    def HorizontalSize(self, horizontalSize: float):
        """
        Setter for property: (float) HorizontalSize
         Returns the size of the horizontal zone.  
           It must be greater than zero.   
         
        """
        pass
    
    ## Getter for property: (int) LabelColor
    ##  Returns the color of the label(text).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return int
    @property
    def LabelColor(self) -> int:
        """
        Getter for property: (int) LabelColor
         Returns the color of the label(text).  
             
         
        """
        pass
    
    ## Setter for property: (int) LabelColor

    ##  Returns the color of the label(text).  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LabelColor.setter
    def LabelColor(self, labelColor: int):
        """
        Setter for property: (int) LabelColor
         Returns the color of the label(text).  
             
         
        """
        pass
    
    ## Getter for property: (int) LabelFont
    ##  Returns the font of the label(text).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return int
    @property
    def LabelFont(self) -> int:
        """
        Getter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    
    ## Setter for property: (int) LabelFont

    ##  Returns the font of the label(text).  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LabelFont.setter
    def LabelFont(self, labelFont: int):
        """
        Setter for property: (int) LabelFont
         Returns the font of the label(text).  
             
         
        """
        pass
    
    ## Getter for property: (float) LabelHeight
    ##  Returns the height of the label(text).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the height of the label(text).  
             
         
        """
        pass
    
    ## Setter for property: (float) LabelHeight

    ##  Returns the height of the label(text).  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LabelHeight.setter
    def LabelHeight(self, labelHeight: float):
        """
        Setter for property: (float) LabelHeight
         Returns the height of the label(text).  
             
         
        """
        pass
    
    ## Getter for property: (bool) LabelItalicized
    ##  Returns the flag indicates the label(text) is italic or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def LabelItalicized(self) -> bool:
        """
        Getter for property: (bool) LabelItalicized
         Returns the flag indicates the label(text) is italic or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) LabelItalicized

    ##  Returns the flag indicates the label(text) is italic or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LabelItalicized.setter
    def LabelItalicized(self, italic: bool):
        """
        Setter for property: (bool) LabelItalicized
         Returns the flag indicates the label(text) is italic or not.  
             
         
        """
        pass
    
    ## Getter for property: (int) LabelWidth
    ##  Returns the width of the label(text) like Regular, Bold.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return int
    @property
    def LabelWidth(self) -> int:
        """
        Getter for property: (int) LabelWidth
         Returns the width of the label(text) like Regular, Bold.  
             
         
        """
        pass
    
    ## Setter for property: (int) LabelWidth

    ##  Returns the width of the label(text) like Regular, Bold.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LabelWidth.setter
    def LabelWidth(self, labelWidth: int):
        """
        Setter for property: (int) LabelWidth
         Returns the width of the label(text) like Regular, Bold.  
             
         
        """
        pass
    
    ## Getter for property: (str) LabelsToSkip
    ##  Returns the characters to skip in label(text).  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def LabelsToSkip(self) -> str:
        """
        Getter for property: (str) LabelsToSkip
         Returns the characters to skip in label(text).  
             
         
        """
        pass
    
    ## Setter for property: (str) LabelsToSkip

    ##  Returns the characters to skip in label(text).  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LabelsToSkip.setter
    def LabelsToSkip(self, labelsToSkip: str):
        """
        Setter for property: (str) LabelsToSkip
         Returns the characters to skip in label(text).  
             
         
        """
        pass
    
    ## Getter for property: (float) MarkingHeight
    ##  Returns the height of the marking.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def MarkingHeight(self) -> float:
        """
        Getter for property: (float) MarkingHeight
         Returns the height of the marking.  
             
         
        """
        pass
    
    ## Setter for property: (float) MarkingHeight

    ##  Returns the height of the marking.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @MarkingHeight.setter
    def MarkingHeight(self, markingHeight: float):
        """
        Setter for property: (float) MarkingHeight
         Returns the height of the marking.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) MarkingLineColorWidth
    ##  Returns the color and width of marking line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def MarkingLineColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) MarkingLineColorWidth
         Returns the color and width of marking line.  
             
         
        """
        pass
    
    ## Getter for property: (@link ZoneOrigin NXOpen.Diagramming.ZoneOrigin@endlink) Origin
    ##  Returns the type of zone origin like TopLeft/BottomRight.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return ZoneOrigin
    @property
    def Origin(self) -> ZoneOrigin:
        """
        Getter for property: (@link ZoneOrigin NXOpen.Diagramming.ZoneOrigin@endlink) Origin
         Returns the type of zone origin like TopLeft/BottomRight.  
             
         
        """
        pass
    
    ## Setter for property: (@link ZoneOrigin NXOpen.Diagramming.ZoneOrigin@endlink) Origin

    ##  Returns the type of zone origin like TopLeft/BottomRight.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Origin.setter
    def Origin(self, origin: ZoneOrigin):
        """
        Setter for property: (@link ZoneOrigin NXOpen.Diagramming.ZoneOrigin@endlink) Origin
         Returns the type of zone origin like TopLeft/BottomRight.  
             
         
        """
        pass
    
    ## Getter for property: (float) VerticalSize
    ##  Returns the size of the vertical zone.  
    ##    It must be greater than zero.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def VerticalSize(self) -> float:
        """
        Getter for property: (float) VerticalSize
         Returns the size of the vertical zone.  
           It must be greater than zero.   
         
        """
        pass
    
    ## Setter for property: (float) VerticalSize

    ##  Returns the size of the vertical zone.  
    ##    It must be greater than zero.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @VerticalSize.setter
    def VerticalSize(self, verticalSize: float):
        """
        Setter for property: (float) VerticalSize
         Returns the size of the vertical zone.  
           It must be greater than zero.   
         
        """
        pass
    
##  Represents the Sheet class.  <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::SheetBuilder  NXOpen::Diagramming::SheetBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Sheet(BaseObject): 
    """ Represents the Sheet class. """


    ##  Logs a group and all its members to delete. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="group"> (@link Group NXOpen.Diagramming.Group@endlink) </param>
    def LogGroupToDelete(self, group: Group) -> None:
        """
         Logs a group and all its members to delete. 
        """
        pass
    
import NXOpen
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SmartDiagrammingManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ##  Creates a @link NXOpen::Diagramming::ReferenceGeometryBuilder NXOpen::Diagramming::ReferenceGeometryBuilder@endlink . 
    ##  @return builder (@link ReferenceGeometryBuilder NXOpen.Diagramming.ReferenceGeometryBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="referenceGeometry"> (@link ReferenceGeometry NXOpen.Diagramming.ReferenceGeometry@endlink)  @link NXOpen::Diagramming::ReferenceGeometry NXOpen::Diagramming::ReferenceGeometry@endlink  to be edited, if NULL then create a new one </param>
    def CreateReferenceGeometryBuilder(self, referenceGeometry: ReferenceGeometry) -> ReferenceGeometryBuilder:
        """
         Creates a @link NXOpen::Diagramming::ReferenceGeometryBuilder NXOpen::Diagramming::ReferenceGeometryBuilder@endlink . 
         @return builder (@link ReferenceGeometryBuilder NXOpen.Diagramming.ReferenceGeometryBuilder@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a TextStyleBuilder.
##      <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class TextStyleBuilder(NXOpen.TaggedObject): 
    """
    Represents a TextStyleBuilder.
    """


    ##  Represents the option @link NXOpen::Diagramming::TextStyleBuilder::TextAlignment NXOpen::Diagramming::TextStyleBuilder::TextAlignment@endlink 
    ##            for a @link NXOpen::Diagramming::TextStyleBuilder NXOpen::Diagramming::TextStyleBuilder@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item></list>
    class TextAlignmentType(Enum):
        """
        Members Include: <Left> <Center> <Right>
        """
        Left: int
        Center: int
        Right: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TextStyleBuilder.TextAlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the option 
    ##            for a @link NXOpen::Diagramming::TextStyleBuilder NXOpen::Diagramming::TextStyleBuilder@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## ResizeOutline</term><description> 
    ## </description> </item><item><term> 
    ## ShrinkText</term><description> 
    ## </description> </item></list>
    class TextAutoFitType(Enum):
        """
        Members Include: <NotSet> <ResizeOutline> <ShrinkText>
        """
        NotSet: int
        ResizeOutline: int
        ShrinkText: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TextStyleBuilder.TextAutoFitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the option 
    ##            for a @link NXOpen::Diagramming::TextStyleBuilder::TruncationMode NXOpen::Diagramming::TextStyleBuilder::TruncationMode@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Trim</term><description> 
    ## </description> </item><item><term> 
    ## Suffix</term><description> 
    ## </description> </item></list>
    class TruncationModes(Enum):
        """
        Members Include: <NotSet> <Trim> <Suffix>
        """
        NotSet: int
        Trim: int
        Suffix: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TextStyleBuilder.TruncationModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link TextStyleBuilder.TextAlignmentType NXOpen.Diagramming.TextStyleBuilder.TextAlignmentType@endlink) TextAlignment
    ##  Returns the text alignment of the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return TextStyleBuilder.TextAlignmentType
    @property
    def TextAlignment(self) -> TextStyleBuilder.TextAlignmentType:
        """
        Getter for property: (@link TextStyleBuilder.TextAlignmentType NXOpen.Diagramming.TextStyleBuilder.TextAlignmentType@endlink) TextAlignment
         Returns the text alignment of the annotation   
            
         
        """
        pass
    
    ## Setter for property: (@link TextStyleBuilder.TextAlignmentType NXOpen.Diagramming.TextStyleBuilder.TextAlignmentType@endlink) TextAlignment

    ##  Returns the text alignment of the annotation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TextAlignment.setter
    def TextAlignment(self, alignment: TextStyleBuilder.TextAlignmentType):
        """
        Setter for property: (@link TextStyleBuilder.TextAlignmentType NXOpen.Diagramming.TextStyleBuilder.TextAlignmentType@endlink) TextAlignment
         Returns the text alignment of the annotation   
            
         
        """
        pass
    
    ## Getter for property: (bool) TextAllowWrapping
    ##  Returns the text allow wrapping   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def TextAllowWrapping(self) -> bool:
        """
        Getter for property: (bool) TextAllowWrapping
         Returns the text allow wrapping   
            
         
        """
        pass
    
    ## Setter for property: (bool) TextAllowWrapping

    ##  Returns the text allow wrapping   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TextAllowWrapping.setter
    def TextAllowWrapping(self, allowWrapping: bool):
        """
        Setter for property: (bool) TextAllowWrapping
         Returns the text allow wrapping   
            
         
        """
        pass
    
    ## Getter for property: (@link TextStyleBuilder.TextAutoFitType NXOpen.Diagramming.TextStyleBuilder.TextAutoFitType@endlink) TextAutoFit
    ##  Returns the text auto fit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return TextStyleBuilder.TextAutoFitType
    @property
    def TextAutoFit(self) -> TextStyleBuilder.TextAutoFitType:
        """
        Getter for property: (@link TextStyleBuilder.TextAutoFitType NXOpen.Diagramming.TextStyleBuilder.TextAutoFitType@endlink) TextAutoFit
         Returns the text auto fit   
            
         
        """
        pass
    
    ## Setter for property: (@link TextStyleBuilder.TextAutoFitType NXOpen.Diagramming.TextStyleBuilder.TextAutoFitType@endlink) TextAutoFit

    ##  Returns the text auto fit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TextAutoFit.setter
    def TextAutoFit(self, autoFit: TextStyleBuilder.TextAutoFitType):
        """
        Setter for property: (@link TextStyleBuilder.TextAutoFitType NXOpen.Diagramming.TextStyleBuilder.TextAutoFitType@endlink) TextAutoFit
         Returns the text auto fit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextColorFontWidth
    ##  Returns the text color font width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextColorFontWidth(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextColorFontWidth
         Returns the text color font width   
            
         
        """
        pass
    
    ## Getter for property: (float) TextHeight
    ##  Returns the height of the annotation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def TextHeight(self) -> float:
        """
        Getter for property: (float) TextHeight
         Returns the height of the annotation   
            
         
        """
        pass
    
    ## Setter for property: (float) TextHeight

    ##  Returns the height of the annotation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TextHeight.setter
    def TextHeight(self, height: float):
        """
        Setter for property: (float) TextHeight
         Returns the height of the annotation   
            
         
        """
        pass
    
    ## Getter for property: (bool) TextOverlined
    ##  Returns whether the text is overlined   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def TextOverlined(self) -> bool:
        """
        Getter for property: (bool) TextOverlined
         Returns whether the text is overlined   
            
         
        """
        pass
    
    ## Setter for property: (bool) TextOverlined

    ##  Returns whether the text is overlined   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TextOverlined.setter
    def TextOverlined(self, overlined: bool):
        """
        Setter for property: (bool) TextOverlined
         Returns whether the text is overlined   
            
         
        """
        pass
    
    ## Getter for property: (bool) TextUnderlined
    ##  Returns whether the text is underlined   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def TextUnderlined(self) -> bool:
        """
        Getter for property: (bool) TextUnderlined
         Returns whether the text is underlined   
            
         
        """
        pass
    
    ## Setter for property: (bool) TextUnderlined

    ##  Returns whether the text is underlined   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @TextUnderlined.setter
    def TextUnderlined(self, underlined: bool):
        """
        Setter for property: (bool) TextUnderlined
         Returns whether the text is underlined   
            
         
        """
        pass
    
    ## Getter for property: (@link TextStyleBuilder.TruncationModes NXOpen.Diagramming.TextStyleBuilder.TruncationModes@endlink) TruncationMode
    ##  Returns the text truncation mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TextStyleBuilder.TruncationModes
    @property
    def TruncationMode(self) -> TextStyleBuilder.TruncationModes:
        """
        Getter for property: (@link TextStyleBuilder.TruncationModes NXOpen.Diagramming.TextStyleBuilder.TruncationModes@endlink) TruncationMode
         Returns the text truncation mode   
            
         
        """
        pass
    
    ## Setter for property: (@link TextStyleBuilder.TruncationModes NXOpen.Diagramming.TextStyleBuilder.TruncationModes@endlink) TruncationMode

    ##  Returns the text truncation mode   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @TruncationMode.setter
    def TruncationMode(self, truncation: TextStyleBuilder.TruncationModes):
        """
        Setter for property: (@link TextStyleBuilder.TruncationModes NXOpen.Diagramming.TextStyleBuilder.TruncationModes@endlink) TruncationMode
         Returns the text truncation mode   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class TitleBlockCellBuilderList(NXOpen.TaggedObject): 
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
    ## <param name="objects"> (@link TitleBlockCellBuilder List[NXOpen.Diagramming.TitleBlockCellBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[TitleBlockCellBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: TitleBlockCellBuilder) -> None:
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
    ## <param name="obj"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: TitleBlockCellBuilder) -> None:
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
    ## <param name="obj"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: TitleBlockCellBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="obj"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: TitleBlockCellBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> TitleBlockCellBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link TitleBlockCellBuilder List[NXOpen.Diagramming.TitleBlockCellBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[TitleBlockCellBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link TitleBlockCellBuilder List[NXOpen.Diagramming.TitleBlockCellBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: TitleBlockCellBuilder) -> None:
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
    ## <param name="objects"> (@link TitleBlockCellBuilder List[NXOpen.Diagramming.TitleBlockCellBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[TitleBlockCellBuilder]) -> None:
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link TitleBlockCellBuilderList NXOpen.Diagramming.TitleBlockCellBuilderList@endlink) </param>
    ## <param name="object1"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link TitleBlockCellBuilder NXOpen.Diagramming.TitleBlockCellBuilder@endlink)  second item </param>
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
## 
##     Represents a builder to edit @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink 's cell 
##      <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class TitleBlockCellBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder to edit <ja_class>NXOpen.Diagramming.TitleBlock</ja_class>'s cell 
    """


    ## Getter for property: (str) Label
    ##  Returns the cell label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the cell label   
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##  Returns the cell label   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the cell label   
            
         
        """
        pass
    
    ## Getter for property: (bool) Lock
    ##  Returns the lock status   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def Lock(self) -> bool:
        """
        Getter for property: (bool) Lock
         Returns the lock status   
            
         
        """
        pass
    
    ## Setter for property: (bool) Lock

    ##  Returns the lock status   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Lock.setter
    def Lock(self, lockStatus: bool):
        """
        Setter for property: (bool) Lock
         Returns the lock status   
            
         
        """
        pass
    
    ## Getter for property: (str) Value
    ##  Returns the editable text of the cell   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the editable text of the cell   
            
         
        """
        pass
    
    ## Setter for property: (str) Value

    ##  Returns the editable text of the cell   
    ##     
    ##  
    ## Setter License requirements: drafting ("DRAFTING")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Value.setter
    def Value(self, text: str):
        """
        Setter for property: (str) Value
         Returns the editable text of the cell   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Title Block.  <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::DiagrammingManager  NXOpen::Diagramming::DiagrammingManager @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class TitleBlockCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Title Block. """


    ##  Creates a @link NXOpen::Diagramming::DefineTitleBlockBuilder NXOpen::Diagramming::DefineTitleBlockBuilder@endlink . 
    ##  @return builder (@link DefineTitleBlockBuilder NXOpen.Diagramming.DefineTitleBlockBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="titleBlock"> (@link TitleBlock NXOpen.Diagramming.TitleBlock@endlink)  @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink  to be edited, if NULL then create a new one </param>
    def CreateDefineTitleBlockBuilder(self, titleBlock: TitleBlock) -> DefineTitleBlockBuilder:
        """
         Creates a @link NXOpen::Diagramming::DefineTitleBlockBuilder NXOpen::Diagramming::DefineTitleBlockBuilder@endlink . 
         @return builder (@link DefineTitleBlockBuilder NXOpen.Diagramming.DefineTitleBlockBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Diagramming::PopulateTitleBlockBuilder NXOpen::Diagramming::PopulateTitleBlockBuilder@endlink . 
    ##  @return builder (@link PopulateTitleBlockBuilder NXOpen.Diagramming.PopulateTitleBlockBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="titleBlocks"> (@link TitleBlock List[NXOpen.Diagramming.TitleBlock]@endlink) </param>
    def CreatePopulateTitleBlockBuilder(self, titleBlocks: List[TitleBlock]) -> PopulateTitleBlockBuilder:
        """
         Creates a @link NXOpen::Diagramming::PopulateTitleBlockBuilder NXOpen::Diagramming::PopulateTitleBlockBuilder@endlink . 
         @return builder (@link PopulateTitleBlockBuilder NXOpen.Diagramming.PopulateTitleBlockBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return titleBlock (@link TitleBlock NXOpen.Diagramming.TitleBlock@endlink):  @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink  with this name. .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> TitleBlock:
        """
         Finds the @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return titleBlock (@link TitleBlock NXOpen.Diagramming.TitleBlock@endlink):  @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Diagramming::TitleBlock NXOpen::Diagramming::TitleBlock@endlink   <br> To create or edit an instance of this class, use @link NXOpen::Diagramming::DefineTitleBlockBuilder  NXOpen::Diagramming::DefineTitleBlockBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class TitleBlock(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.Diagramming.TitleBlock</ja_class> """
    pass


##  the trimming mark style type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Triangle</term><description> 
##  Triangle </description> </item><item><term> 
## Corner</term><description> 
## </description> </item></list>
class TrimmingMarkStyleType(Enum):
    """
    Members Include: <Triangle> <Corner>
    """
    Triangle: int
    Corner: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TrimmingMarkStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  the vertical centering mark type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  None </description> </item><item><term> 
## BottomArrow</term><description> 
##  Bottom Arrow </description> </item><item><term> 
## TopArrow</term><description> 
##  Top Arrow </description> </item><item><term> 
## BottomandTopArrow</term><description> 
##  Bottom and Top Arrow </description> </item><item><term> 
## BottomandTopLine</term><description> 
## </description> </item></list>
class VerticalCenteringMarkType(Enum):
    """
    Members Include: <NotSet> <BottomArrow> <TopArrow> <BottomandTopArrow> <BottomandTopLine>
    """
    NotSet: int
    BottomArrow: int
    TopArrow: int
    BottomandTopArrow: int
    BottomandTopLine: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> VerticalCenteringMarkType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
## 
##      View operations to be performed on a @link Diagramming::Sheet Diagramming::Sheet@endlink .
##      <br> To obtain an instance of this class, refer to @link NXOpen::Diagramming::SheetManager  NXOpen::Diagramming::SheetManager @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ViewOperations(NXOpen.Object): 
    """
     View operations to be performed on a <ja_class>Diagramming.Sheet</ja_class>.
    """


    ##  Fits the sheet 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def Fit(sheet: Sheet) -> None:
        """
         Fits the sheet 
        """
        pass
    
    ##  Fits the sheet to the given objects 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    ## <param name="elements"> (@link SheetElement List[NXOpen.Diagramming.SheetElement]@endlink)  The elements to be fit to </param>
    def FitToElements(sheet: Sheet, elements: List[SheetElement]) -> None:
        """
         Fits the sheet to the given objects 
        """
        pass
    
    ##  Fits the sheet to the currently selected objects 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    def FitToSelection(sheet: Sheet) -> None:
        """
         Fits the sheet to the currently selected objects 
        """
        pass
    
    ##  Zooms the sheet to a given scale 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    ## <param name="scale"> (float) </param>
    def Scale(sheet: Sheet, scale: float) -> None:
        """
         Zooms the sheet to a given scale 
        """
        pass
    
    ##  Pans the sheet to the given location 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="sheet"> (@link Sheet NXOpen.Diagramming.Sheet@endlink) </param>
    ## <param name="x"> (float) </param>
    ## <param name="y"> (float) </param>
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    def SetViewport(sheet: Sheet, x: float, y: float, width: float, height: float) -> None:
        """
         Pans the sheet to the given location 
        """
        pass
    
##  the zone origin 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## BottomRight</term><description> 
##  Bottom Right </description> </item><item><term> 
## TopLeft</term><description> 
##  Top Left </description> </item><item><term> 
## TopRight</term><description> 
##  Top Right </description> </item><item><term> 
## BottomLeft</term><description> 
## </description> </item></list>
class ZoneOrigin(Enum):
    """
    Members Include: <BottomRight> <TopLeft> <TopRight> <BottomLeft>
    """
    BottomRight: int
    TopLeft: int
    TopRight: int
    BottomLeft: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ZoneOrigin:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.Diagramming
## Classes, Enums and Structs under NXOpen.Diagramming namespace

##  @link AnnotationBuilderTextTypeOption NXOpen.Diagramming.AnnotationBuilderTextTypeOption @endlink is an alias for @link AnnotationBuilder.TextTypeOption NXOpen.Diagramming.AnnotationBuilder.TextTypeOption@endlink
AnnotationBuilderTextTypeOption = AnnotationBuilder.TextTypeOption


##  @link CannedAnnotationBuilderInheritOption NXOpen.Diagramming.CannedAnnotationBuilderInheritOption @endlink is an alias for @link CannedAnnotationBuilder.InheritOption NXOpen.Diagramming.CannedAnnotationBuilder.InheritOption@endlink
CannedAnnotationBuilderInheritOption = CannedAnnotationBuilder.InheritOption


##  @link ConnectionBuilderShapeOption NXOpen.Diagramming.ConnectionBuilderShapeOption @endlink is an alias for @link ConnectionBuilder.ShapeOption NXOpen.Diagramming.ConnectionBuilder.ShapeOption@endlink
ConnectionBuilderShapeOption = ConnectionBuilder.ShapeOption


##  @link LeaderLineBuilderVerticalAlignmentOption NXOpen.Diagramming.LeaderLineBuilderVerticalAlignmentOption @endlink is an alias for @link LeaderLineBuilder.VerticalAlignmentOption NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignmentOption@endlink
LeaderLineBuilderVerticalAlignmentOption = LeaderLineBuilder.VerticalAlignmentOption


##  @link RenderingPropertiesBuilderFillPatterns NXOpen.Diagramming.RenderingPropertiesBuilderFillPatterns @endlink is an alias for @link RenderingPropertiesBuilder.FillPatterns NXOpen.Diagramming.RenderingPropertiesBuilder.FillPatterns@endlink
RenderingPropertiesBuilderFillPatterns = RenderingPropertiesBuilder.FillPatterns


##  @link SheetBordersAndZonesBuilderArrowDirectionType NXOpen.Diagramming.SheetBordersAndZonesBuilderArrowDirectionType @endlink is an alias for @link SheetBordersAndZonesBuilder.ArrowDirectionType NXOpen.Diagramming.SheetBordersAndZonesBuilder.ArrowDirectionType@endlink
SheetBordersAndZonesBuilderArrowDirectionType = SheetBordersAndZonesBuilder.ArrowDirectionType


##  @link SheetBordersAndZonesBuilderArrowStyleType NXOpen.Diagramming.SheetBordersAndZonesBuilderArrowStyleType @endlink is an alias for @link SheetBordersAndZonesBuilder.ArrowStyleType NXOpen.Diagramming.SheetBordersAndZonesBuilder.ArrowStyleType@endlink
SheetBordersAndZonesBuilderArrowStyleType = SheetBordersAndZonesBuilder.ArrowStyleType


##  @link SheetBordersAndZonesBuilderHorizontalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilderHorizontalCenteringMarkType @endlink is an alias for @link SheetBordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.HorizontalCenteringMarkType@endlink
SheetBordersAndZonesBuilderHorizontalCenteringMarkType = SheetBordersAndZonesBuilder.HorizontalCenteringMarkType


##  @link SheetBordersAndZonesBuilderTrimmingMarkStyleType NXOpen.Diagramming.SheetBordersAndZonesBuilderTrimmingMarkStyleType @endlink is an alias for @link SheetBordersAndZonesBuilder.TrimmingMarkStyleType NXOpen.Diagramming.SheetBordersAndZonesBuilder.TrimmingMarkStyleType@endlink
SheetBordersAndZonesBuilderTrimmingMarkStyleType = SheetBordersAndZonesBuilder.TrimmingMarkStyleType


##  @link SheetBordersAndZonesBuilderVerticalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilderVerticalCenteringMarkType @endlink is an alias for @link SheetBordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.Diagramming.SheetBordersAndZonesBuilder.VerticalCenteringMarkType@endlink
SheetBordersAndZonesBuilderVerticalCenteringMarkType = SheetBordersAndZonesBuilder.VerticalCenteringMarkType


##  @link SheetBordersAndZonesBuilderZoneMethod NXOpen.Diagramming.SheetBordersAndZonesBuilderZoneMethod @endlink is an alias for @link SheetBordersAndZonesBuilder.ZoneMethod NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneMethod@endlink
SheetBordersAndZonesBuilderZoneMethod = SheetBordersAndZonesBuilder.ZoneMethod


##  @link SheetBordersAndZonesBuilderZoneOrigin NXOpen.Diagramming.SheetBordersAndZonesBuilderZoneOrigin @endlink is an alias for @link SheetBordersAndZonesBuilder.ZoneOrigin NXOpen.Diagramming.SheetBordersAndZonesBuilder.ZoneOrigin@endlink
SheetBordersAndZonesBuilderZoneOrigin = SheetBordersAndZonesBuilder.ZoneOrigin


##  @link SheetElementBuilderResizeOptionType NXOpen.Diagramming.SheetElementBuilderResizeOptionType @endlink is an alias for @link SheetElementBuilder.ResizeOptionType NXOpen.Diagramming.SheetElementBuilder.ResizeOptionType@endlink
SheetElementBuilderResizeOptionType = SheetElementBuilder.ResizeOptionType


##  @link TextStyleBuilderTextAlignmentType NXOpen.Diagramming.TextStyleBuilderTextAlignmentType @endlink is an alias for @link TextStyleBuilder.TextAlignmentType NXOpen.Diagramming.TextStyleBuilder.TextAlignmentType@endlink
TextStyleBuilderTextAlignmentType = TextStyleBuilder.TextAlignmentType


##  @link TextStyleBuilderTextAutoFitType NXOpen.Diagramming.TextStyleBuilderTextAutoFitType @endlink is an alias for @link TextStyleBuilder.TextAutoFitType NXOpen.Diagramming.TextStyleBuilder.TextAutoFitType@endlink
TextStyleBuilderTextAutoFitType = TextStyleBuilder.TextAutoFitType


##  @link TextStyleBuilderTruncationModes NXOpen.Diagramming.TextStyleBuilderTruncationModes @endlink is an alias for @link TextStyleBuilder.TruncationModes NXOpen.Diagramming.TextStyleBuilder.TruncationModes@endlink
TextStyleBuilderTruncationModes = TextStyleBuilder.TruncationModes


