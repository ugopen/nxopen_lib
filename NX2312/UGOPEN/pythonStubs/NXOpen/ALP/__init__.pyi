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
    ##   the select components   
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
          the select components   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectResources
    ##   the select resources   
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
          the select resources   
            
         
        """
        pass
    
    ##  The search resources 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SearchResources(builder: AddExternalResourceBuilder) -> None:
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
    ##   the assignment state   
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
          the assignment state   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink) AssignmentState

    ##   the assignment state   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AssignmentState.setter
    def AssignmentState(self, assignmentState: AddMfgFeaturesBuilder.FeatureAssignmentState):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.FeatureAssignmentState NXOpen.ALP.AddMfgFeaturesBuilder.FeatureAssignmentState@endlink) AssignmentState
          the assignment state   
            
         
        """
        pass
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo
    ##   the criteria connected to   
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
          the criteria connected to   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo

    ##   the criteria connected to   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CriteriaConnectedTo.setter
    def CriteriaConnectedTo(self, criteriaConnectedTo: AddMfgFeaturesBuilder.ConnectedTo):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.ConnectedTo NXOpen.ALP.AddMfgFeaturesBuilder.ConnectedTo@endlink) CriteriaConnectedTo
          the criteria connected to   
            
         
        """
        pass
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass
    ##   the feature class   
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
          the feature class   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass

    ##   the feature class   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FeatureClass.setter
    def FeatureClass(self, featureClass: AddMfgFeaturesBuilder.Class):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.Class NXOpen.ALP.AddMfgFeaturesBuilder.Class@endlink) FeatureClass
          the feature class   
            
         
        """
        pass
    
    ## Getter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType
    ##   the feature type   
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
          the feature type   
            
         
        """
        pass
    
    ## Setter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType

    ##   the feature type   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FeatureType.setter
    def FeatureType(self, featureType: AddMfgFeaturesBuilder.Type):
        """
        Setter for property: (@link AddMfgFeaturesBuilder.Type NXOpen.ALP.AddMfgFeaturesBuilder.Type@endlink) FeatureType
          the feature type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectParts
    ##   the select parts   
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
          the select parts   
            
         
        """
        pass
    
    ##  The Search Button 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def SearchButton(builder: AddMfgFeaturesBuilder) -> None:
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
    ##   the name   
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
          the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
    ##   an API that gets parent tag  
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
          an API that gets parent tag  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance

    ##   an API that gets parent tag  
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ParentPartOccurance.setter
    def ParentPartOccurance(self, parent: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ParentPartOccurance
          an API that gets parent tag  
            
         
        """
        pass
    
    ## Getter for property: (str) WorkareaTypeName
    ##   the type of workarea   
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
          the type of workarea   
            
         
        """
        pass
    
    ## Setter for property: (str) WorkareaTypeName

    ##   the type of workarea   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @WorkareaTypeName.setter
    def WorkareaTypeName(self, workareaType: str):
        """
        Setter for property: (str) WorkareaTypeName
          the type of workarea   
            
         
        """
        pass
    
    ##  Get internal name  
    ##  @return internalName (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    ##  
    def GetInternalName(builder: AddWorkareaBuilder, displayName: str) -> str:
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
    def SetInternalName(builder: AddWorkareaBuilder, displayName: str, internalName: str) -> None:
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
    @staticmethod
    def Enter(builder: ALPApplicationBuilder) -> None:
        """
          Enter the ALP application 
        """
        pass
    
    ##   Exit the ALP application this call will destroy the builder
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    @staticmethod
    def Exit(builder: ALPApplicationBuilder) -> None:
        """
          Exit the ALP application this call will destroy the builder
        """
        pass
    
    ##  Get the global selection builder
    ##  @return selectionBuilder (@link GlobalSelectionBuilder NXOpen.ALP.GlobalSelectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: ld_line_designer ("FULL LINE DESIGNER")
    @staticmethod
    def GetGlobalSelectionBuilder(builder: ALPApplicationBuilder) -> GlobalSelectionBuilder:
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
    @staticmethod
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
    @staticmethod
    def GetApplicationBuilder() -> ALPApplicationBuilder:
        """
         Application builder is return 
         @return builder (@link ALPApplicationBuilder NXOpen.ALP.ALPApplicationBuilder@endlink): .
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
    ##   the selected line property   
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
          the selected line property   
            
         
        """
        pass
    
    ##  The method calculate a new weld distribution proposal 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def CalculateProposal(builder: AutoWeldDistributionBuilder) -> None:
        """
         The method calculate a new weld distribution proposal 
        """
        pass
    
    ##  The method execute the new weld distribution proposal 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ExecuteProposal(builder: AutoWeldDistributionBuilder) -> None:
        """
         The method execute the new weld distribution proposal 
        """
        pass
    
    ##  The selected line object method 
    ##  @return selectLine (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedLineObject(builder: AutoWeldDistributionBuilder) -> NXOpen.TaggedObject:
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
    def SortChildStationsByFlows(builder: AutoWeldDistributionBuilder, selectLine: NXOpen.TaggedObject) -> None:
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
    def SuppressStation(builder: AutoWeldDistributionBuilder, stationTag: NXOpen.TaggedObject, bSuppress: bool) -> None:
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
        Members Include: <Isometric> <Top> <Bottom> <Left> <Right> <Front> <Back>
        """
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
    
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectNode
    ##   the select node   
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
          the select node   
            
         
        """
        pass
    
    ## Getter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum
    ##   the view change enum   
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
          the view change enum   
            
         
        """
        pass
    
    ## Setter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum

    ##   the view change enum   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ViewChangeEnum.setter
    def ViewChangeEnum(self, viewChangeEnum: CaptureImageBuilder.CaptureImage):
        """
        Setter for property: (@link CaptureImageBuilder.CaptureImage NXOpen.ALP.CaptureImageBuilder.CaptureImage@endlink) ViewChangeEnum
          the view change enum   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def ZoomToFitButton(builder: CaptureImageBuilder) -> None:
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
    ##   the selected attribute to get or set config variant condition string   
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
          the selected attribute to get or set config variant condition string   
            
         
        """
        pass
    
    ## Setter for property: (str) ConfigVariantCondition

    ##   the selected attribute to get or set config variant condition string   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConfigVariantCondition.setter
    def ConfigVariantCondition(self, configVariantCondition: str):
        """
        Setter for property: (str) ConfigVariantCondition
          the selected attribute to get or set config variant condition string   
            
         
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
## 0.1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class CycleTimeBuilder(NXOpen.Builder): 
    """ """


    ## Getter for property: (float) CycleTime
    ##   the cycle time   
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
          the cycle time   
            
         
        """
        pass
    
    ## Setter for property: (float) CycleTime

    ##   the cycle time   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CycleTime.setter
    def CycleTime(self, cycleTime: float):
        """
        Setter for property: (float) CycleTime
          the cycle time   
            
         
        """
        pass
    
    ## Getter for property: (bool) OverwriteToggle
    ##   the override toggle   
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
          the override toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) OverwriteToggle

    ##   the override toggle   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @OverwriteToggle.setter
    def OverwriteToggle(self, overwriteToggle: bool):
        """
        Setter for property: (bool) OverwriteToggle
          the override toggle   
            
         
        """
        pass
    
