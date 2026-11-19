from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Represents the anchor position of a record display, which is used to position a note 
##  the normal marker without anchor type 
class AnchorType(Enum):
    """
    Members Include: <NotSet> <Start> <End> <MaximumValue> <MinimumValue> <AbsPercentage>
    """
    NotSet: int
    Start: int
    End: int
    MaximumValue: int
    MinimumValue: int
    AbsPercentage: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AnchorType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the angle axis display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AngleAxisStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the angle axis display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link AngleUnit NXOpen.CAE.Xyplot.AngleUnit@endlink) AngleUnit
    ##   the angle axis number unit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return AngleUnit
    @property
    def AngleUnit(self) -> AngleUnit:
        """
        Getter for property: (@link AngleUnit NXOpen.CAE.Xyplot.AngleUnit@endlink) AngleUnit
          the angle axis number unit   
            
         
        """
        pass
    
    ## Setter for property: (@link AngleUnit NXOpen.CAE.Xyplot.AngleUnit@endlink) AngleUnit

    ##   the angle axis number unit   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AngleUnit.setter
    def AngleUnit(self, unit: AngleUnit):
        """
        Setter for property: (@link AngleUnit NXOpen.CAE.Xyplot.AngleUnit@endlink) AngleUnit
          the angle axis number unit   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) LineDisplaySettings
    ##   the angle axis lines display styles   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def LineDisplaySettings(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) LineDisplaySettings
          the angle axis lines display styles   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
##  Represents the angle axis display value unit 
##  Display angle in degree unit 
class AngleUnit(Enum):
    """
    Members Include: <Degree> <Radian> <Rev>
    """
    Degree: int
    Radian: int
    Rev: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AngleUnit:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##   @brief  Represents a data accessor to retrieve data of a function which is plotted in 3D Argand graphs.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class Argand3DFunctionDataAccessor(IFunctionDataAccessor): 
    """ <summary> Represents a data accessor to retrieve data of a function which is plotted in 3D Argand graphs. </summary> """


    ##  Asks display data. 
    ##  @return A tuple consisting of (dependentValues, indenpendent1Values, indenpendent2Values). 
    ##  - dependentValues is: List[float].
    ##  - indenpendent1Values is: List[float].
    ##  - indenpendent2Values is: List[float].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskDisplayData(argand3DFunctionDataAccessor: Argand3DFunctionDataAccessor) -> Tuple[List[float], List[float], List[float]]:
        """
         Asks display data. 
         @return A tuple consisting of (dependentValues, indenpendent1Values, indenpendent2Values). 
         - dependentValues is: List[float].
         - indenpendent1Values is: List[float].
         - indenpendent2Values is: List[float].

        """
        pass
    
import NXOpen.CAE
import NXOpen.CAE.FTK
##  Represents the argument axis display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ArgumentAxisStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the argument axis display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (bool) RangeAuto
    ##   a value indicating whether to set axis range automatically   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def RangeAuto(self) -> bool:
        """
        Getter for property: (bool) RangeAuto
          a value indicating whether to set axis range automatically   
            
         
        """
        pass
    
    ## Setter for property: (bool) RangeAuto

    ##   a value indicating whether to set axis range automatically   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @RangeAuto.setter
    def RangeAuto(self, rangeAutomation: bool):
        """
        Setter for property: (bool) RangeAuto
          a value indicating whether to set axis range automatically   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType
    ##   the unit system type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionUnitSystem
    @property
    def UnitSystemType(self) -> NXOpen.CAE.XyFunctionUnitSystem:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType
          the unit system type  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType

    ##   the unit system type  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnitSystemType.setter
    def UnitSystemType(self, unitSystemType: NXOpen.CAE.XyFunctionUnitSystem):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType
          the unit system type  
            
         
        """
        pass
    
    ##  Gets the customer indices 
    ##  @return customerIndices (List[int]):  Customer range .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCustomerRange(pArgumentAxisStyle: ArgumentAxisStyleSetting) -> List[int]:
        """
         Gets the customer indices 
         @return customerIndices (List[int]):  Customer range .
        """
        pass
    
    ##  Gets display unit
    ##  @return dispUnit (@link NXOpen.CAE.FTK.BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDisplayUnit(pArgumentAxisStyle: ArgumentAxisStyleSetting) -> NXOpen.CAE.FTK.BaseUnit:
        """
         Gets display unit
         @return dispUnit (@link NXOpen.CAE.FTK.BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
        """
        pass
    
    ##  Gets the indices of label 
    ##  @return labelIndices (List[int]):  Customer range .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemLabel"> (str) </param>
    def GetIndicesOfLabel(pArgumentAxisStyle: ArgumentAxisStyleSetting, itemLabel: str) -> List[int]:
        """
         Gets the indices of label 
         @return labelIndices (List[int]):  Customer range .
        """
        pass
    
    ##  Gets nth item label 
    ##  @return nthItemLabel (str):    .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nth"> (int) </param>
    def GetNthItemLabel(pArgumentAxisStyle: ArgumentAxisStyleSetting, nth: int) -> str:
        """
         Gets nth item label 
         @return nthItemLabel (str):    .
        """
        pass
    
    ##  Logs an update event for changing display unit before committing AxisStyleSetting change.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def LogUnitChangedEvent(pArgumentAxisStyle: ArgumentAxisStyleSetting) -> None:
        """
         Logs an update event for changing display unit before committing AxisStyleSetting change.
        """
        pass
    
    ##  Sets the customer indices 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Customer range 
    def SetCustomerIndices(pArgumentAxisStyle: ArgumentAxisStyleSetting, customerIndices: List[int]) -> None:
        """
         Sets the customer indices 
        """
        pass
    
import NXOpen
import NXOpen.CAE.FTK
##   @brief  Represents a data accessor to retrieve axis data.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class AxisAccessor(NXOpen.TransientObject): 
    """ <summary> Represents a data accessor to retrieve axis data. </summary> """


    ## Getter for property: (@link AxisType NXOpen.CAE.Xyplot.AxisType@endlink) AxisType
    ##   the axis type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return AxisType
    @property
    def AxisType(self) -> AxisType:
        """
        Getter for property: (@link AxisType NXOpen.CAE.Xyplot.AxisType@endlink) AxisType
          the axis type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FTK.BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
    ##   the axis unit.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.CAE.FTK.BaseUnit
    @property
    def Unit(self) -> NXOpen.CAE.FTK.BaseUnit:
        """
        Getter for property: (@link NXOpen.CAE.FTK.BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink) Unit
          the axis unit.  
             
         
        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(axisAccessor: AxisAccessor) -> None:
        """
         Destroys the object. 
        """
        pass
    
    ##  Gets the axis labels. 
    ##  @return axisLabels (List[str]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLabel(axisAccessor: AxisAccessor) -> List[str]:
        """
         Gets the axis labels. 
         @return axisLabels (List[str]): .
        """
        pass
    
##  Represents the DB scale for plot 
##  Db 10 
class AxisDBScale(Enum):
    """
    Members Include: <Ten> <Twenty>
    """
    Ten: int
    Twenty: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AxisDBScale:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the axis direction 
##  X-axis 
class AxisDirection(Enum):
    """
    Members Include: <X> <Y> <Z>
    """
    X: int
    Y: int
    Z: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AxisDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the axis item display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AxisItemStyle(TextStyleSetting): 
    """ Represents the axis item display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (int) MaximumCharacterCount
    ##   the maximum character count.  
    ##    The minimum value is 1.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def MaximumCharacterCount(self) -> int:
        """
        Getter for property: (int) MaximumCharacterCount
          the maximum character count.  
           The minimum value is 1.   
         
        """
        pass
    
    ## Setter for property: (int) MaximumCharacterCount

    ##   the maximum character count.  
    ##    The minimum value is 1.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumCharacterCount.setter
    def MaximumCharacterCount(self, maximumCharacterCount: int):
        """
        Setter for property: (int) MaximumCharacterCount
          the maximum character count.  
           The minimum value is 1.   
         
        """
        pass
    
    ## Getter for property: (@link AxisItemTruncationDirection NXOpen.CAE.Xyplot.AxisItemTruncationDirection@endlink) TruncationDirection
    ##   the truncation direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return AxisItemTruncationDirection
    @property
    def TruncationDirection(self) -> AxisItemTruncationDirection:
        """
        Getter for property: (@link AxisItemTruncationDirection NXOpen.CAE.Xyplot.AxisItemTruncationDirection@endlink) TruncationDirection
          the truncation direction   
            
         
        """
        pass
    
    ## Setter for property: (@link AxisItemTruncationDirection NXOpen.CAE.Xyplot.AxisItemTruncationDirection@endlink) TruncationDirection

    ##   the truncation direction   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TruncationDirection.setter
    def TruncationDirection(self, truncationDirection: AxisItemTruncationDirection):
        """
        Setter for property: (@link AxisItemTruncationDirection NXOpen.CAE.Xyplot.AxisItemTruncationDirection@endlink) TruncationDirection
          the truncation direction   
            
         
        """
        pass
    
##  Represents the truncation direction for axis item 
##  If string length exceeds maximum character count, truncating the end of string 
class AxisItemTruncationDirection(Enum):
    """
    Members Include: <End> <Beginning>
    """
    End: int
    Beginning: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AxisItemTruncationDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the axis label display style. Call @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AxisLabelStyle(CustomTextStyleSetting): 
    """ Represents the axis label display style. Call <ja_method>CAE.Xyplot.IDisplayStyle.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (bool) IncludeMeasureType
    ##   the option specifies whether to include measure type in axis label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IncludeMeasureType(self) -> bool:
        """
        Getter for property: (bool) IncludeMeasureType
          the option specifies whether to include measure type in axis label   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeMeasureType

    ##   the option specifies whether to include measure type in axis label   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IncludeMeasureType.setter
    def IncludeMeasureType(self, hasIncludeMeasureType: bool):
        """
        Setter for property: (bool) IncludeMeasureType
          the option specifies whether to include measure type in axis label   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeUnit
    ##   the option specifies whether to include unit information in axis label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IncludeUnit(self) -> bool:
        """
        Getter for property: (bool) IncludeUnit
          the option specifies whether to include unit information in axis label   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeUnit

    ##   the option specifies whether to include unit information in axis label   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IncludeUnit.setter
    def IncludeUnit(self, hasIncludeUnit: bool):
        """
        Setter for property: (bool) IncludeUnit
          the option specifies whether to include unit information in axis label   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseSingleLine
    ##   the option specifies whether to display axis label in a single line   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseSingleLine(self) -> bool:
        """
        Getter for property: (bool) UseSingleLine
          the option specifies whether to display axis label in a single line   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseSingleLine

    ##   the option specifies whether to display axis label in a single line   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseSingleLine.setter
    def UseSingleLine(self, isSingleLine: bool):
        """
        Setter for property: (bool) UseSingleLine
          the option specifies whether to display axis label in a single line   
            
         
        """
        pass
    
##  Represents an axis model object on a XY graphing.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AxisModel(BasicModel): 
    """ Represents an axis model object on a XY graphing. """


    ##  Gives expected display limits to calculate a zoom scale range which could be used by @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink  for zooming operation.
    ##                 the new display limits must be less than the original display limits returned by @link CAE::Xyplot::AxisModel::GetDisplayLimits CAE::Xyplot::AxisModel::GetDisplayLimits@endlink 
    ##  @return A tuple consisting of (startScale, endScale). 
    ##  - startScale is: float.
    ##  - endScale is: float.

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="newStartDisplayLimit"> (float) </param>
    ## <param name="newEndDisplayLimit"> (float) </param>
    @staticmethod
    def CalculateZoomScale(axisModel: AxisModel, newStartDisplayLimit: float, newEndDisplayLimit: float) -> Tuple[float, float]:
        """
         Gives expected display limits to calculate a zoom scale range which could be used by @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink  for zooming operation.
                        the new display limits must be less than the original display limits returned by @link CAE::Xyplot::AxisModel::GetDisplayLimits CAE::Xyplot::AxisModel::GetDisplayLimits@endlink 
         @return A tuple consisting of (startScale, endScale). 
         - startScale is: float.
         - endScale is: float.

        """
        pass
    
    ##  Gets the display limit values in display unit 
    ##  @return A tuple consisting of (startDisplayLimit, endDisplayLimit). 
    ##  - startDisplayLimit is: float.
    ##  - endDisplayLimit is: float.

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDisplayLimits(axisModel: AxisModel) -> Tuple[float, float]:
        """
         Gets the display limit values in display unit 
         @return A tuple consisting of (startDisplayLimit, endDisplayLimit). 
         - startDisplayLimit is: float.
         - endDisplayLimit is: float.

        """
        pass
    
import NXOpen.CAE
import NXOpen.CAE.FTK
##  Represents the axis display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class AxisStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the axis display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link AxisType NXOpen.CAE.Xyplot.AxisType@endlink) AxisType
    ##   the axis scale type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return AxisType
    @property
    def AxisType(self) -> AxisType:
        """
        Getter for property: (@link AxisType NXOpen.CAE.Xyplot.AxisType@endlink) AxisType
          the axis scale type   
            
         
        """
        pass
    
    ## Setter for property: (@link AxisType NXOpen.CAE.Xyplot.AxisType@endlink) AxisType

    ##   the axis scale type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @AxisType.setter
    def AxisType(self, axisType: AxisType):
        """
        Setter for property: (@link AxisType NXOpen.CAE.Xyplot.AxisType@endlink) AxisType
          the axis scale type   
            
         
        """
        pass
    
    ## Getter for property: (int) GraphOverhead
    ##   the round value to display.  
    ##    It is a percent value. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
    ##                 is not @link CAE::Xyplot::AxisTypeAuto CAE::Xyplot::AxisTypeAuto@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def GraphOverhead(self) -> int:
        """
        Getter for property: (int) GraphOverhead
          the round value to display.  
           It is a percent value. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
                        is not @link CAE::Xyplot::AxisTypeAuto CAE::Xyplot::AxisTypeAuto@endlink .   
         
        """
        pass
    
    ## Setter for property: (int) GraphOverhead

    ##   the round value to display.  
    ##    It is a percent value. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
    ##                 is not @link CAE::Xyplot::AxisTypeAuto CAE::Xyplot::AxisTypeAuto@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @GraphOverhead.setter
    def GraphOverhead(self, graphOverhead: int):
        """
        Setter for property: (int) GraphOverhead
          the round value to display.  
           It is a percent value. Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
                        is not @link CAE::Xyplot::AxisTypeAuto CAE::Xyplot::AxisTypeAuto@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link LimitsType NXOpen.CAE.Xyplot.LimitsType@endlink) LimitsType
    ##   the limits type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LimitsType
    @property
    def LimitsType(self) -> LimitsType:
        """
        Getter for property: (@link LimitsType NXOpen.CAE.Xyplot.LimitsType@endlink) LimitsType
          the limits type  
            
         
        """
        pass
    
    ## Setter for property: (@link LimitsType NXOpen.CAE.Xyplot.LimitsType@endlink) LimitsType

    ##   the limits type  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LimitsType.setter
    def LimitsType(self, limitsType: LimitsType):
        """
        Setter for property: (@link LimitsType NXOpen.CAE.Xyplot.LimitsType@endlink) LimitsType
          the limits type  
            
         
        """
        pass
    
    ## Getter for property: (int) LogDecades
    ##   the number of Log decades to display.  
    ##    Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
    ##                 is @link CAE::Xyplot::AxisTypeLog CAE::Xyplot::AxisTypeLog@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def LogDecades(self) -> int:
        """
        Getter for property: (int) LogDecades
          the number of Log decades to display.  
           Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
                        is @link CAE::Xyplot::AxisTypeLog CAE::Xyplot::AxisTypeLog@endlink .   
         
        """
        pass
    
    ## Setter for property: (int) LogDecades

    ##   the number of Log decades to display.  
    ##    Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
    ##                 is @link CAE::Xyplot::AxisTypeLog CAE::Xyplot::AxisTypeLog@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LogDecades.setter
    def LogDecades(self, logDecades: int):
        """
        Setter for property: (int) LogDecades
          the number of Log decades to display.  
           Avaliable when @link CAE::Xyplot::AxisStyleSetting::AxisType CAE::Xyplot::AxisStyleSetting::AxisType@endlink 
                        is @link CAE::Xyplot::AxisTypeLog CAE::Xyplot::AxisTypeLog@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType
    ##   the unit system type  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.XyFunctionUnitSystem
    @property
    def UnitSystemType(self) -> NXOpen.CAE.XyFunctionUnitSystem:
        """
        Getter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType
          the unit system type  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType

    ##   the unit system type  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UnitSystemType.setter
    def UnitSystemType(self, unitSystemType: NXOpen.CAE.XyFunctionUnitSystem):
        """
        Setter for property: (@link NXOpen.CAE.XyFunctionUnitSystem NXOpen.CAE.XyFunctionUnitSystem@endlink) UnitSystemType
          the unit system type  
            
         
        """
        pass
    
    ## Getter for property: (bool) UseAbsoluteValue
    ##   the option indicates whether to use absolute value.  
    ##    This option is only valid for Y-Axis and color axis.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def UseAbsoluteValue(self) -> bool:
        """
        Getter for property: (bool) UseAbsoluteValue
          the option indicates whether to use absolute value.  
           This option is only valid for Y-Axis and color axis.  
         
        """
        pass
    
    ## Setter for property: (bool) UseAbsoluteValue

    ##   the option indicates whether to use absolute value.  
    ##    This option is only valid for Y-Axis and color axis.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @UseAbsoluteValue.setter
    def UseAbsoluteValue(self, useAbsValue: bool):
        """
        Setter for property: (bool) UseAbsoluteValue
          the option indicates whether to use absolute value.  
           This option is only valid for Y-Axis and color axis.  
         
        """
        pass
    
    ##  Gets the dB settings 
    ##  @return dBSettings (@link NXOpen.CAE.SignalProcessingDBSettings NXOpen.CAE.SignalProcessingDBSettings@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDBSettings(pThis: AxisStyleSetting) -> NXOpen.CAE.SignalProcessingDBSettings:
        """
         Gets the dB settings 
         @return dBSettings (@link NXOpen.CAE.SignalProcessingDBSettings NXOpen.CAE.SignalProcessingDBSettings@endlink): .
        """
        pass
    
    ##  Gets display unit
    ##  @return dispUnit (@link NXOpen.CAE.FTK.BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDisplayUnit(pThis: AxisStyleSetting) -> NXOpen.CAE.FTK.BaseUnit:
        """
         Gets display unit
         @return dispUnit (@link NXOpen.CAE.FTK.BaseUnit NXOpen.CAE.FTK.BaseUnit@endlink): .
        """
        pass
    
    ##  Gets the fixed limits
    ##  @return A tuple consisting of (lowerLimit, upperLimit). 
    ##  - lowerLimit is: float.  .
    ##  - upperLimit is: float.  .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFixedLimits(pThis: AxisStyleSetting) -> Tuple[float, float]:
        """
         Gets the fixed limits
         @return A tuple consisting of (lowerLimit, upperLimit). 
         - lowerLimit is: float.  .
         - upperLimit is: float.  .

        """
        pass
    
    ##  Logs an update event for changing display unit before committing AxisStyleSetting change.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def LogUnitChangedEvent(pThis: AxisStyleSetting) -> None:
        """
         Logs an update event for changing display unit before committing AxisStyleSetting change.
        """
        pass
    
    ##  Sets the fixed limits
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##   
    def SetFixedLimits(pThis: AxisStyleSetting, lowerLimit: float, upperLimit: float) -> None:
        """
         Sets the fixed limits
        """
        pass
    
##  Represents the type of scale for X or Y axis 
##  Automatic type 
class AxisType(Enum):
    """
    Members Include: <Auto> <Linear> <Log> <Db> <Octave> <OneThirdOctave> <OneTwelfthOctave>
    """
    Auto: int
    Linear: int
    Log: int
    Db: int
    Octave: int
    OneThirdOctave: int
    OneTwelfthOctave: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> AxisType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the axis y display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AxisYStyleSetting(AxisStyleSetting): 
    """ Represents the axis y display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (bool) BarLowerLimit
    ##   the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def BarLowerLimit(self) -> bool:
        """
        Getter for property: (bool) BarLowerLimit
          the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y   
            
         
        """
        pass
    
    ## Setter for property: (bool) BarLowerLimit

    ##   the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @BarLowerLimit.setter
    def BarLowerLimit(self, barLowerLimit: bool):
        """
        Setter for property: (bool) BarLowerLimit
          the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y   
            
         
        """
        pass
    
##   @brief  Represents a data accessor to retrieve data of a function which is plotted in BarChart graphs.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class BarChartFunctionDataAccessor(IFunctionDataAccessor): 
    """ <summary> Represents a data accessor to retrieve data of a function which is plotted in BarChart graphs. </summary> """


    ##  Asks display data. 
    ##  @return A tuple consisting of (indenpendentValues, dependentValues). 
    ##  - indenpendentValues is: List[float].
    ##  - dependentValues is: List[float].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskDisplayData(barChartFunctionDataAccessor: BarChartFunctionDataAccessor) -> Tuple[List[float], List[float]]:
        """
         Asks display data. 
         @return A tuple consisting of (indenpendentValues, dependentValues). 
         - indenpendentValues is: List[float].
         - dependentValues is: List[float].

        """
        pass
    
    ##  Asks point labels. 
    ##  @return pointLabels (List[str]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskPointLabels(barChartFunctionDataAccessor: BarChartFunctionDataAccessor) -> List[str]:
        """
         Asks point labels. 
         @return pointLabels (List[str]): .
        """
        pass
    
##   @brief 
##         Manages the display of bar chart plot. 
## 
##  
##         
##         Call @link CAE::Xyplot::I2DDataPlot::EditRecord CAE::Xyplot::I2DDataPlot::EditRecord@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class BarChartPlot(Plot): 
    """ <summary>
        Manages the display of bar chart plot.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I2DDataPlot.EditRecord</ja_method> to edit data for this class.
        </remarks> """
    pass


import NXOpen
##  Represents the bar chart display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class BarChartStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the bar chart display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
    ##   the filling color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the filling color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor

    ##   the filling color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the filling color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
    ##   the outline color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
          the outline color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor

    ##   the outline color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
          the outline color   
            
         
        """
        pass
    
    ## Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarkerIdx
    ##   the point marker   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return PointMarker
    @property
    def PointMarkerIdx(self) -> PointMarker:
        """
        Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarkerIdx
          the point marker   
            
         
        """
        pass
    
    ## Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarkerIdx

    ##   the point marker   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PointMarkerIdx.setter
    def PointMarkerIdx(self, pointMarker: PointMarker):
        """
        Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarkerIdx
          the point marker   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOutline
    ##   the outline visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowOutline(self) -> bool:
        """
        Getter for property: (bool) ShowOutline
          the outline visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOutline

    ##   the outline visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowOutline.setter
    def ShowOutline(self, showOutline: bool):
        """
        Setter for property: (bool) ShowOutline
          the outline visibility   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowText
    ##   the text visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowText(self) -> bool:
        """
        Getter for property: (bool) ShowText
          the text visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowText

    ##   the text visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowText.setter
    def ShowText(self, showText: bool):
        """
        Setter for property: (bool) ShowText
          the text visibility   
            
         
        """
        pass
    
    ## Getter for property: (int) SpaceBetweenTextAndBar
    ##   the spaces between text and bar measured in percentage.  
    ##    The acceptable range is 0-10.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def SpaceBetweenTextAndBar(self) -> int:
        """
        Getter for property: (int) SpaceBetweenTextAndBar
          the spaces between text and bar measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    
    ## Setter for property: (int) SpaceBetweenTextAndBar

    ##   the spaces between text and bar measured in percentage.  
    ##    The acceptable range is 0-10.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SpaceBetweenTextAndBar.setter
    def SpaceBetweenTextAndBar(self, spaceBetweenTextAndBar: int):
        """
        Setter for property: (int) SpaceBetweenTextAndBar
          the spaces between text and bar measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    
##  Represents the bar filling color option 
##  Fill color or contour color with no shading 
class BarColorOption(Enum):
    """
    Members Include: <Fill> <Hidden> <Shaded>
    """
    Fill: int
    Hidden: int
    Shaded: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> BarColorOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the 2d bar display style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BarStyle2DSetting(BaseBarStyleSetting): 
    """ Represents the 2d bar display style. """


    ## Getter for property: (float) ConstantWidth
    ##   the constant bar width.  
    ##    The range is from 0.05 to 100.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def ConstantWidth(self) -> float:
        """
        Getter for property: (float) ConstantWidth
          the constant bar width.  
           The range is from 0.05 to 100.   
         
        """
        pass
    
    ## Setter for property: (float) ConstantWidth

    ##   the constant bar width.  
    ##    The range is from 0.05 to 100.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ConstantWidth.setter
    def ConstantWidth(self, constBarWidth: float):
        """
        Setter for property: (float) ConstantWidth
          the constant bar width.  
           The range is from 0.05 to 100.   
         
        """
        pass
    
    ## Getter for property: (bool) ShowConstantWidth
    ##   a value indicating whether to set bar width as constant   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ShowConstantWidth(self) -> bool:
        """
        Getter for property: (bool) ShowConstantWidth
          a value indicating whether to set bar width as constant   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowConstantWidth

    ##   a value indicating whether to set bar width as constant   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ShowConstantWidth.setter
    def ShowConstantWidth(self, showConstBarWidth: bool):
        """
        Setter for property: (bool) ShowConstantWidth
          a value indicating whether to set bar width as constant   
            
         
        """
        pass
    
##  Represents the 3d bar display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BarStyle3DSetting(BaseBarStyleSetting): 
    """ Represents the 3d bar display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link BarColorOption NXOpen.CAE.Xyplot.BarColorOption@endlink) ColorOption
    ##   the filling color option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return BarColorOption
    @property
    def ColorOption(self) -> BarColorOption:
        """
        Getter for property: (@link BarColorOption NXOpen.CAE.Xyplot.BarColorOption@endlink) ColorOption
          the filling color option   
            
         
        """
        pass
    
    ## Setter for property: (@link BarColorOption NXOpen.CAE.Xyplot.BarColorOption@endlink) ColorOption

    ##   the filling color option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: BarColorOption):
        """
        Setter for property: (@link BarColorOption NXOpen.CAE.Xyplot.BarColorOption@endlink) ColorOption
          the filling color option   
            
         
        """
        pass
    
    ## Getter for property: (int) Depth
    ##   the bar depth.  
    ##    The range is from 0 to 100.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Depth(self) -> int:
        """
        Getter for property: (int) Depth
          the bar depth.  
           The range is from 0 to 100.   
         
        """
        pass
    
    ## Setter for property: (int) Depth

    ##   the bar depth.  
    ##    The range is from 0 to 100.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Depth.setter
    def Depth(self, barDepth: int):
        """
        Setter for property: (int) Depth
          the bar depth.  
           The range is from 0 to 100.   
         
        """
        pass
    
import NXOpen
##  Represents the base bar display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BaseBarStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the base bar display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
    ##   the filling color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the filling color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor

    ##   the filling color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the filling color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
    ##   the outline color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
          the outline color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor

    ##   the outline color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
          the outline color   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOutline
    ##   a value indicating whether to display the outline   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ShowOutline(self) -> bool:
        """
        Getter for property: (bool) ShowOutline
          a value indicating whether to display the outline   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOutline

    ##   a value indicating whether to display the outline   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShowOutline.setter
    def ShowOutline(self, showOutline: bool):
        """
        Setter for property: (bool) ShowOutline
          a value indicating whether to display the outline   
            
         
        """
        pass
    
    ## Getter for property: (int) Width
    ##   the bar width.  
    ##    The range is from 0 to 100.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
          the bar width.  
           The range is from 0 to 100.   
         
        """
        pass
    
    ## Setter for property: (int) Width

    ##   the bar width.  
    ##    The range is from 0 to 100.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Width.setter
    def Width(self, barWidth: int):
        """
        Setter for property: (int) Width
          the bar width.  
           The range is from 0 to 100.   
         
        """
        pass
    
import NXOpen
##  Represent an abstract object on display style.  <br> not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class BaseDisplayStyleSetting(NXOpen.TaggedObject): 
    """ Represent an abstract object on display style. """


    ## Getter for property: (str) JournalIdentifier
    ##   the identifier that would be recorded in a journal for this object.  
    ##    
    ##             This may not be the same across different releases of the software.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
          the identifier that would be recorded in a journal for this object.  
           
                    This may not be the same across different releases of the software.   
         
        """
        pass
    
    ## Getter for property: (@link IDisplayStyle NXOpen.CAE.Xyplot.IDisplayStyle@endlink) Owner
    ##   the owner style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return IDisplayStyle
    @property
    def Owner(self) -> IDisplayStyle:
        """
        Getter for property: (@link IDisplayStyle NXOpen.CAE.Xyplot.IDisplayStyle@endlink) Owner
          the owner style   
            
         
        """
        pass
    
    ##  Finds the @link  NXOpen::TaggedObject   NXOpen::TaggedObject @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def Find(tObject: BaseDisplayStyleSetting, journal_identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the @link  NXOpen::TaggedObject   NXOpen::TaggedObject @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
import NXOpen
##  Represents the base grid layout display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BaseGridLayoutStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the base grid layout display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
    ##   the background color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def BackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
          the background color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor

    ##   the background color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @BackgroundColor.setter
    def BackgroundColor(self, bGcolor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
          the background color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorOfBackgroundPlane
    ##   the color of grid background plane  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ColorOfBackgroundPlane(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorOfBackgroundPlane
          the color of grid background plane  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorOfBackgroundPlane

    ##   the color of grid background plane  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ColorOfBackgroundPlane.setter
    def ColorOfBackgroundPlane(self, bGcolor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorOfBackgroundPlane
          the color of grid background plane  
            
         
        """
        pass
    
    ## Getter for property: (int) ContouringLevel
    ##   the contouring level.  
    ##    The value is greater than 0.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ContouringLevel(self) -> int:
        """
        Getter for property: (int) ContouringLevel
          the contouring level.  
           The value is greater than 0.   
         
        """
        pass
    
    ## Setter for property: (int) ContouringLevel

    ##   the contouring level.  
    ##    The value is greater than 0.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ContouringLevel.setter
    def ContouringLevel(self, contouringLevel: int):
        """
        Setter for property: (int) ContouringLevel
          the contouring level.  
           The value is greater than 0.   
         
        """
        pass
    
    ## Getter for property: (@link ContouringRange NXOpen.CAE.Xyplot.ContouringRange@endlink) ContouringRange
    ##   the option to show contour range either on the border or the faces of the grid.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ContouringRange
    @property
    def ContouringRange(self) -> ContouringRange:
        """
        Getter for property: (@link ContouringRange NXOpen.CAE.Xyplot.ContouringRange@endlink) ContouringRange
          the option to show contour range either on the border or the faces of the grid.  
             
         
        """
        pass
    
    ## Setter for property: (@link ContouringRange NXOpen.CAE.Xyplot.ContouringRange@endlink) ContouringRange

    ##   the option to show contour range either on the border or the faces of the grid.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ContouringRange.setter
    def ContouringRange(self, contouringRange: ContouringRange):
        """
        Setter for property: (@link ContouringRange NXOpen.CAE.Xyplot.ContouringRange@endlink) ContouringRange
          the option to show contour range either on the border or the faces of the grid.  
             
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) DenseGridDisplayStyleSettings
    ##   the dense grid display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def DenseGridDisplayStyleSettings(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) DenseGridDisplayStyleSettings
          the dense grid display style   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayContouring
    ##   a value indicating whether to display contouring   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def DisplayContouring(self) -> bool:
        """
        Getter for property: (bool) DisplayContouring
          a value indicating whether to display contouring   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayContouring

    ##   a value indicating whether to display contouring   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DisplayContouring.setter
    def DisplayContouring(self, dispContouring: bool):
        """
        Setter for property: (bool) DisplayContouring
          a value indicating whether to display contouring   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) MajorGridDisplayStyleSettings
    ##   the major grid display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def MajorGridDisplayStyleSettings(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) MajorGridDisplayStyleSettings
          the major grid display style   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBackground
    ##   a value indicating whether to display the background   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ShowBackground(self) -> bool:
        """
        Getter for property: (bool) ShowBackground
          a value indicating whether to display the background   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBackground

    ##   a value indicating whether to display the background   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShowBackground.setter
    def ShowBackground(self, showBg: bool):
        """
        Setter for property: (bool) ShowBackground
          a value indicating whether to display the background   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBackgroundPlane
    ##   a value indicating whether to display the grid background plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowBackgroundPlane(self) -> bool:
        """
        Getter for property: (bool) ShowBackgroundPlane
          a value indicating whether to display the grid background plane   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBackgroundPlane

    ##   a value indicating whether to display the grid background plane   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowBackgroundPlane.setter
    def ShowBackgroundPlane(self, showBg: bool):
        """
        Setter for property: (bool) ShowBackgroundPlane
          a value indicating whether to display the grid background plane   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) TicksDisplayStyleSettings
    ##   the ticks display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def TicksDisplayStyleSettings(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) TicksDisplayStyleSettings
          the ticks display style   
            
         
        """
        pass
    
    ## Getter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) XyGridStyle
    ##   the grid style of XY plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return GridStyle
    @property
    def XyGridStyle(self) -> GridStyle:
        """
        Getter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) XyGridStyle
          the grid style of XY plane   
            
         
        """
        pass
    
    ## Setter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) XyGridStyle

    ##   the grid style of XY plane   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @XyGridStyle.setter
    def XyGridStyle(self, gridStyle: GridStyle):
        """
        Setter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) XyGridStyle
          the grid style of XY plane   
            
         
        """
        pass
    
import NXOpen
##  Represents the base line display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BaseLineStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the base line display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##   the line color  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the line color  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##   the line color  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the line color  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
    ##   the line font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
          the line font   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font

    ##   the line font   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Font.setter
    def Font(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
          the line font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
    ##   the line width  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
          the line width  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width

    ##   the line width  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Width.setter
    def Width(self, lineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
          the line width  
            
         
        """
        pass
    
