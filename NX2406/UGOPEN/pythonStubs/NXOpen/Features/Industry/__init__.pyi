from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the interface for navigator node classes <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class IndustryNavigatorNode(NXOpen.NXObject): 
    """ Represents the interface for navigator node classes"""
    pass


import NXOpen
##   @brief 
##         Represents a project structure node for AEC project setup.
##          
## 
##  
##         
##         This node is to mark a structure node to create
##         
##         
## 
##   <br>  Created in NX2007.0.0  <br> 

class ProjectStructureNode(NXOpen.TransientObject): 
    """ <summary>
        Represents a project structure node for AEC project setup.
        </summary>
        <remarks>
        This node is to mark a structure node to create
        </remarks>
        """


    ## Getter for property: (bool) Checked
    ##  Returns the node check status.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def Checked(self) -> bool:
        """
        Getter for property: (bool) Checked
         Returns the node check status.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Checked

    ##  Returns the node check status.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Checked.setter
    def Checked(self, nodeChecked: bool):
        """
        Setter for property: (bool) Checked
         Returns the node check status.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAsRootPart
    ##  Returns the flag to indicate whether the node is created as the root part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def CreateAsRootPart(self) -> bool:
        """
        Getter for property: (bool) CreateAsRootPart
         Returns the flag to indicate whether the node is created as the root part.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAsRootPart

    ##  Returns the flag to indicate whether the node is created as the root part.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @CreateAsRootPart.setter
    def CreateAsRootPart(self, createAsRootPart: bool):
        """
        Setter for property: (bool) CreateAsRootPart
         Returns the flag to indicate whether the node is created as the root part.  
             
         
        """
        pass
    
    ## Getter for property: (str) PartName
    ##  Returns the node part name used to define the part file name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the node part name used to define the part file name.  
             
         
        """
        pass
    
    ## Setter for property: (str) PartName

    ##  Returns the node part name used to define the part file name.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the node part name used to define the part file name.  
             
         
        """
        pass
    
    ## Getter for property: (str) SelectedSpecialization
    ##  Returns the node specialization used to define what template is used to create the part.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def SelectedSpecialization(self) -> str:
        """
        Getter for property: (str) SelectedSpecialization
         Returns the node specialization used to define what template is used to create the part.  
             
         
        """
        pass
    
    ## Setter for property: (str) SelectedSpecialization

    ##  Returns the node specialization used to define what template is used to create the part.  
    ##      
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @SelectedSpecialization.setter
    def SelectedSpecialization(self, specialization: str):
        """
        Setter for property: (str) SelectedSpecialization
         Returns the node specialization used to define what template is used to create the part.  
             
         
        """
        pass
    
    ## 
    ##                Free resources associated with the instance. After this method
    ##                is called, it is illegal to use the object.  In .NET, this method
    ##                is automatically called when the object is deleted by the garbage
    ##                collector.
    ##             
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
        
                       Free resources associated with the instance. After this method
                       is called, it is illegal to use the object.  In .NET, this method
                       is automatically called when the object is deleted by the garbage
                       collector.
                    
        """
        pass
    
    ##  Gets the child nodes. 
    ##  @return childNodes (@link ProjectStructureNode List[NXOpen.Features.Industry.ProjectStructureNode]@endlink):  The project structure nodes. .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    def GetChildNodes(self) -> List[ProjectStructureNode]:
        """
         Gets the child nodes. 
         @return childNodes (@link ProjectStructureNode List[NXOpen.Features.Industry.ProjectStructureNode]@endlink):  The project structure nodes. .
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.Tooling
## 
##         Represents a @link NXOpen::Features::Industry::SectionFeatureSpreadsheetBuilder NXOpen::Features::Industry::SectionFeatureSpreadsheetBuilder@endlink  builder. 
##         It is used to manage the data contained in the ship sketch based steel feature block.
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SectionFeatureSpreadsheetBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.Features.Industry.SectionFeatureSpreadsheetBuilder</ja_class> builder. 
        It is used to manage the data contained in the ship sketch based steel feature block.
        """


    ## Getter for property: (int) SectionType
    ##  Returns the section type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Removed with no replacement  <br> 

    ## @return int
    @property
    def SectionType(self) -> int:
        """
        Getter for property: (int) SectionType
         Returns the section type   
            
         
        """
        pass
    
    ## Setter for property: (int) SectionType

    ##  Returns the section type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::Features::Industry::SectionFeatureSpreadsheetBuilder NXOpen::Features::Industry::SectionFeatureSpreadsheetBuilder@endlink .SetSectionType()  <br> 

    @SectionType.setter
    def SectionType(self, pSectionType: int):
        """
        Setter for property: (int) SectionType
         Returns the section type   
            
         
        """
        pass
    
    ## Getter for property: (str) SteelFeatureType
    ##  Returns 
    ##             the steel feature type (eg: Profile, Edge Reinforcement, etc)
    ##               
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def SteelFeatureType(self) -> str:
        """
        Getter for property: (str) SteelFeatureType
         Returns 
                    the steel feature type (eg: Profile, Edge Reinforcement, etc)
                      
            
         
        """
        pass
    
    ## Setter for property: (str) SteelFeatureType

    ##  Returns 
    ##             the steel feature type (eg: Profile, Edge Reinforcement, etc)
    ##               
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SteelFeatureType.setter
    def SteelFeatureType(self, steelFeatureType: str):
        """
        Setter for property: (str) SteelFeatureType
         Returns 
                    the steel feature type (eg: Profile, Edge Reinforcement, etc)
                      
            
         
        """
        pass
    
    ##  
    ##             This method caches parameter data from spreadsheet to the builder.   
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def CacheSpreadsheetData(self) -> None:
        """
         
                    This method caches parameter data from spreadsheet to the builder.   
                    
        """
        pass
    
    ##  
    ##             This method deletes the imported sketch which is unwanted any longer. 
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def DeleteImportedSketch(self) -> None:
        """
         
                    This method deletes the imported sketch which is unwanted any longer. 
                    
        """
        pass
    
    ##  
    ##             This method simply changes the value of a parameter. Parameter could be an expression 
    ##             or an attribute. Also a call to UI method UpdateDlgLayout is needed afterwards if UI is 
    ##             concerned.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str)  the parameter name </param>
    ## <param name="parameterValue"> (str)  the parameter value </param>
    def EditParameter(self, parameterName: str, parameterValue: str) -> None:
        """
         
                    This method simply changes the value of a parameter. Parameter could be an expression 
                    or an attribute. Also a call to UI method UpdateDlgLayout is needed afterwards if UI is 
                    concerned.
                    
        """
        pass
    
    ##  
    ##             This method changes the value of a parameter and queries from the spread sheet to update
    ##             the related parameter values. A call to UI method UpdateDlgLayout is needed afterwards
    ##             if UI is concerned.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterName"> (str)  the parameter name </param>
    ## <param name="parameterValue"> (str)  the parameter value </param>
    def EditPrimaryParameter(self, parameterName: str, parameterValue: str) -> None:
        """
         
                    This method changes the value of a parameter and queries from the spread sheet to update
                    the related parameter values. A call to UI method UpdateDlgLayout is needed afterwards
                    if UI is concerned.
                    
        """
        pass
    
    ##  
    ##             This method finds the available section types for the current context data.
    ##             It will do lookups in the registration file to see which context attribute
    ##             in the table matches the current possible context attributes or the current
    ##             context entitie's attributes.  Then it repopulates the list of available
    ##             section types that are used with the current context attribute.  All of
    ##             these table lookups can be expensive for performance.
    ##             
    ##  @return sectionTypes (List[str]):  Array of available section types .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAvailableSectionTypes(self) -> List[str]:
        """
         
                    This method finds the available section types for the current context data.
                    It will do lookups in the registration file to see which context attribute
                    in the table matches the current possible context attributes or the current
                    context entitie's attributes.  Then it repopulates the list of available
                    section types that are used with the current context attribute.  All of
                    these table lookups can be expensive for performance.
                    
         @return sectionTypes (List[str]):  Array of available section types .
        """
        pass
    
    ##  
    ##             This method retrieves all the features that are imported into current work part.
    ##             
    ##  @return ppSketchTag (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetImportedSketches(self) -> List[NXOpen.Features.Feature]:
        """
         
                    This method retrieves all the features that are imported into current work part.
                    
         @return ppSketchTag (@link NXOpen.Features.Feature List[NXOpen.Features.Feature]@endlink): .
        """
        pass
    
    ##  
    ##             This method retrieves all the parameter values related to the current imported
    ##             sketch template.
    ##             
    ##  @return parameters (@link NXOpen.Tooling.SpreadsheetDataParameter List[NXOpen.Tooling.SpreadsheetDataParameter]@endlink):  Array of structures with the parameter data. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetParameterValues(self) -> List[NXOpen.Tooling.SpreadsheetDataParameter]:
        """
         
                    This method retrieves all the parameter values related to the current imported
                    sketch template.
                    
         @return parameters (@link NXOpen.Tooling.SpreadsheetDataParameter List[NXOpen.Tooling.SpreadsheetDataParameter]@endlink):  Array of structures with the parameter data. .
        """
        pass
    
    ##  
    ##             It retrieves the KRUSpreadsheetData object to the builder. In most cases, this method is used
    ##             internally.
    ##             
    ##  @return pKRUData (@link NXOpen.Tooling.SpreadsheetData NXOpen.Tooling.SpreadsheetData@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetSpreadsheetData(self) -> NXOpen.Tooling.SpreadsheetData:
        """
         
                    It retrieves the KRUSpreadsheetData object to the builder. In most cases, this method is used
                    internally.
                    
         @return pKRUData (@link NXOpen.Tooling.SpreadsheetData NXOpen.Tooling.SpreadsheetData@endlink): .
        """
        pass
    
    ##  
    ##             Thie method reads the model file name from the spread sheet, imports the sketch template
    ##             into current work part, and updates the attribute values and expresseion values from the 
    ##             data spreadsheet. 
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def ImportSketch(self) -> None:
        """
         
                    Thie method reads the model file name from the spread sheet, imports the sketch template
                    into current work part, and updates the attribute values and expresseion values from the 
                    data spreadsheet. 
                    
        """
        pass
    
    ##  
    ##             This method cleans up the imported features from current work part, also it rereads 
    ##             the data file  and registration. If UI is concerned, UpdateDlgLayout should be called in UI.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def ResetBuilderData(self) -> None:
        """
         
                    This method cleans up the imported features from current work part, also it rereads 
                    the data file  and registration. If UI is concerned, UpdateDlgLayout should be called in UI.
                    
        """
        pass
    
    ##  
    ##             This method restores parameter data inside the builder. 
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def RestoreSpreadsheetData(self) -> None:
        """
         
                    This method restores parameter data inside the builder. 
                    
        """
        pass
    
    ##  
    ##             Set the context entity on which the context attribute is stored.  For example, if
    ##             you're spreadsheet builder is being used to create an endcut, the body you're about
    ##             to cut should be set as the context entity.  Refer to the individual feature's 
    ##             documentation to see what context entity is expected for the feature you're using.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="contextEntity"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetContextEntity(self, contextEntity: NXOpen.TaggedObject) -> None:
        """
         
                    Set the context entity on which the context attribute is stored.  For example, if
                    you're spreadsheet builder is being used to create an endcut, the body you're about
                    to cut should be set as the context entity.  Refer to the individual feature's 
                    documentation to see what context entity is expected for the feature you're using.
                    
        """
        pass
    
    ##  
    ##             Set a possible context attribute (assuming the context entity has not yet been created).
    ##             If you have any possible context attributes set in this builder, the context entity will
    ##             be ignored, and the context attribute will be selected from the list of possible context attributes.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="possibleContextAttributeIndex"> (int)  the index into the possible context attribute array we wish to set </param>
    ## <param name="possibleContextAttribute"> (str) </param>
    def SetPossibleContextAttribute(self, possibleContextAttributeIndex: int, possibleContextAttribute: str) -> None:
        """
         
                    Set a possible context attribute (assuming the context entity has not yet been created).
                    If you have any possible context attributes set in this builder, the context entity will
                    be ignored, and the context attribute will be selected from the list of possible context attributes.
                    
        """
        pass
    
    ##  
    ##             Set the possible context attribute count (assuming the context entity has not yet been created).
    ##             If you have any possible context attributes set in this builder, the context entity will
    ##             be ignored, and the context attribute will be selected from the list of possible context attributes.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="possibleContextAttributeCount"> (int)  the number of possible context attributes (use this before setting each possible context attribute via SetPossibleContextAttribute)  </param>
    def SetPossibleContextAttributeCount(self, possibleContextAttributeCount: int) -> None:
        """
         
                    Set the possible context attribute count (assuming the context entity has not yet been created).
                    If you have any possible context attributes set in this builder, the context entity will
                    be ignored, and the context attribute will be selected from the list of possible context attributes.
                    
        """
        pass
    
    ##  
    ##             This method sets the rule inputs. 
    ##             The rule inputs will be used to evaluate the section rules and parameter rules defined in xml 
    ##             rule file.
    ##             Ensure the inputs have been clearly described as comment in the xml rule file, so
    ##             the user can use them when they want to modify the rules.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputNames"> (List[str]) </param>
    ## <param name="inputValues"> (List[str]) </param>
    def SetRuleInputs(self, inputNames: List[str], inputValues: List[str]) -> None:
        """
         
                    This method sets the rule inputs. 
                    The rule inputs will be used to evaluate the section rules and parameter rules defined in xml 
                    rule file.
                    Ensure the inputs have been clearly described as comment in the xml rule file, so
                    the user can use them when they want to modify the rules.
                    
        """
        pass
    
    ## Sets the section sub type by string value.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="strSectionType"> (str) </param>
    def SetSectionSubType1(self, strSectionType: str) -> None:
        """
        Sets the section sub type by string value.
        """
        pass
    
    ##  Sets the section sub type2 by string value.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="strSectionType"> (str) </param>
    def SetSectionSubType2(self, strSectionType: str) -> None:
        """
         Sets the section sub type2 by string value.
        """
        pass
    
    ## 
    ##             This method sets the section type outside the block. It provides a way for the block user
    ##             to set up the section type by a string value. the block will look up the registration
    ##             spreadsheet to translate it into number value.
    ##             
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## <param name="builder"> (@link SectionFeatureSpreadsheetBuilder NXOpen.Features.Industry.SectionFeatureSpreadsheetBuilder@endlink) </param>
    ## <param name="strSectionType"> (str) </param>
    @overload
    def SetSectionType(self, strSectionType: str) -> None:
        """
        
                    This method sets the section type outside the block. It provides a way for the block user
                    to set up the section type by a string value. the block will look up the registration
                    spreadsheet to translate it into number value.
                    
        """
        pass
    
    ##  
    ##             It sets the KRUSpreadsheetData object to the builder. In most cases, this method is used
    ##             internally.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pKRUData"> (@link NXOpen.Tooling.SpreadsheetData NXOpen.Tooling.SpreadsheetData@endlink) </param>
    def SetSpreadsheetData(self, pKRUData: NXOpen.Tooling.SpreadsheetData) -> None:
        """
         
                    It sets the KRUSpreadsheetData object to the builder. In most cases, this method is used
                    internally.
                    
        """
        pass
    
    ##  
    ##             Sets the parameter status such as locked, system key, user key, hidden, editable, non-standard value etc.   
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="paramNames"> (List[str]) </param>
    ## <param name="paramStatus"> (List[int]) </param>
    def SetSpreadsheetDataStatus(self, paramNames: List[str], paramStatus: List[int]) -> None:
        """
         
                    Sets the parameter status such as locked, system key, user key, hidden, editable, non-standard value etc.   
                    
        """
        pass
    
    ##  Set default section types of the builder when a new context entity is set.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def SetsDefaultTypesFromContext(self) -> None:
        """
         Set default section types of the builder when a new context entity is set.
        """
        pass
    
    ##  
    ##             This method updates the parameters in the steel feature data spreadsheet using parameters rules. 
    ##             The rule inputs should be set before you call this method.
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def UpdateParametersUsingRules(self) -> None:
        """
         
                    This method updates the parameters in the steel feature data spreadsheet using parameters rules. 
                    The rule inputs should be set before you call this method.
                    
        """
        pass
    
    ##  
    ##             This method takes parameter name and parameter value pairs as input and updates the related
    ##             geometries by updating the expressions, i.e. sketches.   
    ##             
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="paramNames"> (List[str]) </param>
    ## <param name="paramValues"> (List[str]) </param>
    def UpdateSpreadsheetData(self, paramNames: List[str], paramValues: List[str]) -> None:
        """
         
                    This method takes parameter name and parameter value pairs as input and updates the related
                    geometries by updating the expressions, i.e. sketches.   
                    
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  
##         Represents a select project loadfrom builder. 
##         It is used to manage the data contained in the project load from block.
##         
##      
## 
##   <br>  Created in NX2212.0.0  <br> 

class SelectProjectLoadFromBuilder(NXOpen.TaggedObject): 
    """ 
        Represents a select project loadfrom builder. 
        It is used to manage the data contained in the project load from block.
        
     """


    ##  project settings load from 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CustomerDefaults</term><description> 
    ##  load settings from customer default </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  user specify configration file path </description> </item></list>
    class LoadFromValues(Enum):
        """
        Members Include: <CustomerDefaults> <UserDefined>
        """
        CustomerDefaults: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SelectProjectLoadFromBuilder.LoadFromValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Features.Industry.SelectProjectLoadFromBuilder.LoadFromValues@endlink) LoadFrom
    ##  Returns the load from   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return SelectProjectLoadFromBuilder.LoadFromValues
    @property
    def LoadFrom(self) -> SelectProjectLoadFromBuilder.LoadFromValues:
        """
        Getter for property: (@link SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Features.Industry.SelectProjectLoadFromBuilder.LoadFromValues@endlink) LoadFrom
         Returns the load from   
            
         
        """
        pass
    
    ## Setter for property: (@link SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Features.Industry.SelectProjectLoadFromBuilder.LoadFromValues@endlink) LoadFrom

    ##  Returns the load from   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LoadFrom.setter
    def LoadFrom(self, loadFrom: SelectProjectLoadFromBuilder.LoadFromValues):
        """
        Setter for property: (@link SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Features.Industry.SelectProjectLoadFromBuilder.LoadFromValues@endlink) LoadFrom
         Returns the load from   
            
         
        """
        pass
    
    ## Getter for property: (str) UserXMLFilePath
    ##  Returns the user defined xml file Path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def UserXMLFilePath(self) -> str:
        """
        Getter for property: (str) UserXMLFilePath
         Returns the user defined xml file Path   
            
         
        """
        pass
    
    ## Setter for property: (str) UserXMLFilePath

    ##  Returns the user defined xml file Path   
    ##     
    ##  
    ## Setter License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_bim ("AEC Design")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UserXMLFilePath.setter
    def UserXMLFilePath(self, filename: str):
        """
        Setter for property: (str) UserXMLFilePath
         Returns the user defined xml file Path   
            
         
        """
        pass
    
## @package NXOpen.Features.Industry
## Classes, Enums and Structs under NXOpen.Features.Industry namespace

##  @link SelectProjectLoadFromBuilderLoadFromValues NXOpen.Features.Industry.SelectProjectLoadFromBuilderLoadFromValues @endlink is an alias for @link SelectProjectLoadFromBuilder.LoadFromValues NXOpen.Features.Industry.SelectProjectLoadFromBuilder.LoadFromValues@endlink
SelectProjectLoadFromBuilderLoadFromValues = SelectProjectLoadFromBuilder.LoadFromValues