import NXOpen
##  Global Selection  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateGlobalSelectionBuilder  NXOpen::ALP::ALPManager::CreateGlobalSelectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class GlobalSelectionBuilder(NXOpen.Builder): 
    """ Global Selection """


    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Selection
    ##   the selected objects   
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
          the selected objects   
            
         
        """
        pass
    
import NXOpen
##  A class for creating operation/operation group from library  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateLibraryOperationBuilder  NXOpen::ALP::ALPManager::CreateLibraryOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class LibraryOperationBuilder(NXOpen.Builder): 
    """ A class for creating operation/operation group from library """


    ## Getter for property: (str) Name
    ##   the name   
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
          the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
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
    ##   a property to get or set the selected variant rule   
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
          a property to get or set the selected variant rule   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedVariantRuleTag

    ##   a property to get or set the selected variant rule   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SelectedVariantRuleTag.setter
    def SelectedVariantRuleTag(self, variantRuleTag: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) SelectedVariantRuleTag
          a property to get or set the selected variant rule   
            
         
        """
        pass
    
    ## Getter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList
    ##   the variant rule list   
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
          the variant rule list   
            
         
        """
        pass
    
    ## Setter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList

    ##   the variant rule list   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @VariantRuleList.setter
    def VariantRuleList(self, variantRuleList: ModifyVariantBuilder.VariantRules):
        """
        Setter for property: (@link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink) VariantRuleList
          the variant rule list   
            
         
        """
        pass
    
    ##  Add the rule 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def AddRule(builder: ModifyVariantBuilder) -> None:
        """
         Add the rule 
        """
        pass
    
    ##  Remove the rule 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def RemoveRule(builder: ModifyVariantBuilder) -> None:
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
    ##   the name   
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
          the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType
    ##   the operation type   
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
          the operation type   
            
         
        """
        pass
    
    ## Setter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType

    ##   the operation type   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OperationType.setter
    def OperationType(self, operationType: OperationBuilder.Operation):
        """
        Setter for property: (@link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink) OperationType
          the operation type   
            
         
        """
        pass
    
    ## Getter for property: (str) OperationTypeName
    ##   the operation type name   
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
          the operation type name   
            
         
        """
        pass
    
    ## Setter for property: (str) OperationTypeName

    ##   the operation type name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OperationTypeName.setter
    def OperationTypeName(self, name: str):
        """
        Setter for property: (str) OperationTypeName
          the operation type name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectFeatures
    ##   the select features   
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
          the select features   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectOperation
    ##   the select operation   
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
          the select operation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectPart
    ##   the select part   
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
          the select part   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectResources
    ##   the select resources   
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
          the select resources   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectStation
    ##   the select station   
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
          the select station   
            
         
        """
        pass
    
    ## Getter for property: (float) Time
    ##   the time   
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
          the time   
            
         
        """
        pass
    
    ## Setter for property: (float) Time

    ##   the time   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Time.setter
    def Time(self, time: float):
        """
        Setter for property: (float) Time
          the time   
            
         
        """
        pass
    
