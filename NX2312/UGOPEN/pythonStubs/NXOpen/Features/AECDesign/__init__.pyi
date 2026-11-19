from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Tooling
## 
##         Represents a @link Features::AECDesign::AddReusablePartBuilder Features::AECDesign::AddReusablePartBuilder@endlink 
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateBimAddreusepartBuilder  NXOpen::Features::AECDesignCollection::CreateBimAddreusepartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class AddReusablePartBuilder(NXOpen.Tooling.AddReusablePart): 
    """
        Represents a <ja_class>Features.AECDesign.AddReusablePartBuilder</ja_class>
        """


    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
    ##   the level reference  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
          the level reference  
            
         
        """
        pass
    
    ##  Rotates part by the given angle.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="rotationAngle"> (float) </param>
    ## <param name="instance"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="index"> (int) </param>
    def RotatePart(builder: AddReusablePartBuilder, rotationAngle: float, instance: NXOpen.NXObject, index: int) -> None:
        """
         Rotates part by the given angle.
        """
        pass
    
    ##  Sets reusable part attribute.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def SetPartAttribute(builder: AddReusablePartBuilder) -> None:
        """
         Sets reusable part attribute.
        """
        pass
    
import NXOpen
##   @brief 
##         Represents an AlternateCoverThickness builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create AlternateCoverThickness Data in AEC Design.
##         
##      <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AlternateCoverThicknessBuilder(NXOpen.Builder): 
    """ <summary>
        Represents an AlternateCoverThickness builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create AlternateCoverThickness Data in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link AlternateCoverThicknessListItemBuilderList NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilderList@endlink) AlternateCoverThicknessList
    ##   the alternate cover thickness list   
    ##     
    ##  
    ## Getter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return AlternateCoverThicknessListItemBuilderList
    @property
    def AlternateCoverThicknessList(self) -> AlternateCoverThicknessListItemBuilderList:
        """
        Getter for property: (@link AlternateCoverThicknessListItemBuilderList NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilderList@endlink) AlternateCoverThicknessList
          the alternate cover thickness list   
            
         
        """
        pass
    
    ##  The alternate cover thickness item creation function
    ##  @return alternateCoverThicknessListItemBuilder (@link AlternateCoverThicknessListItemBuilder NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_concrete ("Concrete Design")
    def CreateAlternateCoverThicknessListItemBuilder(builder: AlternateCoverThicknessBuilder) -> AlternateCoverThicknessListItemBuilder:
        """
         The alternate cover thickness item creation function
         @return alternateCoverThicknessListItemBuilder (@link AlternateCoverThicknessListItemBuilder NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class AlternateCoverThicknessListItemBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: AlternateCoverThicknessListItemBuilderList, objects: List[AlternateCoverThicknessListItemBuilder]) -> None:
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
    def Append(self, object_list: AlternateCoverThicknessListItemBuilderList, objectValue: AlternateCoverThicknessListItemBuilder) -> None:
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
    def Clear(object_list: AlternateCoverThicknessListItemBuilderList) -> None:
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
    def ClearIndex(object_list: AlternateCoverThicknessListItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: AlternateCoverThicknessListItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: AlternateCoverThicknessListItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: AlternateCoverThicknessListItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: AlternateCoverThicknessListItemBuilderList, obj: AlternateCoverThicknessListItemBuilder) -> None:
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
    def Erase(self, object_list: AlternateCoverThicknessListItemBuilderList, obj: AlternateCoverThicknessListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: AlternateCoverThicknessListItemBuilderList, obj: AlternateCoverThicknessListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link AlternateCoverThicknessListItemBuilder NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: AlternateCoverThicknessListItemBuilderList, index: int) -> AlternateCoverThicknessListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link AlternateCoverThicknessListItemBuilder NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link AlternateCoverThicknessListItemBuilder List[NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: AlternateCoverThicknessListItemBuilderList) -> List[AlternateCoverThicknessListItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link AlternateCoverThicknessListItemBuilder List[NXOpen.Features.AECDesign.AlternateCoverThicknessListItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: AlternateCoverThicknessListItemBuilderList, location: int, objectValue: AlternateCoverThicknessListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: AlternateCoverThicknessListItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: AlternateCoverThicknessListItemBuilderList, index: int) -> None:
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
    def SetContents(object_list: AlternateCoverThicknessListItemBuilderList, objects: List[AlternateCoverThicknessListItemBuilder]) -> None:
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
    def Swap(self, object_list: AlternateCoverThicknessListItemBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: AlternateCoverThicknessListItemBuilderList, object1: AlternateCoverThicknessListItemBuilder, object2: AlternateCoverThicknessListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  Alternate Cover Thickness list item builder  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::AlternateCoverThicknessBuilder::CreateAlternateCoverThicknessListItemBuilder  NXOpen::Features::AECDesign::AlternateCoverThicknessBuilder::CreateAlternateCoverThicknessListItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AlternateCoverThicknessListItemBuilder(NXOpen.TaggedObject): 
    """ Alternate Cover Thickness list item builder """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AlternateCoverThicknessDim
    ##   the alternate cover thickness dim   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AlternateCoverThicknessDim(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AlternateCoverThicknessDim
          the alternate cover thickness dim   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) AlternateCoverThicknessFace
    ##   the alternate cover thickness face  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def AlternateCoverThicknessFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) AlternateCoverThicknessFace
          the alternate cover thickness face  
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class BaseDetailItemBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: BaseDetailItemBuilderList, objects: List[BaseDetailItemBuilder]) -> None:
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
    def Append(self, object_list: BaseDetailItemBuilderList, objectValue: BaseDetailItemBuilder) -> None:
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
    def Clear(object_list: BaseDetailItemBuilderList) -> None:
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
    def ClearIndex(object_list: BaseDetailItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: BaseDetailItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: BaseDetailItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: BaseDetailItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: BaseDetailItemBuilderList, obj: BaseDetailItemBuilder) -> None:
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
    def Erase(self, object_list: BaseDetailItemBuilderList, obj: BaseDetailItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: BaseDetailItemBuilderList, obj: BaseDetailItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link BaseDetailItemBuilder NXOpen.Features.AECDesign.BaseDetailItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: BaseDetailItemBuilderList, index: int) -> BaseDetailItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link BaseDetailItemBuilder NXOpen.Features.AECDesign.BaseDetailItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link BaseDetailItemBuilder List[NXOpen.Features.AECDesign.BaseDetailItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: BaseDetailItemBuilderList) -> List[BaseDetailItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link BaseDetailItemBuilder List[NXOpen.Features.AECDesign.BaseDetailItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: BaseDetailItemBuilderList, location: int, objectValue: BaseDetailItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: BaseDetailItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: BaseDetailItemBuilderList, index: int) -> None:
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
    def SetContents(object_list: BaseDetailItemBuilderList, objects: List[BaseDetailItemBuilder]) -> None:
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
    def Swap(self, object_list: BaseDetailItemBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: BaseDetailItemBuilderList, object1: BaseDetailItemBuilder, object2: BaseDetailItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
## 
##         Represents a BaseDetailItemBuilder.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class BaseDetailItemBuilder(NXOpen.Builder): 
    """
        Represents a BaseDetailItemBuilder.
        """


    ## Getter for property: (str) MaterialLibName
    ##   the material library Name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def MaterialLibName(self) -> str:
        """
        Getter for property: (str) MaterialLibName
          the material library Name   
            
         
        """
        pass
    
    ## Setter for property: (str) MaterialLibName

    ##   the material library Name   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MaterialLibName.setter
    def MaterialLibName(self, materialLibName: str):
        """
        Setter for property: (str) MaterialLibName
          the material library Name   
            
         
        """
        pass
    
    ## Getter for property: (str) MaterialName
    ##   the material enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
          the material enum   
            
         
        """
        pass
    
    ## Setter for property: (str) MaterialName

    ##   the material enum   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
          the material enum   
            
         
        """
        pass
    
    ## Getter for property: (@link MaterialVisualItemBuilder NXOpen.Features.AECDesign.MaterialVisualItemBuilder@endlink) MaterialVisual
    ##   the material visual  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return MaterialVisualItemBuilder
    @property
    def MaterialVisual(self) -> MaterialVisualItemBuilder:
        """
        Getter for property: (@link MaterialVisualItemBuilder NXOpen.Features.AECDesign.MaterialVisualItemBuilder@endlink) MaterialVisual
          the material visual  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (str) ProcessNote
    ##   the process note   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ProcessNote(self) -> str:
        """
        Getter for property: (str) ProcessNote
          the process note   
            
         
        """
        pass
    
    ## Setter for property: (str) ProcessNote

    ##   the process note   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ProcessNote.setter
    def ProcessNote(self, processNote: str):
        """
        Setter for property: (str) ProcessNote
          the process note   
            
         
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class BaseLibraryItemBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: BaseLibraryItemBuilderList, objects: List[BaseLibraryItemBuilder]) -> None:
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
    def Append(self, object_list: BaseLibraryItemBuilderList, objectValue: BaseLibraryItemBuilder) -> None:
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
    def Clear(object_list: BaseLibraryItemBuilderList) -> None:
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
    def ClearIndex(object_list: BaseLibraryItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: BaseLibraryItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: BaseLibraryItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: BaseLibraryItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: BaseLibraryItemBuilderList, obj: BaseLibraryItemBuilder) -> None:
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
    def Erase(self, object_list: BaseLibraryItemBuilderList, obj: BaseLibraryItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: BaseLibraryItemBuilderList, obj: BaseLibraryItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link BaseLibraryItemBuilder NXOpen.Features.AECDesign.BaseLibraryItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: BaseLibraryItemBuilderList, index: int) -> BaseLibraryItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link BaseLibraryItemBuilder NXOpen.Features.AECDesign.BaseLibraryItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link BaseLibraryItemBuilder List[NXOpen.Features.AECDesign.BaseLibraryItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: BaseLibraryItemBuilderList) -> List[BaseLibraryItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link BaseLibraryItemBuilder List[NXOpen.Features.AECDesign.BaseLibraryItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: BaseLibraryItemBuilderList, location: int, objectValue: BaseLibraryItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: BaseLibraryItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: BaseLibraryItemBuilderList, index: int) -> None:
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
    def SetContents(object_list: BaseLibraryItemBuilderList, objects: List[BaseLibraryItemBuilder]) -> None:
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
    def Swap(self, object_list: BaseLibraryItemBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: BaseLibraryItemBuilderList, object1: BaseLibraryItemBuilder, object2: BaseLibraryItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  The builder to define base library detail  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class BaseLibraryItemBuilder(NXOpen.Builder): 
    """ The builder to define base library detail """


    ## Getter for property: (str) Category
    ##   the category   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##   the category   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseDetailItemBuilderList NXOpen.Features.AECDesign.BaseDetailItemBuilderList@endlink) DetailItemList
    ##   the list of @link NXOpen::Features::AECDesign::BaseDetailItemBuilder NXOpen::Features::AECDesign::BaseDetailItemBuilder@endlink  defining the base library item parameters.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BaseDetailItemBuilderList
    @property
    def DetailItemList(self) -> BaseDetailItemBuilderList:
        """
        Getter for property: (@link BaseDetailItemBuilderList NXOpen.Features.AECDesign.BaseDetailItemBuilderList@endlink) DetailItemList
          the list of @link NXOpen::Features::AECDesign::BaseDetailItemBuilder NXOpen::Features::AECDesign::BaseDetailItemBuilder@endlink  defining the base library item parameters.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsDefault
    ##   the flag to indicate whether it is the default item.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def IsDefault(self) -> bool:
        """
        Getter for property: (bool) IsDefault
          the flag to indicate whether it is the default item.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsDefault

    ##   the flag to indicate whether it is the default item.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @IsDefault.setter
    def IsDefault(self, isDefault: bool):
        """
        Setter for property: (bool) IsDefault
          the flag to indicate whether it is the default item.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a @link Features::AECDesign::Beam Features::AECDesign::Beam@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateBeamBuilder  NXOpen::Features::AECDesignCollection::CreateBeamBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BuildingElementTrim.BooleanSetting </term> <description> 
##  
## Trim </description> </item> 
## 
## <item><term> 
##  
## YOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ZOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class BeamBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>Features.AECDesign.Beam</ja_class> builder
    """


    ## The y-axis alignment types
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LeftAligned</term><description> 
    ## </description> </item><item><term> 
    ## RightAligned</term><description> 
    ## </description> </item><item><term> 
    ## CenterlineAligned</term><description> 
    ## </description> </item></list>
    class HorizontalAlignmentTypes(Enum):
        """
        Members Include: <LeftAligned> <RightAligned> <CenterlineAligned>
        """
        LeftAligned: int
        RightAligned: int
        CenterlineAligned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BeamBuilder.HorizontalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## The z-axis alignment types
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TopAligned</term><description> 
    ## </description> </item><item><term> 
    ## BottomAligned</term><description> 
    ## </description> </item><item><term> 
    ## CenterlineAligned</term><description> 
    ## </description> </item></list>
    class VerticalAlignmentTypes(Enum):
        """
        Members Include: <TopAligned> <BottomAligned> <CenterlineAligned>
        """
        TopAligned: int
        BottomAligned: int
        CenterlineAligned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BeamBuilder.VerticalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link BuildingElementTrimBuilder NXOpen.Features.AECDesign.BuildingElementTrimBuilder@endlink) BuildingElementTrim
    ##   the building element trim   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return BuildingElementTrimBuilder
    @property
    def BuildingElementTrim(self) -> BuildingElementTrimBuilder:
        """
        Getter for property: (@link BuildingElementTrimBuilder NXOpen.Features.AECDesign.BuildingElementTrimBuilder@endlink) BuildingElementTrim
          the building element trim   
            
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
    ##   the level reference  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
          the level reference  
            
         
        """
        pass
    
    ## Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
    ##   the material section  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return MaterialSectionBuilder
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
          the material section  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PathGeometry
    ##   the path geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def PathGeometry(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PathGeometry
          the path geometry   
            
         
        """
        pass
    
    ## Getter for property: (@link BeamBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.HorizontalAlignmentTypes@endlink) YAlignmentType
    ##   the y offset alignment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return BeamBuilder.HorizontalAlignmentTypes
    @property
    def YAlignmentType(self) -> BeamBuilder.HorizontalAlignmentTypes:
        """
        Getter for property: (@link BeamBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.HorizontalAlignmentTypes@endlink) YAlignmentType
          the y offset alignment  
            
         
        """
        pass
    
    ## Setter for property: (@link BeamBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.HorizontalAlignmentTypes@endlink) YAlignmentType

    ##   the y offset alignment  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @YAlignmentType.setter
    def YAlignmentType(self, yAlignmentType: BeamBuilder.HorizontalAlignmentTypes):
        """
        Setter for property: (@link BeamBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.HorizontalAlignmentTypes@endlink) YAlignmentType
          the y offset alignment  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##   the y offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
          the y offset   
            
         
        """
        pass
    
    ## Getter for property: (@link BeamBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.VerticalAlignmentTypes@endlink) ZAlignmentType
    ##   the z offset alignment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return BeamBuilder.VerticalAlignmentTypes
    @property
    def ZAlignmentType(self) -> BeamBuilder.VerticalAlignmentTypes:
        """
        Getter for property: (@link BeamBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.VerticalAlignmentTypes@endlink) ZAlignmentType
          the z offset alignment   
            
         
        """
        pass
    
    ## Setter for property: (@link BeamBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.VerticalAlignmentTypes@endlink) ZAlignmentType

    ##   the z offset alignment   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ZAlignmentType.setter
    def ZAlignmentType(self, zAlignmentType: BeamBuilder.VerticalAlignmentTypes):
        """
        Setter for property: (@link BeamBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.VerticalAlignmentTypes@endlink) ZAlignmentType
          the z offset alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZOffset
    ##   the z offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZOffset
          the z offset   
            
         
        """
        pass
    
    ##  Update Ref Columns
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateReferencedColumns(builder: BeamBuilder) -> None:
        """
         Update Ref Columns
        """
        pass
    
import NXOpen.Features
##  Represents a beam feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::BeamBuilder  NXOpen::Features::AECDesign::BeamBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Beam(NXOpen.Features.BodyFeature): 
    """ Represents a beam feature """
    pass


