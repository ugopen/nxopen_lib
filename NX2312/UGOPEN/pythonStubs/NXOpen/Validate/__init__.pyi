from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##      Represents an NX @link NXOpen::Validate::AnalysisResultCollection NXOpen::Validate::AnalysisResultCollection@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class AnalysisResultCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX <ja_class>NXOpen.Validate.AnalysisResultCollection</ja_class> object.
    """


    ##  Represents the type of Analysis Result 
    ##  Maximum Overhang Analysis Checker Result 
    class AnalysisResultType(Enum):
        """
        Members Include: <MaximumOverhangAngle> <PrintTime> <Overheating>
        """
        MaximumOverhangAngle: int
        PrintTime: int
        Overheating: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisResultCollection.AnalysisResultType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Create a @link NXOpen::Validate::CheckChannelRatioBuilder NXOpen::Validate::CheckChannelRatioBuilder@endlink  
    ##  @return channelRatioBuilder (@link CheckChannelRatioBuilder NXOpen.Validate.CheckChannelRatioBuilder@endlink):  check channel ratio builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckChannelRatioBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckChannelRatioBuilder:
        """
         Create a @link NXOpen::Validate::CheckChannelRatioBuilder NXOpen::Validate::CheckChannelRatioBuilder@endlink  
         @return channelRatioBuilder (@link CheckChannelRatioBuilder NXOpen.Validate.CheckChannelRatioBuilder@endlink):  check channel ratio builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckMaximumOverhangAngleBuilder NXOpen::Validate::CheckMaximumOverhangAngleBuilder@endlink  
    ##  @return overhang_builder (@link CheckMaximumOverhangAngleBuilder NXOpen.Validate.CheckMaximumOverhangAngleBuilder@endlink):  check overhang angle builder .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckMaximumOverhangAngleBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckMaximumOverhangAngleBuilder:
        """
         Create a @link NXOpen::Validate::CheckMaximumOverhangAngleBuilder NXOpen::Validate::CheckMaximumOverhangAngleBuilder@endlink  
         @return overhang_builder (@link CheckMaximumOverhangAngleBuilder NXOpen.Validate.CheckMaximumOverhangAngleBuilder@endlink):  check overhang angle builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckMinimumRadiusBuilder NXOpen::Validate::CheckMinimumRadiusBuilder@endlink  
    ##  @return minimum_radius_builder (@link CheckMinimumRadiusBuilder NXOpen.Validate.CheckMinimumRadiusBuilder@endlink):  check minimum radius builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckMinimumRadiusBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckMinimumRadiusBuilder:
        """
         Create a @link NXOpen::Validate::CheckMinimumRadiusBuilder NXOpen::Validate::CheckMinimumRadiusBuilder@endlink  
         @return minimum_radius_builder (@link CheckMinimumRadiusBuilder NXOpen.Validate.CheckMinimumRadiusBuilder@endlink):  check minimum radius builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckMinimumWallThicknessBuilder NXOpen::Validate::CheckMinimumWallThicknessBuilder@endlink  
    ##  @return wallthickness_builder (@link CheckMinimumWallThicknessBuilder NXOpen.Validate.CheckMinimumWallThicknessBuilder@endlink):  check minimum wall thickness builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckMinimumWallThicknessBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckMinimumWallThicknessBuilder:
        """
         Create a @link NXOpen::Validate::CheckMinimumWallThicknessBuilder NXOpen::Validate::CheckMinimumWallThicknessBuilder@endlink  
         @return wallthickness_builder (@link CheckMinimumWallThicknessBuilder NXOpen.Validate.CheckMinimumWallThicknessBuilder@endlink):  check minimum wall thickness builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckModelWithinPrintableVolumeBuilder NXOpen::Validate::CheckModelWithinPrintableVolumeBuilder@endlink  
    ##  @return check_model_within_printable_volume_builder (@link CheckModelWithinPrintableVolumeBuilder NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder@endlink):  check model within printable volume builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckModelWithinPrintableVolumeBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckModelWithinPrintableVolumeBuilder:
        """
         Create a @link NXOpen::Validate::CheckModelWithinPrintableVolumeBuilder NXOpen::Validate::CheckModelWithinPrintableVolumeBuilder@endlink  
         @return check_model_within_printable_volume_builder (@link CheckModelWithinPrintableVolumeBuilder NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder@endlink):  check model within printable volume builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Validate::CheckOverheatingBuilder NXOpen::Validate::CheckOverheatingBuilder@endlink  
    ##  @return overheatingBuilder (@link CheckOverheatingBuilder NXOpen.Validate.CheckOverheatingBuilder@endlink):  check overheating builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckOverheatingBuilder(owningPart: AnalysisResultCollection, persistentResult: AnalysisResult) -> CheckOverheatingBuilder:
        """
         Creates an object of @link NXOpen::Validate::CheckOverheatingBuilder NXOpen::Validate::CheckOverheatingBuilder@endlink  
         @return overheatingBuilder (@link CheckOverheatingBuilder NXOpen.Validate.CheckOverheatingBuilder@endlink):  check overheating builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Validate::CheckPartOrientationBuilder NXOpen::Validate::CheckPartOrientationBuilder@endlink  
    ##  @return partorientation_builder (@link CheckPartOrientationBuilder NXOpen.Validate.CheckPartOrientationBuilder@endlink):  check part orientation builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckPartOrientationBuilder(owning_part: AnalysisResultCollection, persistent_result: PartOrientationAnalysisResult) -> CheckPartOrientationBuilder:
        """
         Creates an object of @link NXOpen::Validate::CheckPartOrientationBuilder NXOpen::Validate::CheckPartOrientationBuilder@endlink  
         @return partorientation_builder (@link CheckPartOrientationBuilder NXOpen.Validate.CheckPartOrientationBuilder@endlink):  check part orientation builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckPorosityBuilder NXOpen::Validate::CheckPorosityBuilder@endlink  
    ##  @return check_porosity_builder (@link CheckPorosityBuilder NXOpen.Validate.CheckPorosityBuilder@endlink):  check porosity builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckPorosityBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckPorosityBuilder:
        """
         Create a @link NXOpen::Validate::CheckPorosityBuilder NXOpen::Validate::CheckPorosityBuilder@endlink  
         @return check_porosity_builder (@link CheckPorosityBuilder NXOpen.Validate.CheckPorosityBuilder@endlink):  check porosity builder .
        """
        pass
    
    ##  Creates an object of @link NXOpen::Validate::CheckPrintTimeBuilder NXOpen::Validate::CheckPrintTimeBuilder@endlink  
    ##  @return partOrientationBuilder (@link CheckPrintTimeBuilder NXOpen.Validate.CheckPrintTimeBuilder@endlink):  check print time builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckPrintTimeBuilder(owningPart: AnalysisResultCollection, persistentResult: AnalysisResult) -> CheckPrintTimeBuilder:
        """
         Creates an object of @link NXOpen::Validate::CheckPrintTimeBuilder NXOpen::Validate::CheckPrintTimeBuilder@endlink  
         @return partOrientationBuilder (@link CheckPrintTimeBuilder NXOpen.Validate.CheckPrintTimeBuilder@endlink):  check print time builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckTrappedSupportsBuilder NXOpen::Validate::CheckTrappedSupportsBuilder@endlink  
    ##  @return trapped_supports_builder (@link CheckTrappedSupportsBuilder NXOpen.Validate.CheckTrappedSupportsBuilder@endlink):  check trapped supports builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckTrappedSupportsBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckTrappedSupportsBuilder:
        """
         Create a @link NXOpen::Validate::CheckTrappedSupportsBuilder NXOpen::Validate::CheckTrappedSupportsBuilder@endlink  
         @return trapped_supports_builder (@link CheckTrappedSupportsBuilder NXOpen.Validate.CheckTrappedSupportsBuilder@endlink):  check trapped supports builder .
        """
        pass
    
    ##  Create a @link NXOpen::Validate::CheckWhollyEnclosedVolumeBuilder NXOpen::Validate::CheckWhollyEnclosedVolumeBuilder@endlink  
    ##  @return check_wholly_enclosed_volume_builder (@link CheckWhollyEnclosedVolumeBuilder NXOpen.Validate.CheckWhollyEnclosedVolumeBuilder@endlink):  check wholly enclosed volume builder .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  Analysis Result 
    def CreateCheckWhollyEnclosedVolumeBuilder(owning_part: AnalysisResultCollection, persistent_result: AnalysisResult) -> CheckWhollyEnclosedVolumeBuilder:
        """
         Create a @link NXOpen::Validate::CheckWhollyEnclosedVolumeBuilder NXOpen::Validate::CheckWhollyEnclosedVolumeBuilder@endlink  
         @return check_wholly_enclosed_volume_builder (@link CheckWhollyEnclosedVolumeBuilder NXOpen.Validate.CheckWhollyEnclosedVolumeBuilder@endlink):  check wholly enclosed volume builder .
        """
        pass
    
    ##  Hide all analysis result objects. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="analysisResults"> (@link AnalysisResult List[NXOpen.Validate.AnalysisResult]@endlink) </param>
    def DeactivateAll(owning_part: AnalysisResultCollection, analysisResults: List[AnalysisResult]) -> None:
        """
         Hide all analysis result objects. 
        """
        pass
    
    ##  Update all analysis result objects. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="analysisResults"> (@link AnalysisResult List[NXOpen.Validate.AnalysisResult]@endlink) </param>
    def EvaluateAll(owning_part: AnalysisResultCollection, analysisResults: List[AnalysisResult]) -> None:
        """
         Update all analysis result objects. 
        """
        pass
    
    ##  Get all analysis result objects from the work part 
    ##  @return analysisResults (@link AnalysisResult List[NXOpen.Validate.AnalysisResult]@endlink):    .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FindAllAnalysisResults(owning_part: AnalysisResultCollection) -> List[AnalysisResult]:
        """
         Get all analysis result objects from the work part 
         @return analysisResults (@link AnalysisResult List[NXOpen.Validate.AnalysisResult]@endlink):    .
        """
        pass
    
    ##  Get all analysis result objects of desired type from the work part 
    ##  @return analysisResults (@link AnalysisResult List[NXOpen.Validate.AnalysisResult]@endlink):    .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="analysisType"> (@link AnalysisResultCollection.AnalysisResultType NXOpen.Validate.AnalysisResultCollection.AnalysisResultType@endlink) </param>
    def FindAllAnalysisResultsOfType(owning_part: AnalysisResultCollection, analysisType: AnalysisResultCollection.AnalysisResultType) -> List[AnalysisResult]:
        """
         Get all analysis result objects of desired type from the work part 
         @return analysisResults (@link AnalysisResult List[NXOpen.Validate.AnalysisResult]@endlink):    .
        """
        pass
    
    ##  Finds the @link NXOpen::Validate::AnalysisResult NXOpen::Validate::AnalysisResult@endlink  with the given identifier. 
    ##  @return analysisResults (@link AnalysisResult NXOpen.Validate.AnalysisResult@endlink):    .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  The identifier of the @link NXOpen::Validate::AnalysisResult NXOpen::Validate::AnalysisResult@endlink  
    def FindObject(owning_part: AnalysisResultCollection, sid: str) -> AnalysisResult:
        """
         Finds the @link NXOpen::Validate::AnalysisResult NXOpen::Validate::AnalysisResult@endlink  with the given identifier. 
         @return analysisResults (@link AnalysisResult NXOpen.Validate.AnalysisResult@endlink):    .
        """
        pass
    
    ##  Get the value of Analysis Checker Result. Returns 0 if value exist, else return -1 
    ##  @return analysisValue (float):  The analysis result value  .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Analysis Result 
    def GetAnalysisResultValue(owning_part: AnalysisResultCollection, persistentResult: AnalysisResult) -> float:
        """
         Get the value of Analysis Checker Result. Returns 0 if value exist, else return -1 
         @return analysisValue (float):  The analysis result value  .
        """
        pass
    
## 
##      Represents a @link NXOpen::Validate::AnalysisResult NXOpen::Validate::AnalysisResult@endlink  object.
##     
## 
##   <br>  Created in NX1872.0.0  <br> 

class AnalysisResult(PersistentResult): 
    """
     Represents a <ja_class>NXOpen.Validate.AnalysisResult</ja_class> object.
    """


    ## Getter for property: (bool) ActiveStatus
    ##   the result's active status   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def ActiveStatus(self) -> bool:
        """
        Getter for property: (bool) ActiveStatus
          the result's active status   
            
         
        """
        pass
    
    ##  Activate the object. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Activate(analysisResult: AnalysisResult) -> None:
        """
         Activate the object. 
        """
        pass
    
    ##  Deactivate the object. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Deactivate(analysisResult: AnalysisResult) -> None:
        """
         Deactivate the object. 
        """
        pass
    
    ##  Evaluata the object. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Evaluate(analysisResult: AnalysisResult) -> None:
        """
         Evaluata the object. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Check Channel Ratio Builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckChannelRatioBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckChannelRatioBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## FailedSegmentsColor </term> <description> 
##  
## 186 </description> </item> 
## 
## <item><term> 
##  
## MaximumWidth </term> <description> 
##  
## 3.0 (millimeters part), 0.1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumRatio </term> <description> 
##  
## 0.02 (millimeters part), 0.02 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PassedSegmentsColor </term> <description> 
##  
## 36 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## SegmentLength </term> <description> 
##  
## 50.0 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyFailedSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CheckChannelRatioBuilder(NXOpen.Builder): 
    """ Represents a Check Channel Ratio Builder """


    ## 
    ## @link CheckChannelRatioBuilderTableData_Struct NXOpen.Validate.CheckChannelRatioBuilderTableData_Struct@endlink is an alias for @link CheckChannelRatioBuilder.TableData NXOpen.Validate.CheckChannelRatioBuilder.TableData@endlink.
    class TableData:
        """
        
        @link CheckChannelRatioBuilderTableData_Struct NXOpen.Validate.CheckChannelRatioBuilderTableData_Struct@endlink is an alias for @link CheckChannelRatioBuilder.TableData NXOpen.Validate.CheckChannelRatioBuilder.TableData@endlink.
        """
        ## Getter for property :(float) Angle
        ## angle value in table
        ## @return float
        @property
        def Angle(self) -> float:
            """
            Getter for property Angle
            angle value in table

            """
            pass
        
        ## Setter for property :(float) Angle
        @Angle.setter
        def Angle(self, value: float):
            """
            Getter for property Angle
            angle value in table
            Setter for property Angle
            angle value in table

            """
            pass
        
        ## Getter for property :(float) MinimumDiameter
        ## minimum diameter value in table
        ## @return float
        @property
        def MinimumDiameter(self) -> float:
            """
            Getter for property MinimumDiameter
            minimum diameter value in table

            """
            pass
        
        ## Setter for property :(float) MinimumDiameter
        @MinimumDiameter.setter
        def MinimumDiameter(self, value: float):
            """
            Getter for property MinimumDiameter
            minimum diameter value in table
            Setter for property MinimumDiameter
            minimum diameter value in table

            """
            pass
        
    
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedSegmentsColor
    ##   the color for segments with insufficient diameters.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FailedSegmentsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedSegmentsColor
          the color for segments with insufficient diameters.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedSegmentsColor

    ##   the color for segments with insufficient diameters.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FailedSegmentsColor.setter
    def FailedSegmentsColor(self, failedColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FailedSegmentsColor
          the color for segments with insufficient diameters.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaximumWidth
    ##   the maximum width of channel openings   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def MaximumWidth(self) -> float:
        """
        Getter for property: (float) MaximumWidth
          the maximum width of channel openings   
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumWidth

    ##   the maximum width of channel openings   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MaximumWidth.setter
    def MaximumWidth(self, maximumWidth: float):
        """
        Setter for property: (float) MaximumWidth
          the maximum width of channel openings   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumRatio
    ##   the minimum ratio    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def MinimumRatio(self) -> float:
        """
        Getter for property: (float) MinimumRatio
          the minimum ratio    
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumRatio

    ##   the minimum ratio    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MinimumRatio.setter
    def MinimumRatio(self, minimumRatio: float):
        """
        Setter for property: (float) MinimumRatio
          the minimum ratio    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) Orientation
    ##   the draw orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def Orientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) Orientation
          the draw orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) Orientation

    ##   the draw orientation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Orientation.setter
    def Orientation(self, orientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) Orientation
          the draw orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
    ##   the draw origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the draw origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin

    ##   the draw origin   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the draw origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PassedSegmentsColor
    ##   the color for segments with sufficient diameters.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def PassedSegmentsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PassedSegmentsColor
          the color for segments with sufficient diameters.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PassedSegmentsColor

    ##   the color for segments with sufficient diameters.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PassedSegmentsColor.setter
    def PassedSegmentsColor(self, passedColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PassedSegmentsColor
          the color for segments with sufficient diameters.  
             
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) SegmentLength
    ##   the segment length    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def SegmentLength(self) -> float:
        """
        Getter for property: (float) SegmentLength
          the segment length    
            
         
        """
        pass
    
    ## Setter for property: (float) SegmentLength

    ##   the segment length    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SegmentLength.setter
    def SegmentLength(self, segmentLength: float):
        """
        Setter for property: (float) SegmentLength
          the segment length    
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyFailedSegments
    ##   the toggle that show only failed segments   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyFailedSegments(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailedSegments
          the toggle that show only failed segments   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyFailedSegments

    ##   the toggle that show only failed segments   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ShowOnlyFailedSegments.setter
    def ShowOnlyFailedSegments(self, showOnlyFailedSegments: bool):
        """
        Setter for property: (bool) ShowOnlyFailedSegments
          the toggle that show only failed segments   
            
         
        """
        pass
    
    ##  Returns the selected Bodies 
    ##  @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBodies(builder: CheckChannelRatioBuilder) -> List[NXOpen.Body]:
        """
         Returns the selected Bodies 
         @return bodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
        """
        pass
    
    ##  Returns the selected faces 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFaces(builder: CheckChannelRatioBuilder) -> List[NXOpen.Face]:
        """
         Returns the selected faces 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
        """
        pass
    
    ##  Gets angle and minimum diameter pair values. 
    ##  @return tableData (@link CheckChannelRatioBuilder.TableData List[NXOpen.Validate.CheckChannelRatioBuilder.TableData]@endlink):  TableData type values. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTableData(builder: CheckChannelRatioBuilder) -> List[CheckChannelRatioBuilder.TableData]:
        """
         Gets angle and minimum diameter pair values. 
         @return tableData (@link CheckChannelRatioBuilder.TableData List[NXOpen.Validate.CheckChannelRatioBuilder.TableData]@endlink):  TableData type values. .
        """
        pass
    
    ##  Set the Bodies 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The objects to apply the attributes to. 
    def SetBodies(builder: CheckChannelRatioBuilder, bodies: List[NXOpen.Body]) -> None:
        """
         Set the Bodies 
        """
        pass
    
    ##  Set the selected faces 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The objects to apply the attributes to. 
    def SetFaces(builder: CheckChannelRatioBuilder, faces: List[NXOpen.Face]) -> None:
        """
         Set the selected faces 
        """
        pass
    
    ##  Sets the needRegenerateFacets toggle 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="needRegenerateFacets"> (bool) </param>
    def SetNeedRegenerateFacets(builder: CheckChannelRatioBuilder, needRegenerateFacets: bool) -> None:
        """
         Sets the needRegenerateFacets toggle 
        """
        pass
    
    ##  Sets angle and minimum diameter pair values. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  TableData type values. 
    def SetTableData(builder: CheckChannelRatioBuilder, tableData: List[CheckChannelRatioBuilder.TableData]) -> None:
        """
         Sets angle and minimum diameter pair values. 
        """
        pass
    
import NXOpen
##   @brief Defines a Validate Checker. 
## 
##  
##       <br> Checker definition contains the information of checker class name, checker parameter values 
##      and call back functions and so on. These information is used to create checker instance for customization
##      of parameters and execution of the check logic. <br> 
##      <br> To create a new instance of this class, use @link NXOpen::Validate::ValidationManager::CreateCheckerDefinition  NXOpen::Validate::ValidationManager::CreateCheckerDefinition @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckerDefinition(NXOpen.TransientObject): 
    """ <summary>Defines a Validate Checker.</summary>
     <para>Checker definition contains the information of checker class name, checker parameter values 
     and call back functions and so on. These information is used to create checker instance for customization
     of parameters and execution of the check logic.</para>
    """


    ## Getter for property: (bool) InteractiveCheckingOnly
    ##   the interactiveCheckingOnly status of the checker.  
    ##   
    ##             Indicates whether or not to execute the checker only in the NX interactive mode.
    ##             When it is true, the checker will not be executed in the ug_check_part batch mode.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def InteractiveCheckingOnly(self) -> bool:
        """
        Getter for property: (bool) InteractiveCheckingOnly
          the interactiveCheckingOnly status of the checker.  
          
                    Indicates whether or not to execute the checker only in the NX interactive mode.
                    When it is true, the checker will not be executed in the ug_check_part batch mode.
                  
         
        """
        pass
    
    ## Setter for property: (bool) InteractiveCheckingOnly

    ##   the interactiveCheckingOnly status of the checker.  
    ##   
    ##             Indicates whether or not to execute the checker only in the NX interactive mode.
    ##             When it is true, the checker will not be executed in the ug_check_part batch mode.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @InteractiveCheckingOnly.setter
    def InteractiveCheckingOnly(self, interactiveCheckingOnly: bool):
        """
        Setter for property: (bool) InteractiveCheckingOnly
          the interactiveCheckingOnly status of the checker.  
          
                    Indicates whether or not to execute the checker only in the NX interactive mode.
                    When it is true, the checker will not be executed in the ug_check_part batch mode.
                  
         
        """
        pass
    
    ##  User defined method that is called when Check-Mate customizes a checker instance.
    ## A callback definition with the following input arguments: 
    ##  - @link CheckerNode NXOpen.Validate.CheckerNode@endlink
    ##  and no return type
    CustomizationHandler = Callable[[CheckerNode], None]
    
    
    ##  Frees resources associated with the instance.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(checkerDefinition: CheckerDefinition) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
    
    ##  User defined method that is called when Check-Mate shows checker document.
    ## A callback definition with the following input arguments: 
    ##  - @link CheckerNode NXOpen.Validate.CheckerNode@endlink
    ##  and no return type
    DocumentationHandler = Callable[[CheckerNode], None]
    
    
    ##  Sets checker customization handler 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="customize"> (@link CheckerDefinition.CustomizationHandler NXOpen.Validate.CheckerDefinition.CustomizationHandler@endlink) </param>
    def SetCustomizationHandler(checkerDefinition: CheckerDefinition, customize: CheckerDefinition.CustomizationHandler) -> None:
        """
         Sets checker customization handler 
        """
        pass
    
    ##  Sets checker document handler 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="document"> (@link CheckerDefinition.DocumentationHandler NXOpen.Validate.CheckerDefinition.DocumentationHandler@endlink) </param>
    def SetDocumentationHandler(checkerDefinition: CheckerDefinition, document: CheckerDefinition.DocumentationHandler) -> None:
        """
         Sets checker document handler 
        """
        pass
    
import NXOpen
##   @brief Represents a checker that validator will use to check against part node.  
## 
##  
##       <br> Checker node contains the information of checker class name and checker parameter attribute values. 
##      If the checker class is a profile which contains child checker instances, you can set the enable flags to
##      the child checker instances in the profile checker class to turn on or off the child checker instances. <br> 
##     
## 
##   <br>  Created in NX7.5.0  <br> 

class CheckerNode(NXOpen.TransientObject): 
    """ <summary>Represents a checker that validator will use to check against part node. </summary>
     <para>Checker node contains the information of checker class name and checker parameter attribute values. 
     If the checker class is a profile which contains child checker instances, you can set the enable flags to
     the child checker instances in the profile checker class to turn on or off the child checker instances.</para>
    """


    ## Getter for property: (str) AttributeCustomizedFormulas
    ##   the customized formula lines of checker.  
    ##   
    ##          <br> For example: <br> 
    ##          <br> "Disabled?;False;save_log_in_part;True" <br> 
    ##          <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def AttributeCustomizedFormulas(self) -> str:
        """
        Getter for property: (str) AttributeCustomizedFormulas
          the customized formula lines of checker.  
          
                 <br> For example: <br> 
                 <br> "Disabled?;False;save_log_in_part;True" <br> 
                 <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
                  
         
        """
        pass
    
    ## Setter for property: (str) AttributeCustomizedFormulas

    ##   the customized formula lines of checker.  
    ##   
    ##          <br> For example: <br> 
    ##          <br> "Disabled?;False;save_log_in_part;True" <br> 
    ##          <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AttributeCustomizedFormulas.setter
    def AttributeCustomizedFormulas(self, formulaLines: str):
        """
        Setter for property: (str) AttributeCustomizedFormulas
          the customized formula lines of checker.  
          
                 <br> For example: <br> 
                 <br> "Disabled?;False;save_log_in_part;True" <br> 
                 <br> For more information, see the Knowledge Fusion and NX Open section of the Knowledge Fusion Help. <br> 
                  
         
        """
        pass
    
    ## Getter for property: (str) ClassName
    ##   the checker class name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
          the checker class name   
            
         
        """
        pass
    
    ## Setter for property: (str) ClassName

    ##   the checker class name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ClassName.setter
    def ClassName(self, className: str):
        """
        Setter for property: (str) ClassName
          the checker class name   
            
         
        """
        pass
    
    ##   @brief 
    ##         Asks the @link Validate::Logger Validate::Logger@endlink  instance designated to the @link Validate::CheckerNode Validate::CheckerNode@endlink .
    ##          
    ## 
    ##  
    ##         
    ##         To obtain an instance of @link Validate::CheckerNode Validate::CheckerNode@endlink , refer to @link Validate::Validator::AppendCheckerNode Validate::Validator::AppendCheckerNode@endlink .
    ##         
    ##         
    ##  @return logger (@link Logger NXOpen.Validate.Logger@endlink):  The logger to log result.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskLogger(checkerNode: CheckerNode) -> Logger:
        """
          @brief 
                Asks the @link Validate::Logger Validate::Logger@endlink  instance designated to the @link Validate::CheckerNode Validate::CheckerNode@endlink .
                 
        
         
                
                To obtain an instance of @link Validate::CheckerNode Validate::CheckerNode@endlink , refer to @link Validate::Validator::AppendCheckerNode Validate::Validator::AppendCheckerNode@endlink .
                
                
         @return logger (@link Logger NXOpen.Validate.Logger@endlink):  The logger to log result.
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets enable flag of child checker instance in a profile checker. 
    ##  @return enableFlag (bool):  The enable flag of child checker in the profile checker. .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The instance name of child checker in the profile checker 
    def GetChildCheckerEnabledFlag(checkerNode: CheckerNode, childCheckerInstance: str) -> bool:
        """
         Gets enable flag of child checker instance in a profile checker. 
         @return enableFlag (bool):  The enable flag of child checker in the profile checker. .
        """
        pass
    
    ##  Gets child checker instance names and enable flags in a profile checker. 
    ##  @return A tuple consisting of (enableFlags, childCheckerInstances). 
    ##  - enableFlags is: List[bool]. The enable flags of child checkers in the profile checker .
    ##  - childCheckerInstances is: List[str]. The instance names of child checkers in the profile checker .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetChildCheckerEnabledFlags(checkerNode: CheckerNode) -> Tuple[List[bool], List[str]]:
        """
         Gets child checker instance names and enable flags in a profile checker. 
         @return A tuple consisting of (enableFlags, childCheckerInstances). 
         - enableFlags is: List[bool]. The enable flags of child checkers in the profile checker .
         - childCheckerInstances is: List[str]. The instance names of child checkers in the profile checker .

        """
        pass
    
    ##  Gets child checker instance names in a profile checker. 
    ##  @return childCheckerInstances (List[str]):  The instance names of child checkers in the profile checker .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetChildCheckerInstanceNames(checkerNode: CheckerNode) -> List[str]:
        """
         Gets child checker instance names in a profile checker. 
         @return childCheckerInstances (List[str]):  The instance names of child checkers in the profile checker .
        """
        pass
    
    ##  Gets a @link Validate::Parameter Validate::Parameter@endlink  of specified title.<br/>
    ##         A parameter can be customized using methods like @link Validate::Parameter::SetBooleanValue Validate::Parameter::SetBooleanValue@endlink ,
    ##         @link Validate::Parameter::SetIntValue Validate::Parameter::SetIntValue@endlink , @link Validate::Parameter::SetDoubleValue Validate::Parameter::SetDoubleValue@endlink ,
    ##         @link Validate::Parameter::SetStringValue Validate::Parameter::SetStringValue@endlink , etc.
    ##         
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parameterTitle"> (str) </param>
    def GetParameter(checkerNode: CheckerNode, parameterTitle: str) -> Parameter:
        """
         Gets a @link Validate::Parameter Validate::Parameter@endlink  of specified title.<br/>
                A parameter can be customized using methods like @link Validate::Parameter::SetBooleanValue Validate::Parameter::SetBooleanValue@endlink ,
                @link Validate::Parameter::SetIntValue Validate::Parameter::SetIntValue@endlink , @link Validate::Parameter::SetDoubleValue Validate::Parameter::SetDoubleValue@endlink ,
                @link Validate::Parameter::SetStringValue Validate::Parameter::SetStringValue@endlink , etc.
                
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink): .
        """
        pass
    
    ##  Gets all the @link Validate::Parameter Validate::Parameter@endlink . 
    ##  @return parameters (@link Parameter List[NXOpen.Validate.Parameter]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetParameters(checkerNode: CheckerNode) -> List[Parameter]:
        """
         Gets all the @link Validate::Parameter Validate::Parameter@endlink . 
         @return parameters (@link Parameter List[NXOpen.Validate.Parameter]@endlink): .
        """
        pass
    
    ##  Sets enable flag of child checker instance in a profile checker. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The instance name of child checker in the profile checker 
    def SetChildCheckerEnabledFlag(checkerNode: CheckerNode, childCheckerInstance: str, enableFlag: bool) -> None:
        """
         Sets enable flag of child checker instance in a profile checker. 
        """
        pass
    
    ##  Sets child checker enable flags in a profile checker. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  The instance names of child checkers in the profile checker 
    def SetChildCheckerEnabledFlags(checkerNode: CheckerNode, childCheckerInstances: List[str], enableFlags: List[bool]) -> None:
        """
         Sets child checker enable flags in a profile checker. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Check Maximum Overhang Angle builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckMaximumOverhangAngleBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckMaximumOverhangAngleBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Angle </term> <description> 
