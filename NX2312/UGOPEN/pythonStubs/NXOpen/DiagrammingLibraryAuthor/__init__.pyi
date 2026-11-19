from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Represents allowed attachment types for port. 
##  none. 
class AllowedAttachmentTypes(Enum):
    """
    Members Include: <NotSet> <ToConnection> <ToNode>
    """
    NotSet: int
    ToConnection: int
    ToNode: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AllowedAttachmentTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  Represents a @link NXOpen::DiagrammingLibraryAuthor::AttributeHolder NXOpen::DiagrammingLibraryAuthor::AttributeHolder@endlink .  
## 
##    <br> Use @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects@endlink  or @link NXOpen::DiagrammingLibraryAuthor::PipeStockBuilder::GetPipeStockObjects NXOpen::DiagrammingLibraryAuthor::PipeStockBuilder::GetPipeStockObjects@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class AttributeHolder(NXOpen.NXObject): 
    """ <summary> Represents a <ja_class>NXOpen.DiagrammingLibraryAuthor.AttributeHolder</ja_class>. </summary> """
    pass


import NXOpen
##   @brief Defines an object represent Equipment data. 
## 
##  
##       <br> Equipment data contains the equipment class name and the id of equipment instances. 
##      These information is used to retrieve equipment from library and link to or unlink from symbol. <br> 
##      <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateEquipmentData  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateEquipmentData @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class EquipmentData(NXOpen.TransientObject): 
    """ <summary>Defines an object represent Equipment data.</summary>
     <para>Equipment data contains the equipment class name and the id of equipment instances. 
     These information is used to retrieve equipment from library and link to or unlink from symbol.</para>
    """


    ##  Frees resources associated with the instance.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(equipmentData: EquipmentData) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
    
import NXOpen
##   @brief  Represents a LineTypeAuthoringBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateLineTypeAuthoringBuilder  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateLineTypeAuthoringBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.3000.0  <br> 

