from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## Class for creating pmi occ note <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAddPmiOccNoteBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAddPmiOccNoteBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AddPMIOccNoteBuilder(NXOpen.Builder): 
    """Class for creating pmi occ note"""


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ComponentSelection
    ##  Returns the component selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ComponentSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ComponentSelection
         Returns the component selection   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AddButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  Returns the note text 
    ##  @return noteText (List[str]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetNoteTextFromListBox(self) -> List[str]:
        """
         Returns the note text 
         @return noteText (List[str]): .
        """
        pass
    
    ##  Sets the note text 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="noteText"> (List[str])  </param>
    def SetNoteTextFromListBox(self, noteText: List[str]) -> None:
        """
         Sets the note text 
        """
        pass
    
import NXOpen
## Class for assignment of mapped type <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAddTypeAttributeBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAddTypeAttributeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Type </term> <description> 
##  
## Mfg0MEEqupment </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1938.0.0  <br> 

class AddTypeAttributeBuilder(NXOpen.Builder): 
    """Class for assignment of mapped type"""


    ##  This enum is providing possible mapped types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Mfg0MEEqupment</term><description> 
    ## </description> </item></list>
    class MappedType(Enum):
        """
        Members Include: <Mfg0MEEqupment>
        """
        Mfg0MEEqupment: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddTypeAttributeBuilder.MappedType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ComponentSelection
    ##  Returns the component selection   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def ComponentSelection(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ComponentSelection
         Returns the component selection   
            
         
        """
        pass
    
    ## Getter for property: (str) MappedTypeName
    ##  Returns the mapped type name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return str
    @property
    def MappedTypeName(self) -> str:
        """
        Getter for property: (str) MappedTypeName
         Returns the mapped type name   
            
         
        """
        pass
    
    ## Setter for property: (str) MappedTypeName

    ##  Returns the mapped type name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @MappedTypeName.setter
    def MappedTypeName(self, name: str):
        """
        Setter for property: (str) MappedTypeName
         Returns the mapped type name   
            
         
        """
        pass
    
    ## Getter for property: (@link AddTypeAttributeBuilder.MappedType NXOpen.LineDesigner.AddTypeAttributeBuilder.MappedType@endlink) Type
    ##  Returns the mapped type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return AddTypeAttributeBuilder.MappedType
    @property
    def Type(self) -> AddTypeAttributeBuilder.MappedType:
        """
        Getter for property: (@link AddTypeAttributeBuilder.MappedType NXOpen.LineDesigner.AddTypeAttributeBuilder.MappedType@endlink) Type
         Returns the mapped type   
            
         
        """
        pass
    
    ## Setter for property: (@link AddTypeAttributeBuilder.MappedType NXOpen.LineDesigner.AddTypeAttributeBuilder.MappedType@endlink) Type

    ##  Returns the mapped type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @Type.setter
    def Type(self, type: AddTypeAttributeBuilder.MappedType):
        """
        Setter for property: (@link AddTypeAttributeBuilder.MappedType NXOpen.LineDesigner.AddTypeAttributeBuilder.MappedType@endlink) Type
         Returns the mapped type   
            
         
        """
        pass
    
import NXOpen
##  use for creating workarea builder <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAddWorkareaBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAddWorkareaBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class AddWorkareaBuilder(NXOpen.Builder): 
    """ use for creating workarea builder"""


    ## Getter for property: (str) Name
    ##  Returns the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Getter for property: (str) ParentName
    ##  Returns the parentName   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ParentName(self) -> str:
        """
        Getter for property: (str) ParentName
         Returns the parentName   
            
         
        """
        pass
    
    ## Setter for property: (str) ParentName

    ##  Returns the parentName   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ParentName.setter
    def ParentName(self, parentName: str):
        """
        Setter for property: (str) ParentName
         Returns the parentName   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
    ##  Returns an API that gets parent tag  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ParentPartOccurance(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance

    ##  Returns an API that gets parent tag  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ParentPartOccurance.setter
    def ParentPartOccurance(self, parent: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    
    ## Getter for property: (str) WorkareaTypeName
    ##  Returns the type of workarea   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def WorkareaTypeName(self) -> str:
        """
        Getter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    
    ## Setter for property: (str) WorkareaTypeName

    ##  Returns the type of workarea   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @WorkareaTypeName.setter
    def WorkareaTypeName(self, workareaType: str):
        """
        Setter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    
    ##  Returns workareaTypes allow children type 
    ##  @return childrenType (List[str]):  This specifies allow workarea type.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="internalName"> (str) </param>
    def GetAllowChildTypeForParent(self, internalName: str) -> List[str]:
        """
         Returns workareaTypes allow children type 
         @return childrenType (List[str]):  This specifies allow workarea type.
        """
        pass
    
    ##  Returns unique workarea name for creation 
    ##  @return workareaDefaultName (str): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetDefaultName(self) -> str:
        """
         Returns unique workarea name for creation 
         @return workareaDefaultName (str): .
        """
        pass
    
    ##  Returns workareaTypes from pax file 
    ##  @return workAreaType (List[str]): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetWorkAreaTypeByParsingPaxFile(self) -> List[str]:
        """
         Returns workareaTypes from pax file 
         @return workAreaType (List[str]): .
        """
        pass
    
    ##  Set Expression internal name  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="displayName"> (str)  </param>
    ## <param name="internalName"> (str) </param>
    def SetInternalName(self, displayName: str, internalName: str) -> None:
        """
         Set Expression internal name  
        """
        pass
    
import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAlignComponentsBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAlignComponentsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Reference </term> <description> 
##  
## AbsoluteinDisplayedPart </description> </item> 
## 
## <item><term> 
##  
## SelectDirectionOption </term> <description> 
##  
## X </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.1  <br> 

class AlignComponentsBuilder(NXOpen.Builder): 
    """  """


    ##  This enum is providing selection of reference to align
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AbsoluteinDisplayedPart</term><description> 
    ## </description> </item><item><term> 
    ## Wcs</term><description> 
    ## </description> </item></list>
    class ReferenceValues(Enum):
        """
        Members Include: <AbsoluteinDisplayedPart> <Wcs>
        """
        AbsoluteinDisplayedPart: int
        Wcs: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignComponentsBuilder.ReferenceValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing selection of direction in to align
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item><item><term> 
    ## UserDefinedDirection</term><description> 
    ## </description> </item></list>
    class SelectDirectionOptionEnum(Enum):
        """
        Members Include: <X> <Y> <Z> <UserDefinedDirection>
        """
        X: int
        Y: int
        Z: int
        UserDefinedDirection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignComponentsBuilder.SelectDirectionOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ComponentToAlignTo
    ##  Returns the component to align to   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def ComponentToAlignTo(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ComponentToAlignTo
         Returns the component to align to   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ComponentsToAlign
    ##  Returns the components to align   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ComponentsToAlign(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ComponentsToAlign
         Returns the components to align   
            
         
        """
        pass
    
    ## Getter for property: (@link AlignComponentsBuilder.ReferenceValues NXOpen.LineDesigner.AlignComponentsBuilder.ReferenceValues@endlink) Reference
    ##  Returns the reference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return AlignComponentsBuilder.ReferenceValues
    @property
    def Reference(self) -> AlignComponentsBuilder.ReferenceValues:
        """
        Getter for property: (@link AlignComponentsBuilder.ReferenceValues NXOpen.LineDesigner.AlignComponentsBuilder.ReferenceValues@endlink) Reference
         Returns the reference   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignComponentsBuilder.ReferenceValues NXOpen.LineDesigner.AlignComponentsBuilder.ReferenceValues@endlink) Reference

    ##  Returns the reference   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @Reference.setter
    def Reference(self, reference: AlignComponentsBuilder.ReferenceValues):
        """
        Setter for property: (@link AlignComponentsBuilder.ReferenceValues NXOpen.LineDesigner.AlignComponentsBuilder.ReferenceValues@endlink) Reference
         Returns the reference   
            
         
        """
        pass
    
    ## Getter for property: (@link AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.LineDesigner.AlignComponentsBuilder.SelectDirectionOptionEnum@endlink) SelectDirectionOption
    ##  Returns the component origin direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return AlignComponentsBuilder.SelectDirectionOptionEnum
    @property
    def SelectDirectionOption(self) -> AlignComponentsBuilder.SelectDirectionOptionEnum:
        """
        Getter for property: (@link AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.LineDesigner.AlignComponentsBuilder.SelectDirectionOptionEnum@endlink) SelectDirectionOption
         Returns the component origin direction   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.LineDesigner.AlignComponentsBuilder.SelectDirectionOptionEnum@endlink) SelectDirectionOption

    ##  Returns the component origin direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @SelectDirectionOption.setter
    def SelectDirectionOption(self, selectDirectionOption: AlignComponentsBuilder.SelectDirectionOptionEnum):
        """
        Setter for property: (@link AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.LineDesigner.AlignComponentsBuilder.SelectDirectionOptionEnum@endlink) SelectDirectionOption
         Returns the component origin direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection
    ##  Returns the specify direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def SpecifyDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection

    ##  Returns the specify direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @SpecifyDirection.setter
    def SpecifyDirection(self, specifyDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
    
import NXOpen
##   <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAllowWorkareaTypesBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAllowWorkareaTypesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class AllowWorkareaTypesBuilder(NXOpen.Builder): 
    """ """


    ##  This button is for adding entry from preference xml file 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AddButton(self) -> None:
        """
         This button is for adding entry from preference xml file 
        """
        pass
    
    ##  This button is for deleting entry from preference xml file 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def DeleteButton(self) -> None:
        """
         This button is for deleting entry from preference xml file 
        """
        pass
    
    ##  This button is for editing entry from preference xml file 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def EditButton(self) -> None:
        """
         This button is for editing entry from preference xml file 
        """
        pass
    
    ##  This button is to restore data from preference xml file 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def RestoreButton(self) -> None:
        """
         This button is to restore data from preference xml file 
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a @link LineDesigner::ColumnFeature LineDesigner::ColumnFeature@endlink  Features.FeatureBuilder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateColumnFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateColumnFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BaseDepth.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BaseDiameter.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BaseHeight.Value </term> <description> 
##  
## 900 (millimeters part), 35 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BaseLowerDiameter.Value </term> <description> 
##  
## 900 (millimeters part), 35 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BaseStyleEnum </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## BaseUpperDiameter.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BaseWidth.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnDepth.Value </term> <description> 
##  
## 600 (millimeters part), 25 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnDiameter.Value </term> <description> 
##  
## 300 (millimeters part), 12 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnHeight.Value </term> <description> 
##  
## 3000 (millimeters part), 120 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnStyleEnum </term> <description> 
##  
## IBeam </description> </item> 
## 
## <item><term> 
##  
## ColumnThickness.Value </term> <description> 
##  
## 30 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnWidth.Value </term> <description> 
##  
## 600 (millimeters part), 25 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ColumnFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>LineDesigner.ColumnFeature</ja_class> Features.FeatureBuilder
    """


    ##  This enum is providing possible column base types   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## Cone</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class ColumnBaseType(Enum):
        """
        Members Include: <NotSet> <Rectangle> <Circle> <Cone> <UserDefined>
        """
        NotSet: int
        Rectangle: int
        Circle: int
        Cone: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnFeatureBuilder.ColumnBaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible column types    
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IBeam</term><description> 
    ## </description> </item><item><term> 
    ## TBeam</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## UserDefine</term><description> 
    ## </description> </item></list>
    class ColumnType(Enum):
        """
        Members Include: <IBeam> <TBeam> <Rectangle> <Circle> <UserDefine>
        """
        IBeam: int
        TBeam: int
        Rectangle: int
        Circle: int
        UserDefine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnFeatureBuilder.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseDepth
    ##  Returns the base depth of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseDepth
         Returns the base depth of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseDiameter
    ##  Returns the base diameter of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseDiameter
         Returns the base diameter of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseHeight
    ##  Returns the base height of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseHeight
         Returns the base height of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseLowerDiameter
    ##  Returns the base lower diameter of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseLowerDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseLowerDiameter
         Returns the base lower diameter of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link ColumnFeatureBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnBaseType@endlink) BaseStyleEnum
    ##  Returns the base cross section type of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ColumnFeatureBuilder.ColumnBaseType
    @property
    def BaseStyleEnum(self) -> ColumnFeatureBuilder.ColumnBaseType:
        """
        Getter for property: (@link ColumnFeatureBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnBaseType@endlink) BaseStyleEnum
         Returns the base cross section type of column feature   
            
         
        """
        pass
    
    ## Setter for property: (@link ColumnFeatureBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnBaseType@endlink) BaseStyleEnum

    ##  Returns the base cross section type of column feature   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BaseStyleEnum.setter
    def BaseStyleEnum(self, baseStyleEnum: ColumnFeatureBuilder.ColumnBaseType):
        """
        Setter for property: (@link ColumnFeatureBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnBaseType@endlink) BaseStyleEnum
         Returns the base cross section type of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseUpperDiameter
    ##  Returns the base upper diameter of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseUpperDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseUpperDiameter
         Returns the base upper diameter of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BaseUserDefineSuperSection
    ##  Returns the user define cross section for base of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def BaseUserDefineSuperSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BaseUserDefineSuperSection
         Returns the user define cross section for base of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseWidth
    ##  Returns the base width of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BaseWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BaseWidth
         Returns the base width of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDepth
    ##  Returns the column depth of column feature    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDepth
         Returns the column depth of column feature    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDiameter
    ##  Returns the column diameter of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDiameter
         Returns the column diameter of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnHeight
    ##  Returns the column height of column feature    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnHeight
         Returns the column height of column feature    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ColumnOriginPoint
    ##  Returns the column origin point is returns where colums is created  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def ColumnOriginPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ColumnOriginPoint
         Returns the column origin point is returns where colums is created  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ColumnOriginPoint

    ##  Returns the column origin point is returns where colums is created  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnOriginPoint.setter
    def ColumnOriginPoint(self, columnOriginPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ColumnOriginPoint
         Returns the column origin point is returns where colums is created  
            
         
        """
        pass
    
    ## Getter for property: (@link ColumnFeatureBuilder.ColumnType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnType@endlink) ColumnStyleEnum
    ##  Returns the column style of column feature    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ColumnFeatureBuilder.ColumnType
    @property
    def ColumnStyleEnum(self) -> ColumnFeatureBuilder.ColumnType:
        """
        Getter for property: (@link ColumnFeatureBuilder.ColumnType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnType@endlink) ColumnStyleEnum
         Returns the column style of column feature    
            
         
        """
        pass
    
    ## Setter for property: (@link ColumnFeatureBuilder.ColumnType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnType@endlink) ColumnStyleEnum

    ##  Returns the column style of column feature    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnStyleEnum.setter
    def ColumnStyleEnum(self, columnStyleEnum: ColumnFeatureBuilder.ColumnType):
        """
        Setter for property: (@link ColumnFeatureBuilder.ColumnType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnType@endlink) ColumnStyleEnum
         Returns the column style of column feature    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnThickness
    ##  Returns the column thickness of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnThickness
         Returns the column thickness of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ColumnUserDefineSuperSection
    ##  Returns the user defined cross section of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def ColumnUserDefineSuperSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ColumnUserDefineSuperSection
         Returns the user defined cross section of column feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnWidth
    ##  Returns the column width  of column feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnWidth
         Returns the column width  of column feature   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a column feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::ColumnFeatureBuilder  NXOpen::LineDesigner::ColumnFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ColumnFeature(NXOpen.Features.Feature): 
    """ Represents a column feature feature """
    pass


import NXOpen
## 
##     Represents a LineDesigner.ColumnGridEquipment builder
## 
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateColumnGridEquipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateColumnGridEquipmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BubbleDiameter </term> <description> 
##  
## 1200 </description> </item> 
## 
## <item><term> 
##  
## BubbleExtension </term> <description> 
##  
## 750 </description> </item> 
## 
## <item><term> 
##  
## BubbleExtensionOffset </term> <description> 
##  
## 400 </description> </item> 
## 
## <item><term> 
##  
## BubbleLeader </term> <description> 
##  
## 750 </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseDepth.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseDiameter.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseHeight.Value </term> <description> 
##  
## 900 (millimeters part), 35 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseLowerDiameter.Value </term> <description> 
##  
## 900 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseTypeEnum </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseUpperDiameter.Value </term> <description> 
##  
## 800 (millimeters part), 32 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnBaseWidth.Value </term> <description> 
##  
## 800 (millimeters part), 35 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnDepth.Value </term> <description> 
##  
## 600 (millimeters part), 25 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnDiameter.Value </term> <description> 
##  
## 800 (millimeters part), 25 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnDisplayIDs </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ColumnElevation.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnHeight.Value </term> <description> 
##  
## 3000 (millimeters part), 120 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnRotate90Degrees </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ColumnSpacingDouble </term> <description> 
##  
## 15000 </description> </item> 
## 
## <item><term> 
##  
## ColumnThickness.Value </term> <description> 
##  
## 30 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ColumnTypeEnum </term> <description> 
##  
## IBeam </description> </item> 
## 
## <item><term> 
##  
## ColumnWideNumber </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ColumnWidth.Value </term> <description> 
##  
## 600 (millimeters part), 12 (inches part) </description> </item> 
## 
## <item><term> 
##  
## CreateBottomBubblesToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CreateLeftBubblesToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CreateRightBubblesToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CreateTopBubblesToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DefineGlobalSizeToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayGridToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## RowDeepNumber </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## RowSpacingDouble </term> <description> 
##  
## 15000 </description> </item> 
## 
## <item><term> 
##  
## SelectGridArea.AllowRotation </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## UseSpacingToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ColumnGridEquipmentBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.ColumnGridEquipment builder

    """


    ##  This enum is providing possible column base types   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## Cone</term><description> 
    ## </description> </item><item><term> 
    ## UserDefine</term><description> 
    ## </description> </item></list>
    class ColumnBaseType(Enum):
        """
        Members Include: <NotSet> <Rectangle> <Circle> <Cone> <UserDefine>
        """
        NotSet: int
        Rectangle: int
        Circle: int
        Cone: int
        UserDefine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnGridEquipmentBuilder.ColumnBaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible column types    
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IBeam</term><description> 
    ## </description> </item><item><term> 
    ## TBeam</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## UserDefine</term><description> 
    ## </description> </item></list>
    class ColumnType(Enum):
        """
        Members Include: <IBeam> <TBeam> <Rectangle> <Circle> <UserDefine>
        """
        IBeam: int
        TBeam: int
        Rectangle: int
        Circle: int
        UserDefine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnGridEquipmentBuilder.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) BubbleDiameter
    ##  Returns the value of bubble diameter in column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def BubbleDiameter(self) -> float:
        """
        Getter for property: (float) BubbleDiameter
         Returns the value of bubble diameter in column grid   
            
         
        """
        pass
    
    ## Setter for property: (float) BubbleDiameter

    ##  Returns the value of bubble diameter in column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BubbleDiameter.setter
    def BubbleDiameter(self, bubbleDiameter: float):
        """
        Setter for property: (float) BubbleDiameter
         Returns the value of bubble diameter in column grid   
            
         
        """
        pass
    
    ## Getter for property: (float) BubbleExtension
    ##  Returns the value of bubble extension of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def BubbleExtension(self) -> float:
        """
        Getter for property: (float) BubbleExtension
         Returns the value of bubble extension of column grid   
            
         
        """
        pass
    
    ## Setter for property: (float) BubbleExtension

    ##  Returns the value of bubble extension of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BubbleExtension.setter
    def BubbleExtension(self, bubbleExtension: float):
        """
        Setter for property: (float) BubbleExtension
         Returns the value of bubble extension of column grid   
            
         
        """
        pass
    
    ## Getter for property: (float) BubbleExtensionOffset
    ##  Returns the bubble extension offset value of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def BubbleExtensionOffset(self) -> float:
        """
        Getter for property: (float) BubbleExtensionOffset
         Returns the bubble extension offset value of column grid   
            
         
        """
        pass
    
    ## Setter for property: (float) BubbleExtensionOffset

    ##  Returns the bubble extension offset value of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BubbleExtensionOffset.setter
    def BubbleExtensionOffset(self, bubbleExtensionOffset: float):
        """
        Setter for property: (float) BubbleExtensionOffset
         Returns the bubble extension offset value of column grid   
            
         
        """
        pass
    
    ## Getter for property: (float) BubbleLeader
    ##  Returns the bubble leader   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def BubbleLeader(self) -> float:
        """
        Getter for property: (float) BubbleLeader
         Returns the bubble leader   
            
         
        """
        pass
    
    ## Setter for property: (float) BubbleLeader

    ##  Returns the bubble leader   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BubbleLeader.setter
    def BubbleLeader(self, bubbleLeader: float):
        """
        Setter for property: (float) BubbleLeader
         Returns the bubble leader   
            
         
        """
        pass
    
    ## Getter for property: (str) BubblesUnallowedChars
    ##  Returns the bubbles unallowed characters in column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def BubblesUnallowedChars(self) -> str:
        """
        Getter for property: (str) BubblesUnallowedChars
         Returns the bubbles unallowed characters in column grid   
            
         
        """
        pass
    
    ## Setter for property: (str) BubblesUnallowedChars

    ##  Returns the bubbles unallowed characters in column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BubblesUnallowedChars.setter
    def BubblesUnallowedChars(self, bubblesUnallowedChars: str):
        """
        Setter for property: (str) BubblesUnallowedChars
         Returns the bubbles unallowed characters in column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ColumnBaseCrossSection
    ##  Returns the column base cross section of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def ColumnBaseCrossSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ColumnBaseCrossSection
         Returns the column base cross section of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseDepth
    ##  Returns the column base depth of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnBaseDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseDepth
         Returns the column base depth of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseDiameter
    ##  Returns the column base diameter of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnBaseDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseDiameter
         Returns the column base diameter of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseHeight
    ##  Returns the column base height of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnBaseHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseHeight
         Returns the column base height of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseLowerDiameter
    ##  Returnsthe column base lower diameter of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnBaseLowerDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseLowerDiameter
         Returnsthe column base lower diameter of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnBaseType@endlink) ColumnBaseTypeEnum
    ##  Returns the column base type of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ColumnGridEquipmentBuilder.ColumnBaseType
    @property
    def ColumnBaseTypeEnum(self) -> ColumnGridEquipmentBuilder.ColumnBaseType:
        """
        Getter for property: (@link ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnBaseType@endlink) ColumnBaseTypeEnum
         Returns the column base type of column grid   
            
         
        """
        pass
    
    ## Setter for property: (@link ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnBaseType@endlink) ColumnBaseTypeEnum

    ##  Returns the column base type of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnBaseTypeEnum.setter
    def ColumnBaseTypeEnum(self, columnBaseTypeEnum: ColumnGridEquipmentBuilder.ColumnBaseType):
        """
        Setter for property: (@link ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnBaseType@endlink) ColumnBaseTypeEnum
         Returns the column base type of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseUpperDiameter
    ##  Returns the column base upper diameter of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnBaseUpperDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseUpperDiameter
         Returns the column base upper diameter of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseWidth
    ##  Returns the column base width of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnBaseWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnBaseWidth
         Returns the column base width of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ColumnCrossSection
    ##  Returns the column cross section of columns of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def ColumnCrossSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) ColumnCrossSection
         Returns the column cross section of columns of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObjectList NXOpen.NXObjectList@endlink) ColumnDataList
    ##  Returns the column data list   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXObjectList
    @property
    def ColumnDataList(self) -> NXOpen.NXObjectList:
        """
        Getter for property: (@link NXOpen.NXObjectList NXOpen.NXObjectList@endlink) ColumnDataList
         Returns the column data list   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDepth
    ##  Returns the column depth of column grid    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDepth
         Returns the column depth of column grid    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDiameter
    ##  Returnsthe column diameter of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnDiameter
         Returnsthe column diameter of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) ColumnDisplayIDs
    ##  Returns the status of column display ids in column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ColumnDisplayIDs(self) -> bool:
        """
        Getter for property: (bool) ColumnDisplayIDs
         Returns the status of column display ids in column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) ColumnDisplayIDs

    ##  Returns the status of column display ids in column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnDisplayIDs.setter
    def ColumnDisplayIDs(self, columnDisplayIDs: bool):
        """
        Setter for property: (bool) ColumnDisplayIDs
         Returns the status of column display ids in column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnElevation
    ##  Returns the column elevation of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnElevation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnElevation
         Returns the column elevation of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnHeight
    ##  Returns the column height of columns of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnHeight
         Returns the column height of columns of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) ColumnRotate90Degrees
    ##  Returns the status of 90 degree column rotation for column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ColumnRotate90Degrees(self) -> bool:
        """
        Getter for property: (bool) ColumnRotate90Degrees
         Returns the status of 90 degree column rotation for column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) ColumnRotate90Degrees

    ##  Returns the status of 90 degree column rotation for column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnRotate90Degrees.setter
    def ColumnRotate90Degrees(self, columnRotate90Degrees: bool):
        """
        Setter for property: (bool) ColumnRotate90Degrees
         Returns the status of 90 degree column rotation for column grid   
            
         
        """
        pass
    
    ## Getter for property: (float) ColumnSpacingDouble
    ##  Returns the spacing between columns   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def ColumnSpacingDouble(self) -> float:
        """
        Getter for property: (float) ColumnSpacingDouble
         Returns the spacing between columns   
            
         
        """
        pass
    
    ## Setter for property: (float) ColumnSpacingDouble

    ##  Returns the spacing between columns   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnSpacingDouble.setter
    def ColumnSpacingDouble(self, columnSpacingDouble: float):
        """
        Setter for property: (float) ColumnSpacingDouble
         Returns the spacing between columns   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnThickness
    ##  Returns the column thickness of coulmn grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnThickness
         Returns the column thickness of coulmn grid   
            
         
        """
        pass
    
    ## Getter for property: (@link ColumnGridEquipmentBuilder.ColumnType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnType@endlink) ColumnTypeEnum
    ##  Returns the column type of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ColumnGridEquipmentBuilder.ColumnType
    @property
    def ColumnTypeEnum(self) -> ColumnGridEquipmentBuilder.ColumnType:
        """
        Getter for property: (@link ColumnGridEquipmentBuilder.ColumnType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnType@endlink) ColumnTypeEnum
         Returns the column type of column grid   
            
         
        """
        pass
    
    ## Setter for property: (@link ColumnGridEquipmentBuilder.ColumnType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnType@endlink) ColumnTypeEnum

    ##  Returns the column type of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnTypeEnum.setter
    def ColumnTypeEnum(self, columnTypeEnum: ColumnGridEquipmentBuilder.ColumnType):
        """
        Setter for property: (@link ColumnGridEquipmentBuilder.ColumnType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnType@endlink) ColumnTypeEnum
         Returns the column type of column grid   
            
         
        """
        pass
    
    ## Getter for property: (int) ColumnWideNumber
    ##  Returns the number of column of columns in column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ColumnWideNumber(self) -> int:
        """
        Getter for property: (int) ColumnWideNumber
         Returns the number of column of columns in column grid   
            
         
        """
        pass
    
    ## Setter for property: (int) ColumnWideNumber

    ##  Returns the number of column of columns in column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColumnWideNumber.setter
    def ColumnWideNumber(self, columnWideNumber: int):
        """
        Setter for property: (int) ColumnWideNumber
         Returns the number of column of columns in column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnWidth
    ##  Returns the column width of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ColumnWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ColumnWidth
         Returns the column width of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateBottomBubblesToggle
    ##  Returns the status to create bottom bubbles of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CreateBottomBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateBottomBubblesToggle
         Returns the status to create bottom bubbles of column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateBottomBubblesToggle

    ##  Returns the status to create bottom bubbles of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CreateBottomBubblesToggle.setter
    def CreateBottomBubblesToggle(self, createBottomBubblesToggle: bool):
        """
        Setter for property: (bool) CreateBottomBubblesToggle
         Returns the status to create bottom bubbles of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateLeftBubblesToggle
    ##  Returns the status to create left bubbles of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CreateLeftBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateLeftBubblesToggle
         Returns the status to create left bubbles of column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateLeftBubblesToggle

    ##  Returns the status to create left bubbles of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CreateLeftBubblesToggle.setter
    def CreateLeftBubblesToggle(self, createLeftBubblesToggle: bool):
        """
        Setter for property: (bool) CreateLeftBubblesToggle
         Returns the status to create left bubbles of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateRightBubblesToggle
    ##  Returns the status to create right bubbles of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CreateRightBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateRightBubblesToggle
         Returns the status to create right bubbles of column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateRightBubblesToggle

    ##  Returns the status to create right bubbles of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CreateRightBubblesToggle.setter
    def CreateRightBubblesToggle(self, createRightBubblesToggle: bool):
        """
        Setter for property: (bool) CreateRightBubblesToggle
         Returns the status to create right bubbles of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateTopBubblesToggle
    ##  Returns the status to create top bubbles in column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def CreateTopBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateTopBubblesToggle
         Returns the status to create top bubbles in column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateTopBubblesToggle

    ##  Returns the status to create top bubbles in column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CreateTopBubblesToggle.setter
    def CreateTopBubblesToggle(self, createTopBubblesToggle: bool):
        """
        Setter for property: (bool) CreateTopBubblesToggle
         Returns the status to create top bubbles in column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefineGlobalSizeToggle
    ##  Returns the define global size toggle of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def DefineGlobalSizeToggle(self) -> bool:
        """
        Getter for property: (bool) DefineGlobalSizeToggle
         Returns the define global size toggle of column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefineGlobalSizeToggle

    ##  Returns the define global size toggle of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DefineGlobalSizeToggle.setter
    def DefineGlobalSizeToggle(self, defineGlobalSizeToggle: bool):
        """
        Setter for property: (bool) DefineGlobalSizeToggle
         Returns the define global size toggle of column grid   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayGridToggle
    ##  Returns the display grid status of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def DisplayGridToggle(self) -> bool:
        """
        Getter for property: (bool) DisplayGridToggle
         Returns the display grid status of column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayGridToggle

    ##  Returns the display grid status of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DisplayGridToggle.setter
    def DisplayGridToggle(self, displayGridToggle: bool):
        """
        Setter for property: (bool) DisplayGridToggle
         Returns the display grid status of column grid   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
    ##  Returns the kf object   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.KFObject
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
         Returns the kf object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObjectList NXOpen.NXObjectList@endlink) RowDataList
    ##  Returns the row data list   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXObjectList
    @property
    def RowDataList(self) -> NXOpen.NXObjectList:
        """
        Getter for property: (@link NXOpen.NXObjectList NXOpen.NXObjectList@endlink) RowDataList
         Returns the row data list   
            
         
        """
        pass
    
    ## Getter for property: (int) RowDeepNumber
    ##  Returns the number of rows of columns in column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def RowDeepNumber(self) -> int:
        """
        Getter for property: (int) RowDeepNumber
         Returns the number of rows of columns in column grid   
            
         
        """
        pass
    
    ## Setter for property: (int) RowDeepNumber

    ##  Returns the number of rows of columns in column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @RowDeepNumber.setter
    def RowDeepNumber(self, rowDeepNumber: int):
        """
        Setter for property: (int) RowDeepNumber
         Returns the number of rows of columns in column grid   
            
         
        """
        pass
    
    ## Getter for property: (float) RowSpacingDouble
    ##  Returns the value of row spacing between columns  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def RowSpacingDouble(self) -> float:
        """
        Getter for property: (float) RowSpacingDouble
         Returns the value of row spacing between columns  
            
         
        """
        pass
    
    ## Setter for property: (float) RowSpacingDouble

    ##  Returns the value of row spacing between columns  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @RowSpacingDouble.setter
    def RowSpacingDouble(self, rowSpacingDouble: float):
        """
        Setter for property: (float) RowSpacingDouble
         Returns the value of row spacing between columns  
            
         
        """
        pass
    
    ## Getter for property: (@link PickRectanglePointsBuilder NXOpen.LineDesigner.PickRectanglePointsBuilder@endlink) SelectGridArea
    ##  Returns the selected grid area of column grid  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PickRectanglePointsBuilder
    @property
    def SelectGridArea(self) -> PickRectanglePointsBuilder:
        """
        Getter for property: (@link PickRectanglePointsBuilder NXOpen.LineDesigner.PickRectanglePointsBuilder@endlink) SelectGridArea
         Returns the selected grid area of column grid  
            
         
        """
        pass
    
    ## Setter for property: (@link PickRectanglePointsBuilder NXOpen.LineDesigner.PickRectanglePointsBuilder@endlink) SelectGridArea

    ##  Returns the selected grid area of column grid  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SelectGridArea.setter
    def SelectGridArea(self, selectGridArea: PickRectanglePointsBuilder):
        """
        Setter for property: (@link PickRectanglePointsBuilder NXOpen.LineDesigner.PickRectanglePointsBuilder@endlink) SelectGridArea
         Returns the selected grid area of column grid  
            
         
        """
        pass
    
    ## Getter for property: (bool) UseSpacingToggle
    ##  Returns the status for using column row spacing of column grid   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def UseSpacingToggle(self) -> bool:
        """
        Getter for property: (bool) UseSpacingToggle
         Returns the status for using column row spacing of column grid   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseSpacingToggle

    ##  Returns the status for using column row spacing of column grid   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UseSpacingToggle.setter
    def UseSpacingToggle(self, useSpacingToggle: bool):
        """
        Setter for property: (bool) UseSpacingToggle
         Returns the status for using column row spacing of column grid   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ModifyColumnsButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
import NXOpen
##  
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateConnectionCreatorBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateConnectionCreatorBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConectionOffset.Value (deprecated) </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ConectionType </term> <description> 
##  
## MoveAndConnect </description> </item> 
## 
## <item><term> 
##  
## ExpressionString </term> <description> 
##  
## 0.0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ConnectionCreatorBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """


    ##  This enum is providing possible connection types    
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MoveAndConnect</term><description> 
    ## </description> </item><item><term> 
    ## Move</term><description> 
    ## </description> </item><item><term> 
    ## Connect</term><description> 
    ## </description> </item></list>
    class ConnectionType(Enum):
        """
        Members Include: <MoveAndConnect> <Move> <Connect>
        """
        MoveAndConnect: int
        Move: int
        Connect: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConnectionCreatorBuilder.ConnectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConectionOffset
    ##  Returns the connection offset   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  The offset value will be retrieved from the UIComp itself.  <br> 

    ## @return NXOpen.Expression
    @property
    def ConectionOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConectionOffset
         Returns the connection offset   
            
         
        """
        pass
    
    ## Getter for property: (@link ConnectionCreatorBuilder.ConnectionType NXOpen.LineDesigner.ConnectionCreatorBuilder.ConnectionType@endlink) ConectionType
    ##  Returns the current connection type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ConnectionCreatorBuilder.ConnectionType
    @property
    def ConectionType(self) -> ConnectionCreatorBuilder.ConnectionType:
        """
        Getter for property: (@link ConnectionCreatorBuilder.ConnectionType NXOpen.LineDesigner.ConnectionCreatorBuilder.ConnectionType@endlink) ConectionType
         Returns the current connection type   
            
         
        """
        pass
    
    ## Setter for property: (@link ConnectionCreatorBuilder.ConnectionType NXOpen.LineDesigner.ConnectionCreatorBuilder.ConnectionType@endlink) ConectionType

    ##  Returns the current connection type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConectionType.setter
    def ConectionType(self, conectionType: ConnectionCreatorBuilder.ConnectionType):
        """
        Setter for property: (@link ConnectionCreatorBuilder.ConnectionType NXOpen.LineDesigner.ConnectionCreatorBuilder.ConnectionType@endlink) ConectionType
         Returns the current connection type   
            
         
        """
        pass
    
    ## Getter for property: (str) ExpressionString
    ##  Returns the connection expression RHS string   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ExpressionString(self) -> str:
        """
        Getter for property: (str) ExpressionString
         Returns the connection expression RHS string   
            
         
        """
        pass
    
    ## Setter for property: (str) ExpressionString

    ##  Returns the connection expression RHS string   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ExpressionString.setter
    def ExpressionString(self, expressionString: str):
        """
        Setter for property: (str) ExpressionString
         Returns the connection expression RHS string   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SourceConnector
    ##  Returns the source connector used in connection  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SourceConnector(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SourceConnector
         Returns the source connector used in connection  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) TargetConnector
    ##  Returns the target connector used in connection   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def TargetConnector(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) TargetConnector
         Returns the target connector used in connection   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link LineDesigner::ConveyorStationFeature LineDesigner::ConveyorStationFeature@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateConveyorStationFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateConveyorStationFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Capacity </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ProcessTime </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## StationType </term> <description> 