##  
## 45 </description> </item> 
## 
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## ExceedExtendToleranceColor </term> <description> 
##  
## 186 </description> </item> 
## 
## <item><term> 
##  
## ExtendedAngularTolerance </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LessThanMaxAngleColor </term> <description> 
##  
## 36 </description> </item> 
## 
## <item><term> 
##  
## MoreThanMaxAngleColor </term> <description> 
##  
## 6 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyExceedingOverhangAngles (deprecated) </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyFailArea </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1872.0.0  <br> 

class CheckMaximumOverhangAngleBuilder(NXOpen.Builder): 
    """ Represents a Check Maximum Overhang Angle builder """


    ## Getter for property: (float) Angle
    ##   the Maximum Angle    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return float
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
          the Maximum Angle    
            
         
        """
        pass
    
    ## Setter for property: (float) Angle

    ##   the Maximum Angle    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
          the Maximum Angle    
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the toggle that automatic update   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the toggle that automatic update   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the toggle that automatic update   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the toggle that automatic update   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
    ##   the draw orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation @endlink   <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
          the draw orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation

    ##   the draw orientation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrientation @endlink   <br> 

    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
          the draw orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
    ##   the draw origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin @endlink   <br> 

    ## @return NXOpen.Point3d
    @property
    def DrawOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
          the draw origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin

    ##   the draw origin   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin   NXOpen::Validate::SelectionAndPlacementBuilder::DrawOrigin @endlink   <br> 

    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
          the draw origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ExceedExtendToleranceColor
    ##   the Exceed Extend Tol color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ExceedExtendToleranceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ExceedExtendToleranceColor
          the Exceed Extend Tol color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ExceedExtendToleranceColor

    ##   the Exceed Extend Tol color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ExceedExtendToleranceColor.setter
    def ExceedExtendToleranceColor(self, exceedExtendTolColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ExceedExtendToleranceColor
          the Exceed Extend Tol color   
            
         
        """
        pass
    
    ## Getter for property: (float) ExtendedAngularTolerance
    ##   the Extended Angular Tol    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return float
    @property
    def ExtendedAngularTolerance(self) -> float:
        """
        Getter for property: (float) ExtendedAngularTolerance
          the Extended Angular Tol    
            
         
        """
        pass
    
    ## Setter for property: (float) ExtendedAngularTolerance

    ##   the Extended Angular Tol    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ExtendedAngularTolerance.setter
    def ExtendedAngularTolerance(self, extendedAngularTol: float):
        """
        Setter for property: (float) ExtendedAngularTolerance
          the Extended Angular Tol    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMaxAngleColor
    ##   the Less Than Max Angle Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def LessThanMaxAngleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMaxAngleColor
          the Less Than Max Angle Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMaxAngleColor

    ##   the Less Than Max Angle Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @LessThanMaxAngleColor.setter
    def LessThanMaxAngleColor(self, nLessThanMaxAngleColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMaxAngleColor
          the Less Than Max Angle Color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMaxAngleColor
    ##   the More Than Max Angle Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def MoreThanMaxAngleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMaxAngleColor
          the More Than Max Angle Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMaxAngleColor

    ##   the More Than Max Angle Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @MoreThanMaxAngleColor.setter
    def MoreThanMaxAngleColor(self, moreThanMaxAngleColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMaxAngleColor
          the More Than Max Angle Color   
            
         
        """
        pass
    
    ## Getter for property: (float) OverhangArea
    ##   the area that need to support   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return float
    @property
    def OverhangArea(self) -> float:
        """
        Getter for property: (float) OverhangArea
          the area that need to support   
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the toggle that preview block   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the toggle that preview block   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the toggle that preview block   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the toggle that preview block   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyExceedingOverhangAngles
    ##   the property will be deprecated.  
    ##    use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea.  <br> 

    ## @return bool
    @property
    def ShowOnlyExceedingOverhangAngles(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyExceedingOverhangAngles
          the property will be deprecated.  
           use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead.   
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyExceedingOverhangAngles

    ##   the property will be deprecated.  
    ##    use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_set_OnlyShowFailArea.  <br> 

    @ShowOnlyExceedingOverhangAngles.setter
    def ShowOnlyExceedingOverhangAngles(self, showOnlyExceed: bool):
        """
        Setter for property: (bool) ShowOnlyExceedingOverhangAngles
          the property will be deprecated.  
           use JA_VALIDATE_CHECK_MAXIMUM_OVERHANG_ANGLE_BUILDER_get_OnlyShowFailArea instead.   
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyFailArea
    ##   the toggle that show only Exceeding Overhang Angles   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
          the toggle that show only Exceeding Overhang Angles   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyFailArea

    ##   the toggle that show only Exceeding Overhang Angles   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
          the toggle that show only Exceeding Overhang Angles   
            
         
        """
        pass
    
    ##  Returns the selected Bodies or Parts
    ##  @return targets (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::GetTargets   NXOpen::Validate::SelectionAndPlacementBuilder::GetTargets @endlink   <br> 

    ## License requirements: None.
    @staticmethod
    def GetTargets(builder: CheckMaximumOverhangAngleBuilder) -> List[NXOpen.Body]:
        """
         Returns the selected Bodies or Parts
         @return targets (@link NXOpen.Body List[NXOpen.Body]@endlink):  .
        """
        pass
    
    ##  Set the Bodies or Parts 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Use @link  NXOpen::Validate::SelectionAndPlacementBuilder::SetTargets   NXOpen::Validate::SelectionAndPlacementBuilder::SetTargets @endlink   <br> 

    ## License requirements: None.
    ##  The objects to apply the attributes to. 
    def SetTargets(builder: CheckMaximumOverhangAngleBuilder, targets: List[NXOpen.Body]) -> None:
        """
         Set the Bodies or Parts 
        """
        pass
    
    ##  Update the checker 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Update(builder: CheckMaximumOverhangAngleBuilder) -> None:
        """
         Update the checker 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Check Minimum Radius builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckMinimumRadiusBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckMinimumRadiusBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## ExcludeConvex </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LessThanMinimumRadiusColor </term> <description> 