import NXOpen
##  Represents an abstract component object on a XY graphing.  <br> not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class BaseModel(NXOpen.NXObject): 
    """ Represents an abstract component object on a XY graphing. """


    ## Getter for property: (@link BaseDisplayStyleSetting NXOpen.CAE.Xyplot.BaseDisplayStyleSetting@endlink) StyleSetting
    ##   the style setting associated to the model   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return BaseDisplayStyleSetting
    @property
    def StyleSetting(self) -> BaseDisplayStyleSetting:
        """
        Getter for property: (@link BaseDisplayStyleSetting NXOpen.CAE.Xyplot.BaseDisplayStyleSetting@endlink) StyleSetting
          the style setting associated to the model   
            
         
        """
        pass
    
import NXOpen
import NXOpen.CAE.FTK
##  Represents the parameters passed to create or modify a plot.  <br> This is an abstract class  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BasePlotParameters(NXOpen.TransientObject): 
    """ Represents the parameters passed to create or modify a plot. """


    ## Getter for property: (int) DeviceIndex
    ##   the index of device on which plot graph will be shown.  
    ##   
    ##                 A value of 1 represents the main graphic window,
    ##                 a value greater than 2 represents separate graphic window.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def DeviceIndex(self) -> int:
        """
        Getter for property: (int) DeviceIndex
          the index of device on which plot graph will be shown.  
          
                        A value of 1 represents the main graphic window,
                        a value greater than 2 represents separate graphic window.   
         
        """
        pass
    
    ## Setter for property: (int) DeviceIndex

    ##   the index of device on which plot graph will be shown.  
    ##   
    ##                 A value of 1 represents the main graphic window,
    ##                 a value greater than 2 represents separate graphic window.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DeviceIndex.setter
    def DeviceIndex(self, deviceIndex: int):
        """
        Setter for property: (int) DeviceIndex
          the index of device on which plot graph will be shown.  
          
                        A value of 1 represents the main graphic window,
                        a value greater than 2 represents separate graphic window.   
         
        """
        pass
    
    ## Getter for property: (int) ViewPortIndex
    ##   the index of a view port on main graphic window, on which plot graph will be shown.  
    ##   
    ##                 Only available when @link CAE::Xyplot::BasePlotParameters::DeviceIndex CAE::Xyplot::BasePlotParameters::DeviceIndex@endlink  is 1.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ViewPortIndex(self) -> int:
        """
        Getter for property: (int) ViewPortIndex
          the index of a view port on main graphic window, on which plot graph will be shown.  
          
                        Only available when @link CAE::Xyplot::BasePlotParameters::DeviceIndex CAE::Xyplot::BasePlotParameters::DeviceIndex@endlink  is 1.   
         
        """
        pass
    
    ## Setter for property: (int) ViewPortIndex

    ##   the index of a view port on main graphic window, on which plot graph will be shown.  
    ##   
    ##                 Only available when @link CAE::Xyplot::BasePlotParameters::DeviceIndex CAE::Xyplot::BasePlotParameters::DeviceIndex@endlink  is 1.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ViewPortIndex.setter
    def ViewPortIndex(self, viewIndex: int):
        """
        Setter for property: (int) ViewPortIndex
          the index of a view port on main graphic window, on which plot graph will be shown.  
          
                        Only available when @link CAE::Xyplot::BasePlotParameters::DeviceIndex CAE::Xyplot::BasePlotParameters::DeviceIndex@endlink  is 1.   
         
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(param: BasePlotParameters) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Gets the records to be plotted 
    ##  @return records (@link NXOpen.CAE.FTK.BaseRecord List[NXOpen.CAE.FTK.BaseRecord]@endlink):  Records .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRecords(param: BasePlotParameters) -> List[NXOpen.CAE.FTK.BaseRecord]:
        """
         Gets the records to be plotted 
         @return records (@link NXOpen.CAE.FTK.BaseRecord List[NXOpen.CAE.FTK.BaseRecord]@endlink):  Records .
        """
        pass
    
    ##  Sets the records to be plotted 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Records 
    def SetRecords(param: BasePlotParameters, records: List[NXOpen.CAE.FTK.BaseRecord]) -> None:
        """
         Sets the records to be plotted 
        """
        pass
    
##  Represents the base symbol display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> This is an abstract class.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class BaseSymbolStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the base symbol display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
    ##   the point marker   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return PointMarker
    @property
    def PointMarker(self) -> PointMarker:
        """
        Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
          the point marker   
            
         
        """
        pass
    
    ## Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker

    ##   the point marker   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @PointMarker.setter
    def PointMarker(self, pointMarker: PointMarker):
        """
        Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
          the point marker   
            
         
        """
        pass
    
import NXOpen
##  Manages the graph template  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class BaseTemplateManager(NXOpen.NXObject): 
    """ Manages the graph template """


    ##  Deletes template file 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Template file name with full path 
    def DeleteTemplate(template_manager: BaseTemplateManager, template_file: str) -> None:
        """
         Deletes template file 
        """
        pass
    
    ## Returns the default template file 
    ##  @return template_file (str):  Template file name with full path .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDefaultTemplate(template_manager: BaseTemplateManager) -> str:
        """
        Returns the default template file 
         @return template_file (str):  Template file name with full path .
        """
        pass
    
    ##  Loads the graph template file 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Template file name with full path 
    def LoadTemplate(template_manager: BaseTemplateManager, template_file: str) -> None:
        """
         Loads the graph template file 
        """
        pass
    
    ## Reload all graph template files so that the modification on the 
    ##                loaded graph template files are reset. The unloaded files under 
    ##                customer directories which is defined by environement variable 
    ##                UGII_BASE_DIR, UGII_VENDOR_DIR, UGII_SITE_DIR and UGII_USER_DIR 
    ##                will be reloaded. Also the graph templates in active root part directory 
    ##                will be reloaded if they are unloaded.  
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ReloadAllTemplateFiles(template_manager: BaseTemplateManager) -> None:
        """
        Reload all graph template files so that the modification on the 
                       loaded graph template files are reset. The unloaded files under 
                       customer directories which is defined by environement variable 
                       UGII_BASE_DIR, UGII_VENDOR_DIR, UGII_SITE_DIR and UGII_USER_DIR 
                       will be reloaded. Also the graph templates in active root part directory 
                       will be reloaded if they are unloaded.  
                    
        """
        pass
    
    ##  Renames template file 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  old template file with full path 
    def RenameTemplateFile(template_manager: BaseTemplateManager, oldTemplateFile: str, newTemplateFileName: str) -> None:
        """
         Renames template file 
        """
        pass
    
    ## Resets system template  
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ResetSystemTemplate(template_manager: BaseTemplateManager) -> None:
        """
        Resets system template  
        """
        pass
    
    ##  Resets to default value 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Template file name with full path 
    def ResetTemplate(template_manager: BaseTemplateManager, template_file: str) -> None:
        """
         Resets to default value 
        """
        pass
    
    ## Saves all templates 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SaveAllTemplates(template_manager: BaseTemplateManager) -> None:
        """
        Saves all templates 
        """
        pass
    
    ##  Saves to new template file 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Source template file name with full path 
    def SaveAsTemplate(template_manager: BaseTemplateManager, source_template_file: str, destination_template_file: str) -> None:
        """
         Saves to new template file 
        """
        pass
    
    ##  Saves to template file 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Template file name with full path 
    def SaveTemplate(template_manager: BaseTemplateManager, template_file: str) -> None:
        """
         Saves to template file 
        """
        pass
    
    ##  @brief Sets the default template file. 
    ## 
    ##  
    ##             
    ##             <ol>
    ##             <li>
    ##             If the input template file is NULL, it will remove default template state.
    ##             </li>
    ##             <li>
    ##             If the input template file is not NULL, it will set the input template as default template.
    ##             </li>
    ##             </ol>
    ##             
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Template file name with full path 
    def SetDefaultTemplate(template_manager: BaseTemplateManager, template_file: str) -> None:
        """
         @brief Sets the default template file. 
        
         
                    
                    <ol>
                    <li>
                    If the input template file is NULL, it will remove default template state.
                    </li>
                    <li>
                    If the input template file is not NULL, it will set the input template as default template.
                    </li>
                    </ol>
                    
                    
        """
        pass
    
    ##  Unloads all graph template files 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def UnloadAllTemplates(template_manager: BaseTemplateManager) -> None:
        """
         Unloads all graph template files 
        """
        pass
    
    ##  Unloads the graph template file 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ##  Template file name with full path 
    def UnloadTemplate(template_manager: BaseTemplateManager, template_file: str) -> None:
        """
         Unloads the graph template file 
        """
        pass
    
##  Represents a abstract component object on a XY graphing.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class BasicModel(BaseModel): 
    """ Represents a abstract component object on a XY graphing. """


    ## Getter for property: (@link IDisplayStyle NXOpen.CAE.Xyplot.IDisplayStyle@endlink) DisplayStyle
    ##   the model display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return IDisplayStyle
    @property
    def DisplayStyle(self) -> IDisplayStyle:
        """
        Getter for property: (@link IDisplayStyle NXOpen.CAE.Xyplot.IDisplayStyle@endlink) DisplayStyle
          the model display style   
            
         
        """
        pass
    
##  Represents the calculation function type 
##  This function has two calculation results, the first one is Maximum Amplitude value in Y axis, the second is the corresponding X value 
class CalculationFunctionType(Enum):
    """
    Members Include: <MaxAmplitude> <MinAmplitude> <MaximumRange> <Rss> <Rms> <LinearAveraging> <IntegratedValue> <SignalPower> <Loudness>
    """
    MaxAmplitude: int
    MinAmplitude: int
    MaximumRange: int
    Rss: int
    Rms: int
    LinearAveraging: int
    IntegratedValue: int
    SignalPower: int
    Loudness: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CalculationFunctionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##   @brief  Represents a data accessor to retrieve data of a function which is plotted in @link CAE::Xyplot::PlotTypePlotCampbell CAE::Xyplot::PlotTypePlotCampbell@endlink  plot.  
## 
##   
## 
##   <br>  Created in NX1926.0.0  <br> 

class CampbellFunctionDataAccessor(IFunctionDataAccessor): 
    """ <summary> Represents a data accessor to retrieve data of a function which is plotted in <ja_enum_member>CAE.Xyplot.PlotType.PlotCampbell</ja_enum_member> plot. </summary> """


    ##  Asks display data. 
    ##  @return A tuple consisting of (orderValue, independentValues, dependentValues, rpmValues). 
    ##  - orderValue is: float.
    ##  - independentValues is: List[float].
    ##  - dependentValues is: List[float].
    ##  - rpmValues is: List[float].

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskDisplayData(campbellFunctionDataAccessor: CampbellFunctionDataAccessor) -> Tuple[float, List[float], List[float], List[float]]:
        """
         Asks display data. 
         @return A tuple consisting of (orderValue, independentValues, dependentValues, rpmValues). 
         - orderValue is: float.
         - independentValues is: List[float].
         - dependentValues is: List[float].
         - rpmValues is: List[float].

        """
        pass
    
##  Represents the graph style for Campbell Plot 
##  Option to display Campbell Plot in Point style 
class CampbellGraphType(Enum):
    """
    Members Include: <Point> <Line>
    """
    Point: int
    Line: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CampbellGraphType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##   @brief  Manages the display of campbell plot. 
## 
##  
##         
##         Call @link CAE::Xyplot::I3DDataPlot::EditRecords CAE::Xyplot::I3DDataPlot::EditRecords@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class CampbellPlot(Plot): 
    """ <summary> Manages the display of campbell plot.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I3DDataPlot.EditRecords</ja_method> to edit data for this class.
        </remarks> """
    pass


##  Represents the point size type for Campbell Plot 
##  Option to display points with const diameters in Point style
class CampbellPointSizeType(Enum):
    """
    Members Include: <Const> <Variable>
    """
    Const: int
    Variable: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CampbellPointSizeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the axis display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ColorAxisStyleSetting(AxisStyleSetting): 
    """ Represents the axis display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link ColorScaleStyle NXOpen.CAE.Xyplot.ColorScaleStyle@endlink) ColorScaleStyleSetting
    ##   the color scale display style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ColorScaleStyle
    @property
    def ColorScaleStyleSetting(self) -> ColorScaleStyle:
        """
        Getter for property: (@link ColorScaleStyle NXOpen.CAE.Xyplot.ColorScaleStyle@endlink) ColorScaleStyleSetting
          the color scale display style.  
             
         
        """
        pass
    
    ## Getter for property: (@link ResultLegendStyle NXOpen.CAE.Xyplot.ResultLegendStyle@endlink) ResultLegendStyleSetting
    ##   the result legend display style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ResultLegendStyle
    @property
    def ResultLegendStyleSetting(self) -> ResultLegendStyle:
        """
        Getter for property: (@link ResultLegendStyle NXOpen.CAE.Xyplot.ResultLegendStyle@endlink) ResultLegendStyleSetting
          the result legend display style.  
             
         
        """
        pass
    
##  Represents a color axis object on a XY graphing.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class ColorAxis(AxisModel): 
    """ Represents a color axis object on a XY graphing. """


    ##  Gets the number of legend levels 
    ##  @return numLevels (int): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColorLegendLevelCount(colorAxis: ColorAxis) -> int:
        """
         Gets the number of legend levels 
         @return numLevels (int): .
        """
        pass
    
##   @brief 
##         Manages the display of color bar plot. 
## 
##  
##         
##         Call @link CAE::Xyplot::I2DDataPlot::EditRecord CAE::Xyplot::I2DDataPlot::EditRecord@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ColorBarPlot(Plot): 
    """ <summary>
        Manages the display of color bar plot.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I2DDataPlot.EditRecord</ja_method> to edit data for this class.
        </remarks> """
    pass


##  Manages the display color map graph. <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ColorMapGraph(Graph): 
    """ Manages the display color map graph."""


    ##  Creates the display order marker on the color map graph. 
    ##  @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Order Value 
    def CreateOrderMarker(graph: ColorMapGraph, orderValue: float) -> MarkerModel:
        """
         Creates the display order marker on the color map graph. 
         @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
        """
        pass
    
##   @brief 
##         Manages the display of color map plot. 
## 
##  
##         
##         Call @link CAE::Xyplot::I3DDataPlot::EditRecords CAE::Xyplot::I3DDataPlot::EditRecords@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ColorMapPlot(Plot): 
    """ <summary>
        Manages the display of color map plot.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I3DDataPlot.EditRecords</ja_method> to edit data for this class.
        </remarks> """
    pass


##  Represents the color scale display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ColorScaleStyle(BaseDisplayStyleSetting): 
    """ Represents the color scale display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (bool) AreColorLegendColorsOverridden
    ##   the option indicates whether to customize the color legend colors   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def AreColorLegendColorsOverridden(self) -> bool:
        """
        Getter for property: (bool) AreColorLegendColorsOverridden
          the option indicates whether to customize the color legend colors   
            
         
        """
        pass
    
    ## Setter for property: (bool) AreColorLegendColorsOverridden

    ##   the option indicates whether to customize the color legend colors   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AreColorLegendColorsOverridden.setter
    def AreColorLegendColorsOverridden(self, areColorsOverridden: bool):
        """
        Setter for property: (bool) AreColorLegendColorsOverridden
          the option indicates whether to customize the color legend colors   
            
         
        """
        pass
    
    ## Getter for property: (bool) AreColorLegendValuesOverridden
    ##   the option indicates whether to customize the color legend values   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def AreColorLegendValuesOverridden(self) -> bool:
        """
        Getter for property: (bool) AreColorLegendValuesOverridden
          the option indicates whether to customize the color legend values   
            
         
        """
        pass
    
    ## Setter for property: (bool) AreColorLegendValuesOverridden

    ##   the option indicates whether to customize the color legend values   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AreColorLegendValuesOverridden.setter
    def AreColorLegendValuesOverridden(self, areValuesOverridden: bool):
        """
        Setter for property: (bool) AreColorLegendValuesOverridden
          the option indicates whether to customize the color legend values   
            
         
        """
        pass
    
    ## Getter for property: (bool) AutoLevel
    ##   the option indicates whether to define color level automatically   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def AutoLevel(self) -> bool:
        """
        Getter for property: (bool) AutoLevel
          the option indicates whether to define color level automatically   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutoLevel

    ##   the option indicates whether to define color level automatically   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AutoLevel.setter
    def AutoLevel(self, useAutoLevel: bool):
        """
        Setter for property: (bool) AutoLevel
          the option indicates whether to define color level automatically   
            
         
        """
        pass
    
    ## Getter for property: (@link ColorSpectrum NXOpen.CAE.Xyplot.ColorSpectrum@endlink) ColorSpectrumType
    ##    the color spectrum type setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ColorSpectrum
    @property
    def ColorSpectrumType(self) -> ColorSpectrum:
        """
        Getter for property: (@link ColorSpectrum NXOpen.CAE.Xyplot.ColorSpectrum@endlink) ColorSpectrumType
           the color spectrum type setting   
            
         
        """
        pass
    
    ## Setter for property: (@link ColorSpectrum NXOpen.CAE.Xyplot.ColorSpectrum@endlink) ColorSpectrumType

    ##    the color spectrum type setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ColorSpectrumType.setter
    def ColorSpectrumType(self, spectrumType: ColorSpectrum):
        """
        Setter for property: (@link ColorSpectrum NXOpen.CAE.Xyplot.ColorSpectrum@endlink) ColorSpectrumType
           the color spectrum type setting   
            
         
        """
        pass
    
    ## Getter for property: (bool) InvertionSpectrum
    ##   the option indicates whether to invert color spectrum   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def InvertionSpectrum(self) -> bool:
        """
        Getter for property: (bool) InvertionSpectrum
          the option indicates whether to invert color spectrum   
            
         
        """
        pass
    
    ## Setter for property: (bool) InvertionSpectrum

    ##   the option indicates whether to invert color spectrum   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @InvertionSpectrum.setter
    def InvertionSpectrum(self, isInverted: bool):
        """
        Setter for property: (bool) InvertionSpectrum
          the option indicates whether to invert color spectrum   
            
         
        """
        pass
    
    ## Getter for property: (int) Level
    ##    the level setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def Level(self) -> int:
        """
        Getter for property: (int) Level
           the level setting   
            
         
        """
        pass
    
    ## Setter for property: (int) Level

    ##    the level setting   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Level.setter
    def Level(self, level: int):
        """
        Setter for property: (int) Level
           the level setting   
            
         
        """
        pass
    
    ## Getter for property: (str) MeasureName
    ##   the option indicates what's the measurement associated with the override settings   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def MeasureName(self) -> str:
        """
        Getter for property: (str) MeasureName
          the option indicates what's the measurement associated with the override settings   
            
         
        """
        pass
    
    ## Setter for property: (str) MeasureName

    ##   the option indicates what's the measurement associated with the override settings   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MeasureName.setter
    def MeasureName(self, measureName: str):
        """
        Setter for property: (str) MeasureName
          the option indicates what's the measurement associated with the override settings   
            
         
        """
        pass
    
    ##  Gets the overrided colors of color legend 
    ##  @return legendColors (List[int]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColorLegendColorsOverridden(pColorScaleStyle: ColorScaleStyle) -> List[int]:
        """
         Gets the overrided colors of color legend 
         @return legendColors (List[int]): .
        """
        pass
    
    ##  Gets the overrided values of color legend 
    ##  @return overridedValues (List[float]): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColorLegendValuesOverridden(pColorScaleStyle: ColorScaleStyle) -> List[float]:
        """
         Gets the overrided values of color legend 
         @return overridedValues (List[float]): .
        """
        pass
    
    ##  Sets the overrided colors of color legend 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="legendColors"> (List[int]) </param>
    def SetColorLegendColorsOverridden(pColorScaleStyle: ColorScaleStyle, legendColors: List[int]) -> None:
        """
         Sets the overrided colors of color legend 
        """
        pass
    
    ##  Sets the overrided values of color legend  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  Makes sure overridedValues are in default unit of @link CAE::Xyplot::ColorScaleStyle::MeasureName CAE::Xyplot::ColorScaleStyle::MeasureName@endlink 
    def SetColorLegendValuesOverridden(pColorScaleStyle: ColorScaleStyle, overridedValues: List[float]) -> None:
        """
         Sets the overrided values of color legend  
        """
        pass
    
##  Represents the color spectrum type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Structural</term><description> 
## </description> </item><item><term> 
## Thermal</term><description> 
## </description> </item><item><term> 
## Grayscale</term><description> 
## </description> </item><item><term> 
## Stoplight</term><description> 
## </description> </item></list>
class ColorSpectrum(Enum):
    """
    Members Include: <Structural> <Thermal> <Grayscale> <Stoplight>
    """
    Structural: int
    Thermal: int
    Grayscale: int
    Stoplight: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ColorSpectrum:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the 2D bar chart plot complex option 
##  Magnitude of the complex data for 2D bar chart plot 
class ComplexOption2DBarChart(Enum):
    """
    Members Include: <Magnitude> <Phase> <Real> <Imaginary> <AtPhaseAngle> <SignedMagnitude>
    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    AtPhaseAngle: int
    SignedMagnitude: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ComplexOption2DBarChart:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the 2D color contour plot complex option 
##  Magnitude of the complex data for 2D color contour plot plot 
class ComplexOption2DColorContour(Enum):
    """
    Members Include: <Magnitude> <Phase> <Real> <Imaginary> <AtPhaseAngle> <SignedMagnitude>
    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    AtPhaseAngle: int
    SignedMagnitude: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ComplexOption2DColorContour:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the 2D plot complex option 
##  Magnitude of the complex data for 2D plot 
class ComplexOption2D(Enum):
    """
    Members Include: <Magnitude> <MagnitudePhase> <Phase> <Real> <RealImaginary> <RealImaginaryPhase> <Polar> <Argand> <Polar3D> <Argand3D> <PhaseMagnitude> <ImaginaryReal> <PhaseRealImaginary> <ImaginaryRealPhase> <PhaseImaginaryReal> <Nichols> <AtPhaseAngle> <SignedMagnitude> <Directivity> <Vector>
    """
    Magnitude: int
    MagnitudePhase: int
    Phase: int
    Real: int
    RealImaginary: int
    RealImaginaryPhase: int
    Polar: int
    Argand: int
    Polar3D: int
    Argand3D: int
    PhaseMagnitude: int
    ImaginaryReal: int
    PhaseRealImaginary: int
    ImaginaryRealPhase: int
    PhaseImaginaryReal: int
    Nichols: int
    AtPhaseAngle: int
    SignedMagnitude: int
    Directivity: int
    Vector: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ComplexOption2D:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the 3D plot complex option 
##  Magnitude of the complex data for 3D plot 
class ComplexOption3D(Enum):
    """
    Members Include: <Magnitude> <Phase> <Real> <Imaginary> <Argand> <Orbit> <Nichols> <AtPhaseAngle> <SignedMagnitude>
    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    Argand: int
    Orbit: int
    Nichols: int
    AtPhaseAngle: int
    SignedMagnitude: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ComplexOption3D:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the complex option for matrix plot 2D 
##  Magnitude of the complex data for matrix 2D plot 
class ComplexOptionMatrix2D(Enum):
    """
    Members Include: <Magnitude> <Phase> <Real> <Imaginary> <AtPhaseAngle> <SignedMagnitude>
    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    AtPhaseAngle: int
    SignedMagnitude: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ComplexOptionMatrix2D:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the contouring range 
##  Option to show contour range on the border of the grid 
class ContouringRange(Enum):
    """
    Members Include: <BorderGrid> <FullGrid>
    """
    BorderGrid: int
    FullGrid: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ContouringRange:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the swap axis  type 
