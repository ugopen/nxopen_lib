from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAE
## 
##         Represents a @link NXOpen::CAE::ModelCheck::AlignBeamElementDirectionBuilder NXOpen::CAE::ModelCheck::AlignBeamElementDirectionBuilder@endlink  builder used to align the Directions of
##         connected beam elements with a seed beam element. You can align the directions by executing either 
##         @link Builder::Commit Builder::Commit@endlink  or @link NXOpen::CAE::ModelCheck::AlignBeamElementDirectionBuilder::AlignDirections NXOpen::CAE::ModelCheck::AlignBeamElementDirectionBuilder::AlignDirections@endlink .
##         The difference between these two methods is @link Builder::Commit Builder::Commit@endlink  aligns the directions
##         and updates direction display, but it does not return the elements that have changed directions.
##         @link NXOpen::CAE::ModelCheck::AlignBeamElementDirectionBuilder::AlignDirections NXOpen::CAE::ModelCheck::AlignBeamElementDirectionBuilder::AlignDirections@endlink  aligns the directions
##         and returns the elements that have changed directions. Both of the methods are only available in fem context.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateAlignBeamElementDirectionBuilder  NXOpen::CAE::ModelCheckManager::CreateAlignBeamElementDirectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class AlignBeamElementDirectionBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder</ja_class> builder used to align the Directions of
        connected beam elements with a seed beam element. You can align the directions by executing either 
        <ja_method>Builder.Commit</ja_method> or <ja_method>NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.AlignDirections</ja_method>.
        The difference between these two methods is <ja_method>Builder.Commit</ja_method> aligns the directions
        and updates direction display, but it does not return the elements that have changed directions.
        <ja_method>NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.AlignDirections</ja_method> aligns the directions
        and returns the elements that have changed directions. Both of the methods are only available in fem context.
        """


    ##   the options to define the connection scope to the seed element for model checking 
    ##  Limits check to only those beam elements in the mesh that contains the Seed Element 
    class ConnectedElementScope(Enum):
        """
        Members Include: <SeedMesh> <AllVisible> <UserSpecified>
        """
        SeedMesh: int
        AllVisible: int
        UserSpecified: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignBeamElementDirectionBuilder.ConnectedElementScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.ConnectedElementScope@endlink) ElementConnectScope
    ##   the option to indicate how to define connected elements for checking   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return AlignBeamElementDirectionBuilder.ConnectedElementScope
    @property
    def ElementConnectScope(self) -> AlignBeamElementDirectionBuilder.ConnectedElementScope:
        """
        Getter for property: (@link AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.ConnectedElementScope@endlink) ElementConnectScope
          the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.ConnectedElementScope@endlink) ElementConnectScope

    ##   the option to indicate how to define connected elements for checking   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ElementConnectScope.setter
    def ElementConnectScope(self, connectScope: AlignBeamElementDirectionBuilder.ConnectedElementScope):
        """
        Setter for property: (@link AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.ConnectedElementScope@endlink) ElementConnectScope
          the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseSeedDirection
    ##   the option indicating whether to reverse element directions so that they are aligned with the seed element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ReverseSeedDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseSeedDirection
          the option indicating whether to reverse element directions so that they are aligned with the seed element   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseSeedDirection

    ##   the option indicating whether to reverse element directions so that they are aligned with the seed element   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReverseSeedDirection.setter
    def ReverseSeedDirection(self, seedDirectionToBeReversed: bool):
        """
        Setter for property: (bool) ReverseSeedDirection
          the option indicating whether to reverse element directions so that they are aligned with the seed element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement
    ##   the seed element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.FEElement
    @property
    def SeedElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement
          the seed element   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement

    ##   the seed element   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SeedElement.setter
    def SeedElement(self, seedElement: NXOpen.CAE.FEElement):
        """
        Setter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement
          the seed element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) UserSpecifiedConnectElements
    ##   the user specified connected elements to be aligned with seed element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.SelectElementsBuilder
    @property
    def UserSpecifiedConnectElements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) UserSpecifiedConnectElements
          the user specified connected elements to be aligned with seed element   
            
         
        """
        pass
    
    ##  Aligns the directions of elements connected to the seed element. Returns the elements
    ##                 that have had the directions successfully reversed. This method will only reverse
    ##                 the directions for beam elements in the current work fem part.
    ##             
    ##  @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def AlignDirections(builder: AlignBeamElementDirectionBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Aligns the directions of elements connected to the seed element. Returns the elements
                        that have had the directions successfully reversed. This method will only reverse
                        the directions for beam elements in the current work fem part.
                    
         @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Display element directions for connected elements, which are to be aligned with seed element direction 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DisplayDirections(builder: AlignBeamElementDirectionBuilder) -> None:
        """
         Display element directions for connected elements, which are to be aligned with seed element direction 
        """
        pass
    
    ##  Finds all visible elements connected with the seed element 
    ##  @return connectedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FindAllVisibleConnectedElements(builder: AlignBeamElementDirectionBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Finds all visible elements connected with the seed element 
         @return connectedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
import NXOpen
import NXOpen.CAE
## 
##         Represents a @link NXOpen::CAE::ModelCheck::AlignShellElementFirstEdgeBuilder NXOpen::CAE::ModelCheck::AlignShellElementFirstEdgeBuilder@endlink  builder used to align the first edges of
##         connected shell elements with a seed element edge.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateAlignShellElementFirstEdgeBuilder  NXOpen::CAE::ModelCheckManager::CreateAlignShellElementFirstEdgeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ElemSelectionMethod </term> <description> 
##  
## ConnectedElementsinSeedMesh </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX12.0.0  <br> 

class AlignShellElementFirstEdgeBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder</ja_class> builder used to align the first edges of
        connected shell elements with a seed element edge.
        """


    ##   the options to define the connection scope to the seed element for model checking 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ConnectedElementsinSeedMesh</term><description> 
    ## </description> </item><item><term> 
    ## AllVisibleConnectedShellElements</term><description> 
    ## </description> </item><item><term> 
    ## SelectedConnectedElements</term><description> 
    ## </description> </item></list>
    class ElemSelectionMode(Enum):
        """
        Members Include: <ConnectedElementsinSeedMesh> <AllVisibleConnectedShellElements> <SelectedConnectedElements>
        """
        ConnectedElementsinSeedMesh: int
        AllVisibleConnectedShellElements: int
        SelectedConnectedElements: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementFirstEdgeBuilder.ElemSelectionMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Direction
    ##   the direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Direction(self) -> bool:
        """
        Getter for property: (bool) Direction
          the direction   
            
         
        """
        pass
    
    ## Setter for property: (bool) Direction

    ##   the direction   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: bool):
        """
        Setter for property: (bool) Direction
          the direction   
            
         
        """
        pass
    
    ## Getter for property: (@link AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder.ElemSelectionMode@endlink) ElemSelectionMethod
    ##   the element selection method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return AlignShellElementFirstEdgeBuilder.ElemSelectionMode
    @property
    def ElemSelectionMethod(self) -> AlignShellElementFirstEdgeBuilder.ElemSelectionMode:
        """
        Getter for property: (@link AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder.ElemSelectionMode@endlink) ElemSelectionMethod
          the element selection method   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder.ElemSelectionMode@endlink) ElemSelectionMethod

    ##   the element selection method   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ElemSelectionMethod.setter
    def ElemSelectionMethod(self, elemSelectionMethod: AlignShellElementFirstEdgeBuilder.ElemSelectionMode):
        """
        Setter for property: (@link AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder.ElemSelectionMode@endlink) ElemSelectionMethod
          the element selection method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) Elements
    ##   the elements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.SelectElementsBuilder
    @property
    def Elements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) Elements
          the elements   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) SeedEdge
    ##   the seed edge   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.SelectElementsBuilder
    @property
    def SeedEdge(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) SeedEdge
          the seed edge   
            
         
        """
        pass
    
    ##  Display first edges for connected elements, which are to be aligned with seed edge 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def DisplayFirstEdges(builder: AlignShellElementFirstEdgeBuilder) -> None:
        """
         Display first edges for connected elements, which are to be aligned with seed edge 
        """
        pass
    