import NXOpen
##   @brief 
##     Represents a classify component builder for AEC.
##      
## 
##  
##     
##     This builder is used to classify component in AEC. 
##     
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateBimclassificationBuilder  NXOpen::Features::AECDesignCollection::CreateBimclassificationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## PropertiesRequisiteType </term> <description> 
##  
## All </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class BIMClassificationBuilder(NXOpen.Builder): 
    """ <summary>
    Represents a classify component builder for AEC.
    </summary>
    <remarks>
    This builder is used to classify component in AEC. 
    </remarks>
    """


    ## Specify display property type
    ## Lists all available properties            
    class RequisiteTypes(Enum):
        """
        Members Include: <All> <Mandatory> <Optional> <UserDefined>
        """
        All: int
        Mandatory: int
        Optional: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BIMClassificationBuilder.RequisiteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) BoolValue
    ##  the bool value of currently accessing property.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BoolValue(self) -> bool:
        """
        Getter for property: (bool) BoolValue
         the bool value of currently accessing property.  
             
         
        """
        pass
    
    ## Setter for property: (bool) BoolValue

    ##  the bool value of currently accessing property.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BoolValue.setter
    def BoolValue(self, boolValue: bool):
        """
        Setter for property: (bool) BoolValue
         the bool value of currently accessing property.  
             
         
        """
        pass
    
    ## Getter for property: (str) Category
    ##  the currently selected category name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         the currently selected category name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##  the currently selected category name.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         the currently selected category name.  
             
         
        """
        pass
    
    ## Getter for property: (int) ComponentType
    ##   the component type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def ComponentType(self) -> int:
        """
        Getter for property: (int) ComponentType
          the component type   
            
         
        """
        pass
    
    ## Setter for property: (int) ComponentType

    ##   the component type   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ComponentType.setter
    def ComponentType(self, componentType: int):
        """
        Setter for property: (int) ComponentType
          the component type   
            
         
        """
        pass
    
    ## Getter for property: (float) DoubleValue
    ##  the double value of currently accessing property.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def DoubleValue(self) -> float:
        """
        Getter for property: (float) DoubleValue
         the double value of currently accessing property.  
             
         
        """
        pass
    
    ## Setter for property: (float) DoubleValue

    ##  the double value of currently accessing property.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DoubleValue.setter
    def DoubleValue(self, doubleValue: float):
        """
        Setter for property: (float) DoubleValue
         the double value of currently accessing property.  
             
         
        """
        pass
    
    ## Getter for property: (int) IntValue
    ##  the int value of currently accessing property.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def IntValue(self) -> int:
        """
        Getter for property: (int) IntValue
         the int value of currently accessing property.  
             
         
        """
        pass
    
    ## Setter for property: (int) IntValue

    ##  the int value of currently accessing property.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @IntValue.setter
    def IntValue(self, intValue: int):
        """
        Setter for property: (int) IntValue
         the int value of currently accessing property.  
             
         
        """
        pass
    
    ## Getter for property: (@link BIMClassificationBuilder.RequisiteTypes NXOpen.Features.AECDesign.BIMClassificationBuilder.RequisiteTypes@endlink) PropertiesRequisiteType
    ##   the properties filter type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return BIMClassificationBuilder.RequisiteTypes
    @property
    def PropertiesRequisiteType(self) -> BIMClassificationBuilder.RequisiteTypes:
        """
        Getter for property: (@link BIMClassificationBuilder.RequisiteTypes NXOpen.Features.AECDesign.BIMClassificationBuilder.RequisiteTypes@endlink) PropertiesRequisiteType
          the properties filter type   
            
         
        """
        pass
    
    ## Setter for property: (@link BIMClassificationBuilder.RequisiteTypes NXOpen.Features.AECDesign.BIMClassificationBuilder.RequisiteTypes@endlink) PropertiesRequisiteType

    ##   the properties filter type   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PropertiesRequisiteType.setter
    def PropertiesRequisiteType(self, propertiesRequisiteType: BIMClassificationBuilder.RequisiteTypes):
        """
        Setter for property: (@link BIMClassificationBuilder.RequisiteTypes NXOpen.Features.AECDesign.BIMClassificationBuilder.RequisiteTypes@endlink) PropertiesRequisiteType
          the properties filter type   
            
         
        """
        pass
    
    ## Getter for property: (str) Property
    ##  the currently accessing property name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Property(self) -> str:
        """
        Getter for property: (str) Property
         the currently accessing property name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Property

    ##  the currently accessing property name.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Property.setter
    def Property(self, propertyName: str):
        """
        Setter for property: (str) Property
         the currently accessing property name.  
             
         
        """
        pass
    
    ## Getter for property: (str) StringValue
    ##  the string value of currently accessing property.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         the string value of currently accessing property.  
             
         
        """
        pass
    
    ## Setter for property: (str) StringValue

    ##  the string value of currently accessing property.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         the string value of currently accessing property.  
             
         
        """
        pass
    
    ##  Gets the select parts 
    ##  @return selectParts (@link NXOpen.Part List[NXOpen.Part]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetSelectParts(builder: BIMClassificationBuilder) -> List[NXOpen.Part]:
        """
         Gets the select parts 
         @return selectParts (@link NXOpen.Part List[NXOpen.Part]@endlink): .
        """
        pass
    
    ##  Sets the variant type and value as property name 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="boolValue"> (bool) </param>
    ## <param name="strDataType"> (str) </param>
    ## <param name="strRequisite"> (str) </param>
    def SetBoolValueAndTypeAsPropertyName(builder: BIMClassificationBuilder, propertyName: str, boolValue: bool, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    
    ##  Sets the variant type and value as property name 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="doubleValue"> (float) </param>
    ## <param name="strDataType"> (str) </param>
    ## <param name="strRequisite"> (str) </param>
    def SetDoubleValueAndTypeAsPropertyName(builder: BIMClassificationBuilder, propertyName: str, doubleValue: float, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    
    ##  Sets the variant type and value as property name 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="intValue"> (int) </param>
    ## <param name="strDataType"> (str) </param>
    ## <param name="strRequisite"> (str) </param>
    def SetIntValueAndTypeAsPropertyName(builder: BIMClassificationBuilder, propertyName: str, intValue: int, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    
    ##  Sets the selected parts. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="selectParts"> (@link NXOpen.Part List[NXOpen.Part]@endlink) </param>
    def SetSelectParts(builder: BIMClassificationBuilder, selectParts: List[NXOpen.Part]) -> None:
        """
         Sets the selected parts. 
        """
        pass
    
    ##  Sets the variant type and value as property name 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="propertyName"> (str) </param>
    ## <param name="stringValue"> (str) </param>
    ## <param name="strDataType"> (str) </param>
    ## <param name="strRequisite"> (str) </param>
    def SetStringValueAndTypeAsPropertyName(builder: BIMClassificationBuilder, propertyName: str, stringValue: str, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a BIM slope builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create BIMSlopeData in AEC Design.
##         
##      <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SlopeAngleDim.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SlopeHeightDim.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## SlopePercentage </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SlopeRatioDen </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## SlopeRatioNum </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SlopeSetting </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class BIMSlopeBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a BIM slope builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create BIMSlopeData in AEC Design.
        </remarks>
    """


    ##  Represent BIM slope types.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Angle</term><description> 
    ## </description> </item><item><term> 
    ## Height</term><description> 
    ## </description> </item><item><term> 
    ## Ratio</term><description> 
    ## </description> </item><item><term> 
    ## Percentage</term><description> 
    ## </description> </item></list>
    class SlopeOption(Enum):
        """
        Members Include: <NotSet> <Angle> <Height> <Ratio> <Percentage>
        """
        NotSet: int
        Angle: int
        Height: int
        Ratio: int
        Percentage: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BIMSlopeBuilder.SlopeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeAngleDim
    ##   the slope angle dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeAngleDim(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeAngleDim
          the slope angle dimension   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeHeightDim
    ##   the slope height dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SlopeHeightDim(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SlopeHeightDim
          the slope height dimension   
            
         
        """
        pass
    
    ## Getter for property: (float) SlopePercentage
    ##   the slope percentage   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def SlopePercentage(self) -> float:
        """
        Getter for property: (float) SlopePercentage
          the slope percentage   
            
         
        """
        pass
    
    ## Setter for property: (float) SlopePercentage

    ##   the slope percentage   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SlopePercentage.setter
    def SlopePercentage(self, slopePercentage: float):
        """
        Setter for property: (float) SlopePercentage
          the slope percentage   
            
         
        """
        pass
    
    ## Getter for property: (float) SlopeRatioDen
    ##   the slope ratio denominator   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def SlopeRatioDen(self) -> float:
        """
        Getter for property: (float) SlopeRatioDen
          the slope ratio denominator   
            
         
        """
        pass
    
    ## Setter for property: (float) SlopeRatioDen

    ##   the slope ratio denominator   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SlopeRatioDen.setter
    def SlopeRatioDen(self, slopeRatioDen: float):
        """
        Setter for property: (float) SlopeRatioDen
          the slope ratio denominator   
            
         
        """
        pass
    
    ## Getter for property: (float) SlopeRatioNum
    ##   the slope ratio numerator   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def SlopeRatioNum(self) -> float:
        """
        Getter for property: (float) SlopeRatioNum
          the slope ratio numerator   
            
         
        """
        pass
    
    ## Setter for property: (float) SlopeRatioNum

    ##   the slope ratio numerator   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SlopeRatioNum.setter
    def SlopeRatioNum(self, slopeRatioNum: float):
        """
        Setter for property: (float) SlopeRatioNum
          the slope ratio numerator   
            
         
        """
        pass
    
    ## Getter for property: (@link BIMSlopeBuilder.SlopeOption NXOpen.Features.AECDesign.BIMSlopeBuilder.SlopeOption@endlink) SlopeSetting
    ##   the slope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BIMSlopeBuilder.SlopeOption
    @property
    def SlopeSetting(self) -> BIMSlopeBuilder.SlopeOption:
        """
        Getter for property: (@link BIMSlopeBuilder.SlopeOption NXOpen.Features.AECDesign.BIMSlopeBuilder.SlopeOption@endlink) SlopeSetting
          the slope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link BIMSlopeBuilder.SlopeOption NXOpen.Features.AECDesign.BIMSlopeBuilder.SlopeOption@endlink) SlopeSetting

    ##   the slope setting   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SlopeSetting.setter
    def SlopeSetting(self, slopeSetting: BIMSlopeBuilder.SlopeOption):
        """
        Setter for property: (@link BIMSlopeBuilder.SlopeOption NXOpen.Features.AECDesign.BIMSlopeBuilder.SlopeOption@endlink) SlopeSetting
          the slope setting   
            
         
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a BoundaryOffset builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create BoundaryOffset Data in AEC Design.
##         
##      <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class BoundaryOffsetBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a BoundaryOffset builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create BoundaryOffset Data in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link BoundaryOffsetListItemBuilderList NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilderList@endlink) BoundaryOffsetList
    ##   the boundary offset list   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return BoundaryOffsetListItemBuilderList
    @property
    def BoundaryOffsetList(self) -> BoundaryOffsetListItemBuilderList:
        """
        Getter for property: (@link BoundaryOffsetListItemBuilderList NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilderList@endlink) BoundaryOffsetList
          the boundary offset list   
            
         
        """
        pass
    
    ##  The boundary offset item creation function
    ##  @return boundaryOffsetListItemBuilder (@link BoundaryOffsetListItemBuilder NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateBoundaryOffsetListItemBuilder(builder: BoundaryOffsetBuilder) -> BoundaryOffsetListItemBuilder:
        """
         The boundary offset item creation function
         @return boundaryOffsetListItemBuilder (@link BoundaryOffsetListItemBuilder NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class BoundaryOffsetListItemBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: BoundaryOffsetListItemBuilderList, objects: List[BoundaryOffsetListItemBuilder]) -> None:
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
    def Append(self, object_list: BoundaryOffsetListItemBuilderList, objectValue: BoundaryOffsetListItemBuilder) -> None:
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
    def Clear(object_list: BoundaryOffsetListItemBuilderList) -> None:
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
    def ClearIndex(object_list: BoundaryOffsetListItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: BoundaryOffsetListItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: BoundaryOffsetListItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: BoundaryOffsetListItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: BoundaryOffsetListItemBuilderList, obj: BoundaryOffsetListItemBuilder) -> None:
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
    def Erase(self, object_list: BoundaryOffsetListItemBuilderList, obj: BoundaryOffsetListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: BoundaryOffsetListItemBuilderList, obj: BoundaryOffsetListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link BoundaryOffsetListItemBuilder NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: BoundaryOffsetListItemBuilderList, index: int) -> BoundaryOffsetListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link BoundaryOffsetListItemBuilder NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link BoundaryOffsetListItemBuilder List[NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: BoundaryOffsetListItemBuilderList) -> List[BoundaryOffsetListItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link BoundaryOffsetListItemBuilder List[NXOpen.Features.AECDesign.BoundaryOffsetListItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: BoundaryOffsetListItemBuilderList, location: int, objectValue: BoundaryOffsetListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: BoundaryOffsetListItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: BoundaryOffsetListItemBuilderList, index: int) -> None:
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
    def SetContents(object_list: BoundaryOffsetListItemBuilderList, objects: List[BoundaryOffsetListItemBuilder]) -> None:
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
    def Swap(self, object_list: BoundaryOffsetListItemBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: BoundaryOffsetListItemBuilderList, object1: BoundaryOffsetListItemBuilder, object2: BoundaryOffsetListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  Boundary offset list item builder  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::BoundaryOffsetBuilder::CreateBoundaryOffsetListItemBuilder  NXOpen::Features::AECDesign::BoundaryOffsetBuilder::CreateBoundaryOffsetListItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class BoundaryOffsetListItemBuilder(NXOpen.TaggedObject): 
    """ Boundary offset list item builder """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BoundaryOffsetCurve
    ##   the boundary offset curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def BoundaryOffsetCurve(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BoundaryOffsetCurve
          the boundary offset curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoundaryOffsetDim
    ##   the boundary offset dim   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BoundaryOffsetDim(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BoundaryOffsetDim
          the boundary offset dim   
            
         
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a building element trim builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create BuildingElementTrimData in AEC Design.
##         
##      <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BooleanSetting </term> <description> 
##  
## Trim </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class BuildingElementTrimBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a building element trim builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create BuildingElementTrimData in AEC Design.
        </remarks>
    """


    ##  Represent building element trim types.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Trim</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class BooleanType(Enum):
        """
        Members Include: <Trim> <NotSet>
        """
        Trim: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BuildingElementTrimBuilder.BooleanType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link BuildingElementTrimBuilder.BooleanType NXOpen.Features.AECDesign.BuildingElementTrimBuilder.BooleanType@endlink) BooleanSetting
    ##   the boolean setting.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return BuildingElementTrimBuilder.BooleanType
    @property
    def BooleanSetting(self) -> BuildingElementTrimBuilder.BooleanType:
        """
        Getter for property: (@link BuildingElementTrimBuilder.BooleanType NXOpen.Features.AECDesign.BuildingElementTrimBuilder.BooleanType@endlink) BooleanSetting
          the boolean setting.  
             
         
        """
        pass
    
    ## Setter for property: (@link BuildingElementTrimBuilder.BooleanType NXOpen.Features.AECDesign.BuildingElementTrimBuilder.BooleanType@endlink) BooleanSetting

    ##   the boolean setting.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BooleanSetting.setter
    def BooleanSetting(self, booleanSetting: BuildingElementTrimBuilder.BooleanType):
        """
        Setter for property: (@link BuildingElementTrimBuilder.BooleanType NXOpen.Features.AECDesign.BuildingElementTrimBuilder.BooleanType@endlink) BooleanSetting
          the boolean setting.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
    ##   the tool body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
          the tool body.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##   @brief 
##         Represents a ceiling builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create ceiling feature in AEC Design.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecCeilingBuilder  NXOpen::Features::AECDesignCollection::CreateAecCeilingBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Offset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Thickness.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TrimFlag </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class CeilingBuilder(NXOpen.Features.FeatureBuilder): 
    """ <summary>
        Represents a ceiling builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create ceiling feature in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link BoundaryOffsetBuilder NXOpen.Features.AECDesign.BoundaryOffsetBuilder@endlink) BoundaryOffset
    ##   the level reference  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BoundaryOffsetBuilder
    @property
    def BoundaryOffset(self) -> BoundaryOffsetBuilder:
        """
        Getter for property: (@link BoundaryOffsetBuilder NXOpen.Features.AECDesign.BoundaryOffsetBuilder@endlink) BoundaryOffset
          the level reference  
            
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
    ##   the level reference  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
          the level reference  
            
         
        """
        pass
    
    ## Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
    ##   the material layers  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MaterialLayersBuilder
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
          the material layers  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##   the offset distance between ceiling and the original room top face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
          the offset distance between ceiling and the original room top face.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectCurves
    ##   the boundary curve to define ceiling.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SelectCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectCurves
          the boundary curve to define ceiling.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
    ##   the tool body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
          the tool body   
            
         
        """
        pass
    
    ## Getter for property: (bool) TrimFlag
    ##   the building element trim flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def TrimFlag(self) -> bool:
        """
        Getter for property: (bool) TrimFlag
          the building element trim flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) TrimFlag

    ##   the building element trim flag   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TrimFlag.setter
    def TrimFlag(self, trimFlag: bool):
        """
        Setter for property: (bool) TrimFlag
          the building element trim flag   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a ceiling feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::CeilingBuilder  NXOpen::Features::AECDesign::CeilingBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Ceiling(NXOpen.Features.BodyFeature): 
    """ Represents a ceiling feature """
    pass


import NXOpen
import NXOpen.Features
##   @brief 
##         Represents a column builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create column feature in AEC Design.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecColumnBuilder  NXOpen::Features::AECDesignCollection::CreateAecColumnBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## XOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## YOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class ColumnBuilder(NXOpen.Features.FeatureBuilder): 
    """ <summary>
        Represents a column builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create column feature in AEC Design.
        </remarks>
    """


    ##  method used to create the support feature. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Points</term><description> 
    ## </description> </item><item><term> 
    ## SpecifyLine</term><description> 
    ## </description> </item></list>
    class CreationMethod(Enum):
        """
        Members Include: <Points> <SpecifyLine>
        """
        Points: int
        SpecifyLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.CreationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the y-axis alignment types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LeftAligned</term><description> 
    ## </description> </item><item><term> 
    ## RightAligned</term><description> 
    ## </description> </item><item><term> 
    ## CenterlineAligned</term><description> 
    ## </description> </item></list>
    class HorizontalAlignmentTypes(Enum):
        """
        Members Include: <LeftAligned> <RightAligned> <CenterlineAligned>
        """
        LeftAligned: int
        RightAligned: int
        CenterlineAligned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.HorizontalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the rotation type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Right90</term><description> 
    ## </description> </item><item><term> 
    ## Left90</term><description> 
    ## </description> </item><item><term> 
    ## Vertical</term><description> 
    ## </description> </item><item><term> 
    ## Horizontal</term><description> 
    ## </description> </item><item><term> 
    ## MoreOption</term><description> 
    ## </description> </item></list>
    class RotationType(Enum):
        """
        Members Include: <Right90> <Left90> <Vertical> <Horizontal> <MoreOption>
        """
        Right90: int
        Left90: int
        Vertical: int
        Horizontal: int
        MoreOption: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.RotationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the z-axis alignment types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TopAligned</term><description> 
    ## </description> </item><item><term> 
    ## BottomAligned</term><description> 
    ## </description> </item><item><term> 
    ## CenterlineAligned</term><description> 
    ## </description> </item></list>
    class VerticalAlignmentTypes(Enum):
        """
        Members Include: <TopAligned> <BottomAligned> <CenterlineAligned>
        """
        TopAligned: int
        BottomAligned: int
        CenterlineAligned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.VerticalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceBottom
    ##   the lower level reference.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReferenceBottom(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceBottom
          the lower level reference.  
             
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceTop
    ##   the higher level reference.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReferenceTop(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceTop
          the higher level reference.  
             
         
        """
        pass
    
    ## Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
    ##   the materialSection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return MaterialSectionBuilder
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
          the materialSection.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PathGeometry
    ##   the path geometry.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def PathGeometry(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PathGeometry
          the path geometry.  
             
         
        """
        pass
    
    ## Getter for property: (@link ColumnBuilder.CreationMethod NXOpen.Features.AECDesign.ColumnBuilder.CreationMethod@endlink) PlacementMethod
    ##   the placement method used to locate the column.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ColumnBuilder.CreationMethod
    @property
    def PlacementMethod(self) -> ColumnBuilder.CreationMethod:
        """
        Getter for property: (@link ColumnBuilder.CreationMethod NXOpen.Features.AECDesign.ColumnBuilder.CreationMethod@endlink) PlacementMethod
          the placement method used to locate the column.  
             
         
        """
        pass
    
    ## Setter for property: (@link ColumnBuilder.CreationMethod NXOpen.Features.AECDesign.ColumnBuilder.CreationMethod@endlink) PlacementMethod

    ##   the placement method used to locate the column.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PlacementMethod.setter
    def PlacementMethod(self, placementMethod: ColumnBuilder.CreationMethod):
        """
        Setter for property: (@link ColumnBuilder.CreationMethod NXOpen.Features.AECDesign.ColumnBuilder.CreationMethod@endlink) PlacementMethod
          the placement method used to locate the column.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Points
    ##   the points.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Points(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Points
          the points.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationAngle
    ##   the rotation angle.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationAngle
          the rotation angle.  
             
         
        """
        pass
    
    ## Getter for property: (@link ColumnBuilder.RotationType NXOpen.Features.AECDesign.ColumnBuilder.RotationType@endlink) RotationOption
    ##   the rotation option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ColumnBuilder.RotationType
    @property
    def RotationOption(self) -> ColumnBuilder.RotationType:
        """
        Getter for property: (@link ColumnBuilder.RotationType NXOpen.Features.AECDesign.ColumnBuilder.RotationType@endlink) RotationOption
          the rotation option.  
             
         
        """
        pass
    
    ## Setter for property: (@link ColumnBuilder.RotationType NXOpen.Features.AECDesign.ColumnBuilder.RotationType@endlink) RotationOption

    ##   the rotation option.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RotationOption.setter
    def RotationOption(self, rotationOption: ColumnBuilder.RotationType):
        """
        Setter for property: (@link ColumnBuilder.RotationType NXOpen.Features.AECDesign.ColumnBuilder.RotationType@endlink) RotationOption
          the rotation option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) TrimWithinLimits
    ##   the flag to indicate whether the trim winthin limits or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def TrimWithinLimits(self) -> bool:
        """
        Getter for property: (bool) TrimWithinLimits
          the flag to indicate whether the trim winthin limits or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) TrimWithinLimits

    ##   the flag to indicate whether the trim winthin limits or not.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TrimWithinLimits.setter
    def TrimWithinLimits(self, isTrimWithinLimits: bool):
        """
        Setter for property: (bool) TrimWithinLimits
          the flag to indicate whether the trim winthin limits or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link ColumnBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.HorizontalAlignmentTypes@endlink) XAlignmentType
    ##   the x offset alignment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ColumnBuilder.HorizontalAlignmentTypes
    @property
    def XAlignmentType(self) -> ColumnBuilder.HorizontalAlignmentTypes:
        """
        Getter for property: (@link ColumnBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.HorizontalAlignmentTypes@endlink) XAlignmentType
          the x offset alignment.  
             
         
        """
        pass
    
    ## Setter for property: (@link ColumnBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.HorizontalAlignmentTypes@endlink) XAlignmentType

    ##   the x offset alignment.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @XAlignmentType.setter
    def XAlignmentType(self, xAlignmentType: ColumnBuilder.HorizontalAlignmentTypes):
        """
        Setter for property: (@link ColumnBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.HorizontalAlignmentTypes@endlink) XAlignmentType
          the x offset alignment.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##   the x offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
          the x offset.  
             
         
        """
        pass
    
    ## Getter for property: (@link ColumnBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.VerticalAlignmentTypes@endlink) YAlignmentType
    ##   the y offset alignment.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ColumnBuilder.VerticalAlignmentTypes
    @property
    def YAlignmentType(self) -> ColumnBuilder.VerticalAlignmentTypes:
        """
        Getter for property: (@link ColumnBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.VerticalAlignmentTypes@endlink) YAlignmentType
          the y offset alignment.  
            
         
        """
        pass
    
    ## Setter for property: (@link ColumnBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.VerticalAlignmentTypes@endlink) YAlignmentType

    ##   the y offset alignment.  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @YAlignmentType.setter
    def YAlignmentType(self, yAlignmentType: ColumnBuilder.VerticalAlignmentTypes):
        """
        Setter for property: (@link ColumnBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.VerticalAlignmentTypes@endlink) YAlignmentType
          the y offset alignment.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##   the y offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
          the y offset.  
             
         
        """
        pass
    
