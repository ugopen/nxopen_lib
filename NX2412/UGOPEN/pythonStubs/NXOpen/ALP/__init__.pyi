from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddExternalResourceBuilder(NXOpen.Builder): 
    """ use for add external resource """
    @property
    def SelectComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectComponents
         Returns the select components   
            
         
        """
        pass
    @property
    def SelectResources(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectResources
         Returns the select resources   
            
         
        """
        pass
    def SearchResources(self) -> None:
        """
         The search resources 
        """
        pass
import NXOpen
class AddMfgFeaturesBuilder(NXOpen.Builder): 
    """ use for cearting Add Mfg Features """
    class Class(Enum):
        """
        Members Include: 
         |Discrete| 
         |Continuous| 

        """
        Discrete: int
        Continuous: int
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.Class:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConnectedTo(Enum):
        """
        Members Include: 
         |AllStationParts| 
         |PartList| 

        """
        AllStationParts: int
        PartList: int
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.ConnectedTo:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FeatureAssignmentState(Enum):
        """
        Members Include: 
         |UnassignedFeatures| 
         |AssignedFeatures| 
         |All| 

        """
        UnassignedFeatures: int
        AssignedFeatures: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.FeatureAssignmentState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |All| 
         |Weld| 
         |Fds| 
         |Clinch| 
         |Stud| 
         |Nut| 
         |Bolt| 
         |Rivet| 

        """
        All: int
        Weld: int
        Fds: int
        Clinch: int
        Stud: int
        Nut: int
        Bolt: int
        Rivet: int
        @staticmethod
        def ValueOf(value: int) -> AddMfgFeaturesBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignmentState(self) -> AddMfgFeaturesBuilder.FeatureAssignmentState:
        """
        Getter for property: ( AddMfgFeaturesBuilder.FeatureAssignmentState NXOp) AssignmentState
         Returns the assignment state   
            
         
        """
        pass
    @AssignmentState.setter
    def AssignmentState(self, assignmentState: AddMfgFeaturesBuilder.FeatureAssignmentState):
        """
        Setter for property: ( AddMfgFeaturesBuilder.FeatureAssignmentState NXOp) AssignmentState
         Returns the assignment state   
            
         
        """
        pass
    @property
    def CriteriaConnectedTo(self) -> AddMfgFeaturesBuilder.ConnectedTo:
        """
        Getter for property: ( AddMfgFeaturesBuilder.ConnectedTo NXOp) CriteriaConnectedTo
         Returns the criteria connected to   
            
         
        """
        pass
    @CriteriaConnectedTo.setter
    def CriteriaConnectedTo(self, criteriaConnectedTo: AddMfgFeaturesBuilder.ConnectedTo):
        """
        Setter for property: ( AddMfgFeaturesBuilder.ConnectedTo NXOp) CriteriaConnectedTo
         Returns the criteria connected to   
            
         
        """
        pass
    @property
    def FeatureClass(self) -> AddMfgFeaturesBuilder.Class:
        """
        Getter for property: ( AddMfgFeaturesBuilder.Class NXOp) FeatureClass
         Returns the feature class   
            
         
        """
        pass
    @FeatureClass.setter
    def FeatureClass(self, featureClass: AddMfgFeaturesBuilder.Class):
        """
        Setter for property: ( AddMfgFeaturesBuilder.Class NXOp) FeatureClass
         Returns the feature class   
            
         
        """
        pass
    @property
    def FeatureType(self) -> AddMfgFeaturesBuilder.Type:
        """
        Getter for property: ( AddMfgFeaturesBuilder.Type NXOp) FeatureType
         Returns the feature type   
            
         
        """
        pass
    @FeatureType.setter
    def FeatureType(self, featureType: AddMfgFeaturesBuilder.Type):
        """
        Setter for property: ( AddMfgFeaturesBuilder.Type NXOp) FeatureType
         Returns the feature type   
            
         
        """
        pass
    @property
    def SelectParts(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectParts
         Returns the select parts   
            
         
        """
        pass
    def SearchButton(self) -> None:
        """
         The Search Button 
        """
        pass
