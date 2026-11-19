from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class represents a part family attribute       
##      <br> Use @link PartFamily::TemplateManager::GetPartFamilyAttribute PartFamily::TemplateManager::GetPartFamilyAttribute@endlink  to get an instance of this class.
##                            This method will not create a new part family attribute. It will only return attribute that is already created.
##                            To create a new attribute, use @link PartFamily::TemplateManager::AddToChosenAttributes PartFamily::TemplateManager::AddToChosenAttributes@endlink , which
##                            will create an attribute and add to chosen attributes list on template manager. It is not allowed to create
##                            a standalone attribute that is not added to chosen attributes list.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class FamilyAttribute(NXOpen.NXObject): 
    """ This class represents a part family attribute       
    """


    ##  The part family attribute types.
    ##             These should always be in synch with the UF_fam_attr_types 
    ##          
    ##  text attribute 
    class AttrType(Enum):
        """
        Members Include: <Text> <Numeric> <Integer> <Double> <String> <Part> <Name> <Instance> <Expression> <Mirror> <Density> <Feature> <Mass> <Material> <Cofm> <Undefined>
        """
        Text: int
        Numeric: int
        Integer: int
        Double: int
        String: int
        Part: int
        Name: int
        Instance: int
        Expression: int
        Mirror: int
        Density: int
        Feature: int
        Mass: int
        Material: int
        Cofm: int
        Undefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FamilyAttribute.AttrType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsOptional
    ##   a value indicating whether the attribute is an optional attribute.  
    ##   
    ##             This could be an optional creation non key attribute or an optional key attribute
    ##           
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IsOptional(self) -> bool:
        """
        Getter for property: (bool) IsOptional
          a value indicating whether the attribute is an optional attribute.  
          
                    This could be an optional creation non key attribute or an optional key attribute
                  
         
        """
        pass
    
    ## Getter for property: (bool) IsRequired
    ##   a value indicating whether the attribute is a required attribute.  
    ##   
    ##             This could be a required creation non key attribute or a required key attribute
    ##           
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IsRequired(self) -> bool:
        """
        Getter for property: (bool) IsRequired
          a value indicating whether the attribute is a required attribute.  
          
                    This could be a required creation non key attribute or a required key attribute
                  
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of the given attribute   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of the given attribute   
            
         
        """
        pass
    
    ## Getter for property: (@link FamilyAttribute.AttrType NXOpen.PartFamily.FamilyAttribute.AttrType@endlink) Type
    ##   the type of the given attribute   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FamilyAttribute.AttrType
    @property
    def Type(self) -> FamilyAttribute.AttrType:
        """
        Getter for property: (@link FamilyAttribute.AttrType NXOpen.PartFamily.FamilyAttribute.AttrType@endlink) Type
          the type of the given attribute   
            
         
        """
        pass
    
    ## Getter for property: (str) Value
    ##   the value of the given attribute   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
          the value of the given attribute   
            
         
        """
        pass
    
    ## Getter for property: (int) Version
    ##   the version of the given attribute   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
          the version of the given attribute   
            
         
        """
        pass
    