import NXOpen.Features
##  Represents a column feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::ColumnBuilder  NXOpen::Features::AECDesign::ColumnBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Column(NXOpen.Features.BodyFeature): 
    """ Represents a column feature """
    pass


import NXOpen
import NXOpen.Features
##   @brief 
##         Represents a crossing rebars builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create crossing rebars feature in AEC Design.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecCrossingRebarsBuilder  NXOpen::Features::AECDesignCollection::CreateAecCrossingRebarsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class CrossingRebarsBuilder(NXOpen.Features.FeatureBuilder): 
    """ <summary>
        Represents a crossing rebars builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create crossing rebars feature in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link AlternateCoverThicknessBuilder NXOpen.Features.AECDesign.AlternateCoverThicknessBuilder@endlink) AlternateCoverThickness
    ##   the alternate cover thickness offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return AlternateCoverThicknessBuilder
    @property
    def AlternateCoverThickness(self) -> AlternateCoverThicknessBuilder:
        """
        Getter for property: (@link AlternateCoverThicknessBuilder NXOpen.Features.AECDesign.AlternateCoverThicknessBuilder@endlink) AlternateCoverThickness
          the alternate cover thickness offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BendingRadius
    ##   the bending radius.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BendingRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BendingRadius
          the bending radius.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the diameter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the diameter.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) EndHook
    ##   the end hook.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarHookBlockBuilder
    @property
    def EndHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) EndHook
          the end hook.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) EndLimit
    ##   the end limit.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarLimitBuilder
    @property
    def EndLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) EndLimit
          the end limit.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) EndPointLocation
    ##   the end point location.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return OnPathDimensionBuilder
    @property
    def EndPointLocation(self) -> OnPathDimensionBuilder:
        """
        Getter for property: (@link OnPathDimensionBuilder NXOpen.GeometricUtilities.OnPathDimensionBuilder@endlink) EndPointLocation
          the end point location.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ExcludeSegment
    ##   the flag to indicate whether to open the exclude segment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def ExcludeSegment(self) -> bool:
        """
        Getter for property: (bool) ExcludeSegment
          the flag to indicate whether to open the exclude segment.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ExcludeSegment

    ##   the flag to indicate whether to open the exclude segment.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ExcludeSegment.setter
    def ExcludeSegment(self, excludeSegment: bool):
        """
        Setter for property: (bool) ExcludeSegment
          the flag to indicate whether to open the exclude segment.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IntervalDistance
    ##   the interval distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def IntervalDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IntervalDistance
          the interval distance.  
             
         
        """
        pass
    
    ## Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
    ##   the materialSection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return MaterialSectionBuilder
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
          the materialSection.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfRebars
    ##   the number of rebars.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NumberOfRebars(self) -> int:
        """
        Getter for property: (int) NumberOfRebars
          the number of rebars.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfRebars

    ##   the number of rebars.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfRebars.setter
    def NumberOfRebars(self, numberOfRebars: int):
        """
        Setter for property: (int) NumberOfRebars
          the number of rebars.  
             
         
        """
        pass
    
    ## Getter for property: (float) NumberOfTurns
    ##   the number of turns.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def NumberOfTurns(self) -> float:
        """
        Getter for property: (float) NumberOfTurns
          the number of turns.  
             
         
        """
        pass
    
    ## Setter for property: (float) NumberOfTurns

    ##   the number of turns.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfTurns.setter
    def NumberOfTurns(self, numberOfTurns: float):
        """
        Setter for property: (float) NumberOfTurns
          the number of turns.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PitchDistance
    ##   the pitch distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PitchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PitchDistance
          the pitch distance.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.CrossingCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.CrossingCreationMethod@endlink) PlacementMethod
    ##   the placement method used to locate the crossing rebars.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.CrossingCreationMethod
    @property
    def PlacementMethod(self) -> RebarsBuilder.CrossingCreationMethod:
        """
        Getter for property: (@link RebarsBuilder.CrossingCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.CrossingCreationMethod@endlink) PlacementMethod
          the placement method used to locate the crossing rebars.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.CrossingCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.CrossingCreationMethod@endlink) PlacementMethod

    ##   the placement method used to locate the crossing rebars.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @PlacementMethod.setter
    def PlacementMethod(self, placementMethod: RebarsBuilder.CrossingCreationMethod):
        """
        Setter for property: (@link RebarsBuilder.CrossingCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.CrossingCreationMethod@endlink) PlacementMethod
          the placement method used to locate the crossing rebars.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseDirection
    ##   the reverse direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
          the reverse direction.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseDirection

    ##   the reverse direction.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
          the reverse direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectEdge
    ##   the select edge.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectEdge
          the select edge.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.SpacingOption NXOpen.Features.AECDesign.RebarsBuilder.SpacingOption@endlink) SpacingSetting
    ##   the space setting.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.SpacingOption
    @property
    def SpacingSetting(self) -> RebarsBuilder.SpacingOption:
        """
        Getter for property: (@link RebarsBuilder.SpacingOption NXOpen.Features.AECDesign.RebarsBuilder.SpacingOption@endlink) SpacingSetting
          the space setting.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.SpacingOption NXOpen.Features.AECDesign.RebarsBuilder.SpacingOption@endlink) SpacingSetting

    ##   the space setting.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SpacingSetting.setter
    def SpacingSetting(self, spacingSetting: RebarsBuilder.SpacingOption):
        """
        Setter for property: (@link RebarsBuilder.SpacingOption NXOpen.Features.AECDesign.RebarsBuilder.SpacingOption@endlink) SpacingSetting
          the space setting.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) StartFace
    ##   the start face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def StartFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) StartFace
          the start face.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) StartHook
    ##   the start hook.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarHookBlockBuilder
    @property
    def StartHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) StartHook
          the start hook.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) StartLimit
    ##   the start limit.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarLimitBuilder
    @property
    def StartLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) StartLimit
          the start limit.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint
    ##   the start point.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint
          the start point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint

    ##   the start point.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint
          the start point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessDistance
    ##   the thickness distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThicknessDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessDistance
          the thickness distance.  
             
         
        """
        pass
    
    ## Getter for property: (float) TurnsAtEnd
    ##   the extra turns at end.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def TurnsAtEnd(self) -> float:
        """
        Getter for property: (float) TurnsAtEnd
          the extra turns at end.  
             
         
        """
        pass
    
    ## Setter for property: (float) TurnsAtEnd

    ##   the extra turns at end.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TurnsAtEnd.setter
    def TurnsAtEnd(self, turnsAtEnd: float):
        """
        Setter for property: (float) TurnsAtEnd
          the extra turns at end.  
             
         
        """
        pass
    
    ## Getter for property: (float) TurnsAtStart
    ##   the extra turns at start.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def TurnsAtStart(self) -> float:
        """
        Getter for property: (float) TurnsAtStart
          the extra turns at start.  
             
         
        """
        pass
    
    ## Setter for property: (float) TurnsAtStart

    ##   the extra turns at start.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TurnsAtStart.setter
    def TurnsAtStart(self, turnsAtStart: float):
        """
        Setter for property: (float) TurnsAtStart
          the extra turns at start.  
             
         
        """
        pass
    
    ##  Updates referenced columns. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_concrete ("Concrete Design")
    @staticmethod
    def UpdateReferencedRebarBodies(builder: CrossingRebarsBuilder) -> None:
        """
         Updates referenced columns. 
        """
        pass
    
import NXOpen.Features
##  Represents a crossingrebars feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::CrossingRebarsBuilder  NXOpen::Features::AECDesign::CrossingRebarsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class CrossingRebars(NXOpen.Features.BodyFeature): 
    """ Represents a crossingrebars feature """
    pass


import NXOpen
import NXOpen.Assemblies
##   @brief 
##         Represents a Explode Component builder for AEC. 
##          
## 
##  
##         
##         This builder is used to explode BIM components in AEC.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateExplodeComponentBuilder  NXOpen::Features::AECDesignCollection::CreateExplodeComponentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SelectScope </term> <description> 
##  
## AllComponents </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class ExplodeComponentBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a Explode Component builder for AEC. 
        </summary>
        <remarks>
        This builder is used to explode BIM components in AEC.
        </remarks>
    """


    ## Specify BIM components scope to explode
    ##  All supported BIM components 
    class ExplodeScope(Enum):
        """
        Members Include: <AllComponents> <SelectedComponents>
        """
        AllComponents: int
        SelectedComponents: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExplodeComponentBuilder.ExplodeScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SelectComponents
    ##   the selected BIM components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def SelectComponents(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) SelectComponents
          the selected BIM components   
            
         
        """
        pass
    
    ## Getter for property: (@link ExplodeComponentBuilder.ExplodeScope NXOpen.Features.AECDesign.ExplodeComponentBuilder.ExplodeScope@endlink) SelectScope
    ##   the BIM components scope   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ExplodeComponentBuilder.ExplodeScope
    @property
    def SelectScope(self) -> ExplodeComponentBuilder.ExplodeScope:
        """
        Getter for property: (@link ExplodeComponentBuilder.ExplodeScope NXOpen.Features.AECDesign.ExplodeComponentBuilder.ExplodeScope@endlink) SelectScope
          the BIM components scope   
            
         
        """
        pass
    
    ## Setter for property: (@link ExplodeComponentBuilder.ExplodeScope NXOpen.Features.AECDesign.ExplodeComponentBuilder.ExplodeScope@endlink) SelectScope

    ##   the BIM components scope   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SelectScope.setter
    def SelectScope(self, selectScope: ExplodeComponentBuilder.ExplodeScope):
        """
        Setter for property: (@link ExplodeComponentBuilder.ExplodeScope NXOpen.Features.AECDesign.ExplodeComponentBuilder.ExplodeScope@endlink) SelectScope
          the BIM components scope   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##   @brief 
