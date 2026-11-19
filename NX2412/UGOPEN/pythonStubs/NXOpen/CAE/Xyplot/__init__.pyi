from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AnchorType(Enum):
    """
    Members Include: 
     |NotSet|  the normal marker without anchor type 
     |Start|  the position of start point in a record display 
     |End|  the position of end point in a record display 
     |MaximumValue|  the position of the point which has maximum value in a record display 
     |MinimumValue|  the position of the point which has minimum value in a record display 
     |AbsPercentage|  the position of the point in the set abscissa percentage 

    """
    NotSet: int
    Start: int
    End: int
    MaximumValue: int
    MinimumValue: int
    AbsPercentage: int
    @staticmethod
    def ValueOf(value: int) -> AnchorType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AngleAxisStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the angle axis display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def AngleUnit(self) -> AngleUnit:
        """
        Getter for property: ( AngleUnit NXOpen.C) AngleUnit
         Returns the angle axis number unit   
            
         
        """
        pass
    @AngleUnit.setter
    def AngleUnit(self, unit: AngleUnit):
        """
        Setter for property: ( AngleUnit NXOpen.C) AngleUnit
         Returns the angle axis number unit   
            
         
        """
        pass
    @property
    def LineDisplaySettings(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) LineDisplaySettings
         Returns the angle axis lines display styles   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
class AngleUnit(Enum):
    """
    Members Include: 
     |Degree|  Display angle in degree unit 
     |Radian|  Display angle in radian unit 
     |Rev|  Display angle in rev unit 

    """
    Degree: int
    Radian: int
    Rev: int
    @staticmethod
    def ValueOf(value: int) -> AngleUnit:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Argand3DFunctionDataAccessor(IFunctionDataAccessor): 
    """  Represents a data accessor to retrieve data of a function which is plotted in 3D Argand graphs.  """
    def AskDisplayData(self) -> Tuple[List[float], List[float], List[float]]:
        """
         Asks display data. 
         Returns A tuple consisting of (dependentValues, indenpendent1Values, indenpendent2Values). 
         - dependentValues is: List[float].
         - indenpendent1Values is: List[float].
         - indenpendent2Values is: List[float].

        """
        pass
import NXOpen.CAE
import NXOpen.CAE.FTK
class ArgumentAxisStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the argument axis display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def RangeAuto(self) -> bool:
        """
        Getter for property: (bool) RangeAuto
         Returns a value indicating whether to set axis range automatically   
            
         
        """
        pass
    @RangeAuto.setter
    def RangeAuto(self, rangeAutomation: bool):
        """
        Setter for property: (bool) RangeAuto
         Returns a value indicating whether to set axis range automatically   
            
         
        """
        pass
    @property
    def UnitSystemType(self) -> NXOpen.CAE.XyFunctionUnitSystem:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionUnitSystem) UnitSystemType
         Returns the unit system type  
            
         
        """
        pass
    @UnitSystemType.setter
    def UnitSystemType(self, unitSystemType: NXOpen.CAE.XyFunctionUnitSystem):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionUnitSystem) UnitSystemType
         Returns the unit system type  
            
         
        """
        pass
    def GetCustomerRange(self) -> List[int]:
        """
         Gets the customer indices 
         Returns customerIndices (List[int]):  Customer range .
        """
        pass
    def GetDisplayUnit(self) -> NXOpen.CAE.FTK.BaseUnit:
        """
         Gets display unit
         Returns dispUnit ( NXOpen.CAE.FTK.BaseUnit): .
        """
        pass
    def GetIndicesOfLabel(self, itemLabel: str) -> List[int]:
        """
         Gets the indices of label 
         Returns labelIndices (List[int]):  Customer range .
        """
        pass
    def GetNthItemLabel(self, nth: int) -> str:
        """
         Gets nth item label 
         Returns nthItemLabel (str):    .
        """
        pass
    def LogUnitChangedEvent(self) -> None:
        """
         Logs an update event for changing display unit before committing AxisStyleSetting change.
        """
        pass
    def SetCustomerIndices(self, customerIndices: List[int]) -> None:
        """
         Sets the customer indices 
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class AxisAccessor(NXOpen.TransientObject): 
    """  Represents a data accessor to retrieve axis data.  """
    @property
    def AxisType(self) -> AxisType:
        """
        Getter for property: ( AxisType NXOpen.C) AxisType
         Returns the axis type.  
             
         
        """
        pass
    @property
    def Unit(self) -> NXOpen.CAE.FTK.BaseUnit:
        """
        Getter for property: ( NXOpen.CAE.FTK.BaseUnit) Unit
         Returns the axis unit.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
    def GetLabel(self) -> List[str]:
        """
         Gets the axis labels. 
         Returns axisLabels (List[str]): .
        """
        pass
class AxisDBScale(Enum):
    """
    Members Include: 
     |Ten|  Db 10 
     |Twenty|  Db 20 

    """
    Ten: int
    Twenty: int
    @staticmethod
    def ValueOf(value: int) -> AxisDBScale:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AxisDirection(Enum):
    """
    Members Include: 
     |X|  X-axis 
     |Y|  Y-axis 
     |Z|  Z-axis 

    """
    X: int
    Y: int
    Z: int
    @staticmethod
    def ValueOf(value: int) -> AxisDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AxisItemStyle(TextStyleSetting): 
    """ Represents the axis item display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def MaximumCharacterCount(self) -> int:
        """
        Getter for property: (int) MaximumCharacterCount
         Returns the maximum character count.  
           The minimum value is 1.   
         
        """
        pass
    @MaximumCharacterCount.setter
    def MaximumCharacterCount(self, maximumCharacterCount: int):
        """
        Setter for property: (int) MaximumCharacterCount
         Returns the maximum character count.  
           The minimum value is 1.   
         
        """
        pass
    @property
    def TruncationDirection(self) -> AxisItemTruncationDirection:
        """
        Getter for property: ( AxisItemTruncationDirection NXOpen.C) TruncationDirection
         Returns the truncation direction   
            
         
        """
        pass
    @TruncationDirection.setter
    def TruncationDirection(self, truncationDirection: AxisItemTruncationDirection):
        """
        Setter for property: ( AxisItemTruncationDirection NXOpen.C) TruncationDirection
         Returns the truncation direction   
            
         
        """
        pass
class AxisItemTruncationDirection(Enum):
    """
    Members Include: 
     |End|  If string length exceeds maximum character count, truncating the end of string 
     |Beginning|  If string length exceeds maximum character count, truncating the beginning of string 

    """
    End: int
    Beginning: int
    @staticmethod
    def ValueOf(value: int) -> AxisItemTruncationDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AxisLabelStyle(CustomTextStyleSetting): 
    """ Represents the axis label display style. Call CAE.Xyplot.IDisplayStyle.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def IncludeMeasureType(self) -> bool:
        """
        Getter for property: (bool) IncludeMeasureType
         Returns the option specifies whether to include measure type in axis label   
            
         
        """
        pass
    @IncludeMeasureType.setter
    def IncludeMeasureType(self, hasIncludeMeasureType: bool):
        """
        Setter for property: (bool) IncludeMeasureType
         Returns the option specifies whether to include measure type in axis label   
            
         
        """
        pass
    @property
    def IncludeUnit(self) -> bool:
        """
        Getter for property: (bool) IncludeUnit
         Returns the option specifies whether to include unit information in axis label   
            
         
        """
        pass
    @IncludeUnit.setter
    def IncludeUnit(self, hasIncludeUnit: bool):
        """
        Setter for property: (bool) IncludeUnit
         Returns the option specifies whether to include unit information in axis label   
            
         
        """
        pass
    @property
    def UseSingleLine(self) -> bool:
        """
        Getter for property: (bool) UseSingleLine
         Returns the option specifies whether to display axis label in a single line   
            
         
        """
        pass
    @UseSingleLine.setter
    def UseSingleLine(self, isSingleLine: bool):
        """
        Setter for property: (bool) UseSingleLine
         Returns the option specifies whether to display axis label in a single line   
            
         
        """
        pass
class AxisModel(BasicModel): 
    """ Represents an axis model object on a XY graphing. """
    def CalculateZoomScale(self, newStartDisplayLimit: float, newEndDisplayLimit: float) -> Tuple[float, float]:
        """
         Gives expected display limits to calculate a zoom scale range which could be used by CAE.Xyplot.Graph for zooming operation.
                        the new display limits must be less than the original display limits returned by CAE.Xyplot.AxisModel.GetDisplayLimits
         Returns A tuple consisting of (startScale, endScale). 
         - startScale is: float.
         - endScale is: float.

        """
        pass
    def GetDisplayLimits(self) -> Tuple[float, float]:
        """
         Gets the display limit values in display unit 
         Returns A tuple consisting of (startDisplayLimit, endDisplayLimit). 
         - startDisplayLimit is: float.
         - endDisplayLimit is: float.

        """
        pass
import NXOpen.CAE
import NXOpen.CAE.FTK
class AxisStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the axis display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def AxisType(self) -> AxisType:
        """
        Getter for property: ( AxisType NXOpen.C) AxisType
         Returns the axis scale type   
            
         
        """
        pass
    @AxisType.setter
    def AxisType(self, axisType: AxisType):
        """
        Setter for property: ( AxisType NXOpen.C) AxisType
         Returns the axis scale type   
            
         
        """
        pass
    @property
    def GraphOverhead(self) -> int:
        """
        Getter for property: (int) GraphOverhead
         Returns the round value to display.  
           It is a percent value. Avaliable when  CAE::Xyplot::AxisStyleSetting::AxisType 
                        is not  CAE::Xyplot::AxisTypeAuto .   
         
        """
        pass
    @GraphOverhead.setter
    def GraphOverhead(self, graphOverhead: int):
        """
        Setter for property: (int) GraphOverhead
         Returns the round value to display.  
           It is a percent value. Avaliable when  CAE::Xyplot::AxisStyleSetting::AxisType 
                        is not  CAE::Xyplot::AxisTypeAuto .   
         
        """
        pass
    @property
    def LimitsType(self) -> LimitsType:
        """
        Getter for property: ( LimitsType NXOpen.C) LimitsType
         Returns the limits type  
            
         
        """
        pass
    @LimitsType.setter
    def LimitsType(self, limitsType: LimitsType):
        """
        Setter for property: ( LimitsType NXOpen.C) LimitsType
         Returns the limits type  
            
         
        """
        pass
    @property
    def LogDecades(self) -> int:
        """
        Getter for property: (int) LogDecades
         Returns the number of Log decades to display.  
           Avaliable when  CAE::Xyplot::AxisStyleSetting::AxisType 
                        is  CAE::Xyplot::AxisTypeLog .   
         
        """
        pass
    @LogDecades.setter
    def LogDecades(self, logDecades: int):
        """
        Setter for property: (int) LogDecades
         Returns the number of Log decades to display.  
           Avaliable when  CAE::Xyplot::AxisStyleSetting::AxisType 
                        is  CAE::Xyplot::AxisTypeLog .   
         
        """
        pass
    @property
    def UnitSystemType(self) -> NXOpen.CAE.XyFunctionUnitSystem:
        """
        Getter for property: ( NXOpen.CAE.XyFunctionUnitSystem) UnitSystemType
         Returns the unit system type  
            
         
        """
        pass
    @UnitSystemType.setter
    def UnitSystemType(self, unitSystemType: NXOpen.CAE.XyFunctionUnitSystem):
        """
        Setter for property: ( NXOpen.CAE.XyFunctionUnitSystem) UnitSystemType
         Returns the unit system type  
            
         
        """
        pass
    @property
    def UseAbsoluteValue(self) -> bool:
        """
        Getter for property: (bool) UseAbsoluteValue
         Returns the option indicates whether to use absolute value.  
           This option is only valid for Y-Axis and color axis.  
         
        """
        pass
    @UseAbsoluteValue.setter
    def UseAbsoluteValue(self, useAbsValue: bool):
        """
        Setter for property: (bool) UseAbsoluteValue
         Returns the option indicates whether to use absolute value.  
           This option is only valid for Y-Axis and color axis.  
         
        """
        pass
    def GetDBSettings(self) -> NXOpen.CAE.SignalProcessingDBSettings:
        """
         Gets the dB settings 
         Returns dBSettings ( NXOpen.CAE.SignalProcessingDBSettings): .
        """
        pass
    def GetDisplayUnit(self) -> NXOpen.CAE.FTK.BaseUnit:
        """
         Gets display unit
         Returns dispUnit ( NXOpen.CAE.FTK.BaseUnit): .
        """
        pass
    def GetFixedLimits(self) -> Tuple[float, float]:
        """
         Gets the fixed limits
         Returns A tuple consisting of (lowerLimit, upperLimit). 
         - lowerLimit is: float.  .
         - upperLimit is: float.  .

        """
        pass
    def LogUnitChangedEvent(self) -> None:
        """
         Logs an update event for changing display unit before committing AxisStyleSetting change.
        """
        pass
    def SetFixedLimits(self, lowerLimit: float, upperLimit: float) -> None:
        """
         Sets the fixed limits
        """
        pass
class AxisType(Enum):
    """
    Members Include: 
     |Auto|  Automatic type 
     |Linear|  Linear type 
     |Log|  Log type 
     |Db|  Db type 
     |Octave|  Octave type 
     |OneThirdOctave|  13 Octave type 
     |OneTwelfthOctave|  112 Octave type 

    """
    Auto: int
    Linear: int
    Log: int
    Db: int
    Octave: int
    OneThirdOctave: int
    OneTwelfthOctave: int
    @staticmethod
    def ValueOf(value: int) -> AxisType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AxisYStyleSetting(AxisStyleSetting): 
    """ Represents the axis y display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def BarLowerLimit(self) -> bool:
        """
        Getter for property: (bool) BarLowerLimit
         Returns the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y   
            
         
        """
        pass
    @BarLowerLimit.setter
    def BarLowerLimit(self, barLowerLimit: bool):
        """
        Setter for property: (bool) BarLowerLimit
         Returns the bar lower limit indicating whether a bar is plotted from minimum or zero position of axis y   
            
         
        """
        pass
class BarChartFunctionDataAccessor(IFunctionDataAccessor): 
    """  Represents a data accessor to retrieve data of a function which is plotted in BarChart graphs.  """
    def AskDisplayData(self) -> Tuple[List[float], List[float]]:
        """
         Asks display data. 
         Returns A tuple consisting of (indenpendentValues, dependentValues). 
         - indenpendentValues is: List[float].
         - dependentValues is: List[float].

        """
        pass
    def AskPointLabels(self) -> List[str]:
        """
         Asks point labels. 
         Returns pointLabels (List[str]): .
        """
        pass
class BarChartPlot(Plot): 
    """ 
        Manages the display of bar chart plot.
        
        Call CAE.Xyplot.I2DDataPlot.EditRecord to edit data for this class.
         """
    pass
import NXOpen
class BarChartStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the bar chart display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FillingColor
         Returns the filling color   
            
         
        """
        pass
    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FillingColor
         Returns the filling color   
            
         
        """
        pass
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OutlineColor
         Returns the outline color   
            
         
        """
        pass
    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OutlineColor
         Returns the outline color   
            
         
        """
        pass
    @property
    def PointMarkerIdx(self) -> PointMarker:
        """
        Getter for property: ( PointMarker NXOpen.C) PointMarkerIdx
         Returns the point marker   
            
         
        """
        pass
    @PointMarkerIdx.setter
    def PointMarkerIdx(self, pointMarker: PointMarker):
        """
        Setter for property: ( PointMarker NXOpen.C) PointMarkerIdx
         Returns the point marker   
            
         
        """
        pass
    @property
    def ShowOutline(self) -> bool:
        """
        Getter for property: (bool) ShowOutline
         Returns the outline visibility   
            
         
        """
        pass
    @ShowOutline.setter
    def ShowOutline(self, showOutline: bool):
        """
        Setter for property: (bool) ShowOutline
         Returns the outline visibility   
            
         
        """
        pass
    @property
    def ShowText(self) -> bool:
        """
        Getter for property: (bool) ShowText
         Returns the text visibility   
            
         
        """
        pass
    @ShowText.setter
    def ShowText(self, showText: bool):
        """
        Setter for property: (bool) ShowText
         Returns the text visibility   
            
         
        """
        pass
    @property
    def SpaceBetweenTextAndBar(self) -> int:
        """
        Getter for property: (int) SpaceBetweenTextAndBar
         Returns the spaces between text and bar measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    @SpaceBetweenTextAndBar.setter
    def SpaceBetweenTextAndBar(self, spaceBetweenTextAndBar: int):
        """
        Setter for property: (int) SpaceBetweenTextAndBar
         Returns the spaces between text and bar measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
class BarColorOption(Enum):
    """
    Members Include: 
     |Fill|  Fill color or contour color with no shading 
     |Hidden|  Background color as fill 
     |Shaded|  Fill Color or contour color with shading 

    """
    Fill: int
    Hidden: int
    Shaded: int
    @staticmethod
    def ValueOf(value: int) -> BarColorOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class BarStyle2DSetting(BaseBarStyleSetting): 
    """ Represents the 2d bar display style. """
    @property
    def ConstantWidth(self) -> float:
        """
        Getter for property: (float) ConstantWidth
         Returns the constant bar width.  
           The range is from 0.05 to 100.   
         
        """
        pass
    @ConstantWidth.setter
    def ConstantWidth(self, constBarWidth: float):
        """
        Setter for property: (float) ConstantWidth
         Returns the constant bar width.  
           The range is from 0.05 to 100.   
         
        """
        pass
    @property
    def ShowConstantWidth(self) -> bool:
        """
        Getter for property: (bool) ShowConstantWidth
         Returns a value indicating whether to set bar width as constant   
            
         
        """
        pass
    @ShowConstantWidth.setter
    def ShowConstantWidth(self, showConstBarWidth: bool):
        """
        Setter for property: (bool) ShowConstantWidth
         Returns a value indicating whether to set bar width as constant   
            
         
        """
        pass
class BarStyle3DSetting(BaseBarStyleSetting): 
    """ Represents the 3d bar display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def ColorOption(self) -> BarColorOption:
        """
        Getter for property: ( BarColorOption NXOpen.C) ColorOption
         Returns the filling color option   
            
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: BarColorOption):
        """
        Setter for property: ( BarColorOption NXOpen.C) ColorOption
         Returns the filling color option   
            
         
        """
        pass
    @property
    def Depth(self) -> int:
        """
        Getter for property: (int) Depth
         Returns the bar depth.  
           The range is from 0 to 100.   
         
        """
        pass
    @Depth.setter
    def Depth(self, barDepth: int):
        """
        Setter for property: (int) Depth
         Returns the bar depth.  
           The range is from 0 to 100.   
         
        """
        pass
import NXOpen
class BaseBarStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the base bar display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FillingColor
         Returns the filling color   
            
         
        """
        pass
    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FillingColor
         Returns the filling color   
            
         
        """
        pass
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OutlineColor
         Returns the outline color   
            
         
        """
        pass
    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OutlineColor
         Returns the outline color   
            
         
        """
        pass
    @property
    def ShowOutline(self) -> bool:
        """
        Getter for property: (bool) ShowOutline
         Returns a value indicating whether to display the outline   
            
         
        """
        pass
    @ShowOutline.setter
    def ShowOutline(self, showOutline: bool):
        """
        Setter for property: (bool) ShowOutline
         Returns a value indicating whether to display the outline   
            
         
        """
        pass
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
         Returns the bar width.  
           The range is from 0 to 100.   
         
        """
        pass
    @Width.setter
    def Width(self, barWidth: int):
        """
        Setter for property: (int) Width
         Returns the bar width.  
           The range is from 0 to 100.   
         
        """
        pass
import NXOpen
class BaseDisplayStyleSetting(NXOpen.TaggedObject): 
    """ Represent an abstract object on display style. """
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
                    This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Owner(self) -> IDisplayStyle:
        """
        Getter for property: ( IDisplayStyle NXOpen.C) Owner
         Returns the owner style   
            
         
        """
        pass
    def Find(self, journal_identifier: str) -> NXOpen.TaggedObject:
        """
         Finds the  NXOpen.TaggedObject  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.TaggedObject):  .
        """
        pass
