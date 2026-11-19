from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class represents the collection of product interface objects  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class Collection(NXOpen.Object): 
    """ This class represents the collection of product interface objects """


    ##  Add the member to the Product Interface Group. It will not be removed from any of the existing group.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="productInterfaceObject"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="selectedGroups"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  items in list </param>
    def AddMemberToGroups(self, productInterfaceObject: NXOpen.TaggedObject, selectedGroups: List[NXOpen.TaggedObject]) -> None:
        """
         Add the member to the Product Interface Group. It will not be removed from any of the existing group.
        """
        pass
    
    ##  Create Product Interface Object Builder 
    ##  @return builder (@link ObjectBuilder NXOpen.Assemblies.ProductInterface.ObjectBuilder@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.1.  Please use @link NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithVersion NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithVersion@endlink  instead.  <br> 

    ## License requirements: None.
    def CreateObjectBuilder(self) -> ObjectBuilder:
        """
         Create Product Interface Object Builder 
         @return builder (@link ObjectBuilder NXOpen.Assemblies.ProductInterface.ObjectBuilder@endlink): .
        """
        pass
    
    ##  Create Product Interface Object Builder with @link NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion@endlink 
    ##  @return builder (@link ObjectBuilder NXOpen.Assemblies.ProductInterface.ObjectBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="version"> (@link ObjectBuilder.BuilderVersion NXOpen.Assemblies.ProductInterface.ObjectBuilder.BuilderVersion@endlink) </param>
    def CreateObjectBuilderWithBuilderVersion(self, version: ObjectBuilder.BuilderVersion) -> ObjectBuilder:
        """
         Create Product Interface Object Builder with @link NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion@endlink 
         @return builder (@link ObjectBuilder NXOpen.Assemblies.ProductInterface.ObjectBuilder@endlink): .
        """
        pass
    
    ##  Create Product Interface Object Builder with version
    ##  @return builder (@link ObjectBuilder NXOpen.Assemblies.ProductInterface.ObjectBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1872.0.0.  Please use @link NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="version"> (int)  Please see the definition at @link NXOpen::Assemblies::ProductInterface::ObjectBuilder::BuilderVersion NXOpen::Assemblies::ProductInterface::ObjectBuilder::BuilderVersion@endlink  </param>
    def CreateObjectBuilderWithVersion(self, version: int) -> ObjectBuilder:
        """
         Create Product Interface Object Builder with version
         @return builder (@link ObjectBuilder NXOpen.Assemblies.ProductInterface.ObjectBuilder@endlink): .
        """
        pass
    
    ##  Create Product Interface Property Builder 
    ##  @return builder (@link PropertyBuilder NXOpen.Assemblies.ProductInterface.PropertyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def CreatePropertyBuilder(self) -> PropertyBuilder:
        """
         Create Product Interface Property Builder 
         @return builder (@link PropertyBuilder NXOpen.Assemblies.ProductInterface.PropertyBuilder@endlink): .
        """
        pass
    
    ##  Delete the Product Interface Group. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prodIntGroup"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="deleteWithMembers"> (bool) </param>
    def DeleteGroup(self, prodIntGroup: NXOpen.TaggedObject, deleteWithMembers: bool) -> None:
        """
         Delete the Product Interface Group. 
        """
        pass
    
    ##  Find the Product Interface Object with input name 
    ##  @return found (@link NXOpen.NXObject NXOpen.NXObject@endlink):  Product Interface Object with this identifier .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Identifier of the product interface object you want </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.NXObject:
        """
         Find the Product Interface Object with input name 
         @return found (@link NXOpen.NXObject NXOpen.NXObject@endlink):  Product Interface Object with this identifier .
        """
        pass
    
    ##  Return the Product Interface Group name 
    ##  @return groupName (str): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prodIntGroup"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def GetGroupName(self, prodIntGroup: NXOpen.TaggedObject) -> str:
        """
         Return the Product Interface Group name 
         @return groupName (str): .
        """
        pass
    
    ##  Returns all the product interface objects in the part 
    ##  @return interface_objects (@link InterfaceObject List[NXOpen.Assemblies.ProductInterface.InterfaceObject]@endlink):  product interface objects in the part .
    ## 
    ##   <br>  Created in NX10.0.2  <br> 

    ## License requirements: None.
    def GetProductInterfaces(self) -> List[InterfaceObject]:
        """
         Returns all the product interface objects in the part 
         @return interface_objects (@link InterfaceObject List[NXOpen.Assemblies.ProductInterface.InterfaceObject]@endlink):  product interface objects in the part .
        """
        pass
    
    ##  Move the member to the Product Interface Group. It will removed from the old group and added to the new group.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prodIntGroup"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="memberToMove"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def MoveMemberToGroup(self, prodIntGroup: NXOpen.TaggedObject, memberToMove: NXOpen.TaggedObject) -> None:
        """
         Move the member to the Product Interface Group. It will removed from the old group and added to the new group.
        """
        pass
    
    ##  Creates the Product Interface Group in the part 
    ##  @return group (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def NewGroup(self) -> NXOpen.TaggedObject:
        """
         Creates the Product Interface Group in the part 
         @return group (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
        """
        pass
    
    ##  Remove the member from the Product Interface Group. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prodIntGroup"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="memberToRemove"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def RemoveMemberFromGroup(self, prodIntGroup: NXOpen.TaggedObject, memberToRemove: NXOpen.TaggedObject) -> None:
        """
         Remove the member from the Product Interface Group. 
        """
        pass
    
    ##  Rename the Product Interface Group 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prodIntGroup"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="groupName"> (str) </param>
    def RenameGroup(self, prodIntGroup: NXOpen.TaggedObject, groupName: str) -> None:
        """
         Rename the Product Interface Group 
        """
        pass
    
    ##  Ungroup the Product Interface Group. This will delete the group and members will be moved to the parent group. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prodIntGroup"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def Ungroup(self, prodIntGroup: NXOpen.TaggedObject) -> None:
        """
         Ungroup the Product Interface Group. This will delete the group and members will be moved to the parent group. 
        """
        pass
    