##         Represents an ExtendToRoofBuilder  for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create ExtendToRoof feature in AEC Design.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateExtendToRoofBuilder  NXOpen::Features::AECDesignCollection::CreateExtendToRoofBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ExtendToRoofBuilder(NXOpen.Features.FeatureBuilder): 
    """ <summary>
        Represents an ExtendToRoofBuilder  for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create ExtendToRoof feature in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectTargets
    ##   the select target objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectTargets(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectTargets
          the select target objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectTools
    ##   the select tool object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectTools(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectTools
          the select tool object   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a extend to roof feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::ExtendToRoofBuilder  NXOpen::Features::AECDesign::ExtendToRoofBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ExtendToRoof(NXOpen.Features.BodyFeature): 
    """ Represents a extend to roof feature """
    pass


import NXOpen
import NXOpen.Features
##   @brief 
##         Represents a floor builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create floor feature in AEC Design.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecFloorBuilder  NXOpen::Features::AECDesignCollection::CreateAecFloorBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BIMSlope.SlopeAngleDim.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## BIMSlope.SlopeHeightDim.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BIMSlope.SlopePercentage </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## BIMSlope.SlopeRatioDen </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## BIMSlope.SlopeRatioNum </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## BIMSlope.SlopeSetting </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## TrimFlag </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class FloorBuilder(NXOpen.Features.FeatureBuilder): 
    """ <summary>
        Represents a floor builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create floor feature in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link BIMSlopeBuilder NXOpen.Features.AECDesign.BIMSlopeBuilder@endlink) BIMSlope
    ##   the BIM slope   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BIMSlopeBuilder
    @property
    def BIMSlope(self) -> BIMSlopeBuilder:
        """
        Getter for property: (@link BIMSlopeBuilder NXOpen.Features.AECDesign.BIMSlopeBuilder@endlink) BIMSlope
          the BIM slope   
            
         
        """
        pass
    
    ## Getter for property: (@link BoundaryOffsetBuilder NXOpen.Features.AECDesign.BoundaryOffsetBuilder@endlink) BoundaryOffset
    ##   the boundary offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BoundaryOffsetBuilder
    @property
    def BoundaryOffset(self) -> BoundaryOffsetBuilder:
        """
        Getter for property: (@link BoundaryOffsetBuilder NXOpen.Features.AECDesign.BoundaryOffsetBuilder@endlink) BoundaryOffset
          the boundary offset   
            
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
    ##   the level reference  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
          the level reference  
            
         
        """
        pass
    
    ## Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
    ##   the material layers  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MaterialLayersBuilder
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
          the material layers  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectCurve
    ##   the boundary curves to define floor.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SelectCurve(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SelectCurve
          the boundary curves to define floor.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SlopeCurve
    ##   the slope curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SlopeCurve(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SlopeCurve
          the slope curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
    ##   the tool body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ToolBody
          the tool body   
            
         
        """
        pass
    
    ## Getter for property: (bool) TrimFlag
    ##   the building element trim flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def TrimFlag(self) -> bool:
        """
        Getter for property: (bool) TrimFlag
          the building element trim flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) TrimFlag

    ##   the building element trim flag   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TrimFlag.setter
    def TrimFlag(self, trimFlag: bool):
        """
        Setter for property: (bool) TrimFlag
          the building element trim flag   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a floor feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::FloorBuilder  NXOpen::Features::AECDesign::FloorBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Floor(NXOpen.Features.BodyFeature): 
    """ Represents a floor feature """
    pass


import NXOpen
## 
##             Represents a @link Features::AECDesign::GridBuilder Features::AECDesign::GridBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateGridBuilder  NXOpen::Features::AECDesignCollection::CreateGridBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class GridBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.GridBuilder</ja_class> builder
        """


    ##  Represents the type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Create</term><description> 
    ## </description> </item><item><term> 
    ## Select</term><description> 
    ## </description> </item><item><term> 
    ## Num</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Create> <Select> <Num>
        """
        Create: int
        Select: int
        Num: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GridBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
## 
##             Represents a @link Features::AECDesign::GridLineNoteBuilder Features::AECDesign::GridLineNoteBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateGridLineNoteBuilder  NXOpen::Features::AECDesignCollection::CreateGridLineNoteBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class GridLineNoteBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.GridLineNoteBuilder</ja_class> builder
        """


    ## Getter for property: (str) BalloonText
    ##   the balloon text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def BalloonText(self) -> str:
        """
        Getter for property: (str) BalloonText
          the balloon text   
            
         
        """
        pass
    
    ## Setter for property: (str) BalloonText

    ##   the balloon text   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BalloonText.setter
    def BalloonText(self, balloonText: str):
        """
        Setter for property: (str) BalloonText
          the balloon text   
            
         
        """
        pass
    
    ##  Updates the balloon text 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateNotes(builder: GridLineNoteBuilder) -> None:
        """
         Updates the balloon text 
        """
        pass
    
import NXOpen
import NXOpen.Annotations
## 
##             Represents a @link Features::AECDesign::GridLineOffsetBuilder Features::AECDesign::GridLineOffsetBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateGridLineOffsetBuilder  NXOpen::Features::AECDesignCollection::CreateGridLineOffsetBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class GridLineOffsetBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.GridLineOffsetBuilder</ja_class> builder
        """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
    ##   the distance to offset the grid line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
          the distance to offset the grid line.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlipAll
    ##   the flag to indicate whether to flip the offset direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def FlipAll(self) -> bool:
        """
        Getter for property: (bool) FlipAll
          the flag to indicate whether to flip the offset direction.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlipAll

    ##   the flag to indicate whether to flip the offset direction.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FlipAll.setter
    def FlipAll(self, bFilped: bool):
        """
        Setter for property: (bool) FlipAll
          the flag to indicate whether to flip the offset direction.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfCopies
    ##   the number of the copied grid lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
          the number of the copied grid lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfCopies

    ##   the number of the copied grid lines.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
          the number of the copied grid lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Section
    ##   the selected sketch curve collector for copying grid line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Section(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Section
          the selected sketch curve collector for copying grid line.  
             
         
        """
        pass
    
    ##  Clears the selection of the target grid line. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def ClearSelection(builder: GridLineOffsetBuilder) -> None:
        """
         Clears the selection of the target grid line. 
        """
        pass
    
    ##  Copies the selection of the target grid line. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def CopyGridLines(builder: GridLineOffsetBuilder) -> None:
        """
         Copies the selection of the target grid line. 
        """
        pass
    
    ##  Selects the target grid line to offset. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  the offset vector 
    def SelectGridLine(builder: GridLineOffsetBuilder, tgBaseLine: NXOpen.Annotations.AECDesignBaseLine, offsetVector: NXOpen.Vector3d) -> None:
        """
         Selects the target grid line to offset. 
        """
        pass
    
    ##  Updates the offset distance of the target grid line. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateDistance(builder: GridLineOffsetBuilder) -> None:
        """
         Updates the offset distance of the target grid line. 
        """
        pass
    
    ##  Updates the offset direction accroding to the flip state. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateFlip(builder: GridLineOffsetBuilder) -> None:
        """
         Updates the offset direction accroding to the flip state. 
        """
        pass
    
    ##  Updates the number of copies of the target grid line. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateNumOfCopies(builder: GridLineOffsetBuilder) -> None:
        """
         Updates the number of copies of the target grid line. 
        """
        pass
    