import NXOpen
import NXOpen.CAE
## 
##         Represents a @link NXOpen::CAE::ModelCheck::AlignShellElementNormalBuilder NXOpen::CAE::ModelCheck::AlignShellElementNormalBuilder@endlink  builder used to align the normals of
##         connected shell elements with a seed shell element. You can align the normals by executing either 
##         @link Builder::Commit Builder::Commit@endlink  or @link NXOpen::CAE::ModelCheck::AlignShellElementNormalBuilder::AlignNormals NXOpen::CAE::ModelCheck::AlignShellElementNormalBuilder::AlignNormals@endlink .
##         The difference between these two methods is @link Builder::Commit Builder::Commit@endlink  aligns the normals
##         and updates normal display, but it does not return the elements that have changed normals.
##         @link NXOpen::CAE::ModelCheck::AlignShellElementNormalBuilder::AlignNormals NXOpen::CAE::ModelCheck::AlignShellElementNormalBuilder::AlignNormals@endlink  aligns the normals
##         and returns the elements that have changed normals. Both of the methods are only available in fem context.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateAlignShellElementNormalBuilder  NXOpen::CAE::ModelCheckManager::CreateAlignShellElementNormalBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class AlignShellElementNormalBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder</ja_class> builder used to align the normals of
        connected shell elements with a seed shell element. You can align the normals by executing either 
        <ja_method>Builder.Commit</ja_method> or <ja_method>NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.AlignNormals</ja_method>.
        The difference between these two methods is <ja_method>Builder.Commit</ja_method> aligns the normals
        and updates normal display, but it does not return the elements that have changed normals.
        <ja_method>NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.AlignNormals</ja_method> aligns the normals
        and returns the elements that have changed normals. Both of the methods are only available in fem context.
        """


    ##   the options to define the connection scope to the seed element for model checking 
    ##  Limits check to only those shell elements in the mesh that contains the Seed Element 
    class ConnectedElementScope(Enum):
        """
        Members Include: <SeedMesh> <AllVisible> <UserSpecified>
        """
        SeedMesh: int
        AllVisible: int
        UserSpecified: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementNormalBuilder.ConnectedElementScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  indicates how display type value is defined 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Arrows</term><description> 
    ## </description> </item><item><term> 
    ## SolidFaceColors</term><description> 
    ## </description> </item></list>
    class DisplayTypeValue(Enum):
        """
        Members Include: <Arrows> <SolidFaceColors>
        """
        Arrows: int
        SolidFaceColors: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementNormalBuilder.DisplayTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   the options to define the orient method to orient normal 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UsingSeedElement</term><description> 
    ## </description> </item><item><term> 
    ## Automatic</term><description> 
    ## </description> </item></list>
    class OrientMethodType(Enum):
        """
        Members Include: <UsingSeedElement> <Automatic>
        """
        UsingSeedElement: int
        Automatic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementNormalBuilder.OrientMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType
    ##   the display type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return AlignShellElementNormalBuilder.DisplayTypeValue
    @property
    def DisplayType(self) -> AlignShellElementNormalBuilder.DisplayTypeValue:
        """
        Getter for property: (@link AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType
          the display type   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType

    ##   the display type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DisplayType.setter
    def DisplayType(self, displayType: AlignShellElementNormalBuilder.DisplayTypeValue):
        """
        Setter for property: (@link AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType
          the display type   
            
         
        """
        pass
    
    ## Getter for property: (@link AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.ConnectedElementScope@endlink) ElementConnectScope
    ##   the option to indicate how to define connected elements for checking   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return AlignShellElementNormalBuilder.ConnectedElementScope
    @property
    def ElementConnectScope(self) -> AlignShellElementNormalBuilder.ConnectedElementScope:
        """
        Getter for property: (@link AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.ConnectedElementScope@endlink) ElementConnectScope
          the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.ConnectedElementScope@endlink) ElementConnectScope

    ##   the option to indicate how to define connected elements for checking   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ElementConnectScope.setter
    def ElementConnectScope(self, connectScope: AlignShellElementNormalBuilder.ConnectedElementScope):
        """
        Setter for property: (@link AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.ConnectedElementScope@endlink) ElementConnectScope
          the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ElementSelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##             @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def ElementSelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ElementSelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                    @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ## Getter for property: (int) NegativeFaceColor
    ##   the negative face color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def NegativeFaceColor(self) -> int:
        """
        Getter for property: (int) NegativeFaceColor
          the negative face color   
            
         
        """
        pass
    
    ## Setter for property: (int) NegativeFaceColor

    ##   the negative face color   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @NegativeFaceColor.setter
    def NegativeFaceColor(self, negativeFaceColor: int):
        """
        Setter for property: (int) NegativeFaceColor
          the negative face color   
            
         
        """
        pass
    
    ## Getter for property: (@link AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.OrientMethodType@endlink) OrientMethod
    ##   the option to indicate how to orient method to orient normal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return AlignShellElementNormalBuilder.OrientMethodType
    @property
    def OrientMethod(self) -> AlignShellElementNormalBuilder.OrientMethodType:
        """
        Getter for property: (@link AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.OrientMethodType@endlink) OrientMethod
          the option to indicate how to orient method to orient normal   
            
         
        """
        pass
    
    ## Setter for property: (@link AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.OrientMethodType@endlink) OrientMethod

    ##   the option to indicate how to orient method to orient normal   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OrientMethod.setter
    def OrientMethod(self, orientMethod: AlignShellElementNormalBuilder.OrientMethodType):
        """
        Setter for property: (@link AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.OrientMethodType@endlink) OrientMethod
          the option to indicate how to orient method to orient normal   
            
         
        """
        pass
    
    ## Getter for property: (int) PositiveFaceColor
    ##   the positive face color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def PositiveFaceColor(self) -> int:
        """
        Getter for property: (int) PositiveFaceColor
          the positive face color   
            
         
        """
        pass
    
    ## Setter for property: (int) PositiveFaceColor

    ##   the positive face color   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @PositiveFaceColor.setter
    def PositiveFaceColor(self, positiveFaceColor: int):
        """
        Setter for property: (int) PositiveFaceColor
          the positive face color   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseSeedNormal
    ##   the option indicating whether to reverse element normals so that they are aligned with the seed element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ReverseSeedNormal(self) -> bool:
        """
        Getter for property: (bool) ReverseSeedNormal
          the option indicating whether to reverse element normals so that they are aligned with the seed element   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseSeedNormal

    ##   the option indicating whether to reverse element normals so that they are aligned with the seed element   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReverseSeedNormal.setter
    def ReverseSeedNormal(self, seedNormalToBeReversed: bool):
        """
        Setter for property: (bool) ReverseSeedNormal
          the option indicating whether to reverse element normals so that they are aligned with the seed element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement
    ##   the seed element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.FEElement
    @property
    def SeedElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement
          the seed element   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement

    ##   the seed element   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SeedElement.setter
    def SeedElement(self, seedElement: NXOpen.CAE.FEElement):
        """
        Setter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SeedElement
          the seed element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) UserSpecifiedConnectElements
    ##   the user specified connected elements to be aligned with seed element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.SelectElementsBuilder
    @property
    def UserSpecifiedConnectElements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) UserSpecifiedConnectElements
          the user specified connected elements to be aligned with seed element   
            
         
        """
        pass
    
    ##  Aligns the normals of elements connected to the seed element. Returns the elements
    ##                 that have had the normals successfully reversed. This method will only reverse
    ##                 the normals for shell elements in the current work fem part.
    ##             
    ##  @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def AlignNormals(builder: AlignShellElementNormalBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Aligns the normals of elements connected to the seed element. Returns the elements
                        that have had the normals successfully reversed. This method will only reverse
                        the normals for shell elements in the current work fem part.
                    
         @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
    ##  Display element normals for connected elements, which are to be aligned with seed element normal 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DisplayNormals(builder: AlignShellElementNormalBuilder) -> None:
        """
         Display element normals for connected elements, which are to be aligned with seed element normal 
        """
        pass
    
    ##  Finds all visible elements connected with the seed element 
    ##  @return connectedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FindAllVisibleConnectedElements(builder: AlignShellElementNormalBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Finds all visible elements connected with the seed element 
         @return connectedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
##  the option indicates the check scope for a model check command 
##  check all displayed elements or nodes 
class CheckScope(Enum):
    """
    Members Include: <Displayed> <Selected>
    """
    Displayed: int
    Selected: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CheckScope:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::ModelCheck::CorrectBeamElementsBuilder NXOpen::CAE::ModelCheck::CorrectBeamElementsBuilder@endlink 
##             to check and correct for dangling nodes of 1d elements.
##              <br> 
##             It will check 1D elements for free leg nodes. 
##             If any of the nodes of the 1D element is not connected to any other element, then it will be considered as a free leg node. 
##              <br>            
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateCorrectBeamElementsBuilder  NXOpen::CAE::ModelCheckManager::CreateCorrectBeamElementsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class CorrectBeamElementsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder</ja_class>
            to check and correct for dangling nodes of 1d elements.
            <para>
            It will check 1D elements for free leg nodes. 
            If any of the nodes of the 1D element is not connected to any other element, then it will be considered as a free leg node. 
            </para>           
        """


    ##  Represents the elements to check from 
    ##  All the displayed elements 
    class ElementToCheck(Enum):
        """
        Members Include: <Displayed> <Selected>
        """
        Displayed: int
        Selected: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CorrectBeamElementsBuilder.ElementToCheck:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder.ElementToCheck@endlink) ElemCheckOption
    ##   the element select option .  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return CorrectBeamElementsBuilder.ElementToCheck
    @property
    def ElemCheckOption(self) -> CorrectBeamElementsBuilder.ElementToCheck:
        """
        Getter for property: (@link CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder.ElementToCheck@endlink) ElemCheckOption
          the element select option .  
            
         
        """
        pass
    
    ## Setter for property: (@link CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder.ElementToCheck@endlink) ElemCheckOption

    ##   the element select option .  
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ElemCheckOption.setter
    def ElemCheckOption(self, option: CorrectBeamElementsBuilder.ElementToCheck):
        """
        Setter for property: (@link CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder.ElementToCheck@endlink) ElemCheckOption
          the element select option .  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) ElementSelection
    ##   the selected elements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.SelectElementsBuilder
    @property
    def ElementSelection(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) ElementSelection
          the selected elements   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) NodeToReplace
    ##   the node to replace   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.SelectFENodeList
    @property
    def NodeToReplace(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) NodeToReplace
          the node to replace   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) ReplacementNode
    ##   the replacement node  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.SelectFENodeList
    @property
    def ReplacementNode(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) ReplacementNode
          the replacement node  
            
         
        """
        pass
    
    ##  Correct failed element
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ##  element to correct
    def CorrectFailedElements(builder: CorrectBeamElementsBuilder, failedElement: NXOpen.CAE.FEElement, nodeToReplace: NXOpen.CAE.FENode, replacementNode: NXOpen.CAE.FENode) -> None:
        """
         Correct failed element
        """
        pass
    
    ##  Delete dangling nodes of elements
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ##  elements having dangling nodes
    def DeleteDanglingNodesInElements(builder: CorrectBeamElementsBuilder, failedElement: List[NXOpen.CAE.FEElement]) -> None:
        """
         Delete dangling nodes of elements
        """
        pass
    
    ##  Delete failed elements
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ##  elements to delete
    def DeleteFailedElements(builder: CorrectBeamElementsBuilder, failedElement: List[NXOpen.CAE.FEElement]) -> None:
        """
         Delete failed elements
        """
        pass
    
    ##  Calculate the dangling nodes from selected or displayed elements
    ##  @return failedElement (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  elements having dangling nodes.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def IdentifyFailedElements(builder: CorrectBeamElementsBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Calculate the dangling nodes from selected or displayed elements
         @return failedElement (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  elements having dangling nodes.
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder@endlink 
##             to check for duplicate elements within the candidate elements.
##              <br> 
##             Duplicate elements are elements which share the same corner nodes,but do not include
##             the middle nodes.
##              <br> 
##             The general workflow is:
##             <ol>
##             <li> Set the candidate elements </li>
##             <li> Set the display settings data </li>
##             <li> Identify the duplicate elements </li>
##             <li> Set the preference option </li>
##             <li> Delete the duplicate elements </li>
##             </ol>
##             You can delete duplicate elements through @link Builder::Commit Builder::Commit@endlink  or
##             @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DeleteDuplicateElements NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DeleteDuplicateElements@endlink .
##             Commits the builder to delete duplicate elements.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateDuplicateElementsCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateDuplicateElementsCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class DuplicateElementsCheckBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder</ja_class>
            to check for duplicate elements within the candidate elements.
            <para>
            Duplicate elements are elements which share the same corner nodes,but do not include
            the middle nodes.
            </para>
            The general workflow is:
            <ol>
            <li> Set the candidate elements </li>
            <li> Set the display settings data </li>
            <li> Identify the duplicate elements </li>
            <li> Set the preference option </li>
            <li> Delete the duplicate elements </li>
            </ol>
            You can delete duplicate elements through <ja_method>Builder.Commit</ja_method> or
            <ja_method>NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeleteDuplicateElements</ja_method>.
            Commits the builder to delete duplicate elements.
        """


    ##  Represents the duplicate elements deleting preference 
    ##  Keep the elements with higher labels 
    class DeletePreference(Enum):
        """
        Members Include: <KeepHighLabel> <KeepLowLabel> <KeepSelected> <RemoveSelected>
        """
        KeepHighLabel: int
        KeepLowLabel: int
        KeepSelected: int
        RemoveSelected: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DuplicateElementsCheckBuilder.DeletePreference:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the display settings of duplicated elements detected 
    class DisplaySettings:
        """
         Represents the display settings of duplicated elements detected 
        """
        ## Getter for property :(bool) ShowDuplicateElements
        ## Whether to show duplicate elements
        ## @return bool
        @property
        def ShowDuplicateElements(self) -> bool:
            """
            Getter for property ShowDuplicateElements
            Whether to show duplicate elements

            """
            pass
        
        ## Setter for property :(bool) ShowDuplicateElements
        @ShowDuplicateElements.setter
        def ShowDuplicateElements(self, value: bool):
            """
            Getter for property ShowDuplicateElements
            Whether to show duplicate elements
            Setter for property ShowDuplicateElements
            Whether to show duplicate elements

            """
            pass
        
        ## Getter for property :(bool) ShowElementLabels
        ## Whether to show labels of duplicate elements
        ## @return bool
        @property
        def ShowElementLabels(self) -> bool:
            """
            Getter for property ShowElementLabels
            Whether to show labels of duplicate elements

            """
            pass
        
        ## Setter for property :(bool) ShowElementLabels
        @ShowElementLabels.setter
        def ShowElementLabels(self, value: bool):
            """
            Getter for property ShowElementLabels
            Whether to show labels of duplicate elements
            Setter for property ShowElementLabels
            Whether to show labels of duplicate elements

            """
            pass
        
        ## Getter for property :(int) ElementsColor
        ## The display color of duplicate elements
        ## @return int
        @property
        def ElementsColor(self) -> int:
            """
            Getter for property ElementsColor
            The display color of duplicate elements

            """
            pass
        
        ## Setter for property :(int) ElementsColor
        @ElementsColor.setter
        def ElementsColor(self, value: int):
            """
            Getter for property ElementsColor
            The display color of duplicate elements
            Setter for property ElementsColor
            The display color of duplicate elements

            """
            pass
        
        ## Getter for property :(@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) ElementsWidth
        ## The display line width of duplicate elements
        ## @return @link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink
        @property
        def ElementsWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property ElementsWidth
            The display line width of duplicate elements

            """
            pass
        
        ## Setter for property :(@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) ElementsWidth
        @ElementsWidth.setter
        def ElementsWidth(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property ElementsWidth
            The display line width of duplicate elements
            Setter for property ElementsWidth
            The display line width of duplicate elements

            """
            pass
        
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings@endlink) DisplaySettingsData
    ##   the display settings for duplicate elements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return DuplicateElementsCheckBuilder.DisplaySettings
    @property
    def DisplaySettingsData(self) -> DuplicateElementsCheckBuilder.DisplaySettings:
        """
        Getter for property: (@link DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings@endlink) DisplaySettingsData
          the display settings for duplicate elements   
            
         
        """
        pass
    
    ## Setter for property: (@link DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings@endlink) DisplaySettingsData

    ##   the display settings for duplicate elements   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DisplaySettingsData.setter
    def DisplaySettingsData(self, displaySettings: DuplicateElementsCheckBuilder.DisplaySettings):
        """
        Setter for property: (@link DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings@endlink) DisplaySettingsData
          the display settings for duplicate elements   
            
         
        """
        pass
    
    ## Getter for property: (int) DuplicateElementGroupsCount
    ##   the duplicate elements group count, each group contains elements that are
    ##                 duplicates of each other and each group contains at least two duplicate elements   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def DuplicateElementGroupsCount(self) -> int:
        """
        Getter for property: (int) DuplicateElementGroupsCount
          the duplicate elements group count, each group contains elements that are
                        duplicates of each other and each group contains at least two duplicate elements   
            
         
        """
        pass
    
    ## Getter for property: (@link DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeletePreference@endlink) Preference
    ##   the duplicate elements deleting preference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return DuplicateElementsCheckBuilder.DeletePreference
    @property
    def Preference(self) -> DuplicateElementsCheckBuilder.DeletePreference:
        """
        Getter for property: (@link DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeletePreference@endlink) Preference
          the duplicate elements deleting preference   
            
         
        """
        pass
    
    ## Setter for property: (@link DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeletePreference@endlink) Preference

    ##   the duplicate elements deleting preference   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Preference.setter
    def Preference(self, deletePreference: DuplicateElementsCheckBuilder.DeletePreference):
        """
        Setter for property: (@link DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeletePreference@endlink) Preference
          the duplicate elements deleting preference   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) PreferenceElements
    ##   the preference elements for keep selected and remove selected options   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.SelectElementsBuilder
    @property
    def PreferenceElements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: (@link NXOpen.CAE.SelectElementsBuilder NXOpen.CAE.SelectElementsBuilder@endlink) PreferenceElements
          the preference elements for keep selected and remove selected options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##                 @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                        @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ##  Deletes the duplicate elements and clear all cached duplicate elements in this builder.
    ##                 The method @link Builder::Commit Builder::Commit@endlink  will also do the same thing. Duplicate elements
    ##                 can only be deleted when the context part of this builder is a @link NXOpen::CAE::BaseFemPart NXOpen::CAE::BaseFemPart@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def DeleteDuplicateElements(builder: DuplicateElementsCheckBuilder) -> None:
        """
         Deletes the duplicate elements and clear all cached duplicate elements in this builder.
                        The method @link Builder::Commit Builder::Commit@endlink  will also do the same thing. Duplicate elements
                        can only be deleted when the context part of this builder is a @link NXOpen::CAE::BaseFemPart NXOpen::CAE::BaseFemPart@endlink  
        """
        pass
    
    ##  Returns the duplicate elements of specified group index 
    ##  @return duplicateElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="groupIndex"> (int) </param>
    def GetDuplicateElements(builder: DuplicateElementsCheckBuilder, groupIndex: int) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the duplicate elements of specified group index 
         @return duplicateElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink): .
        """
        pass
    
    ##  Calculates to find the duplicate elements and display them in the
    ##                 @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings@endlink .
    ##                 The detected duplicate elements are cached, to access the cached calculation result, you could use
    ##                 @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DuplicateElementGroupsCount NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DuplicateElementGroupsCount@endlink  and
    ##                 @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::GetDuplicateElements NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::GetDuplicateElements@endlink . The previous
    ##                 cached data will be cleaned automatically when you start a new identification. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def IdentifyDuplicateElements(builder: DuplicateElementsCheckBuilder) -> None:
        """
         Calculates to find the duplicate elements and display them in the
                        @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings@endlink .
                        The detected duplicate elements are cached, to access the cached calculation result, you could use
                        @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DuplicateElementGroupsCount NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DuplicateElementGroupsCount@endlink  and
                        @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::GetDuplicateElements NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::GetDuplicateElements@endlink . The previous
                        cached data will be cleaned automatically when you start a new identification. 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder@endlink 
