from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class FamilyAttribute(NXOpen.NXObject): 
    """ This class represents a part family attribute       
    """
    class AttrType(Enum):
        """
        Members Include: 
         |Text|  text attribute 
         |Numeric|  numeric attribute 
         |Integer|  integer attribute 
         |Double|  double attribute 
         |String|  string attribute 
         |Part|  part attribute 
         |Name|  name attribute 
         |Instance|  instance attribute 
         |Expression|  expression attribute 
         |Mirror|  mirror attribute 
         |Density|  density attribute 
         |Feature|  feature attribute 
         |Mass|  asserted mass attribute 
         |Material|  material attribute 
         |Cofm|  center of mass attribute 
         |Undefined|  undefined attribute type 

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
        @staticmethod
        def ValueOf(value: int) -> FamilyAttribute.AttrType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsOptional(self) -> bool:
        """
        Getter for property: (bool) IsOptional
         Returns a value indicating whether the attribute is an optional attribute.  
          
                    This could be an optional creation non key attribute or an optional key attribute
                  
         
        """
        pass
    @property
    def IsRequired(self) -> bool:
        """
        Getter for property: (bool) IsRequired
         Returns a value indicating whether the attribute is a required attribute.  
          
                    This could be a required creation non key attribute or a required key attribute
                  
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the given attribute   
            
         
        """
        pass
    @property
    def Type(self) -> FamilyAttribute.AttrType:
        """
        Getter for property: ( FamilyAttribute.AttrType NXOpen.P) Type
         Returns the type of the given attribute   
            
         
        """
        pass
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the value of the given attribute   
            
         
        """
        pass
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
         Returns the version of the given attribute   
            
         
        """
        pass
import NXOpen
class InstanceDefinition(NXOpen.TransientObject): 
    """ This class repesents a part family table record (or instance definition on the template) and is 
        createddeleted by PartFamily.TemplateManager.         
     """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage collector
                 
        """
        pass
    def GetValueOfAttribute(self, partFamAttr: FamilyAttribute) -> str:
        """
         Get the value for passed atribute
                 
         Returns value (str): .
        """
        pass
    def SetValueOfAttribute(self, partFamAttr: FamilyAttribute, value: str) -> None:
        """
         Set the value for passed atribute with the value
                 
        """
        pass
import NXOpen
class InstanceSelectionCriteria(NXOpen.TaggedObject): 
    """
        Represents the selection criteria of a part family instance
    """
    @property
    def Family(self) -> Template:
        """
        Getter for property: ( Template NXOpen.P) Family
         Returns the  NXOpen::PartFamily::Template  that corresponds to this criteria object   
            
         
        """
        pass
    @property
    def Instance(self) -> Instance:
        """
        Getter for property: ( Instance NXOpen.P) Instance
         Returns the  NXOpen::PartFamily::Instance  of criteria.  
             
         
        """
        pass
    def GetCriteriaStrings(self) -> List[str]:
        """
         Obtains the criteria strings associated with this selection criteria.
                    Output "criteriaStringArray" would be an array of TEXT_pc_t with each element of the form for e.g. "p7  100",
                    where "p7" is the attribute, "100" the value and "" the expression connecting both 
         Returns criteriaStringArray (List[str]): .
        """
        pass
    def IsValidPartFamilyInstanceSelectionCriteria(self) -> bool:
        """
         Returns true if the selection criteria evaluates to a valid part family instance, false otherwise. 
         Returns isValidCriteria (bool): .
        """
        pass
    @overload
    def SetPartFamilyInstanceSelectionCriteria(self, attributes: List[FamilyAttribute], criteriaStringArray: List[str]) -> None:
        """
         Sets criteria on NXOpen.PartFamily.InstanceSelectionCriteria.
                    This criteria can be used while adding a part family member to assembly. 
                    Number of elements in "attributes" and "criteriaStringArray" should always match the "attributeCount".
                    "criteriaStringArray" has to be an array of TEXT_pc_t with each element of the form for e.g. "p7 = 100",
                    where "p7" is the attribute, "100" the value and "=" the expression connecting both 
        """
        pass
    @overload
    def SetPartFamilyInstanceSelectionCriteria(self, memberName: str) -> None:
        """
         Sets criteria on NXOpen.PartFamily.InstanceSelectionCriteria.
                    This routine can be used when user wants to add a part family member to assembly directly using 
                    the "memberName" instead of using attribute criteria. This "memberName" will be ignored in case 
                    the InstenaceSelectionCriteria already has any valid attribute criteria or if the user adds a valid 
                    attribute criteria later on.
                    User could obtain valid "memberName" using NXOpen.PartFamily.Template.GetMembers.
        """
        pass
