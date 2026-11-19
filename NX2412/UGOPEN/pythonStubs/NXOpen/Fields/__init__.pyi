from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ComplexScalarFieldWrapper(NXOpen.NXObject): 
    """ This class defines a complex value that is internally 
        backed up by a  field or two expressions. """
    def GetExpression(self) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         Returns expression ( NXOpen.Expression):  existing expression or NULL .
        """
        pass
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field; 
                    NULL otherwise 
         Returns field ( Field NXOpen):  existing field or NULL .
        """
        pass
    def GetImaginaryExpression(self) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         Returns expression ( NXOpen.Expression):  existing expression or NULL .
        """
        pass
    def SetExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    def SetExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    def SetField(self, field: Field) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    def SetFieldWithScaleFactor(self, field: Field, scale_factor: float) -> None:
        """
         Sets the implementation of the wrapper to the specified field and scale factor 
        """
        pass
    def SetImaginaryExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    def SetMagnitudePhaseExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    def SetRealImaginaryExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
import NXOpen
class ComplexVectorFieldWrapper(NXOpen.NXObject): 
    """ This class defines a complex value that is internally 
        backed up by a  field or six expressions. """
    def GetExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         Returns expression ( NXOpen.Expression):  existing expression or NULL .
        """
        pass
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field; 
                    NULL otherwise 
         Returns field ( Field NXOpen):  existing field or NULL .
        """
        pass
    def GetImaginaryExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         Returns expression ( NXOpen.Expression):  existing expression or NULL .
        """
        pass
    def SetExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    def SetField(self, field: Field, scale_factor: float) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
    def SetImaginaryExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
