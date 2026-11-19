from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link ModlUtils::EquationEditorBuilder ModlUtils::EquationEditorBuilder@endlink  builder 
## 
##   <br>  Created in NX1953.0.0  <br> 

class EquationEditorBuilder(NXOpen.TaggedObject): 
    """ Represents a <ja_class>ModlUtils.EquationEditorBuilder</ja_class> builder """


    ## Getter for property: (str) EquationString
    ##   the equation string   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def EquationString(self) -> str:
        """
        Getter for property: (str) EquationString
          the equation string   
            
         
        """
        pass
    
    ## Setter for property: (str) EquationString

    ##   the equation string   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EquationString.setter
    def EquationString(self, userExpression: str):
        """
        Setter for property: (str) EquationString
          the equation string   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link ModlUtils::ImportTemplatePart ModlUtils::ImportTemplatePart@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Part::CreateImportTemplatePartBuilder  NXOpen::Part::CreateImportTemplatePartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ImportTemplatePartBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>ModlUtils.ImportTemplatePart</ja_class> builder """


    ## Getter for property: (str) TemplatePartFileSpec
    ##   the template part file spec   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def TemplatePartFileSpec(self) -> str:
        """
        Getter for property: (str) TemplatePartFileSpec
          the template part file spec   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplatePartFileSpec

    ##   the template part file spec   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TemplatePartFileSpec.setter
    def TemplatePartFileSpec(self, templatePartFileSpec: str):
        """
        Setter for property: (str) TemplatePartFileSpec
          the template part file spec   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link ModlUtils::ImportTemplatePart ModlUtils::ImportTemplatePart@endlink  builder  <br> To create or edit an instance of this class, use @link NXOpen::ModlUtils::ImportTemplatePartBuilder  NXOpen::ModlUtils::ImportTemplatePartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ImportTemplatePart(NXOpen.TaggedObject): 
    """ Represents a <ja_class>ModlUtils.ImportTemplatePart</ja_class> builder """
    pass


import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class SelectObjectDimListItemBuilderList(NXOpen.TaggedObject): 
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
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Clear(object_list: SelectObjectDimListItemBuilderList) -> None:
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
    def ClearIndex(object_list: SelectObjectDimListItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: SelectObjectDimListItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: SelectObjectDimListItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: SelectObjectDimListItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: SelectObjectDimListItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: SelectObjectDimListItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location of the first item 
    def Swap(object_list: SelectObjectDimListItemBuilderList, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class SelectObjectDimListItemList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: SelectObjectDimListItemList, objects: List[SelectObjectDimListItem]) -> None:
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
    def Append(self, object_list: SelectObjectDimListItemList, objectValue: SelectObjectDimListItem) -> None:
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
    def Clear(object_list: SelectObjectDimListItemList) -> None:
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
    def ClearIndex(object_list: SelectObjectDimListItemList, delete_idx: int) -> None:
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
    def Clear(object_list: SelectObjectDimListItemList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: SelectObjectDimListItemList, index: int) -> None:
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
    def Erase(self, object_list: SelectObjectDimListItemList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: SelectObjectDimListItemList, obj: SelectObjectDimListItem) -> None:
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
    def Erase(self, object_list: SelectObjectDimListItemList, obj: SelectObjectDimListItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: SelectObjectDimListItemList, obj: SelectObjectDimListItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: SelectObjectDimListItemList, index: int) -> SelectObjectDimListItem:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link SelectObjectDimListItem List[NXOpen.ModlUtils.SelectObjectDimListItem]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: SelectObjectDimListItemList) -> List[SelectObjectDimListItem]:
        """
         Gets the contents of the entire list 
         @return objects (@link SelectObjectDimListItem List[NXOpen.ModlUtils.SelectObjectDimListItem]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: SelectObjectDimListItemList, location: int, objectValue: SelectObjectDimListItem) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: SelectObjectDimListItemList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: SelectObjectDimListItemList, index: int) -> None:
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
    def SetContents(object_list: SelectObjectDimListItemList, objects: List[SelectObjectDimListItem]) -> None:
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
    def Swap(self, object_list: SelectObjectDimListItemList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: SelectObjectDimListItemList, object1: SelectObjectDimListItem, object2: SelectObjectDimListItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  Represents a local specification of select object and dimension block  <br> To create a new instance of this class, use @link NXOpen::ModlUtils::SelectObjectDimList::CreateSelectObjectDimListItem  NXOpen::ModlUtils::SelectObjectDimList::CreateSelectObjectDimListItem @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SelectObjectDimListItem(NXOpen.Builder): 
    """ Represents a local specification of select object and dimension block """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Dimension
    ##   the dimension for the given item in the list  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Dimension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Dimension
          the dimension for the given item in the list  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Selection
    ##   the select object list which contains faces or points or curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Selection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Selection
          the select object list which contains faces or points or curves   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  the builder for a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects 
## 
##   <br>  Created in NX2007.0.0  <br> 

class SelectObjectDimList(NXOpen.TaggedObject): 
    """ the builder for a list of <ja_class>ModlUtils.SelectObjectDimListItem</ja_class> objects """


    ## Getter for property: (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) List
    ##   a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return SelectObjectDimListItemList
    @property
    def List(self) -> SelectObjectDimListItemList:
        """
        Getter for property: (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) List
          a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects   
            
         
        """
        pass
    
    ##  Creates a @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  
    ##  @return builder (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def CreateSelectObjectDimListItem(dataManager: SelectObjectDimList) -> SelectObjectDimListItem:
        """
         Creates a @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  
         @return builder (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink): .
        """
        pass
    
## @package NXOpen.ModlUtils
## Classes, Enums and Structs under NXOpen.ModlUtils namespace