##  
## 186 </description> </item> 
## 
## <item><term> 
##  
## MinimumRadius </term> <description> 
##  
## 0.5 (millimeters part), 0.02 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MoreThanMinimumRadiusColor </term> <description> 
##  
## 36 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyFailArea </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckMinimumRadiusBuilder(NXOpen.Builder): 
    """ Represents a Check Minimum Radius builder """


    ##  Represents the curvature type 
    ##  3D Minimum 
    class CurvatureTypes(Enum):
        """
        Members Include: <Radius> <Sectional>
        """
        Radius: int
        Sectional: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CheckMinimumRadiusBuilder.CurvatureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.Validate.CheckMinimumRadiusBuilder.CurvatureTypes@endlink) CurvatureType
    ##   the curvature type to compute and display.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CheckMinimumRadiusBuilder.CurvatureTypes
    @property
    def CurvatureType(self) -> CheckMinimumRadiusBuilder.CurvatureTypes:
        """
        Getter for property: (@link CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.Validate.CheckMinimumRadiusBuilder.CurvatureTypes@endlink) CurvatureType
          the curvature type to compute and display.  
            
         
        """
        pass
    
    ## Setter for property: (@link CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.Validate.CheckMinimumRadiusBuilder.CurvatureTypes@endlink) CurvatureType

    ##   the curvature type to compute and display.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CurvatureType.setter
    def CurvatureType(self, curvatureType: CheckMinimumRadiusBuilder.CurvatureTypes):
        """
        Setter for property: (@link CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.Validate.CheckMinimumRadiusBuilder.CurvatureTypes@endlink) CurvatureType
          the curvature type to compute and display.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExcludeConvex
    ##   the Exclude Convex    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ExcludeConvex(self) -> bool:
        """
        Getter for property: (bool) ExcludeConvex
          the Exclude Convex    
            
         
        """
        pass
    
    ## Setter for property: (bool) ExcludeConvex

    ##   the Exclude Convex    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ExcludeConvex.setter
    def ExcludeConvex(self, excludeConvex: bool):
        """
        Setter for property: (bool) ExcludeConvex
          the Exclude Convex    
            
         
        """
        pass
    
    ## Getter for property: (float) FailureArea
    ##   the area where radius is less than the minimum radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def FailureArea(self) -> float:
        """
        Getter for property: (float) FailureArea
          the area where radius is less than the minimum radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinimumRadiusColor
    ##   the Less Than Minimum Radius Color  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def LessThanMinimumRadiusColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinimumRadiusColor
          the Less Than Minimum Radius Color  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinimumRadiusColor

    ##   the Less Than Minimum Radius Color  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LessThanMinimumRadiusColor.setter
    def LessThanMinimumRadiusColor(self, lessThanMinimumRadiusColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinimumRadiusColor
          the Less Than Minimum Radius Color  
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumRadius
    ##   the Minimum Radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def MinimumRadius(self) -> float:
        """
        Getter for property: (float) MinimumRadius
          the Minimum Radius   
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumRadius

    ##   the Minimum Radius   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MinimumRadius.setter
    def MinimumRadius(self, minimumRadius: float):
        """
        Setter for property: (float) MinimumRadius
          the Minimum Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinimumRadiusColor
    ##   the More Than Minimum Radius Color  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def MoreThanMinimumRadiusColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinimumRadiusColor
          the More Than Minimum Radius Color  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinimumRadiusColor

    ##   the More Than Minimum Radius Color  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MoreThanMinimumRadiusColor.setter
    def MoreThanMinimumRadiusColor(self, moreThanMinimumRadiusColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinimumRadiusColor
          the More Than Minimum Radius Color  
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyFailArea
    ##   the show only less than minimum radius toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
          the show only less than minimum radius toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyFailArea

    ##   the show only less than minimum radius toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
          the show only less than minimum radius toggle   
            
         
        """
        pass
    
    ##  Returns the dynamic result 
    ##  @return minimumRadius (float):  The minimum radius evaluated .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The specified face 
    def GetDynamicResult(builder: CheckMinimumRadiusBuilder, selectedFace: NXOpen.Face, dynamicPnt: NXOpen.Point3d) -> float:
        """
         Returns the dynamic result 
         @return minimumRadius (float):  The minimum radius evaluated .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Check Minimum Wall Thickness builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckMinimumWallThicknessBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckMinimumWallThicknessBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## LessThanMinThicknessColor </term> <description> 
##  
## 186 </description> </item> 
## 
## <item><term> 
##  
## MoreThanMinThicknessColor </term> <description> 
##  
## 36 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyFailArea </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Thickness </term> <description> 
##  
## 0.4 (millimeters part), 0.015 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckMinimumWallThicknessBuilder(NXOpen.Builder): 
    """ Represents a Check Minimum Wall Thickness builder """


    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (float) FailureArea
    ##   the area where wall thickness is less than the minimum wall thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def FailureArea(self) -> float:
        """
        Getter for property: (float) FailureArea
          the area where wall thickness is less than the minimum wall thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinThicknessColor
    ##   the Less Than Min Thickness Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def LessThanMinThicknessColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinThicknessColor
          the Less Than Min Thickness Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinThicknessColor

    ##   the Less Than Min Thickness Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @LessThanMinThicknessColor.setter
    def LessThanMinThicknessColor(self, lessThanMinThicknessColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) LessThanMinThicknessColor
          the Less Than Min Thickness Color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinThicknessColor
    ##   the More Than Min Thickness Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def MoreThanMinThicknessColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinThicknessColor
          the More Than Min Thickness Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinThicknessColor

    ##   the More Than Min Thickness Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @MoreThanMinThicknessColor.setter
    def MoreThanMinThicknessColor(self, moreThanMinThicknessColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) MoreThanMinThicknessColor
          the More Than Min Thickness Color   
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyFailArea
    ##   the show only less than min thickness toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
          the show only less than min thickness toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyFailArea

    ##   the show only less than min thickness toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
          the show only less than min thickness toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) Thickness
    ##   the minimum thickness    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
          the minimum thickness    
            
         
        """
        pass
    
    ## Setter for property: (float) Thickness

    ##   the minimum thickness    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
          the minimum thickness    
            
         
        """
        pass
    
    ##  Returns the dynamic result 
    ##  @return A tuple consisting of (valid, thickness, direction, closestPnt). 
    ##  - valid is: bool. The thickness is valid or not .
    ##  - thickness is: float. The thickness evaluated .
    ##  - direction is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. The normal of closest element .
    ##  - closestPnt is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The closest point on the specified face .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The specified face 
    @staticmethod
    def GetDynamicResult(builder: CheckMinimumWallThicknessBuilder, selectedFace: NXOpen.Face, dynamicPnt: NXOpen.Point3d) -> Tuple[bool, float, NXOpen.Vector3d, NXOpen.Point3d]:
        """
         Returns the dynamic result 
         @return A tuple consisting of (valid, thickness, direction, closestPnt). 
         - valid is: bool. The thickness is valid or not .
         - thickness is: float. The thickness evaluated .
         - direction is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. The normal of closest element .
         - closestPnt is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The closest point on the specified face .

        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Validate::CheckModelWithinPrintableVolumeBuilder NXOpen::Validate::CheckModelWithinPrintableVolumeBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckModelWithinPrintableVolumeBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckModelWithinPrintableVolumeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CloseToPrintableVolumeColor </term> <description> 
##  
## 6 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## DistanceTolerance </term> <description> 
##  
## 1.0 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OutOfPrintableVolumeColor </term> <description> 
##  
## 186 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## PrinterDiameter </term> <description> 
##  
## 200.0 (millimeters part), 8.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PrinterHeight </term> <description> 
##  
## 200.0 (millimeters part), 8.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PrinterLength </term> <description> 
##  
## 200.0 (millimeters part), 8.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PrinterWidth </term> <description> 
##  
## 200.0 (millimeters part), 8.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## WithinPrintableVolumeColor </term> <description> 
##  
## 36 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckModelWithinPrintableVolumeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder</ja_class> """


    ##  Represents the printer shape type 
    ##  printer volume shape is block 
    class PrinterShapeTypes(Enum):
        """
        Members Include: <Block> <Cylinder>
        """
        Block: int
        Cylinder: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the show type 
    ##  show type is printer 
    class ShowTypes(Enum):
        """
        Members Include: <Printer> <Product> <Both>
        """
        Printer: int
        Product: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CheckModelWithinPrintableVolumeBuilder.ShowTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CloseToPrintableVolumeColor
    ##   the Close to Printable Volume Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def CloseToPrintableVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CloseToPrintableVolumeColor
          the Close to Printable Volume Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CloseToPrintableVolumeColor

    ##   the Close to Printable Volume Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CloseToPrintableVolumeColor.setter
    def CloseToPrintableVolumeColor(self, closetoPrintableVolumeColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) CloseToPrintableVolumeColor
          the Close to Printable Volume Color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##   the distance tolerance used to check the product bounding box and the printer bounding box   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
          the distance tolerance used to check the product bounding box and the printer bounding box   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##   the distance tolerance used to check the product bounding box and the printer bounding box   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
          the distance tolerance used to check the product bounding box and the printer bounding box   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutOfPrintableVolumeColor
    ##   the Out Of Printable Volume Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OutOfPrintableVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutOfPrintableVolumeColor
          the Out Of Printable Volume Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutOfPrintableVolumeColor

    ##   the Out Of Printable Volume Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OutOfPrintableVolumeColor.setter
    def OutOfPrintableVolumeColor(self, outOfPrintableVolumeColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutOfPrintableVolumeColor
          the Out Of Printable Volume Color   
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) PrinterDiameter
    ##   the printer diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def PrinterDiameter(self) -> float:
        """
        Getter for property: (float) PrinterDiameter
          the printer diameter   
            
         
        """
        pass
    
    ## Setter for property: (float) PrinterDiameter

    ##   the printer diameter   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterDiameter.setter
    def PrinterDiameter(self, printerDiameter: float):
        """
        Setter for property: (float) PrinterDiameter
          the printer diameter   
            
         
        """
        pass
    
    ## Getter for property: (float) PrinterHeight
    ##   the printer height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def PrinterHeight(self) -> float:
        """
        Getter for property: (float) PrinterHeight
          the printer height   
            
         
        """
        pass
    
    ## Setter for property: (float) PrinterHeight

    ##   the printer height   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterHeight.setter
    def PrinterHeight(self, printerHeight: float):
        """
        Setter for property: (float) PrinterHeight
          the printer height   
            
         
        """
        pass
    
    ## Getter for property: (float) PrinterLength
    ##   the printer length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def PrinterLength(self) -> float:
        """
        Getter for property: (float) PrinterLength
          the printer length   
            
         
        """
        pass
    
    ## Setter for property: (float) PrinterLength

    ##   the printer length   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterLength.setter
    def PrinterLength(self, printerLength: float):
        """
        Setter for property: (float) PrinterLength
          the printer length   
            
         
        """
        pass
    
    ## Getter for property: (str) PrinterName
    ##   the printer name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def PrinterName(self) -> str:
        """
        Getter for property: (str) PrinterName
          the printer name   
            
         
        """
        pass
    
    ## Setter for property: (str) PrinterName

    ##   the printer name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterName.setter
    def PrinterName(self, printerName: str):
        """
        Setter for property: (str) PrinterName
          the printer name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) PrinterOrientation
    ##   the printer orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def PrinterOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) PrinterOrientation
          the printer orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) PrinterOrientation

    ##   the printer orientation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterOrientation.setter
    def PrinterOrientation(self, printerOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) PrinterOrientation
          the printer orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PrinterOrigin
    ##   the printer origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PrinterOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PrinterOrigin
          the printer origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PrinterOrigin

    ##   the printer origin   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterOrigin.setter
    def PrinterOrigin(self, printerOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PrinterOrigin
          the printer origin   
            
         
        """
        pass
    
    ## Getter for property: (@link CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes@endlink) PrinterShapeType
    ##   the shape type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes
    @property
    def PrinterShapeType(self) -> CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes:
        """
        Getter for property: (@link CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes@endlink) PrinterShapeType
          the shape type   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes@endlink) PrinterShapeType

    ##   the shape type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterShapeType.setter
    def PrinterShapeType(self, printerShapeType: CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes):
        """
        Setter for property: (@link CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes@endlink) PrinterShapeType
          the shape type   
            
         
        """
        pass
    
    ## Getter for property: (float) PrinterWidth
    ##   the printer width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def PrinterWidth(self) -> float:
        """
        Getter for property: (float) PrinterWidth
          the printer width   
            
         
        """
        pass
    
    ## Setter for property: (float) PrinterWidth

    ##   the printer width   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PrinterWidth.setter
    def PrinterWidth(self, printerWidth: float):
        """
        Setter for property: (float) PrinterWidth
          the printer width   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (@link CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.ShowTypes@endlink) ShowType
    ##   the show type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CheckModelWithinPrintableVolumeBuilder.ShowTypes
    @property
    def ShowType(self) -> CheckModelWithinPrintableVolumeBuilder.ShowTypes:
        """
        Getter for property: (@link CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.ShowTypes@endlink) ShowType
          the show type   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.ShowTypes@endlink) ShowType

    ##   the show type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowType.setter
    def ShowType(self, showType: CheckModelWithinPrintableVolumeBuilder.ShowTypes):
        """
        Setter for property: (@link CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.ShowTypes@endlink) ShowType
          the show type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WithinPrintableVolumeColor
    ##   the Within Printable Volume Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def WithinPrintableVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WithinPrintableVolumeColor
          the Within Printable Volume Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WithinPrintableVolumeColor

    ##   the Within Printable Volume Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WithinPrintableVolumeColor.setter
    def WithinPrintableVolumeColor(self, withinPrintableVolumeColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WithinPrintableVolumeColor
          the Within Printable Volume Color   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Check Overheating builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckOverheatingBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckOverheatingBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## MaximumOverhangAngle.Value </term> <description> 
##  
## 60 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyOverheatingAreas </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckOverheatingBuilder(NXOpen.Builder): 
    """ Represents a Check Overheating builder """


    ## Getter for property: (bool) AutomaticUpdate
    ##   the toggle that automatic update   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the toggle that automatic update   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the toggle that automatic update   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the toggle that automatic update   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumOverhangAngle
    ##   the Maximum Overhang Angle    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumOverhangAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumOverhangAngle
          the Maximum Overhang Angle    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonOverheatingColor
    ##   the Less Than Max Overhang Angle Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def NonOverheatingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonOverheatingColor
          the Less Than Max Overhang Angle Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonOverheatingColor

    ##   the Less Than Max Overhang Angle Color   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @NonOverheatingColor.setter
    def NonOverheatingColor(self, nonOverHeatingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonOverheatingColor
          the Less Than Max Overhang Angle Color   
            
         
        """
        pass
    
    ## Getter for property: (float) OverheatingArea
    ##   the area that will overheat   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def OverheatingArea(self) -> float:
        """
        Getter for property: (float) OverheatingArea
          the area that will overheat   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverheatingColor
    ##   the More than Max Overhang Angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OverheatingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverheatingColor
          the More than Max Overhang Angle   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverheatingColor

    ##   the More than Max Overhang Angle   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OverheatingColor.setter
    def OverheatingColor(self, overheatingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverheatingColor
          the More than Max Overhang Angle   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyOverheatingAreas
    ##   the toggle that show only Overheating Areas   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyOverheatingAreas(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyOverheatingAreas
          the toggle that show only Overheating Areas   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyOverheatingAreas

    ##   the toggle that show only Overheating Areas   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowOnlyOverheatingAreas.setter
    def ShowOnlyOverheatingAreas(self, showOnlyOverheat: bool):
        """
        Setter for property: (bool) ShowOnlyOverheatingAreas
          the toggle that show only Overheating Areas   
            
         
        """
        pass
    
    ##  Update the checker 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def Update(builder: CheckOverheatingBuilder) -> None:
        """
         Update the checker 
        """
        pass
    
import NXOpen
##  Represents a @link Validate::PartOrientationAnalysisResult Validate::PartOrientationAnalysisResult@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckPartOrientationBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckPartOrientationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Accuracy </term> <description> 
##  
## Medium </description> </item> 
## 
## <item><term> 
##  
## FDMPrintTimeParameter.LayerThickness.Value </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FDMPrintTimeParameter.NozzleDiameter.Value </term> <description> 
##  
## 0.5 (millimeters part), 0.025 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FDMPrintTimeParameter.TravelSpeed.Value </term> <description> 
##  
## 150.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MJFPrintTimeParameter.LayerPrintTime.Value </term> <description> 
##  
## 30.0 (millimeters part), 30.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MJFPrintTimeParameter.LayerThickness.Value </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaxOverhangAngleForOverHeating.Value </term> <description> 
##  
## 60.0 </description> </item> 
## 
## <item><term> 
##  
## MaxOverhangAngleForVolume.Value </term> <description> 
##  
## 45.0 </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.HatchSpacing.Value </term> <description> 
##  
## 1.0 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.IslandLength.Value </term> <description> 
##  
## 10.0 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.LayerThickness.Value </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.RecoatingTime.Value </term> <description> 
##  
## 5.0 (millimeters part), 5.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.SkyWritingTime.Value </term> <description> 
##  
## 0.8 (millimeters part), 0.8 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.TravelSpeed.Value </term> <description> 
##  
## 150.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Printer </term> <description> 
##  
## PowderBedFusion </description> </item> 
## 
## <item><term> 
##  
## ValidateOverheating </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ValidatePrintTime </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ValidateSupportVolume </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ValidateSurfaceArea </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## WeightOverheating </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## WeightPrintTime </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## WeightSupportVolume </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## WeightSurfaceArea </term> <description> 
##  
## 100 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckPartOrientationBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Validate.PartOrientationAnalysisResult</ja_class> builder """


    ##  Represents the accuracy level for part orientation optimization 
    ##  Represents coarse accuracy. This would be computationaly faster. 
    class AccuracyLevel(Enum):
        """
        Members Include: <Coarse> <Low> <Medium> <High> <VeryHigh>
        """
        Coarse: int
        Low: int
        Medium: int
        High: int
        VeryHigh: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CheckPartOrientationBuilder.AccuracyLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CheckPartOrientationBuilder.AccuracyLevel NXOpen.Validate.CheckPartOrientationBuilder.AccuracyLevel@endlink) Accuracy
    ##   the accuracy for optimization.  
    ##    Higher accuracy will take long computation time.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CheckPartOrientationBuilder.AccuracyLevel
    @property
    def Accuracy(self) -> CheckPartOrientationBuilder.AccuracyLevel:
        """
        Getter for property: (@link CheckPartOrientationBuilder.AccuracyLevel NXOpen.Validate.CheckPartOrientationBuilder.AccuracyLevel@endlink) Accuracy
          the accuracy for optimization.  
           Higher accuracy will take long computation time.  
         
        """
        pass
    
    ## Setter for property: (@link CheckPartOrientationBuilder.AccuracyLevel NXOpen.Validate.CheckPartOrientationBuilder.AccuracyLevel@endlink) Accuracy

    ##   the accuracy for optimization.  
    ##    Higher accuracy will take long computation time.  
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Accuracy.setter
    def Accuracy(self, accuracy: CheckPartOrientationBuilder.AccuracyLevel):
        """
        Setter for property: (@link CheckPartOrientationBuilder.AccuracyLevel NXOpen.Validate.CheckPartOrientationBuilder.AccuracyLevel@endlink) Accuracy
          the accuracy for optimization.  
           Higher accuracy will take long computation time.  
         
        """
        pass
    
    ## Getter for property: (@link FDMPrintTimeParameter NXOpen.Validate.FDMPrintTimeParameter@endlink) FDMPrintTimeParameter
    ##   the print time parameter for fused deposition modelling printer type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return FDMPrintTimeParameter
    @property
    def FDMPrintTimeParameter(self) -> FDMPrintTimeParameter:
        """
        Getter for property: (@link FDMPrintTimeParameter NXOpen.Validate.FDMPrintTimeParameter@endlink) FDMPrintTimeParameter
          the print time parameter for fused deposition modelling printer type   
            
         
        """
        pass
    
    ## Getter for property: (@link MJFPrintTimeParameter NXOpen.Validate.MJFPrintTimeParameter@endlink) MJFPrintTimeParameter
    ##   the print time parameter for multi jet fusion printer type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MJFPrintTimeParameter
    @property
    def MJFPrintTimeParameter(self) -> MJFPrintTimeParameter:
        """
        Getter for property: (@link MJFPrintTimeParameter NXOpen.Validate.MJFPrintTimeParameter@endlink) MJFPrintTimeParameter
          the print time parameter for multi jet fusion printer type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxOverhangAngleForOverHeating
    ##   the maximum overhang angle for overheating step   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxOverhangAngleForOverHeating(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxOverhangAngleForOverHeating
          the maximum overhang angle for overheating step   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxOverhangAngleForVolume
    ##   the maximum overhang angle for support volume parameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxOverhangAngleForVolume(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxOverhangAngleForVolume
          the maximum overhang angle for support volume parameter   
            
         
        """
        pass
    
    ## Getter for property: (@link PBFPrintTimeParameter NXOpen.Validate.PBFPrintTimeParameter@endlink) PBFPrintTimeParameter
    ##   the print time parameter for powder bed fusion printer type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PBFPrintTimeParameter
    @property
    def PBFPrintTimeParameter(self) -> PBFPrintTimeParameter:
        """
        Getter for property: (@link PBFPrintTimeParameter NXOpen.Validate.PBFPrintTimeParameter@endlink) PBFPrintTimeParameter
          the print time parameter for powder bed fusion printer type   
            
         
        """
        pass
    
    ## Getter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer
    ##   the printer type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CheckPrintTimeBuilder.PrinterType
    @property
    def Printer(self) -> CheckPrintTimeBuilder.PrinterType:
        """
        Getter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer
          the printer type   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer

    ##   the printer type   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Printer.setter
    def Printer(self, printer: CheckPrintTimeBuilder.PrinterType):
        """
        Setter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer
          the printer type   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (bool) ValidateOverheating
    ##   the overheating checker flag.  
    ##    If switched ON overheating area would be optimized.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ValidateOverheating(self) -> bool:
        """
        Getter for property: (bool) ValidateOverheating
          the overheating checker flag.  
           If switched ON overheating area would be optimized.  
         
        """
        pass
    
    ## Setter for property: (bool) ValidateOverheating

    ##   the overheating checker flag.  
    ##    If switched ON overheating area would be optimized.  
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ValidateOverheating.setter
    def ValidateOverheating(self, overheating: bool):
        """
        Setter for property: (bool) ValidateOverheating
          the overheating checker flag.  
           If switched ON overheating area would be optimized.  
         
        """
        pass
    
    ## Getter for property: (bool) ValidatePrintTime
    ##   the print time checker flag.  
    ##    If switched ON print time would be optimized.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ValidatePrintTime(self) -> bool:
        """
        Getter for property: (bool) ValidatePrintTime
          the print time checker flag.  
           If switched ON print time would be optimized.  
         
        """
        pass
    
    ## Setter for property: (bool) ValidatePrintTime

    ##   the print time checker flag.  
    ##    If switched ON print time would be optimized.  
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ValidatePrintTime.setter
    def ValidatePrintTime(self, printTime: bool):
        """
        Setter for property: (bool) ValidatePrintTime
          the print time checker flag.  
           If switched ON print time would be optimized.  
         
        """
        pass
    
    ## Getter for property: (bool) ValidateSupportVolume
    ##   the support volume checker flag.  
    ##    If switched ON support volume would be optimized.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ValidateSupportVolume(self) -> bool:
        """
        Getter for property: (bool) ValidateSupportVolume
          the support volume checker flag.  
           If switched ON support volume would be optimized.  
         
        """
        pass
    
    ## Setter for property: (bool) ValidateSupportVolume

    ##   the support volume checker flag.  
    ##    If switched ON support volume would be optimized.  
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ValidateSupportVolume.setter
    def ValidateSupportVolume(self, supportVolume: bool):
        """
        Setter for property: (bool) ValidateSupportVolume
          the support volume checker flag.  
           If switched ON support volume would be optimized.  
         
        """
        pass
    
    ## Getter for property: (bool) ValidateSurfaceArea
    ##   the surface area checker flag.  
    ##    If switched ON surface area would be optimized.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ValidateSurfaceArea(self) -> bool:
        """
        Getter for property: (bool) ValidateSurfaceArea
          the surface area checker flag.  
           If switched ON surface area would be optimized.  
         
        """
        pass
    
    ## Setter for property: (bool) ValidateSurfaceArea

    ##   the surface area checker flag.  
    ##    If switched ON surface area would be optimized.  
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ValidateSurfaceArea.setter
    def ValidateSurfaceArea(self, surfaceArea: bool):
        """
        Setter for property: (bool) ValidateSurfaceArea
          the surface area checker flag.  
           If switched ON surface area would be optimized.  
         
        """
        pass
    
    ## Getter for property: (int) WeightOverheating
    ##   the weight for overheating   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def WeightOverheating(self) -> int:
        """
        Getter for property: (int) WeightOverheating
          the weight for overheating   
            
         
        """
        pass
    
    ## Setter for property: (int) WeightOverheating

    ##   the weight for overheating   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WeightOverheating.setter
    def WeightOverheating(self, weightOverheating: int):
        """
        Setter for property: (int) WeightOverheating
          the weight for overheating   
            
         
        """
        pass
    
    ## Getter for property: (int) WeightPrintTime
    ##   the weight for print time   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def WeightPrintTime(self) -> int:
        """
        Getter for property: (int) WeightPrintTime
          the weight for print time   
            
         
        """
        pass
    
    ## Setter for property: (int) WeightPrintTime

    ##   the weight for print time   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WeightPrintTime.setter
    def WeightPrintTime(self, weightPrintTime: int):
        """
        Setter for property: (int) WeightPrintTime
          the weight for print time   
            
         
        """
        pass
    
    ## Getter for property: (int) WeightSupportVolume
    ##   the weight for support volume   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def WeightSupportVolume(self) -> int:
        """
        Getter for property: (int) WeightSupportVolume
          the weight for support volume   
            
         
        """
        pass
    
    ## Setter for property: (int) WeightSupportVolume

    ##   the weight for support volume   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WeightSupportVolume.setter
    def WeightSupportVolume(self, weightSupportVolume: int):
        """
        Setter for property: (int) WeightSupportVolume
          the weight for support volume   
            
         
        """
        pass
    
    ## Getter for property: (int) WeightSurfaceArea
    ##   the weight for surface area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return int
    @property
    def WeightSurfaceArea(self) -> int:
        """
        Getter for property: (int) WeightSurfaceArea
          the weight for surface area   
            
         
        """
        pass
    
    ## Setter for property: (int) WeightSurfaceArea

    ##   the weight for surface area   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WeightSurfaceArea.setter
    def WeightSurfaceArea(self, weightSurfaceArea: int):
        """
        Setter for property: (int) WeightSurfaceArea
          the weight for surface area   
            
         
        """
        pass
    
    ##  Calculate the checker at current orientation
    ##  @return checker_values (@link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink):  The values of checker and its range .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def CalculateCheck(builder: CheckPartOrientationBuilder) -> List[PartOrientationAnalysisResult.CheckerValues]:
        """
         Calculate the checker at current orientation
         @return checker_values (@link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink):  The values of checker and its range .
        """
        pass
    
    ##  Get minimum orientation for specific checker 
    ##  @return A tuple consisting of (origin, orientation, checker_values). 
    ##  - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
    ##  - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
    ##  - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="checker_index"> (@link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink) </param>
    @staticmethod
    def GetMinimumOrientation(builder: CheckPartOrientationBuilder, checker_index: PartOrientationAnalysisResult.CheckerIndex) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get minimum orientation for specific checker 
         @return A tuple consisting of (origin, orientation, checker_values). 
         - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
         - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
         - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range .

        """
        pass
    
    ##  Get number of optimum orientations
    ##  @return numOfOptimumOrientations (int): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def GetNumOfOptimumOrientations(builder: CheckPartOrientationBuilder) -> int:
        """
         Get number of optimum orientations
         @return numOfOptimumOrientations (int): .
        """
        pass
    
    ##  Get the optimum orientation at given index
    ##  @return A tuple consisting of (origin, orientation, checker_values). 
    ##  - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
    ##  - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
    ##  - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range. .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Index of optimum solution, should be within [0, num_of_optimum_orientations) 
    @staticmethod
    def GetOptimumOrientation(builder: CheckPartOrientationBuilder, optimum_orientation_index: int) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get the optimum orientation at given index
         @return A tuple consisting of (origin, orientation, checker_values). 
         - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
         - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
         - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range. .

        """
        pass
    
    ##  Get the persistent part orientation optimization result.
    ##  @return persistent_result (@link PartOrientationAnalysisResult NXOpen.Validate.PartOrientationAnalysisResult@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def GetPartOrientationResult(builder: CheckPartOrientationBuilder) -> PartOrientationAnalysisResult:
        """
         Get the persistent part orientation optimization result.
         @return persistent_result (@link PartOrientationAnalysisResult NXOpen.Validate.PartOrientationAnalysisResult@endlink): .
        """
        pass
    
    ##  Orient the build plane or part to the optimum orientation specified by index
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ##  The index of optimum solution. Should be with in [0 NumOfOptimumOrientations)
    def OptimumSolution(builder: CheckPartOrientationBuilder, orientationIndex: int) -> None:
        """
         Orient the build plane or part to the optimum orientation specified by index
        """
        pass
    
    ##  Orient the build plane or part to the minimum for specified checker
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ## <param name="checkerIndex"> (@link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink) </param>
    def OrientToMinimum(builder: CheckPartOrientationBuilder, checkerIndex: PartOrientationAnalysisResult.CheckerIndex) -> None:
        """
         Orient the build plane or part to the minimum for specified checker
        """
        pass
    
    ##  Remove all orientations.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def RemoveAllSolutions(builder: CheckPartOrientationBuilder) -> None:
        """
         Remove all orientations.
        """
        pass
    
    ##  The api to start the optimization process 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def StartCalculation(builder: CheckPartOrientationBuilder) -> None:
        """
         The api to start the optimization process 
        """
        pass
    
import NXOpen
##  Represents a Check Porosity Builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckPorosityBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckPorosityBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ColorMapDisplayOptionType </term> <description> 
##  
## All </description> </item> 
## 
## <item><term> 
##  
## MaximumPorosity </term> <description> 
##  
## 100.0 (millimeters part), 4.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumPorosity </term> <description> 
##  
## 0.0 (millimeters part), 0.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## TargetPorosity </term> <description> 
##  
## 50.0 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## VoxelSize.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CheckPorosityBuilder(NXOpen.Builder): 
    """ Represents a Check Porosity Builder """


    ##  Represent color map display option type 
    ##  Display All 
    class ColorMapDisplayOptionTypes(Enum):
        """
        Members Include: <All> <WithinLimits> <OutsideLimits> <AboveTarget> <BelowTarget>
        """
        All: int
        WithinLimits: int
        OutsideLimits: int
        AboveTarget: int
        BelowTarget: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CheckPorosityBuilder.ColorMapDisplayOptionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AboveLimit
    ##   the aboveLimit in volume results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def AboveLimit(self) -> float:
        """
        Getter for property: (float) AboveLimit
          the aboveLimit in volume results group   
            
         
        """
        pass
    
    ## Getter for property: (float) AboveTarget
    ##   the aboveTarget in volume results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def AboveTarget(self) -> float:
        """
        Getter for property: (float) AboveTarget
          the aboveTarget in volume results group   
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) Average
    ##   the average in porosity results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Average(self) -> float:
        """
        Getter for property: (float) Average
          the average in porosity results group   
            
         
        """
        pass
    
    ## Getter for property: (float) BelowLimit
    ##   the belowLimit in volume results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def BelowLimit(self) -> float:
        """
        Getter for property: (float) BelowLimit
          the belowLimit in volume results group   
            
         
        """
        pass
    
    ## Getter for property: (float) BelowTarget
    ##   the belowTarget in volume results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def BelowTarget(self) -> float:
        """
        Getter for property: (float) BelowTarget
          the belowTarget in volume results group   
            
         
        """
        pass
    
    ## Getter for property: (@link CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.Validate.CheckPorosityBuilder.ColorMapDisplayOptionTypes@endlink) ColorMapDisplayOptionType
    ##   the color map display option types   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return CheckPorosityBuilder.ColorMapDisplayOptionTypes
    @property
    def ColorMapDisplayOptionType(self) -> CheckPorosityBuilder.ColorMapDisplayOptionTypes:
        """
        Getter for property: (@link CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.Validate.CheckPorosityBuilder.ColorMapDisplayOptionTypes@endlink) ColorMapDisplayOptionType
          the color map display option types   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.Validate.CheckPorosityBuilder.ColorMapDisplayOptionTypes@endlink) ColorMapDisplayOptionType

    ##   the color map display option types   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ColorMapDisplayOptionType.setter
    def ColorMapDisplayOptionType(self, colorMapDisplayOptionType: CheckPorosityBuilder.ColorMapDisplayOptionTypes):
        """
        Setter for property: (@link CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.Validate.CheckPorosityBuilder.ColorMapDisplayOptionTypes@endlink) ColorMapDisplayOptionType
          the color map display option types   
            
         
        """
        pass
    
    ## Getter for property: (@link GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) GeometricConstraintDataManager
    ##   the Geometric Constraint Data Manager builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return GeometricConstraintDataManager
    @property
    def GeometricConstraintDataManager(self) -> GeometricConstraintDataManager:
        """
        Getter for property: (@link GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) GeometricConstraintDataManager
          the Geometric Constraint Data Manager builder  
            
         
        """
        pass
    
    ## Getter for property: (float) Maximum
    ##   the maximum in porosity results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Maximum(self) -> float:
        """
        Getter for property: (float) Maximum
          the maximum in porosity results group   
            
         
        """
        pass
    
    ## Getter for property: (float) MaximumPorosity
    ##   the Maximum Porosity    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def MaximumPorosity(self) -> float:
        """
        Getter for property: (float) MaximumPorosity
          the Maximum Porosity    
            
         
        """
        pass
    
    ## Setter for property: (float) MaximumPorosity

    ##   the Maximum Porosity    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MaximumPorosity.setter
    def MaximumPorosity(self, maximumPorosity: float):
        """
        Setter for property: (float) MaximumPorosity
          the Maximum Porosity    
            
         
        """
        pass
    
    ## Getter for property: (float) Median
    ##   the median in porosity results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Median(self) -> float:
        """
        Getter for property: (float) Median
          the median in porosity results group   
            
         
        """
        pass
    
    ## Getter for property: (float) Minimum
    ##   the minimum in porosity results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Minimum(self) -> float:
        """
        Getter for property: (float) Minimum
          the minimum in porosity results group   
            
         
        """
        pass
    
    ## Getter for property: (float) MinimumPorosity
    ##   the Minimum Porosity    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def MinimumPorosity(self) -> float:
        """
        Getter for property: (float) MinimumPorosity
          the Minimum Porosity    
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumPorosity

    ##   the Minimum Porosity    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MinimumPorosity.setter
    def MinimumPorosity(self, minimumPorosity: float):
        """
        Setter for property: (float) MinimumPorosity
          the Minimum Porosity    
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (float) TargetPorosity
    ##   the Target Porosity    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def TargetPorosity(self) -> float:
        """
        Getter for property: (float) TargetPorosity
          the Target Porosity    
            
         
        """
        pass
    
    ## Setter for property: (float) TargetPorosity

    ##   the Target Porosity    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TargetPorosity.setter
    def TargetPorosity(self, targetPorosity: float):
        """
        Setter for property: (float) TargetPorosity
          the Target Porosity    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VoxelSize
    ##   the expression representing the voxel size   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VoxelSize
          the expression representing the voxel size   
            
         
        """
        pass
    
    ## Getter for property: (float) WithinLimit
    ##   the withinLimit in volume results group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def WithinLimit(self) -> float:
        """
        Getter for property: (float) WithinLimit
          the withinLimit in volume results group   
            
         
        """
        pass
    
    ##  Adds geometric constraint point 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="face"> (@link NXOpen.Face NXOpen.Face@endlink) </param>
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def AddGeometricConstraintPoint(builder: CheckPorosityBuilder, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Adds geometric constraint point 
        """
        pass
    
    ##  Clears geometric constraint points 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ClearGeometricConstraintPoints(builder: CheckPorosityBuilder) -> None:
        """
         Clears geometric constraint points 
        """
        pass
    
    ##  Deletes geometric constraint point 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def DeleteGeometricConstraintPoint(builder: CheckPorosityBuilder, point: NXOpen.Point) -> None:
        """
         Deletes geometric constraint point 
        """
        pass
    
    ##  Creates color legend 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def MakeColorLegend(builder: CheckPorosityBuilder) -> None:
        """
         Creates color legend 
        """
        pass
    
    ##  Removes color legend 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RemoveColorLegend(builder: CheckPorosityBuilder) -> None:
        """
         Removes color legend 
        """
        pass
    
    ##  Sets geometric constraint point 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="face"> (@link NXOpen.Face NXOpen.Face@endlink) </param>
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def SetGeometricConstraintPoint(builder: CheckPorosityBuilder, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Sets geometric constraint point 
        """
        pass
    
import NXOpen
##  Represents a Check Print Time builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckPrintTimeBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckPrintTimeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## FDMPrintTimeParameter.LayerThickness.Value </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FDMPrintTimeParameter.NozzleDiameter.Value </term> <description> 
##  
## 0.5 (millimeters part), 0.025 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FDMPrintTimeParameter.TravelSpeed.Value </term> <description> 
##  
## 150.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MJFPrintTimeParameter.LayerPrintTime.Value </term> <description> 
##  
## 30.0 (millimeters part), 30.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MJFPrintTimeParameter.LayerThickness.Value </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.HatchSpacing.Value </term> <description> 
##  
## 1.0 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.IslandLength.Value </term> <description> 
##  
## 10.0 (millimeters part), 0.05 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.LayerThickness.Value </term> <description> 
##  
## 0.1 (millimeters part), 0.005 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.RecoatingTime.Value </term> <description> 
##  
## 5.0 (millimeters part), 5.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.SkyWritingTime.Value </term> <description> 
##  
## 0.8 (millimeters part), 0.8 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PBFPrintTimeParameter.TravelSpeed.Value </term> <description> 
##  
## 150.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Printer </term> <description> 
##  
## PowderBedFusion </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckPrintTimeBuilder(NXOpen.Builder): 
    """ Represents a Check Print Time builder """


    ##  Represents the type of printer 
    ##  Powder Bed Fusion(PBF) 
    class PrinterType(Enum):
        """
        Members Include: <PowderBedFusion> <MultiJetFusion> <FusedDepositionModeling>
        """
        PowderBedFusion: int
        MultiJetFusion: int
        FusedDepositionModeling: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CheckPrintTimeBuilder.PrinterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the boolean flag for automatic update   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the boolean flag for automatic update   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the boolean flag for automatic update   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the boolean flag for automatic update   
            
         
        """
        pass
    
    ## Getter for property: (@link FDMPrintTimeParameter NXOpen.Validate.FDMPrintTimeParameter@endlink) FDMPrintTimeParameter
    ##   the Fusion Deposition Modeling(FDM) printer parameters   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return FDMPrintTimeParameter
    @property
    def FDMPrintTimeParameter(self) -> FDMPrintTimeParameter:
        """
        Getter for property: (@link FDMPrintTimeParameter NXOpen.Validate.FDMPrintTimeParameter@endlink) FDMPrintTimeParameter
          the Fusion Deposition Modeling(FDM) printer parameters   
            
         
        """
        pass
    
    ## Getter for property: (@link MJFPrintTimeParameter NXOpen.Validate.MJFPrintTimeParameter@endlink) MJFPrintTimeParameter
    ##   the Multi Jet Fusion(MJF) printer parameters   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return MJFPrintTimeParameter
    @property
    def MJFPrintTimeParameter(self) -> MJFPrintTimeParameter:
        """
        Getter for property: (@link MJFPrintTimeParameter NXOpen.Validate.MJFPrintTimeParameter@endlink) MJFPrintTimeParameter
          the Multi Jet Fusion(MJF) printer parameters   
            
         
        """
        pass
    
    ## Getter for property: (@link PBFPrintTimeParameter NXOpen.Validate.PBFPrintTimeParameter@endlink) PBFPrintTimeParameter
    ##   the Powder Bed Fusion(PBF) printer parameters   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return PBFPrintTimeParameter
    @property
    def PBFPrintTimeParameter(self) -> PBFPrintTimeParameter:
        """
        Getter for property: (@link PBFPrintTimeParameter NXOpen.Validate.PBFPrintTimeParameter@endlink) PBFPrintTimeParameter
          the Powder Bed Fusion(PBF) printer parameters   
            
         
        """
        pass
    
    ## Getter for property: (float) PrintTime
    ##   the estimated time to print the part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def PrintTime(self) -> float:
        """
        Getter for property: (float) PrintTime
          the estimated time to print the part   
            
         
        """
        pass
    
    ## Getter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer
    ##   the printer type option as @link NXOpen::Validate::CheckPrintTimeBuilder::PrinterType NXOpen::Validate::CheckPrintTimeBuilder::PrinterType@endlink   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return CheckPrintTimeBuilder.PrinterType
    @property
    def Printer(self) -> CheckPrintTimeBuilder.PrinterType:
        """
        Getter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer
          the printer type option as @link NXOpen::Validate::CheckPrintTimeBuilder::PrinterType NXOpen::Validate::CheckPrintTimeBuilder::PrinterType@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer

    ##   the printer type option as @link NXOpen::Validate::CheckPrintTimeBuilder::PrinterType NXOpen::Validate::CheckPrintTimeBuilder::PrinterType@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_additive_design (" NX Additive Design")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Printer.setter
    def Printer(self, printerType: CheckPrintTimeBuilder.PrinterType):
        """
        Setter for property: (@link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink) Printer
          the printer type option as @link NXOpen::Validate::CheckPrintTimeBuilder::PrinterType NXOpen::Validate::CheckPrintTimeBuilder::PrinterType@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ##  Update the checker 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_additive_design (" NX Additive Design")
    @staticmethod
    def Update(builder: CheckPrintTimeBuilder) -> None:
        """
         Update the checker 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Check Trapped Supports Builder  <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckTrappedSupportsBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckTrappedSupportsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Angle </term> <description> 
##  
## 45 </description> </item> 
## 
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## NonTrappedSupportAreasColor </term> <description> 
##  
## 36 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyFailArea </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## TrappedSupportAreasColor </term> <description> 
##  
## 186 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckTrappedSupportsBuilder(NXOpen.Builder): 
    """ Represents a Check Trapped Supports Builder """


    ## Getter for property: (float) Angle
    ##   the Maximum Overhang Angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
          the Maximum Overhang Angle   
            
         
        """
        pass
    
    ## Setter for property: (float) Angle

    ##   the Maximum Overhang Angle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
          the Maximum Overhang Angle   
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonTrappedSupportAreasColor
    ##   the non-Trapped Supports Areas Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def NonTrappedSupportAreasColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonTrappedSupportAreasColor
          the non-Trapped Supports Areas Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonTrappedSupportAreasColor

    ##   the non-Trapped Supports Areas Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @NonTrappedSupportAreasColor.setter
    def NonTrappedSupportAreasColor(self, nonTrappedSupportAreasColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NonTrappedSupportAreasColor
          the non-Trapped Supports Areas Color   
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyFailArea
    ##   the show only trapped aupport areas   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyFailArea(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyFailArea
          the show only trapped aupport areas   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyFailArea

    ##   the show only trapped aupport areas   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ShowOnlyFailArea.setter
    def ShowOnlyFailArea(self, showOnlyFailArea: bool):
        """
        Setter for property: (bool) ShowOnlyFailArea
          the show only trapped aupport areas   
            
         
        """
        pass
    
    ## Getter for property: (float) TrappedArea
    ##   the trapped area   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return float
    @property
    def TrappedArea(self) -> float:
        """
        Getter for property: (float) TrappedArea
          the trapped area   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrappedSupportAreasColor
    ##   the Trapped Supports Areas Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def TrappedSupportAreasColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrappedSupportAreasColor
          the Trapped Supports Areas Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrappedSupportAreasColor

    ##   the Trapped Supports Areas Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @TrappedSupportAreasColor.setter
    def TrappedSupportAreasColor(self, trappedSupportAreasColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) TrappedSupportAreasColor
          the Trapped Supports Areas Color   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::Validate::CheckWhollyEnclosedVolumeBuilder NXOpen::Validate::CheckWhollyEnclosedVolumeBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Validate::AnalysisResultCollection::CreateCheckWhollyEnclosedVolumeBuilder  NXOpen::Validate::AnalysisResultCollection::CreateCheckWhollyEnclosedVolumeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolutionBuilder.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## PreviewState </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## WhollyEnclosedVolumeColor </term> <description> 
##  
## 36 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CheckWhollyEnclosedVolumeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Validate.CheckWhollyEnclosedVolumeBuilder</ja_class> """


    ## Getter for property: (bool) AutomaticUpdate
    ##   the automatic update toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##   the automatic update toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
          the automatic update toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
    ##   the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolutionBuilder(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolutionBuilder
          the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewState
    ##   the preview toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def PreviewState(self) -> bool:
        """
        Getter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewState

    ##   the preview toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PreviewState.setter
    def PreviewState(self, previewState: bool):
        """
        Setter for property: (bool) PreviewState
          the preview toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##   the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> SelectionAndPlacementBuilder:
        """
        Getter for property: (@link SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
          the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WhollyEnclosedVolumeColor
    ##   the Enclosed Void Volume Color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def WhollyEnclosedVolumeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WhollyEnclosedVolumeColor
          the Enclosed Void Volume Color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WhollyEnclosedVolumeColor

    ##   the Enclosed Void Volume Color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @WhollyEnclosedVolumeColor.setter
    def WhollyEnclosedVolumeColor(self, whollyEnclosedVolumeColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) WhollyEnclosedVolumeColor
          the Enclosed Void Volume Color   
            
         
        """
        pass
    
import NXOpen
##  Represents an object that manages Checker Editor Configuration.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ConfigureCheckerManager(NXOpen.Object): 
    """ Represents an object that manages Checker Editor Configuration.
    """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Class for Print Time Parameter for Fused Deposition Modelling 
## 
##   <br>  Created in NX1899.0.0  <br> 

class FDMPrintTimeParameter(NXOpen.TaggedObject): 
    """ Class for Print Time Parameter for Fused Deposition Modelling """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerThickness
    ##   the Layer thickness or slice thickness for printer.  
    ##   
    ##         Specify the thickness of material to be added on each layer.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LayerThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerThickness
          the Layer thickness or slice thickness for printer.  
          
                Specify the thickness of material to be added on each layer.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NozzleDiameter
    ##   the Jet nozzle diameter of printer.  
    ##    Specify the width of the
    ##         nozzle determining the material thickness along the print path.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NozzleDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NozzleDiameter
          the Jet nozzle diameter of printer.  
           Specify the width of the
                nozzle determining the material thickness along the print path.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TravelSpeed
    ##   the Scan Speed(Travel Speed) of the printer.  
    ##    Specify the speed of the print path.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TravelSpeed(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TravelSpeed
          the Scan Speed(Travel Speed) of the printer.  
           Specify the speed of the print path.   
         
        """
        pass
    
import NXOpen
##  This class represents the collection  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class KeyPerformanceInterfaceCollection(NXOpen.Object): 
    """ This class represents the collection """


    ##  Creates Linked Parameter Requirements Builder 
    ##  @return builder (@link LinkedParameterReqDialogBuilder NXOpen.Validate.LinkedParameterReqDialogBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_sdpd_mpm_a (" NX Parameter Management Author")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateLinkedParameterRequirementsBuilder(part: NXOpen.Part) -> LinkedParameterReqDialogBuilder:
        """
         Creates Linked Parameter Requirements Builder 
         @return builder (@link LinkedParameterReqDialogBuilder NXOpen.Validate.LinkedParameterReqDialogBuilder@endlink): .
        """
        pass
    
    ## Creates a new requirement check with pmi type 
    ##  @return validation (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link JA_KPI_COLLECTION_create_pmi_check JA_KPI_COLLECTION_create_pmi_check@endlink  instead.  <br> 

    ## License requirements: nx_sdpd_mpm_a (" NX Parameter Management Author")
    ##  name of requirement check 
    def CreateNewPmiCheck(requirement: Requirement, checkName: str, pmiValue: str, pmi: NXOpen.TaggedObject, detailtype: int) -> RequirementCheck:
        """
        Creates a new requirement check with pmi type 
         @return validation (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
        """
        pass
    
    ## Creates a new requirement check with pmi
    ##  @return validation (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_sdpd_mpm_a (" NX Parameter Management Author")
    ##  name of requirement check 
    def CreatePmiCheck(requirement: Requirement, checkName: str, pmiValue: str, pmi: NXOpen.TaggedObject, detailtype: int, useRelativeTol: bool) -> RequirementCheck:
        """
        Creates a new requirement check with pmi
         @return validation (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
        """
        pass
    
    ##  Refreshes Linked Parameter Requirements 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_sdpd_mpm_a (" NX Parameter Management Author")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="requirementTags"> (@link Requirement List[NXOpen.Validate.Requirement]@endlink) </param>
    ## <param name="refreshToLatest"> (bool) </param>
    def RefreshLinkedParameterRequirements(part: NXOpen.Part, requirementTags: List[Requirement], refreshToLatest: bool) -> None:
        """
         Refreshes Linked Parameter Requirements 
        """
        pass
    
import NXOpen
##  Represents a Builder class for crating object of linked paramter requirements dialog   <br> To create a new instance of this class, use @link NXOpen::Validate::KeyPerformanceInterfaceCollection::CreateLinkedParameterRequirementsBuilder  NXOpen::Validate::KeyPerformanceInterfaceCollection::CreateLinkedParameterRequirementsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class LinkedParameterReqDialogBuilder(NXOpen.Builder): 
    """ Represents a Builder class for crating object of linked paramter requirements dialog  """


    ##  Appends measurable attribute to builder 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_sdpd_mpm_a (" NX Parameter Management Author")
    ## 
    ## <param name="logicalItemId"> (str) </param>
    ## <param name="logicalItemRevId"> (str) </param>
    ## <param name="mesAttrName"> (str) </param>
    ## <param name="mesAttrRevId"> (str) </param>
    def AppendMeasurableAttribute(builder: LinkedParameterReqDialogBuilder, logicalItemId: str, logicalItemRevId: str, mesAttrName: str, mesAttrRevId: str) -> None:
        """
         Appends measurable attribute to builder 
        """
        pass
    
import NXOpen
## Logs validation outcomes and details for @link Validate::CheckerDefinition Validate::CheckerDefinition@endlink .
##     
## 
##   <br>  Created in NX1899.0.0  <br> 

class Logger(NXOpen.TransientObject): 
    """Logs validation outcomes and details for <ja_class>Validate.CheckerDefinition</ja_class>.
    """


    ##  Frees the object from memory. After this method is called,
    ##         it is illegal to use the object. In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(logger: Logger) -> None:
        """
         Frees the object from memory. After this method is called,
                it is illegal to use the object. In .NET, this method is automatically
                called when the object is deleted by the garbage collector. 
        """
        pass
    
    ##  Logs a Boolean (logical) attribute. 
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogBooleanAttribute(logger: Logger, title: str, booleanValue: bool) -> None:
        """
         Logs a Boolean (logical) attribute. 
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Logs an array attributes of Boolean (logical) type.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogBooleanAttributes(logger: Logger, title: str, attrs: List[bool]) -> None:
        """
         Logs an array attributes of Boolean (logical) type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Asks a child logger node.
    ##          @code 
    ##         childLogger = logger.LogChildNode("Attributes");    
    ##          @endcode 
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The name of the child logger.
    def LogChildNode(logger: Logger, childLoggerName: str) -> Logger:
        """
         Asks a child logger node.
                 @code 
                childLogger = logger.LogChildNode("Attributes");    
                 @endcode 
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs an integer number attribute.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogIntegerAttribute(logger: Logger, title: str, integerValue: int) -> None:
        """
         Logs an integer number attribute.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Logs an array attributes of integer type.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogIntegerAttributes(logger: Logger, title: str, attrs: List[int]) -> None:
        """
         Logs an array attributes of integer type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Logs a validation message node.
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The validation outcome.
    def LogMessageNode(logger: Logger, outcome: NXOpen.Validation.Result, message: str) -> Logger:
        """
         Logs a validation message node.
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs a validation outcome and a @link NXObject NXObject@endlink  as validation outcome detail.
    ##         
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## The validation outcome.
    def LogNXObject(logger: Logger, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject) -> None:
        """
         Logs a validation outcome and a @link NXObject NXObject@endlink  as validation outcome detail.
                
        """
        pass
    
    ##  Logs a validation outcome node and a @link NXObject NXObject@endlink  with a message as validation outcome detail.
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## The validation outcome.
    def LogNXObjectNode(logger: Logger, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str) -> Logger:
        """
         Logs a validation outcome node and a @link NXObject NXObject@endlink  with a message as validation outcome detail.
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs a validation outcome node and a @link NXObject NXObject@endlink  as validation outcome detail.
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## The validation outcome.
    def LogNXObjectNodeOnly(logger: Logger, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject) -> Logger:
        """
         Logs a validation outcome node and a @link NXObject NXObject@endlink  as validation outcome detail.
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs a validation outcome node and a @link NXObject NXObject@endlink  with detailed information as validation outcome detail.
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## The validation outcome.
    def LogNXObjectNodeWithInfo(logger: Logger, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str, objectName: str, referencePoints: List[NXOpen.Point3d], referenceVectors: List[NXOpen.Vector3d]) -> Logger:
        """
         Logs a validation outcome node and a @link NXObject NXObject@endlink  with detailed information as validation outcome detail.
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs a set of @link NXObject NXObject@endlink  in a child logger.
    ##          @code 
    ##         objSetLogger = logger.LogNXObjectSet("Failed Bodies", "The connection locations conflict with the constraints.");
    ##         ' the objSetLogger is a child of the logger.
    ##         objSetLogger.LogNXObject(Validation.Result.Failed, body1 );
    ##         objSetLogger.LogNXObject(Validation.Result.Failed, body2 );        
    ##          @endcode 
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger that is created.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The name of the set.
    def LogNXObjectSet(logger: Logger, name: str, message: str) -> Logger:
        """
         Logs a set of @link NXObject NXObject@endlink  in a child logger.
                 @code 
                objSetLogger = logger.LogNXObjectSet("Failed Bodies", "The connection locations conflict with the constraints.");
                ' the objSetLogger is a child of the logger.
                objSetLogger.LogNXObject(Validation.Result.Failed, body1 );
                objSetLogger.LogNXObject(Validation.Result.Failed, body2 );        
                 @endcode 
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger that is created.
        """
        pass
    
    ##  Logs a validation outcome and a @link NXObject NXObject@endlink  as validation outcome detail.
    ##         
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## The validation outcome.
    @overload
    def LogNXObject(self, logger: Logger, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str) -> None:
        """
         Logs a validation outcome and a @link NXObject NXObject@endlink  as validation outcome detail.
                
        """
        pass
    
    ##  Logs a validation outcome and a @link NXObject NXObject@endlink  as validation outcome detail.
    ##         
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## The validation outcome.
    @overload
    def LogNXObject(self, logger: Logger, outcome: NXOpen.Validation.Result, anObject: NXOpen.NXObject, message: str, objectName: str, referencePoints: List[NXOpen.Point3d], referenceVectors: List[NXOpen.Vector3d]) -> None:
        """
         Logs a validation outcome and a @link NXObject NXObject@endlink  as validation outcome detail.
                
        """
        pass
    
    ##  Logs a real number attribute.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogRealAttribute(logger: Logger, title: str, realValue: float) -> None:
        """
         Logs a real number attribute.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Logs an array attributes of real type.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogRealAttributes(logger: Logger, title: str, attrs: List[float]) -> None:
        """
         Logs an array attributes of real type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Logs a validation outcome with descriptive message.
    ##         
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The validation outcome.
    def LogResult(logger: Logger, outcome: NXOpen.Validation.Result, message: str) -> None:
        """
         Logs a validation outcome with descriptive message.
                
        """
        pass
    
    ##  Logs a validation outcome node with a descriptive message.
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The validation outcome.
    def LogResultNode(logger: Logger, outcome: NXOpen.Validation.Result, message: str) -> Logger:
        """
         Logs a validation outcome node with a descriptive message.
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs a validation outcome node without a descriptive message.
    ##         
    ##  @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The validation outcome.
    def LogResultNodeOnly(logger: Logger, outcome: NXOpen.Validation.Result) -> Logger:
        """
         Logs a validation outcome node without a descriptive message.
                
         @return childLogger (@link Logger NXOpen.Validate.Logger@endlink):  The child logger of this logger.
        """
        pass
    
    ##  Logs a string attribute.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogStringAttribute(logger: Logger, title: str, stringValue: str) -> None:
        """
         Logs a string attribute.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
    ##  Logs an array attributes of string type.
    ##         If attribute with the same title exists already, overwrites it. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The title of attribute. 
    def LogStringAttributes(logger: Logger, title: str, attrs: List[str]) -> None:
        """
         Logs an array attributes of string type.
                If attribute with the same title exists already, overwrites it. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Class for Print Time Parameter for Multi Jet Fusion printer
## 
##   <br>  Created in NX1899.0.0  <br> 

class MJFPrintTimeParameter(NXOpen.TaggedObject): 
    """ Class for Print Time Parameter for Multi Jet Fusion printer"""


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerPrintTime
    ##   the Layer Print Time or print speed of printer.  
    ##   
    ##         Specify the time needed to add a new layer of metal powder.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LayerPrintTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerPrintTime
          the Layer Print Time or print speed of printer.  
          
                Specify the time needed to add a new layer of metal powder.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerThickness
    ##   the Layer thickness or slice thickness for printing process.  
    ##   
    ##         Specify the thickness of material to be added on each layer.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LayerThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerThickness
          the Layer thickness or slice thickness for printing process.  
          
                Specify the thickness of material to be added on each layer.   
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Validate::Override NXOpen::Validate::Override@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Validate::ResultObject::CreateOverrideBuilder  NXOpen::Validate::ResultObject::CreateOverrideBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## RequestType </term> <description> 
##  
## Permanent </description> </item> 
## 
## <item><term> 
##  
## ToState </term> <description> 
##  
## Passed </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.5.0  <br> 

class OverrideBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Validate.Override</ja_class> builder """


    ##  Represents the override request decision action 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Approved</term><description> 
    ## </description> </item><item><term> 
    ## Rejected</term><description> 
    ## </description> </item><item><term> 
    ## Pending</term><description> 
    ## </description> </item></list>
    class DecisionActions(Enum):
        """
        Members Include: <Approved> <Rejected> <Pending>
        """
        Approved: int
        Rejected: int
        Pending: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverrideBuilder.DecisionActions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the override request type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Permanent</term><description> 
    ## </description> </item><item><term> 
    ## Temporary</term><description> 
    ## </description> </item></list>
    class RequestTypes(Enum):
        """
        Members Include: <Permanent> <Temporary>
        """
        Permanent: int
        Temporary: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverrideBuilder.RequestTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the override request to state 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Passed</term><description> 
    ## </description> </item><item><term> 
    ## Failed</term><description> 
    ## </description> </item></list>
    class ToStates(Enum):
        """
        Members Include: <Passed> <Failed>
        """
        Passed: int
        Failed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OverrideBuilder.ToStates:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Category
    ##   the category of override request.  
    ##   
    ##             The category is optional unless override reason configuration is mandatory in Teamcenter.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
          the category of override request.  
          
                    The category is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##   the category of override request.  
    ##   
    ##             The category is optional unless override reason configuration is mandatory in Teamcenter.
    ##           
    ##  
    ## Setter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
          the category of override request.  
          
                    The category is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    
    ## Getter for property: (@link OverrideBuilder.DecisionActions NXOpen.Validate.OverrideBuilder.DecisionActions@endlink) DecisionAction
    ##   the decision action of override request
    ##             The decision action is automatically pending while override request is created.  
    ##    If any property of override request is changed, the decision action will be pending.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return OverrideBuilder.DecisionActions
    @property
    def DecisionAction(self) -> OverrideBuilder.DecisionActions:
        """
        Getter for property: (@link OverrideBuilder.DecisionActions NXOpen.Validate.OverrideBuilder.DecisionActions@endlink) DecisionAction
          the decision action of override request
                    The decision action is automatically pending while override request is created.  
           If any property of override request is changed, the decision action will be pending.
                  
         
        """
        pass
    
    ## Setter for property: (@link OverrideBuilder.DecisionActions NXOpen.Validate.OverrideBuilder.DecisionActions@endlink) DecisionAction

    ##   the decision action of override request
    ##             The decision action is automatically pending while override request is created.  
    ##    If any property of override request is changed, the decision action will be pending.
    ##           
    ##  
    ## Setter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DecisionAction.setter
    def DecisionAction(self, decisionAction: OverrideBuilder.DecisionActions):
        """
        Setter for property: (@link OverrideBuilder.DecisionActions NXOpen.Validate.OverrideBuilder.DecisionActions@endlink) DecisionAction
          the decision action of override request
                    The decision action is automatically pending while override request is created.  
           If any property of override request is changed, the decision action will be pending.
                  
         
        """
        pass
    
    ## Getter for property: (str) DecisionUser
    ##   the decision user 
    ##             The decision user is a Teamcenter user in the Validation Administration group.  
    ##    If the decision user is empty, it means thant any user in the group can review override request.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DecisionUser(self) -> str:
        """
        Getter for property: (str) DecisionUser
          the decision user 
                    The decision user is a Teamcenter user in the Validation Administration group.  
           If the decision user is empty, it means thant any user in the group can review override request.
                  
         
        """
        pass
    
    ## Setter for property: (str) DecisionUser

    ##   the decision user 
    ##             The decision user is a Teamcenter user in the Validation Administration group.  
    ##    If the decision user is empty, it means thant any user in the group can review override request.
    ##           
    ##  
    ## Setter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DecisionUser.setter
    def DecisionUser(self, decisionUser: str):
        """
        Setter for property: (str) DecisionUser
          the decision user 
                    The decision user is a Teamcenter user in the Validation Administration group.  
           If the decision user is empty, it means thant any user in the group can review override request.
                  
         
        """
        pass
    
    ## Getter for property: (str) Reason
    ##   the reason of override request.  
    ##   
    ##             The reason is optional unless override reason configuration is mandatory in Teamcenter.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Reason(self) -> str:
        """
        Getter for property: (str) Reason
          the reason of override request.  
          
                    The reason is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    
    ## Setter for property: (str) Reason

    ##   the reason of override request.  
    ##   
    ##             The reason is optional unless override reason configuration is mandatory in Teamcenter.
    ##           
    ##  
    ## Setter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Reason.setter
    def Reason(self, reason: str):
        """
        Setter for property: (str) Reason
          the reason of override request.  
          
                    The reason is optional unless override reason configuration is mandatory in Teamcenter.
                  
         
        """
        pass
    
    ## Getter for property: (@link OverrideBuilder.RequestTypes NXOpen.Validate.OverrideBuilder.RequestTypes@endlink) RequestType
    ##   the type of override request  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return OverrideBuilder.RequestTypes
    @property
    def RequestType(self) -> OverrideBuilder.RequestTypes:
        """
        Getter for property: (@link OverrideBuilder.RequestTypes NXOpen.Validate.OverrideBuilder.RequestTypes@endlink) RequestType
          the type of override request  
            
         
        """
        pass
    
    ## Setter for property: (@link OverrideBuilder.RequestTypes NXOpen.Validate.OverrideBuilder.RequestTypes@endlink) RequestType

    ##   the type of override request  
    ##     
    ##  
    ## Setter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RequestType.setter
    def RequestType(self, requestType: OverrideBuilder.RequestTypes):
        """
        Setter for property: (@link OverrideBuilder.RequestTypes NXOpen.Validate.OverrideBuilder.RequestTypes@endlink) RequestType
          the type of override request  
            
         
        """
        pass
    
    ## Getter for property: (@link OverrideBuilder.ToStates NXOpen.Validate.OverrideBuilder.ToStates@endlink) ToState
    ##   the to state of override request   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return OverrideBuilder.ToStates
    @property
    def ToState(self) -> OverrideBuilder.ToStates:
        """
        Getter for property: (@link OverrideBuilder.ToStates NXOpen.Validate.OverrideBuilder.ToStates@endlink) ToState
          the to state of override request   
            
         
        """
        pass
    
    ## Setter for property: (@link OverrideBuilder.ToStates NXOpen.Validate.OverrideBuilder.ToStates@endlink) ToState

    ##   the to state of override request   
    ##     
    ##  
    ## Setter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ToState.setter
    def ToState(self, toState: OverrideBuilder.ToStates):
        """
        Setter for property: (@link OverrideBuilder.ToStates NXOpen.Validate.OverrideBuilder.ToStates@endlink) ToState
          the to state of override request   
            
         
        """
        pass
    
    ##  Returns the decision comments 
    ##  @return decisionComments (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetDecisionComments(self) -> List[str]:
        """
         Returns the decision comments 
         @return decisionComments (List[str]): .
        """
        pass
    
    ##  Returns the detail reason 
    ##  @return detailReason (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetDetailReason(self) -> List[str]:
        """
         Returns the detail reason 
         @return detailReason (List[str]): .
        """
        pass
    
    ##  Sets the decision comments 
    ##             The decision comments is optional.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  
    def SetDecisionComments(self, decisionComments: List[str]) -> None:
        """
         Sets the decision comments 
                    The decision comments is optional.
                
        """
        pass
    
    ##  Sets the detail reason 
    ##             The detail reason is optional unless override reason configuration is mandatory in Teamcenter.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  
    def SetDetailReason(self, detailReason: List[str]) -> None:
        """
         Sets the detail reason 
                    The detail reason is optional unless override reason configuration is mandatory in Teamcenter.
                
        """
        pass
    
import NXOpen
## Represents a @link NXOpen::Validate::Override NXOpen::Validate::Override@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::Validate::OverrideBuilder  NXOpen::Validate::OverrideBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class Override(NXOpen.NXObject): 
    """Represents a <ja_class>NXOpen.Validate.Override</ja_class> object."""
    pass


import NXOpen
##   @brief  Represents a NX @link NXOpen::Validate::Parameter NXOpen::Validate::Parameter@endlink .  
## 
##  
##       <br> A parameter is defined with a name, value formula and data type as well as whether the parameter can hold multiple
##      values or single value and the data to build pull down menu or List selection dialogue to customize the values at runtime.
##      Parameters are used to execute check logic. <br> 
##     
## 
##   <br>  Created in NX1899.0.0  <br> 

class Parameter(NXOpen.TransientObject): 
    """ <summary> Represents a NX <ja_class>NXOpen.Validate.Parameter</ja_class>. </summary>
     <para>A parameter is defined with a name, value formula and data type as well as whether the parameter can hold multiple
     values or single value and the data to build pull down menu or List selection dialogue to customize the values at runtime.
     Parameters are used to execute check logic.</para>
    """


    ## Getter for property: (str) Title
    ##   the title string of the parameter.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
          the title string of the parameter.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.RuleManager.RuleType NXOpen.RuleManager.RuleType@endlink) Type
    ##   the data type of a parameter.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.RuleManager.RuleType
    @property
    def Type(self) -> NXOpen.RuleManager.RuleType:
        """
        Getter for property: (@link NXOpen.RuleManager.RuleType NXOpen.RuleManager.RuleType@endlink) Type
          the data type of a parameter.  
            
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(parameter: Parameter) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets boolean type value from a single value parameter.
    ##  @return value (bool):  The boolean type value.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBooleanValue(parameter: Parameter) -> bool:
        """
         Gets boolean type value from a single value parameter.
         @return value (bool):  The boolean type value.
        """
        pass
    
    ##  Gets boolean type values from a multi-value parameter.
    ##  @return value (List[bool]):  The boolean type values.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBooleanValues(parameter: Parameter) -> List[bool]:
        """
         Gets boolean type values from a multi-value parameter.
         @return value (List[bool]):  The boolean type values.
        """
        pass
    
    ##  Gets real number type value from a single value parameter.
    ##  @return value (float):  The real number type value.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDoubleValue(parameter: Parameter) -> float:
        """
         Gets real number type value from a single value parameter.
         @return value (float):  The real number type value.
        """
        pass
    
    ##  Gets real number type values from a multi-value parameter.
    ##  @return value (List[float]):  The real number type values.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDoubleValues(parameter: Parameter) -> List[float]:
        """
         Gets real number type values from a multi-value parameter.
         @return value (List[float]):  The real number type values.
        """
        pass
    
    ##  Gets integer number type value from a single value parameter.
    ##  @return value (int):  The integer number type value.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetIntValue(parameter: Parameter) -> int:
        """
         Gets integer number type value from a single value parameter.
         @return value (int):  The integer number type value.
        """
        pass
    
    ##  Gets integer number type values from a multi-value parameter.
    ##  @return value (List[int]):  The integer number type values.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetIntValues(parameter: Parameter) -> List[int]:
        """
         Gets integer number type values from a multi-value parameter.
         @return value (List[int]):  The integer number type values.
        """
        pass
    
    ##  Gets @link NXObject NXObject@endlink  type value from a single value parameter.
    ##  @return value (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The NXObject type value.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNXObjectValue(parameter: Parameter) -> NXOpen.NXObject:
        """
         Gets @link NXObject NXObject@endlink  type value from a single value parameter.
         @return value (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The NXObject type value.
        """
        pass
    
    ##  Gets @link NXObject NXObject@endlink  values from a multi-value parameter.
    ##  @return value (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The NXObject type values.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNXObjectValues(parameter: Parameter) -> List[NXOpen.NXObject]:
        """
         Gets @link NXObject NXObject@endlink  values from a multi-value parameter.
         @return value (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  The NXObject type values.
        """
        pass
    
    ##  Gets @link Point3d Point3d@endlink  type value from a single value parameter.
    ##  @return value (@link NXOpen.Point3d NXOpen.Point3d@endlink):  Point3d type value.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPoint3dValue(parameter: Parameter) -> NXOpen.Point3d:
        """
         Gets @link Point3d Point3d@endlink  type value from a single value parameter.
         @return value (@link NXOpen.Point3d NXOpen.Point3d@endlink):  Point3d type value.
        """
        pass
    
    ##  Gets @link Point3d Point3d@endlink  type values from a multi-value parameter.
    ##  @return value (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  Point3d type values.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPoint3dValues(parameter: Parameter) -> List[NXOpen.Point3d]:
        """
         Gets @link Point3d Point3d@endlink  type values from a multi-value parameter.
         @return value (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink):  Point3d type values.
        """
        pass
    
    ##  Gets string type value from a single value parameter.
    ##  @return value (str):  The string type value.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStringValue(parameter: Parameter) -> str:
        """
         Gets string type value from a single value parameter.
         @return value (str):  The string type value.
        """
        pass
    
    ##  Gets string type values from a multi-value parameter.
    ##  @return value (List[str]):  The string type values.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStringValues(parameter: Parameter) -> List[str]:
        """
         Gets string type values from a multi-value parameter.
         @return value (List[str]):  The string type values.
        """
        pass
    
    ##  Gets @link Vector3d Vector3d@endlink  type value from a single value parameter.
    ##  @return value (@link NXOpen.Vector3d NXOpen.Vector3d@endlink):  Vector3d type value.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetVector3dValue(parameter: Parameter) -> NXOpen.Vector3d:
        """
         Gets @link Vector3d Vector3d@endlink  type value from a single value parameter.
         @return value (@link NXOpen.Vector3d NXOpen.Vector3d@endlink):  Vector3d type value.
        """
        pass
    
    ##  Gets @link Vector3d Vector3d@endlink  type values from a multi-value parameter.
    ##  @return value (@link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink):  Vector3d type values.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetVector3dValues(parameter: Parameter) -> List[NXOpen.Vector3d]:
        """
         Gets @link Vector3d Vector3d@endlink  type values from a multi-value parameter.
         @return value (@link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink):  Vector3d type values.
        """
        pass
    
    ##  Finds out if a parameter is single value or multi-value. True - multi-value list; false - single value. 
    ##  @return isList (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def IsList(parameter: Parameter) -> bool:
        """
         Finds out if a parameter is single value or multi-value. True - multi-value list; false - single value. 
         @return isList (bool): .
        """
        pass
    
    ##  Sets boolean type value to a single value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The boolean type value.
    def SetBooleanValue(parameter: Parameter, data: bool) -> None:
        """
         Sets boolean type value to a single value parameter.
        """
        pass
    
    ##  Sets boolean type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The boolean type values.
    def SetBooleanValues(parameter: Parameter, data: List[bool]) -> None:
        """
         Sets boolean type values to a multi-value parameter.
        """
        pass
    
    ##  Sets real number type value to a single value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The real number type value.
    def SetDoubleValue(parameter: Parameter, data: float) -> None:
        """
         Sets real number type value to a single value parameter.
        """
        pass
    
    ##  Sets real number type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The real number type values.
    def SetDoubleValues(parameter: Parameter, data: List[float]) -> None:
        """
         Sets real number type values to a multi-value parameter.
        """
        pass
    
    ##  Sets integer number type value to a single value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The integer number type value.
    def SetIntValue(parameter: Parameter, data: int) -> None:
        """
         Sets integer number type value to a single value parameter.
        """
        pass
    
    ##  Sets integer number type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The integer number type values.
    def SetIntValues(parameter: Parameter, data: List[int]) -> None:
        """
         Sets integer number type values to a multi-value parameter.
        """
        pass
    
    ##  Sets @link NXObject NXObject@endlink  value to a single value parameter.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The NXObject type value.
    def SetNXObjectValue(parameter: Parameter, data: NXOpen.NXObject) -> None:
        """
         Sets @link NXObject NXObject@endlink  value to a single value parameter.
        """
        pass
    
    ##  Sets @link NXObject NXObject@endlink  type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The NXObject type values.
    def SetNXObjectValues(parameter: Parameter, data: List[NXOpen.NXObject]) -> None:
        """
         Sets @link NXObject NXObject@endlink  type values to a multi-value parameter.
        """
        pass
    
    ##  Sets @link Point3d Point3d@endlink  type value to a single value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Point3d type value.
    def SetPoint3dValue(parameter: Parameter, data: NXOpen.Point3d) -> None:
        """
         Sets @link Point3d Point3d@endlink  type value to a single value parameter.
        """
        pass
    
    ##  Sets @link Point3d Point3d@endlink  type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Point3d type values.
    def SetPoint3dValues(parameter: Parameter, data: List[NXOpen.Point3d]) -> None:
        """
         Sets @link Point3d Point3d@endlink  type values to a multi-value parameter.
        """
        pass
    
    ##  Sets string type value to a single value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The string type value.
    def SetStringValue(parameter: Parameter, data: str) -> None:
        """
         Sets string type value to a single value parameter.
        """
        pass
    
    ##  Sets string type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The string type values.
    def SetStringValues(parameter: Parameter, data: List[str]) -> None:
        """
         Sets string type values to a multi-value parameter.
        """
        pass
    
    ##  Sets @link Vector3d Vector3d@endlink  type value to a single value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Vector3d type value.
    def SetVector3dValue(parameter: Parameter, data: NXOpen.Vector3d) -> None:
        """
         Sets @link Vector3d Vector3d@endlink  type value to a single value parameter.
        """
        pass
    
    ##  Sets @link Vector3d Vector3d@endlink  type values to a multi-value parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Vector3d type values.
    def SetVector3dValues(parameter: Parameter, data: List[NXOpen.Vector3d]) -> None:
        """
         Sets @link Vector3d Vector3d@endlink  type values to a multi-value parameter.
        """
        pass
    
import NXOpen
## Represents a NX @link NXOpen::Validate::Parser NXOpen::Validate::Parser@endlink .
##      <br> To create a new instance of this class, use @link NXOpen::Validate::ValidationManager::CreateParser  NXOpen::Validate::ValidationManager::CreateParser @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class Parser(NXOpen.TaggedObject): 
    """Represents a NX <ja_class>NXOpen.Validate.Parser</ja_class>.
    """


    ##  The data source type of check result. 
    ##  Result of most recent run 
    class DataSourceTypes(Enum):
        """
        Members Include: <MostRecentRun> <ResultFromPart> <ResultFromTeamcenter> <ResultFromNXChecks> <ResultFromLogFile>
        """
        MostRecentRun: int
        ResultFromPart: int
        ResultFromTeamcenter: int
        ResultFromNXChecks: int
        ResultFromLogFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Parser.DataSourceTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link Parser.DataSourceTypes NXOpen.Validate.Parser.DataSourceTypes@endlink) DataSource
    ##   the result data source type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return Parser.DataSourceTypes
    @property
    def DataSource(self) -> Parser.DataSourceTypes:
        """
        Getter for property: (@link Parser.DataSourceTypes NXOpen.Validate.Parser.DataSourceTypes@endlink) DataSource
          the result data source type   
            
         
        """
        pass
    
    ## Setter for property: (@link Parser.DataSourceTypes NXOpen.Validate.Parser.DataSourceTypes@endlink) DataSource

    ##   the result data source type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DataSource.setter
    def DataSource(self, dataSource: Parser.DataSourceTypes):
        """
        Setter for property: (@link Parser.DataSourceTypes NXOpen.Validate.Parser.DataSourceTypes@endlink) DataSource
          the result data source type   
            
         
        """
        pass
    
    ## Getter for property: (int) MaxDisplayObjects
    ##   the Max entity count to display of current module   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return int
    @property
    def MaxDisplayObjects(self) -> int:
        """
        Getter for property: (int) MaxDisplayObjects
          the Max entity count to display of current module   
            
         
        """
        pass
    
    ## Setter for property: (int) MaxDisplayObjects

    ##   the Max entity count to display of current module   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @MaxDisplayObjects.setter
    def MaxDisplayObjects(self, maxDisplayObjects: int):
        """
        Setter for property: (int) MaxDisplayObjects
          the Max entity count to display of current module   
            
         
        """
        pass
    
    ##  Clears result objects 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ClearResultObjects(parser: Parser) -> None:
        """
         Clears result objects 
        """
        pass
    
    ##  Runs parsing process 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Commit(parser: Parser) -> None:
        """
         Runs parsing process 
        """
        pass
    
    ##  Deletes result object, return error code 
    ##  @return status (int):   .
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: None.
    ##   
    def DeleteResult(parser: Parser, resultObject: ResultObject) -> int:
        """
         Deletes result object, return error code 
         @return status (int):   .
        """
        pass
    
    ##  Deletes result object, return error list 
    ##  @return errors (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  List of errors encountered during the delete .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##   
    def DeleteResultObject(parser: Parser, resultObject: ResultObject) -> NXOpen.ErrorList:
        """
         Deletes result object, return error list 
         @return errors (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  List of errors encountered during the delete .
        """
        pass
    
    ##  Gets entity result objects from input object 
    ##  @return objectResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##   
    def GetObjectResultObjects(parser: Parser, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets entity result objects from input object 
         @return objectResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
        """
        pass
    
    ##  Gets entity set result objects from input object 
    ##  @return objectSetResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##   
    def GetObjectSetResultObjects(parser: Parser, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets entity set result objects from input object 
         @return objectSetResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
        """
        pass
    
    ##  Gets part result objects 
    ##  @return partResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):   .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPartResultObjects(parser: Parser) -> List[ResultObject]:
        """
         Gets part result objects 
         @return partResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):   .
        """
        pass
    
    ##  Gets profile result objects 
    ##  @return profileResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):   .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## <param name="parser"> (@link Parser NXOpen.Validate.Parser@endlink) </param>
    @staticmethod
    @overload
    def GetProfileResultObjects(self, parser: Parser) -> List[ResultObject]:
        """
         Gets profile result objects 
         @return profileResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):   .
        """
        pass
    
    ##  Gets profile result objects from input object 
    ##  @return profileResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):   .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##   
    @overload
    def GetProfileResultObjects(self, parser: Parser, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets profile result objects from input object 
         @return profileResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):   .
        """
        pass
    
    ##  Gets test result objects 
    ##  @return testResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## <param name="parser"> (@link Parser NXOpen.Validate.Parser@endlink) </param>
    @staticmethod
    @overload
    def GetTestResultObjects(self, parser: Parser) -> List[ResultObject]:
        """
         Gets test result objects 
         @return testResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
        """
        pass
    
    ##  Gets test result objects from input object 
    ##  @return testResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##   
    @overload
    def GetTestResultObjects(self, parser: Parser, resultObject: ResultObject) -> List[ResultObject]:
        """
         Gets test result objects from input object 
         @return testResultObject (@link ResultObject List[NXOpen.Validate.ResultObject]@endlink):  .
        """
        pass
    
import NXOpen
##   @brief Represents a part file that validator will check against.  
## 
##  
##       <br> Part node contains the information of part filename and part object. 
##      You can create the part node by inputting part filename, or by inputting part object, or by inputting both.
##      Validator will use the part object in the part node for checking. Only when the part object in the part node
##      is NULL, then validator will use the part filename for checking. <br> 
##     
## 
##   <br>  Created in NX7.5.0  <br> 

class PartNode(NXOpen.TransientObject): 
    """ <summary>Represents a part file that validator will check against. </summary>
     <para>Part node contains the information of part filename and part object. 
     You can create the part node by inputting part filename, or by inputting part object, or by inputting both.
     Validator will use the part object in the part node for checking. Only when the part object in the part node
     is <ja_NULL>, then validator will use the part filename for checking.</para>
    """


    ## Getter for property: (str) FileName
    ##   the part file name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the part file name   
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the part file name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the part file name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) PartObject
    ##   the part object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Part
    @property
    def PartObject(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) PartObject
          the part object   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) PartObject

    ##   the part object   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @PartObject.setter
    def PartObject(self, part: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) PartObject
          the part object   
            
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
import NXOpen
## 
##      This can be created using a @link NXOpen::Validate::CheckPartOrientationBuilder NXOpen::Validate::CheckPartOrientationBuilder@endlink  object.
##     
## 
##   <br>  Created in NX1899.0.0  <br> 

class PartOrientationAnalysisResult(AnalysisResult): 
    """
     This can be created using a <ja_class>NXOpen.Validate.CheckPartOrientationBuilder</ja_class> object.
    """


    ##  Represents the index of checker used for part orientation optimization 
    ##  Projected Surface Area Checker 
    class CheckerIndex(Enum):
        """
        Members Include: <Minimum> <SurfaceArea> <SupportVolume> <PrintTime> <Overheat> <Maximum>
        """
        Minimum: int
        SurfaceArea: int
        SupportVolume: int
        PrintTime: int
        Overheat: int
        Maximum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOrientationAnalysisResult.CheckerIndex:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the checker value and range for specific checker 
    class CheckerValues:
        """
         Represents the checker value and range for specific checker 
        """
        ## Getter for property :(@link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink) MCheckerIndex
        ## Index of the checker
        ## @return @link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink
        @property
        def MCheckerIndex(self) -> PartOrientationAnalysisResult.CheckerIndex:
            """
            Getter for property MCheckerIndex
            Index of the checker

            """
            pass
        
        ## Setter for property :(@link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink) MCheckerIndex
        @MCheckerIndex.setter
        def MCheckerIndex(self, value: PartOrientationAnalysisResult.CheckerIndex):
            """
            Getter for property MCheckerIndex
            Index of the checker
            Setter for property MCheckerIndex
            Index of the checker

            """
            pass
        
        ## Getter for property :(float) MCheckerMinValue
        ## Minimum value of checker
        ## @return float
        @property
        def MCheckerMinValue(self) -> float:
            """
            Getter for property MCheckerMinValue
            Minimum value of checker

            """
            pass
        
        ## Setter for property :(float) MCheckerMinValue
        @MCheckerMinValue.setter
        def MCheckerMinValue(self, value: float):
            """
            Getter for property MCheckerMinValue
            Minimum value of checker
            Setter for property MCheckerMinValue
            Minimum value of checker

            """
            pass
        
        ## Getter for property :(float) MCheckerValue
        ## Current value of checker
        ## @return float
        @property
        def MCheckerValue(self) -> float:
            """
            Getter for property MCheckerValue
            Current value of checker

            """
            pass
        
        ## Setter for property :(float) MCheckerValue
        @MCheckerValue.setter
        def MCheckerValue(self, value: float):
            """
            Getter for property MCheckerValue
            Current value of checker
            Setter for property MCheckerValue
            Current value of checker

            """
            pass
        
        ## Getter for property :(float) MCheckerMaxValue
        ## Maximum value of checker
        ## @return float
        @property
        def MCheckerMaxValue(self) -> float:
            """
            Getter for property MCheckerMaxValue
            Maximum value of checker

            """
            pass
        
        ## Setter for property :(float) MCheckerMaxValue
        @MCheckerMaxValue.setter
        def MCheckerMaxValue(self, value: float):
            """
            Getter for property MCheckerMaxValue
            Maximum value of checker
            Setter for property MCheckerMaxValue
            Maximum value of checker

            """
            pass
        
    
    
    ##  Get minimum orientation for specific checker 
    ##  @return A tuple consisting of (origin, orientation, checker_values). 
    ##  - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
    ##  - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
    ##  - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="checker_index"> (@link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink) </param>
    @staticmethod
    def GetMinimumOrientation(analysis_result: PartOrientationAnalysisResult, checker_index: PartOrientationAnalysisResult.CheckerIndex) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get minimum orientation for specific checker 
         @return A tuple consisting of (origin, orientation, checker_values). 
         - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
         - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
         - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range .

        """
        pass
    
    ##  Get the number of optimal solutions
    ##  @return num_of_optimum_orientations (int):  Num of optimum orientation available .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNumOfOptimumOrientations(analysis_result: PartOrientationAnalysisResult) -> int:
        """
         Get the number of optimal solutions
         @return num_of_optimum_orientations (int):  Num of optimum orientation available .
        """
        pass
    
    ##  Get the optimum orientation at given index
    ##  @return A tuple consisting of (origin, orientation, checker_values). 
    ##  - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
    ##  - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
    ##  - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range. .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Index of optimum solution, should be within [0, num_of_optimum_orientations) 
    @staticmethod
    def GetOptimumOrientation(analysis_result: PartOrientationAnalysisResult, optimum_orientation_index: int) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, List[PartOrientationAnalysisResult.CheckerValues]]:
        """
         Get the optimum orientation at given index
         @return A tuple consisting of (origin, orientation, checker_values). 
         - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. Origin for the optimum orientation .
         - orientation is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. Z direction of the optimum orientation .
         - checker_values is: @link PartOrientationAnalysisResult.CheckerValues List[NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues]@endlink. The values of checker and its range. .

        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Class for Print Time Parameter for Powder Bed Fusion type printer 
## 
##   <br>  Created in NX1899.0.0  <br> 

class PBFPrintTimeParameter(NXOpen.TaggedObject): 
    """ Class for Print Time Parameter for Powder Bed Fusion type printer """


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HatchSpacing
    ##   the Hatch Distance(Hatch Spacing) for printing process.  
    ##    Specify the width of melted metal powder along the laser path.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HatchSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HatchSpacing
          the Hatch Distance(Hatch Spacing) for printing process.  
           Specify the width of melted metal powder along the laser path.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IslandLength
    ##   the Hatch Pattern Length(Island Length) for printing process.  
    ##    
    ##         Specify the average length of tile within the laser does crosshatching.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def IslandLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) IslandLength
          the Hatch Pattern Length(Island Length) for printing process.  
           
                Specify the average length of tile within the laser does crosshatching.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerThickness
    ##   the Layer thickness or slice thickness for printing process.  
    ##   
    ##         Specify the thickness of material to be added on each layer.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LayerThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LayerThickness
          the Layer thickness or slice thickness for printing process.  
          
                Specify the thickness of material to be added on each layer.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RecoatingTime
    ##   the Recoatig time or Time to lay the powder for each layer for printing process.  
    ##   
    ##         Specify the time needed to add a new layer of metal powder.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RecoatingTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RecoatingTime
          the Recoatig time or Time to lay the powder for each layer for printing process.  
          
                Specify the time needed to add a new layer of metal powder.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SkyWritingTime
    ##   the Sky writing time of the laser for printing process.  
    ##    
    ##         Specify the time the laser needs to decelerate and accelerate
    ##         again when changing its scan direction.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SkyWritingTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SkyWritingTime
          the Sky writing time of the laser for printing process.  
           
                Specify the time the laser needs to decelerate and accelerate
                again when changing its scan direction.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TravelSpeed
    ##   the Scan Speed(Travel Speed) of laser for printing process.  
    ##    Specify the speed of the print path.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TravelSpeed(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TravelSpeed
          the Scan Speed(Travel Speed) of laser for printing process.  
           Specify the speed of the print path.   
         
        """
        pass
    
import NXOpen
## 
##      Represents an NX @link NXOpen::Validate::PersistentResultCollection NXOpen::Validate::PersistentResultCollection@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class PersistentResultCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX <ja_class>NXOpen.Validate.PersistentResultCollection</ja_class> object.
    """
    pass


import NXOpen
## 
##      Represents a @link NXOpen::Validate::PersistentResult NXOpen::Validate::PersistentResult@endlink  object.
##     
## 
##   <br>  Created in NX1872.0.0  <br> 

class PersistentResult(NXOpen.NXObject): 
    """
     Represents a <ja_class>NXOpen.Validate.PersistentResult</ja_class> object.
    """


    ## Getter for property: (str) CheckerClassId
    ##   the checker class id.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def CheckerClassId(self) -> str:
        """
        Getter for property: (str) CheckerClassId
          the checker class id.  
             
         
        """
        pass
    
    ## Setter for property: (str) CheckerClassId

    ##   the checker class id.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @CheckerClassId.setter
    def CheckerClassId(self, class_id: str):
        """
        Setter for property: (str) CheckerClassId
          the checker class id.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel
    ##   the error level.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Validation.Result
    @property
    def ErrorLevel(self) -> NXOpen.Validation.Result:
        """
        Getter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel
          the error level.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel

    ##   the error level.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @ErrorLevel.setter
    def ErrorLevel(self, error_level: NXOpen.Validation.Result):
        """
        Setter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) ErrorLevel
          the error level.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UpToDateStatus
    ##   the result's uptodate status.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def UpToDateStatus(self) -> bool:
        """
        Getter for property: (bool) UpToDateStatus
          the result's uptodate status.  
             
         
        """
        pass
    
    ##  Add the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddTrackingObjects(persistentResult: PersistentResult, key: str, objects: List[NXOpen.TaggedObject]) -> None:
        """
         Add the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects.
        """
        pass
    
    ##  Get the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects which trigger the @link Validate::PersistentResult Validate::PersistentResult@endlink  re-run when modified. For example, if a PersistentResult tracks a Face, it will re-run when the Face is modfied.
    ##  @return objects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):   .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="key"> (str) </param>
    def GetTrackingObjects(persistentResult: PersistentResult, key: str) -> List[NXOpen.TaggedObject]:
        """
         Get the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects which trigger the @link Validate::PersistentResult Validate::PersistentResult@endlink  re-run when modified. For example, if a PersistentResult tracks a Face, it will re-run when the Face is modfied.
         @return objects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):   .
        """
        pass
    
## 
##      This can be created using a @link NXOpen::Validate::PorosityAnalysisResult NXOpen::Validate::PorosityAnalysisResult@endlink  object.
##     
## 
##   <br>  Created in NX1926.0.0  <br> 

class PorosityAnalysisResult(AnalysisResult): 
    """
     This can be created using a <ja_class>NXOpen.Validate.PorosityAnalysisResult</ja_class> object.
    """
    pass


import NXOpen
##   @brief Defines a checker profile. 
## 
##  
##       <br> Profile definition contains the information of the class name, the parameter values, 
##      and the child checkers and so on. These informations are used to create profile instance for customization
##      of parameters. <br> 
##      <br> To create a new instance of this class, use @link NXOpen::Validate::ValidationManager::DefineCheckerProfile  NXOpen::Validate::ValidationManager::DefineCheckerProfile @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ProfileDefinition(NXOpen.TransientObject): 
    """ <summary>Defines a checker profile.</summary>
     <para>Profile definition contains the information of the class name, the parameter values, 
     and the child checkers and so on. These informations are used to create profile instance for customization
     of parameters.</para>
    """


    ##  Add child checker and its customization parameters to this profile definition.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="checkerClassId"> (str) </param>
    ## <param name="parameters"> (@link Parameter List[NXOpen.Validate.Parameter]@endlink) </param>
    def AddChildChecker(profileDefinition: ProfileDefinition, checkerClassId: str, parameters: List[Parameter]) -> None:
        """
         Add child checker and its customization parameters to this profile definition.
        """
        pass
    
    ##  User defined method that is called when Check-Mate customizes a checker profile instance.
    ## A callback definition with the following input arguments: 
    ##  - @link CheckerNode NXOpen.Validate.CheckerNode@endlink
    ##  and no return type
    CustomizationHandler = Callable[[CheckerNode], None]
    
    
    ##  Frees resources associated with the instance.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(profileDefinition: ProfileDefinition) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
    
    ##  User defined method that is called when Check-Mate shows checker profile document.
    ## A callback definition with the following input arguments: 
    ##  - @link CheckerNode NXOpen.Validate.CheckerNode@endlink
    ##  and no return type
    DocumentationHandler = Callable[[CheckerNode], None]
    
    
    ##  Sets if the checker profile can be customized by user.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="allowUserCustomize"> (bool) </param>
    def SetAllowUserCustomize(profileDefinition: ProfileDefinition, allowUserCustomize: bool) -> None:
        """
         Sets if the checker profile can be customized by user.
        """
        pass
    
    ##  Sets checker profile customization handler. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="customize"> (@link ProfileDefinition.CustomizationHandler NXOpen.Validate.ProfileDefinition.CustomizationHandler@endlink) </param>
    def SetCustomizationHandler(profileDefinition: ProfileDefinition, customize: ProfileDefinition.CustomizationHandler) -> None:
        """
         Sets checker profile customization handler. 
        """
        pass
    
    ##  Sets checker profile document handler. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="document"> (@link ProfileDefinition.DocumentationHandler NXOpen.Validate.ProfileDefinition.DocumentationHandler@endlink) </param>
    def SetDocumentationHandler(profileDefinition: ProfileDefinition, document: ProfileDefinition.DocumentationHandler) -> None:
        """
         Sets checker profile document handler. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Validate::RequirementCollection::CreateRequirementBuilder  NXOpen::Validate::RequirementCollection::CreateRequirementBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataTypeOption </term> <description> 
##  
## Number </description> </item> 
## 
## <item><term> 
##  
## DefinitionMethodOption </term> <description> 
##  
## SingleSidedComparison </description> </item> 
## 
## <item><term> 
##  
## RelationalOperatorOption </term> <description> 
##  
## Equal </description> </item> 
## 
## <item><term> 
##  
## RelationalOperatorOptionOnMaximumValue </term> <description> 
##  
## LessThan </description> </item> 
## 
## <item><term> 
##  
## RelationalOperatorOptionOnMinimumValue </term> <description> 
##  
## LessThan </description> </item> 
## 
## <item><term> 
##  
## SeverityOption </term> <description> 
##  
## Error </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.5.0  <br> 

class RequirementBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Validate.Requirement</ja_class> builder """


    ##  This enum represents the data type of the value in requirement 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Number</term><description> 
    ## </description> </item><item><term> 
    ## String</term><description> 
    ## </description> </item><item><term> 
    ## Boolean</term><description> 
    ## </description> </item><item><term> 
    ## Integer</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item></list>
    class DataTypeOptions(Enum):
        """
        Members Include: <Number> <String> <Boolean> <Integer> <Point>
        """
        Number: int
        String: int
        Boolean: int
        Integer: int
        Point: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.DataTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the type of requirement definition method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SingleSidedComparison</term><description> 
    ## </description> </item><item><term> 
    ## DoubleSidedComparison</term><description> 
    ## </description> </item><item><term> 
    ## SetOfValues</term><description> 
    ## </description> </item><item><term> 
    ## Formula</term><description> 
    ## </description> </item></list>
    class DefinitionMethodOptions(Enum):
        """
        Members Include: <SingleSidedComparison> <DoubleSidedComparison> <SetOfValues> <Formula>
        """
        SingleSidedComparison: int
        DoubleSidedComparison: int
        SetOfValues: int
        Formula: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.DefinitionMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   This enum represents the relational operator for comparing values 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Equal</term><description> 
    ## </description> </item><item><term> 
    ## NotEqual</term><description> 
    ## </description> </item><item><term> 
    ## LessThan</term><description> 
    ## </description> </item><item><term> 
    ## LessThanOrEqual</term><description> 
    ## </description> </item><item><term> 
    ## GreaterThan</term><description> 
    ## </description> </item><item><term> 
    ## GreaterThanOrEqual</term><description> 
    ## </description> </item></list>
    class RelationalOperatorOptions(Enum):
        """
        Members Include: <Equal> <NotEqual> <LessThan> <LessThanOrEqual> <GreaterThan> <GreaterThanOrEqual>
        """
        Equal: int
        NotEqual: int
        LessThan: int
        LessThanOrEqual: int
        GreaterThan: int
        GreaterThanOrEqual: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.RelationalOperatorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   This enum represents the type of requirement 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ValidationLimit</term><description> 
    ## </description> </item><item><term> 
    ## DesignLimit</term><description> 
    ## </description> </item></list>
    class RequirementTypeOptions(Enum):
        """
        Members Include: <ValidationLimit> <DesignLimit>
        """
        ValidationLimit: int
        DesignLimit: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.RequirementTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the severity level when a requirement is not satisfied 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Error</term><description> 
    ## </description> </item><item><term> 
    ## Warning</term><description> 
    ## </description> </item><item><term> 
    ## Information</term><description> 
    ## </description> </item></list>
    class SeverityOptions(Enum):
        """
        Members Include: <Error> <Warning> <Information>
        """
        Error: int
        Warning: int
        Information: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementBuilder.SeverityOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link RequirementBuilder.DataTypeOptions NXOpen.Validate.RequirementBuilder.DataTypeOptions@endlink) DataTypeOption
    ##   the data type option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementBuilder.DataTypeOptions
    @property
    def DataTypeOption(self) -> RequirementBuilder.DataTypeOptions:
        """
        Getter for property: (@link RequirementBuilder.DataTypeOptions NXOpen.Validate.RequirementBuilder.DataTypeOptions@endlink) DataTypeOption
          the data type option   
            
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.DataTypeOptions NXOpen.Validate.RequirementBuilder.DataTypeOptions@endlink) DataTypeOption

    ##   the data type option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DataTypeOption.setter
    def DataTypeOption(self, dataTypeOption: RequirementBuilder.DataTypeOptions):
        """
        Setter for property: (@link RequirementBuilder.DataTypeOptions NXOpen.Validate.RequirementBuilder.DataTypeOptions@endlink) DataTypeOption
          the data type option   
            
         
        """
        pass
    
    ## Getter for property: (@link RequirementBuilder.DefinitionMethodOptions NXOpen.Validate.RequirementBuilder.DefinitionMethodOptions@endlink) DefinitionMethodOption
    ##   the definition method option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementBuilder.DefinitionMethodOptions
    @property
    def DefinitionMethodOption(self) -> RequirementBuilder.DefinitionMethodOptions:
        """
        Getter for property: (@link RequirementBuilder.DefinitionMethodOptions NXOpen.Validate.RequirementBuilder.DefinitionMethodOptions@endlink) DefinitionMethodOption
          the definition method option   
            
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.DefinitionMethodOptions NXOpen.Validate.RequirementBuilder.DefinitionMethodOptions@endlink) DefinitionMethodOption

    ##   the definition method option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DefinitionMethodOption.setter
    def DefinitionMethodOption(self, definitionMethodOption: RequirementBuilder.DefinitionMethodOptions):
        """
        Setter for property: (@link RequirementBuilder.DefinitionMethodOptions NXOpen.Validate.RequirementBuilder.DefinitionMethodOptions@endlink) DefinitionMethodOption
          the definition method option   
            
         
        """
        pass
    
    ## Getter for property: (str) DoubleSidedMaximumValue
    ##   the maximum value in double sided comparison   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DoubleSidedMaximumValue(self) -> str:
        """
        Getter for property: (str) DoubleSidedMaximumValue
          the maximum value in double sided comparison   
            
         
        """
        pass
    
    ## Setter for property: (str) DoubleSidedMaximumValue

    ##   the maximum value in double sided comparison   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DoubleSidedMaximumValue.setter
    def DoubleSidedMaximumValue(self, doubleSidedMaximumValue: str):
        """
        Setter for property: (str) DoubleSidedMaximumValue
          the maximum value in double sided comparison   
            
         
        """
        pass
    
    ## Getter for property: (str) DoubleSidedMinimumValue
    ##   the minimum value in double sided comparison   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def DoubleSidedMinimumValue(self) -> str:
        """
        Getter for property: (str) DoubleSidedMinimumValue
          the minimum value in double sided comparison   
            
         
        """
        pass
    
    ## Setter for property: (str) DoubleSidedMinimumValue

    ##   the minimum value in double sided comparison   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @DoubleSidedMinimumValue.setter
    def DoubleSidedMinimumValue(self, doubleSidedMinimumValue: str):
        """
        Setter for property: (str) DoubleSidedMinimumValue
          the minimum value in double sided comparison   
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##    @brief  the user defined formula.  
    ##    Only effective when 
    ##         @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption@endlink  is set to 
    ##         @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  
    ## 
    ##  
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
           @brief  the user defined formula.  
           Only effective when 
                @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption@endlink  is set to 
                @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  
        
         
                  
         
        """
        pass
    
    ## Setter for property: (str) Formula

    ##    @brief  the user defined formula.  
    ##    Only effective when 
    ##         @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption@endlink  is set to 
    ##         @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  
    ## 
    ##  
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Formula.setter
    def Formula(self, formula: str):
        """
        Setter for property: (str) Formula
           @brief  the user defined formula.  
           Only effective when 
                @link NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption NXOpen::Validate::RequirementBuilder::SetDefinitionMethodOption@endlink  is set to 
                @link NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula NXOpen::Validate::RequirementBuilder::DefinitionMethodOptionsFormula@endlink .  
        
         
                  
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of requirement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of requirement   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name of requirement   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name of requirement   
            
         
        """
        pass
    
    ## Getter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOption
    ##   the relational operator option between expression label and the value in single sided comparison   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementBuilder.RelationalOperatorOptions
    @property
    def RelationalOperatorOption(self) -> RequirementBuilder.RelationalOperatorOptions:
        """
        Getter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOption
          the relational operator option between expression label and the value in single sided comparison   
            
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOption

    ##   the relational operator option between expression label and the value in single sided comparison   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RelationalOperatorOption.setter
    def RelationalOperatorOption(self, relationalOperatorOption: RequirementBuilder.RelationalOperatorOptions):
        """
        Setter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOption
          the relational operator option between expression label and the value in single sided comparison   
            
         
        """
        pass
    
    ## Getter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMaximumValue
    ##   the relational operator between expression label and maximum value in double sided comparison:
    ##              [expression] &lt; or &lt;= maximum value.  
    ##   
    ##             The valid operator is either LessThan or LessThanOrEqual.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementBuilder.RelationalOperatorOptions
    @property
    def RelationalOperatorOptionOnMaximumValue(self) -> RequirementBuilder.RelationalOperatorOptions:
        """
        Getter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMaximumValue
          the relational operator between expression label and maximum value in double sided comparison:
                     [expression] &lt; or &lt;= maximum value.  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMaximumValue

    ##   the relational operator between expression label and maximum value in double sided comparison:
    ##              [expression] &lt; or &lt;= maximum value.  
    ##   
    ##             The valid operator is either LessThan or LessThanOrEqual.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RelationalOperatorOptionOnMaximumValue.setter
    def RelationalOperatorOptionOnMaximumValue(self, relationalOperatorOnMaximumValue: RequirementBuilder.RelationalOperatorOptions):
        """
        Setter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMaximumValue
          the relational operator between expression label and maximum value in double sided comparison:
                     [expression] &lt; or &lt;= maximum value.  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    
    ## Getter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMinimumValue
    ##   the relational operator between minimum value and expression label in double sided comparison:
    ##              minimum value &lt; or &lt;= [expression].  
    ##   
    ##             The valid operator is either LessThan or LessThanOrEqual.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementBuilder.RelationalOperatorOptions
    @property
    def RelationalOperatorOptionOnMinimumValue(self) -> RequirementBuilder.RelationalOperatorOptions:
        """
        Getter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMinimumValue
          the relational operator between minimum value and expression label in double sided comparison:
                     minimum value &lt; or &lt;= [expression].  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMinimumValue

    ##   the relational operator between minimum value and expression label in double sided comparison:
    ##              minimum value &lt; or &lt;= [expression].  
    ##   
    ##             The valid operator is either LessThan or LessThanOrEqual.
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RelationalOperatorOptionOnMinimumValue.setter
    def RelationalOperatorOptionOnMinimumValue(self, relationalOperatorOnMinimumValue: RequirementBuilder.RelationalOperatorOptions):
        """
        Setter for property: (@link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink) RelationalOperatorOptionOnMinimumValue
          the relational operator between minimum value and expression label in double sided comparison:
                     minimum value &lt; or &lt;= [expression].  
          
                    The valid operator is either LessThan or LessThanOrEqual.
                  
         
        """
        pass
    
    ## Getter for property: (float) RequirementTolerance
    ##   the tolerance for point type requirement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def RequirementTolerance(self) -> float:
        """
        Getter for property: (float) RequirementTolerance
          the tolerance for point type requirement   
            
         
        """
        pass
    
    ## Setter for property: (float) RequirementTolerance

    ##   the tolerance for point type requirement   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RequirementTolerance.setter
    def RequirementTolerance(self, requirementTolerance: float):
        """
        Setter for property: (float) RequirementTolerance
          the tolerance for point type requirement   
            
         
        """
        pass
    
    ## Getter for property: (@link RequirementBuilder.RequirementTypeOptions NXOpen.Validate.RequirementBuilder.RequirementTypeOptions@endlink) RequirementTypeOption
    ##   the requirement type option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return RequirementBuilder.RequirementTypeOptions
    @property
    def RequirementTypeOption(self) -> RequirementBuilder.RequirementTypeOptions:
        """
        Getter for property: (@link RequirementBuilder.RequirementTypeOptions NXOpen.Validate.RequirementBuilder.RequirementTypeOptions@endlink) RequirementTypeOption
          the requirement type option   
            
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.RequirementTypeOptions NXOpen.Validate.RequirementBuilder.RequirementTypeOptions@endlink) RequirementTypeOption

    ##   the requirement type option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RequirementTypeOption.setter
    def RequirementTypeOption(self, requirementTypeOption: RequirementBuilder.RequirementTypeOptions):
        """
        Setter for property: (@link RequirementBuilder.RequirementTypeOptions NXOpen.Validate.RequirementBuilder.RequirementTypeOptions@endlink) RequirementTypeOption
          the requirement type option   
            
         
        """
        pass
    
    ## Getter for property: (@link RequirementBuilder.SeverityOptions NXOpen.Validate.RequirementBuilder.SeverityOptions@endlink) SeverityOption
    ##   the severity option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementBuilder.SeverityOptions
    @property
    def SeverityOption(self) -> RequirementBuilder.SeverityOptions:
        """
        Getter for property: (@link RequirementBuilder.SeverityOptions NXOpen.Validate.RequirementBuilder.SeverityOptions@endlink) SeverityOption
          the severity option   
            
         
        """
        pass
    
    ## Setter for property: (@link RequirementBuilder.SeverityOptions NXOpen.Validate.RequirementBuilder.SeverityOptions@endlink) SeverityOption

    ##   the severity option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SeverityOption.setter
    def SeverityOption(self, severityOption: RequirementBuilder.SeverityOptions):
        """
        Setter for property: (@link RequirementBuilder.SeverityOptions NXOpen.Validate.RequirementBuilder.SeverityOptions@endlink) SeverityOption
          the severity option   
            
         
        """
        pass
    
    ## Getter for property: (str) SingleSidedValue
    ##   the value for single sided comparison   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def SingleSidedValue(self) -> str:
        """
        Getter for property: (str) SingleSidedValue
          the value for single sided comparison   
            
         
        """
        pass
    
    ## Setter for property: (str) SingleSidedValue

    ##   the value for single sided comparison   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SingleSidedValue.setter
    def SingleSidedValue(self, singleSidedValue: str):
        """
        Setter for property: (str) SingleSidedValue
          the value for single sided comparison   
            
         
        """
        pass
    
    ##  Returns the requirement description 
    ##  @return requirementDescription (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetRequirementDescription(self) -> List[str]:
        """
         Returns the requirement description 
         @return requirementDescription (List[str]): .
        """
        pass
    
    ##  Returns the valid values 
    ##  @return validValues (List[str]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetValidValues(self) -> List[str]:
        """
         Returns the valid values 
         @return validValues (List[str]): .
        """
        pass
    
    ##  Sets the requirement description 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetRequirementDescription(self, requirementDescription: List[str]) -> None:
        """
         Sets the requirement description 
        """
        pass
    
    ##  Sets the valid values 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  
    def SetValidValues(self, validValues: List[str]) -> None:
        """
         Sets the valid values 
        """
        pass
    
import NXOpen
## 
##      Represents an NX @link NXOpen::Validate::RequirementCheckCollection NXOpen::Validate::RequirementCheckCollection@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class RequirementCheckCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX <ja_class>NXOpen.Validate.RequirementCheckCollection</ja_class> object.
    """


    ##  Create a requirement check 
    ##  @return requirementCheck (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def CreateRequirementCheck(part: RequirementCheckCollection) -> RequirementCheck:
        """
         Create a requirement check 
         @return requirementCheck (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
        """
        pass
    
import NXOpen
## 
##      Represents an NX @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Validate::RequirementCheckCollection::CreateRequirementCheck  NXOpen::Validate::RequirementCheckCollection::CreateRequirementCheck @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class RequirementCheck(NXOpen.Validation): 
    """
     Represents an NX <ja_class>NXOpen.Validate.RequirementCheck</ja_class> object.
    """


    ##  This enum represents the Save Results to Teamcenter option 
    ##  Do not perform save. 
    class SaveResultsToTeamcenterOptions(Enum):
        """
        Members Include: <DoNotSave> <SaveIfPassed> <AlwaysSave>
        """
        DoNotSave: int
        SaveIfPassed: int
        AlwaysSave: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementCheck.SaveResultsToTeamcenterOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) CheckName
    ##   the name of requirement check shown in Requirements Validation dialog   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def CheckName(self) -> str:
        """
        Getter for property: (str) CheckName
          the name of requirement check shown in Requirements Validation dialog   
            
         
        """
        pass
    
    ## Setter for property: (str) CheckName

    ##   the name of requirement check shown in Requirements Validation dialog   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @CheckName.setter
    def CheckName(self, checkName: str):
        """
        Setter for property: (str) CheckName
          the name of requirement check shown in Requirements Validation dialog   
            
         
        """
        pass
    
    ## Getter for property: (str) Formula
    ##   the formula of requirement check   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Formula(self) -> str:
        """
        Getter for property: (str) Formula
          the formula of requirement check   
            
         
        """
        pass
    
    ## Getter for property: (@link Requirement NXOpen.Validate.Requirement@endlink) ParentRequirement
    ##   the parent @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return Requirement
    @property
    def ParentRequirement(self) -> Requirement:
        """
        Getter for property: (@link Requirement NXOpen.Validate.Requirement@endlink) ParentRequirement
          the parent @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link Requirement NXOpen.Validate.Requirement@endlink) ParentRequirement

    ##   the parent @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @ParentRequirement.setter
    def ParentRequirement(self, parentRequirement: Requirement):
        """
        Setter for property: (@link Requirement NXOpen.Validate.Requirement@endlink) ParentRequirement
          the parent @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.Validate.RequirementCheck.SaveResultsToTeamcenterOptions@endlink) SaveResultsToTeamcenterOption
    ##   the Save Results to Teamcenter option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return RequirementCheck.SaveResultsToTeamcenterOptions
    @property
    def SaveResultsToTeamcenterOption(self) -> RequirementCheck.SaveResultsToTeamcenterOptions:
        """
        Getter for property: (@link RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.Validate.RequirementCheck.SaveResultsToTeamcenterOptions@endlink) SaveResultsToTeamcenterOption
          the Save Results to Teamcenter option   
            
         
        """
        pass
    
    ## Setter for property: (@link RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.Validate.RequirementCheck.SaveResultsToTeamcenterOptions@endlink) SaveResultsToTeamcenterOption

    ##   the Save Results to Teamcenter option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SaveResultsToTeamcenterOption.setter
    def SaveResultsToTeamcenterOption(self, option: RequirementCheck.SaveResultsToTeamcenterOptions):
        """
        Setter for property: (@link RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.Validate.RequirementCheck.SaveResultsToTeamcenterOptions@endlink) SaveResultsToTeamcenterOption
          the Save Results to Teamcenter option   
            
         
        """
        pass
    
    ##  Sets the formula of requirement check. The requirement check will be re-evaluated. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="formula"> (str) </param>
    def SetFormula(requirementCheck: RequirementCheck, formula: str) -> None:
        """
         Sets the formula of requirement check. The requirement check will be re-evaluated. 
        """
        pass
    
