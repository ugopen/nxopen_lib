from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AlternateIdManager(NXOpen.TransientObject): 
    """ This class is responsible for setting and getting NX Manager database attribute. """
    class AlternateIdsData:
        """
        Contains alternate Ids data 
         AlternateIdManagerAlternateIdsData_Struct NXOp is an alias for  AlternateIdManager.AlternateIdsData NXOp.
        """
        @property
        def AlternateItemId(self) -> str:
            """
            Getter for property AlternateItemId
            the new value for the alternate item ID

            """
            pass
        @AlternateItemId.setter
        def AlternateItemId(self, value: str):
            """
            Getter for property AlternateItemId
            the new value for the alternate item ID
            Setter for property AlternateItemId
            the new value for the alternate item ID

            """
            pass
        @property
        def AlternateRevId(self) -> str:
            """
            Getter for property AlternateRevId
            the new value for the alternate Revision ID

            """
            pass
        @AlternateRevId.setter
        def AlternateRevId(self, value: str):
            """
            Getter for property AlternateRevId
            the new value for the alternate Revision ID
            Setter for property AlternateRevId
            the new value for the alternate Revision ID

            """
            pass
        @property
        def AlternateName(self) -> str:
            """
            Getter for property AlternateName
            the new value for the alternate Name

            """
            pass
        @AlternateName.setter
        def AlternateName(self, value: str):
            """
            Getter for property AlternateName
            the new value for the alternate Name
            Setter for property AlternateName
            the new value for the alternate Name

            """
            pass
        @property
        def AlternateDescription(self) -> str:
            """
            Getter for property AlternateDescription
            the new value for the alternate Description

            """
            pass
        @AlternateDescription.setter
        def AlternateDescription(self, value: str):
            """
            Getter for property AlternateDescription
            the new value for the alternate Description
            Setter for property AlternateDescription
            the new value for the alternate Description

            """
            pass
        @property
        def Modifiable(self) -> bool:
            """
            Getter for property Modifiable
            the new value for the alternate for modifiable flag

            """
            pass
        @Modifiable.setter
        def Modifiable(self, value: bool):
            """
            Getter for property Modifiable
            the new value for the alternate for modifiable flag
            Setter for property Modifiable
            the new value for the alternate for modifiable flag

            """
            pass
    class AssignAlternateRevData:
        """
        Contains alternate Revision Id data 
         AlternateIdManagerAssignAlternateRevData_Struct NXOp is an alias for  AlternateIdManager.AssignAlternateRevData NXOp.
        """
        @property
        def AlternateRevId(self) -> str:
            """
            Getter for property AlternateRevId
            the new value the alternate Revision ID

            """
            pass
        @AlternateRevId.setter
        def AlternateRevId(self, value: str):
            """
            Getter for property AlternateRevId
            the new value the alternate Revision ID
            Setter for property AlternateRevId
            the new value the alternate Revision ID

            """
            pass
        @property
        def Modifiable(self) -> bool:
            """
            Getter for property Modifiable
            the new value of flag for revision modifiable

            """
            pass
        @Modifiable.setter
        def Modifiable(self, value: bool):
            """
            Getter for property Modifiable
            the new value of flag for revision modifiable
            Setter for property Modifiable
            the new value of flag for revision modifiable

            """
            pass
    def AssignAlternateId(self) -> Tuple[str, str]:
        """
         This method generates alternate item and revision IDs and sets these generated
                values on this manager class. Note that the ID context and type must be set on the
                builder in order for this assign operation to be successful. 
         Returns A tuple consisting of (alternate_item_id, alternate_rev_id). 
         - alternate_item_id is: str. the newly generated alternate item ID value
                                                       that was set on this manager .
         - alternate_rev_id is: str. the newly generated alternate revision ID value
                                                       that was set on this manager .

        """
        pass
    def AssignAlternateIds(self, context: str, id_type: str) -> AlternateIdManager.AlternateIdsData:
        """
         Generates the alternate ID information by calling
                AssignAlternateIds . Returns pointer to  PDM.Altids.AlternateIdsData object. 
                Sets Alternate Name,Alternate Id,Alternate Revision ,Alternate Description,
                flag for alternate Id modifiable and flag for revision modifiable into Alternate Manager object.
                
         Returns alt_info ( AlternateIdManager.AlternateIdsData NXOp): Contains alternate Ids data .
        """
        pass
    def AssignAlternateRevId(self) -> str:
        """
         This method generates an alternate rev ID and sets this generated value on
                this manager class.  Note that the ID context and type must be set on the
                builder in order for this assign operation to be successful. 
         Returns alternate_rev_id (str):  the newly generated alternate rev ID
                                                       value that was set on this manager .
        """
        pass
    def AssignAlternateRevision(self) -> AlternateIdManager.AssignAlternateRevData:
        """
         Generates the alternate Revision ID information. 
                Sets Alternate Revision and flag for revision modifiable into Alternate Manager object.
                
         Returns revInfo ( AlternateIdManager.AssignAlternateRevData NXOp): Contains alternate Revision Id data .
        """
        pass
    def CreateAlternateIdInformation(self) -> None:
        """
         Adds the alternate ID information set by calling
                SetAlternateIdInformation and the various "assign" and "set"
                methods. The context, ID type, alternate ID, alternate revision ID, and the
                alternate name must all be set before calling this method. 
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def GetAllContexts(self) -> List[str]:
        """
         Gets a list of all the available contexts. 
         Returns contexts (List[str]):  list of contexts .
        """
        pass
    def GetAllIdTypes(self, context: str) -> List[str]:
        """
         Gets a list of all the available ID types for a given context. 
         Returns id_types (List[str]):  list of ID types .
        """
        pass
    def GetAlternateDescription(self) -> str:
        """
         Gets the value of a alternate name as it is currently set on this manager class. 
         Returns alternate_description (str):  the current value of the alternate
                                                            description on this manager .
        """
        pass
    def GetAlternateIdAsDefaultIndentifier(self) -> bool:
        """
         Gets (as it is currently set on this manager class) whether the
                alternate ID information should be the default indentifier. 
         Returns alternate_id_as_default_indentifier (bool):  the current value of option
                                                                            on this manager .
        """
        pass
    def GetAlternateItemId(self) -> str:
        """
         Gets the value of a alternate ID as it is currently set on this manager class. 
         Returns alternate_item_id (str):  the current value of the alternate item ID on this manager .
        """
        pass
    def GetAlternateName(self) -> str:
        """
         Gets the value of a alternate name as it is currently set on this manager class. 
         Returns alternate_name (str):  the current value of the alternate name on
                                                     this manager .
        """
        pass
    def GetAlternateRevId(self) -> str:
        """
         Gets the value of a alternate rev ID as it is currently set on this manager class. 
         Returns alternate_rev_id (str):  the current value of the alternate rev ID
                                                       on this manager .
        """
        pass
    def GetContext(self) -> str:
        """
         Gets the value of a context as it is currently set on this manager class. 
         Returns context (str):  the current value of the context on this manager .
        """
        pass
    def GetIdType(self) -> str:
        """
         Gets the value of a ID type as it is currently set on this manager class. 
         Returns id_type (str):  the current value of the ID type on this manager .
        """
        pass
    def SetAlternateDescription(self, alternate_description: str) -> None:
        """
         Sets the value of the alternate description. 
        """
        pass
    def SetAlternateIdAsDefaultIndentifier(self, alternate_id_as_default_indentifier: bool) -> None:
        """
         Sets whether the alternate ID information should be the default indentifier. 
        """
        pass
    def SetAlternateIdInformation(self, context: str, id_type: str, alternate_item_id: str, alternate_rev_id: str, alternate_name: str, alternate_description: str, alternate_id_as_default_indentifier: bool) -> None:
        """
         Sets alternate ID information on this manager class.  can be specified
                for parameters which are set via other set or assign methods on this builder. 
        """
        pass
    def SetAlternateItemId(self, alternate_item_id: str) -> None:
        """
         Sets the value of the alternate item ID. 
        """
        pass
    def SetAlternateName(self, alternate_name: str) -> None:
        """
         Sets the value of the alternate name. 
        """
        pass
    def SetAlternateRevId(self, alternate_rev_id: str) -> None:
        """
         Sets the value of the alternate rev ID. 
        """
        pass
    def SetContext(self, context: str) -> None:
        """
         Sets the value of a context. 
        """
        pass
    def SetIdType(self, id_type: str) -> None:
        """
         Sets the value of an ID type. 
        """
        pass
import NXOpen
class AssyCloneCompDisp(NXOpen.NXObject): 
    """ Represents a ASSY_clone_comp_disp class """
    pass
import NXOpen
class AttributeGroupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of attribute group objects.  A smaller list of attribute groups can be
    retrieved by using the method NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroups
    for classes that implement the NXOpen.PDM.IAttributeGroupOwner interface.  """
    def FindObject(self, journal_identifier: str) -> AttributeGroup:
        """
         Finds the  NXOpen.PDM.AttributeGroup  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
            An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( AttributeGroup NXOp):  AttributeGroup found, or null if no such attribute group exists.
        """
        pass
import NXOpen
class AttributeGroupDescriptionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of attribute group description objects.  A smaller list of attribute groups
    descriptions can be retrieved by using the method
    NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroupDescriptions
    for classes that implement the NXOpen.PDM.IAttributeGroupOwner interface."""
    def FindObject(self, journal_identifier: str) -> AttributeGroupDescription:
        """
         Finds the  NXOpen.PDM.AttributeGroupDescription  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
            An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( AttributeGroupDescription NXOp):  AttributeGroupDescription found, or null if no such attribute group description exists.
        """
        pass
import NXOpen
class AttributeGroupDescription(NXOpen.NXObject): 
    """ Represents an attribute group type. """
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the display name for the attribute group description.  
             
         
        """
        pass
    @property
    def MaximumNumberOfAttributeGroupsAllowed(self) -> int:
        """
        Getter for property: (int) MaximumNumberOfAttributeGroupsAllowed
         Returns the maximum number of attribute groups of this type that can be assigned to an object.  
              
         
        """
        pass
    @property
    def MinimumNumberOfAttributeGroupsAllowed(self) -> int:
        """
        Getter for property: (int) MinimumNumberOfAttributeGroupsAllowed
         Returns the minimum number of attribute groups of this type that can be assigned to an object.  
              
         
        """
        pass