##  no swap for 2d 
class CoordinateType(Enum):
    """
    Members Include: <Xy> <Yx> <Xyz> <Yxz> <Zyx> <Yzx> <Xzy> <Zxy>
    """
    Xy: int
    Yx: int
    Xyz: int
    Yxz: int
    Zyx: int
    Yzx: int
    Xzy: int
    Zxy: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CoordinateType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the curve display style. Call Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified. <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CurveDisplaySettings(BaseDisplayStyleSetting): 
    """ Represents the curve display style. Call Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified."""


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##   the line color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the line color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##   the line color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the line color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
    ##   the line font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
          the line font   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font

    ##   the line font   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Font.setter
    def Font(self, gridFont: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
          the line font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
    ##   the line width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
          the line width   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width

    ##   the line width   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Width.setter
    def Width(self, gridWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
          the line width   
            
         
        """
        pass
    
##   @brief  Represents the text content definition in title options  
## 
##    <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class CustomTextStyleSetting(TextStyleSetting): 
    """ <summary> Represents the text content definition in title options </summary> """


    ## Getter for property: (bool) UseAutomatic
    ##   a value indicating whether to define text content automatically .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def UseAutomatic(self) -> bool:
        """
        Getter for property: (bool) UseAutomatic
          a value indicating whether to define text content automatically .  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseAutomatic

    ##   a value indicating whether to define text content automatically .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UseAutomatic.setter
    def UseAutomatic(self, useAutomatic: bool):
        """
        Setter for property: (bool) UseAutomatic
          a value indicating whether to define text content automatically .  
             
         
        """
        pass
    
    ##  Returns the text content defined by user. 
    ##  @return text (List[str]): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUserDefinedText(pThis: CustomTextStyleSetting) -> List[str]:
        """
         Returns the text content defined by user. 
         @return text (List[str]): .
        """
        pass
    
    ##  Sets the text content defined by user. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ##   
    def SetUserDefinedText(pThis: CustomTextStyleSetting, text: List[str]) -> None:
        """
         Sets the text content defined by user. 
        """
        pass
    
import NXOpen
import NXOpen.CAE.FTK
import NXOpen.Fields
##  XYPlot exporter function handler  <br> To obtain an instance of this class use @link NXOpen::CAE::Xyplot::XYPlotManager::DataExporter NXOpen::CAE::Xyplot::XYPlotManager::DataExporter@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class DataExporter(NXOpen.Object): 
    """ XYPlot exporter function handler """


    ##  Exports calculation legends' content to output files or listing window. 
    ##             
    ##             It exports calculation legends' content to listing window if output file is not specified in@link  NXOpen::CAE::FTK::ExportFilesParameter  NXOpen::CAE::FTK::ExportFilesParameter@endlink .
    ##             
    ##             
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="exportFilesParam"> (@link NXOpen.CAE.FTK.ExportFilesParameter NXOpen.CAE.FTK.ExportFilesParameter@endlink) </param>
    ## <param name="calculationlegendTableModels"> (@link LegendTable List[NXOpen.CAE.Xyplot.LegendTable]@endlink) </param>
    def ExportCalculationLegendsToFiles(exportFilesParam: NXOpen.CAE.FTK.ExportFilesParameter, calculationlegendTableModels: List[LegendTable]) -> None:
        """
         Exports calculation legends' content to output files or listing window. 
                    
                    It exports calculation legends' content to listing window if output file is not specified in@link  NXOpen::CAE::FTK::ExportFilesParameter  NXOpen::CAE::FTK::ExportFilesParameter@endlink .
                    
                    
        """
        pass
    
    ##  Exports the data with given parameter settings to files.
    ##             
    ##             The data will be printed to listing window when no file is specified in @link  NXOpen::CAE::FTK::ExportFilesParameter  NXOpen::CAE::FTK::ExportFilesParameter@endlink .
    ##             
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="exportDataParam"> (@link DataExportParameters NXOpen.CAE.Xyplot.DataExportParameters@endlink) </param>
    ## <param name="exportFilesParam"> (@link NXOpen.CAE.FTK.ExportFilesParameter NXOpen.CAE.FTK.ExportFilesParameter@endlink) </param>
    def ExportToFiles(exportDataParam: DataExportParameters, exportFilesParam: NXOpen.CAE.FTK.ExportFilesParameter) -> None:
        """
         Exports the data with given parameter settings to files.
                    
                    The data will be printed to listing window when no file is specified in @link  NXOpen::CAE::FTK::ExportFilesParameter  NXOpen::CAE::FTK::ExportFilesParameter@endlink .
                    
                    
        """
        pass
    
    ##  Exports data with given parameter settings to table field.
    ##                 Field names can be specified optionally. If not specified, the field name will be set with default record name.
    ##                 This does not support for BarChart and Matrix Plot.
    ##  @return tables (@link NXOpen.Fields.FieldTable List[NXOpen.Fields.FieldTable]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="exportParam"> (@link DataExportParameters NXOpen.CAE.Xyplot.DataExportParameters@endlink) </param>
    ## <param name="customFieldNames"> (List[str]) </param>
    def ExportToTableField(exportParam: DataExportParameters, customFieldNames: List[str]) -> List[NXOpen.Fields.FieldTable]:
        """
         Exports data with given parameter settings to table field.
                        Field names can be specified optionally. If not specified, the field name will be set with default record name.
                        This does not support for BarChart and Matrix Plot.
         @return tables (@link NXOpen.Fields.FieldTable List[NXOpen.Fields.FieldTable]@endlink): .
        """
        pass
    
    ##  Creates an object @link  NXOpen::CAE::Xyplot::DisplayDataExportParameters   NXOpen::CAE::Xyplot::DisplayDataExportParameters @endlink  to contain the
    ##                 settings when exporting display data. The object needs to be destroyed after excuting exporting data. 
    ##                 The display data means the current data displayed on the view excluding zoom status, show/hide status, display style(line, bar, scatter etc.). 
    ##  @return displayExportParam (@link DisplayDataExportParameters NXOpen.CAE.Xyplot.DisplayDataExportParameters@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewDisplayDataExportParameters() -> DisplayDataExportParameters:
        """
         Creates an object @link  NXOpen::CAE::Xyplot::DisplayDataExportParameters   NXOpen::CAE::Xyplot::DisplayDataExportParameters @endlink  to contain the
                        settings when exporting display data. The object needs to be destroyed after excuting exporting data. 
                        The display data means the current data displayed on the view excluding zoom status, show/hide status, display style(line, bar, scatter etc.). 
         @return displayExportParam (@link DisplayDataExportParameters NXOpen.CAE.Xyplot.DisplayDataExportParameters@endlink): .
        """
        pass
    
    ##  Creates an object @link  NXOpen::CAE::FTK::ExportFilesParameter   NXOpen::CAE::FTK::ExportFilesParameter @endlink  to contain the
    ##                 settings when exporting data. The object needs to be destroyed after excuting exporting data. 
    ##  @return exportFilesParam (@link NXOpen.CAE.FTK.ExportFilesParameter NXOpen.CAE.FTK.ExportFilesParameter@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewExportFilesParameters() -> NXOpen.CAE.FTK.ExportFilesParameter:
        """
         Creates an object @link  NXOpen::CAE::FTK::ExportFilesParameter   NXOpen::CAE::FTK::ExportFilesParameter @endlink  to contain the
                        settings when exporting data. The object needs to be destroyed after excuting exporting data. 
         @return exportFilesParam (@link NXOpen.CAE.FTK.ExportFilesParameter NXOpen.CAE.FTK.ExportFilesParameter@endlink): .
        """
        pass
    
    ##  Creates an object @link  NXOpen::CAE::Xyplot::SourceDataExportParameters   NXOpen::CAE::Xyplot::SourceDataExportParameters @endlink  to contain the
    ##                 settings when exporting source data. This object needs to be destroyed after excuting exporting data. 
    ##  @return sourceExportParam (@link SourceDataExportParameters NXOpen.CAE.Xyplot.SourceDataExportParameters@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewSourceDataExportParameters() -> SourceDataExportParameters:
        """
         Creates an object @link  NXOpen::CAE::Xyplot::SourceDataExportParameters   NXOpen::CAE::Xyplot::SourceDataExportParameters @endlink  to contain the
                        settings when exporting source data. This object needs to be destroyed after excuting exporting data. 
         @return sourceExportParam (@link SourceDataExportParameters NXOpen.CAE.Xyplot.SourceDataExportParameters@endlink): .
        """
        pass
    
import NXOpen
##  Represents the parameters passed to export the data of a plot.  <br> This is an abstract class  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class DataExportParameters(NXOpen.TransientObject): 
    """ Represents the parameters passed to export the data of a plot. """


    ## Getter for property: (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) Plot
    ##   the plot which is being exported.  
    ##    Uses this method when all exported data are in same plot,
    ##             otherwise uses method @link CAE::Xyplot::DataExportParameters::GetPlots CAE::Xyplot::DataExportParameters::GetPlots@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return Plot
    @property
    def Plot(self) -> Plot:
        """
        Getter for property: (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) Plot
          the plot which is being exported.  
           Uses this method when all exported data are in same plot,
                    otherwise uses method @link CAE::Xyplot::DataExportParameters::GetPlots CAE::Xyplot::DataExportParameters::GetPlots@endlink    
         
        """
        pass
    
    ## Setter for property: (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) Plot

    ##   the plot which is being exported.  
    ##    Uses this method when all exported data are in same plot,
    ##             otherwise uses method @link CAE::Xyplot::DataExportParameters::GetPlots CAE::Xyplot::DataExportParameters::GetPlots@endlink    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Plot.setter
    def Plot(self, plot: Plot):
        """
        Setter for property: (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) Plot
          the plot which is being exported.  
           Uses this method when all exported data are in same plot,
                    otherwise uses method @link CAE::Xyplot::DataExportParameters::GetPlots CAE::Xyplot::DataExportParameters::GetPlots@endlink    
         
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(param: DataExportParameters) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Gets the plots which data is to be exported 
    ##  @return plots (@link Plot List[NXOpen.CAE.Xyplot.Plot]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPlots(param: DataExportParameters) -> List[Plot]:
        """
         Gets the plots which data is to be exported 
         @return plots (@link Plot List[NXOpen.CAE.Xyplot.Plot]@endlink): .
        """
        pass
    
    ##  Gets the data index vector of the plot. 
    ##  @return plotDataIndices (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRecordIndices(param: DataExportParameters) -> List[int]:
        """
         Gets the data index vector of the plot. 
         @return plotDataIndices (List[int]): .
        """
        pass
    
    ##  Sets the plots which data is to be exported 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="plots"> (@link Plot List[NXOpen.CAE.Xyplot.Plot]@endlink) </param>
    def SetPlots(param: DataExportParameters, plots: List[Plot]) -> None:
        """
         Sets the plots which data is to be exported 
        """
        pass
    
    ##  Sets the plot data index vector 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="plotDataIndices"> (List[int]) </param>
    def SetRecordIndices(param: DataExportParameters, plotDataIndices: List[int]) -> None:
        """
         Sets the plot data index vector 
        """
        pass
    
##  Represents the decimal number format 
##  Show decimal automatically 
class DecimalFormat(Enum):
    """
    Members Include: <Actual> <X> <Xx> <Xxx> <Xxxx> <Xexx> <Xxexx> <Xxxexx> <Xxxxexx>
    """
    Actual: int
    X: int
    Xx: int
    Xxx: int
    Xxxx: int
    Xexx: int
    Xxexx: int
    Xxxexx: int
    Xxxxexx: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> DecimalFormat:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Manages the 2D bar chart diagram display styles. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class DiagramDisplayStyles2DBarChart(DiagramDisplayStyles): 
    """ Manages the 2D bar chart diagram display styles. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (int) SpaceBetweenFunctions
    ##   the space between functions measured in percentage.  
    ##    The acceptable range is 0-10.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def SpaceBetweenFunctions(self) -> int:
        """
        Getter for property: (int) SpaceBetweenFunctions
          the space between functions measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    
    ## Setter for property: (int) SpaceBetweenFunctions

    ##   the space between functions measured in percentage.  
    ##    The acceptable range is 0-10.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SpaceBetweenFunctions.setter
    def SpaceBetweenFunctions(self, spaceBetweenFunctions: int):
        """
        Setter for property: (int) SpaceBetweenFunctions
          the space between functions measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    
    ## Getter for property: (int) SpaceBetweenItems
    ##   the space between items measured in percentage.  
    ##    The acceptable range is 0-10.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def SpaceBetweenItems(self) -> int:
        """
        Getter for property: (int) SpaceBetweenItems
          the space between items measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    
    ## Setter for property: (int) SpaceBetweenItems

    ##   the space between items measured in percentage.  
    ##    The acceptable range is 0-10.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SpaceBetweenItems.setter
    def SpaceBetweenItems(self, spaceBetweenItems: int):
        """
        Setter for property: (int) SpaceBetweenItems
          the space between items measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    
    ##  Gets the bar chart bar display style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return barChartStyle (@link BarChartStyleSetting NXOpen.CAE.Xyplot.BarChartStyleSetting@endlink):  Bar Chart Bar style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetBarChartStyleSetting(diagramStyles: DiagramDisplayStyles2DBarChart, styleIndex: int) -> BarChartStyleSetting:
        """
         Gets the bar chart bar display style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return barChartStyle (@link BarChartStyleSetting NXOpen.CAE.Xyplot.BarChartStyleSetting@endlink):  Bar Chart Bar style .
        """
        pass
    
##  Manages the display styles for 2D diagram.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class DiagramDisplayStyles2D(DiagramDisplayStyles): 
    """ Manages the display styles for 2D diagram. """


    ##  Gets the nth graph options display style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return graphOptions (@link GraphOptionsStyle2D NXOpen.CAE.Xyplot.GraphOptionsStyle2D@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetGraphOptionsStyle(diagramStyles: DiagramDisplayStyles2D, styleIndex: int) -> GraphOptionsStyle2D:
        """
         Gets the nth graph options display style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return graphOptions (@link GraphOptionsStyle2D NXOpen.CAE.Xyplot.GraphOptionsStyle2D@endlink): .
        """
        pass
    
import NXOpen
##  Manages the diagram display styles of Campbell Plot. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class DiagramDisplayStylesCampbell(DiagramDisplayStyles): 
    """ Manages the diagram display styles of Campbell Plot. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link CampbellGraphType NXOpen.CAE.Xyplot.CampbellGraphType@endlink) GraphType
    ##   the graph type for Campbell Plot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return CampbellGraphType
    @property
    def GraphType(self) -> CampbellGraphType:
        """
        Getter for property: (@link CampbellGraphType NXOpen.CAE.Xyplot.CampbellGraphType@endlink) GraphType
          the graph type for Campbell Plot   
            
         
        """
        pass
    
    ## Setter for property: (@link CampbellGraphType NXOpen.CAE.Xyplot.CampbellGraphType@endlink) GraphType

    ##   the graph type for Campbell Plot   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GraphType.setter
    def GraphType(self, graphStyle: CampbellGraphType):
        """
        Setter for property: (@link CampbellGraphType NXOpen.CAE.Xyplot.CampbellGraphType@endlink) GraphType
          the graph type for Campbell Plot   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
    ##   the line width.  
    ##    
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
          the line width.  
           
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth

    ##   the line width.  
    ##    
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LineWidth.setter
    def LineWidth(self, lineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
          the line width.  
           
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
    ##   the point marker.  
    ##   
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return PointMarker
    @property
    def PointMarker(self) -> PointMarker:
        """
        Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
          the point marker.  
          
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker

    ##   the point marker.  
    ##   
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PointMarker.setter
    def PointMarker(self, pointMarker: PointMarker):
        """
        Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
          the point marker.  
          
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypeLine CAE::Xyplot::CampbellGraphTypeLine@endlink .   
         
        """
        pass
    
    ## Getter for property: (float) PointSizeScale
    ##   the scale of point size which must between 0.  
    ##   5 and 2.0. 
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def PointSizeScale(self) -> float:
        """
        Getter for property: (float) PointSizeScale
          the scale of point size which must between 0.  
          5 and 2.0. 
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
         
        """
        pass
    
    ## Setter for property: (float) PointSizeScale

    ##   the scale of point size which must between 0.  
    ##   5 and 2.0. 
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PointSizeScale.setter
    def PointSizeScale(self, sizeScale: float):
        """
        Setter for property: (float) PointSizeScale
          the scale of point size which must between 0.  
          5 and 2.0. 
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link CampbellPointSizeType NXOpen.CAE.Xyplot.CampbellPointSizeType@endlink) PointSizeType
    ##   the style of point size.  
    ##    
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return CampbellPointSizeType
    @property
    def PointSizeType(self) -> CampbellPointSizeType:
        """
        Getter for property: (@link CampbellPointSizeType NXOpen.CAE.Xyplot.CampbellPointSizeType@endlink) PointSizeType
          the style of point size.  
           
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link CampbellPointSizeType NXOpen.CAE.Xyplot.CampbellPointSizeType@endlink) PointSizeType

    ##   the style of point size.  
    ##    
    ##                 Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
    ##                 is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PointSizeType.setter
    def PointSizeType(self, sizeStyle: CampbellPointSizeType):
        """
        Setter for property: (@link CampbellPointSizeType NXOpen.CAE.Xyplot.CampbellPointSizeType@endlink) PointSizeType
          the style of point size.  
           
                        Only available when @link CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType@endlink  
                        is @link CAE::Xyplot::CampbellGraphTypePoint CAE::Xyplot::CampbellGraphTypePoint@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) ShowBackground
    ##   a value indicating whether to show background in color of the minimmum value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ShowBackground(self) -> bool:
        """
        Getter for property: (bool) ShowBackground
          a value indicating whether to show background in color of the minimmum value   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBackground

    ##   a value indicating whether to show background in color of the minimmum value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ShowBackground.setter
    def ShowBackground(self, showBackground: bool):
        """
        Setter for property: (bool) ShowBackground
          a value indicating whether to show background in color of the minimmum value   
            
         
        """
        pass
    
##  Manages the display styles for ColorMap diagram.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class DiagramDisplayStylesColorMap(DiagramDisplayStyles): 
    """ Manages the display styles for ColorMap diagram. """


    ## Getter for property: (@link GraphOptionsStyleColorMap NXOpen.CAE.Xyplot.GraphOptionsStyleColorMap@endlink) GraphOptionsStyle
    ##  the graph options style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return GraphOptionsStyleColorMap
    @property
    def GraphOptionsStyle(self) -> GraphOptionsStyleColorMap:
        """
        Getter for property: (@link GraphOptionsStyleColorMap NXOpen.CAE.Xyplot.GraphOptionsStyleColorMap@endlink) GraphOptionsStyle
         the graph options style.  
             
         
        """
        pass
    
##  Manages the diagram display styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class DiagramDisplayStyles(BaseDisplayStyleSetting): 
    """ Manages the diagram display styles. """


    ## Getter for property: (int) StyleCount
    ##   the style count   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def StyleCount(self) -> int:
        """
        Getter for property: (int) StyleCount
          the style count   
            
         
        """
        pass
    
    ##  Gets the bar display style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return barStyle (@link BaseBarStyleSetting NXOpen.CAE.Xyplot.BaseBarStyleSetting@endlink):  Bar style .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetBarStyleSetting(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> BaseBarStyleSetting:
        """
         Gets the bar display style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return barStyle (@link BaseBarStyleSetting NXOpen.CAE.Xyplot.BaseBarStyleSetting@endlink):  Bar style .
        """
        pass
    
    ##  Gets the graph style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return graphStyle (@link GraphStyle NXOpen.CAE.Xyplot.GraphStyle@endlink):  Graph style .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetGraphStyle(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> GraphStyle:
        """
         Gets the graph style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return graphStyle (@link GraphStyle NXOpen.CAE.Xyplot.GraphStyle@endlink):  Graph style .
        """
        pass
    
    ##   @brief Gets the graph style name. 
    ## 
    ##  
    ##                 The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink .
    ##  @return graphStyleName (str):  Graph style Name.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetGraphStyleName(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> str:
        """
          @brief Gets the graph style name. 
        
         
                        The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink .
         @return graphStyleName (str):  Graph style Name.
        """
        pass
    
    ##  Gets the line display style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return lineStyle (@link BaseLineStyleSetting NXOpen.CAE.Xyplot.BaseLineStyleSetting@endlink):  Line style .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetLineStyleSetting(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> BaseLineStyleSetting:
        """
         Gets the line display style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return lineStyle (@link BaseLineStyleSetting NXOpen.CAE.Xyplot.BaseLineStyleSetting@endlink):  Line style .
        """
        pass
    
    ##  Gets the scatter display style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return scatterStyle (@link ScatterStyleSetting NXOpen.CAE.Xyplot.ScatterStyleSetting@endlink):  Scatter style .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetScatterStyleSetting(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> ScatterStyleSetting:
        """
         Gets the scatter display style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return scatterStyle (@link ScatterStyleSetting NXOpen.CAE.Xyplot.ScatterStyleSetting@endlink):  Scatter style .
        """
        pass
    
    ##  Gets the surface display style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return surfaceStyle (@link SurfaceStyleSetting NXOpen.CAE.Xyplot.SurfaceStyleSetting@endlink):  Surface style .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetSurfaceStyleSetting(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> SurfaceStyleSetting:
        """
         Gets the surface display style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return surfaceStyle (@link SurfaceStyleSetting NXOpen.CAE.Xyplot.SurfaceStyleSetting@endlink):  Surface style .
        """
        pass
    
    ##  Gets the vector display style. The style index must be greater than or equal to 0 and
    ##             less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ##  @return vectorStyle (@link VectorStyle2DSetting NXOpen.CAE.Xyplot.VectorStyle2DSetting@endlink):  Line style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def GetVectorStyleSetting(diagramStyles: DiagramDisplayStyles, styleIndex: int) -> VectorStyle2DSetting:
        """
         Gets the vector display style. The style index must be greater than or equal to 0 and
                    less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
         @return vectorStyle (@link VectorStyle2DSetting NXOpen.CAE.Xyplot.VectorStyle2DSetting@endlink):  Line style .
        """
        pass
    
    ##  Sets the graph style. The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def SetGraphStyle(diagramStyles: DiagramDisplayStyles, styleIndex: int, graphStyle: GraphStyle) -> None:
        """
         Sets the graph style. The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink . 
        """
        pass
    
    ##   @brief Sets the graph style name. 
    ## 
    ##  
    ##                 The style index must be greater than or equal to 0 and
    ##                 less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Style index 
    def SetGraphStyleName(diagramStyles: DiagramDisplayStyles, styleIndex: int, graphStyleName: str) -> None:
        """
          @brief Sets the graph style name. 
        
         
                        The style index must be greater than or equal to 0 and
                        less than @link CAE::Xyplot::DiagramDisplayStyles::StyleCount  CAE::Xyplot::DiagramDisplayStyles::StyleCount @endlink .
        """
        pass
    
##  Represents the direction option 
##  Option to show plot in the X axis direction 
class Direction(Enum):
    """
    Members Include: <X> <Z> <Xz>
    """
    X: int
    Z: int
    Xz: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Direction:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the parameter settings for export display data. <br> To create a new instance of this class, use @link NXOpen::CAE::Xyplot::DataExporter::NewDisplayDataExportParameters  NXOpen::CAE::Xyplot::DataExporter::NewDisplayDataExportParameters @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class DisplayDataExportParameters(DataExportParameters): 
    """ Represents the parameter settings for export display data."""


    ##  Gets the graph index vector 
    ##  @return graphIndices (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGraphIndices(param: DisplayDataExportParameters) -> List[int]:
        """
         Gets the graph index vector 
         @return graphIndices (List[int]): .
        """
        pass
    
    ##  Sets the graph index vector. The count of graph indices must be same to record indices. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="graphIndices"> (List[int]) </param>
    def SetGraphIndices(param: DisplayDataExportParameters, graphIndices: List[int]) -> None:
        """
         Sets the graph index vector. The count of graph indices must be same to record indices. 
        """
        pass
    
##  Represents the color for flow result 
##  Uses the upper or lower color of color limits 
class FlowResultColor(Enum):
    """
    Members Include: <NotSet> <Shaded>
    """
    NotSet: int
    Shaded: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FlowResultColor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the font type 
##  NX Font 
class Fonttype(Enum):
    """
    Members Include: <Nx> <Standard>
    """
    Nx: int
    Standard: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Fonttype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the formula expression style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class FormulaExpressionStyle(BaseDisplayStyleSetting): 
    """ Represents the formula expression style. """


    ## Getter for property: (@link FormulaGridType NXOpen.CAE.Xyplot.FormulaGridType@endlink) FormulaGridType
    ##   the formula grid type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FormulaGridType
    @property
    def FormulaGridType(self) -> FormulaGridType:
        """
        Getter for property: (@link FormulaGridType NXOpen.CAE.Xyplot.FormulaGridType@endlink) FormulaGridType
          the formula grid type   
            
         
        """
        pass
    
    ## Setter for property: (@link FormulaGridType NXOpen.CAE.Xyplot.FormulaGridType@endlink) FormulaGridType

    ##   the formula grid type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FormulaGridType.setter
    def FormulaGridType(self, formulaGridType: FormulaGridType):
        """
        Setter for property: (@link FormulaGridType NXOpen.CAE.Xyplot.FormulaGridType@endlink) FormulaGridType
          the formula grid type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsIncludeNegativeInfinity
    ##   a value indicating whether to include negative infinity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsIncludeNegativeInfinity(self) -> bool:
        """
        Getter for property: (bool) IsIncludeNegativeInfinity
          a value indicating whether to include negative infinity   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsIncludeNegativeInfinity

    ##   a value indicating whether to include negative infinity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsIncludeNegativeInfinity.setter
    def IsIncludeNegativeInfinity(self, isInclude: bool):
        """
        Setter for property: (bool) IsIncludeNegativeInfinity
          a value indicating whether to include negative infinity   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsIncludePositiveInfinity
    ##   a value indicating whether to include positive infinity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def IsIncludePositiveInfinity(self) -> bool:
        """
        Getter for property: (bool) IsIncludePositiveInfinity
          a value indicating whether to include positive infinity   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsIncludePositiveInfinity

    ##   a value indicating whether to include positive infinity   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @IsIncludePositiveInfinity.setter
    def IsIncludePositiveInfinity(self, isInclude: bool):
        """
        Setter for property: (bool) IsIncludePositiveInfinity
          a value indicating whether to include positive infinity   
            
         
        """
        pass
    
    ##  Get the variable values 
    ##  @return variableValues (List[float]):  Get the variable values .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetVariableValues(pThis: FormulaExpressionStyle) -> List[float]:
        """
         Get the variable values 
         @return variableValues (List[float]):  Get the variable values .
        """
        pass
    
    ##  Set the variable values 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Set the variable values 
    def SetVariableValues(pThis: FormulaExpressionStyle, variableValues: List[float]) -> None:
        """
         Set the variable values 
        """
        pass
    
##  Manages the formula grid style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class FormulaGridStyle(BaseDisplayStyleSetting): 
    """ Manages the formula grid style. """


    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  Gets the formula expression style. 
    ##  @return pExpressionStyle (@link FormulaExpressionStyle NXOpen.CAE.Xyplot.FormulaExpressionStyle@endlink):  expression style .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExpressionStyle(pFormulaGridStyle: FormulaGridStyle) -> FormulaExpressionStyle:
        """
         Gets the formula expression style. 
         @return pExpressionStyle (@link FormulaExpressionStyle NXOpen.CAE.Xyplot.FormulaExpressionStyle@endlink):  expression style .
        """
        pass
    
    ##  Gets the grid line style. 
    ##  @return pGridLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):  grid line style .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGridLineStyle(pFormulaGridStyle: FormulaGridStyle) -> CurveDisplaySettings:
        """
         Gets the grid line style. 
         @return pGridLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):  grid line style .
        """
        pass
    
    ##  Gets the grid value text style. 
    ##  @return pGridValueTextStyle (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink):  grid value text style .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGridValueTextStyle(pFormulaGridStyle: FormulaGridStyle) -> TextStyleSetting:
        """
         Gets the grid value text style. 
         @return pGridValueTextStyle (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink):  grid value text style .
        """
        pass
    
##  Represents the formula grid type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
## </description> </item><item><term> 
## DiagonalLineInHaighDiagram</term><description> 
## </description> </item></list>
class FormulaGridType(Enum):
    """
    Members Include: <NotSet> <DiagonalLineInHaighDiagram>
    """
    NotSet: int
    DiagonalLineInHaighDiagram: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FormulaGridType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the frequency band summation band type mode 
##  Mode to follow the synchronization driven by current curve or other curves and axes 
class FrequencyBandSummationBandTypeMode(Enum):
    """
    Members Include: <Infer> <UserDefined>
    """
    Infer: int
    UserDefined: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FrequencyBandSummationBandTypeMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the frequency band summation band type 
##  Octave 
class FrequencyBandSummationBandType(Enum):
    """
    Members Include: <Octave> <OneThirdOctave> <OneTwelfthOctave>
    """
    Octave: int
    OneThirdOctave: int
    OneTwelfthOctave: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FrequencyBandSummationBandType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the frequency band summation display mode 
##  Step Lines 
class FrequencyBandSummationDisplayMode(Enum):
    """
    Members Include: <StepLines> <ConnectCentralFrequencies>
    """
    StepLines: int
    ConnectCentralFrequencies: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FrequencyBandSummationDisplayMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the frequency band summation display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class FrequencyBandSummationStyle(BaseDisplayStyleSetting): 
    """ Represents the frequency band summation display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) BandType
    ##   a value specifies the frequency band summation band type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FrequencyBandSummationBandType
    @property
    def BandType(self) -> FrequencyBandSummationBandType:
        """
        Getter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) BandType
          a value specifies the frequency band summation band type.  
             
         
        """
        pass
    
    ## Setter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) BandType

    ##   a value specifies the frequency band summation band type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BandType.setter
    def BandType(self, bandType: FrequencyBandSummationBandType):
        """
        Setter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) BandType
          a value specifies the frequency band summation band type.  
             
         
        """
        pass
    
    ## Getter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) BandTypeMode
    ##   a value specifies the frequency band summation band type mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FrequencyBandSummationBandTypeMode
    @property
    def BandTypeMode(self) -> FrequencyBandSummationBandTypeMode:
        """
        Getter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) BandTypeMode
          a value specifies the frequency band summation band type mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) BandTypeMode

    ##   a value specifies the frequency band summation band type mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BandTypeMode.setter
    def BandTypeMode(self, bandTypeMode: FrequencyBandSummationBandTypeMode):
        """
        Setter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) BandTypeMode
          a value specifies the frequency band summation band type mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) DisplayMode
    ##   a value specifies the frequency band summation display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FrequencyBandSummationDisplayMode
    @property
    def DisplayMode(self) -> FrequencyBandSummationDisplayMode:
        """
        Getter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) DisplayMode
          a value specifies the frequency band summation display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) DisplayMode

    ##   a value specifies the frequency band summation display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: FrequencyBandSummationDisplayMode):
        """
        Setter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) DisplayMode
          a value specifies the frequency band summation display mode.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   a value specifies whether to show frequency band summation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          a value specifies whether to show frequency band summation.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   a value specifies whether to show frequency band summation.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          a value specifies whether to show frequency band summation.  
             
         
        """
        pass
    
##  Represents the function data accessor type
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
## </description> </item><item><term> 
## Xy</term><description> 
## </description> </item><item><term> 
## Xyz</term><description> 
## </description> </item><item><term> 
## Argand3D</term><description> 
## </description> </item><item><term> 
## BarChart</term><description> 
## </description> </item><item><term> 
## Matrix</term><description> 
## </description> </item><item><term> 
## Campbell</term><description> 
## </description> </item></list>
class FunctionDataAccessor(Enum):
    """
    Members Include: <NotSet> <Xy> <Xyz> <Argand3D> <BarChart> <Matrix> <Campbell>
    """
    NotSet: int
    Xy: int
    Xyz: int
    Argand3D: int
    BarChart: int
    Matrix: int
    Campbell: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FunctionDataAccessor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##   @brief  Represents a data accessor to retrieve calculation results for function of @link CAE::Xyplot::CalculationFunctionType CAE::Xyplot::CalculationFunctionType@endlink .  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class FunctionLegendAccessor(NXOpen.TransientObject): 
    """ <summary> Represents a data accessor to retrieve calculation results for function of <ja_enum>CAE.Xyplot.CalculationFunctionType</ja_enum>. </summary> """


    ##  Asks the function name. 
    ##  @return funcName (str): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="funcType"> (@link CalculationFunctionType NXOpen.CAE.Xyplot.CalculationFunctionType@endlink) </param>
    def AskFunctionName(funcLegendAccessor: FunctionLegendAccessor, funcType: CalculationFunctionType) -> str:
        """
         Asks the function name. 
         @return funcName (str): .
        """
        pass
    
    ##  Asks the calcualtion result. 
    ##  @return A tuple consisting of (hasNumberValue, results). 
    ##  - hasNumberValue is: bool.
    ##  - results is: List[float].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="funcType"> (@link CalculationFunctionType NXOpen.CAE.Xyplot.CalculationFunctionType@endlink) </param>
    @staticmethod
    def AskFunctionResult(funcLegendAccessor: FunctionLegendAccessor, funcType: CalculationFunctionType) -> Tuple[bool, List[float]]:
        """
         Asks the calcualtion result. 
         @return A tuple consisting of (hasNumberValue, results). 
         - hasNumberValue is: bool.
         - results is: List[float].

        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(funcLegendAccessor: FunctionLegendAccessor) -> None:
        """
         Destroys the object. 
        """
        pass
    
