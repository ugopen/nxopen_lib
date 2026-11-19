from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAE
class AlignBeamElementDirectionBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder builder used to align the Directions of
        connected beam elements with a seed beam element. You can align the directions by executing either 
        Builder.Commit or NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.AlignDirections.
        The difference between these two methods is Builder.Commit aligns the directions
        and updates direction display, but it does not return the elements that have changed directions.
        NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.AlignDirections aligns the directions
        and returns the elements that have changed directions. Both of the methods are only available in fem context.
        """
    class ConnectedElementScope(Enum):
        """
        Members Include: 
         |SeedMesh|  Limits check to only those beam elements in the mesh that contains the Seed Element 
         |AllVisible|  Limits check to only those beam elements which are connected to the Seed Element and are currently visible
         |UserSpecified|  Limits check to only those beam elements specified in NXOpen.CAE.ModelCheck.AlignBeamElementDirectionBuilder.UserSpecifiedConnectElements 

        """
        SeedMesh: int
        AllVisible: int
        UserSpecified: int
        @staticmethod
        def ValueOf(value: int) -> AlignBeamElementDirectionBuilder.ConnectedElementScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ElementConnectScope(self) -> AlignBeamElementDirectionBuilder.ConnectedElementScope:
        """
        Getter for property: ( AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE) ElementConnectScope
         Returns the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    @ElementConnectScope.setter
    def ElementConnectScope(self, connectScope: AlignBeamElementDirectionBuilder.ConnectedElementScope):
        """
        Setter for property: ( AlignBeamElementDirectionBuilder.ConnectedElementScope NXOpen.CAE) ElementConnectScope
         Returns the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    @property
    def ReverseSeedDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseSeedDirection
         Returns the option indicating whether to reverse element directions so that they are aligned with the seed element   
            
         
        """
        pass
    @ReverseSeedDirection.setter
    def ReverseSeedDirection(self, seedDirectionToBeReversed: bool):
        """
        Setter for property: (bool) ReverseSeedDirection
         Returns the option indicating whether to reverse element directions so that they are aligned with the seed element   
            
         
        """
        pass
    @property
    def SeedElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: ( NXOpen.CAE.FEElement) SeedElement
         Returns the seed element   
            
         
        """
        pass
    @SeedElement.setter
    def SeedElement(self, seedElement: NXOpen.CAE.FEElement):
        """
        Setter for property: ( NXOpen.CAE.FEElement) SeedElement
         Returns the seed element   
            
         
        """
        pass
    @property
    def UserSpecifiedConnectElements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: ( NXOpen.CAE.SelectElementsBuilder) UserSpecifiedConnectElements
         Returns the user specified connected elements to be aligned with seed element   
            
         
        """
        pass
    def AlignDirections(self) -> List[NXOpen.CAE.FEElement]:
        """
         Aligns the directions of elements connected to the seed element. Returns the elements
                        that have had the directions successfully reversed. This method will only reverse
                        the directions for beam elements in the current work fem part.
                    
         Returns reversedElements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def DisplayDirections(self) -> None:
        """
         Display element directions for connected elements, which are to be aligned with seed element direction 
        """
        pass
    def FindAllVisibleConnectedElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Finds all visible elements connected with the seed element 
         Returns connectedElements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
import NXOpen
import NXOpen.CAE
class AlignShellElementFirstEdgeBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.ModelCheck.AlignShellElementFirstEdgeBuilder builder used to align the first edges of
        connected shell elements with a seed element edge.
        """
    class ElemSelectionMode(Enum):
        """
        Members Include: 
         |ConnectedElementsinSeedMesh| 
         |AllVisibleConnectedShellElements| 
         |SelectedConnectedElements| 

        """
        ConnectedElementsinSeedMesh: int
        AllVisibleConnectedShellElements: int
        SelectedConnectedElements: int
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementFirstEdgeBuilder.ElemSelectionMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Direction(self) -> bool:
        """
        Getter for property: (bool) Direction
         Returns the direction   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: bool):
        """
        Setter for property: (bool) Direction
         Returns the direction   
            
         
        """
        pass
    @property
    def ElemSelectionMethod(self) -> AlignShellElementFirstEdgeBuilder.ElemSelectionMode:
        """
        Getter for property: ( AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE) ElemSelectionMethod
         Returns the element selection method   
            
         
        """
        pass
    @ElemSelectionMethod.setter
    def ElemSelectionMethod(self, elemSelectionMethod: AlignShellElementFirstEdgeBuilder.ElemSelectionMode):
        """
        Setter for property: ( AlignShellElementFirstEdgeBuilder.ElemSelectionMode NXOpen.CAE) ElemSelectionMethod
         Returns the element selection method   
            
         
        """
        pass
    @property
    def Elements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: ( NXOpen.CAE.SelectElementsBuilder) Elements
         Returns the elements   
            
         
        """
        pass
    @property
    def SeedEdge(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: ( NXOpen.CAE.SelectElementsBuilder) SeedEdge
         Returns the seed edge   
            
         
        """
        pass
    def DisplayFirstEdges(self) -> None:
        """
         Display first edges for connected elements, which are to be aligned with seed edge 
        """
        pass
import NXOpen
import NXOpen.CAE
class AlignShellElementNormalBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder builder used to align the normals of
        connected shell elements with a seed shell element. You can align the normals by executing either 
        Builder.Commit or NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.AlignNormals.
        The difference between these two methods is Builder.Commit aligns the normals
        and updates normal display, but it does not return the elements that have changed normals.
        NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.AlignNormals aligns the normals
        and returns the elements that have changed normals. Both of the methods are only available in fem context.
        """
    class ConnectedElementScope(Enum):
        """
        Members Include: 
         |SeedMesh|  Limits check to only those shell elements in the mesh that contains the Seed Element 
         |AllVisible|  Limits check to only those shell elements which are connected to the Seed Element and are currently visible
         |UserSpecified|  Limits check to only those shell elements specified in NXOpen.CAE.ModelCheck.AlignShellElementNormalBuilder.UserSpecifiedConnectElements 

        """
        SeedMesh: int
        AllVisible: int
        UserSpecified: int
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementNormalBuilder.ConnectedElementScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayTypeValue(Enum):
        """
        Members Include: 
         |Arrows| 
         |SolidFaceColors| 

        """
        Arrows: int
        SolidFaceColors: int
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementNormalBuilder.DisplayTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientMethodType(Enum):
        """
        Members Include: 
         |UsingSeedElement| 
         |Automatic| 

        """
        UsingSeedElement: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> AlignShellElementNormalBuilder.OrientMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def DisplayType(self) -> AlignShellElementNormalBuilder.DisplayTypeValue:
        """
        Getter for property: ( AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE) DisplayType
         Returns the display type   
            
         
        """
        pass
    @DisplayType.setter
    def DisplayType(self, displayType: AlignShellElementNormalBuilder.DisplayTypeValue):
        """
        Setter for property: ( AlignShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE) DisplayType
         Returns the display type   
            
         
        """
        pass
    @property
    def ElementConnectScope(self) -> AlignShellElementNormalBuilder.ConnectedElementScope:
        """
        Getter for property: ( AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE) ElementConnectScope
         Returns the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    @ElementConnectScope.setter
    def ElementConnectScope(self, connectScope: AlignShellElementNormalBuilder.ConnectedElementScope):
        """
        Setter for property: ( AlignShellElementNormalBuilder.ConnectedElementScope NXOpen.CAE) ElementConnectScope
         Returns the option to indicate how to define connected elements for checking   
            
         
        """
        pass
    @property
    def ElementSelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) ElementSelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                     NXOpen::CAE::FEElement    
         
        """
        pass
    @property
    def NegativeFaceColor(self) -> int:
        """
        Getter for property: (int) NegativeFaceColor
         Returns the negative face color   
            
         
        """
        pass
    @NegativeFaceColor.setter
    def NegativeFaceColor(self, negativeFaceColor: int):
        """
        Setter for property: (int) NegativeFaceColor
         Returns the negative face color   
            
         
        """
        pass
    @property
    def OrientMethod(self) -> AlignShellElementNormalBuilder.OrientMethodType:
        """
        Getter for property: ( AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE) OrientMethod
         Returns the option to indicate how to orient method to orient normal   
            
         
        """
        pass
    @OrientMethod.setter
    def OrientMethod(self, orientMethod: AlignShellElementNormalBuilder.OrientMethodType):
        """
        Setter for property: ( AlignShellElementNormalBuilder.OrientMethodType NXOpen.CAE) OrientMethod
         Returns the option to indicate how to orient method to orient normal   
            
         
        """
        pass
    @property
    def PositiveFaceColor(self) -> int:
        """
        Getter for property: (int) PositiveFaceColor
         Returns the positive face color   
            
         
        """
        pass
    @PositiveFaceColor.setter
    def PositiveFaceColor(self, positiveFaceColor: int):
        """
        Setter for property: (int) PositiveFaceColor
         Returns the positive face color   
            
         
        """
        pass
    @property
    def ReverseSeedNormal(self) -> bool:
        """
        Getter for property: (bool) ReverseSeedNormal
         Returns the option indicating whether to reverse element normals so that they are aligned with the seed element   
            
         
        """
        pass
    @ReverseSeedNormal.setter
    def ReverseSeedNormal(self, seedNormalToBeReversed: bool):
        """
        Setter for property: (bool) ReverseSeedNormal
         Returns the option indicating whether to reverse element normals so that they are aligned with the seed element   
            
         
        """
        pass
    @property
    def SeedElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: ( NXOpen.CAE.FEElement) SeedElement
         Returns the seed element   
            
         
        """
        pass
    @SeedElement.setter
    def SeedElement(self, seedElement: NXOpen.CAE.FEElement):
        """
        Setter for property: ( NXOpen.CAE.FEElement) SeedElement
         Returns the seed element   
            
         
        """
        pass
    @property
    def UserSpecifiedConnectElements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: ( NXOpen.CAE.SelectElementsBuilder) UserSpecifiedConnectElements
         Returns the user specified connected elements to be aligned with seed element   
            
         
        """
        pass
    def AlignNormals(self) -> List[NXOpen.CAE.FEElement]:
        """
         Aligns the normals of elements connected to the seed element. Returns the elements
                        that have had the normals successfully reversed. This method will only reverse
                        the normals for shell elements in the current work fem part.
                    
         Returns reversedElements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
    def DisplayNormals(self) -> None:
        """
         Display element normals for connected elements, which are to be aligned with seed element normal 
        """
        pass
    def FindAllVisibleConnectedElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Finds all visible elements connected with the seed element 
         Returns connectedElements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
class CheckScope(Enum):
    """
    Members Include: 
     |Displayed|  check all displayed elements or nodes 
     |Selected|  check selected elements or nodes 

    """
    Displayed: int
    Selected: int
    @staticmethod
    def ValueOf(value: int) -> CheckScope:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE
class CorrectBeamElementsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.ModelCheck.CorrectBeamElementsBuilder
            to check and correct for dangling nodes of 1d elements.
            
            It will check 1D elements for free leg nodes. 
            If any of the nodes of the 1D element is not connected to any other element, then it will be considered as a free leg node. 
                       
        """
    class ElementToCheck(Enum):
        """
        Members Include: 
         |Displayed|  All the displayed elements 
         |Selected|  Selected elements 

        """
        Displayed: int
        Selected: int
        @staticmethod
        def ValueOf(value: int) -> CorrectBeamElementsBuilder.ElementToCheck:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def ElemCheckOption(self) -> CorrectBeamElementsBuilder.ElementToCheck:
        """
        Getter for property: ( CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE) ElemCheckOption
         Returns the element select option .  
            
         
        """
        pass
    @ElemCheckOption.setter
    def ElemCheckOption(self, option: CorrectBeamElementsBuilder.ElementToCheck):
        """
        Setter for property: ( CorrectBeamElementsBuilder.ElementToCheck NXOpen.CAE) ElemCheckOption
         Returns the element select option .  
            
         
        """
        pass
    @property
    def ElementSelection(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: ( NXOpen.CAE.SelectElementsBuilder) ElementSelection
         Returns the selected elements   
            
         
        """
        pass
    @property
    def NodeToReplace(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: ( NXOpen.CAE.SelectFENodeList) NodeToReplace
         Returns the node to replace   
            
         
        """
        pass
    @property
    def ReplacementNode(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: ( NXOpen.CAE.SelectFENodeList) ReplacementNode
         Returns the replacement node  
            
         
        """
        pass
    def CorrectFailedElements(self, failedElement: NXOpen.CAE.FEElement, nodeToReplace: NXOpen.CAE.FENode, replacementNode: NXOpen.CAE.FENode) -> None:
        """
         Correct failed element
        """
        pass
    def CreateFailedElementsGroup(self, failedElement: List[NXOpen.CAE.FEElement]) -> None:
        """
         Create group of failed elements 
        """
        pass
    def DeleteDanglingNodesInElements(self, failedElement: List[NXOpen.CAE.FEElement]) -> None:
        """
         Delete dangling nodes of elements
        """
        pass
    def DeleteFailedElements(self, failedElement: List[NXOpen.CAE.FEElement]) -> None:
        """
         Delete failed elements
        """
        pass
    def IdentifyFailedElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Calculate the dangling nodes from selected or displayed elements
         Returns failedElement ( NXOpen.CAE.FEElement Li):  elements having dangling nodes.
        """
        pass
import NXOpen
import NXOpen.CAE
class DuplicateElementsCheckBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder
            to check for duplicate elements within the candidate elements.
            
            Duplicate elements are elements which share the same corner nodes,but do not include
            the middle nodes.
            
            The general workflow is:
            
             Set the candidate elements 
             Set the display settings data 
             Identify the duplicate elements 
             Set the preference option 
             Delete the duplicate elements 
            
            You can delete duplicate elements through Builder.Commit or
            NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DeleteDuplicateElements.
            Commits the builder to delete duplicate elements.
        """
    class DeletePreference(Enum):
        """
        Members Include: 
         |KeepHighLabel|  Keep the elements with higher labels 
         |KeepLowLabel|  Keep the elements with lower labels 
         |KeepSelected|  Keep the elements specified in the element list
                                                                                                         NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.PreferenceElements 
         |RemoveSelected|  Delete the elements specified in the element list
                                                                                                         NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.PreferenceElements 

        """
        KeepHighLabel: int
        KeepLowLabel: int
        KeepSelected: int
        RemoveSelected: int
        @staticmethod
        def ValueOf(value: int) -> DuplicateElementsCheckBuilder.DeletePreference:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplaySettings:
        """
         Represents the display settings of duplicated elements detected 
         DuplicateElementsCheckBuilderDisplaySettings_Struct NXOpen.CAE is an alias for  DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE.
        """
        @property
        def ShowDuplicateElements(self) -> bool:
            """
            Getter for property ShowDuplicateElements
            Whether to show duplicate elements

            """
            pass
        @ShowDuplicateElements.setter
        def ShowDuplicateElements(self, value: bool):
            """
            Getter for property ShowDuplicateElements
            Whether to show duplicate elements
            Setter for property ShowDuplicateElements
            Whether to show duplicate elements

            """
            pass
        @property
        def ShowElementLabels(self) -> bool:
            """
            Getter for property ShowElementLabels
            Whether to show labels of duplicate elements

            """
            pass
        @ShowElementLabels.setter
        def ShowElementLabels(self, value: bool):
            """
            Getter for property ShowElementLabels
            Whether to show labels of duplicate elements
            Setter for property ShowElementLabels
            Whether to show labels of duplicate elements

            """
            pass
        @property
        def ElementsColor(self) -> int:
            """
            Getter for property ElementsColor
            The display color of duplicate elements

            """
            pass
        @ElementsColor.setter
        def ElementsColor(self, value: int):
            """
            Getter for property ElementsColor
            The display color of duplicate elements
            Setter for property ElementsColor
            The display color of duplicate elements

            """
            pass
        @property
        def ElementsWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property ElementsWidth
            The display line width of duplicate elements

            """
            pass
        @ElementsWidth.setter
        def ElementsWidth(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property ElementsWidth
            The display line width of duplicate elements
            Setter for property ElementsWidth
            The display line width of duplicate elements

            """
            pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def DisplaySettingsData(self) -> DuplicateElementsCheckBuilder.DisplaySettings:
        """
        Getter for property: ( DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE) DisplaySettingsData
         Returns the display settings for duplicate elements   
            
         
        """
        pass
    @DisplaySettingsData.setter
    def DisplaySettingsData(self, displaySettings: DuplicateElementsCheckBuilder.DisplaySettings):
        """
        Setter for property: ( DuplicateElementsCheckBuilder.DisplaySettings NXOpen.CAE) DisplaySettingsData
         Returns the display settings for duplicate elements   
            
         
        """
        pass
    @property
    def DuplicateElementGroupsCount(self) -> int:
        """
        Getter for property: (int) DuplicateElementGroupsCount
         Returns the duplicate elements group count, each group contains elements that are
                        duplicates of each other and each group contains at least two duplicate elements   
            
         
        """
        pass
    @property
    def Preference(self) -> DuplicateElementsCheckBuilder.DeletePreference:
        """
        Getter for property: ( DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE) Preference
         Returns the duplicate elements deleting preference   
            
         
        """
        pass
    @Preference.setter
    def Preference(self, deletePreference: DuplicateElementsCheckBuilder.DeletePreference):
        """
        Setter for property: ( DuplicateElementsCheckBuilder.DeletePreference NXOpen.CAE) Preference
         Returns the duplicate elements deleting preference   
            
         
        """
        pass
    @property
    def PreferenceElements(self) -> NXOpen.CAE.SelectElementsBuilder:
        """
        Getter for property: ( NXOpen.CAE.SelectElementsBuilder) PreferenceElements
         Returns the preference elements for keep selected and remove selected options   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                         NXOpen::CAE::FEElement    
         
        """
        pass
    def DeleteDuplicateElements(self) -> None:
        """
         Deletes the duplicate elements and clear all cached duplicate elements in this builder.
                        The method Builder.Commit will also do the same thing. Duplicate elements
                        can only be deleted when the context part of this builder is a NXOpen.CAE.BaseFemPart 
        """
        pass
    def GetDuplicateElements(self, groupIndex: int) -> List[NXOpen.CAE.FEElement]:
        """
         Returns the duplicate elements of specified group index 
         Returns duplicateElements ( NXOpen.CAE.FEElement Li): .
        """
        pass
    def IdentifyDuplicateElements(self) -> None:
        """
         Calculates to find the duplicate elements and display them in the
                        NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings.
                        The detected duplicate elements are cached, to access the cached calculation result, you could use
                        NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DuplicateElementGroupsCount and
                        NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.GetDuplicateElements. The previous
                        cached data will be cleaned automatically when you start a new identification. 
        """
        pass
import NXOpen
import NXOpen.CAE
class DuplicateNodesCheckBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder
            to check for duplicate nodes within the candidate nodes.
            
            Duplicate nodes are nodes which distance between each other is less than
            specific tolerance value and at least one duplicate node can be merged away.
            
            The general workflow is:
            
             Set the candidate nodes 
             Set the check settings and display settings data 
             Identify the duplicate nodes 
             Set the preference option 
             Merge duplicate nodes 
            
            You can merge duplicate nodes through Builder.Commit or
            NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.MergeDuplicateNodes.
            Commits the builder to merge duplicate nodes and update the mesh in graphic window.
        """
    class ListOption(Enum):
        """
        Members Include: 
         |All|  List all duplicate node pairs found 
         |Mergeable|  List the duplicate node pairs mergeable 
         |Unmergeable|  List the duplicate node pairs unmergeable 

        """
        All: int
        Mergeable: int
        Unmergeable: int
        @staticmethod
        def ValueOf(value: int) -> DuplicateNodesCheckBuilder.ListOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MergePreference(Enum):
        """
        Members Include: 
         |NotSet|  No preference 
         |KeepHighLabel|  Keep the nodes with higher labels 
         |KeepLowLabel|  Keep the nodes with lower labels 
         |KeepSelected|  Keep the nodes specified in the node list
                                                                                                 NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.SelectPreferenceNodesList 
         |RemoveSelected|  Merge the nodes specified in the node list
                                                                                                 NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.SelectPreferenceNodesList 

        """
        NotSet: int
        KeepHighLabel: int
        KeepLowLabel: int
        KeepSelected: int
        RemoveSelected: int
        @staticmethod
        def ValueOf(value: int) -> DuplicateNodesCheckBuilder.MergePreference:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplaySettings:
        """
         Represents the display settings data 
         DuplicateNodesCheckBuilderDisplaySettings_Struct NXOpen.CAE is an alias for  DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE.
        """
        @property
        def ShowDuplicateNodes(self) -> bool:
            """
            Getter for property ShowDuplicateNodes
            Whether to show duplicate nodes

            """
            pass
        @ShowDuplicateNodes.setter
        def ShowDuplicateNodes(self, value: bool):
            """
            Getter for property ShowDuplicateNodes
            Whether to show duplicate nodes
            Setter for property ShowDuplicateNodes
            Whether to show duplicate nodes

            """
            pass
        @property
        def ShowMergedNodeLabels(self) -> bool:
            """
            Getter for property ShowMergedNodeLabels
            Whether to show merged node labels

            """
            pass
        @ShowMergedNodeLabels.setter
        def ShowMergedNodeLabels(self, value: bool):
            """
            Getter for property ShowMergedNodeLabels
            Whether to show merged node labels
            Setter for property ShowMergedNodeLabels
            Whether to show merged node labels

            """
            pass
        @property
        def ShowRetainedNodeLabels(self) -> bool:
            """
            Getter for property ShowRetainedNodeLabels
            Whether to show retained node labels

            """
            pass
        @ShowRetainedNodeLabels.setter
        def ShowRetainedNodeLabels(self, value: bool):
            """
            Getter for property ShowRetainedNodeLabels
            Whether to show retained node labels
            Setter for property ShowRetainedNodeLabels
            Whether to show retained node labels

            """
            pass
        @property
        def KeepNodesColor(self) -> int:
            """
            Getter for property KeepNodesColor
            The kept nodes display color

            """
            pass
        @KeepNodesColor.setter
        def KeepNodesColor(self, value: int):
            """
            Getter for property KeepNodesColor
            The kept nodes display color
            Setter for property KeepNodesColor
            The kept nodes display color

            """
            pass
        @property
        def MergeNodesColor(self) -> int:
            """
            Getter for property MergeNodesColor
            The merged nodes display color

            """
            pass
        @MergeNodesColor.setter
        def MergeNodesColor(self, value: int):
            """
            Getter for property MergeNodesColor
            The merged nodes display color
            Setter for property MergeNodesColor
            The merged nodes display color

            """
            pass
        @property
        def UnableToMergeNodesColor(self) -> int:
            """
            Getter for property UnableToMergeNodesColor
            """
            pass
        @UnableToMergeNodesColor.setter
        def UnableToMergeNodesColor(self, value: int):
            """
            Getter for property UnableToMergeNodesColorSetter for property UnableToMergeNodesColor
            """
            pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def DisplaySettingsData(self) -> DuplicateNodesCheckBuilder.DisplaySettings:
        """
        Getter for property: ( DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE) DisplaySettingsData
         Returns the display settings for duplicate nodes   
            
         
        """
        pass
    @DisplaySettingsData.setter
    def DisplaySettingsData(self, displaySettings: DuplicateNodesCheckBuilder.DisplaySettings):
        """
        Setter for property: ( DuplicateNodesCheckBuilder.DisplaySettings NXOpen.CAE) DisplaySettingsData
         Returns the display settings for duplicate nodes   
            
         
        """
        pass
    @property
    def DuplicateNodeGroupsCount(self) -> int:
        """
        Getter for property: (int) DuplicateNodeGroupsCount
         Returns the duplicate nodes group count, each group contains nodes that are
                        duplicates of each other and each group contains at least two duplicate nodes   
            
         
        """
        pass
    @property
    def IgnoreNodesConnectedToTinyEdges(self) -> bool:
        """
        Getter for property: (bool) IgnoreNodesConnectedToTinyEdges
         Returns a value indicating whether to ignore nodes connected to tiny edges   
            
         
        """
        pass
    @IgnoreNodesConnectedToTinyEdges.setter
    def IgnoreNodesConnectedToTinyEdges(self, ignoreTinyEdgeNodes: bool):
        """
        Setter for property: (bool) IgnoreNodesConnectedToTinyEdges
         Returns a value indicating whether to ignore nodes connected to tiny edges   
            
         
        """
        pass
    @property
    def IgnoreNodesInSameMesh(self) -> bool:
        """
        Getter for property: (bool) IgnoreNodesInSameMesh
         Returns a value indicating whether to ignore nodes in same mesh   
            
         
        """
        pass
    @IgnoreNodesInSameMesh.setter
    def IgnoreNodesInSameMesh(self, ignoreSameMeshNodes: bool):
        """
        Setter for property: (bool) IgnoreNodesInSameMesh
         Returns a value indicating whether to ignore nodes in same mesh   
            
         
        """
        pass
    @property
    def ListingType(self) -> DuplicateNodesCheckBuilder.ListOption:
        """
        Getter for property: ( DuplicateNodesCheckBuilder.ListOption NXOpen.CAE) ListingType
         Returns an option indicating what information to be listed   
            
         
        """
        pass
    @ListingType.setter
    def ListingType(self, listOption: DuplicateNodesCheckBuilder.ListOption):
        """
        Setter for property: ( DuplicateNodesCheckBuilder.ListOption NXOpen.CAE) ListingType
         Returns an option indicating what information to be listed   
            
         
        """
        pass
    @property
    def MergeOccurrenceNodes(self) -> bool:
        """
        Getter for property: (bool) MergeOccurrenceNodes
         Returns a value indicating whether to merge occurrence nodes in afem context   
            
         
        """
        pass
    @MergeOccurrenceNodes.setter
    def MergeOccurrenceNodes(self, mergeOccurrenceNodes: bool):
        """
        Setter for property: (bool) MergeOccurrenceNodes
         Returns a value indicating whether to merge occurrence nodes in afem context   
            
         
        """
        pass
    @property
    def Preference(self) -> DuplicateNodesCheckBuilder.MergePreference:
        """
        Getter for property: ( DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE) Preference
         Returns the duplicate nodes merging preference   
            
         
        """
        pass
    @Preference.setter
    def Preference(self, mergePreference: DuplicateNodesCheckBuilder.MergePreference):
        """
        Setter for property: ( DuplicateNodesCheckBuilder.MergePreference NXOpen.CAE) Preference
         Returns the duplicate nodes merging preference   
            
         
        """
        pass
    @property
    def SelectPreferenceNodesList(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: ( NXOpen.CAE.SelectFENodeList) SelectPreferenceNodesList
         Returns the preference nodes select list for keep selected and remove selected options   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects for checking.  
           The objects must be  NXOpen::CAE::Mesh  or
                         NXOpen::CAE::FENode    
         
        """
        pass
    @property
    def Tolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Tolerance
         Returns the tolerance used to determine if the nodes are duplicates of each other   
            
         
        """
        pass
    def GetDuplicateNodes(self, groupIndex: int) -> List[NXOpen.CAE.FENode]:
        """
         Returns the duplicate nodes of specified group index 
         Returns duplicateNodes ( NXOpen.CAE.FENode Li): .
        """
        pass
    def IdentifyDuplicateNodes(self) -> None:
        """
         Calculates to find the duplicate nodes and display them in
                        NXOpen.CAE.ModelCheck.DuplicateElementsCheckBuilder.DisplaySettings.
                        The detected duplicate nodes are cached, to access the cached calculation result, you could use
                        NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.DuplicateNodeGroupsCount and
                        NXOpen.CAE.ModelCheck.DuplicateNodesCheckBuilder.GetDuplicateNodes. The previous
                        cached data will be cleaned automatically when you start a new identification. 
        """
        pass
    def MergeDuplicateNodes(self) -> None:
        """
         Merges the duplicate nodes and clear all cached duplicate nodes in this builder.
                        The method Builder.Commit will also do the same thing. Duplicate nodes
                        can only be merged when the context part of this builder is a NXOpen.CAE.BaseFemPart. 
        """
        pass
import NXOpen
import NXOpen.CAE
class ElementEdgeCheckBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder which can be
            used to detect free element edges or non-manifold edges.
            
            A free edge is any Element edge that is not shared by any other element face (on
            either 2D or 3D elements ) within the defined scope of the check.
            A non-manifold edge is any Element edge that is shared more than 2 element faces (on
            either 2D or 3D elements ) within the defined scope of the check.
            
            The computation scope ElementEdgeCheckBuilder.ComputationScope
            will affect on the checking result. The free element edges or non-manifold edges found will
            be displayed using the display setting NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.EdgeDisplayStyle.
            You can execute checking through Builder.Commit or
            NXOpen.CAE.ModelCheck.ElementEdgeCheckBuilder.ExecuteCheck. Commiting the builder
            performs checking and displays the free edges and non-manifold edges in graphic window.
        """
    class Scope(Enum):
        """
        Members Include: 
         |EntireModel|  Takes all elements in the model into account while computing 
         |VisibleModel|  Only takes visible elements into account while computing 
         |SelectedModels|  Only takes selected elements into account while computing 

        """
        EntireModel: int
        VisibleModel: int
        SelectedModels: int
        @staticmethod
        def ValueOf(value: int) -> ElementEdgeCheckBuilder.Scope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EdgeDisplayStyle:
        """
         the display style of the edges detected 
         ElementEdgeCheckBuilderEdgeDisplayStyle_Struct NXOpen.CAE is an alias for  ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE.
        """
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            line font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            line font
            Setter for property Font
            line font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            line width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            line width
            Setter for property Width
            line width

            """
            pass
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            line color

            """
            pass
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            line color
            Setter for property Color
            line color

            """
            pass
    @property
    def CheckFreeEdges(self) -> bool:
        """
        Getter for property: (bool) CheckFreeEdges
         Returns the value indicating whether to check free edges or not   
            
         
        """
        pass
    @CheckFreeEdges.setter
    def CheckFreeEdges(self, checkFreeEdges: bool):
        """
        Setter for property: (bool) CheckFreeEdges
         Returns the value indicating whether to check free edges or not   
            
         
        """
        pass
    @property
    def CheckNonManifoldEdges(self) -> bool:
        """
        Getter for property: (bool) CheckNonManifoldEdges
         Returns the value indicating whether to check non-manifold edges or not   
            
         
        """
        pass
    @CheckNonManifoldEdges.setter
    def CheckNonManifoldEdges(self, checkNonManifoldEdges: bool):
        """
        Setter for property: (bool) CheckNonManifoldEdges
         Returns the value indicating whether to check non-manifold edges or not   
            
         
        """
        pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def ComputationScope(self) -> ElementEdgeCheckBuilder.Scope:
        """
        Getter for property: ( ElementEdgeCheckBuilder.Scope NXOpen.CAE) ComputationScope
         Returns the computation scope   
            
         
        """
        pass
    @ComputationScope.setter
    def ComputationScope(self, computationScope: ElementEdgeCheckBuilder.Scope):
        """
        Setter for property: ( ElementEdgeCheckBuilder.Scope NXOpen.CAE) ComputationScope
         Returns the computation scope   
            
         
        """
        pass
    @property
    def FreeEdgeDisplayStyle(self) -> ElementEdgeCheckBuilder.EdgeDisplayStyle:
        """
        Getter for property: ( ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE) FreeEdgeDisplayStyle
         Returns the display style for free edges detected   
            
         
        """
        pass
    @FreeEdgeDisplayStyle.setter
    def FreeEdgeDisplayStyle(self, freeEdgesStyle: ElementEdgeCheckBuilder.EdgeDisplayStyle):
        """
        Setter for property: ( ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE) FreeEdgeDisplayStyle
         Returns the display style for free edges detected   
            
         
        """
        pass
    @property
    def NonManifoldEdgeDisplayStyle(self) -> ElementEdgeCheckBuilder.EdgeDisplayStyle:
        """
        Getter for property: ( ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE) NonManifoldEdgeDisplayStyle
         Returns the displaying style for non-manifold edges detected   
            
         
        """
        pass
    @NonManifoldEdgeDisplayStyle.setter
    def NonManifoldEdgeDisplayStyle(self, nonManifoldEdgeStyle: ElementEdgeCheckBuilder.EdgeDisplayStyle):
        """
        Setter for property: ( ElementEdgeCheckBuilder.EdgeDisplayStyle NXOpen.CAE) NonManifoldEdgeDisplayStyle
         Returns the displaying style for non-manifold edges detected   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                         NXOpen::CAE::FEElement    
         
        """
        pass
    def DoCheck(self) -> Tuple[List[NXOpen.CAE.FEElemEdge], List[NXOpen.CAE.FEElemEdge], List[NXOpen.CAE.FEElement], NXOpen.CAE.CaeGroup]:
        """
         Finds free edges when CAE.ModelCheck.ElementEdgeCheckBuilder.CheckFreeEdges is set,
                        and non-manifold edges when CAE.ModelCheck.ElementEdgeCheckBuilder.CheckNonManifoldEdges is set,
                        returns the associated elements and output group for free andor non-manifold element edges.
                        For the associated elements, if both checks are done at the same time, the elements associated to free edges are
                        returned firstly in the list.
                     
         Returns A tuple consisting of (freeEdges, nonManifoldEdges, assoElems, outputGroup). 
         - freeEdges is:  NXOpen.CAE.FEElemEdge Li. free element edges .
         - nonManifoldEdges is:  NXOpen.CAE.FEElemEdge Li. non-manifold element edges .
         - assoElems is:  NXOpen.CAE.FEElement Li. associated elements for free andor non-manifold element edges,
                                                                                                 if both checks are done at the same time, the elements associated
                                                                                                 to free edges are returned firstly in the list.
                                                                                              .
         - outputGroup is:  NXOpen.CAE.CaeGroup. output group for free andor non-manifold element edges .

        """
        pass
    def ExecuteCheck(self) -> Tuple[List[NXOpen.CAE.FEElemEdge], List[NXOpen.CAE.FEElemEdge]]:
        """
         Finds free edges when CAE.ModelCheck.ElementEdgeCheckBuilder.CheckFreeEdges is set,
                        and non-manifold edges when CAE.ModelCheck.ElementEdgeCheckBuilder.CheckNonManifoldEdges is set.
                        The method Builder.Commit will also do the same thing,
                        but display the element edges instead of returning them.
                     
         Returns A tuple consisting of (freeEdges, nonManifoldEdges). 
         - freeEdges is:  NXOpen.CAE.FEElemEdge Li. free element edges .
         - nonManifoldEdges is:  NXOpen.CAE.FEElemEdge Li. non-manifold element edges .

        """
        pass
    def HideInputMeshes(self, hideInputMeshes: bool) -> None:
        """
         Hides or unhides the input meshes 
        """
        pass
import NXOpen
import NXOpen.CAE
class ElementMaterialOrientationCheckBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder
            used to check the material orientation for shell and solid elements.
            Use Builder.Commit to calculate material orientation and to display
            an orientation vector for each input element.
            Use NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.DoCheck
            to calculate the material orientation for each input element and return the orientation vector
            result. If an element fails when calculating its material orientation,
            the element will be displayed in red and listed in an information window.
        """
    class MaterialOrientationArrowheadType(Enum):
        """
        Members Include: 
         |ShowArrowHead|  the arrowheads are shown 
         |HideArrowHead|  the arrowheads are hidden 

        """
        ShowArrowHead: int
        HideArrowHead: int
        @staticmethod
        def ValueOf(value: int) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialOrientationSolidElementDisplayType(Enum):
        """
        Members Include: 
         |SolidAllElements|  all solid elements 
         |SolidExteriorElements|  only exterior solid elements 

        """
        SolidAllElements: int
        SolidExteriorElements: int
        @staticmethod
        def ValueOf(value: int) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialOrientationType(Enum):
        """
        Members Include: 
         |Shell|  the material orientation of shell element 
         |SolidFirstDirection|  the first  direction of solid element material orientation 
         |SolidSecondDirection|  the second direction of solid element material orientation 
         |SolidThirdDirection|  the third  direction of solid element material orientation 

        """
        Shell: int
        SolidFirstDirection: int
        SolidSecondDirection: int
        SolidThirdDirection: int
        @staticmethod
        def ValueOf(value: int) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrowPercentage(self) -> int:
        """
        Getter for property: (int) ArrowPercentage
         Returns the percentage of how many arrows should be displayed.  
             
         
        """
        pass
    @ArrowPercentage.setter
    def ArrowPercentage(self, arrowPercentage: int):
        """
        Setter for property: (int) ArrowPercentage
         Returns the percentage of how many arrows should be displayed.  
             
         
        """
        pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def CheckShellOrientation(self) -> bool:
        """
        Getter for property: (bool) CheckShellOrientation
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @CheckShellOrientation.setter
    def CheckShellOrientation(self, checkShellOrientation: bool):
        """
        Setter for property: (bool) CheckShellOrientation
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @property
    def CheckSolidExteriorOnly(self) -> bool:
        """
        Getter for property: (bool) CheckSolidExteriorOnly
         Returns the exterior solid elements only toggle.  
             
         
        """
        pass
    @CheckSolidExteriorOnly.setter
    def CheckSolidExteriorOnly(self, checkSolidExteriorOnly: bool):
        """
        Setter for property: (bool) CheckSolidExteriorOnly
         Returns the exterior solid elements only toggle.  
             
         
        """
        pass
    @property
    def CheckSolidFirstDirection(self) -> bool:
        """
        Getter for property: (bool) CheckSolidFirstDirection
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @CheckSolidFirstDirection.setter
    def CheckSolidFirstDirection(self, checkShellOrientation: bool):
        """
        Setter for property: (bool) CheckSolidFirstDirection
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @property
    def CheckSolidSecondDirection(self) -> bool:
        """
        Getter for property: (bool) CheckSolidSecondDirection
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @CheckSolidSecondDirection.setter
    def CheckSolidSecondDirection(self, checkShellOrientation: bool):
        """
        Setter for property: (bool) CheckSolidSecondDirection
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @property
    def CheckSolidThirdDirection(self) -> bool:
        """
        Getter for property: (bool) CheckSolidThirdDirection
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @CheckSolidThirdDirection.setter
    def CheckSolidThirdDirection(self, checkShellOrientation: bool):
        """
        Setter for property: (bool) CheckSolidThirdDirection
         Returns the shell orientation toggle.  
             
         
        """
        pass
    @property
    def EnableArrowShowThrough(self) -> bool:
        """
        Getter for property: (bool) EnableArrowShowThrough
         Returns the arrow show through value.  
             
         
        """
        pass
    @EnableArrowShowThrough.setter
    def EnableArrowShowThrough(self, arrowShowThrough: bool):
        """
        Setter for property: (bool) EnableArrowShowThrough
         Returns the arrow show through value.  
             
         
        """
        pass
    @property
    def EnableTranslucency(self) -> bool:
        """
        Getter for property: (bool) EnableTranslucency
         Returns the option which indicates whether to enable translucency or not.  
             
         
        """
        pass
    @EnableTranslucency.setter
    def EnableTranslucency(self, enableTranslucency: bool):
        """
        Setter for property: (bool) EnableTranslucency
         Returns the option which indicates whether to enable translucency or not.  
             
         
        """
        pass
    @property
    def HideArrowhead(self) -> bool:
        """
        Getter for property: (bool) HideArrowhead
         Returns the hide arrow head toggle.  
             
         
        """
        pass
    @HideArrowhead.setter
    def HideArrowhead(self, hideArrowhead: bool):
        """
        Setter for property: (bool) HideArrowhead
         Returns the hide arrow head toggle.  
             
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                         NXOpen::CAE::FEElement    
         
        """
        pass
    @property
    def ShellOrientationColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ShellOrientationColor
         Returns the shell orientation color.  
             
         
        """
        pass
    @ShellOrientationColor.setter
    def ShellOrientationColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ShellOrientationColor
         Returns the shell orientation color.  
             
         
        """
        pass
    @property
    def SolidFirstDirectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SolidFirstDirectionColor
         Returns the solid first direction color.  
             
         
        """
        pass
    @SolidFirstDirectionColor.setter
    def SolidFirstDirectionColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SolidFirstDirectionColor
         Returns the solid first direction color.  
             
         
        """
        pass
    @property
    def SolidSecondDirectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SolidSecondDirectionColor
         Returns the solid first direction color.  
             
         
        """
        pass
    @SolidSecondDirectionColor.setter
    def SolidSecondDirectionColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SolidSecondDirectionColor
         Returns the solid first direction color.  
             
         
        """
        pass
    @property
    def SolidThirdDirectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SolidThirdDirectionColor
         Returns the solid first direction color.  
             
         
        """
        pass
    @SolidThirdDirectionColor.setter
    def SolidThirdDirectionColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SolidThirdDirectionColor
         Returns the solid first direction color.  
             
         
        """
        pass
    @property
    def TranslucencyPercentage(self) -> int:
        """
        Getter for property: (int) TranslucencyPercentage
         Returns the translucency percentage.  
             
         
        """
        pass
    @TranslucencyPercentage.setter
    def TranslucencyPercentage(self, translucencyPercentage: int):
        """
        Setter for property: (int) TranslucencyPercentage
         Returns the translucency percentage.  
             
         
        """
        pass
    def Display(self) -> None:
        """
         
                            Will display the data that was calculated with
                            NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.RequestData before.
                        
                        
                            This is what you will see when recording scripts.
                            If you are writing scripts manually, you can use Builder.Commit,
                            which is the same as calling both methods in one go.
                         
        """
        pass
    def DoCheck(self) -> Tuple[List[NXOpen.Vector3d], List[ElementMaterialOrientationCheckBuilder.MaterialOrientationType], List[NXOpen.CAE.FEElement]]:
        """
         Calculates the material orientation vector for input elements and returns the orientation vector result. 
         Returns A tuple consisting of (orientation, orientationType, elements). 
         - orientation is:  NXOpen.Vector3d Li. material orientation vector .
         - orientationType is:  ElementMaterialOrientationCheckBuilder.MaterialOrientationType List[NXOpen.C.
         - elements is:  NXOpen.CAE.FEElement Li. the elements associated with the orientation vectors.

        """
        pass
    def GetArrowDensity(self) -> int:
        """
         Gets the percentage of how many arrows should be displayed. 
         Returns arrowDensity (int): .
        """
        pass
    def GetArrowShowThrough(self) -> bool:
        """
         Gets the arrow show through value. 
         Returns arrowShowThrough (bool): .
        """
        pass
    def GetArrowheadDisplayType(self) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType:
        """
         Gets the arrowhead display type. 
         Returns displayType ( ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType NXOpen.CAE): .
        """
        pass
    def GetCheckOrientation(self, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType) -> bool:
        """
         Gets the option value which indicates whether to check for the specified material orientation type. 
         Returns checkOrientation (bool): .
        """
        pass
    def GetCheckTranslucency(self) -> bool:
        """
         Gets the option value which indicates whether to set translucency or not. 
         Returns checkOrientation (bool): .
        """
        pass
    def GetOrientationColor(self, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType) -> NXOpen.NXColor:
        """
         Gets the display color of a specified material orientation type. 
         Returns color ( NXOpen.NXColor): .
        """
        pass
    def GetSolidElementDisplayType(self) -> ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType:
        """
         Gets the solid element display type. 
         Returns displayType ( ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType NXOpen.CAE): .
        """
        pass
    def GetTranslucencyValue(self) -> int:
        """
         Gets the translucency value. 
         Returns translucencyValue (int): .
        """
        pass
    def RequestData(self) -> None:
        """
         
                            Calculates material orientation vector for input elements and keeps that data internally as a prerequisite
                            to call NXOpen.CAE.ModelCheck.ElementMaterialOrientationCheckBuilder.Display later.
                        
                        
                            This is what you will see when recording scripts.
                            If you are writing scripts manually, you can use Builder.Commit,
                            which is the same as calling both methods in one go.
                         
        """
        pass
    def SetArrowDensity(self, arrowDensity: int) -> None:
        """
         Sets the percentage of how many arrows should be displayed. 
        """
        pass
    def SetArrowShowThrough(self, arrowShowThrough: bool) -> None:
        """
         Sets the arrow show through value. 
        """
        pass
    def SetArrowheadDisplayType(self, displayType: ElementMaterialOrientationCheckBuilder.MaterialOrientationArrowheadType) -> None:
        """
         Sets the arrowhead display type. 
        """
        pass
    def SetCheckOrientation(self, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType, checkOrientation: bool) -> None:
        """
         Sets the option value which indicates whether to check for the specified material orientation type. 
        """
        pass
    def SetCheckTranslucency(self, checkOrientation: bool) -> None:
        """
         Sets the option value which indicates whether to set translucency or not. 
        """
        pass
    def SetOrientationColor(self, orientationType: ElementMaterialOrientationCheckBuilder.MaterialOrientationType, color: NXOpen.NXColor) -> None:
        """
         Sets the display color of a specified material orientation type. 
        """
        pass
    def SetSolidElementDisplayType(self, displayType: ElementMaterialOrientationCheckBuilder.MaterialOrientationSolidElementDisplayType) -> None:
        """
         Sets the solid element display type. 
        """
        pass
    def SetTranslucencyValue(self, translucencyValue: int) -> None:
        """
         Sets the translucency value. 
        """
        pass
import NXOpen
import NXOpen.CAE
class ElementQualityCheckBuilder(NXOpen.Builder): 
    """Represents a NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder to
         perform quality checking on the candidate elements. Set the properties of the 
        NXOpen.CAE.ModelCheck.ElementQualitySetting instance for the
        current solver language in the CAE part to define the specific quality checks to perform. 

        Those elements with failed quality check results will be displayed according to the display setting
        NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ShowFailedElementsLabel and 
        NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.FailedElementsColor.

        The report will be generated according to NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ElementReportFormat

        You can do element quality check by Builder.Commit and 
        NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ExecuteCheck. 
        Builder.Commit performs the check, displays the failed elements and generates the report 
        in a listing window. But NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder just performs the check and
        returns the check result NXOpen.CAE.ModelCheck.ElementQualityCheckResults
        """
    class OutputElements(Enum):
        """
        Members Include: 
         |NotSet|  Output nothing 
         |Failed|  Creates OUTPUT group with failed elements 
         |Warning|  Creates OUTPUT group with warning elements 
         |FailedAndWarning|  Creates OUTPUT group with both warning and failed elements 

        """
        NotSet: int
        Failed: int
        Warning: int
        FailedAndWarning: int
        @staticmethod
        def ValueOf(value: int) -> ElementQualityCheckBuilder.OutputElements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportFormat(Enum):
        """
        Members Include: 
         |NotSet|  Does not generate report 
         |Worst|  Only lists check results for elements with worst results in the report 
         |Failed|  Only lists check results for elements with error results in the report 
         |Warning|  Only lists check results for elements with warning results in the report 
         |FailedAndWarning|  Lists check results for elements with both error and warning results in the report 
         |All|  Lists check results for all elements 

        """
        NotSet: int
        Worst: int
        Failed: int
        Warning: int
        FailedAndWarning: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ElementQualityCheckBuilder.ReportFormat:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def ElementReportFormat(self) -> ElementQualityCheckBuilder.ReportFormat:
        """
        Getter for property: ( ElementQualityCheckBuilder.ReportFormat NXOpen.CAE) ElementReportFormat
         Returns the report style   
            
         
        """
        pass
    @ElementReportFormat.setter
    def ElementReportFormat(self, reportElements: ElementQualityCheckBuilder.ReportFormat):
        """
        Setter for property: ( ElementQualityCheckBuilder.ReportFormat NXOpen.CAE) ElementReportFormat
         Returns the report style   
            
         
        """
        pass
    @property
    def ElementsOutputOption(self) -> ElementQualityCheckBuilder.OutputElements:
        """
        Getter for property: ( ElementQualityCheckBuilder.OutputElements NXOpen.CAE) ElementsOutputOption
         Returns the element output options   
            
         
        """
        pass
    @ElementsOutputOption.setter
    def ElementsOutputOption(self, outputElements: ElementQualityCheckBuilder.OutputElements):
        """
        Setter for property: ( ElementQualityCheckBuilder.OutputElements NXOpen.CAE) ElementsOutputOption
         Returns the element output options   
            
         
        """
        pass
    @property
    def FailedElementsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FailedElementsColor
         Returns the display color of failed elements   
            
         
        """
        pass
    @FailedElementsColor.setter
    def FailedElementsColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FailedElementsColor
         Returns the display color of failed elements   
            
         
        """
        pass
    @property
    def NumberFormat(self) -> NXOpen.CAE.NumberFormat:
        """
        Getter for property: ( NXOpen.CAE.NumberFormat) NumberFormat
         Returns the number format option   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                         NXOpen::CAE::FEElement    
         
        """
        pass
    @property
    def ShowFailedElementsLabel(self) -> bool:
        """
        Getter for property: (bool) ShowFailedElementsLabel
         Returns the value indicating whether to show label for those failed elements   
            
         
        """
        pass
    @ShowFailedElementsLabel.setter
    def ShowFailedElementsLabel(self, showFailedElementsLabel: bool):
        """
        Setter for property: (bool) ShowFailedElementsLabel
         Returns the value indicating whether to show label for those failed elements   
            
         
        """
        pass
    @property
    def WarningElementsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WarningElementsColor
         Returns the display color of warning elements   
            
         
        """
        pass
    @WarningElementsColor.setter
    def WarningElementsColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WarningElementsColor
         Returns the display color of warning elements   
            
         
        """
        pass
    def AttemptFixFailingElements(self, testTypes: List[TestValueTypes.TestType]) -> None:
        """
         Attempt fixing the element quality of failed elements for given test types 
        """
        pass
    def AttemptFixFailingSelectedElements(self, testTypes: List[TestValueTypes.TestType], elements: List[NXOpen.CAE.FEElement]) -> None:
        """
         Attempt fixing the element quality of failed selected elements for given test types 
        """
        pass
    def ExecuteCheck(self) -> ElementQualityCheckResults:
        """
         
                        Returns the results after performing element quality check on the target elements or meshes,
                        and displays the warned andor failed elements.
                        
                        
                        
                        
                        The target elements or meshes are set by calling NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.SelectionList
                        
                        
                        You could also use Builder.Commit to do the check,
                        the differences are that Builder.Commit generates the report to listing window but does not return the results.
                        
                        
                        
                    
         Returns checkResults ( ElementQualityCheckResults NXOpen.CAE): .
        """
        pass
    def WriteResultsToFile(self, outputFile: str, eqcResults: ElementQualityCheckResults) -> None:
        """
         
                        Writes the element quality check results into a text file.
                        
                        
                        
                        
                        The text file is overriden with the element quality check results if it already exists.
                        
                        
                        NXOpen.CAE.ModelCheck.ElementQualityCheckResults are generated by calling
                        NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ExecuteCheck.
                        
                        
                        The settings of NXOpen.CAE.NumberFormat can be changed after calling
                        NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.NumberFormat.
                        
                        
                        The report format can be changed with NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder.ElementReportFormat.
                        
                        
                        
                    
        """
        pass
import NXOpen
class ElementQualityCheckResults(NXOpen.TransientObject): 
    """ Represents the element quality checking result of NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder
    """
    class TestSummary:
        """
         Reprents the summary data of a specified quality checking test type 
         ElementQualityCheckResultsTestSummary_Struct NXOpen.CAE is an alias for  ElementQualityCheckResults.TestSummary NXOpen.CAE.
        """
        @property
        def TestType(self) -> TestValueTypes.TestType:
            """
            Getter for property TestType
            the test type

            """
            pass
        @TestType.setter
        def TestType(self, value: TestValueTypes.TestType):
            """
            Getter for property TestType
            the test type
            Setter for property TestType
            the test type

            """
            pass
        @property
        def WorstTestValue(self) -> float:
            """
            Getter for property WorstTestValue
            the worst test value of the specified test within all checked elements.

            """
            pass
        @WorstTestValue.setter
        def WorstTestValue(self, value: float):
            """
            Getter for property WorstTestValue
            the worst test value of the specified test within all checked elements.
            Setter for property WorstTestValue
            the worst test value of the specified test within all checked elements.

            """
            pass
        @property
        def HasTestValue(self) -> bool:
            """
            Getter for property HasTestValue
            indicates whether the test has a test value.

            """
            pass
        @HasTestValue.setter
        def HasTestValue(self, value: bool):
            """
            Getter for property HasTestValue
            indicates whether the test has a test value.
            Setter for property HasTestValue
            indicates whether the test has a test value.

            """
            pass
        @property
        def TestCount(self) -> int:
            """
            Getter for property TestCount
            indicates the total number of elements tested for this test

            """
            pass
        @TestCount.setter
        def TestCount(self, value: int):
            """
            Getter for property TestCount
            indicates the total number of elements tested for this test
            Setter for property TestCount
            indicates the total number of elements tested for this test

            """
            pass
        @property
        def ErrorCount(self) -> int:
            """
            Getter for property ErrorCount
            the count of elements with error results

            """
            pass
        @ErrorCount.setter
        def ErrorCount(self, value: int):
            """
            Getter for property ErrorCount
            the count of elements with error results
            Setter for property ErrorCount
            the count of elements with error results

            """
            pass
        @property
        def WarnedCount(self) -> int:
            """
            Getter for property WarnedCount
            the count of elements with warning results.

            """
            pass
        @WarnedCount.setter
        def WarnedCount(self, value: int):
            """
            Getter for property WarnedCount
            the count of elements with warning results.
            Setter for property WarnedCount
            the count of elements with warning results.

            """
            pass
    @property
    def ElementTestCount(self) -> int:
        """
        Getter for property: (int) ElementTestCount
         Returns the total number of element tested during a test session   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetElementTestResultByIndex(self, index: int) -> ElementTestResult:
        """
         Returns test results of each element. Caller needs to free the memory of the test result by NXOpen.CAE.ModelCheck.ElementTestResult.JA_EQ_ELEM_RESULT_Dispose.
         Returns elementResult ( ElementTestResult NXOpen.CAE): .
        """
        pass
    def GetTestSummary(self) -> List[ElementQualityCheckResults.TestSummary]:
        """
         Returns summary data of tests executed by NXOpen.CAE.ModelCheck.ElementQualityCheckBuilder
         Returns testSummaries ( ElementQualityCheckResults.TestSummary List[NXOpen.C): .
        """
        pass
import NXOpen
class ElementQualitySettingCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.CAE.ModelCheck.ElementQualitySetting in a cae part.  """
    def FindObject(self, journalIdentifier: str) -> ElementQualitySetting:
        """
         Finds the NXOpen.CAE.ModelCheck.ElementQualitySetting with the given identifier as
                    recorded in a journal. An exception will be thrown if no object can be found with the given
                    journal identifier 
                
         Returns found ( ElementQualitySetting NXOpen.CAE):  .
        """
        pass
    def GetElementQualitySetting(self, solverName: str) -> ElementQualitySetting:
        """
         Retuns the NXOpen.CAE.ModelCheck.ElementQualitySetting of a specified solver. 
         Returns pEQValues ( ElementQualitySetting NXOpen.CAE):  .
        """
        pass
import NXOpen
import NXOpen.CAE
class ElementQualitySetting(NXOpen.NXObject): 
    """
    

    Represents element quality check settings of a specified solver language. Each solve language has a
    NXOpen.CAE.ModelCheck.ElementQualitySetting.

    To get a quality check criteria value of a specfied quality test for one element, you can call
    NXOpen.CAE.ModelCheck.ElementQualitySetting.LocateTestDescriptorName to get the test
    criteria value name, then call NXOpen.CAE.ModelCheck.ElementQualitySetting.GetQualityValue to
    get the criteria value object.


    
    """
    class LimitValue(Enum):
        """
        Members Include: 
         |WarningAndErrorLimit|  Both warning and error criteria value could be defined  
         |ErrorLimitOnly|  Only error criteria value could be defined 
         |ExtendedOptions|  All the criteria values could be defined 

        """
        WarningAndErrorLimit: int
        ErrorLimitOnly: int
        ExtendedOptions: int
        @staticmethod
        def ValueOf(value: int) -> ElementQualitySetting.LimitValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LimitValueOption(self) -> ElementQualitySetting.LimitValue:
        """
        Getter for property: ( ElementQualitySetting.LimitValue NXOpen.CAE) LimitValueOption
         Returns the limit value option   
            
         
        """
        pass
    @LimitValueOption.setter
    def LimitValueOption(self, limitValueOption: ElementQualitySetting.LimitValue):
        """
        Setter for property: ( ElementQualitySetting.LimitValue NXOpen.CAE) LimitValueOption
         Returns the limit value option   
            
         
        """
        pass
    @property
    def TestValueCount(self) -> int:
        """
        Getter for property: (int) TestValueCount
         Returns the count of  NXOpen::CAE::ModelCheck::QualityTestValue  in the setting   
            
         
        """
        pass
    @property
    def UseElementSpecificValue(self) -> bool:
        """
        Getter for property: (bool) UseElementSpecificValue
         Returns an option indicating whether to use element specific quality value for testing   
            
         
        """
        pass
    @UseElementSpecificValue.setter
    def UseElementSpecificValue(self, useElementSpecificValue: bool):
        """
        Setter for property: (bool) UseElementSpecificValue
         Returns an option indicating whether to use element specific quality value for testing   
            
         
        """
        pass
    def GetQualityValue(self, descriptorName: str) -> ITestValue:
        """
         Returns the test quality value with the specified descriptor name 
         Returns qualityValue ( ITestValue NXOpen.CAE): .
        """
        pass
    def GetTestValueByIndex(self, index: int) -> QualityTestValue:
        """
        Returns the NXOpen.CAE.ModelCheck.QualityTestValue at the specified index in the setting  
         Returns pTestValue ( QualityTestValue NXOpen.CAE):  .
        """
        pass
    def GetTestValueByType(self, testType: TestValueTypes.TestType) -> QualityTestValue:
        """
         Returns the NXOpen.CAE.ModelCheck.QualityTestValue of a specified NXOpen.CAE.ModelCheck.TestValueTypes.TestType 
         Returns pTestValue ( QualityTestValue NXOpen.CAE): .
        """
        pass
    def LocateTestDescriptorName(self, element: NXOpen.CAE.FEElement, testType: TestValueTypes.TestType, useElemSpecific: bool) -> str:
        """
         Returns the name of a quality test value, which is associated with
                    an element for a specified test type 
         Returns descriptorName (str): .
        """
        pass
    def ResetToCustomerDefault(self) -> None:
        """
         Reset the quality check setting as customer default 
        """
        pass
import NXOpen
class ElementSpecificTestValue(NXOpen.NXObject): 
    """  Represents the quality setting for a specfied element reference  """
    @property
    def DoTest(self) -> bool:
        """
        Getter for property: (bool) DoTest
         Returns an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    @DoTest.setter
    def DoTest(self, doTest: bool):
        """
        Setter for property: (bool) DoTest
         Returns an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
import NXOpen
import NXOpen.CAE
class ElementTestResult(NXOpen.TransientObject): 
    """ Represents quality checking result for an element.  """
    @property
    def OverallResult(self) -> TestValueTypes.Result:
        """
        Getter for property: ( TestValueTypes.Result NXOpen.CAE) OverallResult
         Returns the overall result of this element.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetTestElement(self) -> NXOpen.CAE.FEElement:
        """
         Returns the element associated with quality test results 
         Returns pElementTag ( NXOpen.CAE.FEElement): .
        """
        pass
    def GetTestResults(self) -> List[TestResult]:
        """
         Returns the quality test results of this element 
         Returns testResults ( TestResult List[NXOpen.C): .
        """
        pass
import NXOpen
import NXOpen.CAE
class FaceClearanceCheckBuilder(NXOpen.Builder): 
    """Represents a NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder to perform polygon face
    interference or clearance check. You can do the check by Builder.Commit or 
    NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder.DoCheck. Builder.Commit
    performs the check and displays the failed faces in graphics window. NXOpen.CAE.ModelCheck.FaceClearanceCheckBuilder.DoCheck
    performs the check and if faces are detected violating the check, returns the output group containing the failed faces.
    """
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the clearance.  
           If the clearance value is zero, an intersection check between faces will be
                performed. If the clearance value is non-zero, a clearance check will be performed. If a negative
                non-zero clearance is set, the absolute value will be used   
         
        """
        pass
    def DoCheck(self) -> NXOpen.CAE.CaeGroup:
        """
         Perform the clearance check. All polygon faces on the current display are considered for
                the check. If polygon faces are detected as intersecting or violating the given clearance, they
                are placed in a group, which would be returned 
         Returns faceSet ( NXOpen.CAE.CaeGroup):  the group contains the failed faces .
        """
        pass
import NXOpen
import NXOpen.CAE
class IElementQualityChecker(NXOpen.TransientObject): 
    """  Represents the iterface of solver element quality checker which calculate all kinds of element quality check results.  """
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
    def GetArea(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets area value for 2D element face. 
         Returns pArea (float): .
        """
        pass
    def GetAspectRatio(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets aspect ratio value. 
         Returns pAspectRatio (float): .
        """
        pass
    def GetAxisRadius(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets axis radius value. 
         Returns pAxisRadius (float): .
        """
        pass
    def GetCohesiveElementRatio(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets cohesive element ratio value. 
         Returns pCohesRatio (float): .
        """
        pass
    def GetCollapse(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets collapse value. 
         Returns pCollapseValue (float): .
        """
        pass
    def GetConsistDistance(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets consist distance value. 
         Returns pConsistDistance (float): .
        """
        pass
    def GetEdgePointLengthRatioAndAngle(self, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float]:
        """
         Gets edge point length ratio and edge point included angle. 
         Returns A tuple consisting of (pRatioValue, pAngleValue). 
         - pRatioValue is: float.
         - pAngleValue is: float.

        """
        pass
    def GetElementSize(self, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float, float]:
        """
         Gets minimum, maximum and average element edge length. 
         Returns A tuple consisting of (pMinSize, pMazSize, pAvgSize). 
         - pMinSize is: float.
         - pMazSize is: float.
         - pAvgSize is: float.

        """
        pass
    def GetInteriorAngle(self, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float]:
        """
         Gets minimum and maximum interior angle value. 
         Returns A tuple consisting of (pMinAngle, pMaxAngle). 
         - pMinAngle is: float.
         - pMaxAngle is: float.

        """
        pass
    def GetJacobian(self, pElem: NXOpen.CAE.FEElement) -> Tuple[float, float, bool]:
        """
         Gets jacobian value. 
         Returns A tuple consisting of (pJacobianZero, pJacobianRatio, pJacobianSign). 
         - pJacobianZero is: float.
         - pJacobianRatio is: float.
         - pJacobianSign is: bool.

        """
        pass
    def GetLaminateRatio(self, pElem: NXOpen.CAE.FEElement, matMatrix: NXOpen.Matrix3x3, stackAxis: int, totalPlyThick: float) -> Tuple[float, float]:
        """
         Calculates ratio of longest edge to shortest edge in stacking direction and
                        ratio of the difference between thickness in stacking direction as defined by grids and thickness as defined by ply thickness specification
                        to the thickness in the stacking direction as defined by grids for CHEXA and CPENTA elements referencing PCOMPS entries only. 
         Returns A tuple consisting of (lamEdgeRatio, lamThickRatio). 
         - lamEdgeRatio is: float.
         - lamThickRatio is: float.

        """
        pass
    def GetOffsetLengthRatio(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets element offset length ratio for beam and bar element. 
         Returns pOffsetLengthRatio (float): .
        """
        pass
    def GetParallelDeviation(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets parallel deviation angle. 
         Returns pParallelDeviation (float): .
        """
        pass
    def GetShapeFactor(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets shape factor. 
         Returns pShapeFactor (float): .
        """
        pass
    def GetSkew(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets skew value. 
         Returns pSkewValue (float): .
        """
        pass
    def GetTaper(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets taper value. 
         Returns pTaperValue (float): .
        """
        pass
    def GetTwist(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets twist value. 
         Returns pTwistValue (float): .
        """
        pass
    def GetVolume(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets volume value for 3D element. 
         Returns pVolume (float): .
        """
        pass
    def GetWarp(self, pElem: NXOpen.CAE.FEElement) -> float:
        """
         Gets warp factor value. 
         Returns pWarpValue (float): .
        """
        pass
import NXOpen
class ISelectionBuilder(NXOpen.Object): 
    """  Represents the model check selection builder  """
    @property
    @abstractmethod
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
import NXOpen
class ITestValue(NXOpen.Object): 
    """  Represents the quality check criteria value settings  """
    @property
    @abstractmethod
    def DoTest(self) -> bool:
        """
        Getter for property: (bool) DoTest
         Returns an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    @DoTest.setter
    def DoTest(self, doTest: bool):
        """
        Setter for property: (bool) DoTest
         Returns an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    @abstractmethod
    def GetCriteriaValue(self, criteriaType: TestValueTypes.CriteriaType) -> Tuple[NXOpen.Unit, float]:
        """
         Returns the criteria value. An exception will be thrown if there is no criteria value associated with this test 
         Returns A tuple consisting of (unit, criteriaValue). 
         - unit is:  NXOpen.Unit.
         - criteriaValue is: float.

        """
        pass
    @abstractmethod
    def GetElementReferences(self) -> List[TestValueTypes.ElementReference]:
        """
         Returns the element reference definitions associated with this test 
         Returns elemReferences ( TestValueTypes.ElementReference List[NXOpen.C): .
        """
        pass
    @abstractmethod
    def GetIsSolverSpecificTest(self) -> Tuple[bool, bool]:
        """
         To know whether this quality test is a solver specific test and a system test 
         Returns A tuple consisting of (isSolverSpecificTest, isSystemTest). 
         - isSolverSpecificTest is: bool.
         - isSystemTest is: bool.

        """
        pass
    @abstractmethod
    def GetTestType(self) -> TestValueTypes.TestType:
        """
         Returns the test type 
         Returns testType ( TestValueTypes.TestType NXOpen.CAE): .
        """
        pass
    @abstractmethod
    def GetValidator(self) -> TestValueTypes.Validator:
        """
         Returns the validator type 
         Returns validator ( TestValueTypes.Validator NXOpen.CAE): .
        """
        pass
    @abstractmethod
    def HasCriteriaValue(self) -> bool:
        """
         Tells whether there is criteria value associated with this test 
         Returns hasCriteriaValue (bool): .
        """
        pass
    @abstractmethod
    def ResetToCustomerDefault(self) -> None:
        """
         Reset as customer default setting 
        """
        pass
    @abstractmethod
    @overload
    def SetCriteriaValue(self, criteriaType: TestValueTypes.CriteriaType, criteriaValue: float, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        """
        pass
    @abstractmethod
    @overload
    def SetCriteriaValue(self, criteriaType: TestValueTypes.CriteriaType, criteriaValue: str, unit: NXOpen.Unit) -> None:
        """
        Sets the criteria value. An exception will be thrown if there is no criteria value associated with this test 
        """
        pass
import NXOpen
class ModelSetupCheckBuilder(NXOpen.Builder): 
    """Represents a NXOpen.CAE.ModelCheck.ModelSetupCheckBuilder which can be
        used to check if the active NXOpen.CAE.SimSolution contains all the necessary 
        items for the analysis, including elements, loads, constraints and materials. Also it could check 
        label conficts and component connect status.
        Builder.Commit performs the check. The check result is written into a report
        file or listed in a separate information window, along with an error summary for each topic  """
    @property
    def CheckAllComponents(self) -> bool:
        """
        Getter for property: (bool) CheckAllComponents
         Returns the value indicating whether to check all components associated with the assembly FEM in the 
                        model check, regardless of load status.  
           If false, only the fully loaded components are included 
                        in the check   
         
        """
        pass
    @CheckAllComponents.setter
    def CheckAllComponents(self, checkAllComponents: bool):
        """
        Setter for property: (bool) CheckAllComponents
         Returns the value indicating whether to check all components associated with the assembly FEM in the 
                        model check, regardless of load status.  
           If false, only the fully loaded components are included 
                        in the check   
         
        """
        pass
    @property
    def CheckLabelConflicts(self) -> bool:
        """
        Getter for property: (bool) CheckLabelConflicts
         Returns the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
                    and reports the label range in which the conflict occurs   
            
         
        """
        pass
    @CheckLabelConflicts.setter
    def CheckLabelConflicts(self, checkLabelConflicts: bool):
        """
        Setter for property: (bool) CheckLabelConflicts
         Returns the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
                    and reports the label range in which the conflict occurs   
            
         
        """
        pass
    @property
    def CheckUnconnectedComponent(self) -> bool:
        """
        Getter for property: (bool) CheckUnconnectedComponent
         Returns the option specifying whether to check for component FEMs that are not connected    
            
         
        """
        pass
    @CheckUnconnectedComponent.setter
    def CheckUnconnectedComponent(self, checkUnconnectedComponent: bool):
        """
        Setter for property: (bool) CheckUnconnectedComponent
         Returns the option specifying whether to check for component FEMs that are not connected    
            
         
        """
        pass
    @property
    def IsDetailedMessage(self) -> bool:
        """
        Getter for property: (bool) IsDetailedMessage
         Returns the value indicating whether to list comprehensive descriptions of any problems and suggest
                        possible remedies.  
           If false, only the simple descriptions of problems are listed   
         
        """
        pass
    @IsDetailedMessage.setter
    def IsDetailedMessage(self, isDetailedMessage: bool):
        """
        Setter for property: (bool) IsDetailedMessage
         Returns the value indicating whether to list comprehensive descriptions of any problems and suggest
                        possible remedies.  
           If false, only the simple descriptions of problems are listed   
         
        """
        pass
    @property
    def ReportFileName(self) -> str:
        """
        Getter for property: (str) ReportFileName
         Returns the full name of the report file.  
           If NULL, the report is listed in a separate listing window    
         
        """
        pass
    @ReportFileName.setter
    def ReportFileName(self, reportFileName: str):
        """
        Setter for property: (str) ReportFileName
         Returns the full name of the report file.  
           If NULL, the report is listed in a separate listing window    
         
        """
        pass
    def DoCheck(self) -> int:
        """
         Performs model setup check
         Returns checkStatus (int):  Model setup checking result. Zero indicates the checking is successful .
        """
        pass
import NXOpen
class QualityTestValue(NXOpen.NXObject): 
    """  Represents quality test settings of a specified test type  """
    @property
    def DoTest(self) -> bool:
        """
        Getter for property: (bool) DoTest
         Returns an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    @DoTest.setter
    def DoTest(self, doTest: bool):
        """
        Setter for property: (bool) DoTest
         Returns an option value indicating whether to do element quality check for this test    
            
         
        """
        pass
    @property
    def ElementSpecificTestCount(self) -> int:
        """
        Getter for property: (int) ElementSpecificTestCount
         Returns the count of  NXOpen::CAE::ModelCheck::ElementSpecificTestValue  in this test setting   
            
         
        """
        pass
    def GetElementSpecificTestByIndex(self, index: int) -> ElementSpecificTestValue:
        """
         Returns NXOpen.CAE.ModelCheck.ElementSpecificTestValue of specified index in this test setting 
         Returns pElemTestValue ( ElementSpecificTestValue NXOpen.CAE): .
        """
        pass
import NXOpen
import NXOpen.CAE
class ReverseBeamElementDirectionBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder used to reverse directions
        for specified beam elements. You can reverse beam element directions by using either Builder.Commit
        or NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.ReverseDirections.
        The difference between these two methods is Builder.Commit reverses the directions
        and updates direction display, but it does not return the beam elements which were reversed
        successfully. NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.ReverseDirections 
        reverses directions and returns the beam elements which were reversed successfully.
        Both of the methods are only available in fem context.
        """
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                     NXOpen::CAE::FEElement    
         
        """
        pass
    def DisplayDirections(self) -> None:
        """
         Display directions of NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.SelectionList 
        """
        pass
    def ReverseDirections(self) -> List[NXOpen.CAE.FEElement]:
        """
         Reverses directions specified in NXOpen.CAE.ModelCheck.ReverseBeamElementDirectionBuilder.SelectionList
                        and returns those elements whose directions were reversed successfully. This method will only reverse
                        the directions for beam elements in the current work fem part.
                    
         Returns reversedElements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
import NXOpen
import NXOpen.CAE
class ReverseShellElementNormalBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder used to reverse normals
        for specified shell elements. You can reverse shell element normals by using either Builder.Commit
        or NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.ReverseNormals.
        The difference between these two methods is Builder.Commit reverses the normals
        and updates normal display, but it does not return the shell elements which were reversed
        successfully. NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.ReverseNormals 
        reverses normals and returns the shell elements which were reversed successfully.
        Both of the methods are only available in fem context.
        """
    class DisplayTypeValue(Enum):
        """
        Members Include: 
         |Arrows| 
         |SolidFaceColors| 

        """
        Arrows: int
        SolidFaceColors: int
        @staticmethod
        def ValueOf(value: int) -> ReverseShellElementNormalBuilder.DisplayTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def DisplayType(self) -> ReverseShellElementNormalBuilder.DisplayTypeValue:
        """
        Getter for property: ( ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE) DisplayType
         Returns the display type   
            
         
        """
        pass
    @DisplayType.setter
    def DisplayType(self, displayType: ReverseShellElementNormalBuilder.DisplayTypeValue):
        """
        Setter for property: ( ReverseShellElementNormalBuilder.DisplayTypeValue NXOpen.CAE) DisplayType
         Returns the display type   
            
         
        """
        pass
    @property
    def NegativeFaceColor(self) -> int:
        """
        Getter for property: (int) NegativeFaceColor
         Returns the negative face color   
            
         
        """
        pass
    @NegativeFaceColor.setter
    def NegativeFaceColor(self, negativeFaceColor: int):
        """
        Setter for property: (int) NegativeFaceColor
         Returns the negative face color   
            
         
        """
        pass
    @property
    def PositiveFaceColor(self) -> int:
        """
        Getter for property: (int) PositiveFaceColor
         Returns the positive face color   
            
         
        """
        pass
    @PositiveFaceColor.setter
    def PositiveFaceColor(self, positiveFaceColor: int):
        """
        Setter for property: (int) PositiveFaceColor
         Returns the positive face color   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                     NXOpen::CAE::FEElement    
         
        """
        pass
    def CreateElementGroupOfSubdomains(self) -> List[NXOpen.NXObject]:
        """
         Create element group of subdomains 
         Returns ppSubdomainGroupTag ( NXOpen.NXObject Li):  Arrary of subdomain groups tag .
        """
        pass
    def CreateInconsistentElementEdgeGroup(self) -> NXOpen.CAE.CaeGroup:
        """
         Creates inconsistent element edge group 
                    
         Returns groupTag ( NXOpen.CAE.CaeGroup):  .
        """
        pass
    def DisplayNormals(self) -> None:
        """
         Display normals of NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.SelectionList 
        """
        pass
    def ReverseNormals(self) -> List[NXOpen.CAE.FEElement]:
        """
         Reverses normals specified in NXOpen.CAE.ModelCheck.ReverseShellElementNormalBuilder.SelectionList
                        and returns those elements whose normals were reversed successfully. This method will only reverse
                        the normals for shell elements in the current work fem part.
                    
         Returns reversedElements ( NXOpen.CAE.FEElement Li):  .
        """
        pass
import NXOpen
class SolidElementFaceNormalBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder used to reorient normals
        for left handed solid elements.
        Both of the methods are only available in fem context.
        """
    @property
    def CheckScopeOption(self) -> CheckScope:
        """
        Getter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @CheckScopeOption.setter
    def CheckScopeOption(self, scope: CheckScope):
        """
        Setter for property: ( CheckScope NXOpen.CAE) CheckScopeOption
         Returns the check scope setting   
            
         
        """
        pass
    @property
    def NegativeFaceColor(self) -> int:
        """
        Getter for property: (int) NegativeFaceColor
         Returns the negative face color   
            
         
        """
        pass
    @NegativeFaceColor.setter
    def NegativeFaceColor(self, negativeFaceColor: int):
        """
        Setter for property: (int) NegativeFaceColor
         Returns the negative face color   
            
         
        """
        pass
    @property
    def PositiveFaceColor(self) -> int:
        """
        Getter for property: (int) PositiveFaceColor
         Returns the positive face color   
            
         
        """
        pass
    @PositiveFaceColor.setter
    def PositiveFaceColor(self, positiveFaceColor: int):
        """
        Setter for property: (int) PositiveFaceColor
         Returns the positive face color   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectionList
         Returns the selected objects to be checked.  
           The objects must be  NXOpen::CAE::Mesh  or
                     NXOpen::CAE::FEElement    
         
        """
        pass
    def CreateGroupOfLeftHandedElements(self) -> None:
        """
         Create group for the left handed elements in
                        NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder.CreateGroupOfLeftHandedElements
                        and returns those elements which were grouped successfully. This method will only group left handed solid elements
                        in the current work fem part.
                    
        """
        pass
    def DisplayNormals(self) -> None:
        """
         Display normals of NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder.DisplayNormals 
        """
        pass
    def ReorientLeftHandedElements(self) -> None:
        """
         Reorient normals specified in NXOpen.CAE.ModelCheck.SolidElementFaceNormalBuilder.ReorientLeftHandedElements
                        which normal is left handed and returns those elements whose normals were reoriented successfully. This method will only reorient
                        the normals for solid left handed elements in the current work fem part.
                    
        """
        pass
import NXOpen
class TestResult(NXOpen.TransientObject): 
    """ Represents quality checking result of a quality test
    """
    @property
    def TestType(self) -> TestValueTypes.TestType:
        """
        Getter for property: ( TestValueTypes.TestType NXOpen.CAE) TestType
         Returns the test type   
            
         
        """
        pass
    @property
    def TestValue(self) -> float:
        """
        Getter for property: (float) TestValue
         Returns the test value.  
           An exception will be thrown f there is no test value associated with this test   
         
        """
        pass
    @property
    def ValidatedTestResult(self) -> TestValueTypes.Result:
        """
        Getter for property: ( TestValueTypes.Result NXOpen.CAE) ValidatedTestResult
         Returns the validation result of comparing test value with the criteria value.  
          
                    if no test value is associated this test, the result just indicates the test 
                    is passed or failed   
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def HasTestValue(self) -> bool:
        """
         Tells whether there is a test value associated with this test 
         Returns hasTestValue (bool): .
        """
        pass
import NXOpen
class TestValueTypes(NXOpen.Object): 
    """  Represents the quality check criteria value settings  """
    class CriteriaType(Enum):
        """
        Members Include: 
         |Warning|  reports as warning if the check result failed with the criteria value 
         |Error|  reports as error if the check result failed with the criteria value 
         |Worst|  reports as worst if the check result failed with the criteria value 

        """
        Warning: int
        Error: int
        Worst: int
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.CriteriaType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Result(Enum):
        """
        Members Include: 
         |Passed|  indicates the test value does not violate the criteria values 
         |Failed|  indicates the test value violates the error criteria value 
         |Exception|  indicates there is an exception thrown during the checking 
         |NotApply|  indicates the test is not available or not done for an element  
         |Warned|  indicates the test value violates the warning criteria value 

        """
        Passed: int
        Failed: int
        Exception: int
        NotApply: int
        Warned: int
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TestType(Enum):
        """
        Members Include: 
         |JacobianZero|  
         |JacobianRatio|  
         |JacobianSign|  
         |Volume|  
         |AxisymmetricY|  When elements are modeled in XZ plane,
                                                                          check consistent Y.
                                                                          When elements are modeled in XY plane,
                                                                          check consistent Z.
         |AxisymmetricX|  When elements are modeled in XZ plane,
                                                                          check X = 0.0.
                                                                          When elements are modeled in XY plane,
                                                                          check Y = 0.0.
         |AspectRatio|  
         |SkewAngle|  
         |InteriorAngleMinimum|  
         |InteriorAngleMaximum|  
         |Taper|  
         |WarpFactor|  
         |FaceWarpCoefficient|  
         |EdgePointLengthRatio|  
         |EdgePointIncludedAngle|  
         |LengthRatioOffset|  
         |ParallelDeviation|  
         |ShapeFactor|  
         |Twist|  
         |LengthMinimum|  
         |LengthMaximum|  
         |TetCollapse|  
         |WarpageAngle|  
         |CohesiveElement|  
         |LaminateTaperRatio|  Ratio of longest edge to shortest edge in
                                                                          stacking direction for the elements
                                                                          that reference PCOMPS entries only.
         |LaminateThicknessRatio|  Ratio of the difference between thickness
                                                                          in stacking direction as defined by grids
                                                                          and thickness as defined by ply thickness
                                                                          specification to the thickness in the stacking
                                                                          direction as defined by grids for the elements
                                                                          that reference PCOMPS entries only.
         |Area|  

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
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.TestType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Validator(Enum):
        """
        Members Include: 
         |NotSet|  indicates no criteria value defined, not necessary to compare the check result with criteria value 
         |GreatThan|  the check passes if the check result is great than the criteria value 
         |GreatThanOrEqual|  the check passes if the check result is equal or great than the criteria value 
         |SmallThan|  the check passes if the check result is small than the criteria value 
         |SmallThanOrEqual|  the check passes if the check result is equal or small than the criteria value 

        """
        NotSet: int
        GreatThan: int
        GreatThanOrEqual: int
        SmallThan: int
        SmallThanOrEqual: int
        @staticmethod
        def ValueOf(value: int) -> TestValueTypes.Validator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ElementReference:
        """
         represents an element reference definition associated with this test 
         TestValueTypesElementReference_Struct NXOpen.CAE is an alias for  TestValueTypes.ElementReference NXOpen.CAE.
        """
        @property
        def ElementTypeName(self) -> str:
            """
            Getter for property ElementTypeName
            the element type name, which is defined in solver specific item

            """
            pass
        @ElementTypeName.setter
        def ElementTypeName(self, value: str):
            """
            Getter for property ElementTypeName
            the element type name, which is defined in solver specific item
            Setter for property ElementTypeName
            the element type name, which is defined in solver specific item

            """
            pass
        @property
        def ElementPropertyName(self) -> str:
            """
            Getter for property ElementPropertyName
            a specified integer element property name

            """
            pass
        @ElementPropertyName.setter
        def ElementPropertyName(self, value: str):
            """
            Getter for property ElementPropertyName
            a specified integer element property name
            Setter for property ElementPropertyName
            a specified integer element property name

            """
            pass
        @property
        def ElementPropertyValue(self) -> int:
            """
            Getter for property ElementPropertyValue
            the control value of integer element property, only valid when property name is not NULL

            """
            pass
        @ElementPropertyValue.setter
        def ElementPropertyValue(self, value: int):
            """
            Getter for property ElementPropertyValue
            the control value of integer element property, only valid when property name is not NULL
            Setter for property ElementPropertyValue
            the control value of integer element property, only valid when property name is not NULL

            """
            pass