import NXOpen
## 
##      Represents an NX @link NXOpen::Validate::RequirementCollection NXOpen::Validate::RequirementCollection@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class RequirementCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX <ja_class>NXOpen.Validate.RequirementCollection</ja_class> object.
    """


    ##  This enum represents the type of external source where requirement is defined 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LocalFile</term><description> 
    ## </description> </item><item><term> 
    ## TeamcenterFile</term><description> 
    ## </description> </item><item><term> 
    ## Teamcenter</term><description> 
    ## </description> </item><item><term> 
    ## MeasurableAttribute</term><description> 
    ## </description> </item></list>
    class SourceTypeOptions(Enum):
        """
        Members Include: <LocalFile> <TeamcenterFile> <Teamcenter> <MeasurableAttribute>
        """
        LocalFile: int
        TeamcenterFile: int
        Teamcenter: int
        MeasurableAttribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RequirementCollection.SourceTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) RevisionRule
    ##   the revision rule for requirement from Teamcenter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def RevisionRule(self) -> str:
        """
        Getter for property: (str) RevisionRule
          the revision rule for requirement from Teamcenter   
            
         
        """
        pass
    
    ## Setter for property: (str) RevisionRule

    ##   the revision rule for requirement from Teamcenter   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @RevisionRule.setter
    def RevisionRule(self, rule: str):
        """
        Setter for property: (str) RevisionRule
          the revision rule for requirement from Teamcenter   
            
         
        """
        pass
    
    ##  Creates a @link NXOpen::Validate::RequirementBuilder NXOpen::Validate::RequirementBuilder@endlink  
    ##  @return builder (@link RequirementBuilder NXOpen.Validate.RequirementBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="requirement"> (@link Requirement NXOpen.Validate.Requirement@endlink) </param>
    def CreateRequirementBuilder(part: RequirementCollection, requirement: Requirement) -> RequirementBuilder:
        """
         Creates a @link NXOpen::Validate::RequirementBuilder NXOpen::Validate::RequirementBuilder@endlink  
         @return builder (@link RequirementBuilder NXOpen.Validate.RequirementBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  with the given identifier.
    ##             An exception will be thrown if no object can be found with given identifier. 
    ##  @return requirement (@link Requirement NXOpen.Validate.Requirement@endlink):  @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  with the identifier .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  The identifier of the @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  
    def FindObject(part: RequirementCollection, id: str) -> Requirement:
        """
         Finds the @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  with the given identifier.
                    An exception will be thrown if no object can be found with given identifier. 
         @return requirement (@link Requirement NXOpen.Validate.Requirement@endlink):  @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  with the identifier .
        """
        pass
    
    ##   Loads @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  from external source.
    ##              The source can be local file, Teamcenter requirement item or item revision, and Teamcenter spreadsheet dataset
    ##              for which the input sourceType is LocalFile, Teamcenter and TeamcenterFile respectively.
    ##          <br/>
    ## 
    ##              Example inputs when sourceType is LocalFile
    ##          <ol>
    ##          <li>source: "C:\requirement.xml" or "C:\requirement_spreadsheet.xls"</li>
    ##          <li>revision: empty string</li>
    ##          <li>project: "category_A" It's a project node name in the source XML file or a sheet name in the source spreadsheet file.</li>
    ##          </ol>
    ##          <br/>
    ## 
    ##              Example inputs when sourceType is Teamcenter
    ##          
    ##              If source is item revision 000084/A:
    ##          <ol>
    ##          <li>source: "000084"</li>
    ##          <li>revision: "A"</li>
    ##          <li>project: empty string</li>
    ##          </ol>
    ##          
    ##              If source is item 000084:
    ##          <ol>
    ##          <li>source: "000084"</li>
    ##          <li>revision:empty string</li>
    ##          <li>project: empty string</li>
    ##          </ol>
    ##          <br/>
    ##              Example inputs when sourceType is TeamcenterFile
    ##          
    ##              If source is a spreadsheet dataset in an item revision 000085/A:
    ##          <ol>
    ##          <li>source: 000085</li>
    ##          <li>revision: A</li>
    ##          <li>project: "category_A" It's a sheet name in the source spreadsheet.</li>
    ##          </ol>
    ##          
    ##              If source is a spreadsheet dataset in item 000085:
    ##          <ol>
    ##          <li>source: "000085"</li>
    ##          <li>revision: empty string</li>
    ##          <li>project: "category_A" It's a sheet name in the source spreadsheet.</li>
    ##          </ol>
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  Type of the external source 
    def LoadFromExternalSource(part: RequirementCollection, sourceType: RequirementCollection.SourceTypeOptions, source: str, revision: str, project: str) -> None:
        """
          Loads @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  from external source.
                     The source can be local file, Teamcenter requirement item or item revision, and Teamcenter spreadsheet dataset
                     for which the input sourceType is LocalFile, Teamcenter and TeamcenterFile respectively.
                 <br/>
        
                     Example inputs when sourceType is LocalFile
                 <ol>
                 <li>source: "C:\requirement.xml" or "C:\requirement_spreadsheet.xls"</li>
                 <li>revision: empty string</li>
                 <li>project: "category_A" It's a project node name in the source XML file or a sheet name in the source spreadsheet file.</li>
                 </ol>
                 <br/>
        
                     Example inputs when sourceType is Teamcenter
                 
                     If source is item revision 000084/A:
                 <ol>
                 <li>source: "000084"</li>
                 <li>revision: "A"</li>
                 <li>project: empty string</li>
                 </ol>
                 
                     If source is item 000084:
                 <ol>
                 <li>source: "000084"</li>
                 <li>revision:empty string</li>
                 <li>project: empty string</li>
                 </ol>
                 <br/>
                     Example inputs when sourceType is TeamcenterFile
                 
                     If source is a spreadsheet dataset in an item revision 000085/A:
                 <ol>
                 <li>source: 000085</li>
                 <li>revision: A</li>
                 <li>project: "category_A" It's a sheet name in the source spreadsheet.</li>
                 </ol>
                 
                     If source is a spreadsheet dataset in item 000085:
                 <ol>
                 <li>source: "000085"</li>
                 <li>revision: empty string</li>
                 <li>project: "category_A" It's a sheet name in the source spreadsheet.</li>
                 </ol>
                
        """
        pass
    
    ##  Refreshes the requirements from external source. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="requirementTags"> (@link Requirement List[NXOpen.Validate.Requirement]@endlink) </param>
    def RefreshFromExternalSource(part: RequirementCollection, requirementTags: List[Requirement]) -> None:
        """
         Refreshes the requirements from external source. 
        """
        pass
    
import NXOpen
## 
##      Represents a @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::Validate::RequirementBuilder  NXOpen::Validate::RequirementBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class Requirement(NXOpen.NXObject): 
    """
     Represents a <ja_class>NXOpen.Validate.Requirement</ja_class> object.
    """


    ##  Deletes a user requirement and child @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  or removes a external requirement. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Delete(requirement: Requirement) -> None:
        """
         Deletes a user requirement and child @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  or removes a external requirement. 
        """
        pass
    
    ##  Creates a @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  for a requirement
    ##  @return requirementCheck (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ##  name of requirement check 
    def NewCheck(requirement: Requirement, name: str, formula: str) -> RequirementCheck:
        """
         Creates a @link NXOpen::Validate::RequirementCheck NXOpen::Validate::RequirementCheck@endlink  for a requirement
         @return requirementCheck (@link RequirementCheck NXOpen.Validate.RequirementCheck@endlink): .
        """
        pass
    
    ##  Refreshs a requirement from external source.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RefreshFromExternalSource(requirement: Requirement) -> None:
        """
         Refreshs a requirement from external source.
        """
        pass
    
import NXOpen
##  @brief  Represents a check-mate result object.  
## 
##  
##     
## 
##   <br>  Created in NX7.5.0  <br> 

class ResultObject(NXOpen.NXObject): 
    """<summary> Represents a check-mate result object. </summary>
    """


    ##  The type of check result 
    ##  Part 
    class ResultTypes(Enum):
        """
        Members Include: <Part> <Profile> <Test> <Object> <ObjectSet>
        """
        Part: int
        Profile: int
        Test: int
        Object: int
        ObjectSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ResultObject.ResultTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) CategoryName
    ##   the category name of check result.  
    ##   
    ##             Return empty if the ResultObject has no this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def CategoryName(self) -> str:
        """
        Getter for property: (str) CategoryName
          the category name of check result.  
          
                    Return empty if the ResultObject has no this property.
                  
         
        """
        pass
    
    ## Getter for property: (str) ClassName
    ##   the class name of check result.  
    ##   
    ##             Return empty if the ResultObject has no this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
          the class name of check result.  
          
                    Return empty if the ResultObject has no this property.
                  
         
        """
        pass
    
    ## Getter for property: (bool) Disabled
    ##   the disabled status of check result.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def Disabled(self) -> bool:
        """
        Getter for property: (bool) Disabled
          the disabled status of check result.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Object
    ##   the NX object referenced by the check result.  
    ##   
    ##             Return NULL if the ResultObject has no this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def Object(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) Object
          the NX object referenced by the check result.  
          
                    Return NULL if the ResultObject has no this property.
                  
         
        """
        pass
    
    ## Getter for property: (bool) OutOfDate
    ##   the out of date status of check result.  
    ##   
    ##         Returns error code if part is unloaded. Result of unloaded part is assumed up to date. The program may not be able to detect the modifications in the part.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def OutOfDate(self) -> bool:
        """
        Getter for property: (bool) OutOfDate
          the out of date status of check result.  
          
                Returns error code if part is unloaded. Result of unloaded part is assumed up to date. The program may not be able to detect the modifications in the part.
                  
         
        """
        pass
    
    ## Getter for property: (@link Override NXOpen.Validate.Override@endlink) Override
    ##   the override request object of check result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return Override
    @property
    def Override(self) -> Override:
        """
        Getter for property: (@link Override NXOpen.Validate.Override@endlink) Override
          the override request object of check result   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) Status
    ##   the error status of check result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Validation.Result
    @property
    def Status(self) -> NXOpen.Validation.Result:
        """
        Getter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) Status
          the error status of check result   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) Status

    ##   the error status of check result   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Status.setter
    def Status(self, status: NXOpen.Validation.Result):
        """
        Setter for property: (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink) Status
          the error status of check result   
            
         
        """
        pass
    
    ## Getter for property: (int) TotalObjectsCount
    ##   the total objects count of check result.  
    ##   
    ##             Return zero if the ResultObject has no this property.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return int
    @property
    def TotalObjectsCount(self) -> int:
        """
        Getter for property: (int) TotalObjectsCount
          the total objects count of check result.  
          
                    Return zero if the ResultObject has no this property.
                  
         
        """
        pass
    
    ## Getter for property: (@link ResultObject.ResultTypes NXOpen.Validate.ResultObject.ResultTypes@endlink) Type
    ##   the type of check result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ResultObject.ResultTypes
    @property
    def Type(self) -> ResultObject.ResultTypes:
        """
        Getter for property: (@link ResultObject.ResultTypes NXOpen.Validate.ResultObject.ResultTypes@endlink) Type
          the type of check result   
            
         
        """
        pass
    
    ## Setter for property: (@link ResultObject.ResultTypes NXOpen.Validate.ResultObject.ResultTypes@endlink) Type

    ##   the type of check result   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Type.setter
    def Type(self, type: ResultObject.ResultTypes):
        """
        Setter for property: (@link ResultObject.ResultTypes NXOpen.Validate.ResultObject.ResultTypes@endlink) Type
          the type of check result   
            
         
        """
        pass
    
    ##  
    ##              Ask a single value attribute of check result. 
    ##              Refer to the VARIABLE table column in the section "Variables Supported by Check-Mate Templates" 
    ##              in %UGII_BASE_DIR%\design_tools\checkmate\customization\guide.html for the collection of attribute names. 
    ##              "No" in the "Can be a list of values?" table column indicates it is a single value attribute.
    ##          
    ##  @return value (@link NXOpen.NXObject.AttributeInformation NXOpen.NXObject.AttributeInformation@endlink):  the value name of check result .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## the attribute name of check result
    def AskAttribute(check_result: ResultObject, name: str) -> NXOpen.NXObject.AttributeInformation:
        """
         
                     Ask a single value attribute of check result. 
                     Refer to the VARIABLE table column in the section "Variables Supported by Check-Mate Templates" 
                     in %UGII_BASE_DIR%\design_tools\checkmate\customization\guide.html for the collection of attribute names. 
                     "No" in the "Can be a list of values?" table column indicates it is a single value attribute.
                 
         @return value (@link NXOpen.NXObject.AttributeInformation NXOpen.NXObject.AttributeInformation@endlink):  the value name of check result .
        """
        pass
    
    ##  
    ##              Ask a multi-value attribute of check result. 
    ##              Refer to the VARIABLE table column in the section "Variables Supported by Check-Mate Templates" 
    ##              in %UGII_BASE_DIR%\design_tools\checkmate\customization\guide.html for the collection of attribute names. 
    ##              "Yes" in the "Can be a list of values?" table column indicates it is a multi-value attribute.
    ##          
    ##  @return attributes (@link NXOpen.NXObject.AttributeInformation List[NXOpen.NXObject.AttributeInformation]@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## the attribute name of check result
    def AskAttributes(check_result: ResultObject, name: str) -> List[NXOpen.NXObject.AttributeInformation]:
        """
         
                     Ask a multi-value attribute of check result. 
                     Refer to the VARIABLE table column in the section "Variables Supported by Check-Mate Templates" 
                     in %UGII_BASE_DIR%\design_tools\checkmate\customization\guide.html for the collection of attribute names. 
                     "Yes" in the "Can be a list of values?" table column indicates it is a multi-value attribute.
                 
         @return attributes (@link NXOpen.NXObject.AttributeInformation List[NXOpen.NXObject.AttributeInformation]@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Validate::OverrideBuilder NXOpen::Validate::OverrideBuilder@endlink  
    ##  @return builder (@link OverrideBuilder NXOpen.Validate.OverrideBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ## <param name="override_request"> (@link Override NXOpen.Validate.Override@endlink) </param>
    def CreateOverrideBuilder(check_result: ResultObject, override_request: Override) -> OverrideBuilder:
        """
         Creates a @link NXOpen::Validate::OverrideBuilder NXOpen::Validate::OverrideBuilder@endlink  
         @return builder (@link OverrideBuilder NXOpen.Validate.OverrideBuilder@endlink): .
        """
        pass
    
    ##  Deletes user override request @link NXOpen::Validate::Override NXOpen::Validate::Override@endlink . 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    @staticmethod
    def DeleteOverride(check_result: ResultObject) -> None:
        """
         Deletes user override request @link NXOpen::Validate::Override NXOpen::Validate::Override@endlink . 
        """
        pass
    
import NXOpen
##  Represents a Builder for RuleSave functionality <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class RuleBaseSaveBuilder(NXOpen.Builder): 
    """ Represents a Builder for RuleSave functionality"""


    ## Getter for property: (str) Category
    ##   the category   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##   the category   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Getter for property: (str) ClassID
    ##   the class name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ClassID(self) -> str:
        """
        Getter for property: (str) ClassID
          the class name   
            
         
        """
        pass
    
    ## Setter for property: (str) ClassID

    ##   the class name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ClassID.setter
    def ClassID(self, classID: str):
        """
        Setter for property: (str) ClassID
          the class name   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisabledToggle
    ##   the disabled toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def DisabledToggle(self) -> bool:
        """
        Getter for property: (bool) DisabledToggle
          the disabled toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisabledToggle

    ##   the disabled toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DisabledToggle.setter
    def DisabledToggle(self, disabledToggle: bool):
        """
        Setter for property: (bool) DisabledToggle
          the disabled toggle   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the rule name   
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
          the rule name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the rule name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, ruleName: str):
        """
        Setter for property: (str) Name
          the rule name   
            
         
        """
        pass
    
    ## Getter for property: (bool) SaveLogInPartToggle
    ##   the save log in part toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def SaveLogInPartToggle(self) -> bool:
        """
        Getter for property: (bool) SaveLogInPartToggle
          the save log in part toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) SaveLogInPartToggle

    ##   the save log in part toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SaveLogInPartToggle.setter
    def SaveLogInPartToggle(self, saveLogInPart: bool):
        """
        Setter for property: (bool) SaveLogInPartToggle
          the save log in part toggle   
            
         
        """
        pass
    
    ##  Returns the description 
    ##  @return text (List[str]):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDescription(builder: RuleBaseSaveBuilder) -> List[str]:
        """
         Returns the description 
         @return text (List[str]):  .
        """
        pass
    
    ##  Sets the description 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDescription(builder: RuleBaseSaveBuilder, text: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    
    ##  Sets the rule folder path 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  Rule folder path 
    def SetFolderPath(builder: RuleBaseSaveBuilder, folderPath: str) -> None:
        """
         Sets the rule folder path 
        """
        pass
    
    ##  Sets the rule file name 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  Rule file name 
    def SetRuleFileName(builder: RuleBaseSaveBuilder, ruleFileName: str) -> None:
        """
         Sets the rule file name 
        """
        pass
    
