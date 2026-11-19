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
    ##  Returns the equation string   
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
         Returns the equation string   
            
         
        """
        pass
    
    ## Setter for property: (str) EquationString

    ##  Returns the equation string   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EquationString.setter
    def EquationString(self, userExpression: str):
        """
        Setter for property: (str) EquationString
         Returns the equation string   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link ModlUtils::ImportTemplatePart ModlUtils::ImportTemplatePart@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Part::CreateImportTemplatePartBuilder  NXOpen::Part::CreateImportTemplatePartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ImportTemplatePartBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>ModlUtils.ImportTemplatePart</ja_class> builder """


    ## Getter for property: (str) TemplatePartFileSpec
    ##  Returns the template part file spec   
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
         Returns the template part file spec   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplatePartFileSpec

    ##  Returns the template part file spec   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TemplatePartFileSpec.setter
    def TemplatePartFileSpec(self, templatePartFileSpec: str):
        """
        Setter for property: (str) TemplatePartFileSpec
         Returns the template part file spec   
            
         
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
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectObjectDimListItemBuilderList NXOpen.ModlUtils.SelectObjectDimListItemBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemBuilderList NXOpen.ModlUtils.SelectObjectDimListItemBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemBuilderList NXOpen.ModlUtils.SelectObjectDimListItemBuilderList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemBuilderList NXOpen.ModlUtils.SelectObjectDimListItemBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
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
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    def Swap(self, index1: int, index2: int) -> None:
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
    ## <param name="objects"> (@link SelectObjectDimListItem List[NXOpen.ModlUtils.SelectObjectDimListItem]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[SelectObjectDimListItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
    ## <param name="objectValue"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: SelectObjectDimListItem) -> None:
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
    ## <param name="obj"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: SelectObjectDimListItem) -> None:
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
    ## <param name="obj"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: SelectObjectDimListItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    ## <param name="obj"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  Object to find index for </param>
    def FindIndex(self, obj: SelectObjectDimListItem) -> int:
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
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> SelectObjectDimListItem:
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
    def GetContents(self) -> List[SelectObjectDimListItem]:
        """
         Gets the contents of the entire list 
         @return objects (@link SelectObjectDimListItem List[NXOpen.ModlUtils.SelectObjectDimListItem]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: SelectObjectDimListItem) -> None:
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
    ## <param name="objects"> (@link SelectObjectDimListItem List[NXOpen.ModlUtils.SelectObjectDimListItem]@endlink)  The list contents </param>
    def SetContents(self, objects: List[SelectObjectDimListItem]) -> None:
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
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
    ## <param name="object_list"> (@link SelectObjectDimListItemList NXOpen.ModlUtils.SelectObjectDimListItemList@endlink) </param>
    ## <param name="object1"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  first item </param>
    ## <param name="object2"> (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink)  second item </param>
    @overload
    def Swap(self, object1: SelectObjectDimListItem, object2: SelectObjectDimListItem) -> None:
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
    ##  Returns the dimension for the given item in the list  
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
         Returns the dimension for the given item in the list  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Selection
    ##  Returns the select object list which contains faces or points or curves   
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
         Returns the select object list which contains faces or points or curves   
            
         
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
    ##  Returns a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects   
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
         Returns a list of @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  objects   
            
         
        """
        pass
    
    ##  Creates a @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  
    ##  @return builder (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def CreateSelectObjectDimListItem(self) -> SelectObjectDimListItem:
        """
         Creates a @link ModlUtils::SelectObjectDimListItem ModlUtils::SelectObjectDimListItem@endlink  
         @return builder (@link SelectObjectDimListItem NXOpen.ModlUtils.SelectObjectDimListItem@endlink): .
        """
        pass
    
## @package NXOpen.ModlUtils
## Classes, Enums and Structs under NXOpen.ModlUtils namespace