import NXOpen
class AddWorkareaBuilder(NXOpen.Builder): 
    """ use for creating workarea builder"""
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def ParentPartOccurance(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    @ParentPartOccurance.setter
    def ParentPartOccurance(self, parent: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    @property
    def WorkareaTypeName(self) -> str:
        """
        Getter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    @WorkareaTypeName.setter
    def WorkareaTypeName(self, workareaType: str):
        """
        Setter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    def GetInternalName(self, displayName: str) -> str:
        """
         Get internal name  
         Returns internalName (str): .
        """
        pass
    def SetInternalName(self, displayName: str, internalName: str) -> None:
        """
         Set Expression internal name  
        """
        pass
import NXOpen
class ALPApplicationBuilder(NXOpen.NXObject): 
    """
    Represents a class to create enter and exit the ALP application
    """
    def Enter(self) -> None:
        """
          Enter the ALP application 
        """
        pass
    def Exit(self) -> None:
        """
          Exit the ALP application this call will destroy the builder
        """
        pass
    def GetGlobalSelectionBuilder(self) -> GlobalSelectionBuilder:
        """
         Get the global selection builder
         Returns selectionBuilder ( GlobalSelectionBuilder NXOp): .
        """
        pass
import NXOpen
class ALPManager(NXOpen.Object): 
    """ Represents a manager of ALP builders """
    def CloseApplication() -> None:
        """
          
                close ALP Application
                 
        """
        pass
    def ConsolidateUndoMarks(undoMarkId: int) -> None:
        """
        Consolidate Undo Marks 
        """
        pass
    def CreateAddExternalResourceBuilder(part: NXOpen.Part) -> AddExternalResourceBuilder:
        """
         Creates Add External Resource Builder
         Returns builder ( AddExternalResourceBuilder NXOp):  .
        """
        pass
    def CreateAddMfgFeaturesBuilder(part: NXOpen.Part) -> AddMfgFeaturesBuilder:
        """
         Creates a Add MFG Features Dialoge Builder
         Returns builder ( AddMfgFeaturesBuilder NXOp):  .
        """
        pass
    def CreateAddWorkareaBuilder(part: NXOpen.Part) -> AddWorkareaBuilder:
        """
         Creates Add Workarea Builder
         Returns builder ( AddWorkareaBuilder NXOp):  .
        """
        pass
    def CreateApplicationBuilder(part: NXOpen.Part) -> ALPApplicationBuilder:
        """
         Create the application builder 
         Returns builder ( ALPApplicationBuilder NXOp):  .
        """
        pass
    def CreateAutoWeldDistributionBuilder(part: NXOpen.Part) -> AutoWeldDistributionBuilder:
        """
         Creates auto_weld_distribution builder
         Returns builder ( AutoWeldDistributionBuilder NXOp):  .
        """
        pass
    def CreateCaptureImageBuilder(part: NXOpen.Part) -> CaptureImageBuilder:
        """
         Creates a capture image Dialoge Builder
         Returns builder ( CaptureImageBuilder NXOp):  .
        """
        pass
    def CreateConfigVariantConditionBuilder(part: NXOpen.Part) -> ConfigVariantConditionBuilder:
        """
         Creates Config Variant Conditions Dialoge Builder
         Returns builder ( ConfigVariantConditionBuilder NXOp):  .
        """
        pass
    def CreateCycleTimeBuilder(part: NXOpen.Part) -> CycleTimeBuilder:
        """
         Creates a Cycle Time Dialoge Builder
         Returns builder ( CycleTimeBuilder NXOp):  .
        """
        pass
    def CreateFlowsManagerBuilder(part: NXOpen.Part) -> FlowsManagerBuilder:
        """
         Creates flows manager builder
         Returns builder ( FlowsManagerBuilder NXOp):  .
        """
        pass
    def CreateGlobalSelectionBuilder(part: NXOpen.Part) -> GlobalSelectionBuilder:
        """
         Create global selection builder 
         Returns builder ( GlobalSelectionBuilder NXOp): .
        """
        pass
    def CreateLibraryOperationBuilder(part: NXOpen.Part) -> LibraryOperationBuilder:
        """
         Creates libray operation builder
         Returns builder ( LibraryOperationBuilder NXOp):  .
        """
        pass
    def CreateMaterialFlowNode(part: NXOpen.Part) -> MaterialFlowNode:
        """
         Creates material flow node
         Returns builder ( MaterialFlowNode NXOp):  .
        """
        pass
    def CreateModifyVariantBuilder(part: NXOpen.Part) -> ModifyVariantBuilder:
        """
         Creates Modify Variant Builder
         Returns builder ( ModifyVariantBuilder NXOp):  .
        """
        pass
    def CreateOperationBuilder(part: NXOpen.Part) -> OperationBuilder:
        """
         Creates a Operation Dialoge Builder
         Returns builder ( OperationBuilder NXOp):  .
        """
        pass
    def CreateOperationGroupBuilder(part: NXOpen.Part) -> OperationGroupBuilder:
        """
         Creates Operation Group Builder
         Returns builder ( OperationGroupBuilder NXOp):  .
        """
        pass
    def CreatePositionProductBuilder(part: NXOpen.Part) -> PositionProductBuilder:
        """
         Creates a Position Product Dialoge Builder
         Returns builder ( PositionProductBuilder NXOp):  .
        """
        pass
    def CreateStationTaktTimeBuilder(part: NXOpen.Part) -> StationTaktTimeBuilder:
        """
         Creates station takt time builder
         Returns builder ( StationTaktTimeBuilder NXOp):  .
        """
        pass
    def CreateSuggestPartBuilder(part: NXOpen.Part) -> SuggestPartBuilder:
        """
         Creates suggest part builder
         Returns builder ( SuggestPartBuilder NXOp):  .
        """
        pass
    def CreateValidateToolBuilder(part: NXOpen.Part) -> ValidateToolBuilder:
        """
         Creates validate tool builder
         Returns builder ( ValidateToolBuilder NXOp):  .
        """
        pass
    def CreateVariantConditionBuilder(part: NXOpen.Part) -> VariantConditionBuilder:
        """
         Creates Variant conditions Dialoge Builder
         Returns builder ( VariantConditionBuilder NXOp):  .
        """
        pass
    def CreateWeldConsistencyCheckerBuilder(part: NXOpen.Part) -> WeldConsistencyCheckerBuilder:
        """
         Creates weld_consistency_checker_builder
         Returns builder ( WeldConsistencyCheckerBuilder NXOp):  .
        """
        pass
    def GetApplicationBuilder() -> ALPApplicationBuilder:
        """
         Application builder is return 
         Returns builder ( ALPApplicationBuilder NXOp): .
        """
        pass
    def OpenApplication(lineItemID: str, lineRevisionID: str, ccUUID: str, variantObject: NXOpen.NXObject) -> None:
        """
          
                Opens ALP Application
                 
        """
        pass
class AlpPertLayout(Enum):
    """
    Members Include: 
     |Toptobottom| 
     |Lefttoright| 

    """
    Toptobottom: int
    Lefttoright: int
    @staticmethod
    def ValueOf(value: int) -> AlpPertLayout:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class AutoWeldDistributionBuilder(NXOpen.Builder): 
    """ use for creation of Automatic Weld Distribution Builder """
    @property
    def SelectedLine(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectedLine
         Returns the selected line property   
            
         
        """
        pass
    def CalculateProposal(self) -> None:
        """
         The method calculate a new weld distribution proposal 
        """
        pass
    def ExecuteProposal(self) -> None:
        """
         The method execute the new weld distribution proposal 
        """
        pass
    def GetSelectedLineObject(self) -> NXOpen.TaggedObject:
        """
         The selected line object method 
         Returns selectLine ( NXOpen.TaggedObject): .
        """
        pass
    def SortChildStationsByFlows(self, selectLine: NXOpen.TaggedObject) -> None:
        """
         The method sort the child stations by flows and scope flows 
        """
        pass
    def SuppressStation(self, stationTag: NXOpen.TaggedObject, bSuppress: bool) -> None:
        """
         The method suppress station from proposal 
        """
        pass
import NXOpen
class CaptureImageBuilder(NXOpen.Builder): 
    """ """
    class CaptureImage(Enum):
        """
        Members Include: 
         |Trimetric| 
         |Isometric| 
         |Top| 
         |Bottom| 
         |Left| 
         |Right| 
         |Front| 
         |Back| 

        """
        Trimetric: int
        Isometric: int
        Top: int
        Bottom: int
        Left: int
        Right: int
        Front: int
        Back: int
        @staticmethod
        def ValueOf(value: int) -> CaptureImageBuilder.CaptureImage:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EmphasizeToggle(self) -> bool:
        """
        Getter for property: (bool) EmphasizeToggle
         Returns the emphasize toggle   
            
         
        """
        pass
    @EmphasizeToggle.setter
    def EmphasizeToggle(self, emphasizeToggle: bool):
        """
        Setter for property: (bool) EmphasizeToggle
         Returns the emphasize toggle   
            
         
        """
        pass
    @property
    def PartOccOfSelectedNode(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) PartOccOfSelectedNode
         Returns
                a method that gets the partOCc from the Diagraming Node
                  
            
         
        """
        pass
    @PartOccOfSelectedNode.setter
    def PartOccOfSelectedNode(self, partOccFromDiagramingNode: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) PartOccOfSelectedNode
         Returns
                a method that gets the partOCc from the Diagraming Node
                  
            
         
        """
        pass
    @property
    def SelectNode(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectNode
         Returns the select node   
            
         
        """
        pass
    @property
    def View(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) View
         Returns
                a method that gets the view tag from the UI, 
                  
            
         
        """
        pass
    @View.setter
    def View(self, viewTag: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) View
         Returns
                a method that gets the view tag from the UI, 
                  
            
         
        """
        pass
    @property
    def ViewChangeEnum(self) -> CaptureImageBuilder.CaptureImage:
        """
        Getter for property: ( CaptureImageBuilder.CaptureImage NXOp) ViewChangeEnum
         Returns the view change enum   
            
         
        """
        pass
    @ViewChangeEnum.setter
    def ViewChangeEnum(self, viewChangeEnum: CaptureImageBuilder.CaptureImage):
        """
        Setter for property: ( CaptureImageBuilder.CaptureImage NXOp) ViewChangeEnum
         Returns the view change enum   
            
         
        """
        pass
    def EmphasiseAssignedProduct(self, emphasize: bool, onlyDIPA: bool) -> None:
        """
         EmphasiseAssignedProduct 
        """
        pass
    def PreviewForImageCapture(self) -> None:
        """
         Preview selected Line ot Station before capturing am image of them
        """
        pass
    def ZoomToFitButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
class ConfigVariantConditionBuilder(NXOpen.Builder): 
    """ For creating and editing Product Configurator Variant Conditions """
    @property
    def ConfigVariantCondition(self) -> str:
        """
        Getter for property: (str) ConfigVariantCondition
         Returns the selected attribute to get or set config variant condition string   
            
         
        """
        pass
    @ConfigVariantCondition.setter
    def ConfigVariantCondition(self, configVariantCondition: str):
        """
        Setter for property: (str) ConfigVariantCondition
         Returns the selected attribute to get or set config variant condition string   
            
         
        """
        pass
import NXOpen
class CriticalResources(NXOpen.Object): 
    """ 
    Represents assembly line planner journaling methods for Critical Resources related functionalities   
     """
    def SetCritical(resources: List[NXOpen.NXObject], value: bool) -> None:
        """
          
                SetUnset input resources as critical based on input value
                 
        """
        pass
import NXOpen
class CycleTimeBuilder(NXOpen.Builder): 
    """ """
    @property
    def CycleTime(self) -> float:
        """
        Getter for property: (float) CycleTime
         Returns the cycle time   
            
         
        """
        pass
    @CycleTime.setter
    def CycleTime(self, cycleTime: float):
        """
        Setter for property: (float) CycleTime
         Returns the cycle time   
            
         
        """
        pass
    @property
    def OverwriteToggle(self) -> bool:
        """
        Getter for property: (bool) OverwriteToggle
         Returns the override toggle   
            
         
        """
        pass
    @OverwriteToggle.setter
    def OverwriteToggle(self, overwriteToggle: bool):
        """
        Setter for property: (bool) OverwriteToggle
         Returns the override toggle   
            
         
        """
        pass
import NXOpen
class FlowsManagerBuilder(NXOpen.Builder): 
    """ """
    class Type(Enum):
        """
        Members Include: 
         |NotSet| 
         |Flow| 
         |ScopeFlow| 
         |Any| 

        """
        NotSet: int
        Flow: int
        ScopeFlow: int
        Any: int
        @staticmethod
        def ValueOf(value: int) -> FlowsManagerBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SourceSelectObject(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SourceSelectObject
         Returns the source select object   
            
         
        """
        pass
    @property
    def TargetSelectObject(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) TargetSelectObject
         Returns the target select object   
            
         
        """
        pass
    def CreateFlow(self, input: NXOpen.TaggedObject, output: NXOpen.TaggedObject) -> bool:
        """
         TODO: fill in a description for this 
         Returns results (bool): .
        """
        pass
    def CreateFlowButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def DeleteFlow(self, input: NXOpen.TaggedObject, output: NXOpen.TaggedObject) -> bool:
        """
         TODO: fill in a description for this 
         Returns results (bool): .
        """
        pass
    def GetAllFlowableObjects(self) -> List[NXOpen.TaggedObject]:
        """
         TODO: fill in a description for this 
         Returns operations ( NXOpen.TaggedObject Li): .
        """
        pass
    def GetAllFlowsByType(self, type: FlowsManagerBuilder.Type) -> Tuple[List[NXOpen.TaggedObject], List[NXOpen.TaggedObject]]:
        """
         TODO: fill in a description for this 
         Returns A tuple consisting of (input, output). 
         - input is:  NXOpen.TaggedObject Li.
         - output is:  NXOpen.TaggedObject Li.

        """
        pass
    def GetIncomingFlowsByType(self, input: NXOpen.TaggedObject, type: FlowsManagerBuilder.Type) -> List[NXOpen.TaggedObject]:
        """
         TODO: fill in a description for this 
         Returns results ( NXOpen.TaggedObject Li): .
        """
        pass
    def GetOutgoingFlowsByType(self, input: NXOpen.TaggedObject, type: FlowsManagerBuilder.Type) -> List[NXOpen.TaggedObject]:
        """
         TODO: fill in a description for this 
         Returns results ( NXOpen.TaggedObject Li): .
        """
        pass
    def HasFlow(self, input: NXOpen.TaggedObject, output: NXOpen.TaggedObject) -> FlowsManagerBuilder.Type:
        """
         TODO: fill in a description for this 
         Returns results ( FlowsManagerBuilder.Type NXOp): .
        """
        pass
import NXOpen
class GlobalSelectionBuilder(NXOpen.Builder): 
    """ Global Selection """
    @property
    def Selection(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Selection
         Returns the selected objects   
            
         
        """
        pass
import NXOpen
class LibraryOperationBuilder(NXOpen.Builder): 
    """ A class for creating operationoperation group from library """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
import NXOpen
class LibraryOperation(NXOpen.Object): 
    """ 
    Represents assembly line planner journaling methods for Library Operation related functionalities   
     """
    def CreateRootModel() -> List[NXOpen.NXObject]:
        """
         
                Creates root node
                 
         Returns rootObjects ( NXOpen.NXObject Li):  LibraryOperation root objects .
        """
        pass
    def GetChildren(itemId: str, itemRevId: str) -> List[NXOpen.NXObject]:
        """
          
                Get Childrens
                 
         Returns childObjects ( NXOpen.NXObject Li): .
        """
        pass
import NXOpen
class MaterialFlowNode(NXOpen.NXObject): 
    """ Represents Material Flow information """
    pass
import NXOpen
class ModifyVariantBuilder(NXOpen.Builder): 
    """ For modifying Variant Rule """
    class VariantRules(Enum):
        """
        Members Include: 
         |VariantRuleName| 

        """
        VariantRuleName: int
        @staticmethod
        def ValueOf(value: int) -> ModifyVariantBuilder.VariantRules:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SelectedVariantRuleTag(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) SelectedVariantRuleTag
         Returns a property to get or set the selected variant rule   
            
         
        """
        pass
    @SelectedVariantRuleTag.setter
    def SelectedVariantRuleTag(self, variantRuleTag: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) SelectedVariantRuleTag
         Returns a property to get or set the selected variant rule   
            
         
        """
        pass
    @property
    def VariantRuleList(self) -> ModifyVariantBuilder.VariantRules:
        """
        Getter for property: ( ModifyVariantBuilder.VariantRules NXOp) VariantRuleList
         Returns the variant rule list   
            
         
        """
        pass
    @VariantRuleList.setter
    def VariantRuleList(self, variantRuleList: ModifyVariantBuilder.VariantRules):
        """
        Setter for property: ( ModifyVariantBuilder.VariantRules NXOp) VariantRuleList
         Returns the variant rule list   
            
         
        """
        pass
    def AddRule(self) -> None:
        """
         Add the rule 
        """
        pass
    def RemoveRule(self) -> None:
        """
         Remove the rule 
        """
        pass
import NXOpen
class OperationBuilder(NXOpen.Builder): 
    """ use for cearting operation """
    class Operation(Enum):
        """
        Members Include: 
         |Undefined| 
         |Operator| 
         |Tooling| 
         |Safety| 
         |Conveyance| 
         |MHRobot| 
         |GeoWeld| 
         |Respot| 
         |StudNutBolt| 
         |RivetFDS| 
         |Scribing| 
         |Vision| 
         |LaserSpotWeld| 
         |MigWeld| 
         |SealingAdhesive| 
         |LaserCut| 
         |Hemming| 
         |RobotHold| 

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
        @staticmethod
        def ValueOf(value: int) -> OperationBuilder.Operation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def OperationType(self) -> OperationBuilder.Operation:
        """
        Getter for property: ( OperationBuilder.Operation NXOp) OperationType
         Returns the operation type   
            
         
        """
        pass
    @OperationType.setter
    def OperationType(self, operationType: OperationBuilder.Operation):
        """
        Setter for property: ( OperationBuilder.Operation NXOp) OperationType
         Returns the operation type   
            
         
        """
        pass
    @property
    def OperationTypeName(self) -> str:
        """
        Getter for property: (str) OperationTypeName
         Returns the operation type name   
            
         
        """
        pass
    @OperationTypeName.setter
    def OperationTypeName(self, name: str):
        """
        Setter for property: (str) OperationTypeName
         Returns the operation type name   
            
         
        """
        pass
    @property
    def SelectFeatures(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectFeatures
         Returns the select features   
            
         
        """
        pass
    @property
    def SelectOperation(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectOperation
         Returns the select operation   
            
         
        """
        pass
    @property
    def SelectPart(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectPart
         Returns the select part   
            
         
        """
        pass
    @property
    def SelectResources(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectResources
         Returns the select resources   
            
         
        """
        pass
    @property
    def SelectStation(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectStation
         Returns the select station   
            
         
        """
        pass
    @property
    def Time(self) -> float:
        """
        Getter for property: (float) Time
         Returns the time   
            
         
        """
        pass
    @Time.setter
    def Time(self, time: float):
        """
        Setter for property: (float) Time
         Returns the time   
            
         
        """
        pass
import NXOpen
class OperationGroupBuilder(NXOpen.Builder): 
    """ A class for creating operation group in structure """
    @property
    def GroupName(self) -> str:
        """
        Getter for property: (str) GroupName
         Returns the group name   
            
         
        """
        pass
    @GroupName.setter
    def GroupName(self, groupName: str):
        """
        Setter for property: (str) GroupName
         Returns the group name   
            
         
        """
        pass
import NXOpen
class Pert(NXOpen.Object): 
    """ 
    Represents assembly line planner journaling methods for PERT related functionalities   
    PERT - Program evalution review technique used to understand material flow in manufacturing process planning
     """
    def ApplyLayout(partoccSheet: NXOpen.NXObject, sheetLayoutOption: AlpPertLayout) -> None:
        """
          
                Performs layouting of diagramming sheet nodes
                 
        """
        pass
    def CreateFlow(sourceStationPartOcc: NXOpen.NXObject, destStationPartOcc: NXOpen.NXObject) -> NXOpen.NXObject:
        """
         
                Creates the flow
                 
         Returns flowObject ( NXOpen.NXObject):  Connection flow object .
        """
        pass
    def DeleteFlow(flowsToDelete: List[NXOpen.NXObject], doNotUpdate: bool) -> None:
        """
          
                Deletes the flow
                 
        """
        pass
import NXOpen
class PositionProductBuilder(NXOpen.Builder): 
    """ use for cearting Position Product """
    @property
    def SelectedResource(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectedResource
         Returns the select resource   
            
         
        """
        pass
import NXOpen
class ProductVisibility(NXOpen.Object): 
    """ Represents colorhide assigned products functionalities methods """
    def GetColorAssignmentIndication() -> bool:
        """
         
                Get Color Assignment Indication
                 
         Returns indication (bool): .
        """
        pass
    def GetHideAssignmentIndication() -> bool:
        """
         
                Get Hide Assignment Indication
                 
         Returns indication (bool): .
        """
        pass
    def SetColorAssignmentIndication(indication: bool) -> None:
        """
         
                Set Color Assignment Indication
                 
        """
        pass
    def SetHideAssignmentIndication(indication: bool) -> None:
        """
         
                Set Hide Assignment Indication
                 
        """
        pass
    def UpdateProductsVisiblity(productPartOcc: List[NXOpen.NXObject]) -> None:
        """
         
                Update visiblity of targeted products
                 
        """
        pass
import NXOpen
class StationTaktTimeBuilder(NXOpen.Builder): 
    """ station takt time """
    class Radio(Enum):
        """
        Members Include: 
         |UseLineTaktTime| 
         |SetforLoadedStation| 

        """
        UseLineTaktTime: int
        SetforLoadedStation: int
        @staticmethod
        def ValueOf(value: int) -> StationTaktTimeBuilder.Radio:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def StationTaktTime(self) -> float:
        """
        Getter for property: (float) StationTaktTime
         Returns the station takt time   
            
         
        """
        pass
    @StationTaktTime.setter
    def StationTaktTime(self, stationTaktTime: float):
        """
        Setter for property: (float) StationTaktTime
         Returns the station takt time   
            
         
        """
        pass
    @property
    def TaktTimeEnum(self) -> StationTaktTimeBuilder.Radio:
        """
        Getter for property: ( StationTaktTimeBuilder.Radio NXOp) TaktTimeEnum
         Returns the takt time enum   
            
         
        """
        pass
    @TaktTimeEnum.setter
    def TaktTimeEnum(self, taktTimeEnum: StationTaktTimeBuilder.Radio):
        """
        Setter for property: ( StationTaktTimeBuilder.Radio NXOp) TaktTimeEnum
         Returns the takt time enum   
            
         
        """
        pass
import NXOpen
class SuggestPartBuilder(NXOpen.Builder): 
    """ use for suggesting parts to assign to station """
    @property
    def ColorForAssignParts(self) -> int:
        """
        Getter for property: (int) ColorForAssignParts
         Returns the assign part color   
            
         
        """
        pass
    @ColorForAssignParts.setter
    def ColorForAssignParts(self, color: int):
        """
        Setter for property: (int) ColorForAssignParts
         Returns the assign part color   
            
         
        """
        pass
    @property
    def ColorForIncomingParts(self) -> int:
        """
        Getter for property: (int) ColorForIncomingParts
         Returns the incoming part color   
            
         
        """
        pass
    @ColorForIncomingParts.setter
    def ColorForIncomingParts(self, color: int):
        """
        Setter for property: (int) ColorForIncomingParts
         Returns the incoming part color   
            
         
        """
        pass
    @property
    def ColorForSuggestedParts(self) -> int:
        """
        Getter for property: (int) ColorForSuggestedParts
         Returns the assign part color   
            
         
        """
        pass
    @ColorForSuggestedParts.setter
    def ColorForSuggestedParts(self, color: int):
        """
        Setter for property: (int) ColorForSuggestedParts
         Returns the assign part color   
            
         
        """
        pass
    @property
    def NextStation(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) NextStation
         Returns the next  station   
            
         
        """
        pass
    @property
    def PrevStation(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) PrevStation
         Returns the prev  station   
            
         
        """
        pass
    @property
    def SelectedStation(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectedStation
         Returns the selected station property   
            
         
        """
        pass
    @property
    def StationProcess(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) StationProcess
         Returns the selected station Process   
            
         
        """
        pass
    def CollectSuggestedParts(self) -> None:
        """
         To restore display state 
        """
        pass
    def GetSelectedParts(self) -> List[NXOpen.TaggedObject]:
        """
         The method to get the suggested parts
         Returns selectedParts ( NXOpen.TaggedObject Li): .
        """
        pass
    def RestoreDisplaystate(self) -> None:
        """
         To restore display state 
        """
        pass
    def SetSelectedParts(self, selectedParts: List[NXOpen.NXObject]) -> None:
        """
         The method to set the input parts for the commit function
        """
        pass
import NXOpen
class UINodeUtils(NXOpen.Object): 
    """ Represents a utils of assembly line planner for journaling uinode methods """
    def AddAdditionalResources(targetCompResList: List[NXOpen.NXObject]) -> None:
        """
         To add external resource 
        """
        pass
    def AssignMfgFeature(selectedFeature: List[NXOpen.NXObject], operationPartOcc: NXOpen.NXObject, totalWeldTime: float, allowMultipleAssignment: bool) -> None:
        """
         To assign features to operation 
        """
        pass
    def ClearSearchedFeatures(stationPartOccTag: NXOpen.NXObject) -> None:
        """
         To Clear Searched Features 
        """
        pass
    def CreateNewItem(temp_part_name: str, itemType: str, applicationName: str, partUnits: NXOpen.Part.Units, dbPartNo: str) -> NXOpen.NXObject:
        """
         To create new item
         Returns partTag ( NXOpen.NXObject): .
        """
        pass
    def CreateOperationFromLibrary(operationObjectTag: NXOpen.NXObject, clonnedGroupTag: NXOpen.NXObject, objectName: str) -> NXOpen.NXObject:
        """
         To create new item
         Returns childOperationTag ( NXOpen.NXObject): .
        """
        pass
    def CreateOperationGroupFromLibrary(operationObjectTag: NXOpen.NXObject, objectName: str) -> None:
        """
         To create new item
        """
        pass
    def GetItemRevisionName(partTag: NXOpen.Part) -> str:
        """
         To get item revision name 
         Returns itemRevName (str): .
        """
        pass
    def MoveUnAssignedFeaturesToNextStation(mfgPartOccTags: List[NXOpen.NXObject], currentStationPartOccTag: NXOpen.NXObject, nextStationName: str) -> None:
        """
         To Move remaining un assigned features to next station
        """
        pass
    def ProductAndStationAssignment(selectedProduct: List[NXOpen.NXObject], selectedStation: List[NXOpen.NXObject], objectToRefresh: List[NXOpen.NXObject]) -> None:
        """
         To assign product And station
        """
        pass
    def ProductAndStationUnassignment(selectedProduct: List[NXOpen.NXObject], unassignOption: int, label: str) -> None:
        """
         To unassign product And station
        """
        pass
    def RemoveAdditionalResources(resToBeRemoved: List[NXOpen.NXObject], removingChildOfPackage: bool) -> None:
        """
         To remove external resource 
        """
        pass
    def RotateComponent(partOccTags: List[NXOpen.NXObject], isClockwise: bool, rotateAsGroup: bool, angleStep: float) -> None:
        """
         To rotate a given component in clockwise or anticlockwise direction by 90 degrees 
        """
        pass
    def SetInContextEndItem(operationPartOcc: NXOpen.NXObject, setOption: bool) -> None:
        """
         To set or unset an assembly as special end item 
        """
        pass
    def ShowHideFeatures(isHidden: bool) -> None:
        """
         To showhide features
        """
        pass
    def UnAssignMfgFeature(selectedFeature: List[NXOpen.NXObject], operationName: str, selectedOpPartOcc: NXOpen.NXObject) -> None:
        """
         To unassign features from operation 
        """
        pass
    def UnAssignMfgFeatureFromAllOperations(selectedFeature: List[NXOpen.NXObject]) -> None:
        """
         To unassign features from all operations 
        """
        pass
    def UpdateOperationName(operationPartOcc: NXOpen.NXObject, newOperationName: str) -> None:
        """
         To Update the Operation Name 
        """
        pass
    def UpdateOperationTime(operationPartOcc: NXOpen.NXObject, newOperationTime: float) -> None:
        """
         To Update the Operation Time 
        """
        pass
import NXOpen
class ValidateToolBuilder(NXOpen.Builder): 
    """ use for creation of weld conistency checker builder """
    @property
    def SelectOperation(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectOperation
         Returns the selected operation property   
            
         
        """
        pass
    @property
    def SelectTool(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectTool
         Returns the selected tool property   
            
         
        """
        pass
    def AssignTool(self) -> None:
        """
         The method to assign the selected tool to the operation 
        """
        pass
    def CalculateToolClearence(self) -> None:
        """
         The method to calculate tool clearence from all features assigned to operation 
        """
        pass
    def MapToolInstanceFromReuseLibrary(self, itemId: str, revId: str) -> NXOpen.TaggedObject:
        """
         The method to load new tool instance from re-use library if needed 
         Returns newToolOcc ( NXOpen.TaggedObject): .
        """
        pass
    def SetIsFlipToolAllowed(self, flipToolAllowed: bool) -> None:
        """
         The method to set the flip tool allowed 
        """
        pass
    def SetReusePieChartBuilder(self, pieChartBuilder: NXOpen.TaggedObject) -> None:
        """
         Set pie chart builder 
        """
        pass
    def SetRotationStepSize(self, stepSize: float) -> None:
        """
         The method to set the rotation step size 
        """
        pass
    def SetSelectedWeld(self, selectedWeld: NXOpen.TaggedObject) -> None:
        """
         The method to set the selected welds for validation
        """
        pass
    def SwapWorkingTool(self, newToolOcc: NXOpen.TaggedObject) -> None:
        """
         The method to replace current tool with new tool 
        """
        pass
import NXOpen
class VariantConditionBuilder(NXOpen.Builder): 
    """ For creating and editing Variant Conditions """
    class Condition(Enum):
        """
        Members Include: 
         |And| 
         |Or| 

        """
        And: int
        Or: int
        @staticmethod
        def ValueOf(value: int) -> VariantConditionBuilder.Condition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LogicalAction(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: ( VariantConditionBuilder.Condition NXOp) LogicalAction
         Returns the logical action   
            
         
        """
        pass
    @LogicalAction.setter
    def LogicalAction(self, logicalAction: VariantConditionBuilder.Condition):
        """
        Setter for property: ( VariantConditionBuilder.Condition NXOp) LogicalAction
         Returns the logical action   
            
         
        """
        pass
    @property
    def OperationName(self) -> str:
        """
        Getter for property: (str) OperationName
         Returns the operation name   
            
         
        """
        pass
    @OperationName.setter
    def OperationName(self, operationName: str):
        """
        Setter for property: (str) OperationName
         Returns the operation name   
            
         
        """
        pass
    @property
    def OperatorType(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: ( VariantConditionBuilder.Condition NXOp) OperatorType
         Returns the operator type   
            
         
        """
        pass
    @OperatorType.setter
    def OperatorType(self, operatorType: VariantConditionBuilder.Condition):
        """
        Setter for property: ( VariantConditionBuilder.Condition NXOp) OperatorType
         Returns the operator type   
            
         
        """
        pass
    @property
    def OptionName(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: ( VariantConditionBuilder.Condition NXOp) OptionName
         Returns the option name   
            
         
        """
        pass
    @OptionName.setter
    def OptionName(self, optionName: VariantConditionBuilder.Condition):
        """
        Setter for property: ( VariantConditionBuilder.Condition NXOp) OptionName
         Returns the option name   
            
         
        """
        pass
    @property
    def OptionValue(self) -> VariantConditionBuilder.Condition:
        """
        Getter for property: ( VariantConditionBuilder.Condition NXOp) OptionValue
         Returns the option value   
            
         
        """
        pass
    @OptionValue.setter
    def OptionValue(self, optionValue: VariantConditionBuilder.Condition):
        """
        Setter for property: ( VariantConditionBuilder.Condition NXOp) OptionValue
         Returns the option value   
            
         
        """
        pass
    @property
    def SelectOperation(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectOperation
         Returns the select operation   
            
         
        """
        pass
    @property
    def VariantCondition(self) -> str:
        """
        Getter for property: (str) VariantCondition
         Returns a property to get or set the defined string of variant condition   
            
         
        """
        pass
    @VariantCondition.setter
    def VariantCondition(self, variantCondition: str):
        """
        Setter for property: (str) VariantCondition
         Returns a property to get or set the defined string of variant condition   
            
         
        """
        pass
    def AddLine(self) -> None:
        """
         Add a new line to the variant condition
        """
        pass
    def DeleteLine(self) -> None:
        """
         Delete an existing line from the variant condition 
        """
        pass
    def MoveDown(self) -> None:
        """
         Move an existing condition one line down in the set of variant condition 
        """
        pass
    def MoveUp(self) -> None:
        """
         Move an existing condition one line up in the set of variant condition 
        """
        pass
    def ReplaceLine(self) -> None:
        """
         Replace an existing line with a new condition 
        """
        pass
import NXOpen
class WebGantt(NXOpen.Object): 
    """ Represents a web gantt of line designer for journaling """
    def CreateLinkBetweenOperation(selectedOperation: List[str]) -> None:
        """
         To create links between operations
        """
        pass
    def DeleteLinksForMultipleOperation(selectedOperation: List[str]) -> None:
        """
        To delete links between multilpe operations
        """
        pass
    def DeleteLinksForSingleOperation(selectedOperation: List[str]) -> None:
        """
         To delete link between single operations
        """
        pass
    def DeleteOperation(selectedOperation: List[str]) -> None:
        """
        To delete operation
        """
        pass
    def DeleteOperationGroup(selectedOperationGroup: List[str], moveOperationToStation: bool) -> None:
        """
        To delete operation group
        """
        pass
    def DuplicateOperationsAndGroups(selectedOperations: List[NXOpen.NXObject], selectedOperationGroups: List[NXOpen.NXObject]) -> None:
        """
        To Duplicate selection operations and operation groups
        """
        pass
    def LoadNewStationRoot(ganttTitle: str) -> None:
        """
        To Load new staion while Gantt view is open
        """
        pass
    def MoveOperationToGroup(selectedOperation: List[NXOpen.NXObject], parentPartOccTag: NXOpen.NXObject) -> None:
        """
        To move operation to group
        """
        pass
    def RemoveOperationFromGroup(selectedOperation: List[str]) -> None:
        """
        To remove operation from group
        """
        pass
    def SetResetTransientFlag(selectedOpParents: List[NXOpen.NXObject], isSetTransient: bool) -> None:
        """
        To set reset transient
        """
        pass
    def SetUpdatedGanttData() -> None:
        """
         To set updated Gantt Data
        """
        pass
    def SetUpdatedGanttDataResetNameAndTime(operationType: str) -> None:
        """
         To set updated Gantt Data with reset flag
        """
        pass
import NXOpen
class WeldConsistencyCheckerBuilder(NXOpen.Builder): 
    """ use for creation of weld conistency checker builder """
    def UnAssignWeldPoints(self, selectedWeldPoints: List[NXOpen.NXObject]) -> None:
        """
         An API function which un-assign all the weld points in the list from operations conatined in the active station  
        """
        pass
