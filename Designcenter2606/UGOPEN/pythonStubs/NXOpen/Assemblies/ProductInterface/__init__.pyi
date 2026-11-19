from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Collection(NXOpen.Object): 
    """ This class represents the collection of product interface objects """
    def AddMemberToGroups(self, productInterfaceObject: NXOpen.TaggedObject, selectedGroups: List[NXOpen.TaggedObject]) -> None:
        """
         Add the member to the Product Interface Group. It will not be removed from any of the existing group.
        """
        pass
    def CreateObjectBuilder(self) -> ObjectBuilder:
        """
         Create Product Interface Object Builder 
         Returns builder ( ObjectBuilder NXOpen.Assemblie): .
        """
        pass
    def CreateObjectBuilderWithBuilderVersion(self, version: ObjectBuilder.BuilderVersion) -> ObjectBuilder:
        """
         Create Product Interface Object Builder with NXOpen.Assemblies.ProductInterface.Collection.CreateObjectBuilderWithBuilderVersion
         Returns builder ( ObjectBuilder NXOpen.Assemblie): .
        """
        pass
    def CreateObjectBuilderWithVersion(self, version: int) -> ObjectBuilder:
        """
         Create Product Interface Object Builder with version
         Returns builder ( ObjectBuilder NXOpen.Assemblie): .
        """
        pass
    def CreatePropertyBuilder(self) -> PropertyBuilder:
        """
         Create Product Interface Property Builder 
         Returns builder ( PropertyBuilder NXOpen.Assemblie): .
        """
        pass
    def DeleteGroup(self, prodIntGroup: NXOpen.TaggedObject, deleteWithMembers: bool) -> None:
        """
         Delete the Product Interface Group. 
        """
        pass
    def FindObject(self, journal_identifier: str) -> NXOpen.NXObject:
        """
         Find the Product Interface Object with input name 
         Returns found ( NXOpen.NXObject):  Product Interface Object with this identifier .
        """
        pass
    def GetGroupName(self, prodIntGroup: NXOpen.TaggedObject) -> str:
        """
         Return the Product Interface Group name 
         Returns groupName (str): .
        """
        pass
    def GetProductInterfaces(self) -> List[InterfaceObject]:
        """
         Returns all the product interface objects in the part 
         Returns interface_objects ( InterfaceObject List[NXOpen.Assembl):  product interface objects in the part .
        """
        pass
    def MoveMemberToGroup(self, prodIntGroup: NXOpen.TaggedObject, memberToMove: NXOpen.TaggedObject) -> None:
        """
         Move the member to the Product Interface Group. It will removed from the old group and added to the new group.
        """
        pass
    def NewGroup(self) -> NXOpen.TaggedObject:
        """
         Creates the Product Interface Group in the part 
         Returns group ( NXOpen.TaggedObject): .
        """
        pass
    def RemoveMemberFromGroup(self, prodIntGroup: NXOpen.TaggedObject, memberToRemove: NXOpen.TaggedObject) -> None:
        """
         Remove the member from the Product Interface Group. 
        """
        pass
    def RenameGroup(self, prodIntGroup: NXOpen.TaggedObject, groupName: str) -> None:
        """
         Rename the Product Interface Group 
        """
        pass
    def Ungroup(self, prodIntGroup: NXOpen.TaggedObject) -> None:
        """
         Ungroup the Product Interface Group. This will delete the group and members will be moved to the parent group. 
        """
        pass