import NXOpen
##  This class repesents a part family table record (or instance definition on the template) and is 
##         created/deleted by @link PartFamily::TemplateManager PartFamily::TemplateManager@endlink .         
##       <br> Use @link PartFamily::TemplateManager::AddInstanceDefinition PartFamily::TemplateManager::AddInstanceDefinition@endlink  to create a new instance defintion.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class InstanceDefinition(NXOpen.TransientObject): 
    """ This class repesents a part family table record (or instance definition on the template) and is 
        created/deleted by <ja_class>PartFamily.TemplateManager</ja_class>.         
     """


    ##  Free resources associated with the instance. After this method
    ##             is called, it is illegal to use the object.  In .NET, this method
    ##             is automatically called when the object is deleted by the garbage collector
    ##          
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(instanceDefinition: InstanceDefinition) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage collector
                 
        """
        pass
    
    ##  Get the value for passed atribute
    ##          
    ##  @return value (str): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="partFamAttr"> (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink) </param>
    def GetValueOfAttribute(instanceDefinition: InstanceDefinition, partFamAttr: FamilyAttribute) -> str:
        """
         Get the value for passed atribute
                 
         @return value (str): .
        """
        pass
    
    ##  Set the value for passed atribute with the value
    ##          
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="partFamAttr"> (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink) </param>
    ## <param name="value"> (str) </param>
    def SetValueOfAttribute(instanceDefinition: InstanceDefinition, partFamAttr: FamilyAttribute, value: str) -> None:
        """
         Set the value for passed atribute with the value
                 
        """
        pass
    
import NXOpen
## 
##         Represents the selection criteria of a part family instance
##      <br> Use @link NXOpen::Assemblies::Component::CreateEmptyPartFamilyInstanceSelectionCriteria NXOpen::Assemblies::Component::CreateEmptyPartFamilyInstanceSelectionCriteria@endlink  to get an instance of this class.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class InstanceSelectionCriteria(NXOpen.TaggedObject): 
    """
        Represents the selection criteria of a part family instance
    """


    ## Getter for property: (@link Template NXOpen.PartFamily.Template@endlink) Family
    ##   the @link NXOpen::PartFamily::Template NXOpen::PartFamily::Template@endlink  that corresponds to this criteria object   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Template
    @property
    def Family(self) -> Template:
        """
        Getter for property: (@link Template NXOpen.PartFamily.Template@endlink) Family
          the @link NXOpen::PartFamily::Template NXOpen::PartFamily::Template@endlink  that corresponds to this criteria object   
            
         
        """
        pass
    
    ## Getter for property: (@link Instance NXOpen.PartFamily.Instance@endlink) Instance
    ##   the @link NXOpen::PartFamily::Instance NXOpen::PartFamily::Instance@endlink  of criteria.  
    ##      
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Instance
    @property
    def Instance(self) -> Instance:
        """
        Getter for property: (@link Instance NXOpen.PartFamily.Instance@endlink) Instance
          the @link NXOpen::PartFamily::Instance NXOpen::PartFamily::Instance@endlink  of criteria.  
             
         
        """
        pass
    
    ##  Obtains the criteria strings associated with this selection criteria.
    ##             Output "criteriaStringArray" would be an array of TEXT_pc_t with each element of the form for e.g. "p7 > 100",
    ##             where "p7" is the attribute, "100" the value and ">" the expression connecting both 
    ##  @return criteriaStringArray (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetCriteriaStrings(instanceSelectionCriteria: InstanceSelectionCriteria) -> List[str]:
        """
         Obtains the criteria strings associated with this selection criteria.
                    Output "criteriaStringArray" would be an array of TEXT_pc_t with each element of the form for e.g. "p7 > 100",
                    where "p7" is the attribute, "100" the value and ">" the expression connecting both 
         @return criteriaStringArray (List[str]): .
        """
        pass
    
    ##  Returns true if the selection criteria evaluates to a valid part family instance, false otherwise. 
    ##  @return isValidCriteria (bool): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def IsValidPartFamilyInstanceSelectionCriteria(instanceSelectionCriteria: InstanceSelectionCriteria) -> bool:
        """
         Returns true if the selection criteria evaluates to a valid part family instance, false otherwise. 
         @return isValidCriteria (bool): .
        """
        pass
    
    ##  Sets criteria on @link NXOpen::PartFamily::InstanceSelectionCriteria NXOpen::PartFamily::InstanceSelectionCriteria@endlink .
    ##             This criteria can be used while adding a part family member to assembly. 
    ##             Number of elements in "attributes" and "criteriaStringArray" should always match the "attributeCount".
    ##             "criteriaStringArray" has to be an array of TEXT_pc_t with each element of the form for e.g. "p7 >= 100",
    ##             where "p7" is the attribute, "100" the value and ">=" the expression connecting both 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## <param name="instanceSelectionCriteria"> (@link InstanceSelectionCriteria NXOpen.PartFamily.InstanceSelectionCriteria@endlink) </param>
    ## <param name="attributes"> (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink) </param>
    ## <param name="criteriaStringArray"> (List[str]) </param>
    @overload
    def SetPartFamilyInstanceSelectionCriteria(self, instanceSelectionCriteria: InstanceSelectionCriteria, attributes: List[FamilyAttribute], criteriaStringArray: List[str]) -> None:
        """
         Sets criteria on @link NXOpen::PartFamily::InstanceSelectionCriteria NXOpen::PartFamily::InstanceSelectionCriteria@endlink .
                    This criteria can be used while adding a part family member to assembly. 
                    Number of elements in "attributes" and "criteriaStringArray" should always match the "attributeCount".
                    "criteriaStringArray" has to be an array of TEXT_pc_t with each element of the form for e.g. "p7 >= 100",
                    where "p7" is the attribute, "100" the value and ">=" the expression connecting both 
        """
        pass
    
    ##  Sets criteria on @link NXOpen::PartFamily::InstanceSelectionCriteria NXOpen::PartFamily::InstanceSelectionCriteria@endlink .
    ##             This routine can be used when user wants to add a part family member to assembly directly using 
    ##             the "memberName" instead of using attribute criteria. This "memberName" will be ignored in case 
    ##             the InstenaceSelectionCriteria already has any valid attribute criteria or if the user adds a valid 
    ##             attribute criteria later on.
    ##             User could obtain valid "memberName" using @link NXOpen::PartFamily::Template::GetMembers NXOpen::PartFamily::Template::GetMembers@endlink .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## <param name="instanceSelectionCriteria"> (@link InstanceSelectionCriteria NXOpen.PartFamily.InstanceSelectionCriteria@endlink) </param>
    ## <param name="memberName"> (str) </param>
    @overload
    def SetPartFamilyInstanceSelectionCriteria(self, instanceSelectionCriteria: InstanceSelectionCriteria, memberName: str) -> None:
        """
         Sets criteria on @link NXOpen::PartFamily::InstanceSelectionCriteria NXOpen::PartFamily::InstanceSelectionCriteria@endlink .
                    This routine can be used when user wants to add a part family member to assembly directly using 
                    the "memberName" instead of using attribute criteria. This "memberName" will be ignored in case 
                    the InstenaceSelectionCriteria already has any valid attribute criteria or if the user adds a valid 
                    attribute criteria later on.
                    User could obtain valid "memberName" using @link NXOpen::PartFamily::Template::GetMembers NXOpen::PartFamily::Template::GetMembers@endlink .
        """
        pass
    
import NXOpen
## 
##         Represents an instance of a part family member
##      <br> Use @link NXOpen::Part::GetFamilyInstance NXOpen::Part::GetFamilyInstance@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class Instance(NXOpen.TaggedObject): 
    """
        Represents an instance of a part family member
    """


    ## Getter for property: (@link Template NXOpen.PartFamily.Template@endlink) Family
    ##   the @link NXOpen::PartFamily::Template NXOpen::PartFamily::Template@endlink  of instance.  
    ##      
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Template
    @property
    def Family(self) -> Template:
        """
        Getter for property: (@link Template NXOpen.PartFamily.Template@endlink) Family
          the @link NXOpen::PartFamily::Template NXOpen::PartFamily::Template@endlink  of instance.  
             
         
        """
        pass
    
    ## Getter for property: (int) Version
    ##   the version of instance.  
    ##      
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
          the version of instance.  
             
         
        """
        pass
    
    ##  Returns whether this instance/member is out of date relative to the definition on the template. 
    ##  @return status (bool): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def IsOutOfDate(instance: Instance) -> bool:
        """
         Returns whether this instance/member is out of date relative to the definition on the template. 
         @return status (bool): .
        """
        pass
    
    ##  Load the @link NXOpen::PartFamily::Template NXOpen::PartFamily::Template@endlink  of instance. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def LoadFamily(instance: Instance) -> None:
        """
         Load the @link NXOpen::PartFamily::Template NXOpen::PartFamily::Template@endlink  of instance. 
        """
        pass
    