import NXOpen
## 
##             Represents a @link Features::AECDesign::GridLinePreferencesBuilder Features::AECDesign::GridLinePreferencesBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateGridLinePreferencesBuilder  NXOpen::Features::AECDesignCollection::CreateGridLinePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class GridLinePreferencesBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.GridLinePreferencesBuilder</ja_class> builder
        """


    ## Getter for property: (float) AnnotationScale
    ##   the scale of grid annotation.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def AnnotationScale(self) -> float:
        """
        Getter for property: (float) AnnotationScale
          the scale of grid annotation.  
             
         
        """
        pass
    
    ## Setter for property: (float) AnnotationScale

    ##   the scale of grid annotation.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AnnotationScale.setter
    def AnnotationScale(self, scale: float):
        """
        Setter for property: (float) AnnotationScale
          the scale of grid annotation.  
             
         
        """
        pass
    
    ## Getter for property: (int) CenterSegmentType
    ##   the type of center segment.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def CenterSegmentType(self) -> int:
        """
        Getter for property: (int) CenterSegmentType
          the type of center segment.  
             
         
        """
        pass
    
    ## Setter for property: (int) CenterSegmentType

    ##   the type of center segment.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @CenterSegmentType.setter
    def CenterSegmentType(self, centerSegmentType: int):
        """
        Setter for property: (int) CenterSegmentType
          the type of center segment.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateEndAnnotation
    ##   the flag to indicate whether to create the end annoation of grid line or not.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def CreateEndAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateEndAnnotation
          the flag to indicate whether to create the end annoation of grid line or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateEndAnnotation

    ##   the flag to indicate whether to create the end annoation of grid line or not.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @CreateEndAnnotation.setter
    def CreateEndAnnotation(self, createEndAnnotation: bool):
        """
        Setter for property: (bool) CreateEndAnnotation
          the flag to indicate whether to create the end annoation of grid line or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateStartAnnotation
    ##   the flag to indicate whether to create the start annoation of grid line or not.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def CreateStartAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateStartAnnotation
          the flag to indicate whether to create the start annoation of grid line or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateStartAnnotation

    ##   the flag to indicate whether to create the start annoation of grid line or not.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @CreateStartAnnotation.setter
    def CreateStartAnnotation(self, createStartAnnotation: bool):
        """
        Setter for property: (bool) CreateStartAnnotation
          the flag to indicate whether to create the start annoation of grid line or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LineEndSegmentLength
    ##   the length of grid line end segment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LineEndSegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LineEndSegmentLength
          the length of grid line end segment   
            
         
        """
        pass
    
    ## Getter for property: (int) SymbolType
    ##   the type of grid line end symbol.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def SymbolType(self) -> int:
        """
        Getter for property: (int) SymbolType
          the type of grid line end symbol.  
             
         
        """
        pass
    
    ## Setter for property: (int) SymbolType

    ##   the type of grid line end symbol.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SymbolType.setter
    def SymbolType(self, symbolType: int):
        """
        Setter for property: (int) SymbolType
          the type of grid line end symbol.  
             
         
        """
        pass
    
    ##  Updates the grid line color, style, width.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="endSegmentColor"> (int) </param>
    ## <param name="endSegmentStyle"> (int) </param>
    ## <param name="endSegmentWidth"> (int) </param>
    ## <param name="centerSegmentColor"> (int) </param>
    ## <param name="centerSegmentStyle"> (int) </param>
    ## <param name="centerSegmentWidth"> (int) </param>
    def UpdateColorStyleWidth(builder: GridLinePreferencesBuilder, endSegmentColor: int, endSegmentStyle: int, endSegmentWidth: int, centerSegmentColor: int, centerSegmentStyle: int, centerSegmentWidth: int) -> None:
        """
         Updates the grid line color, style, width.
        """
        pass
    
import NXOpen.Features
##  Represents a AEC grid feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::GridBuilder  NXOpen::Features::AECDesign::GridBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Grid(NXOpen.Features.Feature): 
    """ Represents a AEC grid feature """
    pass


import NXOpen
import NXOpen.Assemblies
## 
##            Represents a @link Features::AECDesign::LabellingRoomsBuilder Features::AECDesign::LabellingRoomsBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateLabellingAecRoomsBuilder  NXOpen::Features::AECDesignCollection::CreateLabellingAecRoomsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LabellingRoomsBuilder(NXOpen.Builder): 
    """
           Represents a <ja_class>Features.AECDesign.LabellingRoomsBuilder</ja_class> builder
        """


    ##  Settings that indicate how to handle the exsiting label.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Preserve</term><description> 
    ## </description> </item><item><term> 
    ## Delete</term><description> 
    ## </description> </item></list>
    class ExisingaeclabelType(Enum):
        """
        Members Include: <Preserve> <Delete>
        """
        Preserve: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LabellingRoomsBuilder.ExisingaeclabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Associativity
    ##   the setting that indicates whether pmi note  will be associative with room or equipment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Associativity(self) -> bool:
        """
        Getter for property: (bool) Associativity
          the setting that indicates whether pmi note  will be associative with room or equipment  
            
         
        """
        pass
    
    ## Setter for property: (bool) Associativity

    ##   the setting that indicates whether pmi note  will be associative with room or equipment  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Associativity.setter
    def Associativity(self, isAssociativity: bool):
        """
        Setter for property: (bool) Associativity
          the setting that indicates whether pmi note  will be associative with room or equipment  
            
         
        """
        pass
    
    ## Getter for property: (@link LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Features.AECDesign.LabellingRoomsBuilder.ExisingaeclabelType@endlink) ExsitingLabelOption
    ##  the option to specify how to handle existing label  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LabellingRoomsBuilder.ExisingaeclabelType
    @property
    def ExsitingLabelOption(self) -> LabellingRoomsBuilder.ExisingaeclabelType:
        """
        Getter for property: (@link LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Features.AECDesign.LabellingRoomsBuilder.ExisingaeclabelType@endlink) ExsitingLabelOption
         the option to specify how to handle existing label  
            
         
        """
        pass
    
    ## Setter for property: (@link LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Features.AECDesign.LabellingRoomsBuilder.ExisingaeclabelType@endlink) ExsitingLabelOption

    ##  the option to specify how to handle existing label  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ExsitingLabelOption.setter
    def ExsitingLabelOption(self, existingLabel: LabellingRoomsBuilder.ExisingaeclabelType):
        """
        Setter for property: (@link LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Features.AECDesign.LabellingRoomsBuilder.ExisingaeclabelType@endlink) ExsitingLabelOption
         the option to specify how to handle existing label  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) RoomsSelection
    ##   the rooms or equipment selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Assemblies.SelectComponentList
    @property
    def RoomsSelection(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: (@link NXOpen.Assemblies.SelectComponentList NXOpen.Assemblies.SelectComponentList@endlink) RoomsSelection
          the rooms or equipment selection   
            
         
        """
        pass
    
import NXOpen
## 
##             Represents a @link Features::AECDesign::LevelBuilder Features::AECDesign::LevelBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateLevelBuilder  NXOpen::Features::AECDesignCollection::CreateLevelBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class LevelBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.LevelBuilder</ja_class> builder
        """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumX
    ##   the maximum X position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumX
          the maximum X position   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumY
    ##   the maximum Y position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumY
          the maximum Y position   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumX
    ##   the minimum X position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumX(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumX
          the minimum X position   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumY
    ##   the minimum Y position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumY(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumY
          the minimum Y position   
            
         
        """
        pass
    
import NXOpen
## 
##             Represents a @link Features::AECDesign::GridLineNoteBuilder Features::AECDesign::GridLineNoteBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateLevelLineNoteBuilder  NXOpen::Features::AECDesignCollection::CreateLevelLineNoteBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class LevelLineNoteBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.GridLineNoteBuilder</ja_class> builder
        """


    ## Getter for property: (str) LabelText
    ##   the label text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def LabelText(self) -> str:
        """
        Getter for property: (str) LabelText
          the label text   
            
         
        """
        pass
    
    ## Setter for property: (str) LabelText

    ##   the label text   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LabelText.setter
    def LabelText(self, labelText: str):
        """
        Setter for property: (str) LabelText
          the label text   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LevelHeight
    ##   the height of aec level   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LevelHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LevelHeight
          the height of aec level   
            
         
        """
        pass
    
import NXOpen
## 
##             Represents a @link Features::AECDesign::LevelLinePreferencesBuilder Features::AECDesign::LevelLinePreferencesBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateLevelLinePreferencesBuilder  NXOpen::Features::AECDesignCollection::CreateLevelLinePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class LevelLinePreferencesBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.LevelLinePreferencesBuilder</ja_class> builder
        """


    ## Getter for property: (float) AnnotationScale
    ##   the scale of level annotation.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def AnnotationScale(self) -> float:
        """
        Getter for property: (float) AnnotationScale
          the scale of level annotation.  
             
         
        """
        pass
    
    ## Setter for property: (float) AnnotationScale

    ##   the scale of level annotation.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AnnotationScale.setter
    def AnnotationScale(self, scale: float):
        """
        Setter for property: (float) AnnotationScale
          the scale of level annotation.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateEndAnnotation
    ##   the flag to indicate whether to create the end annoation of level line or not.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def CreateEndAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateEndAnnotation
          the flag to indicate whether to create the end annoation of level line or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateEndAnnotation

    ##   the flag to indicate whether to create the end annoation of level line or not.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @CreateEndAnnotation.setter
    def CreateEndAnnotation(self, createEndAnnotation: bool):
        """
        Setter for property: (bool) CreateEndAnnotation
          the flag to indicate whether to create the end annoation of level line or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateStartAnnotation
    ##   the flag to indicate whether to create the start annoation of level line or not.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def CreateStartAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateStartAnnotation
          the flag to indicate whether to create the start annoation of level line or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateStartAnnotation

    ##   the flag to indicate whether to create the start annoation of level line or not.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @CreateStartAnnotation.setter
    def CreateStartAnnotation(self, createStartAnnotation: bool):
        """
        Setter for property: (bool) CreateStartAnnotation
          the flag to indicate whether to create the start annoation of level line or not.  
             
         
        """
        pass
    
    ## Getter for property: (int) SymbolType
    ##   the type of level line end symbol.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def SymbolType(self) -> int:
        """
        Getter for property: (int) SymbolType
          the type of level line end symbol.  
             
         
        """
        pass
    
    ## Setter for property: (int) SymbolType

    ##   the type of level line end symbol.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SymbolType.setter
    def SymbolType(self, symbolType: int):
        """
        Setter for property: (int) SymbolType
          the type of level line end symbol.  
             
         
        """
        pass
    
    ##  Updates the level line color, style, width.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="color"> (int) </param>
    ## <param name="style"> (int) </param>
    ## <param name="width"> (int) </param>
    def UpdateColorStyleWidth(builder: LevelLinePreferencesBuilder, color: int, style: int, width: int) -> None:
        """
         Updates the level line color, style, width.
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a level parts builder for AEC.
##          
## 
##  
##         
##         This builder is used to create level parts in AEC. 
##         
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecLevelPartsBuilder  NXOpen::Features::AECDesignCollection::CreateAecLevelPartsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LevelPartsBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a level parts builder for AEC.
        </summary>
        <remarks>
        This builder is used to create level parts in AEC. 
        </remarks>
        """


    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) Placement
    ##   the placement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Part
    @property
    def Placement(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) Placement
          the placement   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) Placement

    ##   the placement   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Placement.setter
    def Placement(self, placement: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) Placement
          the placement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ReferenceGeometry
    ##   the reference geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ReferenceGeometry(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ReferenceGeometry
          the reference geometry   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a ship section feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::LevelPartsBuilder  NXOpen::Features::AECDesign::LevelPartsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LevelParts(NXOpen.Features.BodyFeature): 
    """ Represents a ship section feature """
    pass


import NXOpen
##   @brief 
##             Represents a level reference builder which can be used by features for AEC Design. 
##              
## 
##  
##             
##             This builder is used to define the level reference.
##             
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LevelReferenceBuilder(NXOpen.Builder): 
    """ <summary>
            Represents a level reference builder which can be used by features for AEC Design. 
            </summary>
            <remarks>
            This builder is used to define the level reference.
            </remarks>
        """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##   the offset distance from the reference level.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
          the offset distance from the reference level.  
             
         
        """
        pass
    
    ## Getter for property: (str) ReferenceLevelName
    ##   the reference level  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ReferenceLevelName(self) -> str:
        """
        Getter for property: (str) ReferenceLevelName
          the reference level  
            
         
        """
        pass
    
    ## Setter for property: (str) ReferenceLevelName

    ##   the reference level  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReferenceLevelName.setter
    def ReferenceLevelName(self, levelName: str):
        """
        Setter for property: (str) ReferenceLevelName
          the reference level  
            
         
        """
        pass
    
import NXOpen
##  Represents a ship section feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::LevelReferenceBuilder  NXOpen::Features::AECDesign::LevelReferenceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LevelReference(NXOpen.NXObject): 
    """ Represents a ship section feature """
    pass


import NXOpen.Features
##  Represents a AEC level feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::LevelBuilder  NXOpen::Features::AECDesign::LevelBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Level(NXOpen.Features.Feature): 
    """ Represents a AEC level feature """
    pass


import NXOpen
## 
##         Represents a @link Features::AECDesign::LibraryManagerBuilder Features::AECDesign::LibraryManagerBuilder@endlink 
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateLibraryManagerBuilder  NXOpen::Features::AECDesignCollection::CreateLibraryManagerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LibraryManagerBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>Features.AECDesign.LibraryManagerBuilder</ja_class>
        """


    ## Getter for property: (@link BaseLibraryItemBuilderList NXOpen.Features.AECDesign.BaseLibraryItemBuilderList@endlink) LibraryItemList
    ##   the base library item detail builder list   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BaseLibraryItemBuilderList
    @property
    def LibraryItemList(self) -> BaseLibraryItemBuilderList:
        """
        Getter for property: (@link BaseLibraryItemBuilderList NXOpen.Features.AECDesign.BaseLibraryItemBuilderList@endlink) LibraryItemList
          the base library item detail builder list   
            
         
        """
        pass
    
    ##  Creates a @link NXOpen::Features::AECDesign::MaterialDataContainerBuilder NXOpen::Features::AECDesign::MaterialDataContainerBuilder@endlink  
    ##  @return dataContainerItem (@link MaterialDataContainerBuilder NXOpen.Features.AECDesign.MaterialDataContainerBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateMaterialDataContainerBuilder(builder: LibraryManagerBuilder) -> MaterialDataContainerBuilder:
        """
         Creates a @link NXOpen::Features::AECDesign::MaterialDataContainerBuilder NXOpen::Features::AECDesign::MaterialDataContainerBuilder@endlink  
         @return dataContainerItem (@link MaterialDataContainerBuilder NXOpen.Features.AECDesign.MaterialDataContainerBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::AECDesign::MaterialLayerDetailBuilder NXOpen::Features::AECDesign::MaterialLayerDetailBuilder@endlink  
    ##  @return layerItem (@link MaterialLayerDetailBuilder NXOpen.Features.AECDesign.MaterialLayerDetailBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateMaterialLayerDetailBuilder(builder: LibraryManagerBuilder) -> MaterialLayerDetailBuilder:
        """
         Creates a @link NXOpen::Features::AECDesign::MaterialLayerDetailBuilder NXOpen::Features::AECDesign::MaterialLayerDetailBuilder@endlink  
         @return layerItem (@link MaterialLayerDetailBuilder NXOpen.Features.AECDesign.MaterialLayerDetailBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::AECDesign::MaterialSectionDetailBuilder NXOpen::Features::AECDesign::MaterialSectionDetailBuilder@endlink  
    ##  @return sectionItem (@link MaterialSectionDetailBuilder NXOpen.Features.AECDesign.MaterialSectionDetailBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateMaterialSectionDetailBuilder(builder: LibraryManagerBuilder) -> MaterialSectionDetailBuilder:
        """
         Creates a @link NXOpen::Features::AECDesign::MaterialSectionDetailBuilder NXOpen::Features::AECDesign::MaterialSectionDetailBuilder@endlink  
         @return sectionItem (@link MaterialSectionDetailBuilder NXOpen.Features.AECDesign.MaterialSectionDetailBuilder@endlink): .
        """
        pass
    
    ##  Exports the current layer definition as the specific xml file. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="filePath"> (str) </param>
    def ExportFromBuilder(builder: LibraryManagerBuilder, filePath: str) -> None:
        """
         Exports the current layer definition as the specific xml file. 
        """
        pass
    
    ##  Find the material detail layer builder or material detail section builder by the name. 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def Find(builder: LibraryManagerBuilder, identifier: str) -> NXOpen.TaggedObject:
        """
         Find the material detail layer builder or material detail section builder by the name. 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Imports the specific layer definition xml file. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="filePath"> (str) </param>
    def ImportToBuilder(builder: LibraryManagerBuilder, filePath: str) -> None:
        """
         Imports the specific layer definition xml file. 
        """
        pass
    
    ##  Merges the specific category from xml file. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="filePath"> (str) </param>
    ## <param name="caterory"> (str) </param>
    def MergeCategoryFromXML(builder: LibraryManagerBuilder, filePath: str, caterory: str) -> None:
        """
         Merges the specific category from xml file. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##   @brief 
##         Represents a longitudinal rebars builder for AEC Design. 
##          
## 
##  
##         
##         This builder is used to create longitudinal rebars feature in AEC Design.
##         
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecLongitudinalRebarsBuilder  NXOpen::Features::AECDesignCollection::CreateAecLongitudinalRebarsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class LongitudinalRebarsBuilder(NXOpen.Features.FeatureBuilder): 
    """ <summary>
        Represents a longitudinal rebars builder for AEC Design. 
        </summary>
        <remarks>
        This builder is used to create longitudinal rebars feature in AEC Design.
        </remarks>
    """


    ## Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) CrossingRebarsFeature
    ##   the select crossing features.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Features.SelectFeatureList
    @property
    def CrossingRebarsFeature(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: (@link NXOpen.Features.SelectFeatureList NXOpen.Features.SelectFeatureList@endlink) CrossingRebarsFeature
          the select crossing features.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##   the diameter.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
          the diameter.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndFacesThickness
    ##   the end faces thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndFacesThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndFacesThickness
          the end faces thickness.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) EndHook
    ##   the end hook.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarHookBlockBuilder
    @property
    def EndHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) EndHook
          the end hook.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) EndLimit
    ##   the end limit.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarLimitBuilder
    @property
    def EndLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) EndLimit
          the end limit.  
             
         
        """
        pass
    
    ## Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
    ##   the materialSection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return MaterialSectionBuilder
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: (@link MaterialSectionBuilder NXOpen.Features.AECDesign.MaterialSectionBuilder@endlink) MaterialSection
          the materialSection.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfRebars
    ##   the number of rebars.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NumberOfRebars(self) -> int:
        """
        Getter for property: (int) NumberOfRebars
          the number of rebars.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfRebars

    ##   the number of rebars.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfRebars.setter
    def NumberOfRebars(self, numberOfRebars: int):
        """
        Setter for property: (int) NumberOfRebars
          the number of rebars.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.PatternOption NXOpen.Features.AECDesign.RebarsBuilder.PatternOption@endlink) PatternSetting
    ##   the space setting.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.PatternOption
    @property
    def PatternSetting(self) -> RebarsBuilder.PatternOption:
        """
        Getter for property: (@link RebarsBuilder.PatternOption NXOpen.Features.AECDesign.RebarsBuilder.PatternOption@endlink) PatternSetting
          the space setting.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.PatternOption NXOpen.Features.AECDesign.RebarsBuilder.PatternOption@endlink) PatternSetting

    ##   the space setting.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @PatternSetting.setter
    def PatternSetting(self, patternSetting: RebarsBuilder.PatternOption):
        """
        Setter for property: (@link RebarsBuilder.PatternOption NXOpen.Features.AECDesign.RebarsBuilder.PatternOption@endlink) PatternSetting
          the space setting.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.LongitudinalCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.LongitudinalCreationMethod@endlink) PlacementMethod
    ##   the placement method used to locate the longitudinal rebars.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.LongitudinalCreationMethod
    @property
    def PlacementMethod(self) -> RebarsBuilder.LongitudinalCreationMethod:
        """
        Getter for property: (@link RebarsBuilder.LongitudinalCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.LongitudinalCreationMethod@endlink) PlacementMethod
          the placement method used to locate the longitudinal rebars.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.LongitudinalCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.LongitudinalCreationMethod@endlink) PlacementMethod

    ##   the placement method used to locate the longitudinal rebars.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @PlacementMethod.setter
    def PlacementMethod(self, placementMethod: RebarsBuilder.LongitudinalCreationMethod):
        """
        Setter for property: (@link RebarsBuilder.LongitudinalCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.LongitudinalCreationMethod@endlink) PlacementMethod
          the placement method used to locate the longitudinal rebars.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectEdge
    ##   the select edge.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectEdge
          the select edge.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SpecifyPoint
    ##   the specify point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SpecifyPoint(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SpecifyPoint
          the specify point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) StartFace
    ##   the start face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def StartFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) StartFace
          the start face.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartFacesThickness
    ##   the start faces thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartFacesThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartFacesThickness
          the start faces thickness.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) StartHook
    ##   the start hook.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarHookBlockBuilder
    @property
    def StartHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: (@link RebarHookBlockBuilder NXOpen.Features.AECDesign.RebarHookBlockBuilder@endlink) StartHook
          the start hook.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) StartLimit
    ##   the start limit.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarLimitBuilder
    @property
    def StartLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: (@link RebarLimitBuilder NXOpen.Features.AECDesign.RebarLimitBuilder@endlink) StartLimit
          the start limit.  
             
         
        """
        pass
    
    ##  Rotate the rebar 90 degrees. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_concrete ("Concrete Design")
    @staticmethod
    def AlternateSolution(builder: LongitudinalRebarsBuilder) -> None:
        """
         Rotate the rebar 90 degrees. 
        """
        pass
    
    ##  Updates referenced columns. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_concrete ("Concrete Design")
    @staticmethod
    def UpdateReferencedRebarBodies(builder: LongitudinalRebarsBuilder) -> None:
        """
         Updates referenced columns. 
        """
        pass
    
import NXOpen.Features
##  Represents a longitudinal rebars feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::LongitudinalRebarsBuilder  NXOpen::Features::AECDesign::LongitudinalRebarsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class LongitudinalRebars(NXOpen.Features.BodyFeature): 
    """ Represents a longitudinal rebars feature """
    pass


import NXOpen
##  The builder to define material data container  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::LibraryManagerBuilder::CreateMaterialDataContainerBuilder  NXOpen::Features::AECDesign::LibraryManagerBuilder::CreateMaterialDataContainerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class MaterialDataContainerBuilder(BaseLibraryItemBuilder): 
    """ The builder to define material data container """


    ## Getter for property: (@link BaseLibraryItemBuilderList NXOpen.Features.AECDesign.BaseLibraryItemBuilderList@endlink) ContainerItemList
    ##   the list of base library item detail builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return BaseLibraryItemBuilderList
    @property
    def ContainerItemList(self) -> BaseLibraryItemBuilderList:
        """
        Getter for property: (@link BaseLibraryItemBuilderList NXOpen.Features.AECDesign.BaseLibraryItemBuilderList@endlink) ContainerItemList
          the list of base library item detail builder   
            
         
        """
        pass
    
    ##  Finds the material data container builder by the name. 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def Find(builder: MaterialDataContainerBuilder, identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the material data container builder by the name. 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Initializes the material data container builder. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedLibraryItem"> (@link BaseLibraryItemBuilder NXOpen.Features.AECDesign.BaseLibraryItemBuilder@endlink) </param>
    def InitializeFromBuilder(builder: MaterialDataContainerBuilder, selectedLibraryItem: BaseLibraryItemBuilder) -> None:
        """
         Initializes the material data container builder. 
        """
        pass
    
    ##  Sets the material data container builder name and category 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  Journal identifier of the object 
    def SetNameAndCategory(builder: MaterialDataContainerBuilder, name: str, category: str) -> None:
        """
         Sets the material data container builder name and category 
        """
        pass
    
import NXOpen
##  The builder to define material layer detail  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::LibraryManagerBuilder::CreateMaterialLayerDetailBuilder  NXOpen::Features::AECDesign::LibraryManagerBuilder::CreateMaterialLayerDetailBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class MaterialLayerDetailBuilder(BaseLibraryItemBuilder): 
    """ The builder to define material layer detail """


    ##  Creates a @link NXOpen::Features::AECDesign::MaterialLayerDetailItemBuilder NXOpen::Features::AECDesign::MaterialLayerDetailItemBuilder@endlink  
    ##  @return layerItem (@link MaterialLayerDetailItemBuilder NXOpen.Features.AECDesign.MaterialLayerDetailItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateMaterialLayerDetailItemBuilder(builder: MaterialLayerDetailBuilder) -> MaterialLayerDetailItemBuilder:
        """
         Creates a @link NXOpen::Features::AECDesign::MaterialLayerDetailItemBuilder NXOpen::Features::AECDesign::MaterialLayerDetailItemBuilder@endlink  
         @return layerItem (@link MaterialLayerDetailItemBuilder NXOpen.Features.AECDesign.MaterialLayerDetailItemBuilder@endlink): .
        """
        pass
    
    ##  Finds the material detail layer item builder by the name. 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def Find(builder: MaterialLayerDetailBuilder, identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the material detail layer item builder by the name. 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Init the material detail layer item builder. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedLibraryItem"> (@link BaseLibraryItemBuilder NXOpen.Features.AECDesign.BaseLibraryItemBuilder@endlink) </param>
    def InitFromBuilder(builder: MaterialLayerDetailBuilder, selectedLibraryItem: BaseLibraryItemBuilder) -> None:
        """
         Init the material detail layer item builder. 
        """
        pass
    
    ##  Sets the material layer detail builder name and category 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  Journal identifier of the object 
    def SetNameAndCategory(builder: MaterialLayerDetailBuilder, name: str, category: str) -> None:
        """
         Sets the material layer detail builder name and category 
        """
        pass
    
import NXOpen
## 
##         Represents a BaseLibraryItemBuilder.
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::MaterialLayerDetailBuilder::CreateMaterialLayerDetailItemBuilder  NXOpen::Features::AECDesign::MaterialLayerDetailBuilder::CreateMaterialLayerDetailItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class MaterialLayerDetailItemBuilder(BaseDetailItemBuilder): 
    """
        Represents a BaseLibraryItemBuilder.
        """


    ## Getter for property: (bool) Primary
    ##   the primary   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def Primary(self) -> bool:
        """
        Getter for property: (bool) Primary
          the primary   
            
         
        """
        pass
    
    ## Setter for property: (bool) Primary

    ##   the primary   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Primary.setter
    def Primary(self, primary: bool):
        """
        Setter for property: (bool) Primary
          the primary   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness   
            
         
        """
        pass
    
import NXOpen
##   @brief 
##             Represents a specific layer builder which can be used by features for AEC Design. 
##              
## 
##  
##             
##             This builder is used to define the layer.
##             
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class MaterialLayersBuilder(NXOpen.Builder): 
    """ <summary>
            Represents a specific layer builder which can be used by features for AEC Design. 
            </summary>
            <remarks>
            This builder is used to define the layer.
            </remarks>
        """


    ## Getter for property: (str) Layer
    ##   the layer name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Layer(self) -> str:
        """
        Getter for property: (str) Layer
          the layer name  
            
         
        """
        pass
    
    ## Setter for property: (str) Layer

    ##   the layer name  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Layer.setter
    def Layer(self, layerName: str):
        """
        Setter for property: (str) Layer
          the layer name  
            
         
        """
        pass
    
import NXOpen
##  Represents a ship section feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::MaterialLayersBuilder  NXOpen::Features::AECDesign::MaterialLayersBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class MaterialLayer(NXOpen.NXObject): 
    """ Represents a ship section feature """
    pass


import NXOpen
##   @brief 
##             Represents a specific section builder which can be used by features for AEC Design. 
##              
## 
##  
##             
##             This builder is used to define the section.
##             
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class MaterialSectionBuilder(NXOpen.Builder): 
    """ <summary>
            Represents a specific section builder which can be used by features for AEC Design. 
            </summary>
            <remarks>
            This builder is used to define the section.
            </remarks>
        """


    ## Getter for property: (str) SectionName
    ##   the section name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def SectionName(self) -> str:
        """
        Getter for property: (str) SectionName
          the section name  
            
         
        """
        pass
    
    ## Setter for property: (str) SectionName

    ##   the section name  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SectionName.setter
    def SectionName(self, sectionName: str):
        """
        Setter for property: (str) SectionName
          the section name  
            
         
        """
        pass
    
import NXOpen
##  The builder to define material section detail  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::LibraryManagerBuilder::CreateMaterialSectionDetailBuilder  NXOpen::Features::AECDesign::LibraryManagerBuilder::CreateMaterialSectionDetailBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class MaterialSectionDetailBuilder(BaseLibraryItemBuilder): 
    """ The builder to define material section detail """


    ##  Creates a @link NXOpen::Features::AECDesign::MaterialSectionDetailItemBuilder NXOpen::Features::AECDesign::MaterialSectionDetailItemBuilder@endlink  
    ##  @return sectionItem (@link MaterialSectionDetailItemBuilder NXOpen.Features.AECDesign.MaterialSectionDetailItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateMaterialSectionDetailItemBuilder(builder: MaterialSectionDetailBuilder) -> MaterialSectionDetailItemBuilder:
        """
         Creates a @link NXOpen::Features::AECDesign::MaterialSectionDetailItemBuilder NXOpen::Features::AECDesign::MaterialSectionDetailItemBuilder@endlink  
         @return sectionItem (@link MaterialSectionDetailItemBuilder NXOpen.Features.AECDesign.MaterialSectionDetailItemBuilder@endlink): .
        """
        pass
    
    ##  Finds the material detail section item builder by the name. 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def Find(builder: MaterialSectionDetailBuilder, identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the material detail section item builder by the name. 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Init the material detail section item builder. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedLibraryItem"> (@link BaseLibraryItemBuilder NXOpen.Features.AECDesign.BaseLibraryItemBuilder@endlink) </param>
    def InitFromBuilder(builder: MaterialSectionDetailBuilder, selectedLibraryItem: BaseLibraryItemBuilder) -> None:
        """
         Init the material detail section item builder. 
        """
        pass
    
    ##  Sets the material section detail builder name and category 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  Journal identifier of the object 
    def SetNameAndCategory(builder: MaterialSectionDetailBuilder, name: str, category: str) -> None:
        """
         Sets the material section detail builder name and category 
        """
        pass
    
## 
##         Represents a BaseLibraryItemBuilder.
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::MaterialSectionDetailBuilder::CreateMaterialSectionDetailItemBuilder  NXOpen::Features::AECDesign::MaterialSectionDetailBuilder::CreateMaterialSectionDetailItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class MaterialSectionDetailItemBuilder(BaseDetailItemBuilder): 
    """
        Represents a BaseLibraryItemBuilder.
        """


    ## Getter for property: (@link SectionFeatureSpreadsheetBuilder NXOpen.Features.AECDesign.SectionFeatureSpreadsheetBuilder@endlink) SectionStock
    ##   the section stock  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return SectionFeatureSpreadsheetBuilder
    @property
    def SectionStock(self) -> SectionFeatureSpreadsheetBuilder:
        """
        Getter for property: (@link SectionFeatureSpreadsheetBuilder NXOpen.Features.AECDesign.SectionFeatureSpreadsheetBuilder@endlink) SectionStock
          the section stock  
            
         
        """
        pass
    
import NXOpen
##  Represents a ship section feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::MaterialSectionBuilder  NXOpen::Features::AECDesign::MaterialSectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class MaterialSection(NXOpen.NXObject): 
    """ Represents a ship section feature """
    pass


import NXOpen
## 
##         Represents a @link NXOpen::Features::AECDesign::MaterialVisualItemBuilder NXOpen::Features::AECDesign::MaterialVisualItemBuilder@endlink  builder. This builder is used to
##         change the material color and studio material name for visualization. 
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class MaterialVisualItemBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.Features.AECDesign.MaterialVisualItemBuilder</ja_class> builder. This builder is used to
        change the material color and studio material name for visualization. 
        """


    ## Getter for property: (int) Color
    ##   the color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
          the color   
            
         
        """
        pass
    
    ## Setter for property: (int) Color

    ##   the color   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
          the color   
            
         
        """
        pass
    
    ## Getter for property: (str) StudioMaterialName
    ##   the name of the studio material to apply   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def StudioMaterialName(self) -> str:
        """
        Getter for property: (str) StudioMaterialName
          the name of the studio material to apply   
            
         
        """
        pass
    
    ## Setter for property: (str) StudioMaterialName

    ##   the name of the studio material to apply   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StudioMaterialName.setter
    def StudioMaterialName(self, studioMaterialName: str):
        """
        Setter for property: (str) StudioMaterialName
          the name of the studio material to apply   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a @link Features::AECDesign::Opening Features::AECDesign::Opening@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecOpeningBuilder  NXOpen::Features::AECDesignCollection::CreateAecOpeningBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class OpeningBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>Features.AECDesign.Opening</ja_class> builder
    """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CustomShape
    ##   the custom shape   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def CustomShape(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CustomShape
          the custom shape   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OpeningPenetrationDepth
    ##   the depth of opening   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OpeningPenetrationDepth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OpeningPenetrationDepth
          the depth of opening   
            
         
        """
        pass
    
    ## Getter for property: (@link ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
    ##   the direction used to project the custom shape curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ProjectionOptions
    @property
    def ProjectionDirection(self) -> ProjectionOptions:
        """
        Getter for property: (@link ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
          the direction used to project the custom shape curves   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectTargetFaces
    ##   the select target faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectTargetFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectTargetFaces
          the select target faces   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a opening feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::OpeningBuilder  NXOpen::Features::AECDesign::OpeningBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Opening(NXOpen.Features.BodyFeature): 
    """ Represents a opening feature """
    pass


import NXOpen
## 
##             Represents a @link Features::AECDesign::PickCurveBuilder Features::AECDesign::PickCurveBuilder@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreatePickCurveBuilder  NXOpen::Features::AECDesignCollection::CreatePickCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PickCurveBuilder(NXOpen.Builder): 
    """
            Represents a <ja_class>Features.AECDesign.PickCurveBuilder</ja_class> builder
        """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurvesToSelect
    ##   the selected curve list  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def CurvesToSelect(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurvesToSelect
          the selected curve list  
            
         
        """
        pass
    
    ##  Set the state of multi-segment
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="bMultiSegment"> (bool) </param>
    def SetMultiSegment(builder: PickCurveBuilder, bMultiSegment: bool) -> None:
        """
         Set the state of multi-segment
        """
        pass
    
import NXOpen
import NXOpen.Features.Industry
##   @brief 
##         Represents a project setup builder for AEC.
##          
## 
##  
##         
##         This builder is used to setup project in AEC. 
##         
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecProjectSetupBuilder  NXOpen::Features::AECDesignCollection::CreateAecProjectSetupBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ProjectLoadFromBuilder.LoadFrom </term> <description> 
##  
## CustomerDefaults </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class ProjectSetupBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a project setup builder for AEC.
        </summary>
        <remarks>
        This builder is used to setup project in AEC. 
        </remarks>
        """


    ## Getter for property: (bool) IsNewStructure
    ##   the flag to indicate whether it is new structure or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def IsNewStructure(self) -> bool:
        """
        Getter for property: (bool) IsNewStructure
          the flag to indicate whether it is new structure or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsNewStructure

    ##   the flag to indicate whether it is new structure or not.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @IsNewStructure.setter
    def IsNewStructure(self, isNewStructure: bool):
        """
        Setter for property: (bool) IsNewStructure
          the flag to indicate whether it is new structure or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsSaveAsSharePart
    ##   the flag to indicate whether it is to save as the shared part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def IsSaveAsSharePart(self) -> bool:
        """
        Getter for property: (bool) IsSaveAsSharePart
          the flag to indicate whether it is to save as the shared part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsSaveAsSharePart

    ##   the flag to indicate whether it is to save as the shared part.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @IsSaveAsSharePart.setter
    def IsSaveAsSharePart(self, isSaveAsSharePart: bool):
        """
        Setter for property: (bool) IsSaveAsSharePart
          the flag to indicate whether it is to save as the shared part.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.Industry.SelectProjectLoadFromBuilder NXOpen.Features.Industry.SelectProjectLoadFromBuilder@endlink) ProjectLoadFromBuilder
    ##   the projectLoadFromBuilder.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Features.Industry.SelectProjectLoadFromBuilder
    @property
    def ProjectLoadFromBuilder(self) -> NXOpen.Features.Industry.SelectProjectLoadFromBuilder:
        """
        Getter for property: (@link NXOpen.Features.Industry.SelectProjectLoadFromBuilder NXOpen.Features.Industry.SelectProjectLoadFromBuilder@endlink) ProjectLoadFromBuilder
          the projectLoadFromBuilder.  
            
         
        """
        pass
    
    ## Getter for property: (str) ProjectName
    ##   the project name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
          the project name   
            
         
        """
        pass
    
    ## Setter for property: (str) ProjectName

    ##   the project name   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ProjectName.setter
    def ProjectName(self, projectName: str):
        """
        Setter for property: (str) ProjectName
          the project name   
            
         
        """
        pass
    
    ##  Gets the structure root node. 
    ##  @return rootNode (@link NXOpen.Features.Industry.ProjectStructureNode NXOpen.Features.Industry.ProjectStructureNode@endlink):  the root structure node. .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRootNode(builder: ProjectSetupBuilder) -> NXOpen.Features.Industry.ProjectStructureNode:
        """
         Gets the structure root node. 
         @return rootNode (@link NXOpen.Features.Industry.ProjectStructureNode NXOpen.Features.Industry.ProjectStructureNode@endlink):  the root structure node. .
        """
        pass
    
import NXOpen
##   @brief 
##             Represents a rebar hook block builder which can be used by features for AEC Design. 
##              
## 
##  
##             
##             This builder is used to define the rebar hook block.
##             
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RebarHookBlockBuilder(NXOpen.Builder): 
    """ <summary>
            Represents a rebar hook block builder which can be used by features for AEC Design. 
            </summary>
            <remarks>
            This builder is used to define the rebar hook block.
            </remarks>
        """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookAngle
    ##   the hook angle.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HookAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookAngle
          the hook angle.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookLength
    ##   the hook length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HookLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookLength
          the hook length.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookOffset
    ##   the hook offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HookOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookOffset
          the hook offset.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.HookOffsetOption NXOpen.Features.AECDesign.RebarsBuilder.HookOffsetOption@endlink) HookOffsetType
    ##   the hook offset type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.HookOffsetOption
    @property
    def HookOffsetType(self) -> RebarsBuilder.HookOffsetOption:
        """
        Getter for property: (@link RebarsBuilder.HookOffsetOption NXOpen.Features.AECDesign.RebarsBuilder.HookOffsetOption@endlink) HookOffsetType
          the hook offset type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.HookOffsetOption NXOpen.Features.AECDesign.RebarsBuilder.HookOffsetOption@endlink) HookOffsetType

    ##   the hook offset type.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HookOffsetType.setter
    def HookOffsetType(self, hookOffsetType: RebarsBuilder.HookOffsetOption):
        """
        Setter for property: (@link RebarsBuilder.HookOffsetOption NXOpen.Features.AECDesign.RebarsBuilder.HookOffsetOption@endlink) HookOffsetType
          the hook offset type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookRadius
    ##   the hook radius.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HookRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HookRadius
          the hook radius.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.HookOption NXOpen.Features.AECDesign.RebarsBuilder.HookOption@endlink) HookType
    ##   the hook type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.HookOption
    @property
    def HookType(self) -> RebarsBuilder.HookOption:
        """
        Getter for property: (@link RebarsBuilder.HookOption NXOpen.Features.AECDesign.RebarsBuilder.HookOption@endlink) HookType
          the hook type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.HookOption NXOpen.Features.AECDesign.RebarsBuilder.HookOption@endlink) HookType

    ##   the hook type.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HookType.setter
    def HookType(self, hookType: RebarsBuilder.HookOption):
        """
        Setter for property: (@link RebarsBuilder.HookOption NXOpen.Features.AECDesign.RebarsBuilder.HookOption@endlink) HookType
          the hook type.  
             
         
        """
        pass
    
