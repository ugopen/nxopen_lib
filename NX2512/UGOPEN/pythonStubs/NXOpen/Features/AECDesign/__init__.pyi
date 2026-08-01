from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Tooling
class AddReusablePartBuilder(NXOpen.Tooling.AddReusablePart): 
    """
        Represents a Features.AECDesign.AddReusablePartBuilder
        """
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReference
         Returns the level reference  
            
         
        """
        pass
    def RotatePart(self, rotationAngle: float, instance: NXOpen.NXObject, index: int) -> None:
        """
         Rotates part by the given angle.
        """
        pass
    def SetPartAttribute(self) -> None:
        """
         Sets reusable part attribute.
        """
        pass
import NXOpen
class AlternateCoverThicknessBuilder(NXOpen.Builder): 
    """ 
        Represents an AlternateCoverThickness builder for AEC Design. 
        
        
        This builder is used to create AlternateCoverThickness Data in AEC Design.
        
    """
    @property
    def AlternateCoverThicknessList(self) -> AlternateCoverThicknessListItemBuilderList:
        """
        Getter for property: ( AlternateCoverThicknessListItemBuilderList NXOpen.Featu) AlternateCoverThicknessList
         Returns the alternate cover thickness list   
            
         
        """
        pass
    def CreateAlternateCoverThicknessListItemBuilder(self) -> AlternateCoverThicknessListItemBuilder:
        """
         The alternate cover thickness item creation function
         Returns alternateCoverThicknessListItemBuilder ( AlternateCoverThicknessListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class AlternateCoverThicknessListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[AlternateCoverThicknessListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: AlternateCoverThicknessListItemBuilder) -> None:
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
    def Erase(self, obj: AlternateCoverThicknessListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: AlternateCoverThicknessListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: AlternateCoverThicknessListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> AlternateCoverThicknessListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( AlternateCoverThicknessListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[AlternateCoverThicknessListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( AlternateCoverThicknessListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: AlternateCoverThicknessListItemBuilder) -> None:
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
    def SetContents(self, objects: List[AlternateCoverThicknessListItemBuilder]) -> None:
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
    def Swap(self, object1: AlternateCoverThicknessListItemBuilder, object2: AlternateCoverThicknessListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class AlternateCoverThicknessListItemBuilder(NXOpen.TaggedObject): 
    """ Alternate Cover Thickness list item builder """
    @property
    def AlternateCoverThicknessDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AlternateCoverThicknessDim
         Returns the alternate cover thickness dim   
            
         
        """
        pass
    @property
    def AlternateCoverThicknessFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) AlternateCoverThicknessFace
         Returns the alternate cover thickness face  
            
         
        """
        pass
import NXOpen
class BaseDetailItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BaseDetailItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BaseDetailItemBuilder) -> None:
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
    def Erase(self, obj: BaseDetailItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BaseDetailItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BaseDetailItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BaseDetailItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BaseDetailItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BaseDetailItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BaseDetailItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BaseDetailItemBuilder) -> None:
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
    def SetContents(self, objects: List[BaseDetailItemBuilder]) -> None:
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
    def Swap(self, object1: BaseDetailItemBuilder, object2: BaseDetailItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BaseDetailItemBuilder(NXOpen.Builder): 
    """
        Represents a BaseDetailItemBuilder.
        """
    @property
    def MaterialLibName(self) -> str:
        """
        Getter for property: (str) MaterialLibName
         Returns the material library Name   
            
         
        """
        pass
    @MaterialLibName.setter
    def MaterialLibName(self, materialLibName: str):
        """
        Setter for property: (str) MaterialLibName
         Returns the material library Name   
            
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material enum   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material enum   
            
         
        """
        pass
    @property
    def MaterialVisual(self) -> MaterialVisualItemBuilder:
        """
        Getter for property: ( MaterialVisualItemBuilder NXOpen.Featu) MaterialVisual
         Returns the material visual  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def ProcessNote(self) -> str:
        """
        Getter for property: (str) ProcessNote
         Returns the process note   
            
         
        """
        pass
    @ProcessNote.setter
    def ProcessNote(self, processNote: str):
        """
        Setter for property: (str) ProcessNote
         Returns the process note   
            
         
        """
        pass
import NXOpen
class BaseLibraryItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BaseLibraryItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BaseLibraryItemBuilder) -> None:
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
    def Erase(self, obj: BaseLibraryItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BaseLibraryItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BaseLibraryItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BaseLibraryItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BaseLibraryItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BaseLibraryItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BaseLibraryItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BaseLibraryItemBuilder) -> None:
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
    def SetContents(self, objects: List[BaseLibraryItemBuilder]) -> None:
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
    def Swap(self, object1: BaseLibraryItemBuilder, object2: BaseLibraryItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BaseLibraryItemBuilder(NXOpen.Builder): 
    """ The builder to define base library detail """
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @property
    def DetailItemList(self) -> BaseDetailItemBuilderList:
        """
        Getter for property: ( BaseDetailItemBuilderList NXOpen.Featu) DetailItemList
         Returns the list of  NXOpen::Features::AECDesign::BaseDetailItemBuilder  defining the base library item parameters.  
             
         
        """
        pass
    @property
    def IsDefault(self) -> bool:
        """
        Getter for property: (bool) IsDefault
         Returns the flag to indicate whether it is the default item.  
             
         
        """
        pass
    @IsDefault.setter
    def IsDefault(self, isDefault: bool):
        """
        Setter for property: (bool) IsDefault
         Returns the flag to indicate whether it is the default item.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class BeamBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.AECDesign.Beam builder
    """
    class HorizontalAlignmentTypes(Enum):
        """
        Members Include: 
         |LeftAligned| 
         |RightAligned| 
         |CenterlineAligned| 

        """
        LeftAligned: int
        RightAligned: int
        CenterlineAligned: int
        @staticmethod
        def ValueOf(value: int) -> BeamBuilder.HorizontalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VerticalAlignmentTypes(Enum):
        """
        Members Include: 
         |TopAligned| 
         |BottomAligned| 
         |CenterlineAligned| 

        """
        TopAligned: int
        BottomAligned: int
        CenterlineAligned: int
        @staticmethod
        def ValueOf(value: int) -> BeamBuilder.VerticalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildingElementTrim(self) -> BuildingElementTrimBuilder:
        """
        Getter for property: ( BuildingElementTrimBuilder NXOpen.Featu) BuildingElementTrim
         Returns the building element trim   
            
         
        """
        pass
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReference
         Returns the level reference  
            
         
        """
        pass
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: ( MaterialSectionBuilder NXOpen.Featu) MaterialSection
         Returns the material section  
            
         
        """
        pass
    @property
    def PathGeometry(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PathGeometry
         Returns the path geometry   
            
         
        """
        pass
    @property
    def YAlignmentType(self) -> BeamBuilder.HorizontalAlignmentTypes:
        """
        Getter for property: ( BeamBuilder.HorizontalAlignmentTypes NXOpen.Featu) YAlignmentType
         Returns the y offset alignment  
            
         
        """
        pass
    @YAlignmentType.setter
    def YAlignmentType(self, yAlignmentType: BeamBuilder.HorizontalAlignmentTypes):
        """
        Setter for property: ( BeamBuilder.HorizontalAlignmentTypes NXOpen.Featu) YAlignmentType
         Returns the y offset alignment  
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset   
            
         
        """
        pass
    @property
    def ZAlignmentType(self) -> BeamBuilder.VerticalAlignmentTypes:
        """
        Getter for property: ( BeamBuilder.VerticalAlignmentTypes NXOpen.Featu) ZAlignmentType
         Returns the z offset alignment   
            
         
        """
        pass
    @ZAlignmentType.setter
    def ZAlignmentType(self, zAlignmentType: BeamBuilder.VerticalAlignmentTypes):
        """
        Setter for property: ( BeamBuilder.VerticalAlignmentTypes NXOpen.Featu) ZAlignmentType
         Returns the z offset alignment   
            
         
        """
        pass
    @property
    def ZOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZOffset
         Returns the z offset   
            
         
        """
        pass
    def UpdateReferencedColumns(self) -> None:
        """
         Update Ref Columns
        """
        pass
import NXOpen.Features
class Beam(NXOpen.Features.BodyFeature): 
    """ Represents a beam feature """
    pass
import NXOpen
class BIMClassificationBuilder(NXOpen.Builder): 
    """ 
    Represents a classify component builder for AEC.
    
    
    This builder is used to classify component in AEC. 
    
    """
    class RequisiteTypes(Enum):
        """
        Members Include: 
         |All| Lists all available properties            
         |Mandatory| Lists only the mandatory properties  
         |Optional| Lists only the optional properties    
         |UserDefined| 

        """
        All: int
        Mandatory: int
        Optional: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> BIMClassificationBuilder.RequisiteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoolValue(self) -> bool:
        """
        Getter for property: (bool) BoolValue
         Returnsthe bool value of currently accessing property.  
             
         
        """
        pass
    @BoolValue.setter
    def BoolValue(self, boolValue: bool):
        """
        Setter for property: (bool) BoolValue
         Returnsthe bool value of currently accessing property.  
             
         
        """
        pass
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returnsthe currently selected category name.  
             
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returnsthe currently selected category name.  
             
         
        """
        pass
    @property
    def ComponentType(self) -> int:
        """
        Getter for property: (int) ComponentType
         Returns the component type   
            
         
        """
        pass
    @ComponentType.setter
    def ComponentType(self, componentType: int):
        """
        Setter for property: (int) ComponentType
         Returns the component type   
            
         
        """
        pass
    @property
    def DoubleValue(self) -> float:
        """
        Getter for property: (float) DoubleValue
         Returnsthe double value of currently accessing property.  
             
         
        """
        pass
    @DoubleValue.setter
    def DoubleValue(self, doubleValue: float):
        """
        Setter for property: (float) DoubleValue
         Returnsthe double value of currently accessing property.  
             
         
        """
        pass
    @property
    def IntValue(self) -> int:
        """
        Getter for property: (int) IntValue
         Returnsthe int value of currently accessing property.  
             
         
        """
        pass
    @IntValue.setter
    def IntValue(self, intValue: int):
        """
        Setter for property: (int) IntValue
         Returnsthe int value of currently accessing property.  
             
         
        """
        pass
    @property
    def PropertiesRequisiteType(self) -> BIMClassificationBuilder.RequisiteTypes:
        """
        Getter for property: ( BIMClassificationBuilder.RequisiteTypes NXOpen.Featu) PropertiesRequisiteType
         Returns the properties filter type   
            
         
        """
        pass
    @PropertiesRequisiteType.setter
    def PropertiesRequisiteType(self, propertiesRequisiteType: BIMClassificationBuilder.RequisiteTypes):
        """
        Setter for property: ( BIMClassificationBuilder.RequisiteTypes NXOpen.Featu) PropertiesRequisiteType
         Returns the properties filter type   
            
         
        """
        pass
    @property
    def Property(self) -> str:
        """
        Getter for property: (str) Property
         Returnsthe currently accessing property name.  
             
         
        """
        pass
    @Property.setter
    def Property(self, propertyName: str):
        """
        Setter for property: (str) Property
         Returnsthe currently accessing property name.  
             
         
        """
        pass
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returnsthe string value of currently accessing property.  
             
         
        """
        pass
    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returnsthe string value of currently accessing property.  
             
         
        """
        pass
    def GetSelectParts(self) -> List[NXOpen.Part]:
        """
         Gets the select parts 
         Returns selectParts ( NXOpen.Part Li): .
        """
        pass
    def SetBoolValueAndTypeAsPropertyName(self, propertyName: str, boolValue: bool, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    def SetDoubleValueAndTypeAsPropertyName(self, propertyName: str, doubleValue: float, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    def SetIntValueAndTypeAsPropertyName(self, propertyName: str, intValue: int, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
    def SetReclassify(self, isReclassify: bool) -> None:
        """
         Sets reclassify 
        """
        pass
    def SetSelectParts(self, selectParts: List[NXOpen.Part]) -> None:
        """
         Sets the selected parts. 
        """
        pass
    def SetStringValueAndTypeAsPropertyName(self, propertyName: str, stringValue: str, strDataType: str, strRequisite: str) -> None:
        """
         Sets the variant type and value as property name 
        """
        pass
import NXOpen
class BIMSlopeBuilder(NXOpen.Builder): 
    """ 
        Represents a BIM slope builder for AEC Design. 
        
        
        This builder is used to create BIMSlopeData in AEC Design.
        
    """
    class SlopeOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |Angle| 
         |Height| 
         |Ratio| 
         |Percentage| 

        """
        NotSet: int
        Angle: int
        Height: int
        Ratio: int
        Percentage: int
        @staticmethod
        def ValueOf(value: int) -> BIMSlopeBuilder.SlopeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SlopeAngleDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeAngleDim
         Returns the slope angle dimension   
            
         
        """
        pass
    @property
    def SlopeHeightDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeHeightDim
         Returns the slope height dimension   
            
         
        """
        pass
    @property
    def SlopePercentage(self) -> float:
        """
        Getter for property: (float) SlopePercentage
         Returns the slope percentage   
            
         
        """
        pass
    @SlopePercentage.setter
    def SlopePercentage(self, slopePercentage: float):
        """
        Setter for property: (float) SlopePercentage
         Returns the slope percentage   
            
         
        """
        pass
    @property
    def SlopeRatioDen(self) -> float:
        """
        Getter for property: (float) SlopeRatioDen
         Returns the slope ratio denominator   
            
         
        """
        pass
    @SlopeRatioDen.setter
    def SlopeRatioDen(self, slopeRatioDen: float):
        """
        Setter for property: (float) SlopeRatioDen
         Returns the slope ratio denominator   
            
         
        """
        pass
    @property
    def SlopeRatioNum(self) -> float:
        """
        Getter for property: (float) SlopeRatioNum
         Returns the slope ratio numerator   
            
         
        """
        pass
    @SlopeRatioNum.setter
    def SlopeRatioNum(self, slopeRatioNum: float):
        """
        Setter for property: (float) SlopeRatioNum
         Returns the slope ratio numerator   
            
         
        """
        pass
    @property
    def SlopeSetting(self) -> BIMSlopeBuilder.SlopeOption:
        """
        Getter for property: ( BIMSlopeBuilder.SlopeOption NXOpen.Featu) SlopeSetting
         Returns the slope setting   
            
         
        """
        pass
    @SlopeSetting.setter
    def SlopeSetting(self, slopeSetting: BIMSlopeBuilder.SlopeOption):
        """
        Setter for property: ( BIMSlopeBuilder.SlopeOption NXOpen.Featu) SlopeSetting
         Returns the slope setting   
            
         
        """
        pass
import NXOpen
class BoundaryOffsetBuilder(NXOpen.Builder): 
    """ 
        Represents a BoundaryOffset builder for AEC Design. 
        
        
        This builder is used to create BoundaryOffset Data in AEC Design.
        
    """
    @property
    def BoundaryOffsetList(self) -> BoundaryOffsetListItemBuilderList:
        """
        Getter for property: ( BoundaryOffsetListItemBuilderList NXOpen.Featu) BoundaryOffsetList
         Returns the boundary offset list   
            
         
        """
        pass
    def CreateBoundaryOffsetListItemBuilder(self) -> BoundaryOffsetListItemBuilder:
        """
         The boundary offset item creation function
         Returns boundaryOffsetListItemBuilder ( BoundaryOffsetListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen
class BoundaryOffsetListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BoundaryOffsetListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BoundaryOffsetListItemBuilder) -> None:
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
    def Erase(self, obj: BoundaryOffsetListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BoundaryOffsetListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BoundaryOffsetListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BoundaryOffsetListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BoundaryOffsetListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BoundaryOffsetListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BoundaryOffsetListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BoundaryOffsetListItemBuilder) -> None:
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
    def SetContents(self, objects: List[BoundaryOffsetListItemBuilder]) -> None:
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
    def Swap(self, object1: BoundaryOffsetListItemBuilder, object2: BoundaryOffsetListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BoundaryOffsetListItemBuilder(NXOpen.TaggedObject): 
    """ Boundary offset list item builder """
    @property
    def BoundaryOffsetCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BoundaryOffsetCurve
         Returns the boundary offset curve   
            
         
        """
        pass
    @property
    def BoundaryOffsetDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoundaryOffsetDim
         Returns the boundary offset dim   
            
         
        """
        pass
import NXOpen
class BuildingElementTrimBuilder(NXOpen.Builder): 
    """ 
        Represents a building element trim builder for AEC Design. 
        
        
        This builder is used to create BuildingElementTrimData in AEC Design.
        
    """
    class BooleanType(Enum):
        """
        Members Include: 
         |Trim| 
         |NotSet| 

        """
        Trim: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> BuildingElementTrimBuilder.BooleanType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BooleanSetting(self) -> BuildingElementTrimBuilder.BooleanType:
        """
        Getter for property: ( BuildingElementTrimBuilder.BooleanType NXOpen.Featu) BooleanSetting
         Returns the boolean setting.  
             
         
        """
        pass
    @BooleanSetting.setter
    def BooleanSetting(self, booleanSetting: BuildingElementTrimBuilder.BooleanType):
        """
        Setter for property: ( BuildingElementTrimBuilder.BooleanType NXOpen.Featu) BooleanSetting
         Returns the boolean setting.  
             
         
        """
        pass
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ToolBody
         Returns the tool body.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class CeilingBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents a ceiling builder for AEC Design. 
        
        
        This builder is used to create ceiling feature in AEC Design.
        
    """
    @property
    def BoundaryOffset(self) -> BoundaryOffsetBuilder:
        """
        Getter for property: ( BoundaryOffsetBuilder NXOpen.Featu) BoundaryOffset
         Returns the level reference  
            
         
        """
        pass
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReference
         Returns the level reference  
            
         
        """
        pass
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: ( MaterialLayersBuilder NXOpen.Featu) MaterialLayers
         Returns the material layers  
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset distance between ceiling and the original room top face.  
             
         
        """
        pass
    @property
    def SelectCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectCurves
         Returns the boundary curve to define ceiling.  
             
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ToolBody
         Returns the tool body   
            
         
        """
        pass
    @property
    def TrimFlag(self) -> bool:
        """
        Getter for property: (bool) TrimFlag
         Returns the building element trim flag   
            
         
        """
        pass
    @TrimFlag.setter
    def TrimFlag(self, trimFlag: bool):
        """
        Setter for property: (bool) TrimFlag
         Returns the building element trim flag   
            
         
        """
        pass
import NXOpen.Features
class Ceiling(NXOpen.Features.BodyFeature): 
    """ Represents a ceiling feature """
    pass
import NXOpen
import NXOpen.Features
class ColumnBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents a column builder for AEC Design. 
        
        
        This builder is used to create column feature in AEC Design.
        
    """
    class CreationMethod(Enum):
        """
        Members Include: 
         |Points| 
         |SpecifyLine| 

        """
        Points: int
        SpecifyLine: int
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.CreationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HorizontalAlignmentTypes(Enum):
        """
        Members Include: 
         |LeftAligned| 
         |RightAligned| 
         |CenterlineAligned| 

        """
        LeftAligned: int
        RightAligned: int
        CenterlineAligned: int
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.HorizontalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RotationType(Enum):
        """
        Members Include: 
         |Right90| 
         |Left90| 
         |Vertical| 
         |Horizontal| 
         |MoreOption| 

        """
        Right90: int
        Left90: int
        Vertical: int
        Horizontal: int
        MoreOption: int
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.RotationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VerticalAlignmentTypes(Enum):
        """
        Members Include: 
         |TopAligned| 
         |BottomAligned| 
         |CenterlineAligned| 

        """
        TopAligned: int
        BottomAligned: int
        CenterlineAligned: int
        @staticmethod
        def ValueOf(value: int) -> ColumnBuilder.VerticalAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LevelReferenceBottom(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReferenceBottom
         Returns the lower level reference.  
             
         
        """
        pass
    @property
    def LevelReferenceTop(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReferenceTop
         Returns the higher level reference.  
             
         
        """
        pass
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: ( MaterialSectionBuilder NXOpen.Featu) MaterialSection
         Returns the materialSection.  
             
         
        """
        pass
    @property
    def PathGeometry(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PathGeometry
         Returns the path geometry.  
             
         
        """
        pass
    @property
    def PlacementMethod(self) -> ColumnBuilder.CreationMethod:
        """
        Getter for property: ( ColumnBuilder.CreationMethod NXOpen.Featu) PlacementMethod
         Returns the placement method used to locate the column.  
             
         
        """
        pass
    @PlacementMethod.setter
    def PlacementMethod(self, placementMethod: ColumnBuilder.CreationMethod):
        """
        Setter for property: ( ColumnBuilder.CreationMethod NXOpen.Featu) PlacementMethod
         Returns the placement method used to locate the column.  
             
         
        """
        pass
    @property
    def Points(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Points
         Returns the points.  
             
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle.  
             
         
        """
        pass
    @property
    def RotationOption(self) -> ColumnBuilder.RotationType:
        """
        Getter for property: ( ColumnBuilder.RotationType NXOpen.Featu) RotationOption
         Returns the rotation option.  
             
         
        """
        pass
    @RotationOption.setter
    def RotationOption(self, rotationOption: ColumnBuilder.RotationType):
        """
        Setter for property: ( ColumnBuilder.RotationType NXOpen.Featu) RotationOption
         Returns the rotation option.  
             
         
        """
        pass
    @property
    def TrimWithinLimits(self) -> bool:
        """
        Getter for property: (bool) TrimWithinLimits
         Returns the flag to indicate whether the trim winthin limits or not.  
             
         
        """
        pass
    @TrimWithinLimits.setter
    def TrimWithinLimits(self, isTrimWithinLimits: bool):
        """
        Setter for property: (bool) TrimWithinLimits
         Returns the flag to indicate whether the trim winthin limits or not.  
             
         
        """
        pass
    @property
    def XAlignmentType(self) -> ColumnBuilder.HorizontalAlignmentTypes:
        """
        Getter for property: ( ColumnBuilder.HorizontalAlignmentTypes NXOpen.Featu) XAlignmentType
         Returns the x offset alignment.  
             
         
        """
        pass
    @XAlignmentType.setter
    def XAlignmentType(self, xAlignmentType: ColumnBuilder.HorizontalAlignmentTypes):
        """
        Setter for property: ( ColumnBuilder.HorizontalAlignmentTypes NXOpen.Featu) XAlignmentType
         Returns the x offset alignment.  
             
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset.  
             
         
        """
        pass
    @property
    def YAlignmentType(self) -> ColumnBuilder.VerticalAlignmentTypes:
        """
        Getter for property: ( ColumnBuilder.VerticalAlignmentTypes NXOpen.Featu) YAlignmentType
         Returns the y offset alignment.  
            
         
        """
        pass
    @YAlignmentType.setter
    def YAlignmentType(self, yAlignmentType: ColumnBuilder.VerticalAlignmentTypes):
        """
        Setter for property: ( ColumnBuilder.VerticalAlignmentTypes NXOpen.Featu) YAlignmentType
         Returns the y offset alignment.  
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset.  
             
         
        """
        pass
import NXOpen.Features
class Column(NXOpen.Features.BodyFeature): 
    """ Represents a column feature """
    pass
import NXOpen.Features
class ConcreteRebarAnnotationBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents a concrete rebar annotation builder for AEC Design. 
        
        
        This builder is used to create concrete rebar annotation feature in AEC Design.
        
    """
    @property
    def LeaderLine(self) -> bool:
        """
        Getter for property: (bool) LeaderLine
         Returns the option to add leaderline to annotation.  
             
         
        """
        pass
    @LeaderLine.setter
    def LeaderLine(self, leaderLine: bool):
        """
        Setter for property: (bool) LeaderLine
         Returns the option to add leaderline to annotation.  
             
         
        """
        pass
    @property
    def RebarFeature(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) RebarFeature
         Returns the select rebar feature.  
             
         
        """
        pass
    @property
    def TextRotation(self) -> bool:
        """
        Getter for property: (bool) TextRotation
         Returns the option to rotate text 90 degrees to annotation.  
             
         
        """
        pass
    @TextRotation.setter
    def TextRotation(self, textRotation: bool):
        """
        Setter for property: (bool) TextRotation
         Returns the option to rotate text 90 degrees to annotation.  
             
         
        """
        pass
import NXOpen.Features
class ConcreteRebarAnnotation(NXOpen.Features.BodyFeature): 
    """ Represents a concreterebarannotation feature """
    pass
import NXOpen
import NXOpen.Features
class CrossingRebarsBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents a crossing rebars builder for AEC Design. 
        
        
        This builder is used to create crossing rebars feature in AEC Design.
        
    """
    @property
    def AlternateCoverThickness(self) -> AlternateCoverThicknessBuilder:
        """
        Getter for property: ( AlternateCoverThicknessBuilder NXOpen.Featu) AlternateCoverThickness
         Returns the alternate cover thickness offset   
            
         
        """
        pass
    @property
    def BendingRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendingRadius
         Returns the bending radius.  
             
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter.  
             
         
        """
        pass
    @property
    def EndHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: ( RebarHookBlockBuilder NXOpen.Featu) EndHook
         Returns the end hook.  
             
         
        """
        pass
    @property
    def EndLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: ( RebarLimitBuilder NXOpen.Featu) EndLimit
         Returns the end limit.  
             
         
        """
        pass
    @property
    def EndPointLocation(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) EndPointLocation
         Returns the end point location.  
             
         
        """
        pass
    @property
    def ExcludeSegment(self) -> bool:
        """
        Getter for property: (bool) ExcludeSegment
         Returns the flag to indicate whether to open the exclude segment.  
             
         
        """
        pass
    @ExcludeSegment.setter
    def ExcludeSegment(self, excludeSegment: bool):
        """
        Setter for property: (bool) ExcludeSegment
         Returns the flag to indicate whether to open the exclude segment.  
             
         
        """
        pass
    @property
    def IntervalDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IntervalDistance
         Returns the interval distance.  
             
         
        """
        pass
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: ( MaterialSectionBuilder NXOpen.Featu) MaterialSection
         Returns the materialSection.  
             
         
        """
        pass
    @property
    def NumberOfRebars(self) -> int:
        """
        Getter for property: (int) NumberOfRebars
         Returns the number of rebars.  
             
         
        """
        pass
    @NumberOfRebars.setter
    def NumberOfRebars(self, numberOfRebars: int):
        """
        Setter for property: (int) NumberOfRebars
         Returns the number of rebars.  
             
         
        """
        pass
    @property
    def NumberOfTurns(self) -> float:
        """
        Getter for property: (float) NumberOfTurns
         Returns the number of turns.  
             
         
        """
        pass
    @NumberOfTurns.setter
    def NumberOfTurns(self, numberOfTurns: float):
        """
        Setter for property: (float) NumberOfTurns
         Returns the number of turns.  
             
         
        """
        pass
    @property
    def PitchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PitchDistance
         Returns the pitch distance.  
             
         
        """
        pass
    @property
    def PlacementMethod(self) -> RebarsBuilder.CrossingCreationMethod:
        """
        Getter for property: ( RebarsBuilder.CrossingCreationMethod NXOpen.Featu) PlacementMethod
         Returns the placement method used to locate the crossing rebars.  
             
         
        """
        pass
    @PlacementMethod.setter
    def PlacementMethod(self, placementMethod: RebarsBuilder.CrossingCreationMethod):
        """
        Setter for property: ( RebarsBuilder.CrossingCreationMethod NXOpen.Featu) PlacementMethod
         Returns the placement method used to locate the crossing rebars.  
             
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction.  
             
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction.  
             
         
        """
        pass
    @property
    def SelectEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectEdge
         Returns the select edge.  
             
         
        """
        pass
    @property
    def SpacingSetting(self) -> RebarsBuilder.SpacingOption:
        """
        Getter for property: ( RebarsBuilder.SpacingOption NXOpen.Featu) SpacingSetting
         Returns the space setting.  
             
         
        """
        pass
    @SpacingSetting.setter
    def SpacingSetting(self, spacingSetting: RebarsBuilder.SpacingOption):
        """
        Setter for property: ( RebarsBuilder.SpacingOption NXOpen.Featu) SpacingSetting
         Returns the space setting.  
             
         
        """
        pass
    @property
    def StartFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) StartFace
         Returns the start face.  
             
         
        """
        pass
    @property
    def StartHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: ( RebarHookBlockBuilder NXOpen.Featu) StartHook
         Returns the start hook.  
             
         
        """
        pass
    @property
    def StartLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: ( RebarLimitBuilder NXOpen.Featu) StartLimit
         Returns the start limit.  
             
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the start point.  
             
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the start point.  
             
         
        """
        pass
    @property
    def ThicknessDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessDistance
         Returns the thickness distance.  
             
         
        """
        pass
    @property
    def TurnsAtEnd(self) -> float:
        """
        Getter for property: (float) TurnsAtEnd
         Returns the extra turns at end.  
             
         
        """
        pass
    @TurnsAtEnd.setter
    def TurnsAtEnd(self, turnsAtEnd: float):
        """
        Setter for property: (float) TurnsAtEnd
         Returns the extra turns at end.  
             
         
        """
        pass
    @property
    def TurnsAtStart(self) -> float:
        """
        Getter for property: (float) TurnsAtStart
         Returns the extra turns at start.  
             
         
        """
        pass
    @TurnsAtStart.setter
    def TurnsAtStart(self, turnsAtStart: float):
        """
        Setter for property: (float) TurnsAtStart
         Returns the extra turns at start.  
             
         
        """
        pass
    def UpdateReferencedRebarBodies(self) -> None:
        """
         Updates referenced columns. 
        """
        pass
import NXOpen.Features
class CrossingRebars(NXOpen.Features.BodyFeature): 
    """ Represents a crossingrebars feature """
    pass
import NXOpen
import NXOpen.Assemblies
class ExplodeComponentBuilder(NXOpen.Builder): 
    """ 
        Represents a Explode Component builder for AEC. 
        
        
        This builder is used to explode BIM components in AEC.
        
    """
    class ExplodeScope(Enum):
        """
        Members Include: 
         |AllComponents|  All supported BIM components 
         |SelectedComponents|  User selected BIM components 

        """
        AllComponents: int
        SelectedComponents: int
        @staticmethod
        def ValueOf(value: int) -> ExplodeComponentBuilder.ExplodeScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SelectComponents(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) SelectComponents
         Returns the selected BIM components   
            
         
        """
        pass
    @property
    def SelectScope(self) -> ExplodeComponentBuilder.ExplodeScope:
        """
        Getter for property: ( ExplodeComponentBuilder.ExplodeScope NXOpen.Featu) SelectScope
         Returns the BIM components scope   
            
         
        """
        pass
    @SelectScope.setter
    def SelectScope(self, selectScope: ExplodeComponentBuilder.ExplodeScope):
        """
        Setter for property: ( ExplodeComponentBuilder.ExplodeScope NXOpen.Featu) SelectScope
         Returns the BIM components scope   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class ExtendToRoofBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents an ExtendToRoofBuilder  for AEC Design. 
        
        
        This builder is used to create ExtendToRoof feature in AEC Design.
        
    """
    @property
    def SelectTargets(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectTargets
         Returns the select target objects   
            
         
        """
        pass
    @property
    def SelectTools(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectTools
         Returns the select tool object   
            
         
        """
        pass
import NXOpen.Features
class ExtendToRoof(NXOpen.Features.BodyFeature): 
    """ Represents a extend to roof feature """
    pass
import NXOpen
import NXOpen.Features
class FloorBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents a floor builder for AEC Design. 
        
        
        This builder is used to create floor feature in AEC Design.
        
    """
    @property
    def BIMSlope(self) -> BIMSlopeBuilder:
        """
        Getter for property: ( BIMSlopeBuilder NXOpen.Featu) BIMSlope
         Returns the BIM slope   
            
         
        """
        pass
    @property
    def BoundaryOffset(self) -> BoundaryOffsetBuilder:
        """
        Getter for property: ( BoundaryOffsetBuilder NXOpen.Featu) BoundaryOffset
         Returns the boundary offset   
            
         
        """
        pass
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReference
         Returns the level reference  
            
         
        """
        pass
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: ( MaterialLayersBuilder NXOpen.Featu) MaterialLayers
         Returns the material layers  
            
         
        """
        pass
    @property
    def SelectCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectCurve
         Returns the boundary curves to define floor.  
             
         
        """
        pass
    @property
    def SlopeCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SlopeCurve
         Returns the slope curve   
            
         
        """
        pass
    @property
    def ToolBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ToolBody
         Returns the tool body   
            
         
        """
        pass
    @property
    def TrimFlag(self) -> bool:
        """
        Getter for property: (bool) TrimFlag
         Returns the building element trim flag   
            
         
        """
        pass
    @TrimFlag.setter
    def TrimFlag(self, trimFlag: bool):
        """
        Setter for property: (bool) TrimFlag
         Returns the building element trim flag   
            
         
        """
        pass
import NXOpen.Features
class Floor(NXOpen.Features.BodyFeature): 
    """ Represents a floor feature """
    pass
import NXOpen
class GridBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.GridBuilder builder
        """
    class Types(Enum):
        """
        Members Include: 
         |Create| 
         |Select| 
         |Num| 

        """
        Create: int
        Select: int
        Num: int
        @staticmethod
        def ValueOf(value: int) -> GridBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class GridLineNoteBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.GridLineNoteBuilder builder
        """
    @property
    def BalloonText(self) -> str:
        """
        Getter for property: (str) BalloonText
         Returns the balloon text   
            
         
        """
        pass
    @BalloonText.setter
    def BalloonText(self, balloonText: str):
        """
        Setter for property: (str) BalloonText
         Returns the balloon text   
            
         
        """
        pass
    def UpdateNotes(self) -> None:
        """
         Updates the balloon text 
        """
        pass
import NXOpen
import NXOpen.Annotations
class GridLineOffsetBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.GridLineOffsetBuilder builder
        """
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance to offset the grid line.  
             
         
        """
        pass
    @property
    def FlipAll(self) -> bool:
        """
        Getter for property: (bool) FlipAll
         Returns the flag to indicate whether to flip the offset direction.  
             
         
        """
        pass
    @FlipAll.setter
    def FlipAll(self, bFilped: bool):
        """
        Setter for property: (bool) FlipAll
         Returns the flag to indicate whether to flip the offset direction.  
             
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of the copied grid lines.  
             
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of the copied grid lines.  
             
         
        """
        pass
    @property
    def Section(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Section
         Returns the selected sketch curve collector for copying grid line.  
             
         
        """
        pass
    def ClearSelection(self) -> None:
        """
         Clears the selection of the target grid line. 
        """
        pass
    def CopyGridLines(self) -> None:
        """
         Copies the selection of the target grid line. 
        """
        pass
    def SelectGridLine(self, tgBaseLine: NXOpen.Annotations.AECDesignBaseLine, offsetVector: NXOpen.Vector3d) -> None:
        """
         Selects the target grid line to offset. 
        """
        pass
    def UpdateDistance(self) -> None:
        """
         Updates the offset distance of the target grid line. 
        """
        pass
    def UpdateFlip(self) -> None:
        """
         Updates the offset direction accroding to the flip state. 
        """
        pass
    def UpdateNumOfCopies(self) -> None:
        """
         Updates the number of copies of the target grid line. 
        """
        pass
import NXOpen
class GridLinePreferencesBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.GridLinePreferencesBuilder builder
        """
    @property
    def AnnotationScale(self) -> float:
        """
        Getter for property: (float) AnnotationScale
         Returns the scale of grid annotation.  
             
         
        """
        pass
    @AnnotationScale.setter
    def AnnotationScale(self, scale: float):
        """
        Setter for property: (float) AnnotationScale
         Returns the scale of grid annotation.  
             
         
        """
        pass
    @property
    def CenterSegmentType(self) -> int:
        """
        Getter for property: (int) CenterSegmentType
         Returns the type of center segment.  
             
         
        """
        pass
    @CenterSegmentType.setter
    def CenterSegmentType(self, centerSegmentType: int):
        """
        Setter for property: (int) CenterSegmentType
         Returns the type of center segment.  
             
         
        """
        pass
    @property
    def CreateEndAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateEndAnnotation
         Returns the flag to indicate whether to create the end annoation of grid line or not.  
             
         
        """
        pass
    @CreateEndAnnotation.setter
    def CreateEndAnnotation(self, createEndAnnotation: bool):
        """
        Setter for property: (bool) CreateEndAnnotation
         Returns the flag to indicate whether to create the end annoation of grid line or not.  
             
         
        """
        pass
    @property
    def CreateStartAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateStartAnnotation
         Returns the flag to indicate whether to create the start annoation of grid line or not.  
             
         
        """
        pass
    @CreateStartAnnotation.setter
    def CreateStartAnnotation(self, createStartAnnotation: bool):
        """
        Setter for property: (bool) CreateStartAnnotation
         Returns the flag to indicate whether to create the start annoation of grid line or not.  
             
         
        """
        pass
    @property
    def LineEndSegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineEndSegmentLength
         Returns the length of grid line end segment   
            
         
        """
        pass
    @property
    def SymbolType(self) -> int:
        """
        Getter for property: (int) SymbolType
         Returns the type of grid line end symbol.  
             
         
        """
        pass
    @SymbolType.setter
    def SymbolType(self, symbolType: int):
        """
        Setter for property: (int) SymbolType
         Returns the type of grid line end symbol.  
             
         
        """
        pass
    def UpdateColorStyleWidth(self, endSegmentColor: int, endSegmentStyle: int, endSegmentWidth: int, centerSegmentColor: int, centerSegmentStyle: int, centerSegmentWidth: int) -> None:
        """
         Updates the grid line color, style, width.
        """
        pass
import NXOpen.Features
class Grid(NXOpen.Features.Feature): 
    """ Represents a AEC grid feature """
    pass
import NXOpen
class IFCPropertiesBuilder(NXOpen.Builder): 
    """ 
       Represents an IFC properties builder for AEC.
       
       
       This builder is used to deal with ifc properties in AEC. 
       
       """
    def CreateCommonPropertiesSetManager(self) -> None:
        """
         Create CommonPropertiesSetManager 
        """
        pass
    def SetBuilderAtrributes(self, part: NXOpen.Part, isEntityType: bool, categoryName: str, propertyeName: str, propertyType: str, propertyValue: str) -> None:
        """
        Set builder attributes 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class LabellingRoomsBuilder(NXOpen.Builder): 
    """
           Represents a Features.AECDesign.LabellingRoomsBuilder builder
        """
    class ExisingaeclabelType(Enum):
        """
        Members Include: 
         |Preserve| 
         |Delete| 

        """
        Preserve: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> LabellingRoomsBuilder.ExisingaeclabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associativity(self) -> bool:
        """
        Getter for property: (bool) Associativity
         Returns the setting that indicates whether pmi note  will be associative with room or equipment  
            
         
        """
        pass
    @Associativity.setter
    def Associativity(self, isAssociativity: bool):
        """
        Setter for property: (bool) Associativity
         Returns the setting that indicates whether pmi note  will be associative with room or equipment  
            
         
        """
        pass
    @property
    def ExsitingLabelOption(self) -> LabellingRoomsBuilder.ExisingaeclabelType:
        """
        Getter for property: ( LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Featu) ExsitingLabelOption
         Returnsthe option to specify how to handle existing label  
            
         
        """
        pass
    @ExsitingLabelOption.setter
    def ExsitingLabelOption(self, existingLabel: LabellingRoomsBuilder.ExisingaeclabelType):
        """
        Setter for property: ( LabellingRoomsBuilder.ExisingaeclabelType NXOpen.Featu) ExsitingLabelOption
         Returnsthe option to specify how to handle existing label  
            
         
        """
        pass
    @property
    def RoomsSelection(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) RoomsSelection
         Returns the rooms or equipment selection   
            
         
        """
        pass
import NXOpen
class LevelBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.LevelBuilder builder
        """
    @property
    def MaximumX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumX
         Returns the maximum X position   
            
         
        """
        pass
    @property
    def MaximumY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumY
         Returns the maximum Y position   
            
         
        """
        pass
    @property
    def MinimumX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumX
         Returns the minimum X position   
            
         
        """
        pass
    @property
    def MinimumY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumY
         Returns the minimum Y position   
            
         
        """
        pass
import NXOpen
class LevelLineNoteBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.GridLineNoteBuilder builder
        """
    @property
    def LabelText(self) -> str:
        """
        Getter for property: (str) LabelText
         Returns the label text   
            
         
        """
        pass
    @LabelText.setter
    def LabelText(self, labelText: str):
        """
        Setter for property: (str) LabelText
         Returns the label text   
            
         
        """
        pass
    @property
    def LevelHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LevelHeight
         Returns the height of aec level   
            
         
        """
        pass
import NXOpen
class LevelLinePreferencesBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.LevelLinePreferencesBuilder builder
        """
    @property
    def AnnotationScale(self) -> float:
        """
        Getter for property: (float) AnnotationScale
         Returns the scale of level annotation.  
             
         
        """
        pass
    @AnnotationScale.setter
    def AnnotationScale(self, scale: float):
        """
        Setter for property: (float) AnnotationScale
         Returns the scale of level annotation.  
             
         
        """
        pass
    @property
    def CreateEndAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateEndAnnotation
         Returns the flag to indicate whether to create the end annoation of level line or not.  
             
         
        """
        pass
    @CreateEndAnnotation.setter
    def CreateEndAnnotation(self, createEndAnnotation: bool):
        """
        Setter for property: (bool) CreateEndAnnotation
         Returns the flag to indicate whether to create the end annoation of level line or not.  
             
         
        """
        pass
    @property
    def CreateStartAnnotation(self) -> bool:
        """
        Getter for property: (bool) CreateStartAnnotation
         Returns the flag to indicate whether to create the start annoation of level line or not.  
             
         
        """
        pass
    @CreateStartAnnotation.setter
    def CreateStartAnnotation(self, createStartAnnotation: bool):
        """
        Setter for property: (bool) CreateStartAnnotation
         Returns the flag to indicate whether to create the start annoation of level line or not.  
             
         
        """
        pass
    @property
    def SymbolType(self) -> int:
        """
        Getter for property: (int) SymbolType
         Returns the type of level line end symbol.  
             
         
        """
        pass
    @SymbolType.setter
    def SymbolType(self, symbolType: int):
        """
        Setter for property: (int) SymbolType
         Returns the type of level line end symbol.  
             
         
        """
        pass
    def UpdateColorStyleWidth(self, color: int, style: int, width: int) -> None:
        """
         Updates the level line color, style, width.
        """
        pass
import NXOpen
class LevelPartsBuilder(NXOpen.Builder): 
    """ 
        Represents a level parts builder for AEC.
        
        
        This builder is used to create level parts in AEC. 
        
        """
    @property
    def Placement(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Placement
         Returns the placement   
            
         
        """
        pass
    @Placement.setter
    def Placement(self, placement: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Placement
         Returns the placement   
            
         
        """
        pass
    @property
    def ReferenceGeometry(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ReferenceGeometry
         Returns the reference geometry   
            
         
        """
        pass
import NXOpen.Features
class LevelParts(NXOpen.Features.BodyFeature): 
    """ Represents a ship section feature """
    pass
import NXOpen
class LevelReferenceBuilder(NXOpen.Builder): 
    """ 
            Represents a level reference builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the level reference.
            
        """
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset distance from the reference level.  
             
         
        """
        pass
    @property
    def ReferenceLevelName(self) -> str:
        """
        Getter for property: (str) ReferenceLevelName
         Returns the reference level  
            
         
        """
        pass
    @ReferenceLevelName.setter
    def ReferenceLevelName(self, levelName: str):
        """
        Setter for property: (str) ReferenceLevelName
         Returns the reference level  
            
         
        """
        pass
import NXOpen
class LevelReference(NXOpen.NXObject): 
    """ Represents a ship section feature """
    pass
import NXOpen.Features
class Level(NXOpen.Features.Feature): 
    """ Represents a AEC level feature """
    pass
import NXOpen
class LibraryManagerBuilder(NXOpen.Builder): 
    """
        Represents a Features.AECDesign.LibraryManagerBuilder
        """
    @property
    def LibraryItemList(self) -> BaseLibraryItemBuilderList:
        """
        Getter for property: ( BaseLibraryItemBuilderList NXOpen.Featu) LibraryItemList
         Returns the base library item detail builder list   
            
         
        """
        pass
    def CreateMaterialDataContainerBuilder(self) -> MaterialDataContainerBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialDataContainerBuilder 
         Returns dataContainerItem ( MaterialDataContainerBuilder NXOpen.Featu): .
        """
        pass
    def CreateMaterialLayerDetailBuilder(self) -> MaterialLayerDetailBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialLayerDetailBuilder 
         Returns layerItem ( MaterialLayerDetailBuilder NXOpen.Featu): .
        """
        pass
    def CreateMaterialRailingDetailBuilder(self) -> MaterialRailingDetailBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialRailingDetailBuilder 
         Returns railingItem ( MaterialRailingDetailBuilder NXOpen.Featu): .
        """
        pass
    def CreateMaterialSectionDetailBuilder(self) -> MaterialSectionDetailBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialSectionDetailBuilder 
         Returns sectionItem ( MaterialSectionDetailBuilder NXOpen.Featu): .
        """
        pass
    def CreateMaterialStairDetailBuilder(self) -> MaterialStairDetailBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialStairDetailBuilder 
         Returns stairItem ( MaterialStairDetailBuilder NXOpen.Featu): .
        """
        pass
    def ExportFromBuilder(self, filePath: str) -> None:
        """
         Exports the current layer definition as the specific xml file. 
        """
        pass
    def Find(self, identifier: str) -> NXOpen.TaggedObject:
        """
         Find the material detail layer builder or material detail section builder by the name. 
         Returns found ( NXOpen.TaggedObject):  .
        """
        pass
    def ImportToBuilder(self, filePath: str) -> None:
        """
         Imports the specific layer definition xml file. 
        """
        pass
    def MergeCategoryFromXML(self, filePath: str, caterory: str) -> None:
        """
         Merges the specific category from xml file. 
        """
        pass
import NXOpen
import NXOpen.Features
class LongitudinalRebarsBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
        Represents a longitudinal rebars builder for AEC Design. 
        
        
        This builder is used to create longitudinal rebars feature in AEC Design.
        
    """
    @property
    def CrossingRebarsFeature(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) CrossingRebarsFeature
         Returns the select crossing features.  
             
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter.  
             
         
        """
        pass
    @property
    def EndFacesThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndFacesThickness
         Returns the end faces thickness.  
             
         
        """
        pass
    @property
    def EndHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: ( RebarHookBlockBuilder NXOpen.Featu) EndHook
         Returns the end hook.  
             
         
        """
        pass
    @property
    def EndLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: ( RebarLimitBuilder NXOpen.Featu) EndLimit
         Returns the end limit.  
             
         
        """
        pass
    @property
    def MaterialSection(self) -> MaterialSectionBuilder:
        """
        Getter for property: ( MaterialSectionBuilder NXOpen.Featu) MaterialSection
         Returns the materialSection.  
             
         
        """
        pass
    @property
    def NumberOfRebars(self) -> int:
        """
        Getter for property: (int) NumberOfRebars
         Returns the number of rebars.  
             
         
        """
        pass
    @NumberOfRebars.setter
    def NumberOfRebars(self, numberOfRebars: int):
        """
        Setter for property: (int) NumberOfRebars
         Returns the number of rebars.  
             
         
        """
        pass
    @property
    def PatternSetting(self) -> RebarsBuilder.PatternOption:
        """
        Getter for property: ( RebarsBuilder.PatternOption NXOpen.Featu) PatternSetting
         Returns the space setting.  
             
         
        """
        pass
    @PatternSetting.setter
    def PatternSetting(self, patternSetting: RebarsBuilder.PatternOption):
        """
        Setter for property: ( RebarsBuilder.PatternOption NXOpen.Featu) PatternSetting
         Returns the space setting.  
             
         
        """
        pass
    @property
    def PlacementMethod(self) -> RebarsBuilder.LongitudinalCreationMethod:
        """
        Getter for property: ( RebarsBuilder.LongitudinalCreationMethod NXOpen.Featu) PlacementMethod
         Returns the placement method used to locate the longitudinal rebars.  
             
         
        """
        pass
    @PlacementMethod.setter
    def PlacementMethod(self, placementMethod: RebarsBuilder.LongitudinalCreationMethod):
        """
        Setter for property: ( RebarsBuilder.LongitudinalCreationMethod NXOpen.Featu) PlacementMethod
         Returns the placement method used to locate the longitudinal rebars.  
             
         
        """
        pass
    @property
    def SelectEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectEdge
         Returns the select edge.  
             
         
        """
        pass
    @property
    def SpecifyPoint(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SpecifyPoint
         Returns the specify point   
            
         
        """
        pass
    @property
    def StartFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) StartFace
         Returns the start face.  
             
         
        """
        pass
    @property
    def StartFacesThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartFacesThickness
         Returns the start faces thickness.  
             
         
        """
        pass
    @property
    def StartHook(self) -> RebarHookBlockBuilder:
        """
        Getter for property: ( RebarHookBlockBuilder NXOpen.Featu) StartHook
         Returns the start hook.  
             
         
        """
        pass
    @property
    def StartLimit(self) -> RebarLimitBuilder:
        """
        Getter for property: ( RebarLimitBuilder NXOpen.Featu) StartLimit
         Returns the start limit.  
             
         
        """
        pass
    def AlternateSolution(self) -> None:
        """
         Rotate the rebar 90 degrees. 
        """
        pass
    def UpdateReferencedRebarBodies(self) -> None:
        """
         Updates referenced columns. 
        """
        pass
import NXOpen.Features
class LongitudinalRebars(NXOpen.Features.BodyFeature): 
    """ Represents a longitudinal rebars feature """
    pass
import NXOpen
class MaterialDataContainerBuilder(BaseLibraryItemBuilder): 
    """ The builder to define material data container """
    @property
    def ContainerItemList(self) -> BaseLibraryItemBuilderList:
        """
        Getter for property: ( BaseLibraryItemBuilderList NXOpen.Featu) ContainerItemList
         Returns the list of base library item detail builder   
            
         
        """
        pass
    def Find(self, identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the material data container builder by the name. 
         Returns found ( NXOpen.TaggedObject):  .
        """
        pass
    def InitializeFromBuilder(self, selectedLibraryItem: BaseLibraryItemBuilder) -> None:
        """
         Initializes the material data container builder. 
        """
        pass
    def SetNameAndCategory(self, name: str, category: str) -> None:
        """
         Sets the material data container builder name and category 
        """
        pass
import NXOpen
class MaterialLayerDetailBuilder(BaseLibraryItemBuilder): 
    """ The builder to define material layer detail """
    def CreateMaterialLayerDetailItemBuilder(self) -> MaterialLayerDetailItemBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialLayerDetailItemBuilder 
         Returns layerItem ( MaterialLayerDetailItemBuilder NXOpen.Featu): .
        """
        pass
    def Find(self, identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the material detail layer item builder by the name. 
         Returns found ( NXOpen.TaggedObject):  .
        """
        pass
    def InitFromBuilder(self, selectedLibraryItem: BaseLibraryItemBuilder) -> None:
        """
         Init the material detail layer item builder. 
        """
        pass
    def SetNameAndCategory(self, name: str, category: str) -> None:
        """
         Sets the material layer detail builder name and category 
        """
        pass
import NXOpen
class MaterialLayerDetailItemBuilder(BaseDetailItemBuilder): 
    """
        Represents a BaseLibraryItemBuilder.
        """
    @property
    def Primary(self) -> bool:
        """
        Getter for property: (bool) Primary
         Returns the primary   
            
         
        """
        pass
    @Primary.setter
    def Primary(self, primary: bool):
        """
        Setter for property: (bool) Primary
         Returns the primary   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
import NXOpen
class MaterialLayersBuilder(NXOpen.Builder): 
    """ 
            Represents a specific layer builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the layer.
            
        """
    @property
    def Layer(self) -> str:
        """
        Getter for property: (str) Layer
         Returns the layer name  
            
         
        """
        pass
    @Layer.setter
    def Layer(self, layerName: str):
        """
        Setter for property: (str) Layer
         Returns the layer name  
            
         
        """
        pass
import NXOpen
class MaterialLayer(NXOpen.NXObject): 
    """ Represents a ship section feature """
    pass
class MaterialRailingBuilder(MaterialSectionBuilder): 
    """ 
            Represents a specific material railing builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the material railing.
            
        """
    pass
class MaterialRailingDetailBuilder(MaterialSectionDetailBuilder): 
    """ The builder to define material railing detail """
    def CreateMaterialRailingDetailItemBuilder(self) -> MaterialRailingDetailItemBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialRailingDetailItemBuilder 
         Returns railingItem ( MaterialRailingDetailItemBuilder NXOpen.Featu): .
        """
        pass
class MaterialRailingDetailItemBuilder(MaterialSectionDetailItemBuilder): 
    """
        Represents a MaterialRailingDetailItemBuilder.
        """
    class TypeName(Enum):
        """
        Members Include: 
         |Rail| 
         |Baluster| 

        """
        Rail: int
        Baluster: int
        @staticmethod
        def ValueOf(value: int) -> MaterialRailingDetailItemBuilder.TypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ProfileType(self) -> MaterialRailingDetailItemBuilder.TypeName:
        """
        Getter for property: ( MaterialRailingDetailItemBuilder.TypeName NXOpen.Featu) ProfileType
         Returns the profile type   
            
         
        """
        pass
    @ProfileType.setter
    def ProfileType(self, profileType: MaterialRailingDetailItemBuilder.TypeName):
        """
        Setter for property: ( MaterialRailingDetailItemBuilder.TypeName NXOpen.Featu) ProfileType
         Returns the profile type   
            
         
        """
        pass
import NXOpen
class MaterialRailing(NXOpen.NXObject): 
    """ Represents a material railing feature """
    pass
import NXOpen
class MaterialSectionBuilder(NXOpen.Builder): 
    """ 
            Represents a specific section builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the section.
            
        """
    @property
    def SectionName(self) -> str:
        """
        Getter for property: (str) SectionName
         Returns the section name  
            
         
        """
        pass
    @SectionName.setter
    def SectionName(self, sectionName: str):
        """
        Setter for property: (str) SectionName
         Returns the section name  
            
         
        """
        pass
import NXOpen
class MaterialSectionDetailBuilder(BaseLibraryItemBuilder): 
    """ The builder to define material section detail """
    def CreateMaterialSectionDetailItemBuilder(self) -> MaterialSectionDetailItemBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialSectionDetailItemBuilder 
         Returns sectionItem ( MaterialSectionDetailItemBuilder NXOpen.Featu): .
        """
        pass
    def Find(self, identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the material detail section item builder by the name. 
         Returns found ( NXOpen.TaggedObject):  .
        """
        pass
    def InitFromBuilder(self, selectedLibraryItem: BaseLibraryItemBuilder) -> None:
        """
         Init the material detail section item builder. 
        """
        pass
    def SetNameAndCategory(self, name: str, category: str) -> None:
        """
         Sets the material section detail builder name and category 
        """
        pass
class MaterialSectionDetailItemBuilder(BaseDetailItemBuilder): 
    """
        Represents a BaseLibraryItemBuilder.
        """
    @property
    def SectionStock(self) -> SectionFeatureSpreadsheetBuilder:
        """
        Getter for property: ( SectionFeatureSpreadsheetBuilder NXOpen.Featu) SectionStock
         Returns the section stock  
            
         
        """
        pass
import NXOpen
class MaterialSection(NXOpen.NXObject): 
    """ Represents a ship section feature """
    pass
class MaterialStairBuilder(MaterialLayersBuilder): 
    """ 
            Represents a specific material stair builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the material stair.
            
        """
    pass
class MaterialStairDetailBuilder(MaterialLayerDetailBuilder): 
    """ The builder to define material stair detail """
    def CreateMaterialStairDetailItemBuilder(self) -> MaterialStairDetailItemBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialStairDetailItemBuilder 
         Returns stairItem ( MaterialStairDetailItemBuilder NXOpen.Featu): .
        """
        pass
    def CreateMaterialStairDetailItemStringerBuilder(self) -> MaterialStairDetailItemStringerBuilder:
        """
         Creates a NXOpen.Features.AECDesign.MaterialStairDetailItemStringerBuilder 
         Returns stairItem ( MaterialStairDetailItemStringerBuilder NXOpen.Featu): .
        """
        pass
class MaterialStairDetailItemBuilder(MaterialLayerDetailItemBuilder): 
    """
        Represents a MaterialStairDetailItemBuilder.
        """
    class TypeName(Enum):
        """
        Members Include: 
         |Tread| 
         |Riser| 
         |Stringer| 
         |Carriage| 

        """
        Tread: int
        Riser: int
        Stringer: int
        Carriage: int
        @staticmethod
        def ValueOf(value: int) -> MaterialStairDetailItemBuilder.TypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SlabType(self) -> MaterialStairDetailItemBuilder.TypeName:
        """
        Getter for property: ( MaterialStairDetailItemBuilder.TypeName NXOpen.Featu) SlabType
         Returns the slab type   
            
         
        """
        pass
    @SlabType.setter
    def SlabType(self, slabType: MaterialStairDetailItemBuilder.TypeName):
        """
        Setter for property: ( MaterialStairDetailItemBuilder.TypeName NXOpen.Featu) SlabType
         Returns the slab type   
            
         
        """
        pass
import NXOpen
class MaterialStairDetailItemStringerBuilder(MaterialStairDetailItemBuilder): 
    """
        Represents a MaterialStairDetailItemStringerBuilder.
        """
    @property
    def StructuralDepthOnRun(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StructuralDepthOnRun
         Returns the structural depth on run   
            
         
        """
        pass
    @property
    def TotalDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TotalDepth
         Returns the total depth   
            
         
        """
        pass
import NXOpen
class MaterialStair(NXOpen.NXObject): 
    """ Represents a material stair feature """
    pass
import NXOpen
class MaterialVisualItemBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Features.AECDesign.MaterialVisualItemBuilder builder. This builder is used to
        change the material color and studio material name for visualization. 
        """
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns the color   
            
         
        """
        pass
    @property
    def StudioMaterialName(self) -> str:
        """
        Getter for property: (str) StudioMaterialName
         Returns the name of the studio material to apply   
            
         
        """
        pass
    @StudioMaterialName.setter
    def StudioMaterialName(self, studioMaterialName: str):
        """
        Setter for property: (str) StudioMaterialName
         Returns the name of the studio material to apply   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class OpeningBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.AECDesign.Opening builder
    """
    @property
    def CustomShape(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CustomShape
         Returns the custom shape   
            
         
        """
        pass
    @property
    def OpeningPenetrationDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OpeningPenetrationDepth
         Returns the depth of opening   
            
         
        """
        pass
    @property
    def ProjectionDirection(self) -> ProjectionOptions:
        """
        Getter for property: ( ProjectionOptions NXOpen.Geome) ProjectionDirection
         Returns the direction used to project the custom shape curves   
            
         
        """
        pass
    @property
    def SelectTargetFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectTargetFaces
         Returns the select target faces   
            
         
        """
        pass
import NXOpen.Features
class Opening(NXOpen.Features.BodyFeature): 
    """ Represents a opening feature """
    pass
import NXOpen
class PickCurveBuilder(NXOpen.Builder): 
    """
            Represents a Features.AECDesign.PickCurveBuilder builder
        """
    @property
    def CurvesToSelect(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurvesToSelect
         Returns the selected curve list  
            
         
        """
        pass
    def SetMultiSegment(self, bMultiSegment: bool) -> None:
        """
         Set the state of multi-segment
        """
        pass
import NXOpen
import NXOpen.Features.Industry
class ProjectSetupBuilder(NXOpen.Builder): 
    """ 
        Represents a project setup builder for AEC.
        
        
        This builder is used to setup project in AEC. 
        
        """
    @property
    def IsNewStructure(self) -> bool:
        """
        Getter for property: (bool) IsNewStructure
         Returns the flag to indicate whether it is new structure or not.  
             
         
        """
        pass
    @IsNewStructure.setter
    def IsNewStructure(self, isNewStructure: bool):
        """
        Setter for property: (bool) IsNewStructure
         Returns the flag to indicate whether it is new structure or not.  
             
         
        """
        pass
    @property
    def IsSaveAsSharePart(self) -> bool:
        """
        Getter for property: (bool) IsSaveAsSharePart
         Returns the flag to indicate whether it is to save as the shared part.  
             
         
        """
        pass
    @IsSaveAsSharePart.setter
    def IsSaveAsSharePart(self, isSaveAsSharePart: bool):
        """
        Setter for property: (bool) IsSaveAsSharePart
         Returns the flag to indicate whether it is to save as the shared part.  
             
         
        """
        pass
    @property
    def ProjectLoadFromBuilder(self) -> NXOpen.Features.Industry.SelectProjectLoadFromBuilder:
        """
        Getter for property: ( NXOpen.Features.Industry.SelectProjectLoadFromBuilder) ProjectLoadFromBuilder
         Returns the projectLoadFromBuilder.  
            
         
        """
        pass
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
         Returns the project name   
            
         
        """
        pass
    @ProjectName.setter
    def ProjectName(self, projectName: str):
        """
        Setter for property: (str) ProjectName
         Returns the project name   
            
         
        """
        pass
    def GetRootNode(self) -> NXOpen.Features.Industry.ProjectStructureNode:
        """
         Gets the structure root node. 
         Returns rootNode ( NXOpen.Features.Industry.ProjectStructureNode):  the root structure node. .
        """
        pass
import NXOpen
import NXOpen.Features
class RailingBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Features.AECDesign.Railing builder
    """
    class AlignmentTypes(Enum):
        """
        Members Include: 
         |Left| 
         |Center| 
         |Right| 
         |LeftAndRight| 
         |OnStringer| 

        """
        Left: int
        Center: int
        Right: int
        LeftAndRight: int
        OnStringer: int
        @staticmethod
        def ValueOf(value: int) -> RailingBuilder.AlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlacementOptions(Enum):
        """
        Members Include: 
         |AttachedToStair| 
         |OnCurve| 

        """
        AttachedToStair: int
        OnCurve: int
        @staticmethod
        def ValueOf(value: int) -> RailingBuilder.PlacementOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignmentOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AlignmentOffset
         Returns the alignment offset distance   
            
         
        """
        pass
    @property
    def AlignmentType(self) -> RailingBuilder.AlignmentTypes:
        """
        Getter for property: ( RailingBuilder.AlignmentTypes NXOpen.Featu) AlignmentType
         Returns the alignment type   
            
         
        """
        pass
    @AlignmentType.setter
    def AlignmentType(self, alignmentType: RailingBuilder.AlignmentTypes):
        """
        Setter for property: ( RailingBuilder.AlignmentTypes NXOpen.Featu) AlignmentType
         Returns the alignment type   
            
         
        """
        pass
    @property
    def BalusterInterval(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BalusterInterval
         Returns the baluster interval   
            
         
        """
        pass
    @property
    def Handrail(self) -> bool:
        """
        Getter for property: (bool) Handrail
         Returns the create handrail flag   
            
         
        """
        pass
    @Handrail.setter
    def Handrail(self, handrail: bool):
        """
        Setter for property: (bool) Handrail
         Returns the create handrail flag   
            
         
        """
        pass
    @property
    def HandrailHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HandrailHeight
         Returns the handrail height   
            
         
        """
        pass
    @property
    def HandrailOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HandrailOffset
         Returns the handrail offset distance   
            
         
        """
        pass
    @property
    def MaterialRailing(self) -> MaterialRailingBuilder:
        """
        Getter for property: ( MaterialRailingBuilder NXOpen.Featu) MaterialRailing
         Returns the material railing   
            
         
        """
        pass
    @property
    def RailingHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RailingHeight
         Returns the overall height of the railing   
            
         
        """
        pass
    @property
    def ReferenceCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ReferenceCurve
         Returns the reference curve   
            
         
        """
        pass
    @property
    def ReferenceStair(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReferenceStair
         Returns the reference stair bodies   
            
         
        """
        pass
    @property
    def ReverseHandrailOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseHandrailOffsetDirection
         Returns the reverse handrail offset direction flag   
            
         
        """
        pass
    @ReverseHandrailOffsetDirection.setter
    def ReverseHandrailOffsetDirection(self, reverseHandrailOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseHandrailOffsetDirection
         Returns the reverse handrail offset direction flag   
            
         
        """
        pass
    @property
    def TopRail(self) -> bool:
        """
        Getter for property: (bool) TopRail
         Returns the create top rail flag   
            
         
        """
        pass
    @TopRail.setter
    def TopRail(self, topRail: bool):
        """
        Setter for property: (bool) TopRail
         Returns the create top rail flag   
            
         
        """
        pass
    @property
    def Type(self) -> RailingBuilder.PlacementOptions:
        """
        Getter for property: ( RailingBuilder.PlacementOptions NXOpen.Featu) Type
         Returns the railing placement option   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: RailingBuilder.PlacementOptions):
        """
        Setter for property: ( RailingBuilder.PlacementOptions NXOpen.Featu) Type
         Returns the railing placement option   
            
         
        """
        pass
import NXOpen.Features
class Railing(NXOpen.Features.BodyFeature): 
    """ Represents a railing feature """
    pass
import NXOpen
class RebarHookBlockBuilder(NXOpen.Builder): 
    """ 
            Represents a rebar hook block builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the rebar hook block.
            
        """
    @property
    def HookAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HookAngle
         Returns the hook angle.  
             
         
        """
        pass
    @property
    def HookLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HookLength
         Returns the hook length.  
             
         
        """
        pass
    @property
    def HookOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HookOffset
         Returns the hook offset.  
             
         
        """
        pass
    @property
    def HookOffsetType(self) -> RebarsBuilder.HookOffsetOption:
        """
        Getter for property: ( RebarsBuilder.HookOffsetOption NXOpen.Featu) HookOffsetType
         Returns the hook offset type.  
             
         
        """
        pass
    @HookOffsetType.setter
    def HookOffsetType(self, hookOffsetType: RebarsBuilder.HookOffsetOption):
        """
        Setter for property: ( RebarsBuilder.HookOffsetOption NXOpen.Featu) HookOffsetType
         Returns the hook offset type.  
             
         
        """
        pass
    @property
    def HookRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HookRadius
         Returns the hook radius.  
             
         
        """
        pass
    @property
    def HookType(self) -> RebarsBuilder.HookOption:
        """
        Getter for property: ( RebarsBuilder.HookOption NXOpen.Featu) HookType
         Returns the hook type.  
             
         
        """
        pass
    @HookType.setter
    def HookType(self, hookType: RebarsBuilder.HookOption):
        """
        Setter for property: ( RebarsBuilder.HookOption NXOpen.Featu) HookType
         Returns the hook type.  
             
         
        """
        pass
import NXOpen
class RebarHookBlock(NXOpen.NXObject): 
    """ Represents an aecdesign rebar hook block feature """
    pass
import NXOpen
class RebarLimitBuilder(NXOpen.Builder): 
    """ 
            Represents a rebar limit builder which can be used by features for AEC Design. 
            
            
            This builder is used to define the rebar limit.
            
        """
    @property
    def LimitDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LimitDistance
         Returns the limit distance.  
             
         
        """
        pass
    @property
    def LimitType(self) -> RebarsBuilder.LimitOption:
        """
        Getter for property: ( RebarsBuilder.LimitOption NXOpen.Featu) LimitType
         Returns the limit type.  
             
         
        """
        pass
    @LimitType.setter
    def LimitType(self, limitType: RebarsBuilder.LimitOption):
        """
        Setter for property: ( RebarsBuilder.LimitOption NXOpen.Featu) LimitType
         Returns the limit type.  
             
         
        """
        pass
    @property
    def SelectTarget(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectTarget
         Returns the select target   
            
         
        """
        pass
import NXOpen
class RebarLimit(NXOpen.NXObject): 
    """ Represents an aecdesign rebar limit feature """
    pass
import NXOpen
class RebarsBuilder(NXOpen.Builder): 
    """
        Represents a RebarsBuilder.
        """
    class CrossingCreationMethod(Enum):
        """
        Members Include: 
         |Rectangular| 
         |CylindricalSpiral| 
         |CylindricalCircular| 

        """
        Rectangular: int
        CylindricalSpiral: int
        CylindricalCircular: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.CrossingCreationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HookOffsetOption(Enum):
        """
        Members Include: 
         |CoverThickness| 
         |UserDefined| 

        """
        CoverThickness: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.HookOffsetOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HookOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |Degrees90| 
         |Degrees135| 
         |Degrees180| 
         |UserDefined| 

        """
        NotSet: int
        Degrees90: int
        Degrees135: int
        Degrees180: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.HookOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LimitOption(Enum):
        """
        Members Include: 
         |Value| 
         |SymmetricValue| 
         |UntilNext| 
         |UntilSelected| 
         |UntilExtended| 
         |OffsetFromSelected| 

        """
        Value: int
        SymmetricValue: int
        UntilNext: int
        UntilSelected: int
        UntilExtended: int
        OffsetFromSelected: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.LimitOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LongitudinalCreationMethod(Enum):
        """
        Members Include: 
         |WithinRectangular| 
         |WithinCylindrical| 
         |OnPoint| 

        """
        WithinRectangular: int
        WithinCylindrical: int
        OnPoint: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.LongitudinalCreationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PatternOption(Enum):
        """
        Members Include: 
         |FourBarAround| 
         |SixBarsMirrored| 
         |EightBarsAround| 
         |EightBarsMirrored| 
         |TenBarsMirrored| 
         |TwelveBarsMirrored| 

        """
        FourBarAround: int
        SixBarsMirrored: int
        EightBarsAround: int
        EightBarsMirrored: int
        TenBarsMirrored: int
        TwelveBarsMirrored: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.PatternOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpacingOption(Enum):
        """
        Members Include: 
         |EquallyDistributed| 
         |ExactSpacing| 
         |ExactSpacingFirst| 
         |ExactSpacingLast| 
         |ExactSpacingMiddle| 
         |ExactSpacingFirstAndLast| 

        """
        EquallyDistributed: int
        ExactSpacing: int
        ExactSpacingFirst: int
        ExactSpacingLast: int
        ExactSpacingMiddle: int
        ExactSpacingFirstAndLast: int
        @staticmethod
        def ValueOf(value: int) -> RebarsBuilder.SpacingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class RoofBoundaryListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[RoofBoundaryListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: RoofBoundaryListItemBuilder) -> None:
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
    def Erase(self, obj: RoofBoundaryListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: RoofBoundaryListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: RoofBoundaryListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> RoofBoundaryListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( RoofBoundaryListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[RoofBoundaryListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( RoofBoundaryListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: RoofBoundaryListItemBuilder) -> None:
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
    def SetContents(self, objects: List[RoofBoundaryListItemBuilder]) -> None:
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
    def Swap(self, object1: RoofBoundaryListItemBuilder, object2: RoofBoundaryListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class RoofBoundaryListItemBuilder(NXOpen.TaggedObject): 
    """ roof boundary list item builder """
    class ExtensionOption(Enum):
        """
        Members Include: 
         |OverhangType| 
         |OffsetType| 

        """
        OverhangType: int
        OffsetType: int
        @staticmethod
        def ValueOf(value: int) -> RoofBoundaryListItemBuilder.ExtensionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BoundaryCurve
         Returns the boundary curve   
            
         
        """
        pass
    @property
    def BoundaryItemName(self) -> str:
        """
        Getter for property: (str) BoundaryItemName
         Returns the boundary item name   
            
         
        """
        pass
    @BoundaryItemName.setter
    def BoundaryItemName(self, boundaryItemName: str):
        """
        Setter for property: (str) BoundaryItemName
         Returns the boundary item name   
            
         
        """
        pass
    @property
    def ExtensionDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDim
         Returns the extension dim   
            
         
        """
        pass
    @property
    def ExtensionType(self) -> RoofBoundaryListItemBuilder.ExtensionOption:
        """
        Getter for property: ( RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Featu) ExtensionType
         Returns the roof extension type.  
             
         
        """
        pass
    @ExtensionType.setter
    def ExtensionType(self, extensionType: RoofBoundaryListItemBuilder.ExtensionOption):
        """
        Setter for property: ( RoofBoundaryListItemBuilder.ExtensionOption NXOpen.Featu) ExtensionType
         Returns the roof extension type.  
             
         
        """
        pass
    @property
    def Slope(self) -> BIMSlopeBuilder:
        """
        Getter for property: ( BIMSlopeBuilder NXOpen.Featu) Slope
         Returns the BIM slope   
            
         
        """
        pass
import NXOpen
class RoofBuilder(NXOpen.Builder): 
    """ 
        Represents a roof builder for AEC.
        
        
        This builder is used to roof in AEC. 
        
        """
    class TopOption(Enum):
        """
        Members Include: 
         |FootprintType| 
         |ExtrusionType| 

        """
        FootprintType: int
        ExtrusionType: int
        @staticmethod
        def ValueOf(value: int) -> RoofBuilder.TopOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Boundaries(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Boundaries
         Returns the boundaries   
            
         
        """
        pass
    @property
    def BoundaryList(self) -> RoofBoundaryListItemBuilderList:
        """
        Getter for property: ( RoofBoundaryListItemBuilderList NXOpen.Featu) BoundaryList
         Returns the list of boundary objects   
            
         
        """
        pass
    @property
    def EndLimitDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndLimitDistance
         Returns the end limit distance   
            
         
        """
        pass
    @property
    def LevelReference(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReference
         Returns the level reference  
            
         
        """
        pass
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: ( MaterialLayersBuilder NXOpen.Featu) MaterialLayers
         Returns the layer  
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset   
            
         
        """
        pass
    @property
    def OverhangDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OverhangDistance
         Returns the overhang distance   
            
         
        """
        pass
    @property
    def StartLimitDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartLimitDistance
         Returns the start limit distance   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
    @property
    def TopType(self) -> RoofBuilder.TopOption:
        """
        Getter for property: ( RoofBuilder.TopOption NXOpen.Featu) TopType
         Returns the region option, which defines the plate areas in case of body faces as plate boundary.  
             
         
        """
        pass
    @TopType.setter
    def TopType(self, topType: RoofBuilder.TopOption):
        """
        Setter for property: ( RoofBuilder.TopOption NXOpen.Featu) TopType
         Returns the region option, which defines the plate areas in case of body faces as plate boundary.  
             
         
        """
        pass
    def CreateRoofBoundaryListItemBuilder(self) -> RoofBoundaryListItemBuilder:
        """
         The roof boundary item create function
         Returns roofBoundaryListItemBuilder ( RoofBoundaryListItemBuilder NXOpen.Featu): .
        """
        pass
import NXOpen.Features
class Roof(NXOpen.Features.BodyFeature): 
    """ Represents an roof feature """
    pass
import NXOpen
class RoomAttributeListBuilder(NXOpen.TaggedObject): 
    """ The builder to define room attributes """
    def SetAttribute(self, index: int, attrName: str, attrValue: str) -> None:
        """
         
                    Sets the specific attribute name and value given the index in the list. 
                    
        """
        pass
    def SetRoomPurpose(self, roomPurpose: str) -> None:
        """
         
                    Sets the room purpose. 
                    
                    
                    If room purpose changes, this will try to reconstruct the attribute list because
                    different attributes are pre-defined for different room purposes. 
                    
                    
        """
        pass
    def UpdateAttributeValue(self, row: int, headString: str, value: str) -> None:
        """
         
                    Updates the specific attribute value.
                    
        """
        pass
    def UpdateEvaluatdValue(self, rowIndex: int) -> bool:
        """
         
                    Updates evaluated attribute value.
                    
         Returns needUpdateList (bool): .
        """
        pass
import NXOpen
class RoomBuilder(NXOpen.Builder): 
    """ 
        Represents a room builder for aec application.
        
        
        This builder is used to define a room.
        
        """
    @property
    def Associativity(self) -> bool:
        """
        Getter for property: (bool) Associativity
         Returns the room label associativity with floor face   
            
         
        """
        pass
    @Associativity.setter
    def Associativity(self, associativity: bool):
        """
        Setter for property: (bool) Associativity
         Returns the room label associativity with floor face   
            
         
        """
        pass
    @property
    def AttributeList(self) -> RoomAttributeListBuilder:
        """
        Getter for property: ( RoomAttributeListBuilder NXOpen.Featu) AttributeList
         Returns    the room attribute list.  
            
         
                    
                        The room attributes defines attributes those are applied to the room component and body.
                       
         
        """
        pass
    @property
    def FaceList(self) -> RoomFaceListItemBuilderList:
        """
        Getter for property: ( RoomFaceListItemBuilderList NXOpen.Featu) FaceList
         Returns the list of room face   
            
         
        """
        pass
    @property
    def ProjectionDirection(self) -> ProjectionOptions:
        """
        Getter for property: ( ProjectionOptions NXOpen.Geome) ProjectionDirection
         Returns the projection direction   
            
         
        """
        pass
    @property
    def RoomColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) RoomColor
         Returns the color to be assigned to the created room body.  
            
         
        """
        pass
    @RoomColor.setter
    def RoomColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) RoomColor
         Returns the color to be assigned to the created room body.  
            
         
        """
        pass
    @property
    def RoomName(self) -> str:
        """
        Getter for property: (str) RoomName
         Returns the room name   
            
         
        """
        pass
    @RoomName.setter
    def RoomName(self, roomName: str):
        """
        Setter for property: (str) RoomName
         Returns the room name   
            
         
        """
        pass
    def CreateRoomFaceListItemBuilder(self) -> RoomFaceListItemBuilder:
        """
         The room face item create function
         Returns roomFaceListItemBuilder ( RoomFaceListItemBuilder NXOpen.Featu): .
        """
        pass
    def EvaluateAttributes(self, bUpdateRoomAreaAndVolume: bool) -> None:
        """
         Evaluates room attributes. 
        """
        pass
    def GetCreatedRoomBodies(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the created room bodies. 
         Returns createdRoomBodies ( NXOpen.TaggedObject Li): .
        """
        pass
    def ResetAttributes(self, bUpdateRoomAreaAndVolume: bool) -> None:
        """
         Resets room attributes. 
        """
        pass
    def UpdateRoomID(self, roomID: str) -> None:
        """
         Updates room ID. 
        """
        pass
    def UpdateTypeForAttributeListBuilder(self) -> None:
        """
         Updates room type which is either creation or adopt to the attribute list builder. 
        """
        pass
import NXOpen
class RoomFaceListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[RoomFaceListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: RoomFaceListItemBuilder) -> None:
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
    def Erase(self, obj: RoomFaceListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: RoomFaceListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: RoomFaceListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> RoomFaceListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( RoomFaceListItemBuilder NXOpen.Featu):  object found at input index .
        """
        pass
    def GetContents(self) -> List[RoomFaceListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( RoomFaceListItemBuilder List[NXOpen.Fea):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: RoomFaceListItemBuilder) -> None:
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
    def SetContents(self, objects: List[RoomFaceListItemBuilder]) -> None:
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
    def Swap(self, object1: RoomFaceListItemBuilder, object2: RoomFaceListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class RoomFaceListItemBuilder(NXOpen.Builder): 
    """ room face list item builder """
    @property
    def DivideCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) DivideCurve
         Returns the divide curve   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the face   
            
         
        """
        pass
    @property
    def ProjectionDirection(self) -> ProjectionOptions:
        """
        Getter for property: ( ProjectionOptions NXOpen.Geome) ProjectionDirection
         Returns the projection direction   
            
         
        """
        pass
    @property
    def Regions(self) -> NXOpen.RegionPointList:
        """
        Getter for property: ( NXOpen.RegionPointList) Regions
         Returns the region   
            
         
        """
        pass
    def CreateRegionBody(self) -> List[NXOpen.TaggedObject]:
        """
         Creates region body 
         Returns regionBody ( NXOpen.TaggedObject Li):  Body associated with the select region point. .
        """
        pass
    def DeleteRegionBody(self) -> None:
        """
         Delete the current region body. 
        """
        pass
    def SetPointToRegionList(self, targetBody: NXOpen.Body, regionPoint: NXOpen.Point3d) -> None:
        """
         Set the region point.
        """
        pass
    def SetProjectionDirection(self, projectionType: int, projectionVector: NXOpen.Direction) -> None:
        """
         Sets the projection direction
        """
        pass
    def SetRegionPoints(self, regionPoints: List[NXOpen.Point3d]) -> None:
        """
         Set the points derived from the regions of the sheet, that has the inscribed boundaries, to keep for the final 
                  room feature. 
        """
        pass
    def SetRoomFaceItemName(self, roomFaceItemName: str) -> None:
        """
         Sets room face name. 
        """
        pass
import NXOpen
class RoomReportBuilder(NXOpen.Builder): 
    """ 
        Represents a room report builder for aec application.
        
        
        This builder is used to define a room report.
        
        """
    @property
    def ReportFile(self) -> str:
        """
        Getter for property: (str) ReportFile
         Returns the report file.  
             
         
        """
        pass
    @ReportFile.setter
    def ReportFile(self, filename: str):
        """
        Setter for property: (str) ReportFile
         Returns the report file.  
             
         
        """
        pass
    def SetLevelParts(self, levelParts: List[NXOpen.Part]) -> None:
        """
         Sets the selected level parts. 
        """
        pass
import NXOpen.Features
class Room(NXOpen.Features.BodyFeature): 
    """ Represents an room feature """
    pass
import NXOpen.Features.Industry
class SectionFeatureSpreadsheetBuilder(NXOpen.Features.Industry.SectionFeatureSpreadsheetBuilder): 
    """
        Represents a NXOpen.Features.AECDesign.SectionFeatureSpreadsheetBuilder builder. 
        It is used to manage the data contained in the ship sketch based steel feature block.
        """
    pass
import NXOpen
import NXOpen.Features
class StairBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Features.AECDesign.Stair builder
    """
    class AlignmentTypes(Enum):
        """
        Members Include: 
         |LeftExteriorSupport| 
         |Left| 
         |Center| 
         |Right| 
         |RightExteriorSupport| 

        """
        LeftExteriorSupport: int
        Left: int
        Center: int
        Right: int
        RightExteriorSupport: int
        @staticmethod
        def ValueOf(value: int) -> StairBuilder.AlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StairTypes(Enum):
        """
        Members Include: 
         |Straight| 
         |StraightWithLandings| 
         |FullSpiral| 
         |PartialSpiral| 
         |LShapedWinder| 
         |UShapedWinder| 

        """
        Straight: int
        StraightWithLandings: int
        FullSpiral: int
        PartialSpiral: int
        LShapedWinder: int
        UShapedWinder: int
        @staticmethod
        def ValueOf(value: int) -> StairBuilder.StairTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SupportTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Carriage| 
         |Stringer| 

        """
        NotSet: int
        Carriage: int
        Stringer: int
        @staticmethod
        def ValueOf(value: int) -> StairBuilder.SupportTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TerminationTypes(Enum):
        """
        Members Include: 
         |EndWithRiser| 
         |EndWithTread| 

        """
        EndWithRiser: int
        EndWithTread: int
        @staticmethod
        def ValueOf(value: int) -> StairBuilder.TerminationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TurnDirectionTypes(Enum):
        """
        Members Include: 
         |RightHand| 
         |LeftHand| 

        """
        RightHand: int
        LeftHand: int
        @staticmethod
        def ValueOf(value: int) -> StairBuilder.TurnDirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PointPair:
        """
         Represents the start and end point pair 
         StairBuilderPointPair_Struct NXOpen.Featu is an alias for  StairBuilder.PointPair NXOpen.Featu.
        """
        @property
        def StartPoint(self) -> NXOpen.Point:
            """
            Getter for property StartPoint
            Start point

            """
            pass
        @StartPoint.setter
        def StartPoint(self, value: NXOpen.Point):
            """
            Getter for property StartPoint
            Start point
            Setter for property StartPoint
            Start point

            """
            pass
        @property
        def EndPoint(self) -> NXOpen.Point:
            """
            Getter for property EndPoint
            End point

            """
            pass
        @EndPoint.setter
        def EndPoint(self, value: NXOpen.Point):
            """
            Getter for property EndPoint
            End point
            Setter for property EndPoint
            End point

            """
            pass
    @property
    def AlignmentOffsetDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AlignmentOffsetDim
         Returns the alignment offset distance   
            
         
        """
        pass
    @property
    def AlignmentType(self) -> StairBuilder.AlignmentTypes:
        """
        Getter for property: ( StairBuilder.AlignmentTypes NXOpen.Featu) AlignmentType
         Returns the alignment type   
            
         
        """
        pass
    @AlignmentType.setter
    def AlignmentType(self, alignmentType: StairBuilder.AlignmentTypes):
        """
        Setter for property: ( StairBuilder.AlignmentTypes NXOpen.Featu) AlignmentType
         Returns the alignment type   
            
         
        """
        pass
    @property
    def BottomLevel(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) BottomLevel
         Returns the bottom level reference   
            
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the end or through point   
            
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the end or through point   
            
         
        """
        pass
    @property
    def FullSpiralAngleDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FullSpiralAngleDim
         Returns the full spiral angle   
            
         
        """
        pass
    @property
    def LeftCarriageOffsetDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LeftCarriageOffsetDim
         Returns the left carriage offset distance   
            
         
        """
        pass
    @property
    def LeftStringerDepthDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LeftStringerDepthDim
         Returns the left stringer depth   
            
         
        """
        pass
    @property
    def LeftSupportType(self) -> StairBuilder.SupportTypes:
        """
        Getter for property: ( StairBuilder.SupportTypes NXOpen.Featu) LeftSupportType
         Returns the left support type   
            
         
        """
        pass
    @LeftSupportType.setter
    def LeftSupportType(self, leftSupportType: StairBuilder.SupportTypes):
        """
        Setter for property: ( StairBuilder.SupportTypes NXOpen.Featu) LeftSupportType
         Returns the left support type   
            
         
        """
        pass
    @property
    def MaterialStair(self) -> MaterialStairBuilder:
        """
        Getter for property: ( MaterialStairBuilder NXOpen.Featu) MaterialStair
         Returns the material stair   
            
         
        """
        pass
    @property
    def MiddleCarriage(self) -> bool:
        """
        Getter for property: (bool) MiddleCarriage
         Returns the create middle carriage flag   
            
         
        """
        pass
    @MiddleCarriage.setter
    def MiddleCarriage(self, middleCarriage: bool):
        """
        Setter for property: (bool) MiddleCarriage
         Returns the create middle carriage flag   
            
         
        """
        pass
    @property
    def MinimumHeadroomDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumHeadroomDim
         Returns the minimum headroom   
            
         
        """
        pass
    @property
    def PartialSpiralAngleDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PartialSpiralAngleDim
         Returns the partial spiral angle   
            
         
        """
        pass
    @property
    def ReverseOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseOffsetDirection
         Returns the reverse offset direction flag   
            
         
        """
        pass
    @ReverseOffsetDirection.setter
    def ReverseOffsetDirection(self, reverseOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseOffsetDirection
         Returns the reverse offset direction flag   
            
         
        """
        pass
    @property
    def RightCarriageOffsetDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RightCarriageOffsetDim
         Returns the right carriage offset distance   
            
         
        """
        pass
    @property
    def RightStringerDepthDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RightStringerDepthDim
         Returns the right stringer depth   
            
         
        """
        pass
    @property
    def RightSupportType(self) -> StairBuilder.SupportTypes:
        """
        Getter for property: ( StairBuilder.SupportTypes NXOpen.Featu) RightSupportType
         Returns the right support type   
            
         
        """
        pass
    @RightSupportType.setter
    def RightSupportType(self, rightSupportType: StairBuilder.SupportTypes):
        """
        Setter for property: ( StairBuilder.SupportTypes NXOpen.Featu) RightSupportType
         Returns the right support type   
            
         
        """
        pass
    @property
    def RiserNumberExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RiserNumberExp
         Returns the riser number   
            
         
        """
        pass
    @property
    def RunWidthDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RunWidthDim
         Returns the run width   
            
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the start or center point   
            
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the start or center point   
            
         
        """
        pass
    @property
    def TerminationType(self) -> StairBuilder.TerminationTypes:
        """
        Getter for property: ( StairBuilder.TerminationTypes NXOpen.Featu) TerminationType
         Returns the termination type   
            
         
        """
        pass
    @TerminationType.setter
    def TerminationType(self, terminationType: StairBuilder.TerminationTypes):
        """
        Setter for property: ( StairBuilder.TerminationTypes NXOpen.Featu) TerminationType
         Returns the termination type   
            
         
        """
        pass
    @property
    def TopLevel(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) TopLevel
         Returns the top level reference   
            
         
        """
        pass
    @property
    def TopLevelOpening(self) -> bool:
        """
        Getter for property: (bool) TopLevelOpening
         Returns the top level opening flag   
            
         
        """
        pass
    @TopLevelOpening.setter
    def TopLevelOpening(self, topLevelOpening: bool):
        """
        Setter for property: (bool) TopLevelOpening
         Returns the top level opening flag   
            
         
        """
        pass
    @property
    def TreadDepthDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TreadDepthDim
         Returns the tread depth   
            
         
        """
        pass
    @property
    def TrimStringerAtTopLevel(self) -> bool:
        """
        Getter for property: (bool) TrimStringerAtTopLevel
         Returns the trim stringer at top level flag   
            
         
        """
        pass
    @TrimStringerAtTopLevel.setter
    def TrimStringerAtTopLevel(self, trimStringerAtTopLevel: bool):
        """
        Setter for property: (bool) TrimStringerAtTopLevel
         Returns the trim stringer at top level flag   
            
         
        """
        pass
    @property
    def TurnDirection(self) -> StairBuilder.TurnDirectionTypes:
        """
        Getter for property: ( StairBuilder.TurnDirectionTypes NXOpen.Featu) TurnDirection
         Returns the turn direction   
            
         
        """
        pass
    @TurnDirection.setter
    def TurnDirection(self, turnDirection: StairBuilder.TurnDirectionTypes):
        """
        Setter for property: ( StairBuilder.TurnDirectionTypes NXOpen.Featu) TurnDirection
         Returns the turn direction   
            
         
        """
        pass
    @property
    def Type(self) -> StairBuilder.StairTypes:
        """
        Getter for property: ( StairBuilder.StairTypes NXOpen.Featu) Type
         Returns the stair type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: StairBuilder.StairTypes):
        """
        Setter for property: ( StairBuilder.StairTypes NXOpen.Featu) Type
         Returns the stair type   
            
         
        """
        pass
    def AddNewStartEndPointPair(self) -> None:
        """
         The add new empty start and end point pair method 
        """
        pass
    def GetStartEndPointPairs(self) -> List[StairBuilder.PointPair]:
        """
         The get start and end point pairs method 
         Returns pointPairs ( StairBuilder.PointPair List[NXOpen.Fea): .
        """
        pass
    def SetStartEndPointPairs(self, pointPairs: List[StairBuilder.PointPair]) -> None:
        """
         The set start and end point pairs method 
        """
        pass
import NXOpen.Features
class Stair(NXOpen.Features.BodyFeature): 
    """ Represents a stair feature """
    pass
import NXOpen
import NXOpen.Features
class WallBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a NXOpen.Features.AECDesign.Wall builder
        """
    class AlignmentOption(Enum):
        """
        Members Include: 
         |Exterior| 
         |Interior| 
         |Centerline| 

        """
        Exterior: int
        Interior: int
        Centerline: int
        @staticmethod
        def ValueOf(value: int) -> WallBuilder.AlignmentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BooleanOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |Unite| 
         |Trim| 

        """
        NotSet: int
        Unite: int
        Trim: int
        @staticmethod
        def ValueOf(value: int) -> WallBuilder.BooleanOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Alignment(self) -> WallBuilder.AlignmentOption:
        """
        Getter for property: ( WallBuilder.AlignmentOption NXOpen.Featu) Alignment
         Returns the alignment   
            
         
        """
        pass
    @Alignment.setter
    def Alignment(self, alignment: WallBuilder.AlignmentOption):
        """
        Setter for property: ( WallBuilder.AlignmentOption NXOpen.Featu) Alignment
         Returns the alignment   
            
         
        """
        pass
    @property
    def AlternateSolutionPoint(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) AlternateSolutionPoint
         Returns the intersection points to apply alternate split solution   
            
         
        """
        pass
    @property
    def BooleanType(self) -> WallBuilder.BooleanOption:
        """
        Getter for property: ( WallBuilder.BooleanOption NXOpen.Featu) BooleanType
         Returns the boolean type   
            
         
        """
        pass
    @BooleanType.setter
    def BooleanType(self, booleanType: WallBuilder.BooleanOption):
        """
        Setter for property: ( WallBuilder.BooleanOption NXOpen.Featu) BooleanType
         Returns the boolean type   
            
         
        """
        pass
    @property
    def LevelReferenceBottom(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReferenceBottom
         Returns the bottom level reference   
            
         
        """
        pass
    @property
    def LevelReferenceTop(self) -> LevelReferenceBuilder:
        """
        Getter for property: ( LevelReferenceBuilder NXOpen.Featu) LevelReferenceTop
         Returns the top level reference   
            
         
        """
        pass
    @property
    def MaterialLayers(self) -> MaterialLayersBuilder:
        """
        Getter for property: ( MaterialLayersBuilder NXOpen.Featu) MaterialLayers
         Returns the material layers   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset   
            
         
        """
        pass
    @property
    def ReverseOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseOffsetDirection
         Returns the logic to reverse offset direction or not, true means reversed   
            
         
        """
        pass
    @ReverseOffsetDirection.setter
    def ReverseOffsetDirection(self, reverseOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseOffsetDirection
         Returns the logic to reverse offset direction or not, true means reversed   
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section   
            
         
        """
        pass
    @property
    def SelectedBodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectedBodies
         Returns the selected bodies   
            
         
        """
        pass
    @property
    def Split(self) -> bool:
        """
        Getter for property: (bool) Split
         Returns the toggle to split wall body itself or not   
            
         
        """
        pass
    @Split.setter
    def Split(self, split: bool):
        """
        Setter for property: (bool) Split
         Returns the toggle to split wall body itself or not   
            
         
        """
        pass
import NXOpen.Features
class Wall(NXOpen.Features.BodyFeature): 
    """ Represents a wall feature """
    pass