##  
## Load </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ConveyorStationFeatureBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.ConveyorStationFeature</ja_class> builder
    """


    ##   This enum is providing possible  types of station feature 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Load</term><description> 
    ## </description> </item><item><term> 
    ## Unload</term><description> 
    ## </description> </item><item><term> 
    ## ProcessRun</term><description> 
    ## </description> </item><item><term> 
    ## ProcessStop</term><description> 
    ## </description> </item><item><term> 
    ## Idle</term><description> 
    ## </description> </item><item><term> 
    ## Decision</term><description> 
    ## </description> </item><item><term> 
    ## Marriage</term><description> 
    ## </description> </item><item><term> 
    ## Disassembly</term><description> 
    ## </description> </item><item><term> 
    ## Assembly</term><description> 
    ## </description> </item><item><term> 
    ## Stop</term><description> 
    ## </description> </item><item><term> 
    ## LimitSwitch</term><description> 
    ## </description> </item><item><term> 
    ## ProximitySwitch</term><description> 
    ## </description> </item><item><term> 
    ## Reader</term><description> 
    ## </description> </item><item><term> 
    ## Pusher</term><description> 
    ## </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Load> <Unload> <ProcessRun> <ProcessStop> <Idle> <Decision> <Marriage> <Disassembly> <Assembly> <Stop> <LimitSwitch> <ProximitySwitch> <Reader> <Pusher>
        """
        Load: int
        Unload: int
        ProcessRun: int
        ProcessStop: int
        Idle: int
        Decision: int
        Marriage: int
        Disassembly: int
        Assembly: int
        Stop: int
        LimitSwitch: int
        ProximitySwitch: int
        Reader: int
        Pusher: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConveyorStationFeatureBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) Capacity
    ##  Returns the conveyor station capacity   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def Capacity(self) -> float:
        """
        Getter for property: (float) Capacity
         Returns the conveyor station capacity   
            
         
        """
        pass
    
    ## Setter for property: (float) Capacity

    ##  Returns the conveyor station capacity   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Capacity.setter
    def Capacity(self, capacity: float):
        """
        Setter for property: (float) Capacity
         Returns the conveyor station capacity   
            
         
        """
        pass
    
    ## Getter for property: (float) ProcessTime
    ##  Returns  the Process time   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def ProcessTime(self) -> float:
        """
        Getter for property: (float) ProcessTime
         Returns  the Process time   
            
         
        """
        pass
    
    ## Setter for property: (float) ProcessTime

    ##  Returns  the Process time   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ProcessTime.setter
    def ProcessTime(self, processTime: float):
        """
        Setter for property: (float) ProcessTime
         Returns  the Process time   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StationLocation
    ##  Returns the conveyor station location   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StationLocation(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StationLocation
         Returns the conveyor station location   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StationLocation

    ##  Returns the conveyor station location   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StationLocation.setter
    def StationLocation(self, stationLocation: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StationLocation
         Returns the conveyor station location   
            
         
        """
        pass
    
    ## Getter for property: (str) StationName
    ##  Returns the station name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def StationName(self) -> str:
        """
        Getter for property: (str) StationName
         Returns the station name   
            
         
        """
        pass
    
    ## Setter for property: (str) StationName

    ##  Returns the station name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StationName.setter
    def StationName(self, stationName: str):
        """
        Setter for property: (str) StationName
         Returns the station name   
            
         
        """
        pass
    
    ## Getter for property: (@link ConveyorStationFeatureBuilder.Type NXOpen.LineDesigner.ConveyorStationFeatureBuilder.Type@endlink) StationType
    ##  Returns the conveyor station type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ConveyorStationFeatureBuilder.Type
    @property
    def StationType(self) -> ConveyorStationFeatureBuilder.Type:
        """
        Getter for property: (@link ConveyorStationFeatureBuilder.Type NXOpen.LineDesigner.ConveyorStationFeatureBuilder.Type@endlink) StationType
         Returns the conveyor station type   
            
         
        """
        pass
    
    ## Setter for property: (@link ConveyorStationFeatureBuilder.Type NXOpen.LineDesigner.ConveyorStationFeatureBuilder.Type@endlink) StationType

    ##  Returns the conveyor station type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StationType.setter
    def StationType(self, stationType: ConveyorStationFeatureBuilder.Type):
        """
        Setter for property: (@link ConveyorStationFeatureBuilder.Type NXOpen.LineDesigner.ConveyorStationFeatureBuilder.Type@endlink) StationType
         Returns the conveyor station type   
            
         
        """
        pass
    
    ##  Description of conveyor station is return
    ##  @return description (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetDescription(self) -> List[str]:
        """
         Description of conveyor station is return
         @return description (List[str]): .
        """
        pass
    
    ##  Description for conveyor station is set
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="description"> (List[str])  </param>
    def SetDescription(self, description: List[str]) -> None:
        """
         Description for conveyor station is set
        """
        pass
    
    ##      
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="secNode"> (@link DBConveyorNode NXOpen.LineDesigner.DBConveyorNode@endlink) </param>
    def SetSECNode(self, secNode: DBConveyorNode) -> None:
        """
             
        """
        pass
    
import NXOpen.Features
##  Represents a conveyor station feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::ConveyorStationFeatureBuilder  NXOpen::LineDesigner::ConveyorStationFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ConveyorStationFeature(NXOpen.Features.Feature): 
    """ Represents a conveyor station feature feature """
    pass


import NXOpen
## 
##     Represents a @link LineDesigner::CoverFeature LineDesigner::CoverFeature@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateCoverFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateCoverFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CoverThickness.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LoadRequirements </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## UseCoverOffset </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class CoverFeatureBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.CoverFeature</ja_class> builder
    """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CoverThickness
    ##  Returnsthe cover thickness   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CoverThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CoverThickness
         Returnsthe cover thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) LoadRequirements
    ##  Returnsthe load requirement   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LoadRequirements(self) -> float:
        """
        Getter for property: (float) LoadRequirements
         Returnsthe load requirement   
            
         
        """
        pass
    
    ## Setter for property: (float) LoadRequirements

    ##  Returnsthe load requirement   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LoadRequirements.setter
    def LoadRequirements(self, loadRequirements: float):
        """
        Setter for property: (float) LoadRequirements
         Returnsthe load requirement   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseCoverOffset
    ##  Returns the cover offset is return, if cover is present over hole   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def UseCoverOffset(self) -> bool:
        """
        Getter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseCoverOffset

    ##  Returns the cover offset is return, if cover is present over hole   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UseCoverOffset.setter
    def UseCoverOffset(self, useCoverOffset: bool):
        """
        Setter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a cover feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::CoverFeatureBuilder  NXOpen::LineDesigner::CoverFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CoverFeature(NXOpen.Features.BodyFeature): 
    """ Represents a cover feature """
    pass


