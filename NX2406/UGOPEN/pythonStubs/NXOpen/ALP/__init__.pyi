from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  use for add external resource  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateAddExternalResourceBuilder  NXOpen::ALP::ALPManager::CreateAddExternalResourceBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class AddExternalResourceBuilder(NXOpen.Builder): 
    """ use for add external resource """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectComponents
    ##  Returns the select components   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectComponents
         Returns the select components   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectResources
    ##  Returns the select resources   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectResources(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectResources
         Returns the select resources   
            
         
        """
        pass
    
    ##  The search resources 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def SearchResources(self) -> None:
        """
         The search resources 
        """
        pass
    
import NXOpen
##  use for cearting Add Mfg Features  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateAddMfgFeaturesBuilder  NXOpen::ALP::ALPManager::CreateAddMfgFeaturesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AssignmentState </term> <description> 
##  
## UnassignedFeatures </description> </item> 
## 
## <item><term> 
##  
## CriteriaConnectedTo </term> <description> 
##  
## AllStationParts </description> </item> 
## 
## <item><term> 
##  
## FeatureClass </term> <description> 
##  
## Discrete </description> </item> 
## 
## <item><term> 
##  
## FeatureType </term> <description> 
##  
## All </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class AddMfgFeaturesBuilder(NXOpen.Builder): 
    """ use for cearting Add Mfg Features """


    ##  the criteria class 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Discrete</term><description> 
    ## </description> </item><item><term> 
    ## Continuous</term><description> 
    ## </description> </item></list>
    class Class(Enum):
        """
        Members Include: <Discrete> <Continuous>
        """
        Discrete: int
        Continuous: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.Class:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the connectedto values 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AllStationParts</term><description> 
    ## </description> </item><item><term> 
    ## PartList</term><description> 
    ## </description> </item></list>
    class ConnectedTo(Enum):
        """
        Members Include: <AllStationParts> <PartList>
        """
        AllStationParts: int
        PartList: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.ConnectedTo:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the assignment state values 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UnassignedFeatures</term><description> 
    ## </description> </item><item><term> 
    ## AssignedFeatures</term><description> 
    ## </description> </item><item><term> 
    ## All</term><description> 
    ## </description> </item></list>
    class FeatureAssignmentState(Enum):
        """
        Members Include: <UnassignedFeatures> <AssignedFeatures> <All>
        """
        UnassignedFeatures: int
        AssignedFeatures: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.FeatureAssignmentState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the criteria type values 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## Weld</term><description> 
    ## </description> </item><item><term> 
    ## Fds</term><description> 
    ## </description> </item><item><term> 
    ## Clinch</term><description> 
    ## </description> </item><item><term> 
    ## Stud</term><description> 
    ## </description> </item><item><term> 
    ## Nut</term><description> 
    ## </description> </item><item><term> 
    ## Bolt</term><description> 
    ## </description> </item><item><term> 
    ## Rivet</term><description> 
    ## </description> </item></list>
    class Type(Enum):
        """
        Members Include: <All> <Weld> <Fds> <Clinch> <Stud> <Nut> <Bolt> <Rivet>
        """
        All: int
        Weld: int
        Fds: int
        Clinch: int
        Stud: int
        Nut: int
        Bolt: int
        Rivet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink) AssignmentState
    ##  Returns the assignment state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddMfgFeaturesBuilder.FeatureAssignmentState
    @property
    def AssignmentState(self) -> AddMfgFeaturesBuilder.FeatureAssignmentState:
        """
        Getter for property: (@link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink) AssignmentState
         Returns the assignment state   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink) AssignmentState

    ##  Returns the assignment state   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AssignmentState.setter
    def AssignmentState(self, assignmentState: AddMfgFeaturesBuilder.FeatureAssignmentState):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink) AssignmentState
         Returns the assignment state   
            
         
        """
        pass
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo
    ##  Returns the criteria connected to   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddMfgFeaturesBuilder.ConnectedTo
    @property
    def CriteriaConnectedTo(self) -> AddMfgFeaturesBuilder.ConnectedTo:
        """
        Getter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo
         Returns the criteria connected to   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo

    ##  Returns the criteria connected to   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CriteriaConnectedTo.setter
    def CriteriaConnectedTo(self, criteriaConnectedTo: AddMfgFeaturesBuilder.ConnectedTo):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo
         Returns the criteria connected to   
            
         
        """
        pass
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass
    ##  Returns the feature class   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddMfgFeaturesBuilder.Class
    @property
    def FeatureClass(self) -> AddMfgFeaturesBuilder.Class:
        """
        Getter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass
         Returns the feature class   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass

    ##  Returns the feature class   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FeatureClass.setter
    def FeatureClass(self, featureClass: AddMfgFeaturesBuilder.Class):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass
         Returns the feature class   
            
         
        """
        pass
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType
    ##  Returns the feature type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddMfgFeaturesBuilder.Type
    @property
    def FeatureType(self) -> AddMfgFeaturesBuilder.Type:
        """
        Getter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType
         Returns the feature type   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType

    ##  Returns the feature type   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FeatureType.setter
    def FeatureType(self, featureType: AddMfgFeaturesBuilder.Type):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType
         Returns the feature type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectParts
    ##  Returns the select parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectParts(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectParts
         Returns the select parts   
            
         
        """
        pass
    
    ##  The Search Button 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def SearchButton(self) -> None:
        """
         The Search Button 
        """
        pass
    
import NXOpen
##  use for creating workarea builder <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateAddWorkareaBuilder  NXOpen::ALP::ALPManager::CreateAddWorkareaBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class AddWorkareaBuilder(NXOpen.Builder): 
    """ use for creating workarea builder"""


    ## Getter for property: (str) Name
    ##  Returns the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
    ##  Returns an API that gets parent tag  
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ParentPartOccurance(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance

    ##  Returns an API that gets parent tag  
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ParentPartOccurance.setter
    def ParentPartOccurance(self, parent: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    
    ## Getter for property: (str) WorkareaTypeName
    ##  Returns the type of workarea   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def WorkareaTypeName(self) -> str:
        """
        Getter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    
    ## Setter for property: (str) WorkareaTypeName

    ##  Returns the type of workarea   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @WorkareaTypeName.setter
    def WorkareaTypeName(self, workareaType: str):
        """
        Setter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    
    ##  Get internal name  
    ##  @return internalName (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="displayName"> (str)  </param>
    def GetInternalName(self, displayName: str) -> str:
        """
         Get internal name  
         @return internalName (str): .
        """
        pass
    
    ##  Set Expression internal name  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="displayName"> (str)  </param>
    ## <param name="internalName"> (str) </param>
    def SetInternalName(self, displayName: str, internalName: str) -> None:
        """
         Set Expression internal name  
        """
        pass
    
import NXOpen
## 
##     Represents a class to create enter and exit the ALP application
##     
## 
##   <br>  Created in NX1926.0.0  <br> 

class ALPApplicationBuilder(NXOpen.NXObject): 
    """
    Represents a class to create enter and exit the ALP application
    """


    ##   Enter the ALP application 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def Enter(self) -> None:
        """
          Enter the ALP application 
        """
        pass
    
    ##   Exit the ALP application this call will destroy the builder
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def Exit(self) -> None:
        """
          Exit the ALP application this call will destroy the builder
        """
        pass
    
    ##  Get the global selection builder
    ##  @return selectionBuilder (@link GlobalSelectionBuilder NXOpen.ALP.GlobalSelectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    def GetGlobalSelectionBuilder(self) -> GlobalSelectionBuilder:
        """
         Get the global selection builder
         @return selectionBuilder (@link GlobalSelectionBuilder NXOpen.ALP.GlobalSelectionBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a manager of ALP builders  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ALPManager(NXOpen.Object): 
    """ Represents a manager of ALP builders """


    ## Consolidate Undo Marks 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="undoMarkId"> (int) </param>
    def ConsolidateUndoMarks(undoMarkId: int) -> None:
        """
        Consolidate Undo Marks 
        """
        pass
    
    ##  Creates Add External Resource Builder
    ##  @return builder (@link AddExternalResourceBuilder NXOpen.ALP.AddExternalResourceBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAddExternalResourceBuilder(part: NXOpen.Part) -> AddExternalResourceBuilder:
        """
         Creates Add External Resource Builder
         @return builder (@link AddExternalResourceBuilder NXOpen.ALP.AddExternalResourceBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Add MFG Features Dialoge Builder
    ##  @return builder (@link AddMfgFeaturesBuilder NXOpen.ALP.AddMfgFeaturesBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAddMfgFeaturesBuilder(part: NXOpen.Part) -> AddMfgFeaturesBuilder:
        """
         Creates a Add MFG Features Dialoge Builder
         @return builder (@link AddMfgFeaturesBuilder NXOpen.ALP.AddMfgFeaturesBuilder@endlink):  .
        """
        pass
    
    ##  Creates Add Workarea Builder
    ##  @return builder (@link AddWorkareaBuilder NXOpen.ALP.AddWorkareaBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAddWorkareaBuilder(part: NXOpen.Part) -> AddWorkareaBuilder:
        """
         Creates Add Workarea Builder
         @return builder (@link AddWorkareaBuilder NXOpen.ALP.AddWorkareaBuilder@endlink):  .
        """
        pass
    
    ##  Create the application builder 
    ##  @return builder (@link ALPApplicationBuilder NXOpen.ALP.ALPApplicationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateApplicationBuilder(part: NXOpen.Part) -> ALPApplicationBuilder:
        """
         Create the application builder 
         @return builder (@link ALPApplicationBuilder NXOpen.ALP.ALPApplicationBuilder@endlink):  .
        """
        pass
    
    ##  Creates auto_weld_distribution builder
    ##  @return builder (@link AutoWeldDistributionBuilder NXOpen.ALP.AutoWeldDistributionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateAutoWeldDistributionBuilder(part: NXOpen.Part) -> AutoWeldDistributionBuilder:
        """
         Creates auto_weld_distribution builder
         @return builder (@link AutoWeldDistributionBuilder NXOpen.ALP.AutoWeldDistributionBuilder@endlink):  .
        """
        pass
    
    ##  Creates a capture image Dialoge Builder
    ##  @return builder (@link CaptureImageBuilder NXOpen.ALP.CaptureImageBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateCaptureImageBuilder(part: NXOpen.Part) -> CaptureImageBuilder:
        """
         Creates a capture image Dialoge Builder
         @return builder (@link CaptureImageBuilder NXOpen.ALP.CaptureImageBuilder@endlink):  .
        """
        pass
    
    ##  Creates Config Variant Conditions Dialoge Builder
    ##  @return builder (@link ConfigVariantConditionBuilder NXOpen.ALP.ConfigVariantConditionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateConfigVariantConditionBuilder(part: NXOpen.Part) -> ConfigVariantConditionBuilder:
        """
         Creates Config Variant Conditions Dialoge Builder
         @return builder (@link ConfigVariantConditionBuilder NXOpen.ALP.ConfigVariantConditionBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Cycle Time Dialoge Builder
    ##  @return builder (@link CycleTimeBuilder NXOpen.ALP.CycleTimeBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateCycleTimeBuilder(part: NXOpen.Part) -> CycleTimeBuilder:
        """
         Creates a Cycle Time Dialoge Builder
         @return builder (@link CycleTimeBuilder NXOpen.ALP.CycleTimeBuilder@endlink):  .
        """
        pass
    
    ##  Creates flows manager builder
    ##  @return builder (@link FlowsManagerBuilder NXOpen.ALP.FlowsManagerBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateFlowsManagerBuilder(part: NXOpen.Part) -> FlowsManagerBuilder:
        """
         Creates flows manager builder
         @return builder (@link FlowsManagerBuilder NXOpen.ALP.FlowsManagerBuilder@endlink):  .
        """
        pass
    
    ##  Create global selection builder 
    ##  @return builder (@link GlobalSelectionBuilder NXOpen.ALP.GlobalSelectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateGlobalSelectionBuilder(part: NXOpen.Part) -> GlobalSelectionBuilder:
        """
         Create global selection builder 
         @return builder (@link GlobalSelectionBuilder NXOpen.ALP.GlobalSelectionBuilder@endlink): .
        """
        pass
    
    ##  Creates libray operation builder
    ##  @return builder (@link LibraryOperationBuilder NXOpen.ALP.LibraryOperationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateLibraryOperationBuilder(part: NXOpen.Part) -> LibraryOperationBuilder:
        """
         Creates libray operation builder
         @return builder (@link LibraryOperationBuilder NXOpen.ALP.LibraryOperationBuilder@endlink):  .
        """
        pass
    
    ##  Creates material flow node
    ##  @return builder (@link MaterialFlowNode NXOpen.ALP.MaterialFlowNode@endlink):  .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateMaterialFlowNode(part: NXOpen.Part) -> MaterialFlowNode:
        """
         Creates material flow node
         @return builder (@link MaterialFlowNode NXOpen.ALP.MaterialFlowNode@endlink):  .
        """
        pass
    
    ##  Creates Modify Variant Builder
    ##  @return builder (@link ModifyVariantBuilder NXOpen.ALP.ModifyVariantBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateModifyVariantBuilder(part: NXOpen.Part) -> ModifyVariantBuilder:
        """
         Creates Modify Variant Builder
         @return builder (@link ModifyVariantBuilder NXOpen.ALP.ModifyVariantBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Operation Dialoge Builder
    ##  @return builder (@link OperationBuilder NXOpen.ALP.OperationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateOperationBuilder(part: NXOpen.Part) -> OperationBuilder:
        """
         Creates a Operation Dialoge Builder
         @return builder (@link OperationBuilder NXOpen.ALP.OperationBuilder@endlink):  .
        """
        pass
    
    ##  Creates Operation Group Builder
    ##  @return builder (@link OperationGroupBuilder NXOpen.ALP.OperationGroupBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateOperationGroupBuilder(part: NXOpen.Part) -> OperationGroupBuilder:
        """
         Creates Operation Group Builder
         @return builder (@link OperationGroupBuilder NXOpen.ALP.OperationGroupBuilder@endlink):  .
        """
        pass
    
    ##  Creates a Position Product Dialoge Builder
    ##  @return builder (@link PositionProductBuilder NXOpen.ALP.PositionProductBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePositionProductBuilder(part: NXOpen.Part) -> PositionProductBuilder:
        """
         Creates a Position Product Dialoge Builder
         @return builder (@link PositionProductBuilder NXOpen.ALP.PositionProductBuilder@endlink):  .
        """
        pass
    
    ##  Creates station takt time builder
    ##  @return builder (@link StationTaktTimeBuilder NXOpen.ALP.StationTaktTimeBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateStationTaktTimeBuilder(part: NXOpen.Part) -> StationTaktTimeBuilder:
        """
         Creates station takt time builder
         @return builder (@link StationTaktTimeBuilder NXOpen.ALP.StationTaktTimeBuilder@endlink):  .
        """
        pass
    
    ##  Creates suggest part builder
    ##  @return builder (@link SuggestPartBuilder NXOpen.ALP.SuggestPartBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateSuggestPartBuilder(part: NXOpen.Part) -> SuggestPartBuilder:
        """
         Creates suggest part builder
         @return builder (@link SuggestPartBuilder NXOpen.ALP.SuggestPartBuilder@endlink):  .
        """
        pass
    
    ##  Creates validate tool builder
    ##  @return builder (@link ValidateToolBuilder NXOpen.ALP.ValidateToolBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateValidateToolBuilder(part: NXOpen.Part) -> ValidateToolBuilder:
        """
         Creates validate tool builder
         @return builder (@link ValidateToolBuilder NXOpen.ALP.ValidateToolBuilder@endlink):  .
        """
        pass
    
    ##  Creates Variant conditions Dialoge Builder
    ##  @return builder (@link VariantConditionBuilder NXOpen.ALP.VariantConditionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateVariantConditionBuilder(part: NXOpen.Part) -> VariantConditionBuilder:
        """
         Creates Variant conditions Dialoge Builder
         @return builder (@link VariantConditionBuilder NXOpen.ALP.VariantConditionBuilder@endlink):  .
        """
        pass
    
    ##  Creates weld_consistency_checker_builder
    ##  @return builder (@link WeldConsistencyCheckerBuilder NXOpen.ALP.WeldConsistencyCheckerBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateWeldConsistencyCheckerBuilder(part: NXOpen.Part) -> WeldConsistencyCheckerBuilder:
        """
         Creates weld_consistency_checker_builder
         @return builder (@link WeldConsistencyCheckerBuilder NXOpen.ALP.WeldConsistencyCheckerBuilder@endlink):  .
        """
        pass
    
    ##  Application builder is return 
    ##  @return builder (@link ALPApplicationBuilder NXOpen.ALP.ALPApplicationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def GetApplicationBuilder() -> ALPApplicationBuilder:
        """
         Application builder is return 
         @return builder (@link ALPApplicationBuilder NXOpen.ALP.ALPApplicationBuilder@endlink): .
        """
        pass
    
    ##   @brief  
    ##         Opens ALP Application
    ##          
    ## 
    ##   
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="lineItemID"> (str)  line itemId </param>
    ## <param name="lineRevisionID"> (str)  line revision id </param>
    ## <param name="ccUUID"> (str)  collaborative context UUID</param>
    ## <param name="variantObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  variant configuration specification </param>
    def OpenApplication(lineItemID: str, lineRevisionID: str, ccUUID: str, variantObject: NXOpen.NXObject) -> None:
        """
          @brief  
                Opens ALP Application
                 
        
          
        """
        pass
    
##  Represents sheet layout options 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Toptobottom</term><description> 
## </description> </item><item><term> 
## Lefttoright</term><description> 
## </description> </item></list>
class AlpPertLayout(Enum):
    """
    Members Include: <Toptobottom> <Lefttoright>
    """
    Toptobottom: int
    Lefttoright: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AlpPertLayout:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  use for creation of Automatic Weld Distribution Builder  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateAutoWeldDistributionBuilder  NXOpen::ALP::ALPManager::CreateAutoWeldDistributionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class AutoWeldDistributionBuilder(NXOpen.Builder): 
    """ use for creation of Automatic Weld Distribution Builder """


    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectedLine
    ##  Returns the selected line property   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectedLine(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectedLine
         Returns the selected line property   
            
         
        """
        pass
    
    ##  The method calculate a new weld distribution proposal 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def CalculateProposal(self) -> None:
        """
         The method calculate a new weld distribution proposal 
        """
        pass
    
    ##  The method execute the new weld distribution proposal 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def ExecuteProposal(self) -> None:
        """
         The method execute the new weld distribution proposal 
        """
        pass
    
    ##  The selected line object method 
    ##  @return selectLine (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetSelectedLineObject(self) -> NXOpen.TaggedObject:
        """
         The selected line object method 
         @return selectLine (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
        """
        pass
    
    ##  The method sort the child stations by flows and scope flows 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectLine"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SortChildStationsByFlows(self, selectLine: NXOpen.TaggedObject) -> None:
        """
         The method sort the child stations by flows and scope flows 
        """
        pass
    
    ##  The method suppress station from proposal 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="stationTag"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="bSuppress"> (bool) </param>
    def SuppressStation(self, stationTag: NXOpen.TaggedObject, bSuppress: bool) -> None:
        """
         The method suppress station from proposal 
        """
        pass
    
import NXOpen
##   <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateCaptureImageBuilder  NXOpen::ALP::ALPManager::CreateCaptureImageBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EmphasizeToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ViewChangeEnum </term> <description> 
##  
## Isometric </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CaptureImageBuilder(NXOpen.Builder): 
    """ """


    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Trimetric</term><description> 
    ## </description> </item><item><term> 
    ## Isometric</term><description> 
    ## </description> </item><item><term> 
    ## Top</term><description> 
    ## </description> </item><item><term> 
    ## Bottom</term><description> 
    ## </description> </item><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item><item><term> 
    ## Front</term><description> 
    ## </description> </item><item><term> 
    ## Back</term><description> 
    ## </description> </item></list>
    class CaptureImage(Enum):
        """
        Members Include: <Trimetric> <Isometric> <Top> <Bottom> <Left> <Right> <Front> <Back>
        """
        Trimetric: int
        Isometric: int
        Top: int
        Bottom: int
        Left: int
        Right: int
        Front: int
        Back: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CaptureImageBuilder.CaptureImage:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) EmphasizeToggle
    ##  Returns the emphasize toggle   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def EmphasizeToggle(self) -> bool:
        """
        Getter for property: (bool) EmphasizeToggle
         Returns the emphasize toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) EmphasizeToggle

    ##  Returns the emphasize toggle   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @EmphasizeToggle.setter
    def EmphasizeToggle(self, emphasizeToggle: bool):
        """
        Setter for property: (bool) EmphasizeToggle
         Returns the emphasize toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectNode
    ##  Returns the select node   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectNode(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectNode
         Returns the select node   
            
         
        """
        pass
    
    ## Getter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum
    ##  Returns the view change enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return CaptureImageBuilder.CaptureImage
    @property
    def ViewChangeEnum(self) -> CaptureImageBuilder.CaptureImage:
        """
        Getter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum
         Returns the view change enum   
            
         
        """
        pass
    
    ## Setter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum

    ##  Returns the view change enum   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ViewChangeEnum.setter
    def ViewChangeEnum(self, viewChangeEnum: CaptureImageBuilder.CaptureImage):
        """
        Setter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum
         Returns the view change enum   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def ZoomToFitButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
import NXOpen
##  For creating and editing Product Configurator Variant Conditions  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateConfigVariantConditionBuilder  NXOpen::ALP::ALPManager::CreateConfigVariantConditionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class ConfigVariantConditionBuilder(NXOpen.Builder): 
    """ For creating and editing Product Configurator Variant Conditions """


    ## Getter for property: (str) ConfigVariantCondition
    ##  Returns the selected attribute to get or set config variant condition string   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def ConfigVariantCondition(self) -> str:
        """
        Getter for property: (str) ConfigVariantCondition
         Returns the selected attribute to get or set config variant condition string   
            
         
        """
        pass
    
    ## Setter for property: (str) ConfigVariantCondition

    ##  Returns the selected attribute to get or set config variant condition string   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConfigVariantCondition.setter
    def ConfigVariantCondition(self, configVariantCondition: str):
        """
        Setter for property: (str) ConfigVariantCondition
         Returns the selected attribute to get or set config variant condition string   
            
         
        """
        pass
    
import NXOpen
##   <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateCycleTimeBuilder  NXOpen::ALP::ALPManager::CreateCycleTimeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CycleTime </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class CycleTimeBuilder(NXOpen.Builder): 
    """ """


    ## Getter for property: (float) CycleTime
    ##  Returns the cycle time   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def CycleTime(self) -> float:
        """
        Getter for property: (float) CycleTime
         Returns the cycle time   
            
         
        """
        pass
    
    ## Setter for property: (float) CycleTime

    ##  Returns the cycle time   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CycleTime.setter
    def CycleTime(self, cycleTime: float):
        """
        Setter for property: (float) CycleTime
         Returns the cycle time   
            
         
        """
        pass
    
    ## Getter for property: (bool) OverwriteToggle
    ##  Returns the override toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def OverwriteToggle(self) -> bool:
        """
        Getter for property: (bool) OverwriteToggle
         Returns the override toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) OverwriteToggle

    ##  Returns the override toggle   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @OverwriteToggle.setter
    def OverwriteToggle(self, overwriteToggle: bool):
        """
        Setter for property: (bool) OverwriteToggle
         Returns the override toggle   
            
         
        """
        pass
    
import NXOpen
##   <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateFlowsManagerBuilder  NXOpen::ALP::ALPManager::CreateFlowsManagerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class FlowsManagerBuilder(NXOpen.Builder): 
    """ """


    ##  TODO: fill in a description for this 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Flow</term><description> 
    ## </description> </item><item><term> 
    ## ScopeFlow</term><description> 
    ## </description> </item><item><term> 
    ## Any</term><description> 
    ## </description> </item></list>
    class Type(Enum):
        """
        Members Include: <NotSet> <Flow> <ScopeFlow> <Any>
        """
        NotSet: int
        Flow: int
        ScopeFlow: int
        Any: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlowsManagerBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SourceSelectObject
    ##  Returns the source select object   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SourceSelectObject(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SourceSelectObject
         Returns the source select object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) TargetSelectObject
    ##  Returns the target select object   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def TargetSelectObject(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) TargetSelectObject
         Returns the target select object   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return results (bool): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="input"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="output"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateFlow(self, input: NXOpen.TaggedObject, output: NXOpen.TaggedObject) -> bool:
        """
         TODO: fill in a description for this 
         @return results (bool): .
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def CreateFlowButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return results (bool): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="input"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="output"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def DeleteFlow(self, input: NXOpen.TaggedObject, output: NXOpen.TaggedObject) -> bool:
        """
         TODO: fill in a description for this 
         @return results (bool): .
        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return operations (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def GetAllFlowableObjects(self) -> List[NXOpen.TaggedObject]:
        """
         TODO: fill in a description for this 
         @return operations (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return A tuple consisting of (input, output). 
    ##  - input is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink.
    ##  - output is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink.

    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="type"> (@link FlowsManagerBuilder.Type NXOpen.ALP.FlowsManagerBuilder.Type@endlink) </param>
    def GetAllFlowsByType(self, type: FlowsManagerBuilder.Type) -> Tuple[List[NXOpen.TaggedObject], List[NXOpen.TaggedObject]]:
        """
         TODO: fill in a description for this 
         @return A tuple consisting of (input, output). 
         - input is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink.
         - output is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink.

        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return results (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="input"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="type"> (@link FlowsManagerBuilder.Type NXOpen.ALP.FlowsManagerBuilder.Type@endlink) </param>
    def GetIncomingFlowsByType(self, input: NXOpen.TaggedObject, type: FlowsManagerBuilder.Type) -> List[NXOpen.TaggedObject]:
        """
         TODO: fill in a description for this 
         @return results (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return results (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="input"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="type"> (@link FlowsManagerBuilder.Type NXOpen.ALP.FlowsManagerBuilder.Type@endlink) </param>
    def GetOutgoingFlowsByType(self, input: NXOpen.TaggedObject, type: FlowsManagerBuilder.Type) -> List[NXOpen.TaggedObject]:
        """
         TODO: fill in a description for this 
         @return results (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  TODO: fill in a description for this 
    ##  @return results (@link FlowsManagerBuilder.Type NXOpen.ALP.FlowsManagerBuilder.Type@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="input"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="output"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def HasFlow(self, input: NXOpen.TaggedObject, output: NXOpen.TaggedObject) -> FlowsManagerBuilder.Type:
        """
         TODO: fill in a description for this 
         @return results (@link FlowsManagerBuilder.Type NXOpen.ALP.FlowsManagerBuilder.Type@endlink): .
        """
        pass
    
import NXOpen
##  Global Selection  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateGlobalSelectionBuilder  NXOpen::ALP::ALPManager::CreateGlobalSelectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class GlobalSelectionBuilder(NXOpen.Builder): 
    """ Global Selection """


    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Selection
    ##  Returns the selected objects   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Selection(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Selection
         Returns the selected objects   
            
         
        """
        pass
    
import NXOpen
##  A class for creating operation/operation group from library  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateLibraryOperationBuilder  NXOpen::ALP::ALPManager::CreateLibraryOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class LibraryOperationBuilder(NXOpen.Builder): 
    """ A class for creating operation/operation group from library """


    ## Getter for property: (str) Name
    ##  Returns the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
import NXOpen
##   @brief 
##     Represents assembly line planner journaling methods for Library Operation related functionalities   
##      
## 
##    <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class LibraryOperation(NXOpen.Object): 
    """ <summary>
    Represents assembly line planner journaling methods for Library Operation related functionalities   
    </summary> """


    ##   @brief 
    ##         Creates root node
    ##          
    ## 
    ##   
    ##  @return rootObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  LibraryOperation root objects .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def CreateRootModel() -> List[NXOpen.NXObject]:
        """
          @brief 
                Creates root node
                 
        
          
         @return rootObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  LibraryOperation root objects .
        """
        pass
    
    ##   @brief  
    ##         Get Childrens
    ##          
    ## 
    ##   
    ##  @return childObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="itemId"> (str) </param>
    ## <param name="itemRevId"> (str) </param>
    def GetChildren(itemId: str, itemRevId: str) -> List[NXOpen.NXObject]:
        """
          @brief  
                Get Childrens
                 
        
          
         @return childObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
import NXOpen
##  Represents Material Flow information  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateMaterialFlowNode  NXOpen::ALP::ALPManager::CreateMaterialFlowNode @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class MaterialFlowNode(NXOpen.NXObject): 
    """ Represents Material Flow information """
    pass


import NXOpen
##  For modifying Variant Rule  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateModifyVariantBuilder  NXOpen::ALP::ALPManager::CreateModifyVariantBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## VariantRuleList </term> <description> 
##  
## VariantRuleName </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class ModifyVariantBuilder(NXOpen.Builder): 
    """ For modifying Variant Rule """


    ##  This enum is used for defining different rules in dropdown 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## VariantRuleName</term><description> 
    ## </description> </item></list>
    class VariantRules(Enum):
        """
        Members Include: <VariantRuleName>
        """
        VariantRuleName: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ModifyVariantBuilder.VariantRules:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedVariantRuleTag
    ##  Returns a property to get or set the selected variant rule   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def SelectedVariantRuleTag(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedVariantRuleTag
         Returns a property to get or set the selected variant rule   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedVariantRuleTag

    ##  Returns a property to get or set the selected variant rule   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SelectedVariantRuleTag.setter
    def SelectedVariantRuleTag(self, variantRuleTag: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedVariantRuleTag
         Returns a property to get or set the selected variant rule   
            
         
        """
        pass
    
    ## Getter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList
    ##  Returns the variant rule list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ModifyVariantBuilder.VariantRules
    @property
    def VariantRuleList(self) -> ModifyVariantBuilder.VariantRules:
        """
        Getter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList
         Returns the variant rule list   
            
         
        """
        pass
    
    ## Setter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList

    ##  Returns the variant rule list   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @VariantRuleList.setter
    def VariantRuleList(self, variantRuleList: ModifyVariantBuilder.VariantRules):
        """
        Setter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList
         Returns the variant rule list   
            
         
        """
        pass
    
    ##  Add the rule 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def AddRule(self) -> None:
        """
         Add the rule 
        """
        pass
    
    ##  Remove the rule 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def RemoveRule(self) -> None:
        """
         Remove the rule 
        """
        pass
    
import NXOpen
##  use for cearting operation  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateOperationBuilder  NXOpen::ALP::ALPManager::CreateOperationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## OperationType </term> <description> 
##  
## Undefined </description> </item> 
## 
## <item><term> 
##  
## Time </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class OperationBuilder(NXOpen.Builder): 
    """ use for cearting operation """


    ##  This enum have collection of all type of operation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ## </description> </item><item><term> 
    ## Operator</term><description> 
    ## </description> </item><item><term> 
    ## Tooling</term><description> 
    ## </description> </item><item><term> 
    ## Safety</term><description> 
    ## </description> </item><item><term> 
    ## Conveyance</term><description> 
    ## </description> </item><item><term> 
    ## MHRobot</term><description> 
    ## </description> </item><item><term> 
    ## GeoWeld</term><description> 
    ## </description> </item><item><term> 
    ## Respot</term><description> 
    ## </description> </item><item><term> 
    ## StudNutBolt</term><description> 
    ## </description> </item><item><term> 
    ## RivetFDS</term><description> 
    ## </description> </item><item><term> 
    ## Scribing</term><description> 
    ## </description> </item><item><term> 
    ## Vision</term><description> 
    ## </description> </item><item><term> 
    ## LaserSpotWeld</term><description> 
    ## </description> </item><item><term> 
    ## MigWeld</term><description> 
    ## </description> </item><item><term> 
    ## SealingAdhesive</term><description> 
    ## </description> </item><item><term> 
    ## LaserCut</term><description> 
    ## </description> </item><item><term> 
    ## Hemming</term><description> 
    ## </description> </item><item><term> 
    ## RobotHold</term><description> 
    ## </description> </item></list>
    class Operation(Enum):
        """
        Members Include: <Undefined> <Operator> <Tooling> <Safety> <Conveyance> <MHRobot> <GeoWeld> <Respot> <StudNutBolt> <RivetFDS> <Scribing> <Vision> <LaserSpotWeld> <MigWeld> <SealingAdhesive> <LaserCut> <Hemming> <RobotHold>
        """
        Undefined: int
        Operator: int
        Tooling: int
        Safety: int
        Conveyance: int
        MHRobot: int
        GeoWeld: int
        Respot: int
        StudNutBolt: int
        RivetFDS: int
        Scribing: int
        Vision: int
        LaserSpotWeld: int
        MigWeld: int
        SealingAdhesive: int
        LaserCut: int
        Hemming: int
        RobotHold: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OperationBuilder.Operation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Name
    ##  Returns the name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Getter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType
    ##  Returns the operation type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return OperationBuilder.Operation
    @property
    def OperationType(self) -> OperationBuilder.Operation:
        """
        Getter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType
         Returns the operation type   
            
         
        """
        pass
    
    ## Setter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType

    ##  Returns the operation type   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OperationType.setter
    def OperationType(self, operationType: OperationBuilder.Operation):
        """
        Setter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType
         Returns the operation type   
            
         
        """
        pass
    
    ## Getter for property: (str) OperationTypeName
    ##  Returns the operation type name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def OperationTypeName(self) -> str:
        """
        Getter for property: (str) OperationTypeName
         Returns the operation type name   
            
         
        """
        pass
    
    ## Setter for property: (str) OperationTypeName

    ##  Returns the operation type name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OperationTypeName.setter
    def OperationTypeName(self, name: str):
        """
        Setter for property: (str) OperationTypeName
         Returns the operation type name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectFeatures
    ##  Returns the select features   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectFeatures(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectFeatures
         Returns the select features   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectOperation
    ##  Returns the select operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectOperation(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectOperation
         Returns the select operation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectPart
    ##  Returns the select part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectPart(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectPart
         Returns the select part   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectResources
    ##  Returns the select resources   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectResources(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectResources
         Returns the select resources   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectStation
    ##  Returns the select station   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectStation(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectStation
         Returns the select station   
            
         
        """
        pass
    
    ## Getter for property: (float) Time
    ##  Returns the time   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Time(self) -> float:
        """
        Getter for property: (float) Time
         Returns the time   
            
         
        """
        pass
    
    ## Setter for property: (float) Time

    ##  Returns the time   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Time.setter
    def Time(self, time: float):
        """
        Setter for property: (float) Time
         Returns the time   
            
         
        """
        pass
    
import NXOpen
##  A class for creating operation group in structure  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateOperationGroupBuilder  NXOpen::ALP::ALPManager::CreateOperationGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class OperationGroupBuilder(NXOpen.Builder): 
    """ A class for creating operation group in structure """


    ## Getter for property: (str) GroupName
    ##  Returns the group name   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def GroupName(self) -> str:
        """
        Getter for property: (str) GroupName
         Returns the group name   
            
         
        """
        pass
    
    ## Setter for property: (str) GroupName

    ##  Returns the group name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @GroupName.setter
    def GroupName(self, groupName: str):
        """
        Setter for property: (str) GroupName
         Returns the group name   
            
         
        """
        pass
    
import NXOpen
##   @brief 
##     Represents assembly line planner journaling methods for PERT related functionalities   
##     PERT - Program evalution review technique used to understand material flow in manufacturing process planning
##      
## 
##    <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX2306.3000.0  <br> 

class Pert(NXOpen.Object): 
    """ <summary>
    Represents assembly line planner journaling methods for PERT related functionalities   
    PERT - Program evalution review technique used to understand material flow in manufacturing process planning
    </summary> """


    ##   @brief  
    ##         Performs layouting of diagramming sheet nodes
    ##          
    ## 
    ##   
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="partoccSheet"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Specific occurrence of Diagramming sheet </param>
    ## <param name="sheetLayoutOption"> (@link AlpPertLayout NXOpen.ALP.AlpPertLayout@endlink)  Determines layout option </param>
    def ApplyLayout(partoccSheet: NXOpen.NXObject, sheetLayoutOption: AlpPertLayout) -> None:
        """
          @brief  
                Performs layouting of diagramming sheet nodes
                 
        
          
        """
        pass
    
    ##   @brief 
    ##         Creates the flow
    ##          
    ## 
    ##   
    ##  @return flowObject (@link NXOpen.NXObject NXOpen.NXObject@endlink):  Connection flow object .
    ## 
    ##   <br>  Created in NX2306.3000.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="sourceStationPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Specific occurrence of Source Station </param>
    ## <param name="destStationPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Specific occurrence of Destination Station </param>
    def CreateFlow(sourceStationPartOcc: NXOpen.NXObject, destStationPartOcc: NXOpen.NXObject) -> NXOpen.NXObject:
        """
          @brief 
                Creates the flow
                 
        
          
         @return flowObject (@link NXOpen.NXObject NXOpen.NXObject@endlink):  Connection flow object .
        """
        pass
    
    ##   @brief  
    ##         Deletes the flow
    ##          
    ## 
    ##   
    ## 
    ##   <br>  Created in NX2306.3000.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="flowsToDelete"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  An array of flows we want to delete </param>
    ## <param name="doNotUpdate"> (bool)  Determines whether to perform the update action  </param>
    def DeleteFlow(flowsToDelete: List[NXOpen.NXObject], doNotUpdate: bool) -> None:
        """
          @brief  
                Deletes the flow
                 
        
          
        """
        pass
    
import NXOpen
##  use for cearting Position Product  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreatePositionProductBuilder  NXOpen::ALP::ALPManager::CreatePositionProductBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class PositionProductBuilder(NXOpen.Builder): 
    """ use for cearting Position Product """


    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectedResource
    ##  Returns the select resource   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectedResource(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectedResource
         Returns the select resource   
            
         
        """
        pass
    
import NXOpen
##  Represents color/hide assigned products functionalities methods  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ProductVisibility(NXOpen.Object): 
    """ Represents color/hide assigned products functionalities methods """


    ##   @brief 
    ##         Get Color Assignment Indication
    ##          
    ## 
    ##   
    ##  @return indication (bool): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def GetColorAssignmentIndication() -> bool:
        """
          @brief 
                Get Color Assignment Indication
                 
        
          
         @return indication (bool): .
        """
        pass
    
    ##   @brief 
    ##         Get Hide Assignment Indication
    ##          
    ## 
    ##   
    ##  @return indication (bool): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def GetHideAssignmentIndication() -> bool:
        """
          @brief 
                Get Hide Assignment Indication
                 
        
          
         @return indication (bool): .
        """
        pass
    
    ##   @brief 
    ##         Set Color Assignment Indication
    ##          
    ## 
    ##   
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="indication"> (bool) </param>
    def SetColorAssignmentIndication(indication: bool) -> None:
        """
          @brief 
                Set Color Assignment Indication
                 
        
          
        """
        pass
    
    ##   @brief 
    ##         Set Hide Assignment Indication
    ##          
    ## 
    ##   
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="indication"> (bool) </param>
    def SetHideAssignmentIndication(indication: bool) -> None:
        """
          @brief 
                Set Hide Assignment Indication
                 
        
          
        """
        pass
    
    ##   @brief 
    ##         Update visiblity of targeted products
    ##          
    ## 
    ##   
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="productPartOcc"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def UpdateProductsVisiblity(productPartOcc: List[NXOpen.NXObject]) -> None:
        """
          @brief 
                Update visiblity of targeted products
                 
        
          
        """
        pass
    
import NXOpen
##  station takt time  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateStationTaktTimeBuilder  NXOpen::ALP::ALPManager::CreateStationTaktTimeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## StationTaktTime </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TaktTimeEnum </term> <description> 
##  
## UseLineTaktTime </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class StationTaktTimeBuilder(NXOpen.Builder): 
    """ station takt time """


    ##  takt time enum 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UseLineTaktTime</term><description> 
    ## </description> </item><item><term> 
    ## SetforLoadedStation</term><description> 
    ## </description> </item></list>
    class Radio(Enum):
        """
        Members Include: <UseLineTaktTime> <SetforLoadedStation>
        """
        UseLineTaktTime: int
        SetforLoadedStation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StationTaktTimeBuilder.Radio:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) StationTaktTime
    ##  Returns the station takt time   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def StationTaktTime(self) -> float:
        """
        Getter for property: (float) StationTaktTime
         Returns the station takt time   
            
         
        """
        pass
    
    ## Setter for property: (float) StationTaktTime

    ##  Returns the station takt time   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @StationTaktTime.setter
    def StationTaktTime(self, stationTaktTime: float):
        """
        Setter for property: (float) StationTaktTime
         Returns the station takt time   
            
         
        """
        pass
    
    ## Getter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum
    ##  Returns the takt time enum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return StationTaktTimeBuilder.Radio
    @property
    def TaktTimeEnum(self) -> StationTaktTimeBuilder.Radio:
        """
        Getter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum
         Returns the takt time enum   
            
         
        """
        pass
    
    ## Setter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum

    ##  Returns the takt time enum   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TaktTimeEnum.setter
    def TaktTimeEnum(self, taktTimeEnum: StationTaktTimeBuilder.Radio):
        """
        Setter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum
         Returns the takt time enum   
            
         
        """
        pass
    
import NXOpen
##  use for suggesting parts to assign to station  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateSuggestPartBuilder  NXOpen::ALP::ALPManager::CreateSuggestPartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SuggestPartBuilder(NXOpen.Builder): 
    """ use for suggesting parts to assign to station """


    ## Getter for property: (int) ColorForAssignParts
    ##  Returns the assign part color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def ColorForAssignParts(self) -> int:
        """
        Getter for property: (int) ColorForAssignParts
         Returns the assign part color   
            
         
        """
        pass
    
    ## Setter for property: (int) ColorForAssignParts

    ##  Returns the assign part color   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ColorForAssignParts.setter
    def ColorForAssignParts(self, color: int):
        """
        Setter for property: (int) ColorForAssignParts
         Returns the assign part color   
            
         
        """
        pass
    
    ## Getter for property: (int) ColorForIncomingParts
    ##  Returns the incoming part color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def ColorForIncomingParts(self) -> int:
        """
        Getter for property: (int) ColorForIncomingParts
         Returns the incoming part color   
            
         
        """
        pass
    
    ## Setter for property: (int) ColorForIncomingParts

    ##  Returns the incoming part color   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ColorForIncomingParts.setter
    def ColorForIncomingParts(self, color: int):
        """
        Setter for property: (int) ColorForIncomingParts
         Returns the incoming part color   
            
         
        """
        pass
    
    ## Getter for property: (int) ColorForSuggestedParts
    ##  Returns the assign part color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def ColorForSuggestedParts(self) -> int:
        """
        Getter for property: (int) ColorForSuggestedParts
         Returns the assign part color   
            
         
        """
        pass
    
    ## Setter for property: (int) ColorForSuggestedParts

    ##  Returns the assign part color   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ColorForSuggestedParts.setter
    def ColorForSuggestedParts(self, color: int):
        """
        Setter for property: (int) ColorForSuggestedParts
         Returns the assign part color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) NextStation
    ##  Returns the next  station   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def NextStation(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) NextStation
         Returns the next  station   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) PrevStation
    ##  Returns the prev  station   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def PrevStation(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) PrevStation
         Returns the prev  station   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectedStation
    ##  Returns the selected station property   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectedStation(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectedStation
         Returns the selected station property   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) StationProcess
    ##  Returns the selected station Process   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def StationProcess(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) StationProcess
         Returns the selected station Process   
            
         
        """
        pass
    
    ##  To restore display state 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def CollectSuggestedParts(self) -> None:
        """
         To restore display state 
        """
        pass
    
    ##  The method to get the suggested parts
    ##  @return selectedParts (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetSelectedParts(self) -> List[NXOpen.TaggedObject]:
        """
         The method to get the suggested parts
         @return selectedParts (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink): .
        """
        pass
    
    ##  To restore display state 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def RestoreDisplaystate(self) -> None:
        """
         To restore display state 
        """
        pass
    
    ##  The method to set the input parts for the commit function
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="selectedParts"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetSelectedParts(self, selectedParts: List[NXOpen.NXObject]) -> None:
        """
         The method to set the input parts for the commit function
        """
        pass
    
import NXOpen
##  Represents a utils of assembly line planner for journaling uinode methods  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class UINodeUtils(NXOpen.Object): 
    """ Represents a utils of assembly line planner for journaling uinode methods """


    ##  To add external resource 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="targetCompResList"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def AddAdditionalResources(targetCompResList: List[NXOpen.NXObject]) -> None:
        """
         To add external resource 
        """
        pass
    
    ##  To assign features to operation 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedFeature"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="operationPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="totalWeldTime"> (float) </param>
    ## <param name="allowMultipleAssignment"> (bool) </param>
    def AssignMfgFeature(selectedFeature: List[NXOpen.NXObject], operationPartOcc: NXOpen.NXObject, totalWeldTime: float, allowMultipleAssignment: bool) -> None:
        """
         To assign features to operation 
        """
        pass
    
    ##  To Clear Searched Features 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="stationPartOccTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def ClearSearchedFeatures(stationPartOccTag: NXOpen.NXObject) -> None:
        """
         To Clear Searched Features 
        """
        pass
    
    ##  To create new item
    ##  @return partTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="temp_part_name"> (str) </param>
    ## <param name="itemType"> (str) </param>
    ## <param name="applicationName"> (str) </param>
    ## <param name="partUnits"> (@link NXOpen.Part.Units NXOpen.Part.Units@endlink) </param>
    ## <param name="dbPartNo"> (str) </param>
    def CreateNewItem(temp_part_name: str, itemType: str, applicationName: str, partUnits: NXOpen.Part.Units, dbPartNo: str) -> NXOpen.NXObject:
        """
         To create new item
         @return partTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  To create new item
    ##  @return childOperationTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="operationObjectTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="clonnedGroupTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="objectName"> (str) </param>
    def CreateOperationFromLibrary(operationObjectTag: NXOpen.NXObject, clonnedGroupTag: NXOpen.NXObject, objectName: str) -> NXOpen.NXObject:
        """
         To create new item
         @return childOperationTag (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  To create new item
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="operationObjectTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="objectName"> (str) </param>
    def CreateOperationGroupFromLibrary(operationObjectTag: NXOpen.NXObject, objectName: str) -> None:
        """
         To create new item
        """
        pass
    
    ##  To get item revision name 
    ##  @return itemRevName (str): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="partTag"> (@link NXOpen.Part NXOpen.Part@endlink)  </param>
    def GetItemRevisionName(partTag: NXOpen.Part) -> str:
        """
         To get item revision name 
         @return itemRevName (str): .
        """
        pass
    
    ##  To Move remaining un assigned features to next station
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="mfgPartOccTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="currentStationPartOccTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="nextStationName"> (str) </param>
    def MoveUnAssignedFeaturesToNextStation(mfgPartOccTags: List[NXOpen.NXObject], currentStationPartOccTag: NXOpen.NXObject, nextStationName: str) -> None:
        """
         To Move remaining un assigned features to next station
        """
        pass
    
    ##  To assign product And station
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedProduct"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="selectedStation"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="objectToRefresh"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def ProductAndStationAssignment(selectedProduct: List[NXOpen.NXObject], selectedStation: List[NXOpen.NXObject], objectToRefresh: List[NXOpen.NXObject]) -> None:
        """
         To assign product And station
        """
        pass
    
    ##  To unassign product And station
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedProduct"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="unassignOption"> (int) </param>
    ## <param name="label"> (str) </param>
    def ProductAndStationUnassignment(selectedProduct: List[NXOpen.NXObject], unassignOption: int, label: str) -> None:
        """
         To unassign product And station
        """
        pass
    
    ##  To remove external resource 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="resToBeRemoved"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="removingChildOfPackage"> (bool) </param>
    def RemoveAdditionalResources(resToBeRemoved: List[NXOpen.NXObject], removingChildOfPackage: bool) -> None:
        """
         To remove external resource 
        """
        pass
    
    ##  To rotate a given component in clockwise or anticlockwise direction by 90 degrees 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="partOccTags"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="isClockwise"> (bool) </param>
    ## <param name="rotateAsGroup"> (bool) </param>
    ## <param name="angleStep"> (float) </param>
    def RotateComponent(partOccTags: List[NXOpen.NXObject], isClockwise: bool, rotateAsGroup: bool, angleStep: float) -> None:
        """
         To rotate a given component in clockwise or anticlockwise direction by 90 degrees 
        """
        pass
    
    ##  To set or unset an assembly as special end item 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="operationPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="setOption"> (bool) </param>
    def SetInContextEndItem(operationPartOcc: NXOpen.NXObject, setOption: bool) -> None:
        """
         To set or unset an assembly as special end item 
        """
        pass
    
    ##  To show/hide features
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="isHidden"> (bool) </param>
    def ShowHideFeatures(isHidden: bool) -> None:
        """
         To show/hide features
        """
        pass
    
    ##  To unassign features from operation 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedFeature"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="operationName"> (str) </param>
    ## <param name="selectedOpPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def UnAssignMfgFeature(selectedFeature: List[NXOpen.NXObject], operationName: str, selectedOpPartOcc: NXOpen.NXObject) -> None:
        """
         To unassign features from operation 
        """
        pass
    
    ##  To Update the Operation Name 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="operationPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="newOperationName"> (str) </param>
    def UpdateOperationName(operationPartOcc: NXOpen.NXObject, newOperationName: str) -> None:
        """
         To Update the Operation Name 
        """
        pass
    
    ##  To Update the Operation Time 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="operationPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="newOperationTime"> (float) </param>
    def UpdateOperationTime(operationPartOcc: NXOpen.NXObject, newOperationTime: float) -> None:
        """
         To Update the Operation Time 
        """
        pass
    
import NXOpen
##  use for creation of weld conistency checker builder  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateValidateToolBuilder  NXOpen::ALP::ALPManager::CreateValidateToolBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ValidateToolBuilder(NXOpen.Builder): 
    """ use for creation of weld conistency checker builder """


    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectOperation
    ##  Returns the selected operation property   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectOperation(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectOperation
         Returns the selected operation property   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectTool
    ##  Returns the selected tool property   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectTool(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectTool
         Returns the selected tool property   
            
         
        """
        pass
    
    ##  The method to assign the selected tool to the operation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def AssignTool(self) -> None:
        """
         The method to assign the selected tool to the operation 
        """
        pass
    
    ##  The method to calculate tool clearence from all features assigned to operation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def CalculateToolClearence(self) -> None:
        """
         The method to calculate tool clearence from all features assigned to operation 
        """
        pass
    
    ##  The method to load new tool instance from re-use library if needed 
    ##  @return newToolOcc (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="itemId"> (str) </param>
    ## <param name="revId"> (str) </param>
    def MapToolInstanceFromReuseLibrary(self, itemId: str, revId: str) -> NXOpen.TaggedObject:
        """
         The method to load new tool instance from re-use library if needed 
         @return newToolOcc (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
        """
        pass
    
    ##  The method to set the flip tool allowed 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="flipToolAllowed"> (bool) </param>
    def SetIsFlipToolAllowed(self, flipToolAllowed: bool) -> None:
        """
         The method to set the flip tool allowed 
        """
        pass
    
    ##  Set pie chart builder 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pieChartBuilder"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetReusePieChartBuilder(self, pieChartBuilder: NXOpen.TaggedObject) -> None:
        """
         Set pie chart builder 
        """
        pass
    
    ##  The method to set the rotation step size 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="stepSize"> (float) </param>
    def SetRotationStepSize(self, stepSize: float) -> None:
        """
         The method to set the rotation step size 
        """
        pass
    
    ##  The method to set the selected welds for validation
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedWeld"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SetSelectedWeld(self, selectedWeld: NXOpen.TaggedObject) -> None:
        """
         The method to set the selected welds for validation
        """
        pass
    
    ##  The method to replace current tool with new tool 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="newToolOcc"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def SwapWorkingTool(self, newToolOcc: NXOpen.TaggedObject) -> None:
        """
         The method to replace current tool with new tool 
        """
        pass
    
import NXOpen
##  For creating and editing Variant Conditions  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateVariantConditionBuilder  NXOpen::ALP::ALPManager::CreateVariantConditionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1938.0.0  <br> 

class VariantConditionBuilder(NXOpen.Builder): 
    """ For creating and editing Variant Conditions """


    ##  This enum is used for defining different contions together 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## And</term><description> 
    ## </description> </item><item><term> 
    ## Or</term><description> 
    ## </description> </item></list>
    class Condition(Enum):
        """
        Members Include: <And> <Or>
        """
        And: int
        Or: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VariantConditionBuilder.Condition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) LogicalAction
    ##  Returns the logical action   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return VariantConditionBuilder.Condition
    @property
    def LogicalAction(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) LogicalAction
         Returns the logical action   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) LogicalAction

    ##  Returns the logical action   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @LogicalAction.setter
    def LogicalAction(self, logicalAction: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) LogicalAction
         Returns the logical action   
            
         
        """
        pass
    
    ## Getter for property: (str) OperationName
    ##  Returns the operation name   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return str
    @property
    def OperationName(self) -> str:
        """
        Getter for property: (str) OperationName
         Returns the operation name   
            
         
        """
        pass
    
    ## Setter for property: (str) OperationName

    ##  Returns the operation name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OperationName.setter
    def OperationName(self, operationName: str):
        """
        Setter for property: (str) OperationName
         Returns the operation name   
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType
    ##  Returns the operator type   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return VariantConditionBuilder.Condition
    @property
    def OperatorType(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType
         Returns the operator type   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType

    ##  Returns the operator type   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OperatorType.setter
    def OperatorType(self, operatorType: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType
         Returns the operator type   
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName
    ##  Returns the option name   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return VariantConditionBuilder.Condition
    @property
    def OptionName(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName
         Returns the option name   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName

    ##  Returns the option name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OptionName.setter
    def OptionName(self, optionName: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName
         Returns the option name   
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue
    ##  Returns the option value   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## @return VariantConditionBuilder.Condition
    @property
    def OptionValue(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue
         Returns the option value   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue

    ##  Returns the option value   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OptionValue.setter
    def OptionValue(self, optionValue: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue
         Returns the option value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectOperation
    ##  Returns the select operation   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectOperation(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectOperation
         Returns the select operation   
            
         
        """
        pass
    
    ## Getter for property: (str) VariantCondition
    ##  Returns a property to get or set the defined string of variant condition   
    ##     
    ##  
    ## Getter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1942.0.0  <br> 

    ## @return str
    @property
    def VariantCondition(self) -> str:
        """
        Getter for property: (str) VariantCondition
         Returns a property to get or set the defined string of variant condition   
            
         
        """
        pass
    
    ## Setter for property: (str) VariantCondition

    ##  Returns a property to get or set the defined string of variant condition   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1942.0.0  <br> 

    @VariantCondition.setter
    def VariantCondition(self, variantCondition: str):
        """
        Setter for property: (str) VariantCondition
         Returns a property to get or set the defined string of variant condition   
            
         
        """
        pass
    
    ##  Add a new line to the variant condition
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def AddLine(self) -> None:
        """
         Add a new line to the variant condition
        """
        pass
    
    ##  Delete an existing line from the variant condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def DeleteLine(self) -> None:
        """
         Delete an existing line from the variant condition 
        """
        pass
    
    ##  Move an existing condition one line down in the set of variant condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def MoveDown(self) -> None:
        """
         Move an existing condition one line down in the set of variant condition 
        """
        pass
    
    ##  Move an existing condition one line up in the set of variant condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def MoveUp(self) -> None:
        """
         Move an existing condition one line up in the set of variant condition 
        """
        pass
    
    ##  Replace an existing line with a new condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def ReplaceLine(self) -> None:
        """
         Replace an existing line with a new condition 
        """
        pass
    
import NXOpen
##  Represents a web gantt of line designer for journaling  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class WebGantt(NXOpen.Object): 
    """ Represents a web gantt of line designer for journaling """


    ##  To create links between operations
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperation"> (List[str]) </param>
    def CreateLinkBetweenOperation(selectedOperation: List[str]) -> None:
        """
         To create links between operations
        """
        pass
    
    ## To delete links between multilpe operations
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperation"> (List[str]) </param>
    def DeleteLinksForMultipleOperation(selectedOperation: List[str]) -> None:
        """
        To delete links between multilpe operations
        """
        pass
    
    ##  To delete link between single operations
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperation"> (List[str]) </param>
    def DeleteLinksForSingleOperation(selectedOperation: List[str]) -> None:
        """
         To delete link between single operations
        """
        pass
    
    ## To delete operation
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperation"> (List[str]) </param>
    def DeleteOperation(selectedOperation: List[str]) -> None:
        """
        To delete operation
        """
        pass
    
    ## To delete operation group
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperationGroup"> (List[str]) </param>
    ## <param name="moveOperationToStation"> (bool) </param>
    def DeleteOperationGroup(selectedOperationGroup: List[str], moveOperationToStation: bool) -> None:
        """
        To delete operation group
        """
        pass
    
    ## To Duplicate selection operations and operation groups
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperations"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="selectedOperationGroups"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def DuplicateOperationsAndGroups(selectedOperations: List[NXOpen.NXObject], selectedOperationGroups: List[NXOpen.NXObject]) -> None:
        """
        To Duplicate selection operations and operation groups
        """
        pass
    
    ## To Load new staion while Gantt view is open
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="ganttTitle"> (str) </param>
    def LoadNewStationRoot(ganttTitle: str) -> None:
        """
        To Load new staion while Gantt view is open
        """
        pass
    
    ## To move operation to group
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperation"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="parentPartOccTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def MoveOperationToGroup(selectedOperation: List[NXOpen.NXObject], parentPartOccTag: NXOpen.NXObject) -> None:
        """
        To move operation to group
        """
        pass
    
    ## To remove operation from group
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOperation"> (List[str]) </param>
    def RemoveOperationFromGroup(selectedOperation: List[str]) -> None:
        """
        To remove operation from group
        """
        pass
    
    ## To set reset transient
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="selectedOpParents"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="isSetTransient"> (bool) </param>
    def SetResetTransientFlag(selectedOpParents: List[NXOpen.NXObject], isSetTransient: bool) -> None:
        """
        To set reset transient
        """
        pass
    
    ##  To set updated Gantt Data
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    def SetUpdatedGanttData() -> None:
        """
         To set updated Gantt Data
        """
        pass
    
    ##  To set updated Gantt Data with reset flag
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## <param name="operationType"> (str) </param>
    def SetUpdatedGanttDataResetNameAndTime(operationType: str) -> None:
        """
         To set updated Gantt Data with reset flag
        """
        pass
    
import NXOpen
##  use for creation of weld conistency checker builder  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateWeldConsistencyCheckerBuilder  NXOpen::ALP::ALPManager::CreateWeldConsistencyCheckerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class WeldConsistencyCheckerBuilder(NXOpen.Builder): 
    """ use for creation of weld conistency checker builder """


    ##  An API function which un-assign all the weld points in the list from operations conatined in the active station  
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ## <param name="selectedWeldPoints"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def UnAssignWeldPoints(self, selectedWeldPoints: List[NXOpen.NXObject]) -> None:
        """
         An API function which un-assign all the weld points in the list from operations conatined in the active station  
        """
        pass
    
## @package NXOpen.ALP
## Classes, Enums and Structs under NXOpen.ALP namespace

##  @link AddMfgFeaturesBuilderClass NXOpen.ALP.AddMfgFeaturesBuilderClass @endlink is an alias for @link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink
AddMfgFeaturesBuilderClass = AddMfgFeaturesBuilder.Class


##  @link AddMfgFeaturesBuilderConnectedTo NXOpen.ALP.AddMfgFeaturesBuilderConnectedTo @endlink is an alias for @link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink
AddMfgFeaturesBuilderConnectedTo = AddMfgFeaturesBuilder.ConnectedTo


##  @link AddMfgFeaturesBuilderFeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilderFeatureAssignmentState @endlink is an alias for @link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink
AddMfgFeaturesBuilderFeatureAssignmentState = AddMfgFeaturesBuilder.FeatureAssignmentState


##  @link AddMfgFeaturesBuilderType NXOpen.ALP.AddMfgFeaturesBuilderType @endlink is an alias for @link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink
AddMfgFeaturesBuilderType = AddMfgFeaturesBuilder.Type


##  @link CaptureImageBuilderCaptureImage NXOpen.ALP.CaptureImageBuilderCaptureImage @endlink is an alias for @link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink
CaptureImageBuilderCaptureImage = CaptureImageBuilder.CaptureImage


##  @link FlowsManagerBuilderType NXOpen.ALP.FlowsManagerBuilderType @endlink is an alias for @link FlowsManagerBuilder.Type NXOpen.ALP.FlowsManagerBuilder.Type@endlink
FlowsManagerBuilderType = FlowsManagerBuilder.Type


##  @link ModifyVariantBuilderVariantRules NXOpen.ALP.ModifyVariantBuilderVariantRules @endlink is an alias for @link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink
ModifyVariantBuilderVariantRules = ModifyVariantBuilder.VariantRules


##  @link OperationBuilderOperation NXOpen.ALP.OperationBuilderOperation @endlink is an alias for @link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink
OperationBuilderOperation = OperationBuilder.Operation


##  @link StationTaktTimeBuilderRadio NXOpen.ALP.StationTaktTimeBuilderRadio @endlink is an alias for @link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink
StationTaktTimeBuilderRadio = StationTaktTimeBuilder.Radio


##  @link VariantConditionBuilderCondition NXOpen.ALP.VariantConditionBuilderCondition @endlink is an alias for @link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink
VariantConditionBuilderCondition = VariantConditionBuilder.Condition