import NXOpen
##  Represents an object that manages checker rule
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class RuleCheckerManager(NXOpen.Object): 
    """ Represents an object that manages checker rule
    """


    ##  The JA method support for create rule properties builder
    ##  @return builder (@link RulePropertiesBuilder NXOpen.Validate.RulePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: ug_kf_author ("UG/Knowledge Fusion - Author")
    ## <param name="ruleInstance"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="readOnly"> (bool) </param>
    def CreateRulePropertiesBuilder(ruleInstance: NXOpen.NXObject, readOnly: bool) -> RulePropertiesBuilder:
        """
         The JA method support for create rule properties builder
         @return builder (@link RulePropertiesBuilder NXOpen.Validate.RulePropertiesBuilder@endlink): .
        """
        pass
    
    ##  The JA method support for create rule save as builder
    ##  @return builder (@link RuleSaveAsBuilder NXOpen.Validate.RuleSaveAsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: ug_kf_author ("UG/Knowledge Fusion - Author")
    ## <param name="ruleInstance"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateRuleSaveAsBuilder(ruleInstance: NXOpen.NXObject) -> RuleSaveAsBuilder:
        """
         The JA method support for create rule save as builder
         @return builder (@link RuleSaveAsBuilder NXOpen.Validate.RuleSaveAsBuilder@endlink): .
        """
        pass
    
    ##  The JA method support for create rule save builder
    ##  @return builder (@link RuleSaveBuilder NXOpen.Validate.RuleSaveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: ug_kf_author ("UG/Knowledge Fusion - Author")
    ## <param name="ruleInstance"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateRuleSaveBuilder(ruleInstance: NXOpen.NXObject) -> RuleSaveBuilder:
        """
         The JA method support for create rule save builder
         @return builder (@link RuleSaveBuilder NXOpen.Validate.RuleSaveBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a Builder for Rule Properties functionality <br> To create a new instance of this class, use @link NXOpen::Validate::RuleCheckerManager::CreateRulePropertiesBuilder  NXOpen::Validate::RuleCheckerManager::CreateRulePropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DisabledToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SaveLogInPartToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class RulePropertiesBuilder(NXOpen.Builder): 
    """ Represents a Builder for Rule Properties functionality"""


    ## Getter for property: (str) Category
    ##   the category   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##   the category   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
          the category   
            
         
        """
        pass
    
    ## Getter for property: (str) ClassID
    ##   the class name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ClassID(self) -> str:
        """
        Getter for property: (str) ClassID
          the class name   
            
         
        """
        pass
    
    ## Setter for property: (str) ClassID

    ##   the class name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ClassID.setter
    def ClassID(self, classID: str):
        """
        Setter for property: (str) ClassID
          the class name   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisabledToggle
    ##   the disabled toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def DisabledToggle(self) -> bool:
        """
        Getter for property: (bool) DisabledToggle
          the disabled toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisabledToggle

    ##   the disabled toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DisabledToggle.setter
    def DisabledToggle(self, disabledToggle: bool):
        """
        Setter for property: (bool) DisabledToggle
          the disabled toggle   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the rule name   
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
          the rule name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the rule name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, ruleName: str):
        """
        Setter for property: (str) Name
          the rule name   
            
         
        """
        pass
    
    ## Getter for property: (bool) SaveLogInPartToggle
    ##   the save log in part toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def SaveLogInPartToggle(self) -> bool:
        """
        Getter for property: (bool) SaveLogInPartToggle
          the save log in part toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) SaveLogInPartToggle

    ##   the save log in part toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SaveLogInPartToggle.setter
    def SaveLogInPartToggle(self, saveLogInPart: bool):
        """
        Setter for property: (bool) SaveLogInPartToggle
          the save log in part toggle   
            
         
        """
        pass
    
    ##  Returns the description 
    ##  @return text (List[str]):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDescription(builder: RulePropertiesBuilder) -> List[str]:
        """
         Returns the description 
         @return text (List[str]):  .
        """
        pass
    
    ##  Sets the description 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDescription(builder: RulePropertiesBuilder, text: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    