import NXOpen
class DisplayPropertiesBuilder(NXOpen.Builder): 
    """  Represents a builder class for editing display properties of a NXOpen.Fields.Field 
    Used to edit a NXOpen.Fields.Field display properties.
    """
    class BalStrainType(Enum):
        """
        Members Include: 
         |Xx| 
         |Yy| 
         |Zz| 
         |Xy| 
         |Yz| 
         |Zx| 
         |OffSetXX| 
         |OffSetYY| 
         |OffSetZZ| 
         |OffSetXY| 
         |OffSetYZ| 
         |OffSetZX| 

        """
        Xx: int
        Yy: int
        Zz: int
        Xy: int
        Yz: int
        Zx: int
        OffSetXX: int
        OffSetYY: int
        OffSetZZ: int
        OffSetXY: int
        OffSetYZ: int
        OffSetZX: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.BalStrainType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComplexScalarType(Enum):
        """
        Members Include: 
         |Mag| 
         |Real| 
         |Imaginary| 
         |Phase| 

        """
        Mag: int
        Real: int
        Imaginary: int
        Phase: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ComplexScalarType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComplexVectorType(Enum):
        """
        Members Include: 
         |XReal| 
         |YReal| 
         |ZReal| 
         |XImaginary| 
         |YImaginary| 
         |ZImaginary| 

        """
        XReal: int
        YReal: int
        ZReal: int
        XImaginary: int
        YImaginary: int
        ZImaginary: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ComplexVectorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DepDispTypeEnum(Enum):
        """
        Members Include: 
         |Symbol| 
         |Surface| 
         |SurfaceEdges| 
         |Hide| 

        """
        Symbol: int
        Surface: int
        SurfaceEdges: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DepDispTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DepDomColorEnum(Enum):
        """
        Members Include: 
         |Inherit| 
         |Specified| 
         |Spectrum| 

        """
        Inherit: int
        Specified: int
        Spectrum: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DepDomColorEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DepLabelValueEnum(Enum):
        """
        Members Include: 
         |NotSet| 
         |MinimumMaximum| 
         |Maximum| 
         |Minimum| 
         |All| 

        """
        NotSet: int
        MinimumMaximum: int
        Maximum: int
        Minimum: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DepLabelValueEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DispResolutionEnum(Enum):
        """
        Members Include: 
         |Coarse| 
         |Standard| 
         |Fine| 
         |ExtraFine| 
         |SuperFine| 
         |UltraFine| 
         |UserSpecified| 

        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        UserSpecified: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.DispResolutionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FieldQuantityType(Enum):
        """
        Members Include: 
         |Type0| 
         |Type1| 
         |Type2| 
         |Type3| 
         |Type4| 
         |Type5| 
         |Type6| 
         |Type7| 
         |Type8| 
         |Type9| 
         |Type10| 
         |Type11| 
         |Type12| 
         |Type13| 
         |Type14| 
         |Type15| 

        """
        Type0: int
        Type1: int
        Type2: int
        Type3: int
        Type4: int
        Type5: int
        Type6: int
        Type7: int
        Type8: int
        Type9: int
        Type10: int
        Type11: int
        Type12: int
        Type13: int
        Type14: int
        Type15: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.FieldQuantityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HeteroTblDispOptionEnum(Enum):
        """
        Members Include: 
         |ShowAverageValue| 
         |PrimaryVarValues| 
         |Show1StValue| 
         |ShowLastValue| 
         |ShowMinimumValue| 
         |ShowMaximumValue| 
         |Hide| 

        """
        ShowAverageValue: int
        PrimaryVarValues: int
        Show1StValue: int
        ShowLastValue: int
        ShowMinimumValue: int
        ShowMaximumValue: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.HeteroTblDispOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IndepDomDispType(Enum):
        """
        Members Include: 
         |Normal| 
         |Point| 
         |PlusSign| 
         |Asterisk| 
         |Circle| 
         |PoundSign| 
         |Cross| 
         |Square| 
         |Triangle| 
         |Diamond| 
         |Centerline| 
         |Hide| 

        """
        Normal: int
        Point: int
        PlusSign: int
        Asterisk: int
        Circle: int
        PoundSign: int
        Cross: int
        Square: int
        Triangle: int
        Diamond: int
        Centerline: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.IndepDomDispType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Legacy3DType(Enum):
        """
        Members Include: 
         |X| 
         |Y| 
         |Z| 

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.Legacy3DType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LegendPos(Enum):
        """
        Members Include: 
         |Hide| 
         |Left| 
         |Right| 

        """
        Hide: int
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.LegendPos:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineFontEnum(Enum):
        """
        Members Include: 
         |Solid|  Solid 
         |Dashed|  Dashed 
         |Phantom|  Phantom 
         |Centerline|  Centerline 
         |Dotted|  Dotted 
         |LongDashed|  LongDashed 
         |DottedDashed|  DottedDashed 
         |Eight|  LongDashedDoubleDotted
         |Nine|  LongDashedDotted for OOTB Fonts and Undulating for shipbuilding fonts 
         |Ten|  LongDashedTriplicateDotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  LongDashedDoubleShortDashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        LongDashed: int
        DottedDashed: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.LineFontEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineWidthEnum(Enum):
        """
        Members Include: 
         |Normal| 
         |Thick| 
         |Thin| 
         |One| 
         |Two| 
         |Three| 
         |Four| 
         |Five| 
         |Six| 
         |Seven| 
         |Eight| 
         |Nine| 

        """
        Normal: int
        Thick: int
        Thin: int
        One: int
        Two: int
        Three: int
        Four: int
        Five: int
        Six: int
        Seven: int
        Eight: int
        Nine: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.LineWidthEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalarType(Enum):
        """
        Members Include: 
         |Hide| 
         |Mag| 

        """
        Hide: int
        Mag: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ScalarType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TblPointTypeEnum(Enum):
        """
        Members Include: 
         |Hide| 
         |Show| 

        """
        Hide: int
        Show: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.TblPointTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TensorType(Enum):
        """
        Members Include: 
         |Xx| 
         |Yy| 
         |Zz| 
         |Xy| 
         |Yz| 
         |Zx| 
         |Mean| 
         |MidPrncpl| 
         |MinPrncpl| 
         |MaxPrncpl| 
         |Octahedral| 
         |VonMises| 

        """
        Xx: int
        Yy: int
        Zz: int
        Xy: int
        Yz: int
        Zx: int
        Mean: int
        MidPrncpl: int
        MinPrncpl: int
        MaxPrncpl: int
        Octahedral: int
        VonMises: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.TensorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValueRange(Enum):
        """
        Members Include: 
         |Auto| 
         |Specified| 

        """
        Auto: int
        Specified: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ValueRange:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValuesEnum(Enum):
        """
        Members Include: 
         |Hide| 
         |Point| 
         |PlusSign| 
         |Asterisk| 
         |Circle| 
         |PoundSign| 
         |Cross| 
         |Square| 
         |Triangle| 
         |Diamond| 
         |Centerline| 

        """
        Hide: int
        Point: int
        PlusSign: int
        Asterisk: int
        Circle: int
        PoundSign: int
        Cross: int
        Square: int
        Triangle: int
        Diamond: int
        Centerline: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.ValuesEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VectorType(Enum):
        """
        Members Include: 
         |X| 
         |Y| 
         |Z| 
         |Mag| 

        """
        X: int
        Y: int
        Z: int
        Mag: int
        @staticmethod
        def ValueOf(value: int) -> DisplayPropertiesBuilder.VectorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AxisColor
         Returns the axis color   
            
         
        """
        pass
    @AxisColor.setter
    def AxisColor(self, axisColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AxisColor
         Returns the axis color   
            
         
        """
        pass
    @property
    def BasicColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BasicColor
         Returns the basic color   
            
         
        """
        pass
    @BasicColor.setter
    def BasicColor(self, basicColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BasicColor
         Returns the basic color   
            
         
        """
        pass
    @property
    def DepCalcSymblSize(self) -> float:
        """
        Getter for property: (float) DepCalcSymblSize
         Returns the dep calc symbl size   
            
         
        """
        pass
    @DepCalcSymblSize.setter
    def DepCalcSymblSize(self, depCalcSymblSize: float):
        """
        Setter for property: (float) DepCalcSymblSize
         Returns the dep calc symbl size   
            
         
        """
        pass
    @property
    def DepDispType(self) -> DisplayPropertiesBuilder.DepDispTypeEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DepDispTypeEnum NXOpen) DepDispType
         Returns the dep disp type   
            
         
        """
        pass
    @DepDispType.setter
    def DepDispType(self, depDispType: DisplayPropertiesBuilder.DepDispTypeEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DepDispTypeEnum NXOpen) DepDispType
         Returns the dep disp type   
            
         
        """
        pass
    @property
    def DepDomColor(self) -> DisplayPropertiesBuilder.DepDomColorEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DepDomColorEnum NXOpen) DepDomColor
         Returns the dep dom color   
            
         
        """
        pass
    @DepDomColor.setter
    def DepDomColor(self, depDomColor: DisplayPropertiesBuilder.DepDomColorEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DepDomColorEnum NXOpen) DepDomColor
         Returns the dep dom color   
            
         
        """
        pass
    @property
    def DepLabelValues(self) -> DisplayPropertiesBuilder.DepLabelValueEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DepLabelValueEnum NXOpen) DepLabelValues
         Returns the dep label values   
            
         
        """
        pass
    @DepLabelValues.setter
    def DepLabelValues(self, depLabelValues: DisplayPropertiesBuilder.DepLabelValueEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DepLabelValueEnum NXOpen) DepLabelValues
         Returns the dep label values   
            
         
        """
        pass
    @property
    def DepRangeMax(self) -> float:
        """
        Getter for property: (float) DepRangeMax
         Returns the dep range max   
            
         
        """
        pass
    @DepRangeMax.setter
    def DepRangeMax(self, depRangeMax: float):
        """
        Setter for property: (float) DepRangeMax
         Returns the dep range max   
            
         
        """
        pass
    @property
    def DepRangeMin(self) -> float:
        """
        Getter for property: (float) DepRangeMin
         Returns the dependent range min   
            
         
        """
        pass
    @DepRangeMin.setter
    def DepRangeMin(self, depRangeMin: float):
        """
        Setter for property: (float) DepRangeMin
         Returns the dependent range min   
            
         
        """
        pass
    @property
    def DepSelColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) DepSelColor
         Returns the dep sel color   
            
         
        """
        pass
    @DepSelColor.setter
    def DepSelColor(self, depSelColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) DepSelColor
         Returns the dep sel color   
            
         
        """
        pass
    @property
    def DepSymbolSize(self) -> float:
        """
        Getter for property: (float) DepSymbolSize
         Returns the dep symbol size   
            
         
        """
        pass
    @DepSymbolSize.setter
    def DepSymbolSize(self, depSymbolSize: float):
        """
        Setter for property: (float) DepSymbolSize
         Returns the dep symbol size   
            
         
        """
        pass
    @property
    def DisplayResolution(self) -> DisplayPropertiesBuilder.DispResolutionEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DispResolutionEnum NXOpen) DisplayResolution
         Returns the display resolution   
            
         
        """
        pass
    @DisplayResolution.setter
    def DisplayResolution(self, displayResolution: DisplayPropertiesBuilder.DispResolutionEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DispResolutionEnum NXOpen) DisplayResolution
         Returns the display resolution   
            
         
        """
        pass
    @property
    def DummyScale(self) -> float:
        """
        Getter for property: (float) DummyScale
         Returns the dummy scale   
            
         
        """
        pass
    @DummyScale.setter
    def DummyScale(self, dummyScale: float):
        """
        Setter for property: (float) DummyScale
         Returns the dummy scale   
            
         
        """
        pass
    @property
    def FaceAnalysis(self) -> bool:
        """
        Getter for property: (bool) FaceAnalysis
         Returns the face analysis   
            
         
        """
        pass
    @FaceAnalysis.setter
    def FaceAnalysis(self, faceAnalysis: bool):
        """
        Setter for property: (bool) FaceAnalysis
         Returns the face analysis   
            
         
        """
        pass
    @property
    def FieldQuantity(self) -> DisplayPropertiesBuilder.FieldQuantityType:
        """
        Getter for property: ( DisplayPropertiesBuilder.FieldQuantityType NXOpen) FieldQuantity
         Returns the field quantity type  
            
         
        """
        pass
    @FieldQuantity.setter
    def FieldQuantity(self, fieldQuantity: DisplayPropertiesBuilder.FieldQuantityType):
        """
        Setter for property: ( DisplayPropertiesBuilder.FieldQuantityType NXOpen) FieldQuantity
         Returns the field quantity type  
            
         
        """
        pass
    @property
    def HeteroTblDispOption(self) -> DisplayPropertiesBuilder.HeteroTblDispOptionEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen) HeteroTblDispOption
         Returns the heterogeneous table values display option   
            
         
        """
        pass
    @HeteroTblDispOption.setter
    def HeteroTblDispOption(self, hetTblValDispOption: DisplayPropertiesBuilder.HeteroTblDispOptionEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.HeteroTblDispOptionEnum NXOpen) HeteroTblDispOption
         Returns the heterogeneous table values display option   
            
         
        """
        pass
    @property
    def IndepDispType(self) -> DisplayPropertiesBuilder.IndepDomDispType:
        """
        Getter for property: ( DisplayPropertiesBuilder.IndepDomDispType NXOpen) IndepDispType
         Returns the indep disp type   
            
         
        """
        pass
    @IndepDispType.setter
    def IndepDispType(self, indepDispType: DisplayPropertiesBuilder.IndepDomDispType):
        """
        Setter for property: ( DisplayPropertiesBuilder.IndepDomDispType NXOpen) IndepDispType
         Returns the indep disp type   
            
         
        """
        pass
    @property
    def LabelColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LabelColor
         Returns the label color   
            
         
        """
        pass
    @LabelColor.setter
    def LabelColor(self, labelColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LabelColor
         Returns the label color   
            
         
        """
        pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer   
            
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer   
            
         
        """
        pass
    @property
    def LegendPosition(self) -> DisplayPropertiesBuilder.LegendPos:
        """
        Getter for property: ( DisplayPropertiesBuilder.LegendPos NXOpen) LegendPosition
         Returns the legend position   
            
         
        """
        pass
    @LegendPosition.setter
    def LegendPosition(self, legendPosition: DisplayPropertiesBuilder.LegendPos):
        """
        Setter for property: ( DisplayPropertiesBuilder.LegendPos NXOpen) LegendPosition
         Returns the legend position   
            
         
        """
        pass
    @property
    def LineFont(self) -> DisplayPropertiesBuilder.LineFontEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.LineFontEnum NXOpen) LineFont
         Returns the line font   
            
         
        """
        pass
    @LineFont.setter
    def LineFont(self, lineFont: DisplayPropertiesBuilder.LineFontEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.LineFontEnum NXOpen) LineFont
         Returns the line font   
            
         
        """
        pass
    @property
    def LineWidth(self) -> DisplayPropertiesBuilder.LineWidthEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.LineWidthEnum NXOpen) LineWidth
         Returns the line width   
            
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, lineWidth: DisplayPropertiesBuilder.LineWidthEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.LineWidthEnum NXOpen) LineWidth
         Returns the line width   
            
         
        """
        pass
    @property
    def OverflowColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OverflowColor
         Returns the overflow color   
            
         
        """
        pass
    @OverflowColor.setter
    def OverflowColor(self, overflowColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OverflowColor
         Returns the overflow color   
            
         
        """
        pass
    @property
    def PartiallyShaded(self) -> bool:
        """
        Getter for property: (bool) PartiallyShaded
         Returns the partially shaded   
            
         
        """
        pass
    @PartiallyShaded.setter
    def PartiallyShaded(self, partiallyShaded: bool):
        """
        Setter for property: (bool) PartiallyShaded
         Returns the partially shaded   
            
         
        """
        pass
    @property
    def PrimaryVar(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PrimaryVar
         Returns the primary var name   
            
         
        """
        pass
    @property
    def Range(self) -> DisplayPropertiesBuilder.ValueRange:
        """
        Getter for property: ( DisplayPropertiesBuilder.ValueRange NXOpen) Range
         Returns the range   
            
         
        """
        pass
    @Range.setter
    def Range(self, range: DisplayPropertiesBuilder.ValueRange):
        """
        Setter for property: ( DisplayPropertiesBuilder.ValueRange NXOpen) Range
         Returns the range   
            
         
        """
        pass
    @property
    def RangeMax(self) -> float:
        """
        Getter for property: (float) RangeMax
         Returns the legend range max   
            
         
        """
        pass
    @RangeMax.setter
    def RangeMax(self, rangeMax: float):
        """
        Setter for property: (float) RangeMax
         Returns the legend range max   
            
         
        """
        pass
    @property
    def RangeMin(self) -> float:
        """
        Getter for property: (float) RangeMin
         Returns the legend range min   
            
         
        """
        pass
    @RangeMin.setter
    def RangeMin(self, rangeMin: float):
        """
        Setter for property: (float) RangeMin
         Returns the legend range min   
            
         
        """
        pass
    @property
    def ShowAxis(self) -> bool:
        """
        Getter for property: (bool) ShowAxis
         Returns the show axis   
            
         
        """
        pass
    @ShowAxis.setter
    def ShowAxis(self, showAxis: bool):
        """
        Setter for property: (bool) ShowAxis
         Returns the show axis   
            
         
        """
        pass
    @property
    def ShowDefaultVal(self) -> bool:
        """
        Getter for property: (bool) ShowDefaultVal
         Returns the show default val   
            
         
        """
        pass
    @ShowDefaultVal.setter
    def ShowDefaultVal(self, showDefaultVal: bool):
        """
        Setter for property: (bool) ShowDefaultVal
         Returns the show default val   
            
         
        """
        pass
    @property
    def ShowDescription(self) -> bool:
        """
        Getter for property: (bool) ShowDescription
         Returns the show description   
            
         
        """
        pass
    @ShowDescription.setter
    def ShowDescription(self, showDescription: bool):
        """
        Setter for property: (bool) ShowDescription
         Returns the show description   
            
         
        """
        pass
    @property
    def ShowLabels(self) -> bool:
        """
        Getter for property: (bool) ShowLabels
         Returns the show labels   
            
         
        """
        pass
    @ShowLabels.setter
    def ShowLabels(self, showLabels: bool):
        """
        Setter for property: (bool) ShowLabels
         Returns the show labels   
            
         
        """
        pass
    @property
    def ShowMapTopo(self) -> bool:
        """
        Getter for property: (bool) ShowMapTopo
         Returns the show map topo   
            
         
        """
        pass
    @ShowMapTopo.setter
    def ShowMapTopo(self, showMapTopo: bool):
        """
        Setter for property: (bool) ShowMapTopo
         Returns the show map topo   
            
         
        """
        pass
    @property
    def ShowName(self) -> bool:
        """
        Getter for property: (bool) ShowName
         Returns the show name   
            
         
        """
        pass
    @ShowName.setter
    def ShowName(self, showName: bool):
        """
        Setter for property: (bool) ShowName
         Returns the show name   
            
         
        """
        pass
    @property
    def ShowOverflowValues(self) -> bool:
        """
        Getter for property: (bool) ShowOverflowValues
         Returns the show overflow   
            
         
        """
        pass
    @ShowOverflowValues.setter
    def ShowOverflowValues(self, showOverflow: bool):
        """
        Setter for property: (bool) ShowOverflowValues
         Returns the show overflow   
            
         
        """
        pass
    @property
    def ShowSrcTblVals(self) -> bool:
        """
        Getter for property: (bool) ShowSrcTblVals
         Returns the show dep src tbl vals   
            
         
        """
        pass
    @ShowSrcTblVals.setter
    def ShowSrcTblVals(self, showSrcTblVals: bool):
        """
        Setter for property: (bool) ShowSrcTblVals
         Returns the show dep src tbl vals   
            
         
        """
        pass
    @property
    def ShowUndefValues(self) -> bool:
        """
        Getter for property: (bool) ShowUndefValues
         Returns the show new undefined values   
            
         
        """
        pass
    @ShowUndefValues.setter
    def ShowUndefValues(self, showUndefValues: bool):
        """
        Setter for property: (bool) ShowUndefValues
         Returns the show new undefined values   
            
         
        """
        pass
    @property
    def ShowUnderflowValues(self) -> bool:
        """
        Getter for property: (bool) ShowUnderflowValues
         Returns the show underflow   
            
         
        """
        pass
    @ShowUnderflowValues.setter
    def ShowUnderflowValues(self, showUnderflow: bool):
        """
        Setter for property: (bool) ShowUnderflowValues
         Returns the show underflow   
            
         
        """
        pass
    @property
    def SpectrumLevels(self) -> int:
        """
        Getter for property: (int) SpectrumLevels
         Returns the spectrum levels   
            
         
        """
        pass
    @SpectrumLevels.setter
    def SpectrumLevels(self, spectrumLevels: int):
        """
        Setter for property: (int) SpectrumLevels
         Returns the spectrum levels   
            
         
        """
        pass
    @property
    def SurfaceOffset(self) -> float:
        """
        Getter for property: (float) SurfaceOffset
         Returns the surface offset   
            
         
        """
        pass
    @SurfaceOffset.setter
    def SurfaceOffset(self, surfaceOffset: float):
        """
        Setter for property: (float) SurfaceOffset
         Returns the surface offset   
            
         
        """
        pass
    @property
    def TblDepColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TblDepColor
         Returns the table dependent color   
            
         
        """
        pass
    @TblDepColor.setter
    def TblDepColor(self, tblDepColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TblDepColor
         Returns the table dependent color   
            
         
        """
        pass
    @property
    def TblDepDispType(self) -> DisplayPropertiesBuilder.DepDispTypeEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DepDispTypeEnum NXOpen) TblDepDispType
         Returns the table dependent display type  
            
         
        """
        pass
    @TblDepDispType.setter
    def TblDepDispType(self, tblDepDispType: DisplayPropertiesBuilder.DepDispTypeEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DepDispTypeEnum NXOpen) TblDepDispType
         Returns the table dependent display type  
            
         
        """
        pass
    @property
    def TblDepDomColor(self) -> DisplayPropertiesBuilder.DepDomColorEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DepDomColorEnum NXOpen) TblDepDomColor
         Returns the table dependent domain color   
            
         
        """
        pass
    @TblDepDomColor.setter
    def TblDepDomColor(self, depDomColor: DisplayPropertiesBuilder.DepDomColorEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DepDomColorEnum NXOpen) TblDepDomColor
         Returns the table dependent domain color   
            
         
        """
        pass
    @property
    def TblDepLabelValues(self) -> DisplayPropertiesBuilder.DepLabelValueEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.DepLabelValueEnum NXOpen) TblDepLabelValues
         Returns the table dependent label values   
            
         
        """
        pass
    @TblDepLabelValues.setter
    def TblDepLabelValues(self, tblDepLabelValues: DisplayPropertiesBuilder.DepLabelValueEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.DepLabelValueEnum NXOpen) TblDepLabelValues
         Returns the table dependent label values   
            
         
        """
        pass
    @property
    def TblDepPtType(self) -> DisplayPropertiesBuilder.TblPointTypeEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.TblPointTypeEnum NXOpen) TblDepPtType
         Returns the tbl dep pt type   
            
         
        """
        pass
    @TblDepPtType.setter
    def TblDepPtType(self, tblDepPtType: DisplayPropertiesBuilder.TblPointTypeEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.TblPointTypeEnum NXOpen) TblDepPtType
         Returns the tbl dep pt type   
            
         
        """
        pass
    @property
    def TblDepSymbolSize(self) -> float:
        """
        Getter for property: (float) TblDepSymbolSize
         Returns the table dependent symbol size   
            
         
        """
        pass
    @TblDepSymbolSize.setter
    def TblDepSymbolSize(self, tblDepSymbolSize: float):
        """
        Setter for property: (float) TblDepSymbolSize
         Returns the table dependent symbol size   
            
         
        """
        pass
    @property
    def TblHetPrimaryValue(self) -> float:
        """
        Getter for property: (float) TblHetPrimaryValue
         Returns the heterogeneous table value to display   
            
         
        """
        pass
    @TblHetPrimaryValue.setter
    def TblHetPrimaryValue(self, hetTblValue: float):
        """
        Setter for property: (float) TblHetPrimaryValue
         Returns the heterogeneous table value to display   
            
         
        """
        pass
    @property
    def TblIndepColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TblIndepColor
         Returns the tbl indep color   
            
         
        """
        pass
    @TblIndepColor.setter
    def TblIndepColor(self, tblIndepColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TblIndepColor
         Returns the tbl indep color   
            
         
        """
        pass
    @property
    def TblIndepPtType(self) -> DisplayPropertiesBuilder.ValuesEnum:
        """
        Getter for property: ( DisplayPropertiesBuilder.ValuesEnum NXOpen) TblIndepPtType
         Returns the tbl indep pt type   
            
         
        """
        pass
    @TblIndepPtType.setter
    def TblIndepPtType(self, tblIndepPtType: DisplayPropertiesBuilder.ValuesEnum):
        """
        Setter for property: ( DisplayPropertiesBuilder.ValuesEnum NXOpen) TblIndepPtType
         Returns the tbl indep pt type   
            
         
        """
        pass
    @property
    def TblSurfaceOffset(self) -> float:
        """
        Getter for property: (float) TblSurfaceOffset
         Returns the table dependent surface offset scaling factor  
            
         
        """
        pass
    @TblSurfaceOffset.setter
    def TblSurfaceOffset(self, tblDepSurfaceOffset: float):
        """
        Setter for property: (float) TblSurfaceOffset
         Returns the table dependent surface offset scaling factor  
            
         
        """
        pass
    @property
    def Translucency(self) -> int:
        """
        Getter for property: (int) Translucency
         Returns the translucency   
            
         
        """
        pass
    @Translucency.setter
    def Translucency(self, translucency: int):
        """
        Setter for property: (int) Translucency
         Returns the translucency   
            
         
        """
        pass
    @property
    def UndefValueColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) UndefValueColor
         Returns the undef value color   
            
         
        """
        pass
    @UndefValueColor.setter
    def UndefValueColor(self, undefValueColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) UndefValueColor
         Returns the undef value color   
            
         
        """
        pass
    @property
    def UnderflowColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) UnderflowColor
         Returns the underflow color   
            
         
        """
        pass
    @UnderflowColor.setter
    def UnderflowColor(self, underflowColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) UnderflowColor
         Returns the underflow color   
            
         
        """
        pass
    @property
    def XMax(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XMax
         Returns the x max   
            
         
        """
        pass
    @property
    def XMin(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XMin
         Returns the x min   
            
         
        """
        pass
    @property
    def XNum(self) -> int:
        """
        Getter for property: (int) XNum
         Returns the x num   
            
         
        """
        pass
    @XNum.setter
    def XNum(self, xNum: int):
        """
        Setter for property: (int) XNum
         Returns the x num   
            
         
        """
        pass
    @property
    def YMax(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YMax
         Returns the y max   
            
         
        """
        pass
    @property
    def YMin(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YMin
         Returns the y min   
            
         
        """
        pass
    @property
    def YNum(self) -> int:
        """
        Getter for property: (int) YNum
         Returns the y num   
            
         
        """
        pass
    @YNum.setter
    def YNum(self, yNum: int):
        """
        Setter for property: (int) YNum
         Returns the y num   
            
         
        """
        pass
    @property
    def ZMax(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZMax
         Returns the z max   
            
         
        """
        pass
    @property
    def ZMin(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZMin
         Returns the z min   
            
         
        """
        pass
    @property
    def ZNum(self) -> int:
        """
        Getter for property: (int) ZNum
         Returns the z num   
            
         
        """
        pass
    @ZNum.setter
    def ZNum(self, zNum: int):
        """
        Setter for property: (int) ZNum
         Returns the z num   
            
         
        """
        pass
import NXOpen
class ExportData(NXOpen.TransientObject): 
    """  Represents data for field export  """
    def AddField(self, field: Field) -> None:
        """
         Add a field 
        """
        pass
    def AddFields(self, fields: List[Field]) -> None:
        """
         Add a field 
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object 
        """
        pass
    def GetFields(self) -> List[Field]:
        """
         Gets the fields 
         Returns fields ( Field List[NXOp):  fields .
        """
        pass
    def GetFileName(self) -> str:
        """
         Get file name 
         Returns fileName (str):  file name .
        """
        pass
    def SetFileName(self, file_name: str) -> None:
        """
         Set file name 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ExternalFileProfileBuilder(NXOpen.TaggedObject): 
    """ 
            Represents a builder class for creating and editing an NXOpen.Fields.Field
            that is defined by an external file reference.
        
        
        
        This builder allows you to define an 
        NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Curve(2D) or
       NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Surface
       (3D) profile from the data with an external file.
       The file must have at least the number of columns of data required for by the dimension of the profile to be created.
       
       
        For NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Curve
        you need to specify two columns from the file.
        
         NXOpen.Fields.ExternalFileProfileBuilder.XColumn, the independent value
         NXOpen.Fields.ExternalFileProfileBuilder.OrdinateColumn, the dependent value
        
        For NXOpen.Fields.ExternalFileProfileBuilder.DimensionChoice.Surface
        you need to specify three columns from the file.
        
         NXOpen.Fields.ExternalFileProfileBuilder.XColumn, the independent value
         NXOpen.Fields.ExternalFileProfileBuilder.YColumn, the independent value
         NXOpen.Fields.ExternalFileProfileBuilder.OrdinateColumn, the dependent value
        
        Please refer to documentation for specific details on the file formats supported.
        
        """
    class CyclicType(Enum):
        """
        Members Include: 
         |NotSet|  not cyclic 
         |XOnly|  cyclic in x direction 
         |YOnly|  cyclic in y direction 
         |Both|  cyclic in both x and y direction 

        """
        NotSet: int
        XOnly: int
        YOnly: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.CyclicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DimensionChoice(Enum):
        """
        Members Include: 
         |Curve|  two dimensional with x axis and ordinate 
         |Surface|  three dimensional with x axis, y axis and ordinate 
         |Any|  undefined dimension, which an existing profile can never actually have 

        """
        Curve: int
        Surface: int
        Any: int
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.DimensionChoice:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Extrapolation(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Parabolic|  Parabolic 
         |Cubic|  Cubic 

        """
        Linear: int
        Parabolic: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.Extrapolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FormatOptions(Enum):
        """
        Members Include: 
         |ComputerRegionalSettings|  Use Computer Regional Settings 
         |DotDecimalSeparator|  Use . as decimal separator 
         |CommaDecimalSeparator|  Use , as decimal separator 
         |DotDecimalSeparatorAndCommaValueDelimiter|  Use . as decimal separator and , as value delimiter
         |CommaDecimalSeparatorAndSemicolonValueDelimiter|  Use , as decimal separator and ; as value delimiter

        """
        ComputerRegionalSettings: int
        DotDecimalSeparator: int
        CommaDecimalSeparator: int
        DotDecimalSeparatorAndCommaValueDelimiter: int
        CommaDecimalSeparatorAndSemicolonValueDelimiter: int
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.FormatOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Interpolation(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Akima|  Akima 
         |Akima72|  Akima72 
         |Cubic|  Cubic 

        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> ExternalFileProfileBuilder.Interpolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Cyclic(self) -> ExternalFileProfileBuilder.CyclicType:
        """
        Getter for property: ( ExternalFileProfileBuilder.CyclicType NXOpen) Cyclic
         Returns   
                    the cyclic type.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone 
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly 
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly 
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth 
                    
                      
         
        """
        pass
    @Cyclic.setter
    def Cyclic(self, cyclicType: ExternalFileProfileBuilder.CyclicType):
        """
        Setter for property: ( ExternalFileProfileBuilder.CyclicType NXOpen) Cyclic
         Returns   
                    the cyclic type.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone 
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly 
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly 
                       NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeBoth 
                    
                      
         
        """
        pass
    @property
    def Dimension(self) -> ExternalFileProfileBuilder.DimensionChoice:
        """
        Getter for property: ( ExternalFileProfileBuilder.DimensionChoice NXOpen) Dimension
         Returns   
                    the dimension.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve  2D
                       NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface  3D
                    
                      
         
        """
        pass
    @Dimension.setter
    def Dimension(self, dimension: ExternalFileProfileBuilder.DimensionChoice):
        """
        Setter for property: ( ExternalFileProfileBuilder.DimensionChoice NXOpen) Dimension
         Returns   
                    the dimension.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve  2D
                       NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface  3D
                    
                      
         
        """
        pass
    @property
    def FormatControlOption(self) -> ExternalFileProfileBuilder.FormatOptions:
        """
        Getter for property: ( ExternalFileProfileBuilder.FormatOptions NXOpen) FormatControlOption
         Returns   
                    the format control of separators 
                     
          
          
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter 
                    
                      
         
        """
        pass
    @FormatControlOption.setter
    def FormatControlOption(self, formatControlType: ExternalFileProfileBuilder.FormatOptions):
        """
        Setter for property: ( ExternalFileProfileBuilder.FormatOptions NXOpen) FormatControlOption
         Returns   
                    the format control of separators 
                     
          
          
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsComputerRegionalSettings 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparator 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparator 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsDotDecimalSeparatorAndCommaValueDelimiter 
                       NXOpen::Fields::ExternalFileProfileBuilder::FormatOptionsCommaDecimalSeparatorAndSemicolonValueDelimiter 
                    
                      
         
        """
        pass
    @property
    def OrdinateColumn(self) -> int:
        """
        Getter for property: (int) OrdinateColumn
         Returns   
                    the column number in the external file corresponding to the ordinate axis.  
          
                     
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    @OrdinateColumn.setter
    def OrdinateColumn(self, columnIdx: int):
        """
        Setter for property: (int) OrdinateColumn
         Returns   
                    the column number in the external file corresponding to the ordinate axis.  
          
                     
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    @property
    def OrdinateOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OrdinateOffset
         Returns   
                    the offset on the ordinate axis.  
          
                     
         
                    
                    The unit of the offset has to match the unit defined in the header
                    of the  NXOpen::Fields::ExternalFileProfileBuilder::OrdinateColumn 
                    in the file set in  NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference .
                      
         
        """
        pass
    @property
    def OrdinateScale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OrdinateScale
         Returns   
                    the scale on the ordinate axis.  
          
                     
         
                    The scale is unitless.  
         
        """
        pass
    @property
    def SlopeLeft(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeLeft
         Returns   
                    the left slope.  
          
                     
         
                    
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve 
                      
         
        """
        pass
    @property
    def SlopeRight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeRight
         Returns   
                    the right slope.  
          
                     
         
                    
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceCurve 
                      
         
        """
        pass
    @property
    def SolverOptions(self) -> ProfileSolverOptionsBuilder:
        """
        Getter for property: ( ProfileSolverOptionsBuilder NXOpen) SolverOptions
         Returns   the solver options.  
           
           
         
        """
        pass
    @property
    def XColumn(self) -> int:
        """
        Getter for property: (int) XColumn
         Returns   
                    the column number in the external file corresponding to the x axis.  
          
                     
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    @XColumn.setter
    def XColumn(self, columnIdx: int):
        """
        Setter for property: (int) XColumn
         Returns   
                    the column number in the external file corresponding to the x axis.  
          
                     
         
                    
                    Column A of an excel file corresponds to the number 1.
                      
         
        """
        pass
    @property
    def XExtrapolation(self) -> ExternalFileProfileBuilder.Extrapolation:
        """
        Getter for property: ( ExternalFileProfileBuilder.Extrapolation NXOpen) XExtrapolation
         Returns   
                    the extrapolation in x direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic 
                    
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone 
                    or  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly 
                      
                      
         
        """
        pass
    @XExtrapolation.setter
    def XExtrapolation(self, extrapolation: ExternalFileProfileBuilder.Extrapolation):
        """
        Setter for property: ( ExternalFileProfileBuilder.Extrapolation NXOpen) XExtrapolation
         Returns   
                    the extrapolation in x direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic 
                    
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone 
                    or  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeYOnly 
                      
                      
         
        """
        pass
    @property
    def XInterpolation(self) -> ExternalFileProfileBuilder.Interpolation:
        """
        Getter for property: ( ExternalFileProfileBuilder.Interpolation NXOpen) XInterpolation
         Returns   
                    the interpolation in x direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic 
                    
                      
         
        """
        pass
    @XInterpolation.setter
    def XInterpolation(self, interpolation: ExternalFileProfileBuilder.Interpolation):
        """
        Setter for property: ( ExternalFileProfileBuilder.Interpolation NXOpen) XInterpolation
         Returns   
                    the interpolation in x direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic 
                    
                      
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns   
                    the offset on the x axis.  
          
                     
         
                    
                    The unit of the offset has to match the unit defined in the header
                    of the  NXOpen::Fields::ExternalFileProfileBuilder::XColumn 
                    in the file set in  NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference .
                      
         
        """
        pass
    @property
    def XScale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XScale
         Returns   
                    the scale on the x axis.  
          
                     
         
                    The scale is unitless.  
         
        """
        pass
    @property
    def YColumn(self) -> int:
        """
        Getter for property: (int) YColumn
         Returns   
                    the column number in the external file corresponding to the y axis.  
          
                     
         
                    
                      
                    Column A of an excel file corresponds to the number 1.
                      
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface .
                      
                      
         
        """
        pass
    @YColumn.setter
    def YColumn(self, columnIdx: int):
        """
        Setter for property: (int) YColumn
         Returns   
                    the column number in the external file corresponding to the y axis.  
          
                     
         
                    
                      
                    Column A of an excel file corresponds to the number 1.
                      
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface .
                      
                      
         
        """
        pass
    @property
    def YExtrapolation(self) -> ExternalFileProfileBuilder.Extrapolation:
        """
        Getter for property: ( ExternalFileProfileBuilder.Extrapolation NXOpen) YExtrapolation
         Returns   
                    the extrapolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic 
                    
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface 
                    and when  NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone 
                    or  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly 
                      
                      
         
        """
        pass
    @YExtrapolation.setter
    def YExtrapolation(self, extrapolation: ExternalFileProfileBuilder.Extrapolation):
        """
        Setter for property: ( ExternalFileProfileBuilder.Extrapolation NXOpen) YExtrapolation
         Returns   
                    the extrapolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationParabolic 
                       NXOpen::Fields::ExternalFileProfileBuilder::ExtrapolationCubic 
                    
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface 
                    and when  NXOpen::Fields::ExternalFileProfileBuilder::SetCyclicType 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeNone 
                    or  NXOpen::Fields::ExternalFileProfileBuilder::CyclicTypeXOnly 
                      
                      
         
        """
        pass
    @property
    def YInterpolation(self) -> ExternalFileProfileBuilder.Interpolation:
        """
        Getter for property: ( ExternalFileProfileBuilder.Interpolation NXOpen) YInterpolation
         Returns   
                    the interpolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic 
                    
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface 
                      
                      
         
        """
        pass
    @YInterpolation.setter
    def YInterpolation(self, interpolation: ExternalFileProfileBuilder.Interpolation):
        """
        Setter for property: ( ExternalFileProfileBuilder.Interpolation NXOpen) YInterpolation
         Returns   
                    the interpolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationLinear 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationAkima72 
                       NXOpen::Fields::ExternalFileProfileBuilder::InterpolationCubic 
                    
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface 
                      
                      
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns   
                    the offset on the y axis.  
          
                     
         
                    
                      
                    Please make sure that the unit of the offset matches the unit defined in the header
                    of the  NXOpen::Fields::ExternalFileProfileBuilder::YColumn 
                    in the file set in  NXOpen::Fields::ExternalFileProfileBuilder::EstablishReference .
                      
                      
                    This is only used when  NXOpen::Fields::ExternalFileProfileBuilder::SetDimensionChoice 
                    is set to  NXOpen::Fields::ExternalFileProfileBuilder::DimensionChoiceSurface .
                      
                      
         
        """
        pass
    @property
    def YScale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YScale
         Returns   
                    the scale on the y axis.  
          
                     
         
                    The scale is unitless.  
         
        """
        pass
    def GetColumnMeasureName(self, columnNumber: int) -> str:
        """
         
                    Returns the measure of the specified column.
                    
                    
                    This only works if the file set in NXOpen.Fields.ExternalFileProfileBuilder.EstablishReference
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)
                    If the file was not read already GetColumnMeasureName will read it.
                    
         Returns measureName (str):  measure name of the specified column .
        """
        pass
    def GetColumnTitle(self, columnNumber: int) -> str:
        """
         
                    Returns the title of the specified column.
                    
                    
                    
                     The title contains the
                     
                      column number(s) in file set in NXOpen.Fields.ExternalFileProfileBuilder.EstablishReference (starting with 1)
                      end column for the variable if applicable
                      column name and
                      localized unit string.
                    
                    e.g. "1: X (unitless)" or "2(..4): Y (mm)"
                    
                    
                    This only works if file set in NXOpen.Fields.ExternalFileProfileBuilder.EstablishReference
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)
                    If the file was not read already GetColumnTitle will read it.
                    
                    
         Returns column_title (str):  title of the specified column .
        """
        pass
    def GetColumnUnit(self, columnNumber: int) -> NXOpen.Unit:
        """
         
                    Returns the unit of the specified column.
                    
                    
                    This only works if the file set in NXOpen.Fields.ExternalFileProfileBuilder.EstablishReference
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)
                    If the file was not read already GetColumnUnit will read it.
                    
         Returns unit ( NXOpen.Unit):  unit of the specified column .
        """
        pass
    def GetNumberOfColumns(self) -> int:
        """
         
                    Gets the number of column titles.
                    
                    
                    
                    Depending on the format of the file set in NXOpen.Fields.ExternalFileProfileBuilder.EstablishReference
                    several columns in the file can belong together making up one common title.
                    
                    
                    This only works if NXOpen.Fields.ExternalFileProfileBuilder.EstablishReference
                    is set to a valid file. (Please refer to documentation for specific details on the file formats supported.)
                    If the file was not read already GetNumberOfColumns will read it.
                    
                    
         Returns numberColumns (int):  number of column titles .
        """
        pass
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        """
         
                        If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
                    
                    
                        It is recommended to call this method when editing a profile that is referenced by another object,
                        which depends on specific measures.
                    
        """
        pass
import NXOpen
class FieldCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Fields """
    pass
import NXOpen
class FieldEvaluator(NXOpen.TaggedObject): 
    """  Represents a Field Evaluator which can be used to evaluate a NXOpen.Fields.Field. 
                        
         """
    class DelaunaySliverDetectionMethodEnum(Enum):
        """
        Members Include: 
         |Edgelengthratio|  Default method if not specified, compares ratio of each edge length to the sum of the lengths of the other two sides 
         |Aspectratio|  Compares the height from the free edge to the opposite vertex to the length of the free edge 

        """
        Edgelengthratio: int
        Aspectratio: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.DelaunaySliverDetectionMethodEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterpolationEnum(Enum):
        """
        Members Include: 
         |NotSet|  No interpolation method; table can only be used as a lookup 
         |Linear1d|  Standard linear interpolation between bounding points 
         |NearestNeighbor1d|  Locates the nearest point and returns its value 
         |InverseDistanceWeighting1d|  Sum of the weighted value of all points, based on the inverse of the distance 
         |Delaunay2dFast|  Triangulates the independent values and uses the bounding triangle, sacrifices accuracy for speed 
         |Delaunay2dMedium|  Triangulates the independent values and uses the bounding triangle, compromise between accuracy and speed 
         |Delaunay2dAccurate|  Triangulates the independent values and uses the bounding triangle, sacrifices speed for accuracy 
         |NearestNeighbor2d|  Locates the nearest point in a plane and returns its value 
         |RenkaShepard2d|  Refined inverse distance weighting in 2D space 
         |InverseDistanceWeighting2d|  Sum of the weighted value of all points in 2D space, based on the inverse of the distance 
         |Delaunay3dFast|  Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices accuracy for speed 
         |Delaunay3dMedium|  Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, compromise between accuracy and speed 
         |Delaunay3dAccurate|  Creates Tetrahedrals using the independent values and uses the bounding tetrahedron, sacrifices speed for accuracy 
         |NearestNeighbor3d|  Locates the nearest point in space and returns its value 
         |RenkaShepard3d|  Refined inverse distance weighting in 3D space 
         |InverseDistanceWeighting3d|  Sum of the weighted value of all points in 3D space, based on the inverse of the distance 
         |NearestNeighborNd|  Locates the nearest point in N dimensional space and returns its value 
         |RenkaShepardNd|  Refined inverse distance weighting in N dimensional space 
         |InverseDistanceWeightingNd|  Sum of the weighted value of all points in N dimensional, based on the inverse of the distance 
         |ApproxNearestNeighbor2d|  Locates the approximate nearest point in a plane and returns its value 
         |ApproxNearestNeighbor3d|  Locates the approximate nearest point in space and returns its value 
         |ApproxNearestNeighborNd|  Locates the approximate nearest point in N dimensional space and returns its value 
         |Akima1d|  akima interpolation 
         |Akima721d|  akima72 interpolation 
         |Cubic1d|  cubic interpolation 
         |Bilinear2d|  linear interpolation in both directions 
         |Biakima2d|  akima interpolation in both directions 
         |Biakima722d|  akima72 interpolation in both directions 
         |Bicubic2d|  cubic interpolation in both directions 
         |AkimaLinear2d|  akima interpolation in x direction, linear in y direction 
         |Akima72Linear2d|  akima72 interpolation in x direction, linear in y direction 
         |CubicLinear2d|  cubic interpolation in x direction, linear in y direction 
         |Conservative3d|  conservative interpolation reserved for load mapping workflows 
         |Lookupvalues1d|  Lookup values interpolator for 1d integer based id table mapping workflows 
         |Lookupvalues2d|  Lookup values interpolator for 2d integer based id table mapping workflows 
         |Lookupvalues3d|  Lookup values interpolator for 3d integer based id table mapping workflows 
         |LeastSquares1d|  Weighted Least Squares Interpolation for 1d domain 
         |LeastSquares2d|  Weighted Least Squares Interpolation for 2d domain 
         |LeastSquares3d|  Weighted Least Squares Interpolation for 3d domain 
         |Bspline1d|  BSpline Interpolation for 1d domain 
         |Bspline2d|  BSpline Interpolation for 2d domain 
         |Bspline3d|  BSpline Interpolation for 3d domain 
         |LinearLeastSquares1d|  Linear Least Squares Interpolation for 1d domain 
         |Spline1d|  Spline Interpolation for 1d domain 

        """
        NotSet: int
        Linear1d: int
        NearestNeighbor1d: int
        InverseDistanceWeighting1d: int
        Delaunay2dFast: int
        Delaunay2dMedium: int
        Delaunay2dAccurate: int
        NearestNeighbor2d: int
        RenkaShepard2d: int
        InverseDistanceWeighting2d: int
        Delaunay3dFast: int
        Delaunay3dMedium: int
        Delaunay3dAccurate: int
        NearestNeighbor3d: int
        RenkaShepard3d: int
        InverseDistanceWeighting3d: int
        NearestNeighborNd: int
        RenkaShepardNd: int
        InverseDistanceWeightingNd: int
        ApproxNearestNeighbor2d: int
        ApproxNearestNeighbor3d: int
        ApproxNearestNeighborNd: int
        Akima1d: int
        Akima721d: int
        Cubic1d: int
        Bilinear2d: int
        Biakima2d: int
        Biakima722d: int
        Bicubic2d: int
        AkimaLinear2d: int
        Akima72Linear2d: int
        CubicLinear2d: int
        Conservative3d: int
        Lookupvalues1d: int
        Lookupvalues2d: int
        Lookupvalues3d: int
        LeastSquares1d: int
        LeastSquares2d: int
        LeastSquares3d: int
        Bspline1d: int
        Bspline2d: int
        Bspline3d: int
        LinearLeastSquares1d: int
        Spline1d: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.InterpolationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InverseDistanceWeightingEnum(Enum):
        """
        Members Include: 
         |All|  Sum of the weighted value of all points, based on the inverse of the distance 
         |Radius|  Sum of the weighted value of points within a radius (as a fraction of the bounding box diagonal), based on the inverse of the distance 
         |NearestPoints|  Sum of the weighted value of N nearest points (as a fraction of the total number of points), based on the inverse of the distance 
         |NumNearestPoints|  Sum of the weighted value of N nearest points, based on the inverse of the distance[This option is not supported] 
         |MaximumRadiusAndPoints|  Sum of the weighted value of N nearest points and points within a radius, based on the inverse of the distance  

        """
        All: int
        Radius: int
        NearestPoints: int
        NumNearestPoints: int
        MaximumRadiusAndPoints: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.InverseDistanceWeightingEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InverseDistanceWeightingPowerOfDistanceEnum(Enum):
        """
        Members Include: 
         |One|  IDW algorithm will use the distance for its calculation 
         |Two|  IDW algorithm will use the squared distance for calculation 
         |Three|  IDW algorithm will use the cubed distance for calculation 

        """
        One: int
        Two: int
        Three: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinearLogOptionEnum(Enum):
        """
        Members Include: 
         |LinearLinear|  Standard linear interpolation. Both Independent variable and Dependent variable scaling are linear 
         |LogLinear|  Independent variable scaling is logarithmic (ln), Dependent variable scaling is linear 
         |LinearLog|  Independent variable scaling is linear, Dependent variable scaling is logarithmic (ln) 
         |LogLog|  Both Independent variable and Dependent variable scaling are logarithmic (ln) 
         |ScaleOffset|  ScaleOffset enum selection option under linear interpolation scheme 

        """
        LinearLinear: int
        LogLinear: int
        LinearLog: int
        LogLog: int
        ScaleOffset: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.LinearLogOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplineDegreeOptionEnum(Enum):
        """
        Members Include: 
         |ThirdOrder|  Spline interpolation using third degree polynomial 
         |FifthOrder|  Spline interpolation using fifth degree polynomial 

        """
        ThirdOrder: int
        FifthOrder: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.SplineDegreeOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValuesOutsideTableInterpolationEnum(Enum):
        """
        Members Include: 
         |Undefined|  No interpolation result 
         |Extrapolate|  Extrapolates from the boundary out into space using the same interpolation method that the interpolator for interior table values uses 
         |Constant|  Returns the boundary value as interpolation result 
         |Linear|  Extrapolates from the boundary out into space using the linear extrapolation method 
         |Parabolic|  Extrapolates from the boundary out into space using the parabolic extrapolation method 
         |Cubic|  Extrapolates from the boundary out into space using the cubic extrapolation method 
         |Userdefined|  Returns the user specified value as the interpolation result 

        """
        Undefined: int
        Extrapolate: int
        Constant: int
        Linear: int
        Parabolic: int
        Cubic: int
        Userdefined: int
        @staticmethod
        def ValueOf(value: int) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InterpolationMethod(self) -> FieldEvaluator.InterpolationEnum:
        """
        Getter for property: ( FieldEvaluator.InterpolationEnum NXOpen) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolation_method: FieldEvaluator.InterpolationEnum):
        """
        Setter for property: ( FieldEvaluator.InterpolationEnum NXOpen) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    def Delete(self) -> None:
        """
         Delete this field evaluator; destroys the field evaluator and removes all references to it.
                
        """
        pass
    def Evaluate(self, dependent_variable: FieldVariable) -> List[float]:
        """
         Evaluate the Field at the specified independent variable NXOpen.Fields.FieldVariable values and return the values for the specified dependent variable. 
                    The number of output values will be the same as number of independent variables specified and these values will be in the same units as the 
                    dependent variable NXOpen.Fields.FieldVariable.   
                
         Returns values (List[float]):  the values evaluated for this dependent variable .
        """
        pass
    def GetDependentVariables(self) -> List[FieldVariable]:
        """
         Returns the dependent variables for this NXOpen.Fields.FieldEvaluator  
                
         Returns dependent_variables ( FieldVariable List[NXOp):  dependent variables for this NXOpen.Fields.FieldEvaluator  .
        """
        pass
    def GetIndependentVariables(self) -> List[FieldVariable]:
        """
         Returns the independent variables for this NXOpen.Fields.FieldEvaluator  
                
         Returns independent_variables ( FieldVariable List[NXOp):  independent variables for this NXOpen.Fields.FieldEvaluator  .
        """
        pass
    def SetIndependentVariableValues(self, independent_variable: FieldVariable, values: List[float]) -> None:
        """
         Sets values at which the Field will be evaluated for this independent variable NXOpen.Fields.FieldVariable. 
                    The number of input values mush be the same for independent variables and these values are assumed to be in the same units as the 
                    independent variable NXOpen.Fields.FieldVariable.   
                
        """
        pass
import NXOpen
class FieldExpression(Field): 
    """  Represents the Field Expression class.
    A field (see NXOpen.Fields.Field) which has exactly one dependent
    variable (see NXOpen.Fields.FieldVariable), where the field function defintions
    is implemented using the NX Expression sub-system NXOpen.Expression. """
    class CombineTableOption(Enum):
        """
        Members Include: 
         |Intersection|  The Intersection option will yield only points (e.g.: time points) which are common among the tables. 
         |Union|  The Union option will include all points from all tables in the expression. 

        """
        Intersection: int
        Union: int
        @staticmethod
        def ValueOf(value: int) -> FieldExpression.CombineTableOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CombineTable(self) -> FieldExpression.CombineTableOption:
        """
        Getter for property: ( FieldExpression.CombineTableOption NXOpen) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    @CombineTable.setter
    def CombineTable(self, tableOption: FieldExpression.CombineTableOption):
        """
        Setter for property: ( FieldExpression.CombineTableOption NXOpen) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    @property
    def FieldExpressionUnits(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) FieldExpressionUnits
         Returns the units of the field expression   
            
         
        """
        pass
    def EditFieldExpression(self, field_exp_string: str, unit_type: NXOpen.Unit, indep_var_array: List[FieldVariable], update_flag: bool) -> None:
        """
         Edit the expression field.  Specifies the new expression string and the array of variables used
                    in the expression string.  Field expressions are children of
                    NXOpen.Fields.FieldFormula.
                 
        """
        pass
    def GetFieldExpressionString(self) -> str:
        """
         Gets the expression string of the expression field 
         Returns field_exp_string (str):  expression string associated with the field .
        """
        pass
    def SetFieldExpressionString(self, field_exp_string: str, updateFlag: bool) -> None:
        """
         Sets the new expression string to the expression field 
        """
        pass
import NXOpen
class FieldFolderCollection(NXOpen.TaggedObjectCollection): 
    """  Provides methods for managing field folders NXOpen.Fields.FieldFolder  """
    def CreateFolder(self, name: str, parent: FieldFolder) -> FieldFolder:
        """
         Creates a Field folder with given name, and optional makes it a subfolder if a parent folder is specified. 
                 
         Returns folder ( FieldFolder NXOpen):  the created NXOpen.Fields.FieldFolder .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> FieldFolder:
        """
         Finds the NXOpen.Fields.FieldFolder with the given identifier as recorded in a journal.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( FieldFolder NXOpen):  field folder found .
        """
        pass
import NXOpen
import NXOpen.CAE
class FieldFolder(NXOpen.NXObject): 
    """  Represents a folder object in the fields   """
    @property
    def Parent(self) -> FieldFolder:
        """
        Getter for property: ( FieldFolder NXOpen) Parent
         Returns the parent folder   
            
         
        """
        pass
    def AddField(self, field: Field) -> None:
        """
          Add a child folder 
        """
        pass
    def AddSubfolder(self, subfolder: FieldFolder) -> None:
        """
          Add a child folder 
        """
        pass
    def RemoveField(self, field: Field) -> None:
        """
          Remove a child folder 
        """
        pass
    def RemoveSubfolder(self, subfolder: FieldFolder) -> None:
        """
          Remove a child folder 
        """
        pass
class FieldFormula(Field): 
    """  Represents the Field Formula class.
    A field (see NXOpen.Fields.Field) which has n number of dependent
    variables, where each dependent variable (see NXOpen.Fields.FieldVariable) is implemented using the NX Expression sub-system.
    In practical terms, a field formula is implemented using n number of field expressions
    NXOpen.Fields.FieldExpression. """
    @property
    def CombineTable(self) -> FieldExpression.CombineTableOption:
        """
        Getter for property: ( FieldExpression.CombineTableOption NXOpen) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    @CombineTable.setter
    def CombineTable(self, tableOption: FieldExpression.CombineTableOption):
        """
        Setter for property: ( FieldExpression.CombineTableOption NXOpen) CombineTable
         Returns the table combine option   
            
         
        """
        pass
    def EditFieldFormula(self, indep_var_array: List[FieldVariable], dep_exp_array: List[FieldExpression]) -> None:
        """
         Edit the formula field.  Specifies the new expression NXOpen.Fields.FieldExpression
                    array and the array of NXOpen.Fields.FieldVariables used.
                
        """
        pass
    def EditFieldFormulaVariables(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable]) -> None:
        """
         Edit the formula field variables.  Specifies the new dependent and independent NXOpen.Fields.FieldVariable
                arrays.  The formula will be updated to reflect the changes (if any) to the variables.  If the dependent variables are changed, the expressions will be changed 
                to 0 if the new variable measure is incompatible with the old variable measure.  If the independent variables change, the expression will be changed
                to 0 if it contains any of the deleted variables.
                
        """
        pass
    def GetDependentExpressions(self) -> List[FieldExpression]:
        """
         Returns the dependent field expressions associated with this formula 
                
         Returns dependent_expressions ( FieldExpression List[NXOp):  dependent expressions  .
        """
        pass
import NXOpen
class FieldLinksTable(Field): 
    """  Represents the Field LinksTable class. 
    A field (see NXOpen.Fields.Field) defined in terms of tabular data involving 
    one look-up independent column, an equal number of look-up fields and one or more 
    dependent variables (see NXOpen.Fields.FieldVariable).  This is similar to a table
    (see NXOpen.Fields.FieldTable), except instead of the interpolation dependent 
    values being defined as numerical contants, they are defined by another field. """
    @property
    def Discontinuities(self) -> bool:
        """
        Getter for property: (bool) Discontinuities
         Returns a flag specifying if the table has discontinuites   
            
         
        """
        pass
    @property
    def ValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
        Getter for property: ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation   
            
         
        """
        pass
    @ValuesOutsideTableInterpolation.setter
    def ValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum):
        """
        Setter for property: ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation   
            
         
        """
        pass
    @overload
    def EditFieldLinksTable(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field]) -> None:
        """
         Edit the LinksTable field.  Specifies the new array of NXOpen.Fields.FieldVariables 
                for independent and dependent variables, as well as the new double values and linked fields.
                The datapoints and linked fields arrays are row based and number of each must equal the 
                num_rows. The data_points array represents the values for the first independent value.  For example, if 
                the LinksTable has a domain of txyz, the values in this array are all values of t.
                The linked fields array must consist of the fields with independent variables representing the 
                remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
                a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
                linked fields and indicate a discontinuity at the associated value of the first independent  variable.
                The dependent quantities are determined from the linked fields.  The linked fields must have the same 
                dependent variables as the Linkstable.
                
        """
        pass
    def EditFieldLinksTableWithConstants(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> None:
        """
         Edit the LinksTable field.  Specifies the new array of NXOpen.Fields.FieldVariables
               for independent and dependent variables, as well as the new double values and linked fields.
               The datapoints and linked fields arrays are row based and number of each must equal the
               num_rows. The data_points array represents the values for the first independent value.  For example, if
               the LinksTable has a domain of txyz, the values in this array are all values of t.
               The linked fields array must consist of the fields with independent variables representing the
               remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has
               a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for
               linked fields and indicate a discontinuity at the associated value of the first independent  variable.
               The dependent quantities are determined from the linked fields.  The linked fields must have the same
               dependent variables as the Linkstable.
               
        """
        pass
    @overload
    def EditFieldLinksTable(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> None:
        """
         Edit the LinksTable field.  Specifies the new array of NXOpen.Fields.FieldVariables 
                for independent and dependent variables, as well as the new double values and linked fields.
                The datapoints, linked fields, and the managed fields arrays are row based and number of each must equal the 
                num_rows. The data_points array represents the values for the first independent value.  For example, if 
                the LinksTable has a domain of txyz, the values in this array are all values of t.
                The linked fields array must consist of the fields with independent variables representing the 
                remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
                a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
                linked fields and indicate a discontinuity at the associated value of the first independent  variable.
                The dependent quantities are determined from the linked fields.  The linked fields must have the same 
                dependent variables as the Linkstable. The managed fields array identifies the fields that should be managed by the links table.
                
        """
        pass
    def GetPrimaryIndependentVariableOffset(self) -> NXOpen.Expression:
        """
         Get the offset value for the primary independent variable 
         Returns offset ( NXOpen.Expression):  the offset for the primary independent variable .
        """
        pass
    def GetPrimaryIndependentVariableScaleFactor(self) -> NXOpen.Expression:
        """
         Get the scale factor for the primary independent variable 
         Returns scaleFactor ( NXOpen.Expression):  the scale factor for the primary independent variable .
        """
        pass
    def SetPrimaryIndependentVariableOffset(self, offset: NXOpen.Expression) -> None:
        """
         Set the offset value for the primary independent variable 
        """
        pass
    def SetPrimaryIndependentVariableScaleFactor(self, scaleFactor: NXOpen.Expression) -> None:
        """
         Set the scale factor for the primary independent variable 
        """
        pass
    def SetSecondaryValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        """
         Set the values outside table interpolation option for sub fields if the sub fields are tables  
        """
        pass
class FieldLink(Field): 
    """  Represents the Field Link class.
    A field (see Fields.Field) which is implemented by another user
    created field of any type.  This provides the ability to override that field's map with a 
    localized map. """
    def EditFieldLink(self, fieldToLink: Field) -> None:
        """
         Edit the link field.  Specifies the new Fields.Field
                    to link to.
                
        """
        pass
import NXOpen
class FieldManager(NXOpen.NXObject): 
    """  Represents the manager class of the Fields  
    This manager class gives access to all the fields NXOpen.Fields.Field within a part.
    It also provides creation methods for the various builders of fields and related classes.
    """
    @property
    def Fields() -> FieldCollection:
        """
         Returns a collection of Fields 
        """
        pass
    @property
    def FieldFolders() -> FieldFolderCollection:
        """
         Returns the field folder collection 
        """
        pass
    def ConvertToLinksTable(self, table: FieldTable) -> FieldLinksTable:
        """
          
                Creates and returns a NXOpen.Fields.FieldLinksTable representation of this table. Deletes the input table and updates all references to point to the links table.
                
         Returns linksTable ( FieldLinksTable NXOpen):  table of fields .
        """
        pass
    def CreateComplexScalarFieldWrapperWithExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed by two scalar expressions 
         Returns complexScalarFieldWrapper ( ComplexScalarFieldWrapper NXOpen):  scalar field wrapper created and associated to the expression .
        """
        pass
    def CreateComplexScalarFieldWrapperWithField(self, field: Field) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed up by a complex scalar field 
         Returns complexScalarFieldWrapper ( ComplexScalarFieldWrapper NXOpen):  vector field wrapper created and associated to the field .
        """
        pass
    def CreateComplexScalarFieldWrapperWithFieldWithScaleFactor(self, field: Field, scaleFactor: float) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed up by a complex scalar field with scale factor 
         Returns complexScalarFieldWrapper ( ComplexScalarFieldWrapper NXOpen):  scalar field wrapper created and associated to the field .
        """
        pass
    def CreateComplexScalarFieldWrapperWithMagnitudePhaseExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed by two scalar magnitudephase expressions 
         Returns complexScalarFieldWrapper ( ComplexScalarFieldWrapper NXOpen):  scalar field wrapper created and associated to the expression .
        """
        pass
    def CreateComplexScalarFieldWrapperWithRealImaginaryExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexScalarFieldWrapper:
        """
         Create a complex scalar field wrapper backed by two scalar realimaginary expressions 
         Returns complexScalarFieldWrapper ( ComplexScalarFieldWrapper NXOpen):  scalar field wrapper created and associated to the expression .
        """
        pass
    def CreateComplexVectorFieldWrapperWithExpressions(self, expressions: List[NXOpen.Expression]) -> ComplexVectorFieldWrapper:
        """
         Create a complex vector field wrapper backed by six scalar expressions 
         Returns complexVectorFieldWrapper ( ComplexVectorFieldWrapper NXOpen):  scalar field wrapper created and associated to the expression .
        """
        pass
    def CreateComplexVectorFieldWrapperWithField(self, field: Field, scaleFactor: float) -> ComplexVectorFieldWrapper:
        """
         Create a complex vector field wrapper backed up by a complex vector field 
         Returns complexVectorFieldWrapper ( ComplexVectorFieldWrapper NXOpen):  vector field wrapper created and associated to the field .
        """
        pass
    @overload
    def CreateDependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit) -> FieldVariable:
        """
         Create a dependent variable to be added to the field 
                 
         Returns dep_var ( FieldVariable NXOpen):  dependent variable created and associated to the field .
        """
        pass
    @overload
    def CreateDependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit, type: FieldVariable.ValueType) -> FieldVariable:
        """
         Create a dependent variable to be added to the field, specifying the variable value type 
                 
         Returns dep_var ( FieldVariable NXOpen):  dependent variable created and associated to the field .
        """
        pass
    def CreateDisplayPropertiesBuilder(self, field_array: List[Field]) -> DisplayPropertiesBuilder:
        """
         Creates a NXOpen.Fields.DisplayPropertiesBuilder 
         Returns builder ( DisplayPropertiesBuilder NXOpen): .
        """
        pass
    def CreateExportData(self) -> ExportData:
        """
         Creates a Fields.ExportData 
         Returns export_data ( ExportData NXOpen):  the export data created .
        """
        pass
    def CreateFieldExpression(self, field_exp_string: str, unit_type: NXOpen.Unit) -> FieldExpression:
        """
         Creates a system NXOpen.Fields.FieldExpression object.  Specifies the new expression 
                    string.
                 
         Returns field_expression ( FieldExpression NXOpen):  field .
        """
        pass
    def CreateFieldFormula(self, field_name: str, indep_var_array: List[FieldVariable], dep_exp_array: List[FieldExpression]) -> FieldFormula:
        """
         Creates a NXOpen.Fields.FieldFormula object with dependent NXOpen.Fields.FieldExpression.
                 
         Returns field_formula ( FieldFormula NXOpen):  field .
        """
        pass
    def CreateFieldLink(self, field_name: str, field_to_link: Field) -> FieldLink:
        """
         Creates a NXOpen.Fields.FieldLink.
                 
         Returns field_link ( FieldLink NXOpen):  field .
        """
        pass
    @overload
    def CreateFieldLinksTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field]) -> FieldLinksTable:
        """
         Creates a NXOpen.Fields.FieldLinksTable object with dependent and independent variables 
                    NXOpen.Fields.FieldVariable.
                 
         Returns field_linkstable ( FieldLinksTable NXOpen):  links table field .
        """
        pass
    def CreateFieldLinksTableWithConstants(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> FieldLinksTable:
        """
         Creates a NXOpen.Fields.FieldLinksTable object with dependent and independent variables
                   with constant value user input NXOpen.Fields.FieldVariable.
                
         Returns field_linkstable ( FieldLinksTable NXOpen):  links table field .
        """
        pass
    @overload
    def CreateFieldLinksTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], link_fields_array: List[Field], managed_fields_array: List[bool]) -> FieldLinksTable:
        """
         Creates a NXOpen.Fields.FieldLinksTable object with dependent and independent variables 
                    NXOpen.Fields.FieldVariable.
                 
         Returns field_linkstable ( FieldLinksTable NXOpen):  links table field .
        """
        pass
    @overload
    def CreateFieldTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float]) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with dependent and independent variables 
                    NXOpen.Fields.FieldVariable.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    def CreateFieldTableFromData(self, field_name_prefix: str, ivar_unit: NXOpen.Unit, dvar_unit: NXOpen.Unit, dvar_type: FieldVariable.ValueType, datapoints: List[float]) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with dependent and independent variables
                    NXOpen.Fields.FieldVariable.  This will create a 2 dimensional table, with the option to specify 
                    the value type for the dependent variable.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    def CreateFieldTableFromDataAndDepVarName(self, field_name_prefix: str, ivar_unit: NXOpen.Unit, dvar_unit: NXOpen.Unit, dvar_type: FieldVariable.ValueType, dvar_name: str, datapoints: List[float]) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with dependent and independent variables
                    NXOpen.Fields.FieldVariable.  This will create a 2 dimensional table, with the option to specify 
                    the value type for the dependent variable, and to specify the Name for the Dependent variable. 
                    Used when the dependent variable name does not come from the Unit Measure.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    @overload
    def CreateFieldTableWithExpressions(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], dupValueProcessOption: FieldTable.DuplicateValueOption, exp_cell_ids: List[int], valueStrings: List[str]) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with duplicate value processing option,dependent and independent variables, and
                     expression strings.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    @overload
    def CreateFieldTableWithExpressions(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], dupValueProcessOption: FieldTable.DuplicateValueOption, exp_cell_ids: List[int], valueStrings: List[str], cellReadOnlys: List[bool]) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with duplicate value processing option,dependent and independent variables, and
                     expression strings.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    def CreateFieldTableWithPoints(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], duplicateValueProcessingOption: FieldTable.DuplicateValueOption, point_object_row_ids: List[int], point_objects: List[NXOpen.Point]) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with duplicate value processing option,dependent and independent variables, and smart points
                
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    @overload
    def CreateFieldTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], duplicateValueProcessingOption: FieldTable.DuplicateValueOption) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with duplicate value processing option,dependent and independent variables 
                    NXOpen.Fields.FieldVariable.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    @overload
    def CreateFieldTable(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], duplicateValueProcessingOption: FieldTable.DuplicateValueOption, struct_data_type: FieldTable.StructDataTableType, numStructDataRows: int, numStructDataColumns: int, numStructDataPlanes: int) -> FieldTable:
        """
         Creates a NXOpen.Fields.FieldTable object with Table Struct Data ,Duplicate value processing option,dependent and independent variables 
                    NXOpen.Fields.FieldVariable.
                 
         Returns field_table ( FieldTable NXOpen):  field .
        """
        pass
    def CreateFieldWrapper(self, field: Field) -> FieldWrapper:
        """
         Create a field wrapper backed up by a field 
         Returns fieldWrapper ( FieldWrapper NXOpen):  scalar field wrapper created and associated to the field .
        """
        pass
    def CreateGlobalSpatialMap(self) -> SpatialMap:
        """
         Creates a global NXOpen.Fields.SpatialMap 
         Returns spatialmap ( SpatialMap NXOpen): .
        """
        pass
    def CreateImportBuilder(self) -> ImportBuilder:
        """
         Creates a NXOpen.Fields.ImportBuilder 
         Returns pBuilder ( ImportBuilder NXOpen):  the import builder created .
        """
        pass
    def CreateImportTableDataBuilder(self, field_name: str, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable]) -> ImportTableDataBuilder:
        """
         Creates a NXOpen.Fields.ImportTableDataBuilder with inputs to create the field on commit
         Returns builder ( ImportTableDataBuilder NXOpen): .
        """
        pass
    def CreateImportTableDataBuilderFromTable(self, field_table: FieldTable) -> ImportTableDataBuilder:
        """
         Creates a NXOpen.Fields.ImportTableDataBuilder with inputs to create the field on commit
         Returns builder ( ImportTableDataBuilder NXOpen): .
        """
        pass
    @overload
    def CreateIndependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit, min_value_set: bool, min_value_inclusive: bool, min_value: float, max_value_set: bool, max_value_inclusive: bool, max_value: float, num_pts_set: bool, num_pts: int, default_value_set: bool, default_value: float) -> FieldVariable:
        """
         Create an independent variable to be added to the field 
                 
         Returns indep_var ( FieldVariable NXOpen):  independent variable created and associated to the field .
        """
        pass
    @overload
    def CreateIndependentVariable(self, owner_field: Field, name_variable: NameVariable, unit_type: NXOpen.Unit, type: FieldVariable.ValueType, min_value_set: bool, min_value_inclusive: bool, min_value: float, max_value_set: bool, max_value_inclusive: bool, max_value: float, num_pts_set: bool, num_pts: int, default_value_set: bool, default_value: float) -> FieldVariable:
        """
         Create an independent variable to be added to the field, specifying the variable value type
                 
         Returns indep_var ( FieldVariable NXOpen):  independent variable created and associated to the field .
        """
        pass
    def CreateMeshSizeFieldData(self, element_size_type: int, mesh_array: List[NXOpen.TaggedObject]) -> Field:
        """
         Create Mesh Size Field NXOpen.Fields.Field object
                 
         Returns field_meshsize ( Field NXOpen):  Created Field .
        """
        pass
    def CreatePathObjects(self) -> PathObjects:
        """
         Creates a NXOpen.Fields.PathObjects 
         Returns pathObjects ( PathObjects NXOpen): .
        """
        pass
    def CreateScalarFieldWrapperWithExpression(self, expression: NXOpen.Expression) -> ScalarFieldWrapper:
        """
         Create a field wrapper backed by a scalar expression 
         Returns scalarFieldWrapper ( ScalarFieldWrapper NXOpen):  scalar field wrapper created and associated to the expression .
        """
        pass
    def CreateScalarFieldWrapperWithField(self, field: Field, scaleFactor: float) -> ScalarFieldWrapper:
        """
         Create a scalar field wrapper backed up by a scaled scalar field 
         Returns scalarFieldWrapper ( ScalarFieldWrapper NXOpen):  scalar field wrapper created and associated to the field .
        """
        pass
    def CreateSpatialMapBuilder(self, spatialmap: SpatialMap) -> SpatialMapBuilder:
        """
         Creates a NXOpen.Fields.SpatialMapBuilder 
         Returns builder ( SpatialMapBuilder NXOpen): .
        """
        pass
    def CreateSubFieldExpression(self, dep_var: FieldVariable) -> FieldExpression:
        """
         Creates a system NXOpen.Fields.FieldExpression object with independent variables.
                    Specifies the new expression string.
                    This method is used to create sub expression fields for a 
                    NXOpen.Fields.FieldFormula.
                 
         Returns field_expression ( FieldExpression NXOpen):  field .
        """
        pass
    def CreateVectorFieldWrapperWithExpressions(self, expressions: List[NXOpen.Expression]) -> VectorFieldWrapper:
        """
         Create a vector field wrapper backed by three scalar expressions 
         Returns vectorFieldWrapper ( VectorFieldWrapper NXOpen):  scalar field wrapper created and associated to the expression .
        """
        pass
    def CreateVectorFieldWrapperWithField(self, field: Field, scaleFactors: List[float]) -> VectorFieldWrapper:
        """
         Create a vector field wrapper backed up by a scaled vector field 
         Returns vectorFieldWrapper ( VectorFieldWrapper NXOpen):  vector field wrapper created and associated to the field .
        """
        pass
    def DeleteField(self, field: Field) -> Field:
        """
         Deletes the specified NXOpen.Fields.Field object; if the object cannot be deleted
                    it is returned.
                 
         Returns field_surviving ( Field NXOpen):  If the field cannot be deleted, it is returned; if the field is deleted, this will be NULL .
        """
        pass
    def DeleteFields(self, fields: List[Field]) -> List[bool]:
        """
         Deletes the specified collections of NXOpen.Fields.Field objects;
                 
         Returns deletionStatus (List[bool]): .
        """
        pass
    def DeleteFolders(self, folders: List[FieldFolder]) -> List[Field]:
        """
         Deletes the specified NXOpen.Fields.FieldFolder folder and its contents.
                    Any fields that cannot be deleted will be returned to the root folder.
                 
         Returns survivingFields ( Field List[NXOp):  any fields that could not be deleted .
        """
        pass
    @overload
    def EditDependentVariable(self, dep_var: FieldVariable, var_name: str, unit_type: NXOpen.Unit) -> None:
        """
         Edit dependent variable 
                 
        """
        pass
    @overload
    def EditDependentVariable(self, dep_var: FieldVariable, unit_type: NXOpen.Unit) -> None:
        """
         Edit dependent variable 
                 
        """
        pass
    @overload
    def EditIndependentVariable(self, indep_var: FieldVariable, var_name: str, unit_type: NXOpen.Unit, min_value_set: bool, min_value_inclusive: bool, min_value: float, max_value_set: bool, max_value_inclusive: bool, max_value: float, num_pts_set: bool, num_pts: int, default_value_set: bool, default_value: float) -> None:
        """
         Edit an independent variable 
                 
        """
        pass
    @overload
    def EditIndependentVariable(self, indep_var: FieldVariable, unit_type: NXOpen.Unit) -> None:
        """
         Edit an independent variable 
                 
        """
        pass
    def ExportFields(self, export_data: ExportData) -> None:
        """
         Exports fields to a text file as defined by export_data parameter 
        """
        pass
    def GetNameVariable(self, variable_name: str, measure_name: str) -> NameVariable:
        """
         Locate an existing, or create a new NXOpen.Fields.NameVariable object 
         Returns name_variable ( NameVariable NXOpen):  name variable with the specified measure and name .
        """
        pass
    def GetValidFieldId(self) -> int:
        """
         Get the next available ID for NXOpen.Fields.Field object 
         Returns valid_id (int):  valid id .
        """
        pass
    def Information(self, fields: List[Field]) -> None:
        """
         Displays information about specified fields.
                 
        """
        pass
    def SetUndefinedVariableValue(self, undefinedValue: float) -> None:
        """
         Set the value to be used for un-set variables and plugin functions when evaluating an expression 
                
        """
        pass