##  Manages the general display styles for 2D bar chart plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class GeneralDisplayStyles2DBarChart(GeneralDisplayStyles): 
    """ Manages the general display styles for 2D bar chart plot. """


    ## Getter for property: (@link ComplexOption2DBarChart NXOpen.CAE.Xyplot.ComplexOption2DBarChart@endlink) ComplexOption
    ##   the complex option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ComplexOption2DBarChart
    @property
    def ComplexOption(self) -> ComplexOption2DBarChart:
        """
        Getter for property: (@link ComplexOption2DBarChart NXOpen.CAE.Xyplot.ComplexOption2DBarChart@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ## Setter for property: (@link ComplexOption2DBarChart NXOpen.CAE.Xyplot.ComplexOption2DBarChart@endlink) ComplexOption

    ##   the complex option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption2DBarChart):
        """
        Setter for property: (@link ComplexOption2DBarChart NXOpen.CAE.Xyplot.ComplexOption2DBarChart@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
##  Manages the general display styles for 2D color contour plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class GeneralDisplayStyles2DColorContour(GeneralDisplayStyles): 
    """ Manages the general display styles for 2D color contour plot. """


    ## Getter for property: (@link ComplexOption2DColorContour NXOpen.CAE.Xyplot.ComplexOption2DColorContour@endlink) ComplexOption
    ##   the complex option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return ComplexOption2DColorContour
    @property
    def ComplexOption(self) -> ComplexOption2DColorContour:
        """
        Getter for property: (@link ComplexOption2DColorContour NXOpen.CAE.Xyplot.ComplexOption2DColorContour@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ## Setter for property: (@link ComplexOption2DColorContour NXOpen.CAE.Xyplot.ComplexOption2DColorContour@endlink) ComplexOption

    ##   the complex option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption2DColorContour):
        """
        Setter for property: (@link ComplexOption2DColorContour NXOpen.CAE.Xyplot.ComplexOption2DColorContour@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
##  Manages the general display styles for 2D plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class GeneralDisplayStyles2D(GeneralDisplayStyles): 
    """ Manages the general display styles for 2D plot. """


    ## Getter for property: (@link ComplexOption2D NXOpen.CAE.Xyplot.ComplexOption2D@endlink) ComplexOption
    ##   the complex option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComplexOption2D
    @property
    def ComplexOption(self) -> ComplexOption2D:
        """
        Getter for property: (@link ComplexOption2D NXOpen.CAE.Xyplot.ComplexOption2D@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ## Setter for property: (@link ComplexOption2D NXOpen.CAE.Xyplot.ComplexOption2D@endlink) ComplexOption

    ##   the complex option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption2D):
        """
        Setter for property: (@link ComplexOption2D NXOpen.CAE.Xyplot.ComplexOption2D@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ##  Switches the X/Y axis 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SwitchXYAxis(generalStyles: GeneralDisplayStyles2D) -> None:
        """
         Switches the X/Y axis 
        """
        pass
    
##  Manages the general display styles for 3D plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class GeneralDisplayStyles3D(GeneralDisplayStyles): 
    """ Manages the general display styles for 3D plot. """


    ## Getter for property: (@link ComplexOption3D NXOpen.CAE.Xyplot.ComplexOption3D@endlink) ComplexOption
    ##   the complex option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return ComplexOption3D
    @property
    def ComplexOption(self) -> ComplexOption3D:
        """
        Getter for property: (@link ComplexOption3D NXOpen.CAE.Xyplot.ComplexOption3D@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ## Setter for property: (@link ComplexOption3D NXOpen.CAE.Xyplot.ComplexOption3D@endlink) ComplexOption

    ##   the complex option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption3D):
        """
        Setter for property: (@link ComplexOption3D NXOpen.CAE.Xyplot.ComplexOption3D@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
##  Manages the general display styles for matrix 2D plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class GeneralDisplayStylesMatrix2D(GeneralDisplayStyles): 
    """ Manages the general display styles for matrix 2D plot. """


    ## Getter for property: (@link ComplexOptionMatrix2D NXOpen.CAE.Xyplot.ComplexOptionMatrix2D@endlink) ComplexOption
    ##   the complex option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return ComplexOptionMatrix2D
    @property
    def ComplexOption(self) -> ComplexOptionMatrix2D:
        """
        Getter for property: (@link ComplexOptionMatrix2D NXOpen.CAE.Xyplot.ComplexOptionMatrix2D@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ## Setter for property: (@link ComplexOptionMatrix2D NXOpen.CAE.Xyplot.ComplexOptionMatrix2D@endlink) ComplexOption

    ##   the complex option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOptionMatrix2D):
        """
        Setter for property: (@link ComplexOptionMatrix2D NXOpen.CAE.Xyplot.ComplexOptionMatrix2D@endlink) ComplexOption
          the complex option   
            
         
        """
        pass
    
    ## Getter for property: (@link MatrixPlot2DLayoutMode NXOpen.CAE.Xyplot.MatrixPlot2DLayoutMode@endlink) LayoutMode
    ##   the layout mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return MatrixPlot2DLayoutMode
    @property
    def LayoutMode(self) -> MatrixPlot2DLayoutMode:
        """
        Getter for property: (@link MatrixPlot2DLayoutMode NXOpen.CAE.Xyplot.MatrixPlot2DLayoutMode@endlink) LayoutMode
          the layout mode   
            
         
        """
        pass
    
    ## Setter for property: (@link MatrixPlot2DLayoutMode NXOpen.CAE.Xyplot.MatrixPlot2DLayoutMode@endlink) LayoutMode

    ##   the layout mode   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LayoutMode.setter
    def LayoutMode(self, layoutMode: MatrixPlot2DLayoutMode):
        """
        Setter for property: (@link MatrixPlot2DLayoutMode NXOpen.CAE.Xyplot.MatrixPlot2DLayoutMode@endlink) LayoutMode
          the layout mode   
            
         
        """
        pass
    
    ##  Switches the X/Y axis 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SwitchXYAxis(generalStyles: GeneralDisplayStylesMatrix2D) -> None:
        """
         Switches the X/Y axis 
        """
        pass
    
##  Manages the general display styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class GeneralDisplayStyles(BaseDisplayStyleSetting): 
    """ Manages the general display styles. """


    ## Getter for property: (float) PhaseAngle
    ##   the phase angle in degree   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return float
    @property
    def PhaseAngle(self) -> float:
        """
        Getter for property: (float) PhaseAngle
          the phase angle in degree   
            
         
        """
        pass
    
    ## Setter for property: (float) PhaseAngle

    ##   the phase angle in degree   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @PhaseAngle.setter
    def PhaseAngle(self, phaseAngle: float):
        """
        Setter for property: (float) PhaseAngle
          the phase angle in degree   
            
         
        """
        pass
    
    ## Getter for property: (@link PhaseRangeOption NXOpen.CAE.Xyplot.PhaseRangeOption@endlink) PhaseRangeOption
    ##   the phase range option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PhaseRangeOption
    @property
    def PhaseRangeOption(self) -> PhaseRangeOption:
        """
        Getter for property: (@link PhaseRangeOption NXOpen.CAE.Xyplot.PhaseRangeOption@endlink) PhaseRangeOption
          the phase range option   
            
         
        """
        pass
    
    ## Setter for property: (@link PhaseRangeOption NXOpen.CAE.Xyplot.PhaseRangeOption@endlink) PhaseRangeOption

    ##   the phase range option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @PhaseRangeOption.setter
    def PhaseRangeOption(self, phaseRangeOption: PhaseRangeOption):
        """
        Setter for property: (@link PhaseRangeOption NXOpen.CAE.Xyplot.PhaseRangeOption@endlink) PhaseRangeOption
          the phase range option   
            
         
        """
        pass
    
##  Manages the display graph 3d.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Graph3D(Graph): 
    """ Manages the display graph 3d. """
    pass


##  Represents the position option of graph name 
##  Option to positon name on top left of grid plane     
class GraphNamePositionOption(Enum):
    """
    Members Include: <TopLeft> <TopCenter> <TopRight> <BottomLeft> <BottomCenter> <BottomRight>
    """
    TopLeft: int
    TopCenter: int
    TopRight: int
    BottomLeft: int
    BottomCenter: int
    BottomRight: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> GraphNamePositionOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the graph name display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class GraphNameStyle(TextStyleSetting): 
    """ Represents the graph name display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link GraphNamePositionOption NXOpen.CAE.Xyplot.GraphNamePositionOption@endlink) PositionOption
    ##   the option specifies how to position the graph name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return GraphNamePositionOption
    @property
    def PositionOption(self) -> GraphNamePositionOption:
        """
        Getter for property: (@link GraphNamePositionOption NXOpen.CAE.Xyplot.GraphNamePositionOption@endlink) PositionOption
          the option specifies how to position the graph name   
            
         
        """
        pass
    
    ## Setter for property: (@link GraphNamePositionOption NXOpen.CAE.Xyplot.GraphNamePositionOption@endlink) PositionOption

    ##   the option specifies how to position the graph name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PositionOption.setter
    def PositionOption(self, positionOption: GraphNamePositionOption):
        """
        Setter for property: (@link GraphNamePositionOption NXOpen.CAE.Xyplot.GraphNamePositionOption@endlink) PositionOption
          the option specifies how to position the graph name   
            
         
        """
        pass
    
##  Manages the specific settings for 2D graph.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class GraphOptionsStyle2D(BaseDisplayStyleSetting): 
    """ Manages the specific settings for 2D graph. """


    ## Getter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) FrequencyBandSummationBandType
    ##   a value specifies the frequency band summation band type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return FrequencyBandSummationBandType
    @property
    def FrequencyBandSummationBandType(self) -> FrequencyBandSummationBandType:
        """
        Getter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) FrequencyBandSummationBandType
          a value specifies the frequency band summation band type   
            
         
        """
        pass
    
    ## Setter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) FrequencyBandSummationBandType

    ##   a value specifies the frequency band summation band type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @FrequencyBandSummationBandType.setter
    def FrequencyBandSummationBandType(self, freqBandSummationBandType: FrequencyBandSummationBandType):
        """
        Setter for property: (@link FrequencyBandSummationBandType NXOpen.CAE.Xyplot.FrequencyBandSummationBandType@endlink) FrequencyBandSummationBandType
          a value specifies the frequency band summation band type   
            
         
        """
        pass
    
    ## Getter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) FrequencyBandSummationBandTypeMode
    ##   a value specifies the frequency band summation band type mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FrequencyBandSummationBandTypeMode
    @property
    def FrequencyBandSummationBandTypeMode(self) -> FrequencyBandSummationBandTypeMode:
        """
        Getter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) FrequencyBandSummationBandTypeMode
          a value specifies the frequency band summation band type mode   
            
         
        """
        pass
    
    ## Setter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) FrequencyBandSummationBandTypeMode

    ##   a value specifies the frequency band summation band type mode   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FrequencyBandSummationBandTypeMode.setter
    def FrequencyBandSummationBandTypeMode(self, freqBandSummationBandTypeMode: FrequencyBandSummationBandTypeMode):
        """
        Setter for property: (@link FrequencyBandSummationBandTypeMode NXOpen.CAE.Xyplot.FrequencyBandSummationBandTypeMode@endlink) FrequencyBandSummationBandTypeMode
          a value specifies the frequency band summation band type mode   
            
         
        """
        pass
    
    ## Getter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) FrequencyBandSummationDisplayMode
    ##   a value specifies the frequency band summation display mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FrequencyBandSummationDisplayMode
    @property
    def FrequencyBandSummationDisplayMode(self) -> FrequencyBandSummationDisplayMode:
        """
        Getter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) FrequencyBandSummationDisplayMode
          a value specifies the frequency band summation display mode   
            
         
        """
        pass
    
    ## Setter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) FrequencyBandSummationDisplayMode

    ##   a value specifies the frequency band summation display mode   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @FrequencyBandSummationDisplayMode.setter
    def FrequencyBandSummationDisplayMode(self, freqBandSummationDisplayMode: FrequencyBandSummationDisplayMode):
        """
        Setter for property: (@link FrequencyBandSummationDisplayMode NXOpen.CAE.Xyplot.FrequencyBandSummationDisplayMode@endlink) FrequencyBandSummationDisplayMode
          a value specifies the frequency band summation display mode   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFrequencyBandSummation
    ##   a value specifies whether to show frequency band summation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowFrequencyBandSummation(self) -> bool:
        """
        Getter for property: (bool) ShowFrequencyBandSummation
          a value specifies whether to show frequency band summation   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFrequencyBandSummation

    ##   a value specifies whether to show frequency band summation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowFrequencyBandSummation.setter
    def ShowFrequencyBandSummation(self, showFreqBandSummation: bool):
        """
        Setter for property: (bool) ShowFrequencyBandSummation
          a value specifies whether to show frequency band summation   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowTotalResponseLineForPolar
    ##   a value specifies whether to show total response line for 2D polar plot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowTotalResponseLineForPolar(self) -> bool:
        """
        Getter for property: (bool) ShowTotalResponseLineForPolar
          a value specifies whether to show total response line for 2D polar plot   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowTotalResponseLineForPolar

    ##   a value specifies whether to show total response line for 2D polar plot   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowTotalResponseLineForPolar.setter
    def ShowTotalResponseLineForPolar(self, showTotalResponseLineForPolar: bool):
        """
        Setter for property: (bool) ShowTotalResponseLineForPolar
          a value specifies whether to show total response line for 2D polar plot   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowTotalResponseLineForVector
    ##   a value specifies whether to show total response line for 2D vector plot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ShowTotalResponseLineForVector(self) -> bool:
        """
        Getter for property: (bool) ShowTotalResponseLineForVector
          a value specifies whether to show total response line for 2D vector plot   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowTotalResponseLineForVector

    ##   a value specifies whether to show total response line for 2D vector plot   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ShowTotalResponseLineForVector.setter
    def ShowTotalResponseLineForVector(self, showTotalResponseLineForVector: bool):
        """
        Setter for property: (bool) ShowTotalResponseLineForVector
          a value specifies whether to show total response line for 2D vector plot   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) TotalResponseLineSetting
    ##   the total response line setting   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def TotalResponseLineSetting(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) TotalResponseLineSetting
          the total response line setting   
            
         
        """
        pass
    
##  Manages the specific settings for ColorMap graph. <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class GraphOptionsStyleColorMap(BaseDisplayStyleSetting): 
    """ Manages the specific settings for ColorMap graph."""


    ## Getter for property: (@link FrequencyBandSummationStyle NXOpen.CAE.Xyplot.FrequencyBandSummationStyle@endlink) FreqBandSummationStyle
    ##  the frequency band summation style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FrequencyBandSummationStyle
    @property
    def FreqBandSummationStyle(self) -> FrequencyBandSummationStyle:
        """
        Getter for property: (@link FrequencyBandSummationStyle NXOpen.CAE.Xyplot.FrequencyBandSummationStyle@endlink) FreqBandSummationStyle
         the frequency band summation style.  
             
         
        """
        pass
    
##  Represents the plot graph style 
##  Option to display plot in curve style 
class GraphStyle(Enum):
    """
    Members Include: <Line> <Bar> <Surface> <Scatter> <ColorBar> <ColorMap> <BarChart> <Vector> <Matrix2D>
    """
    Line: int
    Bar: int
    Surface: int
    Scatter: int
    ColorBar: int
    ColorMap: int
    BarChart: int
    Vector: int
    Matrix2D: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> GraphStyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Manages the display graph. Each graph has its owner axis and graph name.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Graph(BaseModel): 
    """ Manages the display graph. Each graph has its owner axis and graph name. """


    ## Getter for property: (int) RecordCount
    ##   the record count of the graph.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def RecordCount(self) -> int:
        """
        Getter for property: (int) RecordCount
          the record count of the graph.  
             
         
        """
        pass
    
    ##   @brief  Creates an associative marker.  
    ## 
    ##  
    ##             
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive.
    ##             
    ##             
    ##  @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    def CreateAssociativeMarker(graph: Graph, recordIndex: int, attachType: AnchorType, absPercentage: float) -> MarkerModel:
        """
          @brief  Creates an associative marker.  
        
         
                    
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive.
                    
                    
         @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
        """
        pass
    
    ##   @brief  Creates a marker in the position of a source point.  
    ## 
    ##  
    ##                 
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
    ##                 The point index is between 0 and @link CAE::Xyplot::Graph::GetPointCount CAE::Xyplot::Graph::GetPointCount@endlink , 0 is inclusive. 
    ##                 
    ##             
    ##  @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    @overload
    def CreateMarker(self, graph: Graph, recordIndex: int, pointIndex: int) -> MarkerModel:
        """
          @brief  Creates a marker in the position of a source point.  
        
         
                        
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
                        The point index is between 0 and @link CAE::Xyplot::Graph::GetPointCount CAE::Xyplot::Graph::GetPointCount@endlink , 0 is inclusive. 
                        
                    
         @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
        """
        pass
    
    ##   @brief  Creates a marker in the linear interpolation position between two source points.  
    ## 
    ##  
    ##             
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
    ##                 The previous point index is between 0 and @link CAE::Xyplot::Graph::GetPointCount CAE::Xyplot::Graph::GetPointCount@endlink , 0 is inclusive.
    ##                 The next point index is between 0 and @link CAE::Xyplot::Graph::GetPointCount CAE::Xyplot::Graph::GetPointCount@endlink , 0 is inclusive. 
    ##                 The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
    ##             
    ##             
    ##  @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    @overload
    def CreateMarker(self, graph: Graph, recordIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
          @brief  Creates a marker in the linear interpolation position between two source points.  
        
         
                    
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
                        The previous point index is between 0 and @link CAE::Xyplot::Graph::GetPointCount CAE::Xyplot::Graph::GetPointCount@endlink , 0 is inclusive.
                        The next point index is between 0 and @link CAE::Xyplot::Graph::GetPointCount CAE::Xyplot::Graph::GetPointCount@endlink , 0 is inclusive. 
                        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
                    
                    
         @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
        """
        pass
    
    ##  Creates Order Marker and show it in a graph which plot type is @link CAE::Xyplot::PlotTypePlotCampbell CAE::Xyplot::PlotTypePlotCampbell@endlink . 
    ##  @return orderMarkerModel (@link OrderMarkerModel NXOpen.CAE.Xyplot.OrderMarkerModel@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    def CreateOrderMarker(pGraph: Graph, recordIndex: int) -> OrderMarkerModel:
        """
         Creates Order Marker and show it in a graph which plot type is @link CAE::Xyplot::PlotTypePlotCampbell CAE::Xyplot::PlotTypePlotCampbell@endlink . 
         @return orderMarkerModel (@link OrderMarkerModel NXOpen.CAE.Xyplot.OrderMarkerModel@endlink): .
        """
        pass
    
    ##   @brief  Creates an overall marker that shows a calculation result for overall operation.  
    ## 
    ##  
    ##             
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive.
    ##                 The overall marker coud only be created for the data which abscissa measurement is frequency, and different calculation algorithm is applied according to function data type.
    ##                 If the function data type is power or acoustic power, it applies with sum algorithm;
    ##                 If the function data type is PSD, it applies with integration algorithm;
    ##                 To the other types, it applies with RSS algorithm.
    ##             
    ##             
    ##  @return marker (@link OverallMarkerModel NXOpen.CAE.Xyplot.OverallMarkerModel@endlink):  Overall Marker Model .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    def CreateOverallMarker(graph: Graph, recordIndex: int) -> OverallMarkerModel:
        """
          @brief  Creates an overall marker that shows a calculation result for overall operation.  
        
         
                    
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive.
                        The overall marker coud only be created for the data which abscissa measurement is frequency, and different calculation algorithm is applied according to function data type.
                        If the function data type is power or acoustic power, it applies with sum algorithm;
                        If the function data type is PSD, it applies with integration algorithm;
                        To the other types, it applies with RSS algorithm.
                    
                    
         @return marker (@link OverallMarkerModel NXOpen.CAE.Xyplot.OverallMarkerModel@endlink):  Overall Marker Model .
        """
        pass
    
    ##  Creates sound player for a selected display data on a @link CAE::Xyplot::PlotTypePlot2D CAE::Xyplot::PlotTypePlot2D@endlink  plot. 
    ##  @return soundPlayer (@link SoundPlayer NXOpen.CAE.Xyplot.SoundPlayer@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    def CreateSoundPlayer(pGraph: Graph, recordIndex: int) -> SoundPlayer:
        """
         Creates sound player for a selected display data on a @link CAE::Xyplot::PlotTypePlot2D CAE::Xyplot::PlotTypePlot2D@endlink  plot. 
         @return soundPlayer (@link SoundPlayer NXOpen.CAE.Xyplot.SoundPlayer@endlink): .
        """
        pass
    
    ##  Gets the abscissa axes. 
    ##  @return xAxes (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAbscissaAxes(graph: Graph) -> List[BasicModel]:
        """
         Gets the abscissa axes. 
         @return xAxes (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
        """
        pass
    
    ##  Gets anchor point of a record. 
    ##  @return A tuple consisting of (hasAnchorPoint, anchorPoint). 
    ##  - hasAnchorPoint is: bool.
    ##  - anchorPoint is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    ## <param name="anchorType"> (@link AnchorType NXOpen.CAE.Xyplot.AnchorType@endlink) </param>
    @staticmethod
    def GetAnchorPointOfRecord(graph: Graph, recordIndex: int, anchorType: AnchorType) -> Tuple[bool, NXOpen.Point3d]:
        """
         Gets anchor point of a record. 
         @return A tuple consisting of (hasAnchorPoint, anchorPoint). 
         - hasAnchorPoint is: bool.
         - anchorPoint is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
    ##   @brief  Gets the display style index for a given record index in given graph. 
    ## 
    ##  
    ##                 
    ##                      The record index must be greater than and equal to 0 and less than @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink .
    ##                      The display style index is limitted from 0 to 19.
    ##                 
    ##              
    ##  @return displayStyleIndex (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    def GetDisplayStyleOfRecord(graph: Graph, recordIndex: int) -> int:
        """
          @brief  Gets the display style index for a given record index in given graph. 
        
         
                        
                             The record index must be greater than and equal to 0 and less than @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink .
                             The display style index is limitted from 0 to 19.
                        
                     
         @return displayStyleIndex (int): .
        """
        pass
    
    ##  Gets the bounding box of the grid. 
    ##  @return A tuple consisting of (leftBottom, rightTop). 
    ##  - leftBottom is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - rightTop is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGridBoundingBox(graph: Graph) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the bounding box of the grid. 
         @return A tuple consisting of (leftBottom, rightTop). 
         - leftBottom is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - rightTop is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
    ##  Gets XY curve data source identifier by record index from graph 
    ##             
    ##             Only the data displayed on 2D graph in the following complex option type support identifier:
    ##             @link CAE::Xyplot::ComplexOption2DMagnitude CAE::Xyplot::ComplexOption2DMagnitude@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DMagnitudePhase CAE::Xyplot::ComplexOption2DMagnitudePhase@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DPhase CAE::Xyplot::ComplexOption2DPhase@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DReal CAE::Xyplot::ComplexOption2DReal@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DRealImaginary CAE::Xyplot::ComplexOption2DRealImaginary@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DRealImaginaryPhase CAE::Xyplot::ComplexOption2DRealImaginaryPhase@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DPhaseMagnitude CAE::Xyplot::ComplexOption2DPhaseMagnitude@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DImaginaryReal CAE::Xyplot::ComplexOption2DImaginaryReal@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DPhaseRealImaginary CAE::Xyplot::ComplexOption2DPhaseRealImaginary@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DImaginaryRealPhase CAE::Xyplot::ComplexOption2DImaginaryRealPhase@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DPhaseImaginaryReal CAE::Xyplot::ComplexOption2DPhaseImaginaryReal@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DAtPhaseAngle CAE::Xyplot::ComplexOption2DAtPhaseAngle@endlink 
    ##             @link CAE::Xyplot::ComplexOption2DSignedMagnitude CAE::Xyplot::ComplexOption2DSignedMagnitude@endlink 
    ##             
    ##             
    ##  @return identifier (str): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    def GetIdentifier(graph: Graph, recordIndex: int) -> str:
        """
         Gets XY curve data source identifier by record index from graph 
                    
                    Only the data displayed on 2D graph in the following complex option type support identifier:
                    @link CAE::Xyplot::ComplexOption2DMagnitude CAE::Xyplot::ComplexOption2DMagnitude@endlink 
                    @link CAE::Xyplot::ComplexOption2DMagnitudePhase CAE::Xyplot::ComplexOption2DMagnitudePhase@endlink 
                    @link CAE::Xyplot::ComplexOption2DPhase CAE::Xyplot::ComplexOption2DPhase@endlink 
                    @link CAE::Xyplot::ComplexOption2DReal CAE::Xyplot::ComplexOption2DReal@endlink 
                    @link CAE::Xyplot::ComplexOption2DRealImaginary CAE::Xyplot::ComplexOption2DRealImaginary@endlink 
                    @link CAE::Xyplot::ComplexOption2DRealImaginaryPhase CAE::Xyplot::ComplexOption2DRealImaginaryPhase@endlink 
                    @link CAE::Xyplot::ComplexOption2DPhaseMagnitude CAE::Xyplot::ComplexOption2DPhaseMagnitude@endlink 
                    @link CAE::Xyplot::ComplexOption2DImaginaryReal CAE::Xyplot::ComplexOption2DImaginaryReal@endlink 
                    @link CAE::Xyplot::ComplexOption2DPhaseRealImaginary CAE::Xyplot::ComplexOption2DPhaseRealImaginary@endlink 
                    @link CAE::Xyplot::ComplexOption2DImaginaryRealPhase CAE::Xyplot::ComplexOption2DImaginaryRealPhase@endlink 
                    @link CAE::Xyplot::ComplexOption2DPhaseImaginaryReal CAE::Xyplot::ComplexOption2DPhaseImaginaryReal@endlink 
                    @link CAE::Xyplot::ComplexOption2DAtPhaseAngle CAE::Xyplot::ComplexOption2DAtPhaseAngle@endlink 
                    @link CAE::Xyplot::ComplexOption2DSignedMagnitude CAE::Xyplot::ComplexOption2DSignedMagnitude@endlink 
                    
                    
         @return identifier (str): .
        """
        pass
    
    ##  Gets all markers on the graph. 
    ##  @return markers (@link MarkerModel List[NXOpen.CAE.Xyplot.MarkerModel]@endlink):  Marker models .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMarkers(graph: Graph) -> List[MarkerModel]:
        """
         Gets all markers on the graph. 
         @return markers (@link MarkerModel List[NXOpen.CAE.Xyplot.MarkerModel]@endlink):  Marker models .
        """
        pass
    
    ##  Gets the ordinate axes. 
    ##  @return yAxes (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOrdinateAxes(graph: Graph) -> List[BasicModel]:
        """
         Gets the ordinate axes. 
         @return yAxes (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
        """
        pass
    
    ##  Gets the point count of specified record. 
    ##  @return pointCount (int):  Point count .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    def GetPointCount(graph: Graph, recordIndex: int) -> int:
        """
         Gets the point count of specified record. 
         @return pointCount (int):  Point count .
        """
        pass
    
    ##  Gets record name. 
    ##  @return recordName (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    def GetRecordName(graph: Graph, recordIndex: int) -> str:
        """
         Gets record name. 
         @return recordName (str): .
        """
        pass
    
    ##  Gets the Z axis. 
    ##  @return zAxis (@link BasicModel NXOpen.CAE.Xyplot.BasicModel@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetZAxis(graph: Graph) -> BasicModel:
        """
         Gets the Z axis. 
         @return zAxis (@link BasicModel NXOpen.CAE.Xyplot.BasicModel@endlink): .
        """
        pass
    
    ##   @brief Restores style assignments.  
    ## 
    ##  
    ##                 
    ##                 This function just restore display style to system style assignments for current
    ##                 plot and doesn't impact on template.
    ##                 
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RestoreStyleAssignments(graph: Graph) -> None:
        """
          @brief Restores style assignments.  
        
         
                        
                        This function just restore display style to system style assignments for current
                        plot and doesn't impact on template.
                        
                    
        """
        pass
    
    ##  Saves current style assignments to template.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def SaveStyleAssignmentsToTemplate(graph: Graph) -> None:
        """
         Saves current style assignments to template.
        """
        pass
    
    ##   @brief   Sets the display style index for a given record index based on graph. 
    ## 
    ##  
    ##                 
    ##                      The record index must be greater than and equal to 0 and less than @link CAE::Xyplot::Graph::SetRecordCount CAE::Xyplot::Graph::SetRecordCount@endlink .
    ##                      The display style index is limitted from 0 to 19.
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    ## <param name="displayStyleIndex"> (int) </param>
    def SetDisplayStyleOfRecord(graph: Graph, recordIndex: int, displayStyleIndex: int) -> None:
        """
          @brief   Sets the display style index for a given record index based on graph. 
        
         
                        
                             The record index must be greater than and equal to 0 and less than @link CAE::Xyplot::Graph::SetRecordCount CAE::Xyplot::Graph::SetRecordCount@endlink .
                             The display style index is limitted from 0 to 19.
                        
                     
        """
        pass
    
    ##  Sets XY curve data source identifier by record index from graph 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    ## <param name="identifier"> (str) </param>
    def SetIdentifier(graph: Graph, recordIndex: int, identifier: str) -> None:
        """
         Sets XY curve data source identifier by record index from graph 
        """
        pass
    
    ##   @brief 
    ##                 Removes the zoom state for the graph and returns the display to the original state.
    ##                  
    ## 
    ##  
    ##                 
    ##                 The function just updates the model data. To make the display update to reflect the model change, please call
    ##                 @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
    ##                 @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink 
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Unzoom(graph: Graph) -> None:
        """
          @brief 
                        Removes the zoom state for the graph and returns the display to the original state.
                         
        
         
                        
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
                        @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink 
                        
                     
        """
        pass
    
    ##   @brief 
    ##                 Zooms the graph along X direction by a scale range basing on current X axis display range.
    ##                  
    ## 
    ##  
    ##                 
    ##                 <ol>
    ##                 <li>
    ##                 The function just updates the model data. To make the display update to reflect the model change, please call
    ##                 @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
    ##                 @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
    ##                 </li>
    ##                 <li>
    ##                 The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
    ##                 </li>
    ##                 </ol>
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the value must be between 0 and 1
    def ZoomAlongX(graph: Graph, startScale: float, endScale: float) -> None:
        """
          @brief 
                        Zooms the graph along X direction by a scale range basing on current X axis display range.
                         
        
         
                        
                        <ol>
                        <li>
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
                        @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
                        </li>
                        <li>
                        The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
                        </li>
                        </ol>
                        
                     
        """
        pass
    
    ##   @brief 
    ##                 Zooms the graph along both X and Y direction by scale ranges basing on current X and Y axis display range. It is only available to 2D plot.
    ##                  
    ## 
    ##  
    ##                 
    ##                 <ol>
    ##                 <li>
    ##                 The function just updates the model data. To make the display update to reflect the model change, please call
    ##                 @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
    ##                 @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
    ##                 </li>
    ##                 <li>
    ##                 The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
    ##                 </li>
    ##                 </ol>
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the value must be between 0 and 1
    def ZoomAlongXY(graph: Graph, xStartScale: float, xEndScale: float, yStartScale: float, yEndScale: float) -> None:
        """
          @brief 
                        Zooms the graph along both X and Y direction by scale ranges basing on current X and Y axis display range. It is only available to 2D plot.
                         
        
         
                        
                        <ol>
                        <li>
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
                        @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
                        </li>
                        <li>
                        The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
                        </li>
                        </ol>
                        
                     
        """
        pass
    
    ##   @brief 
    ##                 Zooms the graph along Y direction by a scale range basing on current Y axis display range.
    ##                  
    ## 
    ##  
    ##                 
    ##                 <ol>
    ##                 <li>
    ##                 The function just updates the model data. To make the display update to reflect the model change, please call
    ##                 @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
    ##                 @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
    ##                 </li>
    ##                 <li>
    ##                 The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
    ##                 </li>
    ##                 </ol>
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the value must be between 0 and 1
    def ZoomAlongY(graph: Graph, startScale: float, endScale: float) -> None:
        """
          @brief 
                        Zooms the graph along Y direction by a scale range basing on current Y axis display range.
                         
        
         
                        
                        <ol>
                        <li>
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
                        @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
                        </li>
                        <li>
                        The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
                        </li>
                        </ol>
                        
                     
        """
        pass
    
    ##   @brief 
    ##                 Zooms the graph along Z direction by a scale range basing on current Z axis display range. It is only available to 3D plot.
    ##                  
    ## 
    ##  
    ##                 
    ##                 <ol>
    ##                 <li>
    ##                 The function just updates the model data. To make the display update to reflect the model change, please call
    ##                 @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
    ##                 @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
    ##                 </li>
    ##                 <li>
    ##                 The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
    ##                 </li>
    ##                 </ol>
    ##                 
    ##              
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the value must be between 0 and 1
    def ZoomAlongZ(graph: Graph, startScale: float, endScale: float) -> None:
        """
          @brief 
                        Zooms the graph along Z direction by a scale range basing on current Z axis display range. It is only available to 3D plot.
                         
        
         
                        
                        <ol>
                        <li>
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  for an instance of @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  or
                        @link CAE::Xyplot::Graph CAE::Xyplot::Graph@endlink .
                        </li>
                        <li>
                        The scale range could be calculated from @link CAE::Xyplot::AxisModel::CalculateZoomScale CAE::Xyplot::AxisModel::CalculateZoomScale@endlink 
                        </li>
                        </ol>
                        
                     
        """
        pass
    
##  Represents the 2d grid layout display style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class GridLayoutStyle2DSetting(BaseGridLayoutStyleSetting): 
    """ Represents the 2d grid layout display style. """
    pass


##  Represents the 3d grid layout display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class GridLayoutStyle3DSetting(BaseGridLayoutStyleSetting): 
    """ Represents the 3d grid layout display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZxGridStyle
    ##   the grid style of ZX plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return GridStyle
    @property
    def ZxGridStyle(self) -> GridStyle:
        """
        Getter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZxGridStyle
          the grid style of ZX plane   
            
         
        """
        pass
    
    ## Setter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZxGridStyle

    ##   the grid style of ZX plane   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ZxGridStyle.setter
    def ZxGridStyle(self, gridStyle: GridStyle):
        """
        Setter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZxGridStyle
          the grid style of ZX plane   
            
         
        """
        pass
    
    ## Getter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZyGridStyle
    ##   the grid style of ZY plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return GridStyle
    @property
    def ZyGridStyle(self) -> GridStyle:
        """
        Getter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZyGridStyle
          the grid style of ZY plane   
            
         
        """
        pass
    
    ## Setter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZyGridStyle

    ##   the grid style of ZY plane   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ZyGridStyle.setter
    def ZyGridStyle(self, gridStyle: GridStyle):
        """
        Setter for property: (@link GridStyle NXOpen.CAE.Xyplot.GridStyle@endlink) ZyGridStyle
          the grid style of ZY plane   
            
         
        """
        pass
    
##  Represents the grid style for plot 
##  No grid displayed 
class GridStyle(Enum):
    """
    Members Include: <NoGrid> <GridOnly> <TicksOnly> <GridAndTicks> <DenseGrid>
    """
    NoGrid: int
    GridOnly: int
    TicksOnly: int
    GridAndTicks: int
    DenseGrid: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> GridStyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE.FTK
##   @brief  Represents a plot interface which input should be a series of 2D data  
## 
##  
##         
##         This interface is suitable for those plots which own a series of 2d data, and each data can be drawn,edited and deleted independently;
##         
##         
## 
##   <br>  Created in NX12.0.0  <br> 

class I2DDataPlot(NXOpen.Object): 
    """ <summary> Represents a plot interface which input should be a series of 2D data </summary>
        <remarks>
        This interface is suitable for those plots which own a series of 2d data, and each data can be drawn,edited and deleted independently;
        </remarks>
        """


    ##   @brief Edits nth record of plot.  
    ## 
    ##  
    ##             
    ##              <br> 
    ##             <b> Procedure of editing records of plot fully:</b>
    ##             <ol>
    ##             <li>Call this method to edit record data</li>
    ##             <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
    ##             <li>Call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
    ##             <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
    ##             </ol>
    ##              <br> 
    ##             
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nthRecordIdx"> (int) </param>
    ## <param name="record"> (@link NXOpen.CAE.FTK.BaseRecord NXOpen.CAE.FTK.BaseRecord@endlink) </param>
    @abstractmethod
    def EditRecord(plot: I2DDataPlot, nthRecordIdx: int, record: NXOpen.CAE.FTK.BaseRecord) -> None:
        """
          @brief Edits nth record of plot.  
        
         
                    
                     <br> 
                    <b> Procedure of editing records of plot fully:</b>
                    <ol>
                    <li>Call this method to edit record data</li>
                    <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
                    <li>Call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
                    <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
                    </ol>
                     <br> 
                    
                    
        """
        pass
    
import NXOpen
##   @brief  Represents a graph interface which input is 3D data 
## 
##  
##         
##         3D plot data can consist of multiple @link CAE::FTK::ArrayRecord2D CAE::FTK::ArrayRecord2D@endlink  or a @link CAE::FTK::SectionBasedMatrixRecord CAE::FTK::SectionBasedMatrixRecord@endlink 
##         
##         
## 
##   <br>  Created in NX12.0.0  <br> 

class I3DDataGraph(NXOpen.Object): 
    """ <summary> Represents a graph interface which input is 3D data</summary>
        <remarks>
        3D plot data can consist of multiple <ja_class>CAE.FTK.ArrayRecord2D</ja_class> or a <ja_class>CAE.FTK.SectionBasedMatrixRecord</ja_class>
        </remarks>
        """


    ##   @brief  Creates a marker in the position of a source point.  
    ## 
    ##  
    ##             
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
    ##                 The point index is between 0 and @link CAE::Xyplot::I3DDataGraph::GetSourcePointCount CAE::Xyplot::I3DDataGraph::GetSourcePointCount@endlink , 0 is inclusive. 
    ##             
    ##             
    ##  @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    @abstractmethod
    @overload
    def CreateMarker(self, graph: I3DDataGraph, recordIndex: int, sectionIndex: int, pointIndex: int) -> MarkerModel:
        """
          @brief  Creates a marker in the position of a source point.  
        
         
                    
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
                        The point index is between 0 and @link CAE::Xyplot::I3DDataGraph::GetSourcePointCount CAE::Xyplot::I3DDataGraph::GetSourcePointCount@endlink , 0 is inclusive. 
                    
                    
         @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
        """
        pass
    
    ##   @brief  Creates a marker in the linear interpolation position between two source points.  
    ## 
    ##  
    ##             
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
    ##                 The previous/next point index is between 0 and @link CAE::Xyplot::I3DDataGraph::GetSourcePointCount CAE::Xyplot::I3DDataGraph::GetSourcePointCount@endlink , 0 is inclusive.
    ##                 The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
    ##             
    ##             
    ##  @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    @abstractmethod
    @overload
    def CreateMarker(self, graph: I3DDataGraph, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
          @brief  Creates a marker in the linear interpolation position between two source points.  
        
         
                    
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive. 
                        The previous/next point index is between 0 and @link CAE::Xyplot::I3DDataGraph::GetSourcePointCount CAE::Xyplot::I3DDataGraph::GetSourcePointCount@endlink , 0 is inclusive.
                        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
                    
                    
         @return marker (@link MarkerModel NXOpen.CAE.Xyplot.MarkerModel@endlink):  Marker model .
        """
        pass
    
    ##   @brief  Gets the source point count of specified record.  
    ## 
    ##  
    ##             
    ##                 The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive.
    ##             
    ##             
    ##  @return pointCount (int):  Point count .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Record index 
    @abstractmethod
    def GetSourcePointCount(graph: I3DDataGraph, recordIndex: int, sectionIndex: int) -> int:
        """
          @brief  Gets the source point count of specified record.  
        
         
                    
                        The record index is between 0 and @link CAE::Xyplot::Graph::RecordCount CAE::Xyplot::Graph::RecordCount@endlink , 0 is inclusive.
                    
                    
         @return pointCount (int):  Point count .
        """
        pass
    
import NXOpen
import NXOpen.CAE.FTK
##   @brief  Represents a plot interface which input is 3D data 
## 
##  
##         
##         3D plot data can consist of multiple @link CAE::FTK::ArrayRecord2D CAE::FTK::ArrayRecord2D@endlink  or a @link CAE::FTK::SectionBasedMatrixRecord CAE::FTK::SectionBasedMatrixRecord@endlink 
##         To the plot class which implements this interface, all input records will be represented as a whole data.
##         
##         
## 
##   <br>  Created in NX12.0.0  <br> 

class I3DDataPlot(NXOpen.Object): 
    """ <summary> Represents a plot interface which input is 3D data</summary>
        <remarks>
        3D plot data can consist of multiple <ja_class>CAE.FTK.ArrayRecord2D</ja_class> or a <ja_class>CAE.FTK.SectionBasedMatrixRecord</ja_class>
        To the plot class which implements this interface, all input records will be represented as a whole data.
        </remarks>
        """


    ##   @brief Edits records of plot.  
    ## 
    ##  
    ##             
    ##              <br> 
    ##             <b> Procedure of editing records of plot fully:</b>
    ##             <ol>
    ##             <li>Call this method to edit record data</li>
    ##             <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
    ##             <li>Call @link CAE::Xyplot::IDisplayableModel::UpdateDisplay CAE::Xyplot::IDisplayableModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
    ##             <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
    ##             </ol>
    ##              <br> 
    ##             
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="records"> (@link NXOpen.CAE.FTK.BaseRecord List[NXOpen.CAE.FTK.BaseRecord]@endlink) </param>
    @abstractmethod
    def EditRecords(plot: I3DDataPlot, records: List[NXOpen.CAE.FTK.BaseRecord]) -> None:
        """
          @brief Edits records of plot.  
        
         
                    
                     <br> 
                    <b> Procedure of editing records of plot fully:</b>
                    <ol>
                    <li>Call this method to edit record data</li>
                    <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
                    <li>Call @link CAE::Xyplot::IDisplayableModel::UpdateDisplay CAE::Xyplot::IDisplayableModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
                    <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
                    </ol>
                     <br> 
                    
                    
        """
        pass
    
import NXOpen
##   @brief  Represents the axis style setting interface  
## 
##  
##         
##         This interface is suitable for those axis style which own a label style setting and an annotation style setting;
##         
##         
## 
##   <br>  Created in NX1847.0.0  <br> 

class IAxisStyle(NXOpen.Object): 
    """ <summary> Represents the axis style setting interface </summary>
        <remarks>
        This interface is suitable for those axis style which own a label style setting and an annotation style setting;
        </remarks>
        """


    ##  Gets the annotation style 
    ##  @return annotationStyle (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink):  Axis item style .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetAnnotationStyle(axisStyle: IAxisStyle) -> TextStyleSetting:
        """
         Gets the annotation style 
         @return annotationStyle (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink):  Axis item style .
        """
        pass
    
    ##  Gets the label style 
    ##  @return labelStyle (@link CustomTextStyleSetting NXOpen.CAE.Xyplot.CustomTextStyleSetting@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetLabelDisplayStyle(axisStyle: IAxisStyle) -> CustomTextStyleSetting:
        """
         Gets the label style 
         @return labelStyle (@link CustomTextStyleSetting NXOpen.CAE.Xyplot.CustomTextStyleSetting@endlink): .
        """
        pass
    
import NXOpen
##  Represents the interface for curve display style classes.
## 
##   <br>  Created in NX12.0.0  <br> 

class ICurveDisplaySettings(NXOpen.Object): 
    """ Represents the interface for curve display style classes."""


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##   the line color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    @abstractmethod
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the line color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##   the line color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the line color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
    ##   the line font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectFont
    @property
    @abstractmethod
    def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
          the line font   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font

    ##   the line font   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Font.setter
    def Font(self, gridFont: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectFont NXOpen.DisplayableObject.ObjectFont@endlink) Font
          the line font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
    ##   the line width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    @abstractmethod
    def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
          the line width   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width

    ##   the line width   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Width.setter
    def Width(self, gridWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Width
          the line width   
            
         
        """
        pass
    
import NXOpen
##  This interface is suitable for those models which can be deleted. 
## 
##   <br>  Created in NX1899.0.0  <br> 

class IDeletableModel(NXOpen.Object): 
    """ This interface is suitable for those models which can be deleted. """


    ##  Deletes the model 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def Delete(tModel: IDeletableModel) -> None:
        """
         Deletes the model 
        """
        pass
    
import NXOpen
##   @brief  This class represents an interface to the XYPLOT displayable model.  
## 
##   
## 
##   <br>  Created in NX11.0.0  <br> 

class IDisplayableModel(NXOpen.Object): 
    """ <summary> This class represents an interface to the XYPLOT displayable model. </summary> """


    ##  Updates model display 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def UpdateDisplay(displayableModel: IDisplayableModel) -> None:
        """
         Updates model display 
        """
        pass
    
import NXOpen
##  Represents the interface for  plot display style classes
## 
##   <br>  Created in NX9.0.0  <br> 

class IDisplayStyle(NXOpen.Object): 
    """ Represents the interface for  plot display style classes"""


    ## Getter for property: (@link IDisplayStyle NXOpen.CAE.Xyplot.IDisplayStyle@endlink) Owner
    ##   the owner style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return IDisplayStyle
    @property
    @abstractmethod
    def Owner(self) -> IDisplayStyle:
        """
        Getter for property: (@link IDisplayStyle NXOpen.CAE.Xyplot.IDisplayStyle@endlink) Owner
          the owner style   
            
         
        """
        pass
    
    ##  Commits any edits that have been applied to the display style.
    ##                 Triggers the corresponding plot to update graph. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def CommitChange(self) -> None:
        """
         Commits any edits that have been applied to the display style.
                        Triggers the corresponding plot to update graph. 
        """
        pass
    
import NXOpen
##   @brief  Represents a function data accessor interface to retrieve data for given graph index and record index.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class IFunctionDataAccessor(NXOpen.TransientObject): 
    """ <summary> Represents a function data accessor interface to retrieve data for given graph index and record index. </summary> """


    ## Getter for property: (str) FunctionType
    ##   the function type name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def FunctionType(self) -> str:
        """
        Getter for property: (str) FunctionType
          the function type name.  
             
         
        """
        pass
    
    ## Getter for property: (str) RecordName
    ##   the record name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def RecordName(self) -> str:
        """
        Getter for property: (str) RecordName
          the record name.  
             
         
        """
        pass
    
    ## Getter for property: (@link FunctionDataAccessor NXOpen.CAE.Xyplot.FunctionDataAccessor@endlink) Type
    ##   the function data accessor type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return FunctionDataAccessor
    @property
    def Type(self) -> FunctionDataAccessor:
        """
        Getter for property: (@link FunctionDataAccessor NXOpen.CAE.Xyplot.FunctionDataAccessor@endlink) Type
          the function data accessor type.  
             
         
        """
        pass
    
    ##  Asks axis accessor. 
    ##  @return axisAccessor (@link AxisAccessor NXOpen.CAE.Xyplot.AxisAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="axisDirection"> (@link AxisDirection NXOpen.CAE.Xyplot.AxisDirection@endlink) </param>
    def AskAxisAccessor(functionDataAccessor: IFunctionDataAccessor, axisDirection: AxisDirection) -> AxisAccessor:
        """
         Asks axis accessor. 
         @return axisAccessor (@link AxisAccessor NXOpen.CAE.Xyplot.AxisAccessor@endlink): .
        """
        pass
    
    ##  Asks color axis accessor. 
    ##  @return axisAccessor (@link AxisAccessor NXOpen.CAE.Xyplot.AxisAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskColorAxisAccessor(functionDataAccessor: IFunctionDataAccessor) -> AxisAccessor:
        """
         Asks color axis accessor. 
         @return axisAccessor (@link AxisAccessor NXOpen.CAE.Xyplot.AxisAccessor@endlink): .
        """
        pass
    
    ##  Asks function legend accessor. 
    ##  @return functionLegendAccessor (@link FunctionLegendAccessor NXOpen.CAE.Xyplot.FunctionLegendAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskFunctionLegendAccessor(functionDataAccessor: IFunctionDataAccessor) -> FunctionLegendAccessor:
        """
         Asks function legend accessor. 
         @return functionLegendAccessor (@link FunctionLegendAccessor NXOpen.CAE.Xyplot.FunctionLegendAccessor@endlink): .
        """
        pass
    
    ##  Asks legend accessor. 
    ##  @return legendAccessor (@link LegendAccessor NXOpen.CAE.Xyplot.LegendAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskLegendAccessor(functionDataAccessor: IFunctionDataAccessor) -> LegendAccessor:
        """
         Asks legend accessor. 
         @return legendAccessor (@link LegendAccessor NXOpen.CAE.Xyplot.LegendAccessor@endlink): .
        """
        pass
    
    ##  Asks overall level accessor 
    ##  @return overallLevelAccessor (@link OverallLevelAccessor NXOpen.CAE.Xyplot.OverallLevelAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskOverallLevelAccessor(functionDataAccessor: IFunctionDataAccessor) -> OverallLevelAccessor:
        """
         Asks overall level accessor 
         @return overallLevelAccessor (@link OverallLevelAccessor NXOpen.CAE.Xyplot.OverallLevelAccessor@endlink): .
        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(functionDataAccessor: IFunctionDataAccessor) -> None:
        """
         Destroys the object. 
        """
        pass
    
import NXOpen
##  This interface is suitable for those models which are derived from text model. 
## 
##   <br>  Created in NX1899.0.0  <br> 

class ITextModel(NXOpen.Object): 
    """ This interface is suitable for those models which are derived from text model. """


    ##  Results text values 
    ##  @return textValues (List[str]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    @abstractmethod
    def GetTexts(tTextModel: ITextModel) -> List[str]:
        """
         Results text values 
         @return textValues (List[str]): .
        """
        pass
    
import NXOpen
##  Represents the interface for visible display style classes.
## 
##   <br>  Created in NX12.0.0  <br> 

class IVisibleDisplayStyle(NXOpen.Object): 
    """ Represents the interface for visible display style classes."""


    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    @abstractmethod
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
import NXOpen
##  Manages the Leader display styles.  <br> Not support KF.  <br> 
class LeaderStyle(NXOpen.TaggedObject): 
    """ Manages the Leader display styles. """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AnchorColor
    ##   the anchor color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def AnchorColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AnchorColor
          the anchor color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AnchorColor

    ##   the anchor color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AnchorColor.setter
    def AnchorColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AnchorColor
          the anchor color   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) LineStyle
    ##   the line display style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def LineStyle(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) LineStyle
          the line display style.  
             
         
        """
        pass
    
    ## Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
    ##   the anchor point marker   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return PointMarker
    @property
    def PointMarker(self) -> PointMarker:
        """
        Getter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
          the anchor point marker   
            
         
        """
        pass
    
    ## Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker

    ##   the anchor point marker   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PointMarker.setter
    def PointMarker(self, pointMarker: PointMarker):
        """
        Setter for property: (@link PointMarker NXOpen.CAE.Xyplot.PointMarker@endlink) PointMarker
          the anchor point marker   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents a data accessor to retrieve data of a legend.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class LegendAccessor(NXOpen.TransientObject): 
    """ <summary> Represents a data accessor to retrieve data of a legend. </summary> """


    ## Getter for property: (str) FreeText
    ##   the free text.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def FreeText(self) -> str:
        """
        Getter for property: (str) FreeText
          the free text.  
             
         
        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(legendAccessor: LegendAccessor) -> None:
        """
         Destroys the object. 
        """
        pass
    
##  Manages the legend table group styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LegendTableGroupStyle(BaseDisplayStyleSetting): 
    """ Manages the legend table group styles. """


    ## Getter for property: (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink) ActiveLegendTablePosition
    ##   the active legend table position type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LegendTablePositionType
    @property
    def ActiveLegendTablePosition(self) -> LegendTablePositionType:
        """
        Getter for property: (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink) ActiveLegendTablePosition
          the active legend table position type   
            
         
        """
        pass
    
    ## Setter for property: (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink) ActiveLegendTablePosition

    ##   the active legend table position type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ActiveLegendTablePosition.setter
    def ActiveLegendTablePosition(self, activeLegendTablePositionType: LegendTablePositionType):
        """
        Setter for property: (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink) ActiveLegendTablePosition
          the active legend table position type   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  Gets legend table style by type. 
    ##  @return legendTableStyle (@link LegendTableStyle NXOpen.CAE.Xyplot.LegendTableStyle@endlink):  Legend Table style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="legendTablePositionType"> (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink) </param>
    def GetLegendTableStyle(legendTableGroupStyle: LegendTableGroupStyle, legendTablePositionType: LegendTablePositionType) -> LegendTableStyle:
        """
         Gets legend table style by type. 
         @return legendTableStyle (@link LegendTableStyle NXOpen.CAE.Xyplot.LegendTableStyle@endlink):  Legend Table style .
        """
        pass
    
##  Represents the legend table position type 
## The position of legend table can be dragged 
class LegendTablePositionType(Enum):
    """
    Members Include: <Floating> <Docked>
    """
    Floating: int
    Docked: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LegendTablePositionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Manages the legend table styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LegendTableStyle(BaseDisplayStyleSetting): 
    """ Manages the legend table styles. """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
    ##   the legend table header background color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def BackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
          the legend table header background color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor

    ##   the legend table header background color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @BackgroundColor.setter
    def BackgroundColor(self, backgroundColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
          the legend table header background color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) GridBackgroundColor
    ##   the grid background color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def GridBackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) GridBackgroundColor
          the grid background color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) GridBackgroundColor

    ##   the grid background color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @GridBackgroundColor.setter
    def GridBackgroundColor(self, gridBackgroundColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) GridBackgroundColor
          the grid background color   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsBorderLineVisible
    ##   the border line visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsBorderLineVisible(self) -> bool:
        """
        Getter for property: (bool) IsBorderLineVisible
          the border line visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsBorderLineVisible

    ##   the border line visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsBorderLineVisible.setter
    def IsBorderLineVisible(self, isBorderLineVisible: bool):
        """
        Setter for property: (bool) IsBorderLineVisible
          the border line visibility   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsGridBackgroundFilled
    ##   the value of controlling whether the grid background is filled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsGridBackgroundFilled(self) -> bool:
        """
        Getter for property: (bool) IsGridBackgroundFilled
          the value of controlling whether the grid background is filled   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsGridBackgroundFilled

    ##   the value of controlling whether the grid background is filled   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsGridBackgroundFilled.setter
    def IsGridBackgroundFilled(self, isGridBackgroundFilled: bool):
        """
        Setter for property: (bool) IsGridBackgroundFilled
          the value of controlling whether the grid background is filled   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsGridLineVisible
    ##   the grid line visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsGridLineVisible(self) -> bool:
        """
        Getter for property: (bool) IsGridLineVisible
          the grid line visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsGridLineVisible

    ##   the grid line visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsGridLineVisible.setter
    def IsGridLineVisible(self, isGridLineVisible: bool):
        """
        Setter for property: (bool) IsGridLineVisible
          the grid line visibility   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsHeaderVisible
    ##   the legend table header visibility  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsHeaderVisible(self) -> bool:
        """
        Getter for property: (bool) IsHeaderVisible
          the legend table header visibility  
            
         
        """
        pass
    
    ## Setter for property: (bool) IsHeaderVisible

    ##   the legend table header visibility  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsHeaderVisible.setter
    def IsHeaderVisible(self, isHeaderVisible: bool):
        """
        Setter for property: (bool) IsHeaderVisible
          the legend table header visibility  
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumLegendItemCount
    ##   the maximum displayable functions count on legend table page   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def MaximumLegendItemCount(self) -> int:
        """
        Getter for property: (int) MaximumLegendItemCount
          the maximum displayable functions count on legend table page   
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumLegendItemCount

    ##   the maximum displayable functions count on legend table page   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumLegendItemCount.setter
    def MaximumLegendItemCount(self, maxLegendItemCount: int):
        """
        Setter for property: (int) MaximumLegendItemCount
          the maximum displayable functions count on legend table page   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ##  Gets the border line style. 
    ##  @return borderLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):  Border Line style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBorderLineStyle(legendTableStyle: LegendTableStyle) -> CurveDisplaySettings:
        """
         Gets the border line style. 
         @return borderLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):  Border Line style .
        """
        pass
    
    ## Gets the legend table column titles 
    ##  @return columnTitles (List[str]):  column titles.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetColumnTitles(legendTableStyle: LegendTableStyle) -> List[str]:
        """
        Gets the legend table column titles 
         @return columnTitles (List[str]):  column titles.
        """
        pass
    
    ##  Gets the grid line style. 
    ##  @return gridLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):  Grid Line style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGridLineStyle(legendTableStyle: LegendTableStyle) -> CurveDisplaySettings:
        """
         Gets the grid line style. 
         @return gridLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):  Grid Line style .
        """
        pass
    
    ##  Gets the legend table style type 
    ##  @return legendTableStyleType (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPositionType(legendTableStyle: LegendTableStyle) -> LegendTablePositionType:
        """
         Gets the legend table style type 
         @return legendTableStyleType (@link LegendTablePositionType NXOpen.CAE.Xyplot.LegendTablePositionType@endlink): .
        """
        pass
    
    ##  Gets the text style. 
    ##  @return textStyle (@link LegendTableTextStyle NXOpen.CAE.Xyplot.LegendTableTextStyle@endlink):  Text display style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTextStyle(legendTableStyle: LegendTableStyle) -> LegendTableTextStyle:
        """
         Gets the text style. 
         @return textStyle (@link LegendTableTextStyle NXOpen.CAE.Xyplot.LegendTableTextStyle@endlink):  Text display style .
        """
        pass
    
    ## Sets the legend table column titles 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  column titles
    def SetColumnTitles(legendTableStyle: LegendTableStyle, columnTitles: List[str]) -> None:
        """
        Sets the legend table column titles 
        """
        pass
    
##  Manages the legend table text styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LegendTableTextStyle(TextStyleSetting): 
    """ Manages the legend table text styles. """


    ##  Gets the margin value of legend table 
    ##  @return marginValue (float):   .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## margin option
    def GetMargin(pThis: LegendTableTextStyle, marginOption: TextBoxMarginOption) -> float:
        """
         Gets the margin value of legend table 
         @return marginValue (float):   .
        """
        pass
    
    ## Sets the margin value of legend table 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## margin option
    def SetMargin(pThis: LegendTableTextStyle, marginOption: TextBoxMarginOption, marginValue: float) -> None:
        """
        Sets the margin value of legend table 
        """
        pass
    
##  Manages the legend table.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class LegendTable(BaseModel): 
    """ Manages the legend table. """


    ## Getter for property: (@link LegendTableStyle NXOpen.CAE.Xyplot.LegendTableStyle@endlink) LegendTableStyle
    ##   the legend table style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LegendTableStyle
    @property
    def LegendTableStyle(self) -> LegendTableStyle:
        """
        Getter for property: (@link LegendTableStyle NXOpen.CAE.Xyplot.LegendTableStyle@endlink) LegendTableStyle
          the legend table style   
            
         
        """
        pass
    
    ## Gets the free text of legend table item 
    ##  @return freeText (str):   .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## the index of record index
    def GetFreeTextOfLegendItem(pThis: LegendTable, dataIndex: int) -> str:
        """
        Gets the free text of legend table item 
         @return freeText (str):   .
        """
        pass
    
    ## Resets the free text of legend table item 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## the index of record index
    def ResetFreeTextOfLegendItem(pThis: LegendTable, dataIndex: int) -> None:
        """
        Resets the free text of legend table item 
        """
        pass
    
    ## Sets the free text of legend table item 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## the index of record index
    def SetFreeTextOfLegendItem(pThis: LegendTable, dataIndex: int, freeText: str) -> None:
        """
        Sets the free text of legend table item 
        """
        pass
    
##  Represents the axis limits type 
##  Type to use source data limits as axis limits 
class LimitsType(Enum):
    """
    Members Include: <FreeLimits> <OptimizedLimits> <FixedLimits>
    """
    FreeLimits: int
    OptimizedLimits: int
    FixedLimits: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> LimitsType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the 2d line display style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class LineStyle2DSetting(BaseLineStyleSetting): 
    """ Represents the 2d line display style. """
    pass


##  Represents the 3d line display style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class LineStyle3DSetting(BaseLineStyleSetting): 
    """ Represents the 3d line display style. """


    ## Getter for property: (@link Direction NXOpen.CAE.Xyplot.Direction@endlink) Direction
    ##   the line direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Direction
    @property
    def Direction(self) -> Direction:
        """
        Getter for property: (@link Direction NXOpen.CAE.Xyplot.Direction@endlink) Direction
          the line direction   
            
         
        """
        pass
    
    ## Setter for property: (@link Direction NXOpen.CAE.Xyplot.Direction@endlink) Direction

    ##   the line direction   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: Direction):
        """
        Setter for property: (@link Direction NXOpen.CAE.Xyplot.Direction@endlink) Direction
          the line direction   
            
         
        """
        pass
    
##  Represents a marker object on a plotting graph.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class MarkerModel(BasicModel): 
    """ Represents a marker object on a plotting graph. """


    ## Getter for property: (int) PointIndex
    ##   the point index of marker model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def PointIndex(self) -> int:
        """
        Getter for property: (int) PointIndex
          the point index of marker model.  
             
         
        """
        pass
    
    ## Getter for property: (int) RecordIndex
    ##   the record index of marker model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def RecordIndex(self) -> int:
        """
        Getter for property: (int) RecordIndex
          the record index of marker model.  
             
         
        """
        pass
    
    ##  Deletes the marker model 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Delete(markerModel: MarkerModel) -> None:
        """
         Deletes the marker model 
        """
        pass
    
##  Represents the marker display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MarkerStyleSetting(TextStyleSetting): 
    """ Represents the marker display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (float) AbsPercentage
    ##   the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
    ##   0, 1.0]   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def AbsPercentage(self) -> float:
        """
        Getter for property: (float) AbsPercentage
          the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
          0, 1.0]   
         
        """
        pass
    
    ## Setter for property: (float) AbsPercentage

    ##   the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
    ##   0, 1.0]   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AbsPercentage.setter
    def AbsPercentage(self, absPercentage: float):
        """
        Setter for property: (float) AbsPercentage
          the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
          0, 1.0]   
         
        """
        pass
    
    ## Getter for property: (@link AnchorType NXOpen.CAE.Xyplot.AnchorType@endlink) AttachmentType
    ##   the attachment type for associative marker   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return AnchorType
    @property
    def AttachmentType(self) -> AnchorType:
        """
        Getter for property: (@link AnchorType NXOpen.CAE.Xyplot.AnchorType@endlink) AttachmentType
          the attachment type for associative marker   
            
         
        """
        pass
    
    ## Setter for property: (@link AnchorType NXOpen.CAE.Xyplot.AnchorType@endlink) AttachmentType

    ##   the attachment type for associative marker   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AttachmentType.setter
    def AttachmentType(self, anchorType: AnchorType):
        """
        Setter for property: (@link AnchorType NXOpen.CAE.Xyplot.AnchorType@endlink) AttachmentType
          the attachment type for associative marker   
            
         
        """
        pass
    
    ## Getter for property: (bool) DataLabelVisibility
    ##  the option specifies whether to show point label text  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def DataLabelVisibility(self) -> bool:
        """
        Getter for property: (bool) DataLabelVisibility
         the option specifies whether to show point label text  
            
         
        """
        pass
    
    ## Setter for property: (bool) DataLabelVisibility

    ##  the option specifies whether to show point label text  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DataLabelVisibility.setter
    def DataLabelVisibility(self, isShowLabel: bool):
        """
        Setter for property: (bool) DataLabelVisibility
         the option specifies whether to show point label text  
            
         
        """
        pass
    
    ## Getter for property: (bool) NoteTextVisibility
    ##   the option specifies whether to show note text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def NoteTextVisibility(self) -> bool:
        """
        Getter for property: (bool) NoteTextVisibility
          the option specifies whether to show note text   
            
         
        """
        pass
    
    ## Setter for property: (bool) NoteTextVisibility

    ##   the option specifies whether to show note text   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NoteTextVisibility.setter
    def NoteTextVisibility(self, isNoteTextVisible: bool):
        """
        Setter for property: (bool) NoteTextVisibility
          the option specifies whether to show note text   
            
         
        """
        pass
    
    ## Getter for property: (bool) NumberTextVisibility
    ##   the option specifies whether to show number text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def NumberTextVisibility(self) -> bool:
        """
        Getter for property: (bool) NumberTextVisibility
          the option specifies whether to show number text   
            
         
        """
        pass
    
    ## Setter for property: (bool) NumberTextVisibility

    ##   the option specifies whether to show number text   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NumberTextVisibility.setter
    def NumberTextVisibility(self, isNumberTextVisible: bool):
        """
        Setter for property: (bool) NumberTextVisibility
          the option specifies whether to show number text   
            
         
        """
        pass
    
    ## Getter for property: (bool) SnapToData
    ##   the option specifies whether just to search source data when creating associative marker   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def SnapToData(self) -> bool:
        """
        Getter for property: (bool) SnapToData
          the option specifies whether just to search source data when creating associative marker   
            
         
        """
        pass
    
    ## Setter for property: (bool) SnapToData

    ##   the option specifies whether just to search source data when creating associative marker   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SnapToData.setter
    def SnapToData(self, isSnapToData: bool):
        """
        Setter for property: (bool) SnapToData
          the option specifies whether just to search source data when creating associative marker   
            
         
        """
        pass
    
    ##  Gets the note texts 
    ##  @return noteTexts (List[str]):  Note Texts .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNoteTexts(pThis: MarkerStyleSetting) -> List[str]:
        """
         Gets the note texts 
         @return noteTexts (List[str]):  Note Texts .
        """
        pass
    
    ##  Sets the note texts 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Note Texts 
    def SetNoteTexts(pThis: MarkerStyleSetting, noteTexts: List[str]) -> None:
        """
         Sets the note texts 
        """
        pass
    
##   @brief  RRepresents a data accessor to retrieve data of a function which is plotted in Matrix graphs.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class MatrixFunctionDataAccessor(IFunctionDataAccessor): 
    """ <summary> RRepresents a data accessor to retrieve data of a function which is plotted in Matrix graphs. </summary> """


    ##  Asks display data. 
    ##  @return dependentValues (List[float]): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskDisplayData(matrixFunctionDataAccessor: MatrixFunctionDataAccessor) -> List[float]:
        """
         Asks display data. 
         @return dependentValues (List[float]): .
        """
        pass
    
    ##  Asks point labels. 
    ##  @return A tuple consisting of (rowLabels, columnLabels). 
    ##  - rowLabels is: List[str].
    ##  - columnLabels is: List[str].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskPointLabels(matrixFunctionDataAccessor: MatrixFunctionDataAccessor) -> Tuple[List[str], List[str]]:
        """
         Asks point labels. 
         @return A tuple consisting of (rowLabels, columnLabels). 
         - rowLabels is: List[str].
         - columnLabels is: List[str].

        """
        pass
    
##  Manages the display matrix graph 2d.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MatrixGraph2D(Graph): 
    """ Manages the display matrix graph 2d. """
    pass


##  Represents the layout mode for matrix plot 2D 
##  Fill each cell as square 
class MatrixPlot2DLayoutMode(Enum):
    """
    Members Include: <FillEachCellAsSquare> <FillAllAvailableDisplayArea>
    """
    FillEachCellAsSquare: int
    FillAllAvailableDisplayArea: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> MatrixPlot2DLayoutMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##   @brief 
##         Manages the display of matrix plot 2d. 
## 
##  
##         
##         Call @link CAE::Xyplot::I2DDataPlot::EditRecord CAE::Xyplot::I2DDataPlot::EditRecord@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class MatrixPlot2D(Plot): 
    """ <summary>
        Manages the display of matrix plot 2d.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I2DDataPlot.EditRecord</ja_method> to edit data for this class.
        </remarks> """


    ##  Get all available value text types of matrix plot
    ##  @return valueTypes (List[str]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAllValueTypes(matrixPlot2D: MatrixPlot2D) -> List[str]:
        """
         Get all available value text types of matrix plot
         @return valueTypes (List[str]): .
        """
        pass
    
##  Represents the value text style displayed in matrix plot. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class MatrixValueTextStyle(TextStyleSetting): 
    """ Represents the value text style displayed in matrix plot. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (str) ValueType
    ##   the value type.  
    ##    If it is null, no value text will be displayed  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def ValueType(self) -> str:
        """
        Getter for property: (str) ValueType
          the value type.  
           If it is null, no value text will be displayed  
         
        """
        pass
    
    ## Setter for property: (str) ValueType

    ##   the value type.  
    ##    If it is null, no value text will be displayed  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ValueType.setter
    def ValueType(self, valueType: str):
        """
        Setter for property: (str) ValueType
          the value type.  
           If it is null, no value text will be displayed  
         
        """
        pass
    
##  Represents the model type 
##   
class ModelType(Enum):
    """
    Members Include: <Plot> <Graph> <RecordDisplay> <Marker> <Note> <Title> <GraphName> <FunctionName> <XAxis> <XAxisLabel> <XAxisNumber> <YAxis> <YAxisLabel> <YAxisNumber> <ZAxis> <ZAxisLabel> <ZAxisNumber> <ColorAxis> <ColorAxisLabel> <ColorAxisNumber> <AngleAxis> <AngleAxisNumber> <UnknownResult> <PageNumber> <Legend> <LegendTable> <ResultLegend> <FormulaGrid> <FormulaGridValueText> <CalculationLegendTable>
    """
    Plot: int
    Graph: int
    RecordDisplay: int
    Marker: int
    Note: int
    Title: int
    GraphName: int
    FunctionName: int
    XAxis: int
    XAxisLabel: int
    XAxisNumber: int
    YAxis: int
    YAxisLabel: int
    YAxisNumber: int
    ZAxis: int
    ZAxisLabel: int
    ZAxisNumber: int
    ColorAxis: int
    ColorAxisLabel: int
    ColorAxisNumber: int
    AngleAxis: int
    AngleAxisNumber: int
    UnknownResult: int
    PageNumber: int
    Legend: int
    LegendTable: int
    ResultLegend: int
    FormulaGrid: int
    FormulaGridValueText: int
    CalculationLegendTable: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ModelType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a note object on a plot.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class NoteModel(BasicModel): 
    """ Represents a note object on a plot. """


    ##  Deletes the note model 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Delete(noteModel: NoteModel) -> None:
        """
         Deletes the note model 
        """
        pass
    
    ##  Gets the display position of note content. 
    ##  @return position (@link NXOpen.Point2d NXOpen.Point2d@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTextPosition(noteModel: NoteModel) -> NXOpen.Point2d:
        """
         Gets the display position of note content. 
         @return position (@link NXOpen.Point2d NXOpen.Point2d@endlink):   .
        """
        pass
    
    ##  Gets the note content. 
    ##  @return lines (List[str]): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTexts(noteModel: NoteModel) -> List[str]:
        """
         Gets the note content. 
         @return lines (List[str]): .
        """
        pass
    
    ##  Sets the display position of note content with test box corner type. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textBoxConerType"> (@link TextBoxCornerType NXOpen.CAE.Xyplot.TextBoxCornerType@endlink) </param>
    ## <param name="position"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def SetTextPositionWithBoxCorner(noteModel: NoteModel, textBoxConerType: TextBoxCornerType, position: NXOpen.Point2d) -> None:
        """
         Sets the display position of note content with test box corner type. 
        """
        pass
    
    ##  Sets the note content. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="content"> (List[str]) </param>
    def SetTexts(noteModel: NoteModel, content: List[str]) -> None:
        """
         Sets the note content. 
        """
        pass
    
##  Represents the note display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class NoteStyleSetting(TextStyleSetting): 
    """ Represents the note display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ##  Gets the note texts 
    ##  @return noteTexts (List[str]):  Note Texts .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNoteTexts(pThis: NoteStyleSetting) -> List[str]:
        """
         Gets the note texts 
         @return noteTexts (List[str]):  Note Texts .
        """
        pass
    
    ##  Sets the note texts 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Note Texts 
    def SetNoteTexts(pThis: NoteStyleSetting, noteTexts: List[str]) -> None:
        """
         Sets the note texts 
        """
        pass
    
##  Represents an marker which display order value on a @link CAE::Xyplot::PlotTypePlotCampbell CAE::Xyplot::PlotTypePlotCampbell@endlink  plot .  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class OrderMarkerModel(BasicModel): 
    """ Represents an marker which display order value on a <ja_enum_member>CAE.Xyplot.PlotType.PlotCampbell</ja_enum_member> plot . """


    ##  Returns the order value. 
    ##  @return orderValue (float): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOrderValue(orderMarkerModel: OrderMarkerModel) -> float:
        """
         Returns the order value. 
         @return orderValue (float): .
        """
        pass
    
import NXOpen
##   @brief  Represents a data accessor to retrieve the result of overall level.  
## 
##  
##             
##             The overall level function supports frequency domain and time domain. To provide a given data range
##             to calculate in signal power algorithm.
##             
##         
## 
##   <br>  Created in NX1899.0.0  <br> 

class OverallLevelAccessor(NXOpen.TransientObject): 
    """ <summary> Represents a data accessor to retrieve the result of overall level. </summary>
            <remarks>
            The overall level function supports frequency domain and time domain. To provide a given data range
            to calculate in signal power algorithm.
            </remarks>
        """


    ##  Asks the overall level result. 
    ##  @return A tuple consisting of (hasNumberValue, resultValue). 
    ##  - hasNumberValue is: bool.
    ##  - resultValue is: float.

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskOverallLevelResult(overallLevelAccessor: OverallLevelAccessor) -> Tuple[bool, float]:
        """
         Asks the overall level result. 
         @return A tuple consisting of (hasNumberValue, resultValue). 
         - hasNumberValue is: bool.
         - resultValue is: float.

        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(overallLevelAccessor: OverallLevelAccessor) -> None:
        """
         Destroys the object. 
        """
        pass
    
##  Represents an overall marker object that shows a calculation result for overall operation on a plotting graph.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class OverallMarkerModel(BasicModel): 
    """ Represents an overall marker object that shows a calculation result for overall operation on a plotting graph. """


    ##  Returns the calculation result. 
    ##  @return calculationResult (float): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResult(overallMarkerModel: OverallMarkerModel) -> float:
        """
         Returns the calculation result. 
         @return calculationResult (float): .
        """
        pass
    
##  Represents the parameters passed to overlay plot records on an existing plot graph.  <br> To create a new instance of this class, use @link NXOpen::CAE::Xyplot::XYPlotManager::NewOverlayParameters  NXOpen::CAE::Xyplot::XYPlotManager::NewOverlayParameters @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class OverlayParameters(BasePlotParameters): 
    """ Represents the parameters passed to overlay plot records on an existing plot graph. """


    ## Getter for property: (int) SubGraphInStack
    ##   the index of subgraph on a stacked plot, on which the records will be
    ##                 overlaied.  
    ##    The property is only available when overlaying records on
    ##                 a stacked plot. The index value is between 0 and the property value of
    ##                 @link CAE::Xyplot::Plot::SubGraphCountInStack  CAE::Xyplot::Plot::SubGraphCountInStack @endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def SubGraphInStack(self) -> int:
        """
        Getter for property: (int) SubGraphInStack
          the index of subgraph on a stacked plot, on which the records will be
                        overlaied.  
           The property is only available when overlaying records on
                        a stacked plot. The index value is between 0 and the property value of
                        @link CAE::Xyplot::Plot::SubGraphCountInStack  CAE::Xyplot::Plot::SubGraphCountInStack @endlink .   
         
        """
        pass
    
    ## Setter for property: (int) SubGraphInStack

    ##   the index of subgraph on a stacked plot, on which the records will be
    ##                 overlaied.  
    ##    The property is only available when overlaying records on
    ##                 a stacked plot. The index value is between 0 and the property value of
    ##                 @link CAE::Xyplot::Plot::SubGraphCountInStack  CAE::Xyplot::Plot::SubGraphCountInStack @endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @SubGraphInStack.setter
    def SubGraphInStack(self, subGraphIndex: int):
        """
        Setter for property: (int) SubGraphInStack
          the index of subgraph on a stacked plot, on which the records will be
                        overlaied.  
           The property is only available when overlaying records on
                        a stacked plot. The index value is between 0 and the property value of
                        @link CAE::Xyplot::Plot::SubGraphCountInStack  CAE::Xyplot::Plot::SubGraphCountInStack @endlink .   
         
        """
        pass
    
##  Prepresents the phase range option 
##  Displays phase between -360 and 0 
class PhaseRangeOption(Enum):
    """
    Members Include: <NegativeTwoPiToZero> <ZeroToTwoPi> <NegativePiToPi> <NegativeOneHalfPiToHalfPi> <NegativeHalfPiToOneHalfPi>
    """
    NegativeTwoPiToZero: int
    ZeroToTwoPi: int
    NegativePiToPi: int
    NegativeOneHalfPiToHalfPi: int
    NegativeHalfPiToOneHalfPi: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PhaseRangeOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the plate filling color option 
##  Fill color with no shading 
class PlateColorOption(Enum):
    """
    Members Include: <Fill> <Hidden> <Shaded>
    """
    Fill: int
    Hidden: int
    Shaded: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PlateColorOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##   @brief  Manages the display of 2D plot. 
## 
##  
##         
##         Call @link CAE::Xyplot::I2DDataPlot::EditRecord CAE::Xyplot::I2DDataPlot::EditRecord@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Plot2D(Plot): 
    """ <summary> Manages the display of 2D plot.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I2DDataPlot.EditRecord</ja_method> to edit data for this class.
        </remarks> """
    pass


##   @brief  Manages the display of 3D plot. 
## 
##  
##         
##          Call @link CAE::Xyplot::I3DDataPlot::EditRecords CAE::Xyplot::I3DDataPlot::EditRecords@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Plot3D(Plot): 
    """ <summary> Manages the display of 3D plot.</summary>
        <remarks>
         Call <ja_method>CAE.Xyplot.I3DDataPlot.EditRecords</ja_method> to edit data for this class.
        </remarks> """
    pass


##  Manages the plot graph template.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PlotGraphTemplate(BaseDisplayStyleSetting): 
    """ Manages the plot graph template. """


    ## Getter for property: (str) AbscissaCustomMarkerLabel
    ##   the abscissa custom marker label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def AbscissaCustomMarkerLabel(self) -> str:
        """
        Getter for property: (str) AbscissaCustomMarkerLabel
          the abscissa custom marker label   
            
         
        """
        pass
    
    ## Setter for property: (str) AbscissaCustomMarkerLabel

    ##   the abscissa custom marker label   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @AbscissaCustomMarkerLabel.setter
    def AbscissaCustomMarkerLabel(self, xCustomMarkerLabel: str):
        """
        Setter for property: (str) AbscissaCustomMarkerLabel
          the abscissa custom marker label   
            
         
        """
        pass
    
    ## Getter for property: (@link DiagramDisplayStyles NXOpen.CAE.Xyplot.DiagramDisplayStyles@endlink) DiagramDisplayStyles
    ##   the diagram display styles.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return DiagramDisplayStyles
    @property
    def DiagramDisplayStyles(self) -> DiagramDisplayStyles:
        """
        Getter for property: (@link DiagramDisplayStyles NXOpen.CAE.Xyplot.DiagramDisplayStyles@endlink) DiagramDisplayStyles
          the diagram display styles.  
             
         
        """
        pass
    
    ## Getter for property: (@link GeneralDisplayStyles NXOpen.CAE.Xyplot.GeneralDisplayStyles@endlink) GeneralDisplayStyles
    ##   the general display styles.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return GeneralDisplayStyles
    @property
    def GeneralDisplayStyles(self) -> GeneralDisplayStyles:
        """
        Getter for property: (@link GeneralDisplayStyles NXOpen.CAE.Xyplot.GeneralDisplayStyles@endlink) GeneralDisplayStyles
          the general display styles.  
             
         
        """
        pass
    
    ## Getter for property: (str) OrdinateCustomMarkerLabel
    ##   the ordinate custom marker label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def OrdinateCustomMarkerLabel(self) -> str:
        """
        Getter for property: (str) OrdinateCustomMarkerLabel
          the ordinate custom marker label   
            
         
        """
        pass
    
    ## Setter for property: (str) OrdinateCustomMarkerLabel

    ##   the ordinate custom marker label   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @OrdinateCustomMarkerLabel.setter
    def OrdinateCustomMarkerLabel(self, yCustomMarkerLabel: str):
        """
        Setter for property: (str) OrdinateCustomMarkerLabel
          the ordinate custom marker label   
            
         
        """
        pass
    
    ## Getter for property: (@link WallDisplayStyles NXOpen.CAE.Xyplot.WallDisplayStyles@endlink) WallDisplayStyles
    ##   the wall display styles.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return WallDisplayStyles
    @property
    def WallDisplayStyles(self) -> WallDisplayStyles:
        """
        Getter for property: (@link WallDisplayStyles NXOpen.CAE.Xyplot.WallDisplayStyles@endlink) WallDisplayStyles
          the wall display styles.  
             
         
        """
        pass
    
    ## Getter for property: (str) ZCustomMarkerLabel
    ##   the z custom marker label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def ZCustomMarkerLabel(self) -> str:
        """
        Getter for property: (str) ZCustomMarkerLabel
          the z custom marker label   
            
         
        """
        pass
    
    ## Setter for property: (str) ZCustomMarkerLabel

    ##   the z custom marker label   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ZCustomMarkerLabel.setter
    def ZCustomMarkerLabel(self, zCustomMarkerLabel: str):
        """
        Setter for property: (str) ZCustomMarkerLabel
          the z custom marker label   
            
         
        """
        pass
    
    ##  Exports current graph template setting to a template xml file,
    ##                 it will override the template file if it is existing. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Template xml file name 
    def ExportTemplate(graphTemplate: PlotGraphTemplate, strXmlFile: str) -> None:
        """
         Exports current graph template setting to a template xml file,
                        it will override the template file if it is existing. 
        """
        pass
    
    ##  Updates current graph template setting from a template xml file 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Template xml file name 
    def ImportTemplate(graphTemplate: PlotGraphTemplate, strXmlFile: str) -> None:
        """
         Updates current graph template setting from a template xml file 
        """
        pass
    
    ##  Resets the graph template to default values 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ResetToDefault(graphTemplate: PlotGraphTemplate) -> None:
        """
         Resets the graph template to default values 
        """
        pass
    
##  Represents the parameters passed to create a plot.  <br> To create a new instance of this class, use @link NXOpen::CAE::Xyplot::XYPlotManager::NewPlotParameters  NXOpen::CAE::Xyplot::XYPlotManager::NewPlotParameters @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class PlotParameters(BasePlotParameters): 
    """ Represents the parameters passed to create a plot. """


    ## Getter for property: (int) ComplexOption
    ##   the complex options,if complex option is smaller than zero, it will use default complex option from active template file    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def ComplexOption(self) -> int:
        """
        Getter for property: (int) ComplexOption
          the complex options,if complex option is smaller than zero, it will use default complex option from active template file    
            
         
        """
        pass
    
    ## Setter for property: (int) ComplexOption

    ##   the complex options,if complex option is smaller than zero, it will use default complex option from active template file    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ComplexOption.setter
    def ComplexOption(self, complexOption: int):
        """
        Setter for property: (int) ComplexOption
          the complex options,if complex option is smaller than zero, it will use default complex option from active template file    
            
         
        """
        pass
    
    ## Getter for property: (bool) IsToCreateStandalonePlot
    ##   the create standalone plot    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def IsToCreateStandalonePlot(self) -> bool:
        """
        Getter for property: (bool) IsToCreateStandalonePlot
          the create standalone plot    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsToCreateStandalonePlot

    ##   the create standalone plot    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @IsToCreateStandalonePlot.setter
    def IsToCreateStandalonePlot(self, isToCreateStandalonePlot: bool):
        """
        Setter for property: (bool) IsToCreateStandalonePlot
          the create standalone plot    
            
         
        """
        pass
    
    ## Getter for property: (@link PlotGraphTemplate NXOpen.CAE.Xyplot.PlotGraphTemplate@endlink) PlotTemplate
    ##   the plot template to be used by the plot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PlotGraphTemplate
    @property
    def PlotTemplate(self) -> PlotGraphTemplate:
        """
        Getter for property: (@link PlotGraphTemplate NXOpen.CAE.Xyplot.PlotGraphTemplate@endlink) PlotTemplate
          the plot template to be used by the plot   
            
         
        """
        pass
    
    ## Getter for property: (@link PlotType NXOpen.CAE.Xyplot.PlotType@endlink) PlotType
    ##   the plot type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PlotType
    @property
    def PlotType(self) -> PlotType:
        """
        Getter for property: (@link PlotType NXOpen.CAE.Xyplot.PlotType@endlink) PlotType
          the plot type   
            
         
        """
        pass
    
    ## Setter for property: (@link PlotType NXOpen.CAE.Xyplot.PlotType@endlink) PlotType

    ##   the plot type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @PlotType.setter
    def PlotType(self, plotType: PlotType):
        """
        Setter for property: (@link PlotType NXOpen.CAE.Xyplot.PlotType@endlink) PlotType
          the plot type   
            
         
        """
        pass
    
##  Represents the plot type 
##  unknown plot type 
class PlotType(Enum):
    """
    Members Include: <Unknown> <Plot2D> <Plot2DInStack> <Plot3D> <PlotColorBar> <PlotColorMap> <PlotBarChart> <PlotMatrix2D> <PlotCampbell>
    """
    Unknown: int
    Plot2D: int
    Plot2DInStack: int
    Plot3D: int
    PlotColorBar: int
    PlotColorMap: int
    PlotBarChart: int
    PlotMatrix2D: int
    PlotCampbell: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PlotType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE.FTK
##  Manages the plot template  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class Plot(BaseModel): 
    """ Manages the plot template """


    ## Getter for property: (@link PlotGraphTemplate NXOpen.CAE.Xyplot.PlotGraphTemplate@endlink) PlotTemplate
    ##   the plot template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PlotGraphTemplate
    @property
    def PlotTemplate(self) -> PlotGraphTemplate:
        """
        Getter for property: (@link PlotGraphTemplate NXOpen.CAE.Xyplot.PlotGraphTemplate@endlink) PlotTemplate
          the plot template   
            
         
        """
        pass
    
    ## Getter for property: (int) SubGraphCountInStack
    ##   the sub-graph count in a stacked plot.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def SubGraphCountInStack(self) -> int:
        """
        Getter for property: (int) SubGraphCountInStack
          the sub-graph count in a stacked plot.  
             
         
        """
        pass
    
    ##   @brief  Accepts record changed and process data to update data model 
    ## 
    ##  
    ##                  This method is only to update data model, it needs call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to update display to reflect data change.
    ##                 
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def CommitRecordsChange(plot: Plot) -> None:
        """
          @brief  Accepts record changed and process data to update data model 
        
         
                         This method is only to update data model, it needs call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to update display to reflect data change.
                        
                    
        """
        pass
    
    ##  Creates a note with the position of text box corner on the plot. 
    ##  @return noteModel (@link NoteModel NXOpen.CAE.Xyplot.NoteModel@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="textBoxConerType"> (@link TextBoxCornerType NXOpen.CAE.Xyplot.TextBoxCornerType@endlink) </param>
    ## <param name="lines"> (List[str]) </param>
    ## <param name="boxCornerPosition"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def CreateNoteWithTextBoxCorner(plot: Plot, textBoxConerType: TextBoxCornerType, lines: List[str], boxCornerPosition: NXOpen.Point2d) -> NoteModel:
        """
         Creates a note with the position of text box corner on the plot. 
         @return noteModel (@link NoteModel NXOpen.CAE.Xyplot.NoteModel@endlink): .
        """
        pass
    
    ##   @brief  Deletes all records. 
    ## 
    ##  
    ##             
    ##             Higher performance to delete all records from plot than deleting records one by one
    ##              <br> 
    ##             <b> Procedure of deleting records from plot fully:</b>
    ##             <ol>
    ##             <li>Call this method to delete all record data from plot</li>
    ##             <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
    ##             <li>Call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
    ##             <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
    ##             </ol>
    ##              <br> 
    ##             
    ##             
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeleteAllRecords(plot: Plot) -> None:
        """
          @brief  Deletes all records. 
        
         
                    
                    Higher performance to delete all records from plot than deleting records one by one
                     <br> 
                    <b> Procedure of deleting records from plot fully:</b>
                    <ol>
                    <li>Call this method to delete all record data from plot</li>
                    <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
                    <li>Call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
                    <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
                    </ol>
                     <br> 
                    
                    
        """
        pass
    
    ##   @brief  Deletes the nth record. 
    ## 
    ##  
    ##             
    ##             The record index must be greater or equal to 0, and less than @link CAE::Xyplot::Plot::GetRecordCount CAE::Xyplot::Plot::GetRecordCount@endlink 
    ##              <br> 
    ##             <b> Procedure of deleting records from plot fully:</b>
    ##             <ol>
    ##             <li>Call this method to delete record data from plot</li>
    ##             <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
    ##             <li>Call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
    ##             <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
    ##             </ol>
    ##              <br> 
    ##             
    ##             
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="recordIndex"> (int) </param>
    def DeleteRecord(plot: Plot, recordIndex: int) -> None:
        """
          @brief  Deletes the nth record. 
        
         
                    
                    The record index must be greater or equal to 0, and less than @link CAE::Xyplot::Plot::GetRecordCount CAE::Xyplot::Plot::GetRecordCount@endlink 
                     <br> 
                    <b> Procedure of deleting records from plot fully:</b>
                    <ol>
                    <li>Call this method to delete record data from plot</li>
                    <li>Call @link CAE::Xyplot::Plot::CommitRecordsChange CAE::Xyplot::Plot::CommitRecordsChange@endlink  to precess record data change and update data model</li>
                    <li>Call @link CAE::Xyplot::BaseModel::UpdateDisplay CAE::Xyplot::BaseModel::UpdateDisplay@endlink  to regenerate display to reflect data change</li>
                    <li>Optionally call @link CAE::Xyplot::Plot::FitView CAE::Xyplot::Plot::FitView@endlink  to make display fit the view;it is only required when the plot display boundary is changed</li>
                    </ol>
                     <br> 
                    
                    
        """
        pass
    
    ##   @brief  Fits the display view on a reasonable region. 
    ## 
    ##   
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FitView(plot: Plot) -> None:
        """
          @brief  Fits the display view on a reasonable region. 
        
          
        """
        pass
    
    ##  Returns application specific data associated to a record. 
    ##  @return applicationData (@link NXOpen.CAE.FTK.IApplicationData NXOpen.CAE.FTK.IApplicationData@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  The record index starts form 0 to record count -1. Get record count from @link Plot::GetRecordCount Plot::GetRecordCount@endlink  
    def GetApplicationDataOfRecord(plot: Plot, recordIndex: int) -> NXOpen.CAE.FTK.IApplicationData:
        """
         Returns application specific data associated to a record. 
         @return applicationData (@link NXOpen.CAE.FTK.IApplicationData NXOpen.CAE.FTK.IApplicationData@endlink): .
        """
        pass
    
    ##  Gets calculation legend table models on the plot. 
    ##  @return legendTableModels (@link LegendTable List[NXOpen.CAE.Xyplot.LegendTable]@endlink):  Legend Table Objects .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCalculationLegendTables(plot: Plot) -> List[LegendTable]:
        """
         Gets calculation legend table models on the plot. 
         @return legendTableModels (@link LegendTable List[NXOpen.CAE.Xyplot.LegendTable]@endlink):  Legend Table Objects .
        """
        pass
    
    ##  Gets the window device and view index of the plot graph. 
    ##  @return A tuple consisting of (windowDevice, viewIndex). 
    ##  - windowDevice is: int. the device of window .
    ##  - viewIndex is: int. the index of view .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDeviceAndViewIndex(plot: Plot) -> Tuple[int, int]:
        """
         Gets the window device and view index of the plot graph. 
         @return A tuple consisting of (windowDevice, viewIndex). 
         - windowDevice is: int. the device of window .
         - viewIndex is: int. the index of view .

        """
        pass
    
    ##  Gets all graphs on the plot. 
    ##  @return graphs (@link Graph List[NXOpen.CAE.Xyplot.Graph]@endlink):  Graph objects .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetGraphs(plot: Plot) -> List[Graph]:
        """
         Gets all graphs on the plot. 
         @return graphs (@link Graph List[NXOpen.CAE.Xyplot.Graph]@endlink):  Graph objects .
        """
        pass
    
    ##  Gets the legend table models on the plot. 
    ##  @return legendTableModels (@link LegendTable List[NXOpen.CAE.Xyplot.LegendTable]@endlink):  Legend Table Objects .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLegendTables(plot: Plot) -> List[LegendTable]:
        """
         Gets the legend table models on the plot. 
         @return legendTableModels (@link LegendTable List[NXOpen.CAE.Xyplot.LegendTable]@endlink):  Legend Table Objects .
        """
        pass
    
    ##  Gets the models by model type. 
    ##  @return models (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="type"> (@link ModelType NXOpen.CAE.Xyplot.ModelType@endlink) </param>
    def GetModels(plot: Plot, type: ModelType) -> List[BasicModel]:
        """
         Gets the models by model type. 
         @return models (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
        """
        pass
    
    ##  Gets all notes on the plot 
    ##  @return noteModels (@link NoteModel List[NXOpen.CAE.Xyplot.NoteModel]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNotes(plot: Plot) -> List[NoteModel]:
        """
         Gets all notes on the plot 
         @return noteModels (@link NoteModel List[NXOpen.CAE.Xyplot.NoteModel]@endlink): .
        """
        pass
    
    ##  Gets the post environment settings in the plot. 
    ##  @return postEnvironmentSettings (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPostEnvironmentSettings(plot: Plot) -> NXOpen.TaggedObject:
        """
         Gets the post environment settings in the plot. 
         @return postEnvironmentSettings (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Returns the count of plotted records on the plot graph. 
    ##  @return recordCount (int):  Record count .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRecordCount(plot: Plot) -> int:
        """
         Returns the count of plotted records on the plot graph. 
         @return recordCount (int):  Record count .
        """
        pass
    
    ##  Gets the visibility of specified record. 
    ##  @return visibility (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the index of specied record 
    def GetRecordDisplayVisibility(plot: Plot, recordIndex: int) -> bool:
        """
         Gets the visibility of specified record. 
         @return visibility (bool): .
        """
        pass
    
    ##  Gets the titles on the plot. 
    ##  @return titles (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTitles(plot: Plot) -> List[BasicModel]:
        """
         Gets the titles on the plot. 
         @return titles (@link BasicModel List[NXOpen.CAE.Xyplot.BasicModel]@endlink): .
        """
        pass
    
    ##  Gets the bounding box of the plot view. 
    ##  @return A tuple consisting of (leftBottom, rightTop). 
    ##  - leftBottom is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - rightTop is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetViewBoundingBox(plot: Plot) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the bounding box of the plot view. 
         @return A tuple consisting of (leftBottom, rightTop). 
         - leftBottom is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - rightTop is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
    ##  Saves plotted records on a graph to an afu file.
    ##                The record index is between 0 and the value returned from
    ##                @link NXOpen::CAE::Xyplot::Plot::GetRecordCount NXOpen::CAE::Xyplot::Plot::GetRecordCount@endlink . 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  The index of records to be saved 
    def SaveRecords(plot: Plot, recordIndexes: List[int], recordNames: List[str], outputFileName: str, reportError: bool) -> None:
        """
         Saves plotted records on a graph to an afu file.
                       The record index is between 0 and the value returned from
                       @link NXOpen::CAE::Xyplot::Plot::GetRecordCount NXOpen::CAE::Xyplot::Plot::GetRecordCount@endlink . 
        """
        pass
    
    ##  Saves plotted records on a plot graph to a CSV file. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  the indexes of records to be saved 
    def SaveRecordsToCsv(plot: Plot, recordIndex: List[int], recordNames: List[str], csvFileName: str, isWriteHeader: bool) -> None:
        """
         Saves plotted records on a plot graph to a CSV file. 
        """
        pass
    
    ##  Sets the visibility of specified record. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the index of specied record 
    def SetRecordDisplayVisibility(plot: Plot, recordIndex: int, visibility: bool) -> None:
        """
         Sets the visibility of specified record. 
        """
        pass
    
    ##   @brief Writes the template setting of plot to template file. 
    ## 
    ##  
    ##             
    ##             <ol>
    ##             <li>
    ##             If input file is a simple file: 
    ##              <br> 
    ##             If environment variable of UGII_USER_DIR is not set, it will be written into file under user environment directory. 
    ##              <br> 
    ##              <br> 
    ##             If environment variable of UGII_USER_DIR is not set, it will write to write the template setting.
    ##              <br> 
    ##             </li>
    ##             <li>
    ##             If input file is a file with full path, the template settings will be written into the file.
    ##             </li>
    ##             </ol>
    ##             
    ##             
    ##  @return templateFileFullName (str):  the file name with full path .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  simple name or file name with full path 
    def WriteToTemplateFile(plot: Plot, inputTemplateFile: str) -> str:
        """
          @brief Writes the template setting of plot to template file. 
        
         
                    
                    <ol>
                    <li>
                    If input file is a simple file: 
                     <br> 
                    If environment variable of UGII_USER_DIR is not set, it will be written into file under user environment directory. 
                     <br> 
                     <br> 
                    If environment variable of UGII_USER_DIR is not set, it will write to write the template setting.
                     <br> 
                    </li>
                    <li>
                    If input file is a file with full path, the template settings will be written into the file.
                    </li>
                    </ol>
                    
                    
         @return templateFileFullName (str):  the file name with full path .
        """
        pass
    
##  Represents the point marker 
##  No marker 
class PointMarker(Enum):
    """
    Members Include: <NotSet> <Plus> <Dot> <Asterisk> <Circle> <Poundsign> <Cross> <Square> <Triangle> <Diamond> <CenterLine>
    """
    NotSet: int
    Plus: int
    Dot: int
    Asterisk: int
    Circle: int
    Poundsign: int
    Cross: int
    Square: int
    Triangle: int
    Diamond: int
    CenterLine: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PointMarker:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE.FTK
##  Manages the preference data.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class Preference(NXOpen.TaggedObject): 
    """ Manages the preference data. """


    ##  Defines the action of dropping data on a viewport in graphics window 
    ##  Overlay on existing plot, create new plot on non-plot view 
    class DropActionOption(Enum):
        """
        Members Include: <Auto> <Plot> <PlotOnNewWindow> <PlotOnMultipleNewWindows> <MetaKey>
        """
        Auto: int
        Plot: int
        PlotOnNewWindow: int
        PlotOnMultipleNewWindows: int
        MetaKey: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Preference.DropActionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines whether to always show plot graph on a new separate graphic window 
    ##  Prompts user to show plot graph on either an existing or a new separate graphic window 
    class NewWindowChoice(Enum):
        """
        Members Include: <Prompt> <Always>
        """
        Prompt: int
        Always: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Preference.NewWindowChoice:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines the target graphic window type 
    ##  Only shows plot graph on main graphic window 
    class TargetGraphicWindowOption(Enum):
        """
        Members Include: <Main> <Separate> <Both>
        """
        Main: int
        Separate: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Preference.TargetGraphicWindowOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.CAE.FTK.DataManager.AfuRecordZValue NXOpen.CAE.FTK.DataManager.AfuRecordZValue@endlink) AfuRecordZValue
    ##   the Z value type for afu record in 3D plot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.CAE.FTK.DataManager.AfuRecordZValue
    @property
    def AfuRecordZValue(self) -> NXOpen.CAE.FTK.DataManager.AfuRecordZValue:
        """
        Getter for property: (@link NXOpen.CAE.FTK.DataManager.AfuRecordZValue NXOpen.CAE.FTK.DataManager.AfuRecordZValue@endlink) AfuRecordZValue
          the Z value type for afu record in 3D plot   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CAE.FTK.DataManager.AfuRecordZValue NXOpen.CAE.FTK.DataManager.AfuRecordZValue@endlink) AfuRecordZValue

    ##   the Z value type for afu record in 3D plot   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AfuRecordZValue.setter
    def AfuRecordZValue(self, afuZValue: NXOpen.CAE.FTK.DataManager.AfuRecordZValue):
        """
        Setter for property: (@link NXOpen.CAE.FTK.DataManager.AfuRecordZValue NXOpen.CAE.FTK.DataManager.AfuRecordZValue@endlink) AfuRecordZValue
          the Z value type for afu record in 3D plot   
            
         
        """
        pass
    
    ## Getter for property: (@link Preference.DropActionOption NXOpen.CAE.Xyplot.Preference.DropActionOption@endlink) DropOnPlotViewAction
    ##   the action when dropping data to a viewport   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Preference.DropActionOption
    @property
    def DropOnPlotViewAction(self) -> Preference.DropActionOption:
        """
        Getter for property: (@link Preference.DropActionOption NXOpen.CAE.Xyplot.Preference.DropActionOption@endlink) DropOnPlotViewAction
          the action when dropping data to a viewport   
            
         
        """
        pass
    
    ## Setter for property: (@link Preference.DropActionOption NXOpen.CAE.Xyplot.Preference.DropActionOption@endlink) DropOnPlotViewAction

    ##   the action when dropping data to a viewport   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DropOnPlotViewAction.setter
    def DropOnPlotViewAction(self, dropAction: Preference.DropActionOption):
        """
        Setter for property: (@link Preference.DropActionOption NXOpen.CAE.Xyplot.Preference.DropActionOption@endlink) DropOnPlotViewAction
          the action when dropping data to a viewport   
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumDisplayableColumnsInMatrix
    ##   the maximum displayable column count in a matrix plot.  
    ##    The column count must be greater than 0    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def MaximumDisplayableColumnsInMatrix(self) -> int:
        """
        Getter for property: (int) MaximumDisplayableColumnsInMatrix
          the maximum displayable column count in a matrix plot.  
           The column count must be greater than 0    
         
        """
        pass
    
    ## Setter for property: (int) MaximumDisplayableColumnsInMatrix

    ##   the maximum displayable column count in a matrix plot.  
    ##    The column count must be greater than 0    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MaximumDisplayableColumnsInMatrix.setter
    def MaximumDisplayableColumnsInMatrix(self, columnCount: int):
        """
        Setter for property: (int) MaximumDisplayableColumnsInMatrix
          the maximum displayable column count in a matrix plot.  
           The column count must be greater than 0    
         
        """
        pass
    
    ## Getter for property: (int) MaximumDisplayableRowsInMatrix
    ##   the maximum displayable row count in a matrix plot.  
    ##    The row count must be greater than 0    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def MaximumDisplayableRowsInMatrix(self) -> int:
        """
        Getter for property: (int) MaximumDisplayableRowsInMatrix
          the maximum displayable row count in a matrix plot.  
           The row count must be greater than 0    
         
        """
        pass
    
    ## Setter for property: (int) MaximumDisplayableRowsInMatrix

    ##   the maximum displayable row count in a matrix plot.  
    ##    The row count must be greater than 0    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @MaximumDisplayableRowsInMatrix.setter
    def MaximumDisplayableRowsInMatrix(self, rowCount: int):
        """
        Setter for property: (int) MaximumDisplayableRowsInMatrix
          the maximum displayable row count in a matrix plot.  
           The row count must be greater than 0    
         
        """
        pass
    
    ## Getter for property: (int) MaximumSubGraphsInStack
    ##   the maximum sub-graph count in a stacked graph    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def MaximumSubGraphsInStack(self) -> int:
        """
        Getter for property: (int) MaximumSubGraphsInStack
          the maximum sub-graph count in a stacked graph    
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumSubGraphsInStack

    ##   the maximum sub-graph count in a stacked graph    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @MaximumSubGraphsInStack.setter
    def MaximumSubGraphsInStack(self, graphCount: int):
        """
        Setter for property: (int) MaximumSubGraphsInStack
          the maximum sub-graph count in a stacked graph    
            
         
        """
        pass
    
    ## Getter for property: (@link Preference.NewWindowChoice NXOpen.CAE.Xyplot.Preference.NewWindowChoice@endlink) NewWindowSetting
    ##   the new window setting value.  
    ##    Avaliable when @link CAE::Xyplot::Preference::TargetWindowSetting CAE::Xyplot::Preference::TargetWindowSetting@endlink 
    ##                 is @link CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate@endlink .   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Preference.NewWindowChoice
    @property
    def NewWindowSetting(self) -> Preference.NewWindowChoice:
        """
        Getter for property: (@link Preference.NewWindowChoice NXOpen.CAE.Xyplot.Preference.NewWindowChoice@endlink) NewWindowSetting
          the new window setting value.  
           Avaliable when @link CAE::Xyplot::Preference::TargetWindowSetting CAE::Xyplot::Preference::TargetWindowSetting@endlink 
                        is @link CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link Preference.NewWindowChoice NXOpen.CAE.Xyplot.Preference.NewWindowChoice@endlink) NewWindowSetting

    ##   the new window setting value.  
    ##    Avaliable when @link CAE::Xyplot::Preference::TargetWindowSetting CAE::Xyplot::Preference::TargetWindowSetting@endlink 
    ##                 is @link CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate@endlink .   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NewWindowSetting.setter
    def NewWindowSetting(self, newWindowSetting: Preference.NewWindowChoice):
        """
        Setter for property: (@link Preference.NewWindowChoice NXOpen.CAE.Xyplot.Preference.NewWindowChoice@endlink) NewWindowSetting
          the new window setting value.  
           Avaliable when @link CAE::Xyplot::Preference::TargetWindowSetting CAE::Xyplot::Preference::TargetWindowSetting@endlink 
                        is @link CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link Preference.TargetGraphicWindowOption NXOpen.CAE.Xyplot.Preference.TargetGraphicWindowOption@endlink) TargetWindowSetting
    ##   the target window setting value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Preference.TargetGraphicWindowOption
    @property
    def TargetWindowSetting(self) -> Preference.TargetGraphicWindowOption:
        """
        Getter for property: (@link Preference.TargetGraphicWindowOption NXOpen.CAE.Xyplot.Preference.TargetGraphicWindowOption@endlink) TargetWindowSetting
          the target window setting value   
            
         
        """
        pass
    
    ## Setter for property: (@link Preference.TargetGraphicWindowOption NXOpen.CAE.Xyplot.Preference.TargetGraphicWindowOption@endlink) TargetWindowSetting

    ##   the target window setting value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @TargetWindowSetting.setter
    def TargetWindowSetting(self, targetWindowSetting: Preference.TargetGraphicWindowOption):
        """
        Setter for property: (@link Preference.TargetGraphicWindowOption NXOpen.CAE.Xyplot.Preference.TargetGraphicWindowOption@endlink) TargetWindowSetting
          the target window setting value   
            
         
        """
        pass
    
    ##  Saves preference settings to memory file so that preference setting could be shared among sessions 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Save(pThis: Preference) -> None:
        """
         Saves preference settings to memory file so that preference setting could be shared among sessions 
        """
        pass
    