##             to check for duplicate nodes within the candidate nodes.
##              <br> 
##             Duplicate nodes are nodes which distance between each other is less than
##             specific tolerance value and at least one duplicate node can be merged away.
##              <br> 
##             The general workflow is:
##             <ol>
##             <li> Set the candidate nodes </li>
##             <li> Set the check settings and display settings data </li>
##             <li> Identify the duplicate nodes </li>
##             <li> Set the preference option </li>
##             <li> Merge duplicate nodes </li>
##             </ol>
##             You can merge duplicate nodes through @link Builder::Commit Builder::Commit@endlink  or
##             @link NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::MergeDuplicateNodes NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::MergeDuplicateNodes@endlink .
##             Commits the builder to merge duplicate nodes and update the mesh in graphic window.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateDuplicateNodesCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateDuplicateNodesCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class DuplicateNodesCheckBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder</ja_class>
            to check for duplicate nodes within the candidate nodes.
            <para>
            Duplicate nodes are nodes which distance between each other is less than
            specific tolerance value and at least one duplicate node can be merged away.
            </para>
            The general workflow is:
            <ol>
            <li> Set the candidate nodes </li>
            <li> Set the check settings and display settings data </li>
            <li> Identify the duplicate nodes </li>
            <li> Set the preference option </li>
            <li> Merge duplicate nodes </li>
            </ol>
            You can merge duplicate nodes through <ja_method>Builder.Commit</ja_method> or
            <ja_method>NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergeDuplicateNodes</ja_method>.
            Commits the builder to merge duplicate nodes and update the mesh in graphic window.
        """


    ##  Represents the duplicate nodes merging preference 
    ##  List all duplicate node pairs found 
    class ListOption(Enum):
        """
        Members Include: <All> <Mergeable> <Unmergeable>
        """
        All: int
        Mergeable: int
        Unmergeable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DuplicateNodesCheckBuilder.ListOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the duplicate nodes merging preference 
    ##  No preference 
    class MergePreference(Enum):
        """
        Members Include: <NotSet> <KeepHighLabel> <KeepLowLabel> <KeepSelected> <RemoveSelected>
        """
        NotSet: int
        KeepHighLabel: int
        KeepLowLabel: int
        KeepSelected: int
        RemoveSelected: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DuplicateNodesCheckBuilder.MergePreference:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the display settings data 
    class DisplaySettings:
        """
         Represents the display settings data 
        """
        ## Getter for property :(bool) ShowDuplicateNodes
        ## Whether to show duplicate nodes
        ## @return bool
        @property
        def ShowDuplicateNodes(self) -> bool:
            """
            Getter for property ShowDuplicateNodes
            Whether to show duplicate nodes

            """
            pass
        
        ## Setter for property :(bool) ShowDuplicateNodes
        @ShowDuplicateNodes.setter
        def ShowDuplicateNodes(self, value: bool):
            """
            Getter for property ShowDuplicateNodes
            Whether to show duplicate nodes
            Setter for property ShowDuplicateNodes
            Whether to show duplicate nodes

            """
            pass
        
        ## Getter for property :(bool) ShowMergedNodeLabels
        ## Whether to show merged node labels
        ## @return bool
        @property
        def ShowMergedNodeLabels(self) -> bool:
            """
            Getter for property ShowMergedNodeLabels
            Whether to show merged node labels

            """
            pass
        
        ## Setter for property :(bool) ShowMergedNodeLabels
        @ShowMergedNodeLabels.setter
        def ShowMergedNodeLabels(self, value: bool):
            """
            Getter for property ShowMergedNodeLabels
            Whether to show merged node labels
            Setter for property ShowMergedNodeLabels
            Whether to show merged node labels

            """
            pass
        
        ## Getter for property :(bool) ShowRetainedNodeLabels
        ## Whether to show retained node labels
        ## @return bool
        @property
        def ShowRetainedNodeLabels(self) -> bool:
            """
            Getter for property ShowRetainedNodeLabels
            Whether to show retained node labels

            """
            pass
        
        ## Setter for property :(bool) ShowRetainedNodeLabels
        @ShowRetainedNodeLabels.setter
        def ShowRetainedNodeLabels(self, value: bool):
            """
            Getter for property ShowRetainedNodeLabels
            Whether to show retained node labels
            Setter for property ShowRetainedNodeLabels
            Whether to show retained node labels

            """
            pass
        
        ## Getter for property :(int) KeepNodesColor
        ## The kept nodes display color
        ## @return int
        @property
        def KeepNodesColor(self) -> int:
            """
            Getter for property KeepNodesColor
            The kept nodes display color

            """
            pass
        
        ## Setter for property :(int) KeepNodesColor
        @KeepNodesColor.setter
        def KeepNodesColor(self, value: int):
            """
            Getter for property KeepNodesColor
            The kept nodes display color
            Setter for property KeepNodesColor
            The kept nodes display color

            """
            pass
        
        ## Getter for property :(int) MergeNodesColor
        ## The merged nodes display color
        ## @return int
        @property
        def MergeNodesColor(self) -> int:
            """
            Getter for property MergeNodesColor
            The merged nodes display color

            """
            pass
        
        ## Setter for property :(int) MergeNodesColor
        @MergeNodesColor.setter
        def MergeNodesColor(self, value: int):
            """
            Getter for property MergeNodesColor
            The merged nodes display color
            Setter for property MergeNodesColor
            The merged nodes display color

            """
            pass
        
        ## Getter for property :(int) UnableToMergeNodesColor@return int
        @property
        def UnableToMergeNodesColor(self) -> int:
            """
            Getter for property UnableToMergeNodesColor
            """
            pass
        
        ## Setter for property :(int) UnableToMergeNodesColor
        @UnableToMergeNodesColor.setter
        def UnableToMergeNodesColor(self, value: int):
            """
            Getter for property UnableToMergeNodesColorSetter for property UnableToMergeNodesColor
            """
            pass
        
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings@endlink) DisplaySettingsData
    ##   the display settings for duplicate nodes   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return DuplicateNodesCheckBuilder.DisplaySettings
    @property
    def DisplaySettingsData(self) -> DuplicateNodesCheckBuilder.DisplaySettings:
        """
        Getter for property: (@link DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings@endlink) DisplaySettingsData
          the display settings for duplicate nodes   
            
         
        """
        pass
    
    ## Setter for property: (@link DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings@endlink) DisplaySettingsData

    ##   the display settings for duplicate nodes   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DisplaySettingsData.setter
    def DisplaySettingsData(self, displaySettings: DuplicateNodesCheckBuilder.DisplaySettings):
        """
        Setter for property: (@link DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings@endlink) DisplaySettingsData
          the display settings for duplicate nodes   
            
         
        """
        pass
    
    ## Getter for property: (int) DuplicateNodeGroupsCount
    ##   the duplicate nodes group count, each group contains nodes that are
    ##                 duplicates of each other and each group contains at least two duplicate nodes   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def DuplicateNodeGroupsCount(self) -> int:
        """
        Getter for property: (int) DuplicateNodeGroupsCount
          the duplicate nodes group count, each group contains nodes that are
                        duplicates of each other and each group contains at least two duplicate nodes   
            
         
        """
        pass
    
    ## Getter for property: (bool) IgnoreNodesConnectedToTinyEdges
    ##   a value indicating whether to ignore nodes connected to tiny edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IgnoreNodesConnectedToTinyEdges(self) -> bool:
        """
        Getter for property: (bool) IgnoreNodesConnectedToTinyEdges
          a value indicating whether to ignore nodes connected to tiny edges   
            
         
        """
        pass
    
    ## Setter for property: (bool) IgnoreNodesConnectedToTinyEdges

    ##   a value indicating whether to ignore nodes connected to tiny edges   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IgnoreNodesConnectedToTinyEdges.setter
    def IgnoreNodesConnectedToTinyEdges(self, ignoreTinyEdgeNodes: bool):
        """
        Setter for property: (bool) IgnoreNodesConnectedToTinyEdges
          a value indicating whether to ignore nodes connected to tiny edges   
            
         
        """
        pass
    
    ## Getter for property: (bool) IgnoreNodesInSameMesh
    ##   a value indicating whether to ignore nodes in same mesh   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IgnoreNodesInSameMesh(self) -> bool:
        """
        Getter for property: (bool) IgnoreNodesInSameMesh
          a value indicating whether to ignore nodes in same mesh   
            
         
        """
        pass
    
    ## Setter for property: (bool) IgnoreNodesInSameMesh

    ##   a value indicating whether to ignore nodes in same mesh   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IgnoreNodesInSameMesh.setter
    def IgnoreNodesInSameMesh(self, ignoreSameMeshNodes: bool):
        """
        Setter for property: (bool) IgnoreNodesInSameMesh
          a value indicating whether to ignore nodes in same mesh   
            
         
        """
        pass
    
    ## Getter for property: (@link DuplicateNodesCheckBuilder.ListOption NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.ListOption@endlink) ListingType
    ##   an option indicating what information to be listed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return DuplicateNodesCheckBuilder.ListOption
    @property
    def ListingType(self) -> DuplicateNodesCheckBuilder.ListOption:
        """
        Getter for property: (@link DuplicateNodesCheckBuilder.ListOption NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.ListOption@endlink) ListingType
          an option indicating what information to be listed   
            
         
        """
        pass
    
    ## Setter for property: (@link DuplicateNodesCheckBuilder.ListOption NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.ListOption@endlink) ListingType

    ##   an option indicating what information to be listed   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ListingType.setter
    def ListingType(self, listOption: DuplicateNodesCheckBuilder.ListOption):
        """
        Setter for property: (@link DuplicateNodesCheckBuilder.ListOption NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.ListOption@endlink) ListingType
          an option indicating what information to be listed   
            
         
        """
        pass
    
    ## Getter for property: (bool) MergeOccurrenceNodes
    ##   a value indicating whether to merge occurrence nodes in afem context   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def MergeOccurrenceNodes(self) -> bool:
        """
        Getter for property: (bool) MergeOccurrenceNodes
          a value indicating whether to merge occurrence nodes in afem context   
            
         
        """
        pass
    
    ## Setter for property: (bool) MergeOccurrenceNodes

    ##   a value indicating whether to merge occurrence nodes in afem context   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @MergeOccurrenceNodes.setter
    def MergeOccurrenceNodes(self, mergeOccurrenceNodes: bool):
        """
        Setter for property: (bool) MergeOccurrenceNodes
          a value indicating whether to merge occurrence nodes in afem context   
            
         
        """
        pass
    
    ## Getter for property: (@link DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergePreference@endlink) Preference
    ##   the duplicate nodes merging preference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return DuplicateNodesCheckBuilder.MergePreference
    @property
    def Preference(self) -> DuplicateNodesCheckBuilder.MergePreference:
        """
        Getter for property: (@link DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergePreference@endlink) Preference
          the duplicate nodes merging preference   
            
         
        """
        pass
    
    ## Setter for property: (@link DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergePreference@endlink) Preference

    ##   the duplicate nodes merging preference   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Preference.setter
    def Preference(self, mergePreference: DuplicateNodesCheckBuilder.MergePreference):
        """
        Setter for property: (@link DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergePreference@endlink) Preference
          the duplicate nodes merging preference   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) SelectPreferenceNodesList
    ##   the preference nodes select list for keep selected and remove selected options   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.CAE.SelectFENodeList
    @property
    def SelectPreferenceNodesList(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) SelectPreferenceNodesList
          the preference nodes select list for keep selected and remove selected options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects for checking.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##                 @link NXOpen::CAE::FENode NXOpen::CAE::FENode@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects for checking.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                        @link NXOpen::CAE::FENode NXOpen::CAE::FENode@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Tolerance
    ##   the tolerance used to determine if the nodes are duplicates of each other   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Tolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Tolerance
          the tolerance used to determine if the nodes are duplicates of each other   
            
         
        """
        pass
    
    ##  Returns the duplicate nodes of specified group index 
    ##  @return duplicateNodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="groupIndex"> (int) </param>
    def GetDuplicateNodes(builder: DuplicateNodesCheckBuilder, groupIndex: int) -> List[NXOpen.CAE.FENode]:
        """
         Returns the duplicate nodes of specified group index 
         @return duplicateNodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
        """
        pass
    
    ##  Calculates to find the duplicate nodes and display them in
    ##                 @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings@endlink .
    ##                 The detected duplicate nodes are cached, to access the cached calculation result, you could use
    ##                 @link NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::DuplicateNodeGroupsCount NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::DuplicateNodeGroupsCount@endlink  and
    ##                 @link NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::GetDuplicateNodes NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::GetDuplicateNodes@endlink . The previous
    ##                 cached data will be cleaned automatically when you start a new identification. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def IdentifyDuplicateNodes(builder: DuplicateNodesCheckBuilder) -> None:
        """
         Calculates to find the duplicate nodes and display them in
                        @link NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings NXOpen::CAE::ModelCheck::DuplicateElementsCheckBuilder::DisplaySettings@endlink .
                        The detected duplicate nodes are cached, to access the cached calculation result, you could use
                        @link NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::DuplicateNodeGroupsCount NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::DuplicateNodeGroupsCount@endlink  and
                        @link NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::GetDuplicateNodes NXOpen::CAE::ModelCheck::DuplicateNodesCheckBuilder::GetDuplicateNodes@endlink . The previous
                        cached data will be cleaned automatically when you start a new identification. 
        """
        pass
    
    ##  Merges the duplicate nodes and clear all cached duplicate nodes in this builder.
    ##                 The method @link Builder::Commit Builder::Commit@endlink  will also do the same thing. Duplicate nodes
    ##                 can only be merged when the context part of this builder is a @link NXOpen::CAE::BaseFemPart NXOpen::CAE::BaseFemPart@endlink . 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def MergeDuplicateNodes(builder: DuplicateNodesCheckBuilder) -> None:
        """
         Merges the duplicate nodes and clear all cached duplicate nodes in this builder.
                        The method @link Builder::Commit Builder::Commit@endlink  will also do the same thing. Duplicate nodes
                        can only be merged when the context part of this builder is a @link NXOpen::CAE::BaseFemPart NXOpen::CAE::BaseFemPart@endlink . 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::ModelCheck::ElementEdgeCheckBuilder NXOpen::CAE::ModelCheck::ElementEdgeCheckBuilder@endlink  which can be