import NXOpen
##  A class for creating operation group in structure  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateOperationGroupBuilder  NXOpen::ALP::ALPManager::CreateOperationGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class OperationGroupBuilder(NXOpen.Builder): 
    """ A class for creating operation group in structure """


    ## Getter for property: (str) GroupName
    ##   the group name   
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
          the group name   
            
         
        """
        pass
    
    ## Setter for property: (str) GroupName

    ##   the group name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @GroupName.setter
    def GroupName(self, groupName: str):
        """
        Setter for property: (str) GroupName
          the group name   
            
         
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
    ##  Specific occurrence of Diagramming sheet 
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
    ##  Specific occurrence of Source Station 
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
    ##  An array of flows we want to delete 
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
    ##   the select resource   
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
          the select resource   
            
         
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
    ##   the station takt time   
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
          the station takt time   
            
         
        """
        pass
    
    ## Setter for property: (float) StationTaktTime

    ##   the station takt time   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @StationTaktTime.setter
    def StationTaktTime(self, stationTaktTime: float):
        """
        Setter for property: (float) StationTaktTime
          the station takt time   
            
         
        """
        pass
    
    ## Getter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum
    ##   the takt time enum   
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
          the takt time enum   
            
         
        """
        pass
    
    ## Setter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum

    ##   the takt time enum   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TaktTimeEnum.setter
    def TaktTimeEnum(self, taktTimeEnum: StationTaktTimeBuilder.Radio):
        """
        Setter for property: (@link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink) TaktTimeEnum
          the takt time enum   
            
         
        """
        pass
    