##  Represents a Builder for Rule SaveAs functionality <br> To create a new instance of this class, use @link NXOpen::Validate::RuleCheckerManager::CreateRuleSaveAsBuilder  NXOpen::Validate::RuleCheckerManager::CreateRuleSaveAsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DisabledToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SaveLogInPartToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class RuleSaveAsBuilder(RuleBaseSaveBuilder): 
    """ Represents a Builder for Rule SaveAs functionality"""
    pass


##  Represents a Builder for RuleSave functionality <br> To create a new instance of this class, use @link NXOpen::Validate::RuleCheckerManager::CreateRuleSaveBuilder  NXOpen::Validate::RuleCheckerManager::CreateRuleSaveBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DisabledToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SaveLogInPartToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class RuleSaveBuilder(RuleBaseSaveBuilder): 
    """ Represents a Builder for RuleSave functionality"""
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Selection And Placement builder 
## 
##   <br>  Created in NX1899.0.0  <br> 

class SelectionAndPlacementBuilder(NXOpen.TaggedObject): 
    """ Represents a Selection And Placement builder """


    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
    ##   the draw orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
          the draw orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation

    ##   the draw orientation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
          the draw orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
    ##   the draw origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def DrawOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
          the draw origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin

    ##   the draw origin   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
          the draw origin   
            
         
        """
        pass
    
    ##  Returns the selected Bodies or Parts 
    ##  @return targets (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  The targets should be of NXOpen::Body or NXOpen::Part .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTargets(builder: SelectionAndPlacementBuilder) -> List[NXOpen.TaggedObject]:
        """
         Returns the selected Bodies or Parts 
         @return targets (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  The targets should be of NXOpen::Body or NXOpen::Part .
        """
        pass
    
    ##  Set the Bodies or Parts 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The targets should be of NXOpen::Body or NXOpen::Part 
    def SetTargets(builder: SelectionAndPlacementBuilder, targets: List[NXOpen.TaggedObject]) -> None:
        """
         Set the Bodies or Parts 
        """
        pass
    
import NXOpen
##   @brief Represents an object that manages validator and parser associated instance objects. 
## 
##  
##       <br> It handles the creation of new validators and parsers.
##      The ValidationManager also provides @link NXOpen::Validate::ValidationManager::FindValidator NXOpen::Validate::ValidationManager::FindValidator@endlink  to 
##      get validators in current session. <br> 
##      <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class ValidationManager(NXOpen.Object): 
    """ <summary>Represents an object that manages validator and parser associated instance objects.</summary>
     <para>It handles the creation of new validators and parsers.
     The ValidationManager also provides <ja_method>NXOpen.Validate.ValidationManager.FindValidator</ja_method> to 
     get validators in current session.</para>
    """


    ##  Optional settings for defining a @link Validate::Parameter Validate::Parameter@endlink 
    class ParameterOptions:
        """
         Optional settings for defining a @link Validate::Parameter Validate::Parameter@endlink 
        """
        ## Getter for property :(str) Label
        ## Parameter label
        ## @return str
        @property
        def Label(self) -> str:
            """
            Getter for property Label
            Parameter label

            """
            pass
        
        ## Setter for property :(str) Label
        @Label.setter
        def Label(self, value: str):
            """
            Getter for property Label
            Parameter label
            Setter for property Label
            Parameter label

            """
            pass
        
        ## Getter for property :(str) Group
        ## Parameter group.
        ## @return str
        @property
        def Group(self) -> str:
            """
            Getter for property Group
            Parameter group.

            """
            pass
        
        ## Setter for property :(str) Group
        @Group.setter
        def Group(self, value: str):
            """
            Getter for property Group
            Parameter group.
            Setter for property Group
            Parameter group.

            """
            pass
        
        ## Getter for property :(bool) Modifiable
        ## If parameter can be modified.
        ## @return bool
        @property
        def Modifiable(self) -> bool:
            """
            Getter for property Modifiable
            If parameter can be modified.

            """
            pass
        
        ## Setter for property :(bool) Modifiable
        @Modifiable.setter
        def Modifiable(self, value: bool):
            """
            Getter for property Modifiable
            If parameter can be modified.
            Setter for property Modifiable
            If parameter can be modified.

            """
            pass
        
    
    
    ##  User defined method that is called when Check-Mate executes the @link Validate::CheckerNode Validate::CheckerNode@endlink . 
    ## A callback definition with the following input arguments: 
    ##  - @link CheckerNode NXOpen.Validate.CheckerNode@endlink
    ##  and no return type
    DoCheckHandler = Callable[[CheckerNode], None]
    
    
    ##   @brief 
    ##         Creates a @link Validate::CheckerDefinition Validate::CheckerDefinition@endlink .
    ##          
    ## 
    ##  
    ##         
    ##         Once a checker definition is created successfully, the class ID can be used to create instances of @link Validate::CheckerNode Validate::CheckerNode@endlink .<br/>
    ##         To obtain an instance of @link Validate::CheckerNode Validate::CheckerNode@endlink , refer to @link Validate::Validator::AppendCheckerNode Validate::Validator::AppendCheckerNode@endlink .
    ##         This method will check the presence of the ug_checkmate ("UG Check Mate") license.
    ##         
    ##         
    ##  @return checkerDefinition (@link CheckerDefinition NXOpen.Validate.CheckerDefinition@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="classID"> (str) </param>
    ## <param name="displayName"> (str) </param>
    ## <param name="category"> (str) </param>
    ## <param name="parameters"> (@link Parameter List[NXOpen.Validate.Parameter]@endlink) </param>
    ## <param name="doCheck"> (@link ValidationManager.DoCheckHandler NXOpen.Validate.ValidationManager.DoCheckHandler@endlink) </param>
    def CreateCheckerDefinition(classID: str, displayName: str, category: str, parameters: List[Parameter], doCheck: ValidationManager.DoCheckHandler) -> CheckerDefinition:
        """
          @brief 
                Creates a @link Validate::CheckerDefinition Validate::CheckerDefinition@endlink .
                 
        
         
                
                Once a checker definition is created successfully, the class ID can be used to create instances of @link Validate::CheckerNode Validate::CheckerNode@endlink .<br/>
                To obtain an instance of @link Validate::CheckerNode Validate::CheckerNode@endlink , refer to @link Validate::Validator::AppendCheckerNode Validate::Validator::AppendCheckerNode@endlink .
                This method will check the presence of the ug_checkmate ("UG Check Mate") license.
                
                
         @return checkerDefinition (@link CheckerDefinition NXOpen.Validate.CheckerDefinition@endlink): .
        """
        pass
    
    ##  
    ##         Creates a parser.
    ##         
    ##  @return parser (@link Parser NXOpen.Validate.Parser@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  name of the parser 
    def CreateParser(name: str) -> Parser:
        """
         
                Creates a parser.
                
         @return parser (@link Parser NXOpen.Validate.Parser@endlink):  .
        """
        pass
    
    ##  
    ##         Creates a validator.
    ##         
    ##  @return validator (@link Validator NXOpen.Validate.Validator@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  name of the validator 
    def CreateValidator(name: str) -> Validator:
        """
         
                Creates a validator.
                
         @return validator (@link Validator NXOpen.Validate.Validator@endlink):  .
        """
        pass
    
    ##   @brief 
    ##         Creates a @link Validate::ProfileDefinition Validate::ProfileDefinition@endlink .
    ##          
    ## 
    ##  
    ##         
    ##  @return profileDefinition (@link ProfileDefinition NXOpen.Validate.ProfileDefinition@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="classID"> (str) </param>
    ## <param name="displayName"> (str) </param>
    ## <param name="category"> (str) </param>
    ## <param name="parameters"> (@link Parameter List[NXOpen.Validate.Parameter]@endlink) </param>
    def DefineCheckerProfile(classID: str, displayName: str, category: str, parameters: List[Parameter]) -> ProfileDefinition:
        """
          @brief 
                Creates a @link Validate::ProfileDefinition Validate::ProfileDefinition@endlink .
                 
        
         
                
         @return profileDefinition (@link ProfileDefinition NXOpen.Validate.ProfileDefinition@endlink): .
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for an @link NXObject NXObject@endlink . 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    def DefineNXObjectParameter(parameterID: str, parameterValue: NXOpen.NXObject, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for an @link NXObject NXObject@endlink . 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for an @link NXObject NXObject@endlink  array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    def DefineNXObjectParameters(parameterID: str, parameterValue: List[NXOpen.NXObject], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for an @link NXObject NXObject@endlink  array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for an integer number. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: int, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for an integer number. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for an integer array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: List[int], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for an integer array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a @link Vector3d Vector3d@endlink . 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: NXOpen.Vector3d, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a @link Vector3d Vector3d@endlink . 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a @link Vector3d Vector3d@endlink  array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: List[NXOpen.Vector3d], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a @link Vector3d Vector3d@endlink  array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a boolean. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: bool, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a boolean. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a boolean array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: List[bool], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a boolean array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a real number. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: float, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a real number. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a real number array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: List[float], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a real number array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a string. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: str, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a string. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a string array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: List[str], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a string array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a @link Point3d Point3d@endlink . 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: NXOpen.Point3d, options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a single value @link Validate::Parameter Validate::Parameter@endlink  for a @link Point3d Point3d@endlink . 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a @link Point3d Point3d@endlink  array. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    @overload
    def DefineParameter(self, parameterID: str, parameterValue: List[NXOpen.Point3d], options: ValidationManager.ParameterOptions) -> Parameter:
        """
         Creates a multi-value @link Validate::Parameter Validate::Parameter@endlink  for a @link Point3d Point3d@endlink  array. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##  Creates a parameter and binding it to the input parameter. 
    ##  @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  The ID of parameter.
    def DefineReferencingParameter(parameterID: str, referencedParameter: Parameter) -> Parameter:
        """
         Creates a parameter and binding it to the input parameter. 
         @return parameter (@link Parameter NXOpen.Validate.Parameter@endlink):  Return defined parameter.
        """
        pass
    
    ##   @brief 
    ##         Deletes a @link Validate::CheckerDefinition Validate::CheckerDefinition@endlink .
    ##          
    ## 
    ##  
    ##         
    ##         Any instance of @link Validate::CheckerNode Validate::CheckerNode@endlink  based on a checker definition should be eliminated before deleting the checker definition.<br/>
    ##         Refer to @link Validate::Validator::EraseCheckerNode Validate::Validator::EraseCheckerNode@endlink  or @link Validate::Validator::ClearCheckerNodes Validate::Validator::ClearCheckerNodes@endlink .
    ##         
    ##         
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="checkerDefinition"> (@link CheckerDefinition NXOpen.Validate.CheckerDefinition@endlink) </param>
    @staticmethod
    def DeleteCheckerDefinition(checkerDefinition: CheckerDefinition) -> None:
        """
          @brief 
                Deletes a @link Validate::CheckerDefinition Validate::CheckerDefinition@endlink .
                 
        
         
                
                Any instance of @link Validate::CheckerNode Validate::CheckerNode@endlink  based on a checker definition should be eliminated before deleting the checker definition.<br/>
                Refer to @link Validate::Validator::EraseCheckerNode Validate::Validator::EraseCheckerNode@endlink  or @link Validate::Validator::ClearCheckerNodes Validate::Validator::ClearCheckerNodes@endlink .
                
                
        """
        pass
    
    ##  Deletes a @link Validate::ProfileDefinition Validate::ProfileDefinition@endlink .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="profileDefinition"> (@link ProfileDefinition NXOpen.Validate.ProfileDefinition@endlink) </param>
    @staticmethod
    def DeleteCheckerProfileDefinition(profileDefinition: ProfileDefinition) -> None:
        """
         Deletes a @link Validate::ProfileDefinition Validate::ProfileDefinition@endlink .
        """
        pass
    
    ##  
    ##         Deletes a parser.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    @staticmethod
    def DeleteParser(parser: Parser) -> None:
        """
         
                Deletes a parser.
                
        """
        pass
    
    ##  
    ##         Deletes a validator.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  
    @staticmethod
    def DeleteValidator(validator: Validator) -> None:
        """
         
                Deletes a validator.
                
        """
        pass
    
    ##  
    ##         Finds parsers in current session. It will return all parsers with the same name.
    ##         
    ##  @return parsers (@link Parser List[NXOpen.Validate.Parser]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    @staticmethod
    def FindParser(name: str) -> List[Parser]:
        """
         
                Finds parsers in current session. It will return all parsers with the same name.
                
         @return parsers (@link Parser List[NXOpen.Validate.Parser]@endlink):  .
        """
        pass
    
    ##  
    ##         Finds validators in current session. It will return all validators with the same name.
    ##         
    ##  @return validators (@link Validator List[NXOpen.Validate.Validator]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  
    @staticmethod
    def FindValidator(name: str) -> List[Validator]:
        """
         
                Finds validators in current session. It will return all validators with the same name.
                
         @return validators (@link Validator List[NXOpen.Validate.Validator]@endlink):  .
        """
        pass
    
    ##  The display name of the checker.
    ##             Return empty if the checker is not registered.
    ##          @code 
    ##         displayName = validationManager.GetCheckerDisplayName("classID");    
    ##          @endcode 
    ##         
    ##  @return displayName (str):  The display name of the checker. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  The class ID of the checker. 
    @staticmethod
    def GetCheckerDisplayName(classID: str) -> str:
        """
         The display name of the checker.
                    Return empty if the checker is not registered.
                 @code 
                displayName = validationManager.GetCheckerDisplayName("classID");    
                 @endcode 
                
         @return displayName (str):  The display name of the checker. .
        """
        pass
    
    ##  Registers a checker profile definition to validation manager. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="profileDefinition"> (@link ProfileDefinition NXOpen.Validate.ProfileDefinition@endlink) </param>
    @staticmethod
    def RegisterCheckerProfileDefinition(profileDefinition: ProfileDefinition) -> None:
        """
         Registers a checker profile definition to validation manager. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Contains information about run options of check-mate checking process.
##     
##     
## 
##   <br>  Created in NX7.5.0  <br> 

class ValidatorOptions(NXOpen.TaggedObject): 
    """ Contains information about run options of check-mate checking process.
    
    """


    ##  The log mode type. 
    ##  Generate log per session 
    class LogModeTypes(Enum):
        """
        Members Include: <LogPerSession> <LogPerPart>
        """
        LogPerSession: int
        LogPerPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ValidatorOptions.LogModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The results display mode type. 
    ##  Always display results. 
    class ResultsDisplayModeTypes(Enum):
        """
        Members Include: <AlwaysDisplay> <DisplayIfNotPass> <DoNotDisplay>
        """
        AlwaysDisplay: int
        DisplayIfNotPass: int
        DoNotDisplay: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ValidatorOptions.ResultsDisplayModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The save mode type. 
    ##  Do not perform save. 
    class SaveModeTypes(Enum):
        """
        Members Include: <DoNotSave> <SaveIfPassed> <AlwaysSave>
        """
        DoNotSave: int
        SaveIfPassed: int
        AlwaysSave: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ValidatorOptions.SaveModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ValidatorOptions.ResultsDisplayModeTypes NXOpen.Validate.ValidatorOptions.ResultsDisplayModeTypes@endlink) AutoDisplayResults
    ##   the configuration of auto display results   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ValidatorOptions.ResultsDisplayModeTypes
    @property
    def AutoDisplayResults(self) -> ValidatorOptions.ResultsDisplayModeTypes:
        """
        Getter for property: (@link ValidatorOptions.ResultsDisplayModeTypes NXOpen.Validate.ValidatorOptions.ResultsDisplayModeTypes@endlink) AutoDisplayResults
          the configuration of auto display results   
            
         
        """
        pass
    
    ## Setter for property: (@link ValidatorOptions.ResultsDisplayModeTypes NXOpen.Validate.ValidatorOptions.ResultsDisplayModeTypes@endlink) AutoDisplayResults

    ##   the configuration of auto display results   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AutoDisplayResults.setter
    def AutoDisplayResults(self, displayResults: ValidatorOptions.ResultsDisplayModeTypes):
        """
        Setter for property: (@link ValidatorOptions.ResultsDisplayModeTypes NXOpen.Validate.ValidatorOptions.ResultsDisplayModeTypes@endlink) AutoDisplayResults
          the configuration of auto display results   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExcludeNonOwnerParts
    ##   the configuration of excluding parts not owned by the user.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def ExcludeNonOwnerParts(self) -> bool:
        """
        Getter for property: (bool) ExcludeNonOwnerParts
          the configuration of excluding parts not owned by the user.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ExcludeNonOwnerParts

    ##   the configuration of excluding parts not owned by the user.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ExcludeNonOwnerParts.setter
    def ExcludeNonOwnerParts(self, excludeNonOwnerParts: bool):
        """
        Setter for property: (bool) ExcludeNonOwnerParts
          the configuration of excluding parts not owned by the user.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ExcludeReadonlyParts
    ##   the configuration of excluding read-only parts.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def ExcludeReadonlyParts(self) -> bool:
        """
        Getter for property: (bool) ExcludeReadonlyParts
          the configuration of excluding read-only parts.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ExcludeReadonlyParts

    ##   the configuration of excluding read-only parts.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ExcludeReadonlyParts.setter
    def ExcludeReadonlyParts(self, excludeReadonlyParts: bool):
        """
        Setter for property: (bool) ExcludeReadonlyParts
          the configuration of excluding read-only parts.  
             
         
        """
        pass
    
    ## Getter for property: (bool) GenerateCheckFlag
    ##   the configuration of generating check flag if checking results are PASS   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def GenerateCheckFlag(self) -> bool:
        """
        Getter for property: (bool) GenerateCheckFlag
          the configuration of generating check flag if checking results are PASS   
            
         
        """
        pass
    
    ## Setter for property: (bool) GenerateCheckFlag

    ##   the configuration of generating check flag if checking results are PASS   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @GenerateCheckFlag.setter
    def GenerateCheckFlag(self, generateCheckFlag: bool):
        """
        Setter for property: (bool) GenerateCheckFlag
          the configuration of generating check flag if checking results are PASS   
            
         
        """
        pass
    
    ## Getter for property: (bool) GenerateLogFile
    ##   the configuration of generating log file after checking.  
    ##    If True, log file will be generated.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def GenerateLogFile(self) -> bool:
        """
        Getter for property: (bool) GenerateLogFile
          the configuration of generating log file after checking.  
           If True, log file will be generated.   
         
        """
        pass
    
    ## Setter for property: (bool) GenerateLogFile

    ##   the configuration of generating log file after checking.  
    ##    If True, log file will be generated.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @GenerateLogFile.setter
    def GenerateLogFile(self, generate_log_file: bool):
        """
        Setter for property: (bool) GenerateLogFile
          the configuration of generating log file after checking.  
           If True, log file will be generated.   
         
        """
        pass
    
    ## Getter for property: (str) LogFileDirectory
    ##   the configuration of log file directory where the log file will be saved.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def LogFileDirectory(self) -> str:
        """
        Getter for property: (str) LogFileDirectory
          the configuration of log file directory where the log file will be saved.  
             
         
        """
        pass
    
    ## Setter for property: (str) LogFileDirectory

    ##   the configuration of log file directory where the log file will be saved.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @LogFileDirectory.setter
    def LogFileDirectory(self, logFileDirectory: str):
        """
        Setter for property: (str) LogFileDirectory
          the configuration of log file directory where the log file will be saved.  
             
         
        """
        pass
    
    ## Getter for property: (@link ValidatorOptions.LogModeTypes NXOpen.Validate.ValidatorOptions.LogModeTypes@endlink) LogFileMode
    ##   the configuration of log file mode how to generate the log files.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ValidatorOptions.LogModeTypes
    @property
    def LogFileMode(self) -> ValidatorOptions.LogModeTypes:
        """
        Getter for property: (@link ValidatorOptions.LogModeTypes NXOpen.Validate.ValidatorOptions.LogModeTypes@endlink) LogFileMode
          the configuration of log file mode how to generate the log files.  
             
         
        """
        pass
    
    ## Setter for property: (@link ValidatorOptions.LogModeTypes NXOpen.Validate.ValidatorOptions.LogModeTypes@endlink) LogFileMode

    ##   the configuration of log file mode how to generate the log files.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @LogFileMode.setter
    def LogFileMode(self, logFileMode: ValidatorOptions.LogModeTypes):
        """
        Setter for property: (@link ValidatorOptions.LogModeTypes NXOpen.Validate.ValidatorOptions.LogModeTypes@endlink) LogFileMode
          the configuration of log file mode how to generate the log files.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ResultsAutoUpdate
    ##   the configuration of results auto update when work part change   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def ResultsAutoUpdate(self) -> bool:
        """
        Getter for property: (bool) ResultsAutoUpdate
          the configuration of results auto update when work part change   
            
         
        """
        pass
    
    ## Setter for property: (bool) ResultsAutoUpdate

    ##   the configuration of results auto update when work part change   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ResultsAutoUpdate.setter
    def ResultsAutoUpdate(self, autoUpdate: bool):
        """
        Setter for property: (bool) ResultsAutoUpdate
          the configuration of results auto update when work part change   
            
         
        """
        pass
    
    ## Getter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SavePartFile
    ##   the configuration of saving part file after checking finished.  
    ##    If True, part file will be saved.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ValidatorOptions.SaveModeTypes
    @property
    def SavePartFile(self) -> ValidatorOptions.SaveModeTypes:
        """
        Getter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SavePartFile
          the configuration of saving part file after checking finished.  
           If True, part file will be saved.   
         
        """
        pass
    
    ## Setter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SavePartFile

    ##   the configuration of saving part file after checking finished.  
    ##    If True, part file will be saved.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SavePartFile.setter
    def SavePartFile(self, savePartFile: ValidatorOptions.SaveModeTypes):
        """
        Setter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SavePartFile
          the configuration of saving part file after checking finished.  
           If True, part file will be saved.   
         
        """
        pass
    
    ## Getter for property: (bool) SaveResultInPart
    ##   the configuration of saving check results into part file.  
    ##    If True, results will be saved in part file after checking finished.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def SaveResultInPart(self) -> bool:
        """
        Getter for property: (bool) SaveResultInPart
          the configuration of saving check results into part file.  
           If True, results will be saved in part file after checking finished.   
         
        """
        pass
    
    ## Setter for property: (bool) SaveResultInPart

    ##   the configuration of saving check results into part file.  
    ##    If True, results will be saved in part file after checking finished.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SaveResultInPart.setter
    def SaveResultInPart(self, save_result_in_part: bool):
        """
        Setter for property: (bool) SaveResultInPart
          the configuration of saving check results into part file.  
           If True, results will be saved in part file after checking finished.   
         
        """
        pass
    
    ## Getter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SaveResultInTeamcenter
    ##   the configuration of saving check results into Teamcenter.  
    ##    If true, results will be saved into Teamcenter.
    ##          This parameter is for NX Manager mode only   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ValidatorOptions.SaveModeTypes
    @property
    def SaveResultInTeamcenter(self) -> ValidatorOptions.SaveModeTypes:
        """
        Getter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SaveResultInTeamcenter
          the configuration of saving check results into Teamcenter.  
           If true, results will be saved into Teamcenter.
                 This parameter is for NX Manager mode only   
         
        """
        pass
    
    ## Setter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SaveResultInTeamcenter

    ##   the configuration of saving check results into Teamcenter.  
    ##    If true, results will be saved into Teamcenter.
    ##          This parameter is for NX Manager mode only   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SaveResultInTeamcenter.setter
    def SaveResultInTeamcenter(self, save_result_in_teamcenter: ValidatorOptions.SaveModeTypes):
        """
        Setter for property: (@link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink) SaveResultInTeamcenter
          the configuration of saving check results into Teamcenter.  
           If true, results will be saved into Teamcenter.
                 This parameter is for NX Manager mode only   
         
        """
        pass
    
    ## Getter for property: (bool) SkipChecking
    ##   the configuration of skip checking based on result up-to-date status.  
    ##    If True, checking will be skipped if the results are PASS and up-to-date.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def SkipChecking(self) -> bool:
        """
        Getter for property: (bool) SkipChecking
          the configuration of skip checking based on result up-to-date status.  
           If True, checking will be skipped if the results are PASS and up-to-date.   
         
        """
        pass
    
    ## Setter for property: (bool) SkipChecking

    ##   the configuration of skip checking based on result up-to-date status.  
    ##    If True, checking will be skipped if the results are PASS and up-to-date.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SkipChecking.setter
    def SkipChecking(self, skipChecking: bool):
        """
        Setter for property: (bool) SkipChecking
          the configuration of skip checking based on result up-to-date status.  
           If True, checking will be skipped if the results are PASS and up-to-date.   
         
        """
        pass
    
    ## Getter for property: (bool) SkipCheckingDontLoadPart
    ##   the configuration of skipping checking without loading parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def SkipCheckingDontLoadPart(self) -> bool:
        """
        Getter for property: (bool) SkipCheckingDontLoadPart
          the configuration of skipping checking without loading parts   
            
         
        """
        pass
    
    ## Setter for property: (bool) SkipCheckingDontLoadPart

    ##   the configuration of skipping checking without loading parts   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SkipCheckingDontLoadPart.setter
    def SkipCheckingDontLoadPart(self, skipCheckingDontLoadPart: bool):
        """
        Setter for property: (bool) SkipCheckingDontLoadPart
          the configuration of skipping checking without loading parts   
            
         
        """
        pass
    
    ## Getter for property: (bool) SkipOverriddenResultOption
    ##    the configuration of skip checking based on result overriden state.  
    ##    If True, checking will be skipped if the results are overridden.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def SkipOverriddenResultOption(self) -> bool:
        """
        Getter for property: (bool) SkipOverriddenResultOption
           the configuration of skip checking based on result overriden state.  
           If True, checking will be skipped if the results are overridden.   
         
        """
        pass
    
    ## Setter for property: (bool) SkipOverriddenResultOption

    ##    the configuration of skip checking based on result overriden state.  
    ##    If True, checking will be skipped if the results are overridden.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @SkipOverriddenResultOption.setter
    def SkipOverriddenResultOption(self, skipOverriddenResult: bool):
        """
        Setter for property: (bool) SkipOverriddenResultOption
           the configuration of skip checking based on result overriden state.  
           If True, checking will be skipped if the results are overridden.   
         
        """
        pass
    
    ## Getter for property: (bool) StopOnError
    ##   the configuration of stopping checking process on error status.  
    ##    If True, stop checking when there is checker returned error status.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def StopOnError(self) -> bool:
        """
        Getter for property: (bool) StopOnError
          the configuration of stopping checking process on error status.  
           If True, stop checking when there is checker returned error status.   
         
        """
        pass
    
    ## Setter for property: (bool) StopOnError

    ##   the configuration of stopping checking process on error status.  
    ##    If True, stop checking when there is checker returned error status.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @StopOnError.setter
    def StopOnError(self, stopOnError: bool):
        """
        Setter for property: (bool) StopOnError
          the configuration of stopping checking process on error status.  
           If True, stop checking when there is checker returned error status.   
         
        """
        pass
    
    ## Getter for property: (bool) StopOnWarning
    ##   the configuration of stopping checking on warning status.  
    ##    If True, stop checking when there is checker returned warning status.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def StopOnWarning(self) -> bool:
        """
        Getter for property: (bool) StopOnWarning
          the configuration of stopping checking on warning status.  
           If True, stop checking when there is checker returned warning status.   
         
        """
        pass
    
    ## Setter for property: (bool) StopOnWarning

    ##   the configuration of stopping checking on warning status.  
    ##    If True, stop checking when there is checker returned warning status.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @StopOnWarning.setter
    def StopOnWarning(self, stop_on_warning: bool):
        """
        Setter for property: (bool) StopOnWarning
          the configuration of stopping checking on warning status.  
           If True, stop checking when there is checker returned warning status.   
         
        """
        pass
    
    ## Getter for property: (bool) TreatWarningAsFail
    ##   the configuration of treating warning status as fail status.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def TreatWarningAsFail(self) -> bool:
        """
        Getter for property: (bool) TreatWarningAsFail
          the configuration of treating warning status as fail status.  
             
         
        """
        pass
    
    ## Setter for property: (bool) TreatWarningAsFail

    ##   the configuration of treating warning status as fail status.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @TreatWarningAsFail.setter
    def TreatWarningAsFail(self, treatWarningAsFail: bool):
        """
        Setter for property: (bool) TreatWarningAsFail
          the configuration of treating warning status as fail status.  
             
         
        """
        pass
    
import NXOpen
## Represents a NX @link NXOpen::Validate::Validator NXOpen::Validate::Validator@endlink .
##      <br> To create a new instance of this class, use @link NXOpen::Validate::ValidationManager::CreateValidator  NXOpen::Validate::ValidationManager::CreateValidator @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class Validator(NXOpen.TaggedObject): 
    """Represents a NX <ja_class>NXOpen.Validate.Validator</ja_class>.
    """


    ## Getter for property: (@link ValidatorOptions NXOpen.Validate.ValidatorOptions@endlink) ValidatorOptions
    ##   the run options.  
    ##      
    ##  
    ## Getter License requirements: ug_checkmate ("UG Check Mate")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ValidatorOptions
    @property
    def ValidatorOptions(self) -> ValidatorOptions:
        """
        Getter for property: (@link ValidatorOptions NXOpen.Validate.ValidatorOptions@endlink) ValidatorOptions
          the run options.  
             
         
        """
        pass
    
    ##  Adds a checker node.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  checker class name 
    def AppendCheckerNode(self, className: str) -> None:
        """
         Adds a checker node.
                
        """
        pass
    
    ##  Adds checker nodes.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  checkers' class name array 
    def AppendCheckerNodes(self, classNames: List[str]) -> None:
        """
         Adds checker nodes.
                
        """
        pass
    
    ##  Adds part node by part file name 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def AppendPartNode(self, self, fileName: str) -> None:
        """
         Adds part node by part file name 
        """
        pass
    
    ##  Adds part node by part object 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def AppendPartNode(self, self, partObject: NXOpen.Part) -> None:
        """
         Adds part node by part object 
        """
        pass
    
    ##  Adds part nodes by part file names 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def AppendPartNodes(self, self, fileNames: List[str]) -> None:
        """
         Adds part nodes by part file names 
        """
        pass
    
    ##  Adds part nodes by part objects 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def AppendPartNodes(self, self, partObject: List[NXOpen.Part]) -> None:
        """
         Adds part nodes by part objects 
        """
        pass
    
    ##  Clears checker nodes 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    def ClearCheckerNodes(self) -> None:
        """
         Clears checker nodes 
        """
        pass
    
    ##  Clears part nodes 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def ClearPartNodes(self) -> None:
        """
         Clears part nodes 
        """
        pass
    
    ##  Runs checking process and returns the checking status.
    ##             If failed checking statuses are found, it will return @link NXOpen::Validation::ResultFailed NXOpen::Validation::ResultFailed@endlink . 
    ##             Otherwise it will return @link NXOpen::Validation::ResultPass NXOpen::Validation::ResultPass@endlink . 
    ##             Call @link NXOpen::Validate::Validator::GetLastErrorListFromCommit NXOpen::Validate::Validator::GetLastErrorListFromCommit@endlink  for the execeptions happened during the checking process.
    ##         
    ##  @return status (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    def Commit(self) -> NXOpen.Validation.Result:
        """
         Runs checking process and returns the checking status.
                    If failed checking statuses are found, it will return @link NXOpen::Validation::ResultFailed NXOpen::Validation::ResultFailed@endlink . 
                    Otherwise it will return @link NXOpen::Validation::ResultPass NXOpen::Validation::ResultPass@endlink . 
                    Call @link NXOpen::Validate::Validator::GetLastErrorListFromCommit NXOpen::Validate::Validator::GetLastErrorListFromCommit@endlink  for the execeptions happened during the checking process.
                
         @return status (@link NXOpen.Validation.Result NXOpen.Validation.Result@endlink):  .
        """
        pass
    
    ##  Removes a checker node.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  
    def EraseCheckerNode(self, del_ndx: int) -> None:
        """
         Removes a checker node.
                
        """
        pass
    
    ##  Removes a part node 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def ErasePartNode(self, index: int) -> None:
        """
         Removes a part node 
        """
        pass
    
    ##  Returns a checker node.
    ##         
    ##  @return checkerNode (@link CheckerNode NXOpen.Validate.CheckerNode@endlink):  checker node .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    ##  
    def FindCheckerNode(self, index: int) -> CheckerNode:
        """
         Returns a checker node.
                
         @return checkerNode (@link CheckerNode NXOpen.Validate.CheckerNode@endlink):  checker node .
        """
        pass
    
    ##  Finds a part node 
    ##  @return partNode (@link PartNode NXOpen.Validate.PartNode@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  
    def FindPartNode(self, index: int) -> PartNode:
        """
         Finds a part node 
         @return partNode (@link PartNode NXOpen.Validate.PartNode@endlink):  .
        """
        pass
    
    ##  Returns all checker nodes.
    ##         
    ##  @return checkerNode (@link CheckerNode List[NXOpen.Validate.CheckerNode]@endlink):  checker name array .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    def GetCheckerNodes(self) -> List[CheckerNode]:
        """
         Returns all checker nodes.
                
         @return checkerNode (@link CheckerNode List[NXOpen.Validate.CheckerNode]@endlink):  checker name array .
        """
        pass
    
    ##  Return the list of errors happened during last @link NXOpen::Validate::Validator::Commit NXOpen::Validate::Validator::Commit@endlink .
    ##         
    ##  @return errors (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  List of errors encountered during the checking process .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    def GetLastErrorListFromCommit(self) -> NXOpen.ErrorList:
        """
         Return the list of errors happened during last @link NXOpen::Validate::Validator::Commit NXOpen::Validate::Validator::Commit@endlink .
                
         @return errors (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  List of errors encountered during the checking process .
        """
        pass
    
    ##  Returns all part nodes. 
    ##  @return partNodes (@link PartNode List[NXOpen.Validate.PartNode]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: ug_checkmate ("UG Check Mate")
    def GetPartNodes(self) -> List[PartNode]:
        """
         Returns all part nodes. 
         @return partNodes (@link PartNode List[NXOpen.Validate.PartNode]@endlink):  .
        """
        pass
    
import NXOpen
##  @brief Provides a generic comparator for finding differences between two XML
##        format files.
##        The comparator takes @link NXOpen::Validate::XmlComparator::Options NXOpen::Validate::XmlComparator::Options@endlink  to further control the
##        comparison process. It returns @link NXOpen::Validate::XmlComparator::Result NXOpen::Validate::XmlComparator::Result@endlink , and generates report 
##        of detailed differences in HTML file which can be viewed via web browser. 
## 
##  
##      <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX6.0.2  <br> 

class XmlComparator(NXOpen.Object): 
    """<summary>Provides a generic comparator for finding differences between two XML
       format files.
       The comparator takes <ja_struct>NXOpen.Validate.XmlComparator.Options</ja_struct> to further control the
       comparison process. It returns <ja_enum>NXOpen.Validate.XmlComparator.Result</ja_enum>, and generates report 
       of detailed differences in HTML file which can be viewed via web browser.</summary>
    """


    ##  Specifies result of the comparison 
    ##  Represents two xml files are identical 
    class Result(Enum):
        """
        Members Include: <Identical> <Different>
        """
        Identical: int
        Different: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> XmlComparator.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   <br> Represents config options in comparison <br> 
    ##              <br> For example: <br> 
    ## 
    ##              <br> case 1: Defines filter file to control what nodes will be compared;
    ##                 generates comparison report and log; ignores CDATA and processing 
    ##                 instruction nodes. <br> 
    ##                  @code compareOptions.ReportFile           = "auto_report.html";
    ##                       compareOptions.FilterFile           = "filter.xml";
    ##                       compareOptions.LogFile              = "log.log";
    ##                       compareOptions.IgnoreNamespaces     = FALSE;
    ##                       compareOptions.IgnoreUnmatchedNodes = FALSE;
    ##                       compareOptions.IgnoreComments       = FALSE;
    ##                       compareOptions.IgnoreCdata          = TRUE;
    ##                       compareOptions.IgnorePI             = TRUE;
    ##                       CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
    ##                  @endcode 
    ## 
    ##              <br> case 2: Compares all nodes and does not generate report file and log file. <br> 
    ##                  @code compareOptions.ReportFile           = NULL;
    ##                       compareOptions.FilterFile           = NULL;
    ##                       compareOptions.LogFile              = NULL;
    ##                       CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
    ##                 @endcode 
    ##         
    class Options:
        """
          <br> Represents config options in comparison <br> 
                     <br> For example: <br> 
        
                     <br> case 1: Defines filter file to control what nodes will be compared;
                        generates comparison report and log; ignores CDATA and processing 
                        instruction nodes. <br> 
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
        
                     <br> case 2: Compares all nodes and does not generate report file and log file. <br> 
                         @code compareOptions.ReportFile           = NULL;
                              compareOptions.FilterFile           = NULL;
                              compareOptions.LogFile              = NULL;
                              CompareXmlFiles("fileOne.xml", "fileTwo.xml", compareOptions)
                        @endcode 
                
        """
        ## Getter for property :(str) FilterFile
        ## File specification of filter file.
        ## @return str
        @property
        def FilterFile(self) -> str:
            """
            Getter for property FilterFile
            File specification of filter file.

            """
            pass
        
        ## Setter for property :(str) FilterFile
        @FilterFile.setter
        def FilterFile(self, value: str):
            """
            Getter for property FilterFile
            File specification of filter file.
            Setter for property FilterFile
            File specification of filter file.

            """
            pass
        
        ## Getter for property :(str) ReportFile
        ## File specification of report file.
        ## @return str
        @property
        def ReportFile(self) -> str:
            """
            Getter for property ReportFile
            File specification of report file.

            """
            pass
        
        ## Setter for property :(str) ReportFile
        @ReportFile.setter
        def ReportFile(self, value: str):
            """
            Getter for property ReportFile
            File specification of report file.
            Setter for property ReportFile
            File specification of report file.

            """
            pass
        
        ## Getter for property :(str) LogFile
        ## File specification of comparison log file.
        ## @return str
        @property
        def LogFile(self) -> str:
            """
            Getter for property LogFile
            File specification of comparison log file.

            """
            pass
        
        ## Setter for property :(str) LogFile
        @LogFile.setter
        def LogFile(self, value: str):
            """
            Getter for property LogFile
            File specification of comparison log file.
            Setter for property LogFile
            File specification of comparison log file.

            """
            pass
        
        ## Getter for property :(bool) IgnoreNamespaces
        ## Ignores namespace definition during comparison.
        ## @return bool
        @property
        def IgnoreNamespaces(self) -> bool:
            """
            Getter for property IgnoreNamespaces
            Ignores namespace definition during comparison.

            """
            pass
        
        ## Setter for property :(bool) IgnoreNamespaces
        @IgnoreNamespaces.setter
        def IgnoreNamespaces(self, value: bool):
            """
            Getter for property IgnoreNamespaces
            Ignores namespace definition during comparison.
            Setter for property IgnoreNamespaces
            Ignores namespace definition during comparison.

            """
            pass
        
        ## Getter for property :(bool) IgnoreUnmatchedNodes
        ## Ignores unmatched nodes in comparison.
        ## @return bool
        @property
        def IgnoreUnmatchedNodes(self) -> bool:
            """
            Getter for property IgnoreUnmatchedNodes
            Ignores unmatched nodes in comparison.

            """
            pass
        
        ## Setter for property :(bool) IgnoreUnmatchedNodes
        @IgnoreUnmatchedNodes.setter
        def IgnoreUnmatchedNodes(self, value: bool):
            """
            Getter for property IgnoreUnmatchedNodes
            Ignores unmatched nodes in comparison.
            Setter for property IgnoreUnmatchedNodes
            Ignores unmatched nodes in comparison.

            """
            pass
        
        ## Getter for property :(bool) IgnoreComments
        ## Ignores comment nodes in comparison.
        ## @return bool
        @property
        def IgnoreComments(self) -> bool:
            """
            Getter for property IgnoreComments
            Ignores comment nodes in comparison.

            """
            pass
        
        ## Setter for property :(bool) IgnoreComments
        @IgnoreComments.setter
        def IgnoreComments(self, value: bool):
            """
            Getter for property IgnoreComments
            Ignores comment nodes in comparison.
            Setter for property IgnoreComments
            Ignores comment nodes in comparison.

            """
            pass
        
        ## Getter for property :(bool) IgnoreCdata
        ## Ignores CDATA nodes in comparison.
        ## @return bool
        @property
        def IgnoreCdata(self) -> bool:
            """
            Getter for property IgnoreCdata
            Ignores CDATA nodes in comparison.

            """
            pass
        
        ## Setter for property :(bool) IgnoreCdata
        @IgnoreCdata.setter
        def IgnoreCdata(self, value: bool):
            """
            Getter for property IgnoreCdata
            Ignores CDATA nodes in comparison.
            Setter for property IgnoreCdata
            Ignores CDATA nodes in comparison.

            """
            pass
        
        ## Getter for property :(bool) IgnorePI
        ## Ignores processing instruction nodes in comparison.
        ## @return bool
        @property
        def IgnorePI(self) -> bool:
            """
            Getter for property IgnorePI
            Ignores processing instruction nodes in comparison.

            """
            pass
        
        ## Setter for property :(bool) IgnorePI
        @IgnorePI.setter
        def IgnorePI(self, value: bool):
            """
            Getter for property IgnorePI
            Ignores processing instruction nodes in comparison.
            Setter for property IgnorePI
            Ignores processing instruction nodes in comparison.

            """
            pass
        
    
    
    ##  Compares two xml format files. 
    ##             You can use @link NXOpen::Validate::XmlComparator::Options NXOpen::Validate::XmlComparator::Options@endlink to customize the comparison process. 
    ##         
    ##  @return result (@link XmlComparator.Result NXOpen.Validate.XmlComparator.Result@endlink):  comparison result .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    ##  The first xml file to be compared 
    def CompareXmlFiles(workXmlFile: str, masterXmlFile: str, compareOptions: XmlComparator.Options) -> XmlComparator.Result:
        """
         Compares two xml format files. 
                    You can use @link NXOpen::Validate::XmlComparator::Options NXOpen::Validate::XmlComparator::Options@endlink to customize the comparison process. 
                
         @return result (@link XmlComparator.Result NXOpen.Validate.XmlComparator.Result@endlink):  comparison result .
        """
        pass
    
## @package NXOpen.Validate
## Classes, Enums and Structs under NXOpen.Validate namespace

##  @link AnalysisResultCollectionAnalysisResultType NXOpen.Validate.AnalysisResultCollectionAnalysisResultType @endlink is an alias for @link AnalysisResultCollection.AnalysisResultType NXOpen.Validate.AnalysisResultCollection.AnalysisResultType@endlink
AnalysisResultCollectionAnalysisResultType = AnalysisResultCollection.AnalysisResultType


## @link CheckChannelRatioBuilderTableData_Struct NXOpen.Validate.CheckChannelRatioBuilderTableData_Struct@endlink is an alias for @link CheckChannelRatioBuilder.TableData NXOpen.Validate.CheckChannelRatioBuilder.TableData@endlink.
CheckChannelRatioBuilderTableData_Struct = CheckChannelRatioBuilder.TableData


##  @link CheckMinimumRadiusBuilderCurvatureTypes NXOpen.Validate.CheckMinimumRadiusBuilderCurvatureTypes @endlink is an alias for @link CheckMinimumRadiusBuilder.CurvatureTypes NXOpen.Validate.CheckMinimumRadiusBuilder.CurvatureTypes@endlink
CheckMinimumRadiusBuilderCurvatureTypes = CheckMinimumRadiusBuilder.CurvatureTypes


##  @link CheckModelWithinPrintableVolumeBuilderPrinterShapeTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilderPrinterShapeTypes @endlink is an alias for @link CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes@endlink
CheckModelWithinPrintableVolumeBuilderPrinterShapeTypes = CheckModelWithinPrintableVolumeBuilder.PrinterShapeTypes


##  @link CheckModelWithinPrintableVolumeBuilderShowTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilderShowTypes @endlink is an alias for @link CheckModelWithinPrintableVolumeBuilder.ShowTypes NXOpen.Validate.CheckModelWithinPrintableVolumeBuilder.ShowTypes@endlink
CheckModelWithinPrintableVolumeBuilderShowTypes = CheckModelWithinPrintableVolumeBuilder.ShowTypes


##  @link CheckPartOrientationBuilderAccuracyLevel NXOpen.Validate.CheckPartOrientationBuilderAccuracyLevel @endlink is an alias for @link CheckPartOrientationBuilder.AccuracyLevel NXOpen.Validate.CheckPartOrientationBuilder.AccuracyLevel@endlink
CheckPartOrientationBuilderAccuracyLevel = CheckPartOrientationBuilder.AccuracyLevel


##  @link CheckPorosityBuilderColorMapDisplayOptionTypes NXOpen.Validate.CheckPorosityBuilderColorMapDisplayOptionTypes @endlink is an alias for @link CheckPorosityBuilder.ColorMapDisplayOptionTypes NXOpen.Validate.CheckPorosityBuilder.ColorMapDisplayOptionTypes@endlink
CheckPorosityBuilderColorMapDisplayOptionTypes = CheckPorosityBuilder.ColorMapDisplayOptionTypes


##  @link CheckPrintTimeBuilderPrinterType NXOpen.Validate.CheckPrintTimeBuilderPrinterType @endlink is an alias for @link CheckPrintTimeBuilder.PrinterType NXOpen.Validate.CheckPrintTimeBuilder.PrinterType@endlink
CheckPrintTimeBuilderPrinterType = CheckPrintTimeBuilder.PrinterType


##  @link OverrideBuilderDecisionActions NXOpen.Validate.OverrideBuilderDecisionActions @endlink is an alias for @link OverrideBuilder.DecisionActions NXOpen.Validate.OverrideBuilder.DecisionActions@endlink
OverrideBuilderDecisionActions = OverrideBuilder.DecisionActions


##  @link OverrideBuilderRequestTypes NXOpen.Validate.OverrideBuilderRequestTypes @endlink is an alias for @link OverrideBuilder.RequestTypes NXOpen.Validate.OverrideBuilder.RequestTypes@endlink
OverrideBuilderRequestTypes = OverrideBuilder.RequestTypes


##  @link OverrideBuilderToStates NXOpen.Validate.OverrideBuilderToStates @endlink is an alias for @link OverrideBuilder.ToStates NXOpen.Validate.OverrideBuilder.ToStates@endlink
OverrideBuilderToStates = OverrideBuilder.ToStates


##  @link ParserDataSourceTypes NXOpen.Validate.ParserDataSourceTypes @endlink is an alias for @link Parser.DataSourceTypes NXOpen.Validate.Parser.DataSourceTypes@endlink
ParserDataSourceTypes = Parser.DataSourceTypes


##  @link PartOrientationAnalysisResultCheckerIndex NXOpen.Validate.PartOrientationAnalysisResultCheckerIndex @endlink is an alias for @link PartOrientationAnalysisResult.CheckerIndex NXOpen.Validate.PartOrientationAnalysisResult.CheckerIndex@endlink
PartOrientationAnalysisResultCheckerIndex = PartOrientationAnalysisResult.CheckerIndex


## @link PartOrientationAnalysisResultCheckerValues_Struct NXOpen.Validate.PartOrientationAnalysisResultCheckerValues_Struct@endlink is an alias for @link PartOrientationAnalysisResult.CheckerValues NXOpen.Validate.PartOrientationAnalysisResult.CheckerValues@endlink.
PartOrientationAnalysisResultCheckerValues_Struct = PartOrientationAnalysisResult.CheckerValues


##  @link RequirementBuilderDataTypeOptions NXOpen.Validate.RequirementBuilderDataTypeOptions @endlink is an alias for @link RequirementBuilder.DataTypeOptions NXOpen.Validate.RequirementBuilder.DataTypeOptions@endlink
RequirementBuilderDataTypeOptions = RequirementBuilder.DataTypeOptions


##  @link RequirementBuilderDefinitionMethodOptions NXOpen.Validate.RequirementBuilderDefinitionMethodOptions @endlink is an alias for @link RequirementBuilder.DefinitionMethodOptions NXOpen.Validate.RequirementBuilder.DefinitionMethodOptions@endlink
RequirementBuilderDefinitionMethodOptions = RequirementBuilder.DefinitionMethodOptions


##  @link RequirementBuilderRelationalOperatorOptions NXOpen.Validate.RequirementBuilderRelationalOperatorOptions @endlink is an alias for @link RequirementBuilder.RelationalOperatorOptions NXOpen.Validate.RequirementBuilder.RelationalOperatorOptions@endlink
RequirementBuilderRelationalOperatorOptions = RequirementBuilder.RelationalOperatorOptions


##  @link RequirementBuilderRequirementTypeOptions NXOpen.Validate.RequirementBuilderRequirementTypeOptions @endlink is an alias for @link RequirementBuilder.RequirementTypeOptions NXOpen.Validate.RequirementBuilder.RequirementTypeOptions@endlink
RequirementBuilderRequirementTypeOptions = RequirementBuilder.RequirementTypeOptions


##  @link RequirementBuilderSeverityOptions NXOpen.Validate.RequirementBuilderSeverityOptions @endlink is an alias for @link RequirementBuilder.SeverityOptions NXOpen.Validate.RequirementBuilder.SeverityOptions@endlink
RequirementBuilderSeverityOptions = RequirementBuilder.SeverityOptions


##  @link RequirementCheckSaveResultsToTeamcenterOptions NXOpen.Validate.RequirementCheckSaveResultsToTeamcenterOptions @endlink is an alias for @link RequirementCheck.SaveResultsToTeamcenterOptions NXOpen.Validate.RequirementCheck.SaveResultsToTeamcenterOptions@endlink
RequirementCheckSaveResultsToTeamcenterOptions = RequirementCheck.SaveResultsToTeamcenterOptions


##  @link RequirementCollectionSourceTypeOptions NXOpen.Validate.RequirementCollectionSourceTypeOptions @endlink is an alias for @link RequirementCollection.SourceTypeOptions NXOpen.Validate.RequirementCollection.SourceTypeOptions@endlink
RequirementCollectionSourceTypeOptions = RequirementCollection.SourceTypeOptions


##  @link ResultObjectResultTypes NXOpen.Validate.ResultObjectResultTypes @endlink is an alias for @link ResultObject.ResultTypes NXOpen.Validate.ResultObject.ResultTypes@endlink
ResultObjectResultTypes = ResultObject.ResultTypes


## @link ValidationManagerParameterOptions_Struct NXOpen.Validate.ValidationManagerParameterOptions_Struct@endlink is an alias for @link ValidationManager.ParameterOptions NXOpen.Validate.ValidationManager.ParameterOptions@endlink.
ValidationManagerParameterOptions_Struct = ValidationManager.ParameterOptions


##  @link ValidatorOptionsLogModeTypes NXOpen.Validate.ValidatorOptionsLogModeTypes @endlink is an alias for @link ValidatorOptions.LogModeTypes NXOpen.Validate.ValidatorOptions.LogModeTypes@endlink
ValidatorOptionsLogModeTypes = ValidatorOptions.LogModeTypes


##  @link ValidatorOptionsResultsDisplayModeTypes NXOpen.Validate.ValidatorOptionsResultsDisplayModeTypes @endlink is an alias for @link ValidatorOptions.ResultsDisplayModeTypes NXOpen.Validate.ValidatorOptions.ResultsDisplayModeTypes@endlink
ValidatorOptionsResultsDisplayModeTypes = ValidatorOptions.ResultsDisplayModeTypes


##  @link ValidatorOptionsSaveModeTypes NXOpen.Validate.ValidatorOptionsSaveModeTypes @endlink is an alias for @link ValidatorOptions.SaveModeTypes NXOpen.Validate.ValidatorOptions.SaveModeTypes@endlink
ValidatorOptionsSaveModeTypes = ValidatorOptions.SaveModeTypes


## @link XmlComparatorOptions_Struct NXOpen.Validate.XmlComparatorOptions_Struct@endlink is an alias for @link XmlComparator.Options NXOpen.Validate.XmlComparator.Options@endlink.
XmlComparatorOptions_Struct = XmlComparator.Options


##  @link XmlComparatorResult NXOpen.Validate.XmlComparatorResult @endlink is an alias for @link XmlComparator.Result NXOpen.Validate.XmlComparator.Result@endlink
XmlComparatorResult = XmlComparator.Result