import NXOpen
##  This class represents the unique identifier for a part family member.
##         It essentially consitiutes the FAM attr object and value pair. This object is to be used in lieu
##         of member name, whenever a member is needed to be 
##         uniquely identified.
##       <br> Use @link PartFamily::TemplateManager::CreateMemberIdentifier PartFamily::TemplateManager::CreateMemberIdentifier@endlink  to create a new member identifier.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class MemberIdentifier(NXOpen.TransientObject): 
    """ This class represents the unique identifier for a part family member.
        It essentially consitiutes the FAM attr object and value pair. This object is to be used in lieu
        of member name, whenever a member is needed to be 
        uniquely identified.
     """


    ##  Free resources associated with the instance. After this method
    ##             is called, it is illegal to use the object.  In .NET, this method
    ##             is automatically called when the object is deleted by the garbage collector
    ##          
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(memberIdentifier: MemberIdentifier) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage collector
                 
        """
        pass
    
import NXOpen
##  This class serves as the manager for all the part family related operations. 
##         All operations that create, edit or delete part family objects are done through this class. 
##         Use the method @link Part::NewPartFamilyTemplateManager Part::NewPartFamilyTemplateManager@endlink 
##         to create new instance of this class.
##      
## 
##   <br>  Created in NX9.0.0  <br> 

class TemplateManager(NXOpen.TransientObject): 
    """ This class serves as the manager for all the part family related operations. 
        All operations that create, edit or delete part family objects are done through this class. 
        Use the method <ja_method>Part.NewPartFamilyTemplateManager</ja_method>
        to create new instance of this class.
     """


    ## Getter for property: (str) DefaultAlternateIdContext
    ##   the function returns/sets the IdContext to be used while assigning alternate IDs   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DefaultAlternateIdContext(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdContext
          the function returns/sets the IdContext to be used while assigning alternate IDs   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultAlternateIdContext

    ##   the function returns/sets the IdContext to be used while assigning alternate IDs   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DefaultAlternateIdContext.setter
    def DefaultAlternateIdContext(self, defaultContext: str):
        """
        Setter for property: (str) DefaultAlternateIdContext
          the function returns/sets the IdContext to be used while assigning alternate IDs   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultAlternateIdType
    ##   the function returns/sets the IdType to be used while assigning alternate IDs   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DefaultAlternateIdType(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdType
          the function returns/sets the IdType to be used while assigning alternate IDs   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultAlternateIdType

    ##   the function returns/sets the IdType to be used while assigning alternate IDs   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DefaultAlternateIdType.setter
    def DefaultAlternateIdType(self, defaultType: str):
        """
        Setter for property: (str) DefaultAlternateIdType
          the function returns/sets the IdType to be used while assigning alternate IDs   
            
         
        """
        pass
    
    ## Getter for property: (bool) Importable
    ##   the importable flag value   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Importable(self) -> bool:
        """
        Getter for property: (bool) Importable
          the importable flag value   
            
         
        """
        pass
    
    ## Setter for property: (bool) Importable

    ##   the importable flag value   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Importable.setter
    def Importable(self, isImportable: bool):
        """
        Setter for property: (bool) Importable
          the importable flag value   
            
         
        """
        pass
    
    ## Getter for property: (str) SaveDirectory
    ##   the save directory path value   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def SaveDirectory(self) -> str:
        """
        Getter for property: (str) SaveDirectory
          the save directory path value   
            
         
        """
        pass
    
    ## Setter for property: (str) SaveDirectory

    ##   the save directory path value   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SaveDirectory.setter
    def SaveDirectory(self, saveDirectory: str):
        """
        Setter for property: (str) SaveDirectory
          the save directory path value   
            
         
        """
        pass
    
    ## Getter for property: (bool) UpdateMassProperties
    ##   the update mass properties flag value   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def UpdateMassProperties(self) -> bool:
        """
        Getter for property: (bool) UpdateMassProperties
          the update mass properties flag value   
            
         
        """
        pass
    
    ## Setter for property: (bool) UpdateMassProperties

    ##   the update mass properties flag value   
    ##     
    ##  
    ## Setter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UpdateMassProperties.setter
    def UpdateMassProperties(self, isUpdateMassProperties: bool):
        """
        Setter for property: (bool) UpdateMassProperties
          the update mass properties flag value   
            
         
        """
        pass
    
    ##  Adds new attribute of type asserted mass to chosen attributes list of a part family 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: adv_assemblies ("ADVANCED ASSEMBLIES"), solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="attrToAdd"> (str) </param>
    ## <param name="indexAddAt"> (int) </param>
    def AddAssertedMassToChosenAttributes(templateManager: TemplateManager, attrToAdd: str, indexAddAt: int) -> None:
        """
         Adds new attribute of type asserted mass to chosen attributes list of a part family 
        """
        pass
    
    ##  Creates a new family member definition with the supplied name and places it just under previous family member definition.
    ##             If the part family is importable, then the otherNameEntry is a mandatory input.
    ##             Depending on whether we are in managed mode or native, familyMemberDefn name may be os_part_name or 
    ##             db_part_name, and otherNameEntry may be db_part_name or os_part_name.
    ##             In case of non-importable part family otherName Entry may be empty.
    ##         
    ##  @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberDefnName"> (str) </param>
    ## <param name="previousFamilyMemberDefn"> (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink) </param>
    ## <param name="otherNameEntry"> (str) </param>
    def AddInstanceDefinition(templateManager: TemplateManager, familyMemberDefnName: str, previousFamilyMemberDefn: InstanceDefinition, otherNameEntry: str) -> InstanceDefinition:
        """
         Creates a new family member definition with the supplied name and places it just under previous family member definition.
                    If the part family is importable, then the otherNameEntry is a mandatory input.
                    Depending on whether we are in managed mode or native, familyMemberDefn name may be os_part_name or 
                    db_part_name, and otherNameEntry may be db_part_name or os_part_name.
                    In case of non-importable part family otherName Entry may be empty.
                
         @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
        """
        pass
    
    ##  Creates a new family member definition with the supplied member identifier places it just under previous family member definition.
    ##             If the part family is importable, then the otherNameEntry is a mandatory input.
    ##             Depending on whether we are in managed mode or native, otherNameEntry may be db_part_name or os_part_name.
    ##             In case of non-importable part family otherNameEntry may be empty.
    ##         
    ##  @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberIdentifier"> (@link MemberIdentifier NXOpen.PartFamily.MemberIdentifier@endlink) </param>
    ## <param name="previousFamilyMemberDefn"> (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink) </param>
    ## <param name="otherNameEntry"> (str) </param>
    def AddInstanceDefinitionUsingMemberIdentifier(templateManager: TemplateManager, familyMemberIdentifier: MemberIdentifier, previousFamilyMemberDefn: InstanceDefinition, otherNameEntry: str) -> InstanceDefinition:
        """
         Creates a new family member definition with the supplied member identifier places it just under previous family member definition.
                    If the part family is importable, then the otherNameEntry is a mandatory input.
                    Depending on whether we are in managed mode or native, otherNameEntry may be db_part_name or os_part_name.
                    In case of non-importable part family otherNameEntry may be empty.
                
         @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
        """
        pass
    
    ##  Add all optional creation non key attributes to chosen list at the end or after a selected attribute from chosen attribute list.
    ##             To add all optional creation attributes at the end, pass pasteAfter as NULL.
    ##             If an optional attribute is already present in chosen attribute list, it does not add it again.
    ##             Outputs an array of the optional attributes that were actually added to chosen list
    ##         
    ##  @return optionalNonKeyAttrsAdded (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="pasteAfter"> (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink) </param>
    def AddOptionalCreationNonKeyAttrsToChosenAttrs(templateManager: TemplateManager, pasteAfter: FamilyAttribute) -> List[FamilyAttribute]:
        """
         Add all optional creation non key attributes to chosen list at the end or after a selected attribute from chosen attribute list.
                    To add all optional creation attributes at the end, pass pasteAfter as NULL.
                    If an optional attribute is already present in chosen attribute list, it does not add it again.
                    Outputs an array of the optional attributes that were actually added to chosen list
                
         @return optionalNonKeyAttrsAdded (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
        """
        pass
    
    ##  Adds new attributes to chosen attributes list of a part family 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="attrsToAdd"> (List[str]) </param>
    ## <param name="attrsTypes"> (@link FamilyAttribute.AttrType List[NXOpen.PartFamily.FamilyAttribute.AttrType]@endlink) </param>
    ## <param name="indexAddAt"> (int) </param>
    def AddToChosenAttributes(templateManager: TemplateManager, attrsToAdd: List[str], attrsTypes: List[FamilyAttribute.AttrType], indexAddAt: int) -> None:
        """
         Adds new attributes to chosen attributes list of a part family 
        """
        pass
    
    ##  Apply template release status to family members specified in input instDefsToApplyReleaseStatus. It returns success
    ##             and failure codes via errorCodes array. 
    ##         
    ##  @return errorCodes (List[int]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="instDefsToApplyReleaseStatus"> (@link InstanceDefinition List[NXOpen.PartFamily.InstanceDefinition]@endlink) </param>
    def ApplyTemplateReleaseStatusToMembers(templateManager: TemplateManager, instDefsToApplyReleaseStatus: List[InstanceDefinition]) -> List[int]:
        """
         Apply template release status to family members specified in input instDefsToApplyReleaseStatus. It returns success
                    and failure codes via errorCodes array. 
                
         @return errorCodes (List[int]): .
        """
        pass
    
    ##  Creates a member identifier for a part family member from the key attributes
    ##             and value pair.
    ##             In native mode the itemType is NULL
    ##             In managed mode, the value of itemType could be NULL in which case Template's item type will be used while creating the MemberIdentifier
    ##         
    ##  @return memberIdentifier (@link MemberIdentifier NXOpen.PartFamily.MemberIdentifier@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="keyAttrs"> (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink) </param>
    ## <param name="attrValues"> (List[str]) </param>
    ## <param name="itemType"> (str) </param>
    def CreateMemberIdentifier(templateManager: TemplateManager, keyAttrs: List[FamilyAttribute], attrValues: List[str], itemType: str) -> MemberIdentifier:
        """
         Creates a member identifier for a part family member from the key attributes
                    and value pair.
                    In native mode the itemType is NULL
                    In managed mode, the value of itemType could be NULL in which case Template's item type will be used while creating the MemberIdentifier
                
         @return memberIdentifier (@link MemberIdentifier NXOpen.PartFamily.MemberIdentifier@endlink): .
        """
        pass
    
    ##  Creates a part family associated with the owning part 
    ##  @return partFamily (@link Template NXOpen.PartFamily.Template@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    def CreatePartFamily(templateManager: TemplateManager) -> Template:
        """
         Creates a part family associated with the owning part 
         @return partFamily (@link Template NXOpen.PartFamily.Template@endlink): .
        """
        pass
    
    ##  Cut selected attributes of a part family. These will be pasted during paste operation.
    ##             If previously cut attributes are present then they will be lost because the new ones
    ##             will overwrite them.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="cutAttrs"> (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink) </param>
    def CutAttributes(templateManager: TemplateManager, cutAttrs: List[FamilyAttribute]) -> None:
        """
         Cut selected attributes of a part family. These will be pasted during paste operation.
                    If previously cut attributes are present then they will be lost because the new ones
                    will overwrite them.
                
        """
        pass
    
    ##  Delete the family member definition from template manager
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberDefinition"> (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink) </param>
    def DeleteInstanceDefinition(templateManager: TemplateManager, familyMemberDefinition: InstanceDefinition) -> None:
        """
         Delete the family member definition from template manager
                
        """
        pass
    
    ##  Deletes a part family associated with the manager/owning part 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def DeletePartFamily(templateManager: TemplateManager) -> None:
        """
         Deletes a part family associated with the manager/owning part 
        """
        pass
    
    ##  Deletes a given part family attribute 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="partFamilyAttribute"> (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink) </param>
    def DeletePartFamilyAttribute(templateManager: TemplateManager, partFamilyAttribute: FamilyAttribute) -> None:
        """
         Deletes a given part family attribute 
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##             is called, it is illegal to use the object.  In .NET, this method
    ##             is automatically called when the object is deleted by the garbage collector
    ##          
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(templateManager: TemplateManager) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage collector
                 
        """
        pass
    
    ##  Edits a part family associated with the manager/owning part 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def EditPartFamily(templateManager: TemplateManager) -> None:
        """
         Edits a part family associated with the manager/owning part 
        """
        pass
    
    ##  Creates a part family member if it doesn't exist on disk.
    ##  @return partName (str): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="memberName"> (str) </param>
    def EstablishFamilyInstance(templateManager: TemplateManager, memberName: str) -> str:
        """
         Creates a part family member if it doesn't exist on disk.
         @return partName (str): .
        """
        pass
    
    ##  Obtains all key attributes (required and optional) required to construct the MFK ID.
    ##             These would be used to create the unique member identifier.
    ##         
    ##  @return keyAttrs (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetAllKeyAttrs(templateManager: TemplateManager) -> List[FamilyAttribute]:
        """
         Obtains all key attributes (required and optional) required to construct the MFK ID.
                    These would be used to create the unique member identifier.
                
         @return keyAttrs (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
        """
        pass
    
    ##  Returns the attributes on the template manager
    ##             These might include the attributes which have not yet been committed onto the core object and have only been created by this instance of the manager.
    ##             "Use @link Template::GetAttributes Template::GetAttributes@endlink  to get the committed attributes"   
    ##         
    ##  @return attrsOnTemplateManager (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetChosenAttributes(templateManager: TemplateManager) -> List[FamilyAttribute]:
        """
         Returns the attributes on the template manager
                    These might include the attributes which have not yet been committed onto the core object and have only been created by this instance of the manager.
                    "Use @link Template::GetAttributes Template::GetAttributes@endlink  to get the committed attributes"   
                
         @return attrsOnTemplateManager (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
        """
        pass
    
    ##  Obtains the list of messages that may have been encountered in any workflow. 
    ##             This is a generic routine to get all information (Error/Warning/Info) that are deemed useful to user.
    ##             Contains error messages encountered during save like material issues, interpart expression issues, invalid member names.
    ##             In addition, if there were locked attributes (i.e. attributes whose value cannot be updated), 
    ##             this also would contain the names of such attributes.
    ##         
    ##  @return messages (List[str]): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetInfoMessages(templateManager: TemplateManager) -> List[str]:
        """
         Obtains the list of messages that may have been encountered in any workflow. 
                    This is a generic routine to get all information (Error/Warning/Info) that are deemed useful to user.
                    Contains error messages encountered during save like material issues, interpart expression issues, invalid member names.
                    In addition, if there were locked attributes (i.e. attributes whose value cannot be updated), 
                    this also would contain the names of such attributes.
                
         @return messages (List[str]): .
        """
        pass
    
    ##  Get the family member definition already present in family
    ##  @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberDefnName"> (str) </param>
    def GetInstanceDefinition(templateManager: TemplateManager, familyMemberDefnName: str) -> InstanceDefinition:
        """
         Get the family member definition already present in family
         @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
        """
        pass
    
    ##  Obtains the family member definition already present in family
    ##             A non zero return code implies familyMemberDefinition is NULL
    ##         
    ##  @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberIdentifier"> (@link MemberIdentifier NXOpen.PartFamily.MemberIdentifier@endlink) </param>
    def GetInstanceDefinitionUsingMemberIdentifier(templateManager: TemplateManager, familyMemberIdentifier: MemberIdentifier) -> InstanceDefinition:
        """
         Obtains the family member definition already present in family
                    A non zero return code implies familyMemberDefinition is NULL
                
         @return familyMemberDefinition (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink): .
        """
        pass
    
    ##  Get the part family attribute from part family template 
    ##  @return partFamilyAttribute (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="attrType"> (@link FamilyAttribute.AttrType NXOpen.PartFamily.FamilyAttribute.AttrType@endlink) </param>
    ## <param name="attrName"> (str) </param>
    def GetPartFamilyAttribute(templateManager: TemplateManager, attrType: FamilyAttribute.AttrType, attrName: str) -> FamilyAttribute:
        """
         Get the part family attribute from part family template 
         @return partFamilyAttribute (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink): .
        """
        pass
    
    ##  Get the part family template 
    ##             This method may return NULL if there is no template associated with the templatemanager
    ##         
    ##  @return partFamily (@link Template NXOpen.PartFamily.Template@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetPartFamilyTemplate(templateManager: TemplateManager) -> Template:
        """
         Get the part family template 
                    This method may return NULL if there is no template associated with the templatemanager
                
         @return partFamily (@link Template NXOpen.PartFamily.Template@endlink): .
        """
        pass
    
    ##  The list of attribute names of a given type in the owning part
    ##             These can be used to create part family attributes
    ##         
    ##  @return attrNames (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="attrType"> (@link FamilyAttribute.AttrType NXOpen.PartFamily.FamilyAttribute.AttrType@endlink) </param>
    def GetSelectableAttributes(templateManager: TemplateManager, attrType: FamilyAttribute.AttrType) -> List[str]:
        """
         The list of attribute names of a given type in the owning part
                    These can be used to create part family attributes
                
         @return attrNames (List[str]): .
        """
        pass
    
    ##  Move down the specified attributes of a part family by the moveDownCount. 
    ##             If the attributes cannot be moved down by the specified count, this method will execute the 
    ##             partial move and return the count that the attributes are actually moved down by.
    ##         
    ##  @return actualMovedDown (int): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="moveDownAttrs"> (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink) </param>
    ## <param name="moveDownCount"> (int) </param>
    def MoveDownAttributes(templateManager: TemplateManager, moveDownAttrs: List[FamilyAttribute], moveDownCount: int) -> int:
        """
         Move down the specified attributes of a part family by the moveDownCount. 
                    If the attributes cannot be moved down by the specified count, this method will execute the 
                    partial move and return the count that the attributes are actually moved down by.
                
         @return actualMovedDown (int): .
        """
        pass
    
    ##  Move up the specified attributes of a part family by the moveUpCount. 
    ##             If the attributes cannot be moved up by the specified count, this method will execute the 
    ##             partial move and return the count that the attributes are actually moved up by.
    ##         
    ##  @return actualMovedUp (int): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="moveUpAttrs"> (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink) </param>
    ## <param name="moveUpCount"> (int) </param>
    def MoveUpAttributes(templateManager: TemplateManager, moveUpAttrs: List[FamilyAttribute], moveUpCount: int) -> int:
        """
         Move up the specified attributes of a part family by the moveUpCount. 
                    If the attributes cannot be moved up by the specified count, this method will execute the 
                    partial move and return the count that the attributes are actually moved up by.
                
         @return actualMovedUp (int): .
        """
        pass
    
    ##  Paste the cut attributes of a part family. The pasteAfter attribute must be present in
    ##             chosen attributes list for this operation to succeed.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="pasteAfter"> (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink) </param>
    def PasteAttributes(templateManager: TemplateManager, pasteAfter: FamilyAttribute) -> None:
        """
         Paste the cut attributes of a part family. The pasteAfter attribute must be present in
                    chosen attributes list for this operation to succeed.
                
        """
        pass
    
    ##  Repopulates required attributes in chosen list so that it updates as per the teamcenter customizations, if it has changed since last saved template.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def RefreshDefaultAttrs(templateManager: TemplateManager) -> None:
        """
         Repopulates required attributes in chosen list so that it updates as per the teamcenter customizations, if it has changed since last saved template.
                
        """
        pass
    
    ##  Reorder (relocate) familyMemberDefinition just after the previousFamilyMemberDefn
    ##          
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberDefinition"> (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink) </param>
    ## <param name="previousFamilyMemberDefn"> (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink) </param>
    def ReorderInstanceDefinition(templateManager: TemplateManager, familyMemberDefinition: InstanceDefinition, previousFamilyMemberDefn: InstanceDefinition) -> None:
        """
         Reorder (relocate) familyMemberDefinition just after the previousFamilyMemberDefn
                 
        """
        pass
    
    ##  Save part family and apply the values of chosen family member definition to the template part,
    ##             It returns failure codes through errorCode.
    ##         
    ##  @return errorCode (int): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="familyMemberDefinition"> (@link InstanceDefinition NXOpen.PartFamily.InstanceDefinition@endlink) </param>
    def SaveFamilyAndApplyValues(templateManager: TemplateManager, familyMemberDefinition: InstanceDefinition) -> int:
        """
         Save part family and apply the values of chosen family member definition to the template part,
                    It returns failure codes through errorCode.
                
         @return errorCode (int): .
        """
        pass
    
    ##  Save part family and create the family members supplied through input array. It returns success
    ##             and failure codes via errorCodes array.
    ##         
    ##  @return errorCodes (List[int]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="instDefsToCreate"> (@link InstanceDefinition List[NXOpen.PartFamily.InstanceDefinition]@endlink) </param>
    def SaveFamilyAndCreateMembers(templateManager: TemplateManager, instDefsToCreate: List[InstanceDefinition]) -> List[int]:
        """
         Save part family and create the family members supplied through input array. It returns success
                    and failure codes via errorCodes array.
                
         @return errorCodes (List[int]): .
        """
        pass
    
    ##  Save part family and fix the orphan family members supplied through input array. The orphan member that is fixed would also be
    ##             updated to the latest configuration. It returns success and failure codes via errorCodes array. If errorCodes contains error about locked attributes,
    ##             use @link PartFamily::TemplateManager::GetInfoMessages PartFamily::TemplateManager::GetInfoMessages@endlink  to query the names of those locked attributes.
    ##         
    ##  @return errorCodes (List[int]): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="forceUpdate"> (bool) </param>
    ## <param name="instDefsToFix"> (@link InstanceDefinition List[NXOpen.PartFamily.InstanceDefinition]@endlink) </param>
    def SaveFamilyAndFixOrphanMembers(templateManager: TemplateManager, forceUpdate: bool, instDefsToFix: List[InstanceDefinition]) -> List[int]:
        """
         Save part family and fix the orphan family members supplied through input array. The orphan member that is fixed would also be
                    updated to the latest configuration. It returns success and failure codes via errorCodes array. If errorCodes contains error about locked attributes,
                    use @link PartFamily::TemplateManager::GetInfoMessages PartFamily::TemplateManager::GetInfoMessages@endlink  to query the names of those locked attributes.
                
         @return errorCodes (List[int]): .
        """
        pass
    
    ##  Save part family and update the family members supplied through input array. It returns success
    ##             and failure codes via errorCodes array. 
    ##             If errorCodes contains error about locked attributes, use @link PartFamily::TemplateManager::GetInfoMessages PartFamily::TemplateManager::GetInfoMessages@endlink  
    ##             to query the names of those locked attributes.
    ##         
    ##  @return errorCodes (List[int]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="forceUpdate"> (bool) </param>
    ## <param name="instDefsToUpdate"> (@link InstanceDefinition List[NXOpen.PartFamily.InstanceDefinition]@endlink) </param>
    def SaveFamilyAndUpdateMembers(templateManager: TemplateManager, forceUpdate: bool, instDefsToUpdate: List[InstanceDefinition]) -> List[int]:
        """
         Save part family and update the family members supplied through input array. It returns success
                    and failure codes via errorCodes array. 
                    If errorCodes contains error about locked attributes, use @link PartFamily::TemplateManager::GetInfoMessages PartFamily::TemplateManager::GetInfoMessages@endlink  
                    to query the names of those locked attributes.
                
         @return errorCodes (List[int]): .
        """
        pass
    
    ##  Save the changes in template manager to core part family
    ##          
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def SavePartFamily(templateManager: TemplateManager) -> None:
        """
         Save the changes in template manager to core part family
                 
        """
        pass
    