import NXOpen
import NXOpen.Validate
class InterfaceObject(NXOpen.NXObject): 
    """ Represents a Product Interface Object Builder. It creates a product interface object """
    class InterfaceUsageType(Enum):
        """
        Members Include: 
         |Unknown|  usage type as unknown 
         |Output|  usage type as output 
         |Input|  usage type as input 
         |KeyPerformanceInterface|  usage type as key performance interface 

        """
        Unknown: int
        Output: int
        Input: int
        KeyPerformanceInterface: int
        @staticmethod
        def ValueOf(value: int) -> InterfaceObject.InterfaceUsageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InvalidState(Enum):
        """
        Members Include: 
         |Valid|  product interface has no issue 
         |Sleeping|  product interface is sleep 
         |IncorrectOrphan|  product interface is in an incorrect orphan state 
         |SelfReferenced|  product interface references itself 

        """
        Valid: int
        Sleeping: int
        IncorrectOrphan: int
        SelfReferenced: int
        @staticmethod
        def ValueOf(value: int) -> InterfaceObject.InvalidState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ObjectName(self) -> str:
        """
        Getter for property: (str) ObjectName
         Returns the name of the product interface object   
            
         
        """
        pass
    def BreakPIReferencingLinks(self, usageType: InterfaceObject.InterfaceUsageType) -> None:
        """
         Breaks referencing link of PI when usage type changes. When the product interface type changed to input or key performance interface. Break link feature and inter part expression referring to the product interface. 
        """
        pass
    def CheckProductInterfaceObject(self) -> InterfaceObject.InvalidState:
        """
         Check the invalid state of product interface object 
         Returns state ( InterfaceObject.InvalidState NXOpen.Assemblie):  The state of product interface object .
        """
        pass
    def FixInvalidProductInterfaceObject(self) -> bool:
        """
         Fix the invalid state of product interface object 
         Returns fixed (bool):  if true the product interface has an issue and is fixed .
        """
        pass
    def GetInterfaceUsageType(self) -> InterfaceObject.InterfaceUsageType:
        """
         Returns the usage type of the product interface object 
         Returns usageType ( InterfaceObject.InterfaceUsageType NXOpen.Assemblie):  usage type of the product interface object .
        """
        pass
    def GetProductInterfaceDefiningEntity(self) -> NXOpen.NXObject:
        """
         Returns the underlying NX object referenced by the input product interface object  
         Returns nx_item ( NXOpen.NXObject):  nx item referenced by the product interface .
        """
        pass
    def GetProductInterfaceObjectStatus(self) -> str:
        """
         Returns the status of the input product interface object  
         Returns product_interface_status (str):  status of the product interface object .
        """
        pass
    def GetProductInterfaceObjectType(self) -> str:
        """
         Returns the type of the input product interface object  
         Returns product_interface_type (str):  type of the product interface object .
        """
        pass
    def GetRelatedExpressions(self) -> List[NXOpen.NXObject]:
        """
         Returns all expressions related to the product interface object 
         Returns relatedExps ( NXOpen.NXObject Li):  expressions related to the product interface .
        """
        pass
    def GetRelatedPmis(self) -> List[NXOpen.NXObject]:
        """
         Returns all pmis related to the product interface object 
         Returns relatedPmis ( NXOpen.NXObject Li):  pmis related to the product interface .
        """
        pass
    def GetUserComments(self) -> str:
        """
         Returns the user comments on the input product interface object 
         Returns user_comments (str):  user comments on the product interface object .
        """
        pass
    def InsertRelatedExpressions(self, relatedExps: List[NXOpen.NXObject]) -> None:
        """
         Relate expressions to the product interface 
        """
        pass
    def InsertRelatedPmis(self, relatedPmis: List[NXOpen.NXObject]) -> None:
        """
         Relate pmis to the product interface 
        """
        pass
    def InsertRelatedRequirement(self, relatedReq: NXOpen.Validate.Requirement) -> None:
        """
         Relate unvalidated Requirement to the product interface 
        """
        pass
    def RemoveAllRelatedExpressions(self) -> int:
        """
         Removes all related expressions from the product interface object 
         Returns removed (int):  number of expressions removed .
        """
        pass
    def RemoveAllRelatedPmis(self) -> int:
        """
         Removes all related pmis from the product interface object 
         Returns removed (int):  number of pmis removed .
        """
        pass
    def RemoveProductInterfaceObject(self) -> None:
        """
         Removes an object from the product interface set; currently supported types are expressions and geometry  
        """
        pass
    def RemoveRelatedExpression(self, relatedExp: NXOpen.NXObject) -> None:
        """
         Removes related expression from the product interface object 
        """
        pass
    def RemoveRelatedPmi(self, relatedPmi: NXOpen.NXObject) -> None:
        """
         Removes related pmis from the product interface object 
        """
        pass
    def RemoveRelatedRequirement(self, relatedReq: NXOpen.Validate.Requirement) -> None:
        """
         Removes related Requirement from the product interface object 
        """
        pass
    def RenameProductInterfaceObject(self, name: str) -> None:
        """
         Renames an object from the product interface set 
        """
        pass
    def SetInterfaceUsageType(self, usageType: InterfaceObject.InterfaceUsageType) -> None:
        """
         Sets the usage type on the product interface object 
        """
        pass
    def SetUserComments(self, user_comments: str) -> None:
        """
         Sets the user comments on the input product interface object 
        """
        pass