import NXOpen
## 
##     Represents a @link LineDesigner::CreateFactoryElement LineDesigner::CreateFactoryElement@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateCreateFactoryElementBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateCreateFactoryElementBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FactoryType </term> <description> 
##  
## Plant </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class CreateFactoryElementBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.CreateFactoryElement</ja_class> builder
    """


    ##  This enum is providing possible element types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Plant</term><description> 
    ##  Represents the Plant type </description> </item><item><term> 
    ## Station</term><description> 
    ##  Represents the Station type </description> </item><item><term> 
    ## Line</term><description> 
    ##  Represents the Line type </description> </item><item><term> 
    ## Zone</term><description> 
    ##  Represents the Zone type </description> </item><item><term> 
    ## Partition</term><description> 
    ##  Represents the Partition type </description> </item></list>
    class TypeAPI(Enum):
        """
        Members Include: <Plant> <Station> <Line> <Zone> <Partition>
        """
        Plant: int
        Station: int
        Line: int
        Zone: int
        Partition: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CreateFactoryElementBuilder.TypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CreateFactoryElementBuilder.TypeAPI NXOpen.LineDesigner.CreateFactoryElementBuilder.TypeAPI@endlink) FactoryType
    ##  Returns an API that gets element type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return CreateFactoryElementBuilder.TypeAPI
    @property
    def FactoryType(self) -> CreateFactoryElementBuilder.TypeAPI:
        """
        Getter for property: (@link CreateFactoryElementBuilder.TypeAPI NXOpen.LineDesigner.CreateFactoryElementBuilder.TypeAPI@endlink) FactoryType
         Returns an API that gets element type   
            
         
        """
        pass
    
    ## Setter for property: (@link CreateFactoryElementBuilder.TypeAPI NXOpen.LineDesigner.CreateFactoryElementBuilder.TypeAPI@endlink) FactoryType

    ##  Returns an API that gets element type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FactoryType.setter
    def FactoryType(self, factoryType: CreateFactoryElementBuilder.TypeAPI):
        """
        Setter for property: (@link CreateFactoryElementBuilder.TypeAPI NXOpen.LineDesigner.CreateFactoryElementBuilder.TypeAPI@endlink) FactoryType
         Returns an API that gets element type   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns an API that gets name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns an API that gets name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns an API that gets name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns an API that gets name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Position
    ##  Returns an API that gets position   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Position(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Position
         Returns an API that gets position   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Position

    ##  Returns an API that gets position   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Position.setter
    def Position(self, position: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Position
         Returns an API that gets position   
            
         
        """
        pass
    
import NXOpen
##  Represents a create factory element  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::CreateFactoryElementBuilder  NXOpen::LineDesigner::CreateFactoryElementBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CreateFactoryElement(NXOpen.DisplayableObject): 
    """ Represents a create factory element """
    pass


import NXOpen
## 
##     Represents a @link LineDesigner::CreateFence LineDesigner::CreateFence@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateCreateFenceBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateCreateFenceBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CreateFenceBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.CreateFence</ja_class> builder
    """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurveSectionBuilder
    ##  Returns the curve section builder is return   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def CurveSectionBuilder(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurveSectionBuilder
         Returns the curve section builder is return   
            
         
        """
        pass
    
    ## Getter for property: (str) PostFileBrowser
    ##  Returns the post file browser   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def PostFileBrowser(self) -> str:
        """
        Getter for property: (str) PostFileBrowser
         Returns the post file browser   
            
         
        """
        pass
    
    ## Setter for property: (str) PostFileBrowser

    ##  Returns the post file browser   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PostFileBrowser.setter
    def PostFileBrowser(self, filename: str):
        """
        Setter for property: (str) PostFileBrowser
         Returns the post file browser   
            
         
        """
        pass
    
    ## Getter for property: (str) SectionFileBrowser
    ##  Returns the section file browser   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def SectionFileBrowser(self) -> str:
        """
        Getter for property: (str) SectionFileBrowser
         Returns the section file browser   
            
         
        """
        pass
    
    ## Setter for property: (str) SectionFileBrowser

    ##  Returns the section file browser   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SectionFileBrowser.setter
    def SectionFileBrowser(self, filename: str):
        """
        Setter for property: (str) SectionFileBrowser
         Returns the section file browser   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPointPoint
    ##  Returns the start point of fence  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StartPointPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPointPoint
         Returns the start point of fence  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPointPoint

    ##  Returns the start point of fence  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StartPointPoint.setter
    def StartPointPoint(self, startPointPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPointPoint
         Returns the start point of fence  
            
         
        """
        pass
    
import NXOpen
##  Represents a create fence  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::CreateFenceBuilder  NXOpen::LineDesigner::CreateFenceBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CreateFence(NXOpen.DisplayableObject): 
    """ Represents a create fence """
    pass


import NXOpen
## 
##     Represents a @link LineDesigner::CreateSystem LineDesigner::CreateSystem@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateCreateSystemBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateCreateSystemBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CreateSystemBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.CreateSystem</ja_class> builder
    """


    ## Getter for property: (str) ArchPartPath
    ##  Returns an API that gets arch part path   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ArchPartPath(self) -> str:
        """
        Getter for property: (str) ArchPartPath
         Returns an API that gets arch part path   
            
         
        """
        pass
    
    ## Setter for property: (str) ArchPartPath

    ##  Returns an API that gets arch part path   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ArchPartPath.setter
    def ArchPartPath(self, filename: str):
        """
        Setter for property: (str) ArchPartPath
         Returns an API that gets arch part path   
            
         
        """
        pass
    
    ## Getter for property: (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink) JigOnPlane
    ##  Returns an API that gets jig on plane   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return JigOnPlaneBuilder
    @property
    def JigOnPlane(self) -> JigOnPlaneBuilder:
        """
        Getter for property: (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink) JigOnPlane
         Returns an API that gets jig on plane   
            
         
        """
        pass
    
    ## Getter for property: (str) LinePartPath
    ##  Returns an API that gets line part path   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def LinePartPath(self) -> str:
        """
        Getter for property: (str) LinePartPath
         Returns an API that gets line part path   
            
         
        """
        pass
    
    ## Setter for property: (str) LinePartPath

    ##  Returns an API that gets line part path   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LinePartPath.setter
    def LinePartPath(self, filename: str):
        """
        Setter for property: (str) LinePartPath
         Returns an API that gets line part path   
            
         
        """
        pass
    
    ##  An API that preview the system 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def InitPreview(self) -> None:
        """
         An API that preview the system 
        """
        pass
    
    ##  An API that updates system 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def Update(self) -> None:
        """
         An API that updates system 
        """
        pass
    
import NXOpen
##  Represents a create system  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::CreateSystemBuilder  NXOpen::LineDesigner::CreateSystemBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CreateSystem(NXOpen.DisplayableObject): 
    """ Represents a create system """
    pass


##  Represents DB column grid  node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBColumnGridNode  NXOpen::LineDesigner::DBNodeManager::CreateDBColumnGridNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBColumnGridNode(DBSmartComplexEquipmentNode): 
    """ Represents DB column grid  node """
    pass


##  Represents DB conveyor node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBConveyorNode  NXOpen::LineDesigner::DBNodeManager::CreateDBConveyorNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBConveyorNode(DBSmartComplexEquipmentNode): 
    """ Represents DB conveyor node """
    pass


##  Represents DB import factory cad geo node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBFactoryCadGeoNode  NXOpen::LineDesigner::DBNodeManager::CreateDBFactoryCadGeoNode @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DBFactoryCadGeoNode(DBSmartComplexEquipmentNode): 
    """ Represents DB import factory cad geo node """
    pass


##  Represents DB factory node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBFactoryNode  NXOpen::LineDesigner::DBNodeManager::CreateDBFactoryNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBFactoryNode(DBNode): 
    """ Represents DB factory node """


    ## 
    ##            This enum define the factory node type
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Plant</term><description> 
    ## </description> </item><item><term> 
    ## Station</term><description> 
    ## </description> </item><item><term> 
    ## Line</term><description> 
    ## </description> </item><item><term> 
    ## Zone</term><description> 
    ## </description> </item><item><term> 
    ## Partition</term><description> 
    ## </description> </item><item><term> 
    ## Unknown</term><description> 
    ## </description> </item></list>
    class NodeType(Enum):
        """
        Members Include: <Plant> <Station> <Line> <Zone> <Partition> <Unknown>
        """
        Plant: int
        Station: int
        Line: int
        Zone: int
        Partition: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DBFactoryNode.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
##  Represents DB factory node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBFenceNode  NXOpen::LineDesigner::DBNodeManager::CreateDBFenceNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBFenceNode(DBSmartComplexEquipmentNode): 
    """ Represents DB factory node """
    pass


##  Represents DB Floor equipment node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBFloorEquipmentNode  NXOpen::LineDesigner::DBNodeManager::CreateDBFloorEquipmentNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBFloorEquipmentNode(DBSmartComplexEquipmentNode): 
    """ Represents DB Floor equipment node """
    pass


##  Represents DB node container <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBNodeContainer  NXOpen::LineDesigner::DBNodeManager::CreateDBNodeContainer @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBNodeContainer(DBSmartComplexEquipmentNode): 
    """ Represents DB node container"""
    pass


import NXOpen
##  Represents a manager of line designer db nodes  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBNodeManager(NXOpen.Object): 
    """ Represents a manager of line designer db nodes """


    ## Creates column grid node 
    ##  @return node (@link DBColumnGridNode NXOpen.LineDesigner.DBColumnGridNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBColumnGridNode(part: NXOpen.Part) -> DBColumnGridNode:
        """
        Creates column grid node 
         @return node (@link DBColumnGridNode NXOpen.LineDesigner.DBColumnGridNode@endlink):  .
        """
        pass
    
    ##  Creates conveyor node 
    ##  @return node (@link DBConveyorNode NXOpen.LineDesigner.DBConveyorNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBConveyorNode(part: NXOpen.Part) -> DBConveyorNode:
        """
         Creates conveyor node 
         @return node (@link DBConveyorNode NXOpen.LineDesigner.DBConveyorNode@endlink):  .
        """
        pass
    
    ##  Creates FactoryCad node 
    ##  @return node (@link DBFactoryCadGeoNode NXOpen.LineDesigner.DBFactoryCadGeoNode@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBFactoryCadGeoNode(part: NXOpen.Part) -> DBFactoryCadGeoNode:
        """
         Creates FactoryCad node 
         @return node (@link DBFactoryCadGeoNode NXOpen.LineDesigner.DBFactoryCadGeoNode@endlink):  .
        """
        pass
    
    ##  Factory node creation API
    ##  @return node (@link DBFactoryNode NXOpen.LineDesigner.DBFactoryNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="type"> (@link DBFactoryNode.NodeType NXOpen.LineDesigner.DBFactoryNode.NodeType@endlink)  Type of factory node </param>
    def CreateDBFactoryNode(part: NXOpen.Part, type: DBFactoryNode.NodeType) -> DBFactoryNode:
        """
         Factory node creation API
         @return node (@link DBFactoryNode NXOpen.LineDesigner.DBFactoryNode@endlink):  .
        """
        pass
    
    ##  Creates fence node 
    ##  @return node (@link DBFenceNode NXOpen.LineDesigner.DBFenceNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBFenceNode(part: NXOpen.Part) -> DBFenceNode:
        """
         Creates fence node 
         @return node (@link DBFenceNode NXOpen.LineDesigner.DBFenceNode@endlink):  .
        """
        pass
    
    ##  Creates floor equipment node 
    ##  @return node (@link DBFloorEquipmentNode NXOpen.LineDesigner.DBFloorEquipmentNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBFloorEquipmentNode(part: NXOpen.Part) -> DBFloorEquipmentNode:
        """
         Creates floor equipment node 
         @return node (@link DBFloorEquipmentNode NXOpen.LineDesigner.DBFloorEquipmentNode@endlink):  .
        """
        pass
    
    ##  Creates node container  
    ##  @return node (@link DBNodeContainer NXOpen.LineDesigner.DBNodeContainer@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBNodeContainer(part: NXOpen.Part) -> DBNodeContainer:
        """
         Creates node container  
         @return node (@link DBNodeContainer NXOpen.LineDesigner.DBNodeContainer@endlink):  .
        """
        pass
    
    ##  Creates platform equipment node 
    ##  @return node (@link DBPlatformEquipmentNode NXOpen.LineDesigner.DBPlatformEquipmentNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBPlatformEquipmentNode(part: NXOpen.Part) -> DBPlatformEquipmentNode:
        """
         Creates platform equipment node 
         @return node (@link DBPlatformEquipmentNode NXOpen.LineDesigner.DBPlatformEquipmentNode@endlink):  .
        """
        pass
    
    ##  Creates stairway equipment node 
    ##  @return node (@link DBStairwayEquipmentNode NXOpen.LineDesigner.DBStairwayEquipmentNode@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDBStairwayEquipmentNode(part: NXOpen.Part) -> DBStairwayEquipmentNode:
        """
         Creates stairway equipment node 
         @return node (@link DBStairwayEquipmentNode NXOpen.LineDesigner.DBStairwayEquipmentNode@endlink):  .
        """
        pass
    
import NXOpen
##  Represents a utils of line designer for journaling uinode methods  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class DBNodeUtils(NXOpen.Object): 
    """ Represents a utils of line designer for journaling uinode methods """


    ##  An API to check if part has db node 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partTag"> (@link NXOpen.Part NXOpen.Part@endlink)  </param>
    def ContainsDBNode(partTag: NXOpen.Part) -> None:
        """
         An API to check if part has db node 
        """
        pass
    
import NXOpen
##  Represents DB node  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBNode(NXOpen.NXObject): 
    """ Represents DB node """
    pass


##  Represents DB platform equipment node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBPlatformEquipmentNode  NXOpen::LineDesigner::DBNodeManager::CreateDBPlatformEquipmentNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBPlatformEquipmentNode(DBSmartComplexEquipmentNode): 
    """ Represents DB platform equipment node """
    pass


##  Represents DB factory node 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBSmartComplexEquipmentNode(DBSmartEquipmentNode): 
    """ Represents DB factory node """
    pass


##  Represents DB factory node 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBSmartEquipmentNode(DBNode): 
    """ Represents DB factory node """
    pass


##  Represents DB stairway equipment node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBStairwayEquipmentNode  NXOpen::LineDesigner::DBNodeManager::CreateDBStairwayEquipmentNode @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DBStairwayEquipmentNode(DBSmartComplexEquipmentNode): 
    """ Represents DB stairway equipment node """


    ##  An API to add left railing to stairway 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AddLeftRailing(self) -> None:
        """
         An API to add left railing to stairway 
        """
        pass
    
    ##  An API to add right railing to stairway 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AddRightRailing(self) -> None:
        """
         An API to add right railing to stairway 
        """
        pass
    
    ##  An API to remove both railings to stairway 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def RemoveBothRailing(self) -> None:
        """
         An API to remove both railings to stairway 
        """
        pass
    
    ##  An API to remove left railing to stairway 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def RemoveLeftRailing(self) -> None:
        """
         An API to remove left railing to stairway 
        """
        pass
    
    ##  An API to remove right railing to stairway 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def RemoveRightRailing(self) -> None:
        """
         An API to remove right railing to stairway 
        """
        pass
    
import NXOpen
##  Define Robot <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateDefineRobotBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateDefineRobotBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BaseFrameReversePropagation </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.1  <br> 

class DefineRobotBuilder(NXOpen.Builder): 
    """ Define Robot"""


    ## Getter for property: (str) BaseFrameCompitableTypeName
    ##  Returns the base frame compitable type name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def BaseFrameCompitableTypeName(self) -> str:
        """
        Getter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    
    ## Setter for property: (str) BaseFrameCompitableTypeName

    ##  Returns the base frame compitable type name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameCompitableTypeName.setter
    def BaseFrameCompitableTypeName(self, baseFrameCompitableTypeName: str):
        """
        Setter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector
    ##  Returns the base frame direction of connector   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def BaseFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector

    ##  Returns the base frame direction of connector   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameDirectionOfConnector.setter
    def BaseFrameDirectionOfConnector(self, baseFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection
    ##  Returns the base frame parallel to object direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def BaseFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection

    ##  Returns the base frame parallel to object direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameParallelToObjectDirection.setter
    def BaseFrameParallelToObjectDirection(self, baseFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint
    ##  Returns the base frame point   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Point
    @property
    def BaseFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint

    ##  Returns the base frame point   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFramePoint.setter
    def BaseFramePoint(self, baseFramePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    
    ## Getter for property: (bool) BaseFrameReversePropagation
    ##  Returns the base frame reverse propagation   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def BaseFrameReversePropagation(self) -> bool:
        """
        Getter for property: (bool) BaseFrameReversePropagation
         Returns the base frame reverse propagation   
            
         
        """
        pass
    
    ## Setter for property: (bool) BaseFrameReversePropagation

    ##  Returns the base frame reverse propagation   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameReversePropagation.setter
    def BaseFrameReversePropagation(self, baseFrameReversePropagation: bool):
        """
        Setter for property: (bool) BaseFrameReversePropagation
         Returns the base frame reverse propagation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector
    ##  Returns the tool frame direction of connector   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def ToolFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector

    ##  Returns the tool frame direction of connector   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolFrameDirectionOfConnector.setter
    def ToolFrameDirectionOfConnector(self, toolFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection
    ##  Returns the tool frame parallel to object direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def ToolFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection

    ##  Returns the tool frame parallel to object direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolFrameParallelToObjectDirection.setter
    def ToolFrameParallelToObjectDirection(self, toolFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint
    ##  Returns the tool frame point   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Point
    @property
    def ToolFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint

    ##  Returns the tool frame point   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolFramePoint.setter
    def ToolFramePoint(self, toolFramePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    
    ##   The base frame compatible connector types are returns 
    ##  @return baseFrameCompatibleTypeList (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetBaseFrameCompatibleTypeList(self) -> List[str]:
        """
          The base frame compatible connector types are returns 
         @return baseFrameCompatibleTypeList (List[str]): .
        """
        pass
    
    ##  The base frame connector propagated expressions 
    ##  @return baseFramePropagatedExpression (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetBaseFramePropagatedExpression(self) -> List[NXOpen.Expression]:
        """
         The base frame connector propagated expressions 
         @return baseFramePropagatedExpression (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  The tool frame connector propagated expressions 
    ##  @return toolFramePropagatedExpression (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetToolFramePropagatedExpression(self) -> List[NXOpen.Expression]:
        """
         The tool frame connector propagated expressions 
         @return toolFramePropagatedExpression (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  The base connector compatible types are set 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="baseFrameCompatibleTypeList"> (List[str])  </param>
    def SetBaseFrameCompatibleTypeList(self, baseFrameCompatibleTypeList: List[str]) -> None:
        """
         The base connector compatible types are set 
        """
        pass
    
    ## The base frame connector propagated expressions are set 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="baseFramePropagatedExpression"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def SetBaseFramePropagatedExpression(self, baseFramePropagatedExpression: List[NXOpen.Expression]) -> None:
        """
        The base frame connector propagated expressions are set 
        """
        pass
    
    ##  The Nth expressions from base frame connector propagated expressions are set
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="nthBaseFramePropagatedExpression"> (int) </param>
    ## <param name="baseFramePropagatedExpression"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetNthBaseFramePropagatedExpression(self, nthBaseFramePropagatedExpression: int, baseFramePropagatedExpression: NXOpen.Expression) -> None:
        """
         The Nth expressions from base frame connector propagated expressions are set
        """
        pass
    
    ##  The Nth expressions from tool frame connector propagated expressions are set
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="nthToolFramePropagatedExpression"> (int) </param>
    ## <param name="toolFramePropagatedExpression"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetNthToolFramePropagatedExpression(self, nthToolFramePropagatedExpression: int, toolFramePropagatedExpression: NXOpen.Expression) -> None:
        """
         The Nth expressions from tool frame connector propagated expressions are set
        """
        pass
    
    ## The tool frame connector propagated expressions are set 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="toolFramePropagatedExpression"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def SetToolFramePropagatedExpression(self, toolFramePropagatedExpression: List[NXOpen.Expression]) -> None:
        """
        The tool frame connector propagated expressions are set 
        """
        pass
    
import NXOpen
##  Define Tool  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateDefineToolBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateDefineToolBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class DefineToolBuilder(NXOpen.Builder): 
    """ Define Tool """


    ##  This enum is providing possible tool type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Gun</term><description> 
    ## </description> </item><item><term> 
    ## ServoGun</term><description> 
    ## </description> </item><item><term> 
    ## PneumaticServoGun</term><description> 
    ## </description> </item><item><term> 
    ## Gripper</term><description> 
    ## </description> </item><item><term> 
    ## AdhesiveGun</term><description> 
    ## </description> </item><item><term> 
    ## ClinchGun</term><description> 
    ## </description> </item><item><term> 
    ## PaintGun</term><description> 
    ## </description> </item><item><term> 
    ## RivetGun</term><description> 
    ## </description> </item><item><term> 
    ## SealerGun</term><description> 
    ## </description> </item><item><term> 
    ## WeldGun</term><description> 
    ## </description> </item><item><term> 
    ## NutWelder</term><description> 
    ## </description> </item><item><term> 
    ## StudWelder</term><description> 
    ## </description> </item><item><term> 
    ## FlowDrillScrew</term><description> 
    ## </description> </item><item><term> 
    ## MultiTool</term><description> 
    ## </description> </item></list>
    class ToolType(Enum):
        """
        Members Include: <Gun> <ServoGun> <PneumaticServoGun> <Gripper> <AdhesiveGun> <ClinchGun> <PaintGun> <RivetGun> <SealerGun> <WeldGun> <NutWelder> <StudWelder> <FlowDrillScrew> <MultiTool>
        """
        Gun: int
        ServoGun: int
        PneumaticServoGun: int
        Gripper: int
        AdhesiveGun: int
        ClinchGun: int
        PaintGun: int
        RivetGun: int
        SealerGun: int
        WeldGun: int
        NutWelder: int
        StudWelder: int
        FlowDrillScrew: int
        MultiTool: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DefineToolBuilder.ToolType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) BaseFrameCompitableTypeName
    ##  Returns the base frame compitable type name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def BaseFrameCompitableTypeName(self) -> str:
        """
        Getter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    
    ## Setter for property: (str) BaseFrameCompitableTypeName

    ##  Returns the base frame compitable type name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameCompitableTypeName.setter
    def BaseFrameCompitableTypeName(self, baseFrameCompitableTypeName: str):
        """
        Setter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector
    ##  Returns the base frame direction of connector   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def BaseFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector

    ##  Returns the base frame direction of connector   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameDirectionOfConnector.setter
    def BaseFrameDirectionOfConnector(self, baseFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection
    ##  Returns the base frame parallel to object direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def BaseFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection

    ##  Returns the base frame parallel to object direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFrameParallelToObjectDirection.setter
    def BaseFrameParallelToObjectDirection(self, baseFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint
    ##  Returns the base frame point   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Point
    @property
    def BaseFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint

    ##  Returns the base frame point   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @BaseFramePoint.setter
    def BaseFramePoint(self, baseFramePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefineToolTypeToggle
    ##  Returns the define tool type toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def DefineToolTypeToggle(self) -> bool:
        """
        Getter for property: (bool) DefineToolTypeToggle
         Returns the define tool type toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefineToolTypeToggle

    ##  Returns the define tool type toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DefineToolTypeToggle.setter
    def DefineToolTypeToggle(self, defineToolTypeToggle: bool):
        """
        Setter for property: (bool) DefineToolTypeToggle
         Returns the define tool type toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPart NXOpen.SelectPart@endlink) SelectGunTips
    ##  Returns the select gun tips   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectPart
    @property
    def SelectGunTips(self) -> NXOpen.SelectPart:
        """
        Getter for property: (@link NXOpen.SelectPart NXOpen.SelectPart@endlink) SelectGunTips
         Returns the select gun tips   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector
    ##  Returns the tool frame direction of connector   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def ToolFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector

    ##  Returns the tool frame direction of connector   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolFrameDirectionOfConnector.setter
    def ToolFrameDirectionOfConnector(self, toolFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection
    ##  Returns the tool frame parallel to object direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def ToolFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection

    ##  Returns the tool frame parallel to object direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolFrameParallelToObjectDirection.setter
    def ToolFrameParallelToObjectDirection(self, toolFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint
    ##  Returns the tool frame point   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Point
    @property
    def ToolFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint

    ##  Returns the tool frame point   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolFramePoint.setter
    def ToolFramePoint(self, toolFramePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    
    ## Getter for property: (@link DefineToolBuilder.ToolType NXOpen.LineDesigner.DefineToolBuilder.ToolType@endlink) ToolTypeList
    ##  Returns the tool type list   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return DefineToolBuilder.ToolType
    @property
    def ToolTypeList(self) -> DefineToolBuilder.ToolType:
        """
        Getter for property: (@link DefineToolBuilder.ToolType NXOpen.LineDesigner.DefineToolBuilder.ToolType@endlink) ToolTypeList
         Returns the tool type list   
            
         
        """
        pass
    
    ## Setter for property: (@link DefineToolBuilder.ToolType NXOpen.LineDesigner.DefineToolBuilder.ToolType@endlink) ToolTypeList

    ##  Returns the tool type list   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @ToolTypeList.setter
    def ToolTypeList(self, enumToolType: DefineToolBuilder.ToolType):
        """
        Setter for property: (@link DefineToolBuilder.ToolType NXOpen.LineDesigner.DefineToolBuilder.ToolType@endlink) ToolTypeList
         Returns the tool type list   
            
         
        """
        pass
    
    ##   The base frame compatible connector types are returns 
    ##  @return baseFrameCompatibleTypeList (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetBaseFrameCompatibleTypeList(self) -> List[str]:
        """
          The base frame compatible connector types are returns 
         @return baseFrameCompatibleTypeList (List[str]): .
        """
        pass
    
    ##  The base frame connector propagated expressions 
    ##  @return baseFramePropagatedExpression (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetBaseFramePropagatedExpression(self) -> List[NXOpen.Expression]:
        """
         The base frame connector propagated expressions 
         @return baseFramePropagatedExpression (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  To remove objects
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def RemoveButton(self) -> None:
        """
         To remove objects
        """
        pass
    
    ##  The base connector compatible types are set 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="baseFrameCompatibleTypeList"> (List[str])  </param>
    def SetBaseFrameCompatibleTypeList(self, baseFrameCompatibleTypeList: List[str]) -> None:
        """
         The base connector compatible types are set 
        """
        pass
    
    ## The base frame connector propagated expressions are set 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="baseFramePropagatedExpression"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def SetBaseFramePropagatedExpression(self, baseFramePropagatedExpression: List[NXOpen.Expression]) -> None:
        """
        The base frame connector propagated expressions are set 
        """
        pass
    
    ##  The Nth expressions from base frame connector propagated expressions are set
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="nthBaseFramePropagatedExpression"> (int) </param>
    ## <param name="baseFramePropagatedExpression"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetNthBaseFramePropagatedExpression(self, nthBaseFramePropagatedExpression: int, baseFramePropagatedExpression: NXOpen.Expression) -> None:
        """
         The Nth expressions from base frame connector propagated expressions are set
        """
        pass
    
##  Represents a typed connector feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::TypedConnectorFeatureBuilder  NXOpen::LineDesigner::TypedConnectorFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DiamondConnectorFeature(TypedConnectorFeature): 
    """ Represents a typed connector feature feature """
    pass


import NXOpen
##  
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateDisconnectConnectionBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateDisconnectConnectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class DisconnectConnectionBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """


    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) SelConnector
    ##  Returns an API that gives connector   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def SelConnector(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) SelConnector
         Returns an API that gives connector   
            
         
        """
        pass
    
    ##  This method is to disconnect selected components with current component 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="selectedComponent"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink)  First selected object. </param>
    ## <param name="componentToDisconnect"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  All selected objects to disconnect. </param>
    def Disconnect(self, selectedComponent: NXOpen.TaggedObject, componentToDisconnect: List[NXOpen.TaggedObject]) -> None:
        """
         This method is to disconnect selected components with current component 
        """
        pass
    
import NXOpen
##   <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateDistributeComponentsBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateDistributeComponentsBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class DistributeComponentsBuilder(NXOpen.Builder): 
    """ """


    ## Getter for property: (bool) IsUserDefinedDirection
    ##  Returns the user defined   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return bool
    @property
    def IsUserDefinedDirection(self) -> bool:
        """
        Getter for property: (bool) IsUserDefinedDirection
         Returns the user defined   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsUserDefinedDirection

    ##  Returns the user defined   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @IsUserDefinedDirection.setter
    def IsUserDefinedDirection(self, isUserDefinedDirection: bool):
        """
        Setter for property: (bool) IsUserDefinedDirection
         Returns the user defined   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedCompList
    ##  Returns the selected comp list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectedCompList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedCompList
         Returns the selected comp list   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection
    ##  Returns the specify direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.Direction
    @property
    def SpecifyDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection

    ##  Returns the specify direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @SpecifyDirection.setter
    def SpecifyDirection(self, specifyDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
    
import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateEndItemAssemblyStateBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateEndItemAssemblyStateBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AssemblyItemState </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## AssemblyOccurenceState </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1876.0.0  <br> 

class EndItemAssemblyStateBuilder(NXOpen.Builder): 
    """  """


    ## Getter for property: (bool) AssemblyItemState
    ##  Returns the assembly item state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    ## @return bool
    @property
    def AssemblyItemState(self) -> bool:
        """
        Getter for property: (bool) AssemblyItemState
         Returns the assembly item state   
            
         
        """
        pass
    
    ## Setter for property: (bool) AssemblyItemState

    ##  Returns the assembly item state   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    @AssemblyItemState.setter
    def AssemblyItemState(self, assemblyItemState: bool):
        """
        Setter for property: (bool) AssemblyItemState
         Returns the assembly item state   
            
         
        """
        pass
    
    ## Getter for property: (bool) AssemblyOccurenceState
    ##  Returns the assembly occurence state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    ## @return bool
    @property
    def AssemblyOccurenceState(self) -> bool:
        """
        Getter for property: (bool) AssemblyOccurenceState
         Returns the assembly occurence state   
            
         
        """
        pass
    
    ## Setter for property: (bool) AssemblyOccurenceState

    ##  Returns the assembly occurence state   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    @AssemblyOccurenceState.setter
    def AssemblyOccurenceState(self, assemblyOccurenceState: bool):
        """
        Setter for property: (bool) AssemblyOccurenceState
         Returns the assembly occurence state   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Display
##  use for creation of enhanced shadow outline builder  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateEnhancedShadowOutLineBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateEnhancedShadowOutLineBuilder @endlink  <br> 
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
## Xcyc </description> </item> 
## 
## <item><term> 
##  
## LayerSettings.LayerOption </term> <description> 
##  
## Work </description> </item> 
## 
## <item><term> 
##  
## LevelOfOutline </term> <description> 
##  
## Simple </description> </item> 
## 
## <item><term> 
##  
## ReferenceSetToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ScopeOfOutline </term> <description> 
##  
## CompleteComponent </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class EnhancedShadowOutLineBuilder(NXOpen.Builder): 
    """ use for creation of enhanced shadow outline builder """


    ##  This enum used to represent drawing options
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Xcyc</term><description> 
    ## </description> </item><item><term> 
    ## Yczc</term><description> 
    ## </description> </item><item><term> 
    ## Zcxc</term><description> 
    ## </description> </item><item><term> 
    ## Custom</term><description> 
    ## </description> </item></list>
    class DrawingPlaneOptions(Enum):
        """
        Members Include: <Xcyc> <Yczc> <Zcxc> <Custom>
        """
        Xcyc: int
        Yczc: int
        Zcxc: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EnhancedShadowOutLineBuilder.DrawingPlaneOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum used to represent outline level
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Simple</term><description> 
    ## </description> </item><item><term> 
    ## Detailed</term><description> 
    ## </description> </item></list>
    class OutLineLevel(Enum):
        """
        Members Include: <Simple> <Detailed>
        """
        Simple: int
        Detailed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EnhancedShadowOutLineBuilder.OutLineLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum used to represent scope of the outline
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CompleteComponent</term><description> 
    ## </description> </item><item><term> 
    ## Objects</term><description> 
    ## </description> </item></list>
    class OutLineScope(Enum):
        """
        Members Include: <CompleteComponent> <Objects>
        """
        CompleteComponent: int
        Objects: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EnhancedShadowOutLineBuilder.OutLineScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.DrawingPlaneOptions@endlink) DrawingPlaneOption
    ##  Returns the drawing plane option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return EnhancedShadowOutLineBuilder.DrawingPlaneOptions
    @property
    def DrawingPlaneOption(self) -> EnhancedShadowOutLineBuilder.DrawingPlaneOptions:
        """
        Getter for property: (@link EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.DrawingPlaneOptions@endlink) DrawingPlaneOption
         Returns the drawing plane option   
            
         
        """
        pass
    
    ## Setter for property: (@link EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.DrawingPlaneOptions@endlink) DrawingPlaneOption

    ##  Returns the drawing plane option   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DrawingPlaneOption.setter
    def DrawingPlaneOption(self, drawingPlaneOption: EnhancedShadowOutLineBuilder.DrawingPlaneOptions):
        """
        Setter for property: (@link EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.DrawingPlaneOptions@endlink) DrawingPlaneOption
         Returns the drawing plane option   
            
         
        """
        pass
    
    ## Getter for property: (str) InputText
    ##  Returns the input text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def InputText(self) -> str:
        """
        Getter for property: (str) InputText
         Returns the input text   
            
         
        """
        pass
    
    ## Setter for property: (str) InputText

    ##  Returns the input text   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @InputText.setter
    def InputText(self, inputText: str):
        """
        Setter for property: (str) InputText
         Returns the input text   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Display.LayerSettingsBuilder NXOpen.Display.LayerSettingsBuilder@endlink) LayerSettings
    ##  Returns the layer setting for elbows to be placed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Display.LayerSettingsBuilder
    @property
    def LayerSettings(self) -> NXOpen.Display.LayerSettingsBuilder:
        """
        Getter for property: (@link NXOpen.Display.LayerSettingsBuilder NXOpen.Display.LayerSettingsBuilder@endlink) LayerSettings
         Returns the layer setting for elbows to be placed   
            
         
        """
        pass
    
    ## Getter for property: (@link EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineLevel@endlink) LevelOfOutline
    ##  Returns the out line enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return EnhancedShadowOutLineBuilder.OutLineLevel
    @property
    def LevelOfOutline(self) -> EnhancedShadowOutLineBuilder.OutLineLevel:
        """
        Getter for property: (@link EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineLevel@endlink) LevelOfOutline
         Returns the out line enum   
            
         
        """
        pass
    
    ## Setter for property: (@link EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineLevel@endlink) LevelOfOutline

    ##  Returns the out line enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LevelOfOutline.setter
    def LevelOfOutline(self, levelOfOutline: EnhancedShadowOutLineBuilder.OutLineLevel):
        """
        Setter for property: (@link EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineLevel@endlink) LevelOfOutline
         Returns the out line enum   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) LineColorFontWidth
    ##  Returns the outline color font width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) LineColorFontWidth
         Returns the outline color font width   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReferenceSetToggle
    ##  Returns the reference set toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def ReferenceSetToggle(self) -> bool:
        """
        Getter for property: (bool) ReferenceSetToggle
         Returns the reference set toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReferenceSetToggle

    ##  Returns the reference set toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ReferenceSetToggle.setter
    def ReferenceSetToggle(self, referenceSetToggle: bool):
        """
        Setter for property: (bool) ReferenceSetToggle
         Returns the reference set toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link EnhancedShadowOutLineBuilder.OutLineScope NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineScope@endlink) ScopeOfOutline
    ##  Returns the description enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return EnhancedShadowOutLineBuilder.OutLineScope
    @property
    def ScopeOfOutline(self) -> EnhancedShadowOutLineBuilder.OutLineScope:
        """
        Getter for property: (@link EnhancedShadowOutLineBuilder.OutLineScope NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineScope@endlink) ScopeOfOutline
         Returns the description enum   
            
         
        """
        pass
    
    ## Setter for property: (@link EnhancedShadowOutLineBuilder.OutLineScope NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineScope@endlink) ScopeOfOutline

    ##  Returns the description enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ScopeOfOutline.setter
    def ScopeOfOutline(self, scopeOfOutline: EnhancedShadowOutLineBuilder.OutLineScope):
        """
        Setter for property: (@link EnhancedShadowOutLineBuilder.OutLineScope NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineScope@endlink) ScopeOfOutline
         Returns the description enum   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
    ##  Returns the select object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
         Returns the select object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SpecifyPlane
    ##  Returns the specify plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def SpecifyPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SpecifyPlane
         Returns the specify plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SpecifyPlane

    ##  Returns the specify plane   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SpecifyPlane.setter
    def SpecifyPlane(self, specifyPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) SpecifyPlane
         Returns the specify plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextColorFontWidth
    ##  Returns the text color font width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextColorFontWidth(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextColorFontWidth
         Returns the text color font width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TextHeight
    ##  Returns the text height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TextHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TextHeight
         Returns the text height   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation
    ##  Returns the text location   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def TextLocation(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation
         Returns the text location   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation

    ##  Returns the text location   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TextLocation.setter
    def TextLocation(self, textLocation: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation
         Returns the text location   
            
         
        """
        pass
    
    ##  Returns the selected reference set 
    ##  @return selectedReferenceSet (List[str]): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetSelectedReferenceSet(self) -> List[str]:
        """
         Returns the selected reference set 
         @return selectedReferenceSet (List[str]): .
        """
        pass
    
    ##  Sets the selected reference set 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="selectedReferenceSet"> (List[str])  </param>
    def SetSelectedReferenceSet(self, selectedReferenceSet: List[str]) -> None:
        """
         Sets the selected reference set 
        """
        pass
    
import NXOpen
## 
##     Represents a @link LineDesigner::ExportPlantToDWG LineDesigner::ExportPlantToDWG@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateExportPlantToDwgBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateExportPlantToDwgBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SaveAs </term> <description> 
##  
## T2d </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ExportPlantToDWGBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.ExportPlantToDWG</ja_class> builder
    """


    ##  This enum represents dwg saving types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## T2d</term><description> 
    ##  Represents the 2D type </description> </item><item><term> 
    ## T3d</term><description> 
    ##  Represents the 3D type </description> </item></list>
    class SaveAsType(Enum):
        """
        Members Include: <T2d> <T3d>
        """
        T2d: int
        T3d: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportPlantToDWGBuilder.SaveAsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) FileName
    ##  Returns the file name     
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name     
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##  Returns the file name     
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the file name     
            
         
        """
        pass
    
    ## Getter for property: (str) FolderName
    ##  Returns the folder name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    
    ## Setter for property: (str) FolderName

    ##  Returns the folder name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FolderName.setter
    def FolderName(self, foldername: str):
        """
        Setter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    
    ## Getter for property: (@link ExportPlantToDWGBuilder.SaveAsType NXOpen.LineDesigner.ExportPlantToDWGBuilder.SaveAsType@endlink) SaveAs
    ##  Returns an API to get save as type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ExportPlantToDWGBuilder.SaveAsType
    @property
    def SaveAs(self) -> ExportPlantToDWGBuilder.SaveAsType:
        """
        Getter for property: (@link ExportPlantToDWGBuilder.SaveAsType NXOpen.LineDesigner.ExportPlantToDWGBuilder.SaveAsType@endlink) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    
    ## Setter for property: (@link ExportPlantToDWGBuilder.SaveAsType NXOpen.LineDesigner.ExportPlantToDWGBuilder.SaveAsType@endlink) SaveAs

    ##  Returns an API to get save as type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SaveAs.setter
    def SaveAs(self, saveAs: ExportPlantToDWGBuilder.SaveAsType):
        """
        Setter for property: (@link ExportPlantToDWGBuilder.SaveAsType NXOpen.LineDesigner.ExportPlantToDWGBuilder.SaveAsType@endlink) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    
import NXOpen
##  Represents the export plant to dwg  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::ExportPlantToDWGBuilder  NXOpen::LineDesigner::ExportPlantToDWGBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ExportPlantToDWG(NXOpen.NXObject): 
    """ Represents the export plant to dwg """
    pass


import NXOpen
## 
##     Represents a @link LineDesigner::ExportToDWG LineDesigner::ExportToDWG@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateExportToDwgBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateExportToDwgBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MonochromeDisplay </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SaveAs </term> <description> 
##  
## T2d </description> </item> 
## 
## <item><term> 
##  
## TemplateSheet </term> <description> 
##  
## A0Size </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ExportToDWGBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.ExportToDWG</ja_class> builder
    """


    ##  This enum represents the dwg saving types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## T2d</term><description> 
    ##  Represents the 2D type </description> </item><item><term> 
    ## T3d</term><description> 
    ##  Represents the 3D type </description> </item></list>
    class SaveAsTypeAPI(Enum):
        """
        Members Include: <T2d> <T3d>
        """
        T2d: int
        T3d: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportToDWGBuilder.SaveAsTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the dwg sheet template types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## A0Size</term><description> 
    ##  Represents the A0 type </description> </item><item><term> 
    ## A1Size</term><description> 
    ##  Represents the A1 type </description> </item><item><term> 
    ## A2Size</term><description> 
    ##  Represents the A2 type </description> </item><item><term> 
    ## A3Size</term><description> 
    ##  Represents the A3 type </description> </item><item><term> 
    ## A4Size</term><description> 
    ##  Represents the A4 type </description> </item></list>
    class TemplateTypeAPI(Enum):
        """
        Members Include: <A0Size> <A1Size> <A2Size> <A3Size> <A4Size>
        """
        A0Size: int
        A1Size: int
        A2Size: int
        A3Size: int
        A4Size: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportToDWGBuilder.TemplateTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) FileName
    ##  Returns the file name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name   
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##  Returns the file name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the file name   
            
         
        """
        pass
    
    ## Getter for property: (str) FolderName
    ##  Returns the folder name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    
    ## Setter for property: (str) FolderName

    ##  Returns the folder name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FolderName.setter
    def FolderName(self, foldername: str):
        """
        Setter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    
    ## Getter for property: (bool) MonochromeDisplay
    ##  Returnsthe monochrome display is return  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def MonochromeDisplay(self) -> bool:
        """
        Getter for property: (bool) MonochromeDisplay
         Returnsthe monochrome display is return  
            
         
        """
        pass
    
    ## Setter for property: (bool) MonochromeDisplay

    ##  Returnsthe monochrome display is return  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MonochromeDisplay.setter
    def MonochromeDisplay(self, monochromeDisplay: bool):
        """
        Setter for property: (bool) MonochromeDisplay
         Returnsthe monochrome display is return  
            
         
        """
        pass
    
    ## Getter for property: (@link ExportToDWGBuilder.SaveAsTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.SaveAsTypeAPI@endlink) SaveAs
    ##  Returns an API to get save as type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ExportToDWGBuilder.SaveAsTypeAPI
    @property
    def SaveAs(self) -> ExportToDWGBuilder.SaveAsTypeAPI:
        """
        Getter for property: (@link ExportToDWGBuilder.SaveAsTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.SaveAsTypeAPI@endlink) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    
    ## Setter for property: (@link ExportToDWGBuilder.SaveAsTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.SaveAsTypeAPI@endlink) SaveAs

    ##  Returns an API to get save as type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SaveAs.setter
    def SaveAs(self, saveAs: ExportToDWGBuilder.SaveAsTypeAPI):
        """
        Setter for property: (@link ExportToDWGBuilder.SaveAsTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.SaveAsTypeAPI@endlink) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    
    ## Getter for property: (@link ExportToDWGBuilder.TemplateTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.TemplateTypeAPI@endlink) TemplateSheet
    ##  Returns the template sheet type   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ExportToDWGBuilder.TemplateTypeAPI
    @property
    def TemplateSheet(self) -> ExportToDWGBuilder.TemplateTypeAPI:
        """
        Getter for property: (@link ExportToDWGBuilder.TemplateTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.TemplateTypeAPI@endlink) TemplateSheet
         Returns the template sheet type   
            
         
        """
        pass
    
    ## Setter for property: (@link ExportToDWGBuilder.TemplateTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.TemplateTypeAPI@endlink) TemplateSheet

    ##  Returns the template sheet type   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TemplateSheet.setter
    def TemplateSheet(self, templateSheet: ExportToDWGBuilder.TemplateTypeAPI):
        """
        Setter for property: (@link ExportToDWGBuilder.TemplateTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.TemplateTypeAPI@endlink) TemplateSheet
         Returns the template sheet type   
            
         
        """
        pass
    
import NXOpen
##  Represents an export to dwg  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::ExportToDWGBuilder  NXOpen::LineDesigner::ExportToDWGBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ExportToDWG(NXOpen.DisplayableObject): 
    """ Represents an export to dwg """
    pass


import NXOpen
##     <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateFactorycadgeoequipmentassemblyBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateFactorycadgeoequipmentassemblyBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class FactoryCadGeoEquipmentAssemblyBuilder(NXOpen.Builder): 
    """   """


    ##  Contains feature update status report 
    ## @link FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct@endlink is an alias for @link FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData@endlink.
    class UpdatedControlData:
        """
         Contains feature update status report 
        @link FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct@endlink is an alias for @link FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData@endlink.
        """
        ## Getter for property :(str) SControlName@return str
        @property
        def SControlName(self) -> str:
            """
            Getter for property SControlName
            """
            pass
        
        ## Setter for property :(str) SControlName
        @SControlName.setter
        def SControlName(self, value: str):
            """
            Getter for property SControlNameSetter for property SControlName
            """
            pass
        
        ## Getter for property :(float) DControlValue@return float
        @property
        def DControlValue(self) -> float:
            """
            Getter for property DControlValue
            """
            pass
        
        ## Setter for property :(float) DControlValue
        @DControlValue.setter
        def DControlValue(self, value: float):
            """
            Getter for property DControlValueSetter for property DControlValue
            """
            pass
        
        ## Getter for property :(float) DMinValue@return float
        @property
        def DMinValue(self) -> float:
            """
            Getter for property DMinValue
            """
            pass
        
        ## Setter for property :(float) DMinValue
        @DMinValue.setter
        def DMinValue(self, value: float):
            """
            Getter for property DMinValueSetter for property DMinValue
            """
            pass
        
        ## Getter for property :(float) DMaxValue@return float
        @property
        def DMaxValue(self) -> float:
            """
            Getter for property DMaxValue
            """
            pass
        
        ## Setter for property :(float) DMaxValue
        @DMaxValue.setter
        def DMaxValue(self, value: float):
            """
            Getter for property DMaxValueSetter for property DMaxValue
            """
            pass
        
        ## Getter for property :(float) DIncrement@return float
        @property
        def DIncrement(self) -> float:
            """
            Getter for property DIncrement
            """
            pass
        
        ## Setter for property :(float) DIncrement
        @DIncrement.setter
        def DIncrement(self, value: float):
            """
            Getter for property DIncrementSetter for property DIncrement
            """
            pass
        
        ## Getter for property :(str) VDblLov@return str
        @property
        def VDblLov(self) -> str:
            """
            Getter for property VDblLov
            """
            pass
        
        ## Setter for property :(str) VDblLov
        @VDblLov.setter
        def VDblLov(self, value: str):
            """
            Getter for property VDblLovSetter for property VDblLov
            """
            pass
        
        ## Getter for property :(str) VStrLov@return str
        @property
        def VStrLov(self) -> str:
            """
            Getter for property VStrLov
            """
            pass
        
        ## Setter for property :(str) VStrLov
        @VStrLov.setter
        def VStrLov(self, value: str):
            """
            Getter for property VStrLovSetter for property VStrLov
            """
            pass
        
        ## Getter for property :(bool) BEnforceValues@return bool
        @property
        def BEnforceValues(self) -> bool:
            """
            Getter for property BEnforceValues
            """
            pass
        
        ## Setter for property :(bool) BEnforceValues
        @BEnforceValues.setter
        def BEnforceValues(self, value: bool):
            """
            Getter for property BEnforceValuesSetter for property BEnforceValues
            """
            pass
        
        ## Getter for property :(bool) BIsEditable@return bool
        @property
        def BIsEditable(self) -> bool:
            """
            Getter for property BIsEditable
            """
            pass
        
        ## Setter for property :(bool) BIsEditable
        @BIsEditable.setter
        def BIsEditable(self, value: bool):
            """
            Getter for property BIsEditableSetter for property BIsEditable
            """
            pass
        
        ## Getter for property :(float) DConversionFactor@return float
        @property
        def DConversionFactor(self) -> float:
            """
            Getter for property DConversionFactor
            """
            pass
        
        ## Setter for property :(float) DConversionFactor
        @DConversionFactor.setter
        def DConversionFactor(self, value: float):
            """
            Getter for property DConversionFactorSetter for property DConversionFactor
            """
            pass
        
    
    
    ##     
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ReadFcadDatasetFiles(self) -> None:
        """
            
        """
        pass
    
    ## Read the FactoryCAD files from folder for native mode
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ReadFcadFiles(self) -> None:
        """
        Read the FactoryCAD files from folder for native mode
        """
        pass
    
    ##     
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="key"> (str) </param>
    ## <param name="tagObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetStringToObjectMap(self, key: str, tagObject: NXOpen.TaggedObject) -> None:
        """
            
        """
        pass
    
    ##     
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="updatedControlDatas"> (@link FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData List[NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData]@endlink) </param>
    def UpdateData(self, updatedControlDatas: List[FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData]) -> None:
        """
            
        """
        pass
    
import NXOpen
##     <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateFactorycadgeoequipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateFactorycadgeoequipmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class FactoryCadGeoEquipmentBuilder(NXOpen.Builder): 
    """   """


    ##  Contains feature update status report 
    ## @link FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct@endlink is an alias for @link FactoryCadGeoEquipmentBuilder.UpdatedControlData NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder.UpdatedControlData@endlink.
    class UpdatedControlData:
        """
         Contains feature update status report 
        @link FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct@endlink is an alias for @link FactoryCadGeoEquipmentBuilder.UpdatedControlData NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder.UpdatedControlData@endlink.
        """
        ## Getter for property :(str) SControlName@return str
        @property
        def SControlName(self) -> str:
            """
            Getter for property SControlName
            """
            pass
        
        ## Setter for property :(str) SControlName
        @SControlName.setter
        def SControlName(self, value: str):
            """
            Getter for property SControlNameSetter for property SControlName
            """
            pass
        
        ## Getter for property :(float) DControlValue@return float
        @property
        def DControlValue(self) -> float:
            """
            Getter for property DControlValue
            """
            pass
        
        ## Setter for property :(float) DControlValue
        @DControlValue.setter
        def DControlValue(self, value: float):
            """
            Getter for property DControlValueSetter for property DControlValue
            """
            pass
        
        ## Getter for property :(float) DMinValue@return float
        @property
        def DMinValue(self) -> float:
            """
            Getter for property DMinValue
            """
            pass
        
        ## Setter for property :(float) DMinValue
        @DMinValue.setter
        def DMinValue(self, value: float):
            """
            Getter for property DMinValueSetter for property DMinValue
            """
            pass
        
        ## Getter for property :(float) DMaxValue@return float
        @property
        def DMaxValue(self) -> float:
            """
            Getter for property DMaxValue
            """
            pass
        
        ## Setter for property :(float) DMaxValue
        @DMaxValue.setter
        def DMaxValue(self, value: float):
            """
            Getter for property DMaxValueSetter for property DMaxValue
            """
            pass
        
        ## Getter for property :(float) DIncrement@return float
        @property
        def DIncrement(self) -> float:
            """
            Getter for property DIncrement
            """
            pass
        
        ## Setter for property :(float) DIncrement
        @DIncrement.setter
        def DIncrement(self, value: float):
            """
            Getter for property DIncrementSetter for property DIncrement
            """
            pass
        
        ## Getter for property :(str) VDblLov@return str
        @property
        def VDblLov(self) -> str:
            """
            Getter for property VDblLov
            """
            pass
        
        ## Setter for property :(str) VDblLov
        @VDblLov.setter
        def VDblLov(self, value: str):
            """
            Getter for property VDblLovSetter for property VDblLov
            """
            pass
        
        ## Getter for property :(str) VStrLov@return str
        @property
        def VStrLov(self) -> str:
            """
            Getter for property VStrLov
            """
            pass
        
        ## Setter for property :(str) VStrLov
        @VStrLov.setter
        def VStrLov(self, value: str):
            """
            Getter for property VStrLovSetter for property VStrLov
            """
            pass
        
        ## Getter for property :(bool) BEnforceValues@return bool
        @property
        def BEnforceValues(self) -> bool:
            """
            Getter for property BEnforceValues
            """
            pass
        
        ## Setter for property :(bool) BEnforceValues
        @BEnforceValues.setter
        def BEnforceValues(self, value: bool):
            """
            Getter for property BEnforceValuesSetter for property BEnforceValues
            """
            pass
        
        ## Getter for property :(bool) BIsEditable@return bool
        @property
        def BIsEditable(self) -> bool:
            """
            Getter for property BIsEditable
            """
            pass
        
        ## Setter for property :(bool) BIsEditable
        @BIsEditable.setter
        def BIsEditable(self, value: bool):
            """
            Getter for property BIsEditableSetter for property BIsEditable
            """
            pass
        
    
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Node
    ##  Returns    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def Node(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Node
         Returns    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Node

    ##  Returns    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Node.setter
    def Node(self, node: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Node
         Returns    
            
         
        """
        pass
    
import NXOpen
##     <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateFloorequipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateFloorequipmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FloorThickness.Value </term> <description> 
##  
## 254 (millimeters part), 10 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class FloorEquipmentBuilder(NXOpen.Builder): 
    """   """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FloorThickness
    ##  Returns the floor thickness   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FloorThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FloorThickness
         Returns the floor thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
    ##  Returns the kf object   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.KFObject
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
         Returns the kf object   
            
         
        """
        pass
    
    ## Getter for property: (bool) MakeSketchInternal
    ##  Returns the make sketchiInternal    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def MakeSketchInternal(self) -> bool:
        """
        Getter for property: (bool) MakeSketchInternal
         Returns the make sketchiInternal    
            
         
        """
        pass
    
    ## Setter for property: (bool) MakeSketchInternal

    ##  Returns the make sketchiInternal    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MakeSketchInternal.setter
    def MakeSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) MakeSketchInternal
         Returns the make sketchiInternal    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectOutline
    ##  Returns the outline used for creation of floor is return   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SelectOutline(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectOutline
         Returns the outline used for creation of floor is return   
            
         
        """
        pass
    
import NXOpen
## 
##     Represents a @link LineDesigner::GateFeature LineDesigner::GateFeature@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateGateFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateGateFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## LinearDimElevation.Value </term> <description> 
##  
## 650 (millimeters part), 25.6 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimGateThickness.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OpeningStyleEnum </term> <description> 
##  
## Left </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class GateFeatureBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.GateFeature</ja_class> builder
    """


    ##  This enum represents gate opening style 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Middle</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item></list>
    class GateOpeningStyle(Enum):
        """
        Members Include: <Left> <Middle> <Right>
        """
        Left: int
        Middle: int
        Right: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GateFeatureBuilder.GateOpeningStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimElevation
    ##  Returns the elevation used for creation of gate   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimElevation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimElevation
         Returns the elevation used for creation of gate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimGateThickness
    ##  Returns the gate thickness   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimGateThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimGateThickness
         Returns the gate thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link GateFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.GateFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum
    ##  Returns the opening style of gate   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return GateFeatureBuilder.GateOpeningStyle
    @property
    def OpeningStyleEnum(self) -> GateFeatureBuilder.GateOpeningStyle:
        """
        Getter for property: (@link GateFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.GateFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum
         Returns the opening style of gate   
            
         
        """
        pass
    
    ## Setter for property: (@link GateFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.GateFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum

    ##  Returns the opening style of gate   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OpeningStyleEnum.setter
    def OpeningStyleEnum(self, openingStyleEnum: GateFeatureBuilder.GateOpeningStyle):
        """
        Setter for property: (@link GateFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.GateFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum
         Returns the opening style of gate   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a gate feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::GateFeatureBuilder  NXOpen::LineDesigner::GateFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class GateFeature(NXOpen.Features.Feature): 
    """ Represents a gate feature """
    pass


import NXOpen
##  Global Selection  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateGlobalSelectionBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateGlobalSelectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class GlobalSelectionBuilder(NXOpen.Builder): 
    """ Global Selection """


    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Selection
    ##  Returns the selected objects   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Selection(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Selection
         Returns the selected objects   
            
         
        """
        pass
    
##  Represents a typed connector feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::TypedConnectorFeatureBuilder  NXOpen::LineDesigner::TypedConnectorFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class HeadConnectorFeature(TypedConnectorFeature): 
    """ Represents a typed connector feature feature """
    pass


import NXOpen
import NXOpen.Features
## 
##     Represents a @link LineDesigner::HoleFeature LineDesigner::HoleFeature@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateHoleFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateHoleFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AddCover </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CoverThickness.Value </term> <description> 
##  
## 127 (millimeters part), 5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LoadRequirements </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TextSize </term> <description> 
##  
## 60 </description> </item> 
## 
## <item><term> 
##  
## UseCoverOffset </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class HoleFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>LineDesigner.HoleFeature</ja_class> builder
    """


    ## Getter for property: (bool) AddCover
    ##  Returns the presence of cover over hole is checked  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AddCover(self) -> bool:
        """
        Getter for property: (bool) AddCover
         Returns the presence of cover over hole is checked  
            
         
        """
        pass
    
    ## Setter for property: (bool) AddCover

    ##  Returns the presence of cover over hole is checked  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AddCover.setter
    def AddCover(self, addCover: bool):
        """
        Setter for property: (bool) AddCover
         Returns the presence of cover over hole is checked  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CoverThickness
    ##  Returns the cover thickness   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CoverThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CoverThickness
         Returns the cover thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) LoadRequirements
    ##  Returns the load requirements   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LoadRequirements(self) -> float:
        """
        Getter for property: (float) LoadRequirements
         Returns the load requirements   
            
         
        """
        pass
    
    ## Setter for property: (float) LoadRequirements

    ##  Returns the load requirements   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LoadRequirements.setter
    def LoadRequirements(self, loadRequirements: float):
        """
        Setter for property: (float) LoadRequirements
         Returns the load requirements   
            
         
        """
        pass
    
    ## Getter for property: (bool) MakeSketchInternal
    ##  Returns    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def MakeSketchInternal(self) -> bool:
        """
        Getter for property: (bool) MakeSketchInternal
         Returns    
            
         
        """
        pass
    
    ## Setter for property: (bool) MakeSketchInternal

    ##  Returns    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MakeSketchInternal.setter
    def MakeSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) MakeSketchInternal
         Returns    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectOutline
    ##  Returns the selected outline for creation of hole   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SelectOutline(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectOutline
         Returns the selected outline for creation of hole   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation
    ##  Returns the text location of hole   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def TextLocation(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation
         Returns the text location of hole   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation

    ##  Returns the text location of hole   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TextLocation.setter
    def TextLocation(self, textLocation: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextLocation
         Returns the text location of hole   
            
         
        """
        pass
    
    ## Getter for property: (float) TextSize
    ##  Returns the text size   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def TextSize(self) -> float:
        """
        Getter for property: (float) TextSize
         Returns the text size   
            
         
        """
        pass
    
    ## Setter for property: (float) TextSize

    ##  Returns the text size   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TextSize.setter
    def TextSize(self, textSize: float):
        """
        Setter for property: (float) TextSize
         Returns the text size   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseCoverOffset
    ##  Returns the cover offset is return, if cover is present over hole   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def UseCoverOffset(self) -> bool:
        """
        Getter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseCoverOffset

    ##  Returns the cover offset is return, if cover is present over hole   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UseCoverOffset.setter
    def UseCoverOffset(self, useCoverOffset: bool):
        """
        Setter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    
    ##  Get text string 
    ##  @return enterTextString (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetEnterTextString(self) -> List[str]:
        """
         Get text string 
         @return enterTextString (List[str]): .
        """
        pass
    
    ##  Set text string 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="enterTextString"> (List[str])  </param>
    def SetEnterTextString(self, enterTextString: List[str]) -> None:
        """
         Set text string 
        """
        pass
    
import NXOpen.Features
##  Represents a hole feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::HoleFeatureBuilder  NXOpen::LineDesigner::HoleFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class HoleFeature(NXOpen.Features.BodyFeature): 
    """ Represents a hole feature feature """
    pass


import NXOpen
##  
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateImportFactoryCadGeoBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateImportFactoryCadGeoBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ImportFactoryCadGeoBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """


    ## Getter for property: (str) DlgFileName
    ##  Returns the path of dlg file which user wants to import in NX   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    ## @return str
    @property
    def DlgFileName(self) -> str:
        """
        Getter for property: (str) DlgFileName
         Returns the path of dlg file which user wants to import in NX   
            
         
        """
        pass
    
    ## Setter for property: (str) DlgFileName

    ##  Returns the path of dlg file which user wants to import in NX   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    @DlgFileName.setter
    def DlgFileName(self, dlgFileName: str):
        """
        Setter for property: (str) DlgFileName
         Returns the path of dlg file which user wants to import in NX   
            
         
        """
        pass
    
    ## Getter for property: (str) GeoFileName
    ##  Returns the path of geo file which user wants to import in NX   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def GeoFileName(self) -> str:
        """
        Getter for property: (str) GeoFileName
         Returns the path of geo file which user wants to import in NX   
            
         
        """
        pass
    
    ## Setter for property: (str) GeoFileName

    ##  Returns the path of geo file which user wants to import in NX   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @GeoFileName.setter
    def GeoFileName(self, geoFileName: str):
        """
        Setter for property: (str) GeoFileName
         Returns the path of geo file which user wants to import in NX   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsInEditMode
    ##  Returns an in edit mode when dialog is opening before inserting object   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    ## @return bool
    @property
    def IsInEditMode(self) -> bool:
        """
        Getter for property: (bool) IsInEditMode
         Returns an in edit mode when dialog is opening before inserting object   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsInEditMode

    ##  Returns an in edit mode when dialog is opening before inserting object   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    @IsInEditMode.setter
    def IsInEditMode(self, bIsInEditMode: bool):
        """
        Setter for property: (bool) IsInEditMode
         Returns an in edit mode when dialog is opening before inserting object   
            
         
        """
        pass
    
    ## Getter for property: (str) ParameterSetFileName
    ##  Returns the path of parameter set file which user wants to import in NX   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    ## @return str
    @property
    def ParameterSetFileName(self) -> str:
        """
        Getter for property: (str) ParameterSetFileName
         Returns the path of parameter set file which user wants to import in NX   
            
         
        """
        pass
    
    ## Setter for property: (str) ParameterSetFileName

    ##  Returns the path of parameter set file which user wants to import in NX   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    @ParameterSetFileName.setter
    def ParameterSetFileName(self, parameterSetFileName: str):
        """
        Setter for property: (str) ParameterSetFileName
         Returns the path of parameter set file which user wants to import in NX   
            
         
        """
        pass
    
    ##    
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="factoryCadGeoPartTag"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def LoadFactoryCadGeoBuilderToData(self, factoryCadGeoPartTag: NXOpen.Part) -> None:
        """
           
        """
        pass
    
import NXOpen
## 
##     Represents a @link LineDesigner::InsertSheet LineDesigner::InsertSheet@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateInsertSheetBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateInsertSheetBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## UnitsEnum </term> <description> 
##  
## Millimeters </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class InsertSheetBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.InsertSheet</ja_class> builder
    """


    ##  This enum represents the units types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Millimeters</term><description> 
    ##  Represents the Millimeters type </description> </item><item><term> 
    ## Inches</term><description> 
    ##  Represents the Inches type </description> </item></list>
    class APIUnits(Enum):
        """
        Members Include: <Millimeters> <Inches>
        """
        Millimeters: int
        Inches: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InsertSheetBuilder.APIUnits:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) NameString
    ##  Returns the name string   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def NameString(self) -> str:
        """
        Getter for property: (str) NameString
         Returns the name string   
            
         
        """
        pass
    
    ## Setter for property: (str) NameString

    ##  Returns the name string   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NameString.setter
    def NameString(self, nameString: str):
        """
        Setter for property: (str) NameString
         Returns the name string   
            
         
        """
        pass
    
    ## Getter for property: (str) NumberString
    ##  Returns the number string   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def NumberString(self) -> str:
        """
        Getter for property: (str) NumberString
         Returns the number string   
            
         
        """
        pass
    
    ## Setter for property: (str) NumberString

    ##  Returns the number string   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NumberString.setter
    def NumberString(self, numberString: str):
        """
        Setter for property: (str) NumberString
         Returns the number string   
            
         
        """
        pass
    
    ## Getter for property: (str) RevisionString
    ##  Returns the revision string   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def RevisionString(self) -> str:
        """
        Getter for property: (str) RevisionString
         Returns the revision string   
            
         
        """
        pass
    
    ## Setter for property: (str) RevisionString

    ##  Returns the revision string   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @RevisionString.setter
    def RevisionString(self, revisionString: str):
        """
        Setter for property: (str) RevisionString
         Returns the revision string   
            
         
        """
        pass
    
    ## Getter for property: (int) ScaleEnum
    ##  Returns the scale enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ScaleEnum(self) -> int:
        """
        Getter for property: (int) ScaleEnum
         Returns the scale enum   
            
         
        """
        pass
    
    ## Setter for property: (int) ScaleEnum

    ##  Returns the scale enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ScaleEnum.setter
    def ScaleEnum(self, scaleEnum: int):
        """
        Setter for property: (int) ScaleEnum
         Returns the scale enum   
            
         
        """
        pass
    
    ## Getter for property: (str) SecondaryNumberString
    ##  Returns the secondary number string   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def SecondaryNumberString(self) -> str:
        """
        Getter for property: (str) SecondaryNumberString
         Returns the secondary number string   
            
         
        """
        pass
    
    ## Setter for property: (str) SecondaryNumberString

    ##  Returns the secondary number string   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SecondaryNumberString.setter
    def SecondaryNumberString(self, secondaryNumberString: str):
        """
        Setter for property: (str) SecondaryNumberString
         Returns the secondary number string   
            
         
        """
        pass
    
    ## Getter for property: (int) SizeEnum
    ##  Returns the size enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def SizeEnum(self) -> int:
        """
        Getter for property: (int) SizeEnum
         Returns the size enum   
            
         
        """
        pass
    
    ## Setter for property: (int) SizeEnum

    ##  Returns the size enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SizeEnum.setter
    def SizeEnum(self, sizeEnum: int):
        """
        Setter for property: (int) SizeEnum
         Returns the size enum   
            
         
        """
        pass
    
    ## Getter for property: (@link InsertSheetBuilder.APIUnits NXOpen.LineDesigner.InsertSheetBuilder.APIUnits@endlink) UnitsEnum
    ##  Returns the units enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return InsertSheetBuilder.APIUnits
    @property
    def UnitsEnum(self) -> InsertSheetBuilder.APIUnits:
        """
        Getter for property: (@link InsertSheetBuilder.APIUnits NXOpen.LineDesigner.InsertSheetBuilder.APIUnits@endlink) UnitsEnum
         Returns the units enum   
            
         
        """
        pass
    
    ## Setter for property: (@link InsertSheetBuilder.APIUnits NXOpen.LineDesigner.InsertSheetBuilder.APIUnits@endlink) UnitsEnum

    ##  Returns the units enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UnitsEnum.setter
    def UnitsEnum(self, unitsEnum: InsertSheetBuilder.APIUnits):
        """
        Setter for property: (@link InsertSheetBuilder.APIUnits NXOpen.LineDesigner.InsertSheetBuilder.APIUnits@endlink) UnitsEnum
         Returns the units enum   
            
         
        """
        pass
    
import NXOpen.Drawings
##  Represents an insert sheet  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::InsertSheetBuilder  NXOpen::LineDesigner::InsertSheetBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class InsertSheet(NXOpen.Drawings.DrawingSheet): 
    """ Represents an insert sheet """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Jig on plane  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateJigOnPlaneBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateJigOnPlaneBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class JigOnPlaneBuilder(NXOpen.TaggedObject): 
    """ Jig on plane """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedPoints
    ##  Returnsthe selected points   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectedPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedPoints
         Returnsthe selected points   
            
         
        """
        pass
    
    ##  Selected jig plane matrix 
    ##  @return A tuple consisting of (rotation, origin). 
    ##  - rotation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.
    ##  - origin is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetJigPlaneParams(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Vector3d]:
        """
         Selected jig plane matrix 
         @return A tuple consisting of (rotation, origin). 
         - rotation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.
         - origin is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.

        """
        pass
    
import NXOpen
## 
##     Represents a class to create enter and exit the LineDesigner application
##     
## 
##   <br>  Created in NX9.0.0  <br> 

class LineDesignerApplicationBuilder(NXOpen.NXObject): 
    """
    Represents a class to create enter and exit the LineDesigner application
    """


    ##  To enter lineDesigner application 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def Enter(self) -> None:
        """
         To enter lineDesigner application 
        """
        pass
    
    ##  To exit LineDesigner application this call will destroy the builder
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def Exit(self) -> None:
        """
         To exit LineDesigner application this call will destroy the builder
        """
        pass
    
    ##  To get the global selection builder
    ##  @return selectionBuilder (@link GlobalSelectionBuilder NXOpen.LineDesigner.GlobalSelectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetGlobalSelectionBuilder(self) -> GlobalSelectionBuilder:
        """
         To get the global selection builder
         @return selectionBuilder (@link GlobalSelectionBuilder NXOpen.LineDesigner.GlobalSelectionBuilder@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Drawings
##  Represents a manager of line designer builders  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class LineDesignerManager(NXOpen.Object): 
    """ Represents a manager of line designer builders """


    ##   Consolidate Undo Marks 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="undoMarkId"> (int) </param>
    def ConsolidateUndoMarks(undoMarkId: int) -> None:
        """
          Consolidate Undo Marks 
        """
        pass
    
    ##  Creates a Add PMI Occ Note Builder
    ##  @return builder (@link AddPMIOccNoteBuilder NXOpen.LineDesigner.AddPMIOccNoteBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partOccTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateAddPmiOccNoteBuilder(partOccTag: NXOpen.TaggedObject) -> AddPMIOccNoteBuilder:
        """
         Creates a Add PMI Occ Note Builder
         @return builder (@link AddPMIOccNoteBuilder NXOpen.LineDesigner.AddPMIOccNoteBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Add Type Attribute Builder
    ##  @return builder (@link AddTypeAttributeBuilder NXOpen.LineDesigner.AddTypeAttributeBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAddTypeAttributeBuilder(part: NXOpen.Part) -> AddTypeAttributeBuilder:
        """
         Creates a Add Type Attribute Builder
         @return builder (@link AddTypeAttributeBuilder NXOpen.LineDesigner.AddTypeAttributeBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Add Workarea builder
    ##  @return builder (@link AddWorkareaBuilder NXOpen.LineDesigner.AddWorkareaBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAddWorkareaBuilder(part: NXOpen.Part) -> AddWorkareaBuilder:
        """
         Creates a Add Workarea builder
         @return builder (@link AddWorkareaBuilder NXOpen.LineDesigner.AddWorkareaBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Align Component Dialoge Builder
    ##  @return builder (@link AlignComponentsBuilder NXOpen.LineDesigner.AlignComponentsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAlignComponentsBuilder(part: NXOpen.Part) -> AlignComponentsBuilder:
        """
         Creates a Align Component Dialoge Builder
         @return builder (@link AlignComponentsBuilder NXOpen.LineDesigner.AlignComponentsBuilder@endlink): .
        """
        pass
    
    ##  Creates a AllowWorkareaTypes builder
    ##  @return builder (@link AllowWorkareaTypesBuilder NXOpen.LineDesigner.AllowWorkareaTypesBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAllowWorkareaTypesBuilder(part: NXOpen.Part) -> AllowWorkareaTypesBuilder:
        """
         Creates a AllowWorkareaTypes builder
         @return builder (@link AllowWorkareaTypesBuilder NXOpen.LineDesigner.AllowWorkareaTypesBuilder@endlink):  .
        """
        pass
    
    ##  Create the application builder 
    ##  @return builder (@link LineDesignerApplicationBuilder NXOpen.LineDesigner.LineDesignerApplicationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateApplicationBuilder(part: NXOpen.Part) -> LineDesignerApplicationBuilder:
        """
         Create the application builder 
         @return builder (@link LineDesignerApplicationBuilder NXOpen.LineDesigner.LineDesignerApplicationBuilder@endlink):  .
        """
        pass
    
    ##  Create column feature builder 
    ##  @return builder (@link ColumnFeatureBuilder NXOpen.LineDesigner.ColumnFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="column_feature"> (@link ColumnFeature NXOpen.LineDesigner.ColumnFeature@endlink)  @link LineDesigner::ColumnFeature LineDesigner::ColumnFeature@endlink  to be edited </param>
    @overload
    def CreateColumnFeatureBuilder(part: NXOpen.Part, column_feature: ColumnFeature) -> ColumnFeatureBuilder:
        """
         Create column feature builder 
         @return builder (@link ColumnFeatureBuilder NXOpen.LineDesigner.ColumnFeatureBuilder@endlink):  .
        """
        pass
    
    ## Create column feature builder inside a node or using node 
    ##  @return builder (@link ColumnFeatureBuilder NXOpen.LineDesigner.ColumnFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="node"> (@link DBNode NXOpen.LineDesigner.DBNode@endlink) </param>
    @overload
    def CreateColumnFeatureBuilder(part: NXOpen.Part, node: DBNode) -> ColumnFeatureBuilder:
        """
        Create column feature builder inside a node or using node 
         @return builder (@link ColumnFeatureBuilder NXOpen.LineDesigner.ColumnFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Create column grid equipment Builder 
    ##  @return builder (@link ColumnGridEquipmentBuilder NXOpen.LineDesigner.ColumnGridEquipmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="dbnode"> (@link DBColumnGridNode NXOpen.LineDesigner.DBColumnGridNode@endlink)  </param>
    def CreateColumnGridEquipmentBuilder(part: NXOpen.Part, dbnode: DBColumnGridNode) -> ColumnGridEquipmentBuilder:
        """
         Create column grid equipment Builder 
         @return builder (@link ColumnGridEquipmentBuilder NXOpen.LineDesigner.ColumnGridEquipmentBuilder@endlink):  .
        """
        pass
    
    ##  Create Connection Creator Builder
    ##  @return builder (@link ConnectionCreatorBuilder NXOpen.LineDesigner.ConnectionCreatorBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateConnectionCreatorBuilder(part: NXOpen.Part) -> ConnectionCreatorBuilder:
        """
         Create Connection Creator Builder
         @return builder (@link ConnectionCreatorBuilder NXOpen.LineDesigner.ConnectionCreatorBuilder@endlink):  .
        """
        pass
    
    ##  Create conveyor station feature builder 
    ##  @return builder (@link ConveyorStationFeatureBuilder NXOpen.LineDesigner.ConveyorStationFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="railing_feature"> (@link ConveyorStationFeature NXOpen.LineDesigner.ConveyorStationFeature@endlink)  @link LineDesigner::ConveyorStationFeature LineDesigner::ConveyorStationFeature@endlink  to be edited </param>
    def CreateConveyorStationFeatureBuilder(part: NXOpen.Part, railing_feature: ConveyorStationFeature) -> ConveyorStationFeatureBuilder:
        """
         Create conveyor station feature builder 
         @return builder (@link ConveyorStationFeatureBuilder NXOpen.LineDesigner.ConveyorStationFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Create CoverFeature builder 
    ##  @return builder (@link CoverFeatureBuilder NXOpen.LineDesigner.CoverFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="cover_feature"> (@link CoverFeature NXOpen.LineDesigner.CoverFeature@endlink)  @link LineDesigner::CoverFeature LineDesigner::CoverFeature@endlink  to be edited </param>
    def CreateCoverFeatureBuilder(part: NXOpen.Part, cover_feature: CoverFeature) -> CoverFeatureBuilder:
        """
         Create CoverFeature builder 
         @return builder (@link CoverFeatureBuilder NXOpen.LineDesigner.CoverFeatureBuilder@endlink):  .
        """
        pass
    
    ## Create factory element builder 
    ##  @return builder (@link CreateFactoryElementBuilder NXOpen.LineDesigner.CreateFactoryElementBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="create_factory_element"> (@link CreateFactoryElement NXOpen.LineDesigner.CreateFactoryElement@endlink)  @link LineDesigner::CreateFactoryElement LineDesigner::CreateFactoryElement@endlink  to be edited </param>
    def CreateCreateFactoryElementBuilder(part: NXOpen.Part, create_factory_element: CreateFactoryElement) -> CreateFactoryElementBuilder:
        """
        Create factory element builder 
         @return builder (@link CreateFactoryElementBuilder NXOpen.LineDesigner.CreateFactoryElementBuilder@endlink):  .
        """
        pass
    
    ##  Create fence builder 
    ##  @return builder (@link CreateFenceBuilder NXOpen.LineDesigner.CreateFenceBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="create_fence"> (@link CreateFence NXOpen.LineDesigner.CreateFence@endlink)  @link LineDesigner::CreateFence LineDesigner::CreateFence@endlink  to be edited </param>
    def CreateCreateFenceBuilder(part: NXOpen.Part, create_fence: CreateFence) -> CreateFenceBuilder:
        """
         Create fence builder 
         @return builder (@link CreateFenceBuilder NXOpen.LineDesigner.CreateFenceBuilder@endlink):  .
        """
        pass
    
    ##  Create system builder 
    ##  @return builder (@link CreateSystemBuilder NXOpen.LineDesigner.CreateSystemBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="create_system"> (@link CreateSystem NXOpen.LineDesigner.CreateSystem@endlink)  @link LineDesigner::CreateSystem LineDesigner::CreateSystem@endlink  to be edited </param>
    def CreateCreateSystemBuilder(part: NXOpen.Part, create_system: CreateSystem) -> CreateSystemBuilder:
        """
         Create system builder 
         @return builder (@link CreateSystemBuilder NXOpen.LineDesigner.CreateSystemBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Define Robot Dialoge Builder
    ##  @return builder (@link DefineRobotBuilder NXOpen.LineDesigner.DefineRobotBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDefineRobotBuilder(part: NXOpen.Part) -> DefineRobotBuilder:
        """
         Creates a Define Robot Dialoge Builder
         @return builder (@link DefineRobotBuilder NXOpen.LineDesigner.DefineRobotBuilder@endlink): .
        """
        pass
    
    ##  Creates a Define Tool Dialoge Builder
    ##  @return builder (@link DefineToolBuilder NXOpen.LineDesigner.DefineToolBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDefineToolBuilder(part: NXOpen.Part) -> DefineToolBuilder:
        """
         Creates a Define Tool Dialoge Builder
         @return builder (@link DefineToolBuilder NXOpen.LineDesigner.DefineToolBuilder@endlink): .
        """
        pass
    
    ##  Create Disconnect Connection Builder
    ##  @return builder (@link DisconnectConnectionBuilder NXOpen.LineDesigner.DisconnectConnectionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDisconnectConnectionBuilder(part: NXOpen.Part) -> DisconnectConnectionBuilder:
        """
         Create Disconnect Connection Builder
         @return builder (@link DisconnectConnectionBuilder NXOpen.LineDesigner.DisconnectConnectionBuilder@endlink):  .
        """
        pass
    
    ##  To create distribute components builder
    ##  @return builder (@link DistributeComponentsBuilder NXOpen.LineDesigner.DistributeComponentsBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDistributeComponentsBuilder(part: NXOpen.Part) -> DistributeComponentsBuilder:
        """
         To create distribute components builder
         @return builder (@link DistributeComponentsBuilder NXOpen.LineDesigner.DistributeComponentsBuilder@endlink):  .
        """
        pass
    
    ##  Creates a End Item assembly State Builder
    ##  @return builder (@link EndItemAssemblyStateBuilder NXOpen.LineDesigner.EndItemAssemblyStateBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="appObjectTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateEndItemAssemblyStateBuilder(appObjectTag: NXOpen.TaggedObject) -> EndItemAssemblyStateBuilder:
        """
         Creates a End Item assembly State Builder
         @return builder (@link EndItemAssemblyStateBuilder NXOpen.LineDesigner.EndItemAssemblyStateBuilder@endlink):  .
        """
        pass
    
    ##  Creates an Enhanced 2D shadow outline Dialoge Builder
    ##  @return builder (@link EnhancedShadowOutLineBuilder NXOpen.LineDesigner.EnhancedShadowOutLineBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateEnhancedShadowOutLineBuilder(part: NXOpen.Part) -> EnhancedShadowOutLineBuilder:
        """
         Creates an Enhanced 2D shadow outline Dialoge Builder
         @return builder (@link EnhancedShadowOutLineBuilder NXOpen.LineDesigner.EnhancedShadowOutLineBuilder@endlink):  .
        """
        pass
    
    ##  Create the export plant to DWG builder 
    ##  @return builder (@link ExportPlantToDWGBuilder NXOpen.LineDesigner.ExportPlantToDWGBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="export_plant_to_dwg"> (@link ExportPlantToDWG NXOpen.LineDesigner.ExportPlantToDWG@endlink)  @link LineDesigner::ExportPlantToDWG LineDesigner::ExportPlantToDWG@endlink  to be edited </param>
    def CreateExportPlantToDwgBuilder(part: NXOpen.Part, export_plant_to_dwg: ExportPlantToDWG) -> ExportPlantToDWGBuilder:
        """
         Create the export plant to DWG builder 
         @return builder (@link ExportPlantToDWGBuilder NXOpen.LineDesigner.ExportPlantToDWGBuilder@endlink):  .
        """
        pass
    
    ##  Creates the export to DWG builder 
    ##  @return builder (@link ExportToDWGBuilder NXOpen.LineDesigner.ExportToDWGBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="export_to_dwg"> (@link ExportToDWG NXOpen.LineDesigner.ExportToDWG@endlink)  @link LineDesigner::ExportToDWG LineDesigner::ExportToDWG@endlink  to be edited </param>
    def CreateExportToDwgBuilder(part: NXOpen.Part, export_to_dwg: ExportToDWG) -> ExportToDWGBuilder:
        """
         Creates the export to DWG builder 
         @return builder (@link ExportToDWGBuilder NXOpen.LineDesigner.ExportToDWGBuilder@endlink):  .
        """
        pass
    
    ##  To create a rename factory cad geo equipment builder
    ##  @return builder (@link FactoryCadGeoEquipmentBuilder NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="dbnode"> (@link DBFactoryCadGeoNode NXOpen.LineDesigner.DBFactoryCadGeoNode@endlink)  </param>
    def CreateFactorycadgeoequipmentBuilder(part: NXOpen.Part, dbnode: DBFactoryCadGeoNode) -> FactoryCadGeoEquipmentBuilder:
        """
         To create a rename factory cad geo equipment builder
         @return builder (@link FactoryCadGeoEquipmentBuilder NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder@endlink):  .
        """
        pass
    
    ##  To create a rename factory cad geo equipment assembly builder
    ##  @return builder (@link FactoryCadGeoEquipmentBuilder NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateFactorycadgeoequipmentassemblyBuilder(part: NXOpen.Part) -> FactoryCadGeoEquipmentBuilder:
        """
         To create a rename factory cad geo equipment assembly builder
         @return builder (@link FactoryCadGeoEquipmentBuilder NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder@endlink):  .
        """
        pass
    
    ## Create Floor builder 
    ##  @return builder (@link FloorEquipmentBuilder NXOpen.LineDesigner.FloorEquipmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="dbnode"> (@link DBFloorEquipmentNode NXOpen.LineDesigner.DBFloorEquipmentNode@endlink)  </param>
    def CreateFloorequipmentBuilder(part: NXOpen.Part, dbnode: DBFloorEquipmentNode) -> FloorEquipmentBuilder:
        """
        Create Floor builder 
         @return builder (@link FloorEquipmentBuilder NXOpen.LineDesigner.FloorEquipmentBuilder@endlink):  .
        """
        pass
    
    ##  Create GateFeature builder 
    ##  @return builder (@link GateFeatureBuilder NXOpen.LineDesigner.GateFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="cover_feature"> (@link GateFeature NXOpen.LineDesigner.GateFeature@endlink)  @link LineDesigner::GateFeature LineDesigner::GateFeature@endlink  to be edited </param>
    def CreateGateFeatureBuilder(part: NXOpen.Part, cover_feature: GateFeature) -> GateFeatureBuilder:
        """
         Create GateFeature builder 
         @return builder (@link GateFeatureBuilder NXOpen.LineDesigner.GateFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Create global selection builder 
    ##  @return builder (@link GlobalSelectionBuilder NXOpen.LineDesigner.GlobalSelectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateGlobalSelectionBuilder(part: NXOpen.Part) -> GlobalSelectionBuilder:
        """
         Create global selection builder 
         @return builder (@link GlobalSelectionBuilder NXOpen.LineDesigner.GlobalSelectionBuilder@endlink): .
        """
        pass
    
    ##  Create HoleFeature builder 
    ##  @return builder (@link HoleFeatureBuilder NXOpen.LineDesigner.HoleFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="hole_feature"> (@link HoleFeature NXOpen.LineDesigner.HoleFeature@endlink)  @link LineDesigner::HoleFeature LineDesigner::HoleFeature@endlink  to be edited </param>
    def CreateHoleFeatureBuilder(part: NXOpen.Part, hole_feature: HoleFeature) -> HoleFeatureBuilder:
        """
         Create HoleFeature builder 
         @return builder (@link HoleFeatureBuilder NXOpen.LineDesigner.HoleFeatureBuilder@endlink):  .
        """
        pass
    
    ##  To get the import factory cad geo builder 
    ##  @return builder (@link ImportFactoryCadGeoBuilder NXOpen.LineDesigner.ImportFactoryCadGeoBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateImportFactoryCadGeoBuilder(part: NXOpen.Part) -> ImportFactoryCadGeoBuilder:
        """
         To get the import factory cad geo builder 
         @return builder (@link ImportFactoryCadGeoBuilder NXOpen.LineDesigner.ImportFactoryCadGeoBuilder@endlink): .
        """
        pass
    
    ##  Creates the insert sheet builder 
    ##  @return builder (@link InsertSheetBuilder NXOpen.LineDesigner.InsertSheetBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="insert_sheet"> (@link InsertSheet NXOpen.LineDesigner.InsertSheet@endlink)  @link LineDesigner::InsertSheet LineDesigner::InsertSheet@endlink  to be edited </param>
    def CreateInsertSheetBuilder(part: NXOpen.Part, insert_sheet: InsertSheet) -> InsertSheetBuilder:
        """
         Creates the insert sheet builder 
         @return builder (@link InsertSheetBuilder NXOpen.LineDesigner.InsertSheetBuilder@endlink):  .
        """
        pass
    
    ## Create the jig on plane builder 
    ##  @return builder (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateJigOnPlaneBuilder(part: NXOpen.Part) -> JigOnPlaneBuilder:
        """
        Create the jig on plane builder 
         @return builder (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Connector List Builder
    ##  @return builder (@link ListOfConnectorsBuilder NXOpen.LineDesigner.ListOfConnectorsBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateListOfConnectorsBuilder(part: NXOpen.Part) -> ListOfConnectorsBuilder:
        """
         Creates a Connector List Builder
         @return builder (@link ListOfConnectorsBuilder NXOpen.LineDesigner.ListOfConnectorsBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Modify Connected System Builder
    ##  @return builder (@link ModifyConnectedSystemBuilder NXOpen.LineDesigner.ModifyConnectedSystemBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateModifyConnectedSystemBuilder(part: NXOpen.Part) -> ModifyConnectedSystemBuilder:
        """
         Creates a Modify Connected System Builder
         @return builder (@link ModifyConnectedSystemBuilder NXOpen.LineDesigner.ModifyConnectedSystemBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Mount Dialoge Builder
    ##  @return builder (@link MountBuilder NXOpen.LineDesigner.MountBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateMountBuilder(part: NXOpen.Part) -> MountBuilder:
        """
         Creates a Mount Dialoge Builder
         @return builder (@link MountBuilder NXOpen.LineDesigner.MountBuilder@endlink):  .
        """
        pass
    
    ## Create pick rectangle points builder 
    ##  @return builder (@link PickRectanglePointsBuilder NXOpen.LineDesigner.PickRectanglePointsBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePickRectanglePointsBuilder(part: NXOpen.Part) -> PickRectanglePointsBuilder:
        """
        Create pick rectangle points builder 
         @return builder (@link PickRectanglePointsBuilder NXOpen.LineDesigner.PickRectanglePointsBuilder@endlink):  .
        """
        pass
    
    ##  Creates the plan view manager instance 
    ##  @return planViewManager (@link PlanViewManager NXOpen.LineDesigner.PlanViewManager@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePlanViewManagerInstance(part: NXOpen.Part) -> PlanViewManager:
        """
         Creates the plan view manager instance 
         @return planViewManager (@link PlanViewManager NXOpen.LineDesigner.PlanViewManager@endlink): .
        """
        pass
    
    ##  Creates a Plant Sim attribute exchange  Builder
    ##  @return builder (@link PlantSimExchangeBuilder NXOpen.LineDesigner.PlantSimExchangeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePlantSimExchangeBuilder(part: NXOpen.Part) -> PlantSimExchangeBuilder:
        """
         Creates a Plant Sim attribute exchange  Builder
         @return builder (@link PlantSimExchangeBuilder NXOpen.LineDesigner.PlantSimExchangeBuilder@endlink): .
        """
        pass
    
    ##  Create Platform Equipment Builder 
    ##  @return builder (@link PlatformEquipmentBuilder NXOpen.LineDesigner.PlatformEquipmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="dbnode"> (@link DBPlatformEquipmentNode NXOpen.LineDesigner.DBPlatformEquipmentNode@endlink)  </param>
    def CreatePlatformEquipmentBuilder(part: NXOpen.Part, dbnode: DBPlatformEquipmentNode) -> PlatformEquipmentBuilder:
        """
         Create Platform Equipment Builder 
         @return builder (@link PlatformEquipmentBuilder NXOpen.LineDesigner.PlatformEquipmentBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Preferences builder
    ##  @return builder (@link PreferencesBuilder NXOpen.LineDesigner.PreferencesBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePreferencesBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates a Preferences builder
         @return builder (@link PreferencesBuilder NXOpen.LineDesigner.PreferencesBuilder@endlink):  .
        """
        pass
    
    ##  Create production unit creator builder 
    ##  @return builder (@link ProductionUnitCreatorBuilder NXOpen.LineDesigner.ProductionUnitCreatorBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateProductionUnitCreatorBuilder(part: NXOpen.Part) -> ProductionUnitCreatorBuilder:
        """
         Create production unit creator builder 
         @return builder (@link ProductionUnitCreatorBuilder NXOpen.LineDesigner.ProductionUnitCreatorBuilder@endlink):  .
        """
        pass
    
    ##  Create rail opening feature builder 
    ##  @return builder (@link RailOpeningFeatureBuilder NXOpen.LineDesigner.RailOpeningFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="railing_feature"> (@link RailOpeningFeature NXOpen.LineDesigner.RailOpeningFeature@endlink)  @link LineDesigner::RailOpeningFeature LineDesigner::RailOpeningFeature@endlink  to be edited </param>
    def CreateRailOpeningFeatureBuilder(part: NXOpen.Part, railing_feature: RailOpeningFeature) -> RailOpeningFeatureBuilder:
        """
         Create rail opening feature builder 
         @return builder (@link RailOpeningFeatureBuilder NXOpen.LineDesigner.RailOpeningFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Create railing feature builder 
    ##  @return builder (@link RailingFeatureBuilder NXOpen.LineDesigner.RailingFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="railing_feature"> (@link RailingFeature NXOpen.LineDesigner.RailingFeature@endlink)  @link LineDesigner::RailingFeature LineDesigner::RailingFeature@endlink  to be edited </param>
    @overload
    def CreateRailingFeatureBuilder(part: NXOpen.Part, railing_feature: RailingFeature) -> RailingFeatureBuilder:
        """
         Create railing feature builder 
         @return builder (@link RailingFeatureBuilder NXOpen.LineDesigner.RailingFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Create railing feature builder 
    ##  @return builder (@link RailingFeatureBuilder NXOpen.LineDesigner.RailingFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="node"> (@link DBNode NXOpen.LineDesigner.DBNode@endlink) </param>
    @overload
    def CreateRailingFeatureBuilder(part: NXOpen.Part, node: DBNode) -> RailingFeatureBuilder:
        """
         Create railing feature builder 
         @return builder (@link RailingFeatureBuilder NXOpen.LineDesigner.RailingFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Rename Dialoge Builder
    ##  @return builder (@link RenameDialogeBuilder NXOpen.LineDesigner.RenameDialogeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateRenameDialogeBuilder(part: NXOpen.Part) -> RenameDialogeBuilder:
        """
         Creates a Rename Dialoge Builder
         @return builder (@link RenameDialogeBuilder NXOpen.LineDesigner.RenameDialogeBuilder@endlink): .
        """
        pass
    
    ##  To create a rename ItemRevision Builder
    ##  @return builder (@link RenameItemRevisionBuilder NXOpen.LineDesigner.RenameItemRevisionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partOccTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateRenameItemRevisionBuilder(partOccTag: NXOpen.TaggedObject) -> RenameItemRevisionBuilder:
        """
         To create a rename ItemRevision Builder
         @return builder (@link RenameItemRevisionBuilder NXOpen.LineDesigner.RenameItemRevisionBuilder@endlink):  .
        """
        pass
    
    ##  Create resize connector Builder 
    ##  @return builder (@link ResizeConnectorBuilder NXOpen.LineDesigner.ResizeConnectorBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateResizeConnectorBuilder(part: NXOpen.Part) -> ResizeConnectorBuilder:
        """
         Create resize connector Builder 
         @return builder (@link ResizeConnectorBuilder NXOpen.LineDesigner.ResizeConnectorBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Rotate component builder
    ##  @return builder (@link RotateComponentBuilder NXOpen.LineDesigner.RotateComponentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateRotateComponentBuilder(part: NXOpen.Part) -> RotateComponentBuilder:
        """
         Creates a Rotate component builder
         @return builder (@link RotateComponentBuilder NXOpen.LineDesigner.RotateComponentBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Selection Tool Builder
    ##  @return builder (@link SelectionToolBuilder NXOpen.LineDesigner.SelectionToolBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateSelectionToolBuilder(part: NXOpen.Part) -> SelectionToolBuilder:
        """
         Creates a Selection Tool Builder
         @return builder (@link SelectionToolBuilder NXOpen.LineDesigner.SelectionToolBuilder@endlink):  .
        """
        pass
    
    ##  Create single element conveyor builder    
    ##  @return builder (@link SingleElementConveyorBuilder NXOpen.LineDesigner.SingleElementConveyorBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="node"> (@link DBConveyorNode NXOpen.LineDesigner.DBConveyorNode@endlink)  </param>
    def CreateSingleElementConveyorBuilder(part: NXOpen.Part, node: DBConveyorNode) -> SingleElementConveyorBuilder:
        """
         Create single element conveyor builder    
         @return builder (@link SingleElementConveyorBuilder NXOpen.LineDesigner.SingleElementConveyorBuilder@endlink):  .
        """
        pass
    
    ## Create StairwayEquipment builder 
    ##  @return builder (@link StairwayEquipmentBuilder NXOpen.LineDesigner.StairwayEquipmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="dbnode"> (@link DBStairwayEquipmentNode NXOpen.LineDesigner.DBStairwayEquipmentNode@endlink)  </param>
    def CreateStairwayEquipmentBuilder(part: NXOpen.Part, dbnode: DBStairwayEquipmentNode) -> StairwayEquipmentBuilder:
        """
        Create StairwayEquipment builder 
         @return builder (@link StairwayEquipmentBuilder NXOpen.LineDesigner.StairwayEquipmentBuilder@endlink):  .
        """
        pass
    
    ##  Create typed connector feature builder 
    ##  @return builder (@link TypedConnectorFeatureBuilder NXOpen.LineDesigner.TypedConnectorFeatureBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="typed_connector_feature"> (@link TypedConnectorFeature NXOpen.LineDesigner.TypedConnectorFeature@endlink)  @link LineDesigner::TypedConnectorFeature LineDesigner::TypedConnectorFeature@endlink  to be edited </param>
    def CreateTypedConnectorFeatureBuilder(part: NXOpen.Part, typed_connector_feature: TypedConnectorFeature) -> TypedConnectorFeatureBuilder:
        """
         Create typed connector feature builder 
         @return builder (@link TypedConnectorFeatureBuilder NXOpen.LineDesigner.TypedConnectorFeatureBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Unmount Dialoge Builder
    ##  @return builder (@link UnmountBuilder NXOpen.LineDesigner.UnmountBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateUnmountBuilder(part: NXOpen.Part) -> UnmountBuilder:
        """
         Creates a Unmount Dialoge Builder
         @return builder (@link UnmountBuilder NXOpen.LineDesigner.UnmountBuilder@endlink):  .
        """
        pass
    
    ## Create the drawing sheet builder 
    ##  @return builder (@link NXOpen.Drawings.DrawingSheetBuilder NXOpen.Drawings.DrawingSheetBuilder@endlink):  the drawing sheet Builder with this identifier .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="owning_part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="sheet"> (@link NXOpen.Drawings.DrawingSheet NXOpen.Drawings.DrawingSheet@endlink)  the drawing sheet </param>
    def DrawingSheetBuilder(owning_part: NXOpen.Part, sheet: NXOpen.Drawings.DrawingSheet) -> NXOpen.Drawings.DrawingSheetBuilder:
        """
        Create the drawing sheet builder 
         @return builder (@link NXOpen.Drawings.DrawingSheetBuilder NXOpen.Drawings.DrawingSheetBuilder@endlink):  the drawing sheet Builder with this identifier .
        """
        pass
    
    ##  Application builder is return 
    ##  @return builder (@link LineDesignerApplicationBuilder NXOpen.LineDesigner.LineDesignerApplicationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetApplicationBuilder() -> LineDesignerApplicationBuilder:
        """
         Application builder is return 
         @return builder (@link LineDesignerApplicationBuilder NXOpen.LineDesigner.LineDesignerApplicationBuilder@endlink): .
        """
        pass
    
    ##  Returns the reuse library utility builder 
    ##  @return builder (@link ReuseLibraryUtilityBuilder NXOpen.LineDesigner.ReuseLibraryUtilityBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetReuseLibraryUtilityBuilder() -> ReuseLibraryUtilityBuilder:
        """
         Returns the reuse library utility builder 
         @return builder (@link ReuseLibraryUtilityBuilder NXOpen.LineDesigner.ReuseLibraryUtilityBuilder@endlink): .
        """
        pass
    
    ##  To create a new navigator production unit builder
    ##  @return builder (@link PlantProductionUnitCreatorBuilder NXOpen.LineDesigner.PlantProductionUnitCreatorBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def PlantCreateProductionUnitCreatorBuilder(part: NXOpen.Part) -> PlantProductionUnitCreatorBuilder:
        """
         To create a new navigator production unit builder
         @return builder (@link PlantProductionUnitCreatorBuilder NXOpen.LineDesigner.PlantProductionUnitCreatorBuilder@endlink):  .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a manager of line designer user callbacks  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class LineDesignerUserCallBackManager(NXOpen.Object): 
    """ Represents a manager of line designer user callbacks """


    ##  This enum is providing the event id 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PasteEvent</term><description> 
    ## </description> </item><item><term> 
    ## EndPasteEvent</term><description> 
    ## </description> </item><item><term> 
    ## ComponentReplaceEvent</term><description> 
    ## </description> </item></list>
    class EventType(Enum):
        """
        Members Include: <PasteEvent> <EndPasteEvent> <ComponentReplaceEvent>
        """
        PasteEvent: int
        EndPasteEvent: int
        ComponentReplaceEvent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LineDesignerUserCallBackManager.EventType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  To call user defined function
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="eventId"> (@link LineDesignerUserCallBackManager.EventType NXOpen.LineDesigner.LineDesignerUserCallBackManager.EventType@endlink)   event Id to find the function to be invoke </param>
    ## <param name="src_occ"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  </param>
    ## <param name="target_occ"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  </param>
    def CallUserdefinedFunctions(eventId: LineDesignerUserCallBackManager.EventType, src_occ: NXOpen.Assemblies.Component, target_occ: NXOpen.Assemblies.Component) -> None:
        """
         To call user defined function
        """
        pass
    
    ##  User defined method that is called from a particular event 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink
    ##  - @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink
    ##  and no return type
    CustomerCallbackHandler = Callable[[NXOpen.Assemblies.Component, NXOpen.Assemblies.Component], None]
    
    
    ##  To check if user defined function is registered
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="eventId"> (@link LineDesignerUserCallBackManager.EventType NXOpen.LineDesigner.LineDesignerUserCallBackManager.EventType@endlink)   event Id to find the function to be invoke </param>
    def IsUserdefinedFunctionAvailable(eventId: LineDesignerUserCallBackManager.EventType) -> None:
        """
         To check if user defined function is registered
        """
        pass
    
    ##  To register user defined function
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="handler"> (@link LineDesignerUserCallBackManager.CustomerCallbackHandler NXOpen.LineDesigner.LineDesignerUserCallBackManager.CustomerCallbackHandler@endlink)  method to register </param>
    ## <param name="eventId"> (@link LineDesignerUserCallBackManager.EventType NXOpen.LineDesigner.LineDesignerUserCallBackManager.EventType@endlink)  event id </param>
    def RegisterUserdefinedFunctions(handler: LineDesignerUserCallBackManager.CustomerCallbackHandler, eventId: LineDesignerUserCallBackManager.EventType) -> None:
        """
         To register user defined function
        """
        pass
    
    ##  To register user defined function
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="eventId"> (@link LineDesignerUserCallBackManager.EventType NXOpen.LineDesigner.LineDesignerUserCallBackManager.EventType@endlink)  event id </param>
    def UnregisterUserdefinedFunctions(eventId: LineDesignerUserCallBackManager.EventType) -> None:
        """
         To register user defined function
        """
        pass
    
import NXOpen
##  For creating and editing Connectors types in LineDesigner  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateListOfConnectorsBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateListOfConnectorsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ListOfConnectorsBuilder(NXOpen.Builder): 
    """ For creating and editing Connectors types in LineDesigner """


    ##  Add a new Connector type 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AddNewType(self) -> None:
        """
         Add a new Connector type 
        """
        pass
    
    ##  Restore to defaults 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def RestoreDefault(self) -> None:
        """
         Restore to defaults 
        """
        pass
    
import NXOpen
##  Represents Model Base Object  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ModelBaseObject(NXOpen.NXObject): 
    """ Represents Model Base Object """
    pass


import NXOpen
##  Represents a manager of line designer model  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ModelPlantManager(NXOpen.Object): 
    """ Represents a manager of line designer model """


    ##   Activate Plant Model  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink)  </param>
    ## <param name="activate"> (bool)  </param>
    def ActivatePlantModel(modelPlantRoot: ModelPlantRoot, activate: bool) -> None:
        """
          Activate Plant Model  
        """
        pass
    
    ##   Clean Plant Model  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink)  </param>
    def CleanPlantModel(modelPlantRoot: ModelPlantRoot) -> None:
        """
          Clean Plant Model  
        """
        pass
    
    ##   Establish Plant Model Root 
    ##  @return modelPlantRoot (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetModelPlantRoot() -> ModelPlantRoot:
        """
          Establish Plant Model Root 
         @return modelPlantRoot (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink):  .
        """
        pass
    
    ##   Move Resource Instances  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink)  </param>
    ## <param name="resourceInstances"> (@link ModelResourceInstance List[NXOpen.LineDesigner.ModelResourceInstance]@endlink)  </param>
    ## <param name="newParent"> (@link ModelBaseObject NXOpen.LineDesigner.ModelBaseObject@endlink)  </param>
    def MoveResourceInstances(modelPlantRoot: ModelPlantRoot, resourceInstances: List[ModelResourceInstance], newParent: ModelBaseObject) -> None:
        """
          Move Resource Instances  
        """
        pass
    
    ##   Obsolete Production Unit  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink) </param>
    ## <param name="productionUnitToObsolete"> (@link ModelProductionUnit NXOpen.LineDesigner.ModelProductionUnit@endlink) </param>
    def ObsoleteProductionUnit(modelPlantRoot: ModelPlantRoot, productionUnitToObsolete: ModelProductionUnit) -> None:
        """
          Obsolete Production Unit  
        """
        pass
    
    ##   Read Plant Model  
    ##  @return plantRoot (@link NXOpen.NXObject NXOpen.NXObject@endlink):  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink)  </param>
    def ReadPlantModel(modelPlantRoot: ModelPlantRoot) -> NXOpen.NXObject:
        """
          Read Plant Model  
         @return plantRoot (@link NXOpen.NXObject NXOpen.NXObject@endlink):  .
        """
        pass
    
    ##   Restore Target Production Unit  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink)  </param>
    def RestoreTargetProductionUnit(modelPlantRoot: ModelPlantRoot) -> None:
        """
          Restore Target Production Unit  
        """
        pass
    
    ##   Set Target Production Unit  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="modelPlantRoot"> (@link ModelPlantRoot NXOpen.LineDesigner.ModelPlantRoot@endlink)  </param>
    ## <param name="productionUnit"> (@link ModelProductionUnit NXOpen.LineDesigner.ModelProductionUnit@endlink)  </param>
    ## <param name="keep"> (bool)  </param>
    def SetTargetProductionUnit(modelPlantRoot: ModelPlantRoot, productionUnit: ModelProductionUnit, keep: bool) -> None:
        """
          Set Target Production Unit  
        """
        pass
    
import NXOpen
##  Represents a manager of line designer plant model  <br> Established by LineDesigner_ModelPlantManager when we enter the application  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ModelPlantRoot(NXOpen.NXObject): 
    """ Represents a manager of line designer plant model """
    pass


##  Represents Production Unit 
## 
##   <br>  Created in NX9.0.0  <br> 

class ModelProductionUnit(ModelBaseObject): 
    """ Represents Production Unit """
    pass


##  Represents Resource Instance 
## 
##   <br>  Created in NX9.0.0  <br> 

class ModelResourceInstance(ModelBaseObject): 
    """ Represents Resource Instance """
    pass


import NXOpen
## Class for assignment of mapped type <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateModifyConnectedSystemBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateModifyConnectedSystemBuilder @endlink  <br> 
## 
##   <br>  Created in NX1938.0.0  <br> 

class ModifyConnectedSystemBuilder(NXOpen.Builder): 
    """Class for assignment of mapped type"""


    ##  Get the Expression Value
    ##  @return exp (List[str]): .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="expressionTitle"> (str) </param>
    def CollectExpressionValues(self, expressionTitle: str) -> List[str]:
        """
         Get the Expression Value
         @return exp (List[str]): .
        """
        pass
    
    ##  Collect shared Expression
    ##  @return numExpresssion (int): .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def CollectSharedExpression(self) -> int:
        """
         Collect shared Expression
         @return numExpresssion (int): .
        """
        pass
    
    ##  Get the Expression Title
    ##  @return expTitle (str): .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="expression"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def GetExpressionTitle(self, expression: NXOpen.Expression) -> str:
        """
         Get the Expression Title
         @return expTitle (str): .
        """
        pass
    
    ##  Get the expressions in the attribute
    ##  @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetExpressionsArray(self) -> List[NXOpen.Expression]:
        """
         Get the expressions in the attribute
         @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  Set selected component  
    ##  @return selectedCompTag (@link NXOpen.NXObject NXOpen.NXObject@endlink):  .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetSelectedComponent(self) -> NXOpen.NXObject:
        """
         Set selected component  
         @return selectedCompTag (@link NXOpen.NXObject NXOpen.NXObject@endlink):  .
        """
        pass
    
    ##  Get tooltipMessage component  
    ##  @return toolTipMessage (str):  .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetToolTipMessage(self) -> str:
        """
         Get tooltipMessage component  
         @return toolTipMessage (str):  .
        """
        pass
    
    ##  Set Expression Value  
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="name"> (str)  </param>
    ## <param name="value"> (float) </param>
    def SetExpressionValue(self, name: str, value: float) -> None:
        """
         Set Expression Value  
        """
        pass
    
    ##  Set the expressions in the attribute 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="expressionValues"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def SetExpressionsArray(self, expressionValues: List[NXOpen.Expression]) -> None:
        """
         Set the expressions in the attribute 
        """
        pass
    
    ##  Set selected component  
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="selectedCompTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def SetSelectedComponent(self, selectedCompTag: NXOpen.NXObject) -> None:
        """
         Set selected component  
        """
        pass
    
    ##  Set tooltipMessage component  
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="toolTipMessage"> (str)  </param>
    def SetToolTipMessage(self, toolTipMessage: str) -> None:
        """
         Set tooltipMessage component  
        """
        pass
    
import NXOpen
## 
##     MountBuilder Class: Used when mounting a tool on robot.
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateMountBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateMountBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FlipEnum </term> <description> 
##  
## X </description> </item> 
## 
## <item><term> 
##  
## MountEnum </term> <description> 
##  
## MoveandMount </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.2  <br> 

class MountBuilder(NXOpen.Builder): 
    """
    MountBuilder Class: Used when mounting a tool on robot.
    """


    ##  This enum is providing possible flip types    
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ## </description> </item><item><term> 
    ## Y</term><description> 
    ## </description> </item><item><term> 
    ## Z</term><description> 
    ## </description> </item></list>
    class FlipType(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MountBuilder.FlipType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible mount types    
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MoveandMount</term><description> 
    ## </description> </item><item><term> 
    ## MountOnly</term><description> 
    ## </description> </item></list>
    class MountType(Enum):
        """
        Members Include: <MoveandMount> <MountOnly>
        """
        MoveandMount: int
        MountOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MountBuilder.MountType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MountBuilder.FlipType NXOpen.LineDesigner.MountBuilder.FlipType@endlink) FlipEnum
    ##  Returns the flip enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return MountBuilder.FlipType
    @property
    def FlipEnum(self) -> MountBuilder.FlipType:
        """
        Getter for property: (@link MountBuilder.FlipType NXOpen.LineDesigner.MountBuilder.FlipType@endlink) FlipEnum
         Returns the flip enum   
            
         
        """
        pass
    
    ## Setter for property: (@link MountBuilder.FlipType NXOpen.LineDesigner.MountBuilder.FlipType@endlink) FlipEnum

    ##  Returns the flip enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @FlipEnum.setter
    def FlipEnum(self, flipEnum: MountBuilder.FlipType):
        """
        Setter for property: (@link MountBuilder.FlipType NXOpen.LineDesigner.MountBuilder.FlipType@endlink) FlipEnum
         Returns the flip enum   
            
         
        """
        pass
    
    ## Getter for property: (@link MountBuilder.MountType NXOpen.LineDesigner.MountBuilder.MountType@endlink) MountEnum
    ##  Returns the mount enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return MountBuilder.MountType
    @property
    def MountEnum(self) -> MountBuilder.MountType:
        """
        Getter for property: (@link MountBuilder.MountType NXOpen.LineDesigner.MountBuilder.MountType@endlink) MountEnum
         Returns the mount enum   
            
         
        """
        pass
    
    ## Setter for property: (@link MountBuilder.MountType NXOpen.LineDesigner.MountBuilder.MountType@endlink) MountEnum

    ##  Returns the mount enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @MountEnum.setter
    def MountEnum(self, mountEnum: MountBuilder.MountType):
        """
        Setter for property: (@link MountBuilder.MountType NXOpen.LineDesigner.MountBuilder.MountType@endlink) MountEnum
         Returns the mount enum   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectSource
    ##  Returns the select source   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectSource(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectSource
         Returns the select source   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectTarget
    ##  Returns the select target   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectTarget(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectTarget
         Returns the select target   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def FlipButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Pick Rectangle Points  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreatePickRectanglePointsBuilder  NXOpen::LineDesigner::LineDesignerManager::CreatePickRectanglePointsBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class PickRectanglePointsBuilder(NXOpen.TaggedObject): 
    """ Pick Rectangle Points """


    ## Getter for property: (bool) AllowRotation
    ##  Returns the check for rotaion   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AllowRotation(self) -> bool:
        """
        Getter for property: (bool) AllowRotation
         Returns the check for rotaion   
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowRotation

    ##  Returns the check for rotaion   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AllowRotation.setter
    def AllowRotation(self, rotaion: bool):
        """
        Setter for property: (bool) AllowRotation
         Returns the check for rotaion   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPartList NXOpen.SelectPartList@endlink) PointsSelection
    ##  Returns the points of selection are return   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectPartList
    @property
    def PointsSelection(self) -> NXOpen.SelectPartList:
        """
        Getter for property: (@link NXOpen.SelectPartList NXOpen.SelectPartList@endlink) PointsSelection
         Returns the points of selection are return   
            
         
        """
        pass
    
    ##  To reset rectangle data 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ResetData(self) -> None:
        """
         To reset rectangle data 
        """
        pass
    
    ##  To reset rectangle width and height 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ResetWidthHeight(self) -> None:
        """
         To reset rectangle width and height 
        """
        pass
    
    ##  To set rectangle width and height 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    def SetWidthHeight(self, width: float, height: float) -> None:
        """
         To set rectangle width and height 
        """
        pass
    
    ##  To update rectangle angle 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="angle"> (float) </param>
    def UpdateRecAngle(self, angle: float) -> None:
        """
         To update rectangle angle 
        """
        pass
    
    ##  To update rectangle height 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="height"> (float) </param>
    def UpdateRecHeight(self, height: float) -> None:
        """
         To update rectangle height 
        """
        pass
    
    ##  To update rectangle width 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="width"> (float) </param>
    def UpdateRecWidth(self, width: float) -> None:
        """
         To update rectangle width 
        """
        pass
    
    ##  To update rectangle points
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def UpdateRectangle(self) -> None:
        """
         To update rectangle points
        """
        pass
    
import NXOpen
##  
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::PlantCreateProductionUnitCreatorBuilder  NXOpen::LineDesigner::LineDesignerManager::PlantCreateProductionUnitCreatorBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PlantProductionUnitCreatorBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """


    ## Getter for property: (str) ProductionUnitId
    ##  Returns the production unit id   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ProductionUnitId(self) -> str:
        """
        Getter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    
    ## Setter for property: (str) ProductionUnitId

    ##  Returns the production unit id   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ProductionUnitId.setter
    def ProductionUnitId(self, productionUnitId: str):
        """
        Setter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    
    ## Getter for property: (str) ProductionUnitName
    ##  Returns the production unit name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ProductionUnitName(self) -> str:
        """
        Getter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    
    ## Setter for property: (str) ProductionUnitName

    ##  Returns the production unit name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ProductionUnitName.setter
    def ProductionUnitName(self, productionUnitName: str):
        """
        Setter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    
    ## Getter for property: (str) ProductionUnitTypeString
    ##  Returns the type of a production unit   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def ProductionUnitTypeString(self) -> str:
        """
        Getter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    
    ## Setter for property: (str) ProductionUnitTypeString

    ##  Returns the type of a production unit   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ProductionUnitTypeString.setter
    def ProductionUnitTypeString(self, productionUnitType: str):
        """
        Setter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    
    ##  The assign ID  of production unit
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AssignId(self) -> None:
        """
         The assign ID  of production unit
        """
        pass
    
    ##  The production unit description
    ##  @return productionUnitDescription (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetProductionUnitDescription(self) -> List[str]:
        """
         The production unit description
         @return productionUnitDescription (List[str]): .
        """
        pass
    
    ##  The production unit description is set 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="productionUnitDescription"> (List[str])  </param>
    def SetProductionUnitDescription(self, productionUnitDescription: List[str]) -> None:
        """
         The production unit description is set 
        """
        pass
    
    ##  The production unit parent is set
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="parent"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def SetProductionUnitParent(self, parent: NXOpen.NXObject) -> None:
        """
         The production unit parent is set
        """
        pass
    
import NXOpen
##  This class is used for sharing Attribute and JT with Plant Simulation <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreatePlantSimExchangeBuilder  NXOpen::LineDesigner::LineDesignerManager::CreatePlantSimExchangeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1938.0.0  <br> 

class PlantSimExchangeBuilder(NXOpen.Builder): 
    """ This class is used for sharing Attribute and JT with Plant Simulation"""


    ## Getter for property: (str) NativeFolderBrowser
    ##  Returns the native folder browser0   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return str
    @property
    def NativeFolderBrowser(self) -> str:
        """
        Getter for property: (str) NativeFolderBrowser
         Returns the native folder browser0   
            
         
        """
        pass
    
    ## Setter for property: (str) NativeFolderBrowser

    ##  Returns the native folder browser0   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @NativeFolderBrowser.setter
    def NativeFolderBrowser(self, foldername: str):
        """
        Setter for property: (str) NativeFolderBrowser
         Returns the native folder browser0   
            
         
        """
        pass
    
import NXOpen
##  Represents a singleton JA for PlanViewManager  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreatePlanViewManagerInstance  NXOpen::LineDesigner::LineDesignerManager::CreatePlanViewManagerInstance @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class PlanViewManager(NXOpen.TaggedObject): 
    """ Represents a singleton JA for PlanViewManager """


    ##   To set/unset 2D planning view 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="setView"> (bool) </param>
    def SetTwoDPlanningView(self, setView: bool) -> None:
        """
          To set/unset 2D planning view 
        """
        pass
    
import NXOpen
##   
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreatePlatformEquipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreatePlatformEquipmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AddRailingToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DeckCeilingHeightForCenterline.Value </term> <description> 
##  
## 9000 (millimeters part), 354.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckCeilingHeightForPolyline.Value </term> <description> 
##  
## 9000 (millimeters part), 354.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckElevationForCenterline.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckElevationForPolyline.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckHeightForCenterline.Value </term> <description> 
##  
## 525 (millimeters part), 21 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckHeightForPolyline.Value </term> <description> 
##  
## 1750 (millimeters part), 68.9 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckLengthForCenterline.Value </term> <description> 
##  
## 2540 (millimeters part), 100 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckSupportEnum </term> <description> 
##  
## NoSupports </description> </item> 
## 
## <item><term> 
##  
## DeckThicknessForCenterline.Value </term> <description> 
##  
## 300 (millimeters part), 12 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckThicknessForPolyline.Value </term> <description> 
##  
## 300 (millimeters part), 12 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckWidthForCenterline.Value </term> <description> 
##  
## 2438 (millimeters part), 96 (inches part) </description> </item> 
## 
## <item><term> 
##  
## DeckingMaterial </term> <description> 
##  
## MetalGrate </description> </item> 
## 
## <item><term> 
##  
## DistanceFromCenterline.Value </term> <description> 
##  
## 660 (millimeters part), 26 (inches part) </description> </item> 
## 
## <item><term> 
##  
## HorizontalGridSpacing.Value </term> <description> 
##  
## 4000 (millimeters part), 157.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OutlineEnum </term> <description> 
##  
## Polyline </description> </item> 
## 
## <item><term> 
##  
## SideFromCenterlineEnum </term> <description> 
##  
## RightTopSide </description> </item> 
## 
## <item><term> 
##  
## SupportsFromCeiling </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TypeEnum </term> <description> 
##  
## Platform </description> </item> 
## 
## <item><term> 
##  
## VerticalGridSpacing.Value </term> <description> 
##  
## 3200 (millimeters part), 126 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class PlatformEquipmentBuilder(NXOpen.Builder): 
    """  
    
    
    
    
    
    """


    ##  This enum is providing possible deck support types  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoSupports</term><description> 
    ## </description> </item><item><term> 
    ## CornersSupportsOnly</term><description> 
    ## </description> </item><item><term> 
    ## AutomaticSupportinGridPattern</term><description> 
    ## </description> </item><item><term> 
    ## ManualSupports</term><description> 
    ## </description> </item></list>
    class DeckSupportTypeAPI(Enum):
        """
        Members Include: <NoSupports> <CornersSupportsOnly> <AutomaticSupportinGridPattern> <ManualSupports>
        """
        NoSupports: int
        CornersSupportsOnly: int
        AutomaticSupportinGridPattern: int
        ManualSupports: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.DeckSupportTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible deck material type  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MetalGrate</term><description> 
    ## </description> </item><item><term> 
    ## CheckerPlate</term><description> 
    ## </description> </item></list>
    class DeckingMaterialTypeAPI(Enum):
        """
        Members Include: <MetalGrate> <CheckerPlate>
        """
        MetalGrate: int
        CheckerPlate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.DeckingMaterialTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible outline types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Polyline</term><description> 
    ## </description> </item><item><term> 
    ## Centerline</term><description> 
    ## </description> </item></list>
    class OutlineTypeAPI(Enum):
        """
        Members Include: <Polyline> <Centerline>
        """
        Polyline: int
        Centerline: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.OutlineTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible sides for centerline outline type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## RightTopSide</term><description> 
    ## </description> </item><item><term> 
    ## LeftBottomSide</term><description> 
    ## </description> </item></list>
    class SideFromCenterlineTypeAPI(Enum):
        """
        Members Include: <RightTopSide> <LeftBottomSide>
        """
        RightTopSide: int
        LeftBottomSide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.SideFromCenterlineTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible platform types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Platform</term><description> 
    ## </description> </item><item><term> 
    ## Mezzanine</term><description> 
    ## </description> </item></list>
    class TypeAPI(Enum):
        """
        Members Include: <Platform> <Mezzanine>
        """
        Platform: int
        Mezzanine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.TypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AddRailingToggle
    ##  Returns the railing toggle to check railing is prsent for platform or not  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AddRailingToggle(self) -> bool:
        """
        Getter for property: (bool) AddRailingToggle
         Returns the railing toggle to check railing is prsent for platform or not  
            
         
        """
        pass
    
    ## Setter for property: (bool) AddRailingToggle

    ##  Returns the railing toggle to check railing is prsent for platform or not  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AddRailingToggle.setter
    def AddRailingToggle(self, addRailingToggle: bool):
        """
        Setter for property: (bool) AddRailingToggle
         Returns the railing toggle to check railing is prsent for platform or not  
            
         
        """
        pass
    
    ## Getter for property: (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink) CenterlineJigOnPlane
    ##  Returns the Centerlinejig on plane builder   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return JigOnPlaneBuilder
    @property
    def CenterlineJigOnPlane(self) -> JigOnPlaneBuilder:
        """
        Getter for property: (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink) CenterlineJigOnPlane
         Returns the Centerlinejig on plane builder   
            
         
        """
        pass
    
    ## Setter for property: (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink) CenterlineJigOnPlane

    ##  Returns the Centerlinejig on plane builder   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CenterlineJigOnPlane.setter
    def CenterlineJigOnPlane(self, centerlineJigOnPlane: JigOnPlaneBuilder):
        """
        Setter for property: (@link JigOnPlaneBuilder NXOpen.LineDesigner.JigOnPlaneBuilder@endlink) CenterlineJigOnPlane
         Returns the Centerlinejig on plane builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckCeilingHeightForCenterline
    ##  Returns the deck ceiling height for centerline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckCeilingHeightForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckCeilingHeightForCenterline
         Returns the deck ceiling height for centerline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckCeilingHeightForPolyline
    ##  Returns the deck ceiling height for polyline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckCeilingHeightForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckCeilingHeightForPolyline
         Returns the deck ceiling height for polyline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckElevationForCenterline
    ##  Returns the deck elevation for centerline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckElevationForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckElevationForCenterline
         Returns the deck elevation for centerline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckElevationForPolyline
    ##  Returns the deck elevation for polyline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckElevationForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckElevationForPolyline
         Returns the deck elevation for polyline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckHeightForCenterline
    ##  Returns the deck height for centerline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckHeightForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckHeightForCenterline
         Returns the deck height for centerline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckHeightForPolyline
    ##  Returnsthe deck height for polyline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckHeightForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckHeightForPolyline
         Returnsthe deck height for polyline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckLengthForCenterline
    ##  Returns the deck length for centerline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckLengthForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckLengthForCenterline
         Returns the deck length for centerline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckSupportTypeAPI@endlink) DeckSupportEnum
    ##  Returns the deck support type for platform  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PlatformEquipmentBuilder.DeckSupportTypeAPI
    @property
    def DeckSupportEnum(self) -> PlatformEquipmentBuilder.DeckSupportTypeAPI:
        """
        Getter for property: (@link PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckSupportTypeAPI@endlink) DeckSupportEnum
         Returns the deck support type for platform  
            
         
        """
        pass
    
    ## Setter for property: (@link PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckSupportTypeAPI@endlink) DeckSupportEnum

    ##  Returns the deck support type for platform  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DeckSupportEnum.setter
    def DeckSupportEnum(self, deckSupportEnum: PlatformEquipmentBuilder.DeckSupportTypeAPI):
        """
        Setter for property: (@link PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckSupportTypeAPI@endlink) DeckSupportEnum
         Returns the deck support type for platform  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckThicknessForCenterline
    ##  Returns the deck thickness for centerline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckThicknessForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckThicknessForCenterline
         Returns the deck thickness for centerline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckThicknessForPolyline
    ##  Returns the deck thickness for polyline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckThicknessForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckThicknessForPolyline
         Returns the deck thickness for polyline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckWidthForCenterline
    ##  Returns the deck width for centerline platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DeckWidthForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DeckWidthForCenterline
         Returns the deck width for centerline platform   
            
         
        """
        pass
    
    ## Getter for property: (@link PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckingMaterialTypeAPI@endlink) DeckingMaterial
    ##  Returns the decking material   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PlatformEquipmentBuilder.DeckingMaterialTypeAPI
    @property
    def DeckingMaterial(self) -> PlatformEquipmentBuilder.DeckingMaterialTypeAPI:
        """
        Getter for property: (@link PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckingMaterialTypeAPI@endlink) DeckingMaterial
         Returns the decking material   
            
         
        """
        pass
    
    ## Setter for property: (@link PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckingMaterialTypeAPI@endlink) DeckingMaterial

    ##  Returns the decking material   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DeckingMaterial.setter
    def DeckingMaterial(self, deckingMaterial: PlatformEquipmentBuilder.DeckingMaterialTypeAPI):
        """
        Setter for property: (@link PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckingMaterialTypeAPI@endlink) DeckingMaterial
         Returns the decking material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromCenterline
    ##  Returns the distance of platform from centerline   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromCenterline
         Returns the distance of platform from centerline   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HorizontalGridSpacing
    ##  Returns the horizontal grid spacing   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HorizontalGridSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HorizontalGridSpacing
         Returns the horizontal grid spacing   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSketchInternal
    ##  Returns the issketchiInternal    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def IsSketchInternal(self) -> bool:
        """
        Getter for property: (bool) IsSketchInternal
         Returns the issketchiInternal    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSketchInternal

    ##  Returns the issketchiInternal    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IsSketchInternal.setter
    def IsSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) IsSketchInternal
         Returns the issketchiInternal    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
    ##  Returns the kf object   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.KFObject
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
         Returns the kf object   
            
         
        """
        pass
    
    ## Getter for property: (@link PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.OutlineTypeAPI@endlink) OutlineEnum
    ##  Returns the outline type enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PlatformEquipmentBuilder.OutlineTypeAPI
    @property
    def OutlineEnum(self) -> PlatformEquipmentBuilder.OutlineTypeAPI:
        """
        Getter for property: (@link PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.OutlineTypeAPI@endlink) OutlineEnum
         Returns the outline type enum   
            
         
        """
        pass
    
    ## Setter for property: (@link PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.OutlineTypeAPI@endlink) OutlineEnum

    ##  Returns the outline type enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OutlineEnum.setter
    def OutlineEnum(self, outlineEnum: PlatformEquipmentBuilder.OutlineTypeAPI):
        """
        Setter for property: (@link PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.OutlineTypeAPI@endlink) OutlineEnum
         Returns the outline type enum   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PolylineSuperSection
    ##  Returns the polyline section for platform   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def PolylineSuperSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PolylineSuperSection
         Returns the polyline section for platform   
            
         
        """
        pass
    
    ## Getter for property: (@link PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.SideFromCenterlineTypeAPI@endlink) SideFromCenterlineEnum
    ##  Returns the side from center line    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PlatformEquipmentBuilder.SideFromCenterlineTypeAPI
    @property
    def SideFromCenterlineEnum(self) -> PlatformEquipmentBuilder.SideFromCenterlineTypeAPI:
        """
        Getter for property: (@link PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.SideFromCenterlineTypeAPI@endlink) SideFromCenterlineEnum
         Returns the side from center line    
            
         
        """
        pass
    
    ## Setter for property: (@link PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.SideFromCenterlineTypeAPI@endlink) SideFromCenterlineEnum

    ##  Returns the side from center line    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SideFromCenterlineEnum.setter
    def SideFromCenterlineEnum(self, sideFromCenterlineEnum: PlatformEquipmentBuilder.SideFromCenterlineTypeAPI):
        """
        Setter for property: (@link PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.SideFromCenterlineTypeAPI@endlink) SideFromCenterlineEnum
         Returns the side from center line    
            
         
        """
        pass
    
    ## Getter for property: (bool) StatusOfPlatformCeilingHeightUpdation
    ##  Returns the platform ceiling height updation status   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def StatusOfPlatformCeilingHeightUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformCeilingHeightUpdation
         Returns the platform ceiling height updation status   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatusOfPlatformCeilingHeightUpdation

    ##  Returns the platform ceiling height updation status   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StatusOfPlatformCeilingHeightUpdation.setter
    def StatusOfPlatformCeilingHeightUpdation(self, statusOfPlatformCeilingHeightUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformCeilingHeightUpdation
         Returns the platform ceiling height updation status   
            
         
        """
        pass
    
    ## Getter for property: (bool) StatusOfPlatformElevationUpdation
    ##  Returns the platform elevation updation status   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def StatusOfPlatformElevationUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformElevationUpdation
         Returns the platform elevation updation status   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatusOfPlatformElevationUpdation

    ##  Returns the platform elevation updation status   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StatusOfPlatformElevationUpdation.setter
    def StatusOfPlatformElevationUpdation(self, statusOfPlatformElevationUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformElevationUpdation
         Returns the platform elevation updation status   
            
         
        """
        pass
    
    ## Getter for property: (bool) StatusOfPlatformHeightUpdation
    ##  Returns the platform height updation status   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def StatusOfPlatformHeightUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformHeightUpdation
         Returns the platform height updation status   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatusOfPlatformHeightUpdation

    ##  Returns the platform height updation status   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StatusOfPlatformHeightUpdation.setter
    def StatusOfPlatformHeightUpdation(self, statusOfPlatformHeightUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformHeightUpdation
         Returns the platform height updation status   
            
         
        """
        pass
    
    ## Getter for property: (bool) StatusOfPlatformSupportDefaultFromCeilingToggleUpdation
    ##  Returns the platform supportDefaultFromCeilingToggle updation status   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def StatusOfPlatformSupportDefaultFromCeilingToggleUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformSupportDefaultFromCeilingToggleUpdation
         Returns the platform supportDefaultFromCeilingToggle updation status   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatusOfPlatformSupportDefaultFromCeilingToggleUpdation

    ##  Returns the platform supportDefaultFromCeilingToggle updation status   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StatusOfPlatformSupportDefaultFromCeilingToggleUpdation.setter
    def StatusOfPlatformSupportDefaultFromCeilingToggleUpdation(self, statusOfPlatformSupportDefaultFromCeilingToggleUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformSupportDefaultFromCeilingToggleUpdation
         Returns the platform supportDefaultFromCeilingToggle updation status   
            
         
        """
        pass
    
    ## Getter for property: (bool) StatusOfPlatformSupportOptionUpdation
    ##  Returns the platform supportOption updation status   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def StatusOfPlatformSupportOptionUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformSupportOptionUpdation
         Returns the platform supportOption updation status   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatusOfPlatformSupportOptionUpdation

    ##  Returns the platform supportOption updation status   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StatusOfPlatformSupportOptionUpdation.setter
    def StatusOfPlatformSupportOptionUpdation(self, statusOfPlatformSupportOptionUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformSupportOptionUpdation
         Returns the platform supportOption updation status   
            
         
        """
        pass
    
    ## Getter for property: (bool) StatusOfPlatformThicknessUpdation
    ##  Returns the platform thickness updation status   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def StatusOfPlatformThicknessUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformThicknessUpdation
         Returns the platform thickness updation status   
            
         
        """
        pass
    
    ## Setter for property: (bool) StatusOfPlatformThicknessUpdation

    ##  Returns the platform thickness updation status   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StatusOfPlatformThicknessUpdation.setter
    def StatusOfPlatformThicknessUpdation(self, statusOfPlatformThicknessUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformThicknessUpdation
         Returns the platform thickness updation status   
            
         
        """
        pass
    
    ## Getter for property: (bool) SupportsFromCeiling
    ##  Returns the option to check , if supports are from ceiling   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def SupportsFromCeiling(self) -> bool:
        """
        Getter for property: (bool) SupportsFromCeiling
         Returns the option to check , if supports are from ceiling   
            
         
        """
        pass
    
    ## Setter for property: (bool) SupportsFromCeiling

    ##  Returns the option to check , if supports are from ceiling   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SupportsFromCeiling.setter
    def SupportsFromCeiling(self, supportsFromCeiling: bool):
        """
        Setter for property: (bool) SupportsFromCeiling
         Returns the option to check , if supports are from ceiling   
            
         
        """
        pass
    
    ## Getter for property: (@link PlatformEquipmentBuilder.TypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.TypeAPI@endlink) TypeEnum
    ##  Returns the platform type enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PlatformEquipmentBuilder.TypeAPI
    @property
    def TypeEnum(self) -> PlatformEquipmentBuilder.TypeAPI:
        """
        Getter for property: (@link PlatformEquipmentBuilder.TypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.TypeAPI@endlink) TypeEnum
         Returns the platform type enum   
            
         
        """
        pass
    
    ## Setter for property: (@link PlatformEquipmentBuilder.TypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.TypeAPI@endlink) TypeEnum

    ##  Returns the platform type enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TypeEnum.setter
    def TypeEnum(self, typeEnum: PlatformEquipmentBuilder.TypeAPI):
        """
        Setter for property: (@link PlatformEquipmentBuilder.TypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.TypeAPI@endlink) TypeEnum
         Returns the platform type enum   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VerticalGridSpacing
    ##  Returns the vertical grid spacing   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VerticalGridSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VerticalGridSpacing
         Returns the vertical grid spacing   
            
         
        """
        pass
    
    ##   
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def SupportCrossSectionButton(self) -> None:
        """
          
        """
        pass
    
import NXOpen
##  use for creating preferences builder <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreatePreferencesBuilder  NXOpen::LineDesigner::LineDesignerManager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """ use for creating preferences builder"""
    pass


import NXOpen
import NXOpen.Assemblies
##  
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateProductionUnitCreatorBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateProductionUnitCreatorBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ProductionUnitCreatorBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """


    ## Getter for property: (str) ProductionUnitId
    ##  Returns the production unit id   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ProductionUnitId(self) -> str:
        """
        Getter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    
    ## Setter for property: (str) ProductionUnitId

    ##  Returns the production unit id   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ProductionUnitId.setter
    def ProductionUnitId(self, productionUnitId: str):
        """
        Setter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    
    ## Getter for property: (str) ProductionUnitName
    ##  Returns the production unit name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ProductionUnitName(self) -> str:
        """
        Getter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    
    ## Setter for property: (str) ProductionUnitName

    ##  Returns the production unit name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ProductionUnitName.setter
    def ProductionUnitName(self, productionUnitName: str):
        """
        Setter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    
    ## Getter for property: (str) ProductionUnitTypeString
    ##  Returns the type of a production unit   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ProductionUnitTypeString(self) -> str:
        """
        Getter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    
    ## Setter for property: (str) ProductionUnitTypeString

    ##  Returns the type of a production unit   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ProductionUnitTypeString.setter
    def ProductionUnitTypeString(self, productionUnitType: str):
        """
        Setter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    
    ##  The assign ID  of production unit
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def AssignId(self) -> None:
        """
         The assign ID  of production unit
        """
        pass
    
    ##  The production unit description
    ##  @return productionUnitDescription (List[str]): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetProductionUnitDescription(self) -> List[str]:
        """
         The production unit description
         @return productionUnitDescription (List[str]): .
        """
        pass
    
    ##  The production unit description is set 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="productionUnitDescription"> (List[str])  </param>
    def SetProductionUnitDescription(self, productionUnitDescription: List[str]) -> None:
        """
         The production unit description is set 
        """
        pass
    
    ##  The production unit parent is set
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="parent"> (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink)  </param>
    def SetProductionUnitParent(self, parent: NXOpen.Assemblies.Partition) -> None:
        """
         The production unit parent is set
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
## 
##         Represents a @link LineDesigner::RailingFeature LineDesigner::RailingFeature@endlink  Features.FeatureBuilder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateRailingFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateRailingFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EnumPostCrossStyle </term> <description> 
##  
## Rectangle </description> </item> 
## 
## <item><term> 
##  
## EnumRailCrossStyle </term> <description> 
##  
## Rectangle </description> </item> 
## 
## <item><term> 
##  
## EnumSpacingType </term> <description> 
##  
## CountandSpan </description> </item> 
## 
## <item><term> 
##  
## IntegerCount </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## LinearDimBottomElevation.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPitchBy.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPostCrossDia.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPostCrossLength.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPostCrossTickness.Value </term> <description> 
##  
## 3.35 (millimeters part), 0.13 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPostCrossWidth.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPostHeight.Value </term> <description> 
##  
## 1067 (millimeters part), 42 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimPostSpacing.Value </term> <description> 
##  
## 500 (millimeters part), 20 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimRailCrossDia.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimRailCrossLength.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.57 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimRailCrossWidth.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OnPathDimSpanBy.Expression.Value </term> <description> 
##  
## 1067 (millimeters part), 42 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PostOffset </term> <description> 
##  
## PostOnCurve </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class RailingFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a <ja_class>LineDesigner.RailingFeature</ja_class> Features.FeatureBuilder
    """


    ##  This enum is providing possible post offset types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PostOnCurve</term><description> 
    ## </description> </item><item><term> 
    ## PostLeftOfCurve</term><description> 
    ## </description> </item><item><term> 
    ## PostRightOfCurve</term><description> 
    ## </description> </item></list>
    class PostOffsetType(Enum):
        """
        Members Include: <PostOnCurve> <PostLeftOfCurve> <PostRightOfCurve>
        """
        PostOnCurve: int
        PostLeftOfCurve: int
        PostRightOfCurve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.PostOffsetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible railing cross styles 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item></list>
    class RailCrossStyle(Enum):
        """
        Members Include: <Rectangle> <Circle>
        """
        Rectangle: int
        Circle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.RailCrossStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible selection post cross styles 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## IBeam</term><description> 
    ## </description> </item><item><term> 
    ## Rectangle</term><description> 
    ## </description> </item><item><term> 
    ## Circle</term><description> 
    ## </description> </item><item><term> 
    ## UserDefine</term><description> 
    ## </description> </item></list>
    class SelPostcrossStyle(Enum):
        """
        Members Include: <IBeam> <Rectangle> <Circle> <UserDefine>
        """
        IBeam: int
        Rectangle: int
        Circle: int
        UserDefine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.SelPostcrossStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is providing possible space types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CountandSpan</term><description> 
    ## </description> </item><item><term> 
    ## PitchandSpan</term><description> 
    ## </description> </item><item><term> 
    ## CountandPitch</term><description> 
    ## </description> </item></list>
    class SpaceType(Enum):
        """
        Members Include: <CountandSpan> <PitchandSpan> <CountandPitch>
        """
        CountandSpan: int
        PitchandSpan: int
        CountandPitch: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.SpaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link RailingFeatureBuilder.SelPostcrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.SelPostcrossStyle@endlink) EnumPostCrossStyle
    ##  Returns the post cross style enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return RailingFeatureBuilder.SelPostcrossStyle
    @property
    def EnumPostCrossStyle(self) -> RailingFeatureBuilder.SelPostcrossStyle:
        """
        Getter for property: (@link RailingFeatureBuilder.SelPostcrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.SelPostcrossStyle@endlink) EnumPostCrossStyle
         Returns the post cross style enum   
            
         
        """
        pass
    
    ## Setter for property: (@link RailingFeatureBuilder.SelPostcrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.SelPostcrossStyle@endlink) EnumPostCrossStyle

    ##  Returns the post cross style enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @EnumPostCrossStyle.setter
    def EnumPostCrossStyle(self, enumPostCrossStyle: RailingFeatureBuilder.SelPostcrossStyle):
        """
        Setter for property: (@link RailingFeatureBuilder.SelPostcrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.SelPostcrossStyle@endlink) EnumPostCrossStyle
         Returns the post cross style enum   
            
         
        """
        pass
    
    ## Getter for property: (@link RailingFeatureBuilder.RailCrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.RailCrossStyle@endlink) EnumRailCrossStyle
    ##  Returns the railing cross style enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return RailingFeatureBuilder.RailCrossStyle
    @property
    def EnumRailCrossStyle(self) -> RailingFeatureBuilder.RailCrossStyle:
        """
        Getter for property: (@link RailingFeatureBuilder.RailCrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.RailCrossStyle@endlink) EnumRailCrossStyle
         Returns the railing cross style enum   
            
         
        """
        pass
    
    ## Setter for property: (@link RailingFeatureBuilder.RailCrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.RailCrossStyle@endlink) EnumRailCrossStyle

    ##  Returns the railing cross style enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @EnumRailCrossStyle.setter
    def EnumRailCrossStyle(self, enumRailCrossStyle: RailingFeatureBuilder.RailCrossStyle):
        """
        Setter for property: (@link RailingFeatureBuilder.RailCrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.RailCrossStyle@endlink) EnumRailCrossStyle
         Returns the railing cross style enum   
            
         
        """
        pass
    
    ## Getter for property: (@link RailingFeatureBuilder.SpaceType NXOpen.LineDesigner.RailingFeatureBuilder.SpaceType@endlink) EnumSpacingType
    ##  Returns an API to get spacing type enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return RailingFeatureBuilder.SpaceType
    @property
    def EnumSpacingType(self) -> RailingFeatureBuilder.SpaceType:
        """
        Getter for property: (@link RailingFeatureBuilder.SpaceType NXOpen.LineDesigner.RailingFeatureBuilder.SpaceType@endlink) EnumSpacingType
         Returns an API to get spacing type enum   
            
         
        """
        pass
    
    ## Setter for property: (@link RailingFeatureBuilder.SpaceType NXOpen.LineDesigner.RailingFeatureBuilder.SpaceType@endlink) EnumSpacingType

    ##  Returns an API to get spacing type enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @EnumSpacingType.setter
    def EnumSpacingType(self, enumSpacingType: RailingFeatureBuilder.SpaceType):
        """
        Setter for property: (@link RailingFeatureBuilder.SpaceType NXOpen.LineDesigner.RailingFeatureBuilder.SpaceType@endlink) EnumSpacingType
         Returns an API to get spacing type enum   
            
         
        """
        pass
    
    ## Getter for property: (int) IntegerCount
    ##  Returns an API to get integer count   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def IntegerCount(self) -> int:
        """
        Getter for property: (int) IntegerCount
         Returns an API to get integer count   
            
         
        """
        pass
    
    ## Setter for property: (int) IntegerCount

    ##  Returns an API to get integer count   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IntegerCount.setter
    def IntegerCount(self, integerCount: int):
        """
        Setter for property: (int) IntegerCount
         Returns an API to get integer count   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSketchInternal
    ##  Returns an API to check if sketch is internal    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IsSketchInternal(self) -> bool:
        """
        Getter for property: (bool) IsSketchInternal
         Returns an API to check if sketch is internal    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSketchInternal

    ##  Returns an API to check if sketch is internal    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @IsSketchInternal.setter
    def IsSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) IsSketchInternal
         Returns an API to check if sketch is internal    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimBottomElevation
    ##  Returns an API to get bottom elevation   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimBottomElevation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimBottomElevation
         Returns an API to get bottom elevation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPitchBy
    ##  Returns an API to get pitch by   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPitchBy(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPitchBy
         Returns an API to get pitch by   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossDia
    ##  Returns the post cross dimension of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPostCrossDia(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossDia
         Returns the post cross dimension of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossLength
    ##  Returns the post cross length  of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPostCrossLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossLength
         Returns the post cross length  of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossTickness
    ##  Returns the post cross thickness  of railing feature    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPostCrossTickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossTickness
         Returns the post cross thickness  of railing feature    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossWidth
    ##  Returns the post cross width  of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPostCrossWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostCrossWidth
         Returns the post cross width  of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostHeight
    ##  Returns the post height of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPostHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostHeight
         Returns the post height of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostSpacing
    ##  Returns the post spacing  of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimPostSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimPostSpacing
         Returns the post spacing  of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimRailCrossDia
    ##  Returns an API to get railing cross diamension   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimRailCrossDia(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimRailCrossDia
         Returns an API to get railing cross diamension   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimRailCrossLength
    ##  Returns the railing cross length of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimRailCrossLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimRailCrossLength
         Returns the railing cross length of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimRailCrossWidth
    ##  Returns the railing cross width  of railing feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimRailCrossWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimRailCrossWidth
         Returns the railing cross width  of railing feature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) OnPathDimSpanBy
    ##  Returns an API to get on path dimension span by   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.OnPathDimensionBuilder
    @property
    def OnPathDimSpanBy(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) OnPathDimSpanBy
         Returns an API to get on path dimension span by   
            
         
        """
        pass
    
    ## Getter for property: (@link RailingFeatureBuilder.PostOffsetType NXOpen.LineDesigner.RailingFeatureBuilder.PostOffsetType@endlink) PostOffset
    ##  Returns the post offset  of railing feature    
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return RailingFeatureBuilder.PostOffsetType
    @property
    def PostOffset(self) -> RailingFeatureBuilder.PostOffsetType:
        """
        Getter for property: (@link RailingFeatureBuilder.PostOffsetType NXOpen.LineDesigner.RailingFeatureBuilder.PostOffsetType@endlink) PostOffset
         Returns the post offset  of railing feature    
            
         
        """
        pass
    
    ## Setter for property: (@link RailingFeatureBuilder.PostOffsetType NXOpen.LineDesigner.RailingFeatureBuilder.PostOffsetType@endlink) PostOffset

    ##  Returns the post offset  of railing feature    
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PostOffset.setter
    def PostOffset(self, postOffset: RailingFeatureBuilder.PostOffsetType):
        """
        Setter for property: (@link RailingFeatureBuilder.PostOffsetType NXOpen.LineDesigner.RailingFeatureBuilder.PostOffsetType@endlink) PostOffset
         Returns the post offset  of railing feature    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectionCurves
    ##  Returns the selected curves are return   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SelectionCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectionCurves
         Returns the selected curves are return   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectionPostCrossSection
    ##  Returns the selection post cross section   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SelectionPostCrossSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectionPostCrossSection
         Returns the selection post cross section   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a rail feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::RailingFeatureBuilder  NXOpen::LineDesigner::RailingFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class RailingFeature(NXOpen.Features.Feature): 
    """ Represents a rail feature """
    pass


import NXOpen
import NXOpen.Features
## 
##     Represents a @link LineDesigner::RailOpeningFeature LineDesigner::RailOpeningFeature@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateRailOpeningFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateRailOpeningFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## LinearDimElevation.Value </term> <description> 
##  
## 650 (millimeters part), 25.6 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimGateThickness.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LinearDimOpeningWidth.Value </term> <description> 
##  
## 350 (millimeters part), 14 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OpeningAddGate </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## OpeningStyleEnum </term> <description> 
##  
## Left </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class RailOpeningFeatureBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>LineDesigner.RailOpeningFeature</ja_class> builder
    """


    ##   This enum is providing possible gate opening styles
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Middle</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item></list>
    class GateOpeningStyle(Enum):
        """
        Members Include: <Left> <Middle> <Right>
        """
        Left: int
        Middle: int
        Right: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RailOpeningFeatureBuilder.GateOpeningStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimElevation
    ##  Returns the rail opening elevation   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimElevation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimElevation
         Returns the rail opening elevation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimGateThickness
    ##  Returns the gate thickness   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimGateThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimGateThickness
         Returns the gate thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimOpeningWidth
    ##  Returns the rail opening width   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearDimOpeningWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearDimOpeningWidth
         Returns the rail opening width   
            
         
        """
        pass
    
    ## Getter for property: (bool) OpeningAddGate
    ##  Returns the opening add gate is return  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def OpeningAddGate(self) -> bool:
        """
        Getter for property: (bool) OpeningAddGate
         Returns the opening add gate is return  
            
         
        """
        pass
    
    ## Setter for property: (bool) OpeningAddGate

    ##  Returns the opening add gate is return  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OpeningAddGate.setter
    def OpeningAddGate(self, openingAddGate: bool):
        """
        Setter for property: (bool) OpeningAddGate
         Returns the opening add gate is return  
            
         
        """
        pass
    
    ## Getter for property: (@link RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.RailOpeningFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum
    ##  Returns the rail opening style enum   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return RailOpeningFeatureBuilder.GateOpeningStyle
    @property
    def OpeningStyleEnum(self) -> RailOpeningFeatureBuilder.GateOpeningStyle:
        """
        Getter for property: (@link RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.RailOpeningFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum
         Returns the rail opening style enum   
            
         
        """
        pass
    
    ## Setter for property: (@link RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.RailOpeningFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum

    ##  Returns the rail opening style enum   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OpeningStyleEnum.setter
    def OpeningStyleEnum(self, openingStyleEnum: RailOpeningFeatureBuilder.GateOpeningStyle):
        """
        Setter for property: (@link RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.RailOpeningFeatureBuilder.GateOpeningStyle@endlink) OpeningStyleEnum
         Returns the rail opening style enum   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseDirection
    ##  Returns the reverse direction of rail opening   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction of rail opening   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseDirection

    ##  Returns the reverse direction of rail opening   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction of rail opening   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
    ##  Returns the selected point of rail opening feature   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def SelectPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
         Returns the selected point of rail opening feature   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint

    ##  Returns the selected point of rail opening feature   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SelectPoint.setter
    def SelectPoint(self, selectPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
         Returns the selected point of rail opening feature   
            
         
        """
        pass
    
    ##  Direction of rail opening 
    ##  @return dirVector (@link NXOpen.Direction NXOpen.Direction@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetDirVector(self) -> NXOpen.Direction:
        """
         Direction of rail opening 
         @return dirVector (@link NXOpen.Direction NXOpen.Direction@endlink): .
        """
        pass
    
    ##       
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="dirVector"> (@link NXOpen.Direction NXOpen.Direction@endlink) </param>
    def SetDirVector(self, dirVector: NXOpen.Direction) -> None:
        """
              
        """
        pass
    
    ##      
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="railingFrec"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) </param>
    def SetRailingFeature(self, railingFrec: NXOpen.Features.Feature) -> None:
        """
             
        """
        pass
    
import NXOpen.Features
##  Represents a rail Opening feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::RailOpeningFeatureBuilder  NXOpen::LineDesigner::RailOpeningFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class RailOpeningFeature(NXOpen.Features.Feature): 
    """ Represents a rail Opening feature """
    pass


import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateRenameDialogeBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateRenameDialogeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## NumberingStartAt </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## SelectionEnum </term> <description> 
##  
## ItemRevisionName </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 

class RenameDialogeBuilder(NXOpen.Builder): 
    """  """


    ##  This enum is providing selection of occurence or iteme revision name for rename 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ItemRevisionName</term><description> 
    ## </description> </item><item><term> 
    ## OccurenceName</term><description> 
    ## </description> </item></list>
    class SelectionTypeAPI(Enum):
        """
        Members Include: <ItemRevisionName> <OccurenceName>
        """
        ItemRevisionName: int
        OccurenceName: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RenameDialogeBuilder.SelectionTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Name
    ##  Returns the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberingStartAt
    ##  Returns the numbering start at   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def NumberingStartAt(self) -> int:
        """
        Getter for property: (int) NumberingStartAt
         Returns the numbering start at   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberingStartAt

    ##  Returns the numbering start at   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @NumberingStartAt.setter
    def NumberingStartAt(self, numberingStartAt: int):
        """
        Setter for property: (int) NumberingStartAt
         Returns the numbering start at   
            
         
        """
        pass
    
    ## Getter for property: (@link RenameDialogeBuilder.SelectionTypeAPI NXOpen.LineDesigner.RenameDialogeBuilder.SelectionTypeAPI@endlink) SelectionEnum
    ##  Returns the item or occurence selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return RenameDialogeBuilder.SelectionTypeAPI
    @property
    def SelectionEnum(self) -> RenameDialogeBuilder.SelectionTypeAPI:
        """
        Getter for property: (@link RenameDialogeBuilder.SelectionTypeAPI NXOpen.LineDesigner.RenameDialogeBuilder.SelectionTypeAPI@endlink) SelectionEnum
         Returns the item or occurence selection   
            
         
        """
        pass
    
    ## Setter for property: (@link RenameDialogeBuilder.SelectionTypeAPI NXOpen.LineDesigner.RenameDialogeBuilder.SelectionTypeAPI@endlink) SelectionEnum

    ##  Returns the item or occurence selection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @SelectionEnum.setter
    def SelectionEnum(self, selectionEnum: RenameDialogeBuilder.SelectionTypeAPI):
        """
        Setter for property: (@link RenameDialogeBuilder.SelectionTypeAPI NXOpen.LineDesigner.RenameDialogeBuilder.SelectionTypeAPI@endlink) SelectionEnum
         Returns the item or occurence selection   
            
         
        """
        pass
    
import NXOpen
##    <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateRenameItemRevisionBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateRenameItemRevisionBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.3  <br> 

class RenameItemRevisionBuilder(NXOpen.Builder): 
    """  """


    ## Getter for property: (str) ItemRevisionName
    ##  Returns the item revision name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def ItemRevisionName(self) -> str:
        """
        Getter for property: (str) ItemRevisionName
         Returns the item revision name   
            
         
        """
        pass
    
    ## Setter for property: (str) ItemRevisionName

    ##  Returns the item revision name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @ItemRevisionName.setter
    def ItemRevisionName(self, itemRevisionName: str):
        """
        Setter for property: (str) ItemRevisionName
         Returns the item revision name   
            
         
        """
        pass
    
    ## Getter for property: (str) OccurrenceName
    ##  Returns the occurrence name is return   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return str
    @property
    def OccurrenceName(self) -> str:
        """
        Getter for property: (str) OccurrenceName
         Returns the occurrence name is return   
            
         
        """
        pass
    
    ## Setter for property: (str) OccurrenceName

    ##  Returns the occurrence name is return   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @OccurrenceName.setter
    def OccurrenceName(self, occurrenceName: str):
        """
        Setter for property: (str) OccurrenceName
         Returns the occurrence name is return   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) PartOccurence
    ##  Returns the part occurence   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def PartOccurence(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) PartOccurence
         Returns the part occurence   
            
         
        """
        pass
    
import NXOpen
## 
##     
##     
##     
##     
##     
##       <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateResizeConnectorBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateResizeConnectorBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConnectorSize </term> <description> 
##  
## 50.0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class ResizeConnectorBuilder(NXOpen.Builder): 
    """
    
    
    
    
    
     """


    ## Getter for property: (float) ConnectorSize
    ##  Returnsthe current connector size   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def ConnectorSize(self) -> float:
        """
        Getter for property: (float) ConnectorSize
         Returnsthe current connector size   
            
         
        """
        pass
    
    ## Setter for property: (float) ConnectorSize

    ##  Returnsthe current connector size   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConnectorSize.setter
    def ConnectorSize(self, connectorSize: float):
        """
        Setter for property: (float) ConnectorSize
         Returnsthe current connector size   
            
         
        """
        pass
    
import NXOpen
##  Represents a manager of line designer plant model  <br> Established by LineDesigner_ReuseLibraryUtilityBuilder whenever it is needed.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ReuseLibraryDragData(NXOpen.NXObject): 
    """ Represents a manager of line designer plant model """


    ## Getter for property: (int) ActionType
    ##  Returns the action type of drag data   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ActionType(self) -> int:
        """
        Getter for property: (int) ActionType
         Returns the action type of drag data   
            
         
        """
        pass
    
    ## Setter for property: (int) ActionType

    ##  Returns the action type of drag data   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ActionType.setter
    def ActionType(self, actionType: int):
        """
        Setter for property: (int) ActionType
         Returns the action type of drag data   
            
         
        """
        pass
    
    ## Getter for property: (str) CategoryName
    ##  Returns the category name of Drag Data   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def CategoryName(self) -> str:
        """
        Getter for property: (str) CategoryName
         Returns the category name of Drag Data   
            
         
        """
        pass
    
    ## Setter for property: (str) CategoryName

    ##  Returns the category name of Drag Data   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CategoryName.setter
    def CategoryName(self, categoryName: str):
        """
        Setter for property: (str) CategoryName
         Returns the category name of Drag Data   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasCsysImport
    ##  Returns an API to check if drag data has csys import   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def HasCsysImport(self) -> bool:
        """
        Getter for property: (bool) HasCsysImport
         Returns an API to check if drag data has csys import   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasCsysImport

    ##  Returns an API to check if drag data has csys import   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @HasCsysImport.setter
    def HasCsysImport(self, hasCsysImport: bool):
        """
        Setter for property: (bool) HasCsysImport
         Returns an API to check if drag data has csys import   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasSketchImport
    ##  Returns an API to check if drag data has sketch to import   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def HasSketchImport(self) -> bool:
        """
        Getter for property: (bool) HasSketchImport
         Returns an API to check if drag data has sketch to import   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasSketchImport

    ##  Returns an API to check if drag data has sketch to import   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @HasSketchImport.setter
    def HasSketchImport(self, hasSketchImport: bool):
        """
        Setter for property: (bool) HasSketchImport
         Returns an API to check if drag data has sketch to import   
            
         
        """
        pass
    
    ## Getter for property: (str) KrxFile
    ##  Returns the krx file name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def KrxFile(self) -> str:
        """
        Getter for property: (str) KrxFile
         Returns the krx file name   
            
         
        """
        pass
    
    ## Setter for property: (str) KrxFile

    ##  Returns the krx file name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @KrxFile.setter
    def KrxFile(self, krxFile: str):
        """
        Setter for property: (str) KrxFile
         Returns the krx file name   
            
         
        """
        pass
    
    ## Getter for property: (str) LibName
    ##  Returns the library name of  Reuse Library Drag data  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def LibName(self) -> str:
        """
        Getter for property: (str) LibName
         Returns the library name of  Reuse Library Drag data  
            
         
        """
        pass
    
    ## Setter for property: (str) LibName

    ##  Returns the library name of  Reuse Library Drag data  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LibName.setter
    def LibName(self, libName: str):
        """
        Setter for property: (str) LibName
         Returns the library name of  Reuse Library Drag data  
            
         
        """
        pass
    
    ## Getter for property: (int) NativeItem
    ##  Returns the native item   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def NativeItem(self) -> int:
        """
        Getter for property: (int) NativeItem
         Returns the native item   
            
         
        """
        pass
    
    ## Setter for property: (int) NativeItem

    ##  Returns the native item   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NativeItem.setter
    def NativeItem(self, nativeItem: int):
        """
        Setter for property: (int) NativeItem
         Returns the native item   
            
         
        """
        pass
    
    ## Getter for property: (str) ObjectId
    ##  Returns the object id of Drag Data  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ObjectId(self) -> str:
        """
        Getter for property: (str) ObjectId
         Returns the object id of Drag Data  
            
         
        """
        pass
    
    ## Setter for property: (str) ObjectId

    ##  Returns the object id of Drag Data  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ObjectId.setter
    def ObjectId(self, objectId: str):
        """
        Setter for property: (str) ObjectId
         Returns the object id of Drag Data  
            
         
        """
        pass
    
    ## Getter for property: (str) PartFile
    ##  Returns the part file name is return   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def PartFile(self) -> str:
        """
        Getter for property: (str) PartFile
         Returns the part file name is return   
            
         
        """
        pass
    
    ## Setter for property: (str) PartFile

    ##  Returns the part file name is return   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PartFile.setter
    def PartFile(self, partFile: str):
        """
        Setter for property: (str) PartFile
         Returns the part file name is return   
            
         
        """
        pass
    
    ## Getter for property: (int) PartType
    ##  Returns the part type of Reuse Library Drag data   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def PartType(self) -> int:
        """
        Getter for property: (int) PartType
         Returns the part type of Reuse Library Drag data   
            
         
        """
        pass
    
    ## Setter for property: (int) PartType

    ##  Returns the part type of Reuse Library Drag data   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PartType.setter
    def PartType(self, partType: int):
        """
        Setter for property: (int) PartType
         Returns the part type of Reuse Library Drag data   
            
         
        """
        pass
    
    ## Getter for property: (str) PathInLib
    ##  Returns the path in library of drag data  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def PathInLib(self) -> str:
        """
        Getter for property: (str) PathInLib
         Returns the path in library of drag data  
            
         
        """
        pass
    
    ## Setter for property: (str) PathInLib

    ##  Returns the path in library of drag data  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PathInLib.setter
    def PathInLib(self, pathInLib: str):
        """
        Setter for property: (str) PathInLib
         Returns the path in library of drag data  
            
         
        """
        pass
    
    ## Getter for property: (bool) SpareDialogForDragAndDrop
    ##  Returns an API to check if spare dialog for drag and drop is allowed   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def SpareDialogForDragAndDrop(self) -> bool:
        """
        Getter for property: (bool) SpareDialogForDragAndDrop
         Returns an API to check if spare dialog for drag and drop is allowed   
            
         
        """
        pass
    
    ## Setter for property: (bool) SpareDialogForDragAndDrop

    ##  Returns an API to check if spare dialog for drag and drop is allowed   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SpareDialogForDragAndDrop.setter
    def SpareDialogForDragAndDrop(self, spareDialogForDragAndDrop: bool):
        """
        Setter for property: (bool) SpareDialogForDragAndDrop
         Returns an API to check if spare dialog for drag and drop is allowed   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateName
    ##  Returns the template name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def TemplateName(self) -> str:
        """
        Getter for property: (str) TemplateName
         Returns the template name   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateName

    ##  Returns the template name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TemplateName.setter
    def TemplateName(self, templateName: str):
        """
        Setter for property: (str) TemplateName
         Returns the template name   
            
         
        """
        pass
    
    ## Getter for property: (str) TypeName
    ##  Returns an API to get type name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def TypeName(self) -> str:
        """
        Getter for property: (str) TypeName
         Returns an API to get type name   
            
         
        """
        pass
    
    ## Setter for property: (str) TypeName

    ##  Returns an API to get type name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TypeName.setter
    def TypeName(self, typeName: str):
        """
        Setter for property: (str) TypeName
         Returns an API to get type name   
            
         
        """
        pass
    
import NXOpen
##  Represents a JA for ReuseLibraryUtility  <br> Established by LineDesigner_LineDesignerManager whenever it is needed.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ReuseLibraryUtilityBuilder(NXOpen.TaggedObject): 
    """ Represents a JA for ReuseLibraryUtility """


    ## Getter for property: (bool) DoNormalCloning
    ##  Returns the normal drop or cloning Drop   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    ## @return bool
    @property
    def DoNormalCloning(self) -> bool:
        """
        Getter for property: (bool) DoNormalCloning
         Returns the normal drop or cloning Drop   
            
         
        """
        pass
    
    ## Setter for property: (bool) DoNormalCloning

    ##  Returns the normal drop or cloning Drop   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    @DoNormalCloning.setter
    def DoNormalCloning(self, doNormalCloning: bool):
        """
        Setter for property: (bool) DoNormalCloning
         Returns the normal drop or cloning Drop   
            
         
        """
        pass
    
    ##   To allows cloning of data set attched to FCAD object 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="bRenameAssembly"> (bool) </param>
    def CloneForFCADDataSet(self, part: NXOpen.NXObject, bRenameAssembly: bool) -> None:
        """
          To allows cloning of data set attched to FCAD object 
        """
        pass
    
    ##  To create drag data 
    ##  @return dragData (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def CreateDragData(self) -> ReuseLibraryDragData:
        """
         To create drag data 
         @return dragData (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink): .
        """
        pass
    
    ##  Mark Drag and Drop as completed 
    ## 
    ##   <br>  Created in NX2312.3000.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def DragAndDropCompleted(self, part: NXOpen.NXObject) -> None:
        """
         Mark Drag and Drop as completed 
        """
        pass
    
    ##   To handle dropping of LD smart part 
    ##  @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="reuseLibraryDragData"> (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink) </param>
    ## <param name="dropPoint"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def DropFCADPartInNative(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
          To handle dropping of LD smart part 
         @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##   To handle dropping of knowledge enabled part KRU_KE_PART 
    ##  @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="reuseLibraryDragData"> (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink) </param>
    ## <param name="dropPoint"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="isSkipAddReusableCompUI"> (bool) </param>
    def DropKnowledgeEnabledPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d, isSkipAddReusableCompUI: bool) -> NXOpen.NXObject:
        """
          To handle dropping of knowledge enabled part KRU_KE_PART 
         @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##   To handle dropping of LD smart part 
    ##  @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="reuseLibraryDragData"> (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink) </param>
    ## <param name="dropPoint"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def DropLDSmartPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
          To handle dropping of LD smart part 
         @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##   To handle dropping of normal part 
    ##  @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="reuseLibraryDragData"> (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink) </param>
    ## <param name="dropPoint"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def DropNormalPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
          To handle dropping of normal part 
         @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##   To handle dropping of other part 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="reuseLibraryDragData"> (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink) </param>
    ## <param name="dropPoint"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def DropOtherPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> None:
        """
          To handle dropping of other part 
        """
        pass
    
    ##  To handle dropping of PTS part 
    ##  @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="reuseLibraryDragData"> (@link ReuseLibraryDragData NXOpen.LineDesigner.ReuseLibraryDragData@endlink) </param>
    ## <param name="dropPoint"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def DropPTSPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
         To handle dropping of PTS part 
         @return droppedPart (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##   To executes the renaming of the cloned component when it is added under an assembly 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ExecuteRenameAssembly(self) -> None:
        """
          To executes the renaming of the cloned component when it is added under an assembly 
        """
        pass
    
    ##  Get dialog file name for object getting inserting  
    ##  @return dlgFilePath (str): .
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def GetDLGFile(self, part: NXOpen.NXObject) -> str:
        """
         Get dialog file name for object getting inserting  
         @return dlgFilePath (str): .
        """
        pass
    
    ##  Get Geo file name for object getting inserting  
    ##  @return geoFileName (str): .
    ## 
    ##   <br>  Created in NX1855.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def GetGEOFile(self, part: NXOpen.NXObject) -> str:
        """
         Get Geo file name for object getting inserting  
         @return geoFileName (str): .
        """
        pass
    
    ##  Get Parameter file name for object getting inserting  
    ##  @return parameterSetFilePath (str): .
    ## 
    ##   <br>  Created in NX1876.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def GetParameterSetFile(self, part: NXOpen.NXObject) -> str:
        """
         Get Parameter file name for object getting inserting  
         @return parameterSetFilePath (str): .
        """
        pass
    
    ##   To keep source library item ID 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="keepSourcePath"> (bool) </param>
    def KeepSourceLibraryID(self, part: NXOpen.NXObject, keepSourcePath: bool) -> None:
        """
          To keep source library item ID 
        """
        pass
    
    ##   To load data set attched to FCAD object 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def LoadFCADGeoFile(self, part: NXOpen.NXObject) -> None:
        """
          To load data set attched to FCAD object 
        """
        pass
    
    ##   To mount tool from library on robot 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="connectorFaceTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def MountToolOnRobot(self, part: NXOpen.NXObject, connectorFaceTag: NXOpen.TaggedObject) -> None:
        """
          To mount tool from library on robot 
        """
        pass
    
    ##  Move component to the location 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="position"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def MoveComponentToLocation(self, part: NXOpen.NXObject, position: NXOpen.Vector3d) -> None:
        """
         Move component to the location 
        """
        pass
    
    ##   To place part from library using connector 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="connectorFaceTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def PlacementByConnector(self, part: NXOpen.NXObject, connectorFaceTag: NXOpen.TaggedObject) -> None:
        """
          To place part from library using connector 
        """
        pass
    
    ##   To populate MDO information 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def PopulateMDOInfo(self, part: NXOpen.NXObject) -> None:
        """
          To populate MDO information 
        """
        pass
    
    ##   To update cloned part 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def UpdateClonedPartTag(self, part: NXOpen.NXObject) -> None:
        """
          To update cloned part 
        """
        pass
    
import NXOpen
##  Create a builder to rotate a component by 90 degrees. <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateRotateComponentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateRotateComponentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngularDim.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RotateAsGroup </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class RotateComponentBuilder(NXOpen.Builder): 
    """ Create a builder to rotate a component by 90 degrees."""


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularDim
    ##  Returns the angular dimension for rotate component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularDim(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularDim
         Returns the angular dimension for rotate component   
            
         
        """
        pass
    
    ## Getter for property: (bool) RotateAsGroup
    ##  Returns the toggle to rotate as group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def RotateAsGroup(self) -> bool:
        """
        Getter for property: (bool) RotateAsGroup
         Returns the toggle to rotate as group   
            
         
        """
        pass
    
    ## Setter for property: (bool) RotateAsGroup

    ##  Returns the toggle to rotate as group   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @RotateAsGroup.setter
    def RotateAsGroup(self, toggle: bool):
        """
        Setter for property: (bool) RotateAsGroup
         Returns the toggle to rotate as group   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
    ##  Returns the selected component   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
         Returns the selected component   
            
         
        """
        pass
    
import NXOpen
## 
##     
##     
##     
##     
##     
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateSelectionToolBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateSelectionToolBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AddOption </term> <description> 
##  
## Add </description> </item> 
## 
## <item><term> 
##  
## AddToReferenceSet </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ExcludeConnectors </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ExcludeSmallObjects </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IncludeAboveZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## View </term> <description> 
##  
## AllFourteen </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1938.0.0  <br> 

class SelectionToolBuilder(NXOpen.Builder): 
    """
    
    
    
    
    
    """


    ## This enum provides options for adding or replacing objects to reference set 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Add</term><description> 
    ## </description> </item><item><term> 
    ## Replace</term><description> 
    ## </description> </item></list>
    class RefSetOption(Enum):
        """
        Members Include: <Add> <Replace>
        """
        Add: int
        Replace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SelectionToolBuilder.RefSetOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## This enum provides view options for calculating the selection 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SixStandard</term><description> 
    ## </description> </item><item><term> 
    ## EightIsometric</term><description> 
    ## </description> </item><item><term> 
    ## AllFourteen</term><description> 
    ## </description> </item></list>
    class SelectionView(Enum):
        """
        Members Include: <SixStandard> <EightIsometric> <AllFourteen>
        """
        SixStandard: int
        EightIsometric: int
        AllFourteen: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SelectionToolBuilder.SelectionView:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectionToolBuilder.RefSetOption NXOpen.LineDesigner.SelectionToolBuilder.RefSetOption@endlink) AddOption
    ##  Returns the add option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return SelectionToolBuilder.RefSetOption
    @property
    def AddOption(self) -> SelectionToolBuilder.RefSetOption:
        """
        Getter for property: (@link SelectionToolBuilder.RefSetOption NXOpen.LineDesigner.SelectionToolBuilder.RefSetOption@endlink) AddOption
         Returns the add option   
            
         
        """
        pass
    
    ## Setter for property: (@link SelectionToolBuilder.RefSetOption NXOpen.LineDesigner.SelectionToolBuilder.RefSetOption@endlink) AddOption

    ##  Returns the add option   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @AddOption.setter
    def AddOption(self, addOption: SelectionToolBuilder.RefSetOption):
        """
        Setter for property: (@link SelectionToolBuilder.RefSetOption NXOpen.LineDesigner.SelectionToolBuilder.RefSetOption@endlink) AddOption
         Returns the add option   
            
         
        """
        pass
    
    ## Getter for property: (bool) AddToReferenceSet
    ##  Returns the add to Reference set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return bool
    @property
    def AddToReferenceSet(self) -> bool:
        """
        Getter for property: (bool) AddToReferenceSet
         Returns the add to Reference set   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddToReferenceSet

    ##  Returns the add to Reference set   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @AddToReferenceSet.setter
    def AddToReferenceSet(self, addToRefSet: bool):
        """
        Setter for property: (bool) AddToReferenceSet
         Returns the add to Reference set   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExcludeConnectors
    ##  Returns the exclude connectors toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return bool
    @property
    def ExcludeConnectors(self) -> bool:
        """
        Getter for property: (bool) ExcludeConnectors
         Returns the exclude connectors toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ExcludeConnectors

    ##  Returns the exclude connectors toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @ExcludeConnectors.setter
    def ExcludeConnectors(self, excludeConnectors: bool):
        """
        Setter for property: (bool) ExcludeConnectors
         Returns the exclude connectors toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExcludeObjectSize
    ##  Returns the exclude small object size  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExcludeObjectSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExcludeObjectSize
         Returns the exclude small object size  
            
         
        """
        pass
    
    ## Getter for property: (bool) ExcludeSmallObjects
    ##  Returns the exclude object toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return bool
    @property
    def ExcludeSmallObjects(self) -> bool:
        """
        Getter for property: (bool) ExcludeSmallObjects
         Returns the exclude object toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ExcludeSmallObjects

    ##  Returns the exclude object toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @ExcludeSmallObjects.setter
    def ExcludeSmallObjects(self, excludeSmallObjects: bool):
        """
        Setter for property: (bool) ExcludeSmallObjects
         Returns the exclude object toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeAboveZ
    ##  Returns the include above z   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return bool
    @property
    def IncludeAboveZ(self) -> bool:
        """
        Getter for property: (bool) IncludeAboveZ
         Returns the include above z   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeAboveZ

    ##  Returns the include above z   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @IncludeAboveZ.setter
    def IncludeAboveZ(self, includeAboveZ: bool):
        """
        Setter for property: (bool) IncludeAboveZ
         Returns the include above z   
            
         
        """
        pass
    
    ## Getter for property: (str) SelectedRefSet
    ##  Returns the selected ref set name string   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return str
    @property
    def SelectedRefSet(self) -> str:
        """
        Getter for property: (str) SelectedRefSet
         Returns the selected ref set name string   
            
         
        """
        pass
    
    ## Setter for property: (str) SelectedRefSet

    ##  Returns the selected ref set name string   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @SelectedRefSet.setter
    def SelectedRefSet(self, refSetName: str):
        """
        Setter for property: (str) SelectedRefSet
         Returns the selected ref set name string   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionToolBuilder.SelectionView NXOpen.LineDesigner.SelectionToolBuilder.SelectionView@endlink) View
    ##  Returns the view   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return SelectionToolBuilder.SelectionView
    @property
    def View(self) -> SelectionToolBuilder.SelectionView:
        """
        Getter for property: (@link SelectionToolBuilder.SelectionView NXOpen.LineDesigner.SelectionToolBuilder.SelectionView@endlink) View
         Returns the view   
            
         
        """
        pass
    
    ## Setter for property: (@link SelectionToolBuilder.SelectionView NXOpen.LineDesigner.SelectionToolBuilder.SelectionView@endlink) View

    ##  Returns the view   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @View.setter
    def View(self, view: SelectionToolBuilder.SelectionView):
        """
        Setter for property: (@link SelectionToolBuilder.SelectionView NXOpen.LineDesigner.SelectionToolBuilder.SelectionView@endlink) View
         Returns the view   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def CalculateSelection(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def InvertSelection(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ShowAll(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ShowOnly(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
import NXOpen
##       <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateSingleElementConveyorBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateSingleElementConveyorBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SingleElementConveyorBuilder(NXOpen.Builder): 
    """     """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstConveyingSurfaceCroner
    ##  Returns the first conveying surface corner of conveyor  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def FirstConveyingSurfaceCroner(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstConveyingSurfaceCroner
         Returns the first conveying surface corner of conveyor  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstConveyingSurfaceCroner

    ##  Returns the first conveying surface corner of conveyor  
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FirstConveyingSurfaceCroner.setter
    def FirstConveyingSurfaceCroner(self, firstConveyingSurfaceCroner: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstConveyingSurfaceCroner
         Returns the first conveying surface corner of conveyor  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
    ##  Returns the kf object   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.KFObject
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
         Returns the kf object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovingDirection
    ##  Returns the moving direction of conveyor   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def MovingDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovingDirection
         Returns the moving direction of conveyor   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovingDirection

    ##  Returns the moving direction of conveyor   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MovingDirection.setter
    def MovingDirection(self, dirVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MovingDirection
         Returns the moving direction of conveyor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnConveyingSurface
    ##  Returns the point on surface of conveyor are return   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointOnConveyingSurface(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnConveyingSurface
         Returns the point on surface of conveyor are return   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnConveyingSurface

    ##  Returns the point on surface of conveyor are return   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PointOnConveyingSurface.setter
    def PointOnConveyingSurface(self, pointOnConveyingSurface: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnConveyingSurface
         Returns the point on surface of conveyor are return   
            
         
        """
        pass
    
    ## Getter for property: (bool) Reversible
    ##  Returns the option to check whether conveyor is reversible   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Reversible(self) -> bool:
        """
        Getter for property: (bool) Reversible
         Returns the option to check whether conveyor is reversible   
            
         
        """
        pass
    
    ## Setter for property: (bool) Reversible

    ##  Returns the option to check whether conveyor is reversible   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Reversible.setter
    def Reversible(self, reversible: bool):
        """
        Setter for property: (bool) Reversible
         Returns the option to check whether conveyor is reversible   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondConveyingSurfaceCorner
    ##  Returns the second conveying surface corner of conveyor   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def SecondConveyingSurfaceCorner(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondConveyingSurfaceCorner
         Returns the second conveying surface corner of conveyor   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondConveyingSurfaceCorner

    ##  Returns the second conveying surface corner of conveyor   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SecondConveyingSurfaceCorner.setter
    def SecondConveyingSurfaceCorner(self, secondConveyingSurfaceCorner: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondConveyingSurfaceCorner
         Returns the second conveying surface corner of conveyor   
            
         
        """
        pass
    
import NXOpen
##     <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateStairwayEquipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateStairwayEquipmentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AddRiserToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## AddStringerToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## EndElevation.Value </term> <description> 
##  
## 2425 (millimeters part), 117 (inches part) </description> </item> 
## 
## <item><term> 
##  
## NoOfStairs </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## Rise.Value </term> <description> 
##  
## 175 (millimeters part), 7 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Run.Value </term> <description> 
##  
## 280 (millimeters part), 11 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StairNosing.Value </term> <description> 
##  
## 13 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StairWidth.Value </term> <description> 
##  
## 915 (millimeters part), 36 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StartElevation.Value </term> <description> 
##  
## 4000 (millimeters part), 180 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StringerHeight.Value </term> <description> 
##  
## 305 (millimeters part), 12 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StringerWidth.Value </term> <description> 
##  
## 37.5 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TotalRise.Value </term> <description> 
##  
## -1575 (millimeters part), -63 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TotalRun.Value </term> <description> 
##  
## 2240 (millimeters part), 88 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TreadHeight.Value </term> <description> 
##  
## 50 (millimeters part), 1.5 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class StairwayEquipmentBuilder(NXOpen.Builder): 
    """   """


    ## Getter for property: (bool) AddLeftRailingToggle
    ##  Returns the left railing toggle   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AddLeftRailingToggle(self) -> bool:
        """
        Getter for property: (bool) AddLeftRailingToggle
         Returns the left railing toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddLeftRailingToggle

    ##  Returns the left railing toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AddLeftRailingToggle.setter
    def AddLeftRailingToggle(self, addLeftRailingToggle: bool):
        """
        Setter for property: (bool) AddLeftRailingToggle
         Returns the left railing toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) AddRightRailingToggle
    ##  Returns the right railing toggle   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AddRightRailingToggle(self) -> bool:
        """
        Getter for property: (bool) AddRightRailingToggle
         Returns the right railing toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddRightRailingToggle

    ##  Returns the right railing toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AddRightRailingToggle.setter
    def AddRightRailingToggle(self, addRightRailingToggle: bool):
        """
        Setter for property: (bool) AddRightRailingToggle
         Returns the right railing toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) AddRiserToggle
    ##  Returns the riser toggle   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AddRiserToggle(self) -> bool:
        """
        Getter for property: (bool) AddRiserToggle
         Returns the riser toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddRiserToggle

    ##  Returns the riser toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AddRiserToggle.setter
    def AddRiserToggle(self, addRiserToggle: bool):
        """
        Setter for property: (bool) AddRiserToggle
         Returns the riser toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) AddStringerToggle
    ##  Returns the stringer toggle   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def AddStringerToggle(self) -> bool:
        """
        Getter for property: (bool) AddStringerToggle
         Returns the stringer toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddStringerToggle

    ##  Returns the stringer toggle   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AddStringerToggle.setter
    def AddStringerToggle(self, addStringerToggle: bool):
        """
        Setter for property: (bool) AddStringerToggle
         Returns the stringer toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndElevation
    ##  Returns the end elevation of stairway  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndElevation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndElevation
         Returns the end elevation of stairway  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
    ##  Returns the kf object is return  
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.KFObject
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: (@link NXOpen.KFObject NXOpen.KFObject@endlink) KfObject
         Returns the kf object is return  
            
         
        """
        pass
    
    ## Getter for property: (int) NoOfStairs
    ##  Returns the number of stairs   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def NoOfStairs(self) -> int:
        """
        Getter for property: (int) NoOfStairs
         Returns the number of stairs   
            
         
        """
        pass
    
    ## Setter for property: (int) NoOfStairs

    ##  Returns the number of stairs   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NoOfStairs.setter
    def NoOfStairs(self, noOfStairs: int):
        """
        Setter for property: (int) NoOfStairs
         Returns the number of stairs   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Rise
    ##  Returns the vertical distance between two steps   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Rise(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Rise
         Returns the vertical distance between two steps   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Run
    ##  Returns the run   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Run(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Run
         Returns the run   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StairNosing
    ##  Returns the stair nosing   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StairNosing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StairNosing
         Returns the stair nosing   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StairWidth
    ##  Returns the stair width   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StairWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StairWidth
         Returns the stair width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartElevation
    ##  Returns the start elevation of stairway   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartElevation(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartElevation
         Returns the start elevation of stairway   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StringerHeight
    ##  Returns the stringer height   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StringerHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StringerHeight
         Returns the stringer height   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StringerWidth
    ##  Returns the stringer width   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StringerWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StringerWidth
         Returns the stringer width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TotalRise
    ##  Returns the total rise   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TotalRise(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TotalRise
         Returns the total rise   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TotalRun
    ##  Returns the total run   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TotalRun(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TotalRun
         Returns the total run   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TreadHeight
    ##  Returns the tread height   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TreadHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TreadHeight
         Returns the tread height   
            
         
        """
        pass
    
##  Represents a typed connector feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::TypedConnectorFeatureBuilder  NXOpen::LineDesigner::TypedConnectorFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class TailConnectorFeature(TypedConnectorFeature): 
    """ Represents a typed connector feature feature """
    pass


import NXOpen
import NXOpen.Features
## 
##     Represents a @link LineDesigner::TypedConnectorFeature LineDesigner::TypedConnectorFeature@endlink  Features.FeatureBuilder
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateTypedConnectorFeatureBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateTypedConnectorFeatureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MismatchBehavior </term> <description> 
##  
## Dontcreatetheconnection </description> </item> 
## 
## <item><term> 
##  
## ReversePropagation </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class TypedConnectorFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>LineDesigner.TypedConnectorFeature</ja_class> Features.FeatureBuilder
    """


    ##  This enum is providing possible behavior on mismatch in propagated expressions 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Dontcreatetheconnection</term><description> 
    ## </description> </item><item><term> 
    ## Continuewithoutpropagatingtheparticularone</term><description> 
    ## </description> </item></list>
    class BehaviorOnMismatch(Enum):
        """
        Members Include: <Dontcreatetheconnection> <Continuewithoutpropagatingtheparticularone>
        """
        Dontcreatetheconnection: int
        Continuewithoutpropagatingtheparticularone: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TypedConnectorFeatureBuilder.BehaviorOnMismatch:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) ConnectorColor
    ##  Returns the connector color   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return int
    @property
    def ConnectorColor(self) -> int:
        """
        Getter for property: (int) ConnectorColor
         Returns the connector color   
            
         
        """
        pass
    
    ## Setter for property: (int) ConnectorColor

    ##  Returns the connector color   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConnectorColor.setter
    def ConnectorColor(self, connectorColor: int):
        """
        Setter for property: (int) ConnectorColor
         Returns the connector color   
            
         
        """
        pass
    
    ## Getter for property: (str) ConnectorCompatibleTypeName
    ##  Returns the connector compatible type name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ConnectorCompatibleTypeName(self) -> str:
        """
        Getter for property: (str) ConnectorCompatibleTypeName
         Returns the connector compatible type name   
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectorCompatibleTypeName

    ##  Returns the connector compatible type name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ConnectorCompatibleTypeName.setter
    def ConnectorCompatibleTypeName(self, connectorCompatibleTypeName: str):
        """
        Setter for property: (str) ConnectorCompatibleTypeName
         Returns the connector compatible type name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorDirection
    ##  Returns the connector direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ConnectorDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorDirection
         Returns the connector direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorDirection

    ##  Returns the connector direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConnectorDirection.setter
    def ConnectorDirection(self, connectorDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorDirection
         Returns the connector direction   
            
         
        """
        pass
    
    ## Getter for property: (str) ConnectorName
    ##  Returns the connector name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def ConnectorName(self) -> str:
        """
        Getter for property: (str) ConnectorName
         Returns the connector name   
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectorName

    ##  Returns the connector name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConnectorName.setter
    def ConnectorName(self, connectorName: str):
        """
        Setter for property: (str) ConnectorName
         Returns the connector name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorParallelToObjectDirection
    ##  Returns the connector parallel to object direction   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ConnectorParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorParallelToObjectDirection
         Returns the connector parallel to object direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorParallelToObjectDirection

    ##  Returns the connector parallel to object direction   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConnectorParallelToObjectDirection.setter
    def ConnectorParallelToObjectDirection(self, connectorParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ConnectorParallelToObjectDirection
         Returns the connector parallel to object direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ConnectorPoint
    ##  Returns the connector point   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def ConnectorPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ConnectorPoint
         Returns the connector point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ConnectorPoint

    ##  Returns the connector point   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConnectorPoint.setter
    def ConnectorPoint(self, connectorPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ConnectorPoint
         Returns the connector point   
            
         
        """
        pass
    
    ## Getter for property: (str) ConnectorTypeName
    ##  Returns the connector type name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ConnectorTypeName(self) -> str:
        """
        Getter for property: (str) ConnectorTypeName
         Returns the connector type name   
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectorTypeName

    ##  Returns the connector type name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ConnectorTypeName.setter
    def ConnectorTypeName(self, connectorTypeName: str):
        """
        Setter for property: (str) ConnectorTypeName
         Returns the connector type name   
            
         
        """
        pass
    
    ## Getter for property: (bool) DefaultConnector
    ##  Returns the status of if reverse propagation is on   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def DefaultConnector(self) -> bool:
        """
        Getter for property: (bool) DefaultConnector
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    
    ## Setter for property: (bool) DefaultConnector

    ##  Returns the status of if reverse propagation is on   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DefaultConnector.setter
    def DefaultConnector(self, defaultConnector: bool):
        """
        Setter for property: (bool) DefaultConnector
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    
    ## Getter for property: (@link TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.LineDesigner.TypedConnectorFeatureBuilder.BehaviorOnMismatch@endlink) MismatchBehavior
    ##  Returns the status of behavior on mismatch property   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TypedConnectorFeatureBuilder.BehaviorOnMismatch
    @property
    def MismatchBehavior(self) -> TypedConnectorFeatureBuilder.BehaviorOnMismatch:
        """
        Getter for property: (@link TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.LineDesigner.TypedConnectorFeatureBuilder.BehaviorOnMismatch@endlink) MismatchBehavior
         Returns the status of behavior on mismatch property   
            
         
        """
        pass
    
    ## Setter for property: (@link TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.LineDesigner.TypedConnectorFeatureBuilder.BehaviorOnMismatch@endlink) MismatchBehavior

    ##  Returns the status of behavior on mismatch property   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MismatchBehavior.setter
    def MismatchBehavior(self, mismatchBehavior: TypedConnectorFeatureBuilder.BehaviorOnMismatch):
        """
        Setter for property: (@link TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.LineDesigner.TypedConnectorFeatureBuilder.BehaviorOnMismatch@endlink) MismatchBehavior
         Returns the status of behavior on mismatch property   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReversePropagation
    ##  Returns the status of if reverse propagation is on   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ReversePropagation(self) -> bool:
        """
        Getter for property: (bool) ReversePropagation
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReversePropagation

    ##  Returns the status of if reverse propagation is on   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ReversePropagation.setter
    def ReversePropagation(self, reversePropagation: bool):
        """
        Setter for property: (bool) ReversePropagation
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    
    ## Getter for property: (str) TypedConnectorName
    ##  Returns the typed connector name   
    ##     
    ##  
    ## Getter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return str
    @property
    def TypedConnectorName(self) -> str:
        """
        Getter for property: (str) TypedConnectorName
         Returns the typed connector name   
            
         
        """
        pass
    
    ## Setter for property: (str) TypedConnectorName

    ##  Returns the typed connector name   
    ##     
    ##  
    ## Setter License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    @TypedConnectorName.setter
    def TypedConnectorName(self, typedConnectorName: str):
        """
        Setter for property: (str) TypedConnectorName
         Returns the typed connector name   
            
         
        """
        pass
    
    ##   The compatible connector types are returns 
    ##  @return connectorCompatibleTypeList (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetConnectorCompatibleTypeList(self) -> List[str]:
        """
          The compatible connector types are returns 
         @return connectorCompatibleTypeList (List[str]): .
        """
        pass
    
    ##  The connectors propagated expressions 
    ##  @return connectorExpressionPropagationList (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetConnectorExpressionPropagationList(self) -> List[NXOpen.Expression]:
        """
         The connectors propagated expressions 
         @return connectorExpressionPropagationList (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  The propagated expressions is set during creation of connector 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def SelectPropagatedExpressions(self) -> None:
        """
         The propagated expressions is set during creation of connector 
        """
        pass
    
    ##  The connector compatible types are set 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="connectorCompatibleTypeList"> (List[str])  </param>
    def SetConnectorCompatibleTypeList(self, connectorCompatibleTypeList: List[str]) -> None:
        """
         The connector compatible types are set 
        """
        pass
    
    ## The connectors propagated expressions are set 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="connectorExpressionPropagationList"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def SetConnectorExpressionPropagationList(self, connectorExpressionPropagationList: List[NXOpen.Expression]) -> None:
        """
        The connectors propagated expressions are set 
        """
        pass
    
    ##  The Nth expressions from connectors propagated expressions are set
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## 
    ## <param name="nthExpressionPropagationList"> (int) </param>
    ## <param name="connectorExpressionPropagationList"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    def SetNthConnectorExpressionPropagationList(self, nthExpressionPropagationList: int, connectorExpressionPropagationList: NXOpen.Expression) -> None:
        """
         The Nth expressions from connectors propagated expressions are set
        """
        pass
    
import NXOpen.Features
##  Represents a typed connector feature feature  <br> To create or edit an instance of this class, use @link NXOpen::LineDesigner::TypedConnectorFeatureBuilder  NXOpen::LineDesigner::TypedConnectorFeatureBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class TypedConnectorFeature(NXOpen.Features.Feature): 
    """ Represents a typed connector feature feature """
    pass


import NXOpen
import NXOpen.Assemblies
import NXOpen.PDM
##  Represents a utils of line designer for journaling uinode methods  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class UINodeUtils(NXOpen.Object): 
    """ Represents a utils of line designer for journaling uinode methods """


    ##  To control execution of BVR Model callbacks 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER") OR alp_planner ("Assembly Line Planner")
    ## <param name="ignore"> (bool)  If true, BVR Model callbacks are ignored to execute</param>
    def BVRModelIgnoreCallbacks(ignore: bool) -> None:
        """
         To control execution of BVR Model callbacks 
        """
        pass
    
    ##  To calculate and set attribute group name 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="attributeGroup"> (@link NXOpen.PDM.AttributeGroup NXOpen.PDM.AttributeGroup@endlink)  </param>
    ## <param name="subAGName"> (str) </param>
    ## <param name="resourceName"> (str) </param>
    def CalculateAndSetNameOfAGAttr(attributeGroup: NXOpen.PDM.AttributeGroup, subAGName: str, resourceName: str) -> None:
        """
         To calculate and set attribute group name 
        """
        pass
    
    ##  Set column occurrence type For Edit In Cell 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="sourcePartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="targetPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def DeleteConnectionInfoNode(sourcePartOcc: NXOpen.NXObject, targetPartOcc: NXOpen.NXObject) -> None:
        """
         Set column occurrence type For Edit In Cell 
        """
        pass
    
    ##  To delete constraint 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="constraintTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def DeleteConstraint(constraintTag: NXOpen.NXObject) -> None:
        """
         To delete constraint 
        """
        pass
    
    ##  To Delete DragAndDrop Undo Mark
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="undoMarkName"> (str) </param>
    def DeleteDragAndDropUndoMark(undoMarkName: str) -> None:
        """
         To Delete DragAndDrop Undo Mark
        """
        pass
    
    ##  To display Assembly PMI Through Shaded Model 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def DisplayPMIThroughShadedModel() -> None:
        """
         To display Assembly PMI Through Shaded Model 
        """
        pass
    
    ##  To DragAndDrop Station
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="stationProcessTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def DragAndDropStation(stationProcessTag: NXOpen.NXObject) -> None:
        """
         To DragAndDrop Station
        """
        pass
    
    ##  To Expand/Collaps End Item
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="selectedEndItem"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def ExpandCollapsEndItem(selectedEndItem: List[NXOpen.NXObject]) -> None:
        """
         To Expand/Collaps End Item
        """
        pass
    
    ##  To get item revision name 
    ##  @return itemRevName (str): .
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partTag"> (@link NXOpen.Part NXOpen.Part@endlink)  </param>
    def GetItemRevisionName(partTag: NXOpen.Part) -> str:
        """
         To get item revision name 
         @return itemRevName (str): .
        """
        pass
    
    ##  To get occurence name 
    ##  @return occurrenceName (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="instanceTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def GetOccurrenceName(instanceTag: NXOpen.NXObject) -> str:
        """
         To get occurence name 
         @return occurrenceName (str): .
        """
        pass
    
    ##  To partially load the children with LD connectors 
    ##  @return found (bool): .
    ## 
    ##   <br>  Created in NX2306.7000.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="owningPartOccurrence"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def LoadChildrenParts(owningPartOccurrence: NXOpen.NXObject) -> bool:
        """
         To partially load the children with LD connectors 
         @return found (bool): .
        """
        pass
    
    ##  To move connectors while DnD of assembly 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partOccTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="targ"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="value"> (float) </param>
    ## <param name="isNotBondConstraint"> (bool) </param>
    ## <param name="isPropogationAllowed"> (bool) </param>
    def MoveConnectors(partOccTag: NXOpen.NXObject, targ: NXOpen.NXObject, value: float, isNotBondConstraint: bool, isPropogationAllowed: bool) -> None:
        """
         To move connectors while DnD of assembly 
        """
        pass
    
    ##  Move Tool to original position 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="mountBuilder"> (@link MountBuilder NXOpen.LineDesigner.MountBuilder@endlink) </param>
    ## <param name="toolBaseConnectorTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def MoveToolToOriginalPosition(mountBuilder: MountBuilder, toolBaseConnectorTag: NXOpen.NXObject) -> None:
        """
         Move Tool to original position 
        """
        pass
    
    ##  Move Tool to Robot and orient as per connector 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="mountBuilder"> (@link MountBuilder NXOpen.LineDesigner.MountBuilder@endlink) </param>
    def MoveToolToRobotAndOrientAsPerConnector(mountBuilder: MountBuilder) -> None:
        """
         Move Tool to Robot and orient as per connector 
        """
        pass
    
    ##  To rename partition 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="objtg"> (@link ModelProductionUnit NXOpen.LineDesigner.ModelProductionUnit@endlink)  </param>
    ## <param name="newName"> (str) </param>
    def Rename(objtg: ModelProductionUnit, newName: str) -> None:
        """
         To rename partition 
        """
        pass
    
    ##  To rename partition in new PLNAV 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="objtg"> (@link NXOpen.Assemblies.Partition NXOpen.Assemblies.Partition@endlink)  </param>
    ## <param name="newName"> (str) </param>
    def RenamePartition(objtg: NXOpen.Assemblies.Partition, newName: str) -> None:
        """
         To rename partition in new PLNAV 
        """
        pass
    
    ##  To resize the Connectors per the Zoom Level 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="connectors"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="connectorSize"> (float) </param>
    def ResizeConnectors(connectors: List[NXOpen.NXObject], connectorSize: float) -> None:
        """
         To resize the Connectors per the Zoom Level 
        """
        pass
    
    ##  Retreive final tool transformation parameters 
    ##  @return A tuple consisting of (finalTransformedToolConnectorPointAfterMoveAndMount, finalTransformedToolConnectorXDirAfterMoveAndMount, finalTransformedToolConnectorYDirAfterMoveAndMount). 
    ##  - finalTransformedToolConnectorPointAfterMoveAndMount is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - finalTransformedToolConnectorXDirAfterMoveAndMount is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.
    ##  - finalTransformedToolConnectorYDirAfterMoveAndMount is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.

    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="builderTag"> (@link MountBuilder NXOpen.LineDesigner.MountBuilder@endlink) </param>
    def RetreiveFinalTransformedToolConnectorDetailsAfterMoveAndMount(builderTag: MountBuilder) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, NXOpen.Vector3d]:
        """
         Retreive final tool transformation parameters 
         @return A tuple consisting of (finalTransformedToolConnectorPointAfterMoveAndMount, finalTransformedToolConnectorXDirAfterMoveAndMount, finalTransformedToolConnectorYDirAfterMoveAndMount). 
         - finalTransformedToolConnectorPointAfterMoveAndMount is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - finalTransformedToolConnectorXDirAfterMoveAndMount is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.
         - finalTransformedToolConnectorYDirAfterMoveAndMount is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.

        """
        pass
    
    ##  To rotate a given component in clockwise or anticlockwise direction by 90 degrees 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partOccTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="isClockwise"> (bool) </param>
    ## <param name="rotateAsGroup"> (bool) </param>
    ## <param name="angleStep"> (float) </param>
    def RotateComponent(partOccTags: List[NXOpen.NXObject], isClockwise: bool, rotateAsGroup: bool, angleStep: float) -> None:
        """
         To rotate a given component in clockwise or anticlockwise direction by 90 degrees 
        """
        pass
    
    ##  Save final tool transformation parameters 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="builderTag"> (@link MountBuilder NXOpen.LineDesigner.MountBuilder@endlink) </param>
    ## <param name="finalTransformedToolConnectorPointAfterMoveAndMount"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="finalTransformedToolConnectorXDirAfterMoveAndMount"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="finalTransformedToolConnectorYDirAfterMoveAndMount"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def SaveFinalTransformedToolConnectorDetailsAfterMoveAndMount(builderTag: MountBuilder, finalTransformedToolConnectorPointAfterMoveAndMount: NXOpen.Point3d, finalTransformedToolConnectorXDirAfterMoveAndMount: NXOpen.Vector3d, finalTransformedToolConnectorYDirAfterMoveAndMount: NXOpen.Vector3d) -> None:
        """
         Save final tool transformation parameters 
        """
        pass
    
    ##  Set column occurrence type For Edit In Cell 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="newPropertyValu"> (str) </param>
    def SetColumnOccurrenceType(partOcc: NXOpen.NXObject, newPropertyValu: str) -> None:
        """
         Set column occurrence type For Edit In Cell 
        """
        pass
    
    ##  To set item revision name 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="partTag"> (@link NXOpen.Part NXOpen.Part@endlink)  </param>
    ## <param name="itemRevName"> (str) </param>
    def SetItemRevisionName(partTag: NXOpen.Part, itemRevName: str) -> None:
        """
         To set item revision name 
        """
        pass
    
    ##  To set occurence name 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="instanceTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    ## <param name="occurrenceName"> (str) </param>
    def SetOccurrenceName(instanceTag: NXOpen.NXObject, occurrenceName: str) -> None:
        """
         To set occurence name 
        """
        pass
    
    ##  Set Target Production Unit 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    ## <param name="constraintTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  </param>
    def SetProductionUnitAsWorkPart(constraintTag: NXOpen.NXObject) -> None:
        """
         Set Target Production Unit 
        """
        pass
    
    ##  To enable assembly PMI 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def ShowAssemblyPMI() -> None:
        """
         To enable assembly PMI 
        """
        pass
    
import NXOpen
## 
##     UnmountBuilder Class: Used when unmounting a tool from robot.
##      <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateUnmountBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateUnmountBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class UnmountBuilder(NXOpen.Builder): 
    """
    UnmountBuilder Class: Used when unmounting a tool from robot.
    """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectUnmountEntity
    ##  Returns the select unmount entity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectUnmountEntity(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectUnmountEntity
         Returns the select unmount entity   
            
         
        """
        pass
    
    ##  The set selected unmount entity
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedUnmountEntityTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetSelectedUnmountEntity(self, selectedUnmountEntityTag: NXOpen.TaggedObject) -> None:
        """
         The set selected unmount entity
        """
        pass
    
## @package NXOpen.LineDesigner
## Classes, Enums and Structs under NXOpen.LineDesigner namespace

##  @link AddTypeAttributeBuilderMappedType NXOpen.LineDesigner.AddTypeAttributeBuilderMappedType @endlink is an alias for @link AddTypeAttributeBuilder.MappedType NXOpen.LineDesigner.AddTypeAttributeBuilder.MappedType@endlink
AddTypeAttributeBuilderMappedType = AddTypeAttributeBuilder.MappedType


##  @link AlignComponentsBuilderReferenceValues NXOpen.LineDesigner.AlignComponentsBuilderReferenceValues @endlink is an alias for @link AlignComponentsBuilder.ReferenceValues NXOpen.LineDesigner.AlignComponentsBuilder.ReferenceValues@endlink
AlignComponentsBuilderReferenceValues = AlignComponentsBuilder.ReferenceValues


##  @link AlignComponentsBuilderSelectDirectionOptionEnum NXOpen.LineDesigner.AlignComponentsBuilderSelectDirectionOptionEnum @endlink is an alias for @link AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.LineDesigner.AlignComponentsBuilder.SelectDirectionOptionEnum@endlink
AlignComponentsBuilderSelectDirectionOptionEnum = AlignComponentsBuilder.SelectDirectionOptionEnum


##  @link ColumnFeatureBuilderColumnBaseType NXOpen.LineDesigner.ColumnFeatureBuilderColumnBaseType @endlink is an alias for @link ColumnFeatureBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnBaseType@endlink
ColumnFeatureBuilderColumnBaseType = ColumnFeatureBuilder.ColumnBaseType


##  @link ColumnFeatureBuilderColumnType NXOpen.LineDesigner.ColumnFeatureBuilderColumnType @endlink is an alias for @link ColumnFeatureBuilder.ColumnType NXOpen.LineDesigner.ColumnFeatureBuilder.ColumnType@endlink
ColumnFeatureBuilderColumnType = ColumnFeatureBuilder.ColumnType


##  @link ColumnGridEquipmentBuilderColumnBaseType NXOpen.LineDesigner.ColumnGridEquipmentBuilderColumnBaseType @endlink is an alias for @link ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnBaseType@endlink
ColumnGridEquipmentBuilderColumnBaseType = ColumnGridEquipmentBuilder.ColumnBaseType


##  @link ColumnGridEquipmentBuilderColumnType NXOpen.LineDesigner.ColumnGridEquipmentBuilderColumnType @endlink is an alias for @link ColumnGridEquipmentBuilder.ColumnType NXOpen.LineDesigner.ColumnGridEquipmentBuilder.ColumnType@endlink
ColumnGridEquipmentBuilderColumnType = ColumnGridEquipmentBuilder.ColumnType


##  @link ConnectionCreatorBuilderConnectionType NXOpen.LineDesigner.ConnectionCreatorBuilderConnectionType @endlink is an alias for @link ConnectionCreatorBuilder.ConnectionType NXOpen.LineDesigner.ConnectionCreatorBuilder.ConnectionType@endlink
ConnectionCreatorBuilderConnectionType = ConnectionCreatorBuilder.ConnectionType


##  @link ConveyorStationFeatureBuilderType NXOpen.LineDesigner.ConveyorStationFeatureBuilderType @endlink is an alias for @link ConveyorStationFeatureBuilder.Type NXOpen.LineDesigner.ConveyorStationFeatureBuilder.Type@endlink
ConveyorStationFeatureBuilderType = ConveyorStationFeatureBuilder.Type


##  @link CreateFactoryElementBuilderTypeAPI NXOpen.LineDesigner.CreateFactoryElementBuilderTypeAPI @endlink is an alias for @link CreateFactoryElementBuilder.TypeAPI NXOpen.LineDesigner.CreateFactoryElementBuilder.TypeAPI@endlink
CreateFactoryElementBuilderTypeAPI = CreateFactoryElementBuilder.TypeAPI


##  @link DBFactoryNodeNodeType NXOpen.LineDesigner.DBFactoryNodeNodeType @endlink is an alias for @link DBFactoryNode.NodeType NXOpen.LineDesigner.DBFactoryNode.NodeType@endlink
DBFactoryNodeNodeType = DBFactoryNode.NodeType


##  @link DefineToolBuilderToolType NXOpen.LineDesigner.DefineToolBuilderToolType @endlink is an alias for @link DefineToolBuilder.ToolType NXOpen.LineDesigner.DefineToolBuilder.ToolType@endlink
DefineToolBuilderToolType = DefineToolBuilder.ToolType


##  @link EnhancedShadowOutLineBuilderDrawingPlaneOptions NXOpen.LineDesigner.EnhancedShadowOutLineBuilderDrawingPlaneOptions @endlink is an alias for @link EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.DrawingPlaneOptions@endlink
EnhancedShadowOutLineBuilderDrawingPlaneOptions = EnhancedShadowOutLineBuilder.DrawingPlaneOptions


##  @link EnhancedShadowOutLineBuilderOutLineLevel NXOpen.LineDesigner.EnhancedShadowOutLineBuilderOutLineLevel @endlink is an alias for @link EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineLevel@endlink
EnhancedShadowOutLineBuilderOutLineLevel = EnhancedShadowOutLineBuilder.OutLineLevel


##  @link EnhancedShadowOutLineBuilderOutLineScope NXOpen.LineDesigner.EnhancedShadowOutLineBuilderOutLineScope @endlink is an alias for @link EnhancedShadowOutLineBuilder.OutLineScope NXOpen.LineDesigner.EnhancedShadowOutLineBuilder.OutLineScope@endlink
EnhancedShadowOutLineBuilderOutLineScope = EnhancedShadowOutLineBuilder.OutLineScope


##  @link ExportPlantToDWGBuilderSaveAsType NXOpen.LineDesigner.ExportPlantToDWGBuilderSaveAsType @endlink is an alias for @link ExportPlantToDWGBuilder.SaveAsType NXOpen.LineDesigner.ExportPlantToDWGBuilder.SaveAsType@endlink
ExportPlantToDWGBuilderSaveAsType = ExportPlantToDWGBuilder.SaveAsType


##  @link ExportToDWGBuilderSaveAsTypeAPI NXOpen.LineDesigner.ExportToDWGBuilderSaveAsTypeAPI @endlink is an alias for @link ExportToDWGBuilder.SaveAsTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.SaveAsTypeAPI@endlink
ExportToDWGBuilderSaveAsTypeAPI = ExportToDWGBuilder.SaveAsTypeAPI


##  @link ExportToDWGBuilderTemplateTypeAPI NXOpen.LineDesigner.ExportToDWGBuilderTemplateTypeAPI @endlink is an alias for @link ExportToDWGBuilder.TemplateTypeAPI NXOpen.LineDesigner.ExportToDWGBuilder.TemplateTypeAPI@endlink
ExportToDWGBuilderTemplateTypeAPI = ExportToDWGBuilder.TemplateTypeAPI


## @link FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct@endlink is an alias for @link FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData NXOpen.LineDesigner.FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData@endlink.
FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct = FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData


## @link FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct@endlink is an alias for @link FactoryCadGeoEquipmentBuilder.UpdatedControlData NXOpen.LineDesigner.FactoryCadGeoEquipmentBuilder.UpdatedControlData@endlink.
FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct = FactoryCadGeoEquipmentBuilder.UpdatedControlData


##  @link GateFeatureBuilderGateOpeningStyle NXOpen.LineDesigner.GateFeatureBuilderGateOpeningStyle @endlink is an alias for @link GateFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.GateFeatureBuilder.GateOpeningStyle@endlink
GateFeatureBuilderGateOpeningStyle = GateFeatureBuilder.GateOpeningStyle


##  @link InsertSheetBuilderAPIUnits NXOpen.LineDesigner.InsertSheetBuilderAPIUnits @endlink is an alias for @link InsertSheetBuilder.APIUnits NXOpen.LineDesigner.InsertSheetBuilder.APIUnits@endlink
InsertSheetBuilderAPIUnits = InsertSheetBuilder.APIUnits


##  @link LineDesignerUserCallBackManagerEventType NXOpen.LineDesigner.LineDesignerUserCallBackManagerEventType @endlink is an alias for @link LineDesignerUserCallBackManager.EventType NXOpen.LineDesigner.LineDesignerUserCallBackManager.EventType@endlink
LineDesignerUserCallBackManagerEventType = LineDesignerUserCallBackManager.EventType


##  @link MountBuilderFlipType NXOpen.LineDesigner.MountBuilderFlipType @endlink is an alias for @link MountBuilder.FlipType NXOpen.LineDesigner.MountBuilder.FlipType@endlink
MountBuilderFlipType = MountBuilder.FlipType


##  @link MountBuilderMountType NXOpen.LineDesigner.MountBuilderMountType @endlink is an alias for @link MountBuilder.MountType NXOpen.LineDesigner.MountBuilder.MountType@endlink
MountBuilderMountType = MountBuilder.MountType


##  @link PlatformEquipmentBuilderDeckingMaterialTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilderDeckingMaterialTypeAPI @endlink is an alias for @link PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckingMaterialTypeAPI@endlink
PlatformEquipmentBuilderDeckingMaterialTypeAPI = PlatformEquipmentBuilder.DeckingMaterialTypeAPI


##  @link PlatformEquipmentBuilderDeckSupportTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilderDeckSupportTypeAPI @endlink is an alias for @link PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.DeckSupportTypeAPI@endlink
PlatformEquipmentBuilderDeckSupportTypeAPI = PlatformEquipmentBuilder.DeckSupportTypeAPI


##  @link PlatformEquipmentBuilderOutlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilderOutlineTypeAPI @endlink is an alias for @link PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.OutlineTypeAPI@endlink
PlatformEquipmentBuilderOutlineTypeAPI = PlatformEquipmentBuilder.OutlineTypeAPI


##  @link PlatformEquipmentBuilderSideFromCenterlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilderSideFromCenterlineTypeAPI @endlink is an alias for @link PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.SideFromCenterlineTypeAPI@endlink
PlatformEquipmentBuilderSideFromCenterlineTypeAPI = PlatformEquipmentBuilder.SideFromCenterlineTypeAPI


##  @link PlatformEquipmentBuilderTypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilderTypeAPI @endlink is an alias for @link PlatformEquipmentBuilder.TypeAPI NXOpen.LineDesigner.PlatformEquipmentBuilder.TypeAPI@endlink
PlatformEquipmentBuilderTypeAPI = PlatformEquipmentBuilder.TypeAPI


##  @link RailingFeatureBuilderPostOffsetType NXOpen.LineDesigner.RailingFeatureBuilderPostOffsetType @endlink is an alias for @link RailingFeatureBuilder.PostOffsetType NXOpen.LineDesigner.RailingFeatureBuilder.PostOffsetType@endlink
RailingFeatureBuilderPostOffsetType = RailingFeatureBuilder.PostOffsetType


##  @link RailingFeatureBuilderRailCrossStyle NXOpen.LineDesigner.RailingFeatureBuilderRailCrossStyle @endlink is an alias for @link RailingFeatureBuilder.RailCrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.RailCrossStyle@endlink
RailingFeatureBuilderRailCrossStyle = RailingFeatureBuilder.RailCrossStyle


##  @link RailingFeatureBuilderSelPostcrossStyle NXOpen.LineDesigner.RailingFeatureBuilderSelPostcrossStyle @endlink is an alias for @link RailingFeatureBuilder.SelPostcrossStyle NXOpen.LineDesigner.RailingFeatureBuilder.SelPostcrossStyle@endlink
RailingFeatureBuilderSelPostcrossStyle = RailingFeatureBuilder.SelPostcrossStyle


##  @link RailingFeatureBuilderSpaceType NXOpen.LineDesigner.RailingFeatureBuilderSpaceType @endlink is an alias for @link RailingFeatureBuilder.SpaceType NXOpen.LineDesigner.RailingFeatureBuilder.SpaceType@endlink
RailingFeatureBuilderSpaceType = RailingFeatureBuilder.SpaceType


##  @link RailOpeningFeatureBuilderGateOpeningStyle NXOpen.LineDesigner.RailOpeningFeatureBuilderGateOpeningStyle @endlink is an alias for @link RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.LineDesigner.RailOpeningFeatureBuilder.GateOpeningStyle@endlink
RailOpeningFeatureBuilderGateOpeningStyle = RailOpeningFeatureBuilder.GateOpeningStyle


##  @link RenameDialogeBuilderSelectionTypeAPI NXOpen.LineDesigner.RenameDialogeBuilderSelectionTypeAPI @endlink is an alias for @link RenameDialogeBuilder.SelectionTypeAPI NXOpen.LineDesigner.RenameDialogeBuilder.SelectionTypeAPI@endlink
RenameDialogeBuilderSelectionTypeAPI = RenameDialogeBuilder.SelectionTypeAPI


##  @link SelectionToolBuilderRefSetOption NXOpen.LineDesigner.SelectionToolBuilderRefSetOption @endlink is an alias for @link SelectionToolBuilder.RefSetOption NXOpen.LineDesigner.SelectionToolBuilder.RefSetOption@endlink
SelectionToolBuilderRefSetOption = SelectionToolBuilder.RefSetOption


##  @link SelectionToolBuilderSelectionView NXOpen.LineDesigner.SelectionToolBuilderSelectionView @endlink is an alias for @link SelectionToolBuilder.SelectionView NXOpen.LineDesigner.SelectionToolBuilder.SelectionView@endlink
SelectionToolBuilderSelectionView = SelectionToolBuilder.SelectionView


##  @link TypedConnectorFeatureBuilderBehaviorOnMismatch NXOpen.LineDesigner.TypedConnectorFeatureBuilderBehaviorOnMismatch @endlink is an alias for @link TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.LineDesigner.TypedConnectorFeatureBuilder.BehaviorOnMismatch@endlink
TypedConnectorFeatureBuilderBehaviorOnMismatch = TypedConnectorFeatureBuilder.BehaviorOnMismatch


