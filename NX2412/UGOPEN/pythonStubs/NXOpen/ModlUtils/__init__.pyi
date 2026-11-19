from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.GeometricUtilities
class EquationEditorBuilder(NXOpen.TaggedObject): 
    """ Represents a ModlUtils.EquationEditorBuilder builder """
    @property
    def EquationString(self) -> str:
        """
        Getter for property: (str) EquationString
         Returns the equation string   
            
         
        """
        pass
    @EquationString.setter
    def EquationString(self, userExpression: str):
        """
        Setter for property: (str) EquationString
         Returns the equation string   
            
         
        """
        pass
import NXOpen
class ImportTemplatePartBuilder(NXOpen.Builder): 
    """ Represents a ModlUtils.ImportTemplatePart builder """
    @property
    def TemplatePartFileSpec(self) -> str:
        """
        Getter for property: (str) TemplatePartFileSpec
         Returns the template part file spec   
            
         
        """
        pass
    @TemplatePartFileSpec.setter
    def TemplatePartFileSpec(self, templatePartFileSpec: str):
        """
        Setter for property: (str) TemplatePartFileSpec
         Returns the template part file spec   
            
         
        """
        pass
import NXOpen
class ImportTemplatePart(NXOpen.TaggedObject): 
    """ Represents a ModlUtils.ImportTemplatePart builder """
    pass
import NXOpen
class SelectObjectDimListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
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
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class SelectObjectDimListItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SelectObjectDimListItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SelectObjectDimListItem) -> None:
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
    def Erase(self, obj: SelectObjectDimListItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SelectObjectDimListItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SelectObjectDimListItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SelectObjectDimListItem:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SelectObjectDimListItem NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SelectObjectDimListItem]:
        """
         Gets the contents of the entire list 
         Returns objects ( SelectObjectDimListItem List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SelectObjectDimListItem) -> None:
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
    def SetContents(self, objects: List[SelectObjectDimListItem]) -> None:
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
    def Swap(self, object1: SelectObjectDimListItem, object2: SelectObjectDimListItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class SelectObjectDimListItem(NXOpen.Builder): 
    """ Represents a local specification of select object and dimension block """
    @property
    def Dimension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Dimension
         Returns the dimension for the given item in the list  
            
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Selection
         Returns the select object list which contains faces or points or curves   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectObjectDimList(NXOpen.TaggedObject): 
    """ the builder for a list of ModlUtils.SelectObjectDimListItem objects """
    @property
    def List(self) -> SelectObjectDimListItemList:
        """
        Getter for property: ( SelectObjectDimListItemList NXOpen.) List
         Returns a list of  ModlUtils::SelectObjectDimListItem  objects   
            
         
        """
        pass
    def CreateSelectObjectDimListItem(self) -> SelectObjectDimListItem:
        """
         Creates a ModlUtils.SelectObjectDimListItem 
         Returns builder ( SelectObjectDimListItem NXOpen.): .
        """
        pass