##             used to detect free element edges or non-manifold edges.
##              <br> 
##             A free edge is any Element edge that is not shared by any other element face (on
##             either 2D or 3D elements ) within the defined scope of the check.
##             A non-manifold edge is any Element edge that is shared more than 2 element faces (on
##             either 2D or 3D elements ) within the defined scope of the check.
##              <br> 
##             The computation scope @link ElementEdgeCheckBuilder::ComputationScope ElementEdgeCheckBuilder::ComputationScope@endlink 
##             will affect on the checking result. The free element edges or non-manifold edges found will
##             be displayed using the display setting @link NXOpen::CAE::ModelCheck::ElementEdgeCheckBuilder::EdgeDisplayStyle NXOpen::CAE::ModelCheck::ElementEdgeCheckBuilder::EdgeDisplayStyle@endlink .
##             You can execute checking through @link Builder::Commit Builder::Commit@endlink  or
##             @link NXOpen::CAE::ModelCheck::ElementEdgeCheckBuilder::ExecuteCheck NXOpen::CAE::ModelCheck::ElementEdgeCheckBuilder::ExecuteCheck@endlink . Commiting the builder
##             performs checking and displays the free edges and non-manifold edges in graphic window.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateElementEdgeCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateElementEdgeCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementEdgeCheckBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder</ja_class> which can be
            used to detect free element edges or non-manifold edges.
            <para>
            A free edge is any Element edge that is not shared by any other element face (on
            either 2D or 3D elements ) within the defined scope of the check.
            A non-manifold edge is any Element edge that is shared more than 2 element faces (on
            either 2D or 3D elements ) within the defined scope of the check.
            </para>
            The computation scope <ja_property_get>ElementEdgeCheckBuilder.ComputationScope</ja_property_get>
            will affect on the checking result. The free element edges or non-manifold edges found will
            be displayed using the display setting <ja_struct>NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle</ja_struct>.
            You can execute checking through <ja_method>Builder.Commit</ja_method> or
            <ja_method>NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.ExecuteCheck</ja_method>. Commiting the builder
            performs checking and displays the free edges and non-manifold edges in graphic window.
        """


    ##  the Scope over which the Computation of free/non-manifold edges with be done 
    ##  Takes all elements in the model into account while computing 
    class Scope(Enum):
        """
        Members Include: <EntireModel> <VisibleModel> <SelectedModels>
        """
        EntireModel: int
        VisibleModel: int
        SelectedModels: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementEdgeCheckBuilder.Scope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the display style of the edges detected 
    class EdgeDisplayStyle:
        """
         the display style of the edges detected 
        """
        ## Getter for property :(@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
        ## line font
        ## @return @link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            line font

            """
            pass
        
        ## Setter for property :(@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            line font
            Setter for property Font
            line font

            """
            pass
        
        ## Getter for property :(@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
        ## line width
        ## @return @link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            line width

            """
            pass
        
        ## Setter for property :(@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            line width
            Setter for property Width
            line width

            """
            pass
        
        ## Getter for property :(int) Color
        ## line color
        ## @return int
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            line color

            """
            pass
        
        ## Setter for property :(int) Color
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            line color
            Setter for property Color
            line color

            """
            pass
        
    
    
    ## Getter for property: (bool) CheckFreeEdges
    ##   the value indicating whether to check free edges or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CheckFreeEdges(self) -> bool:
        """
        Getter for property: (bool) CheckFreeEdges
          the value indicating whether to check free edges or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) CheckFreeEdges

    ##   the value indicating whether to check free edges or not   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CheckFreeEdges.setter
    def CheckFreeEdges(self, checkFreeEdges: bool):
        """
        Setter for property: (bool) CheckFreeEdges
          the value indicating whether to check free edges or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) CheckNonManifoldEdges
    ##   the value indicating whether to check non-manifold edges or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CheckNonManifoldEdges(self) -> bool:
        """
        Getter for property: (bool) CheckNonManifoldEdges
          the value indicating whether to check non-manifold edges or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) CheckNonManifoldEdges

    ##   the value indicating whether to check non-manifold edges or not   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CheckNonManifoldEdges.setter
    def CheckNonManifoldEdges(self, checkNonManifoldEdges: bool):
        """
        Setter for property: (bool) CheckNonManifoldEdges
          the value indicating whether to check non-manifold edges or not   
            
         
        """
        pass
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementEdgeCheckBuilder.Scope NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.Scope@endlink) ComputationScope
    ##   the computation scope   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ElementEdgeCheckBuilder.Scope
    @property
    def ComputationScope(self) -> ElementEdgeCheckBuilder.Scope:
        """
        Getter for property: (@link ElementEdgeCheckBuilder.Scope NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.Scope@endlink) ComputationScope
          the computation scope   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementEdgeCheckBuilder.Scope NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.Scope@endlink) ComputationScope

    ##   the computation scope   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ComputationScope.setter
    def ComputationScope(self, computationScope: ElementEdgeCheckBuilder.Scope):
        """
        Setter for property: (@link ElementEdgeCheckBuilder.Scope NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.Scope@endlink) ComputationScope
          the computation scope   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) FreeEdgeDisplayStyle
    ##   the display style for free edges detected   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ElementEdgeCheckBuilder.EdgeDisplayStyle
    @property
    def FreeEdgeDisplayStyle(self) -> ElementEdgeCheckBuilder.EdgeDisplayStyle:
        """
        Getter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) FreeEdgeDisplayStyle
          the display style for free edges detected   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) FreeEdgeDisplayStyle

    ##   the display style for free edges detected   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @FreeEdgeDisplayStyle.setter
    def FreeEdgeDisplayStyle(self, freeEdgesStyle: ElementEdgeCheckBuilder.EdgeDisplayStyle):
        """
        Setter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) FreeEdgeDisplayStyle
          the display style for free edges detected   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) NonManifoldEdgeDisplayStyle
    ##   the displaying style for non-manifold edges detected   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ElementEdgeCheckBuilder.EdgeDisplayStyle
    @property
    def NonManifoldEdgeDisplayStyle(self) -> ElementEdgeCheckBuilder.EdgeDisplayStyle:
        """
        Getter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) NonManifoldEdgeDisplayStyle
          the displaying style for non-manifold edges detected   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) NonManifoldEdgeDisplayStyle

    ##   the displaying style for non-manifold edges detected   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @NonManifoldEdgeDisplayStyle.setter
    def NonManifoldEdgeDisplayStyle(self, nonManifoldEdgeStyle: ElementEdgeCheckBuilder.EdgeDisplayStyle):
        """
        Setter for property: (@link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink) NonManifoldEdgeDisplayStyle
          the displaying style for non-manifold edges detected   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##                 @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                        @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ##  Finds free edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges@endlink  is set,
    ##                 and non-manifold edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges@endlink  is set,
    ##                 returns the associated elements and output group for free and/or non-manifold element edges.
    ##                 For the associated elements, if both checks are done at the same time, the elements associated to free edges are
    ##                 returned firstly in the list.
    ##              
    ##  @return A tuple consisting of (freeEdges, nonManifoldEdges, assoElems, outputGroup). 
    ##  - freeEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. free element edges .
    ##  - nonManifoldEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. non-manifold element edges .
    ##  - assoElems is: @link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink. associated elements for free and/or non-manifold element edges,
    ##                                                                                          if both checks are done at the same time, the elements associated
    ##                                                                                          to free edges are returned firstly in the list.
    ##                                                                                       .
    ##  - outputGroup is: @link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink. output group for free and/or non-manifold element edges .

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DoCheck(builder: ElementEdgeCheckBuilder) -> Tuple[List[NXOpen.CAE.FEElemEdge], List[NXOpen.CAE.FEElemEdge], List[NXOpen.CAE.FEElement], NXOpen.CAE.CaeGroup]:
        """
         Finds free edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges@endlink  is set,
                        and non-manifold edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges@endlink  is set,
                        returns the associated elements and output group for free and/or non-manifold element edges.
                        For the associated elements, if both checks are done at the same time, the elements associated to free edges are
                        returned firstly in the list.
                     
         @return A tuple consisting of (freeEdges, nonManifoldEdges, assoElems, outputGroup). 
         - freeEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. free element edges .
         - nonManifoldEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. non-manifold element edges .
         - assoElems is: @link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink. associated elements for free and/or non-manifold element edges,
                                                                                                 if both checks are done at the same time, the elements associated
                                                                                                 to free edges are returned firstly in the list.
                                                                                              .
         - outputGroup is: @link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink. output group for free and/or non-manifold element edges .

        """
        pass
    
    ##  Finds free edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges@endlink  is set,
    ##                 and non-manifold edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges@endlink  is set.
    ##                 The method @link Builder::Commit Builder::Commit@endlink  will also do the same thing,
    ##                 but display the element edges instead of returning them.
    ##              
    ##  @return A tuple consisting of (freeEdges, nonManifoldEdges). 
    ##  - freeEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. free element edges .
    ##  - nonManifoldEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. non-manifold element edges .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def ExecuteCheck(builder: ElementEdgeCheckBuilder) -> Tuple[List[NXOpen.CAE.FEElemEdge], List[NXOpen.CAE.FEElemEdge]]:
        """
         Finds free edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckFreeEdges@endlink  is set,
                        and non-manifold edges when @link CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges CAE::ModelCheck::ElementEdgeCheckBuilder::CheckNonManifoldEdges@endlink  is set.
                        The method @link Builder::Commit Builder::Commit@endlink  will also do the same thing,
                        but display the element edges instead of returning them.
                     
         @return A tuple consisting of (freeEdges, nonManifoldEdges). 
         - freeEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. free element edges .
         - nonManifoldEdges is: @link NXOpen.CAE.FEElemEdge List[NXOpen.CAE.FEElemEdge]@endlink. non-manifold element edges .

        """
        pass
    
    ##  Hides or unhides the input meshes 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="hideInputMeshes"> (bool) </param>
    def HideInputMeshes(builder: ElementEdgeCheckBuilder, hideInputMeshes: bool) -> None:
        """
         Hides or unhides the input meshes 
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents a @link NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder@endlink 
##             used to check the material orientation for shell and solid elements.
##             Use @link Builder::Commit Builder::Commit@endlink  to calculate material orientation and to display
##             an orientation vector for each input element.
##             Use @link NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::DoCheck NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::DoCheck@endlink 
##             to calculate the material orientation for each input element and return the orientation vector
##             result. If an element fails when calculating its material orientation,
##             the element will be displayed in red and listed in an information window.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateElementMaterialOrientationCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateElementMaterialOrientationCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementMaterialOrientationCheckBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder</ja_class>
            used to check the material orientation for shell and solid elements.
            Use <ja_method>Builder.Commit</ja_method> to calculate material orientation and to display
            an orientation vector for each input element.
            Use <ja_method>NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.DoCheck</ja_method>
            to calculate the material orientation for each input element and return the orientation vector
            result. If an element fails when calculating its material orientation,
            the element will be displayed in red and listed in an information window.
        """


    ##  the arrowhead display type 
    ##  the arrowheads are shown 
    class MaterialOrientationArrowheadType(Enum):
        """
        Members Include: <ShowArrowHead> <HideArrowHead>
        """
        ShowArrowHead: int
        HideArrowHead: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the solid element display type 
    ##  all solid elements 
    class MaterialOrientationSolidElementDisplayType(Enum):
        """
        Members Include: <SolidAllElements> <SolidExteriorElements>
        """
        SolidAllElements: int
        SolidExteriorElements: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the material orientation type 
    ##  the material orientation of shell element 
    class MaterialOrientationType(Enum):
        """
        Members Include: <Shell> <SolidFirstDirection> <SolidSecondDirection> <SolidThirdDirection>
        """
        Shell: int
        SolidFirstDirection: int
        SolidSecondDirection: int
        SolidThirdDirection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##                 @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                        @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ##   @brief 
    ##                     Will display the data that was calculated with
    ##                     @link NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::RequestData NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::RequestData@endlink  before.
    ##                  
    ## 
    ##  
    ##                 
    ##                     This is what you will see when recording scripts.
    ##                     If you are writing scripts manually, you can use @link Builder::Commit Builder::Commit@endlink ,
    ##                     which is the same as calling both methods in one go.
    ##                  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def Display(builder: ElementMaterialOrientationCheckBuilder) -> None:
        """
          @brief 
                            Will display the data that was calculated with
                            @link NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::RequestData NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::RequestData@endlink  before.
                         
        
         
                        
                            This is what you will see when recording scripts.
                            If you are writing scripts manually, you can use @link Builder::Commit Builder::Commit@endlink ,
                            which is the same as calling both methods in one go.
                         
        """
        pass
    
    ##  Calculates the material orientation vector for input elements and returns the orientation vector result. 
    ##  @return A tuple consisting of (orientation, orientationType, elements). 
    ##  - orientation is: @link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink. material orientation vector .
    ##  - orientationType is: @link ElementMaterialOrientationCheckBuilder.MaterialOrientationType List[NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType]@endlink.
    ##  - elements is: @link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink. the elements associated with the orientation vectors.

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DoCheck(builder: ElementMaterialOrientationCheckBuilder) -> Tuple[List[NXOpen.Vector3d], List[ElementMaterialOrientationCheckBuilder.MaterialOrientationType], List[NXOpen.CAE.FEElement]]:
        """
         Calculates the material orientation vector for input elements and returns the orientation vector result. 
         @return A tuple consisting of (orientation, orientationType, elements). 
         - orientation is: @link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink. material orientation vector .
         - orientationType is: @link ElementMaterialOrientationCheckBuilder.MaterialOrientationType List[NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType]@endlink.
         - elements is: @link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink. the elements associated with the orientation vectors.

        """
        pass
    
    ##  Gets the percentage of how many arrows should be displayed. 
    ##  @return arrowDensity (int): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArrowDensity(builder: ElementMaterialOrientationCheckBuilder) -> int:
        """
         Gets the percentage of how many arrows should be displayed. 
         @return arrowDensity (int): .
        """
        pass
    
    ##  Gets the arrow show through value. 
    ##  @return arrowShowThrough (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArrowShowThrough(builder: ElementMaterialOrientationCheckBuilder) -> bool:
        """
         Gets the arrow show through value. 
         @return arrowShowThrough (bool): .
        """
        pass
    
    ##  Gets the arrowhead display type. 
    ##  @return displayType (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArrowheadDisplayType(builder: ElementMaterialOrientationCheckBuilder) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType:
        """
         Gets the arrowhead display type. 
         @return displayType (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType@endlink): .
        """
        pass
    
    ##  Gets the option value which indicates whether to check for the specified material orientation type. 
    ##  @return checkOrientation (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="orientationType"> (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType@endlink) </param>
    def GetCheckOrientation(builder: ElementMaterialOrientationCheckBuilder, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType) -> bool:
        """
         Gets the option value which indicates whether to check for the specified material orientation type. 
         @return checkOrientation (bool): .
        """
        pass
    
    ##  Gets the option value which indicates whether to set translucency or not. 
    ##  @return checkOrientation (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCheckTranslucency(builder: ElementMaterialOrientationCheckBuilder) -> bool:
        """
         Gets the option value which indicates whether to set translucency or not. 
         @return checkOrientation (bool): .
        """
        pass
    
    ##  Gets the display color of a specified material orientation type. 
    ##  @return color (@link NXOpen.NXColor NXOpen.NXColor@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="orientationType"> (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType@endlink) </param>
    def GetOrientationColor(builder: ElementMaterialOrientationCheckBuilder, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType) -> NXOpen.NXColor:
        """
         Gets the display color of a specified material orientation type. 
         @return color (@link NXOpen.NXColor NXOpen.NXColor@endlink): .
        """
        pass
    
    ##  Gets the solid element display type. 
    ##  @return displayType (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSolidElementDisplayType(builder: ElementMaterialOrientationCheckBuilder) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType:
        """
         Gets the solid element display type. 
         @return displayType (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType@endlink): .
        """
        pass
    
    ##  Gets the translucency value. 
    ##  @return translucencyValue (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTranslucencyValue(builder: ElementMaterialOrientationCheckBuilder) -> int:
        """
         Gets the translucency value. 
         @return translucencyValue (int): .
        """
        pass
    
    ##   @brief 
    ##                     Calculates material orientation vector for input elements and keeps that data internally as a prerequisite
    ##                     to call @link NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::Display NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::Display@endlink  later.
    ##                  
    ## 
    ##  
    ##                 
    ##                     This is what you will see when recording scripts.
    ##                     If you are writing scripts manually, you can use @link Builder::Commit Builder::Commit@endlink ,
    ##                     which is the same as calling both methods in one go.
    ##                  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def RequestData(builder: ElementMaterialOrientationCheckBuilder) -> None:
        """
          @brief 
                            Calculates material orientation vector for input elements and keeps that data internally as a prerequisite
                            to call @link NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::Display NXOpen::CAE::ModelCheck::ElementMaterialOrientationCheckBuilder::Display@endlink  later.
                         
        
         
                        
                            This is what you will see when recording scripts.
                            If you are writing scripts manually, you can use @link Builder::Commit Builder::Commit@endlink ,
                            which is the same as calling both methods in one go.
                         
        """
        pass
    
    ##  Sets the percentage of how many arrows should be displayed. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="arrowDensity"> (int) </param>
    def SetArrowDensity(builder: ElementMaterialOrientationCheckBuilder, arrowDensity: int) -> None:
        """
         Sets the percentage of how many arrows should be displayed. 
        """
        pass
    
    ##  Sets the arrow show through value. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="arrowShowThrough"> (bool) </param>
    def SetArrowShowThrough(builder: ElementMaterialOrientationCheckBuilder, arrowShowThrough: bool) -> None:
        """
         Sets the arrow show through value. 
        """
        pass
    
    ##  Sets the arrowhead display type. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="displayType"> (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType@endlink) </param>
    def SetArrowheadDisplayType(builder: ElementMaterialOrientationCheckBuilder, displayType: ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType) -> None:
        """
         Sets the arrowhead display type. 
        """
        pass
    
    ##  Sets the option value which indicates whether to check for the specified material orientation type. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="orientationType"> (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType@endlink) </param>
    ## <param name="checkOrientation"> (bool) </param>
    def SetCheckOrientation(builder: ElementMaterialOrientationCheckBuilder, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType, checkOrientation: bool) -> None:
        """
         Sets the option value which indicates whether to check for the specified material orientation type. 
        """
        pass
    
    ##  Sets the option value which indicates whether to set translucency or not. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="checkOrientation"> (bool) </param>
    def SetCheckTranslucency(builder: ElementMaterialOrientationCheckBuilder, checkOrientation: bool) -> None:
        """
         Sets the option value which indicates whether to set translucency or not. 
        """
        pass
    
    ##  Sets the display color of a specified material orientation type. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="orientationType"> (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType@endlink) </param>
    ## <param name="color"> (@link NXOpen.NXColor NXOpen.NXColor@endlink) </param>
    def SetOrientationColor(builder: ElementMaterialOrientationCheckBuilder, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType, color: NXOpen.NXColor) -> None:
        """
         Sets the display color of a specified material orientation type. 
        """
        pass
    
    ##  Sets the solid element display type. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="displayType"> (@link ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType@endlink) </param>
    def SetSolidElementDisplayType(builder: ElementMaterialOrientationCheckBuilder, displayType: ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType) -> None:
        """
         Sets the solid element display type. 
        """
        pass
    
    ##  Sets the translucency value. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="translucencyValue"> (int) </param>
    def SetTranslucencyValue(builder: ElementMaterialOrientationCheckBuilder, translucencyValue: int) -> None:
        """
         Sets the translucency value. 
        """
        pass
    
import NXOpen
import NXOpen.CAE
## Represents a @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder@endlink  to
##          perform quality checking on the candidate elements. Set the properties of the 
##         @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink  instance for the
##         current solver language in the CAE part to define the specific quality checks to perform. 
## 
##         Those elements with failed quality check results will be displayed according to the display setting
##         <ja_property_both>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ShowFailedElementsLabel</ja_property_both> and 
##         <ja_property_both>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.FailedElementsColor</ja_property_both>.
## 
##         The report will be generated according to <ja_property_both>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ElementReportFormat</ja_property_both>
## 
##         You can do element quality check by @link Builder::Commit Builder::Commit@endlink  and 
##         @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::ExecuteCheck NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::ExecuteCheck@endlink . 
##         @link Builder::Commit Builder::Commit@endlink  performs the check, displays the failed elements and generates the report 
##         in a listing window. But @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder@endlink  just performs the check and
##         returns the check result @link NXOpen::CAE::ModelCheck::ElementQualityCheckResults NXOpen::CAE::ModelCheck::ElementQualityCheckResults@endlink 
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateElementQualityCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateElementQualityCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementQualityCheckBuilder(NXOpen.Builder): 
    """Represents a <ja_class>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder</ja_class> to
         perform quality checking on the candidate elements. Set the properties of the 
        <ja_class>NXOpen.CAE.ModelCheck.ElementQualitySetting</ja_class> instance for the
        current solver language in the CAE part to define the specific quality checks to perform. 

        Those elements with failed quality check results will be displayed according to the display setting
        <ja_property_both>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ShowFailedElementsLabel</ja_property_both> and 
        <ja_property_both>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.FailedElementsColor</ja_property_both>.

        The report will be generated according to <ja_property_both>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ElementReportFormat</ja_property_both>

        You can do element quality check by <ja_method>Builder.Commit</ja_method> and 
        <ja_method>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ExecuteCheck</ja_method>. 
        <ja_method>Builder.Commit</ja_method> performs the check, displays the failed elements and generates the report 
        in a listing window. But <ja_class>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder</ja_class> just performs the check and
        returns the check result <ja_class>NXOpen.CAE.ModelCheck.ElementQualityCheckResults</ja_class>
        """


    ##  indicates how to create output group 
    ##  Output nothing 
    class OutputElements(Enum):
        """
        Members Include: <NotSet> <Failed> <Warning> <FailedAndWarning>
        """
        NotSet: int
        Failed: int
        Warning: int
        FailedAndWarning: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementQualityCheckBuilder.OutputElements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  indicates how to generate report 
    ##  Does not generate report 
    class ReportFormat(Enum):
        """
        Members Include: <NotSet> <Worst> <Failed> <Warning> <FailedAndWarning> <All>
        """
        NotSet: int
        Worst: int
        Failed: int
        Warning: int
        FailedAndWarning: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementQualityCheckBuilder.ReportFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementQualityCheckBuilder.ReportFormat NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ReportFormat@endlink) ElementReportFormat
    ##   the report style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ElementQualityCheckBuilder.ReportFormat
    @property
    def ElementReportFormat(self) -> ElementQualityCheckBuilder.ReportFormat:
        """
        Getter for property: (@link ElementQualityCheckBuilder.ReportFormat NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ReportFormat@endlink) ElementReportFormat
          the report style   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementQualityCheckBuilder.ReportFormat NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ReportFormat@endlink) ElementReportFormat

    ##   the report style   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ElementReportFormat.setter
    def ElementReportFormat(self, reportElements: ElementQualityCheckBuilder.ReportFormat):
        """
        Setter for property: (@link ElementQualityCheckBuilder.ReportFormat NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ReportFormat@endlink) ElementReportFormat
          the report style   
            
         
        """
        pass
    
    ## Getter for property: (@link ElementQualityCheckBuilder.OutputElements NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.OutputElements@endlink) ElementsOutputOption
    ##   the element output options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ElementQualityCheckBuilder.OutputElements
    @property
    def ElementsOutputOption(self) -> ElementQualityCheckBuilder.OutputElements:
        """
        Getter for property: (@link ElementQualityCheckBuilder.OutputElements NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.OutputElements@endlink) ElementsOutputOption
          the element output options   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementQualityCheckBuilder.OutputElements NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.OutputElements@endlink) ElementsOutputOption

    ##   the element output options   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ElementsOutputOption.setter
    def ElementsOutputOption(self, outputElements: ElementQualityCheckBuilder.OutputElements):
        """
        Setter for property: (@link ElementQualityCheckBuilder.OutputElements NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.OutputElements@endlink) ElementsOutputOption
          the element output options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedElementsColor
    ##   the display color of failed elements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FailedElementsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedElementsColor
          the display color of failed elements   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedElementsColor

    ##   the display color of failed elements   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @FailedElementsColor.setter
    def FailedElementsColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedElementsColor
          the display color of failed elements   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.NumberFormat NXOpen.CAE.NumberFormat@endlink) NumberFormat
    ##   the number format option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.CAE.NumberFormat
    @property
    def NumberFormat(self) -> NXOpen.CAE.NumberFormat:
        """
        Getter for property: (@link NXOpen.CAE.NumberFormat NXOpen.CAE.NumberFormat@endlink) NumberFormat
          the number format option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##                 @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                        @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ## Getter for property: (bool) ShowFailedElementsLabel
    ##   the value indicating whether to show label for those failed elements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def ShowFailedElementsLabel(self) -> bool:
        """
        Getter for property: (bool) ShowFailedElementsLabel
          the value indicating whether to show label for those failed elements   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFailedElementsLabel

    ##   the value indicating whether to show label for those failed elements   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ShowFailedElementsLabel.setter
    def ShowFailedElementsLabel(self, showFailedElementsLabel: bool):
        """
        Setter for property: (bool) ShowFailedElementsLabel
          the value indicating whether to show label for those failed elements   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WarningElementsColor
    ##   the display color of warning elements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def WarningElementsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WarningElementsColor
          the display color of warning elements   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WarningElementsColor

    ##   the display color of warning elements   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @WarningElementsColor.setter
    def WarningElementsColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WarningElementsColor
          the display color of warning elements   
            
         
        """
        pass
    
    ##  Attempt fixing the element quality of failed elements for given test types 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="testTypes"> (@link TestValueTypes.TestType List[NXOpen.CAE.ModelCheck.TestValueTypes.TestType]@endlink) </param>
    def AttemptFixFailingElements(eqcBuilder: ElementQualityCheckBuilder, testTypes: List[TestValueTypes.TestType]) -> None:
        """
         Attempt fixing the element quality of failed elements for given test types 
        """
        pass
    
    ##  Attempt fixing the element quality of failed selected elements for given test types 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="testTypes"> (@link TestValueTypes.TestType List[NXOpen.CAE.ModelCheck.TestValueTypes.TestType]@endlink) </param>
    ## <param name="elements"> (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink) </param>
    def AttemptFixFailingSelectedElements(eqcBuilder: ElementQualityCheckBuilder, testTypes: List[TestValueTypes.TestType], elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Attempt fixing the element quality of failed selected elements for given test types 
        """
        pass
    
    ##   @brief 
    ##                 Returns the results after performing element quality check on the target elements or meshes,
    ##                 and displays the warned and/or failed elements.
    ##                  
    ## 
    ##  
    ##                 
    ##                 <ol>
    ##                 <li>
    ##                 The target elements or meshes are set by calling @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SelectionList NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SelectionList@endlink 
    ##                 </li>
    ##                 <li>
    ##                 You could also use @link Builder::Commit Builder::Commit@endlink  to do the check,
    ##                 the differences are that @link Builder::Commit Builder::Commit@endlink  generates the report to listing window but does not return the results.
    ##                 </li>
    ##                 </ol>
    ##                 
    ##             
    ##  @return checkResults (@link ElementQualityCheckResults NXOpen.CAE.ModelCheck.ElementQualityCheckResults@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def ExecuteCheck(builder: ElementQualityCheckBuilder) -> ElementQualityCheckResults:
        """
          @brief 
                        Returns the results after performing element quality check on the target elements or meshes,
                        and displays the warned and/or failed elements.
                         
        
         
                        
                        <ol>
                        <li>
                        The target elements or meshes are set by calling @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SelectionList NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SelectionList@endlink 
                        </li>
                        <li>
                        You could also use @link Builder::Commit Builder::Commit@endlink  to do the check,
                        the differences are that @link Builder::Commit Builder::Commit@endlink  generates the report to listing window but does not return the results.
                        </li>
                        </ol>
                        
                    
         @return checkResults (@link ElementQualityCheckResults NXOpen.CAE.ModelCheck.ElementQualityCheckResults@endlink): .
        """
        pass
    
    ##   @brief 
    ##                 Writes the element quality check results into a text file.
    ##                  
    ## 
    ##  
    ##                 
    ##                 <ol>
    ##                 <li>
    ##                 The text file is overriden with the element quality check results if it already exists.
    ##                 </li>
    ##                 <li>
    ##                 @link NXOpen::CAE::ModelCheck::ElementQualityCheckResults NXOpen::CAE::ModelCheck::ElementQualityCheckResults@endlink  are generated by calling
    ##                 @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::ExecuteCheck NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::ExecuteCheck@endlink .
    ##                 </li>
    ##                 <li>
    ##                 The settings of @link NXOpen::CAE::NumberFormat NXOpen::CAE::NumberFormat@endlink  can be changed after calling
    ##                 @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::NumberFormat NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::NumberFormat@endlink .
    ##                 </li>
    ##                 <li>
    ##                 The report format can be changed with @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SetElementReportFormat NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SetElementReportFormat@endlink .
    ##                 </li>
    ##                 </ol>
    ##                 
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="outputFile"> (str) </param>
    ## <param name="eqcResults"> (@link ElementQualityCheckResults NXOpen.CAE.ModelCheck.ElementQualityCheckResults@endlink) </param>
    def WriteResultsToFile(eqcBuilder: ElementQualityCheckBuilder, outputFile: str, eqcResults: ElementQualityCheckResults) -> None:
        """
          @brief 
                        Writes the element quality check results into a text file.
                         
        
         
                        
                        <ol>
                        <li>
                        The text file is overriden with the element quality check results if it already exists.
                        </li>
                        <li>
                        @link NXOpen::CAE::ModelCheck::ElementQualityCheckResults NXOpen::CAE::ModelCheck::ElementQualityCheckResults@endlink  are generated by calling
                        @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::ExecuteCheck NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::ExecuteCheck@endlink .
                        </li>
                        <li>
                        The settings of @link NXOpen::CAE::NumberFormat NXOpen::CAE::NumberFormat@endlink  can be changed after calling
                        @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::NumberFormat NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::NumberFormat@endlink .
                        </li>
                        <li>
                        The report format can be changed with @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SetElementReportFormat NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder::SetElementReportFormat@endlink .
                        </li>
                        </ol>
                        
                    
        """
        pass
    