import NXOpen
class BaseGridLayoutStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the base grid layout display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def BackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BackgroundColor
         Returns the background color   
            
         
        """
        pass
    @BackgroundColor.setter
    def BackgroundColor(self, bGcolor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BackgroundColor
         Returns the background color   
            
         
        """
        pass
    @property
    def ColorOfBackgroundPlane(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ColorOfBackgroundPlane
         Returns the color of grid background plane  
            
         
        """
        pass
    @ColorOfBackgroundPlane.setter
    def ColorOfBackgroundPlane(self, bGcolor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ColorOfBackgroundPlane
         Returns the color of grid background plane  
            
         
        """
        pass
    @property
    def ContouringLevel(self) -> int:
        """
        Getter for property: (int) ContouringLevel
         Returns the contouring level.  
           The value is greater than 0.   
         
        """
        pass
    @ContouringLevel.setter
    def ContouringLevel(self, contouringLevel: int):
        """
        Setter for property: (int) ContouringLevel
         Returns the contouring level.  
           The value is greater than 0.   
         
        """
        pass
    @property
    def ContouringRange(self) -> ContouringRange:
        """
        Getter for property: ( ContouringRange NXOpen.C) ContouringRange
         Returns the option to show contour range either on the border or the faces of the grid.  
             
         
        """
        pass
    @ContouringRange.setter
    def ContouringRange(self, contouringRange: ContouringRange):
        """
        Setter for property: ( ContouringRange NXOpen.C) ContouringRange
         Returns the option to show contour range either on the border or the faces of the grid.  
             
         
        """
        pass
    @property
    def DenseGridDisplayStyleSettings(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) DenseGridDisplayStyleSettings
         Returns the dense grid display style   
            
         
        """
        pass
    @property
    def DisplayContouring(self) -> bool:
        """
        Getter for property: (bool) DisplayContouring
         Returns a value indicating whether to display contouring   
            
         
        """
        pass
    @DisplayContouring.setter
    def DisplayContouring(self, dispContouring: bool):
        """
        Setter for property: (bool) DisplayContouring
         Returns a value indicating whether to display contouring   
            
         
        """
        pass
    @property
    def MajorGridDisplayStyleSettings(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) MajorGridDisplayStyleSettings
         Returns the major grid display style   
            
         
        """
        pass
    @property
    def ShowBackground(self) -> bool:
        """
        Getter for property: (bool) ShowBackground
         Returns a value indicating whether to display the background   
            
         
        """
        pass
    @ShowBackground.setter
    def ShowBackground(self, showBg: bool):
        """
        Setter for property: (bool) ShowBackground
         Returns a value indicating whether to display the background   
            
         
        """
        pass
    @property
    def ShowBackgroundPlane(self) -> bool:
        """
        Getter for property: (bool) ShowBackgroundPlane
         Returns a value indicating whether to display the grid background plane   
            
         
        """
        pass
    @ShowBackgroundPlane.setter
    def ShowBackgroundPlane(self, showBg: bool):
        """
        Setter for property: (bool) ShowBackgroundPlane
         Returns a value indicating whether to display the grid background plane   
            
         
        """
        pass
    @property
    def TicksDisplayStyleSettings(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) TicksDisplayStyleSettings
         Returns the ticks display style   
            
         
        """
        pass
    @property
    def XyGridStyle(self) -> GridStyle:
        """
        Getter for property: ( GridStyle NXOpen.C) XyGridStyle
         Returns the grid style of XY plane   
            
         
        """
        pass
    @XyGridStyle.setter
    def XyGridStyle(self, gridStyle: GridStyle):
        """
        Setter for property: ( GridStyle NXOpen.C) XyGridStyle
         Returns the grid style of XY plane   
            
         
        """
        pass
import NXOpen
class BaseLineStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the base line display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the line color  
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the line color  
            
         
        """
        pass
    @property
    def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) Font
         Returns the line font   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) Font
         Returns the line font   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) Width
         Returns the line width  
            
         
        """
        pass
    @Width.setter
    def Width(self, lineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) Width
         Returns the line width  
            
         
        """
        pass
import NXOpen
class BaseModel(NXOpen.NXObject): 
    """ Represents an abstract component object on a XY graphing. """
    @property
    def StyleSetting(self) -> BaseDisplayStyleSetting:
        """
        Getter for property: ( BaseDisplayStyleSetting NXOpen.C) StyleSetting
         Returns the style setting associated to the model   
            
         
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class BasePlotParameters(NXOpen.TransientObject): 
    """ Represents the parameters passed to create or modify a plot. """
    @property
    def DeviceIndex(self) -> int:
        """
        Getter for property: (int) DeviceIndex
         Returns the index of device on which plot graph will be shown.  
          
                        A value of 1 represents the main graphic window,
                        a value greater than 2 represents separate graphic window.   
         
        """
        pass
    @DeviceIndex.setter
    def DeviceIndex(self, deviceIndex: int):
        """
        Setter for property: (int) DeviceIndex
         Returns the index of device on which plot graph will be shown.  
          
                        A value of 1 represents the main graphic window,
                        a value greater than 2 represents separate graphic window.   
         
        """
        pass
    @property
    def ViewPortIndex(self) -> int:
        """
        Getter for property: (int) ViewPortIndex
         Returns the index of a view port on main graphic window, on which plot graph will be shown.  
          
                        Only available when  CAE::Xyplot::BasePlotParameters::DeviceIndex  is 1.   
         
        """
        pass
    @ViewPortIndex.setter
    def ViewPortIndex(self, viewIndex: int):
        """
        Setter for property: (int) ViewPortIndex
         Returns the index of a view port on main graphic window, on which plot graph will be shown.  
          
                        Only available when  CAE::Xyplot::BasePlotParameters::DeviceIndex  is 1.   
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def GetRecords(self) -> List[NXOpen.CAE.FTK.BaseRecord]:
        """
         Gets the records to be plotted 
         Returns records ( NXOpen.CAE.FTK.BaseRecord Li):  Records .
        """
        pass
    def SetRecords(self, records: List[NXOpen.CAE.FTK.BaseRecord]) -> None:
        """
         Sets the records to be plotted 
        """
        pass
class BaseSymbolStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the base symbol display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def PointMarker(self) -> PointMarker:
        """
        Getter for property: ( PointMarker NXOpen.C) PointMarker
         Returns the point marker   
            
         
        """
        pass
    @PointMarker.setter
    def PointMarker(self, pointMarker: PointMarker):
        """
        Setter for property: ( PointMarker NXOpen.C) PointMarker
         Returns the point marker   
            
         
        """
        pass
import NXOpen
class BaseTemplateManager(NXOpen.NXObject): 
    """ Manages the graph template """
    def DeleteTemplate(self, template_file: str) -> None:
        """
         Deletes template file 
        """
        pass
    def GetDefaultTemplate(self) -> str:
        """
        Returns the default template file 
         Returns template_file (str):  Template file name with full path .
        """
        pass
    def LoadTemplate(self, template_file: str) -> None:
        """
         Loads the graph template file 
        """
        pass
    def ReloadAllTemplateFiles(self) -> None:
        """
        Reload all graph template files so that the modification on the 
                       loaded graph template files are reset. The unloaded files under 
                       customer directories which is defined by environement variable 
                       UGII_BASE_DIR, UGII_VENDOR_DIR, UGII_SITE_DIR and UGII_USER_DIR 
                       will be reloaded. Also the graph templates in active root part directory 
                       will be reloaded if they are unloaded.  
                    
        """
        pass
    def RenameTemplateFile(self, oldTemplateFile: str, newTemplateFileName: str) -> None:
        """
         Renames template file 
        """
        pass
    def ResetSystemTemplate(self) -> None:
        """
        Resets system template  
        """
        pass
    def ResetTemplate(self, template_file: str) -> None:
        """
         Resets to default value 
        """
        pass
    def SaveAllTemplates(self) -> None:
        """
        Saves all templates 
        """
        pass
    def SaveAsTemplate(self, source_template_file: str, destination_template_file: str) -> None:
        """
         Saves to new template file 
        """
        pass
    def SaveTemplate(self, template_file: str) -> None:
        """
         Saves to template file 
        """
        pass
    def SetDefaultTemplate(self, template_file: str) -> None:
        """
        Sets the default template file.
                    
                    
                    
                    If the input template file is NULL, it will remove default template state.
                    
                    
                    If the input template file is not NULL, it will set the input template as default template.
                    
                    
                    
                    
        """
        pass
    def UnloadAllTemplates(self) -> None:
        """
         Unloads all graph template files 
        """
        pass
    def UnloadTemplate(self, template_file: str) -> None:
        """
         Unloads the graph template file 
        """
        pass
class BasicModel(BaseModel): 
    """ Represents a abstract component object on a XY graphing. """
    @property
    def DisplayStyle(self) -> IDisplayStyle:
        """
        Getter for property: ( IDisplayStyle NXOpen.C) DisplayStyle
         Returns the model display style   
            
         
        """
        pass
class CalculationFunctionType(Enum):
    """
    Members Include: 
     |MaxAmplitude|  This function has two calculation results, the first one is Maximum Amplitude value in Y axis, the second is the corresponding X value 
     |MinAmplitude|  This function has two calculation results, the first one is Minimum Amplitude value in Y axis, the second is the corresponding X value 
     |MaximumRange| 
     |Rss| 
     |Rms| 
     |LinearAveraging| 
     |IntegratedValue| 
     |SignalPower| 
     |Loudness| 

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
    @staticmethod
    def ValueOf(value: int) -> CalculationFunctionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CampbellFunctionDataAccessor(IFunctionDataAccessor): 
    """  Represents a data accessor to retrieve data of a function which is plotted in CAE.Xyplot.PlotType.PlotCampbell plot.  """
    def AskDisplayData(self) -> Tuple[float, List[float], List[float], List[float]]:
        """
         Asks display data. 
         Returns A tuple consisting of (orderValue, independentValues, dependentValues, rpmValues). 
         - orderValue is: float.
         - independentValues is: List[float].
         - dependentValues is: List[float].
         - rpmValues is: List[float].

        """
        pass
class CampbellGraphType(Enum):
    """
    Members Include: 
     |Point|  Option to display Campbell Plot in Point style 
     |Line|  Option to display Campbell Plot in Line style 

    """
    Point: int
    Line: int
    @staticmethod
    def ValueOf(value: int) -> CampbellGraphType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CampbellPlot(Plot): 
    """  Manages the display of campbell plot.
        
        Call CAE.Xyplot.I3DDataPlot.EditRecords to edit data for this class.
         """
    pass
class CampbellPointSizeType(Enum):
    """
    Members Include: 
     |Const|  Option to display points with const diameters in Point style
     |Variable|  Option to display points with variable diameters correspond to result data in Point style

    """
    Const: int
    Variable: int
    @staticmethod
    def ValueOf(value: int) -> CampbellPointSizeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ColorAxisStyleSetting(AxisStyleSetting): 
    """ Represents the axis display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def ColorScaleStyleSetting(self) -> ColorScaleStyle:
        """
        Getter for property: ( ColorScaleStyle NXOpen.C) ColorScaleStyleSetting
         Returns the color scale display style.  
             
         
        """
        pass
    @property
    def ResultLegendStyleSetting(self) -> ResultLegendStyle:
        """
        Getter for property: ( ResultLegendStyle NXOpen.C) ResultLegendStyleSetting
         Returns the result legend display style.  
             
         
        """
        pass
class ColorAxis(AxisModel): 
    """ Represents a color axis object on a XY graphing. """
    def GetColorLegendLevelCount(self) -> int:
        """
         Gets the number of legend levels 
         Returns numLevels (int): .
        """
        pass
class ColorBarPlot(Plot): 
    """ 
        Manages the display of color bar plot.
        
        Call CAE.Xyplot.I2DDataPlot.EditRecord to edit data for this class.
         """
    pass
class ColorMapGraph(Graph): 
    """ Manages the display color map graph."""
    def CreateOrderMarker(self, orderValue: float) -> MarkerModel:
        """
         Creates the display order marker on the color map graph. 
         Returns marker ( MarkerModel NXOpen.C):  Marker model .
        """
        pass
class ColorMapPlot(Plot): 
    """ 
        Manages the display of color map plot.
        
        Call CAE.Xyplot.I3DDataPlot.EditRecords to edit data for this class.
         """
    pass
class ColorScaleStyle(BaseDisplayStyleSetting): 
    """ Represents the color scale display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def AreColorLegendColorsOverridden(self) -> bool:
        """
        Getter for property: (bool) AreColorLegendColorsOverridden
         Returns the option indicates whether to customize the color legend colors   
            
         
        """
        pass
    @AreColorLegendColorsOverridden.setter
    def AreColorLegendColorsOverridden(self, areColorsOverridden: bool):
        """
        Setter for property: (bool) AreColorLegendColorsOverridden
         Returns the option indicates whether to customize the color legend colors   
            
         
        """
        pass
    @property
    def AreColorLegendValuesOverridden(self) -> bool:
        """
        Getter for property: (bool) AreColorLegendValuesOverridden
         Returns the option indicates whether to customize the color legend values   
            
         
        """
        pass
    @AreColorLegendValuesOverridden.setter
    def AreColorLegendValuesOverridden(self, areValuesOverridden: bool):
        """
        Setter for property: (bool) AreColorLegendValuesOverridden
         Returns the option indicates whether to customize the color legend values   
            
         
        """
        pass
    @property
    def AutoLevel(self) -> bool:
        """
        Getter for property: (bool) AutoLevel
         Returns the option indicates whether to define color level automatically   
            
         
        """
        pass
    @AutoLevel.setter
    def AutoLevel(self, useAutoLevel: bool):
        """
        Setter for property: (bool) AutoLevel
         Returns the option indicates whether to define color level automatically   
            
         
        """
        pass
    @property
    def ColorSpectrumType(self) -> ColorSpectrum:
        """
        Getter for property: ( ColorSpectrum NXOpen.C) ColorSpectrumType
         Returns  the color spectrum type setting   
            
         
        """
        pass
    @ColorSpectrumType.setter
    def ColorSpectrumType(self, spectrumType: ColorSpectrum):
        """
        Setter for property: ( ColorSpectrum NXOpen.C) ColorSpectrumType
         Returns  the color spectrum type setting   
            
         
        """
        pass
    @property
    def InvertionSpectrum(self) -> bool:
        """
        Getter for property: (bool) InvertionSpectrum
         Returns the option indicates whether to invert color spectrum   
            
         
        """
        pass
    @InvertionSpectrum.setter
    def InvertionSpectrum(self, isInverted: bool):
        """
        Setter for property: (bool) InvertionSpectrum
         Returns the option indicates whether to invert color spectrum   
            
         
        """
        pass
    @property
    def Level(self) -> int:
        """
        Getter for property: (int) Level
         Returns  the level setting   
            
         
        """
        pass
    @Level.setter
    def Level(self, level: int):
        """
        Setter for property: (int) Level
         Returns  the level setting   
            
         
        """
        pass
    @property
    def MeasureName(self) -> str:
        """
        Getter for property: (str) MeasureName
         Returns the option indicates what's the measurement associated with the override settings   
            
         
        """
        pass
    @MeasureName.setter
    def MeasureName(self, measureName: str):
        """
        Setter for property: (str) MeasureName
         Returns the option indicates what's the measurement associated with the override settings   
            
         
        """
        pass
    def GetColorLegendColorsOverridden(self) -> List[int]:
        """
         Gets the overrided colors of color legend 
         Returns legendColors (List[int]): .
        """
        pass
    def GetColorLegendValuesOverridden(self) -> List[float]:
        """
         Gets the overrided values of color legend 
         Returns overridedValues (List[float]): .
        """
        pass
    def SetColorLegendColorsOverridden(self, legendColors: List[int]) -> None:
        """
         Sets the overrided colors of color legend 
        """
        pass
    def SetColorLegendValuesOverridden(self, overridedValues: List[float]) -> None:
        """
         Sets the overrided values of color legend  
        """
        pass
class ColorSpectrum(Enum):
    """
    Members Include: 
     |Structural| 
     |Thermal| 
     |Grayscale| 
     |Stoplight| 

    """
    Structural: int
    Thermal: int
    Grayscale: int
    Stoplight: int
    @staticmethod
    def ValueOf(value: int) -> ColorSpectrum:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ComplexOption2DBarChart(Enum):
    """
    Members Include: 
     |Magnitude|  Magnitude of the complex data for 2D bar chart plot 
     |Phase|  Phase of the complex data for 2D bar chart plot 
     |Real|  Real part of the complex data for 2D bar chart plot 
     |Imaginary|  Imaginary part of the complex data for 2D bar chart plot 
     |AtPhaseAngle|  At phase angle for 2D bar chart plot 
     |SignedMagnitude|  Signed magnitude for 2D bar chart plot 

    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    AtPhaseAngle: int
    SignedMagnitude: int
    @staticmethod
    def ValueOf(value: int) -> ComplexOption2DBarChart:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ComplexOption2DColorContour(Enum):
    """
    Members Include: 
     |Magnitude|  Magnitude of the complex data for 2D color contour plot plot 
     |Phase|  Phase of the complex data for 2D color contour plot plot 
     |Real|  Real part of the complex data for 2D color contour plot plot 
     |Imaginary|  Imaginary part of the complex data for 2D color contour plot plot 
     |AtPhaseAngle|  At phase angle for 2D color contour plot plot 
     |SignedMagnitude|  Signed magnitude for 2D color contour plot plot 

    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    AtPhaseAngle: int
    SignedMagnitude: int
    @staticmethod
    def ValueOf(value: int) -> ComplexOption2DColorContour:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ComplexOption2D(Enum):
    """
    Members Include: 
     |Magnitude|  Magnitude of the complex data for 2D plot 
     |MagnitudePhase|  Magnitude and phase angle of complex data for 2D plot 
     |Phase|  Only the phase of the complex data for 2D plot 
     |Real|  Only the real part of the complex data for 2D plot 
     |RealImaginary|  Real and imaginary of the complex data for 2D plot 
     |RealImaginaryPhase|  Real, imaginary and phase angle of the complex data for 2D plot 
     |Polar|  Polar for 2D plot 
     |Argand|  Argand for 2D plot 
     |Polar3D|  Polar for 3D plot 
     |Argand3D|  Argand for 3D plot which z coordindate come from the x coordinate 
     |PhaseMagnitude|  Phase angle and Magnitude of complex data for 2D plot 
     |ImaginaryReal|  Real and imaginary of the complex data for 2D plot 
     |PhaseRealImaginary|  Phase angle, real and imaginary of the complex data for 2D plot 
     |ImaginaryRealPhase|  Imaginary, real and phase angle of the complex data for 2D plot 
     |PhaseImaginaryReal|  Phase angle, imaginary and real of the complex data for 2D plot 
     |Nichols|  Nichols for 2D plot 
     |AtPhaseAngle|  At phase angle for 2D plot 
     |SignedMagnitude|  Signed magnitude for 2D plot 
     |Directivity|  Directivity for 2D plot 
     |Vector|  Vector for 2D plot 

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
    @staticmethod
    def ValueOf(value: int) -> ComplexOption2D:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ComplexOption3D(Enum):
    """
    Members Include: 
     |Magnitude|  Magnitude of the complex data for 3D plot 
     |Phase|  Phase of the complex data for 3D plot 
     |Real|  Real part of the complex data for 3D plot 
     |Imaginary|  Imaginary part of the complex data for 3D plot 
     |Argand|  Argand for 3D plot which use the real z coordindate 
     |Orbit|  Orbit for 3D plot 
     |Nichols|  Nichols for 3D plot 
     |AtPhaseAngle|  At phase angle for 3D plot 
     |SignedMagnitude|  Signed magnitude for 3D plot 

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
    @staticmethod
    def ValueOf(value: int) -> ComplexOption3D:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ComplexOptionMatrix2D(Enum):
    """
    Members Include: 
     |Magnitude|  Magnitude of the complex data for matrix 2D plot 
     |Phase|  Phase of the complex data for matrix 2D plot 
     |Real|  Real part of the complex data for matrix 2D plot 
     |Imaginary|  Imaginary part of the complex data for matrix 2D plot 
     |AtPhaseAngle|  At phase angle for matrix 2D plot 
     |SignedMagnitude|  Signed magnitude for matrix 2D plot 

    """
    Magnitude: int
    Phase: int
    Real: int
    Imaginary: int
    AtPhaseAngle: int
    SignedMagnitude: int
    @staticmethod
    def ValueOf(value: int) -> ComplexOptionMatrix2D:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ContouringRange(Enum):
    """
    Members Include: 
     |BorderGrid|  Option to show contour range on the border of the grid 
     |FullGrid|  Option to show contour range on the face of the grid 

    """
    BorderGrid: int
    FullGrid: int
    @staticmethod
    def ValueOf(value: int) -> ContouringRange:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CoordinateType(Enum):
    """
    Members Include: 
     |Xy|  no swap for 2d 
     |Yx|  swap x and y 
     |Xyz|  no swap for 3d
     |Yxz|  swap x and y 
     |Zyx|  swap x and z 
     |Yzx|  swap x and y firstly and then swap y and z
     |Xzy|  swap Z and y 
     |Zxy|  swap x and y firstly and then swap X and z

    """
    Xy: int
    Yx: int
    Xyz: int
    Yxz: int
    Zyx: int
    Yzx: int
    Xzy: int
    Zxy: int
    @staticmethod
    def ValueOf(value: int) -> CoordinateType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CurveDisplaySettings(BaseDisplayStyleSetting): 
    """ Represents the curve display style. Call Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified."""
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the line color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the line color   
            
         
        """
        pass
    @property
    def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) Font
         Returns the line font   
            
         
        """
        pass
    @Font.setter
    def Font(self, gridFont: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) Font
         Returns the line font   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) Width
         Returns the line width   
            
         
        """
        pass
    @Width.setter
    def Width(self, gridWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) Width
         Returns the line width   
            
         
        """
        pass
class CustomTextStyleSetting(TextStyleSetting): 
    """  Represents the text content definition in title options  """
    @property
    def UseAutomatic(self) -> bool:
        """
        Getter for property: (bool) UseAutomatic
         Returns a value indicating whether to define text content automatically .  
             
         
        """
        pass
    @UseAutomatic.setter
    def UseAutomatic(self, useAutomatic: bool):
        """
        Setter for property: (bool) UseAutomatic
         Returns a value indicating whether to define text content automatically .  
             
         
        """
        pass
    def GetUserDefinedText(self) -> List[str]:
        """
         Returns the text content defined by user. 
         Returns text (List[str]): .
        """
        pass
    def SetUserDefinedText(self, text: List[str]) -> None:
        """
         Sets the text content defined by user. 
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
import NXOpen.Fields
class DataExporter(NXOpen.Object): 
    """ XYPlot exporter function handler """
    def ExportCalculationLegendsToFiles(exportFilesParam: NXOpen.CAE.FTK.ExportFilesParameter, calculationlegendTableModels: List[LegendTable]) -> None:
        """
         Exports calculation legends' content to output files or listing window. 
                    
                    It exports calculation legends' content to listing window if output file is not specified in NXOpen.CAE.FTK.ExportFilesParameter.
                    
                    
        """
        pass
    def ExportToFiles(exportDataParam: DataExportParameters, exportFilesParam: NXOpen.CAE.FTK.ExportFilesParameter) -> None:
        """
         Exports the data with given parameter settings to files.
                    
                    The data will be printed to listing window when no file is specified in  NXOpen.CAE.FTK.ExportFilesParameter.
                    
                    
        """
        pass
    def ExportToTableField(exportParam: DataExportParameters, customFieldNames: List[str]) -> List[NXOpen.Fields.FieldTable]:
        """
         Exports data with given parameter settings to table field.
                        Field names can be specified optionally. If not specified, the field name will be set with default record name.
                        This does not support for BarChart and Matrix Plot.
         Returns tables ( NXOpen.Fields.FieldTable Li): .
        """
        pass
    def NewDisplayDataExportParameters() -> DisplayDataExportParameters:
        """
         Creates an object  NXOpen.CAE.Xyplot.DisplayDataExportParameters  to contain the
                        settings when exporting display data. The object needs to be destroyed after excuting exporting data. 
                        The display data means the current data displayed on the view excluding zoom status, showhide status, display style(line, bar, scatter etc.). 
         Returns displayExportParam ( DisplayDataExportParameters NXOpen.C): .
        """
        pass
    def NewExportFilesParameters() -> NXOpen.CAE.FTK.ExportFilesParameter:
        """
         Creates an object  NXOpen.CAE.FTK.ExportFilesParameter  to contain the
                        settings when exporting data. The object needs to be destroyed after excuting exporting data. 
         Returns exportFilesParam ( NXOpen.CAE.FTK.ExportFilesParameter): .
        """
        pass
    def NewSourceDataExportParameters() -> SourceDataExportParameters:
        """
         Creates an object  NXOpen.CAE.Xyplot.SourceDataExportParameters  to contain the
                        settings when exporting source data. This object needs to be destroyed after excuting exporting data. 
         Returns sourceExportParam ( SourceDataExportParameters NXOpen.C): .
        """
        pass