import NXOpen
class Instance(NXOpen.TaggedObject): 
    """
        Represents an instance of a part family member
    """
    @property
    def Family(self) -> Template:
        """
        Getter for property: ( Template NXOpen.P) Family
         Returns the  NXOpen::PartFamily::Template  of instance.  
             
         
        """
        pass
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
         Returns the version of instance.  
             
         
        """
        pass
    def IsOutOfDate(self) -> bool:
        """
         Returns whether this instancemember is out of date relative to the definition on the template. 
         Returns status (bool): .
        """
        pass
    def LoadFamily(self) -> None:
        """
         Load the NXOpen.PartFamily.Template of instance. 
        """
        pass
import NXOpen
class MemberIdentifier(NXOpen.TransientObject): 
    """ This class represents the unique identifier for a part family member.
        It essentially consitiutes the FAM attr object and value pair. This object is to be used in lieu
        of member name, whenever a member is needed to be 
        uniquely identified.
     """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage collector
                 
        """
        pass
import NXOpen
class TemplateManager(NXOpen.TransientObject): 
    """ This class serves as the manager for all the part family related operations. 
        All operations that create, edit or delete part family objects are done through this class. 
        Use the method Part.NewPartFamilyTemplateManager
        to create new instance of this class.
     """
    @property
    def DefaultAlternateIdContext(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdContext
         Returns the function returnssets the IdContext to be used while assigning alternate IDs   
            
         
        """
        pass
    @DefaultAlternateIdContext.setter
    def DefaultAlternateIdContext(self, defaultContext: str):
        """
        Setter for property: (str) DefaultAlternateIdContext
         Returns the function returnssets the IdContext to be used while assigning alternate IDs   
            
         
        """
        pass
    @property
    def DefaultAlternateIdType(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdType
         Returns the function returnssets the IdType to be used while assigning alternate IDs   
            
         
        """
        pass
    @DefaultAlternateIdType.setter
    def DefaultAlternateIdType(self, defaultType: str):
        """
        Setter for property: (str) DefaultAlternateIdType
         Returns the function returnssets the IdType to be used while assigning alternate IDs   
            
         
        """
        pass
    @property
    def Importable(self) -> bool:
        """
        Getter for property: (bool) Importable
         Returns the importable flag value   
            
         
        """
        pass
    @Importable.setter
    def Importable(self, isImportable: bool):
        """
        Setter for property: (bool) Importable
         Returns the importable flag value   
            
         
        """
        pass
    @property
    def SaveDirectory(self) -> str:
        """
        Getter for property: (str) SaveDirectory
         Returns the save directory path value   
            
         
        """
        pass
    @SaveDirectory.setter
    def SaveDirectory(self, saveDirectory: str):
        """
        Setter for property: (str) SaveDirectory
         Returns the save directory path value   
            
         
        """
        pass
    @property
    def UpdateMassProperties(self) -> bool:
        """
        Getter for property: (bool) UpdateMassProperties
         Returns the update mass properties flag value   
            
         
        """
        pass
    @UpdateMassProperties.setter
    def UpdateMassProperties(self, isUpdateMassProperties: bool):
        """
        Setter for property: (bool) UpdateMassProperties
         Returns the update mass properties flag value   
            
         
        """
        pass
    def AddAssertedMassToChosenAttributes(self, attrToAdd: str, indexAddAt: int) -> None:
        """
         Adds new attribute of type asserted mass to chosen attributes list of a part family 
        """
        pass
    def AddInstanceDefinition(self, familyMemberDefnName: str, previousFamilyMemberDefn: InstanceDefinition, otherNameEntry: str) -> InstanceDefinition:
        """
         Creates a new family member definition with the supplied name and places it just under previous family member definition.
                    If the part family is importable, then the otherNameEntry is a mandatory input.
                    Depending on whether we are in managed mode or native, familyMemberDefn name may be os_part_name or 
                    db_part_name, and otherNameEntry may be db_part_name or os_part_name.
                    In case of non-importable part family otherName Entry may be empty.
                
         Returns familyMemberDefinition ( InstanceDefinition NXOpen.P): .
        """
        pass
    def AddInstanceDefinitionUsingMemberIdentifier(self, familyMemberIdentifier: MemberIdentifier, previousFamilyMemberDefn: InstanceDefinition, otherNameEntry: str) -> InstanceDefinition:
        """
         Creates a new family member definition with the supplied member identifier places it just under previous family member definition.
                    If the part family is importable, then the otherNameEntry is a mandatory input.
                    Depending on whether we are in managed mode or native, otherNameEntry may be db_part_name or os_part_name.
                    In case of non-importable part family otherNameEntry may be empty.
                
         Returns familyMemberDefinition ( InstanceDefinition NXOpen.P): .
        """
        pass
    def AddOptionalCreationNonKeyAttrsToChosenAttrs(self, pasteAfter: FamilyAttribute) -> List[FamilyAttribute]:
        """
         Add all optional creation non key attributes to chosen list at the end or after a selected attribute from chosen attribute list.
                    To add all optional creation attributes at the end, pass pasteAfter as NULL.
                    If an optional attribute is already present in chosen attribute list, it does not add it again.
                    Outputs an array of the optional attributes that were actually added to chosen list
                
         Returns optionalNonKeyAttrsAdded ( FamilyAttribute List[NXOpen): .
        """
        pass
    def AddToChosenAttributes(self, attrsToAdd: List[str], attrsTypes: List[FamilyAttribute.AttrType], indexAddAt: int) -> None:
        """
         Adds new attributes to chosen attributes list of a part family 
        """
        pass
    def ApplyTemplateReleaseStatusToMembers(self, instDefsToApplyReleaseStatus: List[InstanceDefinition]) -> List[int]:
        """
         Apply template release status to family members specified in input instDefsToApplyReleaseStatus. It returns success
                    and failure codes via errorCodes array. 
                
         Returns errorCodes (List[int]): .
        """
        pass
    def CreateMemberIdentifier(self, keyAttrs: List[FamilyAttribute], attrValues: List[str], itemType: str) -> MemberIdentifier:
        """
         Creates a member identifier for a part family member from the key attributes
                    and value pair.
                    In native mode the itemType is NULL
                    In managed mode, the value of itemType could be NULL in which case Template's item type will be used while creating the MemberIdentifier
                
         Returns memberIdentifier ( MemberIdentifier NXOpen.P): .
        """
        pass
    def CreatePartFamily(self) -> Template:
        """
         Creates a part family associated with the owning part 
         Returns partFamily ( Template NXOpen.P): .
        """
        pass
    def CutAttributes(self, cutAttrs: List[FamilyAttribute]) -> None:
        """
         Cut selected attributes of a part family. These will be pasted during paste operation.
                    If previously cut attributes are present then they will be lost because the new ones
                    will overwrite them.
                
        """
        pass
    def DeleteInstanceDefinition(self, familyMemberDefinition: InstanceDefinition) -> None:
        """
         Delete the family member definition from template manager
                
        """
        pass
    def DeletePartFamily(self) -> None:
        """
         Deletes a part family associated with the managerowning part 
        """
        pass
    def DeletePartFamilyAttribute(self, partFamilyAttribute: FamilyAttribute) -> None:
        """
         Deletes a given part family attribute 
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage collector
                 
        """
        pass
    def EditPartFamily(self) -> None:
        """
         Edits a part family associated with the managerowning part 
        """
        pass
    def EstablishFamilyInstance(self, memberName: str) -> str:
        """
         Creates a part family member if it doesn't exist on disk.
         Returns partName (str): .
        """
        pass
    def GetAllKeyAttrs(self) -> List[FamilyAttribute]:
        """
         Obtains all key attributes (required and optional) required to construct the MFK ID.
                    These would be used to create the unique member identifier.
                
         Returns keyAttrs ( FamilyAttribute List[NXOpen): .
        """
        pass
    def GetChosenAttributes(self) -> List[FamilyAttribute]:
        """
         Returns the attributes on the template manager
                    These might include the attributes which have not yet been committed onto the core object and have only been created by this instance of the manager.
                    "Use Template.GetAttributes to get the committed attributes"   
                
         Returns attrsOnTemplateManager ( FamilyAttribute List[NXOpen): .
        """
        pass
    def GetInfoMessages(self) -> List[str]:
        """
         Obtains the list of messages that may have been encountered in any workflow. 
                    This is a generic routine to get all information (ErrorWarningInfo) that are deemed useful to user.
                    Contains error messages encountered during save like material issues, interpart expression issues, invalid member names.
                    In addition, if there were locked attributes (i.e. attributes whose value cannot be updated), 
                    this also would contain the names of such attributes.
                
         Returns messages (List[str]): .
        """
        pass
    def GetInstanceDefinition(self, familyMemberDefnName: str) -> InstanceDefinition:
        """
         Get the family member definition already present in family
         Returns familyMemberDefinition ( InstanceDefinition NXOpen.P): .
        """
        pass
    def GetInstanceDefinitionUsingMemberIdentifier(self, familyMemberIdentifier: MemberIdentifier) -> InstanceDefinition:
        """
         Obtains the family member definition already present in family
                    A non zero return code implies familyMemberDefinition is NULL
                
         Returns familyMemberDefinition ( InstanceDefinition NXOpen.P): .
        """
        pass
    def GetPartFamilyAttribute(self, attrType: FamilyAttribute.AttrType, attrName: str) -> FamilyAttribute:
        """
         Get the part family attribute from part family template 
         Returns partFamilyAttribute ( FamilyAttribute NXOpen.P): .
        """
        pass
    def GetPartFamilyTemplate(self) -> Template:
        """
         Get the part family template 
                    This method may return NULL if there is no template associated with the templatemanager
                
         Returns partFamily ( Template NXOpen.P): .
        """
        pass
    def GetSelectableAttributes(self, attrType: FamilyAttribute.AttrType) -> List[str]:
        """
         The list of attribute names of a given type in the owning part
                    These can be used to create part family attributes
                
         Returns attrNames (List[str]): .
        """
        pass
    def MoveDownAttributes(self, moveDownAttrs: List[FamilyAttribute], moveDownCount: int) -> int:
        """
         Move down the specified attributes of a part family by the moveDownCount. 
                    If the attributes cannot be moved down by the specified count, this method will execute the 
                    partial move and return the count that the attributes are actually moved down by.
                
         Returns actualMovedDown (int): .
        """
        pass
    def MoveUpAttributes(self, moveUpAttrs: List[FamilyAttribute], moveUpCount: int) -> int:
        """
         Move up the specified attributes of a part family by the moveUpCount. 
                    If the attributes cannot be moved up by the specified count, this method will execute the 
                    partial move and return the count that the attributes are actually moved up by.
                
         Returns actualMovedUp (int): .
        """
        pass
    def PasteAttributes(self, pasteAfter: FamilyAttribute) -> None:
        """
         Paste the cut attributes of a part family. The pasteAfter attribute must be present in
                    chosen attributes list for this operation to succeed.
                
        """
        pass
    def RefreshDefaultAttrs(self) -> None:
        """
         Repopulates required attributes in chosen list so that it updates as per the teamcenter customizations, if it has changed since last saved template.
                
        """
        pass
    def ReorderInstanceDefinition(self, familyMemberDefinition: InstanceDefinition, previousFamilyMemberDefn: InstanceDefinition) -> None:
        """
         Reorder (relocate) familyMemberDefinition just after the previousFamilyMemberDefn
                 
        """
        pass
    def SaveFamilyAndApplyValues(self, familyMemberDefinition: InstanceDefinition) -> int:
        """
         Save part family and apply the values of chosen family member definition to the template part,
                    It returns failure codes through errorCode.
                
         Returns errorCode (int): .
        """
        pass
    def SaveFamilyAndCreateMembers(self, instDefsToCreate: List[InstanceDefinition]) -> List[int]:
        """
         Save part family and create the family members supplied through input array. It returns success
                    and failure codes via errorCodes array.
                
         Returns errorCodes (List[int]): .
        """
        pass
    def SaveFamilyAndFixOrphanMembers(self, forceUpdate: bool, instDefsToFix: List[InstanceDefinition]) -> List[int]:
        """
         Save part family and fix the orphan family members supplied through input array. The orphan member that is fixed would also be
                    updated to the latest configuration. It returns success and failure codes via errorCodes array. If errorCodes contains error about locked attributes,
                    use PartFamily.TemplateManager.GetInfoMessages to query the names of those locked attributes.
                
         Returns errorCodes (List[int]): .
        """
        pass
    def SaveFamilyAndUpdateMembers(self, forceUpdate: bool, instDefsToUpdate: List[InstanceDefinition]) -> List[int]:
        """
         Save part family and update the family members supplied through input array. It returns success
                    and failure codes via errorCodes array. 
                    If errorCodes contains error about locked attributes, use PartFamily.TemplateManager.GetInfoMessages 
                    to query the names of those locked attributes.
                
         Returns errorCodes (List[int]): .
        """
        pass
    def SavePartFamily(self) -> None:
        """
         Save the changes in template manager to core part family
                 
        """
        pass
import NXOpen
class Template(NXOpen.NXObject): 
    """ This class represents a part family template       
    """
    @property
    def TemplateName(self) -> str:
        """
        Getter for property: (str) TemplateName
         Returns the name of the part family template   
            
         
        """
        pass
    @property
    def Version(self) -> int:
        """
        Getter for property: (int) Version
         Returns the version of the part family template   
            
         
        """
        pass
    def GetAttributes(self) -> List[FamilyAttribute]:
        """
         Returns the attributes of the part family template.
                    These are the attributes committed onto the core object
                
         Returns templateAttrs ( FamilyAttribute List[NXOpen): .
        """
        pass
    def GetMembers(self) -> List[str]:
        """
         Obtains the members in part family.
         Returns members (List[str]): .
        """
        pass
    def GetValidAttributeValues(self, attr: FamilyAttribute) -> List[str]:
        """
         Returns the valid attribute values for a given part family attribute.
                    These will be useful for selecting a valid match_criteria 
                
         Returns validAttrValues (List[str]): .
        """
        pass
    def IsValidMemberName(self, memberName: str) -> bool:
        """
         Returns true if a member name is valid, false otherwise
         Returns isValidMemberName (bool): .
        """
        pass
