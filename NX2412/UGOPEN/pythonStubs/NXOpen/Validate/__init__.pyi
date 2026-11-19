from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AnalysisResultCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX NXOpen.Validate.AnalysisResultCollection object.
    """
    class AnalysisResultType(Enum):
        """
        Members Include: 
         |MaximumOverhangAngle|  Maximum Overhang Analysis Checker Result 
         |PrintTime|  Print Time Analysis Checker Result 
         |Overheating|  Overheating Analysis Checker Result 

        """
        MaximumOverhangAngle: int
        PrintTime: int
        Overheating: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisResultCollection.AnalysisResultType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateCheckChannelRatioBuilder(self, persistent_result: AnalysisResult) -> CheckChannelRatioBuilder:
        """
         Create a NXOpen.Validate.CheckChannelRatioBuilder 
         Returns channelRatioBuilder ( CheckChannelRatioBuilder NXOpen.):  check channel ratio builder .
        """
        pass
    def CreateCheckMaximumOverhangAngleBuilder(self, persistent_result: AnalysisResult) -> CheckMaximumOverhangAngleBuilder:
        """
         Create a NXOpen.Validate.CheckMaximumOverhangAngleBuilder 
         Returns overhang_builder ( CheckMaximumOverhangAngleBuilder NXOpen.):  check overhang angle builder .
        """
        pass
    def CreateCheckMinimumRadiusBuilder(self, persistent_result: AnalysisResult) -> CheckMinimumRadiusBuilder:
        """
         Create a NXOpen.Validate.CheckMinimumRadiusBuilder 
         Returns minimum_radius_builder ( CheckMinimumRadiusBuilder NXOpen.):  check minimum radius builder .
        """
        pass
    def CreateCheckMinimumWallThicknessBuilder(self, persistent_result: AnalysisResult) -> CheckMinimumWallThicknessBuilder:
        """
         Create a NXOpen.Validate.CheckMinimumWallThicknessBuilder 
         Returns wallthickness_builder ( CheckMinimumWallThicknessBuilder NXOpen.):  check minimum wall thickness builder .
        """
        pass
    def CreateCheckModelWithinPrintableVolumeBuilder(self, persistent_result: AnalysisResult) -> CheckModelWithinPrintableVolumeBuilder:
        """
         Create a NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder 
         Returns check_model_within_printable_volume_builder ( CheckModelWithinPrintableVolumeBuilder NXOpen.):  check model within printable volume builder .
        """
        pass
    def CreateCheckOverheatingBuilder(self, persistentResult: AnalysisResult) -> CheckOverheatingBuilder:
        """
         Creates an object of NXOpen.Validate.CheckOverheatingBuilder 
         Returns overheatingBuilder ( CheckOverheatingBuilder NXOpen.):  check overheating builder .
        """
        pass
    def CreateCheckPartOrientationBuilder(self, persistent_result: PartOrientationAnalysisResult) -> CheckPartOrientationBuilder:
        """
         Creates an object of NXOpen.Validate.CheckPartOrientationBuilder 
         Returns partorientation_builder ( CheckPartOrientationBuilder NXOpen.):  check part orientation builder .
        """
        pass
    def CreateCheckPorosityBuilder(self, persistent_result: AnalysisResult) -> CheckPorosityBuilder:
        """
         Create a NXOpen.Validate.CheckPorosityBuilder 
         Returns check_porosity_builder ( CheckPorosityBuilder NXOpen.):  check porosity builder .
        """
        pass
    def CreateCheckPrintTimeBuilder(self, persistentResult: AnalysisResult) -> CheckPrintTimeBuilder:
        """
         Creates an object of NXOpen.Validate.CheckPrintTimeBuilder 
         Returns partOrientationBuilder ( CheckPrintTimeBuilder NXOpen.):  check print time builder .
        """
        pass
    def CreateCheckTrappedSupportsBuilder(self, persistent_result: AnalysisResult) -> CheckTrappedSupportsBuilder:
        """
         Create a NXOpen.Validate.CheckTrappedSupportsBuilder 
         Returns trapped_supports_builder ( CheckTrappedSupportsBuilder NXOpen.):  check trapped supports builder .
        """
        pass
    def CreateCheckWhollyEnclosedVolumeBuilder(self, persistent_result: AnalysisResult) -> CheckWhollyEnclosedVolumeBuilder:
        """
         Create a NXOpen.Validate.CheckWhollyEnclosedVolumeBuilder 
         Returns check_wholly_enclosed_volume_builder ( CheckWhollyEnclosedVolumeBuilder NXOpen.):  check wholly enclosed volume builder .
        """
        pass
    def DeactivateAll(self, analysisResults: List[AnalysisResult]) -> None:
        """
         Hide all analysis result objects. 
        """
        pass
    def EvaluateAll(self, analysisResults: List[AnalysisResult]) -> None:
        """
         Update all analysis result objects. 
        """
        pass
    def FindAllAnalysisResults(self) -> List[AnalysisResult]:
        """
         Get all analysis result objects from the work part 
         Returns analysisResults ( AnalysisResult List[NXOpe):    .
        """
        pass
    def FindAllAnalysisResultsOfType(self, analysisType: AnalysisResultCollection.AnalysisResultType) -> List[AnalysisResult]:
        """
         Get all analysis result objects of desired type from the work part 
         Returns analysisResults ( AnalysisResult List[NXOpe):    .
        """
        pass
    def FindObject(self, sid: str) -> AnalysisResult:
        """
         Finds the NXOpen.Validate.AnalysisResult with the given identifier. 
         Returns analysisResults ( AnalysisResult NXOpen.):    .
        """
        pass
    def GetAnalysisResultValue(self, persistentResult: AnalysisResult) -> float:
        """
         Get the value of Analysis Checker Result. Returns 0 if value exist, else return -1 
         Returns analysisValue (float):  The analysis result value  .
        """
        pass
class AnalysisResult(PersistentResult): 
    """
     Represents a NXOpen.Validate.AnalysisResult object.
    """
    @property
    def ActiveStatus(self) -> bool:
        """
        Getter for property: (bool) ActiveStatus
         Returns the result's active status   
            
         
        """
        pass
    def Activate(self) -> None:
        """
         Activate the object. 
        """
        pass
    def Deactivate(self) -> None:
        """
         Deactivate the object. 
        """
        pass
    def Evaluate(self) -> None:
        """
         Evaluata the object. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckChannelRatioBuilder(NXOpen.Builder): 
    """ Represents a Check Channel Ratio Builder """
    class TableData:
        """
         CheckChannelRatioBuilderTableData_Struct NXOpen. is an alias for  CheckChannelRatioBuilder.TableData NXOpen..
        """
        @property
        def Angle(self) -> float:
            """
            Getter for property Angle
            angle value in table

            """
            pass
        @Angle.setter
        def Angle(self, value: float):
            """
            Getter for property Angle
            angle value in table
            Setter for property Angle
            angle value in table

            """
            pass
        @property
        def MinimumDiameter(self) -> float:
            """
            Getter for property MinimumDiameter
            minimum diameter value in table

            """
            pass
        @MinimumDiameter.setter
        def MinimumDiameter(self, value: float):
            """
            Getter for property MinimumDiameter
            minimum diameter value in table
            Setter for property MinimumDiameter
            minimum diameter value in table

            """
            pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolution
         Returns the display resolution   
            
         
        """
        pass
    @property
    def FailedSegmentsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FailedSegmentsColor
         Returns the color for segments with insufficient diameters.  
             
         
        """
        pass
    @FailedSegmentsColor.setter
    def FailedSegmentsColor(self, failedColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FailedSegmentsColor
         Returns the color for segments with insufficient diameters.  
             
         
        """
        pass
    @property
    def MaximumWidth(self) -> float:
        """
        Getter for property: (float) MaximumWidth
         Returns the maximum width of channel openings   
            
         
        """
        pass
    @MaximumWidth.setter
    def MaximumWidth(self, maximumWidth: float):
        """
        Setter for property: (float) MaximumWidth
         Returns the maximum width of channel openings   
            
         
        """
        pass
    @property
    def MinimumRatio(self) -> float:
        """
        Getter for property: (float) MinimumRatio
         Returns the minimum ratio    
            
         
        """
        pass
    @MinimumRatio.setter
    def MinimumRatio(self, minimumRatio: float):
        """
        Setter for property: (float) MinimumRatio
         Returns the minimum ratio    
            
         
        """
        pass
    @property
    def Orientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) Orientation
         Returns the draw orientation   
            
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) Orientation
         Returns the draw orientation   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the draw origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the draw origin   
            
         
        """
        pass
    @property
    def PassedSegmentsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) PassedSegmentsColor
         Returns the color for segments with sufficient diameters.  
             
         
        """
        pass
    @PassedSegmentsColor.setter
    def PassedSegmentsColor(self, passedColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) PassedSegmentsColor
         Returns the color for segments with sufficient diameters.  
             
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def SegmentLength(self) -> float:
        """
        Getter for property: (float) SegmentLength
         Returns the segment length    
            
         
        """
        pass
    @SegmentLength.setter
    def SegmentLength(self, segmentLength: float):
        """
        Setter for property: (float) SegmentLength
         Returns the segment length    
            
         
        """
        pass
    @property
    def ShowOnlyFailedSegments(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailedSegments
         Returns the toggle that show only failed segments   
            
         
        """
        pass
    @ShowOnlyFailedSegments.setter
    def ShowOnlyFailedSegments(self, showOnlyFailedSegments: bool):
        """
        Setter for property: (bool) ShowOnlyFailedSegments
         Returns the toggle that show only failed segments   
            
         
        """
        pass
    def GetBodies(self) -> List[NXOpen.Body]:
        """
         Returns the selected Bodies 
         Returns bodies ( NXOpen.Body Li):  .
        """
        pass
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Returns the selected faces 
         Returns faces ( NXOpen.Face Li):  .
        """
        pass
    def GetTableData(self) -> List[CheckChannelRatioBuilder.TableData]:
        """
         Gets angle and minimum diameter pair values. 
         Returns tableData ( CheckChannelRatioBuilder.TableData List[NXOpe):  TableData type values. .
        """
        pass
    def SetBodies(self, bodies: List[NXOpen.Body]) -> None:
        """
         Set the Bodies 
        """
        pass
    def SetFaces(self, faces: List[NXOpen.Face]) -> None:
        """
         Set the selected faces 
        """
        pass
    def SetNeedRegenerateFacets(self, needRegenerateFacets: bool) -> None:
        """
         Sets the needRegenerateFacets toggle 
        """
        pass
    def SetTableData(self, tableData: List[CheckChannelRatioBuilder.TableData]) -> None:
        """
         Sets angle and minimum diameter pair values. 
        """
        pass
import NXOpen
class CheckerDefinition(NXOpen.TransientObject): 
    """ Defines a Validate Checker.
     Checker definition contains the information of checker class name, checker parameter values 
     and call back functions and so on. These information is used to create checker instance for customization
     of parameters and execution of the check logic.
    """
    @property
    def InteractiveCheckingOnly(self) -> bool:
        """
        Getter for property: (bool) InteractiveCheckingOnly
         Returns the interactiveCheckingOnly status of the checker.  
          
                    Indicates whether or not to execute the checker only in the NX interactive mode.
                    When it is true, the checker will not be executed in the ug_check_part batch mode.
                  
         
        """
        pass
    @InteractiveCheckingOnly.setter
    def InteractiveCheckingOnly(self, interactiveCheckingOnly: bool):
        """
        Setter for property: (bool) InteractiveCheckingOnly
         Returns the interactiveCheckingOnly status of the checker.  
          
                    Indicates whether or not to execute the checker only in the NX interactive mode.
                    When it is true, the checker will not be executed in the ug_check_part batch mode.
                  
         
        """
        pass
    CustomizationHandler = Callable[[CheckerNode], None]
    def Dispose(self) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
    DocumentationHandler = Callable[[CheckerNode], None]
    def SetCustomizationHandler(self, customize: CheckerDefinition.CustomizationHandler) -> None:
        """
         Sets checker customization handler 
        """
        pass
    def SetDocumentationHandler(self, document: CheckerDefinition.DocumentationHandler) -> None:
        """
         Sets checker document handler 
        """
        pass
import NXOpen
class CheckerNode(NXOpen.TransientObject): 
    """ Represents a checker that validator will use to check against part node. 
     Checker node contains the information of checker class name and checker parameter attribute values. 
     If the checker class is a profile which contains child checker instances, you can set the enable flags to
     the child checker instances in the profile checker class to turn on or off the child checker instances.
    """
    @property
    def AttributeCustomizedFormulas(self) -> str:
        """
        Getter for property: (str) AttributeCustomizedFormulas
         Returns the customized formula lines of checker.  
          
                  For example:  
                  "Disabled?;False;save_log_in_part;True"  
                  For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help.  
                  
         
        """
        pass
    @AttributeCustomizedFormulas.setter
    def AttributeCustomizedFormulas(self, formulaLines: str):
        """
        Setter for property: (str) AttributeCustomizedFormulas
         Returns the customized formula lines of checker.  
          
                  For example:  
                  "Disabled?;False;save_log_in_part;True"  
                  For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help.  
                  
         
        """
        pass
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
         Returns the checker class name   
            
         
        """
        pass
    @ClassName.setter
    def ClassName(self, className: str):
        """
        Setter for property: (str) ClassName
         Returns the checker class name   
            
         
        """
        pass
    def AskLogger(self) -> Logger:
        """
         
                Asks the Validate.Logger instance designated to the Validate.CheckerNode.
                
                
                To obtain an instance of Validate.CheckerNode, refer to Validate.Validator.AppendCheckerNode.
                
                
         Returns logger ( Logger NXOpen.):  The logger to log result.
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetChildCheckerEnabledFlag(self, childCheckerInstance: str) -> bool:
        """
         Gets enable flag of child checker instance in a profile checker. 
         Returns enableFlag (bool):  The enable flag of child checker in the profile checker. .
        """
        pass
    def GetChildCheckerEnabledFlags(self) -> Tuple[List[bool], List[str]]:
        """
         Gets child checker instance names and enable flags in a profile checker. 
         Returns A tuple consisting of (enableFlags, childCheckerInstances). 
         - enableFlags is: List[bool]. The enable flags of child checkers in the profile checker .
         - childCheckerInstances is: List[str]. The instance names of child checkers in the profile checker .

        """
        pass
    def GetChildCheckerInstanceNames(self) -> List[str]:
        """
         Gets child checker instance names in a profile checker. 
         Returns childCheckerInstances (List[str]):  The instance names of child checkers in the profile checker .
        """
        pass
    def GetParameter(self, parameterTitle: str) -> Parameter:
        """
         Gets a Validate.Parameter of specified title.
                A parameter can be customized using methods like Validate.Parameter.SetBooleanValue,
                Validate.Parameter.SetIntValue, Validate.Parameter.SetDoubleValue,
                Validate.Parameter.SetStringValue, etc.
                
         Returns parameter ( Parameter NXOpen.): .
        """
        pass
    def GetParameters(self) -> List[Parameter]:
        """
         Gets all the Validate.Parameter. 
         Returns parameters ( Parameter List[NXOpe): .
        """
        pass
    def SetChildCheckerEnabledFlag(self, childCheckerInstance: str, enableFlag: bool) -> None:
        """
         Sets enable flag of child checker instance in a profile checker. 
        """
        pass
    def SetChildCheckerEnabledFlags(self, childCheckerInstances: List[str], enableFlags: List[bool]) -> None:
        """
         Sets child checker enable flags in a profile checker. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckMaximumOverhangAngleBuilder(NXOpen.Builder): 
    """ Represents a Check Maximum Overhang Angle builder """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the Maximum Angle    
            
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the Maximum Angle    
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolutionBuilder
         Returns the display resolution   
            
         
        """
        pass
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    @property
    def DrawOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    @property
    def ExceedExtendToleranceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ExceedExtendToleranceColor
         Returns the Exceed Extend Tol color   
            
         
        """
        pass
    @ExceedExtendToleranceColor.setter
    def ExceedExtendToleranceColor(self, exceedExtendTolColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ExceedExtendToleranceColor
         Returns the Exceed Extend Tol color   
            
         
        """
        pass
    @property
    def ExtendedAngularTolerance(self) -> float:
        """
        Getter for property: (float) ExtendedAngularTolerance
         Returns the Extended Angular Tol    
            
         
        """
        pass
    @ExtendedAngularTolerance.setter
    def ExtendedAngularTolerance(self, extendedAngularTol: float):
        """
        Setter for property: (float) ExtendedAngularTolerance
         Returns the Extended Angular Tol    
            
         
        """
        pass
    @property
    def LessThanMaxAngleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LessThanMaxAngleColor
         Returns the Less Than Max Angle Color   
            
         
        """
        pass
    @LessThanMaxAngleColor.setter
    def LessThanMaxAngleColor(self, nLessThanMaxAngleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LessThanMaxAngleColor
         Returns the Less Than Max Angle Color   
            
         
        """
        pass
    @property
    def MoreThanMaxAngleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) MoreThanMaxAngleColor
         Returns the More Than Max Angle Color   
            
         
        """
        pass
    @MoreThanMaxAngleColor.setter
    def MoreThanMaxAngleColor(self, moreThanMaxAngleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) MoreThanMaxAngleColor
         Returns the More Than Max Angle Color   
            
         
        """
        pass
    @property
    def OverhangArea(self) -> float:
        """
        Getter for property: (float) OverhangArea
         Returns the area that need to support   
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the toggle that preview block   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the toggle that preview block   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ShowOnlyExceedingOverhangAngles(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyExceedingOverhangAngles
         Returns the property will be deprecated.  
           use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead.   
         
        """
        pass
    @ShowOnlyExceedingOverhangAngles.setter
    def ShowOnlyExceedingOverhangAngles(self, showOnlyExceed: bool):
        """
        Setter for property: (bool) ShowOnlyExceedingOverhangAngles
         Returns the property will be deprecated.  
           use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead.   
         
        """
        pass
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
         Returns the toggle that show only Exceeding Overhang Angles   
            
         
        """
        pass
    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
         Returns the toggle that show only Exceeding Overhang Angles   
            
         
        """
        pass
    def GetTargets(self) -> List[NXOpen.Body]:
        """
         Returns the selected Bodies or Parts
         Returns targets ( NXOpen.Body Li):  .
        """
        pass
    def SetTargets(self, targets: List[NXOpen.Body]) -> None:
        """
         Set the Bodies or Parts 
        """
        pass
    def Update(self) -> None:
        """
         Update the checker 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckMinimumRadiusBuilder(NXOpen.Builder): 
    """ Represents a Check Minimum Radius builder """
    class CurvatureTypes(Enum):
        """
        Members Include: 
         |Radius|  3D Minimum 
         |Sectional| 

        """
        Radius: int
        Sectional: int
        @staticmethod
        def ValueOf(value: int) -> CheckMinimumRadiusBuilder.CurvatureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def CurvatureType(self) -> CheckMinimumRadiusBuilder.CurvatureTypes:
        """
        Getter for property: ( CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.) CurvatureType
         Returns the curvature type to compute and display.  
            
         
        """
        pass
    @CurvatureType.setter
    def CurvatureType(self, curvatureType: CheckMinimumRadiusBuilder.CurvatureTypes):
        """
        Setter for property: ( CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.) CurvatureType
         Returns the curvature type to compute and display.  
            
         
        """
        pass
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolutionBuilder
         Returns the display resolution   
            
         
        """
        pass
    @property
    def ExcludeConvex(self) -> bool:
        """
        Getter for property: (bool) ExcludeConvex
         Returns the Exclude Convex    
            
         
        """
        pass
    @ExcludeConvex.setter
    def ExcludeConvex(self, excludeConvex: bool):
        """
        Setter for property: (bool) ExcludeConvex
         Returns the Exclude Convex    
            
         
        """
        pass
    @property
    def FailureArea(self) -> float:
        """
        Getter for property: (float) FailureArea
         Returns the area where radius is less than the minimum radius   
            
         
        """
        pass
    @property
    def LessThanMinimumRadiusColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LessThanMinimumRadiusColor
         Returns the Less Than Minimum Radius Color  
            
         
        """
        pass
    @LessThanMinimumRadiusColor.setter
    def LessThanMinimumRadiusColor(self, lessThanMinimumRadiusColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LessThanMinimumRadiusColor
         Returns the Less Than Minimum Radius Color  
            
         
        """
        pass
    @property
    def MinimumRadius(self) -> float:
        """
        Getter for property: (float) MinimumRadius
         Returns the Minimum Radius   
            
         
        """
        pass
    @MinimumRadius.setter
    def MinimumRadius(self, minimumRadius: float):
        """
        Setter for property: (float) MinimumRadius
         Returns the Minimum Radius   
            
         
        """
        pass
    @property
    def MoreThanMinimumRadiusColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) MoreThanMinimumRadiusColor
         Returns the More Than Minimum Radius Color  
            
         
        """
        pass
    @MoreThanMinimumRadiusColor.setter
    def MoreThanMinimumRadiusColor(self, moreThanMinimumRadiusColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) MoreThanMinimumRadiusColor
         Returns the More Than Minimum Radius Color  
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
         Returns the show only less than minimum radius toggle   
            
         
        """
        pass
    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
         Returns the show only less than minimum radius toggle   
            
         
        """
        pass
    def GetDynamicResult(self, selectedFace: NXOpen.Face, dynamicPnt: NXOpen.Point3d) -> float:
        """
         Returns the dynamic result 
         Returns minimumRadius (float):  The minimum radius evaluated .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckMinimumWallThicknessBuilder(NXOpen.Builder): 
    """ Represents a Check Minimum Wall Thickness builder """
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolutionBuilder
         Returns the display resolution   
            
         
        """
        pass
    @property
    def FailureArea(self) -> float:
        """
        Getter for property: (float) FailureArea
         Returns the area where wall thickness is less than the minimum wall thickness   
            
         
        """
        pass
    @property
    def LessThanMinThicknessColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LessThanMinThicknessColor
         Returns the Less Than Min Thickness Color   
            
         
        """
        pass
    @LessThanMinThicknessColor.setter
    def LessThanMinThicknessColor(self, lessThanMinThicknessColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LessThanMinThicknessColor
         Returns the Less Than Min Thickness Color   
            
         
        """
        pass
    @property
    def MoreThanMinThicknessColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) MoreThanMinThicknessColor
         Returns the More Than Min Thickness Color   
            
         
        """
        pass
    @MoreThanMinThicknessColor.setter
    def MoreThanMinThicknessColor(self, moreThanMinThicknessColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) MoreThanMinThicknessColor
         Returns the More Than Min Thickness Color   
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
         Returns the show only less than min thickness toggle   
            
         
        """
        pass
    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
         Returns the show only less than min thickness toggle   
            
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the minimum thickness    
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the minimum thickness    
            
         
        """
        pass
    def GetDynamicResult(self, selectedFace: NXOpen.Face, dynamicPnt: NXOpen.Point3d) -> Tuple[bool, float, NXOpen.Vector3d, NXOpen.Point3d]:
        """
         Returns the dynamic result 
         Returns A tuple consisting of (valid, thickness, direction, closestPnt). 
         - valid is: bool. The thickness is valid or not .
         - thickness is: float. The thickness evaluated .
         - direction is:  NXOpen.Vector3d. The normal of closest element .
         - closestPnt is:  NXOpen.Point3d. The closest point on the specified face .

        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckModelWithinPrintableVolumeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder """
    class PrinterShapeTypes(Enum):
        """
        Members Include: 
         |Block|  printer volume shape is block 
         |Cylinder| 

        """
        Block: int
        Cylinder: int
        @staticmethod
        def ValueOf(value: int) -> CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShowTypes(Enum):
        """
        Members Include: 
         |Printer|  show type is printer 
         |Product| 
         |Both| 

        """
        Printer: int
        Product: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> CheckModelWithinPrintableVolumeBuilder.ShowTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def CloseToPrintableVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CloseToPrintableVolumeColor
         Returns the Close to Printable Volume Color   
            
         
        """
        pass
    @CloseToPrintableVolumeColor.setter
    def CloseToPrintableVolumeColor(self, closetoPrintableVolumeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CloseToPrintableVolumeColor
         Returns the Close to Printable Volume Color   
            
         
        """
        pass
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolutionBuilder
         Returns the display resolution   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used to check the product bounding box and the printer bounding box   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used to check the product bounding box and the printer bounding box   
            
         
        """
        pass
    @property
    def OutOfPrintableVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OutOfPrintableVolumeColor
         Returns the Out Of Printable Volume Color   
            
         
        """
        pass
    @OutOfPrintableVolumeColor.setter
    def OutOfPrintableVolumeColor(self, outOfPrintableVolumeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OutOfPrintableVolumeColor
         Returns the Out Of Printable Volume Color   
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def PrinterDiameter(self) -> float:
        """
        Getter for property: (float) PrinterDiameter
         Returns the printer diameter   
            
         
        """
        pass
    @PrinterDiameter.setter
    def PrinterDiameter(self, printerDiameter: float):
        """
        Setter for property: (float) PrinterDiameter
         Returns the printer diameter   
            
         
        """
        pass
    @property
    def PrinterHeight(self) -> float:
        """
        Getter for property: (float) PrinterHeight
         Returns the printer height   
            
         
        """
        pass
    @PrinterHeight.setter
    def PrinterHeight(self, printerHeight: float):
        """
        Setter for property: (float) PrinterHeight
         Returns the printer height   
            
         
        """
        pass
    @property
    def PrinterLength(self) -> float:
        """
        Getter for property: (float) PrinterLength
         Returns the printer length   
            
         
        """
        pass
    @PrinterLength.setter
    def PrinterLength(self, printerLength: float):
        """
        Setter for property: (float) PrinterLength
         Returns the printer length   
            
         
        """
        pass
    @property
    def PrinterName(self) -> str:
        """
        Getter for property: (str) PrinterName
         Returns the printer name   
            
         
        """
        pass
    @PrinterName.setter
    def PrinterName(self, printerName: str):
        """
        Setter for property: (str) PrinterName
         Returns the printer name   
            
         
        """
        pass
    @property
    def PrinterOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) PrinterOrientation
         Returns the printer orientation   
            
         
        """
        pass
    @PrinterOrientation.setter
    def PrinterOrientation(self, printerOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) PrinterOrientation
         Returns the printer orientation   
            
         
        """
        pass
    @property
    def PrinterOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PrinterOrigin
         Returns the printer origin   
            
         
        """
        pass
    @PrinterOrigin.setter
    def PrinterOrigin(self, printerOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PrinterOrigin
         Returns the printer origin   
            
         
        """
        pass
    @property
    def PrinterShapeType(self) -> CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes:
        """
        Getter for property: ( CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.) PrinterShapeType
         Returns the shape type   
            
         
        """
        pass
    @PrinterShapeType.setter
    def PrinterShapeType(self, printerShapeType: CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes):
        """
        Setter for property: ( CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.) PrinterShapeType
         Returns the shape type   
            
         
        """
        pass
    @property
    def PrinterWidth(self) -> float:
        """
        Getter for property: (float) PrinterWidth
         Returns the printer width   
            
         
        """
        pass
    @PrinterWidth.setter
    def PrinterWidth(self, printerWidth: float):
        """
        Setter for property: (float) PrinterWidth
         Returns the printer width   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ShowType(self) -> CheckModelWithinPrintableVolumeBuilder.ShowTypes:
        """
        Getter for property: ( CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.) ShowType
         Returns the show type   
            
         
        """
        pass
    @ShowType.setter
    def ShowType(self, showType: CheckModelWithinPrintableVolumeBuilder.ShowTypes):
        """
        Setter for property: ( CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.) ShowType
         Returns the show type   
            
         
        """
        pass
    @property
    def WithinPrintableVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WithinPrintableVolumeColor
         Returns the Within Printable Volume Color   
            
         
        """
        pass
    @WithinPrintableVolumeColor.setter
    def WithinPrintableVolumeColor(self, withinPrintableVolumeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WithinPrintableVolumeColor
         Returns the Within Printable Volume Color   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckOverheatingBuilder(NXOpen.Builder): 
    """ Represents a Check Overheating builder """
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolution
         Returns the display resolution   
            
         
        """
        pass
    @property
    def MaximumOverhangAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumOverhangAngle
         Returns the Maximum Overhang Angle    
            
         
        """
        pass
    @property
    def NonOverheatingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonOverheatingColor
         Returns the Less Than Max Overhang Angle Color   
            
         
        """
        pass
    @NonOverheatingColor.setter
    def NonOverheatingColor(self, nonOverHeatingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonOverheatingColor
         Returns the Less Than Max Overhang Angle Color   
            
         
        """
        pass
    @property
    def OverheatingArea(self) -> float:
        """
        Getter for property: (float) OverheatingArea
         Returns the area that will overheat   
            
         
        """
        pass
    @property
    def OverheatingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OverheatingColor
         Returns the More than Max Overhang Angle   
            
         
        """
        pass
    @OverheatingColor.setter
    def OverheatingColor(self, overheatingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OverheatingColor
         Returns the More than Max Overhang Angle   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ShowOnlyOverheatingAreas(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyOverheatingAreas
         Returns the toggle that show only Overheating Areas   
            
         
        """
        pass
    @ShowOnlyOverheatingAreas.setter
    def ShowOnlyOverheatingAreas(self, showOnlyOverheat: bool):
        """
        Setter for property: (bool) ShowOnlyOverheatingAreas
         Returns the toggle that show only Overheating Areas   
            
         
        """
        pass
    def Update(self) -> None:
        """
         Update the checker 
        """
        pass
import NXOpen
class CheckPartOrientationBuilder(NXOpen.Builder): 
    """ Represents a Validate.PartOrientationAnalysisResult builder """
    class AccuracyLevel(Enum):
        """
        Members Include: 
         |Coarse|  Represents coarse accuracy. This would be computationaly faster. 
         |Low|  Represents low accuracy. This would be computationaly fast 
         |Medium|  Represents medium accuracy. This would be resonably computationaly expensive  
         |High|  Represents high accuracy. This would be computationaly expensive 
         |VeryHigh|  Represents very high accuracy. This would be computationaly very expensive 

        """
        Coarse: int
        Low: int
        Medium: int
        High: int
        VeryHigh: int
        @staticmethod
        def ValueOf(value: int) -> CheckPartOrientationBuilder.AccuracyLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Accuracy(self) -> CheckPartOrientationBuilder.AccuracyLevel:
        """
        Getter for property: ( CheckPartOrientationBuilder.AccuracyLevel NXOpen.) Accuracy
         Returns the accuracy for optimization.  
           Higher accuracy will take long computation time.  
         
        """
        pass
    @Accuracy.setter
    def Accuracy(self, accuracy: CheckPartOrientationBuilder.AccuracyLevel):
        """
        Setter for property: ( CheckPartOrientationBuilder.AccuracyLevel NXOpen.) Accuracy
         Returns the accuracy for optimization.  
           Higher accuracy will take long computation time.  
         
        """
        pass
    @property
    def FDMPrintTimeParameter(self) -> FDMPrintTimeParameter:
        """
        Getter for property: ( FDMPrintTimeParameter NXOpen.) FDMPrintTimeParameter
         Returns the print time parameter for fused deposition modelling printer type   
            
         
        """
        pass
    @property
    def MJFPrintTimeParameter(self) -> MJFPrintTimeParameter:
        """
        Getter for property: ( MJFPrintTimeParameter NXOpen.) MJFPrintTimeParameter
         Returns the print time parameter for multi jet fusion printer type   
            
         
        """
        pass
    @property
    def MaxOverhangAngleForOverHeating(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxOverhangAngleForOverHeating
         Returns the maximum overhang angle for overheating step   
            
         
        """
        pass
    @property
    def MaxOverhangAngleForVolume(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxOverhangAngleForVolume
         Returns the maximum overhang angle for support volume parameter   
            
         
        """
        pass
    @property
    def PBFPrintTimeParameter(self) -> PBFPrintTimeParameter:
        """
        Getter for property: ( PBFPrintTimeParameter NXOpen.) PBFPrintTimeParameter
         Returns the print time parameter for powder bed fusion printer type   
            
         
        """
        pass
    @property
    def Printer(self) -> CheckPrintTimeBuilder.PrinterType:
        """
        Getter for property: ( CheckPrintTimeBuilder.PrinterType NXOpen.) Printer
         Returns the printer type   
            
         
        """
        pass
    @Printer.setter
    def Printer(self, printer: CheckPrintTimeBuilder.PrinterType):
        """
        Setter for property: ( CheckPrintTimeBuilder.PrinterType NXOpen.) Printer
         Returns the printer type   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ValidateOverheating(self) -> bool:
        """
        Getter for property: (bool) ValidateOverheating
         Returns the overheating checker flag.  
           If switched ON overheating area would be optimized.  
         
        """
        pass
    @ValidateOverheating.setter
    def ValidateOverheating(self, overheating: bool):
        """
        Setter for property: (bool) ValidateOverheating
         Returns the overheating checker flag.  
           If switched ON overheating area would be optimized.  
         
        """
        pass
    @property
    def ValidatePrintTime(self) -> bool:
        """
        Getter for property: (bool) ValidatePrintTime
         Returns the print time checker flag.  
           If switched ON print time would be optimized.  
         
        """
        pass
    @ValidatePrintTime.setter
    def ValidatePrintTime(self, printTime: bool):
        """
        Setter for property: (bool) ValidatePrintTime
         Returns the print time checker flag.  
           If switched ON print time would be optimized.  
         
        """
        pass
    @property
    def ValidateSupportVolume(self) -> bool:
        """
        Getter for property: (bool) ValidateSupportVolume
         Returns the support volume checker flag.  
           If switched ON support volume would be optimized.  
         
        """
        pass
    @ValidateSupportVolume.setter
    def ValidateSupportVolume(self, supportVolume: bool):
        """
        Setter for property: (bool) ValidateSupportVolume
         Returns the support volume checker flag.  
           If switched ON support volume would be optimized.  
         
        """
        pass
    @property
    def ValidateSurfaceArea(self) -> bool:
        """
        Getter for property: (bool) ValidateSurfaceArea
         Returns the surface area checker flag.  
           If switched ON surface area would be optimized.  
         
        """
        pass
    @ValidateSurfaceArea.setter
    def ValidateSurfaceArea(self, surfaceArea: bool):
        """
        Setter for property: (bool) ValidateSurfaceArea
         Returns the surface area checker flag.  
           If switched ON surface area would be optimized.  
         
        """
        pass
    @property
    def WeightOverheating(self) -> int:
        """
        Getter for property: (int) WeightOverheating
         Returns the weight for overheating   
            
         
        """
        pass
    @WeightOverheating.setter
    def WeightOverheating(self, weightOverheating: int):
        """
        Setter for property: (int) WeightOverheating
         Returns the weight for overheating   
            
         
        """
        pass
    @property
    def WeightPrintTime(self) -> int:
        """
        Getter for property: (int) WeightPrintTime
         Returns the weight for print time   
            
         
        """
        pass
    @WeightPrintTime.setter
    def WeightPrintTime(self, weightPrintTime: int):
        """
        Setter for property: (int) WeightPrintTime
         Returns the weight for print time   
            
         
        """
        pass
    @property
    def WeightSupportVolume(self) -> int:
        """
        Getter for property: (int) WeightSupportVolume
         Returns the weight for support volume   
            
         
        """
        pass
    @WeightSupportVolume.setter
    def WeightSupportVolume(self, weightSupportVolume: int):
        """
        Setter for property: (int) WeightSupportVolume
         Returns the weight for support volume   
            
         
        """
        pass
    @property
    def WeightSurfaceArea(self) -> int:
        """
        Getter for property: (int) WeightSurfaceArea
         Returns the weight for surface area   
            
         
        """
        pass
    @WeightSurfaceArea.setter
    def WeightSurfaceArea(self, weightSurfaceArea: int):
        """
        Setter for property: (int) WeightSurfaceArea
         Returns the weight for surface area   
            
         
        """
        pass
    def CalculateCheck(self) -> List[PartOrientationAnalysisResult.CheckerValues]:
        """
         Calculate the checker at current orientation
         Returns checker_values ( PartOrientationAnalysisResult.CheckerValues List[NXOpe):  The values of checker and its range .
        """
        pass
    def GetMinimumOrientation(self, checker_index: PartOrientationAnalysisResult.CheckerIndex) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get minimum orientation for specific checker 
         Returns A tuple consisting of (origin, orientation, checker_values). 
         - origin is:  NXOpen.Point3d. Origin for the optimum orientation .
         - orientation is:  NXOpen.Vector3d. Z direction of the optimum orientation .
         - checker_values is:  PartOrientationAnalysisResult.CheckerValues List[NXOpe. The values of checker and its range .

        """
        pass
    def GetNumOfOptimumOrientations(self) -> int:
        """
         Get number of optimum orientations
         Returns numOfOptimumOrientations (int): .
        """
        pass
    def GetOptimumOrientation(self, optimum_orientation_index: int) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get the optimum orientation at given index
         Returns A tuple consisting of (origin, orientation, checker_values). 
         - origin is:  NXOpen.Point3d. Origin for the optimum orientation .
         - orientation is:  NXOpen.Vector3d. Z direction of the optimum orientation .
         - checker_values is:  PartOrientationAnalysisResult.CheckerValues List[NXOpe. The values of checker and its range. .

        """
        pass
    def GetPartOrientationResult(self) -> PartOrientationAnalysisResult:
        """
         Get the persistent part orientation optimization result.
         Returns persistent_result ( PartOrientationAnalysisResult NXOpen.): .
        """
        pass
    def OptimumSolution(self, orientationIndex: int) -> None:
        """
         Orient the build plane or part to the optimum orientation specified by index
        """
        pass
    def OrientToMinimum(self, checkerIndex: PartOrientationAnalysisResult.CheckerIndex) -> None:
        """
         Orient the build plane or part to the minimum for specified checker
        """
        pass
    def RemoveAllSolutions(self) -> None:
        """
         Remove all orientations.
        """
        pass
    def StartCalculation(self) -> None:
        """
         The api to start the optimization process 
        """
        pass
import NXOpen
class CheckPorosityBuilder(NXOpen.Builder): 
    """ Represents a Check Porosity Builder """
    class ColorMapDisplayOptionTypes(Enum):
        """
        Members Include: 
         |All|  Display All 
         |WithinLimits| 
         |OutsideLimits| 
         |AboveTarget| 
         |BelowTarget| 

        """
        All: int
        WithinLimits: int
        OutsideLimits: int
        AboveTarget: int
        BelowTarget: int
        @staticmethod
        def ValueOf(value: int) -> CheckPorosityBuilder.ColorMapDisplayOptionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AboveLimit(self) -> float:
        """
        Getter for property: (float) AboveLimit
         Returns the aboveLimit in volume results group   
            
         
        """
        pass
    @property
    def AboveTarget(self) -> float:
        """
        Getter for property: (float) AboveTarget
         Returns the aboveTarget in volume results group   
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def Average(self) -> float:
        """
        Getter for property: (float) Average
         Returns the average in porosity results group   
            
         
        """
        pass
    @property
    def BelowLimit(self) -> float:
        """
        Getter for property: (float) BelowLimit
         Returns the belowLimit in volume results group   
            
         
        """
        pass
    @property
    def BelowTarget(self) -> float:
        """
        Getter for property: (float) BelowTarget
         Returns the belowTarget in volume results group   
            
         
        """
        pass
    @property
    def ColorMapDisplayOptionType(self) -> CheckPorosityBuilder.ColorMapDisplayOptionTypes:
        """
        Getter for property: ( CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.) ColorMapDisplayOptionType
         Returns the color map display option types   
            
         
        """
        pass
    @ColorMapDisplayOptionType.setter
    def ColorMapDisplayOptionType(self, colorMapDisplayOptionType: CheckPorosityBuilder.ColorMapDisplayOptionTypes):
        """
        Setter for property: ( CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.) ColorMapDisplayOptionType
         Returns the color map display option types   
            
         
        """
        pass
    @property
    def GeometricConstraintDataManager(self) -> GeometricConstraintDataManager:
        """
        Getter for property: ( GeometricConstraintDataManager NXOpen.) GeometricConstraintDataManager
         Returns the Geometric Constraint Data Manager builder  
            
         
        """
        pass
    @property
    def Maximum(self) -> float:
        """
        Getter for property: (float) Maximum
         Returns the maximum in porosity results group   
            
         
        """
        pass
    @property
    def MaximumPorosity(self) -> float:
        """
        Getter for property: (float) MaximumPorosity
         Returns the Maximum Porosity    
            
         
        """
        pass
    @MaximumPorosity.setter
    def MaximumPorosity(self, maximumPorosity: float):
        """
        Setter for property: (float) MaximumPorosity
         Returns the Maximum Porosity    
            
         
        """
        pass
    @property
    def Median(self) -> float:
        """
        Getter for property: (float) Median
         Returns the median in porosity results group   
            
         
        """
        pass
    @property
    def Minimum(self) -> float:
        """
        Getter for property: (float) Minimum
         Returns the minimum in porosity results group   
            
         
        """
        pass
    @property
    def MinimumPorosity(self) -> float:
        """
        Getter for property: (float) MinimumPorosity
         Returns the Minimum Porosity    
            
         
        """
        pass
    @MinimumPorosity.setter
    def MinimumPorosity(self, minimumPorosity: float):
        """
        Setter for property: (float) MinimumPorosity
         Returns the Minimum Porosity    
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def TargetPorosity(self) -> float:
        """
        Getter for property: (float) TargetPorosity
         Returns the Target Porosity    
            
         
        """
        pass
    @TargetPorosity.setter
    def TargetPorosity(self, targetPorosity: float):
        """
        Setter for property: (float) TargetPorosity
         Returns the Target Porosity    
            
         
        """
        pass
    @property
    def VoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VoxelSize
         Returns the expression representing the voxel size   
            
         
        """
        pass
    @property
    def WithinLimit(self) -> float:
        """
        Getter for property: (float) WithinLimit
         Returns the withinLimit in volume results group   
            
         
        """
        pass
    def AddGeometricConstraintPoint(self, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Adds geometric constraint point 
        """
        pass
    def ClearGeometricConstraintPoints(self) -> None:
        """
         Clears geometric constraint points 
        """
        pass
    def DeleteGeometricConstraintPoint(self, point: NXOpen.Point) -> None:
        """
         Deletes geometric constraint point 
        """
        pass
    def MakeColorLegend(self) -> None:
        """
         Creates color legend 
        """
        pass
    def RemoveColorLegend(self) -> None:
        """
         Removes color legend 
        """
        pass
    def SetGeometricConstraintPoint(self, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Sets geometric constraint point 
        """
        pass
import NXOpen
class CheckPrintTimeBuilder(NXOpen.Builder): 
    """ Represents a Check Print Time builder """
    class PrinterType(Enum):
        """
        Members Include: 
         |PowderBedFusion|  Powder Bed Fusion(PBF) 
         |MultiJetFusion|  Multi Jet Fusion(MJF) 
         |FusedDepositionModeling|  Fusion Deposition Modeling(FDM) 

        """
        PowderBedFusion: int
        MultiJetFusion: int
        FusedDepositionModeling: int
        @staticmethod
        def ValueOf(value: int) -> CheckPrintTimeBuilder.PrinterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the boolean flag for automatic update   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the boolean flag for automatic update   
            
         
        """
        pass
    @property
    def FDMPrintTimeParameter(self) -> FDMPrintTimeParameter:
        """
        Getter for property: ( FDMPrintTimeParameter NXOpen.) FDMPrintTimeParameter
         Returns the Fusion Deposition Modeling(FDM) printer parameters   
            
         
        """
        pass
    @property
    def MJFPrintTimeParameter(self) -> MJFPrintTimeParameter:
        """
        Getter for property: ( MJFPrintTimeParameter NXOpen.) MJFPrintTimeParameter
         Returns the Multi Jet Fusion(MJF) printer parameters   
            
         
        """
        pass
    @property
    def PBFPrintTimeParameter(self) -> PBFPrintTimeParameter:
        """
        Getter for property: ( PBFPrintTimeParameter NXOpen.) PBFPrintTimeParameter
         Returns the Powder Bed Fusion(PBF) printer parameters   
            
         
        """
        pass
    @property
    def PrintTime(self) -> float:
        """
        Getter for property: (float) PrintTime
         Returns the estimated time to print the part   
            
         
        """
        pass
    @property
    def Printer(self) -> CheckPrintTimeBuilder.PrinterType:
        """
        Getter for property: ( CheckPrintTimeBuilder.PrinterType NXOpen.) Printer
         Returns the printer type option as  NXOpen::Validate::CheckPrintTimeBuilder::PrinterType   
            
         
        """
        pass
    @Printer.setter
    def Printer(self, printerType: CheckPrintTimeBuilder.PrinterType):
        """
        Setter for property: ( CheckPrintTimeBuilder.PrinterType NXOpen.) Printer
         Returns the printer type option as  NXOpen::Validate::CheckPrintTimeBuilder::PrinterType   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    def Update(self) -> None:
        """
         Update the checker 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckTrappedSupportsBuilder(NXOpen.Builder): 
    """ Represents a Check Trapped Supports Builder """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the Maximum Overhang Angle   
            
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the Maximum Overhang Angle   
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolutionBuilder
         Returns the display resolution   
            
         
        """
        pass
    @property
    def NonTrappedSupportAreasColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonTrappedSupportAreasColor
         Returns the non-Trapped Supports Areas Color   
            
         
        """
        pass
    @NonTrappedSupportAreasColor.setter
    def NonTrappedSupportAreasColor(self, nonTrappedSupportAreasColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonTrappedSupportAreasColor
         Returns the non-Trapped Supports Areas Color   
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
         Returns the show only trapped aupport areas   
            
         
        """
        pass
    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
         Returns the show only trapped aupport areas   
            
         
        """
        pass
    @property
    def TrappedArea(self) -> float:
        """
        Getter for property: (float) TrappedArea
         Returns the trapped area   
            
         
        """
        pass
    @property
    def TrappedSupportAreasColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TrappedSupportAreasColor
         Returns the Trapped Supports Areas Color   
            
         
        """
        pass
    @TrappedSupportAreasColor.setter
    def TrappedSupportAreasColor(self, trappedSupportAreasColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TrappedSupportAreasColor
         Returns the Trapped Supports Areas Color   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CheckWhollyEnclosedVolumeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Validate.CheckWhollyEnclosedVolumeBuilder """
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle   
            
         
        """
        pass
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolutionBuilder
         Returns the display resolution   
            
         
        """
        pass
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
         Returns the preview toggle   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: ( SelectionAndPlacementBuilder NXOpen.) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def WhollyEnclosedVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WhollyEnclosedVolumeColor
         Returns the Enclosed Void Volume Color   
            
         
        """
        pass
    @WhollyEnclosedVolumeColor.setter
    def WhollyEnclosedVolumeColor(self, whollyEnclosedVolumeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WhollyEnclosedVolumeColor
         Returns the Enclosed Void Volume Color   
            
         
        """
        pass
import NXOpen
class ConfigureCheckerManager(NXOpen.Object): 
    """ Represents an object that manages Checker Editor Configuration.
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class FDMPrintTimeParameter(NXOpen.TaggedObject): 
    """ Class for Print Time Parameter for Fused Deposition Modelling """
    @property
    def LayerThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LayerThickness
         Returns the Layer thickness or slice thickness for printer.  
          
                Specify the thickness of material to be added on each layer.   
         
        """
        pass
    @property
    def NozzleDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NozzleDiameter
         Returns the Jet nozzle diameter of printer.  
           Specify the width of the
                nozzle determining the material thickness along the print path.   
         
        """
        pass
    @property
    def TravelSpeed(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TravelSpeed
         Returns the Scan Speed(Travel Speed) of the printer.  
           Specify the speed of the print path.   
         
        """
        pass
import NXOpen
class KeyPerformanceInterfaceCollection(NXOpen.Object): 
    """ This class represents the collection """
    class JaPmiObjectDetailType(Enum):
        """
        Members Include: 
         |Unknow| 
         |DimNominalValueDetail| 
         |DimUpperToleranceDetail| 
         |DimLowerToleranceDetail| 
         |DimCalloutDepthValue| 
         |DimCalloutDepthUpperTolerance| 
         |DimCalloutDepthLowerTolerance| 
         |DimCalloutDiameterValue| 
         |DimCalloutDiameterUpperTolerance| 
         |DimCalloutDiameterLowerTolerance| 
         |DimCalloutThruValue| 
         |DimCalloutTipAngleValue| 
         |DimCalloutTipAngleUpperTolerance| 
         |DimCalloutTipAngleLowerTolerance| 
         |DimCalloutCboreDepthValue| 
         |DimCalloutCboreDepthUpperTolerance| 
         |DimCalloutCboreDepthLowerTolerance| 
         |DimCalloutCboreDiameterValue| 
         |DimCalloutCboreDiameterUpperTolerance| 
         |DimCalloutCboreDiameterLowerTolerance| 
         |DimCalloutCboreDiameterFitHoleDeviation| 
         |DimCalloutCboreDiameterFitHoleGrade| 
         |DimCalloutCboreDiameterFitShaftDeviation| 
         |DimCalloutCboreDiameterFitShaftGrade| 
         |DimCalloutHoleDiameterValue| 
         |DimCalloutHoleDiameterUpperTolerance| 
         |DimCalloutHoleDiameterLowerTolerance| 
         |DimCalloutHoleDiameterFitHoleDeviation| 
         |DimCalloutHoleDiameterFitHoleGrade| 
         |DimCalloutHoleDiameterFitShaftDeviation| 
         |DimCalloutHoleDiameterFitShaftGrade| 
         |DimCalloutCsunkDiameterValue| 
         |DimCalloutCsunkDiameterUpperTolerance| 
         |DimCalloutCsunkDiameterLowerTolerance| 
         |DimCalloutCsunkDiameterFitHoleDeviation| 
         |DimCalloutCsunkDiameterFitHoleGrade| 
         |DimCalloutCsunkDiameterFitShaftDeviation| 
         |DimCalloutCsunkDiameterFitShaftGrade| 
         |DimCalloutCsunkAngleValue| 
         |DimCalloutCsunkAngleUpperTolerance| 
         |DimCalloutCsunkAngleLowerTolerance| 
         |DimCalloutAngleValue| 
         |DimCalloutAngleUpperTolerance| 
         |DimCalloutAngleLowerTolerance| 
         |DimCalloutFormValue| 
         |DimCalloutFormUpperTolerance| 
         |DimCalloutFormLowerTolerance| 
         |DimCalloutIsInternalValue| 
         |DimCalloutIsExternalValue| 
         |DimCalloutLeftHandValue| 
         |DimCalloutLengthValue| 
         |DimCalloutLengthUpperTolerance| 
         |DimCalloutLengthLowerTolerance| 
         |DimCalloutMajorDiameterValue| 
         |DimCalloutMajorDiameterUpperTolerance| 
         |DimCalloutMajorDiameterLowerTolerance| 
         |DimCalloutMajorDiameterFitHoleDeviation| 
         |DimCalloutMajorDiameterFitHoleGrade| 
         |DimCalloutMajorDiameterFitShaftDeviation| 
         |DimCalloutMajorDiameterFitShaftGrade| 
         |DimCalloutMethodValue| 
         |DimCalloutMinorDiameterValue| 
         |DimCalloutMinorDiameterUpperTolerance| 
         |DimCalloutMinorDiameterLowerTolerance| 
         |DimCalloutMinorDiameterFitHoleDeviation| 
         |DimCalloutMinorDiameterFitHoleGrade| 
         |DimCalloutMinorDiameterFitShaftDeviation| 
         |DimCalloutMinorDiameterFitShaftGrade| 
         |DimCalloutNominalSizeValue| 
         |DimCalloutIntExtSymbolValue| 
         |DimCalloutThreadsPerUnitValue| 
         |DimCalloutThreadFormValue| 
         |DimCalloutStartChamferDiameterValue| 
         |DimCalloutStartChamferDiameterUpperTolerance| 
         |DimCalloutStartChamferDiameterLowerTolerance| 
         |DimCalloutStartChamferAngleValue| 
         |DimCalloutStartChamferAngleUpperTolerance| 
         |DimCalloutStartChamferAngleLowerTolerance| 
         |DimCalloutStartChamferDiameterFitHoleDeviation| 
         |DimCalloutStartChamferDiameterFitHoleGrade| 
         |DimCalloutStartChamferDiameterFitShaftDeviation| 
         |DimCalloutStartChamferDiameterFitShaftGrade| 
         |DimCalloutEndChamferDiameterValue| 
         |DimCalloutEndChamferDiameterUpperTolerance| 
         |DimCalloutEndChamferDiameterLowerTolerance| 
         |DimCalloutEndChamferAngleValue| 
         |DimCalloutEndChamferAngleUpperTolerance| 
         |DimCalloutEndChamferAngleLowerTolerance| 
         |DimCalloutEndChamferDiameterFitHoleDeviation| 
         |DimCalloutEndChamferDiameterFitHoleGrade| 
         |DimCalloutEndChamferDiameterFitShaftDeviation| 
         |DimCalloutEndChamferDiameterFitShaftGrade| 
         |DimCalloutReliefChamferDiameterValue| 
         |DimCalloutReliefChamferDiameterUpperTolerance| 
         |DimCalloutReliefChamferDiameterLowerTolerance| 
         |DimCalloutReliefChamferAngleValue| 
         |DimCalloutReliefChamferAngleUpperTolerance| 
         |DimCalloutReliefChamferAngleLowerTolerance| 
         |DimCalloutReliefChamferDiameterFitHoleDeviation| 
         |DimCalloutReliefChamferDiameterFitHoleGrade| 
         |DimCalloutReliefChamferDiameterFitShaftDeviation| 
         |DimCalloutReliefChamferDiameterFitShaftGrade| 
         |DimCalloutReliefDepthValue| 
         |DimCalloutReliefDepthUpperTolerance| 
         |DimCalloutReliefDepthLowerTolerance| 
         |DimCalloutReliefDiameterValue| 
         |DimCalloutReliefDiameterLowerTolerance| 
         |DimCalloutReliefDiameterUpperTolerance| 
         |DimCalloutReliefDiameterFitHoleDeviation| 
         |DimCalloutReliefDiameterFitHoleGrade| 
         |DimCalloutReliefDiameterFitShaftDeviation| 
         |DimCalloutReliefDiameterFitShaftGrade| 
         |DimCalloutPitchValue| 
         |DimCalloutPitchUpperTolerance| 
         |DimCalloutPitchLowerTolerance| 
         |DimCalloutDrillSizeValue| 
         |DimCalloutDrillSizeUpperTolerance| 
         |DimCalloutDrillSizeLowerTolerance| 
         |DimCalloutTapDrillSizeValue| 
         |DimCalloutTapDrillSizeUpperTolerance| 
         |DimCalloutTapDrillSizeLowerTolerance| 
         |DimCalloutTapDrillSizeFitHoleDeviation| 
         |DimCalloutTapDrillSizeFitHoleGrade| 
         |DimCalloutTapDrillSizeFitShaftDeviation| 
         |DimCalloutTapDrillSizeFitShaftGrade| 
         |DimCalloutNumStartsEq1Value| 
         |DimCalloutNumStartsEq1UpperTolerance| 
         |DimCalloutNumStartsEq1LowerTolerance| 
         |DimCalloutNumStartsGt1Value| 
         |DimCalloutNumStartsGt1UpperTolerance| 
         |DimCalloutNumStartsGt1LowerTolerance| 
         |DimCalloutIsNotTaperedValue| 
         |DimCalloutIsNotTaperedUpperTolerance| 
         |DimCalloutIsNotTaperedLowerTolerance| 
         |DimCalloutIsTaperedValue| 
         |DimCalloutIsTaperedUpperTolerance| 
         |DimCalloutIsTaperedLowerTolerance| 
         |DimCalloutNumberOfInstancesValue| 
         |DimCalloutNumberOfInstancesUpperTolerance| 
         |DimCalloutNumberOfInstancesLowerTolerance| 
         |DimCalloutBlendRadiusValue| 
         |DimCalloutBlendRadiusUpperTolerance| 
         |DimCalloutBlendRadiusLowerTolerance| 
         |DimCalloutThreadStrValue| 
         |DimCalloutThreadStrUpperTolerance| 
         |DimCalloutThreadStrLowerTolerance| 
         |DimCalloutThreadCountValue| 
         |DimCalloutThreadCountUpperTolerance| 
         |DimCalloutThreadCountLowerTolerance| 
         |DimCalloutThreadFullValue| 
         |DimCalloutThreadFullUpperTolerance| 
         |DimCalloutThreadFullLowerTolerance| 
         |DimCalloutXLengthValue| 
         |DimCalloutXLengthUpperTolerance| 
         |DimCalloutXLengthLowerTolerance| 
         |DimCalloutYLengthValue| 
         |DimCalloutYLengthUpperTolerance| 
         |DimCalloutYLengthLowerTolerance| 
         |DimCalloutCenterLengthValue| 
         |DimCalloutCenterLengthUpperTolerance| 
         |DimCalloutCenterLengthLowerTolerance| 
         |DimCalloutXLengthTopValue| 
         |DimCalloutXLengthTopUpperTolerance| 
         |DimCalloutXLengthTopLowerTolerance| 
         |DimCalloutYLengthTopValue| 
         |DimCalloutYLengthTopUpperTolerance| 
         |DimCalloutYLengthTopLowerTolerance| 
         |DimCalloutCenterLengthTopValue| 
         |DimCalloutCenterLengthTopUpperTolerance| 
         |DimCalloutCenterLengthTopLowerTolerance| 
         |DimCalloutTaperAngleValue| 
         |DimCalloutTaperAngleUpperTolerance| 
         |DimCalloutTaperAngleLowerTolerance| 
         |DimCalloutShaftSizeValue| 
         |DimCalloutShaftSizeUpperTolerance| 
         |DimCalloutShaftSizeLowerTolerance| 
         |DimCalloutShaftSizeFitHoleDeviation| 
         |DimCalloutShaftSizeFitHoleGrade| 
         |DimCalloutShaftSizeFitShaftDeviation| 
         |DimCalloutShaftSizeFitShaftGrade| 
         |DimCalloutFitValue| 
         |DimCalloutFitUpperTolerance| 
         |DimCalloutFitLowerTolerance| 
         |DimCalloutNeckChamferAngleValue| 
         |DimCalloutNeckChamferAngleUpperTolerance| 
         |DimCalloutNeckChamferAngleLowerTolerance| 
         |DimCalloutNeckChamferDiameterValue| 
         |DimCalloutNeckChamferDiameterUpperTolerance| 
         |DimCalloutNeckChamferDiameterLowerTolerance| 
         |DimCalloutNeckChamferDiameterFitHoleDeviation| 
         |DimCalloutNeckChamferDiameterFitHoleGrade| 
         |DimCalloutNeckChamferDiameterFitShaftDeviation| 
         |DimCalloutNeckChamferDiameterFitShaftGrade| 
         |DimCalloutThreadHandednessValue| 
         |DimCalloutThreadToleranceValue| 
         |FcfTypeDetail| 
         |FcfShapeDetail| 
         |FcfToleranceDetail| 
         |FcfModifierDetail| 
         |FcfPrimaryDatumDetail| 
         |FcfPrimaryMcmDetail| 
         |FcfSecondaryDatumDetail| 
         |FcfSecondaryMcmDetail| 
         |FcfTertiaryDatumDetail| 
         |FcfTertiaryMcmDetail| 
         |CompFcfShapeDetail| 
         |CompFcfToleranceDetail| 
         |CompFcfModifierDetail| 
         |CompFcfPrimaryDatumDetail| 
         |CompFcfPrimaryMcmDetail| 
         |CompFcfSecondaryDatumDetail| 
         |CompFcfSecondaryMcmDetail| 
         |CompFcfTertiaryDatumDetail| 
         |CompFcfTertiaryMcmDetail| 
         |SurfinStandardDetail| 
         |SurfinSymbolTypeDetail| 
         |SurfinSurfaceRoughnessDetail| 
         |SurfinMethodTreatCoatDetail| 
         |SurfinRoughnessCutoffDetail| 
         |SurfinDirectionOfLayDetail| 
         |SurfinMinMaterialRemovalDetail| 
         |SurfinRoughnessValueDetail| 
         |SurfinToleranceTypeDetail| 
         |SurfinRoughnessToleranceDetail| 
         |SurfinRoughnessLowerToleranceDetail| 
         |SurfinSurfaceRoughnessMaxDetail| 
         |SurfinSurfaceRoughnessMinDetail| 
         |SurfinRoughnessValueF1Detail| 
         |SurfinRoughnessValueF2Detail| 
         |SurfinSecondaryRoughnessDetail| 
         |SurfinTertiaryRoughnessDetail| 

        """
        Unknow: int
        DimNominalValueDetail: int
        DimUpperToleranceDetail: int
        DimLowerToleranceDetail: int
        DimCalloutDepthValue: int
        DimCalloutDepthUpperTolerance: int
        DimCalloutDepthLowerTolerance: int
        DimCalloutDiameterValue: int
        DimCalloutDiameterUpperTolerance: int
        DimCalloutDiameterLowerTolerance: int
        DimCalloutThruValue: int
        DimCalloutTipAngleValue: int
        DimCalloutTipAngleUpperTolerance: int
        DimCalloutTipAngleLowerTolerance: int
        DimCalloutCboreDepthValue: int
        DimCalloutCboreDepthUpperTolerance: int
        DimCalloutCboreDepthLowerTolerance: int
        DimCalloutCboreDiameterValue: int
        DimCalloutCboreDiameterUpperTolerance: int
        DimCalloutCboreDiameterLowerTolerance: int
        DimCalloutCboreDiameterFitHoleDeviation: int
        DimCalloutCboreDiameterFitHoleGrade: int
        DimCalloutCboreDiameterFitShaftDeviation: int
        DimCalloutCboreDiameterFitShaftGrade: int
        DimCalloutHoleDiameterValue: int
        DimCalloutHoleDiameterUpperTolerance: int
        DimCalloutHoleDiameterLowerTolerance: int
        DimCalloutHoleDiameterFitHoleDeviation: int
        DimCalloutHoleDiameterFitHoleGrade: int
        DimCalloutHoleDiameterFitShaftDeviation: int
        DimCalloutHoleDiameterFitShaftGrade: int
        DimCalloutCsunkDiameterValue: int
        DimCalloutCsunkDiameterUpperTolerance: int
        DimCalloutCsunkDiameterLowerTolerance: int
        DimCalloutCsunkDiameterFitHoleDeviation: int
        DimCalloutCsunkDiameterFitHoleGrade: int
        DimCalloutCsunkDiameterFitShaftDeviation: int
        DimCalloutCsunkDiameterFitShaftGrade: int
        DimCalloutCsunkAngleValue: int
        DimCalloutCsunkAngleUpperTolerance: int
        DimCalloutCsunkAngleLowerTolerance: int
        DimCalloutAngleValue: int
        DimCalloutAngleUpperTolerance: int
        DimCalloutAngleLowerTolerance: int
        DimCalloutFormValue: int
        DimCalloutFormUpperTolerance: int
        DimCalloutFormLowerTolerance: int
        DimCalloutIsInternalValue: int
        DimCalloutIsExternalValue: int
        DimCalloutLeftHandValue: int
        DimCalloutLengthValue: int
        DimCalloutLengthUpperTolerance: int
        DimCalloutLengthLowerTolerance: int
        DimCalloutMajorDiameterValue: int
        DimCalloutMajorDiameterUpperTolerance: int
        DimCalloutMajorDiameterLowerTolerance: int
        DimCalloutMajorDiameterFitHoleDeviation: int
        DimCalloutMajorDiameterFitHoleGrade: int
        DimCalloutMajorDiameterFitShaftDeviation: int
        DimCalloutMajorDiameterFitShaftGrade: int
        DimCalloutMethodValue: int
        DimCalloutMinorDiameterValue: int
        DimCalloutMinorDiameterUpperTolerance: int
        DimCalloutMinorDiameterLowerTolerance: int
        DimCalloutMinorDiameterFitHoleDeviation: int
        DimCalloutMinorDiameterFitHoleGrade: int
        DimCalloutMinorDiameterFitShaftDeviation: int
        DimCalloutMinorDiameterFitShaftGrade: int
        DimCalloutNominalSizeValue: int
        DimCalloutIntExtSymbolValue: int
        DimCalloutThreadsPerUnitValue: int
        DimCalloutThreadFormValue: int
        DimCalloutStartChamferDiameterValue: int
        DimCalloutStartChamferDiameterUpperTolerance: int
        DimCalloutStartChamferDiameterLowerTolerance: int
        DimCalloutStartChamferAngleValue: int
        DimCalloutStartChamferAngleUpperTolerance: int
        DimCalloutStartChamferAngleLowerTolerance: int
        DimCalloutStartChamferDiameterFitHoleDeviation: int
        DimCalloutStartChamferDiameterFitHoleGrade: int
        DimCalloutStartChamferDiameterFitShaftDeviation: int
        DimCalloutStartChamferDiameterFitShaftGrade: int
        DimCalloutEndChamferDiameterValue: int
        DimCalloutEndChamferDiameterUpperTolerance: int
        DimCalloutEndChamferDiameterLowerTolerance: int
        DimCalloutEndChamferAngleValue: int
        DimCalloutEndChamferAngleUpperTolerance: int
        DimCalloutEndChamferAngleLowerTolerance: int
        DimCalloutEndChamferDiameterFitHoleDeviation: int
        DimCalloutEndChamferDiameterFitHoleGrade: int
        DimCalloutEndChamferDiameterFitShaftDeviation: int
        DimCalloutEndChamferDiameterFitShaftGrade: int
        DimCalloutReliefChamferDiameterValue: int
        DimCalloutReliefChamferDiameterUpperTolerance: int
        DimCalloutReliefChamferDiameterLowerTolerance: int
        DimCalloutReliefChamferAngleValue: int
        DimCalloutReliefChamferAngleUpperTolerance: int
        DimCalloutReliefChamferAngleLowerTolerance: int
        DimCalloutReliefChamferDiameterFitHoleDeviation: int
        DimCalloutReliefChamferDiameterFitHoleGrade: int
        DimCalloutReliefChamferDiameterFitShaftDeviation: int
        DimCalloutReliefChamferDiameterFitShaftGrade: int
        DimCalloutReliefDepthValue: int
        DimCalloutReliefDepthUpperTolerance: int
        DimCalloutReliefDepthLowerTolerance: int
        DimCalloutReliefDiameterValue: int
        DimCalloutReliefDiameterLowerTolerance: int
        DimCalloutReliefDiameterUpperTolerance: int
        DimCalloutReliefDiameterFitHoleDeviation: int
        DimCalloutReliefDiameterFitHoleGrade: int
        DimCalloutReliefDiameterFitShaftDeviation: int
        DimCalloutReliefDiameterFitShaftGrade: int
        DimCalloutPitchValue: int
        DimCalloutPitchUpperTolerance: int
        DimCalloutPitchLowerTolerance: int
        DimCalloutDrillSizeValue: int
        DimCalloutDrillSizeUpperTolerance: int
        DimCalloutDrillSizeLowerTolerance: int
        DimCalloutTapDrillSizeValue: int
        DimCalloutTapDrillSizeUpperTolerance: int
        DimCalloutTapDrillSizeLowerTolerance: int
        DimCalloutTapDrillSizeFitHoleDeviation: int
        DimCalloutTapDrillSizeFitHoleGrade: int
        DimCalloutTapDrillSizeFitShaftDeviation: int
        DimCalloutTapDrillSizeFitShaftGrade: int
        DimCalloutNumStartsEq1Value: int
        DimCalloutNumStartsEq1UpperTolerance: int
        DimCalloutNumStartsEq1LowerTolerance: int
        DimCalloutNumStartsGt1Value: int
        DimCalloutNumStartsGt1UpperTolerance: int
        DimCalloutNumStartsGt1LowerTolerance: int
        DimCalloutIsNotTaperedValue: int
        DimCalloutIsNotTaperedUpperTolerance: int
        DimCalloutIsNotTaperedLowerTolerance: int
        DimCalloutIsTaperedValue: int
        DimCalloutIsTaperedUpperTolerance: int
        DimCalloutIsTaperedLowerTolerance: int
        DimCalloutNumberOfInstancesValue: int
        DimCalloutNumberOfInstancesUpperTolerance: int
        DimCalloutNumberOfInstancesLowerTolerance: int
        DimCalloutBlendRadiusValue: int
        DimCalloutBlendRadiusUpperTolerance: int
        DimCalloutBlendRadiusLowerTolerance: int
        DimCalloutThreadStrValue: int
        DimCalloutThreadStrUpperTolerance: int
        DimCalloutThreadStrLowerTolerance: int
        DimCalloutThreadCountValue: int
        DimCalloutThreadCountUpperTolerance: int
        DimCalloutThreadCountLowerTolerance: int
        DimCalloutThreadFullValue: int
        DimCalloutThreadFullUpperTolerance: int
        DimCalloutThreadFullLowerTolerance: int
        DimCalloutXLengthValue: int
        DimCalloutXLengthUpperTolerance: int
        DimCalloutXLengthLowerTolerance: int
        DimCalloutYLengthValue: int
        DimCalloutYLengthUpperTolerance: int
        DimCalloutYLengthLowerTolerance: int
        DimCalloutCenterLengthValue: int
        DimCalloutCenterLengthUpperTolerance: int
        DimCalloutCenterLengthLowerTolerance: int
        DimCalloutXLengthTopValue: int
        DimCalloutXLengthTopUpperTolerance: int
        DimCalloutXLengthTopLowerTolerance: int
        DimCalloutYLengthTopValue: int
        DimCalloutYLengthTopUpperTolerance: int
        DimCalloutYLengthTopLowerTolerance: int
        DimCalloutCenterLengthTopValue: int
        DimCalloutCenterLengthTopUpperTolerance: int
        DimCalloutCenterLengthTopLowerTolerance: int
        DimCalloutTaperAngleValue: int
        DimCalloutTaperAngleUpperTolerance: int
        DimCalloutTaperAngleLowerTolerance: int
        DimCalloutShaftSizeValue: int
        DimCalloutShaftSizeUpperTolerance: int
        DimCalloutShaftSizeLowerTolerance: int
        DimCalloutShaftSizeFitHoleDeviation: int
        DimCalloutShaftSizeFitHoleGrade: int
        DimCalloutShaftSizeFitShaftDeviation: int
        DimCalloutShaftSizeFitShaftGrade: int
        DimCalloutFitValue: int
        DimCalloutFitUpperTolerance: int
        DimCalloutFitLowerTolerance: int
        DimCalloutNeckChamferAngleValue: int
        DimCalloutNeckChamferAngleUpperTolerance: int
        DimCalloutNeckChamferAngleLowerTolerance: int
        DimCalloutNeckChamferDiameterValue: int
        DimCalloutNeckChamferDiameterUpperTolerance: int
        DimCalloutNeckChamferDiameterLowerTolerance: int
        DimCalloutNeckChamferDiameterFitHoleDeviation: int
        DimCalloutNeckChamferDiameterFitHoleGrade: int
        DimCalloutNeckChamferDiameterFitShaftDeviation: int
        DimCalloutNeckChamferDiameterFitShaftGrade: int
        DimCalloutThreadHandednessValue: int
        DimCalloutThreadToleranceValue: int
        FcfTypeDetail: int
        FcfShapeDetail: int
        FcfToleranceDetail: int
        FcfModifierDetail: int
        FcfPrimaryDatumDetail: int
        FcfPrimaryMcmDetail: int
        FcfSecondaryDatumDetail: int
        FcfSecondaryMcmDetail: int
        FcfTertiaryDatumDetail: int
        FcfTertiaryMcmDetail: int
        CompFcfShapeDetail: int
        CompFcfToleranceDetail: int
        CompFcfModifierDetail: int
        CompFcfPrimaryDatumDetail: int
        CompFcfPrimaryMcmDetail: int
        CompFcfSecondaryDatumDetail: int
        CompFcfSecondaryMcmDetail: int
        CompFcfTertiaryDatumDetail: int
        CompFcfTertiaryMcmDetail: int
        SurfinStandardDetail: int
        SurfinSymbolTypeDetail: int
        SurfinSurfaceRoughnessDetail: int
        SurfinMethodTreatCoatDetail: int
        SurfinRoughnessCutoffDetail: int
        SurfinDirectionOfLayDetail: int
        SurfinMinMaterialRemovalDetail: int
        SurfinRoughnessValueDetail: int
        SurfinToleranceTypeDetail: int
        SurfinRoughnessToleranceDetail: int
        SurfinRoughnessLowerToleranceDetail: int
        SurfinSurfaceRoughnessMaxDetail: int
        SurfinSurfaceRoughnessMinDetail: int
        SurfinRoughnessValueF1Detail: int
        SurfinRoughnessValueF2Detail: int
        SurfinSecondaryRoughnessDetail: int
        SurfinTertiaryRoughnessDetail: int
        @staticmethod
        def ValueOf(value: int) -> KeyPerformanceInterfaceCollection.JaPmiObjectDetailType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateLinkedParameterRequirementsBuilder(part: NXOpen.Part) -> LinkedParameterReqDialogBuilder:
        """
         Creates Linked Parameter Requirements Builder 
         Returns builder ( LinkedParameterReqDialogBuilder NXOpen.): .
        """
        pass
    def CreateNewPmiCheck(requirement: Requirement, checkName: str, pmiValue: str, pmi: NXOpen.TaggedObject, detailtype: int) -> RequirementCheck:
        """
        Creates a new requirement check with pmi type 
         Returns validation ( RequirementCheck NXOpen.): .
        """
        pass
    def CreatePmiCheck(requirement: Requirement, checkName: str, pmiValue: str, pmi: NXOpen.TaggedObject, detailtype: int, useRelativeTol: bool) -> RequirementCheck:
        """
        Creates a new requirement check with pmi
         Returns validation ( RequirementCheck NXOpen.): .
        """
        pass
    def CreatePmiCheck2(requirement: Requirement, checkName: str, pmiValue: str, pmi: NXOpen.TaggedObject, detailtype: KeyPerformanceInterfaceCollection.JaPmiObjectDetailType, useRelativeTol: bool) -> RequirementCheck:
        """
        Creates a new requirement check with pmi
         Returns validation ( RequirementCheck NXOpen.): .
        """
        pass
    def RefreshLinkedParameterRequirements(part: NXOpen.Part, requirementTags: List[Requirement], refreshToLatest: bool) -> None:
        """
         Refreshes Linked Parameter Requirements 
        """
        pass
import NXOpen
class LinkedParameterReqDialogBuilder(NXOpen.Builder): 
    """ Represents a Builder class for crating object of linked paramter requirements dialog  """
    def AppendMeasurableAttribute(self, logicalItemId: str, logicalItemRevId: str, mesAttrName: str, mesAttrRevId: str) -> None:
        """
         Appends measurable attribute to builder 
        """
        pass
    def AppendMeasurableAttribute2(self, mesAttrName: str, mesAttrRevId: str) -> None:
        """
         Appends measurable attribute to builder overload 
        """
        pass
import NXOpen
class Logger(NXOpen.TransientObject): 
    """Logs validation outcomes and details for Validate.CheckerDefinition.
    """
    def Dispose(self) -> None:
        """
         Frees the object from memory. After this method is called,
                it is illegal to use the object. In .NET, this method is automatically
                called when the object is deleted by the garbage collector. 
        """
        pass
    def LogBooleanAttribute(self, title: str, booleanValue: bool) -> None:
        """
         Logs a Boolean (logical) attribute. 
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogBooleanAttributes(self, title: str, attrs: List[bool]) -> None:
        """
         Logs an array attributes of Boolean (logical) type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogChildNode(self, childLoggerName: str) -> Logger:
        """
         Asks a child logger node.
                
                childLogger = logger.LogChildNode("Attributes");    
                
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    def LogIntegerAttribute(self, title: str, integerValue: int) -> None:
        """
         Logs an integer number attribute.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogIntegerAttributes(self, title: str, attrs: List[int]) -> None:
        """
         Logs an array attributes of integer type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogMessageNode(self, outcome: NXOpen.Validation.Result, message: str) -> Logger:
        """
         Logs a validation message node.
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    @overload
    def LogNXObject(self, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject) -> None:
        """
         Logs a validation outcome and a NXObject as validation outcome detail.
                
        """
        pass
    def LogNXObjectNode(self, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str) -> Logger:
        """
         Logs a validation outcome node and a NXObject with a message as validation outcome detail.
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    def LogNXObjectNodeOnly(self, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject) -> Logger:
        """
         Logs a validation outcome node and a NXObject as validation outcome detail.
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    def LogNXObjectNodeWithInfo(self, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str, objectName: str, referencePoints: List[NXOpen.Point3d], referenceVectors: List[NXOpen.Vector3d]) -> Logger:
        """
         Logs a validation outcome node and a NXObject with detailed information as validation outcome detail.
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    def LogNXObjectSet(self, name: str, message: str) -> Logger:
        """
         Logs a set of NXObject in a child logger.
                
                objSetLogger = logger.LogNXObjectSet("Failed Bodies", "The connection locations conflict with the constraints.");
                ' the objSetLogger is a child of the logger.
                objSetLogger.LogNXObject(Validation.Result.Failed, body1 );
                objSetLogger.LogNXObject(Validation.Result.Failed, body2 );        
                
                
         Returns childLogger ( Logger NXOpen.):  The child logger that is created.
        """
        pass
    @overload
    def LogNXObject(self, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str) -> None:
        """
         Logs a validation outcome and a NXObject as validation outcome detail.
                
        """
        pass
    @overload
    def LogNXObject(self, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str, objectName: str, referencePoints: List[NXOpen.Point3d], referenceVectors: List[NXOpen.Vector3d]) -> None:
        """
         Logs a validation outcome and a NXObject as validation outcome detail.
                
        """
        pass
    def LogRealAttribute(self, title: str, realValue: float) -> None:
        """
         Logs a real number attribute.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogRealAttributes(self, title: str, attrs: List[float]) -> None:
        """
         Logs an array attributes of real type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogReferencePoints(self, referencePoints: List[NXOpen.Point3d]) -> None:
        """
         Logs reference points for a NXObject as validation outcome detail.
                
        """
        pass
    def LogReferenceVectors(self, locations: List[NXOpen.Point3d], directions: List[NXOpen.Vector3d]) -> None:
        """
         Logs reference vectors for a NXObject as validation outcome detail. Each reference vector is set by a NXOpen.Point3d location and a NXOpen.Vector3d direction.
                
        """
        pass
    def LogResult(self, outcome: NXOpen.Validation.Result, message: str) -> None:
        """
         Logs a validation outcome with descriptive message.
                
        """
        pass
    def LogResultNode(self, outcome: NXOpen.Validation.Result, message: str) -> Logger:
        """
         Logs a validation outcome node with a descriptive message.
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    def LogResultNodeOnly(self, outcome: NXOpen.Validation.Result) -> Logger:
        """
         Logs a validation outcome node without a descriptive message.
                
         Returns childLogger ( Logger NXOpen.):  The child logger of this logger.
        """
        pass
    def LogStringAttribute(self, title: str, stringValue: str) -> None:
        """
         Logs a string attribute.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    def LogStringAttributes(self, title: str, attrs: List[str]) -> None:
        """
         Logs an array attributes of string type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class MJFPrintTimeParameter(NXOpen.TaggedObject): 
    """ Class for Print Time Parameter for Multi Jet Fusion printer"""
    @property
    def LayerPrintTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LayerPrintTime
         Returns the Layer Print Time or print speed of printer.  
          
                Specify the time needed to add a new layer of metal powder.   
         
        """
        pass
    @property
    def LayerThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LayerThickness
         Returns the Layer thickness or slice thickness for printing process.  
          
                Specify the thickness of material to be added on each layer.   
         
        """
        pass
import NXOpen
class OverrideBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Validate.Override builder """
    class DecisionActions(Enum):
        """
        Members Include: 
         |Approved| 
         |Rejected| 
         |Pending| 

        """
        Approved: int
        Rejected: int
        Pending: int
        @staticmethod
        def ValueOf(value: int) -> OverrideBuilder.DecisionActions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RequestTypes(Enum):
        """
        Members Include: 
         |Permanent| 
         |Temporary| 

        """
        Permanent: int
        Temporary: int
        @staticmethod
        def ValueOf(value: int) -> OverrideBuilder.RequestTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ToStates(Enum):
        """
        Members Include: 
         |Passed| 
         |Failed| 

        """
        Passed: int
        Failed: int
        @staticmethod
        def ValueOf(value: int) -> OverrideBuilder.ToStates:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category of override request.  
          
                    The category is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the category of override request.  
          
                    The category is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    @property
    def DecisionAction(self) -> OverrideBuilder.DecisionActions:
        """
        Getter for property: ( OverrideBuilder.DecisionActions NXOpen.) DecisionAction
         Returns the decision action of override request
                    The decision action is automatically pending while override request is created.  
           If any property of override request is changed, the decision action will be pending.
                  
         
        """
        pass
    @DecisionAction.setter
    def DecisionAction(self, decisionAction: OverrideBuilder.DecisionActions):
        """
        Setter for property: ( OverrideBuilder.DecisionActions NXOpen.) DecisionAction
         Returns the decision action of override request
                    The decision action is automatically pending while override request is created.  
           If any property of override request is changed, the decision action will be pending.
                  
         
        """
        pass
    @property
    def DecisionUser(self) -> str:
        """
        Getter for property: (str) DecisionUser
         Returns the decision user 
                    The decision user is a Teamcenter user in the Validation Administration group.  
           If the decision user is empty, it means thant any user in the group can review override request.
                  
         
        """
        pass
    @DecisionUser.setter
    def DecisionUser(self, decisionUser: str):
        """
        Setter for property: (str) DecisionUser
         Returns the decision user 
                    The decision user is a Teamcenter user in the Validation Administration group.  
           If the decision user is empty, it means thant any user in the group can review override request.
                  
         
        """
        pass
    @property
    def Reason(self) -> str:
        """
        Getter for property: (str) Reason
         Returns the reason of override request.  
          
                    The reason is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    @Reason.setter
    def Reason(self, reason: str):
        """
        Setter for property: (str) Reason
         Returns the reason of override request.  
          
                    The reason is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    @property
    def RequestType(self) -> OverrideBuilder.RequestTypes:
        """
        Getter for property: ( OverrideBuilder.RequestTypes NXOpen.) RequestType
         Returns the type of override request  
            
         
        """
        pass
    @RequestType.setter
    def RequestType(self, requestType: OverrideBuilder.RequestTypes):
        """
        Setter for property: ( OverrideBuilder.RequestTypes NXOpen.) RequestType
         Returns the type of override request  
            
         
        """
        pass
    @property
    def ToState(self) -> OverrideBuilder.ToStates:
        """
        Getter for property: ( OverrideBuilder.ToStates NXOpen.) ToState
         Returns the to state of override request   
            
         
        """
        pass
    @ToState.setter
    def ToState(self, toState: OverrideBuilder.ToStates):
        """
        Setter for property: ( OverrideBuilder.ToStates NXOpen.) ToState
         Returns the to state of override request   
            
         
        """
        pass
    def GetDecisionComments(self) -> List[str]:
        """
         Returns the decision comments 
         Returns decisionComments (List[str]): .
        """
        pass
    def GetDetailReason(self) -> List[str]:
        """
         Returns the detail reason 
         Returns detailReason (List[str]): .
        """
        pass
    def SetDecisionComments(self, decisionComments: List[str]) -> None:
        """
         Sets the decision comments 
                    The decision comments is optional.
                
        """
        pass
    def SetDetailReason(self, detailReason: List[str]) -> None:
        """
         Sets the detail reason 
                    The detail reason is optional unless override reason configuration is mandatory in Teamcenter.
                
        """
        pass
import NXOpen
class Override(NXOpen.NXObject): 
    """Represents a NXOpen.Validate.Override object."""
    pass
import NXOpen
class Parameter(NXOpen.TransientObject): 
    """  Represents a NX NXOpen.Validate.Parameter. 
     A parameter is defined with a name, value formula and data type as well as whether the parameter can hold multiple
     values or single value and the data to build pull down menu or List selection dialogue to customize the values at runtime.
     Parameters are used to execute check logic.
    """
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title string of the parameter.  
            
         
        """
        pass
    @property
    def Type(self) -> NXOpen.RuleManager.RuleType:
        """
        Getter for property: ( NXOpen.RuleManager.RuleType) Type
         Returns the data type of a parameter.  
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    def GetBooleanValue(self) -> bool:
        """
         Gets boolean type value from a single value parameter.
         Returns value (bool):  The boolean type value.
        """
        pass
    def GetBooleanValues(self) -> List[bool]:
        """
         Gets boolean type values from a multi-value parameter.
         Returns value (List[bool]):  The boolean type values.
        """
        pass
    def GetDoubleValue(self) -> float:
        """
         Gets real number type value from a single value parameter.
         Returns value (float):  The real number type value.
        """
        pass
    def GetDoubleValues(self) -> List[float]:
        """
         Gets real number type values from a multi-value parameter.
         Returns value (List[float]):  The real number type values.
        """
        pass
    def GetIntValue(self) -> int:
        """
         Gets integer number type value from a single value parameter.
         Returns value (int):  The integer number type value.
        """
        pass
    def GetIntValues(self) -> List[int]:
        """
         Gets integer number type values from a multi-value parameter.
         Returns value (List[int]):  The integer number type values.
        """
        pass
    def GetNXObjectValue(self) -> NXOpen.NXObject:
        """
         Gets NXObject type value from a single value parameter.
         Returns value ( NXOpen.NXObject):  The NXObject type value.
        """
        pass
    def GetNXObjectValues(self) -> List[NXOpen.NXObject]:
        """
         Gets NXObject values from a multi-value parameter.
         Returns value ( NXOpen.NXObject Li):  The NXObject type values.
        """
        pass
    def GetPoint3dValue(self) -> NXOpen.Point3d:
        """
         Gets Point3d type value from a single value parameter.
         Returns value ( NXOpen.Point3d):  Point3d type value.
        """
        pass
    def GetPoint3dValues(self) -> List[NXOpen.Point3d]:
        """
         Gets Point3d type values from a multi-value parameter.
         Returns value ( NXOpen.Point3d Li):  Point3d type values.
        """
        pass
    def GetStringValue(self) -> str:
        """
         Gets string type value from a single value parameter.
         Returns value (str):  The string type value.
        """
        pass
    def GetStringValues(self) -> List[str]:
        """
         Gets string type values from a multi-value parameter.
         Returns value (List[str]):  The string type values.
        """
        pass
    def GetVector3dValue(self) -> NXOpen.Vector3d:
        """
         Gets Vector3d type value from a single value parameter.
         Returns value ( NXOpen.Vector3d):  Vector3d type value.
        """
        pass
    def GetVector3dValues(self) -> List[NXOpen.Vector3d]:
        """
         Gets Vector3d type values from a multi-value parameter.
         Returns value ( NXOpen.Vector3d Li):  Vector3d type values.
        """
        pass
    def IsList(self) -> bool:
        """
         Finds out if a parameter is single value or multi-value. True - multi-value list; false - single value. 
         Returns isList (bool): .
        """
        pass
    def SetBooleanValue(self, data: bool) -> None:
        """
         Sets boolean type value to a single value parameter.
        """
        pass
    def SetBooleanValues(self, data: List[bool]) -> None:
        """
         Sets boolean type values to a multi-value parameter.
        """
        pass
    def SetDoubleValue(self, data: float) -> None:
        """
         Sets real number type value to a single value parameter.
        """
        pass
    def SetDoubleValues(self, data: List[float]) -> None:
        """
         Sets real number type values to a multi-value parameter.
        """
        pass
    def SetIntValue(self, data: int) -> None:
        """
         Sets integer number type value to a single value parameter.
        """
        pass
    def SetIntValues(self, data: List[int]) -> None:
        """
         Sets integer number type values to a multi-value parameter.
        """
        pass
    def SetNXObjectValue(self, data: NXOpen.NXObject) -> None:
        """
         Sets NXObject value to a single value parameter.
        """
        pass
    def SetNXObjectValues(self, data: List[NXOpen.NXObject]) -> None:
        """
         Sets NXObject type values to a multi-value parameter.
        """
        pass
    def SetPoint3dValue(self, data: NXOpen.Point3d) -> None:
        """
         Sets Point3d type value to a single value parameter.
        """
        pass
    def SetPoint3dValues(self, data: List[NXOpen.Point3d]) -> None:
        """
         Sets Point3d type values to a multi-value parameter.
        """
        pass
    def SetStringValue(self, data: str) -> None:
        """
         Sets string type value to a single value parameter.
        """
        pass
    def SetStringValues(self, data: List[str]) -> None:
        """
         Sets string type values to a multi-value parameter.
        """
        pass
    def SetVector3dValue(self, data: NXOpen.Vector3d) -> None:
        """
         Sets Vector3d type value to a single value parameter.
        """
        pass
    def SetVector3dValues(self, data: List[NXOpen.Vector3d]) -> None:
        """
         Sets Vector3d type values to a multi-value parameter.
        """
        pass
import NXOpen
class Parser(NXOpen.TaggedObject): 
    """Represents a NX NXOpen.Validate.Parser.
    """
    class DataSourceTypes(Enum):
        """
        Members Include: 
         |MostRecentRun|  Result of most recent run 
         |ResultFromPart|  Result from part 
         |ResultFromTeamcenter|  Result from Teamcenter 
         |ResultFromNXChecks|  Result from NX checks
         |ResultFromLogFile|  Result from Log File 

        """
        MostRecentRun: int
        ResultFromPart: int
        ResultFromTeamcenter: int
        ResultFromNXChecks: int
        ResultFromLogFile: int
        @staticmethod
        def ValueOf(value: int) -> Parser.DataSourceTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataSource(self) -> Parser.DataSourceTypes:
        """
        Getter for property: ( Parser.DataSourceTypes NXOpen.) DataSource
         Returns the result data source type   
            
         
        """
        pass
    @DataSource.setter
    def DataSource(self, dataSource: Parser.DataSourceTypes):
        """
        Setter for property: ( Parser.DataSourceTypes NXOpen.) DataSource
         Returns the result data source type   
            
         
        """
        pass
    @property
    def MaxDisplayObjects(self) -> int:
        """
        Getter for property: (int) MaxDisplayObjects
         Returns the Max entity count to display of current module   
            
         
        """
        pass
    @MaxDisplayObjects.setter
    def MaxDisplayObjects(self, maxDisplayObjects: int):
        """
        Setter for property: (int) MaxDisplayObjects
         Returns the Max entity count to display of current module   
            
         
        """
        pass
    def ClearResultObjects(self) -> None:
        """
         Clears result objects 
        """
        pass
    def Commit(self) -> None:
        """
         Runs parsing process 
        """
        pass
    def DeleteResult(self, resultObject: ResultObject) -> int:
        """
         Deletes result object, return error code 
         Returns status (int):   .
        """
        pass
    def DeleteResultObject(self, resultObject: ResultObject) -> NXOpen.ErrorList:
        """
         Deletes result object, return error list 
         Returns errors ( NXOpen.ErrorList):  List of errors encountered during the delete .
        """
        pass
    def GetObjectResultObjects(self, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets entity result objects from input object 
         Returns objectResultObject ( ResultObject List[NXOpe):  .
        """
        pass
    def GetObjectSetResultObjects(self, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets entity set result objects from input object 
         Returns objectSetResultObject ( ResultObject List[NXOpe):  .
        """
        pass
    def GetPartResultObjects(self) -> List[ResultObject]:
        """
         Gets part result objects 
         Returns partResultObject ( ResultObject List[NXOpe):   .
        """
        pass
    @overload
    def GetProfileResultObjects(self) -> List[ResultObject]:
        """
         Gets profile result objects 
         Returns profileResultObject ( ResultObject List[NXOpe):   .
        """
        pass
    @overload
    def GetProfileResultObjects(self, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets profile result objects from input object 
         Returns profileResultObject ( ResultObject List[NXOpe):   .
        """
        pass
    @overload
    def GetTestResultObjects(self) -> List[ResultObject]:
        """
         Gets test result objects 
         Returns testResultObject ( ResultObject List[NXOpe):  .
        """
        pass
    @overload
    def GetTestResultObjects(self, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets test result objects from input object 
         Returns testResultObject ( ResultObject List[NXOpe):  .
        """
        pass
import NXOpen
class PartNode(NXOpen.TransientObject): 
    """ Represents a part file that validator will check against. 
     Part node contains the information of part filename and part object. 
     You can create the part node by inputting part filename, or by inputting part object, or by inputting both.
     Validator will use the part object in the part node for checking. Only when the part object in the part node
     is , then validator will use the part filename for checking.
    """
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the part file name   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the part file name   
            
         
        """
        pass
    @property
    def PartObject(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) PartObject
         Returns the part object   
            
         
        """
        pass
    @PartObject.setter
    def PartObject(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) PartObject
         Returns the part object   
            
         
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
class PartOrientationAnalysisResult(AnalysisResult): 
    """
     This can be created using a NXOpen.Validate.CheckPartOrientationBuilder object.
    """
    class CheckerIndex(Enum):
        """
        Members Include: 
         |Minimum| 
         |SurfaceArea|  Projected Surface Area Checker 
         |SupportVolume|  Support Volume Checker 
         |PrintTime|  Print Time Checker 
         |Overheat|  Index for Overheat Checker 
         |Maximum|  Maximum Index of Checkers 

        """
        Minimum: int
        SurfaceArea: int
        SupportVolume: int
        PrintTime: int
        Overheat: int
        Maximum: int
        @staticmethod
        def ValueOf(value: int) -> PartOrientationAnalysisResult.CheckerIndex:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CheckerValues:
        """
         Represents the checker value and range for specific checker 
         PartOrientationAnalysisResultCheckerValues_Struct NXOpen. is an alias for  PartOrientationAnalysisResult.CheckerValues NXOpen..
        """
        @property
        def MCheckerIndex(self) -> PartOrientationAnalysisResult.CheckerIndex:
            """
            Getter for property MCheckerIndex
            Index of the checker

            """
            pass
        @MCheckerIndex.setter
        def MCheckerIndex(self, value: PartOrientationAnalysisResult.CheckerIndex):
            """
            Getter for property MCheckerIndex
            Index of the checker
            Setter for property MCheckerIndex
            Index of the checker

            """
            pass
        @property
        def MCheckerMinValue(self) -> float:
            """
            Getter for property MCheckerMinValue
            Minimum value of checker

            """
            pass
        @MCheckerMinValue.setter
        def MCheckerMinValue(self, value: float):
            """
            Getter for property MCheckerMinValue
            Minimum value of checker
            Setter for property MCheckerMinValue
            Minimum value of checker

            """
            pass
        @property
        def MCheckerValue(self) -> float:
            """
            Getter for property MCheckerValue
            Current value of checker

            """
            pass
        @MCheckerValue.setter
        def MCheckerValue(self, value: float):
            """
            Getter for property MCheckerValue
            Current value of checker
            Setter for property MCheckerValue
            Current value of checker

            """
            pass
        @property
        def MCheckerMaxValue(self) -> float:
            """
            Getter for property MCheckerMaxValue
            Maximum value of checker

            """
            pass
        @MCheckerMaxValue.setter
        def MCheckerMaxValue(self, value: float):
            """
            Getter for property MCheckerMaxValue
            Maximum value of checker
            Setter for property MCheckerMaxValue
            Maximum value of checker

            """
            pass
    def GetMinimumOrientation(self, checker_index: PartOrientationAnalysisResult.CheckerIndex) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get minimum orientation for specific checker 
         Returns A tuple consisting of (origin, orientation, checker_values). 
         - origin is:  NXOpen.Point3d. Origin for the optimum orientation .
         - orientation is:  NXOpen.Vector3d. Z direction of the optimum orientation .
         - checker_values is:  PartOrientationAnalysisResult.CheckerValues List[NXOpe. The values of checker and its range .

        """
        pass
    def GetNumOfOptimumOrientations(self) -> int:
        """
         Get the number of optimal solutions
         Returns num_of_optimum_orientations (int):  Num of optimum orientation available .
        """
        pass
    def GetOptimumOrientation(self, optimum_orientation_index: int) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get the optimum orientation at given index
         Returns A tuple consisting of (origin, orientation, checker_values). 
         - origin is:  NXOpen.Point3d. Origin for the optimum orientation .
         - orientation is:  NXOpen.Vector3d. Z direction of the optimum orientation .
         - checker_values is:  PartOrientationAnalysisResult.CheckerValues List[NXOpe. The values of checker and its range. .

        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PBFPrintTimeParameter(NXOpen.TaggedObject): 
    """ Class for Print Time Parameter for Powder Bed Fusion type printer """
    @property
    def HatchSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HatchSpacing
         Returns the Hatch Distance(Hatch Spacing) for printing process.  
           Specify the width of melted metal powder along the laser path.   
         
        """
        pass
    @property
    def IslandLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IslandLength
         Returns the Hatch Pattern Length(Island Length) for printing process.  
           
                Specify the average length of tile within the laser does crosshatching.   
         
        """
        pass
    @property
    def LayerThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LayerThickness
         Returns the Layer thickness or slice thickness for printing process.  
          
                Specify the thickness of material to be added on each layer.   
         
        """
        pass
    @property
    def RecoatingTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RecoatingTime
         Returns the Recoatig time or Time to lay the powder for each layer for printing process.  
          
                Specify the time needed to add a new layer of metal powder.   
         
        """
        pass
    @property
    def SkyWritingTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SkyWritingTime
         Returns the Sky writing time of the laser for printing process.  
           
                Specify the time the laser needs to decelerate and accelerate
                again when changing its scan direction.   
         
        """
        pass
    @property
    def TravelSpeed(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TravelSpeed
         Returns the Scan Speed(Travel Speed) of laser for printing process.  
           Specify the speed of the print path.   
         
        """
        pass
import NXOpen
class PersistentResultCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX NXOpen.Validate.PersistentResultCollection object.
    """
    pass
import NXOpen
class PersistentResult(NXOpen.NXObject): 
    """
     Represents a NXOpen.Validate.PersistentResult object.
    """
    @property
    def CheckerClassId(self) -> str:
        """
        Getter for property: (str) CheckerClassId
         Returns the checker class id.  
             
         
        """
        pass
    @CheckerClassId.setter
    def CheckerClassId(self, class_id: str):
        """
        Setter for property: (str) CheckerClassId
         Returns the checker class id.  
             
         
        """
        pass
    @property
    def ErrorLevel(self) -> NXOpen.Validation.Result:
        """
        Getter for property: ( NXOpen.Validation.Result) ErrorLevel
         Returns the error level.  
             
         
        """
        pass
    @ErrorLevel.setter
    def ErrorLevel(self, error_level: NXOpen.Validation.Result):
        """
        Setter for property: ( NXOpen.Validation.Result) ErrorLevel
         Returns the error level.  
             
         
        """
        pass
    @property
    def UpToDateStatus(self) -> bool:
        """
        Getter for property: (bool) UpToDateStatus
         Returns the result's uptodate status.  
             
         
        """
        pass
    def AddTrackingObjects(self, key: str, objects: List[NXOpen.TaggedObject]) -> None:
        """
         Add the Validate.PersistentResult tracking objects.
        """
        pass
    def GetTrackingObjects(self, key: str) -> List[NXOpen.TaggedObject]:
        """
         Get the Validate.PersistentResult tracking objects which trigger the Validate.PersistentResult re-run when modified. For example, if a PersistentResult tracks a Face, it will re-run when the Face is modfied.
         Returns objects ( NXOpen.TaggedObject Li):   .
        """
        pass
class PorosityAnalysisResult(AnalysisResult): 
    """
     This can be created using a NXOpen.Validate.PorosityAnalysisResult object.
    """
    pass
import NXOpen
class ProfileDefinition(NXOpen.TransientObject): 
    """ Defines a checker profile.
     Profile definition contains the information of the class name, the parameter values, 
     and the child checkers and so on. These informations are used to create profile instance for customization
     of parameters.
    """
    def AddChildChecker(self, checkerClassId: str, parameters: List[Parameter]) -> None:
        """
         Add child checker and its customization parameters to this profile definition.
        """
        pass
    CustomizationHandler = Callable[[CheckerNode], None]
    def Dispose(self) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
    DocumentationHandler = Callable[[CheckerNode], None]
    def SetAllowUserCustomize(self, allowUserCustomize: bool) -> None:
        """
         Sets if the checker profile can be customized by user.
        """
        pass
    def SetCustomizationHandler(self, customize: ProfileDefinition.CustomizationHandler) -> None:
        """
         Sets checker profile customization handler. 
        """
        pass
    def SetDocumentationHandler(self, document: ProfileDefinition.DocumentationHandler) -> None:
        """
         Sets checker profile document handler. 
        """
        pass
import NXOpen
class RequirementBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Validate.Requirement builder """
    class DataTypeOptions(Enum):
        """
        Members Include: 
         |Number| 
         |String| 
         |Boolean| 
         |Integer| 
         |Point| 

        """
        Number: int
        String: int
        Boolean: int
        Integer: int
        Point: int
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.DataTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefinitionMethodOptions(Enum):
        """
        Members Include: 
         |SingleSidedComparison| 
         |DoubleSidedComparison| 
         |SetOfValues| 
         |Formula| 

        """
        SingleSidedComparison: int
        DoubleSidedComparison: int
        SetOfValues: int
        Formula: int
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.DefinitionMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RelationalOperatorOptions(Enum):
        """
        Members Include: 
         |Equal| 
         |NotEqual| 
         |LessThan| 
         |LessThanOrEqual| 
         |GreaterThan| 
         |GreaterThanOrEqual| 

        """
        Equal: int
        NotEqual: int
        LessThan: int
        LessThanOrEqual: int
        GreaterThan: int
        GreaterThanOrEqual: int
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.RelationalOperatorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RequirementTypeOptions(Enum):
        """
        Members Include: 
         |ValidationLimit| 
         |DesignLimit| 

        """
        ValidationLimit: int
        DesignLimit: int
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.RequirementTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SeverityOptions(Enum):
        """
        Members Include: 
         |Error| 
         |Warning| 
         |Information| 

        """
        Error: int
        Warning: int
        Information: int
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.SeverityOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataTypeOption(self) -> RequirementBuilder.DataTypeOptions:
        """
        Getter for property: ( RequirementBuilder.DataTypeOptions NXOpen.) DataTypeOption
         Returns the data type option   
            
         
        """
        pass
    @DataTypeOption.setter
    def DataTypeOption(self, dataTypeOption: RequirementBuilder.DataTypeOptions):
        """
        Setter for property: ( RequirementBuilder.DataTypeOptions NXOpen.) DataTypeOption
         Returns the data type option   
            
         
        """
        pass
    @property
    def DefinitionMethodOption(self) -> RequirementBuilder.DefinitionMethodOptions:
        """
        Getter for property: ( RequirementBuilder.DefinitionMethodOptions NXOpen.) DefinitionMethodOption
         Returns the definition method option   
            
         
        """
        pass
    @DefinitionMethodOption.setter
    def DefinitionMethodOption(self, definitionMethodOption: RequirementBuilder.DefinitionMethodOptions):
        """
        Setter for property: ( RequirementBuilder.DefinitionMethodOptions NXOpen.) DefinitionMethodOption
         Returns the definition method option   
            
         
        """
        pass
    @property
    def DoubleSidedMaximumValue(self) -> str:
        """
        Getter for property: (str) DoubleSidedMaximumValue
         Returns the maximum value in double sided comparison   
            
         
        """
        pass
    @DoubleSidedMaximumValue.setter
    def DoubleSidedMaximumValue(self, doubleSidedMaximumValue: str):
        """
        Setter for property: (str) DoubleSidedMaximumValue
         Returns the maximum value in double sided comparison   
            
         
        """
        pass
    @property
    def DoubleSidedMinimumValue(self) -> str:
        """
        Getter for property: (str) DoubleSidedMinimumValue
         Returns the minimum value in double sided comparison   
            
         
        """
        pass
    @DoubleSidedMinimumValue.setter
    def DoubleSidedMinimumValue(self, doubleSidedMinimumValue: str):
        """
        Setter for property: (str) DoubleSidedMinimumValue
         Returns the minimum value in double sided comparison   
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns    the user defined formula.  
           Only effective when 
                 NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption  is set to 
                 NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula .  
         
                  
         
        """
        pass
    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
         Returns    the user defined formula.  
           Only effective when 
                 NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption  is set to 
                 NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula .  
         
                  
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of requirement   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of requirement   
            
         
        """
        pass
    @property
    def RelationalOperatorOption(self) -> RequirementBuilder.RelationalOperatorOptions:
        """
        Getter for property: ( RequirementBuilder.RelationalOperatorOptions NXOpen.) RelationalOperatorOption
         Returns the relational operator option between expression label and the value in single sided comparison   
            
         
        """
        pass
    @RelationalOperatorOption.setter
    def RelationalOperatorOption(self, relationalOperatorOption: RequirementBuilder.RelationalOperatorOptions):
        """
        Setter for property: ( RequirementBuilder.RelationalOperatorOptions NXOpen.) RelationalOperatorOption
         Returns the relational operator option between expression label and the value in single sided comparison   
            
         
        """
        pass
    @property
    def RelationalOperatorOptionOnMaximumValue(self) -> RequirementBuilder.RelationalOperatorOptions:
        """
        Getter for property: ( RequirementBuilder.RelationalOperatorOptions NXOpen.) RelationalOperatorOptionOnMaximumValue
         Returns the relational operator between expression label and maximum value in double sided comparison:
                     [expression] &lt; or &lt;= maximum value.  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    @RelationalOperatorOptionOnMaximumValue.setter
    def RelationalOperatorOptionOnMaximumValue(self, relationalOperatorOnMaximumValue: RequirementBuilder.RelationalOperatorOptions):
        """
        Setter for property: ( RequirementBuilder.RelationalOperatorOptions NXOpen.) RelationalOperatorOptionOnMaximumValue
         Returns the relational operator between expression label and maximum value in double sided comparison:
                     [expression] &lt; or &lt;= maximum value.  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    @property
    def RelationalOperatorOptionOnMinimumValue(self) -> RequirementBuilder.RelationalOperatorOptions:
        """
        Getter for property: ( RequirementBuilder.RelationalOperatorOptions NXOpen.) RelationalOperatorOptionOnMinimumValue
         Returns the relational operator between minimum value and expression label in double sided comparison:
                     minimum value &lt; or &lt;= [expression].  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    @RelationalOperatorOptionOnMinimumValue.setter
    def RelationalOperatorOptionOnMinimumValue(self, relationalOperatorOnMinimumValue: RequirementBuilder.RelationalOperatorOptions):
        """
        Setter for property: ( RequirementBuilder.RelationalOperatorOptions NXOpen.) RelationalOperatorOptionOnMinimumValue
         Returns the relational operator between minimum value and expression label in double sided comparison:
                     minimum value &lt; or &lt;= [expression].  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    @property
    def RequirementTolerance(self) -> float:
        """
        Getter for property: (float) RequirementTolerance
         Returns the tolerance for point type requirement   
            
         
        """
        pass
    @RequirementTolerance.setter
    def RequirementTolerance(self, requirementTolerance: float):
        """
        Setter for property: (float) RequirementTolerance
         Returns the tolerance for point type requirement   
            
         
        """
        pass
    @property
    def RequirementTypeOption(self) -> RequirementBuilder.RequirementTypeOptions:
        """
        Getter for property: ( RequirementBuilder.RequirementTypeOptions NXOpen.) RequirementTypeOption
         Returns the requirement type option   
            
         
        """
        pass
    @RequirementTypeOption.setter
    def RequirementTypeOption(self, requirementTypeOption: RequirementBuilder.RequirementTypeOptions):
        """
        Setter for property: ( RequirementBuilder.RequirementTypeOptions NXOpen.) RequirementTypeOption
         Returns the requirement type option   
            
         
        """
        pass
    @property
    def SeverityOption(self) -> RequirementBuilder.SeverityOptions:
        """
        Getter for property: ( RequirementBuilder.SeverityOptions NXOpen.) SeverityOption
         Returns the severity option   
            
         
        """
        pass
    @SeverityOption.setter
    def SeverityOption(self, severityOption: RequirementBuilder.SeverityOptions):
        """
        Setter for property: ( RequirementBuilder.SeverityOptions NXOpen.) SeverityOption
         Returns the severity option   
            
         
        """
        pass
    @property
    def SingleSidedValue(self) -> str:
        """
        Getter for property: (str) SingleSidedValue
         Returns the value for single sided comparison   
            
         
        """
        pass
    @SingleSidedValue.setter
    def SingleSidedValue(self, singleSidedValue: str):
        """
        Setter for property: (str) SingleSidedValue
         Returns the value for single sided comparison   
            
         
        """
        pass
    def GetRequirementDescription(self) -> List[str]:
        """
         Returns the requirement description 
         Returns requirementDescription (List[str]): .
        """
        pass
    def GetValidValues(self) -> List[str]:
        """
         Returns the valid values 
         Returns validValues (List[str]): .
        """
        pass
    def SetRequirementDescription(self, requirementDescription: List[str]) -> None:
        """
         Sets the requirement description 
        """
        pass
    def SetValidValues(self, validValues: List[str]) -> None:
        """
         Sets the valid values 
        """
        pass
import NXOpen
class RequirementCheckCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX NXOpen.Validate.RequirementCheckCollection object.
    """
    def CreateRequirementCheck(self) -> RequirementCheck:
        """
         Create a requirement check 
         Returns requirementCheck ( RequirementCheck NXOpen.): .
        """
        pass
import NXOpen
class RequirementCheck(NXOpen.Validation): 
    """
     Represents an NX NXOpen.Validate.RequirementCheck object.
    """
    class SaveResultsToTeamcenterOptions(Enum):
        """
        Members Include: 
         |DoNotSave|  Do not perform save. 
         |SaveIfPassed|  Perform save only if the result is passed. 
         |AlwaysSave|  Always perform save 

        """
        DoNotSave: int
        SaveIfPassed: int
        AlwaysSave: int
        @staticmethod
        def ValueOf(value: int) -> RequirementCheck.SaveResultsToTeamcenterOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckName(self) -> str:
        """
        Getter for property: (str) CheckName
         Returns the name of requirement check shown in Requirements Validation dialog   
            
         
        """
        pass
    @CheckName.setter
    def CheckName(self, checkName: str):
        """
        Setter for property: (str) CheckName
         Returns the name of requirement check shown in Requirements Validation dialog   
            
         
        """
        pass
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
         Returns the formula of requirement check   
            
         
        """
        pass
    @property
    def ParentRequirement(self) -> Requirement:
        """
        Getter for property: ( Requirement NXOpen.) ParentRequirement
         Returns the parent  NXOpen::Validate::Requirement    
            
         
        """
        pass
    @ParentRequirement.setter
    def ParentRequirement(self, parentRequirement: Requirement):
        """
        Setter for property: ( Requirement NXOpen.) ParentRequirement
         Returns the parent  NXOpen::Validate::Requirement    
            
         
        """
        pass
    @property
    def SaveResultsToTeamcenterOption(self) -> RequirementCheck.SaveResultsToTeamcenterOptions:
        """
        Getter for property: ( RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.) SaveResultsToTeamcenterOption
         Returns the Save Results to Teamcenter option   
            
         
        """
        pass
    @SaveResultsToTeamcenterOption.setter
    def SaveResultsToTeamcenterOption(self, option: RequirementCheck.SaveResultsToTeamcenterOptions):
        """
        Setter for property: ( RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.) SaveResultsToTeamcenterOption
         Returns the Save Results to Teamcenter option   
            
         
        """
        pass
    def SetFormula(self, formula: str) -> None:
        """
         Sets the formula of requirement check. The requirement check will be re-evaluated. 
        """
        pass
import NXOpen
class RequirementCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX NXOpen.Validate.RequirementCollection object.
    """
    class SourceTypeOptions(Enum):
        """
        Members Include: 
         |LocalFile| 
         |TeamcenterFile| 
         |Teamcenter| 
         |MeasurableAttribute| 

        """
        LocalFile: int
        TeamcenterFile: int
        Teamcenter: int
        MeasurableAttribute: int
        @staticmethod
        def ValueOf(value: int) -> RequirementCollection.SourceTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def RevisionRule(self) -> str:
        """
        Getter for property: (str) RevisionRule
         Returns the revision rule for requirement from Teamcenter   
            
         
        """
        pass
    @RevisionRule.setter
    def RevisionRule(self, rule: str):
        """
        Setter for property: (str) RevisionRule
         Returns the revision rule for requirement from Teamcenter   
            
         
        """
        pass
    def CreateRequirementBuilder(self, requirement: Requirement) -> RequirementBuilder:
        """
         Creates a NXOpen.Validate.RequirementBuilder 
         Returns builder ( RequirementBuilder NXOpen.): .
        """
        pass
    def FindObject(self, id: str) -> Requirement:
        """
         Finds the NXOpen.Validate.Requirement with the given identifier.
                    An exception will be thrown if no object can be found with given identifier. 
         Returns requirement ( Requirement NXOpen.):  NXOpen.Validate.Requirement with the identifier .
        """
        pass
    def LoadFromExternalSource(self, sourceType: RequirementCollection.SourceTypeOptions, source: str, revision: str, project: str) -> None:
        """
          Loads NXOpen.Validate.Requirement from external source.
                     The source can be local file, Teamcenter requirement item or item revision, and Teamcenter spreadsheet dataset
                     for which the input sourceType is LocalFile, Teamcenter and TeamcenterFile respectively.
                 
                     Example inputs when sourceType is LocalFile
                 
                 source: "C:\requirement.xml" or "C:\requirement_spreadsheet.xls"
                 revision: empty string
                 project: "category_A" It's a project node name in the source XML file or a sheet name in the source spreadsheet file.
                 
                 
                     Example inputs when sourceType is Teamcenter
                 
                     If source is item revision 000084A:
                 
                 source: "000084"
                 revision: "A"
                 project: empty string
                 
                 
                     If source is item 000084:
                 
                 source: "000084"
                 revision:empty string
                 project: empty string
                 
                 
                     Example inputs when sourceType is TeamcenterFile
                 
                     If source is a spreadsheet dataset in an item revision 000085A:
                 
                 source: 000085
                 revision: A
                 project: "category_A" It's a sheet name in the source spreadsheet.
                 
                 
                     If source is a spreadsheet dataset in item 000085:
                 
                 source: "000085"
                 revision: empty string
                 project: "category_A" It's a sheet name in the source spreadsheet.
                 
                
        """
        pass
    def RefreshFromExternalSource(self, requirementTags: List[Requirement]) -> None:
        """
         Refreshes the requirements from external source. 
        """
        pass
import NXOpen
class Requirement(NXOpen.NXObject): 
    """
     Represents a NXOpen.Validate.Requirement object.
    """
    def Delete(self) -> None:
        """
         Deletes a user requirement and child NXOpen.Validate.RequirementCheck or removes a external requirement. 
        """
        pass
    def NewCheck(self, name: str, formula: str) -> RequirementCheck:
        """
         Creates a NXOpen.Validate.RequirementCheck for a requirement
         Returns requirementCheck ( RequirementCheck NXOpen.): .
        """
        pass
    def RefreshFromExternalSource(self) -> None:
        """
         Refreshs a requirement from external source.
        """
        pass
import NXOpen
class ResultObject(NXOpen.NXObject): 
    """ Represents a check-mate result object. 
    """
    class ResultTypes(Enum):
        """
        Members Include: 
         |Part|  Part 
         |Profile|  Profile 
         |Test|  Test 
         |Object|  Object 
         |ObjectSet|  Object Set 

        """
        Part: int
        Profile: int
        Test: int
        Object: int
        ObjectSet: int
        @staticmethod
        def ValueOf(value: int) -> ResultObject.ResultTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CategoryName(self) -> str:
        """
        Getter for property: (str) CategoryName
         Returns the category name of check result.  
          
                    Return empty if the ResultObject has no this property.
                  
         
        """
        pass
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
         Returns the class name of check result.  
          
                    Return empty if the ResultObject has no this property.
                  
         
        """
        pass
    @property
    def Disabled(self) -> bool:
        """
        Getter for property: (bool) Disabled
         Returns the disabled status of check result.  
             
         
        """
        pass
    @property
    def Object(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) Object
         Returns the NX object referenced by the check result.  
          
                    Return NULL if the ResultObject has no this property.
                  
         
        """
        pass
    @property
    def OutOfDate(self) -> bool:
        """
        Getter for property: (bool) OutOfDate
         Returns the out of date status of check result.  
          
                Returns error code if part is unloaded. Result of unloaded part is assumed up to date. The program may not be able to detect the modifications in the part.
                  
         
        """
        pass
    @property
    def Override(self) -> Override:
        """
        Getter for property: ( Override NXOpen.) Override
         Returns the override request object of check result   
            
         
        """
        pass
    @property
    def Status(self) -> NXOpen.Validation.Result:
        """
        Getter for property: ( NXOpen.Validation.Result) Status
         Returns the error status of check result   
            
         
        """
        pass
    @Status.setter
    def Status(self, status: NXOpen.Validation.Result):
        """
        Setter for property: ( NXOpen.Validation.Result) Status
         Returns the error status of check result   
            
         
        """
        pass
    @property
    def TotalObjectsCount(self) -> int:
        """
        Getter for property: (int) TotalObjectsCount
         Returns the total objects count of check result.  
          
                    Return zero if the ResultObject has no this property.
                  
         
        """
        pass
    @property
    def Type(self) -> ResultObject.ResultTypes:
        """
        Getter for property: ( ResultObject.ResultTypes NXOpen.) Type
         Returns the type of check result   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ResultObject.ResultTypes):
        """
        Setter for property: ( ResultObject.ResultTypes NXOpen.) Type
         Returns the type of check result   
            
         
        """
        pass
    def AskAttribute(self, name: str) -> NXOpen.NXObject.AttributeInformation:
        """
         
                     Ask a single value attribute of check result. 
                     Refer to the VARIABLE table column in the section "Variables Supported by Check-Mate Templates" 
                     in %UGII_BASE_DIR%\design_tools\checkmate\customization\guide.html for the collection of attribute names. 
                     "No" in the "Can be a list of values?" table column indicates it is a single value attribute.
                 
         Returns value ( NXOpen.NXObject.AttributeInformation):  the value name of check result .
        """
        pass
    def AskAttributes(self, name: str) -> List[NXOpen.NXObject.AttributeInformation]:
        """
         
                     Ask a multi-value attribute of check result. 
                     Refer to the VARIABLE table column in the section "Variables Supported by Check-Mate Templates" 
                     in %UGII_BASE_DIR%\design_tools\checkmate\customization\guide.html for the collection of attribute names. 
                     "Yes" in the "Can be a list of values?" table column indicates it is a multi-value attribute.
                 
         Returns attributes ( NXOpen.NXObject.AttributeInformation Li): .
        """
        pass
    def CreateOverrideBuilder(self, override_request: Override) -> OverrideBuilder:
        """
         Creates a NXOpen.Validate.OverrideBuilder 
         Returns builder ( OverrideBuilder NXOpen.): .
        """
        pass
    def DeleteOverride(self) -> None:
        """
         Deletes user override request NXOpen.Validate.Override. 
        """
        pass
import NXOpen
class RuleBaseSaveBuilder(NXOpen.Builder): 
    """ Represents a Builder for RuleSave functionality"""
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @property
    def ClassID(self) -> str:
        """
        Getter for property: (str) ClassID
         Returns the class name   
            
         
        """
        pass
    @ClassID.setter
    def ClassID(self, classID: str):
        """
        Setter for property: (str) ClassID
         Returns the class name   
            
         
        """
        pass
    @property
    def DisabledToggle(self) -> bool:
        """
        Getter for property: (bool) DisabledToggle
         Returns the disabled toggle   
            
         
        """
        pass
    @DisabledToggle.setter
    def DisabledToggle(self, disabledToggle: bool):
        """
        Setter for property: (bool) DisabledToggle
         Returns the disabled toggle   
            
         
        """
        pass
    @property
    def InteractiveCheckingOnlyToggle(self) -> bool:
        """
        Getter for property: (bool) InteractiveCheckingOnlyToggle
         Returns the interactive checking only toggle   
            
         
        """
        pass
    @InteractiveCheckingOnlyToggle.setter
    def InteractiveCheckingOnlyToggle(self, interactiveCheckingOnly: bool):
        """
        Setter for property: (bool) InteractiveCheckingOnlyToggle
         Returns the interactive checking only toggle   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the rule name   
            
         
        """
        pass
    @Name.setter
    def Name(self, ruleName: str):
        """
        Setter for property: (str) Name
         Returns the rule name   
            
         
        """
        pass
    @property
    def SaveLogInPartToggle(self) -> bool:
        """
        Getter for property: (bool) SaveLogInPartToggle
         Returns the save log in part toggle   
            
         
        """
        pass
    @SaveLogInPartToggle.setter
    def SaveLogInPartToggle(self, saveLogInPart: bool):
        """
        Setter for property: (bool) SaveLogInPartToggle
         Returns the save log in part toggle   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         Returns text (List[str]):  .
        """
        pass
    def SetDescription(self, text: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    def SetFolderPath(self, folderPath: str) -> None:
        """
         Sets the rule folder path 
        """
        pass
    def SetRuleFileName(self, ruleFileName: str) -> None:
        """
         Sets the rule file name 
        """
        pass
import NXOpen
class RuleCheckerManager(NXOpen.Object): 
    """ Represents an object that manages checker rule
    """
    def CreateRulePropertiesBuilder(ruleInstance: NXOpen.NXObject, readOnly: bool) -> RulePropertiesBuilder:
        """
         The JA method support for create rule properties builder
         Returns builder ( RulePropertiesBuilder NXOpen.): .
        """
        pass
    def CreateRuleSaveAsBuilder(ruleInstance: NXOpen.NXObject) -> RuleSaveAsBuilder:
        """
         The JA method support for create rule save as builder
         Returns builder ( RuleSaveAsBuilder NXOpen.): .
        """
        pass
    def CreateRuleSaveBuilder(ruleInstance: NXOpen.NXObject) -> RuleSaveBuilder:
        """
         The JA method support for create rule save builder
         Returns builder ( RuleSaveBuilder NXOpen.): .
        """
        pass
import NXOpen
class RulePropertiesBuilder(NXOpen.Builder): 
    """ Represents a Builder for Rule Properties functionality"""
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the category   
            
         
        """
        pass
    @property
    def ClassID(self) -> str:
        """
        Getter for property: (str) ClassID
         Returns the class name   
            
         
        """
        pass
    @ClassID.setter
    def ClassID(self, classID: str):
        """
        Setter for property: (str) ClassID
         Returns the class name   
            
         
        """
        pass
    @property
    def DisabledToggle(self) -> bool:
        """
        Getter for property: (bool) DisabledToggle
         Returns the disabled toggle   
            
         
        """
        pass
    @DisabledToggle.setter
    def DisabledToggle(self, disabledToggle: bool):
        """
        Setter for property: (bool) DisabledToggle
         Returns the disabled toggle   
            
         
        """
        pass
    @property
    def InteractiveCheckingOnlyToggle(self) -> bool:
        """
        Getter for property: (bool) InteractiveCheckingOnlyToggle
         Returns the interactive checking only toggle   
            
         
        """
        pass
    @InteractiveCheckingOnlyToggle.setter
    def InteractiveCheckingOnlyToggle(self, interactiveCheckingOnly: bool):
        """
        Setter for property: (bool) InteractiveCheckingOnlyToggle
         Returns the interactive checking only toggle   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the rule name   
            
         
        """
        pass
    @Name.setter
    def Name(self, ruleName: str):
        """
        Setter for property: (str) Name
         Returns the rule name   
            
         
        """
        pass
    @property
    def SaveLogInPartToggle(self) -> bool:
        """
        Getter for property: (bool) SaveLogInPartToggle
         Returns the save log in part toggle   
            
         
        """
        pass
    @SaveLogInPartToggle.setter
    def SaveLogInPartToggle(self, saveLogInPart: bool):
        """
        Setter for property: (bool) SaveLogInPartToggle
         Returns the save log in part toggle   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         Returns text (List[str]):  .
        """
        pass
    def SetDescription(self, text: List[str]) -> None:
        """
         Sets the description 
        """
        pass
class RuleSaveAsBuilder(RuleBaseSaveBuilder): 
    """ Represents a Builder for Rule SaveAs functionality"""
    pass
class RuleSaveBuilder(RuleBaseSaveBuilder): 
    """ Represents a Builder for RuleSave functionality"""
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectionAndPlacementBuilder(NXOpen.TaggedObject): 
    """ Represents a Selection And Placement builder """
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    @property
    def DrawOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    def GetTargets(self) -> List[NXOpen.TaggedObject]:
        """
         Returns the selected Bodies or Parts 
         Returns targets ( NXOpen.TaggedObject Li):  The targets should be of NXOpen::Body or NXOpen::Part .
        """
        pass
    def SetTargets(self, targets: List[NXOpen.TaggedObject]) -> None:
        """
         Set the Bodies or Parts 
        """
        pass
import NXOpen
class ValidationManager(NXOpen.Object): 
    """ Represents an object that manages validator and parser associated instance objects.
     It handles the creation of new validators and parsers.
     The ValidationManager also provides NXOpen.Validate.ValidationManager.FindValidator to 
     get validators in current session.
    """
    class ParameterOptions:
        """
         Optional settings for defining a  Validate::Parameter 
         ValidationManagerParameterOptions_Struct NXOpen. is an alias for  ValidationManager.ParameterOptions NXOpen..
        """
        @property
        def Label(self) -> str:
            """
            Getter for property Label
            Parameter label

            """
            pass
        @Label.setter
        def Label(self, value: str):
            """
            Getter for property Label
            Parameter label
            Setter for property Label
            Parameter label

            """
            pass
        @property
        def Group(self) -> str:
            """
            Getter for property Group
            Parameter group.

            """
            pass
        @Group.setter
        def Group(self, value: str):
            """
            Getter for property Group
            Parameter group.
            Setter for property Group
            Parameter group.

            """
            pass
        @property
        def Modifiable(self) -> bool:
            """
            Getter for property Modifiable
            If parameter can be modified.

            """
            pass
        @Modifiable.setter
        def Modifiable(self, value: bool):
            """
            Getter for property Modifiable
            If parameter can be modified.
            Setter for property Modifiable
            If parameter can be modified.

            """
            pass
    DoCheckHandler = Callable[[CheckerNode], None]
    def CreateCheckerDefinition(classID: str, displayName: str, category: str, parameters: List[Parameter], doCheck: ValidationManager.DoCheckHandler) -> CheckerDefinition:
        """
         
                Creates a Validate.CheckerDefinition.
                
                
                Once a checker definition is created successfully, the class ID can be used to create instances of Validate.CheckerNode.
                To obtain an instance of Validate.CheckerNode, refer to Validate.Validator.AppendCheckerNode.
                This method will check the presence of the ug_checkmate ("UG Check Mate") license.
                
                
         Returns checkerDefinition ( CheckerDefinition NXOpen.): .
        """
        pass
    def CreateParser(name: str) -> Parser:
        """
         
                Creates a parser.
                
         Returns parser ( Parser NXOpen.):  .
        """
        pass
    def CreateValidator(name: str) -> Validator:
        """
         
                Creates a validator.
                
         Returns validator ( Validator NXOpen.):  .
        """
        pass
    def DefineCheckerProfile(classID: str, displayName: str, category: str, parameters: List[Parameter]) -> ProfileDefinition:
        """
         
                Creates a Validate.ProfileDefinition.
                
                
         Returns profileDefinition ( ProfileDefinition NXOpen.): .
        """
        pass
    def DefineNXObjectParameter(parameterID: str, parameterValue: NXOpen.NXObject, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for an NXObject. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    def DefineNXObjectParameters(parameterID: str, parameterValue: List[NXOpen.NXObject], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for an NXObject array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: int, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for an integer number. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: List[int], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for an integer array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: NXOpen.Vector3d, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for a Vector3d. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: List[NXOpen.Vector3d], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for a Vector3d array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: bool, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for a boolean. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: List[bool], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for a boolean array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: float, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for a real number. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: List[float], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for a real number array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: str, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for a string. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: List[str], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for a string array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: NXOpen.Point3d, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value Validate.Parameter for a Point3d. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    @overload
    def DefineParameter(parameterID: str, parameterValue: List[NXOpen.Point3d], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value Validate.Parameter for a Point3d array. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    def DefineReferencingParameter(parameterID: str, referencedParameter: Parameter) -> Parameter:
        """
         Creates a parameter and binding it to the input parameter. 
         Returns parameter ( Parameter NXOpen.):  Return defined parameter.
        """
        pass
    def DeleteCheckerDefinition(checkerDefinition: CheckerDefinition) -> None:
        """
         
                Deletes a Validate.CheckerDefinition.
                
                
                Any instance of Validate.CheckerNode based on a checker definition should be eliminated before deleting the checker definition.
                Refer to Validate.Validator.EraseCheckerNode or Validate.Validator.ClearCheckerNodes.
                
                
        """
        pass
    def DeleteCheckerProfileDefinition(profileDefinition: ProfileDefinition) -> None:
        """
         Deletes a Validate.ProfileDefinition.
        """
        pass
    def DeleteParser(parser: Parser) -> None:
        """
         
                Deletes a parser.
                
        """
        pass
    def DeleteValidator(validator: Validator) -> None:
        """
         
                Deletes a validator.
                
        """
        pass
    def FindParser(name: str) -> List[Parser]:
        """
         
                Finds parsers in current session. It will return all parsers with the same name.
                
         Returns parsers ( Parser List[NXOpe):  .
        """
        pass
    def FindValidator(name: str) -> List[Validator]:
        """
         
                Finds validators in current session. It will return all validators with the same name.
                
         Returns validators ( Validator List[NXOpe):  .
        """
        pass
    def GetCheckerDisplayName(classID: str) -> str:
        """
         The display name of the checker.
                    Return empty if the checker is not registered.
                
                displayName = validationManager.GetCheckerDisplayName("classID");    
                
                
         Returns displayName (str):  The display name of the checker. .
        """
        pass
    def RegisterCheckerProfileDefinition(profileDefinition: ProfileDefinition) -> None:
        """
         Registers a checker profile definition to validation manager. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ValidatorOptions(NXOpen.TaggedObject): 
    """ Contains information about run options of check-mate checking process.
    
    """
    class LogModeTypes(Enum):
        """
        Members Include: 
         |LogPerSession|  Generate log per session 
         |LogPerPart|  Generate log per part 

        """
        LogPerSession: int
        LogPerPart: int
        @staticmethod
        def ValueOf(value: int) -> ValidatorOptions.LogModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultsDisplayModeTypes(Enum):
        """
        Members Include: 
         |AlwaysDisplay|  Always display results. 
         |DisplayIfNotPass|  Display results if the checking is not passed. 
         |DoNotDisplay|  Do not display results 

        """
        AlwaysDisplay: int
        DisplayIfNotPass: int
        DoNotDisplay: int
        @staticmethod
        def ValueOf(value: int) -> ValidatorOptions.ResultsDisplayModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveModeTypes(Enum):
        """
        Members Include: 
         |DoNotSave|  Do not perform save. 
         |SaveIfPassed|  Perform save only if the checking is passed. 
         |AlwaysSave|  Always perform save 

        """
        DoNotSave: int
        SaveIfPassed: int
        AlwaysSave: int
        @staticmethod
        def ValueOf(value: int) -> ValidatorOptions.SaveModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoDisplayResults(self) -> ValidatorOptions.ResultsDisplayModeTypes:
        """
        Getter for property: ( ValidatorOptions.ResultsDisplayModeTypes NXOpen.) AutoDisplayResults
         Returns the configuration of auto display results   
            
         
        """
        pass
    @AutoDisplayResults.setter
    def AutoDisplayResults(self, displayResults: ValidatorOptions.ResultsDisplayModeTypes):
        """
        Setter for property: ( ValidatorOptions.ResultsDisplayModeTypes NXOpen.) AutoDisplayResults
         Returns the configuration of auto display results   
            
         
        """
        pass
    @property
    def ExcludeNonOwnerParts(self) -> bool:
        """
        Getter for property: (bool) ExcludeNonOwnerParts
         Returns the configuration of excluding parts not owned by the user.  
             
         
        """
        pass
    @ExcludeNonOwnerParts.setter
    def ExcludeNonOwnerParts(self, excludeNonOwnerParts: bool):
        """
        Setter for property: (bool) ExcludeNonOwnerParts
         Returns the configuration of excluding parts not owned by the user.  
             
         
        """
        pass
    @property
    def ExcludeReadonlyParts(self) -> bool:
        """
        Getter for property: (bool) ExcludeReadonlyParts
         Returns the configuration of excluding read-only parts.  
             
         
        """
        pass
    @ExcludeReadonlyParts.setter
    def ExcludeReadonlyParts(self, excludeReadonlyParts: bool):
        """
        Setter for property: (bool) ExcludeReadonlyParts
         Returns the configuration of excluding read-only parts.  
             
         
        """
        pass
    @property
    def GenerateCheckFlag(self) -> bool:
        """
        Getter for property: (bool) GenerateCheckFlag
         Returns the configuration of generating check flag if checking results are PASS   
            
         
        """
        pass
    @GenerateCheckFlag.setter
    def GenerateCheckFlag(self, generateCheckFlag: bool):
        """
        Setter for property: (bool) GenerateCheckFlag
         Returns the configuration of generating check flag if checking results are PASS   
            
         
        """
        pass
    @property
    def GenerateLogFile(self) -> bool:
        """
        Getter for property: (bool) GenerateLogFile
         Returns the configuration of generating log file after checking.  
           If True, log file will be generated.   
         
        """
        pass
    @GenerateLogFile.setter
    def GenerateLogFile(self, generate_log_file: bool):
        """
        Setter for property: (bool) GenerateLogFile
         Returns the configuration of generating log file after checking.  
           If True, log file will be generated.   
         
        """
        pass
    @property
    def LogFileDirectory(self) -> str:
        """
        Getter for property: (str) LogFileDirectory
         Returns the configuration of log file directory where the log file will be saved.  
             
         
        """
        pass
    @LogFileDirectory.setter
    def LogFileDirectory(self, logFileDirectory: str):
        """
        Setter for property: (str) LogFileDirectory
         Returns the configuration of log file directory where the log file will be saved.  
             
         
        """
        pass
    @property
    def LogFileMode(self) -> ValidatorOptions.LogModeTypes:
        """
        Getter for property: ( ValidatorOptions.LogModeTypes NXOpen.) LogFileMode
         Returns the configuration of log file mode how to generate the log files.  
             
         
        """
        pass
    @LogFileMode.setter
    def LogFileMode(self, logFileMode: ValidatorOptions.LogModeTypes):
        """
        Setter for property: ( ValidatorOptions.LogModeTypes NXOpen.) LogFileMode
         Returns the configuration of log file mode how to generate the log files.  
             
         
        """
        pass
    @property
    def ResultsAutoUpdate(self) -> bool:
        """
        Getter for property: (bool) ResultsAutoUpdate
         Returns the configuration of results auto update when work part change   
            
         
        """
        pass
    @ResultsAutoUpdate.setter
    def ResultsAutoUpdate(self, autoUpdate: bool):
        """
        Setter for property: (bool) ResultsAutoUpdate
         Returns the configuration of results auto update when work part change   
            
         
        """
        pass
    @property
    def SavePartFile(self) -> ValidatorOptions.SaveModeTypes:
        """
        Getter for property: ( ValidatorOptions.SaveModeTypes NXOpen.) SavePartFile
         Returns the configuration of saving part file after checking finished.  
           If True, part file will be saved.   
         
        """
        pass
    @SavePartFile.setter
    def SavePartFile(self, savePartFile: ValidatorOptions.SaveModeTypes):
        """
        Setter for property: ( ValidatorOptions.SaveModeTypes NXOpen.) SavePartFile
         Returns the configuration of saving part file after checking finished.  
           If True, part file will be saved.   
         
        """
        pass
    @property
    def SaveResultInPart(self) -> bool:
        """
        Getter for property: (bool) SaveResultInPart
         Returns the configuration of saving check results into part file.  
           If True, results will be saved in part file after checking finished.   
         
        """
        pass
    @SaveResultInPart.setter
    def SaveResultInPart(self, save_result_in_part: bool):
        """
        Setter for property: (bool) SaveResultInPart
         Returns the configuration of saving check results into part file.  
           If True, results will be saved in part file after checking finished.   
         
        """
        pass
    @property
    def SaveResultInTeamcenter(self) -> ValidatorOptions.SaveModeTypes:
        """
        Getter for property: ( ValidatorOptions.SaveModeTypes NXOpen.) SaveResultInTeamcenter
         Returns the configuration of saving check results into Teamcenter.  
           If true, results will be saved into Teamcenter.
                 This parameter is for NX Manager mode only   
         
        """
        pass
    @SaveResultInTeamcenter.setter
    def SaveResultInTeamcenter(self, save_result_in_teamcenter: ValidatorOptions.SaveModeTypes):
        """
        Setter for property: ( ValidatorOptions.SaveModeTypes NXOpen.) SaveResultInTeamcenter
         Returns the configuration of saving check results into Teamcenter.  
           If true, results will be saved into Teamcenter.
                 This parameter is for NX Manager mode only   
         
        """
        pass
    @property
    def SkipChecking(self) -> bool:
        """
        Getter for property: (bool) SkipChecking
         Returns the configuration of skip checking based on result up-to-date status.  
           If True, checking will be skipped if the results are PASS and up-to-date.   
         
        """
        pass
    @SkipChecking.setter
    def SkipChecking(self, skipChecking: bool):
        """
        Setter for property: (bool) SkipChecking
         Returns the configuration of skip checking based on result up-to-date status.  
           If True, checking will be skipped if the results are PASS and up-to-date.   
         
        """
        pass
    @property
    def SkipCheckingDontLoadPart(self) -> bool:
        """
        Getter for property: (bool) SkipCheckingDontLoadPart
         Returns the configuration of skipping checking without loading parts   
            
         
        """
        pass
    @SkipCheckingDontLoadPart.setter
    def SkipCheckingDontLoadPart(self, skipCheckingDontLoadPart: bool):
        """
        Setter for property: (bool) SkipCheckingDontLoadPart
         Returns the configuration of skipping checking without loading parts   
            
         
        """
        pass
    @property
    def SkipOverriddenResultOption(self) -> bool:
        """
        Getter for property: (bool) SkipOverriddenResultOption
         Returns  the configuration of skip checking based on result overriden state.  
           If True, checking will be skipped if the results are overridden.   
         
        """
        pass
    @SkipOverriddenResultOption.setter
    def SkipOverriddenResultOption(self, skipOverriddenResult: bool):
        """
        Setter for property: (bool) SkipOverriddenResultOption
         Returns  the configuration of skip checking based on result overriden state.  
           If True, checking will be skipped if the results are overridden.   
         
        """
        pass
    @property
    def StopOnError(self) -> bool:
        """
        Getter for property: (bool) StopOnError
         Returns the configuration of stopping checking process on error status.  
           If True, stop checking when there is checker returned error status.   
         
        """
        pass
    @StopOnError.setter
    def StopOnError(self, stopOnError: bool):
        """
        Setter for property: (bool) StopOnError
         Returns the configuration of stopping checking process on error status.  
           If True, stop checking when there is checker returned error status.   
         
        """
        pass
    @property
    def StopOnWarning(self) -> bool:
        """
        Getter for property: (bool) StopOnWarning
         Returns the configuration of stopping checking on warning status.  
           If True, stop checking when there is checker returned warning status.   
         
        """
        pass
    @StopOnWarning.setter
    def StopOnWarning(self, stop_on_warning: bool):
        """
        Setter for property: (bool) StopOnWarning
         Returns the configuration of stopping checking on warning status.  
           If True, stop checking when there is checker returned warning status.   
         
        """
        pass
    @property
    def TreatWarningAsFail(self) -> bool:
        """
        Getter for property: (bool) TreatWarningAsFail
         Returns the configuration of treating warning status as fail status.  
             
         
        """
        pass
    @TreatWarningAsFail.setter
    def TreatWarningAsFail(self, treatWarningAsFail: bool):
        """
        Setter for property: (bool) TreatWarningAsFail
         Returns the configuration of treating warning status as fail status.  
             
         
        """
        pass
import NXOpen
class Validator(NXOpen.TaggedObject): 
    """Represents a NX NXOpen.Validate.Validator.
    """
    @property
    def ValidatorOptions(self) -> ValidatorOptions:
        """
        Getter for property: ( ValidatorOptions NXOpen.) ValidatorOptions
         Returns the run options.  
             
         
        """
        pass
    def AppendCheckerNode(self, className: str) -> None:
        """
         Adds a checker node.
                
        """
        pass
    def AppendCheckerNodes(self, classNames: List[str]) -> None:
        """
         Adds checker nodes.
                
        """
        pass
    @overload
    def AppendPartNode(self, fileName: str) -> None:
        """
         Adds part node by part file name 
        """
        pass
    @overload
    def AppendPartNode(self, partObject: NXOpen.Part) -> None:
        """
         Adds part node by part object 
        """
        pass
    @overload
    def AppendPartNodes(self, fileNames: List[str]) -> None:
        """
         Adds part nodes by part file names 
        """
        pass
    @overload
    def AppendPartNodes(self, partObject: List[NXOpen.Part]) -> None:
        """
         Adds part nodes by part objects 
        """
        pass
    def ClearCheckerNodes(self) -> None:
        """
         Clears checker nodes 
        """
        pass
    def ClearPartNodes(self) -> None:
        """
         Clears part nodes 
        """
        pass
    def Commit(self) -> NXOpen.Validation.Result:
        """
         Runs checking process and returns the checking status.
                    If failed checking statuses are found, it will return NXOpen.Validation.Result.Failed. 
                    Otherwise it will return NXOpen.Validation.Result.Pass. 
                    Call NXOpen.Validate.Validator.GetLastErrorListFromCommit for the execeptions happened during the checking process.
                
         Returns status ( NXOpen.Validation.Result):  .
        """
        pass
    def EraseCheckerNode(self, del_ndx: int) -> None:
        """
         Removes a checker node.
                
        """
        pass
    def ErasePartNode(self, index: int) -> None:
        """
         Removes a part node 
        """
        pass
    def FindCheckerNode(self, index: int) -> CheckerNode:
        """
         Returns a checker node.
                
         Returns checkerNode ( CheckerNode NXOpen.):  checker node .
        """
        pass
    def FindPartNode(self, index: int) -> PartNode:
        """
         Finds a part node 
         Returns partNode ( PartNode NXOpen.):  .
        """
        pass
    def GetCheckerNodes(self) -> List[CheckerNode]:
        """
         Returns all checker nodes.
                
         Returns checkerNode ( CheckerNode List[NXOpe):  checker name array .
        """
        pass
    def GetLastErrorListFromCommit(self) -> NXOpen.ErrorList:
        """
         Return the list of errors happened during last NXOpen.Validate.Validator.Commit.
                
         Returns errors ( NXOpen.ErrorList):  List of errors encountered during the checking process .
        """
        pass
    def GetPartNodes(self) -> List[PartNode]:
        """
         Returns all part nodes. 
         Returns partNodes ( PartNode List[NXOpe):  .
        """
        pass
import NXOpen
class XmlComparator(NXOpen.Object): 
    """Provides a generic comparator for finding differences between two XML
       format files.
       The comparator takes NXOpen.Validate.XmlComparator.Options to further control the
       comparison process. It returns NXOpen.Validate.XmlComparator.Result, and generates report 
       of detailed differences in HTML file which can be viewed via web browser.
    """
    class Result(Enum):
        """
        Members Include: 
         |Identical|  Represents two xml files are identical 
         |Different|  Represents two xml files are different 

        """
        Identical: int
        Different: int
        @staticmethod
        def ValueOf(value: int) -> XmlComparator.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Options:
        """
           Represents config options in comparison  
                      For example:  
                      case 1: Defines filter file to control what nodes will be compared;
                        generates comparison report and log; ignores CDATA and processing 
                        instruction nodes.  
                         @code compareOptions.ReportFile           = "auto_report.html";
                              compareOptions.FilterFile           = "filter.xml";
                              compareOptions.LogFile              = "log.log";
                              compareOptions.IgnoreNamespaces     = FALSE;
                              compareOptions.IgnoreUnmatchedNodes = FALSE;
                              compareOptions.IgnoreComments       = FALSE;
                              compareOptions.IgnoreCdata          = TRUE;
                              compareOptions.IgnorePI             = TRUE;
                              CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
                         @endcode 
                      case 2: Compares all nodes and does not generate report file and log file.  
                         @code compareOptions.ReportFile           = NULL;
                              compareOptions.FilterFile           = NULL;
                              compareOptions.LogFile              = NULL;
                              CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
                        @endcode 
                
         XmlComparatorOptions_Struct NXOpen. is an alias for  XmlComparator.Options NXOpen..
        """
        @property
        def FilterFile(self) -> str:
            """
            Getter for property FilterFile
            File specification of filter file.

            """
            pass
        @FilterFile.setter
        def FilterFile(self, value: str):
            """
            Getter for property FilterFile
            File specification of filter file.
            Setter for property FilterFile
            File specification of filter file.

            """
            pass
        @property
        def ReportFile(self) -> str:
            """
            Getter for property ReportFile
            File specification of report file.

            """
            pass
        @ReportFile.setter
        def ReportFile(self, value: str):
            """
            Getter for property ReportFile
            File specification of report file.
            Setter for property ReportFile
            File specification of report file.

            """
            pass
        @property
        def LogFile(self) -> str:
            """
            Getter for property LogFile
            File specification of comparison log file.

            """
            pass
        @LogFile.setter
        def LogFile(self, value: str):
            """
            Getter for property LogFile
            File specification of comparison log file.
            Setter for property LogFile
            File specification of comparison log file.

            """
            pass
        @property
        def IgnoreNamespaces(self) -> bool:
            """
            Getter for property IgnoreNamespaces
            Ignores namespace definition during comparison.

            """
            pass
        @IgnoreNamespaces.setter
        def IgnoreNamespaces(self, value: bool):
            """
            Getter for property IgnoreNamespaces
            Ignores namespace definition during comparison.
            Setter for property IgnoreNamespaces
            Ignores namespace definition during comparison.

            """
            pass
        @property
        def IgnoreUnmatchedNodes(self) -> bool:
            """
            Getter for property IgnoreUnmatchedNodes
            Ignores unmatched nodes in comparison.

            """
            pass
        @IgnoreUnmatchedNodes.setter
        def IgnoreUnmatchedNodes(self, value: bool):
            """
            Getter for property IgnoreUnmatchedNodes
            Ignores unmatched nodes in comparison.
            Setter for property IgnoreUnmatchedNodes
            Ignores unmatched nodes in comparison.

            """
            pass
        @property
        def IgnoreComments(self) -> bool:
            """
            Getter for property IgnoreComments
            Ignores comment nodes in comparison.

            """
            pass
        @IgnoreComments.setter
        def IgnoreComments(self, value: bool):
            """
            Getter for property IgnoreComments
            Ignores comment nodes in comparison.
            Setter for property IgnoreComments
            Ignores comment nodes in comparison.

            """
            pass
        @property
        def IgnoreCdata(self) -> bool:
            """
            Getter for property IgnoreCdata
            Ignores CDATA nodes in comparison.

            """
            pass
        @IgnoreCdata.setter
        def IgnoreCdata(self, value: bool):
            """
            Getter for property IgnoreCdata
            Ignores CDATA nodes in comparison.
            Setter for property IgnoreCdata
            Ignores CDATA nodes in comparison.

            """
            pass
        @property
        def IgnorePI(self) -> bool:
            """
            Getter for property IgnorePI
            Ignores processing instruction nodes in comparison.

            """
            pass
        @IgnorePI.setter
        def IgnorePI(self, value: bool):
            """
            Getter for property IgnorePI
            Ignores processing instruction nodes in comparison.
            Setter for property IgnorePI
            Ignores processing instruction nodes in comparison.

            """
            pass
    def CompareXmlFiles(workXmlFile: str, masterXmlFile: str, compareOptions: XmlComparator.Options) -> XmlComparator.Result:
        """
         Compares two xml format files. 
                    You can use NXOpen.Validate.XmlComparator.Optionsto customize the comparison process. 
                
         Returns result ( XmlComparator.Result NXOpen.):  comparison result .
        """
        pass