class FieldReference(Field): 
    """  Represents an reference field  
    A Reference Field exposes data inside of an abstract data store.  An abstract data store
          is provided by an appropriate application data provider, and allows access to the provider
          data as a Fields.Field
    """
    @property
    def ValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
        Getter for property: ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation.  
          
                    If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
                    use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
                      
         
        """
        pass
    @ValuesOutsideTableInterpolation.setter
    def ValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum):
        """
        Setter for property: ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for linear interpolation.  
          
                    If the reference field is heterogeneous, this method gets the outside table values interpolation method for the primary independent doamin and
                    use set_secondary_values_outside_table_interpolation method for the secondary independent domain.
                      
         
        """
        pass
    def GetSecondaryValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
         If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .
                    Otherwise, an error will be raised.
                    
         Returns interpol_method ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen):  the outside table values interpolation method for sub fields.
        """
        pass
    def SetSecondaryValuesOutsideTableInterpolation(self, interpol_method: FieldEvaluator.ValuesOutsideTableInterpolationEnum) -> None:
        """
         If the reference field is heterogeneous, set the outside table values interpolation method for the secondary independent domain .
                    Otherwise, an error will be raised.
                    
        """
        pass
import NXOpen
import NXOpen.CAE.Xyplot
class FieldTable(Field): 
    """  Represents the Field Table class. 
    A field (see NXOpen.Fields.Field) defined in terms of tabular data involving 
    one or more look-up independent columns and one or more dependent variables (see 
    NXOpen.Fields.FieldVariable) which depend on the look-up columns. """
    class DBFactor(Enum):
        """
        Members Include: 
         |AcousticPowerDefault| 
         |AcousticPressureDefault| 

        """
        AcousticPowerDefault: int
        AcousticPressureDefault: int
        @staticmethod
        def ValueOf(value: int) -> FieldTable.DBFactor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DuplicateValueOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |Average| 
         |Minimum| 
         |Maximum| 
         |First| 
         |Last| 
         |Skip| 

        """
        NotSet: int
        Average: int
        Minimum: int
        Maximum: int
        First: int
        Last: int
        Skip: int
        @staticmethod
        def ValueOf(value: int) -> FieldTable.DuplicateValueOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LoadFileOption(Enum):
        """
        Members Include: 
         |Append|  Append data to the table removing duplicates 
         |Replace|  Replace data removing duplicates 

        """
        Append: int
        Replace: int
        @staticmethod
        def ValueOf(value: int) -> FieldTable.LoadFileOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StructDataTableType(Enum):
        """
        Members Include: 
         |Regular| 
         |Strict| 

        """
        Regular: int
        Strict: int
        @staticmethod
        def ValueOf(value: int) -> FieldTable.StructDataTableType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnnTolerance(self) -> float:
        """
        Getter for property: (float) AnnTolerance
         Returns
                the approximate nearest neighbor (ANN) interpolation tolerance 
                  
            
         
        """
        pass
    @AnnTolerance.setter
    def AnnTolerance(self, ann_tolerance: float):
        """
        Setter for property: (float) AnnTolerance
         Returns
                the approximate nearest neighbor (ANN) interpolation tolerance 
                  
            
         
        """
        pass
    @property
    def CreateInterpolatorOnCommit(self) -> bool:
        """
        Getter for property: (bool) CreateInterpolatorOnCommit
         Returns 
                a flag specifying if interpolator needs to be created on commit
                  
            
         
        """
        pass
    @CreateInterpolatorOnCommit.setter
    def CreateInterpolatorOnCommit(self, shouldCreateInterpolOnCommit: bool):
        """
        Setter for property: (bool) CreateInterpolatorOnCommit
         Returns 
                a flag specifying if interpolator needs to be created on commit
                  
            
         
        """
        pass
    @property
    def DelaunayDeleteSlivers(self) -> bool:
        """
        Getter for property: (bool) DelaunayDeleteSlivers
         Returns the option to delete sliver triangles from the resulting 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    @DelaunayDeleteSlivers.setter
    def DelaunayDeleteSlivers(self, delaunayDeleteSlivers: bool):
        """
        Setter for property: (bool) DelaunayDeleteSlivers
         Returns the option to delete sliver triangles from the resulting 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    @property
    def DelaunayRatioTolerance(self) -> float:
        """
        Getter for property: (float) DelaunayRatioTolerance
         Returns the option for ratio tolerance.  
           Edge Length Tolerance  1-edgelength(0)(edgelength(1)+edgelength(2)). Aspect Ratio Tolerance  (height from free edge to opposite vertex)(length of free edge). Applies to Delaunay interpolation only.   
         
        """
        pass
    @DelaunayRatioTolerance.setter
    def DelaunayRatioTolerance(self, delaunayRatioTolerance: float):
        """
        Setter for property: (float) DelaunayRatioTolerance
         Returns the option for ratio tolerance.  
           Edge Length Tolerance  1-edgelength(0)(edgelength(1)+edgelength(2)). Aspect Ratio Tolerance  (height from free edge to opposite vertex)(length of free edge). Applies to Delaunay interpolation only.   
         
        """
        pass
    @property
    def DelaunaySliverDetectionMethod(self) -> FieldEvaluator.DelaunaySliverDetectionMethodEnum:
        """
        Getter for property: ( FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen) DelaunaySliverDetectionMethod
         Returns the option specifyng the method used to determine if a triangle is a sliver of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    @DelaunaySliverDetectionMethod.setter
    def DelaunaySliverDetectionMethod(self, delaunaySliverDetectionMethod: FieldEvaluator.DelaunaySliverDetectionMethodEnum):
        """
        Setter for property: ( FieldEvaluator.DelaunaySliverDetectionMethodEnum NXOpen) DelaunaySliverDetectionMethod
         Returns the option specifyng the method used to determine if a triangle is a sliver of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    @property
    def DelaunaySnapVertices(self) -> bool:
        """
        Getter for property: (bool) DelaunaySnapVertices
         Returns the option to snap vertices from deleted sliver triangles to the convex hull of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    @DelaunaySnapVertices.setter
    def DelaunaySnapVertices(self, delaunaySnapVertices: bool):
        """
        Setter for property: (bool) DelaunaySnapVertices
         Returns the option to snap vertices from deleted sliver triangles to the convex hull of the 2D Delaunay interpolation mesh.  
            Applies to Delaunay interpolation only.   
         
        """
        pass
    @property
    def DelayedUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayedUpdate
         Returns the delayed update flag on the table is returned  
            
         
        """
        pass
    @DelayedUpdate.setter
    def DelayedUpdate(self, delayedUpdate: bool):
        """
        Setter for property: (bool) DelayedUpdate
         Returns the delayed update flag on the table is returned  
            
         
        """
        pass
    @property
    def Discontinuities(self) -> bool:
        """
        Getter for property: (bool) Discontinuities
         Returns a flag specifying if the table has discontinuites   
            
         
        """
        pass
    @property
    def DuplicateValueProcessingOption(self) -> FieldTable.DuplicateValueOption:
        """
        Getter for property: ( FieldTable.DuplicateValueOption NXOpen) DuplicateValueProcessingOption
         Returns the duplicate value processing option for field independent variable values, the zero value represents no option usedselected   
            
         
        """
        pass
    @DuplicateValueProcessingOption.setter
    def DuplicateValueProcessingOption(self, optionIndex: FieldTable.DuplicateValueOption):
        """
        Setter for property: ( FieldTable.DuplicateValueOption NXOpen) DuplicateValueProcessingOption
         Returns the duplicate value processing option for field independent variable values, the zero value represents no option usedselected   
            
         
        """
        pass
    @property
    def FallbackToDefaultInterpolator(self) -> bool:
        """
        Getter for property: (bool) FallbackToDefaultInterpolator
         Returns 
                a flag specifying if interpolator can fallback to a default interpolator, 
                if the creation of the given interpolator fails
                  
            
         
        """
        pass
    @FallbackToDefaultInterpolator.setter
    def FallbackToDefaultInterpolator(self, shouldFallbackToDefaultInterpolator: bool):
        """
        Setter for property: (bool) FallbackToDefaultInterpolator
         Returns 
                a flag specifying if interpolator can fallback to a default interpolator, 
                if the creation of the given interpolator fails
                  
            
         
        """
        pass
    @property
    def IndependentValueDivisor(self) -> float:
        """
        Getter for property: (float) IndependentValueDivisor
         Returns the linear interpolation divisor for field independent value, the zero value represents no divisor used   
            
         
        """
        pass
    @IndependentValueDivisor.setter
    def IndependentValueDivisor(self, divisor: float):
        """
        Setter for property: (float) IndependentValueDivisor
         Returns the linear interpolation divisor for field independent value, the zero value represents no divisor used   
            
         
        """
        pass
    @property
    def IndependentValueDivisorOption(self) -> bool:
        """
        Getter for property: (bool) IndependentValueDivisorOption
         Returns a value indicating whether to set the linear interpolation divisor for field independent value   
            
         
        """
        pass
    @IndependentValueDivisorOption.setter
    def IndependentValueDivisorOption(self, divisor_option: bool):
        """
        Setter for property: (bool) IndependentValueDivisorOption
         Returns a value indicating whether to set the linear interpolation divisor for field independent value   
            
         
        """
        pass
    @property
    def IndependentValueShift(self) -> float:
        """
        Getter for property: (float) IndependentValueShift
         Returns the linear interpolation shift for field independent value   
            
         
        """
        pass
    @IndependentValueShift.setter
    def IndependentValueShift(self, shift: float):
        """
        Setter for property: (float) IndependentValueShift
         Returns the linear interpolation shift for field independent value   
            
         
        """
        pass
    @property
    def IndependentValueShiftOption(self) -> bool:
        """
        Getter for property: (bool) IndependentValueShiftOption
         Returns a value indicating whether to set the linear interpolation shift for field independent value   
            
         
        """
        pass
    @IndependentValueShiftOption.setter
    def IndependentValueShiftOption(self, shift_option: bool):
        """
        Setter for property: (bool) IndependentValueShiftOption
         Returns a value indicating whether to set the linear interpolation shift for field independent value   
            
         
        """
        pass
    @property
    def InterpolationMethod(self) -> FieldEvaluator.InterpolationEnum:
        """
        Getter for property: ( FieldEvaluator.InterpolationEnum NXOpen) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolation_method: FieldEvaluator.InterpolationEnum):
        """
        Setter for property: ( FieldEvaluator.InterpolationEnum NXOpen) InterpolationMethod
         Returns  
                the interpolation method used when this table data is evaluated.  
          
                  
         
        """
        pass
    @property
    def LinearLogOption(self) -> FieldEvaluator.LinearLogOptionEnum:
        """
        Getter for property: ( FieldEvaluator.LinearLogOptionEnum NXOpen) LinearLogOption
         Returns  
                the linearlog option used when this table data is evaluated using the linear 1d interpolator.  
          
                  
         
        """
        pass
    @LinearLogOption.setter
    def LinearLogOption(self, linear_option: FieldEvaluator.LinearLogOptionEnum):
        """
        Setter for property: ( FieldEvaluator.LinearLogOptionEnum NXOpen) LinearLogOption
         Returns  
                the linearlog option used when this table data is evaluated using the linear 1d interpolator.  
          
                  
         
        """
        pass
    @property
    def ParameterizeIndependentDomain(self) -> bool:
        """
        Getter for property: (bool) ParameterizeIndependentDomain
         Returns the Parameterize Independent Domain option for Table field - toggle switch  
            
         
        """
        pass
    @ParameterizeIndependentDomain.setter
    def ParameterizeIndependentDomain(self, parameterizeIndependentDomain: bool):
        """
        Setter for property: (bool) ParameterizeIndependentDomain
         Returns the Parameterize Independent Domain option for Table field - toggle switch  
            
         
        """
        pass
    @property
    def PersistentInterpolator(self) -> bool:
        """
        Getter for property: (bool) PersistentInterpolator
         Returns 
                a flag specifying if interpolator is persistent between session 
                  
            
         
        """
        pass
    @PersistentInterpolator.setter
    def PersistentInterpolator(self, persistentInterpolator: bool):
        """
        Setter for property: (bool) PersistentInterpolator
         Returns 
                a flag specifying if interpolator is persistent between session 
                  
            
         
        """
        pass
    @property
    def SplineDegreeOption(self) -> FieldEvaluator.SplineDegreeOptionEnum:
        """
        Getter for property: ( FieldEvaluator.SplineDegreeOptionEnum NXOpen) SplineDegreeOption
         Returns  
                the degree option used when this table data is evaluated using the spline 1d interpolator.  
          
                  
         
        """
        pass
    @SplineDegreeOption.setter
    def SplineDegreeOption(self, degree_option: FieldEvaluator.SplineDegreeOptionEnum):
        """
        Setter for property: ( FieldEvaluator.SplineDegreeOptionEnum NXOpen) SplineDegreeOption
         Returns  
                the degree option used when this table data is evaluated using the spline 1d interpolator.  
          
                  
         
        """
        pass
    @property
    def ValuesOutsideHighTableUserdefinedValue(self) -> float:
        """
        Getter for property: (float) ValuesOutsideHighTableUserdefinedValue
         Returns the user defined value to return when the lookup value is greater than the highest value for the independent variable.  
            For 1-D independent domains only; 2-D and higher domains, this value is not used and will error out if accessed.   
         
        """
        pass
    @ValuesOutsideHighTableUserdefinedValue.setter
    def ValuesOutsideHighTableUserdefinedValue(self, userDefinedValueHi: float):
        """
        Setter for property: (float) ValuesOutsideHighTableUserdefinedValue
         Returns the user defined value to return when the lookup value is greater than the highest value for the independent variable.  
            For 1-D independent domains only; 2-D and higher domains, this value is not used and will error out if accessed.   
         
        """
        pass
    @property
    def ValuesOutsideTableInterpolation(self) -> FieldEvaluator.ValuesOutsideTableInterpolationEnum:
        """
        Getter for property: ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for standard linear interpolation   
            
         
        """
        pass
    @ValuesOutsideTableInterpolation.setter
    def ValuesOutsideTableInterpolation(self, interpolationMethod: FieldEvaluator.ValuesOutsideTableInterpolationEnum):
        """
        Setter for property: ( FieldEvaluator.ValuesOutsideTableInterpolationEnum NXOpen) ValuesOutsideTableInterpolation
         Returns the outside table values interpolation method for standard linear interpolation   
            
         
        """
        pass
    @property
    def ValuesOutsideTableUserdefinedValue(self) -> float:
        """
        Getter for property: (float) ValuesOutsideTableUserdefinedValue
         Returns the user defined value to return when lookup value is outside.  
           For 1-D domains, this is the value to return when the the lookup value is below the minimum value.  For 2-D and higher domains, this is the only value that can be specified.   
         
        """
        pass
    @ValuesOutsideTableUserdefinedValue.setter
    def ValuesOutsideTableUserdefinedValue(self, userDefinedValue: float):
        """
        Setter for property: (float) ValuesOutsideTableUserdefinedValue
         Returns the user defined value to return when lookup value is outside.  
           For 1-D domains, this is the value to return when the the lookup value is below the minimum value.  For 2-D and higher domains, this is the only value that can be specified.   
         
        """
        pass
    def CreateInterpolator(self) -> None:
        """
         Create an interpolator 
        """
        pass
    def DeleteStructureData(self) -> None:
        """
         Delete structure data 
        """
        pass
    def EditDbScaling(self, db_scale_factor: float, db_ref_value: float, is_db_scaling: bool) -> None:
        """
         Created a DbScaling object and returns true if successful 
        """
        pass
    def EditFieldTable(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float]) -> None:
        """
         Edit the table field.  Specifies the new array of NXOpen.Fields.FieldVariables for 
                independent and dependent variables, as well as the new double values.
                
        """
        pass
    def EditFieldTableComplexDisplay(self, indep_var_array_complex_display: List[bool], dep_var_array_complex_display: List[bool]) -> None:
        """
         Edit the table field complex display.  Specifies the new array of complex display flags for 
                independent and dependent variables.
                
        """
        pass
    def EditFieldTableComplexUnits(self, dep_var_array_complex_units: List[NXOpen.Unit]) -> None:
        """
         Edit the table field complex units array.  
                    Specifies the new array of complex phase unit tags for dependent variables.  
                    A NULL unit in a given index indicates that the corresponding variable is not complex, or if it is complex, that the value
                    is RealImaginary, in which both components have the same unit as the variable itself.  
                    In the case where the unit is specified, the complex dep variables in magnitudephase representation.  
                    In that case the measure of the specified unit must be angle. 
                
        """
        pass
    @overload
    def EditFieldTableWithExpressions(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], exp_cell_ids: List[int], value_strings: List[str]) -> None:
        """
         Edit the table field with expressions. 
        """
        pass
    @overload
    def EditFieldTableWithExpressions(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], exp_cell_ids: List[int], value_strings: List[str], cellReadOnlys: List[bool]) -> None:
        """
         Edit the table field with expressions. 
        """
        pass
    def EditFieldTableWithPoints(self, indep_var_array: List[FieldVariable], dep_var_array: List[FieldVariable], datapoints: List[float], point_object_row_ids: List[int], point_objects: List[NXOpen.Point]) -> None:
        """
         Edit the table field with point objects. 
        """
        pass
    def EditTableLatticeData(self, lattice_type: FieldTable.StructDataTableType, num_lattice_rows: int, num_lattice_columns: int, num_lattice_planes: int) -> None:
        """
         Edit the lattice table data.  Specifies lattice type,num of lattice rows,columns and planes.
                
        """
        pass
    def EditTableVariables(self, indep_var_array: List[FieldVariable], dep_exp_array: List[FieldVariable]) -> None:
        """
         Edit the table field dependent variables.  Specifies the new dependent NXOpen.Fields.FieldVariable
                array.  If retain number of rows is specified, the total number of rows will remain the same.  Columns with zeros will be added 
                as necessary, or data will be truncated.  This process will be handled for each set of variables, independent and dependent.
                Thus, if the number of independent columns increases and the dependent columns decrease, a column of zeros will be added for the
                new independent variable, and data will be dropped from the dependent values.
                
        """
        pass
    def GetData(self, variable: FieldVariable) -> List[float]:
        """
         Returns the values for the given NXOpen.Fields.FieldVariable in this NXOpen.Fields.FieldTable.  
                    The input NXOpen.Fields.FieldVariable should be retrieved from the field using 
                    NXOpen.Fields.Field.GetIndependentVariables or NXOpen.Fields.Field.GetDependentVariables. 
                    The values are in the same NXOpen.Unit as specified on the NXOpen.Fields.FieldVariable.
                
         Returns values (List[float]):  the row values for this variable .
        """
        pass
    def GetIdwOptions(self) -> Tuple[FieldEvaluator.InverseDistanceWeightingEnum, float, float, int, FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum]:
        """
         Get the inverse distance weighting (IDW) interpolation options 
         Returns A tuple consisting of (nearest_option, nearest_fraction, maximum_radius, number_of_points, power_of_distance). 
         - nearest_option is:  FieldEvaluator.InverseDistanceWeightingEnum NXOpen. nearest option   .
         - nearest_fraction is: float. fraction         .
         - maximum_radius is: float. maximum radius .
         - number_of_points is: int. number of points .
         - power_of_distance is:  FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum NXOpen.

        """
        pass
    def GetTablePoints(self) -> Tuple[List[int], List[NXOpen.Point]]:
        """
         Get point objects associated with table rows. 
         Returns A tuple consisting of (point_object_row_ids, point_objects). 
         - point_object_row_ids is: List[int]. 0 based row ID of rows that have associated point objects, in ascending order .
         - point_objects is:  NXOpen.Point Li. array of num_point_objects point objects associated to rows .

        """
        pass
    def GetVariableOffset(self, varType: FieldVariable.Type) -> NXOpen.Expression:
        """
         Get the offset value for the variable 
         Returns offset ( NXOpen.Expression):  the offset for the variable .
        """
        pass
    def GetVariableScaleFactor(self, varType: FieldVariable.Type) -> NXOpen.Expression:
        """
         Get the scale factor for the variable 
         Returns scaleFactor ( NXOpen.Expression):  the scale factor for the variable .
        """
        pass
    def LoadFromFile(self, filename: str, load_file_option: FieldTable.LoadFileOption) -> None:
        """
         Populate the table from a file replacing or appending data 
        """
        pass
    def ProcessPendingUpdate(self) -> None:
        """
         Process pending update 
        """
        pass
    def SetConservativeOptions(self, ann_tolerance: float, maximum_radius: float, number_of_points: int) -> None:
        """
         Set the conservative interpolation options 
        """
        pass
    def SetConservativeOptionsWithUnits(self, ann_tolerance: float, maximum_radius: float, maximum_radius_unit: NXOpen.Unit, number_of_points: int) -> None:
        """
         Set the conservative interpolation options 
        """
        pass
    def SetIdwOptions(self, nearest_option: FieldEvaluator.InverseDistanceWeightingEnum, nearest_fraction: float, maximum_radius: float, number_of_points: int, power_of_distance: FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum) -> None:
        """
         Set the inverse distance weighting (IDW) interpolation options 
        """
        pass
    def SetIdwOptionsWithUnits(self, nearest_option: FieldEvaluator.InverseDistanceWeightingEnum, nearest_fraction: float, maximum_radius: float, maximum_radius_unit: NXOpen.Unit, number_of_points: int, power_of_distance: FieldEvaluator.InverseDistanceWeightingPowerOfDistanceEnum) -> None:
        """
         The idw options are set with units 
        """
        pass
    def SetVariableOffset(self, varType: FieldVariable.Type, offset: NXOpen.Expression) -> None:
        """
         Set the offset value for the variable 
        """
        pass
    def SetVariableScaleFactor(self, varType: FieldVariable.Type, scaleFactor: NXOpen.Expression) -> None:
        """
         Set the scale factor for the variable 
        """
        pass
    def XYGraph3DStructuredData(self, x_axis_indep_var: FieldVariable, z_axis_indep_var: FieldVariable, y_axis_dep_var: FieldVariable, structured_data_plane_index: int, window_device: int, view_index: int, overlay: bool, scaleFactor: float) -> NXOpen.CAE.Xyplot.Plot:
        """
         Plots or overlays graphs of the Field's structured data versus the Field's specified y-axis dependent variable ; returns newly created plot object.
                    For Tables with 3 independent variables, the structured_data_plane_index parameter must be defined; for tables with 2 independent variables it is ignored.
                
         Returns plot ( NXOpen.CAE.Xyplot.Plot):  Created plot(s) .
        """
        pass