class LineTypeAuthoringBuilder(NXOpen.Builder): 
    """ <summary> Represents a LineTypeAuthoringBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (str) Discipline
    ##   the discipline of the object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    ## @return str
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
          the discipline of the object.  
             
         
        """
        pass
    
    ## Setter for property: (str) Discipline

    ##   the discipline of the object.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
          the discipline of the object.  
             
         
        """
        pass
    
    ## Getter for property: (@link LineTypeBuilderList NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList@endlink) LineTypes
    ##   the list of line types.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    ## @return LineTypeBuilderList
    @property
    def LineTypes(self) -> LineTypeBuilderList:
        """
        Getter for property: (@link LineTypeBuilderList NXOpen.DiagrammingLibraryAuthor.LineTypeBuilderList@endlink) LineTypes
          the list of line types.  
             
         
        """
        pass
    
    ## Getter for property: (str) OutputFolder
    ##   the output folder for generated files.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    ## @return str
    @property
    def OutputFolder(self) -> str:
        """
        Getter for property: (str) OutputFolder
          the output folder for generated files.  
             
         
        """
        pass
    
    ## Setter for property: (str) OutputFolder

    ##   the output folder for generated files.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    @OutputFolder.setter
    def OutputFolder(self, outputFolder: str):
        """
        Setter for property: (str) OutputFolder
          the output folder for generated files.  
             
         
        """
        pass
    
    ##  Creates a new line type 
    ##  @return lineType (@link LineTypeBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    ## License requirements: None.
    def CreateLineType(builder: LineTypeAuthoringBuilder) -> LineTypeBuilder:
        """
         Creates a new line type 
         @return lineType (@link LineTypeBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class LineTypeBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: LineTypeBuilderList, objects: List[LineTypeBuilder]) -> None:
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
    def Append(self, object_list: LineTypeBuilderList, objectValue: LineTypeBuilder) -> None:
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
    def Clear(object_list: LineTypeBuilderList) -> None:
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
    def ClearIndex(object_list: LineTypeBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: LineTypeBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: LineTypeBuilderList, index: int) -> None:
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
    def Erase(self, object_list: LineTypeBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: LineTypeBuilderList, obj: LineTypeBuilder) -> None:
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
    def Erase(self, object_list: LineTypeBuilderList, obj: LineTypeBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: LineTypeBuilderList, obj: LineTypeBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link LineTypeBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: LineTypeBuilderList, index: int) -> LineTypeBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link LineTypeBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link LineTypeBuilder List[NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: LineTypeBuilderList) -> List[LineTypeBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link LineTypeBuilder List[NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: LineTypeBuilderList, location: int, objectValue: LineTypeBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: LineTypeBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: LineTypeBuilderList, index: int) -> None:
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
    def SetContents(object_list: LineTypeBuilderList, objects: List[LineTypeBuilder]) -> None:
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
    def Swap(self, object_list: LineTypeBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: LineTypeBuilderList, object1: LineTypeBuilder, object2: LineTypeBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a LineTypeBuilder.  
## 
##   
## 
##   <br>  Created in NX11.0.1  <br> 

class LineTypeBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a LineTypeBuilder. </summary> """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor
    ##   the line color.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.NXColor
    @property
    def LineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor
          the line color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor

    ##   the line color.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineColor.setter
    def LineColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LineColor
          the line color.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
    ##   the line font.  
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
          the line font.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont

    ##   the line font.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) LineFont
          the line font.  
             
         
        """
        pass
    
    ## Getter for property: (str) LineTypeName
    ##   the name of the line type.  
    ##    It should be unique.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def LineTypeName(self) -> str:
        """
        Getter for property: (str) LineTypeName
          the name of the line type.  
           It should be unique.   
         
        """
        pass
    
    ## Setter for property: (str) LineTypeName

    ##   the name of the line type.  
    ##    It should be unique.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineTypeName.setter
    def LineTypeName(self, name: str):
        """
        Setter for property: (str) LineTypeName
          the name of the line type.  
           It should be unique.   
         
        """
        pass
    
    ## Getter for property: (int) LineTypePriority
    ##   the priority of the line type.  
    ##    It should be greater than or equal to 0.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return int
    @property
    def LineTypePriority(self) -> int:
        """
        Getter for property: (int) LineTypePriority
          the priority of the line type.  
           It should be greater than or equal to 0.   
         
        """
        pass
    
    ## Setter for property: (int) LineTypePriority

    ##   the priority of the line type.  
    ##    It should be greater than or equal to 0.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineTypePriority.setter
    def LineTypePriority(self, priority: int):
        """
        Setter for property: (int) LineTypePriority
          the priority of the line type.  
           It should be greater than or equal to 0.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
    ##   the line width.  
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
          the line width.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth

    ##   the line width.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
          the line width.  
             
         
        """
        pass
    
    ## Getter for property: (str) ObjectId
    ##   the object Id of the line type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return str
    @property
    def ObjectId(self) -> str:
        """
        Getter for property: (str) ObjectId
          the object Id of the line type.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a PipeStockBuilder.  
## 
##   
## 
##   <br>  Created in NX11.0.1  <br> 

class PipeStockBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a PipeStockBuilder. </summary> """


    ##  Creates a new pipe stock 
    ##  @return pipeStockObject (@link AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the pipe stock object .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="instanceId"> (str) </param>
    ## <param name="partId"> (str) </param>
    ## <param name="partName"> (str) </param>
    ## <param name="numberName"> (str) </param>
    def CreatePipeStock(builder: PipeStockBuilder, instanceId: str, partId: str, partName: str, numberName: str) -> AttributeHolder:
        """
         Creates a new pipe stock 
         @return pipeStockObject (@link AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the pipe stock object .
        """
        pass
    
    ##  Deletes the pipe stock which is new created 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  the pipe stock object,
    ##                 only accept the object which is got by @link NXOpen::DiagrammingLibraryAuthor::PipeStockBuilder::CreatePipeStock NXOpen::DiagrammingLibraryAuthor::PipeStockBuilder::CreatePipeStock@endlink  
    def DeletePipeStock(builder: PipeStockBuilder, pipeStockObject: AttributeHolder) -> None:
        """
         Deletes the pipe stock which is new created 
        """
        pass
    
    ##  Gets the pipe stock objects which have user attributes of the pipe stock. 
    ##  @return pipeStockObjects (@link AttributeHolder List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]@endlink):  the pipe stock objects .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPipeStockObjects(builder: PipeStockBuilder) -> List[AttributeHolder]:
        """
         Gets the pipe stock objects which have user attributes of the pipe stock. 
         @return pipeStockObjects (@link AttributeHolder List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]@endlink):  the pipe stock objects .
        """
        pass
    
    ##  Selects the pipe stock folder by the class ID 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="classId"> (str) </param>
    def SelectFolder(builder: PipeStockBuilder, classId: str) -> None:
        """
         Selects the pipe stock folder by the class ID 
        """
        pass
    
    ##  Selects one pipe stock by the symbol ID 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="symbolId"> (str) </param>
    def SelectPipeStock(builder: PipeStockBuilder, symbolId: str) -> None:
        """
         Selects one pipe stock by the symbol ID 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a PortDataBuilder.  
## 
##   
## 
##   <br>  Created in NX11.0.1  <br> 

class PortDataBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a PortDataBuilder. </summary> """


    ## Getter for property: (bool) NozzleBottom
    ##   the nozzle in the bottom edge.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def NozzleBottom(self) -> bool:
        """
        Getter for property: (bool) NozzleBottom
          the nozzle in the bottom edge.  
             
         
        """
        pass
    
    ## Setter for property: (bool) NozzleBottom

    ##   the nozzle in the bottom edge.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NozzleBottom.setter
    def NozzleBottom(self, nozzleBottom: bool):
        """
        Setter for property: (bool) NozzleBottom
          the nozzle in the bottom edge.  
             
         
        """
        pass
    
    ## Getter for property: (bool) NozzleLeft
    ##   the nozzle in the left edge.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def NozzleLeft(self) -> bool:
        """
        Getter for property: (bool) NozzleLeft
          the nozzle in the left edge.  
             
         
        """
        pass
    
    ## Setter for property: (bool) NozzleLeft

    ##   the nozzle in the left edge.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NozzleLeft.setter
    def NozzleLeft(self, nozzleLeft: bool):
        """
        Setter for property: (bool) NozzleLeft
          the nozzle in the left edge.  
             
         
        """
        pass
    
    ## Getter for property: (bool) NozzleRight
    ##   the nozzle in the right edge.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def NozzleRight(self) -> bool:
        """
        Getter for property: (bool) NozzleRight
          the nozzle in the right edge.  
             
         
        """
        pass
    
    ## Setter for property: (bool) NozzleRight

    ##   the nozzle in the right edge.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NozzleRight.setter
    def NozzleRight(self, nozzleRight: bool):
        """
        Setter for property: (bool) NozzleRight
          the nozzle in the right edge.  
             
         
        """
        pass
    
    ## Getter for property: (bool) NozzleTop
    ##   the nozzle in the top edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def NozzleTop(self) -> bool:
        """
        Getter for property: (bool) NozzleTop
          the nozzle in the top edge   
            
         
        """
        pass
    
    ## Setter for property: (bool) NozzleTop

    ##   the nozzle in the top edge   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @NozzleTop.setter
    def NozzleTop(self, nozzleTop: bool):
        """
        Setter for property: (bool) NozzleTop
          the nozzle in the top edge   
            
         
        """
        pass
    
    ##  Creates a new port 
    ##  @return portObject (@link AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the port object .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def CreatePort(builder: PortDataBuilder) -> AttributeHolder:
        """
         Creates a new port 
         @return portObject (@link AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the port object .
        """
        pass
    
    ##  Deletes the port which is new created 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  the port object,
    ##                 only accept the object which is got by @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort@endlink  
    def DeletePort(builder: PortDataBuilder, portObject: AttributeHolder) -> None:
        """
         Deletes the port which is new created 
        """
        pass
    
    ##  Gets the connection direction 
    ##  @return connectionDirection (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the connection direction .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  the port object,
    ##                 only accept the object which is got by @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects@endlink  or @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort@endlink  
    def GetConnectionDirection(builder: PortDataBuilder, portObject: AttributeHolder) -> NXOpen.Point2d:
        """
         Gets the connection direction 
         @return connectionDirection (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the connection direction .
        """
        pass
    
    ##  Gets the port location 
    ##  @return portLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the port location .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  the port object,
    ##                 only accept the object which is got by @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects@endlink  or @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort@endlink  
    def GetPointLocation(builder: PortDataBuilder, portObject: AttributeHolder) -> NXOpen.Point2d:
        """
         Gets the port location 
         @return portLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the port location .
        """
        pass
    
    ##  Gets the port objects which have user attributes of the port. 
    ##  @return portObjects (@link AttributeHolder List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]@endlink):  the port objects .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPortObjects(builder: PortDataBuilder) -> List[AttributeHolder]:
        """
         Gets the port objects which have user attributes of the port. 
         @return portObjects (@link AttributeHolder List[NXOpen.DiagrammingLibraryAuthor.AttributeHolder]@endlink):  the port objects .
        """
        pass
    
    ##  Sets the connection direction  
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  the port object,
    ##                 only accept the object which is got by @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects@endlink  or @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort@endlink  
    def SetConnectionDirection(builder: PortDataBuilder, portObject: AttributeHolder, connectionDirection: NXOpen.Point2d) -> None:
        """
         Sets the connection direction  
        """
        pass
    
    ##  Sets the port location 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ##  the port object,
    ##                 only accept the object which is by @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::GetPortObjects@endlink  or @link NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort NXOpen::DiagrammingLibraryAuthor::PortDataBuilder::CreatePort@endlink  
    def SetPointLocation(builder: PortDataBuilder, portObject: AttributeHolder, portLocation: NXOpen.Point2d) -> None:
        """
         Sets the port location 
        """
        pass
    
import NXOpen
import NXOpen.Gateway
import NXOpen.GeometricUtilities
import NXOpen.Tooling
##   @brief  Represents a Symbol2DBuilder.  
## 
##   
## 
##   <br>  Created in NX11.0.1  <br> 

class Symbol2DBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a Symbol2DBuilder. </summary> """


    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
    ##   the anchor point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Point2d
    @property
    def AnchorPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
          the anchor point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint

    ##   the anchor point   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
          the anchor point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Tooling.SelectReuseLibraryItemBuilder NXOpen.Tooling.SelectReuseLibraryItemBuilder@endlink) DraftingSymbol
    ##   the 2D symbol sub-builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Tooling.SelectReuseLibraryItemBuilder
    @property
    def DraftingSymbol(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: (@link NXOpen.Tooling.SelectReuseLibraryItemBuilder NXOpen.Tooling.SelectReuseLibraryItemBuilder@endlink) DraftingSymbol
          the 2D symbol sub-builder.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EnableScale
    ##   the scaling   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def EnableScale(self) -> bool:
        """
        Getter for property: (bool) EnableScale
          the scaling   
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableScale

    ##   the scaling   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @EnableScale.setter
    def EnableScale(self, enableScale: bool):
        """
        Setter for property: (bool) EnableScale
          the scaling   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) Image
    ##   the image capture builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Gateway.ImageCaptureBuilder
    @property
    def Image(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) Image
          the image capture builder   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) Image

    ##   the image capture builder   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Image.setter
    def Image(self, imageCaptureBuilder: NXOpen.Gateway.ImageCaptureBuilder):
        """
        Setter for property: (@link NXOpen.Gateway.ImageCaptureBuilder NXOpen.Gateway.ImageCaptureBuilder@endlink) Image
          the image capture builder   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsInline
    ##   the inline   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def IsInline(self) -> bool:
        """
        Getter for property: (bool) IsInline
          the inline   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsInline

    ##   the inline   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @IsInline.setter
    def IsInline(self, isInline: bool):
        """
        Setter for property: (bool) IsInline
          the inline   
            
         
        """
        pass
    
    ## Getter for property: (@link PortDataBuilder NXOpen.DiagrammingLibraryAuthor.PortDataBuilder@endlink) PortData
    ##   the port data sub-builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return PortDataBuilder
    @property
    def PortData(self) -> PortDataBuilder:
        """
        Getter for property: (@link PortDataBuilder NXOpen.DiagrammingLibraryAuthor.PortDataBuilder@endlink) PortData
          the port data sub-builder.  
             
         
        """
        pass
    
    ## Getter for property: (str) PrefixLetters
    ##   the prefix   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def PrefixLetters(self) -> str:
        """
        Getter for property: (str) PrefixLetters
          the prefix   
            
         
        """
        pass
    
    ## Setter for property: (str) PrefixLetters

    ##   the prefix   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @PrefixLetters.setter
    def PrefixLetters(self, prefixLetters: str):
        """
        Setter for property: (str) PrefixLetters
          the prefix   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
    ##   the tag location   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Point2d
    @property
    def TagLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
          the tag location   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation

    ##   the tag location   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @TagLocation.setter
    def TagLocation(self, tagLocation: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
          the tag location   
            
         
        """
        pass
    
    ##  Creates a new symbol from another symbol 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="symbolId"> (str) </param>
    def CreateFromSymbol(builder: Symbol2DBuilder, symbolId: str) -> None:
        """
         Creates a new symbol from another symbol 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a Symbol3DBuilder.  
## 
##   
## 
##   <br>  Created in NX11.0.1  <br> 

class Symbol3DBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a Symbol3DBuilder. </summary> """


    ## Getter for property: (@link NXOpen.ITableEditorDataProvider NXOpen.ITableEditorDataProvider@endlink) PortMappingData
    ##   the data provider of the port mapping table.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.ITableEditorDataProvider
    @property
    def PortMappingData(self) -> NXOpen.ITableEditorDataProvider:
        """
        Getter for property: (@link NXOpen.ITableEditorDataProvider NXOpen.ITableEditorDataProvider@endlink) PortMappingData
          the data provider of the port mapping table.  
             
         
        """
        pass
    
import NXOpen
##   @brief  Represents a SymbolBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolBuilder  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SymbolBuilder(NXOpen.Builder): 
    """ <summary> Represents a SymbolBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (int) ActiveVariantId
    ##   the active variant in symbol  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def ActiveVariantId(self) -> int:
        """
        Getter for property: (int) ActiveVariantId
          the active variant in symbol  
            
         
        """
        pass
    
    ## Setter for property: (int) ActiveVariantId

    ##   the active variant in symbol  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ActiveVariantId.setter
    def ActiveVariantId(self, variantId: int):
        """
        Setter for property: (int) ActiveVariantId
          the active variant in symbol  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
    ##   the anchor location point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::AnchorPoint NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::AnchorPoint@endlink  instead.  <br> 

    ## @return NXOpen.Point2d
    @property
    def AnchorPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
          the anchor location point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint

    ##   the anchor location point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::AnchorPoint NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::AnchorPoint@endlink  instead.  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
          the anchor location point  
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the symbol description  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the symbol description  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the symbol description  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the symbol description  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the symbol name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the symbol name  
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the symbol name  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the symbol name  
            
         
        """
        pass
    
    ## Getter for property: (str) Standard
    ##   the symbol standard  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    ## @return str
    @property
    def Standard(self) -> str:
        """
        Getter for property: (str) Standard
          the symbol standard  
            
         
        """
        pass
    
    ## Setter for property: (str) Standard

    ##   the symbol standard  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    @Standard.setter
    def Standard(self, standard: str):
        """
        Setter for property: (str) Standard
          the symbol standard  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
    ##   the tag location point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::TagLocation NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::TagLocation@endlink  instead.  <br> 

    ## @return NXOpen.Point2d
    @property
    def TagLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
          the tag location point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation

    ##   the tag location point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::TagLocation NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder::TagLocation@endlink  instead.  <br> 

    @TagLocation.setter
    def TagLocation(self, tagLocation: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
          the tag location point  
            
         
        """
        pass
    
    ## Getter for property: (str) TagPrefix
    ##   the tag prefix name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def TagPrefix(self) -> str:
        """
        Getter for property: (str) TagPrefix
          the tag prefix name  
            
         
        """
        pass
    
    ## Setter for property: (str) TagPrefix

    ##   the tag prefix name  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TagPrefix.setter
    def TagPrefix(self, tagPrefix: str):
        """
        Setter for property: (str) TagPrefix
          the tag prefix name  
            
         
        """
        pass
    
    ## Getter for property: (str) Unit
    ##   the symbol unit  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    ## @return str
    @property
    def Unit(self) -> str:
        """
        Getter for property: (str) Unit
          the symbol unit  
            
         
        """
        pass
    
    ## Setter for property: (str) Unit

    ##   the symbol unit  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    @Unit.setter
    def Unit(self, unit: str):
        """
        Setter for property: (str) Unit
          the symbol unit  
            
         
        """
        pass
    
    ##  Gets symbol port 
    ##  @return portObject (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="portId"> (str) </param>
    def GetSymbolPort(builder: SymbolBuilder, portId: str) -> NXOpen.NXObject:
        """
         Gets symbol port 
         @return portObject (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Gets symbol variant 
    ##  @return variantObject (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="variantId"> (int) </param>
    def GetSymbolVariant(builder: SymbolBuilder, variantId: int) -> NXOpen.NXObject:
        """
         Gets symbol variant 
         @return variantObject (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a SymbolConnectionPointBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL. 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SymbolConnectionPointBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a SymbolConnectionPointBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) ConnectionDirection
    ##   the connection direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def ConnectionDirection(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) ConnectionDirection
          the connection direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) ConnectionDirection

    ##   the connection direction   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ConnectionDirection.setter
    def ConnectionDirection(self, connectionDirection: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) ConnectionDirection
          the connection direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) Location
    ##   the port location point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def Location(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) Location
          the port location point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) Location

    ##   the port location point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Location.setter
    def Location(self, portLocation: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) Location
          the port location point  
            
         
        """
        pass
    
import NXOpen
##  Represents an object that manages Symbol Designer application specific interfaces.
##       <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SymbolDesignerManager(NXOpen.Object): 
    """ Represents an object that manages Symbol Designer application specific interfaces.
     """


    ##  Creates a @link DiagrammingLibraryAuthor::EquipmentData DiagrammingLibraryAuthor::EquipmentData@endlink . 
    ##  @return equipmentData (@link EquipmentData NXOpen.DiagrammingLibraryAuthor.EquipmentData@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  the identifiers of equipment 
    def CreateEquipmentData(equipmentClass: str, equipmentIds: List[str]) -> EquipmentData:
        """
         Creates a @link DiagrammingLibraryAuthor::EquipmentData DiagrammingLibraryAuthor::EquipmentData@endlink . 
         @return equipmentData (@link EquipmentData NXOpen.DiagrammingLibraryAuthor.EquipmentData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DiagrammingLibraryAuthor::LineTypeAuthoringBuilder NXOpen::DiagrammingLibraryAuthor::LineTypeAuthoringBuilder@endlink . 
    ##  @return builder (@link LineTypeAuthoringBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeAuthoringBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.3000.0  <br> 

    ## License requirements: None.
    ##  the part that will own the object 
    def CreateLineTypeAuthoringBuilder(part: NXOpen.Part) -> LineTypeAuthoringBuilder:
        """
         Creates a @link NXOpen::DiagrammingLibraryAuthor::LineTypeAuthoringBuilder NXOpen::DiagrammingLibraryAuthor::LineTypeAuthoringBuilder@endlink . 
         @return builder (@link LineTypeAuthoringBuilder NXOpen.DiagrammingLibraryAuthor.LineTypeAuthoringBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolBuilder NXOpen::DiagrammingLibraryAuthor::SymbolBuilder@endlink . 
    ##  @return builder (@link SymbolBuilder NXOpen.DiagrammingLibraryAuthor.SymbolBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  the part that will own the object 
    def CreateSymbolBuilder(part: NXOpen.Part) -> SymbolBuilder:
        """
         Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolBuilder NXOpen::DiagrammingLibraryAuthor::SymbolBuilder@endlink . 
         @return builder (@link SymbolBuilder NXOpen.DiagrammingLibraryAuthor.SymbolBuilder@endlink): .
        """
        pass
    
    ##  Create a symbol part. 
    ##  @return symbolPart (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="symbolName"> (str) </param>
    def CreateSymbolPart(symbolName: str) -> NXOpen.Part:
        """
         Create a symbol part. 
         @return symbolPart (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolPortBuilder NXOpen::DiagrammingLibraryAuthor::SymbolPortBuilder@endlink . 
    ##  @return builder (@link SymbolPortBuilder NXOpen.DiagrammingLibraryAuthor.SymbolPortBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  the part that will own the object 
    def CreateSymbolPortBuilder(part: NXOpen.Part, portID: str) -> SymbolPortBuilder:
        """
         Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolPortBuilder NXOpen::DiagrammingLibraryAuthor::SymbolPortBuilder@endlink . 
         @return builder (@link SymbolPortBuilder NXOpen.DiagrammingLibraryAuthor.SymbolPortBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolSaveBuilder NXOpen::DiagrammingLibraryAuthor::SymbolSaveBuilder@endlink . 
    ##  @return builder (@link SymbolSaveBuilder NXOpen.DiagrammingLibraryAuthor.SymbolSaveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  the part that will own the object 
    def CreateSymbolSaveBuilder(part: NXOpen.Part) -> SymbolSaveBuilder:
        """
         Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolSaveBuilder NXOpen::DiagrammingLibraryAuthor::SymbolSaveBuilder@endlink . 
         @return builder (@link SymbolSaveBuilder NXOpen.DiagrammingLibraryAuthor.SymbolSaveBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder@endlink . 
    ##  @return builder (@link SymbolVariantBuilder NXOpen.DiagrammingLibraryAuthor.SymbolVariantBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  the part that will own the object 
    def CreateSymbolVariantBuilder(part: NXOpen.Part, variantID: int) -> SymbolVariantBuilder:
        """
         Creates a @link NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder NXOpen::DiagrammingLibraryAuthor::SymbolVariantBuilder@endlink . 
         @return builder (@link SymbolVariantBuilder NXOpen.DiagrammingLibraryAuthor.SymbolVariantBuilder@endlink): .
        """
        pass
    
    ##  Links equipment to the symbol part. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  the symbol part 
    def LinkEquipment(part: NXOpen.Part, equipmentData: EquipmentData) -> None:
        """
         Links equipment to the symbol part. 
        """
        pass
    
    ##  Open symbol in Symbol Designer environment. 
    ##  @return symbolPart (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="partSpec"> (str) </param>
    @staticmethod
    def OpenSymbolPart(partSpec: str) -> NXOpen.Part:
        """
         Open symbol in Symbol Designer environment. 
         @return symbolPart (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Unlink all equipment from the symbol part. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  the symbol part 
    @staticmethod
    def UnlinkAllEquipment(part: NXOpen.Part) -> None:
        """
         Unlink all equipment from the symbol part. 
        """
        pass
    
    ##  Unlink equipment from the symbol part. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  the symbol part 
    def UnlinkEquipment(part: NXOpen.Part, equipmentData: EquipmentData) -> None:
        """
         Unlink equipment from the symbol part. 
        """
        pass
    
import NXOpen
##   @brief  Represents a SymbolPortBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolPortBuilder  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolPortBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SymbolPortBuilder(NXOpen.Builder): 
    """ <summary> Represents a SymbolPortBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (@link SymbolConnectionPointBuilder NXOpen.DiagrammingLibraryAuthor.SymbolConnectionPointBuilder@endlink) ConnectionPoint
    ##   the symbol connection point sub-builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SymbolConnectionPointBuilder
    @property
    def ConnectionPoint(self) -> SymbolConnectionPointBuilder:
        """
        Getter for property: (@link SymbolConnectionPointBuilder NXOpen.DiagrammingLibraryAuthor.SymbolConnectionPointBuilder@endlink) ConnectionPoint
          the symbol connection point sub-builder.  
             
         
        """
        pass
    
    ##  Get allowed attachment types. 
    ##  @return types (@link AllowedAttachmentTypes NXOpen.DiagrammingLibraryAuthor.AllowedAttachmentTypes@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAllowedAttachmentTypes(builder: SymbolPortBuilder) -> AllowedAttachmentTypes:
        """
         Get allowed attachment types. 
         @return types (@link AllowedAttachmentTypes NXOpen.DiagrammingLibraryAuthor.AllowedAttachmentTypes@endlink): .
        """
        pass
    
    ##  Get port direction
    ##  @return portDirection (str):  the port direction .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDirection(builder: SymbolPortBuilder) -> str:
        """
         Get port direction
         @return portDirection (str):  the port direction .
        """
        pass
    
    ##  Get port id
    ##  @return portID (str):  the port id .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPortID(builder: SymbolPortBuilder) -> str:
        """
         Get port id
         @return portID (str):  the port id .
        """
        pass
    
    ##  Gets the port objects which have user attributes of the port. 
    ##  @return portObject (@link AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the port objects .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPortObject(builder: SymbolPortBuilder) -> AttributeHolder:
        """
         Gets the port objects which have user attributes of the port. 
         @return portObject (@link AttributeHolder NXOpen.DiagrammingLibraryAuthor.AttributeHolder@endlink):  the port objects .
        """
        pass
    
    ##  Set allowed attachment types. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="types"> (@link AllowedAttachmentTypes NXOpen.DiagrammingLibraryAuthor.AllowedAttachmentTypes@endlink) </param>
    def SetAllowedAttachmentTypes(builder: SymbolPortBuilder, types: AllowedAttachmentTypes) -> None:
        """
         Set allowed attachment types. 
        """
        pass
    
    ##  Set port direction 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  the port direction 
    def SetDirection(builder: SymbolPortBuilder, portDirection: str) -> None:
        """
         Set port direction 
        """
        pass
    
    ##  Set port id 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  the port id 
    def SetPortID(builder: SymbolPortBuilder, portID: str) -> None:
        """
         Set port id 
        """
        pass
    
import NXOpen
##   @brief  Represents a SymbolSaveBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolSaveBuilder  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolSaveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SymbolSaveBuilder(NXOpen.Builder): 
    """ <summary> Represents a SymbolSaveBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (str) FileName
    ##   the symbol file name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the symbol file name   
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the symbol file name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the symbol file name   
            
         
        """
        pass
    
    ## Getter for property: (str) FolderPath
    ##   the folder path to save symbol   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
          the folder path to save symbol   
            
         
        """
        pass
    
    ## Setter for property: (str) FolderPath

    ##   the folder path to save symbol   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @FolderPath.setter
    def FolderPath(self, path: str):
        """
        Setter for property: (str) FolderPath
          the folder path to save symbol   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the symbol name   
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
          the symbol name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the symbol name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Name.setter
    def Name(self, symbolName: str):
        """
        Setter for property: (str) Name
          the symbol name   
            
         
        """
        pass
    
    ## Getter for property: (bool) SaveAsMode
    ##   the flag that indicates if save-as mode is used.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SaveAsMode(self) -> bool:
        """
        Getter for property: (bool) SaveAsMode
          the flag that indicates if save-as mode is used.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SaveAsMode

    ##   the flag that indicates if save-as mode is used.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SaveAsMode.setter
    def SaveAsMode(self, isSaveAs: bool):
        """
        Setter for property: (bool) SaveAsMode
          the flag that indicates if save-as mode is used.  
             
         
        """
        pass
    
    ##  Gets the symbol description 
    ##  @return text (List[str]): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDescription(builder: SymbolSaveBuilder) -> List[str]:
        """
         Gets the symbol description 
         @return text (List[str]): .
        """
        pass
    
    ##  Sets the symbol description 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDescription(builder: SymbolSaveBuilder, text: List[str]) -> None:
        """
         Sets the symbol description 
        """
        pass
    
import NXOpen
##   @brief  Represents a SymbolVariantBuilder.  
## 
##   
##         Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolVariantBuilder  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolVariantBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SymbolVariantBuilder(NXOpen.Builder): 
    """ <summary> Represents a SymbolVariantBuilder. </summary> 
        Calling <ja_method>Builder.Commit</ja_method> on this builder will only return <ja_NULL>. """


    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
    ##   the anchor location point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def AnchorPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
          the anchor location point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint

    ##   the anchor location point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) AnchorPoint
          the anchor location point  
            
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the variant description  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the variant description  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the variant description  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the variant description  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
    ##   the tag location point  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def TagLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
          the tag location point  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation

    ##   the tag location point  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TagLocation.setter
    def TagLocation(self, tagLocation: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) TagLocation
          the tag location point  
            
         
        """
        pass
    
    ## Getter for property: (str) VariantName
    ##   the variant name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def VariantName(self) -> str:
        """
        Getter for property: (str) VariantName
          the variant name  
            
         
        """
        pass
    
    ## Setter for property: (str) VariantName

    ##   the variant name  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @VariantName.setter
    def VariantName(self, variantName: str):
        """
        Setter for property: (str) VariantName
          the variant name  
            
         
        """
        pass
    
    ##  Set preview image 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ##  the preview image file 
    def SetPreviewImage(builder: SymbolVariantBuilder, imageFile: str) -> None:
        """
         Set preview image 
        """
        pass
    
## @package NXOpen.DiagrammingLibraryAuthor
## Classes, Enums and Structs under NXOpen.DiagrammingLibraryAuthor namespace