import NXOpen
class AttributeGroupReviseBuilder(NXOpen.Builder): 
    """ Represents an attribute group revise builder.  Given a list of existing attribute groups for an
    attribute group owner, a new revision for each attribute group is created.

    Note: The Builder.Commit returns  for this builder.  Use the 
    NXOpen.PDM.AttributeGroupReviseBuilder.GetRevisedAttributeGroups to get the
    successfully revised attribute groups after the builder is committed.
 """
    class SaveAsActionType(Enum):
        """
        Members Include: 
         |NewRevision| 
         |NewAttributeGroup| 

        """
        NewRevision: int
        NewAttributeGroup: int
        @staticmethod
        def ValueOf(value: int) -> AttributeGroupReviseBuilder.SaveAsActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetLogicalObjects(self) -> List[LogicalObject]:
        """
         Returns list of logical objects created by the builder for use during the revise operation. 
         Returns logicalObjects ( LogicalObject List[NX):   .
        """
        pass
    def GetOperationErrors(self) -> OperationErrors:
        """
         Returns the NXOpen.PDM.OperationErrors object containing
                information about the attribute groups that failed to revise. 
         Returns operationErrors ( OperationErrors NXOp): .
        """
        pass
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns the operation failures during revise of the attribute groups 
         Returns operationFailures ( NXOpen.ErrorList): .
        """
        pass
    def GetRevisedAttributeGroups(self) -> List[AttributeGroup]:
        """
         Returns a list of attribute groups for use during the revise operation.  Before the builder is committed
                this list of attribute groups is used to set any required user attribute.  The attribute groups do
                not exist in Teamcenter until the builder is committed.  After the builder is committed the list only
                contains successfully revised attribute groups.  Any attribute groups that failed to revise are removed
                from the list and are no longer valid after commit.  Call this method after commit to get a list of the
                successfully revised attribute groups. 
         Returns attributeGroups ( AttributeGroup List[NX):   .
        """
        pass
import NXOpen
class AttributeGroup(NXOpen.NXObject): 
    """ Represents an attribute group. """
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the display name for the attribute group.  
             
         
        """
        pass
    def DetachAttributeGroup(self, attributeGroupOwner: IAttributeGroupOwner) -> None:
        """
         Detaches Attribute Group 
        """
        pass
    def GetReferencingAttributeGroupOwners(self) -> List[IAttributeGroupOwner]:
        """
         Returns a list of NXOpen.PDM.IAttributeGroupOwner objects referencing this attribute group. 
         Returns attributeGroupOwners ( IAttributeGroupOwner List[NX):   .
        """
        pass
class AttributeSearchFilterTerm(SearchFilterTerm): 
    """ This search filter term can be used to filter based on attributes. """
    def AddValue(self, internalValue: str, displayValue: str) -> None:
        """
         This function adds a property value to the filter. 
        """
        pass
    def ClearAllValues(self) -> None:
        """
         This function removes all property values from the filter. 
        """
        pass
    def GetExcludeToggle(self) -> bool:
        """
         This function gets whether the term is excluded or included. 
         Returns excludeToggle (bool): .
        """
        pass
    def HasValue(self, internalValue: str) -> bool:
        """
         This function checks if the search filter term has a specified value. 
         Returns hasValue (bool): .
        """
        pass
    def RemoveValue(self, internalValue: str) -> None:
        """
         This function removes a property value from the filter. 
        """
        pass
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets whether the term is excluded or included. 
        """
        pass
import NXOpen
class CaeCloneManager(NXOpen.TransientObject): 
    """  This class is used for executing CAE Clone on a Simulation File or a FeModel File.
     """
    class CloneOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |Sim|  
         |Fem|  
         |Ideal|  
         |Master|  

        """
        NotSet: int
        Sim: int
        Fem: int
        Ideal: int
        Master: int
        @staticmethod
        def ValueOf(value: int) -> CaeCloneManager.CloneOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CommitClone(self) -> None:
        """
         Commits the Clone Operation for the Clone Manager class NXOpen.PDM.CaeCloneManager.
                Deletes all the Part Builders associated with the Clone Manager
                
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def GetContainer(self, option: CaeCloneManager.CloneOption) -> str:
        """
                Gets the container in Teamcenter where the cloned part is saved
                
         Returns container (str): .
        """
        pass
    def GetPartBuilderForClone(self, option: CaeCloneManager.CloneOption) -> PartFromPartBuilder:
        """
         Get Part Builders for Clone Operation of a CAE Simulation or a CAE Model part.  
                Get  builder class NXOpen.PDM.PartFromPartBuilder using this function.
                
         Returns part_builder ( PartFromPartBuilder NXOp):  the part builder .
        """
        pass
    def SetContainer(self, option: CaeCloneManager.CloneOption, container: str) -> None:
        """
                Sets the container in Teamcenter where the cloned part is saved
                
        """
        pass
    def SetIncludeMaster(self, value: bool) -> None:
        """
                Sets the option for include master on the Clone Manager class 
                
        """
        pass
import NXOpen
class CAEFileContainer(NXOpen.TransientObject): 
    """  This class is a File Container class for uploading JT files created by NX CAE Post Processing to Teamcenter. 
    Users can add the JT file names and their corresponding dataset names to this container class.
    Once all the JT file names are added, this class can be used to upload the JT files to Teamcenter.
    The class can be used to upload only to a a single part at a time.
     """
    def AddFile(self, datasetname: str, filename: str) -> None:
        """
          Add a file to the list of files in the file container class NXOpen.PDM.CAEFileContainer.
        """
        pass
    def DeleteFile(self, datasetname: str, filename: str) -> None:
        """
          Delete a file from the list of files in the file container class NXOpen.PDM.CAEFileContainer.
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def DoUpload(self) -> None:
        """
          Upload CAE files to Teamcenter, independent of a standard file-save.  
                Upload all the files in the file container class NXOpen.PDM.CAEFileContainer using this function.
                The JT files should be present in the temporary directory of the system prior to calling this function.
                
        """
        pass
    def GetOwningPart(self) -> str:
        """
         Get the part tag of the owning part of the class NXOpen.PDM.CAEFileContainer.
         Returns partspec (str): .
        """
        pass
    def SetOwningPart(self, partspec: str) -> None:
        """
         Sets the part tag of the owning part of the class NXOpen.PDM.CAEFileContainer.
        """
        pass
class CloneRelatedCae(Enum):
    """
    Members Include: 
     |SimFemIdeal| 
     |FemIdeal| 
     |Ideal| 
     |NotSet| 

    """
    SimFemIdeal: int
    FemIdeal: int
    Ideal: int
    NotSet: int
    @staticmethod
    def ValueOf(value: int) -> CloneRelatedCae:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ConditionalElementRevision(ModelElement): 
    """ 
        Represents a base class that provides common methods for various conditional model elements in a NXOpen.CollaborativeDesign.
    """
    @property
    def EffectivityFormula(self) -> str:
        """
        Getter for property: (str) EffectivityFormula
         Returns the formula string that represents the effectivity of this object in database.  
          
                  
         
        """
        pass
import NXOpen
class ConfigurationContextBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.PDM.ConfigurationContextBuilder builder """
    class ConfigContextMode(Enum):
        """
        Members Include: 
         |Nx4gd| 
         |Assemblies| 
         |ReturnConfigContextDontSetCurrent| 
         |CustomConfigContext| 

        """
        Nx4gd: int
        Assemblies: int
        ReturnConfigContextDontSetCurrent: int
        CustomConfigContext: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurationContextBuilder.ConfigContextMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConfigContextType(Enum):
        """
        Members Include: 
         |AsSaved| 
         |PushedfromTeamcenter| 
         |DefineorLoadContext| 

        """
        AsSaved: int
        PushedfromTeamcenter: int
        DefineorLoadContext: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurationContextBuilder.ConfigContextType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConfigurationDetail(Enum):
        """
        Members Include: 
         |LoadfromTeamcenter| 
         |DefineinNX| 

        """
        LoadfromTeamcenter: int
        DefineinNX: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurationContextBuilder.ConfigurationDetail:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: ( NXOpen.CollaborativeDesign) CollaborativeDesign
         Returns the collaborative design   
            
         
        """
        pass
    @CollaborativeDesign.setter
    def CollaborativeDesign(self, collaborativeDesign: NXOpen.CollaborativeDesign):
        """
        Setter for property: ( NXOpen.CollaborativeDesign) CollaborativeDesign
         Returns the collaborative design   
            
         
        """
        pass
    @property
    def ConfigDetail(self) -> ConfigurationContextBuilder.ConfigurationDetail:
        """
        Getter for property: ( ConfigurationContextBuilder.ConfigurationDetail NXOp) ConfigDetail
         Returns the configuration detail   
            
         
        """
        pass
    @ConfigDetail.setter
    def ConfigDetail(self, configDetail: ConfigurationContextBuilder.ConfigurationDetail):
        """
        Setter for property: ( ConfigurationContextBuilder.ConfigurationDetail NXOp) ConfigDetail
         Returns the configuration detail   
            
         
        """
        pass
    @property
    def ConfigMode(self) -> ConfigurationContextBuilder.ConfigContextMode:
        """
        Getter for property: ( ConfigurationContextBuilder.ConfigContextMode NXOp) ConfigMode
         Returns the configuration mode   
            
         
        """
        pass
    @property
    def ConfigType(self) -> ConfigurationContextBuilder.ConfigContextType:
        """
        Getter for property: ( ConfigurationContextBuilder.ConfigContextType NXOp) ConfigType
         Returns the configuration type   
            
         
        """
        pass
    @ConfigType.setter
    def ConfigType(self, configType: ConfigurationContextBuilder.ConfigContextType):
        """
        Setter for property: ( ConfigurationContextBuilder.ConfigContextType NXOp) ConfigType
         Returns the configuration type   
            
         
        """
        pass
    @property
    def ContentDefinition(self) -> NXOpen.ContentDefinition:
        """
        Getter for property: ( NXOpen.ContentDefinition) ContentDefinition
         Returns the  NXOpen::ContentDefinition  of the subset.  
           
                  
         
        """
        pass
    @ContentDefinition.setter
    def ContentDefinition(self, contentDefinition: NXOpen.ContentDefinition):
        """
        Setter for property: ( NXOpen.ContentDefinition) ContentDefinition
         Returns the  NXOpen::ContentDefinition  of the subset.  
           
                  
         
        """
        pass
    @property
    def EffectivityTable(self) -> EffectivityTableBuilder:
        """
        Getter for property: ( EffectivityTableBuilder NXOp) EffectivityTable
         Returns the  NXOpen::PDM::EffectivityTableBuilder  builder used to edit the effectivity   
            
         
        """
        pass
    @property
    def OverrideFolder(self) -> str:
        """
        Getter for property: (str) OverrideFolder
         Returns the override folder   
            
         
        """
        pass
    @OverrideFolder.setter
    def OverrideFolder(self, folderName: str):
        """
        Setter for property: (str) OverrideFolder
         Returns the override folder   
            
         
        """
        pass
    @property
    def RevisionRule(self) -> str:
        """
        Getter for property: (str) RevisionRule
         Returns the revision rule    
            
         
        """
        pass
    @RevisionRule.setter
    def RevisionRule(self, revisionRule: str):
        """
        Setter for property: (str) RevisionRule
         Returns the revision rule    
            
         
        """
        pass
    @property
    def VariantConfiguration(self) -> VariantConfigurationBuilder:
        """
        Getter for property: ( VariantConfigurationBuilder NXOp) VariantConfiguration
         Returns the  NXOpen::PDM::VariantConfigurationBuilder  builder used to edit variant rule configuration   
            
         
        """
        pass
import NXOpen
class ConfigurationContext(NXOpen.NXObject): 
    """ Represents a Teamcenter Integration configuration context """
    pass
import NXOpen
class ConfigurationManager(NXOpen.Object): 
    """ Represents Configuration Manager  """
    def CreateConfigurationContextBuilder() -> ConfigurationContextBuilder:
        """
         Creates a new NXOpen.PDM.ConfigurationContextBuilder object for 
                     NXOpen.PDM.ConfigurationContextBuilder.ConfigContextMode.Assemblies 
                    mode configuration. 
         Returns builder ( ConfigurationContextBuilder NXOp): .
        """
        pass
    def CreateConfigurationContextBuilderForMultiConfig() -> ConfigurationContextBuilder:
        """
         Creates a new NXOpen.PDM.ConfigurationContextBuilder object for 
                     NXOpen.PDM.ConfigurationContextBuilder.ConfigContextMode.ReturnConfigContextDontSetCurrent 
                    mode configuration. 
         Returns builder ( ConfigurationContextBuilder NXOp): .
        """
        pass
    def CreateDesignWorksetProductConfigurationContextBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> ConfigurationContextBuilder:
        """
         Creates a new NXOpen.PDM.ConfigurationContextBuilder object which maintains custom config context of product part in design workset. 
         Returns builder ( ConfigurationContextBuilder NXOp): .
        """
        pass
    def CreateEffectivityAttributePropertiesBuilder(part: NXOpen.BasePart, objects: List[NXOpen.NXObject]) -> EffectivityAttributePropertiesBuilder:
        """
         Creates a new NXOpen.PDM.EffectivityAttributePropertiesBuilder object. 
         Returns builder ( EffectivityAttributePropertiesBuilder NXOp): .
        """
        pass
    def CreateVariantRulesConfigurationBuilder(part: NXOpen.BasePart) -> VariantRulesConfigurationBuilder:
        """
         Creates a new NXOpen.PDM.VariantRulesConfigurationBuilder object. 
         Returns builder ( VariantRulesConfigurationBuilder NXOp): .
        """
        pass
class ConnectionElementRevision(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    pass
class ConversionRule(Enum):
    """
    Members Include: 
     |WithPrefix| 
     |WithSuffix| 
     |WithReplaceString| 
     |WithRename| 
     |MixedRule| 

    """
    WithPrefix: int
    WithSuffix: int
    WithReplaceString: int
    WithRename: int
    MixedRule: int
    @staticmethod
    def ValueOf(value: int) -> ConversionRule:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CreateSessionBuilder(PartOperationCreateBuilder): 
    """ Represents a builder class that performs Create operations """
    def AutoAssignSessionNameOnPartSelection(self) -> None:
        """
         Auto assign session name 
        """
        pass
    def CreateLogicalObjectsForDialog(self) -> List[LogicalObject]:
        """
         Creates the pre-creation objects for the parts 
         Returns logicalObjects ( LogicalObject List[NX): .
        """
        pass
    def GetSelectedPart(self) -> str:
        """
         Returns the selected part 
         Returns selectedPartName (str): .
        """
        pass
    def GetSelectedSessionType(self) -> int:
        """
         Returns the selected session type 
         Returns sessionType (int): .
        """
        pass
    def GetSessionTypes(self) -> List[str]:
        """
         Returns all session types
         Returns sessionTypes (List[str]):  the session types .
        """
        pass
    def IsAllowSessionNameAutoAssignOnPartSelection(self) -> bool:
        """
         Returns logical value to indicate whether the session name is auto assigned 
         Returns allowSessionNameAutoAssignOnPartSelection (bool): .
        """
        pass
    def SetAllowSessionNameAutoAssignOnPartSelection(self, allowSessionNameAutoAssignOnPartSelection: bool) -> None:
        """
         Sets logical value to indicate whether the session name is auto assigned 
        """
        pass
    def SetSelectedPart(self, selectedPartName: str) -> None:
        """
         Sets the selected part 
        """
        pass
    def SetSelectedSessionType(self, sessionType: int) -> None:
        """
         Sets the selected session type 
        """
        pass
class CrossSheetReference(ModelElement): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    pass
import NXOpen
class CustomWebAppMenuHandler(NXOpen.TransientObject): 
    """ Represents Custom WebApp Menu Handler class """
    CustomWebAppInvokedCallback = Callable[[], None]
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                   it is illegal to use the object.  In .NET, this method is automatically
                   called when the object is deleted by the garbage collector. 
               
        """
        pass
    def GetCommandName(self) -> str:
        """
         Returns the command name 
         Returns command_name (str):  the command name .
        """
        pass
    def GetSelectedUids(self) -> List[str]:
        """
         Returns the unique identifier of the uids in PDM 
         Returns uids (List[str]):  Selected uids .
        """
        pass
    def RegisterCustomWebAppInvokedCallback(self, webapp_cb: CustomWebAppMenuHandler.CustomWebAppInvokedCallback) -> None:
        """
         Registers the add_custom_web_app_menu_callback callback method with the webApp menu
                   handler object.
        """
        pass
import NXOpen
class DatabaseAttributeManager(NXOpen.TransientObject): 
    """ This class is responsible for setting and getting NX Manager database attribute. """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def GetAttribute(self, attribute_title: str) -> str:
        """
         Gets the value of a writable database attribute. 
         Returns attribute_value (str):  the value of the attribute .
        """
        pass
    def LoadAttributes(self, reload: bool) -> None:
        """
         Load the Database Attributes from Teamcenter.
                This operation will not discard any changes made in this session that aren't committed to Teamcenter.
                If 'reload' is set to 'true', attributes that have already been loaded will be loaded again, if otherwise allowed.
                 
        """
        pass
    def LoadAttributesRecursively(self, reload: bool) -> None:
        """
         Recursively load the Database Attributes of this part and all its partially or fully loaded components from Teamcenter. 
                This operation will not discard any changes made in this session that aren't committed to Teamcenter.
                 
        """
        pass
    def RefreshAttributes(self) -> None:
        """
         Force load the Database Attributes from Teamcenter. This removes changes to values made in NX. 
        """
        pass
    def SetAttribute(self, attribute_title: str, attribute_value: str) -> None:
        """
         Sets the value of a writable database attribute. 
        """
        pass
    def StoreAttributes(self) -> None:
        """
         Register DB_PART_NAME and DB_PART_DESC attributes with values set in the attribute_manager 
        """
        pass
import NXOpen
class DatabaseObjectManager(NXOpen.TransientObject): 
    """  This class is used for retrieving PDM database objects.  """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def FindDesignSessionObjects(self, designSessionParamNames: List[str], designSessionParamValues: List[str]) -> DatabaseObject:
        """
         This API finds database object for specified design session search criteria in the Teamcenter database using saved query.
                This API will return NXOpen.PDM.DatabaseObject only if session name is unique, else it will return error.
                Note: Search criteria parameter should contain object_name(Required), object_type(optional), UID(optional) etc.
         Returns databaseObject ( DatabaseObject NXOp):  Database object .
        """
        pass
    def FindObjects(self, findCriterias: List[FindCriteria]) -> List[DatabaseObjects]:
        """
         This API finds database objects in the Teamcenter database using a Teamcenter saved query. 
         Returns databaseObjects ( DatabaseObjects List[NX):  Database objects .
        """
        pass
    def GetDatabaseObjectFromAppSessionUid(self, uId: str) -> DatabaseObject:
        """
         Gets a database object from UID 
         Returns databaseObject ( DatabaseObject NXOp):  Database object .
        """
        pass
    def NewDatabaseobjects(self) -> DatabaseObjects:
        """
         This API constructs a new NXOpen.PDM.DatabaseObjects object. 
         Returns databaseObjects ( DatabaseObjects NXOp):  Database objects .
        """
        pass
    def NewFindcriteria(self, nCriteria: int) -> List[FindCriteria]:
        """
         This API constructs an array of empty NXOpen.PDM.FindCriteria objects. 
         Returns findCriterias ( FindCriteria List[NX):  Find criteria .
        """
        pass
import NXOpen
class DatabaseObjects(NXOpen.TransientObject): 
    """ Represents a collection of NXOpen.PDM.DatabaseObject. """
    def Append(self, databaseObjects: List[DatabaseObjects]) -> None:
        """
         This API appends to the collection of NXOpen.PDM.DatabaseObject. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetDatabaseObjects(self) -> List[DatabaseObject]:
        """
         This API returns the collection of NXOpen.PDM.DatabaseObject as an array. 
         Returns databaseObjects ( DatabaseObject List[NX):  Database objects .
        """
        pass
    def SetDatabaseObjects(self, databaseObjects: List[DatabaseObject]) -> None:
        """
         This API sets the collection of NXOpen.PDM.DatabaseObject. 
        """
        pass
import NXOpen
class DatabaseObject(NXOpen.TransientObject): 
    """ Represents a Teamcenter database object """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
import NXOpen
class DBEntityProxyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.PDM.DBEntityProxy objects """
    def CreateDbEntityProxy(self, title: str, index: int, context: NXOpen.TaggedObject, attributeOwner: NXOpen.TaggedObject) -> DBEntityProxy:
        """
         Creates a NXOpen.PDM.DBEntityProxy 
         Returns dbentityProxy ( DBEntityProxy NXOp): .
        """
        pass
    def FindProxy(self, journal_identifier: str) -> NXOpen.NXObject:
        """
         Find the DBEntityProxy object with input name 
         Returns found ( NXOpen.NXObject):  DBEntity Object with this identifier .
        """
        pass
import NXOpen
class DBEntityProxy(NXOpen.NXObject): 
    """ JA class for the DBEntityProxy object"""
    pass
import NXOpen
class DesignElementRevision(ModelElementRevision): 
    """
        Represents the design element revision in the database. An instance of this class can be obtained from the NXOpen.Assemblies.Component.
    """
    class DesignElementCategory(Enum):
        """
        Members Include: 
         |Shape| 
         |Reuse| 
         |Promissory| 
         |DesignControlElement| 

        """
        Shape: int
        Reuse: int
        Promissory: int
        DesignControlElement: int
        @staticmethod
        def ValueOf(value: int) -> DesignElementRevision.DesignElementCategory:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Category(self) -> DesignElementRevision.DesignElementCategory:
        """
        Getter for property: ( DesignElementRevision.DesignElementCategory NXOp) Category
         Returns the category for design element.  
           Category can be unknown 
                    if the design element is new and does not yet exist in database.
                  
         
        """
        pass
    @property
    def DesignPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) DesignPart
         Returns the part of the underlying design element.  
           This can be NULL for a promissory design element.
                  
         
        """
        pass
    @property
    def Modified(self) -> bool:
        """
        Getter for property: (bool) Modified
         Returns
                    whether the selected  NXOpen::PDM::DesignElementRevision  is modified in the session.  
          
                  
         
        """
        pass
    def GetDesignSubordinateRevisions(self) -> List[DesignSubordinateRevision]:
        """
         
                    Get the immediate child NXOpen.PDM.DesignSubordinateRevision objects.
                    This will return .for non subordinate design element.
                 
         Returns designSubordinateRevision ( DesignSubordinateRevision List[NX): .
        """
        pass
    def GetTransform(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Point3d]:
        """
         Get the transform.
                    Note: The translation component is in meters.
                
         Returns A tuple consisting of (orientation, positionInMeters). 
         - orientation is:  NXOpen.Matrix3x3.
         - positionInMeters is:  NXOpen.Point3d.

        """
        pass
class DesignFeatureRevision(ModelElementRevision): 
    """
        Represents the design feature revision in the database.
    """
    pass
import NXOpen
class DesignSubordinateRevision(ModelElementRevision): 
    """
        Represents the design subordinate revision in the database. An instance of this class can be obtained from the NXOpen.Assemblies.Component.
    """
    @property
    def DesignPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) DesignPart
         Returns the underlying loaded part of this subordinate.  
           Note that it will return NULL if part is not loaded.
                  
         
        """
        pass
    @property
    def Modified(self) -> bool:
        """
        Getter for property: (bool) Modified
         Returns
                    whether the selected  NXOpen::PDM::DesignSubordinateRevision  is modified in the session.  
          
                  
         
        """
        pass
    @property
    def RootDesignElementRevision(self) -> DesignElementRevision:
        """
        Getter for property: ( DesignElementRevision NXOp) RootDesignElementRevision
         Returns the root reuse design element revision.  
          
                  
         
        """
        pass
import NXOpen
class EffectivityAttributePropertiesBuilder(NXOpen.Builder): 
    """
        Represents an NXOpen.PDM.EffectivityAttributePropertiesBuilder to be used for creating effectivity attributes.
        The attribute will be distributed to all objects supplied in the selected object list.
    """
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category.  
            The category is an optional, user-defined string that allows 
                attributes to be grouped together.   
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the category.  
            The category is an optional, user-defined string that allows 
                attributes to be grouped together.   
         
        """
        pass
    @property
    def DisplayValue(self) -> str:
        """
        Getter for property: (str) DisplayValue
         Returns the display value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    @DisplayValue.setter
    def DisplayValue(self, displayValue: str):
        """
        Setter for property: (str) DisplayValue
         Returns the display value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    @property
    def EffectivityTableBuilder(self) -> EffectivityTableBuilder:
        """
        Getter for property: ( EffectivityTableBuilder NXOp) EffectivityTableBuilder
         Returns the effectivity table builder.  
             
         
        """
        pass
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedObjects
         Returns the selected object(s) list.  
            The created attribute will be applied to
                all objects in this list.    
         
        """
        pass
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returns the string value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the attribute title.  
            The title is required for creating an attribute
                and must be unique on the given object.  Once the attribute is created,
                the title cannot be modified.   
         
        """
        pass
    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the attribute title.  
            The title is required for creating an attribute
                and must be unique on the given object.  Once the attribute is created,
                the title cannot be modified.   
         
        """
        pass
    def CreateAttribute(self) -> bool:
        """
         Create the attribute from the data set in the builder.  Unlike calling commit,
                this method will not perform an update.  
         Returns changed (bool):  True if the attribute was creatededited successfully .
        """
        pass
    def Delete(self, objectValue: NXOpen.NXObject) -> None:
        """
         Delete the attribute from the given object. 
        """
        pass
    def SetAttributeObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets the array of objects that have this attribute 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class EffectivityTableBuilder(NXOpen.TaggedObject): 
    """ Represents a builder class for effectivity configuration. """
    def AddEffectivityRow(self, effectivityRow: EffectivityTableRow) -> None:
        """
         Adds the given effectivity row to NXOpen.PDM.EffectivityTableBuilder 
        """
        pass
    def Commit(self) -> None:
        """
         Commit the modified effectivity rows 
        """
        pass
    def CreateNewEffectivityRow(self) -> EffectivityTableRow:
        """
         Creates new effectivity row in NXOpen.PDM.EffectivityTableBuilder object 
         Returns effectivityRow ( EffectivityTableRow NXOp):  newly created empty effectivity row .
        """
        pass
    def GetEffectivityRows(self) -> List[EffectivityTableRow]:
        """
         Gets the existing effectivity rows from effectivity table
         Returns effectivityRows ( EffectivityTableRow List[NX): .
        """
        pass
    def RemoveEffectivityRows(self, effectivityRows: List[EffectivityTableRow]) -> None:
        """
         Removes the given effectivity rows from NXOpen.PDM.EffectivityTableBuilder 
        """
        pass
    def UpdateBuilderDetails(self, cd: NXOpen.CollaborativeDesign, validationBasisFormula: str, effectivityFormulae: List[str]) -> None:
        """
         Updates this builder with new NXOpen.CollaborativeDesign, validation basis formula and effectivity formulae to edit.
                    Effectivity formulae will be validated against provided validation basis formula.
                
        """
        pass
import NXOpen
class EffectivityTableRow(NXOpen.NXObject): 
    """
        Represents the class that contains effectivity parameters.
    """
    pass
class ElementGroup(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    pass
import NXOpen
class ErrorMessageHandler(NXOpen.TransientObject): 
    """
        Represents the class that contains ErrorObjects and Failed Logical Objects.
    """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def GetErrorList(self) -> NXOpen.ErrorList:
        """
         Returns ERROR_LIST_s 
         Returns errorList ( NXOpen.ErrorList): .
        """
        pass
    def GetErrorMessages(self) -> List[str]:
        """
         Returns Error Messages 
         Returns errorMessages (List[str]):  Error Messages  .
        """
        pass
    def GetWarningMessages(self) -> List[str]:
        """
         Returns Warning Messages 
         Returns warningMessages (List[str]):  Warning Messages  .
        """
        pass
class ExistingPartAction(Enum):
    """
    Members Include: 
     |Overwrite| 
     |UseExisting| 
     |Exclude| 
     |Clone| 
     |Retain| 
     |Default| 

    """
    Overwrite: int
    UseExisting: int
    Exclude: int
    Clone: int
    Retain: int
    Default: int
    @staticmethod
    def ValueOf(value: int) -> ExistingPartAction:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ExportFromTeamcenter(ICloneOperation): 
    """ Represents a Export class that performs Create operations """
    def AddDFAFile(self, dfaFile: str) -> None:
        """
         This API adds the dfa file to the export operation. 
        """
        pass
    def CreateZipFileOfExportedParts(self, zipFilePath: str, overwrite: bool) -> int:
        """
         This API creates the zip of exported parts. 
         Returns status (int): .
        """
        pass
    def ExportDFAFiles(self, dfaFiles: List[str], defDir: str, doMixins: bool) -> None:
        """
         This API exports the dfa files to the the specified export directory. 
        """
        pass
    def SetAddDfaMixins(self, isAddDfaMixins: bool) -> None:
        """
         This API specifies whether to add DFA mixins or not. 
        """
        pass
    def SetAssociatedFilesDir(self, objectToBeCloned: AssyCloneCompDisp, directoryName: str) -> None:
        """
         This API sets the directory in which associated files for the specified component will be placed. 
        """
        pass
    def SetAssociatedFilesRootDir(self, rootDirName: str) -> None:
        """
         This API sets the root directory below which part specific associated file directories will be placed.
                    If the associated files root directory is not set then the associated files will be copied to the directory
                    of the exported parts.
                
        """
        pass
    def SetCheckOutData(self, objectToBeCloned: AssyCloneCompDisp, checkoutComment: str) -> int:
        """
         This API sets the check-out data to be used for checking out a particular part. 
         Returns status (int): .
        """
        pass
    def SetDefaultCheckOutData(self, checkoutComment: str) -> None:
        """
         This API sets the default check-out data to be used for checking out all the exported parts. 
        """
        pass
    def SetDefaultDirectory(self, directoryName: str) -> None:
        """
         This API sets the default directory for the parts created during export will be placed in.
                    If this option is never set then the current directory will be used.
                    Note: This option is ignored for user name numbering technique.
                
        """
        pass
    def SetExportDfaWithPart(self, isExportDfaWithPart: bool) -> None:
        """
         This API specifies whether to export DFA file or not. 
        """
        pass
    def SetExternalFiles(self, setExternalFiles: bool) -> None:
        """
         This API sets the option to export the related External files during export operation. 
        """
        pass
    def SetIdentifierDisplayRule(self, displayRule: str) -> None:
        """
         This API stores the current identifier display rule as previous identifier display rule and then sets new for current export session. 
        """
        pass
import NXOpen
class ExportWorksetForReferenceBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Create operations """
    @property
    def DestinationFolder(self) -> str:
        """
        Getter for property: (str) DestinationFolder
         Returns the export directory path   
            
         
        """
        pass
    @DestinationFolder.setter
    def DestinationFolder(self, folderPath: str):
        """
        Setter for property: (str) DestinationFolder
         Returns the export directory path   
            
         
        """
        pass
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets the objects for the modified objects in session. 
         Returns objects ( NXOpen.NXObject Li): .
        """
        pass
    def ValidateObjects(self) -> NXOpen.ErrorList:
        """
         Validate the inputs provided for export 
         Returns validationFailures ( NXOpen.ErrorList): .
        """
        pass
import NXOpen
class ExternalFileReferenceListBuilder(NXOpen.Builder): 
    """ Represents a builder class """
    def GetExternalFileObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets the external file objects for the source part. 
         Returns objects ( NXOpen.NXObject Li): .
        """
        pass
import NXOpen
class FileManagement(NXOpen.TransientObject): 
    """ This class is responsible for Teamcenter file management related activities.  """
    class FileType(Enum):
        """
        Members Include: 
         |CmmDmi| 
         |CpdFeaturePart|  
         |CpdGeometryOverride|  
         |DirectModel|  
         |Excel|  
         |ExcelX|  
         |Image|  
         |Jpeg|  
         |NxDesignatorAssignmentsFile|  
         |NxAttachedPart|  
         |NxPart|  
         |NxPosBin|  
         |NxleSymbolXml|  
         |NxleSymbolPreview|  
         |Preview2d|  
         |Preview3d|  
         |QafBinary|  
         |QafText|  
         |RoutePipeRun|  
         |RoutePipeSpec|  
         |RoutePipeSpecAttr|  
         |RoutePipeRunAttachment|  
         |Text|  
         |Tif|  
         |TrushapeData|  
         |ValidationRuleSet|  

        """
        CmmDmi: int
        CpdFeaturePart: int
        CpdGeometryOverride: int
        DirectModel: int
        Excel: int
        ExcelX: int
        Image: int
        Jpeg: int
        NxDesignatorAssignmentsFile: int
        NxAttachedPart: int
        NxPart: int
        NxPosBin: int
        NxleSymbolXml: int
        NxleSymbolPreview: int
        Preview2d: int
        Preview3d: int
        QafBinary: int
        QafText: int
        RoutePipeRun: int
        RoutePipeSpec: int
        RoutePipeSpecAttr: int
        RoutePipeRunAttachment: int
        Text: int
        Tif: int
        TrushapeData: int
        ValidationRuleSet: int
        @staticmethod
        def ValueOf(value: int) -> FileManagement.FileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def DeleteAttachedFiles(self, associatedObject: List[NXOpen.NXObject], associationTypeName: List[str], datasetTypeName: List[str], datasetName: List[str], namedReferenceName: List[str], isText: List[str], logicalFileName: List[str], keepEmptyDataset: bool) -> List[int]:
        """
         Delete Attached Files From Teamcenter.
                Delete attached files from dataset.
                 . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
                 . associationTypeName - Teamcenter relation type name
                 . datasetTypeName - Teamcenter dataset type name
                 . datasetName - Dataset name for creation or for matching existing dataset
                 . namedReferenceName - Named reference name
                 . isText - Named reference isText flag
                 . logicalFileName - Named reference logical filename
                 . keepEmptyDataset - Flag indicating if datasets should be kept even if they become empty
                
         Returns resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
        """
        pass
    def DeleteExistingAttachedFiles(self, files: List[PdmFile], keepEmptyDataset: bool) -> List[int]:
        """
         Delete Attached Files From Teamcenter.
                Delete given attached files from dataset.
                
         Returns resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def DownloadAssociatedFiles(self, parts: List[NXOpen.BasePart], files: List[PdmFile]) -> None:
        """
          Download the specified named reference files for NX use. 
        """
        pass
    def ExportFiles(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], baseDirectoryNames: List[str], toolNames: List[str]) -> Tuple[List[int], List[str]]:
        """
         Exports all associated files for the specified dataset(s)
                to a directory. The dataset(s) are identified by their Teamcenter 
                item id, Teamcenter item revision id, Teamcenter dataset name, 
                NX dataset type, and  NX dataset relation type.  A base export directory
                name must be specified for each dataset along with the tool name that
                is requesting the export.  The full path to the exported files is 
                returned in an output array.  The full path will be 
                NX_default_directory or export_directory.  Additionally, an array of
                PDI result codes is returned indicating the success (0) or failure 
                (non-zero) of each export.
                The dataset types for FOREIGN_MODEL are the ones included in the 
                Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
                input relation type should be "Foreign".
                The exporting of the associated file is governed by following conditions:        
                The associated filetype should be exportable for combination of the Tool 
                used and the Open action for operation.
                The associated file should not be in the excluded named reference list. 
                For Foreign Datasets it will not export file types included in the Teamcenter
                preference "TC_NX_Foreign_Datasets".
                In case of NX CAM dataset type like "UGCAMCLSF", "UGCAMPTP", "UGCAMShopDoc",
                all the associated files will be exported irrespective of above conditions.
                
                Excluded Named Reference List:
                "UGPART"             
                "UGPART-MASSPR            
                "UGPART-BBOX              
                "UGPART-ATTRIBUTES        
                "UGPART-ATTR             
                "Trushape-Data            
                "BVRSYNCINFO              
                "UG-QuickAccess-Binary    
                "UG-QuickAccess-Text   
                
                
                NX dataset types and relation names
                NX Model Type         NX Relation Type        NX Dataset Type
                MASTER_MODEL          "has shape"             "UGMASTER"
                SPEC_MODEL            "has specification"     "UGPART"
                MAN_MODEL             "has manifestation"     "UGPART"
                ALTREP_MODEL          "has altrep"            "UGALTREP"
                SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"
                SIMULATION_MODEL      "NX_simulation"         "NXSimulation"
                MOTION_MODEL          "NX_simulation"         "NXMotion"
                CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"
                CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"
                CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"
                FOREIGN_MODEL         "Foreign"               ""
                MOTION_MODEL_SPEC     "has specification"     "MotionSim"
                
                For the input itemIds:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
         Returns A tuple consisting of (resultCodes, exportDirectoryNames). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
         - exportDirectoryNames is: List[str]. Resulting location of export directory .

        """
        pass
    @overload
    def ExportNamedReferences(self, itemId: str, itemRevisionId: str, datasetName: str, datasetTypeName: str, datasetRelationTypeName: str, datasetNamedReference: str, exportDirectoryName: str) -> List[str]:
        """
         Export Named Reference From Teamcenter.
                The Dataset Relation Type Names are the names of the Teamcenter relationships used to find the Datasets
                to the correponding Item Revisions.
                Any ImanRelation types can be used.
                
         Returns namedReferences (List[str]):  NamedReferences, full pathnames of files .
        """
        pass
    @overload
    def ExportNamedReferences(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], datasetNamedReferences: List[str], exportDirectoryName: str) -> Tuple[List[int], List[int], List[str]]:
        """
         Export Named Reference From Teamcenter.
                The Dataset Relation Type Names are the names of the Teamcenter relationships used to find the Datasets
                to the correponding Item Revisions.
                Any ImanRelation types can be used.
                
         Returns A tuple consisting of (resultCodes, numNamedReferences, namedReferences). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
         - numNamedReferences is: List[int]. Array of the number of named references for each itemid .
         - namedReferences is: List[str]. NamedReferences, full pathnames of files, array size is namedReferencesLength  .

        """
        pass
    def GetAssociatedFiles(self, parts: List[NXOpen.BasePart], fileTypesToExclude: List[FileManagement.FileType]) -> List[PdmFile]:
        """
          Given an NX part, this method will return a list of named
                reference files in the corresponding Teamcenter dataset. 
         Returns files ( PdmFile List[NX): .
        """
        pass
    def GetAttachedFiles(self, associatedObject: List[NXOpen.NXObject], associationTypeName: List[str], datasetTypeName: List[str], datasetName: List[str], namedReferenceName: List[str], isText: List[str], logicalFileName: List[str], exportDirectoryName: str) -> Tuple[List[int], List[int], List[PdmFile]]:
        """
         Get Attached Files Information From Teamcenter.
                Query attached files information for given specifications.
                 . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
                 . associationTypeName - Teamcenter relation type name
                 . datasetTypeName - Teamcenter dataset type name
                 . datasetName - Dataset name for creation or for matching existing dataset
                 . namedReferenceName - Named reference name
                 . isText - Named reference isText flag
                 . logicalFileName - Named reference logical filename
                 . exportDirectoryName - Where to export files to, if empty then files will not be downloaded
                 . outputFilesLength - Number of total files returned
                
         Returns A tuple consisting of (resultCodes, numOutputFiles, files). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
         - numOutputFiles is: List[int]. Number of output files for each input .
         - files is:  PdmFile List[NX. Output - arry of PdmFiles .

        """
        pass
    def ImportFiles(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], importDirectoryNames: List[str]) -> List[int]:
        """
         Imports all associated files for the specified dataset(s)
                into the Teamcenter database.  The files will be attached to the
                dataset(s) as named references.  The dataset(s) are identified by
                their Teamcenter multifield key, Teamcenter item revision id, Teamcenter 
                dataset name, NX dataset type, and NX dataset relation type.  
                An import directory containing the files must be specified for each 
                dataset.  An array of PDI result codes is returned indicating the 
                success (0) or failure (non-zero) of each import.
                The dataset types for FOREIGN_MODEL are the ones included in the 
                Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
                input relation type should be "Foreign". The named reference information
                from BMIDE setting will be used for the imported file extension.
                
                NX dataset types and relation names
                NX Model Type         NX Relation Type        NX Dataset Type
                MASTER_MODEL          "has shape"             "UGMASTER"
                SPEC_MODEL            "has specification"     "UGPART"
                MAN_MODEL             "has manifestation"     "UGPART"
                ALTREP_MODEL          "has altrep"            "UGALTREP"
                SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"
                SIMULATION_MODEL      "NX_simulation"         "NXSimulation"
                MOTION_MODEL          "NX_simulation"         "NXMotion"
                CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"
                CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"
                CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"
                FOREIGN_MODEL         "Foreign"               ""
                MOTION_MODEL_SPEC     "has specification"     "MotionSim"
                
                For the input itemIds:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
         Returns resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
        """
        pass
    def ImportFilesAndCreateDatasets(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], datasetToolNames: List[str], fileType: List[bool], namedReferenceNames: List[str], importFileNames: List[str], importFileDirectoryNames: List[str]) -> List[int]:
        """
         Import files and create datasets in Teamcenter.
                In order to create multiple datasets at once, please make sure to declare all the arrays of the same desired size.
                This creates the Items (with the specified item ids) and Item Revisions (with the specified item revision ids) in case they don't exist in Teamcenter.
                This creates the datasets if no matching dataset exists in Teamcenter.
                The dataset relation type names are the exact names of the Teamcenter relations used to attach the Datasets to the corresponding Item Revisions. (Any ImanRelation types can be used.)
                
         Returns resultCodes (List[int]):  Result codes. Success (zero), Failure (non-zero). .
        """
        pass
    def SaveAttachedFiles(self, associatedObject: List[NXOpen.NXObject], associationTypeName: List[str], datasetTypeName: List[str], datasetName: List[str], numDatasetPropertyInput: List[int], datasetPropertyNames: List[str], datasetPropertyValues: List[str], ownershipToMatchForNewDataset: List[NXOpen.NXObject], fileVolumeToStore: List[PdmFile], toolUsed: List[str], datasetDescription: List[str], alwaysCreateNewDataset: List[bool], createNewDatasetVersion: List[bool], refreshInSessionLoadedLMD: List[bool], numNamedReferencesPerInput: List[int], namedReferenceName: List[str], isText: List[bool], filePath: List[str], logicalFileName: List[str], allowReplace: List[bool], outputFiles: bool) -> Tuple[List[int], List[PdmFile]]:
        """
         Save Attached Files To Teamcenter.
                Save attached files for given specifications.
                 . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
                 . associationTypeName - Teamcenter relation type name
                 . datasetTypeName - Teamcenter dataset type name
                 . datasetName - Dataset name for creation or for matching existing dataset
                 . numDatasetPropertyInput - Number of dataset property names input for each dataset input
                 . numTotalDatasetProperties - Number of total dataset properties
                 . datasetPropertyNames - To specify required properties when creating new dataset or for updating existing dataset properties
                 . datasetPropertyValues - Dataset property values; need to match one-to-one with datasetPropertyNames
                 . ownershipToMatchForNewDataset - Teamcenter object used to assign new dataset owner, default is current user if not set
                 . fileVolumeToStore - Teamcenter volume for storing file, default is current session volume if not set
                 . toolUsed - Teamcenter toolUsed for new dataset
                 . datasetDescription - Dataset description for new dataset
                 . alwaysCreateNewDataset - Flag indicating if a new dataset should always be created
                 . createNewDatasetVersion - Flag indicating if new dataset version should be created
                 . refreshInSessionLoadedLMD - Flag indicating if in-session loaded Last-Modified-Date should be refreshed
                 . numNamedReferencesPerInput - Number of named references input for each dataset input
                 . numTotalNamedReferences - Number of total named references input
                 . namedReferenceName - Named reference name for each named reference input
                 . isText - Named reference isText flag for each named reference input
                 . filePath - Named reference file path for each named reference input
                 . logicalFileName - Named reference logical filename for each named reference input
                 . allowReplace - Flag indicating to replace if named reference already exists for each named reference input
                 . outputFiles - Flag indicating if files should be returned
                
         Returns A tuple consisting of (resultCodes, files). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). Array size is total number of named references .
         - files is:  PdmFile List[NX. Output - arry of PdmFiles. Array size is total number of named references .

        """
        pass
import NXOpen
class FindCriteria(NXOpen.TransientObject): 
    """ Represents find criteria objects """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetCriteria(self) -> Tuple[str, List[str], List[str]]:
        """
         This API returns the search query name, entries, and values. 
         Returns A tuple consisting of (queryName, entries, values). 
         - queryName is: str. Search query name .
         - entries is: List[str]. Search criteria entries .
         - values is: List[str]. Search criteria values .

        """
        pass
    def SetCriteria(self, queryName: str, entries: List[str], values: List[str]) -> None:
        """
         This API sets the search query name, entries, and values. 
        """
        pass
import NXOpen
class GenericObjectAttributeHolder(NXOpen.NXObject): 
    """
        Represents the class that contains database business logic or pre-creation information for the objects.
    """
    pass
import NXOpen
class IAttributeGroupOwner(NXOpen.Object): 
    """ An interface class for objects that own attribute groups. """
    @abstractmethod
    def Create(self, attributeGroupDescription: AttributeGroupDescription) -> AttributeGroup:
        """
         Creates an attribute group for a NXOpen.PDM.IAttributeGroupOwner, based on an attribute
                group type.  An attribute group type is represented by an NXOpen.PDM.AttributeGroupDescription.
            
         Returns attributeGroup ( AttributeGroup NXOp):  The new attribute group. .
        """
        pass
    @abstractmethod
    @overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: List[AttributeGroup]) -> AttributeGroupReviseBuilder:
        """
         Creates a NXOpen.PDM.AttributeGroupReviseBuilder object.  The builder creates a
                revision for each attribute group in the input list of existing attribute groups. 
         Returns attributeGroupReviseBuilder ( AttributeGroupReviseBuilder NXOp):   .
        """
        pass
    @abstractmethod
    @overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: List[AttributeGroup], keepOriginal: bool, saveAsActionType: AttributeGroupReviseBuilder.SaveAsActionType) -> AttributeGroupReviseBuilder:
        """
         The builder will do a revise or save-as operation for each attribute group in the input list of existing attribute groups 
                depending on input operation type. 
         Returns attributeGroupReviseBuilder ( AttributeGroupReviseBuilder NXOp):   .
        """
        pass
    @abstractmethod
    def GetAttributeGroupDescriptions(self) -> List[AttributeGroupDescription]:
        """
         Returns the NXOpen.PDM.AttributeGroupDescription objects representing the attribute
                group types supported by this object. 
         Returns attributeGroups ( AttributeGroupDescription List[NX):   .
        """
        pass
    @abstractmethod
    def GetAttributeGroups(self) -> List[AttributeGroup]:
        """
         Returns the NXOpen.PDM.AttributeGroup objects owned by this object. 
         Returns attributeGroups ( AttributeGroup List[NX):   .
        """
        pass
import NXOpen
class ICloneOperation(NXOpen.TaggedObject): 
    """ An interface to perform clone operations """
    def AddApplicationRelatedParts(self) -> None:
        """
         This API could be used by application to add related parts in exportclone operation. 
        """
        pass
    def AddAssembly(self, assemblyName: str) -> NXOpen.PartLoadStatus:
        """
         This API adds an assembly to the operation. Any load errors will be placed in the loadStatus argument. 
         Returns loadStatus ( NXOpen.PartLoadStatus): .
        """
        pass
    def AddPart(self, partName: str) -> None:
        """
         This API adds a part to the operation. If the part is an assembly part, any components
                    of the assembly, not already in the operation, will be added as name-only references. 
                
        """
        pass
    def ApplyCICODefaults(self) -> NXOpen.AssyCloneNamingFailures:
        """
         This API applies checkincheckout flags as appropriate for the export operation. 
         Returns namingWarnings ( NXOpen.AssyCloneNamingFailures): .
        """
        pass
    def ApplyDefaultsAndExecute(self, skipExecute: bool) -> Tuple[NXOpen.AssyCloneNamingFailures, NXOpen.AssyCloneNamingFailures]:
        """
         This API performs the exportclone operation, if any naming failures generated during the operation will be
                    reported through the namingFailures argument and naming warnings through namingWarnings argument.
                    In case of naming failures the operation will not be performed. 
                    If skipExecute is true, then only the default values will be populated on objects, but export operation will not be performed(just like dry run).
                    If skipExecute is false, then first default values will be populated on objects and then export will be performed.
                
         Returns A tuple consisting of (namingFailures, namingWarnings). 
         - namingFailures is:  NXOpen.AssyCloneNamingFailures.
         - namingWarnings is:  NXOpen.AssyCloneNamingFailures.

        """
        pass
    def AssignCloneNaming(self, objectToBeCloned: AssyCloneCompDisp, namingTechnique: NamingTechniqueOption, finalName: str) -> int:
        """
         This API assigns the final name for the cloned component using the specified naming technique option. 
         Returns status (int): .
        """
        pass
    def AssignCompDisposition(self, objectToBeCloned: AssyCloneCompDisp, action: ExistingPartAction) -> Tuple[bool, List[AssyCloneCompDisp], List[AssyCloneCompDisp]]:
        """
         This API assigns an explicit disposition to the specified object undergoing clone (which represents a component part referenced in the input assembly).
                    Specifying an explicit disposition assignment means the component will not take advantage of the default disposition value (even if the explicit
                    disposition assigned was equal to the current default disposition value).
                    Disposition assignments in a exportclone operation can trigger disposition cascading. Disposition cascading is the automatic assignment of
                    dispositions made to related components in order to protect the seed assembly from modification. If disposition cascading occurs as a result
                    of a disposition assignment, the 'cascadeDispositions' argument will be true. The 'cascadedComponentDispositions' argument will contain the list of objects
                    to which the cascaded disposition was assigned and 'numCascadedComponents' will indicate the number of objects in that list.
                
         Returns A tuple consisting of (cascadeDispositions, cascadedComponentDispositions, conflictingComponentDispositions). 
         - cascadeDispositions is: bool.
         - cascadedComponentDispositions is:  AssyCloneCompDisp List[NX.
         - conflictingComponentDispositions is:  AssyCloneCompDisp List[NX.

        """
        pass
    def AttachLogFileToAssociatedFiles(self, attachLogFileToAssociatedFiles: bool) -> None:
        """
         This API is used to specify whether to attach the clone log file as a associated file to root parts in exportclone operation. 
        """
        pass
    def CopyAssociatedFiles(self, copyAssociatedFiles: bool) -> None:
        """
         This API sets the option in the current exportclone operation indicating whether associated files 
                    should by default be exportedcloned in the current operation. Associated files will be exportedcloned to the 
                    associated files root directory set by the user. If the associated files root directory is not set
                    then it will be exportedcloned to the directory of the exportedcloned parts.
                
        """
        pass
    def CopyRelations(self, relationTypes: List[str], copyRelations: bool) -> None:
        """
         This API specifies whether the objects with the specified relation type to be exportedcloned when the component they are related to gets exportedcloned.
                    Relation types are strings containing the name of a nonmaster type defined in the database, such as 'manifestation', 'specification', and 'altrep'. 
                
        """
        pass
    def Destroy(self) -> None:
        """
         This API allows the destruction of an instance of the ICloneOpertion. 
        """
        pass
    def FetchObjects(self) -> List[AssyCloneCompDisp]:
        """
         This API fetches the tags of all the components(objects to be cloned) that are added in current exportclone operation. 
         Returns objectsToBeCloned ( AssyCloneCompDisp List[NX): .
        """
        pass
    def FetchObjectsToExcludeFromExport(self) -> List[AssyCloneCompDisp]:
        """
         This API fetches all the objects that are to be excluded from the export operation due to ExcludeReferenceOnly, ExcludeNGC and ExcludeSuppressed options. 
         Returns objectsToBeExcluded ( AssyCloneCompDisp List[NX): .
        """
        pass
    def InitCloneLog(self, logFileName: str) -> None:
        """
         This API will open a log file for writing. 
        """
        pass
    def LoadFromLogFile(self, logFileName: str) -> Tuple[NXOpen.AssyCloneNamingFailures, NXOpen.AssyCloneLogFileFailures, NXOpen.PartLoadStatus]:
        """
         This API reads the specified log file and applies the data in it to the current exportclone operation.
                    If any naming failures occur during loading the log file, these will be reported via the namingFailures  
                    argument and any errors related to log file will be reported through logFileFailures argument.
                    If processing the log file causes new assemblies to be loaded, then any errors
                    while loading the assembly will be reported through the loadStatus argument.
                    If both naming failures and load failures occur, it is not defined which error
                    code the return value of the function will be - if you wish to report both
                    you should check the n_failures member of the namingFailures structure and
                    the failed member of the loadStatus structure to see if errors have occurred.
                
         Returns A tuple consisting of (namingFailures, logFileFailures, loadStatus). 
         - namingFailures is:  NXOpen.AssyCloneNamingFailures.
         - logFileFailures is:  NXOpen.AssyCloneLogFileFailures.
         - loadStatus is:  NXOpen.PartLoadStatus.

        """
        pass
    def PerformPostCommit(self) -> None:
        """
         This API will perform application specific post-commit tasks. 
        """
        pass
    def PerformPreCommit(self) -> None:
        """
         This API will perform application specific pre-commit tasks. 
        """
        pass
    def RenameString(self, renameStr: str) -> None:
        """
         This API is used to generate final name for parts being exportedcloned using renameStr. 
                    Here 'renameStr' will be used as final name for the first part,
                    For the remaining parts to have unique names, _number(where number will be 1,2,3....) will be appended to renameStr to generate unique final names.
                
        """
        pass
    def ReplaceString(self, baseString: str, newString: str) -> None:
        """
         This API is used to generate final name for parts being exportedcloned, by replacing baseString with newString. 
        """
        pass
    def ReprocessNonComponentReferences(self) -> None:
        """
         This API will reprocess the non-component refs for objects to be exportedcloned which were not resolved first time. 
        """
        pass
    def SetCloneExcludeNGC(self, excludeNGC: bool) -> None:
        """
         This API sets the option to exclude the Non Geometric components from Export. 
        """
        pass
    def SetCloneExcludeReferenceOnly(self, excludeReferenceOnly: bool) -> None:
        """
         This API sets the option to exclude the reference only components from Export. 
        """
        pass
    def SetCloneRelatedCae(self, cloneRelatedCae: CloneRelatedCae) -> None:
        """
         This API sets the option to exportclone the related CAE parts when cloning any CAD parts. 
        """
        pass
    def SetCloneRelatedDrawings(self, cloneRelatedDrawings: bool) -> None:
        """
         This API sets the option to exportclone the related drawings when cloning any CAD parts. 
        """
        pass
    def SetConfigurationContextUsingRevRule(self, setDefault: bool, revisionRuleName: str) -> int:
        """
         This API sets the configuration context using the Revision Rule Name. 
         Returns status (int): .
        """
        pass
    def SetDefaultAction(self, defaultAction: ExistingPartAction) -> None:
        """
         This API sets the default action for the current exportclone operation. Any action inappropriate to the current operation will return an error. 
        """
        pass
    def SetDryRun(self, isDryRun: bool) -> None:
        """
         This API sets the dry run flag for the current exportclone operation. If this flag is true and JA_ICLONE_OPERATION_ApplyDefaultsAndExecute is called, 
                    the operation will actually not be performed. Please set JA_ICLONE_OPERATION_SetOutputLogFile for the log file to be generated.
                
        """
        pass
    def SetFinalName(self, objectToBeCloned: AssyCloneCompDisp, finalName: str, allowDuplicates: bool) -> None:
        """
         This API sets the final name on specified component. If duplicate names are identifed and allowDuplicates flag is true then
                    new name is generated for one of the component to avoid conflicts, if allowDuplicates flag is false then it will return
                    with appropriate error code. 
                
        """
        pass
    def SetLoadOption(self, loadOption: NXOpen.LoadOptions.ManagedModeLoadMethod) -> None:
        """
         This API sets the value of the assembly load option for managed mode. 
        """
        pass
    def SetMixedRuleString(self, prefixString: str, suffixString: str, stringToReplace: str, replacementString: str) -> None:
        """
         This API sets the mixed rule naming conversion type. 
                    It enables user to combine the naming rule conversion types prefix, suffix and replace.
                    User must give atleast one of the naming rules input as non-empty value for mixed rule to work. 
                    Note: To enable replace naming rule (i.e. JA_ICLONE_OPERATION_ConversionRule_WithReplaceString)
                    user must give both stringToReplace and replacementString as non-empty values
                
        """
        pass
    def SetNamingTechnique(self, namingTechnique: NamingTechniqueOption) -> None:
        """
         This API is used to set the naming technique, that will be used to generate final name for all the components being exportedcloned. 
        """
        pass
    def SetOutputLogFile(self, logFileName: str) -> None:
        """
         This API is used to specify the absolute path name of the log-file to be used to record exportclone operation,
                    If the value specified is NULL, no logfile will be written.
                
        """
        pass
    def SetPartFamilyTreatment(self, partFamilyTreatment: PartFamilyTreatment) -> None:
        """
         This API will decide how to treat the Part Family members present in export operation depending on 
                    the partFamilyTreatment input value.
                    This API should be used only after assembly has been added for export operation as it will
                    iterate over all the Part Family Members added in export operation and set their behavior specified by
                    the partFamilyTreatment input value.
                    Note 1: If 'UGMGR_CloneImportExportAutoRemovePFM' customer default is enabled then it will always treat
                    Part Family Members as 'Lost' in export, So please do not use this API if this customer default is enabled,
                    since using this API to change the behavior of Part Family Members will not work in that case. 
                    Note 2: If 'UGMGR_CloneImportExportAutoRemovePFM' customer default is disabled then the user must use this API
                    to set the desired behavior of Part Family Members. If the desired behavior is not set using this API then 
                    Part Family Members will not participate anymore in export operation.
                
        """
        pass
    def SetPrefixString(self, prefixStr: str) -> None:
        """
         This API is used to set the prefix string that will be prepended to generate final name for parts being exportedcloned. 
        """
        pass
    def SetSuffixString(self, suffixStr: str) -> None:
        """
         This API is used to set the sufffix string that will be appended to generate final name for parts being exportedcloned. 
        """
        pass
    def TerminateOperation(self) -> None:
        """
         This API is used to terminate the running exportclone operation. Error is returned if the terminate operation encounters an error. 
        """
        pass
import NXOpen
class ListOfValues(NXOpen.TransientObject): 
    """ Represents list of values to be used in search query """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
class LogicalElementRevision(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    pass
import NXOpen
class LogicalObject(NXOpen.NXObject): 
    """
        Represents the class that contains database business logic or pre-creation information for the objects.
    """
    pass
import NXOpen
import NXOpen.Assemblies
class ModelElementRevision(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    class PositioningStatus(Enum):
        """
        Members Include: 
         |AbsolutelyPositioned| 
         |OutOfDate| 
         |UpToDate| 
         |Unknown| 

        """
        AbsolutelyPositioned: int
        OutOfDate: int
        UpToDate: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> ModelElementRevision.PositioningStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EffectivityFormula(self) -> str:
        """
        Getter for property: (str) EffectivityFormula
         Returns the formula string that represents the effectivity of this object in database.  
          
                  
         
        """
        pass
    @property
    def OwningCollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: ( NXOpen.CollaborativeDesign) OwningCollaborativeDesign
         Returns the owning  NXOpen::CollaborativeDesign .  
          
                  
         
        """
        pass
    def GetMemberPartitions(self) -> List[NXOpen.Assemblies.Partition]:
        """
         Get all the partitions of this model element revision.
                
         Returns partitions ( NXOpen.Assemblies.Partition Li): .
        """
        pass
    def GetOverridePart(self) -> NXOpen.Part:
        """
         Get the override part of this model element revision if it has any.
                
         Returns overridePart ( NXOpen.Part): .
        """
        pass
    def GetPositionStatus(self) -> ModelElementRevision.PositioningStatus:
        """
         Gets positioning status of design element. 
                    It returns absolute position if design element is absolutely positioned, 
                    up-to-date if design element is in work collection of positioning task, 
                    out-of-date if design element is in context collection of positioning task and 
                    unknown if design element is not in any of the above.
                    Return status will be one of NXOpen.PDM.ModelElementRevision.PositioningStatus.
                
         Returns positioningStatus ( ModelElementRevision.PositioningStatus NXOp): .
        """
        pass
    def GetPositioningGroups(self) -> List[NXOpen.Assemblies.PositioningGroup]:
        """
         Gets all positioning group which are associated with this design element.
                
         Returns positioningGroups ( NXOpen.Assemblies.PositioningGroup Li): .
        """
        pass
    def IsAbsolutelyPositioned(self) -> bool:
        """
         Determine whether this design element is absolutely positioned or not.
                
         Returns absolutelyPositioned (bool): .
        """
        pass
    def IsExcludedFromSpatialSearch(self) -> bool:
        """
         Determines whether this model element revision is excluded from spatial search.
                
         Returns isExcludedFromSpatialSearch (bool): .
        """
        pass
    def IsMemberOfPositioningGroup(self) -> bool:
        """
         Determine whether this design element is part of positioning group or not.
                
         Returns isMemberOfPositioningGroup (bool): .
        """
        pass
    def SetExcludeFromSpatialSearch(self, excludeFromSpatialSearch: bool) -> None:
        """
         Set or unset this model element revision from exclusion from spatial search.
                
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ModelElement(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    @property
    def OwningCollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: ( NXOpen.CollaborativeDesign) OwningCollaborativeDesign
         Returns the owning  NXOpen::CollaborativeDesign .  
          
                  
         
        """
        pass
    def GetMemberPartitions(self) -> List[NXOpen.Assemblies.Partition]:
        """
         Get all the partitions of this model element revision.
                
         Returns partitions ( NXOpen.Assemblies.Partition Li): .
        """
        pass
class NamingTechniqueOption(Enum):
    """
    Members Include: 
     |AutoTranslate| 
     |NamingRule| 
     |AutoTranslateWithAlternateID| 
     |UserName| 
     |AutoGenerate| 
     |Default| 

    """
    AutoTranslate: int
    NamingRule: int
    AutoTranslateWithAlternateID: int
    UserName: int
    AutoGenerate: int
    Default: int
    @staticmethod
    def ValueOf(value: int) -> NamingTechniqueOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class NativePartLogicalObject(LogicalObject): 
    """
        Represents the class that contains information for the objects participating in import operation.
    """
    def GetExistingPartAction(self) -> PartOperationImportBuilder.ExistingPartAction:
        """
         Gets the existing part action defined for this part 
         Returns existingPartAction ( PartOperationImportBuilder.ExistingPartAction NXOp): .
        """
        pass
    def GetFinalName(self) -> str:
        """
         Gets the final name of this logical object. 
         Returns finalName (str):  the database name assigned to the part being imported .
        """
        pass
    def GetInitialName(self) -> str:
        """
         Gets the initial name of this logical object. 
         Returns initialName (str):  the filename of added for import .
        """
        pass
    def GetValidationMode(self) -> PartOperationImportBuilder.Validation:
        """
         Gets the validation mode setting defined for this part 
         Returns validationMode ( PartOperationImportBuilder.Validation NXOp): .
        """
        pass
    def GetValidationRuleSetFileBrowseOption(self) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
        """
         Gets the validation rule set file browse option defined for this part 
         Returns browseOption ( PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOp): .
        """
        pass
    def IsCandidateForImport(self) -> bool:
        """
         Checks if the part represented by this logical object is a candidate for import.
                    The part is not a candidate for import if it is lost or name-only. 
         Returns isCandidateForImport (bool):  .
        """
        pass
    def IsPartNameAutoAssigned(self) -> bool:
        """
         Gets the flag indicating whether part name is autoassigned or not. 
         Returns isPartNameAutoAssigned (bool): .
        """
        pass
    def SetExistingPartAction(self, existingPartAction: PartOperationImportBuilder.ExistingPartAction) -> None:
        """
         Sets the existing part action defined for this part 
        """
        pass
    def SetValidationMode(self, validationMode: PartOperationImportBuilder.Validation) -> None:
        """
         Sets the validation mode setting defined for this part 
        """
        pass
    def SetValidationRuleSetFileBrowseOption(self, browseOption: PartOperationImportBuilder.ValidationRuleSetFileBrowseOption) -> None:
        """
         Sets the validation rule set file browse option defined for this part 
        """
        pass
import NXOpen
class NonMasterData(NXOpen.TransientObject): 
    """ Represents a class that performs various operations on NonMaster Datasets """
    class CopyNonMasterPartsOption(Enum):
        """
        Members Include: 
         |All|  save all during save as 
         |NotSet|  save none during save as 

        """
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> NonMasterData.CopyNonMasterPartsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateNonMasterListForLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
         Create NonMaster list for the selected logical Object 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def EditNonMasterToCopyName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called. 
         Returns isNameValid (bool):  flag to indicate whether the newName is valid .
        """
        pass
    def GetCopyNonMasterPartsOption(self, logicalObject: LogicalObject) -> NonMasterData.CopyNonMasterPartsOption:
        """
        Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                NonMasterData.CopyNonMasterPartsOption.All and 
                NonMasterData.CopyNonMasterPartsOption.None
         Returns saveOption ( NonMasterData.CopyNonMasterPartsOption NXOp): .
        """
        pass
    def GetNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> List[str]:
        """
         Gets NonMaster list for the given logical Object 
         Returns partFileNames (List[str]):  Non-master part file names .
        """
        pass
    def IsNonMasterForLogicalObjectBeingCopied(self, logicalObject: LogicalObject, part_name: str) -> bool:
        """
         Returns whether or not the non-master part specified for the given NXOpen.PDM.LogicalObjectwill actually
                get saved during the save as operation. 
         Returns do_save_as (bool):  True means that this non-master will be saved.
                        False means that this non-master will not be saved. .
        """
        pass
    def SetNonMasterSaveAsOption(self, logicalObject: LogicalObject, saveOption: NonMasterData.CopyNonMasterPartsOption) -> None:
        """
        Set the nonmasters saveAs option for given logical object. Save As option can be one of these
                NonMasterData.CopyNonMasterPartsOption.All and 
                NonMasterData.CopyNonMasterPartsOption.None
        """
        pass
    def SetSelectedNonMasterToCopy(self, logicalObject: LogicalObject, partName: str) -> None:
        """
         Sets whether or not the non-master part specified will actually
                get saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.  
        """
        pass
import NXOpen
class ObjectCreateBuilder(NXOpen.Builder): 
    """ Represents a builder class that perofrms create operation"""
    @property
    def DefaultDestinationFolder(self) -> str:
        """
        Getter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the object being created.  
          
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    @DefaultDestinationFolder.setter
    def DefaultDestinationFolder(self, defaultDestinationFolder: str):
        """
        Setter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the object being created.  
          
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    def CreateLogicalObjects(self) -> List[LogicalObject]:
        """
         Creates Pre-Creation LogicalObjects 
         Returns logicalObjects ( LogicalObject List[NX): .
        """
        pass
    def GetAttributeHolderObjects(self) -> List[GenericObjectAttributeHolder]:
        """
         Returns an array of AttributeHolderObjects created as part of commit. 
         Returns attributeHolderObjects ( GenericObjectAttributeHolder List[NX): .
        """
        pass
    def SetTypes(self, tcTypes: List[str], baseTCTypes: List[str]) -> None:
        """
         Set Types for which AttributeHolderObject needs to be created.
                   This method will remove all previously set types.
        """
        pass
import NXOpen
class OperationErrors(NXOpen.TransientObject): 
    """ Represents Operation Errors to be returned in TCIN related operations """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
import NXOpen
class OrderedElementGroup(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for ordered elements group in a NXOpen.PDM.ElementGroup.
    """
    pass
import NXOpen
class PartAttributeAssignmentObserverCallbackData(NXOpen.TaggedObject): 
    """ JA interface for PartAttributeAssignmentObserverCallbackData object """
    def GetLogicalObjects(self) -> List[LogicalObject]:
        """
         Gets the NXOpen.PDM.LogicalObject for NX Objects participating in attribute assignment operation 
         Returns logicalObjects ( LogicalObject List[NX): .
        """
        pass
import NXOpen
class PartAttributeAssignmentObserver(NXOpen.Object): 
    """ This class is responsible for invoking user registered callback on attribute assignment in NX """
    UserFunctionHandler = Callable[[PartAttributeAssignmentObserverCallbackData], None]
    def RegisterUserDefinedFunction(handler: PartAttributeAssignmentObserver.UserFunctionHandler) -> int:
        """
         This function registers the user-defined function 
         Returns id (int):  The identifier of the method being registered. This can be used to unregister (using UnRegisterUserDefinedFunction()) if needed  .
        """
        pass
    def UnRegisterUserDefinedFunction(id: int) -> None:
        """
         This function unregisters the user-defined function 
        """
        pass
import NXOpen
class PartBuilder(NXOpen.TransientObject): 
    """ This class serves as the base class for NX Manager part builders. The
        NX Manager part builders are used to create new parts in NX Manager mode.

        
        This class is deprecated in NX10 for "Create" and "Save As of master parts" operations.
        This class should only be used in case of Save As Non Master parts and
        Save As New Item Type Operations.
        For Create of all parts use NXOpen.PDM.PartOperationBuilder and NXOpen.FileNew
        For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.
        
    """
    class Operation(Enum):
        """
        Members Include: 
         |ExportPartNew|  File-Export-NXOpen.Part:New radio button
         |AssemblyDiagram|  Assembly-Report-Assembly Diagram... 
         |AssemblyCreateNewComponent|  Assembly-NXOpen.Assemblies.Component-Create New... 
         |Default|  Default UGManager part selection dialog

        """
        ExportPartNew: int
        AssemblyDiagram: int
        AssemblyCreateNewComponent: int
        Default: int
        @staticmethod
        def ValueOf(value: int) -> PartBuilder.Operation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PartFileNameData:
        """
         Contains part file name information 
         PartBuilderPartFileNameData_Struct NXOp is an alias for  PartBuilder.PartFileNameData NXOp.
        """
        @property
        def PartFileName(self) -> str:
            """
            Getter for property PartFileName
            Part file name

            """
            pass
        @PartFileName.setter
        def PartFileName(self, value: str):
            """
            Getter for property PartFileName
            Part file name
            Setter for property PartFileName
            Part file name

            """
            pass
        @property
        def PartFileNameModifiable(self) -> bool:
            """
            Getter for property PartFileNameModifiable
            False if part file name is not modifiable

            """
            pass
        @PartFileNameModifiable.setter
        def PartFileNameModifiable(self, value: bool):
            """
            Getter for property PartFileNameModifiable
            False if part file name is not modifiable
            Setter for property PartFileNameModifiable
            False if part file name is not modifiable

            """
            pass
    class PartNumberData:
        """
         Contains part number information.
         PartBuilderPartNumberData_Struct NXOp is an alias for  PartBuilder.PartNumberData NXOp.
        """
        @property
        def PartName(self) -> str:
            """
            Getter for property PartName
            The part name

            """
            pass
        @PartName.setter
        def PartName(self, value: str):
            """
            Getter for property PartName
            The part name
            Setter for property PartName
            The part name

            """
            pass
        @property
        def PartNameModifiable(self) -> bool:
            """
            Getter for property PartNameModifiable
            Modifiable flag for part name.

            """
            pass
        @PartNameModifiable.setter
        def PartNameModifiable(self, value: bool):
            """
            Getter for property PartNameModifiable
            Modifiable flag for part name.
            Setter for property PartNameModifiable
            Modifiable flag for part name.

            """
            pass
        @property
        def PartDescription(self) -> str:
            """
            Getter for property PartDescription
            The part description

            """
            pass
        @PartDescription.setter
        def PartDescription(self, value: str):
            """
            Getter for property PartDescription
            The part description
            Setter for property PartDescription
            The part description

            """
            pass
        @property
        def PartDescriptionModifiable(self) -> bool:
            """
            Getter for property PartDescriptionModifiable
            Modifiable flag for part description.

            """
            pass
        @PartDescriptionModifiable.setter
        def PartDescriptionModifiable(self, value: bool):
            """
            Getter for property PartDescriptionModifiable
            Modifiable flag for part description.
            Setter for property PartDescriptionModifiable
            Modifiable flag for part description.

            """
            pass
        @property
        def PartNumber(self) -> str:
            """
            Getter for property PartNumber
            The multifield key

            """
            pass
        @PartNumber.setter
        def PartNumber(self, value: str):
            """
            Getter for property PartNumber
            The multifield key
            Setter for property PartNumber
            The multifield key

            """
            pass
        @property
        def PartNumberModifiable(self) -> bool:
            """
            Getter for property PartNumberModifiable
            Modifiable flag for part number.

            """
            pass
        @PartNumberModifiable.setter
        def PartNumberModifiable(self, value: bool):
            """
            Getter for property PartNumberModifiable
            Modifiable flag for part number.
            Setter for property PartNumberModifiable
            Modifiable flag for part number.

            """
            pass
    class PartRevisionData:
        """
         Contains part revision information 
         PartBuilderPartRevisionData_Struct NXOp is an alias for  PartBuilder.PartRevisionData NXOp.
        """
        @property
        def PartRevision(self) -> str:
            """
            Getter for property PartRevision
            Part revision

            """
            pass
        @PartRevision.setter
        def PartRevision(self, value: str):
            """
            Getter for property PartRevision
            Part revision
            Setter for property PartRevision
            Part revision

            """
            pass
        @property
        def PartRevisionModifiable(self) -> bool:
            """
            Getter for property PartRevisionModifiable
            Revision Modifiable flag.

            """
            pass
        @PartRevisionModifiable.setter
        def PartRevisionModifiable(self, value: bool):
            """
            Getter for property PartRevisionModifiable
            Revision Modifiable flag.
            Setter for property PartRevisionModifiable
            Revision Modifiable flag.

            """
            pass
    @overload
    def AssignPartFileName(self, part_file_type: str) -> str:
        """
        This method generates a part file name given an input part file type and
                assigns this part file name to the builder.
                
                This method depends on the part type, part number, and part revision
                already being set on the builder. Therefore, a call to
                PDM.PartBuilder.CreatePartSpec or,
                more likely, calls to PDM.PartBuilder.AssignPartNumber and
                PDM.PartBuilder.AssignPartRevision must be made
                before calling this method.
                
                
                If this method is called before PDM.PartBuilder.CreatePartSpec
                (as will typically be the case) then the part_file_type and
                part_file_name parameters of
                PDM.PartBuilder.CreatePartSpec
                should be set to  so that the builder will use the values assigned
                by this method. Otherwise, CreatePartSpec will override the values assigned
                here and assign the values of the part_file_type and part_file_name
                parameters to the builder.
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations.  Use NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects
                instead.
                
                
         Returns part_file_name (str):  the assigned part file name .
        """
        pass
    @overload
    def AssignPartFileName(self, part_number: str, part_revision: str, part_file_name_type: str, old_part_file_name: str) -> PartBuilder.PartFileNameData:
        """
        This method generates a part file name and assigns this part 
                file name to the builder.
                
                If this method is called before PDM.PartBuilder.CreatePartSpec
                then the part_file_name parameter of PDM.PartBuilder.CreatePartSpec
                should be set to  so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the values of the part_file_type and part_file_name
                parameters to the builder.
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations.  Use NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects
                instead.
                
                
         Returns part_info ( PartBuilder.PartFileNameData NXOp): .
        """
        pass
    @overload
    def AssignPartNumber(self, part_type: str) -> str:
        """
         This method generates a part number given an input part type and
                assigns this part number to the builder.
                The input part type will also be assigned to the builder. If the
                input part type is  then this method will fail unless the part
                type has already been set on the builder via a previous call to this method
                or to PDM.PartBuilder.CreatePartSpec.
                
                
                If this method is called before PDM.PartBuilder.CreatePartSpec
                (as will typically be the case) then the part_type and
                part_number parameters of
                PDM.PartBuilder.CreatePartSpec
                should be set to  so that the builder will use the values assigned
                by this method. Otherwise, CreatePartSpec will override the values assigned
                here and assign the values of the part_type and part_number
                parameters to the builder.
                
                
                The output part_number:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationCreateBuilder
                for Create and NXOpen.PDM.PartOperationCopyBuilder for Save As instead.
                To assign part number, use NXOpen.PDM.LogicalObject and
                NXOpen.AttributePropertiesBuilder to create DB_PART_NO attribute.
                
                
         Returns part_number (str):  the assigned multifield key .
        """
        pass
    @overload
    def AssignPartNumber(self, old_part_number: str, part_type: str) -> PartBuilder.PartNumberData:
        """
         This method generates a part number given an input part type and
                sets this part number to the builder.
                The input part type will also be assigned to the builder. If the
                input part type is  then this method will fail unless the part
                type has already been set on the builder via a previous call to this method
                or to PDM.PartBuilder.CreatePartSpec.
                
                
                If this overloaded method is called before PDM.PartBuilder.CreatePartSpec
                then the part_number parameter of
                PDM.PartBuilder.CreatePartSpec
                should be set to  so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the value of part_number
                parameter to the builder.
                
                
                The output part_number in part_info structure:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationCreateBuilder
                for Create and NXOpen.PDM.PartOperationCopyBuilder for Save As instead.
                To assign part number, use NXOpen.PDM.LogicalObject and
                NXOpen.AttributePropertiesBuilder to create DB_PART_NO attribute.
                
                
         Returns part_info ( PartBuilder.PartNumberData NXOp):  Contains part number information.
        """
        pass
    @overload
    def AssignPartRevision(self) -> str:
        """
        This method generates a part revision and assigns this part revision
                to the builder.
                
                This method depends on the part type and part number already being
                set on the builder. Therefore, a call to
                PDM.PartBuilder.CreatePartSpec or,
                more likely, to AssignPartNumber must be made
                before calling this method.
                
                
                If this method is called before PDM.PartBuilder.CreatePartSpec
                (as will typically be the case) then the part_revision parameter of
                PDM.PartBuilder.CreatePartSpec
                should be set to  so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the value of the part_revision
                parameters to the builder.
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationCreateBuilder
                for Create and NXOpen.PDM.PartOperationCopyBuilder for Save As instead.
                To assign part number, use NXOpen.PDM.LogicalObject and
                NXOpen.AttributePropertiesBuilder to create DB_PART_REV attribute.
                
                
         Returns part_revision (str):  the assigned part revision .
        """
        pass
    @overload
    def AssignPartRevision(self, overload: int) -> PartBuilder.PartRevisionData:
        """
         This method generates a part revision and sets this part revision to the builder.
                
                This method depends on the part type and part number already being
                set on the builder. Therefore, a call to
                PDM.PartBuilder.CreatePartSpec or,
                more likely, to AssignPartNumber must be made
                before calling this method.
                
                If this method is called before PDM.PartBuilder.CreatePartSpec
                then the part_revision parameter of
                PDM.PartBuilder.CreatePartSpec
                should be set to  so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the value of the part_revision
                parameters to the builder.
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationCreateBuilder
                for Create and NXOpen.PDM.PartOperationCopyBuilder for Save As instead.
                To assign part number, use NXOpen.PDM.LogicalObject and
                NXOpen.AttributePropertiesBuilder to create DB_PART_REV attribute.
                
                
         Returns part_info ( PartBuilder.PartRevisionData NXOp):  Contains part revision information .
        """
        pass
    def CreatePartCreationObject(self) -> PartCreationObject:
        """
         Create an instance of a NXOpen.PDM.PartCreationObject
                class that acts as a proxy for a part in NX Manager mode prior to that part
                being created. 
         Returns creation_object ( PartCreationObject NXOp):  the new NXOpen.PDM.PartCreationObject instance .
        """
        pass
    def CreatePartSpec(self, part_type: str, part_number: str, part_revision: str, part_file_type: str, part_file_name: str) -> None:
        """
         Create the specification for the new part that will be created.
                For the input part_number:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
                NOTE: The part_file_name argument is the Dataset Name and is applicable only while creating
                specs for non-master parts.
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects
                instead.
                
                
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def NewAlternateIdManager(self) -> AlternateIdManager:
        """
         Create an instance of a NXOpen.PDM.AlternateIdManager
                class that will be used to create alternate ID information while creating the new part. 
         Returns alternate_id_manager ( AlternateIdManager NXOp):  the new NXOpen.PDM.AlternateIdManager instance .
        """
        pass
    def NewDatabaseAttributeManager(self) -> DatabaseAttributeManager:
        """
         Create an instance of a NXOpen.PDM.DatabaseAttributeManager
                class that will be used to modify database attributes while creating the new part. 
         Returns attribute_manager ( DatabaseAttributeManager NXOp):  the new NXOpen.PDM.DatabaseAttributeManager instance .
        """
        pass
    def SetAssignPartNumber(self, part_number: str) -> None:
        """
                Sets the part number explicitly into builder.  
                This method is called before PDM.PartBuilder.CreatePartSpec
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationCreateBuilder
                for Create and NXOpen.PDM.PartOperationCopyBuilder for Save As instead.
                To assign part number, use NXOpen.PDM.LogicalObject and
                NXOpen.AttributePropertiesBuilder to set the DB_PART_NO attribute.
                
                
        """
        pass
    def SetAssignPartType(self, part_type: str) -> None:
        """
                Sets the part type explicitly into builder.  
                This method is called before PDM.PartBuilder.CreatePartSpec
                
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects
                instead.
                
                
        """
        pass
    def SetContextOperation(self, operation: PartBuilder.Operation) -> None:
        """
                Sets explicitly the place from where part selection dialog invoked into builder.
                
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use NXOpen.PDM.PartOperationBuilder.CreateSpecificationsForLogicalObjects
                instead.
                
                 
        """
        pass
import NXOpen
class PartCreationObjectAttributePropertiesBuilder(NXOpen.AttributePropertiesBaseBuilder): 
    """
    Represents an NXOpen.PDM.PartCreationObjectAttributePropertiesBuilder.
    """
    pass
import NXOpen
class PartCreationObject(NXOpen.NXObject): 
    """ This class is a proxy for a to-be-created part prior to the part being created.
        Used only in NX Manager mode. """
    def CreateAttributePropertiesBuilder(self) -> PartCreationObjectAttributePropertiesBuilder:
        """
         Create the PartCreationObjectAttributePropertiesBuilder 
         Returns builder ( PartCreationObjectAttributePropertiesBuilder NXOp): .
        """
        pass
class PartFamilyTreatment(Enum):
    """
    Members Include: 
     |TreatAsLostPart| 
     |TurnIntoNormalPart| 

    """
    TreatAsLostPart: int
    TurnIntoNormalPart: int
    @staticmethod
    def ValueOf(value: int) -> PartFamilyTreatment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PartFromPartBuilder(PartBuilder): 
    """ This class provides the methods necessary to create a new part in NX Manager
    from an existing part.

    
    This class is deprecated in NX10 for "Save As of master parts" operation.
    This class should only be used in case of Save As Non Master parts and
    Save As New Item Type Operations.
    For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.
    This class will not support Save As if there are duplicate item ids in database.
    

    
    The operation that this builder supports is equivalent to the file save as operation which can:
    
       Copy a non-master dataset into a previously existing item revision,
       Save a master dataset (and possibly non-master datasets) into a new revision of the same item,
       Save any master or non-master dataset as a completely new item.
    
    

    The part that is saved is always the work part. If the save is successful, then the newly
    saved part will be the display part.

    This class is a singleton meaning only one instance of it can be exist at a time.
    """
    class FileSaveAs(Enum):
        """
        Members Include: 
         |Some|  save selected during save as 
         |All|  save all during save as 
         |NotSet|  save none during save as 

        """
        Some: int
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PartFromPartBuilder.FileSaveAs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DependentFileSaveAsOption(self) -> PartFromPartBuilder.FileSaveAs:
        """
        Getter for property: ( PartFromPartBuilder.FileSaveAs NXOp) DependentFileSaveAsOption
         Returns the dependent files to save during the save as operation
          
          
                  
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use  NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption .
                  
                   
         
        """
        pass
    @DependentFileSaveAsOption.setter
    def DependentFileSaveAsOption(self, save_option: PartFromPartBuilder.FileSaveAs):
        """
        Setter for property: ( PartFromPartBuilder.FileSaveAs NXOp) DependentFileSaveAsOption
         Returns the dependent files to save during the save as operation
          
          
                  
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use  NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption .
                  
                   
         
        """
        pass
    @property
    def NonmasterSaveAsOption(self) -> PartFromPartBuilder.FileSaveAs:
        """
        Getter for property: ( PartFromPartBuilder.FileSaveAs NXOp) NonmasterSaveAsOption
         Returns the non-master parts to save during the save as operation
          
          
                  
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use  NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption .
                  
                  
         
        """
        pass
    @NonmasterSaveAsOption.setter
    def NonmasterSaveAsOption(self, save_option: PartFromPartBuilder.FileSaveAs):
        """
        Setter for property: ( PartFromPartBuilder.FileSaveAs NXOp) NonmasterSaveAsOption
         Returns the non-master parts to save during the save as operation
          
          
                  
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use  NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption .
                  
                  
         
        """
        pass
    def Commit(self) -> None:
        """
         Creates the new part that has been fully-specified by calling methods on this
                builder.
                
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As Non Master parts and Save As New Item Type Operations. 
                For Save As of master parts, use Builder.Commit
                instead.
                 
        """
        pass
    def CreateNonmasterList(self) -> None:
        """
         Initializes the list of non-master parts that can be saved during the
                save as operation.
                
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.CreateNonMasterListForCopyLogicalObject.
                
                
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def EditNonmasterNameToSaveAs(self, old_name: str, new_name: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called.
                
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.EditNonMasterToCopyName.
                
                
         Returns is_name_valid (bool):  Whether  or not the name is a valid data set
                        name. The name will get set on the builder no matter if it is valid or not. .
        """
        pass
    def GetNonmasterList(self) -> List[str]:
        """
         Gets the list of non-master parts.
                
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.GetNonMasterListForCopyLogicalObject.
                
                
         Returns part_filenames (List[str]):  Non-master part file names .
        """
        pass
    def GetNonmasterToSaveAs(self, part_name: str) -> bool:
        """
         Returns whether or not the non-master part specified will actually
                get saved during the save as operation.
                
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.IsNonMasterForLogicalObjectBeingCopied.
                
                
         Returns do_save_as (bool):  True means that this non-master will be saved.
                        False means that this non-master will not be saved. .
        """
        pass
    def SetNonmasterToSaveAs(self, part_name: str, do_save_as: bool) -> None:
        """
         Sets whether or not the non-master part specified will actually
                get saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.
                
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder.SetSelectedNonMasterToCopy.
                
                
        """
        pass
import NXOpen
class PartFromTemplateBuilder(PartBuilder): 
    """ This class provides the methods necessary to create a new part in NX Manager
    from a template part.

    
    Deprecated in NX10.0.0.  Use PDM.PartOperationCreateBuilder  instead.
    

    
    The operation that this builder supports is equivalent to the file new operation which
    creates a new part from a template (or seed) part.
    

    If the operation is successful, then the newly created part will be the display part.
    
    This class is a singleton meaning only one instance of it can be exist at a time.
    """
    @overload
    def Commit(self) -> NXOpen.BasePart:
        """
         Creates the new part that has been fully-specified by calling methods on this
                builder. The new part will be set to display part after it is created. 
         Returns new_part ( NXOpen.BasePart):  newly created part .
        """
        pass
    @overload
    def Commit(self, set_as_display_part: bool) -> NXOpen.BasePart:
        """
         Creates the new part that has been fully-specified by calling methods on this
                builder. The caller specifies whether
                the new part should be set as the display after it is created. 
         Returns new_part ( NXOpen.BasePart):  newly created part .
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def SetSeedPart(self, seed_name: str) -> None:
        """
         Sets the seed part on which the new part will be based. 
        """
        pass
import NXOpen.Assemblies
class PartitionSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create partition search filter term.
     Such filter terms can be used to provide filtering.
    """
    def AddPartitions(self, partition: List[NXOpen.Assemblies.Partition]) -> None:
        """
         This function adds the partitions to partition term. 
        """
        pass
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse partition term or not. 
         Returns excludeToggle (bool): .
        """
        pass
    def IncludeChildPartition(self, includeChildPartitionToggle: bool) -> None:
        """
         This function sets the flag whether to include child partitions or not. 
        """
        pass
    def IsChildPartitionIncluded(self) -> bool:
        """
         This function gets the flag whether to include child partitions or not. 
         Returns includeChildPartitionToggle (bool): .
        """
        pass
    def RemovePartitions(self, partition: List[NXOpen.Assemblies.Partition]) -> None:
        """
         This function removes the partitions from partition term. 
        """
        pass
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse partition term or not. 
        """
        pass
import NXOpen
class PartManager(NXOpen.Object): 
    """ This class contains methods to create and manage parts in NX Manager mode.
    """
    def GetCaeCloneManager(part: NXOpen.BasePart) -> CaeCloneManager:
        """
         Create or get a Clone Manager that can execute a CAE Clone process for a Simulation File or a FeModel File.  
                Creates a Clone Manager for a Simulation tag or a FeModel tag, if it does not already exist.
                Creates part from part builder NXOpen.PDM.PartFromPartBuilder objects for cloning a Simulation File or a FeModel File.
                If called for a FeModel tag, the function will create Part Builders for FeModel Part , associated Idealized Part and CAD master part.
                If called for a Simulation tag, the function will create Part Builders for Simulation Part, associated FeModel Part, Idealized Part and CAD master part.
                
         Returns manager ( CaeCloneManager NXOp):  the clone manager .
        """
        pass
    def NewPartFromPartBuilder() -> PartFromPartBuilder:
        """
         Create an instance of a part builder that creates a new part from an existing part.
                    This is analagous to a File SaveAs operation in NX Manager mode.
                
                    This method will throw an error if the session is not running in
                    NX Manager mode.
                    NXOpen.PDM.PartFromTemplateBuilder is a singleton
                    meaning only one instance of it can exist at one time. Calling this method
                    will destroy the builder if one already exists and return a new instance.
                    
                    Deprecated in NX10 for "Save As of master parts" operation. 
                    This should only be used in case of Save As Non Master parts and Save As New Item Type Operations.
                    For Save As of master parts, use NXOpen.PDM.PartOperationCopyBuilder instead.
                    
                
         Returns part_builder ( PartFromPartBuilder NXOp):  the part builder .
        """
        pass
    def NewPartFromTemplateBuilder() -> PartFromTemplateBuilder:
        """
         Create an instance of a part builder that creates a new part from a template part.
                    This is analagous to a File New operation in NX Manager mode.
                
                    This method will throw an error if the session is not running in
                    NX Manager mode. 
                    NXOpen.PDM.PartFromTemplateBuilder is a singleton
                    meaning only one instance of it can exist at one time. Calling this method
                    will destroy the builder if one already exists and return a new instance.
                
         Returns part_builder ( PartFromTemplateBuilder NXOp):  the part builder .
        """
        pass
    def NewPendingComponentsManager(part: NXOpen.BasePart) -> PendingComponentsManager:
        """
         Creates a pending component manager for a given part. Pending components
                    are ones that have been added from Teamcenter, but are not yet present in NX.
                
         Returns pending_mgr ( PendingComponentsManager NXOp): .
        """
        pass
import NXOpen
class PartNameGenerator(NXOpen.Object): 
    """ Represents the PartNameGenerator """
    class PartAssignInputInfo:
        """
         PartAssignInputInfo struct for input to AutoAssignPartParametersForCreate 
         PartNameGeneratorPartAssignInputInfo_Struct NXOp is an alias for  PartNameGenerator.PartAssignInputInfo NXOp.
        """
        @property
        def ItemType(self) -> str:
            """
            Getter for property ItemType
            """
            pass
        @ItemType.setter
        def ItemType(self, value: str):
            """
            Getter for property ItemTypeSetter for property ItemType
            """
            pass
        @property
        def ModelType(self) -> str:
            """
            Getter for property ModelType
            """
            pass
        @ModelType.setter
        def ModelType(self, value: str):
            """
            Getter for property ModelTypeSetter for property ModelType
            """
            pass
        @property
        def BasePartNumber(self) -> str:
            """
            Getter for property BasePartNumber
            """
            pass
        @BasePartNumber.setter
        def BasePartNumber(self, value: str):
            """
            Getter for property BasePartNumberSetter for property BasePartNumber
            """
            pass
        @property
        def BasePartRevision(self) -> str:
            """
            Getter for property BasePartRevision
            """
            pass
        @BasePartRevision.setter
        def BasePartRevision(self, value: str):
            """
            Getter for property BasePartRevisionSetter for property BasePartRevision
            """
            pass
        @property
        def BasePartName(self) -> str:
            """
            Getter for property BasePartName
            """
            pass
        @BasePartName.setter
        def BasePartName(self, value: str):
            """
            Getter for property BasePartNameSetter for property BasePartName
            """
            pass
        @property
        def GenerateNextItemId(self) -> bool:
            """
            Getter for property GenerateNextItemId
            """
            pass
        @GenerateNextItemId.setter
        def GenerateNextItemId(self, value: bool):
            """
            Getter for property GenerateNextItemIdSetter for property GenerateNextItemId
            """
            pass
    def AutoAssignPartParametersForCreate(inputInfoPtr: PartNameGenerator.PartAssignInputInfo) -> str:
        """
                    This Method will auto assign the required parameters for creating new part in managed mode.
                    It will error out if part type is not fully auto assignable. i.e. If part type has key identifiers  create descriptors
                    which are required but cannot be auto-assigned.
                
         Returns cliSpec (str): .
        """
        pass
import NXOpen
class PartOperationAttributePropertiesBuilder(NXOpen.AttributePropertiesBuilder): 
    """
        Represents an NXOpen.PDM.PartOperationAttributePropertiesBuilder to be used for 
        creating attributes in part operation.
        The attribute will be distributed to all objects supplied in the selected object list.
    """
    @property
    def ReferenceObject(self) -> LogicalObject:
        """
        Getter for property: ( LogicalObject NXOp) ReferenceObject
         Returns the referenced logical object from this attribute.  
           Only used for attribute
                    of Reference Part.    
         
        """
        pass
    @ReferenceObject.setter
    def ReferenceObject(self, referencedLogicalObject: LogicalObject):
        """
        Setter for property: ( LogicalObject NXOp) ReferenceObject
         Returns the referenced logical object from this attribute.  
           Only used for attribute
                    of Reference Part.    
         
        """
        pass
    def CreateOrModifyAttribute(self) -> bool:
        """
         Create the attribute from the data set in the builder.  Unlike calling commit,
                    this method will not perform an update. 
         Returns changed (bool):  True if the attribute was creatededited successfully .
        """
        pass
import NXOpen
class PartOperationBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs various design element operations. 
        The operation can be one of NXOpen.PDM.PartOperationBuilder.OperationType """
    class DependentFileSaveAs(Enum):
        """
        Members Include: 
         |All|  save all during save as 
         |NotSet|  save none during save as 

        """
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationBuilder.DependentFileSaveAs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NonMasterSaveAs(Enum):
        """
        Members Include: 
         |All|  save all during save as 
         |NotSet|  save none during save as 

        """
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationBuilder.NonMasterSaveAs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OperationType(Enum):
        """
        Members Include: 
         |SaveAs|  Save As Part 
         |Revise|  Revise Part 
         |Create|  Create Part 
         |Import|  Import Part 
         |Clone|  Clone Part  

        """
        SaveAs: int
        Revise: int
        Create: int
        Import: int
        Clone: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationBuilder.OperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DefaultDestinationFolder(self) -> str:
        """
        Getter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the part being created .  
           It will be ignored in case of 
                revise and creation of non-masters.
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    @DefaultDestinationFolder.setter
    def DefaultDestinationFolder(self, defaultDestinationFolder: str):
        """
        Setter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the part being created .  
           It will be ignored in case of 
                revise and creation of non-masters.
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    @property
    def DependentFileSaveAsOption(self) -> PartOperationBuilder.DependentFileSaveAs:
        """
        Getter for property: ( PartOperationBuilder.DependentFileSaveAs NXOp) DependentFileSaveAsOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                 PartOperationBuilder::DependentFileSaveAsAll  and 
                 PartOperationBuilder::DependentFileSaveAsNone   
         
        """
        pass
    @DependentFileSaveAsOption.setter
    def DependentFileSaveAsOption(self, saveOption: PartOperationBuilder.DependentFileSaveAs):
        """
        Setter for property: ( PartOperationBuilder.DependentFileSaveAs NXOp) DependentFileSaveAsOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                 PartOperationBuilder::DependentFileSaveAsAll  and 
                 PartOperationBuilder::DependentFileSaveAsNone   
         
        """
        pass
    @property
    def ReplaceAllComponents(self) -> bool:
        """
        Getter for property: (bool) ReplaceAllComponents
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                     PartOperationBuilder::OperationTypeSaveAs  and 
                     PartOperationBuilder::OperationTypeRevise   
         
        """
        pass
    @ReplaceAllComponents.setter
    def ReplaceAllComponents(self, replaceAllComponents: bool):
        """
        Setter for property: (bool) ReplaceAllComponents
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                     PartOperationBuilder::OperationTypeSaveAs  and 
                     PartOperationBuilder::OperationTypeRevise   
         
        """
        pass
    def AddRelatedPartToOperate(self, basePart: NXOpen.BasePart, relatedParts: List[NXOpen.BasePart], relatedPartsReasons: List[str], operation: PartOperationBuilder.OperationType) -> None:
        """
         Add related part to the part undergoing an operation. Example: if user selects a part
                    for Save As which has Linked Part Modules that should also undergo Save As, they should
                    be added as related parts.
                    Applicable only for operation types 
                    PartOperationBuilder.OperationType.SaveAs and 
                    PartOperationBuilder.OperationType.Revise
        """
        pass
    def ClearWarnings(self) -> None:
        """
         Executes method ClearWarningCodeToLogicalObjectsSetMap() which clears m_warningCodeToLogicalObjectsSetMap 
                
        """
        pass
    def CreateLogicalObjects(self) -> List[LogicalObject]:
        """
         Creates the pre-creation objects for the parts 
         Returns logicalObjects ( LogicalObject List[NX): .
        """
        pass
    def CreateNonMasterListForLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
         Create NonMaster list for the selected logical Object 
        """
        pass
    def CreateSpecificationsForLogicalObjects(self, logicalObjects: List[LogicalObject]) -> None:
        """
         Create new specifications for Logical Objects 
        """
        pass
    def EditNonMasterName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called. 
         Returns isNameValid (bool):  flag to indicate whether the newName is valid .
        """
        pass
    def GetAlternateIDManager(self, logicalObject: LogicalObject) -> AlternateIdManager:
        """
         Create an instance of a NXOpen.PDM.AlternateIdManager
                class that will be used to create alternate ID information while creating the new part.
                CreateSpec call should happen before calling this method.
         Returns alternateIDManager ( AlternateIdManager NXOp):  the new NXOpen.PDM.AlternateIdManager instance .
        """
        pass
    def GetCreatedParts(self) -> List[NXOpen.BasePart]:
        """
         Returns Commited Objects 
         Returns commitedParts ( NXOpen.BasePart Li): .
        """
        pass
    def GetDialogOperation(self) -> PartOperationBuilder.OperationType:
        """
         Returns the dialog operation Applicable only for operation types 
                    PartOperationBuilder.OperationType.SaveAs and 
                    PartOperationBuilder.OperationType.Revise
         Returns dialogOperation ( PartOperationBuilder.OperationType NXOp): .
        """
        pass
    def GetErrorMessageHandler(self, refresh: bool) -> ErrorMessageHandler:
        """
         Returns ErrorMessageHandler 
         Returns errorMessageHandler ( ErrorMessageHandler NXOp): .
        """
        pass
    def GetNonMasterCopyOption(self, logicalObject: LogicalObject) -> PartOperationBuilder.NonMasterSaveAs:
        """
        Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                PartOperationBuilder.NonMasterSaveAs.All and 
                PartOperationBuilder.NonMasterSaveAs.None
         Returns saveOption ( PartOperationBuilder.NonMasterSaveAs NXOp): .
        """
        pass
    def GetNonMasterList(self, logicalObject: LogicalObject) -> List[str]:
        """
         Gets NonMaster list for the given logical Object 
         Returns partFileNames (List[str]):  Non-master part file names .
        """
        pass
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns part operation failures 
         Returns operationFailures ( NXOpen.ErrorList): .
        """
        pass
    def IsNonMasterBeingCopied(self, logicalObject: LogicalObject, part_name: str) -> bool:
        """
         Returns whether or not the non master part specified for the given NXOpen.PDM.LogicalObjectwill actually get
                 saved during the save as operation. 
         Returns do_save_as (bool):  True means that this non-master will be saved. False means that this non master will not be saved. .
        """
        pass
    def SetDialogOperation(self, dialogOperation: PartOperationBuilder.OperationType) -> None:
        """
         Sets the dialog operation. Applicable only for operation types 
                    PartOperationBuilder.OperationType.SaveAs and 
                    PartOperationBuilder.OperationType.Revise
        """
        pass
    def SetNonMasterSaveAsOption(self, logicalObject: LogicalObject, saveOption: PartOperationBuilder.NonMasterSaveAs) -> None:
        """
        Set the nonmasters saveAs option for given logical object
        """
        pass
    def SetSelectedNonMasterToSaveAs(self, logicalObject: LogicalObject, partName: str) -> None:
        """
         Sets whether or not the non-master part specified will actually get
                saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.  
        """
        pass
    def SetSelectedParts(self, selectedParts: List[NXOpen.BasePart]) -> List[NXOpen.BasePart]:
        """
         Sets the selected parts. Applicable only for operation types
                    PartOperationBuilder.OperationType.SaveAs and 
                    PartOperationBuilder.OperationType.Revise
                    Also returns an array of parts failed to added, these are not removed from the input array though.
                    NXOpen.PDM.PartOperationBuilder.GetOperationFailures can be called to get the errors occurred
                    during this operation.
                    
         Returns failedParts ( NXOpen.BasePart Li): .
        """
        pass
    def ValidateLogicalObjectsToCommit(self) -> None:
        """
         Validates NXOpen.PDM.LogicalObject objects with this builder and udpates the operation failuers.
                NXOpen.PDM.PartOperationBuilder.GetOperationFailures can be called to get the errors occurred
                during this operation. 
        """
        pass
import NXOpen
class PartOperationCopyBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs various Save As operations. """
    class CopyDependentFiles(Enum):
        """
        Members Include: 
         |All|  save all during save as 
         |NotSet|  save none during save as 

        """
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationCopyBuilder.CopyDependentFiles:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CopyNonMasterParts(Enum):
        """
        Members Include: 
         |All|  save all during save as 
         |NotSet|  save none during save as 

        """
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationCopyBuilder.CopyNonMasterParts:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OperationSubType(Enum):
        """
        Members Include: 
         |Default|  Save As dialog 
         |MakeUnique|  MakeUnique flavour of Save As dialog 

        """
        Default: int
        MakeUnique: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationCopyBuilder.OperationSubType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DependentFilesToCopyOption(self) -> PartOperationCopyBuilder.CopyDependentFiles:
        """
        Getter for property: ( PartOperationCopyBuilder.CopyDependentFiles NXOp) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                 PartOperationCopyBuilder::CopyDependentFilesAll  and 
                 PartOperationCopyBuilder::CopyDependentFilesNone   
         
        """
        pass
    @DependentFilesToCopyOption.setter
    def DependentFilesToCopyOption(self, saveOption: PartOperationCopyBuilder.CopyDependentFiles):
        """
        Setter for property: ( PartOperationCopyBuilder.CopyDependentFiles NXOp) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                 PartOperationCopyBuilder::CopyDependentFilesAll  and 
                 PartOperationCopyBuilder::CopyDependentFilesNone   
         
        """
        pass
    @property
    def ReplaceAllComponentsInSession(self) -> bool:
        """
        Getter for property: (bool) ReplaceAllComponentsInSession
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                     PartOperationBuilder::OperationTypeSaveAs  and 
                     PartOperationBuilder::OperationTypeRevise   
         
        """
        pass
    @ReplaceAllComponentsInSession.setter
    def ReplaceAllComponentsInSession(self, replaceAllComponents: bool):
        """
        Setter for property: (bool) ReplaceAllComponentsInSession
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                     PartOperationBuilder::OperationTypeSaveAs  and 
                     PartOperationBuilder::OperationTypeRevise   
         
        """
        pass
    def AddRelatedPartsToCopy(self, basePart: NXOpen.BasePart, relatedParts: List[NXOpen.BasePart], relatedPartsReasons: List[str], operation: PartOperationBuilder.OperationType) -> None:
        """
         Add related part to the part undergoing an operation. Example: if user selects a part
                    for Save As which has Linked Part Modules that should also undergo Save As, they should
                    be added as related parts.
                    Applicable only for operation types 
                    PartOperationBuilder.OperationType.SaveAs and 
                    PartOperationBuilder.OperationType.Revise
        """
        pass
    def CreateNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
         Create NonMaster list for the selected logical Object 
        """
        pass
    def EditNonMasterToCopyName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called. 
         Returns isNameValid (bool):  flag to indicate whether the newName is valid .
        """
        pass
    def GetCopyNonMasterPartsOption(self, logicalObject: LogicalObject) -> PartOperationCopyBuilder.CopyNonMasterParts:
        """
        Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                PartOperationCopyBuilder.CopyNonMasterParts.All and 
                PartOperationCopyBuilder.CopyNonMasterParts.None
         Returns saveOption ( PartOperationCopyBuilder.CopyNonMasterParts NXOp): .
        """
        pass
    def GetNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> List[str]:
        """
         Gets NonMaster list for the given logical Object 
         Returns partFileNames (List[str]):  Non-master part file names .
        """
        pass
    def GetOperationSubType(self) -> PartOperationCopyBuilder.OperationSubType:
        """
         Returns the NXOpen.PDM.PartOperationCopyBuilder.OperationSubType for Create. 
         Returns dialogOperation ( PartOperationCopyBuilder.OperationSubType NXOp): .
        """
        pass
    def GetSourcePartFromLogicalObject(self, logicalObject: LogicalObject) -> NXOpen.Part:
        """
         Returns the source part of this logical object. 
         Returns sourcePart ( NXOpen.Part): .
        """
        pass
    def IsNonMasterForLogicalObjectBeingCopied(self, logicalObject: LogicalObject, part_name: str) -> bool:
        """
         Returns whether or not the non-master part specified for the given NXOpen.PDM.LogicalObjectwill actually
                get saved during the save as operation. 
         Returns do_save_as (bool):  True means that this non-master will be saved.
                        False means that this non-master will not be saved. .
        """
        pass
    def SetChangeNotice(self, ecnCliSpec: str) -> None:
        """
         Sets the Engineering Change Notice for the parts undergoing save-as 
        """
        pass
    def SetCopyNonMasterPartsOption(self, logicalObject: LogicalObject, saveOption: PartOperationCopyBuilder.CopyNonMasterParts) -> None:
        """
        Set the nonmasters saveAs option for given logical object. Save As option can be one of these
                PartOperationCopyBuilder.CopyNonMasterParts.All and 
                PartOperationCopyBuilder.CopyNonMasterParts.None
        """
        pass
    def SetOperationSubType(self, operationSubType: PartOperationCopyBuilder.OperationSubType) -> None:
        """
         Sets the NXOpen.PDM.PartOperationCopyBuilder.OperationSubType for Create. 
        """
        pass
    def SetSelectedNonMasterToCopy(self, logicalObject: LogicalObject, partName: str) -> None:
        """
         Sets whether or not the non-master part specified will actually
                get saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.  
        """
        pass
    def SetSelectedPartsToCopy(self, selectedParts: List[NXOpen.BasePart]) -> List[NXOpen.BasePart]:
        """
         Sets the selected parts. Applicable only for operation types
                    PartOperationBuilder.OperationType.SaveAs and 
                    PartOperationBuilder.OperationType.Revise
                    Also returns an array of parts failed to added, these are not removed from the input array though.
                    NXOpen.PDM.PartOperationBuilder.GetOperationFailures can be called to get the errors occurred
                    during this operation.
                    
         Returns failedParts ( NXOpen.BasePart Li): .
        """
        pass
import NXOpen
class PartOperationCreateBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs Create operations """
    class OperationSubType(Enum):
        """
        Members Include: 
         |FromTemplate|  Create New Part from template 
         |SelectTemplate|  Populate Part already created in Teamcenter 
         |Rename|  Rename Existing Part 
         |CreateSpecification|  Create Specification and not a Part 
         |RenameNativePartInTc|  Rename Existing native part in session 

        """
        FromTemplate: int
        SelectTemplate: int
        Rename: int
        CreateSpecification: int
        RenameNativePartInTc: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationCreateBuilder.OperationSubType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateLogicalObjectsUsingSeedPart(self, seedPartName: str, numOfPartsToCreate: int) -> List[LogicalObject]:
        """
         Creates PDM.LogicalObject using the seed part provided. The part with provided name must exist in Teamcenter.
         Returns logicalObjects ( LogicalObject List[NX): .
        """
        pass
    def GetAddMaster(self) -> bool:
        """
         Returns logical value to indicate whether master to be added as child component 
         Returns addMaster (bool):  whether master to be added as child component .
        """
        pass
    def GetOperationSubType(self) -> PartOperationCreateBuilder.OperationSubType:
        """
         Returns the NXOpen.PDM.PartOperationCreateBuilder.OperationSubType for Create. 
         Returns dialogOperation ( PartOperationCreateBuilder.OperationSubType NXOp): .
        """
        pass
    def GetResultPartSpecs(self) -> List[str]:
        """
         Get Result Part Specifications.
         Returns resultPartsSpecs (List[str]): .
        """
        pass
    def SetAddMaster(self, addMaster: bool) -> None:
        """
         Sets the Add Master Flag 
                    Use this only in case creating a new Altrep.
                    This will add master as a component to newly created master.
                    This will be set to false if tempalte selected doesn't supports creating new altrep.
                   
        """
        pass
    def SetItemType(self, itemType: str) -> None:
        """
         Sets the selected Item Type 
        """
        pass
    def SetMasterPart(self, masterPart: NXOpen.BasePart) -> None:
        """
         Sets the Master Part 
                    Use this only in case the part your are trying to create supports master model.
                   
        """
        pass
    def SetModelType(self, modelType: str) -> None:
        """
         Sets the selected Model Type 
                    This is same as the Relation Type that is set by NXOpen.FileNew.RelationType and is same as
                    the relation type specified in Template PAX files.
                    This is needed to be set only when the NXOpen.PDM.PartOperationCreateBuilder.OperationSubType is set 
                    to NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.CreateSpecification. In other cases
                    this is read from the Template. If not set this is always assumed to be "master".
                    Example strings are "specification", "manifestation", etc.
                    
        """
        pass
    def SetOperationSubType(self, operatioSubType: PartOperationCreateBuilder.OperationSubType) -> None:
        """
         Sets the NXOpen.PDM.PartOperationCreateBuilder.OperationSubType for Create. 
        """
        pass
    def SetPartSpecToOpen(self, partSpecToOpen: str) -> None:
        """
         Sets the Part Spec of the part to open in case of Select Template Dialog
                    This is only applicable if NXOpen.PDM.PartOperationCreateBuilder.OperationSubType is set to
                    NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.SelectTemplate
                    partSpecTopOpen can be a CLI format (
        DBMFKIDRevId) or full TCIN file specification (starting with %UGMGR)
                   
        """
        pass
    def SetPartsToRename(self, partsToRename: List[NXOpen.BasePart]) -> None:
        """
         Sets the Parts To Rename on the Builder.
                    This is only applicable if NXOpen.PDM.PartOperationCreateBuilder.OperationSubType is set to
                    NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.Rename
                   
        """
        pass
import NXOpen
class PartOperationImportBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs Create operations """
    class CheckoutOptionType(Enum):
        """
        Members Include: 
         |Checkin| 
         |Checkout| 
         |NoChange| 

        """
        Checkin: int
        Checkout: int
        NoChange: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.CheckoutOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConversionRule(Enum):
        """
        Members Include: 
         |AsID| 
         |AsIDandRevision| 
         |WithPrefix| 
         |WithSuffix| 
         |WithReplaceString| 
         |MixedRule| 

        """
        AsID: int
        AsIDandRevision: int
        WithPrefix: int
        WithSuffix: int
        WithReplaceString: int
        MixedRule: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.ConversionRule:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExistingPartAction(Enum):
        """
        Members Include: 
         |Overwrite| 
         |UseExisting| 
         |NewRevision| 
         |Default| 

        """
        Overwrite: int
        UseExisting: int
        NewRevision: int
        Default: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.ExistingPartAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NumberingSourceOption(Enum):
        """
        Members Include: 
         |PartIDGenerator| 
         |OSFilename| 
         |Attribute| 

        """
        PartIDGenerator: int
        OSFilename: int
        Attribute: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.NumberingSourceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PartFamilyTreatment(Enum):
        """
        Members Include: 
         |TreatAsLostPart| 
         |TurnIntoNormalPart| 

        """
        TreatAsLostPart: int
        TurnIntoNormalPart: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.PartFamilyTreatment:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Validation(Enum):
        """
        Members Include: 
         |Off| 
         |ImportFromPart| 
         |RunValidation| 
         |RunValidationHybrid| 
         |Default| 

        """
        Off: int
        ImportFromPart: int
        RunValidation: int
        RunValidationHybrid: int
        Default: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.Validation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValidationRuleSetFileBrowseOption(Enum):
        """
        Members Include: 
         |Native| 
         |Teamcenter| 

        """
        Native: int
        Teamcenter: int
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddCAENonMastersToImport(self) -> bool:
        """
        Getter for property: (bool) AddCAENonMastersToImport
         Returns the add non master to import   
            
         
        """
        pass
    @AddCAENonMastersToImport.setter
    def AddCAENonMastersToImport(self, addCAENonMasters: bool):
        """
        Setter for property: (bool) AddCAENonMastersToImport
         Returns the add non master to import   
            
         
        """
        pass
    @property
    def AddDfaMixins(self) -> bool:
        """
        Getter for property: (bool) AddDfaMixins
         Returns the add dfa mixins   
            
         
        """
        pass
    @AddDfaMixins.setter
    def AddDfaMixins(self, addDfaMixins: bool):
        """
        Setter for property: (bool) AddDfaMixins
         Returns the add dfa mixins   
            
         
        """
        pass
    @property
    def AssignAlternateIds(self) -> bool:
        """
        Getter for property: (bool) AssignAlternateIds
         Returns the method returns the value indicating whether alternate IDs should be created during import   
            
         
        """
        pass
    @AssignAlternateIds.setter
    def AssignAlternateIds(self, createAlternateIDs: bool):
        """
        Setter for property: (bool) AssignAlternateIds
         Returns the method returns the value indicating whether alternate IDs should be created during import   
            
         
        """
        pass
    @property
    def AssociatedFilesRootDirectory(self) -> str:
        """
        Getter for property: (str) AssociatedFilesRootDirectory
         Returns the associated files root directory   
            
         
        """
        pass
    @AssociatedFilesRootDirectory.setter
    def AssociatedFilesRootDirectory(self, foldername: str):
        """
        Setter for property: (str) AssociatedFilesRootDirectory
         Returns the associated files root directory   
            
         
        """
        pass
    @property
    def CheckedoutCommentNotMatchError(self) -> bool:
        """
        Getter for property: (bool) CheckedoutCommentNotMatchError
         Returns the method gets the status of the 'Notify if Checkout Comment not Match' Flag so as to pop an error that the previous checkout
                comment of file which user is trying to override does not match with the checkout comment entered through the dialog.  
          
                  
         
        """
        pass
    @CheckedoutCommentNotMatchError.setter
    def CheckedoutCommentNotMatchError(self, checkedoutCommentNotMatchError: bool):
        """
        Setter for property: (bool) CheckedoutCommentNotMatchError
         Returns the method gets the status of the 'Notify if Checkout Comment not Match' Flag so as to pop an error that the previous checkout
                comment of file which user is trying to override does not match with the checkout comment entered through the dialog.  
          
                  
         
        """
        pass
    @property
    def CheckoutComment(self) -> str:
        """
        Getter for property: (str) CheckoutComment
         Returns the method is used to get the comment added by the user while checking in or checking out   
            
         
        """
        pass
    @CheckoutComment.setter
    def CheckoutComment(self, checkoutComment: str):
        """
        Setter for property: (str) CheckoutComment
         Returns the method is used to get the comment added by the user while checking in or checking out   
            
         
        """
        pass
    @property
    def CheckoutOption(self) -> PartOperationImportBuilder.CheckoutOptionType:
        """
        Getter for property: ( PartOperationImportBuilder.CheckoutOptionType NXOp) CheckoutOption
         Returns the method is used to identify id user want to checkout or checkin the file while import   
            
         
        """
        pass
    @CheckoutOption.setter
    def CheckoutOption(self, checkoutOption: PartOperationImportBuilder.CheckoutOptionType):
        """
        Setter for property: ( PartOperationImportBuilder.CheckoutOptionType NXOp) CheckoutOption
         Returns the method is used to identify id user want to checkout or checkin the file while import   
            
         
        """
        pass
    @property
    def ConversionType(self) -> PartOperationImportBuilder.ConversionRule:
        """
        Getter for property: ( PartOperationImportBuilder.ConversionRule NXOp) ConversionType
         Returns the conversion type   
            
         
        """
        pass
    @ConversionType.setter
    def ConversionType(self, conversionType: PartOperationImportBuilder.ConversionRule):
        """
        Setter for property: ( PartOperationImportBuilder.ConversionRule NXOp) ConversionType
         Returns the conversion type   
            
         
        """
        pass
    @property
    def DefaultAction(self) -> PartOperationImportBuilder.ExistingPartAction:
        """
        Getter for property: ( PartOperationImportBuilder.ExistingPartAction NXOp) DefaultAction
         Returns the default action   
            
         
        """
        pass
    @DefaultAction.setter
    def DefaultAction(self, defaultAction: PartOperationImportBuilder.ExistingPartAction):
        """
        Setter for property: ( PartOperationImportBuilder.ExistingPartAction NXOp) DefaultAction
         Returns the default action   
            
         
        """
        pass
    @property
    def DefaultAlternateIdContext(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdContext
         Returns the method returns the IdContext to be used while assigning alternate IDs during import   
            
         
        """
        pass
    @DefaultAlternateIdContext.setter
    def DefaultAlternateIdContext(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdContext
         Returns the method returns the IdContext to be used while assigning alternate IDs during import   
            
         
        """
        pass
    @property
    def DefaultAlternateIdType(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdType
         Returns the method returns the IdType to be used while assigning alternate IDs during import  
            
         
        """
        pass
    @DefaultAlternateIdType.setter
    def DefaultAlternateIdType(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdType
         Returns the method returns the IdType to be used while assigning alternate IDs during import  
            
         
        """
        pass
    @property
    def DefaultChangeNotice(self) -> str:
        """
        Getter for property: (str) DefaultChangeNotice
         Returns the default change notice for import operation in CLI format.  
             
         
        """
        pass
    @DefaultChangeNotice.setter
    def DefaultChangeNotice(self, defaultChangeNotice: str):
        """
        Setter for property: (str) DefaultChangeNotice
         Returns the default change notice for import operation in CLI format.  
             
         
        """
        pass
    @property
    def DefaultDescription(self) -> str:
        """
        Getter for property: (str) DefaultDescription
         Returns the default description   
            
         
        """
        pass
    @DefaultDescription.setter
    def DefaultDescription(self, defaultDescription: str):
        """
        Setter for property: (str) DefaultDescription
         Returns the default description   
            
         
        """
        pass
    @property
    def DefaultItemType(self) -> str:
        """
        Getter for property: (str) DefaultItemType
         Returns the default item type   
            
         
        """
        pass
    @DefaultItemType.setter
    def DefaultItemType(self, defaultItemType: str):
        """
        Setter for property: (str) DefaultItemType
         Returns the default item type   
            
         
        """
        pass
    @property
    def DefaultName(self) -> str:
        """
        Getter for property: (str) DefaultName
         Returns the default name   
            
         
        """
        pass
    @DefaultName.setter
    def DefaultName(self, defaultName: str):
        """
        Setter for property: (str) DefaultName
         Returns the default name   
            
         
        """
        pass
    @property
    def DefaultOwningGroup(self) -> str:
        """
        Getter for property: (str) DefaultOwningGroup
         Returns the default owning group   
            
         
        """
        pass
    @DefaultOwningGroup.setter
    def DefaultOwningGroup(self, defaultOwningGroup: str):
        """
        Setter for property: (str) DefaultOwningGroup
         Returns the default owning group   
            
         
        """
        pass
    @property
    def DefaultOwningUser(self) -> str:
        """
        Getter for property: (str) DefaultOwningUser
         Returns the default owning user   
            
         
        """
        pass
    @DefaultOwningUser.setter
    def DefaultOwningUser(self, defaultOwningUser: str):
        """
        Setter for property: (str) DefaultOwningUser
         Returns the default owning user   
            
         
        """
        pass
    @property
    def IncludeComponentParts(self) -> bool:
        """
        Getter for property: (bool) IncludeComponentParts
         Returns the include component parts   
            
         
        """
        pass
    @IncludeComponentParts.setter
    def IncludeComponentParts(self, includeComponentParts: bool):
        """
        Setter for property: (bool) IncludeComponentParts
         Returns the include component parts   
            
         
        """
        pass
    @property
    def IncludeDependentParts(self) -> bool:
        """
        Getter for property: (bool) IncludeDependentParts
         Returns the include dependent parts   
            
         
        """
        pass
    @IncludeDependentParts.setter
    def IncludeDependentParts(self, includeDependentParts: bool):
        """
        Setter for property: (bool) IncludeDependentParts
         Returns the include dependent parts   
            
         
        """
        pass
    @property
    def IncludeSubfoldersToggle(self) -> bool:
        """
        Getter for property: (bool) IncludeSubfoldersToggle
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    @IncludeSubfoldersToggle.setter
    def IncludeSubfoldersToggle(self, includeSubfolders: bool):
        """
        Setter for property: (bool) IncludeSubfoldersToggle
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    @property
    def MaintainOriginalFolderStructure(self) -> bool:
        """
        Getter for property: (bool) MaintainOriginalFolderStructure
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    @MaintainOriginalFolderStructure.setter
    def MaintainOriginalFolderStructure(self, maintainOriginalFolderStructure: bool):
        """
        Setter for property: (bool) MaintainOriginalFolderStructure
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    @property
    def NotCheckedoutError(self) -> bool:
        """
        Getter for property: (bool) NotCheckedoutError
         Returns the method gets the status of the 'Notify if Not Checkout' Flag so as to pop an error that the file which
                user is trying to override is not check-out.  
          
                  
         
        """
        pass
    @NotCheckedoutError.setter
    def NotCheckedoutError(self, notCheckedoutError: bool):
        """
        Setter for property: (bool) NotCheckedoutError
         Returns the method gets the status of the 'Notify if Not Checkout' Flag so as to pop an error that the file which
                user is trying to override is not check-out.  
          
                  
         
        """
        pass
    @property
    def NumberAttr(self) -> str:
        """
        Getter for property: (str) NumberAttr
         Returns the number attr   
            
         
        """
        pass
    @NumberAttr.setter
    def NumberAttr(self, numberAttr: str):
        """
        Setter for property: (str) NumberAttr
         Returns the number attr   
            
         
        """
        pass
    @property
    def NumberingSource(self) -> PartOperationImportBuilder.NumberingSourceOption:
        """
        Getter for property: ( PartOperationImportBuilder.NumberingSourceOption NXOp) NumberingSource
         Returns the numbering source   
            
         
        """
        pass
    @NumberingSource.setter
    def NumberingSource(self, numberingSource: PartOperationImportBuilder.NumberingSourceOption):
        """
        Setter for property: ( PartOperationImportBuilder.NumberingSourceOption NXOp) NumberingSource
         Returns the numbering source   
            
         
        """
        pass
    @property
    def OutputLogFile(self) -> str:
        """
        Getter for property: (str) OutputLogFile
         Returns the output log file   
            
         
        """
        pass
    @OutputLogFile.setter
    def OutputLogFile(self, filename: str):
        """
        Setter for property: (str) OutputLogFile
         Returns the output log file   
            
         
        """
        pass
    @property
    def PrefixStr(self) -> str:
        """
        Getter for property: (str) PrefixStr
         Returns the prefix str   
            
         
        """
        pass
    @PrefixStr.setter
    def PrefixStr(self, prefixStr: str):
        """
        Setter for property: (str) PrefixStr
         Returns the prefix str   
            
         
        """
        pass
    @property
    def ProductInterfaces(self) -> bool:
        """
        Getter for property: (bool) ProductInterfaces
         Returns the product interfaces   
            
         
        """
        pass
    @ProductInterfaces.setter
    def ProductInterfaces(self, productInterfaces: bool):
        """
        Setter for property: (bool) ProductInterfaces
         Returns the product interfaces   
            
         
        """
        pass
    @property
    def PublishJTData(self) -> bool:
        """
        Getter for property: (bool) PublishJTData
         Returns the flag for JT data publishing   
            
         
        """
        pass
    @PublishJTData.setter
    def PublishJTData(self, publishJTData: bool):
        """
        Setter for property: (bool) PublishJTData
         Returns the flag for JT data publishing   
            
         
        """
        pass
    @property
    def PublishOptionalInfo(self) -> bool:
        """
        Getter for property: (bool) PublishOptionalInfo
         Returns the optional information publishing   
            
         
        """
        pass
    @PublishOptionalInfo.setter
    def PublishOptionalInfo(self, publishOptionalInfo: bool):
        """
        Setter for property: (bool) PublishOptionalInfo
         Returns the optional information publishing   
            
         
        """
        pass
    @property
    def ReplaceWithStr(self) -> str:
        """
        Getter for property: (str) ReplaceWithStr
         Returns the replace with str   
            
         
        """
        pass
    @ReplaceWithStr.setter
    def ReplaceWithStr(self, replaceWithStr: str):
        """
        Setter for property: (str) ReplaceWithStr
         Returns the replace with str   
            
         
        """
        pass
    @property
    def RevisionAttr(self) -> str:
        """
        Getter for property: (str) RevisionAttr
         Returns the revision attr   
            
         
        """
        pass
    @RevisionAttr.setter
    def RevisionAttr(self, revisionAttr: str):
        """
        Setter for property: (str) RevisionAttr
         Returns the revision attr   
            
         
        """
        pass
    @property
    def StringToReplace(self) -> str:
        """
        Getter for property: (str) StringToReplace
         Returns the string to replace   
            
         
        """
        pass
    @StringToReplace.setter
    def StringToReplace(self, stringToReplace: str):
        """
        Setter for property: (str) StringToReplace
         Returns the string to replace   
            
         
        """
        pass
    @property
    def SuffixStr(self) -> str:
        """
        Getter for property: (str) SuffixStr
         Returns the suffix str   
            
         
        """
        pass
    @SuffixStr.setter
    def SuffixStr(self, suffixStr: str):
        """
        Setter for property: (str) SuffixStr
         Returns the suffix str   
            
         
        """
        pass
    @property
    def SyncArrangements(self) -> bool:
        """
        Getter for property: (bool) SyncArrangements
         Returns the sync arrangements   
            
         
        """
        pass
    @SyncArrangements.setter
    def SyncArrangements(self, syncArrangements: bool):
        """
        Setter for property: (bool) SyncArrangements
         Returns the sync arrangements   
            
         
        """
        pass
    @property
    def UseItemTypeFromPartFile(self) -> bool:
        """
        Getter for property: (bool) UseItemTypeFromPartFile
         Returns the flag to specify if Import can use the Item Type already present in the part during import   
            
         
        """
        pass
    @UseItemTypeFromPartFile.setter
    def UseItemTypeFromPartFile(self, useItemTypeFromPartFile: bool):
        """
        Setter for property: (bool) UseItemTypeFromPartFile
         Returns the flag to specify if Import can use the Item Type already present in the part during import   
            
         
        """
        pass
    @property
    def ValidationAbortImportOnFail(self) -> bool:
        """
        Getter for property: (bool) ValidationAbortImportOnFail
         Returns the validation abort import on fail   
            
         
        """
        pass
    @ValidationAbortImportOnFail.setter
    def ValidationAbortImportOnFail(self, validationAbortImportOnFail: bool):
        """
        Setter for property: (bool) ValidationAbortImportOnFail
         Returns the validation abort import on fail   
            
         
        """
        pass
    @property
    def ValidationMode(self) -> PartOperationImportBuilder.Validation:
        """
        Getter for property: ( PartOperationImportBuilder.Validation NXOp) ValidationMode
         Returns the validation mode   
            
         
        """
        pass
    @ValidationMode.setter
    def ValidationMode(self, validationMode: PartOperationImportBuilder.Validation):
        """
        Setter for property: ( PartOperationImportBuilder.Validation NXOp) ValidationMode
         Returns the validation mode   
            
         
        """
        pass
    @property
    def ValidationRuleSetBrowseOption(self) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
        """
        Getter for property: ( PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOp) ValidationRuleSetBrowseOption
         Returns the validation rule set browse option   
            
         
        """
        pass
    @ValidationRuleSetBrowseOption.setter
    def ValidationRuleSetBrowseOption(self, validationRuleSetBrowseOption: PartOperationImportBuilder.ValidationRuleSetFileBrowseOption):
        """
        Setter for property: ( PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOp) ValidationRuleSetBrowseOption
         Returns the validation rule set browse option   
            
         
        """
        pass
    @property
    def ValidationRuleSetFile(self) -> str:
        """
        Getter for property: (str) ValidationRuleSetFile
         Returns the validation rule set file   
            
         
        """
        pass
    @ValidationRuleSetFile.setter
    def ValidationRuleSetFile(self, filename: str):
        """
        Setter for property: (str) ValidationRuleSetFile
         Returns the validation rule set file   
            
         
        """
        pass
    @property
    def ValidationTreatOutdatedAsPass(self) -> bool:
        """
        Getter for property: (bool) ValidationTreatOutdatedAsPass
         Returns the validation treat outdated as pass   
            
         
        """
        pass
    @ValidationTreatOutdatedAsPass.setter
    def ValidationTreatOutdatedAsPass(self, validationTreatOutdatedAsPass: bool):
        """
        Setter for property: (bool) ValidationTreatOutdatedAsPass
         Returns the validation treat outdated as pass   
            
         
        """
        pass
    @property
    def ValidationTreatWarningAsPass(self) -> bool:
        """
        Getter for property: (bool) ValidationTreatWarningAsPass
         Returns the validation treat warning as pass   
            
         
        """
        pass
    @ValidationTreatWarningAsPass.setter
    def ValidationTreatWarningAsPass(self, validationTreatWarningAsPass: bool):
        """
        Setter for property: (bool) ValidationTreatWarningAsPass
         Returns the validation treat warning as pass   
            
         
        """
        pass
    def AddParts(self, parts: List[str]) -> List[str]:
        """
         Add parts to import 
         Returns errorMsgs (List[str]): .
        """
        pass
    def AddPartsFromFolder(self, folderPath: str) -> List[str]:
        """
         Add parts to import from selected folder 
         Returns errorMsgs (List[str]): .
        """
        pass
    def AddPartsUsingLogFile(self, logFilePath: str) -> List[str]:
        """
         Add parts using log file either clone log file or import log file 
         Returns errorMsgs (List[str]): .
        """
        pass
    def ExecuteDryRun(self) -> None:
        """
         Execute the dry run 
        """
        pass
    def GetDefaultProjectInformation(self) -> Tuple[List[str], List[NXOpen.Session.ProjectAssignmentState]]:
        """
         Get default projects information 
         Returns A tuple consisting of (project_names, assignment_states). 
         - project_names is: List[str]. names of the projects .
         - assignment_states is:  NXOpen.Session.ProjectAssignmentState Li. assignment states .

        """
        pass
    def GetDfaFiles(self) -> List[str]:
        """
         Get the dfa files 
         Returns dfaFiles (List[str]): .
        """
        pass
    def GetExternalFileObjects(self, logicalObject: LogicalObject) -> List[NXOpen.NXObject]:
        """
         Gets the external file objects for the given part. 
         Returns objects ( NXOpen.NXObject Li): .
        """
        pass
    def GetLogicalObjectForPart(self, part_filename: str) -> LogicalObject:
        """
         Gets the known logical object for the given part filename. 
         Returns logicalObject ( LogicalObject NXOp): .
        """
        pass
    def GetUpdatedLogicalObjects(self) -> List[LogicalObject]:
        """
         Gets the updated logical object objects for the parts after item type, relation type or
                    master part for nonmaster is set or changed. 
         Returns logicalObjects ( LogicalObject List[NX): .
        """
        pass
    def RemoveDfaFile(self, filename: str) -> None:
        """
         Remove the dfa file 
        """
        pass
    def ResetAttributes(self, logicalObjects: List[LogicalObject]) -> None:
        """
         Clear all attributes from the selected logical objects 
        """
        pass
    def SetDefaultProjectInformation(self, project_names: List[str], assignment_states: List[NXOpen.Session.ProjectAssignmentState]) -> None:
        """
         Set default projects information 
        """
        pass
    def SetDfaFiles(self, dfaFiles: List[str]) -> None:
        """
         Set the dfa files 
        """
        pass
    def SetExistingPartAttributes(self, logicalObject: LogicalObject, existingPartCliSpec: str) -> None:
        """
         Set attributes of existing part on the given logical object so that 
                    the part gets imported into specified existing item based on action. 
        """
        pass
    def SetPartFamilyTreatment(self, partFamilyTreatment: PartOperationImportBuilder.PartFamilyTreatment) -> None:
        """
         This API will decide how to treat the Part Family members present in import operation depending on 
                    the partFamilyTreatment input value.
                    This API should be used only after assembly has been added for import operation as it will
                    iterate over all the Part Family Members added in import operation and set their behavior specified by
                    the partFamilyTreatment input value.
                    Note 1: If 'Ignore Part Family Member - Include Template Part' customer default is enabled then it will always treat
                    Part Family Members as 'Lost' in import, So please do not use this API if this customer default is enabled,
                    since using this API to change the behavior of Part Family Members will not work in that case. 
                    Note 2: If 'Ignore Part Family Member - Include Template Part' customer default is disabled then the user must use this API
                    to set the desired behavior of Part Family Members. If the desired behavior is not set using this API then 
                    Part Family Members will not participate anymore in import operation.
                
        """
        pass
    def UpdateDestinationFolderForParts(self) -> None:
        """
        The method updates the destination folder for parts getting imported into Teamcenter  
        """
        pass
    def UpdateTeamcenterInformation(self, logicalObjects: List[LogicalObject]) -> None:
        """
         Update the Teamcenter information string attribute TCIN_IMPORT_TEAMCENTER_INFORMATION on given logical objects 
        """
        pass
    def ValidateLogicalObjects(self) -> None:
        """
         Validate the user inputs for following things:
                    - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.
                    - Check for duplicate IdsMfk-Ids
                    - Check if all required attributes have been set
                    - Check for cyclic references
                    - Check if the part to import already exists in database and has no read access
                    - Check if the part to import already exists in database and belong to an invalid type for import(e.g. Shape Design)
                    - Check for duplicate non-master dataset names under same master
                    - Check if it is trying to create two new revisions of same item.
                    - Check if the final name given to the imported part already open in session
                    - Validate master for a non-master being imported; the master should be present in import operation or has to exist in database for successful creation of non-master.
                    - Validate validation parameters e.g. user has selected Run Validation option which requires the user to specify the validation rule set file.
                    - Update Teamcenter information attribute on logical objects
                
        """
        pass
import NXOpen
class PartOperationImportCallbackData(NXOpen.TaggedObject): 
    """ JA interface for PartOperationImportCallbackData object """
    @property
    def ImportBuilder(self) -> PartOperationImportBuilder:
        """
        Getter for property: ( PartOperationImportBuilder NXOp) ImportBuilder
         Returns the  NXOpen::PDM::PartOperationImportBuilder  builder used in this operation   
            
         
        """
        pass
    def GetLogicalObjects(self) -> List[NativePartLogicalObject]:
        """
         Gets the logical objects for parts participating in import operation 
         Returns logicalObjects ( NativePartLogicalObject List[NX):  .
        """
        pass
import NXOpen
class PartOperationImportObserver(NXOpen.TaggedObjectCollection): 
    """
     This class is responsible for invoking registered callbacks at different stages in import operation.
    
     NOTE: Use callback data NXOpen.PDM.PartOperationImportCallbackData, which is
     passed as input to these callback functions, to get the logical objects participating in the current
     import operation. It is recommended not to hold onto these logical objects since there lifecycle is
     controlled by the key attributes viz. Item type, Relation type; which could be updated during this
     operation, resulting in redefining the logical object.
     
    """
    InitializeCb = Callable[[PartOperationImportCallbackData], None]
    def AddInitializeCallback(initialize_cb: PartOperationImportObserver.InitializeCb) -> int:
        """
         Registers a user defined Initialize callback that is called during initialization of import builder 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PostCommitCb = Callable[[PartOperationImportCallbackData], None]
    def AddPostCommitCallback(post_commit_cb: PartOperationImportObserver.PostCommitCb) -> int:
        """
         Registers a user defined PostCommit callback that is called after commit of import operation 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PreAutoassignCb = Callable[[PartOperationImportCallbackData], None]
    def AddPreAutoassignCallback(pre_autoassign_cb: PartOperationImportObserver.PreAutoassignCb) -> int:
        """
         Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PreCommitCb = Callable[[PartOperationImportCallbackData], None]
    def AddPreCommitCallback(pre_commit_cb: PartOperationImportObserver.PreCommitCb) -> int:
        """
         Registers a user defined PreCommit callback that is called before commit of import operation 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PreValidateCb = Callable[[PartOperationImportCallbackData], None]
    def AddPreValidateCallback(pre_validate_cb: PartOperationImportObserver.PreValidateCb) -> int:
        """
         Registers a user defined PreValidate callback that is called at start of validate objects of import operation 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    TerminateCb = Callable[[PartOperationImportCallbackData], None]
    def AddTerminateCallback(terminate_cb: PartOperationImportObserver.TerminateCb) -> int:
        """
         Registers a user defined Terminate callback that is called during destruction of import builder 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    def RemoveInitializeCallback(id: int) -> None:
        """
         Unregisters the user defined Initialize callback 
        """
        pass
    def RemovePostCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PostCommit callback 
        """
        pass
    def RemovePreAutoassignCallback(id: int) -> None:
        """
         Unregisters the user defined PreAutoAssign callback 
        """
        pass
    def RemovePreCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PreCommit callback 
        """
        pass
    def RemovePreValidateCallback(id: int) -> None:
        """
         Unregisters the user defined PreValidate callback 
        """
        pass
    def RemoveTerminateCallback(id: int) -> None:
        """
         Unregisters the user defined Terminate callback 
        """
        pass
import NXOpen
class PartOperationMakeUniqueBuilder(PartOperationCopyBuilder): 
    """ Represents a NXOpen.PDM.PartOperationMakeUniqueBuilder builder """
    @property
    def SelectedComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectedComponents
         Returns the selected components to be made unique are returned.  
              
         
        """
        pass
import NXOpen
class PartOperationValidationPropertiesBuilder(NXOpen.AttributePropertiesBuilder): 
    """
        Represents an NXOpen.PDM.PartOperationValidationPropertiesBuilder to be used 
        for overriding the default validation parameters for a part in import operation.
    """
    def GetValidationRuleSetBrowseOption(self) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
        """
         Gets the validation rule set browse option 
         Returns validationRuleSetBrowseOption ( PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOp): .
        """
        pass
    def GetValidationRuleSetFile(self) -> str:
        """
         Gets the validation rule set file 
         Returns filename (str): .
        """
        pass
    def GetValidationTreatOutdatedAsPass(self) -> bool:
        """
         Gets the validation treat outdated as pass flag 
         Returns validationTreatOutdatedAsPass (bool): .
        """
        pass
    def GetValidationTreatWarningAsPass(self) -> bool:
        """
         Gets the validation treat warning as pass flag 
         Returns validationTreatWarningAsPass (bool): .
        """
        pass
    def SetValidationRuleSetBrowseOption(self, validationRuleSetBrowseOption: PartOperationImportBuilder.ValidationRuleSetFileBrowseOption) -> None:
        """
         Sets the validation rule set browse option 
        """
        pass
    def SetValidationRuleSetFile(self, filename: str) -> None:
        """
         Sets the validation rule set file 
        """
        pass
    def SetValidationTreatOutdatedAsPass(self, validationTreatOutdatedAsPass: bool) -> None:
        """
         Sets the validation treat outdated as pass flag 
        """
        pass
    def SetValidationTreatWarningAsPass(self, validationTreatWarningAsPass: bool) -> None:
        """
         Sets the validation treat warning as pass flag 
        """
        pass
import NXOpen
class PdmCopyOrEditOperationAttributePropertiesBuilder(NXOpen.AttributePropertiesBuilder): 
    """
        Represents an NXOpen.PDM.PdmCopyOrEditOperationAttributePropertiesBuilder to be used 
        for overriding the default values for a part in clone operation.
    """
    pass
import NXOpen
class PdmCopyOrEditOperationBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs Copy or Edit(Clone) operation """
    class CaeRelationTraversalOption(Enum):
        """
        Members Include: 
         |SimFemIdeal| 
         |FemIdeal| 
         |Ideal| 
         |NotSet| 

        """
        SimFemIdeal: int
        FemIdeal: int
        Ideal: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CloneAction(Enum):
        """
        Members Include: 
         |Clone| 
         |Retain| 
         |Revise| 
         |Replace| 
         |Overwrite| 

        """
        Clone: int
        Retain: int
        Revise: int
        Replace: int
        Overwrite: int
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.CloneAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConversionRule(Enum):
        """
        Members Include: 
         |WithPrefix| 
         |WithSuffix| 
         |WithReplaceString| 
         |WithRenumber| 
         |MixedRule| 

        """
        WithPrefix: int
        WithSuffix: int
        WithReplaceString: int
        WithRenumber: int
        MixedRule: int
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.ConversionRule:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NumberingSourceOption(Enum):
        """
        Members Include: 
         |AutoGenerate| 
         |NamingRule| 
         |UserName| 

        """
        AutoGenerate: int
        NamingRule: int
        UserName: int
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.NumberingSourceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignAlternateIds(self) -> bool:
        """
        Getter for property: (bool) AssignAlternateIds
         Returns the function returnssets the flag to assign alternate IDs during Pdm copy or edit operation   
            
         
        """
        pass
    @AssignAlternateIds.setter
    def AssignAlternateIds(self, createAlternateIDs: bool):
        """
        Setter for property: (bool) AssignAlternateIds
         Returns the function returnssets the flag to assign alternate IDs during Pdm copy or edit operation   
            
         
        """
        pass
    @property
    def AssignDefaultChangeNotice(self) -> bool:
        """
        Getter for property: (bool) AssignDefaultChangeNotice
         Returns the function returnssets the flag to assign the default change notice set on builder to target objects created in pdm copy or edit operation.  
             
         
        """
        pass
    @AssignDefaultChangeNotice.setter
    def AssignDefaultChangeNotice(self, assignDefaultChangeNotice: bool):
        """
        Setter for property: (bool) AssignDefaultChangeNotice
         Returns the function returnssets the flag to assign the default change notice set on builder to target objects created in pdm copy or edit operation.  
             
         
        """
        pass
    @property
    def AttachLogFile(self) -> bool:
        """
        Getter for property: (bool) AttachLogFile
         Returns the function returnssets the flag to attach the output log file as associated file to the top part of the input assembly   
            
         
        """
        pass
    @AttachLogFile.setter
    def AttachLogFile(self, attachLogFile: bool):
        """
        Setter for property: (bool) AttachLogFile
         Returns the function returnssets the flag to attach the output log file as associated file to the top part of the input assembly   
            
         
        """
        pass
    @property
    def ConversionType(self) -> PdmCopyOrEditOperationBuilder.ConversionRule:
        """
        Getter for property: ( PdmCopyOrEditOperationBuilder.ConversionRule NXOp) ConversionType
         Returns the function returnssets the conversion type to use for generating a new part ID   
            
         
        """
        pass
    @ConversionType.setter
    def ConversionType(self, conversionType: PdmCopyOrEditOperationBuilder.ConversionRule):
        """
        Setter for property: ( PdmCopyOrEditOperationBuilder.ConversionRule NXOp) ConversionType
         Returns the function returnssets the conversion type to use for generating a new part ID   
            
         
        """
        pass
    @property
    def CopyAltrep(self) -> bool:
        """
        Getter for property: (bool) CopyAltrep
         Returns the function returnssets the flag to copy non-master altrep   
            
         
        """
        pass
    @CopyAltrep.setter
    def CopyAltrep(self, copyAltrep: bool):
        """
        Setter for property: (bool) CopyAltrep
         Returns the function returnssets the flag to copy non-master altrep   
            
         
        """
        pass
    @property
    def CopyAssociatedFiles(self) -> bool:
        """
        Getter for property: (bool) CopyAssociatedFiles
         Returns the function returnssets the flag to copy associated files   
            
         
        """
        pass
    @CopyAssociatedFiles.setter
    def CopyAssociatedFiles(self, copyAssociatedFiles: bool):
        """
        Setter for property: (bool) CopyAssociatedFiles
         Returns the function returnssets the flag to copy associated files   
            
         
        """
        pass
    @property
    def CopyCaeMotion(self) -> bool:
        """
        Getter for property: (bool) CopyCaeMotion
         Returns the function returnssets the flag to copy non-master cae-motion   
            
         
        """
        pass
    @CopyCaeMotion.setter
    def CopyCaeMotion(self, copyCaeMotion: bool):
        """
        Setter for property: (bool) CopyCaeMotion
         Returns the function returnssets the flag to copy non-master cae-motion   
            
         
        """
        pass
    @property
    def CopyCaeRelationOption(self) -> PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption:
        """
        Getter for property: ( PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOp) CopyCaeRelationOption
         Returns the function returnssets the option to include cae components in Pdm copy or edit operation   
            
         
        """
        pass
    @CopyCaeRelationOption.setter
    def CopyCaeRelationOption(self, copyCaeRelationOption: PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption):
        """
        Setter for property: ( PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOp) CopyCaeRelationOption
         Returns the function returnssets the option to include cae components in Pdm copy or edit operation   
            
         
        """
        pass
    @property
    def CopyCaeRelations(self) -> bool:
        """
        Getter for property: (bool) CopyCaeRelations
         Returns the function returnssets the flag to include cae related components in Pdm copy or edit operation   
            
         
        """
        pass
    @CopyCaeRelations.setter
    def CopyCaeRelations(self, copyCaeRelations: bool):
        """
        Setter for property: (bool) CopyCaeRelations
         Returns the function returnssets the flag to include cae related components in Pdm copy or edit operation   
            
         
        """
        pass
    @property
    def CopyDrawingRelations(self) -> bool:
        """
        Getter for property: (bool) CopyDrawingRelations
         Returns the function returnssets the flag to include master drawings of the assemblyparts added in Pdm copy or edit operation   
            
         
        """
        pass
    @CopyDrawingRelations.setter
    def CopyDrawingRelations(self, copyDrawingRelations: bool):
        """
        Setter for property: (bool) CopyDrawingRelations
         Returns the function returnssets the flag to include master drawings of the assemblyparts added in Pdm copy or edit operation   
            
         
        """
        pass
    @property
    def CopyManifestation(self) -> bool:
        """
        Getter for property: (bool) CopyManifestation
         Returns the function returnssets the flag to copy non-master menifestation  
            
         
        """
        pass
    @CopyManifestation.setter
    def CopyManifestation(self, copyManifestation: bool):
        """
        Setter for property: (bool) CopyManifestation
         Returns the function returnssets the flag to copy non-master menifestation  
            
         
        """
        pass
    @property
    def CopySpecification(self) -> bool:
        """
        Getter for property: (bool) CopySpecification
         Returns the function returnssets the flag to copy non-master specification   
            
         
        """
        pass
    @CopySpecification.setter
    def CopySpecification(self, copySpecification: bool):
        """
        Setter for property: (bool) CopySpecification
         Returns the function returnssets the flag to copy non-master specification   
            
         
        """
        pass
    @property
    def DefaultAction(self) -> PdmCopyOrEditOperationBuilder.CloneAction:
        """
        Getter for property: ( PdmCopyOrEditOperationBuilder.CloneAction NXOp) DefaultAction
         Returns the function returnssets the default clone action to use for Pdm copy or edit operation   
            
         
        """
        pass
    @DefaultAction.setter
    def DefaultAction(self, defaultAction: PdmCopyOrEditOperationBuilder.CloneAction):
        """
        Setter for property: ( PdmCopyOrEditOperationBuilder.CloneAction NXOp) DefaultAction
         Returns the function returnssets the default clone action to use for Pdm copy or edit operation   
            
         
        """
        pass
    @property
    def DefaultAlternateIdContext(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdContext
         Returns the function returnssets the IdContext to be used while assigning alternate IDs during clone   
            
         
        """
        pass
    @DefaultAlternateIdContext.setter
    def DefaultAlternateIdContext(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdContext
         Returns the function returnssets the IdContext to be used while assigning alternate IDs during clone   
            
         
        """
        pass
    @property
    def DefaultAlternateIdType(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdType
         Returns the function returnssets the IdType to be used while assigning alternate IDs during clone  
            
         
        """
        pass
    @DefaultAlternateIdType.setter
    def DefaultAlternateIdType(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdType
         Returns the function returnssets the IdType to be used while assigning alternate IDs during clone  
            
         
        """
        pass
    @property
    def DefaultChangeNotice(self) -> str:
        """
        Getter for property: (str) DefaultChangeNotice
         Returns the function returnssets the default change notice for Pdm copy or edit operation in CLI format.  
             
         
        """
        pass
    @DefaultChangeNotice.setter
    def DefaultChangeNotice(self, defaultChangeNotice: str):
        """
        Setter for property: (str) DefaultChangeNotice
         Returns the function returnssets the default change notice for Pdm copy or edit operation in CLI format.  
             
         
        """
        pass
    @property
    def DefaultOwningGroup(self) -> str:
        """
        Getter for property: (str) DefaultOwningGroup
         Returns the function returnssets the default owning group to be assigned to the cloned parts   
            
         
        """
        pass
    @DefaultOwningGroup.setter
    def DefaultOwningGroup(self, defaultOwningGroup: str):
        """
        Setter for property: (str) DefaultOwningGroup
         Returns the function returnssets the default owning group to be assigned to the cloned parts   
            
         
        """
        pass
    @property
    def DefaultOwningUser(self) -> str:
        """
        Getter for property: (str) DefaultOwningUser
         Returns the function returnssets the default owning user to be assigned to the cloned parts   
            
         
        """
        pass
    @DefaultOwningUser.setter
    def DefaultOwningUser(self, defaultOwningUser: str):
        """
        Setter for property: (str) DefaultOwningUser
         Returns the function returnssets the default owning user to be assigned to the cloned parts   
            
         
        """
        pass
    @property
    def IncludeComponentParts(self) -> bool:
        """
        Getter for property: (bool) IncludeComponentParts
         Returns the function returnssets the flag to include component parts of the assembly added in Pdm copy or edit operation   
            
         
        """
        pass
    @IncludeComponentParts.setter
    def IncludeComponentParts(self, includeComponentParts: bool):
        """
        Setter for property: (bool) IncludeComponentParts
         Returns the function returnssets the flag to include component parts of the assembly added in Pdm copy or edit operation   
            
         
        """
        pass
    @property
    def NumberingSource(self) -> PdmCopyOrEditOperationBuilder.NumberingSourceOption:
        """
        Getter for property: ( PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOp) NumberingSource
         Returns the function returnssets the numbering source to use for Part ID generation   
            
         
        """
        pass
    @NumberingSource.setter
    def NumberingSource(self, numberingSource: PdmCopyOrEditOperationBuilder.NumberingSourceOption):
        """
        Setter for property: ( PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOp) NumberingSource
         Returns the function returnssets the numbering source to use for Part ID generation   
            
         
        """
        pass
    @property
    def OutputLogFile(self) -> str:
        """
        Getter for property: (str) OutputLogFile
         Returns the function returnssets the output log file to dump Pdm copy or edit operation information   
            
         
        """
        pass
    @OutputLogFile.setter
    def OutputLogFile(self, filename: str):
        """
        Setter for property: (str) OutputLogFile
         Returns the function returnssets the output log file to dump Pdm copy or edit operation information   
            
         
        """
        pass
    @property
    def PrefixStr(self) -> str:
        """
        Getter for property: (str) PrefixStr
         Returns the function returnssets the prefix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    @PrefixStr.setter
    def PrefixStr(self, prefixStr: str):
        """
        Setter for property: (str) PrefixStr
         Returns the function returnssets the prefix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    @property
    def RenumberStr(self) -> str:
        """
        Getter for property: (str) RenumberStr
         Returns the function returnssets the renumber string to generate a new part ID   
            
         
        """
        pass
    @RenumberStr.setter
    def RenumberStr(self, numberAttr: str):
        """
        Setter for property: (str) RenumberStr
         Returns the function returnssets the renumber string to generate a new part ID   
            
         
        """
        pass
    @property
    def ReplaceWithStr(self) -> str:
        """
        Getter for property: (str) ReplaceWithStr
         Returns the function returnssets the string to replace with, to generate a new part ID   
            
         
        """
        pass
    @ReplaceWithStr.setter
    def ReplaceWithStr(self, replaceWithStr: str):
        """
        Setter for property: (str) ReplaceWithStr
         Returns the function returnssets the string to replace with, to generate a new part ID   
            
         
        """
        pass
    @property
    def RetainOwnership(self) -> bool:
        """
        Getter for property: (bool) RetainOwnership
         Returns the function returnssets the flag to retain ownership of the parts during clone   
            
         
        """
        pass
    @RetainOwnership.setter
    def RetainOwnership(self, retainOwnership: bool):
        """
        Setter for property: (bool) RetainOwnership
         Returns the function returnssets the flag to retain ownership of the parts during clone   
            
         
        """
        pass
    @property
    def StringToReplace(self) -> str:
        """
        Getter for property: (str) StringToReplace
         Returns the function returnssets the string in the source part ID to replace, to generate a new part ID   
            
         
        """
        pass
    @StringToReplace.setter
    def StringToReplace(self, stringToReplace: str):
        """
        Setter for property: (str) StringToReplace
         Returns the function returnssets the string in the source part ID to replace, to generate a new part ID   
            
         
        """
        pass
    @property
    def SuffixStr(self) -> str:
        """
        Getter for property: (str) SuffixStr
         Returns the function returnssets the suffix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    @SuffixStr.setter
    def SuffixStr(self, suffixStr: str):
        """
        Setter for property: (str) SuffixStr
         Returns the function returnssets the suffix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    def AddParts(self, parts: List[str]) -> List[str]:
        """
         This function adds parts to the Pdm copy or edit operation 
         Returns errorMsgs (List[str]): .
        """
        pass
    def AddPartsUsingCloneLogFile(self, logFilePath: str) -> List[str]:
        """
         This function adds parts to the Pdm copy or edit operation using clone log file 
         Returns errorMsgs (List[str]): .
        """
        pass
    def CreateOrUpdatePdmCopyOrEditOperationObjects(self, doUpdate: bool) -> List[PdmCopyOrEditOperationObject]:
        """
         This function createsupdates the operation objects of the parts participating in the Pdm copy or edit operation.
                    Note: The operation object needs to be updated in certain cases, e.g. after item type is changed.
                
         Returns copyOperationObjects ( PdmCopyOrEditOperationObject List[NX): .
        """
        pass
    def ExecuteDryRun(self) -> None:
        """
         This function executes the dry run 
        """
        pass
    def GetDefaultProjectInformation(self) -> Tuple[List[str], List[NXOpen.Session.ProjectAssignmentState]]:
        """
         This function gets the default projects information 
         Returns A tuple consisting of (project_names, assignment_states). 
         - project_names is: List[str]. names of the projects .
         - assignment_states is:  NXOpen.Session.ProjectAssignmentState Li. assignment states .

        """
        pass
    def GetPdmCopyOrEditOperationObject(self, part_filename: str) -> PdmCopyOrEditOperationObject:
        """
         This function gets the operation object for the given part spec. 
         Returns operationObject ( PdmCopyOrEditOperationObject NXOp): .
        """
        pass
    def GetPdmCopyOrEditOperationObjects(self) -> List[PdmCopyOrEditOperationObject]:
        """
         This function gets all the operation objects participating in the Pdm copy or edit operation. 
         Returns copyOperationObjects ( PdmCopyOrEditOperationObject List[NX): .
        """
        pass
    def ResetAttributes(self, objects: List[NXOpen.NXObject]) -> None:
        """
         This function cleara all attributes from the selected operation objects 
        """
        pass
    def SetCloneAction(self, operationObject: PdmCopyOrEditOperationObject, cloneAction: PdmCopyOrEditOperationBuilder.CloneAction) -> List[PdmCopyOrEditOperationObject]:
        """
         This function sets the clone action on given operation objects, this change in action 
                might cause clone action change on related operation objects. Operation objects
                whose action got changed will be returned 
         Returns modifiedLogicalObjects ( PdmCopyOrEditOperationObject List[NX): .
        """
        pass
    def SetConfigurationContextUsingRevRule(self, setDefault: bool, revisionRuleName: str) -> int:
        """
         This function sets the configuration context using the Revision Rule Name. 
         Returns status (int): .
        """
        pass
    def SetDefaultProjectInformation(self, project_names: List[str], assignment_states: List[NXOpen.Session.ProjectAssignmentState]) -> None:
        """
         This function sets the default projects information 
        """
        pass
    def SetLoadOption(self, loadOption: NXOpen.LoadOptions.ManagedModeLoadMethod) -> None:
        """
         This function sets the assembly load option for managed mode. 
        """
        pass
    def SetOverwritePart(self, operationObject: PdmCopyOrEditOperationObject, transientPartCliSpec: str) -> int:
        """
         This function sets the transient part to overwrite for the given operation object, this is needed for OVERWRITE action 
         Returns status (int): .
        """
        pass
    def SetReplacePart(self, operationObject: PdmCopyOrEditOperationObject, replacePartCliSpec: str) -> int:
        """
         This function sets the replacement part for the given operation object, this is needed for Replace action 
         Returns status (int): .
        """
        pass
    def UpdateNonMasterDatasetNameMatchingSaveAsPattern(self, operationObject: PdmCopyOrEditOperationObject) -> int:
        """
         For the input master part, this function updates all nonmaster dataset names by honoring the UGPART_saveas_pattern TC preference 
         Returns status (int): .
        """
        pass
    def UpdateTeamcenterInformation(self, objects: List[NXOpen.NXObject]) -> None:
        """
         This function updates the Teamcenter information string attribute 'TCIN_CLONE_TEAMCENTER_INFORMATION' on given operation objects 
        """
        pass
    def ValidateOperationObjects(self) -> None:
        """
         This function validates the user inputs for following things:
                    - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.
                    - Check for duplicate IdsMfk-Ids
                    - Check if all required attributes have been set
                
        """
        pass
import NXOpen
class PdmCopyOrEditOperationCallbackData(NXOpen.TaggedObject): 
    """ JA interface for PdmCopyOrEditOperationCallbackData object """
    def GetBuilder(self) -> PdmCopyOrEditOperationBuilder:
        """
         The NXOpen.PDM.PdmCopyOrEditOperationBuilder Builder used in this operation 
         Returns builder ( PdmCopyOrEditOperationBuilder NXOp): .
        """
        pass
import NXOpen
class PdmCopyOrEditOperationObject(NXOpen.NXObject): 
    """
        Represents the class for object participating in the Copy operation.
    """
    def GetCurrentPrimaryLogicalObject(self) -> LogicalObject:
        """
         Gets the primary logical object represented by this operation object 
         Returns primaryLogicalObject ( LogicalObject NXOp): .
        """
        pass
    def GetFinalName(self) -> str:
        """
         Gets the final name of this object. 
         Returns finalName (str):  the final name assigned to the part being cloned .
        """
        pass
    def GetInitialName(self) -> str:
        """
         Gets the initial name of this object. 
         Returns initialName (str):  the filename of added for copy .
        """
        pass
    def GetSecondaryLogicalObjects(self) -> List[LogicalObject]:
        """
         Gets the nonmaster logical objects associated with the copy operation object. 
         Returns secondaryLogicalObjects ( LogicalObject List[NX): .
        """
        pass
import NXOpen
class PdmCopyOrEditOperationObserver(NXOpen.TaggedObjectCollection): 
    """
     This class is responsible for invoking registered callbacks at different stages in clone operation.
    
     NOTE: Use callback data NXOpen.PDM.PdmCopyOrEditOperationCallbackData, which is
     passed as input to these callback functions, to get the logical objects participating in the current
     clone operation. It is recommended not to hold onto these logical objects since there lifecycle is
     controlled by the key attributes viz. Item type, Relation type; which could be updated during this
     operation, resulting in redefining the logical object.
     
    """
    InitializeCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    def AddInitializeCallback(initializeCb: PdmCopyOrEditOperationObserver.InitializeCallback) -> int:
        """
         Registers a user defined Initialize callback that is called during the initialization of clone builder 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PostCommitCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    def AddPostCommitCallback(postCommitCb: PdmCopyOrEditOperationObserver.PostCommitCallback) -> int:
        """
         Registers a user defined PostCommit callback that is called after commit of clone operation 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PreAutoassignCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    def AddPreAutoassignCallback(preAutoassignCb: PdmCopyOrEditOperationObserver.PreAutoassignCallback) -> int:
        """
         Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PreCommitCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    def AddPreCommitCallback(preCommitCb: PdmCopyOrEditOperationObserver.PreCommitCallback) -> int:
        """
         Registers a user defined PreCommit callback that is called before commit of clone operation 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PreValidateCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    def AddPreValidateCallback(preValidateCb: PdmCopyOrEditOperationObserver.PreValidateCallback) -> int:
        """
         Registers a user defined PreValidate callback that is called at start of validate objects of clone operation 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    TerminateCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    def AddTerminateCallback(terminateCb: PdmCopyOrEditOperationObserver.TerminateCallback) -> int:
        """
         Registers a user defined Terminate callback that is called during the destruction of clone builder 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    def RemoveInitializeCallback(id: int) -> None:
        """
         Unregisters the user defined Initialize callback 
        """
        pass
    def RemovePostCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PostCommit callback 
        """
        pass
    def RemovePreAutoassignCallback(id: int) -> None:
        """
         Unregisters the user defined PreAutoAssign callback 
        """
        pass
    def RemovePreCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PreCommit callback 
        """
        pass
    def RemovePreValidateCallback(id: int) -> None:
        """
         Unregisters the user defined PreValidate callback 
        """
        pass
    def RemoveTerminateCallback(id: int) -> None:
        """
         Unregisters the user defined Terminate callback 
        """
        pass
import NXOpen
class PdmFile(NXOpen.TransientObject): 
    """  Contains methods for accessing PDM file data.  """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def GetFileLastModifiedDate(self) -> str:
        """
         Get the last modified date of a PDM file. 
         Returns lastModifiedDate (str): .
        """
        pass
    def GetFileName(self) -> str:
        """
         Get the file name of a PDM file. 
         Returns fileName (str): .
        """
        pass
    def GetFileSize(self) -> str:
        """
         Get the file size of a PDM file. 
         Returns size (str): .
        """
        pass
import NXOpen
class PdmManager(NXOpen.Object): 
    """ Contains various PDM utility methods """
    def CreateBVRSearchRecipeFilterBuilder(topPart: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new NXOpen.PDM.SearchRecipeFilterBuilder object which supports Filtering of 
                structure discovery indexed BVR assembly. 
         Returns builder ( SearchRecipeFilterBuilder NXOp): .
        """
        pass
    def CreateDesignWorksetSearchRecipeFilterBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new NXOpen.PDM.SearchRecipeFilterBuilder object which supports Filtering of Design Workset. 
         Returns builder ( SearchRecipeFilterBuilder NXOp): .
        """
        pass
    def CreateExportWorksetForReferenceBuilder(workset: NXOpen.BasePart) -> ExportWorksetForReferenceBuilder:
        """
         Creates a new NXOpen.PDM.ExportWorksetForReferenceBuilder object used for
                    exporting workset outside Teamcenter for reference. 
         Returns builder ( ExportWorksetForReferenceBuilder NXOp): .
        """
        pass
    def CreateMakeUniqueOperationBuilder(part: NXOpen.BasePart) -> PartOperationMakeUniqueBuilder:
        """
        Returns a new NXOpen.PDM.PartOperationMakeUniqueBuilder object
         Returns builder ( PartOperationMakeUniqueBuilder NXOp): .
        """
        pass
    def CreatePartOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> PartOperationAttributePropertiesBuilder:
        """
         Creates a new NXOpen.PDM.PartOperationAttributePropertiesBuilder object. 
         Returns builder ( PartOperationAttributePropertiesBuilder NXOp): .
        """
        pass
    def CreatePartOperationValidationPropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new AttributePropertiesBuilder object. 
         Returns builder ( NXOpen.AttributePropertiesBuilder): .
        """
        pass
    def CreatePdmCopyOrEditOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new AttributePropertiesBuilder object. 
         Returns builder ( NXOpen.AttributePropertiesBuilder): .
        """
        pass
    def CreateProductSearchRecipeFilterBuilder(topPart: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new NXOpen.PDM.SearchRecipeFilterBuilder object which supports Filtering of 
                structure discovery indexed product. 
         Returns builder ( SearchRecipeFilterBuilder NXOp): .
        """
        pass
    def CreateSearchRecipeFilterBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new NXOpen.PDM.SearchRecipeFilterBuilder object which supports Filtering of Design Workset. 
         Returns builder ( SearchRecipeFilterBuilder NXOp): .
        """
        pass
    def CreateVariantRulesConfigurationBuilder(partTag: NXOpen.BasePart) -> VariantRulesConfigurationBuilder:
        """
         Creates a new NXOpen.PDM.VariantRulesConfigurationBuilder object. 
         Returns builder ( VariantRulesConfigurationBuilder NXOp): .
        """
        pass
import NXOpen
class PdmNavigatorNode(NXOpen.TreeListNode): 
    """ Represents a PdmNavigatorNode """
    def GetNodeType(self) -> str:
        """
         Returns the type of the PdmNavigatorNode in PDM 
         Returns type (str):  .
        """
        pass
    def GetUid(self) -> str:
        """
         Returns the unique identifier of the PdmNavigatorNode in PDM 
         Returns uid (str):  .
        """
        pass
import NXOpen
class PdmPart(NXOpen.Object): 
    """ This class serves as a gateway to part-specific tools for NX Manager mode.
    """
    class CheckinInput:
        """
         Reservation check-in input struct 
         PdmPartCheckinInput_Struct NXOp is an alias for  PdmPart.CheckinInput NXOp.
        """
        @property
        def AllowRemote(self) -> bool:
            """
            Getter for property AllowRemote
            True to allow remote check in, false otherwise

            """
            pass
        @AllowRemote.setter
        def AllowRemote(self, value: bool):
            """
            Getter for property AllowRemote
            True to allow remote check in, false otherwise
            Setter for property AllowRemote
            True to allow remote check in, false otherwise

            """
            pass
        @property
        def ExplicitCheckIn(self) -> bool:
            """
            Getter for property ExplicitCheckIn
            True to perform explicit check in, false otherwise

            """
            pass
        @ExplicitCheckIn.setter
        def ExplicitCheckIn(self, value: bool):
            """
            Getter for property ExplicitCheckIn
            True to perform explicit check in, false otherwise
            Setter for property ExplicitCheckIn
            True to perform explicit check in, false otherwise

            """
            pass
        @property
        def IncludeSecondary(self) -> bool:
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
        @IncludeSecondary.setter
        def IncludeSecondary(self, value: bool):
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise
            Setter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
    class CheckoutInput:
        """
         Reservation check-out input struct 
         PdmPartCheckoutInput_Struct NXOp is an alias for  PdmPart.CheckoutInput NXOp.
        """
        @property
        def InputComment(self) -> str:
            """
            Getter for property InputComment
            """
            pass
        @InputComment.setter
        def InputComment(self, value: str):
            """
            Getter for property InputCommentSetter for property InputComment
            """
            pass
        @property
        def InputChangeId(self) -> str:
            """
            Getter for property InputChangeId
            """
            pass
        @InputChangeId.setter
        def InputChangeId(self, value: str):
            """
            Getter for property InputChangeIdSetter for property InputChangeId
            """
            pass
        @property
        def AllowRemote(self) -> bool:
            """
            Getter for property AllowRemote
            True to allow remote check out, false otherwise

            """
            pass
        @AllowRemote.setter
        def AllowRemote(self, value: bool):
            """
            Getter for property AllowRemote
            True to allow remote check out, false otherwise
            Setter for property AllowRemote
            True to allow remote check out, false otherwise

            """
            pass
        @property
        def ExplicitCheckOut(self) -> bool:
            """
            Getter for property ExplicitCheckOut
            True to perform explicit check out, false otherwise

            """
            pass
        @ExplicitCheckOut.setter
        def ExplicitCheckOut(self, value: bool):
            """
            Getter for property ExplicitCheckOut
            True to perform explicit check out, false otherwise
            Setter for property ExplicitCheckOut
            True to perform explicit check out, false otherwise

            """
            pass
        @property
        def IncludeSecondary(self) -> bool:
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
        @IncludeSecondary.setter
        def IncludeSecondary(self, value: bool):
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise
            Setter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
    class PcaexpressionsInput:
        """
         Part Expressions input struct 
         PdmPartPcaexpressionsInput_Struct NXOp is an alias for  PdmPart.PcaexpressionsInput NXOp.
        """
        @property
        def Name(self) -> str:
            """
            Getter for property Name
            Name of PCA Expression

            """
            pass
        @Name.setter
        def Name(self, value: str):
            """
            Getter for property Name
            Name of PCA Expression
            Setter for property Name
            Name of PCA Expression

            """
            pass
        @property
        def Value(self) -> str:
            """
            Getter for property Value
            Value of PCA Expression

            """
            pass
        @Value.setter
        def Value(self, value: str):
            """
            Getter for property Value
            Value of PCA Expression
            Setter for property Value
            Value of PCA Expression

            """
            pass
        @property
        def Unit(self) -> str:
            """
            Getter for property Unit
            Unit of PCA Expression

            """
            pass
        @Unit.setter
        def Unit(self, value: str):
            """
            Getter for property Unit
            Unit of PCA Expression
            Setter for property Unit
            Unit of PCA Expression

            """
            pass
        @property
        def SavedVariants(self) -> str:
            """
            Getter for property SavedVariants
            Saved Variant Rule of PCA Expression

            """
            pass
        @SavedVariants.setter
        def SavedVariants(self, value: str):
            """
            Getter for property SavedVariants
            Saved Variant Rule of PCA Expression
            Setter for property SavedVariants
            Saved Variant Rule of PCA Expression

            """
            pass
        @property
        def Optionfamily(self) -> str:
            """
            Getter for property Optionfamily
            Option Family of PCA Expression

            """
            pass
        @Optionfamily.setter
        def Optionfamily(self, value: str):
            """
            Getter for property Optionfamily
            Option Family of PCA Expression
            Setter for property Optionfamily
            Option Family of PCA Expression

            """
            pass
        @property
        def OptionName(self) -> str:
            """
            Getter for property OptionName
            This input should not be specified and is deprecated

            """
            pass
        @OptionName.setter
        def OptionName(self, value: str):
            """
            Getter for property OptionName
            This input should not be specified and is deprecated
            Setter for property OptionName
            This input should not be specified and is deprecated

            """
            pass
    def ApplyVariantExpressions(self, pcaexpressionsInInput: List[PdmPart.PcaexpressionsInput]) -> None:
        """
         Apply the variant expressions to the part. 
        """
        pass
    def AssignPermanentName(self, new_file_name: str) -> None:
        """
         Assign a permanent name to the temporary part 
        """
        pass
    def CheckinParts(self, partsToCheckIn: List[NXOpen.BasePart], checkInInput: PdmPart.CheckinInput) -> OperationErrors:
        """
         Given an array of parts, check in the parts. 
         Returns pdmOperationErrors ( OperationErrors NXOp):  Errors encountered during the checkin .
        """
        pass
    def Checkout(self) -> None:
        """
         Checkout the part 
        """
        pass
    def CheckoutParts(self, partsToCheckOut: List[NXOpen.BasePart], checkOutInput: PdmPart.CheckoutInput) -> OperationErrors:
        """
         Given an array of parts, check out the parts. 
         Returns pdmOperationErrors ( OperationErrors NXOp):  Errors encountered during the checkout .
        """
        pass
    def ClearPreciseStructureOnSave(self, cancelPreciseOnSave: List[NXOpen.BasePart]) -> None:
        """
         Given an array of parts, this API will remove the 'Precise Structure on Save' on all the parts 
        """
        pass
    def GetCheckedoutStatusAndUser(self) -> Tuple[bool, str]:
        """
         Returns Checked out status of part and Checked out by. 
         Returns A tuple consisting of (isCheckedOut, checkedOutBy). 
         - isCheckedOut is: bool. Checked out status of given part .
         - checkedOutBy is: str. Checked out by user .

        """
        pass
    def GetOwnerAndGroup(self) -> Tuple[str, str]:
        """
         Returns owner and group for part. Loads value from Teamcenter if not available with NX. 
         Returns A tuple consisting of (owner, group). 
         - owner is: str.
         - group is: str.

        """
        pass
    def GetProjects(self) -> List[str]:
        """
         Returns the assigned project names array. Project names information is retrieved from Teamcenter. Loads value from Teamcenter if not available with NX. 
         Returns projects (List[str]): .
        """
        pass
    def GetRelatedDrawingSpecs(self) -> List[str]:
        """
         Get the related drawings specs of loaded part. Returns part specifications of master and non-master drawings, filtering out the diagrams 
         Returns relatedDrawingsCliSpecs (List[str]):  Array of part specification names for the related drawings .
        """
        pass
    def GetRelatedDrawings(self) -> List[str]:
        """
         Get the related drawings of loaded part. Returns part specifications of master and non-master drawings 
         Returns relatedDrawingsCliSpecs (List[str]):  Array of part specification names for the related drawings .
        """
        pass
    def GetRelatedGeometryRepresentationSpecs(self) -> List[str]:
        """
         Get the related geometry representation specs of loaded part. Returns part specifications of the master and altreps, with some error handling 
         Returns relatedGeometryCliSpecs (List[str]):  Array of part specification names for the related geometry representation .
        """
        pass
    def GetReleaseStatus(self) -> str:
        """
         Returns release status of part. Loads value from Teamcenter if not available with NX. 
         Returns releaseStatus (str): .
        """
        pass
    def IsModifiable(self) -> bool:
        """
         Returns true if the part is modifiable. 
         Returns isModifiable (bool): .
        """
        pass
    def ListNonMasters(self, nonMasterFileType: str) -> List[str]:
        """
         Given a part, get the names of the non-master types.
                This function returns a list of all the non-master models of a particular model type
                that are attached to a part revision.
                For each possible model type, it obtains all the non-master files of a part revision.
                This supports following dataset types and Allowed input strings(case-sensitive):
                
                NX dataset types and Allowed Input String(case-sensitive)
                NX Model Type         Allowed Input String(case-sensitive)
                SPEC_MODEL            "specification"
                MAN_MODEL             "manifestation"
                ALTREP_MODEL          "altrep"
                FOREIGN_MODEL         "multi-CAD"
                
                Dataset types for "multi-CAD" should be defined in Teamcenter preference "TC_NX_Foreign_Datasets".
                Format for multi-CAD parts should be in be of the form multi-CAD-datasettype
                e.g. multi-CAD-catia
                
         Returns nonMasterFileNames (List[str]):  Array of names of non-master files .
        """
        pass
    def NewAlternateIdManager(self) -> AlternateIdManager:
        """
         Create an instance of a NXOpen.PDM.AlternateIdManager
                class that will be used to create alternate ID information on the part. 
         Returns alternate_id_manager ( AlternateIdManager NXOp):  the new NXOpen.PDM.AlternateIdManager instance .
        """
        pass
    def NewDatabaseAttributeManager(self) -> DatabaseAttributeManager:
        """
         Create an instance of a NXOpen.PDM.DatabaseAttributeManager
                class that will be used to modify database attributes of the part. 
         Returns attribute_manager ( DatabaseAttributeManager NXOp):  the new NXOpen.PDM.DatabaseAttributeManager instance .
        """
        pass
    def PublishHdImagesForModelViews(self, imageWidth: int, imageHight: int) -> None:
        """
         Publish high-definition images for disclosed model views in the input displayed part. 
        """
        pass
    def SetDefaultFolderForPart(self) -> None:
        """
         Set default folder for the part in which it is to be saved 
        """
        pass
    def SetPreciseStructureOnSave(self, partsToSetPreciseOnSave: List[NXOpen.BasePart]) -> None:
        """
         Given an array of parts, Parts to set precise structure on save. 
        """
        pass
import NXOpen
class PdmSearchManager(NXOpen.Object): 
    """ Represents search manager class """
    def NewPdmListofvalues() -> ListOfValues:
        """
         Creates a new pdm search list of values
         Returns pdmListOfValues ( ListOfValues NXOp):  .
        """
        pass
    def NewPdmSearch() -> PdmSearch:
        """
         Creates a new pdm search 
         Returns tcinPdmSearch ( PdmSearch NXOp):  .
        """
        pass
    def NewPdmSearchresult() -> SearchResult:
        """
         Creates a new pdm search result 
         Returns pdmSearchResult ( SearchResult NXOp):  .
        """
        pass
    def NewPdmSoaquery() -> SoaQuery:
        """
         Creates a new pdm search soa query
         Returns pdmSoaQuery ( SoaQuery NXOp):  .
        """
        pass
import NXOpen
class PdmSearch(NXOpen.TransientObject): 
    """ Represents search query """
    def Advanced(self, entries: List[str], values: List[str]) -> SearchResult:
        """
         This API performs advanced search in the teamcenter and returns the result vector .Internally it will execute the NX standard Queries
                    "__NX_STD_ANY_ITEM_QUERY","__NX_STD_ANY_REV_QUERY" and "__NX_STD_ANY_DS_QUERY". Advanced search takes in detailed inputs to perform the search. 
                    The parameters "entries" and "values" are the internal property names and their values to be searched.
                    The attributevalue pairs are combined logically using AND so that only objects matching ALL of the specified
                    criteria are returned.
                    The method can only be used to search for matches on Teamcenter properties that are string valued.
                    It does not work for properties which are ObjectLOV valued.
                    For example "owning_user" is TC Object valued so the search does not find any matches when attempting to search on it.
                    
                    Please note, this functionality is available starting in Teamcenter 2007.1 MP2.
                    To see how to spell the "real" attribute names rather than the displayed attribute (column) names,
                    use Edit- Options...- General- UI- Sys Admin- Real Property Name in the Rich Client.
                    
                     
         Returns srchResVec ( SearchResult NXOp):  search result .
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def Simple(self, searchCriteria: str) -> SearchResult:
        """
         Perform simple search in the teamcenter and returns the result vector. 
                    Internally it will execute the NX standard Query "__NX_STD_SIMPLE_ITEM_QUERY". 
                    ItemId should be given as the searchCriteria for searching the items
                    
                    Please note,  this functionality is available starting in Teamcenter 2007.1 MP2.
                    
                    
         Returns srchResVec ( SearchResult NXOp):  search result .
        """
        pass
import NXOpen
import NXOpen.PDM.SaveManagement
class PdmSession(NXOpen.Object): 
    """ Represents the NX Manager session """
    class GetConfiguredRevisionInput:
        """
            Input struct to get configured revision of items.  
          
         PdmSessionGetConfiguredRevisionInput_Struct NXOp is an alias for  PdmSession.GetConfiguredRevisionInput NXOp.
        """
        @property
        def ItemId(self) -> str:
            """
            Getter for property ItemId
            item id

            """
            pass
        @ItemId.setter
        def ItemId(self, value: str):
            """
            Getter for property ItemId
            item id
            Setter for property ItemId
            item id

            """
            pass
        @property
        def RevisionRuleName(self) -> str:
            """
            Getter for property RevisionRuleName
            revision rule

            """
            pass
        @RevisionRuleName.setter
        def RevisionRuleName(self, value: str):
            """
            Getter for property RevisionRuleName
            revision rule
            Setter for property RevisionRuleName
            revision rule

            """
            pass
    class GetConfiguredRevisionResult:
        """
            Structure to return the result of get configured revisions of items.  
          
         PdmSessionGetConfiguredRevisionResult_Struct NXOp is an alias for  PdmSession.GetConfiguredRevisionResult NXOp.
        """
        @property
        def ItemId(self) -> str:
            """
            Getter for property ItemId
            item id

            """
            pass
        @ItemId.setter
        def ItemId(self, value: str):
            """
            Getter for property ItemId
            item id
            Setter for property ItemId
            item id

            """
            pass
        @property
        def RevisionRuleName(self) -> str:
            """
            Getter for property RevisionRuleName
            revision rule

            """
            pass
        @RevisionRuleName.setter
        def RevisionRuleName(self, value: str):
            """
            Getter for property RevisionRuleName
            revision rule
            Setter for property RevisionRuleName
            revision rule

            """
            pass
        @property
        def ItemRevisionCliSpec(self) -> str:
            """
            Getter for property ItemRevisionCliSpec
            configured item revision cli spec

            """
            pass
        @ItemRevisionCliSpec.setter
        def ItemRevisionCliSpec(self, value: str):
            """
            Getter for property ItemRevisionCliSpec
            configured item revision cli spec
            Setter for property ItemRevisionCliSpec
            configured item revision cli spec

            """
            pass
        @property
        def HasFailed(self) -> bool:
            """
            Getter for property HasFailed
            failed to fetch item revision using given revision rule

            """
            pass
        @HasFailed.setter
        def HasFailed(self, value: bool):
            """
            Getter for property HasFailed
            failed to fetch item revision using given revision rule
            Setter for property HasFailed
            failed to fetch item revision using given revision rule

            """
            pass
    @property
    def AttributeGroupDescriptions() -> AttributeGroupDescriptionCollection:
        """
         Returns a collection of  NXOpen::PDM::AttributeGroupDescription  objects representing
                    attribute group types.  The collection contains attribute group descriptions for
                     NXOpen::PDM::IAttributeGroupOwner  objects loaded within the NX session.
                    Use the  NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions 
                    to get the specific attribute group descriptions for an attribute group owner.  
        """
        pass
    @property
    def PartOperationImportObserver() -> PartOperationImportObserver:
        """
         Returns the  NXOpen::PDM::PartOperationImportObserver  belonging to this session 
        """
        pass
    @property
    def SaveObserver() -> NXOpen.PDM.SaveManagement.SaveObserver:
        """
         Returns the  NXOpen::PDM::SaveManagement::SaveObserver  belonging to this session 
        """
        pass
    @property
    def SaveAsReviseObserver() -> SaveAsReviseObserver:
        """
         Returns the  NXOpen::PDM::SaveAsReviseObserver  belonging to this session 
        """
        pass
    @property
    def TcinUtils() -> TcinUtils:
        """
         Returns the  NXOpen::PDM::TcinUtils  instance belonging to this session 
        """
        pass
    @property
    def PartNameGenerator() -> PartNameGenerator:
        """
         Returns the  NXOpen::PDM::PartNameGenerator  instance belonging to this session 
        """
        pass
    @property
    def PartAttributeAssignmentObserver() -> PartAttributeAssignmentObserver:
        """
         Returns the  NXOpen::PDM::PartAttributeAssignmentObserver  instance belonging to this session 
        """
        pass
    @property
    def PdmCopyOrEditOperationObserver() -> PdmCopyOrEditOperationObserver:
        """
         Returns the  NXOpen::PDM::PdmCopyOrEditOperationObserver  belonging to this session 
        """
        pass
    def AssignReleaseStatus(parts: List[NXOpen.TaggedObject], workflowName: str) -> OperationErrors:
        """
         Apply the given workflow on the given list of parts 
         Returns operationErrors ( OperationErrors NXOp):  Errors encountered .
        """
        pass
    def CreateCopyOperationBuilder(operation: PartOperationBuilder.OperationType) -> PartOperationCopyBuilder:
        """
        Returns a new NXOpen.PDM.PartOperationCopyBuilder object
         Returns builder ( PartOperationCopyBuilder NXOp): .
        """
        pass
    def CreateCreateOperationBuilder(operation: PartOperationBuilder.OperationType) -> PartOperationCreateBuilder:
        """
        Returns a new NXOpen.PDM.PartOperationCreateBuilder object
         Returns builder ( PartOperationCreateBuilder NXOp): .
        """
        pass
    def CreateCreateSessionBuilder(operation: PartOperationBuilder.OperationType) -> CreateSessionBuilder:
        """
        Returns a new NXOpen.PDM.CreateSessionBuilder object
         Returns builder ( CreateSessionBuilder NXOp): .
        """
        pass
    def CreateExportFromTeamcenterBuilderForConfiguredAssembly(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new NXOpen.PDM.ExportFromTeamcenter object which supports Selective Export of Configured Assembly.
         Returns builder ( ExportFromTeamcenter NXOp): .
        """
        pass
    def CreateExportFromTeamcenterBuilderForDesignWorkset(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new NXOpen.PDM.ExportFromTeamcenter object which supports Selective Export of Design Workset.
         Returns builder ( ExportFromTeamcenter NXOp): .
        """
        pass
    def CreateExportFromTeamcenterBuilderForPartFamily(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new NXOpen.PDM.ExportFromTeamcenter object
         Returns builder ( ExportFromTeamcenter NXOp): .
        """
        pass
    def CreateExportWorksetForReferenceBuilder(workset: NXOpen.BasePart) -> ExportWorksetForReferenceBuilder:
        """
         Creates a new NXOpen.PDM.ExportWorksetForReferenceBuilder object used for
                    exporting workset outside Teamcenter for reference. 
         Returns builder ( ExportWorksetForReferenceBuilder NXOp): .
        """
        pass
    def CreateExternalFileReferenceListBuilder(objects: List[NXOpen.NXObject]) -> ExternalFileReferenceListBuilder:
        """
         Creates a new NXOpen.PDM.ExternalFileReferenceListBuilder object. 
         Returns builder ( ExternalFileReferenceListBuilder NXOp): .
        """
        pass
    def CreateFolder(newFolderName: str, parentFolderName: str) -> None:
        """
         Create folder in Teamcenter with newFolderName under parentFolderName.
                
        """
        pass
    def CreateImportOperationBuilder() -> PartOperationImportBuilder:
        """
        Returns a new NXOpen.PDM.PartOperationImportBuilder object
         Returns builder ( PartOperationImportBuilder NXOp): .
        """
        pass
    def CreateMakeUniqueOperationBuilder(part: NXOpen.BasePart) -> PartOperationMakeUniqueBuilder:
        """
        Returns a new NXOpen.PDM.PartOperationMakeUniqueBuilder object
         Returns builder ( PartOperationMakeUniqueBuilder NXOp): .
        """
        pass
    def CreateObjectCreateBuilder(tcTypes: List[str], baseTCTypes: List[str]) -> ObjectCreateBuilder:
        """
        Returns a new NXOpen.PDM.ObjectCreateBuilder object
         Returns builder ( ObjectCreateBuilder NXOp): .
        """
        pass
    def CreateOperationBuilder(operation: PartOperationBuilder.OperationType) -> PartOperationBuilder:
        """
        Returns a new NXOpen.PDM.PartOperationBuilder object
         Returns builder ( PartOperationBuilder NXOp): .
        """
        pass
    def CreatePartOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> PartOperationAttributePropertiesBuilder:
        """
         Creates a new NXOpen.PDM.PartOperationAttributePropertiesBuilder object. 
         Returns builder ( PartOperationAttributePropertiesBuilder NXOp): .
        """
        pass
    def CreatePartOperationValidationPropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new AttributePropertiesBuilder object. 
         Returns builder ( NXOpen.AttributePropertiesBuilder): .
        """
        pass
    def CreatePdmCopyOrEditOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new AttributePropertiesBuilder object. 
         Returns builder ( NXOpen.AttributePropertiesBuilder): .
        """
        pass
    def CreatePdmCopyOrEditOperationBuilder() -> PdmCopyOrEditOperationBuilder:
        """
        Returns a new NXOpen.PDM.PdmCopyOrEditOperationBuilder object
         Returns builder ( PdmCopyOrEditOperationBuilder NXOp): .
        """
        pass
    def CreateSaveAsNewItemTypeBuilder() -> SaveAsNewItemTypeBuilder:
        """
        Returns a new NXOpen.PDM.SaveAsNewItemTypeBuilder object
         Returns builder ( SaveAsNewItemTypeBuilder NXOp): .
        """
        pass
    def CreateSearchRecipeFilterBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new NXOpen.PDM.SearchRecipeFilterBuilder object which supports Filtering of Design Workset. 
         Returns builder ( SearchRecipeFilterBuilder NXOp): .
        """
        pass
    def CreateSmartSaveBuilder(saveType: SmartSaveBuilder.SaveType) -> SmartSaveBuilder:
        """
         Creates a new SmartSaveBuilder object. 
         Returns builder ( SmartSaveBuilder NXOp): .
        """
        pass
    def CreateSmartSaveBuilderWithContext(smartSaveContext: SmartSaveContext) -> SmartSaveBuilder:
        """
         Creates a new SmartSaveBuilder object. 
         Returns builder ( SmartSaveBuilder NXOp): .
        """
        pass
    def CreateSmartSaveContext(saveType: SmartSaveBuilder.SaveType) -> SmartSaveContext:
        """
         Creates a new SmartSaveContext object. 
         Returns smartSaveContext ( SmartSaveContext NXOp): .
        """
        pass
    def CreateSmartSaveContextWithDialogType(dialogType: SmartSaveBuilder.DialogType, saveType: SmartSaveBuilder.SaveType) -> SmartSaveContext:
        """
         Creates a new SmartSaveContext object. 
         Returns smartSaveContext ( SmartSaveContext NXOp): .
        """
        pass
    def ExportFromTeamcenterCreate(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new NXOpen.PDM.ExportFromTeamcenter object
         Returns builder ( ExportFromTeamcenter NXOp): .
        """
        pass
    def GetCheckedoutStatusOfAllObjectsInSession() -> Tuple[List[NXOpen.NXObject], List[NXOpen.NXObject]]:
        """
                   Returns the checkedout status (checkedoutnon checkedout) of all the objects open in NX.
                
         Returns A tuple consisting of (checkedOutObjects, uncheckedOutObjects). 
         - checkedOutObjects is:  NXOpen.NXObject Li. Array of NXObjects which are open in session and checked out .
         - uncheckedOutObjects is:  NXOpen.NXObject Li. Array of NXObjects which are open in session but not checkout .

        """
        pass
    def GetConfiguredRevisionOfItems(itemInputs: List[PdmSession.GetConfiguredRevisionInput]) -> Tuple[OperationErrors, List[PdmSession.GetConfiguredRevisionResult]]:
        """
         Get the configured item revisions on the provided item using given revision rule. 
         Returns A tuple consisting of (operationErrors, configuredItemRevisionResult). 
         - operationErrors is:  OperationErrors NXOp. Errors encountered .
         - configuredItemRevisionResult is:  PdmSession.GetConfiguredRevisionResult List[NX. Item Revision clis .

        """
        pass
    def GetDatabaseObjectManager() -> DatabaseObjectManager:
        """
         Gets the NXOpen.PDM.DatabaseObjectManager object. 
         Returns databaseObjectManager ( DatabaseObjectManager NXOp): .
        """
        pass
    def GetItemTypes() -> List[str]:
        """
         Returns array of all available Teamcenter Item Types
                
         Returns tcItemsTypes (List[str]): .
        """
        pass
    def GetNXWorkflows(parts: List[NXOpen.TaggedObject]) -> Tuple[OperationErrors, List[str]]:
        """
         Get the NX workflows from Teamcenter for the given list of parts 
         Returns A tuple consisting of (operationErrors, workflowNames). 
         - operationErrors is:  OperationErrors NXOp. Errors encountered .
         - workflowNames is: List[str]. the array of workflow names .

        """
        pass
    def GetSsoSettings() -> Tuple[bool, str, str]:
        """
          Returns the SSO credentials, if SSO is available 
                     The client applications can use these settings to connect to the same Tcserver that NX
                     is using.
                
         Returns A tuple consisting of (isSsoEnabled, ssoServerUrl, ssoAppID). 
         - isSsoEnabled is: bool. if SSO is enabled .
         - ssoServerUrl is: str. the SSO server URL .
         - ssoAppID is: str. the SSO app id .

        """
        pass
    def GetTcserverSettings() -> Tuple[str, str]:
        """
          Returns the connect string and discriminator used by NX session to connect to the Tcserver.
                     The client applications can use these settings to connect to the same Tcserver that NX
                     is using.
                     
                     Tcserver connect string: The connect string is path of the server hosting the services.
                     The connect string for the different transport protocols will be in the following form:
                     4-Tier(HTTP mode): similar to "http:
                     2-Tier(IIOP mode): The Tcserver IOR string; e.g corbaloc:iiop:localhost:PORTNOlocalserver
                     2-tier(TCTP mode): the TCTP connect string; e.g "tctp:
                     
                     Discriminator: The discriminator is a unique identifier and contains unique information related 
                     to a given TC server. This unique identifier (discriminator) is recognized by TC pool manager as
                     the session number that ties the server process to the client. The discriminator functionality 
                     is part of the SOA package. The discriminator allows multiple clients to connect to the same TC server.
                     In 2-Tier(IIOP or TCTP mode), the discriminator will be an empty string.
                     To connect to the same Tcserver as NX, the client can create a Teamcenter::Soa::Client::Connection 
                     object using the connect string and then use the Teamcenter::Services::Core::SessionService to login
                     to Teamcenter Server with the discriminator and the connection object. More information about
                     connecting to the Teamcenter server can be found in the TC SOA API Documentation.
                
         Returns A tuple consisting of (connectString, discriminator). 
         - connectString is: str. the connection string .
         - discriminator is: str. the discriminator .

        """
        pass
    def GetUserGroup() -> str:
        """
         Gets the Teamcenter user group for the current user
                
         Returns userGroup (str): .
        """
        pass
    def GetUserName() -> str:
        """
         Gets the Teamcenter user name for the current user
                
         Returns userName (str): .
        """
        pass
    def GetUserRole() -> str:
        """
         Gets the Teamcenter role for the current user
                
         Returns userRole (str): .
        """
        pass
    def NewCaeFileContainer() -> CAEFileContainer:
        """
         Returns a new NXOpen.PDM.CAEFileContainer object 
         Returns upload ( CAEFileContainer NXOp): .
        """
        pass
    def NewFileManagement() -> FileManagement:
        """
         Returns a new NXOpen.PDM.FileManagement object 
         Returns fileManagement ( FileManagement NXOp): .
        """
        pass
    def SetActiveEngineeringChangeNotice(part: NXOpen.NXObject, ecnMFKId: str, ecnRevsionId: str) -> None:
        """
         Sets active Engineering Change Notice (ECN) for the session.
                    All objects created will be added to solution items of this Engineering Change Notice.
                    The input will be in the format of Change Notice MFK ID and Change Notice Revision ID.
                    Note: Please make sure to set it at the start of the NXOpen program, before object creation.
                
        """
        pass
    def SetDefaultFolder(default_folder_spec: str) -> None:
        """
         Sets default folder.
                The input default folder path in format &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, where username is optional.
                In that case, in :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container
                
        """
        pass
    def SetNativeMode(enable: bool, rereadTemplateInformation: bool) -> None:
        """
         Sets or unsets native mode for the session based on the value of input.
                
        """
        pass
    def SetRevisionRule(setDefault: bool, revisionRule: str) -> None:
        """
         Set the revision rule 
        """
        pass
class PdmSoaqueryNxmgrfielddatatype(Enum):
    """
    Members Include: 
     |Char|  Char type 
     |Date|  Date 
     |Double|  Double 
     |Float|  Float 
     |Int|  Integer 
     |Bool|  Boolean 
     |Short|  Short 
     |String|  String 
     |Reference|  Reference 
     |UntypedReference|  Untyped reference 
     |ExternalReference|  External reference 

    """
    Char: int
    Date: int
    Double: int
    Float: int
    Int: int
    Bool: int
    Short: int
    String: int
    Reference: int
    UntypedReference: int
    ExternalReference: int
    @staticmethod
    def ValueOf(value: int) -> PdmSoaqueryNxmgrfielddatatype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Assemblies
class PendingComponentsManager(NXOpen.TransientObject): 
    """ This class is used for managing a part's pending components, that
        is, those that have been added within Teamcenter but are not yet
        present in NX. An instance of this class for a particular part can
        be created by calling PDM.PartManager.NewPendingComponentsManager.
    """
    def AddComponent(self, handle: str) -> Tuple[NXOpen.Assemblies.Component, NXOpen.PartLoadStatus]:
        """
         Adds a pending component. 
         Returns A tuple consisting of (component, load_status). 
         - component is:  NXOpen.Assemblies.Component.
         - load_status is:  NXOpen.PartLoadStatus. result of loading the component part .

        """
        pass
    def AddNgcComponent(self, handle: str) -> Tuple[NXOpen.Assemblies.Component, NXOpen.PartLoadStatus]:
        """
         Adds a pending NGC component. 
         Returns A tuple consisting of (component, load_status). 
         - component is:  NXOpen.Assemblies.Component.
         - load_status is:  NXOpen.PartLoadStatus. result of loading the ngc component part .

        """
        pass
    def ComponentHasPosition(self, handle: str) -> bool:
        """
         Determines whether a given pending component has been positioned
                    by Teamcenter. If PDM.PendingComponentsManager.AddComponent
                    is called regarding a component without a position, it will automatically
                    be positioned at the origin.
                
         Returns has_position (bool): .
        """
        pass
    def DeleteComponent(self, handle: str) -> None:
        """
         Deletes a pending component. 
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
        """
        pass
    def GetComponentPartFileName(self, handle: str) -> str:
        """
         Gets the NX Manager file name for the part corresponding to
                    a pending component.
                
         Returns file_name (str): .
        """
        pass
    def GetComponents(self) -> List[str]:
        """
         Gets "handles" for the pending components of the part associated
                    with this object.
                
         Returns components (List[str]): .
        """
        pass
import NXOpen
class PersistentSettings(NXOpen.TransientObject): 
    """ Persistently held settings for a Teamcenter user account. Any changes will only
        take effect when PDM.PersistentSettings.Apply is callsed. """
    @property
    def Group(self) -> str:
        """
        Getter for property: (str) Group
         Returns the Teamcenter group in which the user acts by default.  
           Should be
                    one of those given by  PDM::PersistentSettings::GetGroups 
                   
         
        """
        pass
    @Group.setter
    def Group(self, group: str):
        """
        Setter for property: (str) Group
         Returns the Teamcenter group in which the user acts by default.  
           Should be
                    one of those given by  PDM::PersistentSettings::GetGroups 
                   
         
        """
        pass
    @property
    def Volume(self) -> str:
        """
        Getter for property: (str) Volume
         Returns the Teamcenter volume to which the user used by default.  
           Should be
                    one of those given by  PDM::PersistentSettings::GetVolumes    
         
        """
        pass
    @Volume.setter
    def Volume(self, volume: str):
        """
        Setter for property: (str) Volume
         Returns the Teamcenter volume to which the user used by default.  
           Should be
                    one of those given by  PDM::PersistentSettings::GetVolumes    
         
        """
        pass
    def Apply(self) -> None:
        """
         Applies any changes to the settings 
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
        """
        pass
    def GetGroups(self) -> List[str]:
        """
         Gets the names of the Teamcenter groups to which the
                    user belongs. 
                
         Returns groups (List[str]):  the names of the groups .
        """
        pass
    def GetVolumes(self) -> List[str]:
        """
         Gets the names of the Teamcenter volumes which the
                    user may use, given the current group returned by PDM.PersistentSettings.GetGroups.
                
         Returns volumes (List[str]):  the names of the volumes .
        """
        pass
import NXOpen
class PortArtifact(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for port artifact in a NXOpen.PDM.LogicalElementRevision.
    """
    pass
import NXOpen
class PredefinedVolumeObject(NXOpen.NXObject): 
    """ 
        Represents a predefined volume object and this maps to PDM::PredefinedVolumeObject
    """
    def GetVolumeName(self) -> str:
        """
         Returns a name representing this NXOpen.PDM.PredefinedVolumeObject.
                
         Returns volumeName (str): .
        """
        pass
import NXOpen
class PredefinedVolumeSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create volume search filter term.
     Such filter terms can be used to provide filtering.
    """
    def AddVolume(self, volume: NXOpen.NXObject) -> None:
        """
         This function adds the predefined volume to volume term. 
        """
        pass
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse volume term or not. 
         Returns excludeToggle (bool): .
        """
        pass
    def GetOperator(self) -> VolumeSearchFilterTerm.Operator:
        """
         This function gets the volume operator from volume term. 
         Returns volumeOperator ( VolumeSearchFilterTerm.Operator NXOp): .
        """
        pass
    def GetVolumes(self) -> List[NXOpen.NXObject]:
        """
         This function gets the already added predefined volumes from volume term. 
         Returns volumes ( NXOpen.NXObject Li): .
        """
        pass
    def RemoveVolume(self, volume: NXOpen.NXObject) -> None:
        """
         This function removes the predefined volume from volume term. 
        """
        pass
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse volume term or not. 
        """
        pass
    def SetOperator(self, volumeOperator: VolumeSearchFilterTerm.Operator) -> None:
        """
         This function sets the volume operator to volume term. 
        """
        pass
import NXOpen
class ProximitySearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create proximity search filter term.
     Such filter terms can be used to provide filtering.
    """
    def GetDistance(self) -> Tuple[float, NXOpen.Unit]:
        """
         This function gets the distance and it's unit from proximity term. 
         Returns A tuple consisting of (distance, unitType). 
         - distance is: float.
         - unitType is:  NXOpen.Unit.

        """
        pass
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse proximity term or not. 
         Returns excludeToggle (bool): .
        """
        pass
    def GetTargets(self) -> List[NXOpen.NXObject]:
        """
         This function gets the targets from proximity term. 
         Returns targets ( NXOpen.NXObject Li): .
        """
        pass
    def SetDistance(self, distance: float, unitType: NXOpen.Unit) -> None:
        """
         This function sets the distance and it's unit to proximity term. 
        """
        pass
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse proximity term or not. 
        """
        pass
    def SetTargets(self, targets: List[NXOpen.NXObject]) -> None:
        """
         This function sets the targets to proximity term. 
        """
        pass
import NXOpen
class RequirementUtils(NXOpen.Object): 
    """ Collection of PDM utility methods """
    def CreateTraceLinks(requirement_item_numbers: List[str], requirement_revisions: List[str], parts: List[str]) -> None:
        """
         Creates Trace Links from NXOpen.Validate.Requirements to NXOpen.Parts
                For the input requirement_item_numbers:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
        """
        pass
    def NewTracelinkQuery() -> TracelinkQuery:
        """
         Returns a Tracelink query object 
         Returns tracelink_query ( TracelinkQuery NXOp):   .
        """
        pass
    def RemoveTraceLinks(requirement_item_numbers: List[str], requirement_revisions: List[str], parts: List[str]) -> None:
        """
         Removes Trace Links between NXOpen.Validate.Requirements and NXOpen.Parts
                For the input requirement_item_numbers:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
        """
        pass
class SaveAsNewItemTypeBuilder(PdmCopyOrEditOperationBuilder): 
    """ Represents a builder class that performs save as new item type operation """
    @property
    def DependentFilesToCopyOption(self) -> int:
        """
        Getter for property: (int) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
            
         
        """
        pass
    @DependentFilesToCopyOption.setter
    def DependentFilesToCopyOption(self, saveAsOption: int):
        """
        Setter for property: (int) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
            
         
        """
        pass
    def AddSelectedParts(self, parts: List[str]) -> List[str]:
        """
         Adds the selected parts.
         Returns errorMsgs (List[str]): .
        """
        pass
    def CreateOrUpdateSaveAsNewItemTypeOperationObjects(self, doUpdate: bool) -> List[PdmCopyOrEditOperationObject]:
        """
         This function createsupdates the operation objects for the participating parts.
                Note: The operation object needs to be updated in certain cases, e.g. after the item type is changed.
                
         Returns copyOperationObjects ( PdmCopyOrEditOperationObject List[NX): .
        """
        pass
    def SetChangeNotice(self, ecnCliSpec: str) -> None:
        """
         Sets the Engineering Change Notice for the parts undergoing save-as new item type operation
        """
        pass
    def SetItemType(self, itemType: str) -> None:
        """
         Sets the selected Item Type 
        """
        pass
import NXOpen
class SaveAsReviseCallbackData(NXOpen.TaggedObject): 
    """ JA interface for SaveAsReviseCallbackData object """
    def GetCopiedObjects(self, sourceObjects: NXOpen.TaggedObject) -> List[NXOpen.TaggedObject]:
        """
         Gets the source objects tags along with copied objects tags after saveas or revise operation 
         Returns copiedObjects ( NXOpen.TaggedObject Li):  array of copied objects to be saveas or revise .
        """
        pass
    def GetSourceObjects(self) -> Tuple[int, List[NXOpen.TaggedObject]]:
        """
         Gets the source objects tags participating in saveas or revise operation 
         Returns A tuple consisting of (nObjects, sourceObjects). 
         - nObjects is: int. get number of source objects going for SaveAs or Revise .
         - sourceObjects is:  NXOpen.TaggedObject Li. array of source objects to be saveas or revise .

        """
        pass
import NXOpen
class SaveAsReviseObserver(NXOpen.TaggedObjectCollection): 
    """ This class is responsible for invoking registered callback when objects goes for SaveAs and Revise and after the process. """
    PostcopyoperationCb = Callable[[SaveAsReviseCallbackData], None]
    def AddPostcopyoperationCallback(postcopyoperation_cb: SaveAsReviseObserver.PostcopyoperationCb) -> int:
        """
         Registers a user defined postcopyoperation callback that is called just before SaveAs and Revise process 
         Returns id (int):  identifier of registered method (used to deregister the method) .
        """
        pass
    PrecopyoperationCb = Callable[[SaveAsReviseCallbackData], None]
    def AddPrecopyoperationCallback(precopyoperation_cb: SaveAsReviseObserver.PrecopyoperationCb) -> int:
        """
         Registers a user defined precopyoperation callback that is called just before SaveAs and Revise process 
         Returns id (int):  identifier of registered method (used to deregister the method) .
        """
        pass
    def RemovePostcopyoperationCallback(id: int) -> None:
        """
         Deregister the user defined postcopyoperation callback 
        """
        pass
    def RemovePrecopyoperationCallback(id: int) -> None:
        """
         Deregister the user defined precopyoperation callback 
        """
        pass
import NXOpen
class SearchFilterTerm(NXOpen.NXObject): 
    """ This is search filter term which can be used to create recipe filter.
       Collections of such filter terms will be used provide filtering.
    """
    class Type(Enum):
        """
        Members Include: 
         |Proximity| 
         |Volume| 
         |Invalid| 
         |Partition| 
         |Attribute| 

        """
        Proximity: int
        Volume: int
        Invalid: int
        Partition: int
        Attribute: int
        @staticmethod
        def ValueOf(value: int) -> SearchFilterTerm.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetTermType(self) -> SearchFilterTerm.Type:
        """
         This function returns type of search filter term. 
         Returns type ( SearchFilterTerm.Type NXOp): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SearchRecipeFilterBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs search filtering """
    class RecipeLogicValue(Enum):
        """
        Members Include: 
         |Include| 
         |Exclude| 

        """
        Include: int
        Exclude: int
        @staticmethod
        def ValueOf(value: int) -> SearchRecipeFilterBuilder.RecipeLogicValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VolumeTypeValue(Enum):
        """
        Members Include: 
         |Reference| 
         |PreDefined| 
         |New| 

        """
        Reference: int
        PreDefined: int
        New: int
        @staticmethod
        def ValueOf(value: int) -> SearchRecipeFilterBuilder.VolumeTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateAttributeTerm(self, objectType: str, operatorValue: str, internalTitle: str, displayTitle: str, doExclude: bool) -> AttributeSearchFilterTerm:
        """
         This function creates the attribute type search filter term based on the provided attribute values. 
         Returns createdTerm ( AttributeSearchFilterTerm NXOp): .
        """
        pass
    def CreatePartitionTerm(self, partitionScheme: NXOpen.Assemblies.PartitionScheme, partition: List[NXOpen.Assemblies.Partition], includeChildrenPartition: bool, doExclude: bool) -> PartitionSearchFilterTerm:
        """
         This function creates the partition type search filter term based on the provided partitions.
                    All the provided partitions are expected to be of same partition scheme. 
         Returns createdTerm ( PartitionSearchFilterTerm NXOp): .
        """
        pass
    def CreatePredefinedVolumeTerm(self, volumes: List[NXOpen.NXObject], volumeOperator: VolumeSearchFilterTerm.Operator, doExclude: bool) -> PredefinedVolumeSearchFilterTerm:
        """
         This function creates the volume type search filter term based on the predefined volumes. 
         Returns createdTerm ( PredefinedVolumeSearchFilterTerm NXOp): .
        """
        pass
    def CreateProximityTerm(self, targets: List[NXOpen.NXObject], distance: float, unitType: NXOpen.Unit, doExclude: bool) -> ProximitySearchFilterTerm:
        """
         This function creates the proximity type search filter term based on the provided values. 
         Returns createdTerm ( ProximitySearchFilterTerm NXOp): .
        """
        pass
    def CreateVolumeTerm(self, boundingBoxes: List[VolumeSearchFilterTerm.BoundingBox], boxZoneOperator: VolumeSearchFilterTerm.Operator, doExclude: bool) -> VolumeSearchFilterTerm:
        """
         This function creates the volume type search filter term based on the provided values. 
         Returns createdTerm ( VolumeSearchFilterTerm NXOp): .
        """
        pass
    def CreateVolumeTermFromSelectedObjects(self, selectedObjects: List[NXOpen.NXObject], volumeOperator: VolumeSearchFilterTerm.Operator, doExclude: bool) -> SelectedVolumeSearchFilterTerm:
        """
         This function creates the volume type search filter term based on the provided objects. 
         Returns createdTerm ( SelectedVolumeSearchFilterTerm NXOp): .
        """
        pass
    def DeleteSearchFilterTerm(self, termToDelete: SearchFilterTerm) -> None:
        """
         This function deletes the provided search filter term. 
        """
        pass
    def GetPredefinedVolumes(self) -> List[NXOpen.NXObject]:
        """
         This function gets all the predefined volumes. 
         Returns predefinedVolumes ( NXOpen.NXObject Li): .
        """
        pass
    def GetSearchFilterTerms(self) -> List[SearchFilterTerm]:
        """
         This function gets all the search filter terms.
                    It includes already created search terms which are based on existing filter of ProductSubset.
                    It also includes search terms created using "CreateProximityTerm" and "CreateVolumeTerm". 
         Returns terms ( SearchFilterTerm List[NX): .
        """
        pass
    def LoadPartitions(self) -> None:
        """
         This function loads all the partitions from every partition schemes available on server. 
        """
        pass
    def LoadPredefinedVolumes(self) -> None:
        """
         This function loads all the predefined volumes from server. 
        """
        pass
import NXOpen
class SearchResult(NXOpen.TransientObject): 
    """ Represents search query """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetResultItemIds(self) -> List[str]:
        """
         Gets a list of the item_ids from the search result. If Multifield Key environment is enabled, 
                then use Multifield key function PDM.SearchResult.GetResultMfkIds, as 
                this function may return us duplicate item ids if the corresponding parts belong to different domains. 
         Returns itemIds (List[str]):  array of item_ids .
        """
        pass
    def GetResultMfkIds(self) -> List[str]:
        """
         Gets a list of the Multifield Keys from the search results. If Multifield Key
                environment is enabled then always use this function 
                Multifield Key: e.g. %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x 
         Returns mfkIds (List[str]):  array of mfk_ids .
        """
        pass
    def GetResultObjectNames(self) -> List[str]:
        """
         Gets a list of the object names from the search result 
         Returns objectNames (List[str]):  array of object names .
        """
        pass
    def GetResultObjectTypes(self) -> List[str]:
        """
         Gets a list of the object types from the search result 
         Returns objectTypes (List[str]):  array of object types .
        """
        pass
import NXOpen
class SelectedVolumeSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create volume search filter term using objects.
     Such filter terms can be used to provide filtering.
    """
    def GetBoundingBox(self) -> VolumeSearchFilterTerm.BoundingBox:
        """
         This function gets the bounding boxes from volume term. 
         Returns boundingBox ( VolumeSearchFilterTerm.BoundingBox NXOp): .
        """
        pass
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse volume term or not. 
         Returns excludeToggle (bool): .
        """
        pass
    def GetOperator(self) -> VolumeSearchFilterTerm.Operator:
        """
         This function gets the bounding box operator from volume term. 
         Returns volumeOperator ( VolumeSearchFilterTerm.Operator NXOp): .
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.NXObject]:
        """
         This function gets the selected objects from volume term. 
         Returns selectedObjects ( NXOpen.NXObject Li): .
        """
        pass
    def SetBoundingBox(self, boundingBox: VolumeSearchFilterTerm.BoundingBox) -> None:
        """
         This function sets the bounding boxes to volume term. It will overwrite bounding box computed earlier from selected objects. 
        """
        pass
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse volume term or not. 
        """
        pass
    def SetOperator(self, volumeOperator: VolumeSearchFilterTerm.Operator) -> None:
        """
         This function sets the bounding box operator to volume term. 
        """
        pass
    def SetSelectedObjects(self, selectedObjects: List[NXOpen.NXObject]) -> None:
        """
         This function sets the selected object to volume term. It also recomputes bounding box based on provided objects. 
        """
        pass
import NXOpen
class SessionSettings(NXOpen.TransientObject): 
    """ To obtain an instance of this class, refer to NXOpen.Session.NewDatabaseSessionOptions 
        Values for the settings that affect the current Teamcenter session. Any changes will only
        take effect when PDM.SessionSettings.Apply is callsed. """
    @property
    def AdministrationBypass(self) -> bool:
        """
        Getter for property: (bool) AdministrationBypass
         Returns a flag controlling the Teamcenter administrator's bypass option.  
           Only available to administrators.   
         
        """
        pass
    @AdministrationBypass.setter
    def AdministrationBypass(self, admin_bypass_on: bool):
        """
        Setter for property: (bool) AdministrationBypass
         Returns a flag controlling the Teamcenter administrator's bypass option.  
           Only available to administrators.   
         
        """
        pass
    @property
    def AdministrationLogging(self) -> bool:
        """
        Getter for property: (bool) AdministrationLogging
         Returns a flag controlling Teamcenter administration logging.  
           Only available to administrators.   
         
        """
        pass
    @AdministrationLogging.setter
    def AdministrationLogging(self, admin_logging_on: bool):
        """
        Setter for property: (bool) AdministrationLogging
         Returns a flag controlling Teamcenter administration logging.  
           Only available to administrators.   
         
        """
        pass
    @property
    def ApplicationLogging(self) -> bool:
        """
        Getter for property: (bool) ApplicationLogging
         Returns a flag controlling Teamcenter application logging   
            
         
        """
        pass
    @ApplicationLogging.setter
    def ApplicationLogging(self, app_logging_on: bool):
        """
        Setter for property: (bool) ApplicationLogging
         Returns a flag controlling Teamcenter application logging   
            
         
        """
        pass
    @property
    def Group(self) -> str:
        """
        Getter for property: (str) Group
         Returns the Teamcenter group in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetGroups 
                   
         
        """
        pass
    @Group.setter
    def Group(self, group: str):
        """
        Setter for property: (str) Group
         Returns the Teamcenter group in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetGroups 
                   
         
        """
        pass
    @property
    def IsAdministrator(self) -> bool:
        """
        Getter for property: (bool) IsAdministrator
         Returns a flag indicating if the user has Teamcenter administator privileges.  
           Some
                    settings can are only available to administrators, and will raise errors
                    if non-administrators try to access them.
                  
         
        """
        pass
    @property
    def Journaling(self) -> bool:
        """
        Getter for property: (bool) Journaling
         Returns a flag controlling Teamcenter journaling   
            
         
        """
        pass
    @Journaling.setter
    def Journaling(self, journaling_on: bool):
        """
        Setter for property: (bool) Journaling
         Returns a flag controlling Teamcenter journaling   
            
         
        """
        pass
    @property
    def LocalVolume(self) -> str:
        """
        Getter for property: (str) LocalVolume
         Returns the Teamcenter local volume.  
           Should be
                    one of those given by  PDM::SessionSettings::GetLocalVolumes 
                   
         
        """
        pass
    @LocalVolume.setter
    def LocalVolume(self, localVolume: str):
        """
        Setter for property: (str) LocalVolume
         Returns the Teamcenter local volume.  
           Should be
                    one of those given by  PDM::SessionSettings::GetLocalVolumes 
                   
         
        """
        pass
    @property
    def LocationCode(self) -> str:
        """
        Getter for property: (str) LocationCode
         Returns the Teamcenter location code.  
           Should be
                    one of those given by  PDM::SessionSettings::GetLocationCodes 
                   
         
        """
        pass
    @LocationCode.setter
    def LocationCode(self, locationCode: str):
        """
        Setter for property: (str) LocationCode
         Returns the Teamcenter location code.  
           Should be
                    one of those given by  PDM::SessionSettings::GetLocationCodes 
                   
         
        """
        pass
    @property
    def Project(self) -> str:
        """
        Getter for property: (str) Project
         Returns the Teamcenter project in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetProjects 
                   
         
        """
        pass
    @Project.setter
    def Project(self, project: str):
        """
        Setter for property: (str) Project
         Returns the Teamcenter project in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetProjects 
                   
         
        """
        pass
    @property
    def Role(self) -> str:
        """
        Getter for property: (str) Role
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetRoles 
                   
         
        """
        pass
    @Role.setter
    def Role(self, role: str):
        """
        Setter for property: (str) Role
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetRoles 
                   
         
        """
        pass
    @property
    def SecurityLogging(self) -> bool:
        """
        Getter for property: (bool) SecurityLogging
         Returns a flag controlling Teamcenter security logging.  
           Only available to administrators.   
         
        """
        pass
    @SecurityLogging.setter
    def SecurityLogging(self, security_logging_on: bool):
        """
        Setter for property: (bool) SecurityLogging
         Returns a flag controlling Teamcenter security logging.  
           Only available to administrators.   
         
        """
        pass
    @property
    def Volume(self) -> str:
        """
        Getter for property: (str) Volume
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetVolumes 
                   
         
        """
        pass
    @Volume.setter
    def Volume(self, volume: str):
        """
        Setter for property: (str) Volume
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by  PDM::SessionSettings::GetVolumes 
                   
         
        """
        pass
    def Apply(self) -> None:
        """
         Applies any changes to the settings 
        """
        pass
    def ApplyAndRefresh(self) -> None:
        """
         Applies any changes to the session settings and reloads the data model as per the new group and role (if changed). 
                    The following settings are reloaded in this operation:
                    1. Reload Templates 
                    2. Reload Teamcenter preferences 
                    3. Refresh Teamcenter Type customizations
                    
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
        """
        pass
    def DumpValidationInfo(self, log_file_name: str) -> None:
        """
         Dump the validation info .This API can be used to expose the current state from the 
                    UGMGR session, typically the information about the session,assembly,components,their states
                    etc. 
        """
        pass
    def GetGroups(self) -> List[str]:
        """
         Gets the names of the Teamcenter groups to which the
                    user belongs. 
                
         Returns groups (List[str]):  the names of the groups .
        """
        pass
    def GetLocalVolumes(self) -> List[str]:
        """
         Gets the names of the Teamcenter local volumes which the user may use,
                   given the current group returned by PDM.SessionSettings.Group.
                
         Returns localVolumes (List[str]):  the names of the local volumes .
        """
        pass
    def GetLocationCodes(self) -> List[str]:
        """
         Gets the names of the Teamcenter location codes which the user may use, 
                    given the current group returned by PDM.SessionSettings.Group.
                
         Returns locationCodes (List[str]):  the names of the location codes .
        """
        pass
    def GetProjects(self) -> List[str]:
        """
         Gets the names of the Teamcenter projects to which the user belongs also
                    the first entry of the returned projects list is always empty.
                
         Returns projects (List[str]):  the names of the projects .
        """
        pass
    def GetRoles(self) -> List[str]:
        """
         Gets the names of the Teamcenter roles in which the
                    user may act, given the current group returned by PDM.SessionSettings.Group.
                
         Returns roles (List[str]):  the names of the roles .
        """
        pass
    def GetVolumes(self) -> List[str]:
        """
         Gets the names of the Teamcenter volumes which the
                    user may use, given the current group returned by PDM.SessionSettings.Group.
                
         Returns volumes (List[str]):  the names of the volumes .
        """
        pass
class SheetRevision(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a NXOpen.CollaborativeDesign.
    """
    pass
import NXOpen
class SmartSaveBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Save Management operations.
        This can be used to query or update smart save objects  that participate in the save management operations.
        Every smart save object represents NX object that is undergoing save operation."""
    class DialogType(Enum):
        """
        Members Include: 
         |Save| 
         |StageModelSaveAs|  For Stage Model Save As operation 
         |DesignSessionSaveAs|  For Design Session Save As 

        """
        Save: int
        StageModelSaveAs: int
        DesignSessionSaveAs: int
        @staticmethod
        def ValueOf(value: int) -> SmartSaveBuilder.DialogType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveType(Enum):
        """
        Members Include: 
         |Save|  File Save 
         |SaveAll|  File SaveAll 
         |SavePreciseAssembly|  File SavePreciseAssembly 
         |SaveWorkPartOnly|  File SaveWorkPartOnly 
         |SaveAndClose|  File Save And Close 
         |SaveDesignElements|  Save Design Elements 
         |ForceSaveAll|  File ForceSaveAll 

        """
        Save: int
        SaveAll: int
        SavePreciseAssembly: int
        SaveWorkPartOnly: int
        SaveAndClose: int
        SaveDesignElements: int
        ForceSaveAll: int
        @staticmethod
        def ValueOf(value: int) -> SmartSaveBuilder.SaveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DebugDumpEnabled(self) -> bool:
        """
        Getter for property: (bool) DebugDumpEnabled
         Returns the debug dump enabled   
            
         
        """
        pass
    @DebugDumpEnabled.setter
    def DebugDumpEnabled(self, debugDumpEnabled: bool):
        """
        Setter for property: (bool) DebugDumpEnabled
         Returns the debug dump enabled   
            
         
        """
        pass
    @property
    def UseNewSortForDebug(self) -> bool:
        """
        Getter for property: (bool) UseNewSortForDebug
         Returns the new debug sort enabled   
            
         
        """
        pass
    @UseNewSortForDebug.setter
    def UseNewSortForDebug(self, useNewSortForDebug: bool):
        """
        Setter for property: (bool) UseNewSortForDebug
         Returns the new debug sort enabled   
            
         
        """
        pass
    def AddRelatedDrawingsAndSetValidForSave(self) -> bool:
        """
        Adds the modified related drawing non-master smart save objects and sets them valid for Save operation
         Returns foundDependentPartsForSave (bool): .
        """
        pass
    def AssignRemoveProjects(self, smartSaveObjects: List[SmartSaveObject], project_names: List[str], assignment_states: List[NXOpen.Session.ProjectAssignmentState]) -> None:
        """
          Assign or remove projects tofrom objects
        """
        pass
    def CanPerformDefaultSave(self) -> bool:
        """
         Checks whether smart save operation can be performed with default operation type set 
         Returns canPerformDefaultSave (bool): .
        """
        pass
    def ClearValidationFailures(self) -> None:
        """
         Clears operation failures if any 
        """
        pass
    def CreateSpecificationsForSmartSaveObjects(self, smartSaveObjects: List[SmartSaveObject]) -> None:
        """
         Create new specifications for Logical Objects 
        """
        pass
    def GetAlternateIDManager(self, logicalObject: LogicalObject) -> AlternateIdManager:
        """
         Create an instance of a NXOpen.PDM.AlternateIdManager which will be used to create alternate ID information while creating the new part.
         Returns alternateIDManager ( AlternateIdManager NXOp): .
        """
        pass
    def GetAssociatedChangeNoticeNames(self, smartSaveObjects: List[SmartSaveObject]) -> List[str]:
        """
          Gets CLI names of Change Notice associated with Objects involved in Save operation 
         Returns changeNoticeNames (List[str]): .
        """
        pass
    def GetErrorMessageHandler(self, refresh: bool) -> ErrorMessageHandler:
        """
         Returns ErrorMessageHandler 
         Returns errorMessageHandler ( ErrorMessageHandler NXOp): .
        """
        pass
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns operation failures 
         Returns operationFailures ( NXOpen.ErrorList): .
        """
        pass
    def GetSmartSaveObjects(self) -> List[SmartSaveObject]:
        """
         Gets the smart save objects for the modified objects in session. 
         Returns smartSaveObjects ( SmartSaveObject List[NX): .
        """
        pass
    def OnOperationTypeChanged(self, smartSaveObjects: List[SmartSaveObject], operationType: NXOpen.AttributePropertiesBuilder.OperationType) -> None:
        """
         Updates the given smart save objects after operation type change. 
        """
        pass
    def UpdateSmartSaveObjectsOnBuilder(self) -> None:
        """
         Updates the smart save objects with valid operation type and dependencies 
        """
        pass
    def ValidateSmartSaveObjects(self) -> None:
        """
         Validates whether the save operation can be performed on the smart save objects 
        """
        pass
import NXOpen
class SmartSaveContext(NXOpen.TransientObject): 
    """ Represents smart save context """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetSaveType(self) -> SmartSaveBuilder.SaveType:
        """
         Returns the save operation type 
         Returns saveType ( SmartSaveBuilder.SaveType NXOp):   .
        """
        pass
    def GetWorkObjectToRootObjectMap(self) -> Tuple[List[NXOpen.TaggedObject], List[NXOpen.TaggedObject]]:
        """
         Returns the set of work object to root object pairs from the context 
         Returns A tuple consisting of (workObjects, rootObjects). 
         - workObjects is:  NXOpen.TaggedObject Li. array of work objects to be saved .
         - rootObjects is:  NXOpen.TaggedObject Li. array of root objects  .

        """
        pass
    def SetWorkObjectToRootObjectMap(self, workObjects: List[NXOpen.TaggedObject], rootObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Adds the given set of work object to root object pairs to the context 
        """
        pass
import NXOpen
class SmartSaveObject(NXOpen.NXObject): 
    """
        Represents the class for object participating in the smart save operation.
        It is an object that wraps actual NXObject that is modified in the session and processes it to be able to display in Save dialog's table. 
        Refer to technical documentation to know more about Save Management.
    """
    class OperationType(Enum):
        """
        Members Include: 
         |NotSet|  InvalidIgnore 
         |Create|  Create 
         |Revise|  Revise 
         |SaveAs|  SaveAs 
         |Save|  Save 
         |Delete|  DeleteDiscontinue 

        """
        NotSet: int
        Create: int
        Revise: int
        SaveAs: int
        Save: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> SmartSaveObject.OperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetCurrentOperationType(self) -> SmartSaveObject.OperationType:
        """
         Returns the current operation type NXOpen.PDM.SmartSaveObject.OperationType for this smart save object. 
         Returns currentOperationType ( SmartSaveObject.OperationType NXOp): .
        """
        pass
    def GetEffectivityFormula(self) -> str:
        """
         Returns the current effectivity formula for this object. 
         Returns effectivityFormula (str): .
        """
        pass
    def GetModificationReason(self) -> str:
        """
         Returns the modification reason for this smart save object. This reason is used to calculate valid and current operations to be performed. 
         Returns modificationReason (str): .
        """
        pass
    def GetTeamcenterObjectType(self) -> str:
        """
         Returns the Teamcenter object type for this object. 
         Returns objectTcType (str): .
        """
        pass
    def GetValidOperationTypes(self) -> List[SmartSaveObject.OperationType]:
        """
         Returns the valid operation types (array of NXOpen.PDM.SmartSaveObject.OperationType) for this object. 
         Returns currentValidOperationTypes ( SmartSaveObject.OperationType List[NX): .
        """
        pass
    def HasAddContentPrivilege(self) -> bool:
        """
         This is applicable only for 4G components. Returns if the current user can add new components to the Product. 
         Returns addContentPrivilege (bool): .
        """
        pass
    def HasRemoveContentPrivilege(self) -> bool:
        """
         This is applicable only for 4G components. Returns if the current user can remove components to the Product. 
         Returns removeContentPrivilege (bool): .
        """
        pass
    def IsCheckedOutByAnotherUser(self) -> bool:
        """
         Returns if the object is currently checkedout by another user. 
         Returns isCheckedOutByAnotherUser (bool): .
        """
        pass
    def IsDisplayedOnTheSaveDialog(self) -> bool:
        """
         Returns if this object is currently being shown on the save dialog. 
         Returns isDisplayedOnDialog (bool): .
        """
        pass
    def IsExplicitCheckOutNeeded(self) -> bool:
        """
         Returns if the object being saved need to be explicitly checked out. 
         Returns isExplicitCheckOutNeeded (bool): .
        """
        pass
    def IsFrozenByStatus(self) -> bool:
        """
         Returns the state of object in Teamcenter. An object state is considered frozen if the released status on this object marks it to be final. 
         Returns isFrozenByStatus (bool): .
        """
        pass
    def IsMajorRevisable(self) -> bool:
        """
         Returns if the object is major revisable in Teamcenter. 
         Returns isMajorRevisable (bool): .
        """
        pass
    def IsModifiable(self) -> bool:
        """
         Returns if this object is modifiable by the current user. 
         Returns isModifiable (bool): .
        """
        pass
    def IsNonMaster(self) -> bool:
        """
         Returns if this part is a non-master. For non-part objects this will return false. 
         Returns isNonMaster (bool): .
        """
        pass
    def IsReleased(self) -> bool:
        """
         Returns if the object being saved has status applied in Teamcenter. 
         Returns isReleased (bool): .
        """
        pass
    def SetAsDisplayedOnTheSaveDialog(self, markDisplayedOnDialog: bool) -> None:
        """
         Set whether this object is to be shown on the dialog (i.e. valid for user interaction). 
                    Setting this to false will remove the object from the Save dialog's table but it will still be processed for set operation. 
        """
        pass
    def SetCurrentOperationType(self, newOperationType: SmartSaveObject.OperationType) -> None:
        """
         Sets the new operation type NXOpen.PDM.SmartSaveObject.OperationType for this smart save object. This operation should be from among the valid operation types or
                    else the operation will fail. 
        """
        pass
    def SetEffectivityFormula(self, effectivityFormula: str, effectivityDisplayString: str) -> None:
        """
         Sets the new effectivity formula to be applied on this object. 
        """
        pass
    def SetValidOperationTypes(self, newValidOperationTypes: List[SmartSaveObject.OperationType]) -> None:
        """
         Sets the new valid operation types for this object. These operations should be from among the ones returned by 
                    NXOpen.PDM.SmartSaveObject.GetValidOperationTypes or they might be invalid. 
        """
        pass
import NXOpen
class SoaQuery(NXOpen.TransientObject): 
    """ Represents search soa query to perform Teamcenter search"""
    def AddFieldDescription(self, searchVar: PdmSearch, type: PdmSoaqueryNxmgrfielddatatype, name: str, attrName: str, defaultValue: str, logicalOperation: str, mathOperation: str, lov: ListOfValues) -> None:
        """
         Add the field description to create an SOA query 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
import NXOpen
import NXOpen.Assemblies
class TcinUtils(NXOpen.Object): 
    """ Contains various TCIN utility methods """
    def ConvertLegacyDesignControlElements(designControlElements: List[NXOpen.Assemblies.Component]) -> Tuple[List[str], List[str]]:
        """
         Convert legacy Design Control Elements to Stand-alone Design Features 
         Returns A tuple consisting of (legacyDCEIds, newDesignFeatureIds). 
         - legacyDCEIds is: List[str]. array containing list of DCE_ID#REV_ID of DCEs .
         - newDesignFeatureIds is: List[str]. array containing list of DF_ID#REV_ID of new Stand-alone design features .

        """
        pass
import NXOpen
class TracelinkQuery(NXOpen.TransientObject): 
    """ Represents the Trace link query """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                 it is illegal to use the object.  In .NET, this method is automatically
                 called when the object is deleted by the garbage collector.  
        """
        pass
    def GetTracelinkRelationsXml(self) -> str:
        """
         Gets the Traceline Relations. 
         Returns xml_stream (str):  the XML .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class VariantConfigurationBuilder(NXOpen.TaggedObject): 
    """ Represents a builder class that performs variant rule configuration. """
    def AddMultipleVariantRules(self, contextIds: List[str], variantRules: List[str]) -> None:
        """
         Adds given variant rules in case of multiple variant rules to NXOpen.PDM.VariantConfigurationBuilder
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
        """
        pass
    def AskAvailableVariantRules(self, contextId: str, revId: str) -> List[str]:
        """
         Returns the saved variant rules for the give context ID
                The input contextId:
                In case of default domain: it should be Teamcenter item ID.
                In case of non-default domain: it should be the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         Returns variantRules (List[str]):  variant rules from the given context .
        """
        pass
    def GetVariantRuleTableInformation(self) -> Tuple[List[str], List[str]]:
        """
         Returns selected variant rules stored inside NXOpen.PDM.VariantConfigurationBuilder
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         Returns A tuple consisting of (contextIds, variantRules). 
         - contextIds is: List[str]. array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected .
         - variantRules is: List[str]. array of selected variant rules .

        """
        pass
    def RemoveVariantRule(self, contextId: str, variantRule: str) -> None:
        """
         Removes the given variant rule from NXOpen.PDM.VariantConfigurationBuilder if applicable
                The input contextId comprising of multifield key and itemRev_id:
               In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
        """
        pass
import NXOpen
class VariantRulesConfigurationBuilder(NXOpen.Builder): 
    """
        Represents an NXOpen.PDM.VariantRulesConfigurationBuilder to be used for variant rules configuration.
    """
    def AddVariantRulesToConfigure(self, contextIds: List[str], variantRules: List[str]) -> None:
        """
         Adds given variant rules in case of multiple variant rules to NXOpen.PDM.VariantRulesConfigurationBuilder
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
        """
        pass
    def GetVariantRulesForProductAssembly(self, contextId: str, revId: str) -> List[str]:
        """
         Returns the saved variant rules for the give context ID
                The input contextId:
                In case of default domain: it should be Teamcenter item ID.
                In case of non-default domain: it should be the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         Returns variantRules (List[str]):  variant rules from the given context .
        """
        pass
    def GetVariantRulesSelectedForConfiguration(self) -> Tuple[List[str], List[str]]:
        """
         Returns selected variant rules stored inside NXOpen.PDM.VariantRulesConfigurationBuilder
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         Returns A tuple consisting of (contextIds, variantRules). 
         - contextIds is: List[str]. array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected .
         - variantRules is: List[str]. array of selected variant rules .

        """
        pass
import NXOpen
class VolumeSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create volume search filter term.
     Such filter terms can be used to provide filtering.
    """
    class Operator(Enum):
        """
        Members Include: 
         |Inside| 
         |Outside| 
         |Intersects| 
         |InsideOrIntersects| 
         |OutsideOrIntersects| 

        """
        Inside: int
        Outside: int
        Intersects: int
        InsideOrIntersects: int
        OutsideOrIntersects: int
        @staticmethod
        def ValueOf(value: int) -> VolumeSearchFilterTerm.Operator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BoundingBox:
        """
         This struct represents one bounding box. 
         VolumeSearchFilterTermBoundingBox_Struct NXOp is an alias for  VolumeSearchFilterTerm.BoundingBox NXOp.
        """
        @property
        def BottomCorner(self) -> NXOpen.Point3d:
            """
            Getter for property BottomCorner
            Bottom vertex of bounding box in coordinates

            """
            pass
        @BottomCorner.setter
        def BottomCorner(self, value: NXOpen.Point3d):
            """
            Getter for property BottomCorner
            Bottom vertex of bounding box in coordinates
            Setter for property BottomCorner
            Bottom vertex of bounding box in coordinates

            """
            pass
        @property
        def TopCorner(self) -> NXOpen.Point3d:
            """
            Getter for property TopCorner
            Top vertex of bounding box in coordinates

            """
            pass
        @TopCorner.setter
        def TopCorner(self, value: NXOpen.Point3d):
            """
            Getter for property TopCorner
            Top vertex of bounding box in coordinates
            Setter for property TopCorner
            Top vertex of bounding box in coordinates

            """
            pass
    def GetBoundingBoxes(self) -> List[VolumeSearchFilterTerm.BoundingBox]:
        """
         This function gets the bounding boxes from volume term. 
         Returns boundingBoxes ( VolumeSearchFilterTerm.BoundingBox List[NX): .
        """
        pass
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse volume term or not. 
         Returns excludeToggle (bool): .
        """
        pass
    def GetOperator(self) -> VolumeSearchFilterTerm.Operator:
        """
         This function gets the bounding box operator from volume term. 
         Returns boxZoneOperator ( VolumeSearchFilterTerm.Operator NXOp): .
        """
        pass
    def SetBoundingBoxes(self, boundingBoxes: List[VolumeSearchFilterTerm.BoundingBox]) -> None:
        """
         This function sets the bounding boxes to volume term. 
        """
        pass
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse volume term or not. 
        """
        pass
    def SetOperator(self, boxZoneOperator: VolumeSearchFilterTerm.Operator) -> None:
        """
         This function sets the bounding box operator to volume term. 
        """
        pass
import NXOpen
class WebAppSession(NXOpen.Object): 
    """ Represents the Web App session """
    def CreateCustomWebAppMenuHandler() -> CustomWebAppMenuHandler:
        """
         Create a custom WebApp menu handler. 
         Returns menuWrap ( CustomWebAppMenuHandler NXOp):  .
        """
        pass
    def ShowSummary(uid: str, objType: str, classId: str) -> None:
        """
         Send data to Active Workspace from NX 
        """
        pass