import NXOpen
class FieldVariable(NXOpen.NXObject): 
    """  Represents the Field Variables 
    A variable is a symbol on whose value a function, polynomial, etc., depends. For example,
    the variables in the function f(x,y) are x and y. A
    function having a single variable is said to be univariate, one having two variables is said to be
    bivariate, and one having three or more variables is said to be multivariate.  In NX, variables in
    this sense are specifically referred to as independent variables.

    In NX, variables are also used to describe the output of a function; these are referred to
    as the dependent variables.  In NX, a field with a single dependent variable is
    called a scalar field, with three variables of the same measure a vector field,
    all others are simply referred to as fields.

    In NX, all variables have a measure and associated unit type specification (see also
    NXOpen.Unit).
    """
    class Type(Enum):
        """
        Members Include: 
         |Unknown|  
         |Independent|  
         |Dependent|  

        """
        Unknown: int
        Independent: int
        Dependent: int
        @staticmethod
        def ValueOf(value: int) -> FieldVariable.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ValueType(Enum):
        """
        Members Include: 
         |Real|  real 
         |Imaginary|  (Legacy) imaginary 
         |ComplexRealImaginary|  (Legacy) complex_real_imaginary 
         |ComplexMagnitudePhase|  (Legacy) complex_magnitude_phase 
         |Complex|  Complex 
         |Integer|  Integer 

        """
        Real: int
        Imaginary: int
        ComplexRealImaginary: int
        ComplexMagnitudePhase: int
        Complex: int
        Integer: int
        @staticmethod
        def ValueOf(value: int) -> FieldVariable.ValueType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Bounds:
        """
         Variable Bounds structure 
         FieldVariableBounds_Struct NXOpen is an alias for  FieldVariable.Bounds NXOpen.
        """
        @property
        def IsMinimumDefined(self) -> bool:
            """
            Getter for property IsMinimumDefined
            true if minimum bound is defined

            """
            pass
        @IsMinimumDefined.setter
        def IsMinimumDefined(self, value: bool):
            """
            Getter for property IsMinimumDefined
            true if minimum bound is defined
            Setter for property IsMinimumDefined
            true if minimum bound is defined

            """
            pass
        @property
        def IsMinimumInclusive(self) -> bool:
            """
            Getter for property IsMinimumInclusive
            true if minimum bound is inclusive

            """
            pass
        @IsMinimumInclusive.setter
        def IsMinimumInclusive(self, value: bool):
            """
            Getter for property IsMinimumInclusive
            true if minimum bound is inclusive
            Setter for property IsMinimumInclusive
            true if minimum bound is inclusive

            """
            pass
        @property
        def MinimumValue(self) -> float:
            """
            Getter for property MinimumValue
            minimum bound value

            """
            pass
        @MinimumValue.setter
        def MinimumValue(self, value: float):
            """
            Getter for property MinimumValue
            minimum bound value
            Setter for property MinimumValue
            minimum bound value

            """
            pass
        @property
        def IsMaximumDefined(self) -> bool:
            """
            Getter for property IsMaximumDefined
            true if maximum bound is defined

            """
            pass
        @IsMaximumDefined.setter
        def IsMaximumDefined(self, value: bool):
            """
            Getter for property IsMaximumDefined
            true if maximum bound is defined
            Setter for property IsMaximumDefined
            true if maximum bound is defined

            """
            pass
        @property
        def IsMaximumInclusive(self) -> bool:
            """
            Getter for property IsMaximumInclusive
            true if maximum bound is inclusive

            """
            pass
        @IsMaximumInclusive.setter
        def IsMaximumInclusive(self, value: bool):
            """
            Getter for property IsMaximumInclusive
            true if maximum bound is inclusive
            Setter for property IsMaximumInclusive
            true if maximum bound is inclusive

            """
            pass
        @property
        def MaximumValue(self) -> float:
            """
            Getter for property MaximumValue
            maximum bound value

            """
            pass
        @MaximumValue.setter
        def MaximumValue(self, value: float):
            """
            Getter for property MaximumValue
            maximum bound value
            Setter for property MaximumValue
            maximum bound value

            """
            pass
    @property
    def DefaultValue(self) -> float:
        """
        Getter for property: (float) DefaultValue
         Returns the variable's default value which is value used when evaluating a field and no value is specified  
                  
            
         
        """
        pass
    @property
    def Logarithmic(self) -> bool:
        """
        Getter for property: (bool) Logarithmic
         Returns the flag indicating if the units for this variable are storedretrieved as logarithmic units    
                  
            
         
        """
        pass
    @property
    def NameVariable(self) -> NameVariable:
        """
        Getter for property: ( NameVariable NXOpen) NameVariable
         Returns the name variable for this variable.  
            
                  
         
        """
        pass
    @property
    def NumPoints(self) -> int:
        """
        Getter for property: (int) NumPoints
         Returns the number of points used for this variable when generating a table    
                  
            
         
        """
        pass
    @property
    def Units(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) Units
         Returns the units for this variable, which can be NULL if the variable is unitless.  
            
                  
         
        """
        pass
    @property
    def VariableBounds(self) -> FieldVariable.Bounds:
        """
        Getter for property: ( FieldVariable.Bounds NXOpen) VariableBounds
         Returns the variable's minimum and maximum bounds.  
          
                  
         
        """
        pass
    @property
    def VariableType(self) -> FieldVariable.Type:
        """
        Getter for property: ( FieldVariable.Type NXOpen) VariableType
         Returns the type of variable.  
            
                  
         
        """
        pass
import NXOpen
class FieldWrapper(NXOpen.NXObject): 
    """ This class defines a value that is internally backed up by a field. """
    def GetField(self) -> Field:
        """
         Returns the implementation 
         Returns field ( Field NXOpen):  an existing field .
        """
        pass
    def SetField(self, field: Field) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
import NXOpen
import NXOpen.CAE.Xyplot
class Field(NXOpen.DisplayableObject): 
    """ Represents an Field abstract class. 
        Fields represent a way of defining a function for one or more dependent 
        domainsvariables (see NXOpen.Fields.FieldVariable) based on relationships 
        to one or more independent domainsvariables (time, temperature, etc.).
        Fields are a generic, reusable concept that crosses many 
        areas of functionality.  Defined properly, they provide an extendable concept that can 
        service both simple and complicated needs, for example,  modeling elements, properties, 
        materials, boundary conditions in CAEFEM applications. """
    class PlotOption(Enum):
        """
        Members Include: 
         |InterpolatedValues| 
         |InterpolatedValuesWithBounds| 
         |RawTableValues| 

        """
        InterpolatedValues: int
        InterpolatedValuesWithBounds: int
        RawTableValues: int
        @staticmethod
        def ValueOf(value: int) -> Field.PlotOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsLocked(self) -> bool:
        """
        Getter for property: (bool) IsLocked
         Returns a value that indicates whether this field is locked against edits.  
           
                  
         
        """
        pass
    @property
    def IsUserField(self) -> bool:
        """
        Getter for property: (bool) IsUserField
         Returns a value that indicates whether this field is a user createdmanaged field.  
          
                    Many fields are created automatically by the system for internal uses. The life of these
                    fields is managed by the objects that own them and so these fields are 
                    not consider user fields. 
                  
         
        """
        pass
    def AddApplicationData(self, appData: IApplicationData) -> None:
        """
         Adds the specified application data object to the field
                     
                    NOTE: Only one application data object per IApplication can be added
                    and the data must be owned by an IApplication with the same Part::Field::Main 
                    as the field.  
                 
        """
        pass
    def CreateCopyInPart(self, target_part: NXOpen.BasePart) -> Field:
        """
         Copy the field to the target part.
                
         Returns new_field ( Field NXOpen):  newly created field .
        """
        pass
    def CreateTableInPart(self, target_part: NXOpen.BasePart) -> FieldTable:
        """
         Create a new table field from this field (regardless of type).  Note
                 that the table will be created have the N number of rows, where
                 N is the product of the number of points for each independent variable, 
                 resulting in a grid (or lattice).  The resulting field will be in the
                 same part.
                
         Returns new_table ( FieldTable NXOpen):  newly created table .
        """
        pass
    def Delete(self) -> None:
        """
         Delete this field; destroys the field and removes all references to it.
                
        """
        pass
    def GetApplicationData(self, applicationName: str) -> IApplicationData:
        """
         Retrieves the application data associated with the field for the specified application.
                 
         Returns appData ( IApplicationData NXOpen): .
        """
        pass
    def GetDependentVariables(self) -> List[FieldVariable]:
        """
         Returns the dependent variables for this NXOpen.Fields.Field  
                
         Returns dependent_variables ( FieldVariable List[NXOp):  dependent variables for this NXOpen.Fields.FieldVariable  .
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description of the field.
                
         Returns lines (List[str]):  description .
        """
        pass
    def GetFieldEvaluator(self) -> FieldEvaluator:
        """
         Returns a field evaluator which can be used to evaluate this field.
                
         Returns evaluator ( FieldEvaluator NXOpen):  Field Evaluator .
        """
        pass
    def GetFolder(self) -> FieldFolder:
        """
         Get the parent folder for this field.  A null folder returned is in the root collection. 
         Returns folder ( FieldFolder NXOpen):  folder .
        """
        pass
    def GetIdLabel(self) -> int:
        """
         Returns the IDLabel of the field.
                
         Returns id_label (int):  IDLabel .
        """
        pass
    def GetIndependentVariables(self) -> List[FieldVariable]:
        """
         Returns the independent variables for this NXOpen.Fields.Field  
                
         Returns independent_variables ( FieldVariable List[NXOp):  independent variables for this NXOpen.Fields.FieldVariable  .
        """
        pass
    def GetSpatialMap(self) -> SpatialMap:
        """
         Returns the spatial map for the formula field if one exists.
                
         Returns override_map ( SpatialMap NXOpen):  spatial map  .
        """
        pass
    def Reload(self) -> None:
        """
         Reloads the field from its data source.  If the data source does not support
                reload functionality or if the field does not have a data source
                the function will do nothing.
                
        """
        pass
    def Rename(self, new_name: str) -> None:
        """
         Update the name of the field.
                
        """
        pass
    def SetDescription(self, lines: List[str]) -> None:
        """
         Update the description of the field.
                
        """
        pass
    def SetIdLabel(self, id_label: int) -> None:
        """
         Update the IDLabel of the field.
                
        """
        pass
    def SetLocked(self, locked: bool) -> None:
        """
         Set lock value that indicates whether this field is locked against edits. 
                
        """
        pass
    def SetPartContext(self) -> None:
        """
         Set part context.
                
        """
        pass
    def SetSpatialMap(self, override_map: SpatialMap) -> None:
        """
         Set the spatial map for the formula field.
                
        """
        pass
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float]) -> None:
        """
         Creates displayed graphs of the Field's specified independent variable
                    versus all the Field's dependent variables
                 
        """
        pass
    def XYGraph3D(self, x_axis_indep_var: FieldVariable, x_axis_bnds_minimum: float, x_axis_bnds_maximum: float, x_axis_bnds_sample_size: int, z_axis_indep_var: FieldVariable, z_axis_bnds_minimum: float, z_axis_bnds_maximum: float, z_axis_bnds_sample_size: int, y_axis_dep_var: FieldVariable, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], interpolate_table_data: bool, window_device: int, view_index: int, overlay: bool, scaleFactor: float) -> NXOpen.CAE.Xyplot.Plot:
        """
         Plots or overlays graphs of the Field's specified x-axis and z-axis independent variables
                    versus the Field's specified y-axis dependent variable ; returns newly created plot object.
                 
         Returns plot ( NXOpen.CAE.Xyplot.Plot):  Created plot(s) .
        """
        pass
    def XYGraphArgand(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots the Field's specified independent variable 
                    versus all the Field's scaled dependent variables as an Argand graph; returns newly created plot object(s).
                 
         Returns plots ( NXOpen.CAE.Xyplot.Plot Li):  Created plot(s) .
        """
        pass
    def XYGraphPlotData(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool, scaleFactor: float, plotOption: Field.PlotOption) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots or overlays graphs of the Field's specified independent variable raw data or interpolated data
                    versus all the Field's scaled dependent variables; returns newly created plot object(s).
                 
         Returns plots ( NXOpen.CAE.Xyplot.Plot Li):  Created plot(s) .
        """
        pass
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], view_index: int, overlay: bool) -> None:
        """
         Plots or overlays graphs of the Field's specified independent variable
                    versus all the Field's dependent variables
                 
        """
        pass
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool) -> None:
        """
         Plots or overlays graphs of the Field's specified independent variable
                    versus all the Field's dependent variables
                 
        """
        pass
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots or overlays graphs of the Field's specified independent variable
                    versus all the Field's dependent variables; returns newly created plot object(s).
                 
         Returns plots ( NXOpen.CAE.Xyplot.Plot Li):  Created plot(s) .
        """
        pass
    @overload
    def XYGraph(self, indep_var: FieldVariable, abscissa_minimum: float, abscissa_maximum: float, abscissa_point_count: int, constant_indep_var_array: List[FieldVariable], constant_indep_var_value_array: List[float], window_device: int, view_index: int, overlay: bool, scaleFactor: float) -> List[NXOpen.CAE.Xyplot.Plot]:
        """
         Plots or overlays graphs of the Field's specified independent variable 
                    versus all the Field's scaled dependent variables; returns newly created plot object(s).
                 
         Returns plots ( NXOpen.CAE.Xyplot.Plot Li):  Created plot(s) .
        """
        pass
import NXOpen
class IApplicationData(NXOpen.INXObject): 
    """ Interface for all application specific data to be registered on fields. Only one 
    application specific data object per IApplication can be added to a field."""
    @abstractmethod
    def CopyToField(self, field: Field) -> None:
        """
         Copy the Application Data object to the specified field 
        """
        pass
    @abstractmethod
    def DeleteApplicationData(self) -> None:
        """
         Delete the Application Data object 
        """
        pass
    @abstractmethod
    def GetApplication(self) -> IApplication:
        """
         Returns the application associated with this application data object. 
         Returns application ( IApplication NXOpen): .
        """
        pass
import NXOpen
class IApplication(NXOpen.TaggedObject): 
    """ Interface for all applications registered with the Field subsystem. Each application
    type should only be registered once with the Field subsystem. Each application class is identified
    by its name."""
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the application.  
           This name should be unique for each application class.  
         
        """
        pass
import NXOpen
class ImportBuilder(NXOpen.Builder): 
    """ Represents a builder to import fields from a .fld formatted text file """
    class ActionType(Enum):
        """
        Members Include: 
         |Import| 
         |DontImport| 
         |ImportAppend| 
         |Replace| 
         |BackupAndReplace| 
         |ImportPrepend| 

        """
        Import: int
        DontImport: int
        ImportAppend: int
        Replace: int
        BackupAndReplace: int
        ImportPrepend: int
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConflictType(Enum):
        """
        Members Include: 
         |NoConflict| 
         |NameOnlyConflict| 
         |NameOnlyConflictInUse| 
         |CompatibleVariableConflict| 
         |CompatibleVariableConflictInUse| 
         |IncompatibleVariableConflict| 
         |IncompatibleVariableConflictInUse| 

        """
        NoConflict: int
        NameOnlyConflict: int
        NameOnlyConflictInUse: int
        CompatibleVariableConflict: int
        CompatibleVariableConflictInUse: int
        IncompatibleVariableConflict: int
        IncompatibleVariableConflictInUse: int
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ConflictType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportConflictStrategy(Enum):
        """
        Members Include: 
         |AppendtoImportedFieldName| 
         |PrependStringtoImportedFieldName| 
         |UserSpecifiedReplaceandorRename| 

        """
        AppendtoImportedFieldName: int
        PrependStringtoImportedFieldName: int
        UserSpecifiedReplaceandorRename: int
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ImportConflictStrategy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportFieldStrategy(Enum):
        """
        Members Include: 
         |Skip| 
         |RenameExisting| 
         |RenameImported| 
         |Replace| 
         |BackupReplace| 

        """
        Skip: int
        RenameExisting: int
        RenameImported: int
        Replace: int
        BackupReplace: int
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ImportFieldStrategy:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportFilter(Enum):
        """
        Members Include: 
         |All| 
         |Formula| 
         |Table| 
         |LinkedField| 
         |TableofFields| 
         |FilterbyName| 
         |FilterbyDomain| 
         |FilterbyDependentVariableName| 
         |FilterbyIndependentVariableName| 

        """
        All: int
        Formula: int
        Table: int
        LinkedField: int
        TableofFields: int
        FilterbyName: int
        FilterbyDomain: int
        FilterbyDependentVariableName: int
        FilterbyIndependentVariableName: int
        @staticmethod
        def ValueOf(value: int) -> ImportBuilder.ImportFilter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConflictResolutionStrategy(self) -> ImportBuilder.ImportConflictStrategy:
        """
        Getter for property: ( ImportBuilder.ImportConflictStrategy NXOpen) ConflictResolutionStrategy
         Returns the conflict resolution strategy   
            
         
        """
        pass
    @ConflictResolutionStrategy.setter
    def ConflictResolutionStrategy(self, conflictResolutionStrategy: ImportBuilder.ImportConflictStrategy):
        """
        Setter for property: ( ImportBuilder.ImportConflictStrategy NXOpen) ConflictResolutionStrategy
         Returns the conflict resolution strategy   
            
         
        """
        pass
    @property
    def FilterOptions(self) -> ImportBuilder.ImportFilter:
        """
        Getter for property: ( ImportBuilder.ImportFilter NXOpen) FilterOptions
         Returns the filter options   
            
         
        """
        pass
    @FilterOptions.setter
    def FilterOptions(self, filterOptions: ImportBuilder.ImportFilter):
        """
        Setter for property: ( ImportBuilder.ImportFilter NXOpen) FilterOptions
         Returns the filter options   
            
         
        """
        pass
    @property
    def FilterString(self) -> str:
        """
        Getter for property: (str) FilterString
         Returns the filter string   
            
         
        """
        pass
    @FilterString.setter
    def FilterString(self, filterString: str):
        """
        Setter for property: (str) FilterString
         Returns the filter string   
            
         
        """
        pass
    @property
    def ImportField(self) -> Field:
        """
        Getter for property: ( Field NXOpen) ImportField
         Returns the imported field   
            
         
        """
        pass
    @ImportField.setter
    def ImportField(self, import_field: Field):
        """
        Setter for property: ( Field NXOpen) ImportField
         Returns the imported field   
            
         
        """
        pass
    @property
    def ImportFile(self) -> str:
        """
        Getter for property: (str) ImportFile
         Returns the import file   
            
         
        """
        pass
    @ImportFile.setter
    def ImportFile(self, filename: str):
        """
        Setter for property: (str) ImportFile
         Returns the import file   
            
         
        """
        pass
    @property
    def ImportFolders(self) -> bool:
        """
        Getter for property: (bool) ImportFolders
         Returns the import folders option   
            
         
        """
        pass
    @ImportFolders.setter
    def ImportFolders(self, importFolders: bool):
        """
        Setter for property: (bool) ImportFolders
         Returns the import folders option   
            
         
        """
        pass
    @property
    def PrependString(self) -> str:
        """
        Getter for property: (str) PrependString
         Returns the prepend string   
            
         
        """
        pass
    @PrependString.setter
    def PrependString(self, prependString: str):
        """
        Setter for property: (str) PrependString
         Returns the prepend string   
            
         
        """
        pass
    def GetImportAction(self, nthField: int) -> int:
        """
         Get the import action 
         Returns action (int): .
        """
        pass
    def GetNthConflictType(self, nthField: int) -> ImportBuilder.ConflictType:
        """
         Get the nth field conflict type 
         Returns conflict ( ImportBuilder.ConflictType NXOpen): .
        """
        pass
    def GetNthFieldName(self, nthField: int) -> str:
        """
         Get the nth field name 
         Returns importFieldName (str): .
        """
        pass
    def GetNthImportAction(self, nthField: int) -> ImportBuilder.ActionType:
        """
         Get the nth field import action 
         Returns action ( ImportBuilder.ActionType NXOpen): .
        """
        pass
    def GetNumFields(self) -> int:
        """
         Get the number of fields in import file 
         Returns numberOfFields (int): .
        """
        pass
    def SetImportAction(self, nthField: int, action: int) -> None:
        """
         Set the import action 
        """
        pass
    def SetNthImportAction(self, nthField: int, action: ImportBuilder.ActionType) -> None:
        """
         Set the nth field import action 
        """
        pass
import NXOpen
class ImportTableDataBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Fields.ImportTableDataBuilder builder 
    which can be used to import data for NXOpen.Fields.FieldTable """
    @property
    def CreateSpatialMap(self) -> bool:
        """
        Getter for property: (bool) CreateSpatialMap
         Returns the create spatial map value   
            
         
        """
        pass
    @CreateSpatialMap.setter
    def CreateSpatialMap(self, createSpatialMap: bool):
        """
        Setter for property: (bool) CreateSpatialMap
         Returns the create spatial map value   
            
         
        """
        pass
    @property
    def DuplicateValues(self) -> FieldTable.DuplicateValueOption:
        """
        Getter for property: ( FieldTable.DuplicateValueOption NXOpen) DuplicateValues
         Returns the duplicate value option   
            
         
        """
        pass
    @DuplicateValues.setter
    def DuplicateValues(self, duplicate_value_option: FieldTable.DuplicateValueOption):
        """
        Setter for property: ( FieldTable.DuplicateValueOption NXOpen) DuplicateValues
         Returns the duplicate value option   
            
         
        """
        pass
    @property
    def ImportFile(self) -> str:
        """
        Getter for property: (str) ImportFile
         Returns the import data file   
            
         
        """
        pass
    @ImportFile.setter
    def ImportFile(self, filename: str):
        """
        Setter for property: (str) ImportFile
         Returns the import data file   
            
         
        """
        pass
    @property
    def IsStructDataFormat(self) -> bool:
        """
        Getter for property: (bool) IsStructDataFormat
         Returns the is structured data value   
            
         
        """
        pass
    @IsStructDataFormat.setter
    def IsStructDataFormat(self, structured_data_format: bool):
        """
        Setter for property: (bool) IsStructDataFormat
         Returns the is structured data value   
            
         
        """
        pass
    @property
    def NumStructDataColumns(self) -> int:
        """
        Getter for property: (int) NumStructDataColumns
         Returns the number of structured data columns   
            
         
        """
        pass
    @NumStructDataColumns.setter
    def NumStructDataColumns(self, numColumns: int):
        """
        Setter for property: (int) NumStructDataColumns
         Returns the number of structured data columns   
            
         
        """
        pass
    @property
    def NumStructDataPlanes(self) -> int:
        """
        Getter for property: (int) NumStructDataPlanes
         Returns the number of structured data planes   
            
         
        """
        pass
    @NumStructDataPlanes.setter
    def NumStructDataPlanes(self, numPlanes: int):
        """
        Setter for property: (int) NumStructDataPlanes
         Returns the number of structured data planes   
            
         
        """
        pass
    @property
    def NumStructDataRows(self) -> int:
        """
        Getter for property: (int) NumStructDataRows
         Returns the number of structured data rows   
            
         
        """
        pass
    @NumStructDataRows.setter
    def NumStructDataRows(self, numRows: int):
        """
        Setter for property: (int) NumStructDataRows
         Returns the number of structured data rows   
            
         
        """
        pass
    def RescanImportFile(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def SetClearTableOnImport(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ManualInputProfileBuilder(NXOpen.TaggedObject): 
    """ 
            Represents a builder class for creating and editing an NXOpen.Fields.Field
            that is defined by manual input data.
        """
    class CyclicType(Enum):
        """
        Members Include: 
         |NotSet|  not cyclic 
         |XOnly|  cyclic in x direction 

        """
        NotSet: int
        XOnly: int
        @staticmethod
        def ValueOf(value: int) -> ManualInputProfileBuilder.CyclicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Extrapolation(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Parabolic|  Parabolic 

        """
        Linear: int
        Parabolic: int
        @staticmethod
        def ValueOf(value: int) -> ManualInputProfileBuilder.Extrapolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Interpolation(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Akima|  Akima 
         |Akima72|  Akima72 
         |Cubic|  Cubic 

        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> ManualInputProfileBuilder.Interpolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Cyclic(self) -> ManualInputProfileBuilder.CyclicType:
        """
        Getter for property: ( ManualInputProfileBuilder.CyclicType NXOpen) Cyclic
         Returns   
                    the cyclic type.  
          
                 
         
                
                    
                       NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone 
                       NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly 
                    
                  
         
        """
        pass
    @Cyclic.setter
    def Cyclic(self, cyclicType: ManualInputProfileBuilder.CyclicType):
        """
        Setter for property: ( ManualInputProfileBuilder.CyclicType NXOpen) Cyclic
         Returns   
                    the cyclic type.  
          
                 
         
                
                    
                       NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone 
                       NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeXOnly 
                    
                  
         
        """
        pass
    @property
    def OrdinateOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OrdinateOffset
         Returns   
                    the offset on the ordinate axis.  
          
                 
           
         
        """
        pass
    @property
    def OrdinateScale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OrdinateScale
         Returns   
                    the scale on the ordinate axis.  
          
                 
         
                The scale is unitless.  
         
        """
        pass
    @property
    def OrdinateUnitType(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) OrdinateUnitType
         Returns   the unit type corresponding to the ordinate axis.  
           
            
         
        """
        pass
    @OrdinateUnitType.setter
    def OrdinateUnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) OrdinateUnitType
         Returns   the unit type corresponding to the ordinate axis.  
           
            
         
        """
        pass
    @property
    def SlopeLeft(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeLeft
         Returns   
                    the left slope.  
          
                 
         
                
                    This is only used when  NXOpen::Fields::ManualInputProfileBuilder::CyclicType 
                    is set to  NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone 
                  
         
        """
        pass
    @property
    def SlopeRight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeRight
         Returns   
                    the right slope.  
          
                 
         
                
                    This is only used when  NXOpen::Fields::ManualInputProfileBuilder::CyclicType 
                    is set to  NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone 
                  
         
        """
        pass
    @property
    def SolverOptions(self) -> ProfileSolverOptionsBuilder:
        """
        Getter for property: ( ProfileSolverOptionsBuilder NXOpen) SolverOptions
         Returns   the solver options.  
           
           
         
        """
        pass
    @property
    def XExtrapolation(self) -> ManualInputProfileBuilder.Extrapolation:
        """
        Getter for property: ( ManualInputProfileBuilder.Extrapolation NXOpen) XExtrapolation
         Returns   
                    the extrapolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic 
                    
                      
                        This is only used when  NXOpen::Fields::ManualInputProfileBuilder::CyclicType 
                        is set to  NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone 
                      
                  
         
        """
        pass
    @XExtrapolation.setter
    def XExtrapolation(self, extrapolation: ManualInputProfileBuilder.Extrapolation):
        """
        Setter for property: ( ManualInputProfileBuilder.Extrapolation NXOpen) XExtrapolation
         Returns   
                    the extrapolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ManualInputProfileBuilder::ExtrapolationParabolic 
                    
                      
                        This is only used when  NXOpen::Fields::ManualInputProfileBuilder::CyclicType 
                        is set to  NXOpen::Fields::ManualInputProfileBuilder::CyclicTypeNone 
                      
                  
         
        """
        pass
    @property
    def XInterpolation(self) -> ManualInputProfileBuilder.Interpolation:
        """
        Getter for property: ( ManualInputProfileBuilder.Interpolation NXOpen) XInterpolation
         Returns   
                    the interpolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear 
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima 
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72 
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic 
                    
                  
         
        """
        pass
    @XInterpolation.setter
    def XInterpolation(self, interpolation: ManualInputProfileBuilder.Interpolation):
        """
        Setter for property: ( ManualInputProfileBuilder.Interpolation NXOpen) XInterpolation
         Returns   
                    the interpolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationLinear 
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima 
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationAkima72 
                       NXOpen::Fields::ManualInputProfileBuilder::InterpolationCubic 
                    
                  
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns   
                    the offset on the x axis.  
          
                 
           
         
        """
        pass
    @property
    def XScale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XScale
         Returns   
                    the scale on the x axis.  
          
                 
         
                The scale is unitless.  
         
        """
        pass
    @property
    def XUnitType(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) XUnitType
         Returns   the unit type corresponding to the x axis.  
           
            
         
        """
        pass
    @XUnitType.setter
    def XUnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) XUnitType
         Returns   the unit type corresponding to the x axis.  
           
            
         
        """
        pass
    def SetDataPointExpressions(self, dataPointCellIds: List[int], dataPointExpressions: List[str]) -> None:
        """
         
                    Sets the data point expressions.
                
                
                    Some or all data points can be overridden by expressions.
                    The cell ids for the cells to be defined by an expression need to be given in the form: row  numColumns + column.
                    For 2D curves numColumn = 2.
                    The expression is defined in a string. e.g. "1+2" or "3[m]"
                
        """
        pass
    def SetDataPointValues(self, dataPoints: List[float]) -> None:
        """
         
                    Sets the data point values.
                
                
                    The data points are listed as double values row after row.
                    e.g. 3 Curve points (1, 3.4), (2.5, 6.7), (4.25, -3.1)
                    appear as 1, 3.4, 2.5, 6.7, 4.25, -3.1
                
        """
        pass
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        """
         
                    If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
                
                
                    It is recommended to call this method when editing a profile that is referenced by another object,
                    which depends on specific measures.
                
        """
        pass
class ManualInputProfile(FieldTable): 
    """  Represents the Manual Input Profile class. """
    pass
import NXOpen
class NameVariable(NXOpen.NXObject): 
    """ This class stores the common name and measure for field variables. """
    @property
    def Measure(self) -> str:
        """
        Getter for property: (str) Measure
         Returns the measure of the variable   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the variable   
            
         
        """
        pass
import NXOpen
class PathObjectsList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PathObjects]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PathObjects) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: PathObjects) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PathObjects, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PathObjects) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PathObjects:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PathObjects NXOpen):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PathObjects]:
        """
         Gets the contents of the entire list 
         Returns objects ( PathObjects List[NXOp):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PathObjects) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[PathObjects]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: PathObjects, object2: PathObjects) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PathObjects(NXOpen.SelectObjectList): 
    """  Contains objects that define a lattice path  """
    def HandleLatestSelDirection(self) -> None:
        """
         Check the direction of the lastest selection and reverse it if necessary 
        """
        pass
    def ReverseDirection(self) -> None:
        """
         Reverses the order of the objects in the path 
        """
        pass
    def ReverseSectionDirection(self, index: int) -> None:
        """
         Reverses the order of the objects in the path 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ProfileSolverOptionsBuilder(NXOpen.TaggedObject): 
    """ 
            Represents a builder class to handle the solver options of an NXOpen.Fields.Field.
        """
    class CyclicType(Enum):
        """
        Members Include: 
         |NotSet|  not cyclic 
         |XOnly|  cyclic in x direction 
         |YOnly|  cyclic in y direction 
         |Both|  cyclic in both x and y direction 

        """
        NotSet: int
        XOnly: int
        YOnly: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> ProfileSolverOptionsBuilder.CyclicType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Extrapolation(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Parabolic|  Parabolic 
         |Cubic|  Cubic 

        """
        Linear: int
        Parabolic: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> ProfileSolverOptionsBuilder.Extrapolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Interpolation(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Akima|  Akima 
         |Akima72|  Akima72 
         |Cubic|  Cubic 

        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> ProfileSolverOptionsBuilder.Interpolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Cyclic(self) -> ProfileSolverOptionsBuilder.CyclicType:
        """
        Getter for property: ( ProfileSolverOptionsBuilder.CyclicType NXOpen) Cyclic
         Returns   
                    the cyclic type.  
          
                 
         
                
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly 
                    
                  
         
        """
        pass
    @Cyclic.setter
    def Cyclic(self, cyclicType: ProfileSolverOptionsBuilder.CyclicType):
        """
        Setter for property: ( ProfileSolverOptionsBuilder.CyclicType NXOpen) Cyclic
         Returns   
                    the cyclic type.  
          
                 
         
                
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly 
                    
                  
         
        """
        pass
    @property
    def SlopeLeft(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeLeft
         Returns   
                    the left slope.  
          
                 
         
                
                    This is only used when  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType 
                    is set to  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                  
         
        """
        pass
    @property
    def SlopeRight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlopeRight
         Returns   
                    the right slope.  
          
                 
         
                
                    This is only used when  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType 
                    is set to  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                  
         
        """
        pass
    @property
    def XExtrapolation(self) -> ProfileSolverOptionsBuilder.Extrapolation:
        """
        Getter for property: ( ProfileSolverOptionsBuilder.Extrapolation NXOpen) XExtrapolation
         Returns   
                    the extrapolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic 
                    
                      
                        This is only used when  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType 
                        is set to  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                      
                  
         
        """
        pass
    @XExtrapolation.setter
    def XExtrapolation(self, extrapolation: ProfileSolverOptionsBuilder.Extrapolation):
        """
        Setter for property: ( ProfileSolverOptionsBuilder.Extrapolation NXOpen) XExtrapolation
         Returns   
                    the extrapolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic 
                    
                      
                        This is only used when  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicType 
                        is set to  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                      
                  
         
        """
        pass
    @property
    def XInterpolation(self) -> ProfileSolverOptionsBuilder.Interpolation:
        """
        Getter for property: ( ProfileSolverOptionsBuilder.Interpolation NXOpen) XInterpolation
         Returns   
                    the interpolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic 
                    
                  
         
        """
        pass
    @XInterpolation.setter
    def XInterpolation(self, interpolation: ProfileSolverOptionsBuilder.Interpolation):
        """
        Setter for property: ( ProfileSolverOptionsBuilder.Interpolation NXOpen) XInterpolation
         Returns   
                    the interpolation in x direction.  
          
                 
         
                
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic 
                    
                  
         
        """
        pass
    @property
    def YExtrapolation(self) -> ProfileSolverOptionsBuilder.Extrapolation:
        """
        Getter for property: ( ProfileSolverOptionsBuilder.Extrapolation NXOpen) YExtrapolation
         Returns   
                    the extrapolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic 
                    
                      
                    This is only used surface profiles
                    and when  NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType 
                    is set to  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                    or  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly 
                      
                      
         
        """
        pass
    @YExtrapolation.setter
    def YExtrapolation(self, extrapolation: ProfileSolverOptionsBuilder.Extrapolation):
        """
        Setter for property: ( ProfileSolverOptionsBuilder.Extrapolation NXOpen) YExtrapolation
         Returns   
                    the extrapolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationParabolic 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::ExtrapolationCubic 
                    
                      
                    This is only used surface profiles
                    and when  NXOpen::Fields::ProfileSolverOptionsBuilder::SetCyclicType 
                    is set to  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeNone 
                    or  NXOpen::Fields::ProfileSolverOptionsBuilder::CyclicTypeXOnly 
                      
                      
         
        """
        pass
    @property
    def YInterpolation(self) -> ProfileSolverOptionsBuilder.Interpolation:
        """
        Getter for property: ( ProfileSolverOptionsBuilder.Interpolation NXOpen) YInterpolation
         Returns   
                    the interpolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic 
                    
                      
                    This is only used surface profiles
                      
                      
         
        """
        pass
    @YInterpolation.setter
    def YInterpolation(self, interpolation: ProfileSolverOptionsBuilder.Interpolation):
        """
        Setter for property: ( ProfileSolverOptionsBuilder.Interpolation NXOpen) YInterpolation
         Returns   
                    the interpolation in y direction.  
          
                     
         
                    
                    
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationLinear 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationAkima72 
                       NXOpen::Fields::ProfileSolverOptionsBuilder::InterpolationCubic 
                    
                      
                    This is only used surface profiles
                      
                      
         
        """
        pass
import NXOpen
class ScalarFieldWrapper(NXOpen.NXObject): 
    """ This class defines a scalar value that is internally 
        backed up by a (optionally scaled) field or an expression. """
    def GetExpression(self) -> NXOpen.Expression:
        """
         Returns the implementation if the wrapper is backed up by an expression;
                    NULL otherwise 
         Returns expression ( NXOpen.Expression):  an existing expression or NULL .
        """
        pass
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field;
                    NULL otherwise 
         Returns field ( Field NXOpen):  an existing field or NULL .
        """
        pass
    def GetFieldScaleFactor(self) -> float:
        """
         Returns the scale factor to be applied to the field, this is only applicable if the wrapper is backed up by a field 
         Returns scale_factor (float):  the field will be multiplied by this scale factor when being evaluated .
        """
        pass
    def SetExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the implementation of the wrapper to the specified expression 
        """
        pass
    def SetField(self, field: Field, scale_factor: float) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SketchProfileBuilder(NXOpen.TaggedObject): 
    """ 
            Represents a builder class for creating and editing an NXOpen.Fields.Field
            that is defined by a sketch.
        
        
            It is mandatory to select a valid NXOpen.Fields.SketchProfileBuilder.Sketch.
        
    """
    class InterpolationType(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Akima|  Akima 
         |Akima72|  Akima72 
         |Cubic|  Cubic 

        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> SketchProfileBuilder.InterpolationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SamplingPointType(Enum):
        """
        Members Include: 
         |ChordalTolerance|  Chordal tolerance type 
         |EqualArcLength|  Equal arc length type 

        """
        ChordalTolerance: int
        EqualArcLength: int
        @staticmethod
        def ValueOf(value: int) -> SketchProfileBuilder.SamplingPointType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ChordalTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChordalTolerance
         Returns   the chordal tolerance.  
           
           
         
        """
        pass
    @property
    def DiscretePointType(self) -> FieldProfileTable.SamplingPointOption:
        """
        Getter for property: ( FieldProfileTable.SamplingPointOption NXOpen) DiscretePointType
         Returns   the discrete point type.  
           
         
                    
                    
                       NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance 
                       NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength 
                    
                      
         
        """
        pass
    @DiscretePointType.setter
    def DiscretePointType(self, type: FieldProfileTable.SamplingPointOption):
        """
        Setter for property: ( FieldProfileTable.SamplingPointOption NXOpen) DiscretePointType
         Returns   the discrete point type.  
           
         
                    
                    
                       NXOpen::Fields::FieldProfileTable::SamplingPointOptionChordalTolerance 
                       NXOpen::Fields::FieldProfileTable::SamplingPointOptionEqualArcLength 
                    
                      
         
        """
        pass
    @property
    def Interpolation(self) -> SketchProfileBuilder.InterpolationType:
        """
        Getter for property: ( SketchProfileBuilder.InterpolationType NXOpen) Interpolation
         Returns   the interpolation type.  
           
         
                    
                    
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear 
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima 
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72 
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic 
                    
                      
         
        """
        pass
    @Interpolation.setter
    def Interpolation(self, type: SketchProfileBuilder.InterpolationType):
        """
        Setter for property: ( SketchProfileBuilder.InterpolationType NXOpen) Interpolation
         Returns   the interpolation type.  
           
         
                    
                    
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeLinear 
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima 
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeAkima72 
                       NXOpen::Fields::SketchProfileBuilder::InterpolationTypeCubic 
                    
                      
         
        """
        pass
    @property
    def NumberPoints(self) -> int:
        """
        Getter for property: (int) NumberPoints
         Returns   the number of points.  
           
           
         
        """
        pass
    @NumberPoints.setter
    def NumberPoints(self, type: int):
        """
        Setter for property: (int) NumberPoints
         Returns   the number of points.  
           
           
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns   the offset.  
           
         
                    
                    The unit of the offset has to match the
                     NXOpen::Fields::SketchProfileBuilder::UnitType .
                      
         
        """
        pass
    @property
    def PointSamplingType(self) -> SketchProfileBuilder.SamplingPointType:
        """
        Getter for property: ( SketchProfileBuilder.SamplingPointType NXOpen) PointSamplingType
         Returns   the discrete point type.  
           
         
                    
                    
                       NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance 
                       NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength 
                    
                      
         
        """
        pass
    @PointSamplingType.setter
    def PointSamplingType(self, type: SketchProfileBuilder.SamplingPointType):
        """
        Setter for property: ( SketchProfileBuilder.SamplingPointType NXOpen) PointSamplingType
         Returns   the discrete point type.  
           
         
                    
                    
                       NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeChordalTolerance 
                       NXOpen::Fields::SketchProfileBuilder::SamplingPointTypeEqualArcLength 
                    
                      
         
        """
        pass
    @property
    def Points(self) -> NXOpen.PointList:
        """
        Getter for property: ( NXOpen.PointList) Points
         Returns   the list of points.  
           
            
         
        """
        pass
    @property
    def Scale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Scale
         Returns   the scale.  
           
         
                    
                    The scale is unitless.
                      
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.SelectSketch:
        """
        Getter for property: ( NXOpen.SelectSketch) Sketch
         Returns   the sketch.  
           
         
                    
                    For the sketch to be valid
                    
                      its start point must be at x=0
                      it must be continuous
                      it cannot have two y values at the same x value
                    
                      
         
        """
        pass
    @property
    def UnitType(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) UnitType
         Returns   the unit type.  
           
            
         
        """
        pass
    @UnitType.setter
    def UnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) UnitType
         Returns   the unit type.  
           
            
         
        """
        pass
    def SetMeasuresFixed(self, areMeasuresFixed: bool) -> None:
        """
         
                    If the measures are marked as fixed and they are changed, the validation at commit will detect an error and fail.
                
                
                    It is recommended to call this method when editing a profile that is referenced by another object,
                    which depends on specific measures.
                
        """
        pass
import NXOpen
class SpatialMapBuilder(NXOpen.Builder): 
    """  Represents a NXOpen.Fields.SpatialMap builder 
    Used to create and or edit a NXOpen.Fields.SpatialMap.
    """
    class FitSurfaceDirectionType(Enum):
        """
        Members Include: 
         |BestFit| The fit target is sort of rectangular.
         |Vector| Vector will specify the fit direction.
         |Orientation| Orientation will specify the direction and UV orientation. 
         |Csys| CSYS will specify same as orientation but with the need to make it associative with existing geometry. 

        """
        BestFit: int
        Vector: int
        Orientation: int
        Csys: int
        @staticmethod
        def ValueOf(value: int) -> SpatialMapBuilder.FitSurfaceDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) BoundedObjects
         Returns the bounded objects   
            
         
        """
        pass
    @property
    def BoundingBoxMap(self) -> SpatialMap.BoundingBoxMapEnum:
        """
        Getter for property: ( SpatialMap.BoundingBoxMapEnum NXOpen) BoundingBoxMap
         Returns the bounding box map   
            
         
        """
        pass
    @BoundingBoxMap.setter
    def BoundingBoxMap(self, boundBoxMap: SpatialMap.BoundingBoxMapEnum):
        """
        Setter for property: ( SpatialMap.BoundingBoxMapEnum NXOpen) BoundingBoxMap
         Returns the bounding box map   
            
         
        """
        pass
    @property
    def ConstUObjects(self) -> PathObjectsList:
        """
        Getter for property: ( PathObjectsList NXOpen) ConstUObjects
         Returns the list of  NXOpen::Fields::PathObjects  objects that define sections of constant u   
            
         
        """
        pass
    @property
    def ConstVObjects(self) -> PathObjectsList:
        """
        Getter for property: ( PathObjectsList NXOpen) ConstVObjects
         Returns the list of  NXOpen::Fields::PathObjects  objects that define sections of constant v   
            
         
        """
        pass
    @property
    def CoordSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) CoordSystem
         Returns the csys   
            
         
        """
        pass
    @CoordSystem.setter
    def CoordSystem(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) CoordSystem
         Returns the csys   
            
         
        """
        pass
    @property
    def EvaluationTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EvaluationTolerance
         Returns the evaluation tolerance   
            
         
        """
        pass
    @property
    def FaceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FaceTolerance
         Returns the face tolerance for 3D degenerate surface maps   
            
         
        """
        pass
    @property
    def FitSurfaceCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) FitSurfaceCoordinateSystem
         Returns the fit surface orientation coordinate system   
            
         
        """
        pass
    @FitSurfaceCoordinateSystem.setter
    def FitSurfaceCoordinateSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) FitSurfaceCoordinateSystem
         Returns the fit surface orientation coordinate system   
            
         
        """
        pass
    @property
    def FitSurfaceDirectionOption(self) -> SpatialMapBuilder.FitSurfaceDirectionType:
        """
        Getter for property: ( SpatialMapBuilder.FitSurfaceDirectionType NXOpen) FitSurfaceDirectionOption
         Returns the direction option   
            
         
        """
        pass
    @FitSurfaceDirectionOption.setter
    def FitSurfaceDirectionOption(self, directionOption: SpatialMapBuilder.FitSurfaceDirectionType):
        """
        Setter for property: ( SpatialMapBuilder.FitSurfaceDirectionType NXOpen) FitSurfaceDirectionOption
         Returns the direction option   
            
         
        """
        pass
    @property
    def FitSurfaceUDegree(self) -> int:
        """
        Getter for property: (int) FitSurfaceUDegree
         Returns the u degree   
            
         
        """
        pass
    @FitSurfaceUDegree.setter
    def FitSurfaceUDegree(self, uDegree: int):
        """
        Setter for property: (int) FitSurfaceUDegree
         Returns the u degree   
            
         
        """
        pass
    @property
    def FitSurfaceUPatches(self) -> int:
        """
        Getter for property: (int) FitSurfaceUPatches
         Returns the u patches   
            
         
        """
        pass
    @FitSurfaceUPatches.setter
    def FitSurfaceUPatches(self, uPatches: int):
        """
        Setter for property: (int) FitSurfaceUPatches
         Returns the u patches   
            
         
        """
        pass
    @property
    def FitSurfaceVDegree(self) -> int:
        """
        Getter for property: (int) FitSurfaceVDegree
         Returns the v degree   
            
         
        """
        pass
    @FitSurfaceVDegree.setter
    def FitSurfaceVDegree(self, vDegree: int):
        """
        Setter for property: (int) FitSurfaceVDegree
         Returns the v degree   
            
         
        """
        pass
    @property
    def FitSurfaceVPatches(self) -> int:
        """
        Getter for property: (int) FitSurfaceVPatches
         Returns the v patches   
            
         
        """
        pass
    @FitSurfaceVPatches.setter
    def FitSurfaceVPatches(self, vPatches: int):
        """
        Setter for property: (int) FitSurfaceVPatches
         Returns the v patches   
            
         
        """
        pass
    @property
    def FitSurfaceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FitSurfaceVector
         Returns the vector specifies the projection direction  
            
         
        """
        pass
    @FitSurfaceVector.setter
    def FitSurfaceVector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) FitSurfaceVector
         Returns the vector specifies the projection direction  
            
         
        """
        pass
    @property
    def LatticePath(self) -> PathObjects:
        """
        Getter for property: ( PathObjects NXOpen) LatticePath
         Returns the lattice path objects   
            
         
        """
        pass
    @property
    def MapSubtype(self) -> SpatialMap.SubtypeEnum:
        """
        Getter for property: ( SpatialMap.SubtypeEnum NXOpen) MapSubtype
         Returns the map subtype   
            
         
        """
        pass
    @MapSubtype.setter
    def MapSubtype(self, mapSubType: SpatialMap.SubtypeEnum):
        """
        Setter for property: ( SpatialMap.SubtypeEnum NXOpen) MapSubtype
         Returns the map subtype   
            
         
        """
        pass
    @property
    def MapSubtypeMapping(self) -> SpatialMap.SubtypeMappingEnum:
        """
        Getter for property: ( SpatialMap.SubtypeMappingEnum NXOpen) MapSubtypeMapping
         Returns the subtype mapping   
            
         
        """
        pass
    @MapSubtypeMapping.setter
    def MapSubtypeMapping(self, mapSubTypeMapping: SpatialMap.SubtypeMappingEnum):
        """
        Setter for property: ( SpatialMap.SubtypeMappingEnum NXOpen) MapSubtypeMapping
         Returns the subtype mapping   
            
         
        """
        pass
    @property
    def MapType(self) -> SpatialMap.TypeEnum:
        """
        Getter for property: ( SpatialMap.TypeEnum NXOpen) MapType
         Returns the map type   
            
         
        """
        pass
    @MapType.setter
    def MapType(self, mapType: SpatialMap.TypeEnum):
        """
        Setter for property: ( SpatialMap.TypeEnum NXOpen) MapType
         Returns the map type   
            
         
        """
        pass
    @property
    def MappingFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MappingFaces
         Returns the faces to be used as mapping objects   
            
         
        """
        pass
    @property
    def OppositeCorner(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) OppositeCorner
         Returns the opposite corner   
            
         
        """
        pass
    @OppositeCorner.setter
    def OppositeCorner(self, oppositeCorner: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) OppositeCorner
         Returns the opposite corner   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Origin
         Returns the origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def ParametricPlaneMap(self) -> SpatialMap.ParametricPlaneMapEnum:
        """
        Getter for property: ( SpatialMap.ParametricPlaneMapEnum NXOpen) ParametricPlaneMap
         Returns the parametric plane map   
            
         
        """
        pass
    @ParametricPlaneMap.setter
    def ParametricPlaneMap(self, parmPlaneMap: SpatialMap.ParametricPlaneMapEnum):
        """
        Setter for property: ( SpatialMap.ParametricPlaneMapEnum NXOpen) ParametricPlaneMap
         Returns the parametric plane map   
            
         
        """
        pass
    def AutoTolerance(self) -> None:
        """
         The method to set the face tolerance to a default value based on the current state of the field 
        """
        pass
    def CreateLatticeMap(self, numOfLatticeColumn: int, numOfColumns: int, indep_var_array: List[FieldVariable], datapoint: List[float]) -> Tuple[SpatialMap, List[float]]:
        """
         Create a lattice spatial map from the input datapoints array.  The number of columns in the datapoints
                    array is specified by numOfColumns, and should include the total of all independent and dependent columns.
                    Note that the number of dependent columns can be zero.  The independent domain must be x, y, z, xy, xz, yz or xyz and
                    the number of columns must be greater than or equal to the count of the independent variables.
                    
                    The number of rows of data in the datapoints array is calculated by dividing the number of data points by the number of columns.
                    
                    If number of lattice columns is 1, then a parametric line based map will be created.
                    
                    Otherwise the lattice will be a M x N u-v grid, where M is the number of lattice columns and N is calculated based 
                    on the number of rows in the data points array divded by the number of lattice columns 
         Returns A tuple consisting of (latticeMap, parameterizedDatapoints). 
         - latticeMap is:  SpatialMap NXOpen.
         - parameterizedDatapoints is: List[float].

        """
        pass
    def GetBoundingBox(self) -> List[float]:
        """
         The get bounding box
         Returns boundingbox (List[float]): .
        """
        pass
    def ResetMap(self, spatialMap: SpatialMap) -> None:
        """
         Used to reset map on builder
        """
        pass
    def SetBoundingBox(self, boundingbox: List[float]) -> None:
        """
         The set bounding box
        """
        pass
    def SetFitSurfaceOrientation(self, origin: NXOpen.Point3d, mtx: NXOpen.Matrix3x3) -> None:
        """
         The Orientation option definition 
        """
        pass
import NXOpen
class SpatialMap(NXOpen.NXObject): 
    """  Represents the Field Domain Map 
    A Spatial Map provides a mapping from a field's independent domain into a new domain space.
    This Particular map type is designed to map into cartesian, cylindrical, spherical or parametric
    space, allowing the field to be used where these independent domains are required.
    """
    class BoundingBoxMapEnum(Enum):
        """
        Members Include: 
         |OppositeCorner| 
         |Objects| 

        """
        OppositeCorner: int
        Objects: int
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.BoundingBoxMapEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParametricPlaneMapEnum(Enum):
        """
        Members Include: 
         |IsoSections| 
         |IsoLines| 
         |ImportedIsoLines| 

        """
        IsoSections: int
        IsoLines: int
        ImportedIsoLines: int
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.ParametricPlaneMapEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubtypeEnum(Enum):
        """
        Members Include: 
         |NotSet|  No subtype 
         |Surface|  3D degenerate to existing surface 
         |FitSurface|  3D degenerate to fit surface 

        """
        NotSet: int
        Surface: int
        FitSurface: int
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.SubtypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubtypeMappingEnum(Enum):
        """
        Members Include: 
         |Faces|  Map 3D degenerate data to faces 
         |IsoSections|  Map 3D degenerate data using parametric plane using U curves 
         |IsoLines|  Map 3D degenerate data using parametric plane using UV curves 

        """
        Faces: int
        IsoSections: int
        IsoLines: int
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.SubtypeMappingEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeEnum(Enum):
        """
        Members Include: 
         |NotSet|  No Map 
         |Global|  Map to global csys - defaults to cartesian 
         |Cartesian|  Map to cartesian csys 
         |Cylindrical|  Map to cylindrical csys 
         |Spherical|  Map to spherical csys 
         |ParametricSpace|  Map to parametric space - see NXOpen.Fields.SpatialMap.BoundingBoxMapEnum 
         |ParametricPlane|  Map to parametric plane - see NXOpen.Fields.SpatialMap.ParametricPlaneMapEnum 
         |ParametricLine|  Map to parametric line 
         |ImportedParametricLine|  map to imported parametric line 

        """
        NotSet: int
        Global: int
        Cartesian: int
        Cylindrical: int
        Spherical: int
        ParametricSpace: int
        ParametricPlane: int
        ParametricLine: int
        ImportedParametricLine: int
        @staticmethod
        def ValueOf(value: int) -> SpatialMap.TypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
import NXOpen.GeometricUtilities
class TimeSeriesProfileBuilder(NXOpen.TaggedObject): 
    """ 
            Represents a builder class for creating and editing an NXOpen.Fields.Field.
        
    """
    class InterpolationEnum(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Akima|  Akima 
         |Akima72|  Akima72 
         |Cubic|  Cubic 

        """
        Linear: int
        Akima: int
        Akima72: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> TimeSeriesProfileBuilder.InterpolationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ChannelHasMeasureUnknown(self) -> bool:
        """
        Getter for property: (bool) ChannelHasMeasureUnknown
         Returns   
                     whether or not the profile has unknown measure 
                     
          
          
           
         
        """
        pass
    @ChannelHasMeasureUnknown.setter
    def ChannelHasMeasureUnknown(self, channelHasUnknownType: bool):
        """
        Setter for property: (bool) ChannelHasMeasureUnknown
         Returns   
                     whether or not the profile has unknown measure 
                     
          
          
           
         
        """
        pass
    @property
    def ChannelName(self) -> str:
        """
        Getter for property: (str) ChannelName
         Returns   
                    the channel name
                     
          
          
           
         
        """
        pass
    @ChannelName.setter
    def ChannelName(self, channelName: str):
        """
        Setter for property: (str) ChannelName
         Returns   
                    the channel name
                     
          
          
           
         
        """
        pass
    @property
    def ExternalFile(self) -> str:
        """
        Getter for property: (str) ExternalFile
         Returns   
                    the external file.  
          
                     
           
         
        """
        pass
    @ExternalFile.setter
    def ExternalFile(self, fileName: str):
        """
        Setter for property: (str) ExternalFile
         Returns   
                    the external file.  
          
                     
           
         
        """
        pass
    @property
    def Interpolation(self) -> TimeSeriesProfileBuilder.InterpolationEnum:
        """
        Getter for property: ( TimeSeriesProfileBuilder.InterpolationEnum NXOpen) Interpolation
         Returns   
                    the interpolation 
                     
          
          
           
         
        """
        pass
    @Interpolation.setter
    def Interpolation(self, interpolation: TimeSeriesProfileBuilder.InterpolationEnum):
        """
        Setter for property: ( TimeSeriesProfileBuilder.InterpolationEnum NXOpen) Interpolation
         Returns   
                    the interpolation 
                     
          
          
           
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns   
                    the offset on the x axis.  
          
                     
           
         
        """
        pass
    @property
    def ScaleFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ScaleFactor
         Returns   
                    the scale factor
                     
          
          
           
         
        """
        pass
    @property
    def TimeDelta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TimeDelta
         Returns   
                    the time delta
                     
          
          
           
         
        """
        pass
    @property
    def UserDefinedUnitType(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) UserDefinedUnitType
         Returns   
                    the user defined unit 
                     
          
          
           
         
        """
        pass
    @UserDefinedUnitType.setter
    def UserDefinedUnitType(self, unitType: NXOpen.Unit):
        """
        Setter for property: ( NXOpen.Unit) UserDefinedUnitType
         Returns   
                    the user defined unit 
                     
          
          
           
         
        """
        pass
    def SetMeasureFixed(self, isMeasureFixed: bool) -> None:
        """
         
                        If the measure is marked as fixed and is changed, the validation at commit will detect an error and fail.
                    
                    
                        It is recommended to call this method when editing a profile that is referenced by another object,
                        which depends on specific measures.
                    
        """
        pass
import NXOpen
class VectorFieldWrapper(NXOpen.NXObject): 
    """ This class defines a vector value that is internally 
        backed up by a (optionally scaled) field or three expressions. """
    def GetExpressionByIndex(self, index: int) -> NXOpen.Expression:
        """
         Returns the indicated implementation if the wrapper is backed up by expressions; 
                    NULL otherwise 
         Returns expression ( NXOpen.Expression):  existing expression or NULL .
        """
        pass
    def GetField(self) -> Field:
        """
         Returns the implementation if the wrapper is backed up by a field; 
                    NULL otherwise 
         Returns field ( Field NXOpen):  existing field or NULL .
        """
        pass
    def SetExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Sets the implementation of the wrapper to the specified expressions 
        """
        pass
    def SetField(self, field: Field, scale_factors: List[float]) -> None:
        """
         Sets the implementation of the wrapper to the specified field 
        """
        pass