import NXOpen
import NXOpen.Features
class ObjectBuilder(NXOpen.Builder): 
    """ Represents a Product Interface Object Builder. It creates a set of product interface objects """
    class BuilderVersion(Enum):
        """
        Members Include: 
         |Original|  linked feature cannot select the product interface item 
         |One|  linked feature can directly select the product interface item 
         |Two|  product interface builder supports composite curve, composite face and body collector options 
         |Three|  Enables product interface types but used along with the 'Enable Product Interface Type' customer default 

        """
        Original: int
        One: int
        Two: int
        Three: int
        @staticmethod
        def ValueOf(value: int) -> ObjectBuilder.BuilderVersion:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Mate(Enum):
        """
        Members Include: 
         |NoCheck|  no checking for product interface objects 
         |Warn|  warn user while using non product interface objects 
         |Prevent|  restrict user from using non product interface objects 

        """
        NoCheck: int
        Warn: int
        Prevent: int
        @staticmethod
        def ValueOf(value: int) -> ObjectBuilder.Mate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Wave(Enum):
        """
        Members Include: 
         |NoCheck|  no checking for product interface objects 
         |Warn|  warn user while using non product interface objects 
         |Prevent|  restrict user from using non product interface objects 

        """
        NoCheck: int
        Warn: int
        Prevent: int
        @staticmethod
        def ValueOf(value: int) -> ObjectBuilder.Wave:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MateSetting(self) -> ObjectBuilder.Mate:
        """
        Getter for property: ( ObjectBuilder.Mate NXOpen.Assemblie) MateSetting
         Returns the current rule setting for use during creation of mating conditions   
            
         
        """
        pass
    @MateSetting.setter
    def MateSetting(self, mate_setting: ObjectBuilder.Mate):
        """
        Setter for property: ( ObjectBuilder.Mate NXOpen.Assemblie) MateSetting
         Returns the current rule setting for use during creation of mating conditions   
            
         
        """
        pass
    @property
    def PartGeometryCopy(self) -> NXOpen.Features.PartGeometryCopyBuilder:
        """
        Getter for property: ( NXOpen.Features.PartGeometryCopyBuilder) PartGeometryCopy
         Returns the part geometry copy   
            
         
        """
        pass
    @property
    def WaveSetting(self) -> ObjectBuilder.Wave:
        """
        Getter for property: ( ObjectBuilder.Wave NXOpen.Assemblie) WaveSetting
         Returns the current rule setting for use during creation of WAVE geomtery and interpart expressions   
            
         
        """
        pass
    @WaveSetting.setter
    def WaveSetting(self, wave_setting: ObjectBuilder.Wave):
        """
        Setter for property: ( ObjectBuilder.Wave NXOpen.Assemblie) WaveSetting
         Returns the current rule setting for use during creation of WAVE geomtery and interpart expressions   
            
         
        """
        pass
    def AddProductInterface(self, nx_item: NXOpen.NXObject) -> Tuple[InterfaceObject, bool]:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry. If the object already exists, it becomes active.  
         Returns A tuple consisting of (prod_int_item, alreadyExisted). 
         - prod_int_item is:  InterfaceObject NXOpen.Assemblie. the product interface object created or modified .
         - alreadyExisted is: bool.

        """
        pass
    def AddProductInterfaceObject(self, nx_item: NXOpen.NXObject) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry  
         Returns prod_int_item ( InterfaceObject NXOpen.Assemblie):  the product interface object created .
        """
        pass
    def AddProductInterfaceObject1(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry  
         Returns productInterface ( InterfaceObject NXOpen.Assemblie):  the product interface object created .
        """
        pass
    def AddProductInterfaceObject2(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObject.InterfaceUsageType) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry. Interface Usage type can be set using this API.  
         Returns productInterface ( InterfaceObject NXOpen.Assemblie):  the product interface object created .
        """
        pass
    def AddProductInterfaceObject3(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObject.InterfaceUsageType, isGroupAsPIObject: bool) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry. Interface Usage type can be set and Group PI object can created using this API. 
         Returns productInterface ( InterfaceObject NXOpen.Assemblie):  the product interface object created .
        """
        pass
    def EditProductInterfaceObject(self, productInterface: InterfaceObject, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool) -> None:
        """
         Edits a product interface object  
        """
        pass
    def EditProductInterfaceObject1(self, productInterface: InterfaceObject, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObject.InterfaceUsageType) -> None:
        """
         Edits a product interface object with interface object type . Interface Usage type can be set using this API. 
        """
        pass
    def GetBuilderVersion(self) -> ObjectBuilder.BuilderVersion:
        """
         Gets the version of this builder. 
         Returns version ( ObjectBuilder.BuilderVersion NXOpen.Assemblie): .
        """
        pass
    def QueryProductInterfaceObjects(self, part: NXOpen.NXObject) -> List[InterfaceObject]:
        """
         Returns a list of product interface objects in the part 
         Returns prod_int_objs ( InterfaceObject List[NXOpen.Assembl):  objects in the product interface .
        """
        pass
    def RemoveProductInterfaceObject(self, prod_int_item: InterfaceObject) -> None:
        """
         Removes an object from the product interface; currently supported types are expressions and geometry  
        """
        pass
    def SetBuilderVersion(self, version: ObjectBuilder.BuilderVersion) -> None:
        """
         Sets the version of this builder. 
        """
        pass
    def SetUserComments(self, prod_int_item: InterfaceObject, user_comments: str) -> None:
        """
         Sets the user comments on the product interface item passed in  
        """
        pass
    def UpdateAttributesFromPart(self, part: NXOpen.NXObject) -> None:
        """
         Updates the attributes of the product interface items in the part  
        """
        pass
import NXOpen
class PropertyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Assemblies.ProductInterface.PropertyBuilder builder """
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of a product interface provided by users   
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description of a product interface provided by users   
            
         
        """
        pass
    @property
    def InterfaceUsageType(self) -> int:
        """
        Getter for property: (int) InterfaceUsageType
         Returns the interface type of a product interface provided by users   
            
         
        """
        pass
    @InterfaceUsageType.setter
    def InterfaceUsageType(self, interfaceUsageType: int):
        """
        Setter for property: (int) InterfaceUsageType
         Returns the interface type of a product interface provided by users   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of a product interface provided by users   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of a product interface provided by users   
            
         
        """
        pass