##  Manages the probing display styles.  <br> Not support KF.  <br> 
class ProbingStyle(BaseDisplayStyleSetting): 
    """ Manages the probing display styles. """


    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) HelpLineStyle
    ##   the help line display style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def HelpLineStyle(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) HelpLineStyle
          the help line display style.  
             
         
        """
        pass
    
    ## Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) StepLineStyle
    ##   the step line display style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return CurveDisplaySettings
    @property
    def StepLineStyle(self) -> CurveDisplaySettings:
        """
        Getter for property: (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink) StepLineStyle
          the step line display style.  
             
         
        """
        pass
    
    ## Getter for property: (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink) TextStyle
    ##   the text display style.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return TextStyleSetting
    @property
    def TextStyle(self) -> TextStyleSetting:
        """
        Getter for property: (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink) TextStyle
          the text display style.  
             
         
        """
        pass
    
##  Represents the probing text display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ProbingTextStyleSetting(TextStyleSetting): 
    """ Represents the probing text display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (bool) DataLabelVisibility
    ##  the option specifies whether to show point label text  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def DataLabelVisibility(self) -> bool:
        """
        Getter for property: (bool) DataLabelVisibility
         the option specifies whether to show point label text  
            
         
        """
        pass
    
    ## Setter for property: (bool) DataLabelVisibility

    ##  the option specifies whether to show point label text  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DataLabelVisibility.setter
    def DataLabelVisibility(self, isShowLabel: bool):
        """
        Setter for property: (bool) DataLabelVisibility
         the option specifies whether to show point label text  
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents a data accessor to retrieve data from Function Plot.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class ResultAccessor(NXOpen.TransientObject): 
    """ <summary> Represents a data accessor to retrieve data from Function Plot. </summary> """


    ## Getter for property: (int) CanvasIndex
    ##   the canvas index this object was created for.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def CanvasIndex(self) -> int:
        """
        Getter for property: (int) CanvasIndex
          the canvas index this object was created for.  
             
         
        """
        pass
    
    ## Getter for property: (int) GraphCount
    ##   the number of graphs on this canvas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def GraphCount(self) -> int:
        """
        Getter for property: (int) GraphCount
          the number of graphs on this canvas.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OnCanvas
    ##   the result access mode.  
    ##   
    ##             
    ##                 If true, this object retrieves data from a specific canvas.
    ## 
    ##                 If false, this object retrieves data from the entire plot.
    ##                 
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def OnCanvas(self) -> bool:
        """
        Getter for property: (bool) OnCanvas
          the result access mode.  
          
                    
                        If true, this object retrieves data from a specific canvas.
        
                        If false, this object retrieves data from the entire plot.
                        
         
        """
        pass
    
    ## Getter for property: (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) Plot
    ##   the plot this object was created for.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return Plot
    @property
    def Plot(self) -> Plot:
        """
        Getter for property: (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) Plot
          the plot this object was created for.  
             
         
        """
        pass
    
    ## Getter for property: (int) RecordCount
    ##   the number of records this object can access.  
    ##    
    ##             
    ##                 If
    ##     ## @link NXOpen.CAE.Xyplot.ResultAccessor.OnCanvas@endlink is true,
    ##                 then you can retrieve records specific to the canvas this object was created on.
    ## 
    ##                 If @link NXOpen.CAE.Xyplot.ResultAccessor.OnCanvas@endlink is false,
    ##                 then you can retrieve records all records in this plot.
    ##                 
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def RecordCount(self) -> int:
        """
        Getter for property: (int) RecordCount
          the number of records this object can access.  
           
                    
                        If
            ## @link NXOpen.CAE.Xyplot.ResultAccessor.OnCanvas@endlink is true,
                        then you can retrieve records specific to the canvas this object was created on.
        
                        If @link NXOpen.CAE.Xyplot.ResultAccessor.OnCanvas@endlink is false,
                        then you can retrieve records all records in this plot.
                        
         
        """
        pass
    
    ##  Asks argand 3D function data accessor. 
    ##  @return functionDataAccessor (@link Argand3DFunctionDataAccessor NXOpen.CAE.Xyplot.Argand3DFunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor.GraphCount@endlink 
    def AskArgand3DFunctionDataAccessor(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> Argand3DFunctionDataAccessor:
        """
         Asks argand 3D function data accessor. 
         @return functionDataAccessor (@link Argand3DFunctionDataAccessor NXOpen.CAE.Xyplot.Argand3DFunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Asks BarChart function data accessor. 
    ##  @return functionDataAccessor (@link BarChartFunctionDataAccessor NXOpen.CAE.Xyplot.BarChartFunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor.GraphCount@endlink 
    def AskBarChartFunctionDataAccessor(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> BarChartFunctionDataAccessor:
        """
         Asks BarChart function data accessor. 
         @return functionDataAccessor (@link BarChartFunctionDataAccessor NXOpen.CAE.Xyplot.BarChartFunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Asks campbell function data accessor. 
    ##  @return functionDataAccessor (@link CampbellFunctionDataAccessor NXOpen.CAE.Xyplot.CampbellFunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor.GraphCount@endlink 
    def AskCampbellFunctionDataAccessor(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> CampbellFunctionDataAccessor:
        """
         Asks campbell function data accessor. 
         @return functionDataAccessor (@link CampbellFunctionDataAccessor NXOpen.CAE.Xyplot.CampbellFunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Asks function data accessor type. Then choose correct method to get data accessor according to the accessor type returned 
    ##  @return accessorType (@link FunctionDataAccessor NXOpen.CAE.Xyplot.FunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor.GraphCount@endlink 
    def AskFunctionDataAccessorType(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> FunctionDataAccessor:
        """
         Asks function data accessor type. Then choose correct method to get data accessor according to the accessor type returned 
         @return accessorType (@link FunctionDataAccessor NXOpen.CAE.Xyplot.FunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Asks matrix function data accessor. 
    ##  @return functionDataAccessor (@link MatrixFunctionDataAccessor NXOpen.CAE.Xyplot.MatrixFunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor.GraphCount@endlink 
    def AskMatrixFunctionDataAccessor(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> MatrixFunctionDataAccessor:
        """
         Asks matrix function data accessor. 
         @return functionDataAccessor (@link MatrixFunctionDataAccessor NXOpen.CAE.Xyplot.MatrixFunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Asks post environment settings. 
    ##  @return postEnvironment (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskPostEnvironment(resultAccessor: ResultAccessor) -> NXOpen.TaggedObject:
        """
         Asks post environment settings. 
         @return postEnvironment (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink): .
        """
        pass
    
    ##  Asks XY function data accessor. 
    ##  @return functionDataAccessor (@link XYFunctionDataAccessor NXOpen.CAE.Xyplot.XYFunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor@endlink 
    def AskXYFunctionDataAccessor(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> XYFunctionDataAccessor:
        """
         Asks XY function data accessor. 
         @return functionDataAccessor (@link XYFunctionDataAccessor NXOpen.CAE.Xyplot.XYFunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Asks XYZ function data accessor. 
    ##  @return functionDataAccessor (@link XYZFunctionDataAccessor NXOpen.CAE.Xyplot.XYZFunctionDataAccessor@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ##  The graph index starts form 0 to graph count -1. Get graph count from @link ResultAccessor.GraphCount@endlink 
    def AskXYZFunctionDataAccessor(resultAccessor: ResultAccessor, graphIndex: int, recordIndex: int) -> XYZFunctionDataAccessor:
        """
         Asks XYZ function data accessor. 
         @return functionDataAccessor (@link XYZFunctionDataAccessor NXOpen.CAE.Xyplot.XYZFunctionDataAccessor@endlink): .
        """
        pass
    
    ##  Destroys the object. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(resultAccessor: ResultAccessor) -> None:
        """
         Destroys the object. 
        """
        pass
    
    ##   @brief Retrieve a Graph from this Canvas. 
    ## 
    ##  
    ##             
    ##                 
    ##                  <br> This method is useful to retrieve @link NXOpen::CAE::Xyplot::Graph NXOpen::CAE::Xyplot::Graph@endlink  objects in the context of a canvas. <br> 
    ##                  <br> This method raises an error if this object was not constructed with a canvas index. <br> 
    ##                  <br> Graphs can also be retrieved globally from @link NXOpen::CAE::Xyplot::Plot NXOpen::CAE::Xyplot::Plot@endlink  via @link NXOpen::NXObject::FindObject NXOpen::NXObject::FindObject@endlink . <br> 
    ##                  <br> See @link NXOpen::CAE::Xyplot::XYPlotManager::CreateResultAccessorOnCanvas NXOpen::CAE::Xyplot::XYPlotManager::CreateResultAccessorOnCanvas@endlink . <br> 
    ##                 
    ##               
    ##  @return graph (@link Graph NXOpen.CAE.Xyplot.Graph@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  the index of the graph on this canvas 
    def GetNthGraph(resultAccessor: ResultAccessor, graphIdx: int) -> Graph:
        """
          @brief Retrieve a Graph from this Canvas. 
        
         
                    
                        
                         <br> This method is useful to retrieve @link NXOpen::CAE::Xyplot::Graph NXOpen::CAE::Xyplot::Graph@endlink  objects in the context of a canvas. <br> 
                         <br> This method raises an error if this object was not constructed with a canvas index. <br> 
                         <br> Graphs can also be retrieved globally from @link NXOpen::CAE::Xyplot::Plot NXOpen::CAE::Xyplot::Plot@endlink  via @link NXOpen::NXObject::FindObject NXOpen::NXObject::FindObject@endlink . <br> 
                         <br> See @link NXOpen::CAE::Xyplot::XYPlotManager::CreateResultAccessorOnCanvas NXOpen::CAE::Xyplot::XYPlotManager::CreateResultAccessorOnCanvas@endlink . <br> 
                        
                      
         @return graph (@link Graph NXOpen.CAE.Xyplot.Graph@endlink): .
        """
        pass
    
import NXOpen
##  Represents the result legend style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ResultLegendStyle(BaseDisplayStyleSetting): 
    """ Represents the result legend style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) OverflowResultColorOption
    ##   the overflow result color option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FlowResultColor
    @property
    def OverflowResultColorOption(self) -> FlowResultColor:
        """
        Getter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) OverflowResultColorOption
          the overflow result color option   
            
         
        """
        pass
    
    ## Setter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) OverflowResultColorOption

    ##   the overflow result color option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OverflowResultColorOption.setter
    def OverflowResultColorOption(self, colorOption: FlowResultColor):
        """
        Setter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) OverflowResultColorOption
          the overflow result color option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowResultShadedColor
    ##   the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption@endlink 
    ##             is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OverflowResultShadedColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowResultShadedColor
          the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption@endlink 
                    is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowResultShadedColor

    ##   the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption@endlink 
    ##             is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OverflowResultShadedColor.setter
    def OverflowResultShadedColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OverflowResultShadedColor
          the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption@endlink 
                    is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) UnderflowResultColorOption
    ##   the underflow result color option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return FlowResultColor
    @property
    def UnderflowResultColorOption(self) -> FlowResultColor:
        """
        Getter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) UnderflowResultColorOption
          the underflow result color option   
            
         
        """
        pass
    
    ## Setter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) UnderflowResultColorOption

    ##   the underflow result color option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnderflowResultColorOption.setter
    def UnderflowResultColorOption(self, colorOption: FlowResultColor):
        """
        Setter for property: (@link FlowResultColor NXOpen.CAE.Xyplot.FlowResultColor@endlink) UnderflowResultColorOption
          the underflow result color option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowResultShadedColor
    ##   the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption@endlink 
    ##             is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def UnderflowResultShadedColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowResultShadedColor
          the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption@endlink 
                    is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowResultShadedColor

    ##   the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption@endlink 
    ##             is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnderflowResultShadedColor.setter
    def UnderflowResultShadedColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UnderflowResultShadedColor
          the user defined color of overflow result, only available when @link NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption@endlink 
                    is @link NXOpen::CAE::Xyplot::FlowResultColorShaded NXOpen::CAE::Xyplot::FlowResultColorShaded@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link UnknownResultColor NXOpen.CAE.Xyplot.UnknownResultColor@endlink) UnknownResultColorOption
    ##   the unknown result color option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return UnknownResultColor
    @property
    def UnknownResultColorOption(self) -> UnknownResultColor:
        """
        Getter for property: (@link UnknownResultColor NXOpen.CAE.Xyplot.UnknownResultColor@endlink) UnknownResultColorOption
          the unknown result color option   
            
         
        """
        pass
    
    ## Setter for property: (@link UnknownResultColor NXOpen.CAE.Xyplot.UnknownResultColor@endlink) UnknownResultColorOption

    ##   the unknown result color option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UnknownResultColorOption.setter
    def UnknownResultColorOption(self, unknownResultColor: UnknownResultColor):
        """
        Setter for property: (@link UnknownResultColor NXOpen.CAE.Xyplot.UnknownResultColor@endlink) UnknownResultColorOption
          the unknown result color option   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
import NXOpen
##  Represents the scatter display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ScatterStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the scatter display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##   the point color  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the point color  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##   the point color  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the point color  
            
         
        """
        pass
    
import NXOpen
##  It represents a sound player which could play sound for a time-pressure function on a @link CAE::Xyplot::PlotTypePlot2D CAE::Xyplot::PlotTypePlot2D@endlink  plot.  <br> To create a new instance of this class, use @link NXOpen::CAE::Xyplot::Graph::CreateSoundPlayer  NXOpen::CAE::Xyplot::Graph::CreateSoundPlayer @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class SoundPlayer(NXOpen.TransientObject): 
    """ It represents a sound player which could play sound for a time-pressure function on a <ja_enum_member>CAE.Xyplot.PlotType.Plot2D</ja_enum_member> plot. """


    ## Getter for property: (bool) Cyclestate
    ##   the cycle state   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Cyclestate(self) -> bool:
        """
        Getter for property: (bool) Cyclestate
          the cycle state   
            
         
        """
        pass
    
    ## Setter for property: (bool) Cyclestate

    ##   the cycle state   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Cyclestate.setter
    def Cyclestate(self, state: bool):
        """
        Setter for property: (bool) Cyclestate
          the cycle state   
            
         
        """
        pass
    
    ##  Destroys the object 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(soundPlayer: SoundPlayer) -> None:
        """
         Destroys the object 
        """
        pass
    
    ##  Plays sound. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Play(soundPlayer: SoundPlayer) -> None:
        """
         Plays sound. 
        """
        pass
    
    ##  Stops playing sound. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Stop(soundPlayer: SoundPlayer) -> None:
        """
         Stops playing sound. 
        """
        pass
    
##  Represents the parameter settings for exporting source data.  <br> To create a new instance of this class, use @link NXOpen::CAE::Xyplot::DataExporter::NewSourceDataExportParameters  NXOpen::CAE::Xyplot::DataExporter::NewSourceDataExportParameters @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class SourceDataExportParameters(DataExportParameters): 
    """ Represents the parameter settings for exporting source data. """


    ##  Defines the ordinate complex data type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## RealImag</term><description> 
    ## </description> </item><item><term> 
    ## MagPhase</term><description> 
    ## </description> </item></list>
    class ComplextDataSaveOption(Enum):
        """
        Members Include: <RealImag> <MagPhase>
        """
        RealImag: int
        MagPhase: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SourceDataExportParameters.ComplextDataSaveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SourceDataExportParameters.ComplextDataSaveOption NXOpen.CAE.Xyplot.SourceDataExportParameters.ComplextDataSaveOption@endlink) ComplexDataSaveSetting
    ##   the option to save complex data   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return SourceDataExportParameters.ComplextDataSaveOption
    @property
    def ComplexDataSaveSetting(self) -> SourceDataExportParameters.ComplextDataSaveOption:
        """
        Getter for property: (@link SourceDataExportParameters.ComplextDataSaveOption NXOpen.CAE.Xyplot.SourceDataExportParameters.ComplextDataSaveOption@endlink) ComplexDataSaveSetting
          the option to save complex data   
            
         
        """
        pass
    
    ## Setter for property: (@link SourceDataExportParameters.ComplextDataSaveOption NXOpen.CAE.Xyplot.SourceDataExportParameters.ComplextDataSaveOption@endlink) ComplexDataSaveSetting

    ##   the option to save complex data   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ComplexDataSaveSetting.setter
    def ComplexDataSaveSetting(self, complexDataType: SourceDataExportParameters.ComplextDataSaveOption):
        """
        Setter for property: (@link SourceDataExportParameters.ComplextDataSaveOption NXOpen.CAE.Xyplot.SourceDataExportParameters.ComplextDataSaveOption@endlink) ComplexDataSaveSetting
          the option to save complex data   
            
         
        """
        pass
    
    ##  Gets the section data index vector.
    ##                 
    ##                 For @link CAE::Xyplot::PlotTypePlotColorMap CAE::Xyplot::PlotTypePlotColorMap@endlink ,
    ##                 @link CAE::Xyplot::PlotTypePlot3D CAE::Xyplot::PlotTypePlot3D@endlink ,
    ##                 and @link CAE::Xyplot::PlotTypePlotMatrix2D CAE::Xyplot::PlotTypePlotMatrix2D@endlink ,
    ##                 the plot data is composed with multiple section data.
    ##                 When saving the data of above plots to AFU or CSV files, user could specify the indexes of the section data.
    ##                 
    ##             
    ##  @return sectionDataIndices (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSectionDataIndices(param: SourceDataExportParameters) -> List[int]:
        """
         Gets the section data index vector.
                        
                        For @link CAE::Xyplot::PlotTypePlotColorMap CAE::Xyplot::PlotTypePlotColorMap@endlink ,
                        @link CAE::Xyplot::PlotTypePlot3D CAE::Xyplot::PlotTypePlot3D@endlink ,
                        and @link CAE::Xyplot::PlotTypePlotMatrix2D CAE::Xyplot::PlotTypePlotMatrix2D@endlink ,
                        the plot data is composed with multiple section data.
                        When saving the data of above plots to AFU or CSV files, user could specify the indexes of the section data.
                        
                    
         @return sectionDataIndices (List[int]): .
        """
        pass
    
    ##  Sets the section data index vector.
    ##                 
    ##                 For @link CAE::Xyplot::PlotTypePlotColorMap CAE::Xyplot::PlotTypePlotColorMap@endlink ,
    ##                 @link CAE::Xyplot::PlotTypePlot3D CAE::Xyplot::PlotTypePlot3D@endlink ,
    ##                 and @link CAE::Xyplot::PlotTypePlotMatrix2D CAE::Xyplot::PlotTypePlotMatrix2D@endlink ,
    ##                 the plot data is composed with multiple section data.
    ##                 When saving the data of above plots to AFU or CSV files, user could specify the indexes of the section data.
    ##                 
    ##             
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionDataIndices"> (List[int]) </param>
    def SetSectionDataIndices(param: SourceDataExportParameters, sectionDataIndices: List[int]) -> None:
        """
         Sets the section data index vector.
                        
                        For @link CAE::Xyplot::PlotTypePlotColorMap CAE::Xyplot::PlotTypePlotColorMap@endlink ,
                        @link CAE::Xyplot::PlotTypePlot3D CAE::Xyplot::PlotTypePlot3D@endlink ,
                        and @link CAE::Xyplot::PlotTypePlotMatrix2D CAE::Xyplot::PlotTypePlotMatrix2D@endlink ,
                        the plot data is composed with multiple section data.
                        When saving the data of above plots to AFU or CSV files, user could specify the indexes of the section data.
                        
                    
        """
        pass
    
import NXOpen
##   @brief  Manages the display of stacked plot. 
## 
##  
##         
##         Call @link CAE::Xyplot::I2DDataPlot::EditRecord CAE::Xyplot::I2DDataPlot::EditRecord@endlink  to edit data for this class.
##           <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class StackedPlot(Plot): 
    """ <summary> Manages the display of stacked plot.</summary>
        <remarks>
        Call <ja_method>CAE.Xyplot.I2DDataPlot.EditRecord</ja_method> to edit data for this class.
        </remarks> """


    ##  Gets the post environment settings of specific sub plot. 
    ##  @return postEnvironmentSettings (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  The plot index starts form 0 to plot count. Get plot count from @link StackedPlot::GetSubplotCount StackedPlot::GetSubplotCount@endlink  
    def GetPostEnvironmentSettingsOfSubplot(plot: StackedPlot, plotIndex: int) -> NXOpen.TaggedObject:
        """
         Gets the post environment settings of specific sub plot. 
         @return postEnvironmentSettings (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  .
        """
        pass
    
    ##  Get sub plot count in the plot.
    ##  @return subplotCount (int):  Sub plot count .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSubplotCount(plot: StackedPlot) -> int:
        """
         Get sub plot count in the plot.
         @return subplotCount (int):  Sub plot count .
        """
        pass
    
##  Represents the surface filling color option 
##  No shading 
class SurfaceColorOption(Enum):
    """
    Members Include: <NotSet> <Hidden> <Shaded>
    """
    NotSet: int
    Hidden: int
    Shaded: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SurfaceColorOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the surface display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class SurfaceStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the surface display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link SurfaceColorOption NXOpen.CAE.Xyplot.SurfaceColorOption@endlink) ColorOption
    ##   the color option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SurfaceColorOption
    @property
    def ColorOption(self) -> SurfaceColorOption:
        """
        Getter for property: (@link SurfaceColorOption NXOpen.CAE.Xyplot.SurfaceColorOption@endlink) ColorOption
          the color option   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceColorOption NXOpen.CAE.Xyplot.SurfaceColorOption@endlink) ColorOption

    ##   the color option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: SurfaceColorOption):
        """
        Setter for property: (@link SurfaceColorOption NXOpen.CAE.Xyplot.SurfaceColorOption@endlink) ColorOption
          the color option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
    ##   the filling color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the filling color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor

    ##   the filling color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the filling color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
    ##   the outline color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
          the outline color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor

    ##   the outline color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) OutlineColor
          the outline color   
            
         
        """
        pass
    
##  Represents the text alignment 
##  Left align text 
class TextAlignment(Enum):
    """
    Members Include: <Left> <Center> <Right>
    """
    Left: int
    Center: int
    Right: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TextAlignment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the postion of the text box corner 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Center</term><description> 
## </description> </item><item><term> 
## LowerLeft</term><description> 
## </description> </item><item><term> 
## LowerRight</term><description> 
## </description> </item><item><term> 
## UpperLeft</term><description> 
## </description> </item><item><term> 
## UpperRight</term><description> 
## </description> </item></list>
class TextBoxCornerType(Enum):
    """
    Members Include: <Center> <LowerLeft> <LowerRight> <UpperLeft> <UpperRight>
    """
    Center: int
    LowerLeft: int
    LowerRight: int
    UpperLeft: int
    UpperRight: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TextBoxCornerType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the margin position in a text box 
##  The left margin of text box     
class TextBoxMarginOption(Enum):
    """
    Members Include: <Left> <Top> <Right> <Bottom>
    """
    Left: int
    Top: int
    Right: int
    Bottom: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TextBoxMarginOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the text box display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified. <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class TextBoxStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the text box display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified."""


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##   the text box outline color  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the text box outline color  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##   the text box outline color  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the text box outline color  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
    ##   the text box filling color  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the text box filling color  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor

    ##   the text box filling color  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) FillingColor
          the text box filling color  
            
         
        """
        pass
    
    ## Getter for property: (bool) IsFilled
    ##   a value indicating whether to fill the text box   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def IsFilled(self) -> bool:
        """
        Getter for property: (bool) IsFilled
          a value indicating whether to fill the text box   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsFilled

    ##   a value indicating whether to fill the text box   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IsFilled.setter
    def IsFilled(self, isFilled: bool):
        """
        Setter for property: (bool) IsFilled
          a value indicating whether to fill the text box   
            
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   a value indicating whether to display the text box   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          a value indicating whether to display the text box   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   a value indicating whether to display the text box   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          a value indicating whether to display the text box   
            
         
        """
        pass
    
    ##  Gets the text box line style
    ##  @return boxLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):   .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLineStyle(pThis: TextBoxStyleSetting) -> CurveDisplaySettings:
        """
         Gets the text box line style
         @return boxLineStyle (@link CurveDisplaySettings NXOpen.CAE.Xyplot.CurveDisplaySettings@endlink):   .
        """
        pass
    
    ## Gets the margin value of text box 
    ##  @return marginValue (float):   .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## margin option
    def GetMargin(pThis: TextBoxStyleSetting, marginOption: TextBoxMarginOption) -> float:
        """
        Gets the margin value of text box 
         @return marginValue (float):   .
        """
        pass
    
    ## Sets the margin value of text box 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## margin option
    def SetMargin(pThis: TextBoxStyleSetting, marginOption: TextBoxMarginOption, marginValue: float) -> None:
        """
        Sets the margin value of text box 
        """
        pass
    
##  Represents the text orientation 
##  Horizontal text orientation 
class TextOrientation(Enum):
    """
    Members Include: <Horizontal> <Upward> <Downward>
    """
    Horizontal: int
    Upward: int
    Downward: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TextOrientation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.CAE
import NXOpen.Display
import NXOpen.Preferences
##  Represents the text display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
##             to apply style changes to corresponding plot after it's modified.
##          <br> Not support KF.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class TextStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the text display style. Call <ja_method>CAE.Xyplot.BaseDisplayStyleSetting.CommitChange</ja_method>
            to apply style changes to corresponding plot after it's modified.
        """


    ## Getter for property: (@link TextAlignment NXOpen.CAE.Xyplot.TextAlignment@endlink) Alignment
    ##   the text alignment.  
    ##    Only valid for title options, legend options and axis label options.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TextAlignment
    @property
    def Alignment(self) -> TextAlignment:
        """
        Getter for property: (@link TextAlignment NXOpen.CAE.Xyplot.TextAlignment@endlink) Alignment
          the text alignment.  
           Only valid for title options, legend options and axis label options.   
         
        """
        pass
    
    ## Setter for property: (@link TextAlignment NXOpen.CAE.Xyplot.TextAlignment@endlink) Alignment

    ##   the text alignment.  
    ##    Only valid for title options, legend options and axis label options.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Alignment.setter
    def Alignment(self, alignment: TextAlignment):
        """
        Setter for property: (@link TextAlignment NXOpen.CAE.Xyplot.TextAlignment@endlink) Alignment
          the text alignment.  
           Only valid for title options, legend options and axis label options.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##   the text color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the text color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##   the text color   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
          the text color   
            
         
        """
        pass
    
    ## Getter for property: (str) Font
    ##   the text font   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Font(self) -> str:
        """
        Getter for property: (str) Font
          the text font   
            
         
        """
        pass
    
    ## Setter for property: (str) Font

    ##   the text font   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Font.setter
    def Font(self, font: str):
        """
        Setter for property: (str) Font
          the text font   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Preferences.VisualizationFonts.StyleType NXOpen.Preferences.VisualizationFonts.StyleType@endlink) FontStyle
    ##   the text font style.  
    ##    Available when the text font is standard font.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Preferences.VisualizationFonts.StyleType
    @property
    def FontStyle(self) -> NXOpen.Preferences.VisualizationFonts.StyleType:
        """
        Getter for property: (@link NXOpen.Preferences.VisualizationFonts.StyleType NXOpen.Preferences.VisualizationFonts.StyleType@endlink) FontStyle
          the text font style.  
           Available when the text font is standard font.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Preferences.VisualizationFonts.StyleType NXOpen.Preferences.VisualizationFonts.StyleType@endlink) FontStyle

    ##   the text font style.  
    ##    Available when the text font is standard font.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FontStyle.setter
    def FontStyle(self, fontStyle: NXOpen.Preferences.VisualizationFonts.StyleType):
        """
        Setter for property: (@link NXOpen.Preferences.VisualizationFonts.StyleType NXOpen.Preferences.VisualizationFonts.StyleType@endlink) FontStyle
          the text font style.  
           Available when the text font is standard font.   
         
        """
        pass
    
    ## Getter for property: (@link Fonttype NXOpen.CAE.Xyplot.Fonttype@endlink) FontType
    ##   the text font type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Fonttype
    @property
    def FontType(self) -> Fonttype:
        """
        Getter for property: (@link Fonttype NXOpen.CAE.Xyplot.Fonttype@endlink) FontType
          the text font type   
            
         
        """
        pass
    
    ## Setter for property: (@link Fonttype NXOpen.CAE.Xyplot.Fonttype@endlink) FontType

    ##   the text font type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @FontType.setter
    def FontType(self, fontType: Fonttype):
        """
        Setter for property: (@link Fonttype NXOpen.CAE.Xyplot.Fonttype@endlink) FontType
          the text font type   
            
         
        """
        pass
    
    ## Getter for property: (float) GlobalSizeScale
    ##   the scale of global text size.  
    ##   
    ##                 It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true,
    ##                 and @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  is false.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def GlobalSizeScale(self) -> float:
        """
        Getter for property: (float) GlobalSizeScale
          the scale of global text size.  
          
                        It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true,
                        and @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  is false.   
         
        """
        pass
    
    ## Setter for property: (float) GlobalSizeScale

    ##   the scale of global text size.  
    ##   
    ##                 It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true,
    ##                 and @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  is false.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @GlobalSizeScale.setter
    def GlobalSizeScale(self, sizeScale: float):
        """
        Setter for property: (float) GlobalSizeScale
          the scale of global text size.  
          
                        It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true,
                        and @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  is false.   
         
        """
        pass
    
    ## Getter for property: (bool) IsGlobalSizeAutoScaled
    ##   a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
    ##   
    ##                 It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def IsGlobalSizeAutoScaled(self) -> bool:
        """
        Getter for property: (bool) IsGlobalSizeAutoScaled
          a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
          
                        It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true.   
         
        """
        pass
    
    ## Setter for property: (bool) IsGlobalSizeAutoScaled

    ##   a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
    ##   
    ##                 It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @IsGlobalSizeAutoScaled.setter
    def IsGlobalSizeAutoScaled(self, isGlobalSizeAutoScaled: bool):
        """
        Setter for property: (bool) IsGlobalSizeAutoScaled
          a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
          
                        It will be taken only when @link CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting@endlink  is true.   
         
        """
        pass
    
    ## Getter for property: (@link LeaderStyle NXOpen.CAE.Xyplot.LeaderStyle@endlink) LeaderStyle
    ##   the leader style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return LeaderStyle
    @property
    def LeaderStyle(self) -> LeaderStyle:
        """
        Getter for property: (@link LeaderStyle NXOpen.CAE.Xyplot.LeaderStyle@endlink) LeaderStyle
          the leader style   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.NumberFormat NXOpen.CAE.NumberFormat@endlink) NumberFormat
    ##   the number format options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CAE.NumberFormat
    @property
    def NumberFormat(self) -> NXOpen.CAE.NumberFormat:
        """
        Getter for property: (@link NXOpen.CAE.NumberFormat NXOpen.CAE.NumberFormat@endlink) NumberFormat
          the number format options   
            
         
        """
        pass
    
    ## Getter for property: (@link TextOrientation NXOpen.CAE.Xyplot.TextOrientation@endlink) Orientation
    ##   the text orientation.  
    ##    Only invalid for legend options.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TextOrientation
    @property
    def Orientation(self) -> TextOrientation:
        """
        Getter for property: (@link TextOrientation NXOpen.CAE.Xyplot.TextOrientation@endlink) Orientation
          the text orientation.  
           Only invalid for legend options.   
         
        """
        pass
    
    ## Setter for property: (@link TextOrientation NXOpen.CAE.Xyplot.TextOrientation@endlink) Orientation

    ##   the text orientation.  
    ##    Only invalid for legend options.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Orientation.setter
    def Orientation(self, orientation: TextOrientation):
        """
        Setter for property: (@link TextOrientation NXOpen.CAE.Xyplot.TextOrientation@endlink) Orientation
          the text orientation.  
           Only invalid for legend options.   
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##   the text size.  
    ##    The acceptable range is 1-10.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
          the text size.  
           The acceptable range is 1-10.   
         
        """
        pass
    
    ## Setter for property: (int) Size

    ##   the text size.  
    ##    The acceptable range is 1-10.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Size.setter
    def Size(self, size: int):
        """
        Setter for property: (int) Size
          the text size.  
           The acceptable range is 1-10.   
         
        """
        pass
    
    ## Getter for property: (@link TextBoxStyleSetting NXOpen.CAE.Xyplot.TextBoxStyleSetting@endlink) TextBoxStyle
    ##   the style of text box   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return TextBoxStyleSetting
    @property
    def TextBoxStyle(self) -> TextBoxStyleSetting:
        """
        Getter for property: (@link TextBoxStyleSetting NXOpen.CAE.Xyplot.TextBoxStyleSetting@endlink) TextBoxStyle
          the style of text box   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseGlobalFontSetting
    ##   a value indicating whether to use the global setting of text font, font style and font size.  
    ##   
    ##                 If True, you need to set text size scale by setting @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  or
    ##                 @link CAE::Xyplot::TextStyleSetting::GlobalSizeScale CAE::Xyplot::TextStyleSetting::GlobalSizeScale@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def UseGlobalFontSetting(self) -> bool:
        """
        Getter for property: (bool) UseGlobalFontSetting
          a value indicating whether to use the global setting of text font, font style and font size.  
          
                        If True, you need to set text size scale by setting @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  or
                        @link CAE::Xyplot::TextStyleSetting::GlobalSizeScale CAE::Xyplot::TextStyleSetting::GlobalSizeScale@endlink    
         
        """
        pass
    
    ## Setter for property: (bool) UseGlobalFontSetting

    ##   a value indicating whether to use the global setting of text font, font style and font size.  
    ##   
    ##                 If True, you need to set text size scale by setting @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  or
    ##                 @link CAE::Xyplot::TextStyleSetting::GlobalSizeScale CAE::Xyplot::TextStyleSetting::GlobalSizeScale@endlink    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @UseGlobalFontSetting.setter
    def UseGlobalFontSetting(self, useGlobalFontSetting: bool):
        """
        Setter for property: (bool) UseGlobalFontSetting
          a value indicating whether to use the global setting of text font, font style and font size.  
          
                        If True, you need to set text size scale by setting @link CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled@endlink  or
                        @link CAE::Xyplot::TextStyleSetting::GlobalSizeScale CAE::Xyplot::TextStyleSetting::GlobalSizeScale@endlink    
         
        """
        pass
    
    ## Getter for property: (bool) Visibility
    ##   the visibility   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Setter for property: (bool) Visibility

    ##   the visibility   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
          the visibility   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Display.TransientText.TextSize NXOpen.Display.TransientText.TextSize@endlink) Weight
    ##   the text weight.  
    ##    Available when the text font is NX font.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Display.TransientText.TextSize
    @property
    def Weight(self) -> NXOpen.Display.TransientText.TextSize:
        """
        Getter for property: (@link NXOpen.Display.TransientText.TextSize NXOpen.Display.TransientText.TextSize@endlink) Weight
          the text weight.  
           Available when the text font is NX font.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Display.TransientText.TextSize NXOpen.Display.TransientText.TextSize@endlink) Weight

    ##   the text weight.  
    ##    Available when the text font is NX font.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Weight.setter
    def Weight(self, weight: NXOpen.Display.TransientText.TextSize):
        """
        Setter for property: (@link NXOpen.Display.TransientText.TextSize NXOpen.Display.TransientText.TextSize@endlink) Weight
          the text weight.  
           Available when the text font is NX font.   
         
        """
        pass
    
##  Represents the label text type 
##  Not defined type 
class TextType(Enum):
    """
    Members Include: <NotSet> <Title> <Legend> <GraphName> <PageNumber> <Marker> <Note> <ProbingText> <XLabel> <YLabel> <ZLabel> <XNumber> <YNumber> <ZNumber> <ColorAxisLabel> <ColorAxisNumber> <UnknownResultText> <AngleAxisNumber> <AnnotationText> <ArgumentAxisNumber> <BarChartValueText> <LegendTableText> <ResultLegendText> <FormulaGridValueText> <MatrixValueText>
    """
    NotSet: int
    Title: int
    Legend: int
    GraphName: int
    PageNumber: int
    Marker: int
    Note: int
    ProbingText: int
    XLabel: int
    YLabel: int
    ZLabel: int
    XNumber: int
    YNumber: int
    ZNumber: int
    ColorAxisLabel: int
    ColorAxisNumber: int
    UnknownResultText: int
    AngleAxisNumber: int
    AnnotationText: int
    ArgumentAxisNumber: int
    BarChartValueText: int
    LegendTableText: int
    ResultLegendText: int
    FormulaGridValueText: int
    MatrixValueText: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> TextType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the color for unknow result 
##  white 
class UnknownResultColor(Enum):
    """
    Members Include: <White> <Grey>
    """
    White: int
    Grey: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> UnknownResultColor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the 2D vector display style.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class VectorStyle2DSetting(BaseLineStyleSetting): 
    """ Represents the 2D vector display style. """


    ## Getter for property: (bool) DrawText
    ##   a value indicating whether to draw annotation text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def DrawText(self) -> bool:
        """
        Getter for property: (bool) DrawText
          a value indicating whether to draw annotation text   
            
         
        """
        pass
    
    ## Setter for property: (bool) DrawText

    ##   a value indicating whether to draw annotation text   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DrawText.setter
    def DrawText(self, canDrawText: bool):
        """
        Setter for property: (bool) DrawText
          a value indicating whether to draw annotation text   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsAutoTextCount
    ##   a value indicating whether to customize annotation text count   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def IsAutoTextCount(self) -> bool:
        """
        Getter for property: (bool) IsAutoTextCount
          a value indicating whether to customize annotation text count   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsAutoTextCount

    ##   a value indicating whether to customize annotation text count   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @IsAutoTextCount.setter
    def IsAutoTextCount(self, isAutoTextCount: bool):
        """
        Setter for property: (bool) IsAutoTextCount
          a value indicating whether to customize annotation text count   
            
         
        """
        pass
    
    ## Getter for property: (int) MaximumTextCount
    ##   the maximum of customized text count   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def MaximumTextCount(self) -> int:
        """
        Getter for property: (int) MaximumTextCount
          the maximum of customized text count   
            
         
        """
        pass
    
    ## Setter for property: (int) MaximumTextCount

    ##   the maximum of customized text count   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MaximumTextCount.setter
    def MaximumTextCount(self, maximumTextCount: int):
        """
        Setter for property: (int) MaximumTextCount
          the maximum of customized text count   
            
         
        """
        pass
    
    ## Getter for property: (bool) OverlapTextAndVector
    ##   a value indicating whether to allow the annotation text overlap with vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def OverlapTextAndVector(self) -> bool:
        """
        Getter for property: (bool) OverlapTextAndVector
          a value indicating whether to allow the annotation text overlap with vector   
            
         
        """
        pass
    
    ## Setter for property: (bool) OverlapTextAndVector

    ##   a value indicating whether to allow the annotation text overlap with vector   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OverlapTextAndVector.setter
    def OverlapTextAndVector(self, overlapTextAndVector: bool):
        """
        Setter for property: (bool) OverlapTextAndVector
          a value indicating whether to allow the annotation text overlap with vector   
            
         
        """
        pass
    
    ##  Get the nth vector display color 
    ##  @return vectorColor (@link NXOpen.NXColor NXOpen.NXColor@endlink):  Get the nth display vector color .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetNthVectorColor(pThis: VectorStyle2DSetting, index: int) -> NXOpen.NXColor:
        """
         Get the nth vector display color 
         @return vectorColor (@link NXOpen.NXColor NXOpen.NXColor@endlink):  Get the nth display vector color .
        """
        pass
    
    ##  Get the vector display colors 
    ##  @return vectorColors (@link NXOpen.NXColor List[NXOpen.NXColor]@endlink):  Get the display vector colors .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetVectorColors(pThis: VectorStyle2DSetting) -> List[NXOpen.NXColor]:
        """
         Get the vector display colors 
         @return vectorColors (@link NXOpen.NXColor List[NXOpen.NXColor]@endlink):  Get the display vector colors .
        """
        pass
    
    ##  Set the nth vector display color 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Set the nth display vector color 
    def SetNthVectorColors(pThis: VectorStyle2DSetting, index: int, vectorColors: NXOpen.NXColor) -> None:
        """
         Set the nth vector display color 
        """
        pass
    
    ##  Set the vector display colors 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Set the display vector colors 
    def SetVectorColors(pThis: VectorStyle2DSetting, vectorColors: List[NXOpen.NXColor]) -> None:
        """
         Set the vector display colors 
        """
        pass
    
##  Manages the 2D wall display styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class WallDisplayStyles2D(WallDisplayStyles): 
    """ Manages the 2D wall display styles. """


    ##  Gets the angle axis display style. 
    ##  @return angleAxisStyle (@link AngleAxisStyleSetting NXOpen.CAE.Xyplot.AngleAxisStyleSetting@endlink):  Angle Axis style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAngleAxisStyleSetting(wallStyles: WallDisplayStyles2D) -> AngleAxisStyleSetting:
        """
         Gets the angle axis display style. 
         @return angleAxisStyle (@link AngleAxisStyleSetting NXOpen.CAE.Xyplot.AngleAxisStyleSetting@endlink):  Angle Axis style .
        """
        pass
    
    ##  Gets the formula grid style. 
    ##  @return formulaGridStyle (@link FormulaGridStyle NXOpen.CAE.Xyplot.FormulaGridStyle@endlink):  Formula Grid style .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFormulaGridStyle(wallStyles: WallDisplayStyles2D) -> FormulaGridStyle:
        """
         Gets the formula grid style. 
         @return formulaGridStyle (@link FormulaGridStyle NXOpen.CAE.Xyplot.FormulaGridStyle@endlink):  Formula Grid style .
        """
        pass
    
import NXOpen
##  Manages the 3D wall display styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class WallDisplayStyles3D(WallDisplayStyles): 
    """ Manages the 3D wall display styles. """


    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ViewOrientation
    ##   the view orientation matrix   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def ViewOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ViewOrientation
          the view orientation matrix   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ViewOrientation

    ##   the view orientation matrix   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ViewOrientation.setter
    def ViewOrientation(self, orientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ViewOrientation
          the view orientation matrix   
            
         
        """
        pass
    
import NXOpen
##  Manages the wall display styles.  <br> Not support KF.  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class WallDisplayStyles(NXOpen.TaggedObject): 
    """ Manages the wall display styles. """


    ## Getter for property: (@link BaseGridLayoutStyleSetting NXOpen.CAE.Xyplot.BaseGridLayoutStyleSetting@endlink) GridLayoutStyleSetting
    ##   the grid layout display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return BaseGridLayoutStyleSetting
    @property
    def GridLayoutStyleSetting(self) -> BaseGridLayoutStyleSetting:
        """
        Getter for property: (@link BaseGridLayoutStyleSetting NXOpen.CAE.Xyplot.BaseGridLayoutStyleSetting@endlink) GridLayoutStyleSetting
          the grid layout display style   
            
         
        """
        pass
    
    ## Getter for property: (@link ProbingStyle NXOpen.CAE.Xyplot.ProbingStyle@endlink) ProbingStyle
    ##   the probing display style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return ProbingStyle
    @property
    def ProbingStyle(self) -> ProbingStyle:
        """
        Getter for property: (@link ProbingStyle NXOpen.CAE.Xyplot.ProbingStyle@endlink) ProbingStyle
          the probing display style   
            
         
        """
        pass
    
    ##  Gets the axis display style. 
    ##  @return axisStyle (@link IAxisStyle NXOpen.CAE.Xyplot.IAxisStyle@endlink):  Axis style .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  Axis direction 
    def GetAxisStyle(wallStyles: WallDisplayStyles, axisDirection: AxisDirection) -> IAxisStyle:
        """
         Gets the axis display style. 
         @return axisStyle (@link IAxisStyle NXOpen.CAE.Xyplot.IAxisStyle@endlink):  Axis style .
        """
        pass
    
    ## Gets the calculation legend table style 
    ##  @return legendTableStyle (@link LegendTableStyle NXOpen.CAE.Xyplot.LegendTableStyle@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCalculationLegendTableStyle(wallStyles: WallDisplayStyles) -> LegendTableStyle:
        """
        Gets the calculation legend table style 
         @return legendTableStyle (@link LegendTableStyle NXOpen.CAE.Xyplot.LegendTableStyle@endlink): .
        """
        pass
    
    ## Gets the legend table group style 
    ##  @return legendTableGroupStyle (@link LegendTableGroupStyle NXOpen.CAE.Xyplot.LegendTableGroupStyle@endlink):  Legend table group style .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLegendTableGroupStyle(wallStyles: WallDisplayStyles) -> LegendTableGroupStyle:
        """
        Gets the legend table group style 
         @return legendTableGroupStyle (@link LegendTableGroupStyle NXOpen.CAE.Xyplot.LegendTableGroupStyle@endlink):  Legend table group style .
        """
        pass
    
    ##  Gets the text style. 
    ##  @return textStyle (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink):  Text display style .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ##  Text type 
    def GetTextStyleSetting(wallStyles: WallDisplayStyles, textType: TextType) -> TextStyleSetting:
        """
         Gets the text style. 
         @return textStyle (@link TextStyleSetting NXOpen.CAE.Xyplot.TextStyleSetting@endlink):  Text display style .
        """
        pass
    
import NXOpen
##  Manages the separate graphic windows. The value of device index is greater than 0.
##             This class is restricted to being called from a program running during an interactive NX session.
##             If run from a non-interactive session it will return NULL.  <br> To obtain an instance of this class use @link NXOpen::CAE::Xyplot::XYPlotManager::WindowManager NXOpen::CAE::Xyplot::XYPlotManager::WindowManager@endlink .  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class WindowManager(NXOpen.Object): 
    """ Manages the separate graphic windows. The value of device index is greater than 0.
            This class is restricted to being called from a program running during an interactive NX session.
            If run from a non-interactive session it will return <ja_NULL>. """


    ##  Closes the window of specified device index. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##   
    @staticmethod
    def CloseWindow(deviceIndex: int) -> None:
        """
         Closes the window of specified device index. 
        """
        pass
    
    ##  Gets the graphics window title. 
    ##  @return windowTitle (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="deviceIndex"> (int) </param>
    @staticmethod
    def GetWindowTitle(deviceIndex: int) -> str:
        """
         Gets the graphics window title. 
         @return windowTitle (str): .
        """
        pass
    
    ##  Gets the device indices of all the graphic windows. 
    ##  @return deviceIndices (List[int]): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetWindows() -> List[int]:
        """
         Gets the device indices of all the graphic windows. 
         @return deviceIndices (List[int]): .
        """
        pass
    
    ##  Creates a new window and returns the device index. 
    ##  @return deviceIndex (int):   .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewWindow() -> int:
        """
         Creates a new window and returns the device index. 
         @return deviceIndex (int):   .
        """
        pass
    
    ##  Sets the graphics window title. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="deviceIndex"> (int) </param>
    ## <param name="windowTitle"> (str) </param>
    def SetWindowTitle(deviceIndex: int, windowTitle: str) -> None:
        """
         Sets the graphics window title. 
        """
        pass
    
##   @brief  Represents a data accessor to retrieve data of a function which is plotted in 2D graphs or Color Bar graphs.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class XYFunctionDataAccessor(IFunctionDataAccessor): 
    """ <summary> Represents a data accessor to retrieve data of a function which is plotted in 2D graphs or Color Bar graphs. </summary> """


    ##  Asks display data. 
    ##  @return A tuple consisting of (indenpendentValue, dependentValue). 
    ##  - indenpendentValue is: List[float].
    ##  - dependentValue is: List[float].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskDisplayData(xYFunctionDataAccessor: XYFunctionDataAccessor) -> Tuple[List[float], List[float]]:
        """
         Asks display data. 
         @return A tuple consisting of (indenpendentValue, dependentValue). 
         - indenpendentValue is: List[float].
         - dependentValue is: List[float].

        """
        pass
    
import NXOpen
##  XYPlot function manager  <br> To obtain an instance of this class use @link NXOpen::Session::XYPlotManager NXOpen::Session::XYPlotManager@endlink .  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class XYPlotManager(NXOpen.Object): 
    """ XYPlot function manager """


    ## Getter for property: (@link Preference NXOpen.CAE.Xyplot.Preference@endlink) Preference
    ##   the preference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return Preference
    @property
    def Preference(self) -> Preference:
        """
        Getter for property: (@link Preference NXOpen.CAE.Xyplot.Preference@endlink) Preference
          the preference   
            
         
        """
        pass
    
    ## Getter for property: (@link BaseTemplateManager NXOpen.CAE.Xyplot.BaseTemplateManager@endlink) TemplateManager
    ##   the template manager.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return BaseTemplateManager
    @property
    def TemplateManager(self) -> BaseTemplateManager:
        """
        Getter for property: (@link BaseTemplateManager NXOpen.CAE.Xyplot.BaseTemplateManager@endlink) TemplateManager
          the template manager.  
             
         
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::Xyplot::WindowManager NXOpen::CAE::Xyplot::WindowManager@endlink  belonging.
    ##                 This class is restricted to being called from a program running during an interactive NX session.
    ##                 If run from a non-interactive session it will return NULL. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @link WindowManager NXOpen.CAE.Xyplot.WindowManager@endlink
    @property
    def WindowManager() -> WindowManager:
        """
         Returns the @link NXOpen::CAE::Xyplot::WindowManager NXOpen::CAE::Xyplot::WindowManager@endlink  belonging.
                        This class is restricted to being called from a program running during an interactive NX session.
                        If run from a non-interactive session it will return NULL. 
        """
        pass
    
    ##  Returns the @link NXOpen::CAE::Xyplot::DataExporter NXOpen::CAE::Xyplot::DataExporter@endlink  belonging. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link DataExporter NXOpen.CAE.Xyplot.DataExporter@endlink
    @property
    def DataExporter() -> DataExporter:
        """
         Returns the @link NXOpen::CAE::Xyplot::DataExporter NXOpen::CAE::Xyplot::DataExporter@endlink  belonging. 
        """
        pass
    
    ##  This is an internal API and can be changed at any time 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link AutotestUtils NXOpen.CAE.Xyplot.AutotestUtils@endlink
    @property
    def AutotestUtils() -> AutotestUtils:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    
    ##  Aligns axes of all plots. 
    ##                 Ensures that all axes of a certain quantity (force, displacement, etc.) and 
    ##                 data type (real, imaginary, magnitude, etc.) have the same unit, axis type and limits. 
    ##                 This API only valid for Motion and Pre/post application
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    @staticmethod
    def AlignAxesOfPlots(part: NXOpen.BasePart) -> None:
        """
         Aligns axes of all plots. 
                        Ensures that all axes of a certain quantity (force, displacement, etc.) and 
                        data type (real, imaginary, magnitude, etc.) have the same unit, axis type and limits. 
                        This API only valid for Motion and Pre/post application
        """
        pass
    
    ##  Creates a new @link NXOpen::CAE::Xyplot::ResultAccessor NXOpen::CAE::Xyplot::ResultAccessor@endlink  object.
    ##  @return accessor (@link ResultAccessor NXOpen.CAE.Xyplot.ResultAccessor@endlink):   .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="plot"> (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) </param>
    def CreateResultAccessor(plot: Plot) -> ResultAccessor:
        """
         Creates a new @link NXOpen::CAE::Xyplot::ResultAccessor NXOpen::CAE::Xyplot::ResultAccessor@endlink  object.
         @return accessor (@link ResultAccessor NXOpen.CAE.Xyplot.ResultAccessor@endlink):   .
        """
        pass
    
    ##   @brief Creates a new @link NXOpen::CAE::Xyplot::ResultAccessor NXOpen::CAE::Xyplot::ResultAccessor@endlink  object. 
    ## 
    ##  
    ## 
    ##                 
    ##                 Plots may have one or more canvases. Commonly, there is only one canvas that contains multiple graphs. But there are plots --such as stacked plots-- 
    ##                 that have multiple canvases. The number of graphs per canvas depends on display options.
    ##                 
    ##               
    ##  @return accessor (@link ResultAccessor NXOpen.CAE.Xyplot.ResultAccessor@endlink):   .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  The canvas index whose data you want to access. If unsure, pass 0 
    def CreateResultAccessorOnCanvas(plot: Plot, canvasIndex: int) -> ResultAccessor:
        """
          @brief Creates a new @link NXOpen::CAE::Xyplot::ResultAccessor NXOpen::CAE::Xyplot::ResultAccessor@endlink  object. 
        
         
        
                        
                        Plots may have one or more canvases. Commonly, there is only one canvas that contains multiple graphs. But there are plots --such as stacked plots-- 
                        that have multiple canvases. The number of graphs per canvas depends on display options.
                        
                      
         @return accessor (@link ResultAccessor NXOpen.CAE.Xyplot.ResultAccessor@endlink):   .
        """
        pass
    
    ##  Finds the @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  with the given identifier as recorded in a journal
    ##  @return plot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Plot object found, or null if no such plot exists .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Identifier of the @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  to be found 
    @staticmethod
    def FindObject(journalIdentifier: str) -> Plot:
        """
         Finds the @link CAE::Xyplot::Plot CAE::Xyplot::Plot@endlink  with the given identifier as recorded in a journal
         @return plot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Plot object found, or null if no such plot exists .
        """
        pass
    
    ##  Gets all window devices on which XY graph could be plotted 
    ##  @return pWinDevices (List[int]):  Available Plot Winodw Devices .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAvailableWindowDevices() -> List[int]:
        """
         Gets all window devices on which XY graph could be plotted 
         @return pWinDevices (List[int]):  Available Plot Winodw Devices .
        """
        pass
    
    ##  Gets the current plot on the view port of specific device 
    ##  @return currentPlot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Current plot .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Device index 
    def GetCurrentPlot(deviceIndex: int, viewIndex: int) -> Plot:
        """
         Gets the current plot on the view port of specific device 
         @return currentPlot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Current plot .
        """
        pass
    
    ##  Gets all plots on a view of specified window device 
    ##  @return plots (@link Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Plots      .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##   Plot index 
    def GetPlots(windowDevice: int, view: int) -> List[Plot]:
        """
         Gets all plots on a view of specified window device 
         @return plots (@link Plot List[NXOpen.CAE.Xyplot.Plot]@endlink):  Plots      .
        """
        pass
    
    ##  Gets view count and views for specified window device 
    ##  @return pViewsOnDevice (List[int]):  the views on window device.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##   window index  
    @staticmethod
    def GetWindowDevicesViews(windowDevice: int) -> List[int]:
        """
         Gets view count and views for specified window device 
         @return pViewsOnDevice (List[int]):  the views on window device.
        """
        pass
    
    ##  Turns the page of the given plot as current page. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="plot"> (@link Plot NXOpen.CAE.Xyplot.Plot@endlink) </param>
    @staticmethod
    def MakeCurrentPlot(plot: Plot) -> None:
        """
         Turns the page of the given plot as current page. 
        """
        pass
    
    ##  Creates an transient object @link  NXOpen::CAE::Xyplot::PlotParameters   NXOpen::CAE::Xyplot::PlotParameters @endlink  to contain the settings
    ##                 required by overlaying new records on a plot. The object should be destroyed after overlaying plot is created. 
    ##  @return overlayParameters (@link OverlayParameters NXOpen.CAE.Xyplot.OverlayParameters@endlink):  the overlay parameters object created .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewOverlayParameters() -> OverlayParameters:
        """
         Creates an transient object @link  NXOpen::CAE::Xyplot::PlotParameters   NXOpen::CAE::Xyplot::PlotParameters @endlink  to contain the settings
                        required by overlaying new records on a plot. The object should be destroyed after overlaying plot is created. 
         @return overlayParameters (@link OverlayParameters NXOpen.CAE.Xyplot.OverlayParameters@endlink):  the overlay parameters object created .
        """
        pass
    
    ##  Creates an transient object @link  NXOpen::CAE::Xyplot::PlotParameters   NXOpen::CAE::Xyplot::PlotParameters @endlink  to contain the
    ##                 settings required by creating a plot. The object should be destroyed after plot is created. 
    ##  @return plotParameters (@link PlotParameters NXOpen.CAE.Xyplot.PlotParameters@endlink):  the plot parameters object created .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewPlotParameters() -> PlotParameters:
        """
         Creates an transient object @link  NXOpen::CAE::Xyplot::PlotParameters   NXOpen::CAE::Xyplot::PlotParameters @endlink  to contain the
                        settings required by creating a plot. The object should be destroyed after plot is created. 
         @return plotParameters (@link PlotParameters NXOpen.CAE.Xyplot.PlotParameters@endlink):  the plot parameters object created .
        """
        pass
    
    ##  Overlay records with given parameters 
    ##  @return plot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Overlayed plot .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  the overlay parameters 
    @staticmethod
    def OverlayRecords(overlayParameters: OverlayParameters) -> Plot:
        """
         Overlay records with given parameters 
         @return plot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Overlayed plot .
        """
        pass
    
    ##  Creates plot with given parameters 
    ##  @return plot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Created plot .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  the plot parameters 
    @staticmethod
    def PlotRecords(plotParameters: PlotParameters) -> Plot:
        """
         Creates plot with given parameters 
         @return plot (@link Plot NXOpen.CAE.Xyplot.Plot@endlink):  Created plot .
        """
        pass
    
    ##  Clears all plots on a view of main graphics windows and returns to model view
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ##   View index 
    @staticmethod
    def ReturnToModelView(view: int) -> None:
        """
         Clears all plots on a view of main graphics windows and returns to model view
        """
        pass
    
    ##  Shows the next plot on the view port of specific device 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Device index 
    def ShowNextPlot(deviceIndex: int, viewIndex: int) -> None:
        """
         Shows the next plot on the view port of specific device 
        """
        pass
    
    ##  Shows the previous plot on the view port of specific device 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ##  Device index 
    def ShowPreviousPlot(deviceIndex: int, viewIndex: int) -> None:
        """
         Shows the previous plot on the view port of specific device 
        """
        pass
    
    ##  Write the image of current plot on a view to Windows's ClipBoard
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  Device index 
    def WriteImageToClipBoard(deviceIndex: int, viewIndex: int, isUseWhiteBackGround: bool) -> None:
        """
         Write the image of current plot on a view to Windows's ClipBoard
        """
        pass
    
##   @brief  Represents a data accessor to retrieve data of a function which is plotted in 3D graphs or Color Map graphs.  
## 
##   
## 
##   <br>  Created in NX1899.0.0  <br> 

class XYZFunctionDataAccessor(IFunctionDataAccessor): 
    """ <summary> Represents a data accessor to retrieve data of a function which is plotted in 3D graphs or Color Map graphs. </summary> """


    ##  Asks section count. 
    ##  @return sectionCount (int): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AskSectionCount(xYZFunctionDataAccessor: XYZFunctionDataAccessor) -> int:
        """
         Asks section count. 
         @return sectionCount (int): .
        """
        pass
    
    ##  Asks display data. 
    ##  @return A tuple consisting of (indenpendent1Values, indenpendent2Value, dependentValues). 
    ##  - indenpendent1Values is: List[float].
    ##  - indenpendent2Value is: float.
    ##  - dependentValues is: List[float].

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionIndex"> (int) </param>
    @staticmethod
    def AskSectionDisplayData(xYZFunctionDataAccessor: XYZFunctionDataAccessor, sectionIndex: int) -> Tuple[List[float], float, List[float]]:
        """
         Asks display data. 
         @return A tuple consisting of (indenpendent1Values, indenpendent2Value, dependentValues). 
         - indenpendent1Values is: List[float].
         - indenpendent2Value is: float.
         - dependentValues is: List[float].

        """
        pass
    
## @package NXOpen.CAE.Xyplot
## Classes, Enums and Structs under NXOpen.CAE.Xyplot namespace

##  @link PreferenceDropActionOption NXOpen.CAE.Xyplot.PreferenceDropActionOption @endlink is an alias for @link Preference.DropActionOption NXOpen.CAE.Xyplot.Preference.DropActionOption@endlink
PreferenceDropActionOption = Preference.DropActionOption


##  @link PreferenceNewWindowChoice NXOpen.CAE.Xyplot.PreferenceNewWindowChoice @endlink is an alias for @link Preference.NewWindowChoice NXOpen.CAE.Xyplot.Preference.NewWindowChoice@endlink
PreferenceNewWindowChoice = Preference.NewWindowChoice


##  @link PreferenceTargetGraphicWindowOption NXOpen.CAE.Xyplot.PreferenceTargetGraphicWindowOption @endlink is an alias for @link Preference.TargetGraphicWindowOption NXOpen.CAE.Xyplot.Preference.TargetGraphicWindowOption@endlink
PreferenceTargetGraphicWindowOption = Preference.TargetGraphicWindowOption


##  @link SourceDataExportParametersComplextDataSaveOption NXOpen.CAE.Xyplot.SourceDataExportParametersComplextDataSaveOption @endlink is an alias for @link SourceDataExportParameters.ComplextDataSaveOption NXOpen.CAE.Xyplot.SourceDataExportParameters.ComplextDataSaveOption@endlink
SourceDataExportParametersComplextDataSaveOption = SourceDataExportParameters.ComplextDataSaveOption