import NXOpen
class DataExportParameters(NXOpen.TransientObject): 
    """ Represents the parameters passed to export the data of a plot. """
    @property
    def Plot(self) -> Plot:
        """
        Getter for property: ( Plot NXOpen.C) Plot
         Returns the plot which is being exported.  
           Uses this method when all exported data are in same plot,
                    otherwise uses method  CAE::Xyplot::DataExportParameters::GetPlots    
         
        """
        pass
    @Plot.setter
    def Plot(self, plot: Plot):
        """
        Setter for property: ( Plot NXOpen.C) Plot
         Returns the plot which is being exported.  
           Uses this method when all exported data are in same plot,
                    otherwise uses method  CAE::Xyplot::DataExportParameters::GetPlots    
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def GetPlots(self) -> List[Plot]:
        """
         Gets the plots which data is to be exported 
         Returns plots ( Plot List[NXOpen): .
        """
        pass
    def GetRecordIndices(self) -> List[int]:
        """
         Gets the data index vector of the plot. 
         Returns plotDataIndices (List[int]): .
        """
        pass
    def SetPlots(self, plots: List[Plot]) -> None:
        """
         Sets the plots which data is to be exported 
        """
        pass
    def SetRecordIndices(self, plotDataIndices: List[int]) -> None:
        """
         Sets the plot data index vector 
        """
        pass
class DecimalFormat(Enum):
    """
    Members Include: 
     |Actual|  Show decimal automatically 
     |X|  Displays one digit followed by period 
     |Xx|  Displays two digits followed by period 
     |Xxx|  Displays three digits followed by period 
     |Xxxx|  Displays four digits followed by period 
     |Xexx|  Scientific notation with one digit followed by period,for example: 5.3E+05 
     |Xxexx|  Scientific notation with two digits followed by period 
     |Xxxexx|  Scientific notation with three digits followed by period 
     |Xxxxexx|  Scientific notation with four digits followed by period 

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
    @staticmethod
    def ValueOf(value: int) -> DecimalFormat:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DiagramDisplayStyles2DBarChart(DiagramDisplayStyles): 
    """ Manages the 2D bar chart diagram display styles. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def SpaceBetweenFunctions(self) -> int:
        """
        Getter for property: (int) SpaceBetweenFunctions
         Returns the space between functions measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    @SpaceBetweenFunctions.setter
    def SpaceBetweenFunctions(self, spaceBetweenFunctions: int):
        """
        Setter for property: (int) SpaceBetweenFunctions
         Returns the space between functions measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    @property
    def SpaceBetweenItems(self) -> int:
        """
        Getter for property: (int) SpaceBetweenItems
         Returns the space between items measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    @SpaceBetweenItems.setter
    def SpaceBetweenItems(self, spaceBetweenItems: int):
        """
        Setter for property: (int) SpaceBetweenItems
         Returns the space between items measured in percentage.  
           The acceptable range is 0-10.   
         
        """
        pass
    def GetBarChartStyleSetting(self, styleIndex: int) -> BarChartStyleSetting:
        """
         Gets the bar chart bar display style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns barChartStyle ( BarChartStyleSetting NXOpen.C):  Bar Chart Bar style .
        """
        pass
class DiagramDisplayStyles2D(DiagramDisplayStyles): 
    """ Manages the display styles for 2D diagram. """
    def GetGraphOptionsStyle(self, styleIndex: int) -> GraphOptionsStyle2D:
        """
         Gets the nth graph options display style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns graphOptions ( GraphOptionsStyle2D NXOpen.C): .
        """
        pass
import NXOpen
class DiagramDisplayStylesCampbell(DiagramDisplayStyles): 
    """ Manages the diagram display styles of Campbell Plot. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def GraphType(self) -> CampbellGraphType:
        """
        Getter for property: ( CampbellGraphType NXOpen.C) GraphType
         Returns the graph type for Campbell Plot   
            
         
        """
        pass
    @GraphType.setter
    def GraphType(self, graphStyle: CampbellGraphType):
        """
        Setter for property: ( CampbellGraphType NXOpen.C) GraphType
         Returns the graph type for Campbell Plot   
            
         
        """
        pass
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width.  
           
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypeLine .   
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, lineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width.  
           
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypeLine .   
         
        """
        pass
    @property
    def PointMarker(self) -> PointMarker:
        """
        Getter for property: ( PointMarker NXOpen.C) PointMarker
         Returns the point marker.  
          
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypeLine .   
         
        """
        pass
    @PointMarker.setter
    def PointMarker(self, pointMarker: PointMarker):
        """
        Setter for property: ( PointMarker NXOpen.C) PointMarker
         Returns the point marker.  
          
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypeLine .   
         
        """
        pass
    @property
    def PointSizeScale(self) -> float:
        """
        Getter for property: (float) PointSizeScale
         Returns the scale of point size which must between 0.  
          5 and 2.0. 
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypePoint .   
         
        """
        pass
    @PointSizeScale.setter
    def PointSizeScale(self, sizeScale: float):
        """
        Setter for property: (float) PointSizeScale
         Returns the scale of point size which must between 0.  
          5 and 2.0. 
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypePoint .   
         
        """
        pass
    @property
    def PointSizeType(self) -> CampbellPointSizeType:
        """
        Getter for property: ( CampbellPointSizeType NXOpen.C) PointSizeType
         Returns the style of point size.  
           
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypePoint .   
         
        """
        pass
    @PointSizeType.setter
    def PointSizeType(self, sizeStyle: CampbellPointSizeType):
        """
        Setter for property: ( CampbellPointSizeType NXOpen.C) PointSizeType
         Returns the style of point size.  
           
                        Only available when  CAE::Xyplot::DiagramDisplayStylesCampbell::GraphType  
                        is  CAE::Xyplot::CampbellGraphTypePoint .   
         
        """
        pass
    @property
    def ShowBackground(self) -> bool:
        """
        Getter for property: (bool) ShowBackground
         Returns a value indicating whether to show background in color of the minimmum value   
            
         
        """
        pass
    @ShowBackground.setter
    def ShowBackground(self, showBackground: bool):
        """
        Setter for property: (bool) ShowBackground
         Returns a value indicating whether to show background in color of the minimmum value   
            
         
        """
        pass
class DiagramDisplayStylesColorMap(DiagramDisplayStyles): 
    """ Manages the display styles for ColorMap diagram. """
    @property
    def GraphOptionsStyle(self) -> GraphOptionsStyleColorMap:
        """
        Getter for property: ( GraphOptionsStyleColorMap NXOpen.C) GraphOptionsStyle
         Returnsthe graph options style.  
             
         
        """
        pass
class DiagramDisplayStyles(BaseDisplayStyleSetting): 
    """ Manages the diagram display styles. """
    @property
    def StyleCount(self) -> int:
        """
        Getter for property: (int) StyleCount
         Returns the style count   
            
         
        """
        pass
    def GetBarStyleSetting(self, styleIndex: int) -> BaseBarStyleSetting:
        """
         Gets the bar display style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns barStyle ( BaseBarStyleSetting NXOpen.C):  Bar style .
        """
        pass
    def GetGraphStyle(self, styleIndex: int) -> GraphStyle:
        """
         Gets the graph style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns graphStyle ( GraphStyle NXOpen.C):  Graph style .
        """
        pass
    def GetGraphStyleName(self, styleIndex: int) -> str:
        """
         Gets the graph style name.
                        The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount .
         Returns graphStyleName (str):  Graph style Name.
        """
        pass
    def GetLineStyleSetting(self, styleIndex: int) -> BaseLineStyleSetting:
        """
         Gets the line display style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns lineStyle ( BaseLineStyleSetting NXOpen.C):  Line style .
        """
        pass
    def GetScatterStyleSetting(self, styleIndex: int) -> ScatterStyleSetting:
        """
         Gets the scatter display style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns scatterStyle ( ScatterStyleSetting NXOpen.C):  Scatter style .
        """
        pass
    def GetSurfaceStyleSetting(self, styleIndex: int) -> SurfaceStyleSetting:
        """
         Gets the surface display style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns surfaceStyle ( SurfaceStyleSetting NXOpen.C):  Surface style .
        """
        pass
    def GetVectorStyleSetting(self, styleIndex: int) -> VectorStyle2DSetting:
        """
         Gets the vector display style. The style index must be greater than or equal to 0 and
                    less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
         Returns vectorStyle ( VectorStyle2DSetting NXOpen.C):  Line style .
        """
        pass
    def SetGraphStyle(self, styleIndex: int, graphStyle: GraphStyle) -> None:
        """
         Sets the graph style. The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount . 
        """
        pass
    def SetGraphStyleName(self, styleIndex: int, graphStyleName: str) -> None:
        """
         Sets the graph style name.
                        The style index must be greater than or equal to 0 and
                        less than CAE.Xyplot.DiagramDisplayStyles.StyleCount .
        """
        pass
class Direction(Enum):
    """
    Members Include: 
     |X|  Option to show plot in the X axis direction 
     |Z|  Option to show plot in the Z axis direction 
     |Xz|  Option to show plot in the both X and Z axis direction 

    """
    X: int
    Z: int
    Xz: int
    @staticmethod
    def ValueOf(value: int) -> Direction:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DisplayDataExportParameters(DataExportParameters): 
    """ Represents the parameter settings for export display data."""
    def GetGraphIndices(self) -> List[int]:
        """
         Gets the graph index vector 
         Returns graphIndices (List[int]): .
        """
        pass
    def SetGraphIndices(self, graphIndices: List[int]) -> None:
        """
         Sets the graph index vector. The count of graph indices must be same to record indices. 
        """
        pass
class FlowResultColor(Enum):
    """
    Members Include: 
     |NotSet|  Uses the upper or lower color of color limits 
     |Shaded|  User defined color 

    """
    NotSet: int
    Shaded: int
    @staticmethod
    def ValueOf(value: int) -> FlowResultColor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Fonttype(Enum):
    """
    Members Include: 
     |Nx|  NX Font 
     |Standard|  Standard Font 

    """
    Nx: int
    Standard: int
    @staticmethod
    def ValueOf(value: int) -> Fonttype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class FormulaExpressionStyle(BaseDisplayStyleSetting): 
    """ Represents the formula expression style. """
    @property
    def FormulaGridType(self) -> FormulaGridType:
        """
        Getter for property: ( FormulaGridType NXOpen.C) FormulaGridType
         Returns the formula grid type   
            
         
        """
        pass
    @FormulaGridType.setter
    def FormulaGridType(self, formulaGridType: FormulaGridType):
        """
        Setter for property: ( FormulaGridType NXOpen.C) FormulaGridType
         Returns the formula grid type   
            
         
        """
        pass
    @property
    def IsIncludeNegativeInfinity(self) -> bool:
        """
        Getter for property: (bool) IsIncludeNegativeInfinity
         Returns a value indicating whether to include negative infinity   
            
         
        """
        pass
    @IsIncludeNegativeInfinity.setter
    def IsIncludeNegativeInfinity(self, isInclude: bool):
        """
        Setter for property: (bool) IsIncludeNegativeInfinity
         Returns a value indicating whether to include negative infinity   
            
         
        """
        pass
    @property
    def IsIncludePositiveInfinity(self) -> bool:
        """
        Getter for property: (bool) IsIncludePositiveInfinity
         Returns a value indicating whether to include positive infinity   
            
         
        """
        pass
    @IsIncludePositiveInfinity.setter
    def IsIncludePositiveInfinity(self, isInclude: bool):
        """
        Setter for property: (bool) IsIncludePositiveInfinity
         Returns a value indicating whether to include positive infinity   
            
         
        """
        pass
    def GetVariableValues(self) -> List[float]:
        """
         Get the variable values 
         Returns variableValues (List[float]):  Get the variable values .
        """
        pass
    def SetVariableValues(self, variableValues: List[float]) -> None:
        """
         Set the variable values 
        """
        pass
class FormulaGridStyle(BaseDisplayStyleSetting): 
    """ Manages the formula grid style. """
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    def GetExpressionStyle(self) -> FormulaExpressionStyle:
        """
         Gets the formula expression style. 
         Returns pExpressionStyle ( FormulaExpressionStyle NXOpen.C):  expression style .
        """
        pass
    def GetGridLineStyle(self) -> CurveDisplaySettings:
        """
         Gets the grid line style. 
         Returns pGridLineStyle ( CurveDisplaySettings NXOpen.C):  grid line style .
        """
        pass
    def GetGridValueTextStyle(self) -> TextStyleSetting:
        """
         Gets the grid value text style. 
         Returns pGridValueTextStyle ( TextStyleSetting NXOpen.C):  grid value text style .
        """
        pass
class FormulaGridType(Enum):
    """
    Members Include: 
     |NotSet| 
     |DiagonalLineInHaighDiagram| 

    """
    NotSet: int
    DiagonalLineInHaighDiagram: int
    @staticmethod
    def ValueOf(value: int) -> FormulaGridType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class FrequencyBandSummationBandTypeMode(Enum):
    """
    Members Include: 
     |Infer|  Mode to follow the synchronization driven by current curve or other curves and axes 
     |UserDefined|  Mode to change band type of current curve independently 

    """
    Infer: int
    UserDefined: int
    @staticmethod
    def ValueOf(value: int) -> FrequencyBandSummationBandTypeMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class FrequencyBandSummationBandType(Enum):
    """
    Members Include: 
     |Octave|  Octave 
     |OneThirdOctave|  13 Octave 
     |OneTwelfthOctave|  112 Octave 

    """
    Octave: int
    OneThirdOctave: int
    OneTwelfthOctave: int
    @staticmethod
    def ValueOf(value: int) -> FrequencyBandSummationBandType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class FrequencyBandSummationDisplayMode(Enum):
    """
    Members Include: 
     |StepLines|  Step Lines 
     |ConnectCentralFrequencies|  Connect Central Frequencies 

    """
    StepLines: int
    ConnectCentralFrequencies: int
    @staticmethod
    def ValueOf(value: int) -> FrequencyBandSummationDisplayMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class FrequencyBandSummationStyle(BaseDisplayStyleSetting): 
    """ Represents the frequency band summation display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def BandType(self) -> FrequencyBandSummationBandType:
        """
        Getter for property: ( FrequencyBandSummationBandType NXOpen.C) BandType
         Returns a value specifies the frequency band summation band type.  
             
         
        """
        pass
    @BandType.setter
    def BandType(self, bandType: FrequencyBandSummationBandType):
        """
        Setter for property: ( FrequencyBandSummationBandType NXOpen.C) BandType
         Returns a value specifies the frequency band summation band type.  
             
         
        """
        pass
    @property
    def BandTypeMode(self) -> FrequencyBandSummationBandTypeMode:
        """
        Getter for property: ( FrequencyBandSummationBandTypeMode NXOpen.C) BandTypeMode
         Returns a value specifies the frequency band summation band type mode.  
             
         
        """
        pass
    @BandTypeMode.setter
    def BandTypeMode(self, bandTypeMode: FrequencyBandSummationBandTypeMode):
        """
        Setter for property: ( FrequencyBandSummationBandTypeMode NXOpen.C) BandTypeMode
         Returns a value specifies the frequency band summation band type mode.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> FrequencyBandSummationDisplayMode:
        """
        Getter for property: ( FrequencyBandSummationDisplayMode NXOpen.C) DisplayMode
         Returns a value specifies the frequency band summation display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: FrequencyBandSummationDisplayMode):
        """
        Setter for property: ( FrequencyBandSummationDisplayMode NXOpen.C) DisplayMode
         Returns a value specifies the frequency band summation display mode.  
             
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns a value specifies whether to show frequency band summation.  
             
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns a value specifies whether to show frequency band summation.  
             
         
        """
        pass
class FunctionDataAccessor(Enum):
    """
    Members Include: 
     |NotSet| 
     |Xy| 
     |Xyz| 
     |Argand3D| 
     |BarChart| 
     |Matrix| 
     |Campbell| 

    """
    NotSet: int
    Xy: int
    Xyz: int
    Argand3D: int
    BarChart: int
    Matrix: int
    Campbell: int
    @staticmethod
    def ValueOf(value: int) -> FunctionDataAccessor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class FunctionLegendAccessor(NXOpen.TransientObject): 
    """  Represents a data accessor to retrieve calculation results for function of CAE.Xyplot.CalculationFunctionType.  """
    def AskFunctionName(self, funcType: CalculationFunctionType) -> str:
        """
         Asks the function name. 
         Returns funcName (str): .
        """
        pass
    def AskFunctionResult(self, funcType: CalculationFunctionType) -> Tuple[bool, List[float]]:
        """
         Asks the calcualtion result. 
         Returns A tuple consisting of (hasNumberValue, results). 
         - hasNumberValue is: bool.
         - results is: List[float].

        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
class GeneralDisplayStyles2DBarChart(GeneralDisplayStyles): 
    """ Manages the general display styles for 2D bar chart plot. """
    @property
    def ComplexOption(self) -> ComplexOption2DBarChart:
        """
        Getter for property: ( ComplexOption2DBarChart NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption2DBarChart):
        """
        Setter for property: ( ComplexOption2DBarChart NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
class GeneralDisplayStyles2DColorContour(GeneralDisplayStyles): 
    """ Manages the general display styles for 2D color contour plot. """
    @property
    def ComplexOption(self) -> ComplexOption2DColorContour:
        """
        Getter for property: ( ComplexOption2DColorContour NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption2DColorContour):
        """
        Setter for property: ( ComplexOption2DColorContour NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
class GeneralDisplayStyles2D(GeneralDisplayStyles): 
    """ Manages the general display styles for 2D plot. """
    @property
    def ComplexOption(self) -> ComplexOption2D:
        """
        Getter for property: ( ComplexOption2D NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption2D):
        """
        Setter for property: ( ComplexOption2D NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    def SwitchXYAxis(self) -> None:
        """
         Switches the XY axis 
        """
        pass
class GeneralDisplayStyles3D(GeneralDisplayStyles): 
    """ Manages the general display styles for 3D plot. """
    @property
    def ComplexOption(self) -> ComplexOption3D:
        """
        Getter for property: ( ComplexOption3D NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOption3D):
        """
        Setter for property: ( ComplexOption3D NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
class GeneralDisplayStylesMatrix2D(GeneralDisplayStyles): 
    """ Manages the general display styles for matrix 2D plot. """
    @property
    def ComplexOption(self) -> ComplexOptionMatrix2D:
        """
        Getter for property: ( ComplexOptionMatrix2D NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    @ComplexOption.setter
    def ComplexOption(self, complexOption: ComplexOptionMatrix2D):
        """
        Setter for property: ( ComplexOptionMatrix2D NXOpen.C) ComplexOption
         Returns the complex option   
            
         
        """
        pass
    @property
    def LayoutMode(self) -> MatrixPlot2DLayoutMode:
        """
        Getter for property: ( MatrixPlot2DLayoutMode NXOpen.C) LayoutMode
         Returns the layout mode   
            
         
        """
        pass
    @LayoutMode.setter
    def LayoutMode(self, layoutMode: MatrixPlot2DLayoutMode):
        """
        Setter for property: ( MatrixPlot2DLayoutMode NXOpen.C) LayoutMode
         Returns the layout mode   
            
         
        """
        pass
    def SwitchXYAxis(self) -> None:
        """
         Switches the XY axis 
        """
        pass
class GeneralDisplayStyles(BaseDisplayStyleSetting): 
    """ Manages the general display styles. """
    @property
    def PhaseAngle(self) -> float:
        """
        Getter for property: (float) PhaseAngle
         Returns the phase angle in degree   
            
         
        """
        pass
    @PhaseAngle.setter
    def PhaseAngle(self, phaseAngle: float):
        """
        Setter for property: (float) PhaseAngle
         Returns the phase angle in degree   
            
         
        """
        pass
    @property
    def PhaseRangeOption(self) -> PhaseRangeOption:
        """
        Getter for property: ( PhaseRangeOption NXOpen.C) PhaseRangeOption
         Returns the phase range option   
            
         
        """
        pass
    @PhaseRangeOption.setter
    def PhaseRangeOption(self, phaseRangeOption: PhaseRangeOption):
        """
        Setter for property: ( PhaseRangeOption NXOpen.C) PhaseRangeOption
         Returns the phase range option   
            
         
        """
        pass
class Graph3D(Graph): 
    """ Manages the display graph 3d. """
    pass
class GraphNamePositionOption(Enum):
    """
    Members Include: 
     |TopLeft|  Option to positon name on top left of grid plane     
     |TopCenter|  Option to positon name on top center of grid plane   
     |TopRight|  Option to positon name on top right of grid plane    
     |BottomLeft|  Option to positon name on bottom left of grid plane  
     |BottomCenter|  Option to positon name on bottom center of grid plane
     |BottomRight|  Option to positon name on bottom right of grid plane 

    """
    TopLeft: int
    TopCenter: int
    TopRight: int
    BottomLeft: int
    BottomCenter: int
    BottomRight: int
    @staticmethod
    def ValueOf(value: int) -> GraphNamePositionOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GraphNameStyle(TextStyleSetting): 
    """ Represents the graph name display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def PositionOption(self) -> GraphNamePositionOption:
        """
        Getter for property: ( GraphNamePositionOption NXOpen.C) PositionOption
         Returns the option specifies how to position the graph name   
            
         
        """
        pass
    @PositionOption.setter
    def PositionOption(self, positionOption: GraphNamePositionOption):
        """
        Setter for property: ( GraphNamePositionOption NXOpen.C) PositionOption
         Returns the option specifies how to position the graph name   
            
         
        """
        pass
class GraphOptionsStyle2D(BaseDisplayStyleSetting): 
    """ Manages the specific settings for 2D graph. """
    @property
    def FrequencyBandSummationBandType(self) -> FrequencyBandSummationBandType:
        """
        Getter for property: ( FrequencyBandSummationBandType NXOpen.C) FrequencyBandSummationBandType
         Returns a value specifies the frequency band summation band type   
            
         
        """
        pass
    @FrequencyBandSummationBandType.setter
    def FrequencyBandSummationBandType(self, freqBandSummationBandType: FrequencyBandSummationBandType):
        """
        Setter for property: ( FrequencyBandSummationBandType NXOpen.C) FrequencyBandSummationBandType
         Returns a value specifies the frequency band summation band type   
            
         
        """
        pass
    @property
    def FrequencyBandSummationBandTypeMode(self) -> FrequencyBandSummationBandTypeMode:
        """
        Getter for property: ( FrequencyBandSummationBandTypeMode NXOpen.C) FrequencyBandSummationBandTypeMode
         Returns a value specifies the frequency band summation band type mode   
            
         
        """
        pass
    @FrequencyBandSummationBandTypeMode.setter
    def FrequencyBandSummationBandTypeMode(self, freqBandSummationBandTypeMode: FrequencyBandSummationBandTypeMode):
        """
        Setter for property: ( FrequencyBandSummationBandTypeMode NXOpen.C) FrequencyBandSummationBandTypeMode
         Returns a value specifies the frequency band summation band type mode   
            
         
        """
        pass
    @property
    def FrequencyBandSummationDisplayMode(self) -> FrequencyBandSummationDisplayMode:
        """
        Getter for property: ( FrequencyBandSummationDisplayMode NXOpen.C) FrequencyBandSummationDisplayMode
         Returns a value specifies the frequency band summation display mode   
            
         
        """
        pass
    @FrequencyBandSummationDisplayMode.setter
    def FrequencyBandSummationDisplayMode(self, freqBandSummationDisplayMode: FrequencyBandSummationDisplayMode):
        """
        Setter for property: ( FrequencyBandSummationDisplayMode NXOpen.C) FrequencyBandSummationDisplayMode
         Returns a value specifies the frequency band summation display mode   
            
         
        """
        pass
    @property
    def ShowFrequencyBandSummation(self) -> bool:
        """
        Getter for property: (bool) ShowFrequencyBandSummation
         Returns a value specifies whether to show frequency band summation   
            
         
        """
        pass
    @ShowFrequencyBandSummation.setter
    def ShowFrequencyBandSummation(self, showFreqBandSummation: bool):
        """
        Setter for property: (bool) ShowFrequencyBandSummation
         Returns a value specifies whether to show frequency band summation   
            
         
        """
        pass
    @property
    def ShowTotalResponseLineForPolar(self) -> bool:
        """
        Getter for property: (bool) ShowTotalResponseLineForPolar
         Returns a value specifies whether to show total response line for 2D polar plot   
            
         
        """
        pass
    @ShowTotalResponseLineForPolar.setter
    def ShowTotalResponseLineForPolar(self, showTotalResponseLineForPolar: bool):
        """
        Setter for property: (bool) ShowTotalResponseLineForPolar
         Returns a value specifies whether to show total response line for 2D polar plot   
            
         
        """
        pass
    @property
    def ShowTotalResponseLineForVector(self) -> bool:
        """
        Getter for property: (bool) ShowTotalResponseLineForVector
         Returns a value specifies whether to show total response line for 2D vector plot   
            
         
        """
        pass
    @ShowTotalResponseLineForVector.setter
    def ShowTotalResponseLineForVector(self, showTotalResponseLineForVector: bool):
        """
        Setter for property: (bool) ShowTotalResponseLineForVector
         Returns a value specifies whether to show total response line for 2D vector plot   
            
         
        """
        pass
    @property
    def TotalResponseLineSetting(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) TotalResponseLineSetting
         Returns the total response line setting   
            
         
        """
        pass
class GraphOptionsStyleColorMap(BaseDisplayStyleSetting): 
    """ Manages the specific settings for ColorMap graph."""
    @property
    def FreqBandSummationStyle(self) -> FrequencyBandSummationStyle:
        """
        Getter for property: ( FrequencyBandSummationStyle NXOpen.C) FreqBandSummationStyle
         Returnsthe frequency band summation style.  
             
         
        """
        pass
class GraphStyle(Enum):
    """
    Members Include: 
     |Line|  Option to display plot in curve style 
     |Bar|  Option to display plot in bar style  
     |Surface|  Option to display plot in surface style 
     |Scatter|  Option to display plot in scatter style 
     |ColorBar|  Option to display plot in ColorBar style 
     |ColorMap|  Option to display plot in ColorMap style 
     |BarChart|  Option to display plot in BarChart style 
     |Vector|  Option to display plot in vector style 
     |Matrix2D|  Option to display plot in Matrix2D style 

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
    @staticmethod
    def ValueOf(value: int) -> GraphStyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Graph(BaseModel): 
    """ Manages the display graph. Each graph has its owner axis and graph name. """
    @property
    def RecordCount(self) -> int:
        """
        Getter for property: (int) RecordCount
         Returns the record count of the graph.  
             
         
        """
        pass
    def CreateAssociativeMarker(self, recordIndex: int, attachType: AnchorType, absPercentage: float) -> MarkerModel:
        """
          Creates an associative marker. 
                    
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive.
                    
                    
         Returns marker ( MarkerModel NXOpen.C):  Marker model .
        """
        pass
    @overload
    def CreateMarker(self, recordIndex: int, pointIndex: int) -> MarkerModel:
        """
          Creates a marker in the position of a source point. 
                        
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive. 
                        The point index is between 0 and CAE.Xyplot.Graph.GetPointCount, 0 is inclusive. 
                        
                    
         Returns marker ( MarkerModel NXOpen.C):  Marker model .
        """
        pass
    @overload
    def CreateMarker(self, recordIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
          Creates a marker in the linear interpolation position between two source points. 
                    
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive. 
                        The previous point index is between 0 and CAE.Xyplot.Graph.GetPointCount, 0 is inclusive.
                        The next point index is between 0 and CAE.Xyplot.Graph.GetPointCount, 0 is inclusive. 
                        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
                    
                    
         Returns marker ( MarkerModel NXOpen.C):  Marker model .
        """
        pass
    def CreateOrderMarker(self, recordIndex: int) -> OrderMarkerModel:
        """
         Creates Order Marker and show it in a graph which plot type is CAE.Xyplot.PlotType.PlotCampbell. 
         Returns orderMarkerModel ( OrderMarkerModel NXOpen.C): .
        """
        pass
    def CreateOverallMarker(self, recordIndex: int) -> OverallMarkerModel:
        """
          Creates an overall marker that shows a calculation result for overall operation. 
                    
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive.
                        The overall marker coud only be created for the data which abscissa measurement is frequency, and different calculation algorithm is applied according to function data type.
                        If the function data type is power or acoustic power, it applies with sum algorithm;
                        If the function data type is PSD, it applies with integration algorithm;
                        To the other types, it applies with RSS algorithm.
                    
                    
         Returns marker ( OverallMarkerModel NXOpen.C):  Overall Marker Model .
        """
        pass
    def CreateSoundPlayer(self, recordIndex: int) -> SoundPlayer:
        """
         Creates sound player for a selected display data on a CAE.Xyplot.PlotType.Plot2D plot. 
         Returns soundPlayer ( SoundPlayer NXOpen.C): .
        """
        pass
    def GetAbscissaAxes(self) -> List[BasicModel]:
        """
         Gets the abscissa axes. 
         Returns xAxes ( BasicModel List[NXOpen): .
        """
        pass
    def GetAnchorPointOfRecord(self, recordIndex: int, anchorType: AnchorType) -> Tuple[bool, NXOpen.Point3d]:
        """
         Gets anchor point of a record. 
         Returns A tuple consisting of (hasAnchorPoint, anchorPoint). 
         - hasAnchorPoint is: bool.
         - anchorPoint is:  NXOpen.Point3d.

        """
        pass
    def GetDisplayStyleOfRecord(self, recordIndex: int) -> int:
        """
          Gets the display style index for a given record index in given graph.
                        
                             The record index must be greater than and equal to 0 and less than CAE.Xyplot.Graph.RecordCount.
                             The display style index is limitted from 0 to 19.
                        
                     
         Returns displayStyleIndex (int): .
        """
        pass
    def GetGridBoundingBox(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the bounding box of the grid. 
         Returns A tuple consisting of (leftBottom, rightTop). 
         - leftBottom is:  NXOpen.Point3d.
         - rightTop is:  NXOpen.Point3d.

        """
        pass
    def GetIdentifier(self, recordIndex: int) -> str:
        """
         Gets XY curve data source identifier by record index from graph 
                    
                    Only the data displayed on 2D graph in the following complex option type support identifier:
                    CAE.Xyplot.ComplexOption2D.Magnitude
                    CAE.Xyplot.ComplexOption2D.MagnitudePhase
                    CAE.Xyplot.ComplexOption2D.Phase
                    CAE.Xyplot.ComplexOption2D.Real
                    CAE.Xyplot.ComplexOption2D.RealImaginary
                    CAE.Xyplot.ComplexOption2D.RealImaginaryPhase
                    CAE.Xyplot.ComplexOption2D.PhaseMagnitude
                    CAE.Xyplot.ComplexOption2D.ImaginaryReal
                    CAE.Xyplot.ComplexOption2D.PhaseRealImaginary
                    CAE.Xyplot.ComplexOption2D.ImaginaryRealPhase
                    CAE.Xyplot.ComplexOption2D.PhaseImaginaryReal
                    CAE.Xyplot.ComplexOption2D.AtPhaseAngle
                    CAE.Xyplot.ComplexOption2D.SignedMagnitude
                    
                    
         Returns identifier (str): .
        """
        pass
    def GetMarkers(self) -> List[MarkerModel]:
        """
         Gets all markers on the graph. 
         Returns markers ( MarkerModel List[NXOpen):  Marker models .
        """
        pass
    def GetOrdinateAxes(self) -> List[BasicModel]:
        """
         Gets the ordinate axes. 
         Returns yAxes ( BasicModel List[NXOpen): .
        """
        pass
    def GetPointCount(self, recordIndex: int) -> int:
        """
         Gets the point count of specified record. 
         Returns pointCount (int):  Point count .
        """
        pass
    def GetRecordName(self, recordIndex: int) -> str:
        """
         Gets record name. 
         Returns recordName (str): .
        """
        pass
    def GetZAxis(self) -> BasicModel:
        """
         Gets the Z axis. 
         Returns zAxis ( BasicModel NXOpen.C): .
        """
        pass
    def RestoreStyleAssignments(self) -> None:
        """
         Restores style assignments. 
                        
                        This function just restore display style to system style assignments for current
                        plot and doesn't impact on template.
                        
                    
        """
        pass
    def SaveStyleAssignmentsToTemplate(self) -> None:
        """
         Saves current style assignments to template.
        """
        pass
    def SetDisplayStyleOfRecord(self, recordIndex: int, displayStyleIndex: int) -> None:
        """
           Sets the display style index for a given record index based on graph.
                        
                             The record index must be greater than and equal to 0 and less than CAE.Xyplot.Graph.RecordCount.
                             The display style index is limitted from 0 to 19.
                        
                     
        """
        pass
    def SetIdentifier(self, recordIndex: int, identifier: str) -> None:
        """
         Sets XY curve data source identifier by record index from graph 
        """
        pass
    def Unzoom(self) -> None:
        """
         
                        Removes the zoom state for the graph and returns the display to the original state.
                        
                        
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        CAE.Xyplot.BaseModel.UpdateDisplay for an instance of CAE.Xyplot.Plot or
                        CAE.Xyplot.Graph
                        
                     
        """
        pass
    def ZoomAlongX(self, startScale: float, endScale: float) -> None:
        """
         
                        Zooms the graph along X direction by a scale range basing on current X axis display range.
                        
                        
                        
                        
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        CAE.Xyplot.BaseModel.UpdateDisplay for an instance of CAE.Xyplot.Plot or
                        CAE.Xyplot.Graph.
                        
                        
                        The scale range could be calculated from CAE.Xyplot.AxisModel.CalculateZoomScale
                        
                        
                        
                     
        """
        pass
    def ZoomAlongXY(self, xStartScale: float, xEndScale: float, yStartScale: float, yEndScale: float) -> None:
        """
         
                        Zooms the graph along both X and Y direction by scale ranges basing on current X and Y axis display range. It is only available to 2D plot.
                        
                        
                        
                        
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        CAE.Xyplot.BaseModel.UpdateDisplay for an instance of CAE.Xyplot.Plot or
                        CAE.Xyplot.Graph.
                        
                        
                        The scale range could be calculated from CAE.Xyplot.AxisModel.CalculateZoomScale
                        
                        
                        
                     
        """
        pass
    def ZoomAlongY(self, startScale: float, endScale: float) -> None:
        """
         
                        Zooms the graph along Y direction by a scale range basing on current Y axis display range.
                        
                        
                        
                        
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        CAE.Xyplot.BaseModel.UpdateDisplay for an instance of CAE.Xyplot.Plot or
                        CAE.Xyplot.Graph.
                        
                        
                        The scale range could be calculated from CAE.Xyplot.AxisModel.CalculateZoomScale
                        
                        
                        
                     
        """
        pass
    def ZoomAlongZ(self, startScale: float, endScale: float) -> None:
        """
         
                        Zooms the graph along Z direction by a scale range basing on current Z axis display range. It is only available to 3D plot.
                        
                        
                        
                        
                        The function just updates the model data. To make the display update to reflect the model change, please call
                        CAE.Xyplot.BaseModel.UpdateDisplay for an instance of CAE.Xyplot.Plot or
                        CAE.Xyplot.Graph.
                        
                        
                        The scale range could be calculated from CAE.Xyplot.AxisModel.CalculateZoomScale
                        
                        
                        
                     
        """
        pass
class GridLayoutStyle2DSetting(BaseGridLayoutStyleSetting): 
    """ Represents the 2d grid layout display style. """
    pass
class GridLayoutStyle3DSetting(BaseGridLayoutStyleSetting): 
    """ Represents the 3d grid layout display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def ZxGridStyle(self) -> GridStyle:
        """
        Getter for property: ( GridStyle NXOpen.C) ZxGridStyle
         Returns the grid style of ZX plane   
            
         
        """
        pass
    @ZxGridStyle.setter
    def ZxGridStyle(self, gridStyle: GridStyle):
        """
        Setter for property: ( GridStyle NXOpen.C) ZxGridStyle
         Returns the grid style of ZX plane   
            
         
        """
        pass
    @property
    def ZyGridStyle(self) -> GridStyle:
        """
        Getter for property: ( GridStyle NXOpen.C) ZyGridStyle
         Returns the grid style of ZY plane   
            
         
        """
        pass
    @ZyGridStyle.setter
    def ZyGridStyle(self, gridStyle: GridStyle):
        """
        Setter for property: ( GridStyle NXOpen.C) ZyGridStyle
         Returns the grid style of ZY plane   
            
         
        """
        pass
class GridStyle(Enum):
    """
    Members Include: 
     |NoGrid|  No grid displayed 
     |GridOnly|  Only display grid 
     |TicksOnly|  Only display tick 
     |GridAndTicks|  Display both grid and tick 
     |DenseGrid|  Display dense grid 

    """
    NoGrid: int
    GridOnly: int
    TicksOnly: int
    GridAndTicks: int
    DenseGrid: int
    @staticmethod
    def ValueOf(value: int) -> GridStyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class I2DDataPlot(NXOpen.Object): 
    """  Represents a plot interface which input should be a series of 2D data 
        
        This interface is suitable for those plots which own a series of 2d data, and each data can be drawn,edited and deleted independently;
        
        """
    @abstractmethod
    def EditRecord(self, nthRecordIdx: int, record: NXOpen.CAE.FTK.BaseRecord) -> None:
        """
         Edits nth record of plot. 
                    
                    
                     Procedure of editing records of plot fully:
                    
                    Call this method to edit record data
                    Call CAE.Xyplot.Plot.CommitRecordsChange to precess record data change and update data model
                    Call CAE.Xyplot.BaseModel.UpdateDisplay to regenerate display to reflect data change
                    Optionally call CAE.Xyplot.Plot.FitView to make display fit the view;it is only required when the plot display boundary is changed
                    
                    
                    
                    
        """
        pass
import NXOpen
class I3DDataGraph(NXOpen.Object): 
    """  Represents a graph interface which input is 3D data
        
        3D plot data can consist of multiple CAE.FTK.ArrayRecord2D or a CAE.FTK.SectionBasedMatrixRecord
        
        """
    @abstractmethod
    @overload
    def CreateMarker(self, recordIndex: int, sectionIndex: int, pointIndex: int) -> MarkerModel:
        """
          Creates a marker in the position of a source point. 
                    
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive. 
                        The point index is between 0 and CAE.Xyplot.I3DDataGraph.GetSourcePointCount, 0 is inclusive. 
                    
                    
         Returns marker ( MarkerModel NXOpen.C):  Marker model .
        """
        pass
    @abstractmethod
    @overload
    def CreateMarker(self, recordIndex: int, sectionIndex: int, prePointIndex: int, nextPointIndex: int, linearInterpoScale: float) -> MarkerModel:
        """
          Creates a marker in the linear interpolation position between two source points. 
                    
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive. 
                        The previousnext point index is between 0 and CAE.Xyplot.I3DDataGraph.GetSourcePointCount, 0 is inclusive.
                        The linear interpolation scale is between 0 and 1, both 0 and 1 are inclusive. 
                    
                    
         Returns marker ( MarkerModel NXOpen.C):  Marker model .
        """
        pass
    @abstractmethod
    def GetSourcePointCount(self, recordIndex: int, sectionIndex: int) -> int:
        """
          Gets the source point count of specified record. 
                    
                        The record index is between 0 and CAE.Xyplot.Graph.RecordCount, 0 is inclusive.
                    
                    
         Returns pointCount (int):  Point count .
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class I3DDataPlot(NXOpen.Object): 
    """  Represents a plot interface which input is 3D data
        
        3D plot data can consist of multiple CAE.FTK.ArrayRecord2D or a CAE.FTK.SectionBasedMatrixRecord
        To the plot class which implements this interface, all input records will be represented as a whole data.
        
        """
    @abstractmethod
    def EditRecords(self, records: List[NXOpen.CAE.FTK.BaseRecord]) -> None:
        """
         Edits records of plot. 
                    
                    
                     Procedure of editing records of plot fully:
                    
                    Call this method to edit record data
                    Call CAE.Xyplot.Plot.CommitRecordsChange to precess record data change and update data model
                    Call CAE.Xyplot.IDisplayableModel.UpdateDisplay to regenerate display to reflect data change
                    Optionally call CAE.Xyplot.Plot.FitView to make display fit the view;it is only required when the plot display boundary is changed
                    
                    
                    
                    
        """
        pass
import NXOpen
class IAxisStyle(NXOpen.Object): 
    """  Represents the axis style setting interface 
        
        This interface is suitable for those axis style which own a label style setting and an annotation style setting;
        
        """
    @abstractmethod
    def GetAnnotationStyle(self) -> TextStyleSetting:
        """
         Gets the annotation style 
         Returns annotationStyle ( TextStyleSetting NXOpen.C):  Axis item style .
        """
        pass
    @abstractmethod
    def GetLabelDisplayStyle(self) -> CustomTextStyleSetting:
        """
         Gets the label style 
         Returns labelStyle ( CustomTextStyleSetting NXOpen.C): .
        """
        pass
import NXOpen
class ICurveDisplaySettings(NXOpen.Object): 
    """ Represents the interface for curve display style classes."""
    @property
    @abstractmethod
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the line color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the line color   
            
         
        """
        pass
    @property
    @abstractmethod
    def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) Font
         Returns the line font   
            
         
        """
        pass
    @Font.setter
    def Font(self, gridFont: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) Font
         Returns the line font   
            
         
        """
        pass
    @property
    @abstractmethod
    def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) Width
         Returns the line width   
            
         
        """
        pass
    @Width.setter
    def Width(self, gridWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) Width
         Returns the line width   
            
         
        """
        pass
import NXOpen
class IDeletableModel(NXOpen.Object): 
    """ This interface is suitable for those models which can be deleted. """
    @abstractmethod
    def Delete(self) -> None:
        """
         Deletes the model 
        """
        pass
import NXOpen
class IDisplayableModel(NXOpen.Object): 
    """  This class represents an interface to the XYPLOT displayable model.  """
    @abstractmethod
    def UpdateDisplay(self) -> None:
        """
         Updates model display 
        """
        pass
import NXOpen
class IDisplayStyle(NXOpen.Object): 
    """ Represents the interface for  plot display style classes"""
    @property
    @abstractmethod
    def Owner(self) -> IDisplayStyle:
        """
        Getter for property: ( IDisplayStyle NXOpen.C) Owner
         Returns the owner style   
            
         
        """
        pass
    @abstractmethod
    def CommitChange(self) -> None:
        """
         Commits any edits that have been applied to the display style.
                        Triggers the corresponding plot to update graph. 
        """
        pass
import NXOpen
class IFunctionDataAccessor(NXOpen.TransientObject): 
    """  Represents a function data accessor interface to retrieve data for given graph index and record index.  """
    @property
    def FunctionType(self) -> str:
        """
        Getter for property: (str) FunctionType
         Returns the function type name.  
             
         
        """
        pass
    @property
    def RecordName(self) -> str:
        """
        Getter for property: (str) RecordName
         Returns the record name.  
             
         
        """
        pass
    @property
    def Type(self) -> FunctionDataAccessor:
        """
        Getter for property: ( FunctionDataAccessor NXOpen.C) Type
         Returns the function data accessor type.  
             
         
        """
        pass
    def AskAxisAccessor(self, axisDirection: AxisDirection) -> AxisAccessor:
        """
         Asks axis accessor. 
         Returns axisAccessor ( AxisAccessor NXOpen.C): .
        """
        pass
    def AskColorAxisAccessor(self) -> AxisAccessor:
        """
         Asks color axis accessor. 
         Returns axisAccessor ( AxisAccessor NXOpen.C): .
        """
        pass
    def AskFunctionLegendAccessor(self) -> FunctionLegendAccessor:
        """
         Asks function legend accessor. 
         Returns functionLegendAccessor ( FunctionLegendAccessor NXOpen.C): .
        """
        pass
    def AskLegendAccessor(self) -> LegendAccessor:
        """
         Asks legend accessor. 
         Returns legendAccessor ( LegendAccessor NXOpen.C): .
        """
        pass
    def AskOverallLevelAccessor(self) -> OverallLevelAccessor:
        """
         Asks overall level accessor 
         Returns overallLevelAccessor ( OverallLevelAccessor NXOpen.C): .
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
import NXOpen
class ITextModel(NXOpen.Object): 
    """ This interface is suitable for those models which are derived from text model. """
    @abstractmethod
    def GetTexts(self) -> List[str]:
        """
         Results text values 
         Returns textValues (List[str]): .
        """
        pass
import NXOpen
class IVisibleDisplayStyle(NXOpen.Object): 
    """ Represents the interface for visible display style classes."""
    @property
    @abstractmethod
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
import NXOpen
class LeaderStyle(NXOpen.TaggedObject): 
    """ Manages the Leader display styles. """
    @property
    def AnchorColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AnchorColor
         Returns the anchor color   
            
         
        """
        pass
    @AnchorColor.setter
    def AnchorColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AnchorColor
         Returns the anchor color   
            
         
        """
        pass
    @property
    def LineStyle(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) LineStyle
         Returns the line display style.  
             
         
        """
        pass
    @property
    def PointMarker(self) -> PointMarker:
        """
        Getter for property: ( PointMarker NXOpen.C) PointMarker
         Returns the anchor point marker   
            
         
        """
        pass
    @PointMarker.setter
    def PointMarker(self, pointMarker: PointMarker):
        """
        Setter for property: ( PointMarker NXOpen.C) PointMarker
         Returns the anchor point marker   
            
         
        """
        pass
import NXOpen
class LegendAccessor(NXOpen.TransientObject): 
    """  Represents a data accessor to retrieve data of a legend.  """
    @property
    def FreeText(self) -> str:
        """
        Getter for property: (str) FreeText
         Returns the free text.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
class LegendTableGroupStyle(BaseDisplayStyleSetting): 
    """ Manages the legend table group styles. """
    @property
    def ActiveLegendTablePosition(self) -> LegendTablePositionType:
        """
        Getter for property: ( LegendTablePositionType NXOpen.C) ActiveLegendTablePosition
         Returns the active legend table position type   
            
         
        """
        pass
    @ActiveLegendTablePosition.setter
    def ActiveLegendTablePosition(self, activeLegendTablePositionType: LegendTablePositionType):
        """
        Setter for property: ( LegendTablePositionType NXOpen.C) ActiveLegendTablePosition
         Returns the active legend table position type   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    def GetLegendTableStyle(self, legendTablePositionType: LegendTablePositionType) -> LegendTableStyle:
        """
         Gets legend table style by type. 
         Returns legendTableStyle ( LegendTableStyle NXOpen.C):  Legend Table style .
        """
        pass
class LegendTablePositionType(Enum):
    """
    Members Include: 
     |Floating| The position of legend table can be dragged 
     |Docked|  The position of legend table is fixed  

    """
    Floating: int
    Docked: int
    @staticmethod
    def ValueOf(value: int) -> LegendTablePositionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class LegendTableStyle(BaseDisplayStyleSetting): 
    """ Manages the legend table styles. """
    @property
    def BackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BackgroundColor
         Returns the legend table header background color   
            
         
        """
        pass
    @BackgroundColor.setter
    def BackgroundColor(self, backgroundColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BackgroundColor
         Returns the legend table header background color   
            
         
        """
        pass
    @property
    def GridBackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) GridBackgroundColor
         Returns the grid background color   
            
         
        """
        pass
    @GridBackgroundColor.setter
    def GridBackgroundColor(self, gridBackgroundColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) GridBackgroundColor
         Returns the grid background color   
            
         
        """
        pass
    @property
    def IsBorderLineVisible(self) -> bool:
        """
        Getter for property: (bool) IsBorderLineVisible
         Returns the border line visibility   
            
         
        """
        pass
    @IsBorderLineVisible.setter
    def IsBorderLineVisible(self, isBorderLineVisible: bool):
        """
        Setter for property: (bool) IsBorderLineVisible
         Returns the border line visibility   
            
         
        """
        pass
    @property
    def IsGridBackgroundFilled(self) -> bool:
        """
        Getter for property: (bool) IsGridBackgroundFilled
         Returns the value of controlling whether the grid background is filled   
            
         
        """
        pass
    @IsGridBackgroundFilled.setter
    def IsGridBackgroundFilled(self, isGridBackgroundFilled: bool):
        """
        Setter for property: (bool) IsGridBackgroundFilled
         Returns the value of controlling whether the grid background is filled   
            
         
        """
        pass
    @property
    def IsGridLineVisible(self) -> bool:
        """
        Getter for property: (bool) IsGridLineVisible
         Returns the grid line visibility   
            
         
        """
        pass
    @IsGridLineVisible.setter
    def IsGridLineVisible(self, isGridLineVisible: bool):
        """
        Setter for property: (bool) IsGridLineVisible
         Returns the grid line visibility   
            
         
        """
        pass
    @property
    def IsHeaderVisible(self) -> bool:
        """
        Getter for property: (bool) IsHeaderVisible
         Returns the legend table header visibility  
            
         
        """
        pass
    @IsHeaderVisible.setter
    def IsHeaderVisible(self, isHeaderVisible: bool):
        """
        Setter for property: (bool) IsHeaderVisible
         Returns the legend table header visibility  
            
         
        """
        pass
    @property
    def MaximumLegendItemCount(self) -> int:
        """
        Getter for property: (int) MaximumLegendItemCount
         Returns the maximum displayable functions count on legend table page   
            
         
        """
        pass
    @MaximumLegendItemCount.setter
    def MaximumLegendItemCount(self, maxLegendItemCount: int):
        """
        Setter for property: (int) MaximumLegendItemCount
         Returns the maximum displayable functions count on legend table page   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    def GetBorderLineStyle(self) -> CurveDisplaySettings:
        """
         Gets the border line style. 
         Returns borderLineStyle ( CurveDisplaySettings NXOpen.C):  Border Line style .
        """
        pass
    def GetColumnTitles(self) -> List[str]:
        """
        Gets the legend table column titles 
         Returns columnTitles (List[str]):  column titles.
        """
        pass
    def GetGridLineStyle(self) -> CurveDisplaySettings:
        """
         Gets the grid line style. 
         Returns gridLineStyle ( CurveDisplaySettings NXOpen.C):  Grid Line style .
        """
        pass
    def GetPositionType(self) -> LegendTablePositionType:
        """
         Gets the legend table style type 
         Returns legendTableStyleType ( LegendTablePositionType NXOpen.C): .
        """
        pass
    def GetTextStyle(self) -> LegendTableTextStyle:
        """
         Gets the text style. 
         Returns textStyle ( LegendTableTextStyle NXOpen.C):  Text display style .
        """
        pass
    def SetColumnTitles(self, columnTitles: List[str]) -> None:
        """
        Sets the legend table column titles 
        """
        pass
class LegendTableTextStyle(TextStyleSetting): 
    """ Manages the legend table text styles. """
    def GetMargin(self, marginOption: TextBoxMarginOption) -> float:
        """
         Gets the margin value of legend table 
         Returns marginValue (float):   .
        """
        pass
    def SetMargin(self, marginOption: TextBoxMarginOption, marginValue: float) -> None:
        """
        Sets the margin value of legend table 
        """
        pass
class LegendTable(BaseModel): 
    """ Manages the legend table. """
    @property
    def LegendTableStyle(self) -> LegendTableStyle:
        """
        Getter for property: ( LegendTableStyle NXOpen.C) LegendTableStyle
         Returns the legend table style   
            
         
        """
        pass
    def GetFreeTextOfLegendItem(self, dataIndex: int) -> str:
        """
        Gets the free text of legend table item 
         Returns freeText (str):   .
        """
        pass
    def ResetFreeTextOfLegendItem(self, dataIndex: int) -> None:
        """
        Resets the free text of legend table item 
        """
        pass
    def SetFreeTextOfLegendItem(self, dataIndex: int, freeText: str) -> None:
        """
        Sets the free text of legend table item 
        """
        pass
class LimitsType(Enum):
    """
    Members Include: 
     |FreeLimits|  Type to use source data limits as axis limits 
     |OptimizedLimits|  Type to optimize source data limits to natural axis limits 
     |FixedLimits|  Type to use customized data limits as axis limits 

    """
    FreeLimits: int
    OptimizedLimits: int
    FixedLimits: int
    @staticmethod
    def ValueOf(value: int) -> LimitsType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LineStyle2DSetting(BaseLineStyleSetting): 
    """ Represents the 2d line display style. """
    pass
class LineStyle3DSetting(BaseLineStyleSetting): 
    """ Represents the 3d line display style. """
    @property
    def Direction(self) -> Direction:
        """
        Getter for property: ( Direction NXOpen.C) Direction
         Returns the line direction   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: Direction):
        """
        Setter for property: ( Direction NXOpen.C) Direction
         Returns the line direction   
            
         
        """
        pass
class MarkerModel(BasicModel): 
    """ Represents a marker object on a plotting graph. """
    @property
    def PointIndex(self) -> int:
        """
        Getter for property: (int) PointIndex
         Returns the point index of marker model.  
             
         
        """
        pass
    @property
    def RecordIndex(self) -> int:
        """
        Getter for property: (int) RecordIndex
         Returns the record index of marker model.  
             
         
        """
        pass
    def Delete(self) -> None:
        """
         Deletes the marker model 
        """
        pass
class MarkerStyleSetting(TextStyleSetting): 
    """ Represents the marker display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def AbsPercentage(self) -> float:
        """
        Getter for property: (float) AbsPercentage
         Returns the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
          0, 1.0]   
         
        """
        pass
    @AbsPercentage.setter
    def AbsPercentage(self, absPercentage: float):
        """
        Setter for property: (float) AbsPercentage
         Returns the scale of abscissa percentage setting, just for attachment type: Abscissa Percentage, and the value shuould be limited in [0.  
          0, 1.0]   
         
        """
        pass
    @property
    def AttachmentType(self) -> AnchorType:
        """
        Getter for property: ( AnchorType NXOpen.C) AttachmentType
         Returns the attachment type for associative marker   
            
         
        """
        pass
    @AttachmentType.setter
    def AttachmentType(self, anchorType: AnchorType):
        """
        Setter for property: ( AnchorType NXOpen.C) AttachmentType
         Returns the attachment type for associative marker   
            
         
        """
        pass
    @property
    def DataLabelVisibility(self) -> bool:
        """
        Getter for property: (bool) DataLabelVisibility
         Returnsthe option specifies whether to show point label text  
            
         
        """
        pass
    @DataLabelVisibility.setter
    def DataLabelVisibility(self, isShowLabel: bool):
        """
        Setter for property: (bool) DataLabelVisibility
         Returnsthe option specifies whether to show point label text  
            
         
        """
        pass
    @property
    def NoteTextVisibility(self) -> bool:
        """
        Getter for property: (bool) NoteTextVisibility
         Returns the option specifies whether to show note text   
            
         
        """
        pass
    @NoteTextVisibility.setter
    def NoteTextVisibility(self, isNoteTextVisible: bool):
        """
        Setter for property: (bool) NoteTextVisibility
         Returns the option specifies whether to show note text   
            
         
        """
        pass
    @property
    def NumberTextVisibility(self) -> bool:
        """
        Getter for property: (bool) NumberTextVisibility
         Returns the option specifies whether to show number text   
            
         
        """
        pass
    @NumberTextVisibility.setter
    def NumberTextVisibility(self, isNumberTextVisible: bool):
        """
        Setter for property: (bool) NumberTextVisibility
         Returns the option specifies whether to show number text   
            
         
        """
        pass
    @property
    def SnapToData(self) -> bool:
        """
        Getter for property: (bool) SnapToData
         Returns the option specifies whether just to search source data when creating associative marker   
            
         
        """
        pass
    @SnapToData.setter
    def SnapToData(self, isSnapToData: bool):
        """
        Setter for property: (bool) SnapToData
         Returns the option specifies whether just to search source data when creating associative marker   
            
         
        """
        pass
    def GetNoteTexts(self) -> List[str]:
        """
         Gets the note texts 
         Returns noteTexts (List[str]):  Note Texts .
        """
        pass
    def SetNoteTexts(self, noteTexts: List[str]) -> None:
        """
         Sets the note texts 
        """
        pass
class MatrixFunctionDataAccessor(IFunctionDataAccessor): 
    """  RRepresents a data accessor to retrieve data of a function which is plotted in Matrix graphs.  """
    def AskDisplayData(self) -> List[float]:
        """
         Asks display data. 
         Returns dependentValues (List[float]): .
        """
        pass
    def AskPointLabels(self) -> Tuple[List[str], List[str]]:
        """
         Asks point labels. 
         Returns A tuple consisting of (rowLabels, columnLabels). 
         - rowLabels is: List[str].
         - columnLabels is: List[str].

        """
        pass
class MatrixGraph2D(Graph): 
    """ Manages the display matrix graph 2d. """
    pass
class MatrixPlot2DLayoutMode(Enum):
    """
    Members Include: 
     |FillEachCellAsSquare|  Fill each cell as square 
     |FillAllAvailableDisplayArea|  Fill all available display area 

    """
    FillEachCellAsSquare: int
    FillAllAvailableDisplayArea: int
    @staticmethod
    def ValueOf(value: int) -> MatrixPlot2DLayoutMode:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class MatrixPlot2D(Plot): 
    """ 
        Manages the display of matrix plot 2d.
        
        Call CAE.Xyplot.I2DDataPlot.EditRecord to edit data for this class.
         """
    def GetAllValueTypes(self) -> List[str]:
        """
         Get all available value text types of matrix plot
         Returns valueTypes (List[str]): .
        """
        pass
class MatrixValueTextStyle(TextStyleSetting): 
    """ Represents the value text style displayed in matrix plot. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def ValueType(self) -> str:
        """
        Getter for property: (str) ValueType
         Returns the value type.  
           If it is null, no value text will be displayed  
         
        """
        pass
    @ValueType.setter
    def ValueType(self, valueType: str):
        """
        Setter for property: (str) ValueType
         Returns the value type.  
           If it is null, no value text will be displayed  
         
        """
        pass
class ModelType(Enum):
    """
    Members Include: 
     |Plot|   
     |Graph|   
     |RecordDisplay|   
     |Marker|   
     |Note|   
     |Title|   
     |GraphName|   
     |FunctionName|  the lable of a record for CAE.Xyplot.PlotType.PlotColorBar 
     |XAxis|   
     |XAxisLabel|   
     |XAxisNumber|   
     |YAxis|   
     |YAxisLabel|   
     |YAxisNumber|   
     |ZAxis|   
     |ZAxisLabel|   
     |ZAxisNumber|   
     |ColorAxis|  the color indicator for CAE.Xyplot.PlotType.PlotColorBar and CAE.Xyplot.PlotType.PlotColorMap 
     |ColorAxisLabel|   
     |ColorAxisNumber|   
     |AngleAxis|  the axis to display angle divisions on circle grids 
     |AngleAxisNumber|  the angle axis number 
     |UnknownResult|  Obsoleted in NX13 
     |PageNumber|   
     |Legend|   
     |LegendTable|   
     |ResultLegend|   
     |FormulaGrid|   
     |FormulaGridValueText|   
     |CalculationLegendTable|   

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
    @staticmethod
    def ValueOf(value: int) -> ModelType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class NoteModel(BasicModel): 
    """ Represents a note object on a plot. """
    def Delete(self) -> None:
        """
         Deletes the note model 
        """
        pass
    def GetTextPosition(self) -> NXOpen.Point2d:
        """
         Gets the display position of note content. 
         Returns position ( NXOpen.Point2d):   .
        """
        pass
    def GetTexts(self) -> List[str]:
        """
         Gets the note content. 
         Returns lines (List[str]): .
        """
        pass
    def SetTextPositionWithBoxCorner(self, textBoxConerType: TextBoxCornerType, position: NXOpen.Point2d) -> None:
        """
         Sets the display position of note content with test box corner type. 
        """
        pass
    def SetTexts(self, content: List[str]) -> None:
        """
         Sets the note content. 
        """
        pass
class NoteStyleSetting(TextStyleSetting): 
    """ Represents the note display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    def GetNoteTexts(self) -> List[str]:
        """
         Gets the note texts 
         Returns noteTexts (List[str]):  Note Texts .
        """
        pass
    def SetNoteTexts(self, noteTexts: List[str]) -> None:
        """
         Sets the note texts 
        """
        pass
class OrderMarkerModel(BasicModel): 
    """ Represents an marker which display order value on a CAE.Xyplot.PlotType.PlotCampbell plot . """
    def GetOrderValue(self) -> float:
        """
         Returns the order value. 
         Returns orderValue (float): .
        """
        pass
import NXOpen
class OverallLevelAccessor(NXOpen.TransientObject): 
    """  Represents a data accessor to retrieve the result of overall level. 
            
            The overall level function supports frequency domain and time domain. To provide a given data range
            to calculate in signal power algorithm.
            
        """
    def AskOverallLevelResult(self) -> Tuple[bool, float]:
        """
         Asks the overall level result. 
         Returns A tuple consisting of (hasNumberValue, resultValue). 
         - hasNumberValue is: bool.
         - resultValue is: float.

        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
class OverallMarkerModel(BasicModel): 
    """ Represents an overall marker object that shows a calculation result for overall operation on a plotting graph. """
    def GetResult(self) -> float:
        """
         Returns the calculation result. 
         Returns calculationResult (float): .
        """
        pass
class OverlayParameters(BasePlotParameters): 
    """ Represents the parameters passed to overlay plot records on an existing plot graph. """
    @property
    def SubGraphInStack(self) -> int:
        """
        Getter for property: (int) SubGraphInStack
         Returns the index of subgraph on a stacked plot, on which the records will be
                        overlaied.  
           The property is only available when overlaying records on
                        a stacked plot. The index value is between 0 and the property value of
                         CAE::Xyplot::Plot::SubGraphCountInStack  .   
         
        """
        pass
    @SubGraphInStack.setter
    def SubGraphInStack(self, subGraphIndex: int):
        """
        Setter for property: (int) SubGraphInStack
         Returns the index of subgraph on a stacked plot, on which the records will be
                        overlaied.  
           The property is only available when overlaying records on
                        a stacked plot. The index value is between 0 and the property value of
                         CAE::Xyplot::Plot::SubGraphCountInStack  .   
         
        """
        pass
class PhaseRangeOption(Enum):
    """
    Members Include: 
     |NegativeTwoPiToZero|  Displays phase between -360 and 0 
     |ZeroToTwoPi|  Displays phase between 0 and 360 
     |NegativePiToPi|  Displays phase between -180 and 180 
     |NegativeOneHalfPiToHalfPi|  Displays phase between -270 and 90 
     |NegativeHalfPiToOneHalfPi|  Displays phase between -90 and 270 

    """
    NegativeTwoPiToZero: int
    ZeroToTwoPi: int
    NegativePiToPi: int
    NegativeOneHalfPiToHalfPi: int
    NegativeHalfPiToOneHalfPi: int
    @staticmethod
    def ValueOf(value: int) -> PhaseRangeOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class PlateColorOption(Enum):
    """
    Members Include: 
     |Fill|  Fill color with no shading 
     |Hidden|  Background color as fill 
     |Shaded|  Fill Color with shading 

    """
    Fill: int
    Hidden: int
    Shaded: int
    @staticmethod
    def ValueOf(value: int) -> PlateColorOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class Plot2D(Plot): 
    """  Manages the display of 2D plot.
        
        Call CAE.Xyplot.I2DDataPlot.EditRecord to edit data for this class.
         """
    pass
class Plot3D(Plot): 
    """  Manages the display of 3D plot.
        
         Call CAE.Xyplot.I3DDataPlot.EditRecords to edit data for this class.
         """
    pass
class PlotGraphTemplate(BaseDisplayStyleSetting): 
    """ Manages the plot graph template. """
    @property
    def AbscissaCustomMarkerLabel(self) -> str:
        """
        Getter for property: (str) AbscissaCustomMarkerLabel
         Returns the abscissa custom marker label   
            
         
        """
        pass
    @AbscissaCustomMarkerLabel.setter
    def AbscissaCustomMarkerLabel(self, xCustomMarkerLabel: str):
        """
        Setter for property: (str) AbscissaCustomMarkerLabel
         Returns the abscissa custom marker label   
            
         
        """
        pass
    @property
    def DiagramDisplayStyles(self) -> DiagramDisplayStyles:
        """
        Getter for property: ( DiagramDisplayStyles NXOpen.C) DiagramDisplayStyles
         Returns the diagram display styles.  
             
         
        """
        pass
    @property
    def GeneralDisplayStyles(self) -> GeneralDisplayStyles:
        """
        Getter for property: ( GeneralDisplayStyles NXOpen.C) GeneralDisplayStyles
         Returns the general display styles.  
             
         
        """
        pass
    @property
    def OrdinateCustomMarkerLabel(self) -> str:
        """
        Getter for property: (str) OrdinateCustomMarkerLabel
         Returns the ordinate custom marker label   
            
         
        """
        pass
    @OrdinateCustomMarkerLabel.setter
    def OrdinateCustomMarkerLabel(self, yCustomMarkerLabel: str):
        """
        Setter for property: (str) OrdinateCustomMarkerLabel
         Returns the ordinate custom marker label   
            
         
        """
        pass
    @property
    def WallDisplayStyles(self) -> WallDisplayStyles:
        """
        Getter for property: ( WallDisplayStyles NXOpen.C) WallDisplayStyles
         Returns the wall display styles.  
             
         
        """
        pass
    @property
    def ZCustomMarkerLabel(self) -> str:
        """
        Getter for property: (str) ZCustomMarkerLabel
         Returns the z custom marker label   
            
         
        """
        pass
    @ZCustomMarkerLabel.setter
    def ZCustomMarkerLabel(self, zCustomMarkerLabel: str):
        """
        Setter for property: (str) ZCustomMarkerLabel
         Returns the z custom marker label   
            
         
        """
        pass
    def ExportTemplate(self, strXmlFile: str) -> None:
        """
         Exports current graph template setting to a template xml file,
                        it will override the template file if it is existing. 
        """
        pass
    def ImportTemplate(self, strXmlFile: str) -> None:
        """
         Updates current graph template setting from a template xml file 
        """
        pass
    def ResetToDefault(self) -> None:
        """
         Resets the graph template to default values 
        """
        pass
class PlotParameters(BasePlotParameters): 
    """ Represents the parameters passed to create a plot. """
    @property
    def ComplexOption(self) -> int:
        """
        Getter for property: (int) ComplexOption
         Returns the complex options,if complex option is smaller than zero, it will use default complex option from active template file    
            
         
        """
        pass
    @ComplexOption.setter
    def ComplexOption(self, complexOption: int):
        """
        Setter for property: (int) ComplexOption
         Returns the complex options,if complex option is smaller than zero, it will use default complex option from active template file    
            
         
        """
        pass
    @property
    def IsToCreateStandalonePlot(self) -> bool:
        """
        Getter for property: (bool) IsToCreateStandalonePlot
         Returns the create standalone plot    
            
         
        """
        pass
    @IsToCreateStandalonePlot.setter
    def IsToCreateStandalonePlot(self, isToCreateStandalonePlot: bool):
        """
        Setter for property: (bool) IsToCreateStandalonePlot
         Returns the create standalone plot    
            
         
        """
        pass
    @property
    def PlotTemplate(self) -> PlotGraphTemplate:
        """
        Getter for property: ( PlotGraphTemplate NXOpen.C) PlotTemplate
         Returns the plot template to be used by the plot   
            
         
        """
        pass
    @property
    def PlotType(self) -> PlotType:
        """
        Getter for property: ( PlotType NXOpen.C) PlotType
         Returns the plot type   
            
         
        """
        pass
    @PlotType.setter
    def PlotType(self, plotType: PlotType):
        """
        Setter for property: ( PlotType NXOpen.C) PlotType
         Returns the plot type   
            
         
        """
        pass
class PlotType(Enum):
    """
    Members Include: 
     |Unknown|  unknown plot type 
     |Plot2D|  2D plot 
     |Plot2DInStack|  2D plot in stacked sequence 
     |Plot3D|  3D plot 
     |PlotColorBar|  ColorBar plot 
     |PlotColorMap|  ColorMap plot 
     |PlotBarChart|  BarChart plot 
     |PlotMatrix2D|  Matrix 2D plot 
     |PlotCampbell|  Campbell plot 

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
    @staticmethod
    def ValueOf(value: int) -> PlotType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class Plot(BaseModel): 
    """ Manages the plot template """
    @property
    def PlotTemplate(self) -> PlotGraphTemplate:
        """
        Getter for property: ( PlotGraphTemplate NXOpen.C) PlotTemplate
         Returns the plot template   
            
         
        """
        pass
    @property
    def SubGraphCountInStack(self) -> int:
        """
        Getter for property: (int) SubGraphCountInStack
         Returns the sub-graph count in a stacked plot.  
             
         
        """
        pass
    def CommitRecordsChange(self) -> None:
        """
          Accepts record changed and process data to update data model
                         This method is only to update data model, it needs call CAE.Xyplot.BaseModel.UpdateDisplay to update display to reflect data change.
                        
                    
        """
        pass
    def CreateNoteWithTextBoxCorner(self, textBoxConerType: TextBoxCornerType, lines: List[str], boxCornerPosition: NXOpen.Point2d) -> NoteModel:
        """
         Creates a note with the position of text box corner on the plot. 
         Returns noteModel ( NoteModel NXOpen.C): .
        """
        pass
    def DeleteAllRecords(self) -> None:
        """
          Deletes all records.
                    
                    Higher performance to delete all records from plot than deleting records one by one
                    
                     Procedure of deleting records from plot fully:
                    
                    Call this method to delete all record data from plot
                    Call CAE.Xyplot.Plot.CommitRecordsChange to precess record data change and update data model
                    Call CAE.Xyplot.BaseModel.UpdateDisplay to regenerate display to reflect data change
                    Optionally call CAE.Xyplot.Plot.FitView to make display fit the view;it is only required when the plot display boundary is changed
                    
                    
                    
                    
        """
        pass
    def DeleteRecord(self, recordIndex: int) -> None:
        """
          Deletes the nth record.
                    
                    The record index must be greater or equal to 0, and less than CAE.Xyplot.Plot.GetRecordCount
                    
                     Procedure of deleting records from plot fully:
                    
                    Call this method to delete record data from plot
                    Call CAE.Xyplot.Plot.CommitRecordsChange to precess record data change and update data model
                    Call CAE.Xyplot.BaseModel.UpdateDisplay to regenerate display to reflect data change
                    Optionally call CAE.Xyplot.Plot.FitView to make display fit the view;it is only required when the plot display boundary is changed
                    
                    
                    
                    
        """
        pass
    def FitView(self) -> None:
        """
          Fits the display view on a reasonable region. 
        """
        pass
    def GetApplicationDataOfRecord(self, recordIndex: int) -> NXOpen.CAE.FTK.IApplicationData:
        """
         Returns application specific data associated to a record. 
         Returns applicationData ( NXOpen.CAE.FTK.IApplicationData): .
        """
        pass
    def GetCalculationLegendTables(self) -> List[LegendTable]:
        """
         Gets calculation legend table models on the plot. 
         Returns legendTableModels ( LegendTable List[NXOpen):  Legend Table Objects .
        """
        pass
    def GetDeviceAndViewIndex(self) -> Tuple[int, int]:
        """
         Gets the window device and view index of the plot graph. 
         Returns A tuple consisting of (windowDevice, viewIndex). 
         - windowDevice is: int. the device of window .
         - viewIndex is: int. the index of view .

        """
        pass
    def GetGraphs(self) -> List[Graph]:
        """
         Gets all graphs on the plot. 
         Returns graphs ( Graph List[NXOpen):  Graph objects .
        """
        pass
    def GetLegendTables(self) -> List[LegendTable]:
        """
         Gets the legend table models on the plot. 
         Returns legendTableModels ( LegendTable List[NXOpen):  Legend Table Objects .
        """
        pass
    def GetModels(self, type: ModelType) -> List[BasicModel]:
        """
         Gets the models by model type. 
         Returns models ( BasicModel List[NXOpen): .
        """
        pass
    def GetNotes(self) -> List[NoteModel]:
        """
         Gets all notes on the plot 
         Returns noteModels ( NoteModel List[NXOpen): .
        """
        pass
    def GetPostEnvironmentSettings(self) -> NXOpen.TaggedObject:
        """
         Gets the post environment settings in the plot. 
         Returns postEnvironmentSettings ( NXOpen.TaggedObject):  .
        """
        pass
    def GetRecordCount(self) -> int:
        """
         Returns the count of plotted records on the plot graph. 
         Returns recordCount (int):  Record count .
        """
        pass
    def GetRecordDisplayVisibility(self, recordIndex: int) -> bool:
        """
         Gets the visibility of specified record. 
         Returns visibility (bool): .
        """
        pass
    def GetTitles(self) -> List[BasicModel]:
        """
         Gets the titles on the plot. 
         Returns titles ( BasicModel List[NXOpen): .
        """
        pass
    def GetViewBoundingBox(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the bounding box of the plot view. 
         Returns A tuple consisting of (leftBottom, rightTop). 
         - leftBottom is:  NXOpen.Point3d.
         - rightTop is:  NXOpen.Point3d.

        """
        pass
    def SaveRecords(self, recordIndexes: List[int], recordNames: List[str], outputFileName: str, reportError: bool) -> None:
        """
         Saves plotted records on a graph to an afu file.
                       The record index is between 0 and the value returned from
                       NXOpen.CAE.Xyplot.Plot.GetRecordCount. 
        """
        pass
    def SaveRecordsToCsv(self, recordIndex: List[int], recordNames: List[str], csvFileName: str, isWriteHeader: bool) -> None:
        """
         Saves plotted records on a plot graph to a CSV file. 
        """
        pass
    def SetRecordDisplayVisibility(self, recordIndex: int, visibility: bool) -> None:
        """
         Sets the visibility of specified record. 
        """
        pass
    def WriteToTemplateFile(self, inputTemplateFile: str) -> str:
        """
         Writes the template setting of plot to template file.
                    
                    
                    
                    If input file is a simple file: 
                    
                    If environment variable of UGII_USER_DIR is not set, it will be written into file under user environment directory. 
                    
                    
                    If environment variable of UGII_USER_DIR is not set, it will write to write the template setting.
                    
                    
                    
                    If input file is a file with full path, the template settings will be written into the file.
                    
                    
                    
                    
         Returns templateFileFullName (str):  the file name with full path .
        """
        pass
class PointMarker(Enum):
    """
    Members Include: 
     |NotSet|  No marker 
     |Plus|  Plus marker 
     |Dot|  Dot marker 
     |Asterisk|  Asterisk marker 
     |Circle|  Circle marker 
     |Poundsign|  Pound sign marker 
     |Cross|  Cross marker 
     |Square|  Square marker 
     |Triangle|  Triangle marker 
     |Diamond|  Diamond marker 
     |CenterLine|  Center line marker 

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
    @staticmethod
    def ValueOf(value: int) -> PointMarker:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.CAE.FTK
class Preference(NXOpen.TaggedObject): 
    """ Manages the preference data. """
    class DropActionOption(Enum):
        """
        Members Include: 
         |Auto|  Overlay on existing plot, create new plot on non-plot view 
         |Plot|  Always create new plot on the dropped view 
         |PlotOnNewWindow|  Always create plot on a new grpahics window for all selected data 
         |PlotOnMultipleNewWindows|  Create plot on multiple new graphics window, each plot contains a single data 
         |MetaKey|  Same to "Auto" if no meta key pressed, Press "ALT" is equivalent to "Plot", 
                                                                                      Press "SHIFT" is equivalent to "PlotOnNewWindow", Press "ALT" + "SHIFT" is equivalent to "PlotOnMultipleWindows"
                                                                                  

        """
        Auto: int
        Plot: int
        PlotOnNewWindow: int
        PlotOnMultipleNewWindows: int
        MetaKey: int
        @staticmethod
        def ValueOf(value: int) -> Preference.DropActionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NewWindowChoice(Enum):
        """
        Members Include: 
         |Prompt|  Prompts user to show plot graph on either an existing or a new separate graphic window 
         |Always|  Always show plot graph on a new separate graphic window 

        """
        Prompt: int
        Always: int
        @staticmethod
        def ValueOf(value: int) -> Preference.NewWindowChoice:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetGraphicWindowOption(Enum):
        """
        Members Include: 
         |Main|  Only shows plot graph on main graphic window 
         |Separate|  Only shows plot graph on a separate graphic window 
         |Both|  Shows plot graph on either main graphic window or a separate graphic window 

        """
        Main: int
        Separate: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> Preference.TargetGraphicWindowOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AfuRecordZValue(self) -> NXOpen.CAE.FTK.DataManager.AfuRecordZValue:
        """
        Getter for property: ( NXOpen.CAE.FTK.DataManager.AfuRecordZValue) AfuRecordZValue
         Returns the Z value type for afu record in 3D plot   
            
         
        """
        pass
    @AfuRecordZValue.setter
    def AfuRecordZValue(self, afuZValue: NXOpen.CAE.FTK.DataManager.AfuRecordZValue):
        """
        Setter for property: ( NXOpen.CAE.FTK.DataManager.AfuRecordZValue) AfuRecordZValue
         Returns the Z value type for afu record in 3D plot   
            
         
        """
        pass
    @property
    def DropOnPlotViewAction(self) -> Preference.DropActionOption:
        """
        Getter for property: ( Preference.DropActionOption NXOpen.C) DropOnPlotViewAction
         Returns the action when dropping data to a viewport   
            
         
        """
        pass
    @DropOnPlotViewAction.setter
    def DropOnPlotViewAction(self, dropAction: Preference.DropActionOption):
        """
        Setter for property: ( Preference.DropActionOption NXOpen.C) DropOnPlotViewAction
         Returns the action when dropping data to a viewport   
            
         
        """
        pass
    @property
    def MaximumDisplayableColumnsInMatrix(self) -> int:
        """
        Getter for property: (int) MaximumDisplayableColumnsInMatrix
         Returns the maximum displayable column count in a matrix plot.  
           The column count must be greater than 0    
         
        """
        pass
    @MaximumDisplayableColumnsInMatrix.setter
    def MaximumDisplayableColumnsInMatrix(self, columnCount: int):
        """
        Setter for property: (int) MaximumDisplayableColumnsInMatrix
         Returns the maximum displayable column count in a matrix plot.  
           The column count must be greater than 0    
         
        """
        pass
    @property
    def MaximumDisplayableRowsInMatrix(self) -> int:
        """
        Getter for property: (int) MaximumDisplayableRowsInMatrix
         Returns the maximum displayable row count in a matrix plot.  
           The row count must be greater than 0    
         
        """
        pass
    @MaximumDisplayableRowsInMatrix.setter
    def MaximumDisplayableRowsInMatrix(self, rowCount: int):
        """
        Setter for property: (int) MaximumDisplayableRowsInMatrix
         Returns the maximum displayable row count in a matrix plot.  
           The row count must be greater than 0    
         
        """
        pass
    @property
    def MaximumSubGraphsInStack(self) -> int:
        """
        Getter for property: (int) MaximumSubGraphsInStack
         Returns the maximum sub-graph count in a stacked graph    
            
         
        """
        pass
    @MaximumSubGraphsInStack.setter
    def MaximumSubGraphsInStack(self, graphCount: int):
        """
        Setter for property: (int) MaximumSubGraphsInStack
         Returns the maximum sub-graph count in a stacked graph    
            
         
        """
        pass
    @property
    def NewWindowSetting(self) -> Preference.NewWindowChoice:
        """
        Getter for property: ( Preference.NewWindowChoice NXOpen.C) NewWindowSetting
         Returns the new window setting value.  
           Avaliable when  CAE::Xyplot::Preference::TargetWindowSetting 
                        is  CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate .   
         
        """
        pass
    @NewWindowSetting.setter
    def NewWindowSetting(self, newWindowSetting: Preference.NewWindowChoice):
        """
        Setter for property: ( Preference.NewWindowChoice NXOpen.C) NewWindowSetting
         Returns the new window setting value.  
           Avaliable when  CAE::Xyplot::Preference::TargetWindowSetting 
                        is  CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate .   
         
        """
        pass
    @property
    def TargetWindowSetting(self) -> Preference.TargetGraphicWindowOption:
        """
        Getter for property: ( Preference.TargetGraphicWindowOption NXOpen.C) TargetWindowSetting
         Returns the target window setting value   
            
         
        """
        pass
    @TargetWindowSetting.setter
    def TargetWindowSetting(self, targetWindowSetting: Preference.TargetGraphicWindowOption):
        """
        Setter for property: ( Preference.TargetGraphicWindowOption NXOpen.C) TargetWindowSetting
         Returns the target window setting value   
            
         
        """
        pass
    def Save(self) -> None:
        """
         Saves preference settings to memory file so that preference setting could be shared among sessions 
        """
        pass
class ProbingStyle(BaseDisplayStyleSetting): 
    """ Manages the probing display styles. """
    @property
    def HelpLineStyle(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) HelpLineStyle
         Returns the help line display style.  
             
         
        """
        pass
    @property
    def StepLineStyle(self) -> CurveDisplaySettings:
        """
        Getter for property: ( CurveDisplaySettings NXOpen.C) StepLineStyle
         Returns the step line display style.  
             
         
        """
        pass
    @property
    def TextStyle(self) -> TextStyleSetting:
        """
        Getter for property: ( TextStyleSetting NXOpen.C) TextStyle
         Returns the text display style.  
             
         
        """
        pass
class ProbingTextStyleSetting(TextStyleSetting): 
    """ Represents the probing text display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def DataLabelVisibility(self) -> bool:
        """
        Getter for property: (bool) DataLabelVisibility
         Returnsthe option specifies whether to show point label text  
            
         
        """
        pass
    @DataLabelVisibility.setter
    def DataLabelVisibility(self, isShowLabel: bool):
        """
        Setter for property: (bool) DataLabelVisibility
         Returnsthe option specifies whether to show point label text  
            
         
        """
        pass
import NXOpen
class ResultAccessor(NXOpen.TransientObject): 
    """  Represents a data accessor to retrieve data from Function Plot.  """
    @property
    def CanvasIndex(self) -> int:
        """
        Getter for property: (int) CanvasIndex
         Returns the canvas index this object was created for.  
             
         
        """
        pass
    @property
    def GraphCount(self) -> int:
        """
        Getter for property: (int) GraphCount
         Returns the number of graphs on this canvas.  
             
         
        """
        pass
    @property
    def OnCanvas(self) -> bool:
        """
        Getter for property: (bool) OnCanvas
         Returns the result access mode.  
          
                    
                        If true, this object retrieves data from a specific canvas.
                        If false, this object retrieves data from the entire plot.
                        
         
        """
        pass
    @property
    def Plot(self) -> Plot:
        """
        Getter for property: ( Plot NXOpen.C) Plot
         Returns the plot this object was created for.  
             
         
        """
        pass
    @property
    def RecordCount(self) -> int:
        """
        Getter for property: (int) RecordCount
         Returns the number of records this object can access.  
           
                    
                        If
            ##  NXOpen.CAE.Xyplot.Re is true,
                        then you can retrieve records specific to the canvas this object was created on.
                        If  NXOpen.CAE.Xyplot.Re is false,
                        then you can retrieve records all records in this plot.
                        
         
        """
        pass
    def AskArgand3DFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> Argand3DFunctionDataAccessor:
        """
         Asks argand 3D function data accessor. 
         Returns functionDataAccessor ( Argand3DFunctionDataAccessor NXOpen.C): .
        """
        pass
    def AskBarChartFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> BarChartFunctionDataAccessor:
        """
         Asks BarChart function data accessor. 
         Returns functionDataAccessor ( BarChartFunctionDataAccessor NXOpen.C): .
        """
        pass
    def AskCampbellFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> CampbellFunctionDataAccessor:
        """
         Asks campbell function data accessor. 
         Returns functionDataAccessor ( CampbellFunctionDataAccessor NXOpen.C): .
        """
        pass
    def AskFunctionDataAccessorType(self, graphIndex: int, recordIndex: int) -> FunctionDataAccessor:
        """
         Asks function data accessor type. Then choose correct method to get data accessor according to the accessor type returned 
         Returns accessorType ( FunctionDataAccessor NXOpen.C): .
        """
        pass
    def AskMatrixFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> MatrixFunctionDataAccessor:
        """
         Asks matrix function data accessor. 
         Returns functionDataAccessor ( MatrixFunctionDataAccessor NXOpen.C): .
        """
        pass
    def AskPostEnvironment(self) -> NXOpen.TaggedObject:
        """
         Asks post environment settings. 
         Returns postEnvironment ( NXOpen.TaggedObject): .
        """
        pass
    def AskXYFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> XYFunctionDataAccessor:
        """
         Asks XY function data accessor. 
         Returns functionDataAccessor ( XYFunctionDataAccessor NXOpen.C): .
        """
        pass
    def AskXYZFunctionDataAccessor(self, graphIndex: int, recordIndex: int) -> XYZFunctionDataAccessor:
        """
         Asks XYZ function data accessor. 
         Returns functionDataAccessor ( XYZFunctionDataAccessor NXOpen.C): .
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
    def GetNthGraph(self, graphIdx: int) -> Graph:
        """
         Retrieve a Graph from this Canvas.
                    
                        
                        This method is useful to retrieve NXOpen.CAE.Xyplot.Graph objects in the context of a canvas.
                        This method raises an error if this object was not constructed with a canvas index.
                        Graphs can also be retrieved globally from NXOpen.CAE.Xyplot.Plot via NXOpen.NXObject.FindObject.
                        See NXOpen.CAE.Xyplot.XYPlotManager.CreateResultAccessorOnCanvas.
                        
                      
         Returns graph ( Graph NXOpen.C): .
        """
        pass
import NXOpen
class ResultLegendStyle(BaseDisplayStyleSetting): 
    """ Represents the result legend style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def OverflowResultColorOption(self) -> FlowResultColor:
        """
        Getter for property: ( FlowResultColor NXOpen.C) OverflowResultColorOption
         Returns the overflow result color option   
            
         
        """
        pass
    @OverflowResultColorOption.setter
    def OverflowResultColorOption(self, colorOption: FlowResultColor):
        """
        Setter for property: ( FlowResultColor NXOpen.C) OverflowResultColorOption
         Returns the overflow result color option   
            
         
        """
        pass
    @property
    def OverflowResultShadedColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OverflowResultShadedColor
         Returns the user defined color of overflow result, only available when  NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption 
                    is  NXOpen::CAE::Xyplot::FlowResultColorShaded   
            
         
        """
        pass
    @OverflowResultShadedColor.setter
    def OverflowResultShadedColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OverflowResultShadedColor
         Returns the user defined color of overflow result, only available when  NXOpen::CAE::Xyplot::ResultLegendStyle::OverflowResultColorOption 
                    is  NXOpen::CAE::Xyplot::FlowResultColorShaded   
            
         
        """
        pass
    @property
    def UnderflowResultColorOption(self) -> FlowResultColor:
        """
        Getter for property: ( FlowResultColor NXOpen.C) UnderflowResultColorOption
         Returns the underflow result color option   
            
         
        """
        pass
    @UnderflowResultColorOption.setter
    def UnderflowResultColorOption(self, colorOption: FlowResultColor):
        """
        Setter for property: ( FlowResultColor NXOpen.C) UnderflowResultColorOption
         Returns the underflow result color option   
            
         
        """
        pass
    @property
    def UnderflowResultShadedColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) UnderflowResultShadedColor
         Returns the user defined color of overflow result, only available when  NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption 
                    is  NXOpen::CAE::Xyplot::FlowResultColorShaded   
            
         
        """
        pass
    @UnderflowResultShadedColor.setter
    def UnderflowResultShadedColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) UnderflowResultShadedColor
         Returns the user defined color of overflow result, only available when  NXOpen::CAE::Xyplot::ResultLegendStyle::UnderflowResultColorOption 
                    is  NXOpen::CAE::Xyplot::FlowResultColorShaded   
            
         
        """
        pass
    @property
    def UnknownResultColorOption(self) -> UnknownResultColor:
        """
        Getter for property: ( UnknownResultColor NXOpen.C) UnknownResultColorOption
         Returns the unknown result color option   
            
         
        """
        pass
    @UnknownResultColorOption.setter
    def UnknownResultColorOption(self, unknownResultColor: UnknownResultColor):
        """
        Setter for property: ( UnknownResultColor NXOpen.C) UnknownResultColorOption
         Returns the unknown result color option   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
import NXOpen
class ScatterStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the scatter display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the point color  
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the point color  
            
         
        """
        pass
import NXOpen
class SoundPlayer(NXOpen.TransientObject): 
    """ It represents a sound player which could play sound for a time-pressure function on a CAE.Xyplot.PlotType.Plot2D plot. """
    @property
    def Cyclestate(self) -> bool:
        """
        Getter for property: (bool) Cyclestate
         Returns the cycle state   
            
         
        """
        pass
    @Cyclestate.setter
    def Cyclestate(self, state: bool):
        """
        Setter for property: (bool) Cyclestate
         Returns the cycle state   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def Play(self) -> None:
        """
         Plays sound. 
        """
        pass
    def Stop(self) -> None:
        """
         Stops playing sound. 
        """
        pass
class SourceDataExportParameters(DataExportParameters): 
    """ Represents the parameter settings for exporting source data. """
    class ComplextDataSaveOption(Enum):
        """
        Members Include: 
         |RealImag| 
         |MagPhase| 

        """
        RealImag: int
        MagPhase: int
        @staticmethod
        def ValueOf(value: int) -> SourceDataExportParameters.ComplextDataSaveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComplexDataSaveSetting(self) -> SourceDataExportParameters.ComplextDataSaveOption:
        """
        Getter for property: ( SourceDataExportParameters.ComplextDataSaveOption NXOpen.C) ComplexDataSaveSetting
         Returns the option to save complex data   
            
         
        """
        pass
    @ComplexDataSaveSetting.setter
    def ComplexDataSaveSetting(self, complexDataType: SourceDataExportParameters.ComplextDataSaveOption):
        """
        Setter for property: ( SourceDataExportParameters.ComplextDataSaveOption NXOpen.C) ComplexDataSaveSetting
         Returns the option to save complex data   
            
         
        """
        pass
    def GetSectionDataIndices(self) -> List[int]:
        """
         Gets the section data index vector.
                        
                        For CAE.Xyplot.PlotType.PlotColorMap,
                        CAE.Xyplot.PlotType.Plot3D,
                        and CAE.Xyplot.PlotType.PlotMatrix2D,
                        the plot data is composed with multiple section data.
                        When saving the data of above plots to AFU or CSV files, user could specify the indexes of the section data.
                        
                    
         Returns sectionDataIndices (List[int]): .
        """
        pass
    def SetSectionDataIndices(self, sectionDataIndices: List[int]) -> None:
        """
         Sets the section data index vector.
                        
                        For CAE.Xyplot.PlotType.PlotColorMap,
                        CAE.Xyplot.PlotType.Plot3D,
                        and CAE.Xyplot.PlotType.PlotMatrix2D,
                        the plot data is composed with multiple section data.
                        When saving the data of above plots to AFU or CSV files, user could specify the indexes of the section data.
                        
                    
        """
        pass
import NXOpen
class StackedPlot(Plot): 
    """  Manages the display of stacked plot.
        
        Call CAE.Xyplot.I2DDataPlot.EditRecord to edit data for this class.
         """
    def GetPostEnvironmentSettingsOfSubplot(self, plotIndex: int) -> NXOpen.TaggedObject:
        """
         Gets the post environment settings of specific sub plot. 
         Returns postEnvironmentSettings ( NXOpen.TaggedObject):  .
        """
        pass
    def GetSubplotCount(self) -> int:
        """
         Get sub plot count in the plot.
         Returns subplotCount (int):  Sub plot count .
        """
        pass
class SurfaceColorOption(Enum):
    """
    Members Include: 
     |NotSet|  No shading 
     |Hidden|  Background color as fill 
     |Shaded|  Fill Color or contour color with shading 

    """
    NotSet: int
    Hidden: int
    Shaded: int
    @staticmethod
    def ValueOf(value: int) -> SurfaceColorOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SurfaceStyleSetting(BaseSymbolStyleSetting): 
    """ Represents the surface display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def ColorOption(self) -> SurfaceColorOption:
        """
        Getter for property: ( SurfaceColorOption NXOpen.C) ColorOption
         Returns the color option   
            
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: SurfaceColorOption):
        """
        Setter for property: ( SurfaceColorOption NXOpen.C) ColorOption
         Returns the color option   
            
         
        """
        pass
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FillingColor
         Returns the filling color   
            
         
        """
        pass
    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FillingColor
         Returns the filling color   
            
         
        """
        pass
    @property
    def OutlineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OutlineColor
         Returns the outline color   
            
         
        """
        pass
    @OutlineColor.setter
    def OutlineColor(self, outlineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OutlineColor
         Returns the outline color   
            
         
        """
        pass
class TextAlignment(Enum):
    """
    Members Include: 
     |Left|  Left align text 
     |Center|  Center align text 
     |Right|  Right align text 

    """
    Left: int
    Center: int
    Right: int
    @staticmethod
    def ValueOf(value: int) -> TextAlignment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class TextBoxCornerType(Enum):
    """
    Members Include: 
     |Center| 
     |LowerLeft| 
     |LowerRight| 
     |UpperLeft| 
     |UpperRight| 

    """
    Center: int
    LowerLeft: int
    LowerRight: int
    UpperLeft: int
    UpperRight: int
    @staticmethod
    def ValueOf(value: int) -> TextBoxCornerType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class TextBoxMarginOption(Enum):
    """
    Members Include: 
     |Left|  The left margin of text box     
     |Top|  The top margin of text box     
     |Right|  The right margin of text box    
     |Bottom|  The bottom margin of text box   

    """
    Left: int
    Top: int
    Right: int
    Bottom: int
    @staticmethod
    def ValueOf(value: int) -> TextBoxMarginOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class TextBoxStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the text box display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified."""
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the text box outline color  
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the text box outline color  
            
         
        """
        pass
    @property
    def FillingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FillingColor
         Returns the text box filling color  
            
         
        """
        pass
    @FillingColor.setter
    def FillingColor(self, fillingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FillingColor
         Returns the text box filling color  
            
         
        """
        pass
    @property
    def IsFilled(self) -> bool:
        """
        Getter for property: (bool) IsFilled
         Returns a value indicating whether to fill the text box   
            
         
        """
        pass
    @IsFilled.setter
    def IsFilled(self, isFilled: bool):
        """
        Setter for property: (bool) IsFilled
         Returns a value indicating whether to fill the text box   
            
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns a value indicating whether to display the text box   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns a value indicating whether to display the text box   
            
         
        """
        pass
    def GetLineStyle(self) -> CurveDisplaySettings:
        """
         Gets the text box line style
         Returns boxLineStyle ( CurveDisplaySettings NXOpen.C):   .
        """
        pass
    def GetMargin(self, marginOption: TextBoxMarginOption) -> float:
        """
        Gets the margin value of text box 
         Returns marginValue (float):   .
        """
        pass
    def SetMargin(self, marginOption: TextBoxMarginOption, marginValue: float) -> None:
        """
        Sets the margin value of text box 
        """
        pass
class TextOrientation(Enum):
    """
    Members Include: 
     |Horizontal|  Horizontal text orientation 
     |Upward|  Upward text orientation 
     |Downward|  Downward text orientation 

    """
    Horizontal: int
    Upward: int
    Downward: int
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
class TextStyleSetting(BaseDisplayStyleSetting): 
    """ Represents the text display style. Call CAE.Xyplot.BaseDisplayStyleSetting.CommitChange
            to apply style changes to corresponding plot after it's modified.
        """
    @property
    def Alignment(self) -> TextAlignment:
        """
        Getter for property: ( TextAlignment NXOpen.C) Alignment
         Returns the text alignment.  
           Only valid for title options, legend options and axis label options.   
         
        """
        pass
    @Alignment.setter
    def Alignment(self, alignment: TextAlignment):
        """
        Setter for property: ( TextAlignment NXOpen.C) Alignment
         Returns the text alignment.  
           Only valid for title options, legend options and axis label options.   
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the text color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the text color   
            
         
        """
        pass
    @property
    def Font(self) -> str:
        """
        Getter for property: (str) Font
         Returns the text font   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: str):
        """
        Setter for property: (str) Font
         Returns the text font   
            
         
        """
        pass
    @property
    def FontStyle(self) -> NXOpen.Preferences.VisualizationFonts.StyleType:
        """
        Getter for property: ( NXOpen.Preferences.VisualizationFonts.StyleType) FontStyle
         Returns the text font style.  
           Available when the text font is standard font.   
         
        """
        pass
    @FontStyle.setter
    def FontStyle(self, fontStyle: NXOpen.Preferences.VisualizationFonts.StyleType):
        """
        Setter for property: ( NXOpen.Preferences.VisualizationFonts.StyleType) FontStyle
         Returns the text font style.  
           Available when the text font is standard font.   
         
        """
        pass
    @property
    def FontType(self) -> Fonttype:
        """
        Getter for property: ( Fonttype NXOpen.C) FontType
         Returns the text font type   
            
         
        """
        pass
    @FontType.setter
    def FontType(self, fontType: Fonttype):
        """
        Setter for property: ( Fonttype NXOpen.C) FontType
         Returns the text font type   
            
         
        """
        pass
    @property
    def GlobalSizeScale(self) -> float:
        """
        Getter for property: (float) GlobalSizeScale
         Returns the scale of global text size.  
          
                        It will be taken only when  CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting  is true,
                        and  CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled  is false.   
         
        """
        pass
    @GlobalSizeScale.setter
    def GlobalSizeScale(self, sizeScale: float):
        """
        Setter for property: (float) GlobalSizeScale
         Returns the scale of global text size.  
          
                        It will be taken only when  CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting  is true,
                        and  CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled  is false.   
         
        """
        pass
    @property
    def IsGlobalSizeAutoScaled(self) -> bool:
        """
        Getter for property: (bool) IsGlobalSizeAutoScaled
         Returns a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
          
                        It will be taken only when  CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting  is true.   
         
        """
        pass
    @IsGlobalSizeAutoScaled.setter
    def IsGlobalSizeAutoScaled(self, isGlobalSizeAutoScaled: bool):
        """
        Setter for property: (bool) IsGlobalSizeAutoScaled
         Returns a value indicating whether to automatically adjust the scale of global text size to fit the screen.  
          
                        It will be taken only when  CAE::Xyplot::TextStyleSetting::UseGlobalFontSetting  is true.   
         
        """
        pass
    @property
    def LeaderStyle(self) -> LeaderStyle:
        """
        Getter for property: ( LeaderStyle NXOpen.C) LeaderStyle
         Returns the leader style   
            
         
        """
        pass
    @property
    def NumberFormat(self) -> NXOpen.CAE.NumberFormat:
        """
        Getter for property: ( NXOpen.CAE.NumberFormat) NumberFormat
         Returns the number format options   
            
         
        """
        pass
    @property
    def Orientation(self) -> TextOrientation:
        """
        Getter for property: ( TextOrientation NXOpen.C) Orientation
         Returns the text orientation.  
           Only invalid for legend options.   
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: TextOrientation):
        """
        Setter for property: ( TextOrientation NXOpen.C) Orientation
         Returns the text orientation.  
           Only invalid for legend options.   
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the text size.  
           The acceptable range is 1-10.   
         
        """
        pass
    @Size.setter
    def Size(self, size: int):
        """
        Setter for property: (int) Size
         Returns the text size.  
           The acceptable range is 1-10.   
         
        """
        pass
    @property
    def TextBoxStyle(self) -> TextBoxStyleSetting:
        """
        Getter for property: ( TextBoxStyleSetting NXOpen.C) TextBoxStyle
         Returns the style of text box   
            
         
        """
        pass
    @property
    def UseGlobalFontSetting(self) -> bool:
        """
        Getter for property: (bool) UseGlobalFontSetting
         Returns a value indicating whether to use the global setting of text font, font style and font size.  
          
                        If True, you need to set text size scale by setting  CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled  or
                         CAE::Xyplot::TextStyleSetting::GlobalSizeScale    
         
        """
        pass
    @UseGlobalFontSetting.setter
    def UseGlobalFontSetting(self, useGlobalFontSetting: bool):
        """
        Setter for property: (bool) UseGlobalFontSetting
         Returns a value indicating whether to use the global setting of text font, font style and font size.  
          
                        If True, you need to set text size scale by setting  CAE::Xyplot::TextStyleSetting::IsGlobalSizeAutoScaled  or
                         CAE::Xyplot::TextStyleSetting::GlobalSizeScale    
         
        """
        pass
    @property
    def Visibility(self) -> bool:
        """
        Getter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @Visibility.setter
    def Visibility(self, visibility: bool):
        """
        Setter for property: (bool) Visibility
         Returns the visibility   
            
         
        """
        pass
    @property
    def Weight(self) -> NXOpen.Display.TransientText.TextSize:
        """
        Getter for property: ( NXOpen.Display.TransientText.TextSize) Weight
         Returns the text weight.  
           Available when the text font is NX font.   
         
        """
        pass
    @Weight.setter
    def Weight(self, weight: NXOpen.Display.TransientText.TextSize):
        """
        Setter for property: ( NXOpen.Display.TransientText.TextSize) Weight
         Returns the text weight.  
           Available when the text font is NX font.   
         
        """
        pass
class TextType(Enum):
    """
    Members Include: 
     |NotSet|  Not defined type 
     |Title|  Title label 
     |Legend|  Legend label 
     |GraphName|  Graph name label 
     |PageNumber|  Page number label 
     |Marker|  Marker label 
     |Note|  Note label 
     |ProbingText|  Probing label 
     |XLabel|  X Axis name label 
     |YLabel|  Y Axis name label 
     |ZLabel|  Z Axis name label 
     |XNumber|  X Axis number label 
     |YNumber|  Y Axis number label 
     |ZNumber|  Z Axis number label 
     |ColorAxisLabel|  Color Axis name label  
     |ColorAxisNumber|  Color Axis name number 
     |UnknownResultText|  Obsoleted in NX13  
     |AngleAxisNumber|  Angle Axis name number 
     |AnnotationText|  Annotation text in vector plot 
     |ArgumentAxisNumber|  Argument Axis number label 
     |BarChartValueText|  Bar Chart Value text 
     |LegendTableText|  Legend Table text 
     |ResultLegendText|  Result legend text, including unknown, overflow, underflow result  
     |FormulaGridValueText|  Formula Grid Value text 
     |MatrixValueText|  Matrix Value Text 

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
    @staticmethod
    def ValueOf(value: int) -> TextType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class UnknownResultColor(Enum):
    """
    Members Include: 
     |White|  white 
     |Grey|  grey 

    """
    White: int
    Grey: int
    @staticmethod
    def ValueOf(value: int) -> UnknownResultColor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class VectorStyle2DSetting(BaseLineStyleSetting): 
    """ Represents the 2D vector display style. """
    @property
    def DrawText(self) -> bool:
        """
        Getter for property: (bool) DrawText
         Returns a value indicating whether to draw annotation text   
            
         
        """
        pass
    @DrawText.setter
    def DrawText(self, canDrawText: bool):
        """
        Setter for property: (bool) DrawText
         Returns a value indicating whether to draw annotation text   
            
         
        """
        pass
    @property
    def IsAutoTextCount(self) -> bool:
        """
        Getter for property: (bool) IsAutoTextCount
         Returns a value indicating whether to customize annotation text count   
            
         
        """
        pass
    @IsAutoTextCount.setter
    def IsAutoTextCount(self, isAutoTextCount: bool):
        """
        Setter for property: (bool) IsAutoTextCount
         Returns a value indicating whether to customize annotation text count   
            
         
        """
        pass
    @property
    def MaximumTextCount(self) -> int:
        """
        Getter for property: (int) MaximumTextCount
         Returns the maximum of customized text count   
            
         
        """
        pass
    @MaximumTextCount.setter
    def MaximumTextCount(self, maximumTextCount: int):
        """
        Setter for property: (int) MaximumTextCount
         Returns the maximum of customized text count   
            
         
        """
        pass
    @property
    def OverlapTextAndVector(self) -> bool:
        """
        Getter for property: (bool) OverlapTextAndVector
         Returns a value indicating whether to allow the annotation text overlap with vector   
            
         
        """
        pass
    @OverlapTextAndVector.setter
    def OverlapTextAndVector(self, overlapTextAndVector: bool):
        """
        Setter for property: (bool) OverlapTextAndVector
         Returns a value indicating whether to allow the annotation text overlap with vector   
            
         
        """
        pass
    def GetNthVectorColor(self, index: int) -> NXOpen.NXColor:
        """
         Get the nth vector display color 
         Returns vectorColor ( NXOpen.NXColor):  Get the nth display vector color .
        """
        pass
    def GetVectorColors(self) -> List[NXOpen.NXColor]:
        """
         Get the vector display colors 
         Returns vectorColors ( NXOpen.NXColor Li):  Get the display vector colors .
        """
        pass
    def SetNthVectorColors(self, index: int, vectorColors: NXOpen.NXColor) -> None:
        """
         Set the nth vector display color 
        """
        pass
    def SetVectorColors(self, vectorColors: List[NXOpen.NXColor]) -> None:
        """
         Set the vector display colors 
        """
        pass
class WallDisplayStyles2D(WallDisplayStyles): 
    """ Manages the 2D wall display styles. """
    def GetAngleAxisStyleSetting(self) -> AngleAxisStyleSetting:
        """
         Gets the angle axis display style. 
         Returns angleAxisStyle ( AngleAxisStyleSetting NXOpen.C):  Angle Axis style .
        """
        pass
    def GetFormulaGridStyle(self) -> FormulaGridStyle:
        """
         Gets the formula grid style. 
         Returns formulaGridStyle ( FormulaGridStyle NXOpen.C):  Formula Grid style .
        """
        pass
import NXOpen
class WallDisplayStyles3D(WallDisplayStyles): 
    """ Manages the 3D wall display styles. """
    @property
    def ViewOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) ViewOrientation
         Returns the view orientation matrix   
            
         
        """
        pass
    @ViewOrientation.setter
    def ViewOrientation(self, orientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) ViewOrientation
         Returns the view orientation matrix   
            
         
        """
        pass
import NXOpen
class WallDisplayStyles(NXOpen.TaggedObject): 
    """ Manages the wall display styles. """
    @property
    def GridLayoutStyleSetting(self) -> BaseGridLayoutStyleSetting:
        """
        Getter for property: ( BaseGridLayoutStyleSetting NXOpen.C) GridLayoutStyleSetting
         Returns the grid layout display style   
            
         
        """
        pass
    @property
    def ProbingStyle(self) -> ProbingStyle:
        """
        Getter for property: ( ProbingStyle NXOpen.C) ProbingStyle
         Returns the probing display style   
            
         
        """
        pass
    def GetAxisStyle(self, axisDirection: AxisDirection) -> IAxisStyle:
        """
         Gets the axis display style. 
         Returns axisStyle ( IAxisStyle NXOpen.C):  Axis style .
        """
        pass
    def GetCalculationLegendTableStyle(self) -> LegendTableStyle:
        """
        Gets the calculation legend table style 
         Returns legendTableStyle ( LegendTableStyle NXOpen.C): .
        """
        pass
    def GetLegendTableGroupStyle(self) -> LegendTableGroupStyle:
        """
        Gets the legend table group style 
         Returns legendTableGroupStyle ( LegendTableGroupStyle NXOpen.C):  Legend table group style .
        """
        pass
    def GetTextStyleSetting(self, textType: TextType) -> TextStyleSetting:
        """
         Gets the text style. 
         Returns textStyle ( TextStyleSetting NXOpen.C):  Text display style .
        """
        pass
import NXOpen
class WindowManager(NXOpen.Object): 
    """ Manages the separate graphic windows. The value of device index is greater than 0.
            This class is restricted to being called from a program running during an interactive NX session.
            If run from a non-interactive session it will return . """
    def CloseWindow(deviceIndex: int) -> None:
        """
         Closes the window of specified device index. 
        """
        pass
    def GetWindowTitle(deviceIndex: int) -> str:
        """
         Gets the graphics window title. 
         Returns windowTitle (str): .
        """
        pass
    def GetWindows() -> List[int]:
        """
         Gets the device indices of all the graphic windows. 
         Returns deviceIndices (List[int]): .
        """
        pass
    def NewWindow() -> int:
        """
         Creates a new window and returns the device index. 
         Returns deviceIndex (int):   .
        """
        pass
    def SetWindowTitle(deviceIndex: int, windowTitle: str) -> None:
        """
         Sets the graphics window title. 
        """
        pass
class XYFunctionDataAccessor(IFunctionDataAccessor): 
    """  Represents a data accessor to retrieve data of a function which is plotted in 2D graphs or Color Bar graphs.  """
    def AskDisplayData(self) -> Tuple[List[float], List[float]]:
        """
         Asks display data. 
         Returns A tuple consisting of (indenpendentValue, dependentValue). 
         - indenpendentValue is: List[float].
         - dependentValue is: List[float].

        """
        pass
import NXOpen
class XYPlotManager(NXOpen.Object): 
    """ XYPlot function manager """
    @property
    def Preference(self) -> Preference:
        """
        Getter for property: ( Preference NXOpen.C) Preference
         Returns the preference   
            
         
        """
        pass
    @property
    def TemplateManager(self) -> BaseTemplateManager:
        """
        Getter for property: ( BaseTemplateManager NXOpen.C) TemplateManager
         Returns the template manager.  
             
         
        """
        pass
    @property
    def WindowManager() -> WindowManager:
        """
         Returns the  NXOpen::CAE::Xyplot::WindowManager  belonging.
                        This class is restricted to being called from a program running during an interactive NX session.
                        If run from a non-interactive session it will return NULL. 
        """
        pass
    @property
    def DataExporter() -> DataExporter:
        """
         Returns the  NXOpen::CAE::Xyplot::DataExporter  belonging. 
        """
        pass
    @property
    def AutotestUtils() -> AutotestUtils:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    def AlignAxesOfPlots(part: NXOpen.BasePart) -> None:
        """
         Aligns axes of all plots. 
                        Ensures that all axes of a certain quantity (force, displacement, etc.) and 
                        data type (real, imaginary, magnitude, etc.) have the same unit, axis type and limits. 
                        This API only valid for Motion and Prepost application
        """
        pass
    def CreateResultAccessor(plot: Plot) -> ResultAccessor:
        """
         Creates a new NXOpen.CAE.Xyplot.ResultAccessor object.
         Returns accessor ( ResultAccessor NXOpen.C):   .
        """
        pass
    def CreateResultAccessorOnCanvas(plot: Plot, canvasIndex: int) -> ResultAccessor:
        """
         Creates a new NXOpen.CAE.Xyplot.ResultAccessor object.
                        
                        Plots may have one or more canvases. Commonly, there is only one canvas that contains multiple graphs. But there are plots --such as stacked plots-- 
                        that have multiple canvases. The number of graphs per canvas depends on display options.
                        
                      
         Returns accessor ( ResultAccessor NXOpen.C):   .
        """
        pass
    def FindObject(journalIdentifier: str) -> Plot:
        """
         Finds the CAE.Xyplot.Plot with the given identifier as recorded in a journal
         Returns plot ( Plot NXOpen.C):  Plot object found, or null if no such plot exists .
        """
        pass
    def GetAvailableWindowDevices() -> List[int]:
        """
         Gets all window devices on which XY graph could be plotted 
         Returns pWinDevices (List[int]):  Available Plot Winodw Devices .
        """
        pass
    def GetCurrentPlot(deviceIndex: int, viewIndex: int) -> Plot:
        """
         Gets the current plot on the view port of specific device 
         Returns currentPlot ( Plot NXOpen.C):  Current plot .
        """
        pass
    def GetPlots(windowDevice: int, view: int) -> List[Plot]:
        """
         Gets all plots on a view of specified window device 
         Returns plots ( Plot List[NXOpen):  Plots      .
        """
        pass
    def GetWindowDevicesViews(windowDevice: int) -> List[int]:
        """
         Gets view count and views for specified window device 
         Returns pViewsOnDevice (List[int]):  the views on window device.
        """
        pass
    def MakeCurrentPlot(plot: Plot) -> None:
        """
         Turns the page of the given plot as current page. 
        """
        pass
    def NewOverlayParameters() -> OverlayParameters:
        """
         Creates an transient object  NXOpen.CAE.Xyplot.PlotParameters  to contain the settings
                        required by overlaying new records on a plot. The object should be destroyed after overlaying plot is created. 
         Returns overlayParameters ( OverlayParameters NXOpen.C):  the overlay parameters object created .
        """
        pass
    def NewPlotParameters() -> PlotParameters:
        """
         Creates an transient object  NXOpen.CAE.Xyplot.PlotParameters  to contain the
                        settings required by creating a plot. The object should be destroyed after plot is created. 
         Returns plotParameters ( PlotParameters NXOpen.C):  the plot parameters object created .
        """
        pass
    def OverlayRecords(overlayParameters: OverlayParameters) -> Plot:
        """
         Overlay records with given parameters 
         Returns plot ( Plot NXOpen.C):  Overlayed plot .
        """
        pass
    def PlotRecords(plotParameters: PlotParameters) -> Plot:
        """
         Creates plot with given parameters 
         Returns plot ( Plot NXOpen.C):  Created plot .
        """
        pass
    def ReturnToModelView(view: int) -> None:
        """
         Clears all plots on a view of main graphics windows and returns to model view
        """
        pass
    def ShowNextPlot(deviceIndex: int, viewIndex: int) -> None:
        """
         Shows the next plot on the view port of specific device 
        """
        pass
    def ShowPreviousPlot(deviceIndex: int, viewIndex: int) -> None:
        """
         Shows the previous plot on the view port of specific device 
        """
        pass
    def WriteImageToClipBoard(deviceIndex: int, viewIndex: int, isUseWhiteBackGround: bool) -> None:
        """
         Write the image of current plot on a view to Windows's ClipBoard
        """
        pass
class XYZFunctionDataAccessor(IFunctionDataAccessor): 
    """  Represents a data accessor to retrieve data of a function which is plotted in 3D graphs or Color Map graphs.  """
    def AskSectionCount(self) -> int:
        """
         Asks section count. 
         Returns sectionCount (int): .
        """
        pass
    def AskSectionDisplayData(self, sectionIndex: int) -> Tuple[List[float], float, List[float]]:
        """
         Asks display data. 
         Returns A tuple consisting of (indenpendent1Values, indenpendent2Value, dependentValues). 
         - indenpendent1Values is: List[float].
         - indenpendent2Value is: float.
         - dependentValues is: List[float].

        """
        pass