import NXOpen
##  Represents the element quality checking result of @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder@endlink 
##      <br> To obtain an instance of this class use CAE.ModelCheck.ElementQualityCheckBuilder  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementQualityCheckResults(NXOpen.TransientObject): 
    """ Represents the element quality checking result of <ja_class>NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder</ja_class>
    """


    ##  Reprents the summary data of a specified quality checking test type 
    class TestSummary:
        """
         Reprents the summary data of a specified quality checking test type 
        """
        ## Getter for property :(@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink) TestType
        ## the test type
        ## @return @link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink
        @property
        def TestType(self) -> TestValueTypes.TestType:
            """
            Getter for property TestType
            the test type

            """
            pass
        
        ## Setter for property :(@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink) TestType
        @TestType.setter
        def TestType(self, value: TestValueTypes.TestType):
            """
            Getter for property TestType
            the test type
            Setter for property TestType
            the test type

            """
            pass
        
        ## Getter for property :(float) WorstTestValue
        ## the worst test value of the specified test within all checked elements.
        ## @return float
        @property
        def WorstTestValue(self) -> float:
            """
            Getter for property WorstTestValue
            the worst test value of the specified test within all checked elements.

            """
            pass
        
        ## Setter for property :(float) WorstTestValue
        @WorstTestValue.setter
        def WorstTestValue(self, value: float):
            """
            Getter for property WorstTestValue
            the worst test value of the specified test within all checked elements.
            Setter for property WorstTestValue
            the worst test value of the specified test within all checked elements.

            """
            pass
        
        ## Getter for property :(bool) HasTestValue
        ## indicates whether the test has a test value.
        ## @return bool
        @property
        def HasTestValue(self) -> bool:
            """
            Getter for property HasTestValue
            indicates whether the test has a test value.

            """
            pass
        
        ## Setter for property :(bool) HasTestValue
        @HasTestValue.setter
        def HasTestValue(self, value: bool):
            """
            Getter for property HasTestValue
            indicates whether the test has a test value.
            Setter for property HasTestValue
            indicates whether the test has a test value.

            """
            pass
        
        ## Getter for property :(int) TestCount
        ## indicates the total number of elements tested for this test
        ## @return int
        @property
        def TestCount(self) -> int:
            """
            Getter for property TestCount
            indicates the total number of elements tested for this test

            """
            pass
        
        ## Setter for property :(int) TestCount
        @TestCount.setter
        def TestCount(self, value: int):
            """
            Getter for property TestCount
            indicates the total number of elements tested for this test
            Setter for property TestCount
            indicates the total number of elements tested for this test

            """
            pass
        
        ## Getter for property :(int) ErrorCount
        ## the count of elements with error results
        ## @return int
        @property
        def ErrorCount(self) -> int:
            """
            Getter for property ErrorCount
            the count of elements with error results

            """
            pass
        
        ## Setter for property :(int) ErrorCount
        @ErrorCount.setter
        def ErrorCount(self, value: int):
            """
            Getter for property ErrorCount
            the count of elements with error results
            Setter for property ErrorCount
            the count of elements with error results

            """
            pass
        
        ## Getter for property :(int) WarnedCount
        ## the count of elements with warning results.
        ## @return int
        @property
        def WarnedCount(self) -> int:
            """
            Getter for property WarnedCount
            the count of elements with warning results.

            """
            pass
        
        ## Setter for property :(int) WarnedCount
        @WarnedCount.setter
        def WarnedCount(self, value: int):
            """
            Getter for property WarnedCount
            the count of elements with warning results.
            Setter for property WarnedCount
            the count of elements with warning results.

            """
            pass
        
    
    
    ## Getter for property: (int) ElementTestCount
    ##   the total number of element tested during a test session   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def ElementTestCount(self) -> int:
        """
        Getter for property: (int) ElementTestCount
          the total number of element tested during a test session   
            
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Returns test results of each element. Caller needs to free the memory of the test result by @link NXOpen::CAE::ModelCheck::ElementTestResult::JA_EQ_ELEM_RESULT_Dispose NXOpen::CAE::ModelCheck::ElementTestResult::JA_EQ_ELEM_RESULT_Dispose@endlink .
    ##  @return elementResult (@link ElementTestResult NXOpen.CAE.ModelCheck.ElementTestResult@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetElementTestResultByIndex(self, index: int) -> ElementTestResult:
        """
         Returns test results of each element. Caller needs to free the memory of the test result by @link NXOpen::CAE::ModelCheck::ElementTestResult::JA_EQ_ELEM_RESULT_Dispose NXOpen::CAE::ModelCheck::ElementTestResult::JA_EQ_ELEM_RESULT_Dispose@endlink .
         @return elementResult (@link ElementTestResult NXOpen.CAE.ModelCheck.ElementTestResult@endlink): .
        """
        pass
    
    ##  Returns summary data of tests executed by @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder@endlink 
    ##  @return testSummaries (@link ElementQualityCheckResults.TestSummary List[NXOpen.CAE.ModelCheck.ElementQualityCheckResults.TestSummary]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetTestSummary(self) -> List[ElementQualityCheckResults.TestSummary]:
        """
         Returns summary data of tests executed by @link NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder NXOpen::CAE::ModelCheck::ElementQualityCheckBuilder@endlink 
         @return testSummaries (@link ElementQualityCheckResults.TestSummary List[NXOpen.CAE.ModelCheck.ElementQualityCheckResults.TestSummary]@endlink): .
        """
        pass
    
import NXOpen
##   @brief Represents a collection of @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink  in a cae part.  
## 
##    <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaePart  NXOpen::CAE::CaePart @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementQualitySettingCollection(NXOpen.TaggedObjectCollection): 
    """ <summary>Represents a collection of <ja_class>NXOpen.CAE.ModelCheck.ElementQualitySetting</ja_class> in a cae part. </summary> """


    ##  Finds the @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink  with the given identifier as
    ##             recorded in a journal. An exception will be thrown if no object can be found with the given
    ##             journal identifier 
    ##         
    ##  @return found (@link ElementQualitySetting NXOpen.CAE.ModelCheck.ElementQualitySetting@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  
    def FindObject(part: ElementQualitySettingCollection, journalIdentifier: str) -> ElementQualitySetting:
        """
         Finds the @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink  with the given identifier as
                    recorded in a journal. An exception will be thrown if no object can be found with the given
                    journal identifier 
                
         @return found (@link ElementQualitySetting NXOpen.CAE.ModelCheck.ElementQualitySetting@endlink):  .
        """
        pass
    
    ##  Retuns the @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink  of a specified solver. 
    ##  @return pEQValues (@link ElementQualitySetting NXOpen.CAE.ModelCheck.ElementQualitySetting@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="solverName"> (str) </param>
    def GetElementQualitySetting(part: ElementQualitySettingCollection, solverName: str) -> ElementQualitySetting:
        """
         Retuns the @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink  of a specified solver. 
         @return pEQValues (@link ElementQualitySetting NXOpen.CAE.ModelCheck.ElementQualitySetting@endlink):  .
        """
        pass
    
import NXOpen
import NXOpen.CAE
## 
##      @brief 
## 
##     Represents element quality check settings of a specified solver language. Each solve language has a
##     @link NXOpen::CAE::ModelCheck::ElementQualitySetting NXOpen::CAE::ModelCheck::ElementQualitySetting@endlink .
## 
##     To get a quality check criteria value of a specfied quality test for one element, you can call
##     @link NXOpen::CAE::ModelCheck::ElementQualitySetting::LocateTestDescriptorName NXOpen::CAE::ModelCheck::ElementQualitySetting::LocateTestDescriptorName@endlink  to get the test
##     criteria value name, then call @link NXOpen::CAE::ModelCheck::ElementQualitySetting::GetQualityValue NXOpen::CAE::ModelCheck::ElementQualitySetting::GetQualityValue@endlink  to
##     get the criteria value object.
## 
## 
##      
## 
##  
##      <br> Not to support KF  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementQualitySetting(NXOpen.NXObject): 
    """
    <summary>

    Represents element quality check settings of a specified solver language. Each solve language has a
    <ja_class>NXOpen.CAE.ModelCheck.ElementQualitySetting</ja_class>.

    To get a quality check criteria value of a specfied quality test for one element, you can call
    <ja_method>NXOpen.CAE.ModelCheck.ElementQualitySetting.LocateTestDescriptorName</ja_method> to get the test
    criteria value name, then call <ja_method>NXOpen.CAE.ModelCheck.ElementQualitySetting.GetQualityValue</ja_method> to
    get the criteria value object.


    </summary>
    """


    ##  indicates how criteria value is defined 
    ##  Both warning and error criteria value could be defined  
    class LimitValue(Enum):
        """
        Members Include: <WarningAndErrorLimit> <ErrorLimitOnly> <ExtendedOptions>
        """
        WarningAndErrorLimit: int
        ErrorLimitOnly: int
        ExtendedOptions: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElementQualitySetting.LimitValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ElementQualitySetting.LimitValue NXOpen.CAE.ModelCheck.ElementQualitySetting.LimitValue@endlink) LimitValueOption
    ##   the limit value option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return ElementQualitySetting.LimitValue
    @property
    def LimitValueOption(self) -> ElementQualitySetting.LimitValue:
        """
        Getter for property: (@link ElementQualitySetting.LimitValue NXOpen.CAE.ModelCheck.ElementQualitySetting.LimitValue@endlink) LimitValueOption
          the limit value option   
            
         
        """
        pass
    
    ## Setter for property: (@link ElementQualitySetting.LimitValue NXOpen.CAE.ModelCheck.ElementQualitySetting.LimitValue@endlink) LimitValueOption

    ##   the limit value option   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @LimitValueOption.setter
    def LimitValueOption(self, limitValueOption: ElementQualitySetting.LimitValue):
        """
        Setter for property: (@link ElementQualitySetting.LimitValue NXOpen.CAE.ModelCheck.ElementQualitySetting.LimitValue@endlink) LimitValueOption
          the limit value option   
            
         
        """
        pass
    
    ## Getter for property: (int) TestValueCount
    ##   the count of @link NXOpen::CAE::ModelCheck::QualityTestValue NXOpen::CAE::ModelCheck::QualityTestValue@endlink  in the setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def TestValueCount(self) -> int:
        """
        Getter for property: (int) TestValueCount
          the count of @link NXOpen::CAE::ModelCheck::QualityTestValue NXOpen::CAE::ModelCheck::QualityTestValue@endlink  in the setting   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseElementSpecificValue
    ##   an option indicating whether to use element specific quality value for testing   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def UseElementSpecificValue(self) -> bool:
        """
        Getter for property: (bool) UseElementSpecificValue
          an option indicating whether to use element specific quality value for testing   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseElementSpecificValue

    ##   an option indicating whether to use element specific quality value for testing   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @UseElementSpecificValue.setter
    def UseElementSpecificValue(self, useElementSpecificValue: bool):
        """
        Setter for property: (bool) UseElementSpecificValue
          an option indicating whether to use element specific quality value for testing   
            
         
        """
        pass
    
    ##  Returns the test quality value with the specified descriptor name 
    ##  @return qualityValue (@link ITestValue NXOpen.CAE.ModelCheck.ITestValue@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="descriptorName"> (str) </param>
    def GetQualityValue(self, descriptorName: str) -> ITestValue:
        """
         Returns the test quality value with the specified descriptor name 
         @return qualityValue (@link ITestValue NXOpen.CAE.ModelCheck.ITestValue@endlink): .
        """
        pass
    
    ## Returns the @link NXOpen::CAE::ModelCheck::QualityTestValue NXOpen::CAE::ModelCheck::QualityTestValue@endlink  at the specified index in the setting  
    ##  @return pTestValue (@link QualityTestValue NXOpen.CAE.ModelCheck.QualityTestValue@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  
    def GetTestValueByIndex(self, index: int) -> QualityTestValue:
        """
        Returns the @link NXOpen::CAE::ModelCheck::QualityTestValue NXOpen::CAE::ModelCheck::QualityTestValue@endlink  at the specified index in the setting  
         @return pTestValue (@link QualityTestValue NXOpen.CAE.ModelCheck.QualityTestValue@endlink):  .
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::ModelCheck::QualityTestValue NXOpen::CAE::ModelCheck::QualityTestValue@endlink  of a specified @link NXOpen::CAE::ModelCheck::TestValueTypes::TestType NXOpen::CAE::ModelCheck::TestValueTypes::TestType@endlink  
    ##  @return pTestValue (@link QualityTestValue NXOpen.CAE.ModelCheck.QualityTestValue@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="testType"> (@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink) </param>
    def GetTestValueByType(self, testType: TestValueTypes.TestType) -> QualityTestValue:
        """
         Returns the @link NXOpen::CAE::ModelCheck::QualityTestValue NXOpen::CAE::ModelCheck::QualityTestValue@endlink  of a specified @link NXOpen::CAE::ModelCheck::TestValueTypes::TestType NXOpen::CAE::ModelCheck::TestValueTypes::TestType@endlink  
         @return pTestValue (@link QualityTestValue NXOpen.CAE.ModelCheck.QualityTestValue@endlink): .
        """
        pass
    
    ##  Returns the name of a quality test value, which is associated with
    ##             an element for a specified test type 
    ##  @return descriptorName (str): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="element"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    ## <param name="testType"> (@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink) </param>
    ## <param name="useElemSpecific"> (bool) </param>
    def LocateTestDescriptorName(self, element: NXOpen.CAE.FEElement, testType: TestValueTypes.TestType, useElemSpecific: bool) -> str:
        """
         Returns the name of a quality test value, which is associated with
                    an element for a specified test type 
         @return descriptorName (str): .
        """
        pass
    
    ##  Reset the quality check setting as customer default 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def ResetToCustomerDefault(self) -> None:
        """
         Reset the quality check setting as customer default 
        """
        pass
    