import NXOpen
##  use for suggesting parts to assign to station  <br> To create a new instance of this class, use @link NXOpen::ALP::ALPManager::CreateSuggestPartBuilder  NXOpen::ALP::ALPManager::CreateSuggestPartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SuggestPartBuilder(NXOpen.Builder): 
    """ use for suggesting parts to assign to station """


    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectedStation
    ##   the selected station property   
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
          the selected station property   
            
         
        """
        pass
    
    ##  The method to set the input parts for the commit function
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedParts"> (@link NXOpen.Part List[NXOpen.Part]@endlink) </param>
    def SetSelectedParts(builder: SuggestPartBuilder, selectedParts: List[NXOpen.Part]) -> None:
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
    @staticmethod
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
    @staticmethod
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
    ##  
    @staticmethod
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
    @staticmethod
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
    ##   the selected operation property   
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
          the selected operation property   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectTool
    ##   the selected tool property   
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
          the selected tool property   
            
         
        """
        pass
    
    ##  The method to assign the selected tool to the operation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def AssignTool(builder: ValidateToolBuilder) -> None:
        """
         The method to assign the selected tool to the operation 
        """
        pass
    
    ##  The method to calculate tool clearence from all features assigned to operation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def CalculateToolClearence(builder: ValidateToolBuilder) -> None:
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
    def MapToolInstanceFromReuseLibrary(builder: ValidateToolBuilder, itemId: str, revId: str) -> NXOpen.TaggedObject:
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
    def SetIsFlipToolAllowed(builder: ValidateToolBuilder, flipToolAllowed: bool) -> None:
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
    def SetReusePieChartBuilder(builder: ValidateToolBuilder, pieChartBuilder: NXOpen.TaggedObject) -> None:
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
    def SetRotationStepSize(builder: ValidateToolBuilder, stepSize: float) -> None:
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
    def SetSelectedWeld(builder: ValidateToolBuilder, selectedWeld: NXOpen.TaggedObject) -> None:
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
    def SwapWorkingTool(builder: ValidateToolBuilder, newToolOcc: NXOpen.TaggedObject) -> None:
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
    ##   the logical action   
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
          the logical action   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) LogicalAction

    ##   the logical action   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @LogicalAction.setter
    def LogicalAction(self, logicalAction: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) LogicalAction
          the logical action   
            
         
        """
        pass
    
    ## Getter for property: (str) OperationName
    ##   the operation name   
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
          the operation name   
            
         
        """
        pass
    
    ## Setter for property: (str) OperationName

    ##   the operation name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OperationName.setter
    def OperationName(self, operationName: str):
        """
        Setter for property: (str) OperationName
          the operation name   
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType
    ##   the operator type   
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
          the operator type   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType

    ##   the operator type   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OperatorType.setter
    def OperatorType(self, operatorType: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OperatorType
          the operator type   
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName
    ##   the option name   
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
          the option name   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName

    ##   the option name   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OptionName.setter
    def OptionName(self, optionName: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionName
          the option name   
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue
    ##   the option value   
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
          the option value   
            
         
        """
        pass
    
    ## Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue

    ##   the option value   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    @OptionValue.setter
    def OptionValue(self, optionValue: VariantConditionBuilder.Condition):
        """
        Setter for property: (@link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink) OptionValue
          the option value   
            
         
        """
        pass
    
    ## Getter for property: (str) VariantCondition
    ##   a property to get or set the defined string of variant condition   
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
          a property to get or set the defined string of variant condition   
            
         
        """
        pass
    
    ## Setter for property: (str) VariantCondition

    ##   a property to get or set the defined string of variant condition   
    ##     
    ##  
    ## Setter License requirements: alp_planner ("Assembly Line Planner")
    ## 
    ##   <br>  Created in NX1942.0.0  <br> 

    @VariantCondition.setter
    def VariantCondition(self, variantCondition: str):
        """
        Setter for property: (str) VariantCondition
          a property to get or set the defined string of variant condition   
            
         
        """
        pass
    
    ##  Add a new line to the variant condition
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def AddLine(builder: VariantConditionBuilder) -> None:
        """
         Add a new line to the variant condition
        """
        pass
    
    ##  Delete an existing line from the variant condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def DeleteLine(builder: VariantConditionBuilder) -> None:
        """
         Delete an existing line from the variant condition 
        """
        pass
    
    ##  Move an existing condition one line down in the set of variant condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def MoveDown(builder: VariantConditionBuilder) -> None:
        """
         Move an existing condition one line down in the set of variant condition 
        """
        pass
    
    ##  Move an existing condition one line up in the set of variant condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def MoveUp(builder: VariantConditionBuilder) -> None:
        """
         Move an existing condition one line up in the set of variant condition 
        """
        pass
    
    ##  Replace an existing line with a new condition 
    ## 
    ##   <br>  Created in NX1938.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
    def ReplaceLine(builder: VariantConditionBuilder) -> None:
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def RemoveOperationFromGroup(selectedOperation: List[str]) -> None:
        """
        To remove operation from group
        """
        pass
    
    ##  To set updated Gantt Data
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: alp_planner ("Assembly Line Planner")
    @staticmethod
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
    @staticmethod
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
    def UnAssignWeldPoints(builder: WeldConsistencyCheckerBuilder, selectedWeldPoints: List[NXOpen.NXObject]) -> None:
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


##  @link ModifyVariantBuilderVariantRules NXOpen.ALP.ModifyVariantBuilderVariantRules @endlink is an alias for @link ModifyVariantBuilder.VariantRules NXOpen.ALP.ModifyVariantBuilder.VariantRules@endlink
ModifyVariantBuilderVariantRules = ModifyVariantBuilder.VariantRules


##  @link OperationBuilderOperation NXOpen.ALP.OperationBuilderOperation @endlink is an alias for @link OperationBuilder.Operation NXOpen.ALP.OperationBuilder.Operation@endlink
OperationBuilderOperation = OperationBuilder.Operation


##  @link StationTaktTimeBuilderRadio NXOpen.ALP.StationTaktTimeBuilderRadio @endlink is an alias for @link StationTaktTimeBuilder.Radio NXOpen.ALP.StationTaktTimeBuilder.Radio@endlink
StationTaktTimeBuilderRadio = StationTaktTimeBuilder.Radio


##  @link VariantConditionBuilderCondition NXOpen.ALP.VariantConditionBuilderCondition @endlink is an alias for @link VariantConditionBuilder.Condition NXOpen.ALP.VariantConditionBuilder.Condition@endlink
VariantConditionBuilderCondition = VariantConditionBuilder.Condition


