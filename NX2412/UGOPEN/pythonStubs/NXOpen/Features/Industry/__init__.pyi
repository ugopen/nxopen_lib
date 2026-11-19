from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class IndustryNavigatorNode(NXOpen.NXObject): 
    """ Represents the interface for navigator node classes"""
    pass
import NXOpen
class ProjectStructureNode(NXOpen.TransientObject): 
    """ 
        Represents a project structure node for AEC project setup.
        
        
        This node is to mark a structure node to create
        
        """
    @property
    def Checked(self) -> bool:
        """
        Getter for property: (bool) Checked
         Returns the node check status.  
             
         
        """
        pass
    @Checked.setter
    def Checked(self, nodeChecked: bool):
        """
        Setter for property: (bool) Checked
         Returns the node check status.  
             
         
        """
        pass
    @property
    def CreateAsRootPart(self) -> bool:
        """
        Getter for property: (bool) CreateAsRootPart
         Returns the flag to indicate whether the node is created as the root part.  
             
         
        """
        pass
    @CreateAsRootPart.setter
    def CreateAsRootPart(self, createAsRootPart: bool):
        """
        Setter for property: (bool) CreateAsRootPart
         Returns the flag to indicate whether the node is created as the root part.  
             
         
        """
        pass
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the node part name used to define the part file name.  
             
         
        """
        pass
    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the node part name used to define the part file name.  
             
         
        """
        pass
    @property
    def SelectedSpecialization(self) -> str:
        """
        Getter for property: (str) SelectedSpecialization
         Returns the node specialization used to define what template is used to create the part.  
             
         
        """
        pass
    @SelectedSpecialization.setter
    def SelectedSpecialization(self, specialization: str):
        """
        Setter for property: (str) SelectedSpecialization
         Returns the node specialization used to define what template is used to create the part.  
             
         
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
    def GetChildNodes(self) -> List[ProjectStructureNode]:
        """
         Gets the child nodes. 
         Returns childNodes ( ProjectStructureNode List[NXOpen.Fe):  The project structure nodes. .
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.Tooling
class SectionFeatureSpreadsheetBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Features.Industry.SectionFeatureSpreadsheetBuilder builder. 
        It is used to manage the data contained in the ship sketch based steel feature block.
        """
    @property
    def SectionType(self) -> int:
        """
        Getter for property: (int) SectionType
         Returns the section type   
            
         
        """
        pass
    @SectionType.setter
    def SectionType(self, pSectionType: int):
        """
        Setter for property: (int) SectionType
         Returns the section type   
            
         
        """
        pass
    @property
    def SteelFeatureType(self) -> str:
        """
        Getter for property: (str) SteelFeatureType
         Returns 
                    the steel feature type (eg: Profile, Edge Reinforcement, etc)
                      
            
         
        """
        pass
    @SteelFeatureType.setter
    def SteelFeatureType(self, steelFeatureType: str):
        """
        Setter for property: (str) SteelFeatureType
         Returns 
                    the steel feature type (eg: Profile, Edge Reinforcement, etc)
                      
            
         
        """
        pass
    def CacheSpreadsheetData(self) -> None:
        """
         
                    This method caches parameter data from spreadsheet to the builder.   
                    
        """
        pass
    def DeleteImportedSketch(self) -> None:
        """
         
                    This method deletes the imported sketch which is unwanted any longer. 
                    
        """
        pass
    def EditParameter(self, parameterName: str, parameterValue: str) -> None:
        """
         
                    This method simply changes the value of a parameter. Parameter could be an expression 
                    or an attribute. Also a call to UI method UpdateDlgLayout is needed afterwards if UI is 
                    concerned.
                    
        """
        pass
    def EditPrimaryParameter(self, parameterName: str, parameterValue: str) -> None:
        """
         
                    This method changes the value of a parameter and queries from the spread sheet to update
                    the related parameter values. A call to UI method UpdateDlgLayout is needed afterwards
                    if UI is concerned.
                    
        """
        pass
    def GetAvailableSectionTypes(self) -> List[str]:
        """
         
                    This method finds the available section types for the current context data.
                    It will do lookups in the registration file to see which context attribute
                    in the table matches the current possible context attributes or the current
                    context entitie's attributes.  Then it repopulates the list of available
                    section types that are used with the current context attribute.  All of
                    these table lookups can be expensive for performance.
                    
         Returns sectionTypes (List[str]):  Array of available section types .
        """
        pass
    def GetImportedSketches(self) -> List[NXOpen.Features.Feature]:
        """
         
                    This method retrieves all the features that are imported into current work part.
                    
         Returns ppSketchTag ( NXOpen.Features.Feature Li): .
        """
        pass
    def GetParameterValues(self) -> List[NXOpen.Tooling.SpreadsheetDataParameter]:
        """
         
                    This method retrieves all the parameter values related to the current imported
                    sketch template.
                    
         Returns parameters ( NXOpen.Tooling.SpreadsheetDataParameter Li):  Array of structures with the parameter data. .
        """
        pass
    def GetSpreadsheetData(self) -> NXOpen.Tooling.SpreadsheetData:
        """
         
                    It retrieves the KRUSpreadsheetData object to the builder. In most cases, this method is used
                    internally.
                    
         Returns pKRUData ( NXOpen.Tooling.SpreadsheetData): .
        """
        pass
    def ImportSketch(self) -> None:
        """
         
                    Thie method reads the model file name from the spread sheet, imports the sketch template
                    into current work part, and updates the attribute values and expresseion values from the 
                    data spreadsheet. 
                    
        """
        pass
    def ResetBuilderData(self) -> None:
        """
         
                    This method cleans up the imported features from current work part, also it rereads 
                    the data file  and registration. If UI is concerned, UpdateDlgLayout should be called in UI.
                    
        """
        pass
    def RestoreSpreadsheetData(self) -> None:
        """
         
                    This method restores parameter data inside the builder. 
                    
        """
        pass
    def SetContextEntity(self, contextEntity: NXOpen.TaggedObject) -> None:
        """
         
                    Set the context entity on which the context attribute is stored.  For example, if
                    you're spreadsheet builder is being used to create an endcut, the body you're about
                    to cut should be set as the context entity.  Refer to the individual feature's 
                    documentation to see what context entity is expected for the feature you're using.
                    
        """
        pass
    def SetPossibleContextAttribute(self, possibleContextAttributeIndex: int, possibleContextAttribute: str) -> None:
        """
         
                    Set a possible context attribute (assuming the context entity has not yet been created).
                    If you have any possible context attributes set in this builder, the context entity will
                    be ignored, and the context attribute will be selected from the list of possible context attributes.
                    
        """
        pass
    def SetPossibleContextAttributeCount(self, possibleContextAttributeCount: int) -> None:
        """
         
                    Set the possible context attribute count (assuming the context entity has not yet been created).
                    If you have any possible context attributes set in this builder, the context entity will
                    be ignored, and the context attribute will be selected from the list of possible context attributes.
                    
        """
        pass
    def SetRuleInputs(self, inputNames: List[str], inputValues: List[str]) -> None:
        """
         
                    This method sets the rule inputs. 
                    The rule inputs will be used to evaluate the section rules and parameter rules defined in xml 
                    rule file.
                    Ensure the inputs have been clearly described as comment in the xml rule file, so
                    the user can use them when they want to modify the rules.
                    
        """
        pass
    def SetSectionSubType1(self, strSectionType: str) -> None:
        """
        Sets the section sub type by string value.
        """
        pass
    def SetSectionSubType2(self, strSectionType: str) -> None:
        """
         Sets the section sub type2 by string value.
        """
        pass
    @overload
    def SetSectionType(self, strSectionType: str) -> None:
        """
                    This method sets the section type outside the block. It provides a way for the block user
                    to set up the section type by a string value. the block will look up the registration
                    spreadsheet to translate it into number value.
                    
        """
        pass
    def SetSpreadsheetData(self, pKRUData: NXOpen.Tooling.SpreadsheetData) -> None:
        """
         
                    It sets the KRUSpreadsheetData object to the builder. In most cases, this method is used
                    internally.
                    
        """
        pass
    def SetSpreadsheetDataStatus(self, paramNames: List[str], paramStatus: List[int]) -> None:
        """
         
                    Sets the parameter status such as locked, system key, user key, hidden, editable, non-standard value etc.   
                    
        """
        pass
    def SetsDefaultTypesFromContext(self) -> None:
        """
         Set default section types of the builder when a new context entity is set.
        """
        pass
    def UpdateParametersUsingRules(self) -> None:
        """
         
                    This method updates the parameters in the steel feature data spreadsheet using parameters rules. 
                    The rule inputs should be set before you call this method.
                    
        """
        pass
    def UpdateSpreadsheetData(self, paramNames: List[str], paramValues: List[str]) -> None:
        """
         
                    This method takes parameter name and parameter value pairs as input and updates the related
                    geometries by updating the expressions, i.e. sketches.   
                    
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectProjectLoadFromBuilder(NXOpen.TaggedObject): 
    """ 
        Represents a select project loadfrom builder. 
        It is used to manage the data contained in the project load from block.
        
     """
    class LoadFromValues(Enum):
        """
        Members Include: 
         |CustomerDefaults|  load settings from customer default 
         |UserDefined|  user specify configration file path 

        """
        CustomerDefaults: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> SelectProjectLoadFromBuilder.LoadFromValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LoadFrom(self) -> SelectProjectLoadFromBuilder.LoadFromValues:
        """
        Getter for property: ( SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Feat) LoadFrom
         Returns the load from   
            
         
        """
        pass
    @LoadFrom.setter
    def LoadFrom(self, loadFrom: SelectProjectLoadFromBuilder.LoadFromValues):
        """
        Setter for property: ( SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Feat) LoadFrom
         Returns the load from   
            
         
        """
        pass
    @property
    def UserXMLFilePath(self) -> str:
        """
        Getter for property: (str) UserXMLFilePath
         Returns the user defined xml file Path   
            
         
        """
        pass
    @UserXMLFilePath.setter
    def UserXMLFilePath(self, filename: str):
        """
        Setter for property: (str) UserXMLFilePath
         Returns the user defined xml file Path   
            
         
        """
        pass