import NXOpen
import NXOpen.Validate
##  Represents a Product Interface Object Builder. It creates a product interface object  <br> To create a new instance of this class, use @link NXOpen::Assemblies::ProductInterface::ObjectBuilder::AddProductInterfaceObject  NXOpen::Assemblies::ProductInterface::ObjectBuilder::AddProductInterfaceObject @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class InterfaceObject(NXOpen.NXObject): 
    """ Represents a Product Interface Object Builder. It creates a product interface object """


    ##  An enum representing product interface usage types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  usage type as unknown </description> </item><item><term> 
    ## Output</term><description> 
    ##  usage type as output </description> </item><item><term> 
    ## Input</term><description> 
    ##  usage type as input </description> </item><item><term> 
    ## KeyPerformanceInterface</term><description> 
    ##  usage type as key performance interface </description> </item></list>
    class InterfaceUsageType(Enum):
        """
        Members Include: <Unknown> <Output> <Input> <KeyPerformanceInterface>
        """
        Unknown: int
        Output: int
        Input: int
        KeyPerformanceInterface: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InterfaceObject.InterfaceUsageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Invalid state of problematic product interface object 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Valid</term><description> 
    ##  product interface has no issue </description> </item><item><term> 
    ## Sleeping</term><description> 
    ##  product interface is sleep </description> </item><item><term> 
    ## IncorrectOrphan</term><description> 
    ##  product interface is in an incorrect orphan state </description> </item><item><term> 
    ## SelfReferenced</term><description> 
    ##  product interface references itself </description> </item></list>
    class InvalidState(Enum):
        """
        Members Include: <Valid> <Sleeping> <IncorrectOrphan> <SelfReferenced>
        """
        Valid: int
        Sleeping: int
        IncorrectOrphan: int
        SelfReferenced: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InterfaceObject.InvalidState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ObjectName
    ##  Returns the name of the product interface object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def ObjectName(self) -> str:
        """
        Getter for property: (str) ObjectName
         Returns the name of the product interface object   
            
         
        """
        pass
    
    ##  Breaks referencing link of PI when usage type changes. When the product interface type changed to input or key performance interface. Break link feature and inter part expression referring to the product interface. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="usageType"> (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink)  usage type to be set on the product interface object </param>
    def BreakPIReferencingLinks(self, usageType: InterfaceObject.InterfaceUsageType) -> None:
        """
         Breaks referencing link of PI when usage type changes. When the product interface type changed to input or key performance interface. Break link feature and inter part expression referring to the product interface. 
        """
        pass
    
    ##  Check the invalid state of product interface object 
    ##  @return state (@link InterfaceObject.InvalidState NXOpen.Assemblies.ProductInterface.InterfaceObject.InvalidState@endlink):  The state of product interface object .
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: None.
    def CheckProductInterfaceObject(self) -> InterfaceObject.InvalidState:
        """
         Check the invalid state of product interface object 
         @return state (@link InterfaceObject.InvalidState NXOpen.Assemblies.ProductInterface.InterfaceObject.InvalidState@endlink):  The state of product interface object .
        """
        pass
    
    ##  Fix the invalid state of product interface object 
    ##  @return fixed (bool):  if true the product interface has an issue and is fixed .
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: None.
    def FixInvalidProductInterfaceObject(self) -> bool:
        """
         Fix the invalid state of product interface object 
         @return fixed (bool):  if true the product interface has an issue and is fixed .
        """
        pass
    
    ##  Returns the usage type of the product interface object 
    ##  @return usageType (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink):  usage type of the product interface object .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetInterfaceUsageType(self) -> InterfaceObject.InterfaceUsageType:
        """
         Returns the usage type of the product interface object 
         @return usageType (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink):  usage type of the product interface object .
        """
        pass
    
    ##  Returns the underlying NX object referenced by the input product interface object  
    ##  @return nx_item (@link NXOpen.NXObject NXOpen.NXObject@endlink):  nx item referenced by the product interface .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: None.
    def GetProductInterfaceDefiningEntity(self) -> NXOpen.NXObject:
        """
         Returns the underlying NX object referenced by the input product interface object  
         @return nx_item (@link NXOpen.NXObject NXOpen.NXObject@endlink):  nx item referenced by the product interface .
        """
        pass
    
    ##  Returns the status of the input product interface object  
    ##  @return product_interface_status (str):  status of the product interface object .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: None.
    def GetProductInterfaceObjectStatus(self) -> str:
        """
         Returns the status of the input product interface object  
         @return product_interface_status (str):  status of the product interface object .
        """
        pass
    
    ##  Returns the type of the input product interface object  
    ##  @return product_interface_type (str):  type of the product interface object .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: None.
    def GetProductInterfaceObjectType(self) -> str:
        """
         Returns the type of the input product interface object  
         @return product_interface_type (str):  type of the product interface object .
        """
        pass
    
    ##  Returns all expressions related to the product interface object 
    ##  @return relatedExps (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  expressions related to the product interface .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetRelatedExpressions(self) -> List[NXOpen.NXObject]:
        """
         Returns all expressions related to the product interface object 
         @return relatedExps (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  expressions related to the product interface .
        """
        pass
    
    ##  Returns all pmis related to the product interface object 
    ##  @return relatedPmis (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  pmis related to the product interface .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetRelatedPmis(self) -> List[NXOpen.NXObject]:
        """
         Returns all pmis related to the product interface object 
         @return relatedPmis (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  pmis related to the product interface .
        """
        pass
    
    ##  Returns the user comments on the input product interface object 
    ##  @return user_comments (str):  user comments on the product interface object .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: None.
    def GetUserComments(self) -> str:
        """
         Returns the user comments on the input product interface object 
         @return user_comments (str):  user comments on the product interface object .
        """
        pass
    
    ##  Relate expressions to the product interface 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relatedExps"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Expressions to relate to the product interface </param>
    def InsertRelatedExpressions(self, relatedExps: List[NXOpen.NXObject]) -> None:
        """
         Relate expressions to the product interface 
        """
        pass
    
    ##  Relate pmis to the product interface 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relatedPmis"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Pmis to relate to the product interface </param>
    def InsertRelatedPmis(self, relatedPmis: List[NXOpen.NXObject]) -> None:
        """
         Relate pmis to the product interface 
        """
        pass
    
    ##  Relate unvalidated Requirement to the product interface 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relatedReq"> (@link NXOpen.Validate.Requirement NXOpen.Validate.Requirement@endlink)  Requirement to relate to the product interface </param>
    def InsertRelatedRequirement(self, relatedReq: NXOpen.Validate.Requirement) -> None:
        """
         Relate unvalidated Requirement to the product interface 
        """
        pass
    
    ##  Removes all related expressions from the product interface object 
    ##  @return removed (int):  number of expressions removed .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def RemoveAllRelatedExpressions(self) -> int:
        """
         Removes all related expressions from the product interface object 
         @return removed (int):  number of expressions removed .
        """
        pass
    
    ##  Removes all related pmis from the product interface object 
    ##  @return removed (int):  number of pmis removed .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def RemoveAllRelatedPmis(self) -> int:
        """
         Removes all related pmis from the product interface object 
         @return removed (int):  number of pmis removed .
        """
        pass
    
    ##  Removes an object from the product interface set; currently supported types are expressions and geometry  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def RemoveProductInterfaceObject(self) -> None:
        """
         Removes an object from the product interface set; currently supported types are expressions and geometry  
        """
        pass
    
    ##  Removes related expression from the product interface object 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relatedExp"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  the expression to have a relation to product inerface </param>
    def RemoveRelatedExpression(self, relatedExp: NXOpen.NXObject) -> None:
        """
         Removes related expression from the product interface object 
        """
        pass
    
    ##  Removes related pmis from the product interface object 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relatedPmi"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  the Pmi to have a relation to product inerface </param>
    def RemoveRelatedPmi(self, relatedPmi: NXOpen.NXObject) -> None:
        """
         Removes related pmis from the product interface object 
        """
        pass
    
    ##  Removes related Requirement from the product interface object 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relatedReq"> (@link NXOpen.Validate.Requirement NXOpen.Validate.Requirement@endlink)  the Requirement to have a relation to product inerface </param>
    def RemoveRelatedRequirement(self, relatedReq: NXOpen.Validate.Requirement) -> None:
        """
         Removes related Requirement from the product interface object 
        """
        pass
    
    ##  Renames an object from the product interface set 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="name"> (str)  user defined name to be set on the product interface object, if it is empty reset it to default name </param>
    def RenameProductInterfaceObject(self, name: str) -> None:
        """
         Renames an object from the product interface set 
        """
        pass
    
    ##  Sets the usage type on the product interface object 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="usageType"> (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink)  usage type to be set on the product interface object </param>
    def SetInterfaceUsageType(self, usageType: InterfaceObject.InterfaceUsageType) -> None:
        """
         Sets the usage type on the product interface object 
        """
        pass
    
    ##  Sets the user comments on the input product interface object 
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="user_comments"> (str)  user comments to be set on the product interface object </param>
    def SetUserComments(self, user_comments: str) -> None:
        """
         Sets the user comments on the input product interface object 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Product Interface Object Builder. It creates a set of product interface objects  <br> To create a new instance of this class, use @link NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion  NXOpen::Assemblies::ProductInterface::Collection::CreateObjectBuilderWithBuilderVersion @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## PartGeometryCopy.ObjectType </term> <description> 
##  
## BodyCollector </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX5.0.0  <br> 

class ObjectBuilder(NXOpen.Builder): 
    """ Represents a Product Interface Object Builder. It creates a set of product interface objects """


    ##  Version number of product interface builder. The new version is added when new function is added to the product interface.
    ##                 The old versions are kept since user can still use the old recorded NXOpen function.
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Original</term><description> 
    ##  linked feature cannot select the product interface item </description> </item><item><term> 
    ## One</term><description> 
    ##  linked feature can directly select the product interface item </description> </item><item><term> 
    ## Two</term><description> 
    ##  product interface builder supports composite curve, composite face and body collector options </description> </item><item><term> 
    ## Three</term><description> 
    ##  Enables product interface types but used along with the 'Enable Product Interface Type' customer default </description> </item></list>
    class BuilderVersion(Enum):
        """
        Members Include: <Original> <One> <Two> <Three>
        """
        Original: int
        One: int
        Two: int
        Three: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ObjectBuilder.BuilderVersion:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  An enum representing the settings available for rule checking during creation of mating conditions  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoCheck</term><description> 
    ##  no checking for product interface objects </description> </item><item><term> 
    ## Warn</term><description> 
    ##  warn user while using non product interface objects </description> </item><item><term> 
    ## Prevent</term><description> 
    ##  restrict user from using non product interface objects </description> </item></list>
    class Mate(Enum):
        """
        Members Include: <NoCheck> <Warn> <Prevent>
        """
        NoCheck: int
        Warn: int
        Prevent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ObjectBuilder.Mate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  An enum representing settings available for rule checking during creation of WAVE geomtery and interpart expressions  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoCheck</term><description> 
    ##  no checking for product interface objects </description> </item><item><term> 
    ## Warn</term><description> 
    ##  warn user while using non product interface objects </description> </item><item><term> 
    ## Prevent</term><description> 
    ##  restrict user from using non product interface objects </description> </item></list>
    class Wave(Enum):
        """
        Members Include: <NoCheck> <Warn> <Prevent>
        """
        NoCheck: int
        Warn: int
        Prevent: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ObjectBuilder.Wave:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ObjectBuilder.Mate NXOpen.Assemblies.ProductInterface.ObjectBuilder.Mate@endlink) MateSetting
    ##  Returns the current rule setting for use during creation of mating conditions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ObjectBuilder.Mate
    @property
    def MateSetting(self) -> ObjectBuilder.Mate:
        """
        Getter for property: (@link ObjectBuilder.Mate NXOpen.Assemblies.ProductInterface.ObjectBuilder.Mate@endlink) MateSetting
         Returns the current rule setting for use during creation of mating conditions   
            
         
        """
        pass
    
    ## Setter for property: (@link ObjectBuilder.Mate NXOpen.Assemblies.ProductInterface.ObjectBuilder.Mate@endlink) MateSetting

    ##  Returns the current rule setting for use during creation of mating conditions   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MateSetting.setter
    def MateSetting(self, mate_setting: ObjectBuilder.Mate):
        """
        Setter for property: (@link ObjectBuilder.Mate NXOpen.Assemblies.ProductInterface.ObjectBuilder.Mate@endlink) MateSetting
         Returns the current rule setting for use during creation of mating conditions   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.PartGeometryCopyBuilder NXOpen.Features.PartGeometryCopyBuilder@endlink) PartGeometryCopy
    ##  Returns the part geometry copy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Features.PartGeometryCopyBuilder
    @property
    def PartGeometryCopy(self) -> NXOpen.Features.PartGeometryCopyBuilder:
        """
        Getter for property: (@link NXOpen.Features.PartGeometryCopyBuilder NXOpen.Features.PartGeometryCopyBuilder@endlink) PartGeometryCopy
         Returns the part geometry copy   
            
         
        """
        pass
    
    ## Getter for property: (@link ObjectBuilder.Wave NXOpen.Assemblies.ProductInterface.ObjectBuilder.Wave@endlink) WaveSetting
    ##  Returns the current rule setting for use during creation of WAVE geomtery and interpart expressions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ObjectBuilder.Wave
    @property
    def WaveSetting(self) -> ObjectBuilder.Wave:
        """
        Getter for property: (@link ObjectBuilder.Wave NXOpen.Assemblies.ProductInterface.ObjectBuilder.Wave@endlink) WaveSetting
         Returns the current rule setting for use during creation of WAVE geomtery and interpart expressions   
            
         
        """
        pass
    
    ## Setter for property: (@link ObjectBuilder.Wave NXOpen.Assemblies.ProductInterface.ObjectBuilder.Wave@endlink) WaveSetting

    ##  Returns the current rule setting for use during creation of WAVE geomtery and interpart expressions   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @WaveSetting.setter
    def WaveSetting(self, wave_setting: ObjectBuilder.Wave):
        """
        Setter for property: (@link ObjectBuilder.Wave NXOpen.Assemblies.ProductInterface.ObjectBuilder.Wave@endlink) WaveSetting
         Returns the current rule setting for use during creation of WAVE geomtery and interpart expressions   
            
         
        """
        pass
    
    ##  Adds an object to the product interface; currently supported types are expressions and geometry. If the object already exists, it becomes active.  
    ##  @return A tuple consisting of (prod_int_item, alreadyExisted). 
    ##  - prod_int_item is: @link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink. the product interface object created or modified .
    ##  - alreadyExisted is: bool.

    ## 
    ##   <br>  Created in NX8.5.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nx_item"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  nx item to be added to the product interface </param>
    def AddProductInterface(self, nx_item: NXOpen.NXObject) -> Tuple[InterfaceObject, bool]:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry. If the object already exists, it becomes active.  
         @return A tuple consisting of (prod_int_item, alreadyExisted). 
         - prod_int_item is: @link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink. the product interface object created or modified .
         - alreadyExisted is: bool.

        """
        pass
    
    ##  Adds an object to the product interface; currently supported types are expressions and geometry  
    ##  @return prod_int_item (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nx_item"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  nx item to be added to the product interface </param>
    def AddProductInterfaceObject(self, nx_item: NXOpen.NXObject) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry  
         @return prod_int_item (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
        """
        pass
    
    ##  Adds an object to the product interface; currently supported types are expressions and geometry  
    ##  @return productInterface (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nxObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Selected object to add </param>
    ## <param name="name"> (str)  User defined name of selected object </param>
    ## <param name="description"> (str)  User comments of selected object </param>
    ## <param name="reverseDirection"> (bool)  Flag to specify whether to reverse the direction of the source object </param>
    def AddProductInterfaceObject1(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry  
         @return productInterface (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
        """
        pass
    
    ##  Adds an object to the product interface; currently supported types are expressions and geometry. Interface Usage type can be set using this API.  
    ##  @return productInterface (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nxObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Selected object to add </param>
    ## <param name="name"> (str)  User defined name of selected object </param>
    ## <param name="description"> (str)  User comments of selected object </param>
    ## <param name="reverseDirection"> (bool)  Flag to specify whether to reverse the direction of the source object </param>
    ## <param name="interfaceUsageType"> (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink)  Usage type of product interface object </param>
    def AddProductInterfaceObject2(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObject.InterfaceUsageType) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry. Interface Usage type can be set using this API.  
         @return productInterface (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
        """
        pass
    
    ##  Adds an object to the product interface; currently supported types are expressions and geometry. Interface Usage type can be set and Group PI object can created using this API. 
    ##  @return productInterface (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nxObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Selected object to add </param>
    ## <param name="name"> (str)  User defined name of selected object </param>
    ## <param name="description"> (str)  User comments of selected object </param>
    ## <param name="reverseDirection"> (bool)  Flag to specify whether to reverse the direction of the source object </param>
    ## <param name="interfaceUsageType"> (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink)  Usage type of product interface object </param>
    ## <param name="isGroupAsPIObject"> (bool)   whether to create Group PI object or use it in body collector. </param>
    def AddProductInterfaceObject3(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObject.InterfaceUsageType, isGroupAsPIObject: bool) -> InterfaceObject:
        """
         Adds an object to the product interface; currently supported types are expressions and geometry. Interface Usage type can be set and Group PI object can created using this API. 
         @return productInterface (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink):  the product interface object created .
        """
        pass
    
    ##  Edits a product interface object  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="productInterface"> (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink)  Product interface object to be edited </param>
    ## <param name="nxObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Selected object to add </param>
    ## <param name="name"> (str)  User defined name of selected object </param>
    ## <param name="description"> (str)  User comments of selected object </param>
    ## <param name="reverseDirection"> (bool)  Flag to specify whether to reverse the direction of the source object </param>
    def EditProductInterfaceObject(self, productInterface: InterfaceObject, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool) -> None:
        """
         Edits a product interface object  
        """
        pass
    
    ##  Edits a product interface object with interface object type . Interface Usage type can be set using this API. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="productInterface"> (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink)  Product interface object to be edited </param>
    ## <param name="nxObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Selected object to add </param>
    ## <param name="name"> (str)  User defined name of selected object </param>
    ## <param name="description"> (str)  User comments of selected object </param>
    ## <param name="reverseDirection"> (bool)  Flag to specify whether to reverse the direction of the source object </param>
    ## <param name="interfaceUsageType"> (@link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink)  Usage type of product interface object </param>
    def EditProductInterfaceObject1(self, productInterface: InterfaceObject, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObject.InterfaceUsageType) -> None:
        """
         Edits a product interface object with interface object type . Interface Usage type can be set using this API. 
        """
        pass
    
    ##  Gets the version of this builder. 
    ##  @return version (@link ObjectBuilder.BuilderVersion NXOpen.Assemblies.ProductInterface.ObjectBuilder.BuilderVersion@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetBuilderVersion(self) -> ObjectBuilder.BuilderVersion:
        """
         Gets the version of this builder. 
         @return version (@link ObjectBuilder.BuilderVersion NXOpen.Assemblies.ProductInterface.ObjectBuilder.BuilderVersion@endlink): .
        """
        pass
    
    ##  Returns a list of product interface objects in the part 
    ##  @return prod_int_objs (@link InterfaceObject List[NXOpen.Assemblies.ProductInterface.InterfaceObject]@endlink):  objects in the product interface .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  part whose product interface objects have to be queried </param>
    def QueryProductInterfaceObjects(self, part: NXOpen.NXObject) -> List[InterfaceObject]:
        """
         Returns a list of product interface objects in the part 
         @return prod_int_objs (@link InterfaceObject List[NXOpen.Assemblies.ProductInterface.InterfaceObject]@endlink):  objects in the product interface .
        """
        pass
    
    ##  Removes an object from the product interface; currently supported types are expressions and geometry  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prod_int_item"> (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink)  product interface object to be removed from the product interface set</param>
    def RemoveProductInterfaceObject(self, prod_int_item: InterfaceObject) -> None:
        """
         Removes an object from the product interface; currently supported types are expressions and geometry  
        """
        pass
    
    ##  Sets the version of this builder. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="version"> (@link ObjectBuilder.BuilderVersion NXOpen.Assemblies.ProductInterface.ObjectBuilder.BuilderVersion@endlink) </param>
    def SetBuilderVersion(self, version: ObjectBuilder.BuilderVersion) -> None:
        """
         Sets the version of this builder. 
        """
        pass
    
    ##  Sets the user comments on the product interface item passed in  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prod_int_item"> (@link InterfaceObject NXOpen.Assemblies.ProductInterface.InterfaceObject@endlink)  product interface item on which the user comments have to set </param>
    ## <param name="user_comments"> (str)  user comments to be set on specified product interface item </param>
    def SetUserComments(self, prod_int_item: InterfaceObject, user_comments: str) -> None:
        """
         Sets the user comments on the product interface item passed in  
        """
        pass
    
    ##  Updates the attributes of the product interface items in the part  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  part, product interface objects of which need to have their  attributes updated </param>
    def UpdateAttributesFromPart(self, part: NXOpen.NXObject) -> None:
        """
         Updates the attributes of the product interface items in the part  
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Assemblies::ProductInterface::PropertyBuilder NXOpen::Assemblies::ProductInterface::PropertyBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Assemblies::ProductInterface::Collection::CreatePropertyBuilder  NXOpen::Assemblies::ProductInterface::Collection::CreatePropertyBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class PropertyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Assemblies.ProductInterface.PropertyBuilder</ja_class> builder """


    ## Getter for property: (str) Description
    ##  Returns the description of a product interface provided by users   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of a product interface provided by users   
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##  Returns the description of a product interface provided by users   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the description of a product interface provided by users   
            
         
        """
        pass
    
    ## Getter for property: (int) InterfaceUsageType
    ##  Returns the interface type of a product interface provided by users   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def InterfaceUsageType(self) -> int:
        """
        Getter for property: (int) InterfaceUsageType
         Returns the interface type of a product interface provided by users   
            
         
        """
        pass
    
    ## Setter for property: (int) InterfaceUsageType

    ##  Returns the interface type of a product interface provided by users   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @InterfaceUsageType.setter
    def InterfaceUsageType(self, interfaceUsageType: int):
        """
        Setter for property: (int) InterfaceUsageType
         Returns the interface type of a product interface provided by users   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name of a product interface provided by users   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of a product interface provided by users   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name of a product interface provided by users   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of a product interface provided by users   
            
         
        """
        pass
    
## @package NXOpen.Assemblies.ProductInterface
## Classes, Enums and Structs under NXOpen.Assemblies.ProductInterface namespace

##  @link InterfaceObjectInterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObjectInterfaceUsageType @endlink is an alias for @link InterfaceObject.InterfaceUsageType NXOpen.Assemblies.ProductInterface.InterfaceObject.InterfaceUsageType@endlink
InterfaceObjectInterfaceUsageType = InterfaceObject.InterfaceUsageType


##  @link InterfaceObjectInvalidState NXOpen.Assemblies.ProductInterface.InterfaceObjectInvalidState @endlink is an alias for @link InterfaceObject.InvalidState NXOpen.Assemblies.ProductInterface.InterfaceObject.InvalidState@endlink
InterfaceObjectInvalidState = InterfaceObject.InvalidState


##  @link ObjectBuilderBuilderVersion NXOpen.Assemblies.ProductInterface.ObjectBuilderBuilderVersion @endlink is an alias for @link ObjectBuilder.BuilderVersion NXOpen.Assemblies.ProductInterface.ObjectBuilder.BuilderVersion@endlink
ObjectBuilderBuilderVersion = ObjectBuilder.BuilderVersion


##  @link ObjectBuilderMate NXOpen.Assemblies.ProductInterface.ObjectBuilderMate @endlink is an alias for @link ObjectBuilder.Mate NXOpen.Assemblies.ProductInterface.ObjectBuilder.Mate@endlink
ObjectBuilderMate = ObjectBuilder.Mate


##  @link ObjectBuilderWave NXOpen.Assemblies.ProductInterface.ObjectBuilderWave @endlink is an alias for @link ObjectBuilder.Wave NXOpen.Assemblies.ProductInterface.ObjectBuilder.Wave@endlink
ObjectBuilderWave = ObjectBuilder.Wave