import NXOpen
##  Represents an aecdesign rebar hook block feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::RebarHookBlockBuilder  NXOpen::Features::AECDesign::RebarHookBlockBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RebarHookBlock(NXOpen.NXObject): 
    """ Represents an aecdesign rebar hook block feature """
    pass


import NXOpen
##   @brief 
##             Represents a rebar limit builder which can be used by features for AEC Design. 
##              
## 
##  
##             
##             This builder is used to define the rebar limit.
##             
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RebarLimitBuilder(NXOpen.Builder): 
    """ <summary>
            Represents a rebar limit builder which can be used by features for AEC Design. 
            </summary>
            <remarks>
            This builder is used to define the rebar limit.
            </remarks>
        """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LimitDistance
    ##   the limit distance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LimitDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LimitDistance
          the limit distance.  
             
         
        """
        pass
    
    ## Getter for property: (@link RebarsBuilder.LimitOption NXOpen.Features.AECDesign.RebarsBuilder.LimitOption@endlink) LimitType
    ##   the limit type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RebarsBuilder.LimitOption
    @property
    def LimitType(self) -> RebarsBuilder.LimitOption:
        """
        Getter for property: (@link RebarsBuilder.LimitOption NXOpen.Features.AECDesign.RebarsBuilder.LimitOption@endlink) LimitType
          the limit type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RebarsBuilder.LimitOption NXOpen.Features.AECDesign.RebarsBuilder.LimitOption@endlink) LimitType

    ##   the limit type.  
    ##      
    ##  
    ## Setter License requirements: nx_concrete ("Concrete Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LimitType.setter
    def LimitType(self, limitType: RebarsBuilder.LimitOption):
        """
        Setter for property: (@link RebarsBuilder.LimitOption NXOpen.Features.AECDesign.RebarsBuilder.LimitOption@endlink) LimitType
          the limit type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectTarget
    ##   the select target   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectTarget(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectTarget
          the select target   
            
         
        """
        pass
    
import NXOpen
##  Represents an aecdesign rebar limit feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::RebarLimitBuilder  NXOpen::Features::AECDesign::RebarLimitBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RebarLimit(NXOpen.NXObject): 
    """ Represents an aecdesign rebar limit feature """
    pass