import NXOpen
##  This class represents a part family template       
##      <br> Use @link PartFamily::TemplateManager::CreatePartFamily PartFamily::TemplateManager::CreatePartFamily@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class Template(NXOpen.NXObject): 
    """ This class represents a part family template       
    """


    ## Getter for property: (str) TemplateName
    ##   the name of the part family template   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def TemplateName(self) -> str:
        """
        Getter for property: (str) TemplateName
          the name of the part family template   
            
         
        """
        pass
    
    ## Getter for property: (int) Version
    ##   the version of the part family template   
    ##     
    ##  
    ## Getter License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
          the version of the part family template   
            
         
        """
        pass
    
    ##  Returns the attributes of the part family template.
    ##             These are the attributes committed onto the core object
    ##         
    ##  @return templateAttrs (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetAttributes(partFamilyTemplate: Template) -> List[FamilyAttribute]:
        """
         Returns the attributes of the part family template.
                    These are the attributes committed onto the core object
                
         @return templateAttrs (@link FamilyAttribute List[NXOpen.PartFamily.FamilyAttribute]@endlink): .
        """
        pass
    
    ##  Obtains the members in part family.
    ##  @return members (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    @staticmethod
    def GetMembers(partFamilyTemplate: Template) -> List[str]:
        """
         Obtains the members in part family.
         @return members (List[str]): .
        """
        pass
    
    ##  Returns the valid attribute values for a given part family attribute.
    ##             These will be useful for selecting a valid match_criteria 
    ##         
    ##  @return validAttrValues (List[str]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="attr"> (@link FamilyAttribute NXOpen.PartFamily.FamilyAttribute@endlink) </param>
    def GetValidAttributeValues(partFamilyTemplate: Template, attr: FamilyAttribute) -> List[str]:
        """
         Returns the valid attribute values for a given part family attribute.
                    These will be useful for selecting a valid match_criteria 
                
         @return validAttrValues (List[str]): .
        """
        pass
    
    ##  Returns true if a member name is valid, false otherwise
    ##  @return isValidMemberName (bool): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="memberName"> (str) </param>
    def IsValidMemberName(partFamilyTemplate: Template, memberName: str) -> bool:
        """
         Returns true if a member name is valid, false otherwise
         @return isValidMemberName (bool): .
        """
        pass
    
## @package NXOpen.PartFamily
## Classes, Enums and Structs under NXOpen.PartFamily namespace

##  @link FamilyAttributeAttrType NXOpen.PartFamily.FamilyAttributeAttrType @endlink is an alias for @link FamilyAttribute.AttrType NXOpen.PartFamily.FamilyAttribute.AttrType@endlink
FamilyAttributeAttrType = FamilyAttribute.AttrType