import NXOpen
##   @brief  Represents the quality setting for a specfied element reference  
## 
##    <br> Not to support KF  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementSpecificTestValue(NXOpen.NXObject): 
    """ <summary> Represents the quality setting for a specfied element reference </summary> """


    ## Getter for property: (bool) DoTest
    ##   an option value indicating whether to do element quality check for this test    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def DoTest(self) -> bool:
        """
        Getter for property: (bool) DoTest
          an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    
    ## Setter for property: (bool) DoTest

    ##   an option value indicating whether to do element quality check for this test    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DoTest.setter
    def DoTest(self, doTest: bool):
        """
        Setter for property: (bool) DoTest
          an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    
import NXOpen
import NXOpen.CAE
##  Represents quality checking result for an element.   <br> To obtain an instance of this class use CAE.ModelCheck.ElementQualityCheckResults.GetElementTestResults  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ElementTestResult(NXOpen.TransientObject): 
    """ Represents quality checking result for an element.  """


    ## Getter for property: (@link TestValueTypes.Result NXOpen.CAE.ModelCheck.TestValueTypes.Result@endlink) OverallResult
    ##   the overall result of this element.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return TestValueTypes.Result
    @property
    def OverallResult(self) -> TestValueTypes.Result:
        """
        Getter for property: (@link TestValueTypes.Result NXOpen.CAE.ModelCheck.TestValueTypes.Result@endlink) OverallResult
          the overall result of this element.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Returns the element associated with quality test results 
    ##  @return pElementTag (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink): .
    ## 
    ##   <br>  Created in NX1961.0.0  <br> 

    ## License requirements: None.
    def GetTestElement(self) -> NXOpen.CAE.FEElement:
        """
         Returns the element associated with quality test results 
         @return pElementTag (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink): .
        """
        pass
    
    ##  Returns the quality test results of this element 
    ##  @return testResults (@link TestResult List[NXOpen.CAE.ModelCheck.TestResult]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetTestResults(self) -> List[TestResult]:
        """
         Returns the quality test results of this element 
         @return testResults (@link TestResult List[NXOpen.CAE.ModelCheck.TestResult]@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
## Represents a @link NXOpen::CAE::ModelCheck::FaceClearanceCheckBuilder NXOpen::CAE::ModelCheck::FaceClearanceCheckBuilder@endlink  to perform polygon face
##     interference or clearance check. You can do the check by @link Builder::Commit Builder::Commit@endlink  or 
##     @link NXOpen::CAE::ModelCheck::FaceClearanceCheckBuilder::DoCheck NXOpen::CAE::ModelCheck::FaceClearanceCheckBuilder::DoCheck@endlink . @link Builder::Commit Builder::Commit@endlink 
##     performs the check and displays the failed faces in graphics window. @link NXOpen::CAE::ModelCheck::FaceClearanceCheckBuilder::DoCheck NXOpen::CAE::ModelCheck::FaceClearanceCheckBuilder::DoCheck@endlink 
##     performs the check and if faces are detected violating the check, returns the output group containing the failed faces.
##      <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateFaceClearanceCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateFaceClearanceCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class FaceClearanceCheckBuilder(NXOpen.Builder): 
    """Represents a <ja_class>NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder</ja_class> to perform polygon face
    interference or clearance check. You can do the check by <ja_method>Builder.Commit</ja_method> or 
    <ja_method>NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder.DoCheck</ja_method>. <ja_method>Builder.Commit</ja_method>
    performs the check and displays the failed faces in graphics window. <ja_method>NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder.DoCheck</ja_method>
    performs the check and if faces are detected violating the check, returns the output group containing the failed faces.
    """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Clearance
    ##   the clearance.  
    ##    If the clearance value is zero, an intersection check between faces will be
    ##         performed. If the clearance value is non-zero, a clearance check will be performed. If a negative
    ##         non-zero clearance is set, the absolute value will be used   
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Clearance
          the clearance.  
           If the clearance value is zero, an intersection check between faces will be
                performed. If the clearance value is non-zero, a clearance check will be performed. If a negative
                non-zero clearance is set, the absolute value will be used   
         
        """
        pass
    
    ##  Perform the clearance check. All polygon faces on the current display are considered for
    ##         the check. If polygon faces are detected as intersecting or violating the given clearance, they
    ##         are placed in a group, which would be returned 
    ##  @return faceSet (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink):  the group contains the failed faces .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def DoCheck(builder: FaceClearanceCheckBuilder) -> NXOpen.CAE.CaeGroup:
        """
         Perform the clearance check. All polygon faces on the current display are considered for
                the check. If polygon faces are detected as intersecting or violating the given clearance, they
                are placed in a group, which would be returned 
         @return faceSet (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink):  the group contains the failed faces .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  Represents the iterface of solver element quality checker which calculate all kinds of element quality check results.  
## 
##   
## 
##   <br>  Created in NX1965.0.0  <br> 

class IElementQualityChecker(NXOpen.TransientObject): 
    """ <summary> Represents the iterface of solver element quality checker which calculate all kinds of element quality check results. </summary> """


    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(eqChecker: IElementQualityChecker) -> None:
        """
         Destroys the object. 
        """
        pass
    
    ##  Gets area value for 2D element face. 
    ##  @return pArea (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetArea(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets area value for 2D element face. 
         @return pArea (float): .
        """
        pass
    
    ##  Gets aspect ratio value. 
    ##  @return pAspectRatio (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetAspectRatio(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets aspect ratio value. 
         @return pAspectRatio (float): .
        """
        pass
    
    ##  Gets axis radius value. 
    ##  @return pAxisRadius (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetAxisRadius(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets axis radius value. 
         @return pAxisRadius (float): .
        """
        pass
    
    ##  Gets cohesive element ratio value. 
    ##  @return pCohesRatio (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetCohesiveElementRatio(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets cohesive element ratio value. 
         @return pCohesRatio (float): .
        """
        pass
    
    ##  Gets collapse value. 
    ##  @return pCollapseValue (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetCollapse(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets collapse value. 
         @return pCollapseValue (float): .
        """
        pass
    
    ##  Gets consist distance value. 
    ##  @return pConsistDistance (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetConsistDistance(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets consist distance value. 
         @return pConsistDistance (float): .
        """
        pass
    
    ##  Gets edge point length ratio and edge point included angle. 
    ##  @return A tuple consisting of (pRatioValue, pAngleValue). 
    ##  - pRatioValue is: float.
    ##  - pAngleValue is: float.

    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    @staticmethod
    def GetEdgePointLengthRatioAndAngle(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float]:
        """
         Gets edge point length ratio and edge point included angle. 
         @return A tuple consisting of (pRatioValue, pAngleValue). 
         - pRatioValue is: float.
         - pAngleValue is: float.

        """
        pass
    
    ##  Gets minimum, maximum and average element edge length. 
    ##  @return A tuple consisting of (pMinSize, pMazSize, pAvgSize). 
    ##  - pMinSize is: float.
    ##  - pMazSize is: float.
    ##  - pAvgSize is: float.

    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    @staticmethod
    def GetElementSize(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float, float]:
        """
         Gets minimum, maximum and average element edge length. 
         @return A tuple consisting of (pMinSize, pMazSize, pAvgSize). 
         - pMinSize is: float.
         - pMazSize is: float.
         - pAvgSize is: float.

        """
        pass
    
    ##  Gets minimum and maximum interior angle value. 
    ##  @return A tuple consisting of (pMinAngle, pMaxAngle). 
    ##  - pMinAngle is: float.
    ##  - pMaxAngle is: float.

    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    @staticmethod
    def GetInteriorAngle(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float]:
        """
         Gets minimum and maximum interior angle value. 
         @return A tuple consisting of (pMinAngle, pMaxAngle). 
         - pMinAngle is: float.
         - pMaxAngle is: float.

        """
        pass
    
    ##  Gets jacobian value. 
    ##  @return A tuple consisting of (pJacobianZero, pJacobianRatio, pJacobianSign). 
    ##  - pJacobianZero is: float.
    ##  - pJacobianRatio is: float.
    ##  - pJacobianSign is: bool.

    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    @staticmethod
    def GetJacobian(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float, bool]:
        """
         Gets jacobian value. 
         @return A tuple consisting of (pJacobianZero, pJacobianRatio, pJacobianSign). 
         - pJacobianZero is: float.
         - pJacobianRatio is: float.
         - pJacobianSign is: bool.

        """
        pass
    
    ##  Calculates ratio of longest edge to shortest edge in stacking direction and
    ##                 ratio of the difference between thickness in stacking direction as defined by grids and thickness as defined by ply thickness specification
    ##                 to the thickness in the stacking direction as defined by grids for CHEXA and CPENTA elements referencing PCOMPS entries only. 
    ##  @return A tuple consisting of (lamEdgeRatio, lamThickRatio). 
    ##  - lamEdgeRatio is: float.
    ##  - lamThickRatio is: float.

    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    ## <param name="matMatrix"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) </param>
    ## <param name="stackAxis"> (int) </param>
    ## <param name="totalPlyThick"> (float) </param>
    @staticmethod
    def GetLaminateRatio(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement, matMatrix: NXOpen.Matrix3x3, stackAxis: int, totalPlyThick: float) -> Tuple[float, float]:
        """
         Calculates ratio of longest edge to shortest edge in stacking direction and
                        ratio of the difference between thickness in stacking direction as defined by grids and thickness as defined by ply thickness specification
                        to the thickness in the stacking direction as defined by grids for CHEXA and CPENTA elements referencing PCOMPS entries only. 
         @return A tuple consisting of (lamEdgeRatio, lamThickRatio). 
         - lamEdgeRatio is: float.
         - lamThickRatio is: float.

        """
        pass
    
    ##  Gets element offset length ratio for beam and bar element. 
    ##  @return pOffsetLengthRatio (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetOffsetLengthRatio(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets element offset length ratio for beam and bar element. 
         @return pOffsetLengthRatio (float): .
        """
        pass
    
    ##  Gets parallel deviation angle. 
    ##  @return pParallelDeviation (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetParallelDeviation(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets parallel deviation angle. 
         @return pParallelDeviation (float): .
        """
        pass
    
    ##  Gets shape factor. 
    ##  @return pShapeFactor (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetShapeFactor(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets shape factor. 
         @return pShapeFactor (float): .
        """
        pass
    
    ##  Gets skew value. 
    ##  @return pSkewValue (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetSkew(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets skew value. 
         @return pSkewValue (float): .
        """
        pass
    
    ##  Gets taper value. 
    ##  @return pTaperValue (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetTaper(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets taper value. 
         @return pTaperValue (float): .
        """
        pass
    
    ##  Gets twist value. 
    ##  @return pTwistValue (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetTwist(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets twist value. 
         @return pTwistValue (float): .
        """
        pass
    
    ##  Gets volume value for 3D element. 
    ##  @return pVolume (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetVolume(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets volume value for 3D element. 
         @return pVolume (float): .
        """
        pass
    
    ##  Gets warp factor value. 
    ##  @return pWarpValue (float): .
    ## 
    ##   <br>  Created in NX1965.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="pElem"> (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) </param>
    def GetWarp(eqChecker: IElementQualityChecker, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets warp factor value. 
         @return pWarpValue (float): .
        """
        pass
    
import NXOpen
##   @brief  Represents the model check selection builder  
## 
##    <br> This is an interface, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ISelectionBuilder(NXOpen.Object): 
    """ <summary> Represents the model check selection builder </summary> """


    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    @abstractmethod
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents the quality check criteria value settings  
## 
##    <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ITestValue(NXOpen.Object): 
    """ <summary> Represents the quality check criteria value settings </summary> """


    ## Getter for property: (bool) DoTest
    ##   an option value indicating whether to do element quality check for this test    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    @abstractmethod
    def DoTest(self) -> bool:
        """
        Getter for property: (bool) DoTest
          an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    
    ## Setter for property: (bool) DoTest

    ##   an option value indicating whether to do element quality check for this test    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DoTest.setter
    def DoTest(self, doTest: bool):
        """
        Setter for property: (bool) DoTest
          an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    
    ##  Returns the criteria value. An exception will be thrown if there is no criteria value associated with this test 
    ##  @return A tuple consisting of (unit, criteriaValue). 
    ##  - unit is: @link NXOpen.Unit NXOpen.Unit@endlink.
    ##  - criteriaValue is: float.

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="criteriaType"> (@link TestValueTypes.CriteriaType NXOpen.CAE.ModelCheck.TestValueTypes.CriteriaType@endlink) </param>
    @staticmethod
    @abstractmethod
    def GetCriteriaValue(self, criteriaType: TestValueTypes.CriteriaType) -> Tuple[NXOpen.Unit, float]:
        """
         Returns the criteria value. An exception will be thrown if there is no criteria value associated with this test 
         @return A tuple consisting of (unit, criteriaValue). 
         - unit is: @link NXOpen.Unit NXOpen.Unit@endlink.
         - criteriaValue is: float.

        """
        pass
    
    ##  Returns the element reference definitions associated with this test 
    ##  @return elemReferences (@link TestValueTypes.ElementReference List[NXOpen.CAE.ModelCheck.TestValueTypes.ElementReference]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetElementReferences(self) -> List[TestValueTypes.ElementReference]:
        """
         Returns the element reference definitions associated with this test 
         @return elemReferences (@link TestValueTypes.ElementReference List[NXOpen.CAE.ModelCheck.TestValueTypes.ElementReference]@endlink): .
        """
        pass
    
    ##  To know whether this quality test is a solver specific test and a system test 
    ##  @return A tuple consisting of (isSolverSpecificTest, isSystemTest). 
    ##  - isSolverSpecificTest is: bool.
    ##  - isSystemTest is: bool.

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetIsSolverSpecificTest(self) -> Tuple[bool, bool]:
        """
         To know whether this quality test is a solver specific test and a system test 
         @return A tuple consisting of (isSolverSpecificTest, isSystemTest). 
         - isSolverSpecificTest is: bool.
         - isSystemTest is: bool.

        """
        pass
    
    ##  Returns the test type 
    ##  @return testType (@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetTestType(self) -> TestValueTypes.TestType:
        """
         Returns the test type 
         @return testType (@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink): .
        """
        pass
    
    ##  Returns the validator type 
    ##  @return validator (@link TestValueTypes.Validator NXOpen.CAE.ModelCheck.TestValueTypes.Validator@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetValidator(self) -> TestValueTypes.Validator:
        """
         Returns the validator type 
         @return validator (@link TestValueTypes.Validator NXOpen.CAE.ModelCheck.TestValueTypes.Validator@endlink): .
        """
        pass
    
    ##  Tells whether there is criteria value associated with this test 
    ##  @return hasCriteriaValue (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def HasCriteriaValue(self) -> bool:
        """
         Tells whether there is criteria value associated with this test 
         @return hasCriteriaValue (bool): .
        """
        pass
    
    ##  Reset as customer default setting 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def ResetToCustomerDefault(self) -> None:
        """
         Reset as customer default setting 
        """
        pass
    
    ## Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="self"> (@link ITestValue NXOpen.CAE.ModelCheck.ITestValue@endlink) </param>
    ## <param name="criteriaType"> (@link TestValueTypes.CriteriaType NXOpen.CAE.ModelCheck.TestValueTypes.CriteriaType@endlink) </param>
    ## <param name="criteriaValue"> (float) </param>
    ## <param name="unit"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    @abstractmethod
    @overload
    def SetCriteriaValue(self, self, criteriaType: TestValueTypes.CriteriaType, criteriaValue: float, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        """
        pass
    
    ## Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="self"> (@link ITestValue NXOpen.CAE.ModelCheck.ITestValue@endlink) </param>
    ## <param name="criteriaType"> (@link TestValueTypes.CriteriaType NXOpen.CAE.ModelCheck.TestValueTypes.CriteriaType@endlink) </param>
    ## <param name="criteriaValue"> (str) </param>
    ## <param name="unit"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    @abstractmethod
    @overload
    def SetCriteriaValue(self, self, criteriaType: TestValueTypes.CriteriaType, criteriaValue: str, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        """
        pass
    
import NXOpen
## Represents a @link NXOpen::CAE::ModelCheck::ModelSetupCheckBuilder NXOpen::CAE::ModelCheck::ModelSetupCheckBuilder@endlink  which can be
##         used to check if the active @link NXOpen::CAE::SimSolution NXOpen::CAE::SimSolution@endlink  contains all the necessary 
##         items for the analysis, including elements, loads, constraints and materials. Also it could check 
##         label conficts and component connect status.
##         @link Builder::Commit Builder::Commit@endlink  performs the check. The check result is written into a report
##         file or listed in a separate information window, along with an error summary for each topic   <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateModelSetupCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateModelSetupCheckBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ModelSetupCheckBuilder(NXOpen.Builder): 
    """Represents a <ja_class>NXOpen.CAE.ModelCheck.ModelSetupCheckBuilder</ja_class> which can be
        used to check if the active <ja_class>NXOpen.CAE.SimSolution</ja_class> contains all the necessary 
        items for the analysis, including elements, loads, constraints and materials. Also it could check 
        label conficts and component connect status.
        <ja_method>Builder.Commit</ja_method> performs the check. The check result is written into a report
        file or listed in a separate information window, along with an error summary for each topic  """


    ## Getter for property: (bool) CheckAllComponents
    ##   the value indicating whether to check all components associated with the assembly FEM in the 
    ##                 model check, regardless of load status.  
    ##    If false, only the fully loaded components are included 
    ##                 in the check   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CheckAllComponents(self) -> bool:
        """
        Getter for property: (bool) CheckAllComponents
          the value indicating whether to check all components associated with the assembly FEM in the 
                        model check, regardless of load status.  
           If false, only the fully loaded components are included 
                        in the check   
         
        """
        pass
    
    ## Setter for property: (bool) CheckAllComponents

    ##   the value indicating whether to check all components associated with the assembly FEM in the 
    ##                 model check, regardless of load status.  
    ##    If false, only the fully loaded components are included 
    ##                 in the check   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CheckAllComponents.setter
    def CheckAllComponents(self, checkAllComponents: bool):
        """
        Setter for property: (bool) CheckAllComponents
          the value indicating whether to check all components associated with the assembly FEM in the 
                        model check, regardless of load status.  
           If false, only the fully loaded components are included 
                        in the check   
         
        """
        pass
    
    ## Getter for property: (bool) CheckLabelConflicts
    ##   the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
    ##             and reports the label range in which the conflict occurs   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CheckLabelConflicts(self) -> bool:
        """
        Getter for property: (bool) CheckLabelConflicts
          the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
                    and reports the label range in which the conflict occurs   
            
         
        """
        pass
    
    ## Setter for property: (bool) CheckLabelConflicts

    ##   the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
    ##             and reports the label range in which the conflict occurs   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CheckLabelConflicts.setter
    def CheckLabelConflicts(self, checkLabelConflicts: bool):
        """
        Setter for property: (bool) CheckLabelConflicts
          the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
                    and reports the label range in which the conflict occurs   
            
         
        """
        pass
    
    ## Getter for property: (bool) CheckUnconnectedComponent
    ##   the option specifying whether to check for component FEMs that are not connected    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def CheckUnconnectedComponent(self) -> bool:
        """
        Getter for property: (bool) CheckUnconnectedComponent
          the option specifying whether to check for component FEMs that are not connected    
            
         
        """
        pass
    
    ## Setter for property: (bool) CheckUnconnectedComponent

    ##   the option specifying whether to check for component FEMs that are not connected    
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CheckUnconnectedComponent.setter
    def CheckUnconnectedComponent(self, checkUnconnectedComponent: bool):
        """
        Setter for property: (bool) CheckUnconnectedComponent
          the option specifying whether to check for component FEMs that are not connected    
            
         
        """
        pass
    
    ## Getter for property: (bool) IsDetailedMessage
    ##   the value indicating whether to list comprehensive descriptions of any problems and suggest
    ##                 possible remedies.  
    ##    If false, only the simple descriptions of problems are listed   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def IsDetailedMessage(self) -> bool:
        """
        Getter for property: (bool) IsDetailedMessage
          the value indicating whether to list comprehensive descriptions of any problems and suggest
                        possible remedies.  
           If false, only the simple descriptions of problems are listed   
         
        """
        pass
    
    ## Setter for property: (bool) IsDetailedMessage

    ##   the value indicating whether to list comprehensive descriptions of any problems and suggest
    ##                 possible remedies.  
    ##    If false, only the simple descriptions of problems are listed   
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsDetailedMessage.setter
    def IsDetailedMessage(self, isDetailedMessage: bool):
        """
        Setter for property: (bool) IsDetailedMessage
          the value indicating whether to list comprehensive descriptions of any problems and suggest
                        possible remedies.  
           If false, only the simple descriptions of problems are listed   
         
        """
        pass
    
    ## Getter for property: (str) ReportFileName
    ##   the full name of the report file.  
    ##    If NULL, the report is listed in a separate listing window    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ReportFileName(self) -> str:
        """
        Getter for property: (str) ReportFileName
          the full name of the report file.  
           If NULL, the report is listed in a separate listing window    
         
        """
        pass
    
    ## Setter for property: (str) ReportFileName

    ##   the full name of the report file.  
    ##    If NULL, the report is listed in a separate listing window    
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ReportFileName.setter
    def ReportFileName(self, reportFileName: str):
        """
        Setter for property: (str) ReportFileName
          the full name of the report file.  
           If NULL, the report is listed in a separate listing window    
         
        """
        pass
    
    ##  Performs model setup check
    ##  @return checkStatus (int):  Model setup checking result. Zero indicates the checking is successful .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DoCheck(builder: ModelSetupCheckBuilder) -> int:
        """
         Performs model setup check
         @return checkStatus (int):  Model setup checking result. Zero indicates the checking is successful .
        """
        pass
    
import NXOpen
##   @brief  Represents quality test settings of a specified test type  
## 
##    <br> Not to support KF  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class QualityTestValue(NXOpen.NXObject): 
    """ <summary> Represents quality test settings of a specified test type </summary> """


    ## Getter for property: (bool) DoTest
    ##   an option value indicating whether to do element quality check for this test    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def DoTest(self) -> bool:
        """
        Getter for property: (bool) DoTest
          an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    
    ## Setter for property: (bool) DoTest

    ##   an option value indicating whether to do element quality check for this test    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DoTest.setter
    def DoTest(self, doTest: bool):
        """
        Setter for property: (bool) DoTest
          an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    
    ## Getter for property: (int) ElementSpecificTestCount
    ##   the count of @link NXOpen::CAE::ModelCheck::ElementSpecificTestValue NXOpen::CAE::ModelCheck::ElementSpecificTestValue@endlink  in this test setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def ElementSpecificTestCount(self) -> int:
        """
        Getter for property: (int) ElementSpecificTestCount
          the count of @link NXOpen::CAE::ModelCheck::ElementSpecificTestValue NXOpen::CAE::ModelCheck::ElementSpecificTestValue@endlink  in this test setting   
            
         
        """
        pass
    
    ##  Returns @link NXOpen::CAE::ModelCheck::ElementSpecificTestValue NXOpen::CAE::ModelCheck::ElementSpecificTestValue@endlink  of specified index in this test setting 
    ##  @return pElemTestValue (@link ElementSpecificTestValue NXOpen.CAE.ModelCheck.ElementSpecificTestValue@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetElementSpecificTestByIndex(self, index: int) -> ElementSpecificTestValue:
        """
         Returns @link NXOpen::CAE::ModelCheck::ElementSpecificTestValue NXOpen::CAE::ModelCheck::ElementSpecificTestValue@endlink  of specified index in this test setting 
         @return pElemTestValue (@link ElementSpecificTestValue NXOpen.CAE.ModelCheck.ElementSpecificTestValue@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
## 
##         Represents a @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder@endlink  used to reverse directions
##         for specified beam elements. You can reverse beam element directions by using either @link Builder::Commit Builder::Commit@endlink 
##         or @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::ReverseDirections NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::ReverseDirections@endlink .
##         The difference between these two methods is @link Builder::Commit Builder::Commit@endlink  reverses the directions
##         and updates direction display, but it does not return the beam elements which were reversed
##         successfully. @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::ReverseDirections NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::ReverseDirections@endlink  
##         reverses directions and returns the beam elements which were reversed successfully.
##         Both of the methods are only available in fem context.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateReverseBeamElementDirectionBuilder  NXOpen::CAE::ModelCheckManager::CreateReverseBeamElementDirectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ReverseBeamElementDirectionBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder</ja_class> used to reverse directions
        for specified beam elements. You can reverse beam element directions by using either <ja_method>Builder.Commit</ja_method>
        or <ja_method>NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.ReverseDirections</ja_method>.
        The difference between these two methods is <ja_method>Builder.Commit</ja_method> reverses the directions
        and updates direction display, but it does not return the beam elements which were reversed
        successfully. <ja_method>NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.ReverseDirections</ja_method> 
        reverses directions and returns the beam elements which were reversed successfully.
        Both of the methods are only available in fem context.
        """


    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##             @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                    @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ##  Display directions of @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DisplayDirections(builder: ReverseBeamElementDirectionBuilder) -> None:
        """
         Display directions of @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList@endlink  
        """
        pass
    
    ##  Reverses directions specified in @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList@endlink 
    ##                 and returns those elements whose directions were reversed successfully. This method will only reverse
    ##                 the directions for beam elements in the current work fem part.
    ##             
    ##  @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def ReverseDirections(builder: ReverseBeamElementDirectionBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Reverses directions specified in @link NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseBeamElementDirectionBuilder::SelectionList@endlink 
                        and returns those elements whose directions were reversed successfully. This method will only reverse
                        the directions for beam elements in the current work fem part.
                    
         @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
import NXOpen
import NXOpen.CAE
## 
##         Represents a @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder@endlink  used to reverse normals
##         for specified shell elements. You can reverse shell element normals by using either @link Builder::Commit Builder::Commit@endlink 
##         or @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::ReverseNormals NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::ReverseNormals@endlink .
##         The difference between these two methods is @link Builder::Commit Builder::Commit@endlink  reverses the normals
##         and updates normal display, but it does not return the shell elements which were reversed
##         successfully. @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::ReverseNormals NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::ReverseNormals@endlink  
##         reverses normals and returns the shell elements which were reversed successfully.
##         Both of the methods are only available in fem context.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateReverseShellElementNormalBuilder  NXOpen::CAE::ModelCheckManager::CreateReverseShellElementNormalBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class ReverseShellElementNormalBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder</ja_class> used to reverse normals
        for specified shell elements. You can reverse shell element normals by using either <ja_method>Builder.Commit</ja_method>
        or <ja_method>NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.ReverseNormals</ja_method>.
        The difference between these two methods is <ja_method>Builder.Commit</ja_method> reverses the normals
        and updates normal display, but it does not return the shell elements which were reversed
        successfully. <ja_method>NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.ReverseNormals</ja_method> 
        reverses normals and returns the shell elements which were reversed successfully.
        Both of the methods are only available in fem context.
        """


    ##  indicates how display type value is defined 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Arrows</term><description> 
    ## </description> </item><item><term> 
    ## SolidFaceColors</term><description> 
    ## </description> </item></list>
    class DisplayTypeValue(Enum):
        """
        Members Include: <Arrows> <SolidFaceColors>
        """
        Arrows: int
        SolidFaceColors: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReverseShellElementNormalBuilder.DisplayTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (@link ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType
    ##   the display type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ReverseShellElementNormalBuilder.DisplayTypeValue
    @property
    def DisplayType(self) -> ReverseShellElementNormalBuilder.DisplayTypeValue:
        """
        Getter for property: (@link ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType
          the display type   
            
         
        """
        pass
    
    ## Setter for property: (@link ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType

    ##   the display type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DisplayType.setter
    def DisplayType(self, displayType: ReverseShellElementNormalBuilder.DisplayTypeValue):
        """
        Setter for property: (@link ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.DisplayTypeValue@endlink) DisplayType
          the display type   
            
         
        """
        pass
    
    ## Getter for property: (int) NegativeFaceColor
    ##   the negative face color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def NegativeFaceColor(self) -> int:
        """
        Getter for property: (int) NegativeFaceColor
          the negative face color   
            
         
        """
        pass
    
    ## Setter for property: (int) NegativeFaceColor

    ##   the negative face color   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @NegativeFaceColor.setter
    def NegativeFaceColor(self, negativeFaceColor: int):
        """
        Setter for property: (int) NegativeFaceColor
          the negative face color   
            
         
        """
        pass
    
    ## Getter for property: (int) PositiveFaceColor
    ##   the positive face color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def PositiveFaceColor(self) -> int:
        """
        Getter for property: (int) PositiveFaceColor
          the positive face color   
            
         
        """
        pass
    
    ## Setter for property: (int) PositiveFaceColor

    ##   the positive face color   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @PositiveFaceColor.setter
    def PositiveFaceColor(self, positiveFaceColor: int):
        """
        Setter for property: (int) PositiveFaceColor
          the positive face color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##             @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                    @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ##  Create element group of subdomains 
    ##  @return ppSubdomainGroupTag (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Arrary of subdomain groups tag .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def CreateElementGroupOfSubdomains(builder: ReverseShellElementNormalBuilder) -> List[NXOpen.NXObject]:
        """
         Create element group of subdomains 
         @return ppSubdomainGroupTag (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Arrary of subdomain groups tag .
        """
        pass
    
    ##  Creates inconsistent element edge group 
    ##             
    ##  @return groupTag (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def CreateInconsistentElementEdgeGroup(builder: ReverseShellElementNormalBuilder) -> NXOpen.CAE.CaeGroup:
        """
         Creates inconsistent element edge group 
                    
         @return groupTag (@link NXOpen.CAE.CaeGroup NXOpen.CAE.CaeGroup@endlink):  .
        """
        pass
    
    ##  Display normals of @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList@endlink  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DisplayNormals(builder: ReverseShellElementNormalBuilder) -> None:
        """
         Display normals of @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList@endlink  
        """
        pass
    
    ##  Reverses normals specified in @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList@endlink 
    ##                 and returns those elements whose normals were reversed successfully. This method will only reverse
    ##                 the normals for shell elements in the current work fem part.
    ##             
    ##  @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def ReverseNormals(builder: ReverseShellElementNormalBuilder) -> List[NXOpen.CAE.FEElement]:
        """
         Reverses normals specified in @link NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList NXOpen::CAE::ModelCheck::ReverseShellElementNormalBuilder::SelectionList@endlink 
                        and returns those elements whose normals were reversed successfully. This method will only reverse
                        the normals for shell elements in the current work fem part.
                    
         @return reversedElements (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  .
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder@endlink  used to reorient normals
##         for left handed solid elements.
##         Both of the methods are only available in fem context.
##          <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateSolidElementFaceNormalBuilder  NXOpen::CAE::ModelCheckManager::CreateSolidElementFaceNormalBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SolidElementFaceNormalBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder</ja_class> used to reorient normals
        for left handed solid elements.
        Both of the methods are only available in fem context.
        """


    ## Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
    ##   the check scope setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CheckScope
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption

    ##   the check scope setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: (@link CheckScope NXOpen.CAE.ModelCheck.CheckScope@endlink) CheckScopeOption
          the check scope setting   
            
         
        """
        pass
    
    ## Getter for property: (int) NegativeFaceColor
    ##   the negative face color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def NegativeFaceColor(self) -> int:
        """
        Getter for property: (int) NegativeFaceColor
          the negative face color   
            
         
        """
        pass
    
    ## Setter for property: (int) NegativeFaceColor

    ##   the negative face color   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @NegativeFaceColor.setter
    def NegativeFaceColor(self, negativeFaceColor: int):
        """
        Setter for property: (int) NegativeFaceColor
          the negative face color   
            
         
        """
        pass
    
    ## Getter for property: (int) PositiveFaceColor
    ##   the positive face color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def PositiveFaceColor(self) -> int:
        """
        Getter for property: (int) PositiveFaceColor
          the positive face color   
            
         
        """
        pass
    
    ## Setter for property: (int) PositiveFaceColor

    ##   the positive face color   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @PositiveFaceColor.setter
    def PositiveFaceColor(self, positiveFaceColor: int):
        """
        Setter for property: (int) PositiveFaceColor
          the positive face color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
    ##   the selected objects to be checked.  
    ##    The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
    ##             @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectionList
          the selected objects to be checked.  
           The objects must be @link NXOpen::CAE::Mesh NXOpen::CAE::Mesh@endlink  or
                    @link NXOpen::CAE::FEElement NXOpen::CAE::FEElement@endlink    
         
        """
        pass
    
    ##  Create group for the left handed elements in
    ##                 @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::CreateGroupOfLeftHandedElements NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::CreateGroupOfLeftHandedElements@endlink 
    ##                 and returns those elements which were grouped successfully. This method will only group left handed solid elements
    ##                 in the current work fem part.
    ##             
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def CreateGroupOfLeftHandedElements(builder: SolidElementFaceNormalBuilder) -> None:
        """
         Create group for the left handed elements in
                        @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::CreateGroupOfLeftHandedElements NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::CreateGroupOfLeftHandedElements@endlink 
                        and returns those elements which were grouped successfully. This method will only group left handed solid elements
                        in the current work fem part.
                    
        """
        pass
    
    ##  Display normals of @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::DisplayNormals NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::DisplayNormals@endlink  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def DisplayNormals(builder: SolidElementFaceNormalBuilder) -> None:
        """
         Display normals of @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::DisplayNormals NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::DisplayNormals@endlink  
        """
        pass
    
    ##  Reorient normals specified in @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::ReorientLeftHandedElements NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::ReorientLeftHandedElements@endlink 
    ##                 which normal is left handed and returns those elements whose normals were reoriented successfully. This method will only reorient
    ##                 the normals for solid left handed elements in the current work fem part.
    ##             
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    @staticmethod
    def ReorientLeftHandedElements(builder: SolidElementFaceNormalBuilder) -> None:
        """
         Reorient normals specified in @link NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::ReorientLeftHandedElements NXOpen::CAE::ModelCheck::SolidElementFaceNormalBuilder::ReorientLeftHandedElements@endlink 
                        which normal is left handed and returns those elements whose normals were reoriented successfully. This method will only reorient
                        the normals for solid left handed elements in the current work fem part.
                    
        """
        pass
    
import NXOpen
##  Represents quality checking result of a quality test
##      <br> To obtain an instance of this class use CAE.ModelCheck.ElementTestResult.GetTestResults  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class TestResult(NXOpen.TransientObject): 
    """ Represents quality checking result of a quality test
    """


    ## Getter for property: (@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink) TestType
    ##   the test type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return TestValueTypes.TestType
    @property
    def TestType(self) -> TestValueTypes.TestType:
        """
        Getter for property: (@link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink) TestType
          the test type   
            
         
        """
        pass
    
    ## Getter for property: (float) TestValue
    ##   the test value.  
    ##    An exception will be thrown f there is no test value associated with this test   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return float
    @property
    def TestValue(self) -> float:
        """
        Getter for property: (float) TestValue
          the test value.  
           An exception will be thrown f there is no test value associated with this test   
         
        """
        pass
    
    ## Getter for property: (@link TestValueTypes.Result NXOpen.CAE.ModelCheck.TestValueTypes.Result@endlink) ValidatedTestResult
    ##   the validation result of comparing test value with the criteria value.  
    ##   
    ##             if no test value is associated this test, the result just indicates the test 
    ##             is passed or failed   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return TestValueTypes.Result
    @property
    def ValidatedTestResult(self) -> TestValueTypes.Result:
        """
        Getter for property: (@link TestValueTypes.Result NXOpen.CAE.ModelCheck.TestValueTypes.Result@endlink) ValidatedTestResult
          the validation result of comparing test value with the criteria value.  
          
                    if no test value is associated this test, the result just indicates the test 
                    is passed or failed   
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Tells whether there is a test value associated with this test 
    ##  @return hasTestValue (bool): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def HasTestValue(self) -> bool:
        """
         Tells whether there is a test value associated with this test 
         @return hasTestValue (bool): .
        """
        pass
    
import NXOpen
##   @brief  Represents the quality check criteria value settings  
## 
##    <br> No Creator this holds an enum  shared by other classes  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class TestValueTypes(NXOpen.Object): 
    """ <summary> Represents the quality check criteria value settings </summary> """


    ##  the alert level of a criteria value 
    ##  reports as warning if the check result failed with the criteria value 
    class CriteriaType(Enum):
        """
        Members Include: <Warning> <Error> <Worst>
        """
        Warning: int
        Error: int
        Worst: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.CriteriaType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the checking result 
    ##  indicates the test value does not violate the criteria values 
    class Result(Enum):
        """
        Members Include: <Passed> <Failed> <Exception> <NotApply> <Warned>
        """
        Passed: int
        Failed: int
        Exception: int
        NotApply: int
        Warned: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the test types 
    ##  
    class TestType(Enum):
        """
        Members Include: <JacobianZero> <JacobianRatio> <JacobianSign> <Volume> <AxisymmetricY> <AxisymmetricX> <AspectRatio> <SkewAngle> <InteriorAngleMinimum> <InteriorAngleMaximum> <Taper> <WarpFactor> <FaceWarpCoefficient> <EdgePointLengthRatio> <EdgePointIncludedAngle> <LengthRatioOffset> <ParallelDeviation> <ShapeFactor> <Twist> <LengthMinimum> <LengthMaximum> <TetCollapse> <WarpageAngle> <CohesiveElement> <LaminateTaperRatio> <LaminateThicknessRatio> <Area>
        """
        JacobianZero: int
        JacobianRatio: int
        JacobianSign: int
        Volume: int
        AxisymmetricY: int
        AxisymmetricX: int
        AspectRatio: int
        SkewAngle: int
        InteriorAngleMinimum: int
        InteriorAngleMaximum: int
        Taper: int
        WarpFactor: int
        FaceWarpCoefficient: int
        EdgePointLengthRatio: int
        EdgePointIncludedAngle: int
        LengthRatioOffset: int
        ParallelDeviation: int
        ShapeFactor: int
        Twist: int
        LengthMinimum: int
        LengthMaximum: int
        TetCollapse: int
        WarpageAngle: int
        CohesiveElement: int
        LaminateTaperRatio: int
        LaminateThicknessRatio: int
        Area: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.TestType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  indicates how to compare the check result with the criteria value 
    ##  indicates no criteria value defined, not necessary to compare the check result with criteria value 
    class Validator(Enum):
        """
        Members Include: <NotSet> <GreatThan> <GreatThanOrEqual> <SmallThan> <SmallThanOrEqual>
        """
        NotSet: int
        GreatThan: int
        GreatThanOrEqual: int
        SmallThan: int
        SmallThanOrEqual: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.Validator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents an element reference definition associated with this test 
    class ElementReference:
        """
         represents an element reference definition associated with this test 
        """
        ## Getter for property :(str) ElementTypeName
        ## the element type name, which is defined in solver specific item
        ## @return str
        @property
        def ElementTypeName(self) -> str:
            """
            Getter for property ElementTypeName
            the element type name, which is defined in solver specific item

            """
            pass
        
        ## Setter for property :(str) ElementTypeName
        @ElementTypeName.setter
        def ElementTypeName(self, value: str):
            """
            Getter for property ElementTypeName
            the element type name, which is defined in solver specific item
            Setter for property ElementTypeName
            the element type name, which is defined in solver specific item

            """
            pass
        
        ## Getter for property :(str) ElementPropertyName
        ## a specified integer element property name
        ## @return str
        @property
        def ElementPropertyName(self) -> str:
            """
            Getter for property ElementPropertyName
            a specified integer element property name

            """
            pass
        
        ## Setter for property :(str) ElementPropertyName
        @ElementPropertyName.setter
        def ElementPropertyName(self, value: str):
            """
            Getter for property ElementPropertyName
            a specified integer element property name
            Setter for property ElementPropertyName
            a specified integer element property name

            """
            pass
        
        ## Getter for property :(int) ElementPropertyValue
        ## the control value of integer element property, only valid when property name is not NULL
        ## @return int
        @property
        def ElementPropertyValue(self) -> int:
            """
            Getter for property ElementPropertyValue
            the control value of integer element property, only valid when property name is not NULL

            """
            pass
        
        ## Setter for property :(int) ElementPropertyValue
        @ElementPropertyValue.setter
        def ElementPropertyValue(self, value: int):
            """
            Getter for property ElementPropertyValue
            the control value of integer element property, only valid when property name is not NULL
            Setter for property ElementPropertyValue
            the control value of integer element property, only valid when property name is not NULL

            """
            pass
        
    
    
## @package NXOpen.CAE.ModelCheck
## Classes, Enums and Structs under NXOpen.CAE.ModelCheck namespace

##  @link AlignBeamElementDirectionBuilderConnectedElementScope NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilderConnectedElementScope @endlink is an alias for @link AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.ConnectedElementScope@endlink
AlignBeamElementDirectionBuilderConnectedElementScope = AlignBeamElementDirectionBuilder.ConnectedElementScope


##  @link AlignShellElementFirstEdgeBuilderElemSelectionMode NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilderElemSelectionMode @endlink is an alias for @link AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder.ElemSelectionMode@endlink
AlignShellElementFirstEdgeBuilderElemSelectionMode = AlignShellElementFirstEdgeBuilder.ElemSelectionMode


##  @link AlignShellElementNormalBuilderConnectedElementScope NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilderConnectedElementScope @endlink is an alias for @link AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.ConnectedElementScope@endlink
AlignShellElementNormalBuilderConnectedElementScope = AlignShellElementNormalBuilder.ConnectedElementScope


##  @link AlignShellElementNormalBuilderDisplayTypeValue NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilderDisplayTypeValue @endlink is an alias for @link AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.DisplayTypeValue@endlink
AlignShellElementNormalBuilderDisplayTypeValue = AlignShellElementNormalBuilder.DisplayTypeValue


##  @link AlignShellElementNormalBuilderOrientMethodType NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilderOrientMethodType @endlink is an alias for @link AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.OrientMethodType@endlink
AlignShellElementNormalBuilderOrientMethodType = AlignShellElementNormalBuilder.OrientMethodType


##  @link CorrectBeamElementsBuilderElementToCheck NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilderElementToCheck @endlink is an alias for @link CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder.ElementToCheck@endlink
CorrectBeamElementsBuilderElementToCheck = CorrectBeamElementsBuilder.ElementToCheck


##  @link DuplicateElementsCheckBuilderDeletePreference NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDeletePreference @endlink is an alias for @link DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeletePreference@endlink
DuplicateElementsCheckBuilderDeletePreference = DuplicateElementsCheckBuilder.DeletePreference


## @link DuplicateElementsCheckBuilderDisplaySettings_Struct NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilderDisplaySettings_Struct@endlink is an alias for @link DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings@endlink.
DuplicateElementsCheckBuilderDisplaySettings_Struct = DuplicateElementsCheckBuilder.DisplaySettings


## @link DuplicateNodesCheckBuilderDisplaySettings_Struct NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderDisplaySettings_Struct@endlink is an alias for @link DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DisplaySettings@endlink.
DuplicateNodesCheckBuilderDisplaySettings_Struct = DuplicateNodesCheckBuilder.DisplaySettings


##  @link DuplicateNodesCheckBuilderListOption NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderListOption @endlink is an alias for @link DuplicateNodesCheckBuilder.ListOption NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.ListOption@endlink
DuplicateNodesCheckBuilderListOption = DuplicateNodesCheckBuilder.ListOption


##  @link DuplicateNodesCheckBuilderMergePreference NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilderMergePreference @endlink is an alias for @link DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergePreference@endlink
DuplicateNodesCheckBuilderMergePreference = DuplicateNodesCheckBuilder.MergePreference


## @link ElementEdgeCheckBuilderEdgeDisplayStyle_Struct NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderEdgeDisplayStyle_Struct@endlink is an alias for @link ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle@endlink.
ElementEdgeCheckBuilderEdgeDisplayStyle_Struct = ElementEdgeCheckBuilder.EdgeDisplayStyle


##  @link ElementEdgeCheckBuilderScope NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilderScope @endlink is an alias for @link ElementEdgeCheckBuilder.Scope NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.Scope@endlink
ElementEdgeCheckBuilderScope = ElementEdgeCheckBuilder.Scope


##  @link ElementMaterialOrientationCheckBuilderMaterialOrientationArrowheadType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationArrowheadType @endlink is an alias for @link ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType@endlink
ElementMaterialOrientationCheckBuilderMaterialOrientationArrowheadType = ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType


##  @link ElementMaterialOrientationCheckBuilderMaterialOrientationSolidElementDisplayType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationSolidElementDisplayType @endlink is an alias for @link ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType@endlink
ElementMaterialOrientationCheckBuilderMaterialOrientationSolidElementDisplayType = ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType


##  @link ElementMaterialOrientationCheckBuilderMaterialOrientationType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilderMaterialOrientationType @endlink is an alias for @link ElementMaterialOrientationCheckBuilder.MaterialOrientationType NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.MaterialOrientationType@endlink
ElementMaterialOrientationCheckBuilderMaterialOrientationType = ElementMaterialOrientationCheckBuilder.MaterialOrientationType


##  @link ElementQualityCheckBuilderOutputElements NXOpen.CAE.ModelCheck.ElementQualityCheckBuilderOutputElements @endlink is an alias for @link ElementQualityCheckBuilder.OutputElements NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.OutputElements@endlink
ElementQualityCheckBuilderOutputElements = ElementQualityCheckBuilder.OutputElements


##  @link ElementQualityCheckBuilderReportFormat NXOpen.CAE.ModelCheck.ElementQualityCheckBuilderReportFormat @endlink is an alias for @link ElementQualityCheckBuilder.ReportFormat NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ReportFormat@endlink
ElementQualityCheckBuilderReportFormat = ElementQualityCheckBuilder.ReportFormat


## @link ElementQualityCheckResultsTestSummary_Struct NXOpen.CAE.ModelCheck.ElementQualityCheckResultsTestSummary_Struct@endlink is an alias for @link ElementQualityCheckResults.TestSummary NXOpen.CAE.ModelCheck.ElementQualityCheckResults.TestSummary@endlink.
ElementQualityCheckResultsTestSummary_Struct = ElementQualityCheckResults.TestSummary


##  @link ElementQualitySettingLimitValue NXOpen.CAE.ModelCheck.ElementQualitySettingLimitValue @endlink is an alias for @link ElementQualitySetting.LimitValue NXOpen.CAE.ModelCheck.ElementQualitySetting.LimitValue@endlink
ElementQualitySettingLimitValue = ElementQualitySetting.LimitValue


##  @link ReverseShellElementNormalBuilderDisplayTypeValue NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilderDisplayTypeValue @endlink is an alias for @link ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.DisplayTypeValue@endlink
ReverseShellElementNormalBuilderDisplayTypeValue = ReverseShellElementNormalBuilder.DisplayTypeValue


##  @link TestValueTypesCriteriaType NXOpen.CAE.ModelCheck.TestValueTypesCriteriaType @endlink is an alias for @link TestValueTypes.CriteriaType NXOpen.CAE.ModelCheck.TestValueTypes.CriteriaType@endlink
TestValueTypesCriteriaType = TestValueTypes.CriteriaType


## @link TestValueTypesElementReference_Struct NXOpen.CAE.ModelCheck.TestValueTypesElementReference_Struct@endlink is an alias for @link TestValueTypes.ElementReference NXOpen.CAE.ModelCheck.TestValueTypes.ElementReference@endlink.
TestValueTypesElementReference_Struct = TestValueTypes.ElementReference


##  @link TestValueTypesResult NXOpen.CAE.ModelCheck.TestValueTypesResult @endlink is an alias for @link TestValueTypes.Result NXOpen.CAE.ModelCheck.TestValueTypes.Result@endlink
TestValueTypesResult = TestValueTypes.Result


##  @link TestValueTypesTestType NXOpen.CAE.ModelCheck.TestValueTypesTestType @endlink is an alias for @link TestValueTypes.TestType NXOpen.CAE.ModelCheck.TestValueTypes.TestType@endlink
TestValueTypesTestType = TestValueTypes.TestType


##  @link TestValueTypesValidator NXOpen.CAE.ModelCheck.TestValueTypesValidator @endlink is an alias for @link TestValueTypes.Validator NXOpen.CAE.ModelCheck.TestValueTypes.Validator@endlink
TestValueTypesValidator = TestValueTypes.Validator