import NXOpen
## 
##         Represents a RebarsBuilder.
##          <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RebarsBuilder(NXOpen.Builder): 
    """
        Represents a RebarsBuilder.
        """


    ##  method used to create the support crossing rebar feature. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Rectangular</term><description> 
    ## </description> </item><item><term> 
    ## CylindricalSpiral</term><description> 
    ## </description> </item><item><term> 
    ## CylindricalCircular</term><description> 
    ## </description> </item></list>
    class CrossingCreationMethod(Enum):
        """
        Members Include: <Rectangular> <CylindricalSpiral> <CylindricalCircular>
        """
        Rectangular: int
        CylindricalSpiral: int
        CylindricalCircular: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.CrossingCreationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represent hook offset type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CoverThickness</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class HookOffsetOption(Enum):
        """
        Members Include: <CoverThickness> <UserDefined>
        """
        CoverThickness: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.HookOffsetOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represent hook type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Degrees90</term><description> 
    ## </description> </item><item><term> 
    ## Degrees135</term><description> 
    ## </description> </item><item><term> 
    ## Degrees180</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class HookOption(Enum):
        """
        Members Include: <NotSet> <Degrees90> <Degrees135> <Degrees180> <UserDefined>
        """
        NotSet: int
        Degrees90: int
        Degrees135: int
        Degrees180: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.HookOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represent limit types.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Value</term><description> 
    ## </description> </item><item><term> 
    ## SymmetricValue</term><description> 
    ## </description> </item><item><term> 
    ## UntilNext</term><description> 
    ## </description> </item><item><term> 
    ## UntilSelected</term><description> 
    ## </description> </item><item><term> 
    ## UntilExtended</term><description> 
    ## </description> </item><item><term> 
    ## OffsetFromSelected</term><description> 
    ## </description> </item></list>
    class LimitOption(Enum):
        """
        Members Include: <Value> <SymmetricValue> <UntilNext> <UntilSelected> <UntilExtended> <OffsetFromSelected>
        """
        Value: int
        SymmetricValue: int
        UntilNext: int
        UntilSelected: int
        UntilExtended: int
        OffsetFromSelected: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.LimitOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  method used to create the support longitudinal rebar feature. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WithinRectangular</term><description> 
    ## </description> </item><item><term> 
    ## WithinCylindrical</term><description> 
    ## </description> </item><item><term> 
    ## OnPoint</term><description> 
    ## </description> </item></list>
    class LongitudinalCreationMethod(Enum):
        """
        Members Include: <WithinRectangular> <WithinCylindrical> <OnPoint>
        """
        WithinRectangular: int
        WithinCylindrical: int
        OnPoint: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.LongitudinalCreationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represent distribution pattern setting.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FourBarAround</term><description> 
    ## </description> </item><item><term> 
    ## SixBarsMirrored</term><description> 
    ## </description> </item><item><term> 
    ## EightBarsAround</term><description> 
    ## </description> </item><item><term> 
    ## EightBarsMirrored</term><description> 
    ## </description> </item><item><term> 
    ## TenBarsMirrored</term><description> 
    ## </description> </item><item><term> 
    ## TwelveBarsMirrored</term><description> 
    ## </description> </item></list>
    class PatternOption(Enum):
        """
        Members Include: <FourBarAround> <SixBarsMirrored> <EightBarsAround> <EightBarsMirrored> <TenBarsMirrored> <TwelveBarsMirrored>
        """
        FourBarAround: int
        SixBarsMirrored: int
        EightBarsAround: int
        EightBarsMirrored: int
        TenBarsMirrored: int
        TwelveBarsMirrored: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.PatternOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represent distribution spacing setting.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EquallyDistributed</term><description> 
    ## </description> </item><item><term> 
    ## ExactSpacing</term><description> 
    ## </description> </item><item><term> 
    ## ExactSpacingFirst</term><description> 
    ## </description> </item><item><term> 
    ## ExactSpacingLast</term><description> 
    ## </description> </item><item><term> 
    ## ExactSpacingMiddle</term><description> 
    ## </description> </item><item><term> 
    ## ExactSpacingFirstAndLast</term><description> 
    ## </description> </item></list>
    class SpacingOption(Enum):
        """
        Members Include: <EquallyDistributed> <ExactSpacing> <ExactSpacingFirst> <ExactSpacingLast> <ExactSpacingMiddle> <ExactSpacingFirstAndLast>
        """
        EquallyDistributed: int
        ExactSpacing: int
        ExactSpacingFirst: int
        ExactSpacingLast: int
        ExactSpacingMiddle: int
        ExactSpacingFirstAndLast: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.SpacingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class RoofBoundaryListItemBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: RoofBoundaryListItemBuilderList, objects: List[RoofBoundaryListItemBuilder]) -> None:
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
    def Append(self, object_list: RoofBoundaryListItemBuilderList, objectValue: RoofBoundaryListItemBuilder) -> None:
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
    def Clear(object_list: RoofBoundaryListItemBuilderList) -> None:
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
    def ClearIndex(object_list: RoofBoundaryListItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: RoofBoundaryListItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: RoofBoundaryListItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: RoofBoundaryListItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: RoofBoundaryListItemBuilderList, obj: RoofBoundaryListItemBuilder) -> None:
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
    def Erase(self, object_list: RoofBoundaryListItemBuilderList, obj: RoofBoundaryListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: RoofBoundaryListItemBuilderList, obj: RoofBoundaryListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link RoofBoundaryListItemBuilder NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: RoofBoundaryListItemBuilderList, index: int) -> RoofBoundaryListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link RoofBoundaryListItemBuilder NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link RoofBoundaryListItemBuilder List[NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: RoofBoundaryListItemBuilderList) -> List[RoofBoundaryListItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link RoofBoundaryListItemBuilder List[NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: RoofBoundaryListItemBuilderList, location: int, objectValue: RoofBoundaryListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: RoofBoundaryListItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: RoofBoundaryListItemBuilderList, index: int) -> None:
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
    def SetContents(object_list: RoofBoundaryListItemBuilderList, objects: List[RoofBoundaryListItemBuilder]) -> None:
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
    def Swap(self, object_list: RoofBoundaryListItemBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: RoofBoundaryListItemBuilderList, object1: RoofBoundaryListItemBuilder, object2: RoofBoundaryListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  roof boundary list item builder  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::RoofBuilder::CreateRoofBoundaryListItemBuilder  NXOpen::Features::AECDesign::RoofBuilder::CreateRoofBoundaryListItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class RoofBoundaryListItemBuilder(NXOpen.TaggedObject): 
    """ roof boundary list item builder """


    ##  Settings of the roof extension options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OverhangType</term><description> 
    ## </description> </item><item><term> 
    ## OffsetType</term><description> 
    ## </description> </item></list>
    class ExtensionOption(Enum):
        """
        Members Include: <OverhangType> <OffsetType>
        """
        OverhangType: int
        OffsetType: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RoofBoundaryListItemBuilder.ExtensionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BoundaryCurve
    ##   the boundary curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def BoundaryCurve(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BoundaryCurve
          the boundary curve   
            
         
        """
        pass
    
    ## Getter for property: (str) BoundaryItemName
    ##   the boundary item name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def BoundaryItemName(self) -> str:
        """
        Getter for property: (str) BoundaryItemName
          the boundary item name   
            
         
        """
        pass
    
    ## Setter for property: (str) BoundaryItemName

    ##   the boundary item name   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @BoundaryItemName.setter
    def BoundaryItemName(self, boundaryItemName: str):
        """
        Setter for property: (str) BoundaryItemName
          the boundary item name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDim
    ##   the extension dim   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExtensionDim(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExtensionDim
          the extension dim   
            
         
        """
        pass
    
    ## Getter for property: (@link RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder.ExtensionOption@endlink) ExtensionType
    ##   the roof extension type.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return RoofBoundaryListItemBuilder.ExtensionOption
    @property
    def ExtensionType(self) -> RoofBoundaryListItemBuilder.ExtensionOption:
        """
        Getter for property: (@link RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder.ExtensionOption@endlink) ExtensionType
          the roof extension type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder.ExtensionOption@endlink) ExtensionType

    ##   the roof extension type.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ExtensionType.setter
    def ExtensionType(self, extensionType: RoofBoundaryListItemBuilder.ExtensionOption):
        """
        Setter for property: (@link RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder.ExtensionOption@endlink) ExtensionType
          the roof extension type.  
             
         
        """
        pass
    
    ## Getter for property: (@link BIMSlopeBuilder NXOpen.Features.AECDesign.BIMSlopeBuilder@endlink) Slope
    ##   the BIM slope   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BIMSlopeBuilder
    @property
    def Slope(self) -> BIMSlopeBuilder:
        """
        Getter for property: (@link BIMSlopeBuilder NXOpen.Features.AECDesign.BIMSlopeBuilder@endlink) Slope
          the BIM slope   
            
         
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a roof builder for AEC.
##          
## 
##  
##         
##         This builder is used to roof in AEC. 
##         
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecRoofBuilder  NXOpen::Features::AECDesignCollection::CreateAecRoofBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class RoofBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a roof builder for AEC.
        </summary>
        <remarks>
        This builder is used to roof in AEC. 
        </remarks>
        """


    ##  Settings of the roof top options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FootprintType</term><description> 
    ## </description> </item><item><term> 
    ## ExtrusionType</term><description> 
    ## </description> </item></list>
    class TopOption(Enum):
        """
        Members Include: <FootprintType> <ExtrusionType>
        """
        FootprintType: int
        ExtrusionType: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RoofBuilder.TopOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Boundaries
    ##   the boundaries   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Boundaries(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Boundaries
          the boundaries   
            
         
        """
        pass
    
    ## Getter for property: (@link RoofBoundaryListItemBuilderList NXOpen.Features.AECDesign.RoofBoundaryListItemBuilderList@endlink) BoundaryList
    ##   the list of boundary objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RoofBoundaryListItemBuilderList
    @property
    def BoundaryList(self) -> RoofBoundaryListItemBuilderList:
        """
        Getter for property: (@link RoofBoundaryListItemBuilderList NXOpen.Features.AECDesign.RoofBoundaryListItemBuilderList@endlink) BoundaryList
          the list of boundary objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndLimitDistance
    ##   the end limit distance   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndLimitDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndLimitDistance
          the end limit distance   
            
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
    ##   the level reference  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReference
          the level reference  
            
         
        """
        pass
    
    ## Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
    ##   the layer  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MaterialLayersBuilder
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
          the layer  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##   the offset   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
          the offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OverhangDistance
    ##   the overhang distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OverhangDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OverhangDistance
          the overhang distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartLimitDistance
    ##   the start limit distance   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartLimitDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartLimitDistance
          the start limit distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness   
    ##     
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link RoofBuilder.TopOption NXOpen.Features.AECDesign.RoofBuilder.TopOption@endlink) TopType
    ##   the region option, which defines the plate areas in case of body faces as plate boundary.  
    ##      
    ##  
    ## Getter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RoofBuilder.TopOption
    @property
    def TopType(self) -> RoofBuilder.TopOption:
        """
        Getter for property: (@link RoofBuilder.TopOption NXOpen.Features.AECDesign.RoofBuilder.TopOption@endlink) TopType
          the region option, which defines the plate areas in case of body faces as plate boundary.  
             
         
        """
        pass
    
    ## Setter for property: (@link RoofBuilder.TopOption NXOpen.Features.AECDesign.RoofBuilder.TopOption@endlink) TopType

    ##   the region option, which defines the plate areas in case of body faces as plate boundary.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TopType.setter
    def TopType(self, topType: RoofBuilder.TopOption):
        """
        Setter for property: (@link RoofBuilder.TopOption NXOpen.Features.AECDesign.RoofBuilder.TopOption@endlink) TopType
          the region option, which defines the plate areas in case of body faces as plate boundary.  
             
         
        """
        pass
    
    ##  The roof boundary item create function
    ##  @return roofBoundaryListItemBuilder (@link RoofBoundaryListItemBuilder NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateRoofBoundaryListItemBuilder(builder: RoofBuilder) -> RoofBoundaryListItemBuilder:
        """
         The roof boundary item create function
         @return roofBoundaryListItemBuilder (@link RoofBoundaryListItemBuilder NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder@endlink): .
        """
        pass
    
import NXOpen.Features
##  Represents an roof feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::RoofBuilder  NXOpen::Features::AECDesign::RoofBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Roof(NXOpen.Features.BodyFeature): 
    """ Represents an roof feature """
    pass


import NXOpen
##  The builder to define room attributes 
## 
##   <br>  Created in NX2206.0.0  <br> 

class RoomAttributeListBuilder(NXOpen.TaggedObject): 
    """ The builder to define room attributes """


    ##  
    ##             Sets the specific attribute name and value given the index in the list. 
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="attrName"> (str) </param>
    ## <param name="attrValue"> (str) </param>
    def SetAttribute(builder: RoomAttributeListBuilder, index: int, attrName: str, attrValue: str) -> None:
        """
         
                    Sets the specific attribute name and value given the index in the list. 
                    
        """
        pass
    
    ##   @brief 
    ##             Sets the room purpose. 
    ##              
    ## 
    ##  
    ##             
    ##             If room purpose changes, this will try to reconstruct the attribute list because
    ##             different attributes are pre-defined for different room purposes. 
    ##             
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="roomPurpose"> (str) </param>
    def SetRoomPurpose(builder: RoomAttributeListBuilder, roomPurpose: str) -> None:
        """
          @brief 
                    Sets the room purpose. 
                     
        
         
                    
                    If room purpose changes, this will try to reconstruct the attribute list because
                    different attributes are pre-defined for different room purposes. 
                    
                    
        """
        pass
    
    ##  
    ##             Updates the specific attribute value.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="row"> (int) </param>
    ## <param name="headString"> (str) </param>
    ## <param name="value"> (str) </param>
    def UpdateAttributeValue(builder: RoomAttributeListBuilder, row: int, headString: str, value: str) -> None:
        """
         
                    Updates the specific attribute value.
                    
        """
        pass
    
    ##  
    ##             Updates evaluated attribute value.
    ##             
    ##  @return needUpdateList (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="rowIndex"> (int) </param>
    def UpdateEvaluatdValue(builder: RoomAttributeListBuilder, rowIndex: int) -> bool:
        """
         
                    Updates evaluated attribute value.
                    
         @return needUpdateList (bool): .
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a room builder for aec application.
##          
## 
##  
##         
##         This builder is used to define a room.
##         
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecRoomBuilder  NXOpen::Features::AECDesignCollection::CreateAecRoomBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class RoomBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a room builder for aec application.
        </summary>
        <remarks>
        This builder is used to define a room.
        </remarks>
        """


    ## Getter for property: (bool) Associativity
    ##   the room label associativity with floor face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def Associativity(self) -> bool:
        """
        Getter for property: (bool) Associativity
          the room label associativity with floor face   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associativity

    ##   the room label associativity with floor face   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Associativity.setter
    def Associativity(self, associativity: bool):
        """
        Setter for property: (bool) Associativity
          the room label associativity with floor face   
            
         
        """
        pass
    
    ## Getter for property: (@link RoomAttributeListBuilder NXOpen.Features.AECDesign.RoomAttributeListBuilder@endlink) AttributeList
    ##    @brief  the room attribute list.  
    ##     
    ## 
    ##  
    ##             
    ##                 The room attributes defines attributes those are applied to the room component and body.
    ##                
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RoomAttributeListBuilder
    @property
    def AttributeList(self) -> RoomAttributeListBuilder:
        """
        Getter for property: (@link RoomAttributeListBuilder NXOpen.Features.AECDesign.RoomAttributeListBuilder@endlink) AttributeList
           @brief  the room attribute list.  
            
        
         
                    
                        The room attributes defines attributes those are applied to the room component and body.
                       
         
        """
        pass
    
    ## Getter for property: (@link RoomFaceListItemBuilderList NXOpen.Features.AECDesign.RoomFaceListItemBuilderList@endlink) FaceList
    ##   the list of room face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return RoomFaceListItemBuilderList
    @property
    def FaceList(self) -> RoomFaceListItemBuilderList:
        """
        Getter for property: (@link RoomFaceListItemBuilderList NXOpen.Features.AECDesign.RoomFaceListItemBuilderList@endlink) FaceList
          the list of room face   
            
         
        """
        pass
    
    ## Getter for property: (@link ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
    ##   the projection direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ProjectionOptions
    @property
    def ProjectionDirection(self) -> ProjectionOptions:
        """
        Getter for property: (@link ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
          the projection direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RoomColor
    ##   the color to be assigned to the created room body.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def RoomColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RoomColor
          the color to be assigned to the created room body.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RoomColor

    ##   the color to be assigned to the created room body.  
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RoomColor.setter
    def RoomColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RoomColor
          the color to be assigned to the created room body.  
            
         
        """
        pass
    
    ## Getter for property: (str) RoomName
    ##   the room name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def RoomName(self) -> str:
        """
        Getter for property: (str) RoomName
          the room name   
            
         
        """
        pass
    
    ## Setter for property: (str) RoomName

    ##   the room name   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RoomName.setter
    def RoomName(self, roomName: str):
        """
        Setter for property: (str) RoomName
          the room name   
            
         
        """
        pass
    
    ##  The room face item create function
    ##  @return roomFaceListItemBuilder (@link RoomFaceListItemBuilder NXOpen.Features.AECDesign.RoomFaceListItemBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateRoomFaceListItemBuilder(builder: RoomBuilder) -> RoomFaceListItemBuilder:
        """
         The room face item create function
         @return roomFaceListItemBuilder (@link RoomFaceListItemBuilder NXOpen.Features.AECDesign.RoomFaceListItemBuilder@endlink): .
        """
        pass
    
    ##  Evaluates room attributes. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="bUpdateRoomAreaAndVolume"> (bool) </param>
    def EvaluateAttributes(builder: RoomBuilder, bUpdateRoomAreaAndVolume: bool) -> None:
        """
         Evaluates room attributes. 
        """
        pass
    
    ##  Gets the created room bodies. 
    ##  @return createdRoomBodies (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def GetCreatedRoomBodies(builder: RoomBuilder) -> List[NXOpen.TaggedObject]:
        """
         Gets the created room bodies. 
         @return createdRoomBodies (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  Resets room attributes. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="bUpdateRoomAreaAndVolume"> (bool) </param>
    def ResetAttributes(builder: RoomBuilder, bUpdateRoomAreaAndVolume: bool) -> None:
        """
         Resets room attributes. 
        """
        pass
    
    ##  Updates room ID. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="roomID"> (str) </param>
    def UpdateRoomID(builder: RoomBuilder, roomID: str) -> None:
        """
         Updates room ID. 
        """
        pass
    
    ##  Updates room type which is either creation or adopt to the attribute list builder. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def UpdateTypeForAttributeListBuilder(builder: RoomBuilder) -> None:
        """
         Updates room type which is either creation or adopt to the attribute list builder. 
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class RoomFaceListItemBuilderList(NXOpen.TaggedObject): 
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
    def Append(self, object_list: RoomFaceListItemBuilderList, objects: List[RoomFaceListItemBuilder]) -> None:
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
    def Append(self, object_list: RoomFaceListItemBuilderList, objectValue: RoomFaceListItemBuilder) -> None:
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
    def Clear(object_list: RoomFaceListItemBuilderList) -> None:
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
    def ClearIndex(object_list: RoomFaceListItemBuilderList, delete_idx: int) -> None:
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
    def Clear(object_list: RoomFaceListItemBuilderList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: RoomFaceListItemBuilderList, index: int) -> None:
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
    def Erase(self, object_list: RoomFaceListItemBuilderList, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def Erase(self, object_list: RoomFaceListItemBuilderList, obj: RoomFaceListItemBuilder) -> None:
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
    def Erase(self, object_list: RoomFaceListItemBuilderList, obj: RoomFaceListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
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
    def FindIndex(object_list: RoomFaceListItemBuilderList, obj: RoomFaceListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link RoomFaceListItemBuilder NXOpen.Features.AECDesign.RoomFaceListItemBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ##  index of object to return 
    def FindItem(object_list: RoomFaceListItemBuilderList, index: int) -> RoomFaceListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link RoomFaceListItemBuilder NXOpen.Features.AECDesign.RoomFaceListItemBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link RoomFaceListItemBuilder List[NXOpen.Features.AECDesign.RoomFaceListItemBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContents(object_list: RoomFaceListItemBuilderList) -> List[RoomFaceListItemBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link RoomFaceListItemBuilder List[NXOpen.Features.AECDesign.RoomFaceListItemBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  location at which to insert the object 
    def Insert(object_list: RoomFaceListItemBuilderList, location: int, objectValue: RoomFaceListItemBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToBottom(object_list: RoomFaceListItemBuilderList, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  location of the item 
    def MoveToTop(object_list: RoomFaceListItemBuilderList, index: int) -> None:
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
    def SetContents(object_list: RoomFaceListItemBuilderList, objects: List[RoomFaceListItemBuilder]) -> None:
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
    def Swap(self, object_list: RoomFaceListItemBuilderList, index1: int, index2: int) -> None:
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
    def Swap(self, object_list: RoomFaceListItemBuilderList, object1: RoomFaceListItemBuilder, object2: RoomFaceListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  room face list item builder  <br> To create a new instance of this class, use @link NXOpen::Features::AECDesign::RoomBuilder::CreateRoomFaceListItemBuilder  NXOpen::Features::AECDesign::RoomBuilder::CreateRoomFaceListItemBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class RoomFaceListItemBuilder(NXOpen.Builder): 
    """ room face list item builder """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) DivideCurve
    ##   the divide curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def DivideCurve(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) DivideCurve
          the divide curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Faces
    ##   the face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Faces
          the face   
            
         
        """
        pass
    
    ## Getter for property: (@link ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
    ##   the projection direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ProjectionOptions
    @property
    def ProjectionDirection(self) -> ProjectionOptions:
        """
        Getter for property: (@link ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectionDirection
          the projection direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.RegionPointList NXOpen.RegionPointList@endlink) Regions
    ##   the region   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.RegionPointList
    @property
    def Regions(self) -> NXOpen.RegionPointList:
        """
        Getter for property: (@link NXOpen.RegionPointList NXOpen.RegionPointList@endlink) Regions
          the region   
            
         
        """
        pass
    
    ##  Creates region body 
    ##  @return regionBody (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Body associated with the select region point. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    def CreateRegionBody(builder: RoomFaceListItemBuilder) -> List[NXOpen.TaggedObject]:
        """
         Creates region body 
         @return regionBody (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  Body associated with the select region point. .
        """
        pass
    
    ##  Delete the current region body. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    @staticmethod
    def DeleteRegionBody(builder: RoomFaceListItemBuilder) -> None:
        """
         Delete the current region body. 
        """
        pass
    
    ##  Set the region point.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="targetBody"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    ## <param name="regionPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def SetPointToRegionList(builder: RoomFaceListItemBuilder, targetBody: NXOpen.Body, regionPoint: NXOpen.Point3d) -> None:
        """
         Set the region point.
        """
        pass
    
    ##  Sets the projection direction
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  the projection vector. 
    def SetProjectionDirection(builder: RoomFaceListItemBuilder, projectionType: int, projectionVector: NXOpen.Direction) -> None:
        """
         Sets the projection direction
        """
        pass
    
    ##  Set the points derived from the regions of the sheet, that has the inscribed boundaries, to keep for the final 
    ##           room feature. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ##  Points representing the kept regions. 
    def SetRegionPoints(builder: RoomFaceListItemBuilder, regionPoints: List[NXOpen.Point3d]) -> None:
        """
         Set the points derived from the regions of the sheet, that has the inscribed boundaries, to keep for the final 
                  room feature. 
        """
        pass
    
    ##  Sets room face name. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="roomFaceItemName"> (str) </param>
    def SetRoomFaceItemName(builder: RoomFaceListItemBuilder, roomFaceItemName: str) -> None:
        """
         Sets room face name. 
        """
        pass
    
import NXOpen
##   @brief 
##         Represents a room report builder for aec application.
##          
## 
##  
##         
##         This builder is used to define a room report.
##         
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecRoomReportBuilder  NXOpen::Features::AECDesignCollection::CreateAecRoomReportBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class RoomReportBuilder(NXOpen.Builder): 
    """ <summary>
        Represents a room report builder for aec application.
        </summary>
        <remarks>
        This builder is used to define a room report.
        </remarks>
        """


    ## Getter for property: (str) ReportFile
    ##   the report file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def ReportFile(self) -> str:
        """
        Getter for property: (str) ReportFile
          the report file.  
             
         
        """
        pass
    
    ## Setter for property: (str) ReportFile

    ##   the report file.  
    ##      
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ReportFile.setter
    def ReportFile(self, filename: str):
        """
        Setter for property: (str) ReportFile
          the report file.  
             
         
        """
        pass
    
    ##  Sets the selected level parts. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_bim ("AEC Design")
    ## 
    ## <param name="levelParts"> (@link NXOpen.Part List[NXOpen.Part]@endlink) </param>
    def SetLevelParts(builder: RoomReportBuilder, levelParts: List[NXOpen.Part]) -> None:
        """
         Sets the selected level parts. 
        """
        pass
    
import NXOpen.Features
##  Represents an room feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::RoomBuilder  NXOpen::Features::AECDesign::RoomBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Room(NXOpen.Features.BodyFeature): 
    """ Represents an room feature """
    pass


import NXOpen.Features.Industry
## 
##         Represents a @link NXOpen::Features::AECDesign::SectionFeatureSpreadsheetBuilder NXOpen::Features::AECDesign::SectionFeatureSpreadsheetBuilder@endlink  builder. 
##         It is used to manage the data contained in the ship sketch based steel feature block.
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class SectionFeatureSpreadsheetBuilder(NXOpen.Features.Industry.SectionFeatureSpreadsheetBuilder): 
    """
        Represents a <ja_class>NXOpen.Features.AECDesign.SectionFeatureSpreadsheetBuilder</ja_class> builder. 
        It is used to manage the data contained in the ship sketch based steel feature block.
        """
    pass


import NXOpen
import NXOpen.Features
## 
##         Represents a @link NXOpen::Features::AECDesign::Wall NXOpen::Features::AECDesign::Wall@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateWallBuilder  NXOpen::Features::AECDesignCollection::CreateWallBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Alignment </term> <description> 
##  
## Centerline </description> </item> 
## 
## <item><term> 
##  
## BooleanType </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## Split </term> <description> 
##  
## False </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class WallBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a <ja_class>NXOpen.Features.AECDesign.Wall</ja_class> builder
        """


    ## 
    ##              represent wall alignment options
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Exterior</term><description> 
    ## </description> </item><item><term> 
    ## Interior</term><description> 
    ## </description> </item><item><term> 
    ## Centerline</term><description> 
    ## </description> </item></list>
    class AlignmentOption(Enum):
        """
        Members Include: <Exterior> <Interior> <Centerline>
        """
        Exterior: int
        Interior: int
        Centerline: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> WallBuilder.AlignmentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##              represent booleanl options
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Unite</term><description> 
    ## </description> </item><item><term> 
    ## Trim</term><description> 
    ## </description> </item></list>
    class BooleanOption(Enum):
        """
        Members Include: <NotSet> <Unite> <Trim>
        """
        NotSet: int
        Unite: int
        Trim: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> WallBuilder.BooleanOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link WallBuilder.AlignmentOption NXOpen.Features.AECDesign.WallBuilder.AlignmentOption@endlink) Alignment
    ##   the alignment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return WallBuilder.AlignmentOption
    @property
    def Alignment(self) -> WallBuilder.AlignmentOption:
        """
        Getter for property: (@link WallBuilder.AlignmentOption NXOpen.Features.AECDesign.WallBuilder.AlignmentOption@endlink) Alignment
          the alignment   
            
         
        """
        pass
    
    ## Setter for property: (@link WallBuilder.AlignmentOption NXOpen.Features.AECDesign.WallBuilder.AlignmentOption@endlink) Alignment

    ##   the alignment   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Alignment.setter
    def Alignment(self, alignment: WallBuilder.AlignmentOption):
        """
        Setter for property: (@link WallBuilder.AlignmentOption NXOpen.Features.AECDesign.WallBuilder.AlignmentOption@endlink) Alignment
          the alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) AlternateSolutionPoint
    ##   the intersection points to apply alternate split solution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def AlternateSolutionPoint(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) AlternateSolutionPoint
          the intersection points to apply alternate split solution   
            
         
        """
        pass
    
    ## Getter for property: (@link WallBuilder.BooleanOption NXOpen.Features.AECDesign.WallBuilder.BooleanOption@endlink) BooleanType
    ##   the boolean type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return WallBuilder.BooleanOption
    @property
    def BooleanType(self) -> WallBuilder.BooleanOption:
        """
        Getter for property: (@link WallBuilder.BooleanOption NXOpen.Features.AECDesign.WallBuilder.BooleanOption@endlink) BooleanType
          the boolean type   
            
         
        """
        pass
    
    ## Setter for property: (@link WallBuilder.BooleanOption NXOpen.Features.AECDesign.WallBuilder.BooleanOption@endlink) BooleanType

    ##   the boolean type   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BooleanType.setter
    def BooleanType(self, booleanType: WallBuilder.BooleanOption):
        """
        Setter for property: (@link WallBuilder.BooleanOption NXOpen.Features.AECDesign.WallBuilder.BooleanOption@endlink) BooleanType
          the boolean type   
            
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceBottom
    ##   the bottom level reference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReferenceBottom(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceBottom
          the bottom level reference   
            
         
        """
        pass
    
    ## Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceTop
    ##   the top level reference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return LevelReferenceBuilder
    @property
    def LevelReferenceTop(self) -> LevelReferenceBuilder:
        """
        Getter for property: (@link LevelReferenceBuilder NXOpen.Features.AECDesign.LevelReferenceBuilder@endlink) LevelReferenceTop
          the top level reference   
            
         
        """
        pass
    
    ## Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
    ##   the material layers   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MaterialLayersBuilder
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: (@link MaterialLayersBuilder NXOpen.Features.AECDesign.MaterialLayersBuilder@endlink) MaterialLayers
          the material layers   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##   the offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
          the offset   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseOffsetDirection
    ##   the logic to reverse offset direction or not, true means reversed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ReverseOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseOffsetDirection
          the logic to reverse offset direction or not, true means reversed   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseOffsetDirection

    ##   the logic to reverse offset direction or not, true means reversed   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ReverseOffsetDirection.setter
    def ReverseOffsetDirection(self, reverseOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseOffsetDirection
          the logic to reverse offset direction or not, true means reversed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section
    ##   the section   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section
          the section   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectedBodies
    ##   the selected bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectedBodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectedBodies
          the selected bodies   
            
         
        """
        pass
    
    ## Getter for property: (bool) Split
    ##   the toggle to split wall body itself or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def Split(self) -> bool:
        """
        Getter for property: (bool) Split
          the toggle to split wall body itself or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) Split

    ##   the toggle to split wall body itself or not   
    ##     
    ##  
    ## Setter License requirements: nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Split.setter
    def Split(self, split: bool):
        """
        Setter for property: (bool) Split
          the toggle to split wall body itself or not   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a wall feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::AECDesign::WallBuilder  NXOpen::Features::AECDesign::WallBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Wall(NXOpen.Features.BodyFeature): 
    """ Represents a wall feature """
    pass


## @package NXOpen.Features.AECDesign
## Classes, Enums and Structs under NXOpen.Features.AECDesign namespace

##  @link BeamBuilderHorizontalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilderHorizontalAlignmentTypes @endlink is an alias for @link BeamBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.HorizontalAlignmentTypes@endlink
BeamBuilderHorizontalAlignmentTypes = BeamBuilder.HorizontalAlignmentTypes


##  @link BeamBuilderVerticalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilderVerticalAlignmentTypes @endlink is an alias for @link BeamBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.BeamBuilder.VerticalAlignmentTypes@endlink
BeamBuilderVerticalAlignmentTypes = BeamBuilder.VerticalAlignmentTypes


##  @link BIMClassificationBuilderRequisiteTypes NXOpen.Features.AECDesign.BIMClassificationBuilderRequisiteTypes @endlink is an alias for @link BIMClassificationBuilder.RequisiteTypes NXOpen.Features.AECDesign.BIMClassificationBuilder.RequisiteTypes@endlink
BIMClassificationBuilderRequisiteTypes = BIMClassificationBuilder.RequisiteTypes


##  @link BIMSlopeBuilderSlopeOption NXOpen.Features.AECDesign.BIMSlopeBuilderSlopeOption @endlink is an alias for @link BIMSlopeBuilder.SlopeOption NXOpen.Features.AECDesign.BIMSlopeBuilder.SlopeOption@endlink
BIMSlopeBuilderSlopeOption = BIMSlopeBuilder.SlopeOption


##  @link BuildingElementTrimBuilderBooleanType NXOpen.Features.AECDesign.BuildingElementTrimBuilderBooleanType @endlink is an alias for @link BuildingElementTrimBuilder.BooleanType NXOpen.Features.AECDesign.BuildingElementTrimBuilder.BooleanType@endlink
BuildingElementTrimBuilderBooleanType = BuildingElementTrimBuilder.BooleanType


##  @link ColumnBuilderCreationMethod NXOpen.Features.AECDesign.ColumnBuilderCreationMethod @endlink is an alias for @link ColumnBuilder.CreationMethod NXOpen.Features.AECDesign.ColumnBuilder.CreationMethod@endlink
ColumnBuilderCreationMethod = ColumnBuilder.CreationMethod


##  @link ColumnBuilderHorizontalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilderHorizontalAlignmentTypes @endlink is an alias for @link ColumnBuilder.HorizontalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.HorizontalAlignmentTypes@endlink
ColumnBuilderHorizontalAlignmentTypes = ColumnBuilder.HorizontalAlignmentTypes


##  @link ColumnBuilderRotationType NXOpen.Features.AECDesign.ColumnBuilderRotationType @endlink is an alias for @link ColumnBuilder.RotationType NXOpen.Features.AECDesign.ColumnBuilder.RotationType@endlink
ColumnBuilderRotationType = ColumnBuilder.RotationType


##  @link ColumnBuilderVerticalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilderVerticalAlignmentTypes @endlink is an alias for @link ColumnBuilder.VerticalAlignmentTypes NXOpen.Features.AECDesign.ColumnBuilder.VerticalAlignmentTypes@endlink
ColumnBuilderVerticalAlignmentTypes = ColumnBuilder.VerticalAlignmentTypes


##  @link ExplodeComponentBuilderExplodeScope NXOpen.Features.AECDesign.ExplodeComponentBuilderExplodeScope @endlink is an alias for @link ExplodeComponentBuilder.ExplodeScope NXOpen.Features.AECDesign.ExplodeComponentBuilder.ExplodeScope@endlink
ExplodeComponentBuilderExplodeScope = ExplodeComponentBuilder.ExplodeScope


##  @link GridBuilderTypes NXOpen.Features.AECDesign.GridBuilderTypes @endlink is an alias for @link GridBuilder.Types NXOpen.Features.AECDesign.GridBuilder.Types@endlink
GridBuilderTypes = GridBuilder.Types


##  @link LabellingRoomsBuilderExisingaeclabelType NXOpen.Features.AECDesign.LabellingRoomsBuilderExisingaeclabelType @endlink is an alias for @link LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Features.AECDesign.LabellingRoomsBuilder.ExisingaeclabelType@endlink
LabellingRoomsBuilderExisingaeclabelType = LabellingRoomsBuilder.ExisingaeclabelType


##  @link RebarsBuilderCrossingCreationMethod NXOpen.Features.AECDesign.RebarsBuilderCrossingCreationMethod @endlink is an alias for @link RebarsBuilder.CrossingCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.CrossingCreationMethod@endlink
RebarsBuilderCrossingCreationMethod = RebarsBuilder.CrossingCreationMethod


##  @link RebarsBuilderHookOffsetOption NXOpen.Features.AECDesign.RebarsBuilderHookOffsetOption @endlink is an alias for @link RebarsBuilder.HookOffsetOption NXOpen.Features.AECDesign.RebarsBuilder.HookOffsetOption@endlink
RebarsBuilderHookOffsetOption = RebarsBuilder.HookOffsetOption


##  @link RebarsBuilderHookOption NXOpen.Features.AECDesign.RebarsBuilderHookOption @endlink is an alias for @link RebarsBuilder.HookOption NXOpen.Features.AECDesign.RebarsBuilder.HookOption@endlink
RebarsBuilderHookOption = RebarsBuilder.HookOption


##  @link RebarsBuilderLimitOption NXOpen.Features.AECDesign.RebarsBuilderLimitOption @endlink is an alias for @link RebarsBuilder.LimitOption NXOpen.Features.AECDesign.RebarsBuilder.LimitOption@endlink
RebarsBuilderLimitOption = RebarsBuilder.LimitOption


##  @link RebarsBuilderLongitudinalCreationMethod NXOpen.Features.AECDesign.RebarsBuilderLongitudinalCreationMethod @endlink is an alias for @link RebarsBuilder.LongitudinalCreationMethod NXOpen.Features.AECDesign.RebarsBuilder.LongitudinalCreationMethod@endlink
RebarsBuilderLongitudinalCreationMethod = RebarsBuilder.LongitudinalCreationMethod


##  @link RebarsBuilderPatternOption NXOpen.Features.AECDesign.RebarsBuilderPatternOption @endlink is an alias for @link RebarsBuilder.PatternOption NXOpen.Features.AECDesign.RebarsBuilder.PatternOption@endlink
RebarsBuilderPatternOption = RebarsBuilder.PatternOption


##  @link RebarsBuilderSpacingOption NXOpen.Features.AECDesign.RebarsBuilderSpacingOption @endlink is an alias for @link RebarsBuilder.SpacingOption NXOpen.Features.AECDesign.RebarsBuilder.SpacingOption@endlink
RebarsBuilderSpacingOption = RebarsBuilder.SpacingOption


##  @link RoofBoundaryListItemBuilderExtensionOption NXOpen.Features.AECDesign.RoofBoundaryListItemBuilderExtensionOption @endlink is an alias for @link RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Features.AECDesign.RoofBoundaryListItemBuilder.ExtensionOption@endlink
RoofBoundaryListItemBuilderExtensionOption = RoofBoundaryListItemBuilder.ExtensionOption


##  @link RoofBuilderTopOption NXOpen.Features.AECDesign.RoofBuilderTopOption @endlink is an alias for @link RoofBuilder.TopOption NXOpen.Features.AECDesign.RoofBuilder.TopOption@endlink
RoofBuilderTopOption = RoofBuilder.TopOption


##  @link WallBuilderAlignmentOption NXOpen.Features.AECDesign.WallBuilderAlignmentOption @endlink is an alias for @link WallBuilder.AlignmentOption NXOpen.Features.AECDesign.WallBuilder.AlignmentOption@endlink
WallBuilderAlignmentOption = WallBuilder.AlignmentOption


##  @link WallBuilderBooleanOption NXOpen.Features.AECDesign.WallBuilderBooleanOption @endlink is an alias for @link WallBuilder.BooleanOption NXOpen.Features.AECDesign.WallBuilder.BooleanOption@endlink
WallBuilderBooleanOption = WallBuilder.BooleanOption


